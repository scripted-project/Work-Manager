import * as api from './api.js';

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

    let n = 0;
    dashboardData["widgets"].forEach(element => {
        const div = document.createElement('div');
        container.appendChild(div);
        div.id = n;
        load(n, element["id"], '', element["x"], element["y"], element["height"], element["width"]);
        // load element into container
        n += 1;
    });
}

export { load, setUpDashboard };