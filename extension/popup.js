const display_gco2 = document.getElementById("display_gco2");
const display_kwh = document.getElementById("display_kwh");
const display_debug = document.getElementById("display_debug");

setInterval(async () => {
    chrome.storage.local.get(["data", "totalData", "totalDuration", "pageStartTime"], async (result) => {
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

        let jsonResponse = await response.json();
        display_gco2.innerText = jsonResponse.gCO2_total.toFixed(2) + " g";
        display_kwh.innerText = jsonResponse.kWh_total.toFixed(2) + " kWh";
        display_debug.innerText = JSON.stringify({
            totalData: result.totalData,
            totalDuration: result.totalDuration,
            pageTime: Date.now() - result.pageStartTime
        });
    });
}, 1000);
