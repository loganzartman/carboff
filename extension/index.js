let data = 0;
chrome.storage.sync.get(["data"], (result) => {data = result;})

chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
    });
});

const tabsWithDebug = new Set();

chrome.tabs.onUpdated.addListener((tabId) => {
    if (!tabId)
        return;
    if (tabId === chrome.tabs.TAB_ID_NONE)
        return;

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
    chrome.storage.sync.set({data}, () => {});
}, 1000);
