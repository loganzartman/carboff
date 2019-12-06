let data;
let totalDuration;
chrome.storage.local.get(["data", "totalDuration"], (result) => {
    data = result.data;
    totalDuration = result.totalDuration || 0;
});

const tabsWithDebug = new Set();

chrome.tabs.onUpdated.addListener((tabId, changeInfo) => {
    if (!tabId)
        return;
    if (tabId === chrome.tabs.TAB_ID_NONE)
        return;
    
    // track time on this page
    chrome.tabs.query({active: true}, (tabs) => {
        if (tabs.length > 1)
            throw new Error("More than one active tab!");
        
        // check new page loaded
        if (changeInfo.url) {
            chrome.storage.local.set({pageStartTime: Date.now()}, () => {});
        }
    });

    // attach debugger to tab if none present
    if (!tabsWithDebug.has(tabId)) {
        chrome.debugger.attach({tabId}, "1.0", () => {
            if (!chrome.runtime.lastError) {
                tabsWithDebug.add(tabId);
                console.log(`successfully attached to ${tabId}`);

                chrome.debugger.sendCommand({tabId}, "Network.enable");
            }
        });
    }
});

/*
chrome.webRequest.onBeforeRequest.addListener((details) => {
    // TODO: Monitor sent data
});
*/

chrome.tabs.onRemoved.addListener((tabId) => {
    if (tabsWithDebug.has(tabId)) {
        tabsWithDebug.delete(tabId);
        console.log(`removed debugger on ${tabId}`);
    }
});

chrome.debugger.onEvent.addListener((source, method, params) => {
    if (method === "Network.dataReceived") {
        data += params.encodedDataLength;
    }
});

// Write the data to chrome.storage once a second
setInterval(() => {
    chrome.storage.local.set({data, totalDuration}, () => {});
}, 1000);
