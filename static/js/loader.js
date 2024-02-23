import * as api from './api.js';

let n = 0;

function load(containerID, name, settingsString, x, y, height, width) {
    try {
        const iframe = document.createElement('iframe');
        var src = `${baseURL}/widgets/${name}/entry.html${settingsString}`;
        iframe.src = src;
        iframe.style = `
        grid-row-start: ${x};
        grid-column-start: ${y};
        grid-column: 1 / ${width};
        grid-row: 1 / ${height};
        `
        document.getElementById(containerID).appendChild(iframe);
    } catch {}
}

function setUpDashboard(dashboardID) {
    // comments were for video
    const dashboardData = api.get(`/api/dashboards/${dashboardID}`); // get dashboard data
    if (dashboardData == null) {return;} // prove non-null

    const container = document.getElementById('container'); // get container
    if (container == null) {return;} // prove non-null

    dashboardData.widgets.forEach(element => {
        const div = document.createElement('div');
        container.appendChild(div);
        div.id = n;
        load(n, element.id, '', element.x, element.y, element.height, element.width);
        // load element into container
        n += 1;
    });
}

function addWidget(widgetID, dashboardID, x, y, height, width) {
    let currentDash = api.get(`/api/dashboards/${dashboardID}`);
    currentDash.dashboards.push({
        id: widgetID,
        x: x,
        y: y,
        width: width,
        height: height,
        settings: {}
    });
    newDIV("container", n);
    load(n, widgetID, '', x, y, height, width);
    n += 1;
}
function newDIV(container, i) {
    const div = document.createElement('div');
    div.id = i;
    container.appendChild(div);
}
function widgetOverlay() {
    const overlay = document.getElementById("overlay");
    overlay.style.display = 'flex';
    overlay.style.visibility = 'visible';
    
    data = api.get("/api/widgets-lst");
    data.data.forEach(element => {
        overlay.innerHTML += `<button onclick="addWidget(">${element.name}</button>`;
    });
}

export { load, setUpDashboard, addWidget, widgetOverlay, newDIV };