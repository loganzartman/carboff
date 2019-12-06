chrome.runtime.onInstalled.addListener(function() {
    chrome.storage.sync.set({color: '#3aa757'}, function() {
    });
});

chrome.webRequest.onCompleted.addListener(function(details) {
    console.log(details);
},
{urls: ["<all_urls>"]});
