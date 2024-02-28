import * as api from './api.js';
var n = 0;

var searchParams = new URLSearchParams(location.href);
let dashboardID = searchParams.get("id");

// Raw load into a container
function load(widgetID, containerID, settingsString = "") {
    try {
        const iframe = document.createElement('iframe');
        iframe.src = `/widgets/${widgetID}/entry.html?${settingsString}`;
        document.getElementById(containerID).appendChild(iframe);
        return iframe;
    } catch (err) {
        api.post('/api/report', {location: "load_func@loader.js", error: err});
        throw new Error;
    }
}
// instead of a complete raw load, gets the iframe for more control
function get(widgetID, settingsString = "") {
    try {
        const iframe = document.createElement('iframe');
        iframe.src = `/widgets/${widgetID}/entry.html?${settingsString}`;
        return iframe;
    } catch (err) {
        api.post('/api/report', {location: "load_func@loader.js", error: err});
        throw new Error;
    }
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

// Sets up the page for a dashboard
// FIXME: also not thread safe
async function setUpDashboard(id) {
    var dash = await api.get(`/api/dashboards/${id}`);
    let widgets;
    let _id;
    try {
        widgets = dash.widgets;
        _id = dash.id;

        if (_id != id) {
            throw -1;
        }
    } catch (ex) {return;}

    widgets.forEach(element => {
        try {
            let __id = element.id;
            let x = element.x;
            let y = element.y;
            let h = element.height;
            let w = element.width;
            let settings = element.settings;

            newDiv(n);
            load(__id, n);

            n += 1;
        } catch (ex) {}
    });
}

function openOverlay() {
    const overlay = document.getElementById("overlay");
    overlay.style.display = 'flex';
    overlay.style.visibility = 'visible';
}
function closeOverlay() {
    const overlay = document.getElementById('overlay');
    overlay.style.display = 'none';
    overlay.style.visibility = 'hidden';
}

export { 
    load, 
    setUpDashboard, 
    addWidget, 
    newDiv, 
    get, 
    openOverlay, 
    closeOverlay 
}