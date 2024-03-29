const display_gco2 = document.getElementById("display_gco2");
const display_wh = document.getElementById("display_wh");
const display_debug = document.getElementById("display_debug");
const display_wave = document.getElementById("display_wave");
const display_time = document.getElementById("display_time");
const wave_overlay_text = document.getElementById("wave_overlay_text");

document.getElementById("clear_btn").addEventListener("click", (event) => {
    chrome.runtime.sendMessage({clear: true}, () => {
        alert("Reset stats!");
    })
}, false);

document.getElementById("tree_btn").addEventListener("click", (event) => {
    var newWindow = window.open("https://onetreeplanted.org/", '_blank');
    newWindow.focus();
}, false);

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

const updateDisplay = () => {
    chrome.storage.local.get(["data", "totalData", "totalDuration", "pageStartTime"], async (result) => {
        const response = await fetch("http://localhost:5000/impact/action", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                duration: result.totalDuration / (60 * 1000),
                data: result.data,
                location: "us",
                device_type: "laptop",
                network_type: "wireless"
            })
        });

        let jsonResponse = await response.json();
        display_gco2.innerText = jsonResponse.gCO2_total.toFixed(2);
        display_wh.innerText = (jsonResponse.kWh_total * 1000).toFixed(2);
        wave_overlay_text.innerText = jsonResponse.ocean_rise_am.toFixed(2);

        const seconds = (result.totalDuration / 1000) % 60;
        const minutes = (result.totalDuration / (1000 * 60)) % 60;
        const hours = (result.totalDuration / (1000 * 60 * 60));
        display_time.innerText = `${(~~hours).toString().padStart(2, "0")}:${(~~minutes).toString().padStart(2, "0")}:${(~~seconds).toString().padStart(2, "0")}`;
    });
}

setInterval(() => updateDisplay(), 200);
updateDisplay();

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
