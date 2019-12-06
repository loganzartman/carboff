chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
    });
});

chrome.tabs.onCreated.addListener((tab) => {
    if (!tab.id)
        return;
    if (tab.id === chrome.tabs.TAB_ID_NONE)
        return;
    console.log(`created tab ${tab.id}`);
});

chrome.tabs.onRemoved.addListener((tabId) => {
    console.log(`removed tab ${tabId}`);
});
