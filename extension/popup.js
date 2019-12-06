const display = document.getElementById("display");

setInterval(() => {
    chrome.storage.sync.get(["data"], (result) => {
        display.innerText = result.data;
    });
}, 1000);