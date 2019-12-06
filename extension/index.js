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
            }
        });
    }
});

chrome.tabs.onRemoved.addListener((tabId) => {
    if (tabsWithDebug.has(tabId)) {
        tabsWithDebug.delete(tabId);
        console.log(`removed debugger on ${tabId}`);
    }
});
