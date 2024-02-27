import * as api from './api.js';
var n = 0;

var searchParams = new URLSearchParams();
let dashboardID = searchParams;

// Raw load into a container
function load(widgetID, containerID, settingsString = "") {
    const iframe = document.createElement('div');
    iframe.src = `/widgets/${widgetID}/entry.html?${settingsString}`;
    document.getElementById(containerID).innerHTML = iframe;
}
// Creates and returns a new divider/container
function newDiv(id, innerHTML = "", style = "") {
    const div = document.createElement('div');
    div.id = id;
    div.innerHTML = innerHTML;
    div.style = style;
    return div;
}
// Adds a widget to the screen and to a dashboard
// FIXME: Not thread safe
async function addWidget(widgetID) {
    var dash = await api.get(`/api/dashboards/${dashboardID}`);
    dash.widgets.push({
        id: widgetID,
        x: 0,
        y: 0,
        height: 1,
        width: 1,
        settings: {}
    });
    api.post(`/api/dashboards/${dashboardID}`, dash);
    newDiv(n);
    load(widgetID, n);

    n += 1;
}