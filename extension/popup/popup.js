const display_gco2 = document.getElementById("display_gco2");
const display_kwh = document.getElementById("display_kwh");
const display_debug = document.getElementById("display_debug");
const display_wave = document.getElementById("display_wave");

(() => {
    display_wave.width = display_wave.parentElement.offsetWidth;
    display_wave.height = display_wave.parentElement.offsetHeight;
    const ctx = display_wave.getContext("2d");

    const render = () => {
        renderWave(ctx, "#0E2154");
        requestAnimationFrame(render);
    };
    render();
})();

setInterval(async () => {
    chrome.storage.local.get(["data", "totalData", "totalDuration", "pageStartTime"], async (result) => {
        const response = await fetch("http://localhost:5000/impact/action", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                duration: result.totalDuration / 1000,
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

function renderWave(ctx, fillStyle) {
    const nPoints = 100;
    const amplitude = 0.1;
    const frequency = 7;
    const speed = 0.005;
    const octaves = 3;

    ctx.resetTransform();
    ctx.scale(ctx.canvas.width, ctx.canvas.height);
    ctx.fillStyle = "white";
    ctx.fillRect(0,0,1,1);

    ctx.beginPath();
    ctx.moveTo(0,1);

    for (let i = 0; i <= nPoints; i += 1) {
        const x = i / nPoints;
        let displacement = 0;
        for (let o = 0; o < octaves; o++) {
            const randomSpeed = (Math.sin(o * 6581265.2397) * 0.5 + 0.5) * speed;
            displacement += Math.sin(x * frequency * (2 ** o) + Date.now() * randomSpeed) * amplitude * 0.5 ** o;
        }
        ctx.lineTo(x, 0.3 + displacement);
    }

    ctx.lineTo(1,1);
    ctx.fillStyle = fillStyle;
    ctx.fill();
}
