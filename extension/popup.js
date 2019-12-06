const display = document.getElementById("display");

setInterval(async () => {
    chrome.storage.local.get(["data"], async (result) => {
        const response = await fetch("http://localhost:5000/impact/action", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                duration: 0,
                data: result.data,
                location: "us",
                device_type: "laptop",
                network_type: "wireless"
            })
        });

        display.innerText = JSON.stringify(await response.json());
    });
}, 1000);
