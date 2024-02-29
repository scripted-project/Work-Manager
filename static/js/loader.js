import('/static/js/api.js');

var n = 0;

var searchParams = new URLSearchParams(location.href);
let dashboardID = parseInt(searchParams.get("id"));

function setID(id) {
    dashboardID = id;
}

// Raw load into a container
function load(widgetID, containerID, settingsString = "") {
    try {
        const iframe = document.createElement('iframe');
        iframe.src = `/static/widgets/${widgetID}/entry.html?${settingsString}`;
        document.getElementById(containerID).appendChild(iframe);
        return iframe;
    } catch (err) {
        apipost('/api/report', {
            location: "load_func@loader.js", 
            error: `Error: ${err}, Container: ${document.getElementById(containerID)}`
        });
        const p = document.createElement('p');
        p.innerText = err;
        document.getElementById(containerID).appendChild(p);
        throw new Error(err);
    }
}
// instead of a complete raw load, gets the iframe for more control
function get(widgetID, settingsString = "") {
    try {
        const iframe = document.createElement('iframe');
        iframe.src = `/static/widgets/${widgetID}/entry.html?${settingsString}`;
        return iframe;
    } catch (err) {
        apipost('/api/report', err);
        throw new Error(err);
    }
}
// Creates and returns a new divider/container
function newDiv(id, innerHTML = "", style = "") {
    const div = document.createElement('div');
    div.id = id;
    div.innerHTML = innerHTML;
    div.style = style;
    document.body.appendChild(div);
    return div;
}
// Adds a widget to the screen and to a dashboard
async function addWidget(widgetID) {
    try {
        let dash = await apiget(`/api/dashboards/${dashboardID}`);
        dash.widgets.push({
            id: widgetID,
            x: 0,
            y: 0,
            height: 1,
            width: 1,
            settings: {}
        });
        apipost(`/api/dashboards/${dashboardID}`, dash);
        const div = newDiv(n);
        load(widgetID, div.id);

        n += 1;
    } catch (exc) {
        apipost('/api/report', {
            location: "addWidget_func@loader.js",
            error: {ex: exc, n: n}
        });
    }
}

// Sets up the page for a dashboard
// FIXME: also not thread safe
async function setUpDashboard() {
    let id = dashboardID;
    console.log("id: ", id);
    let _dash = await apiget(`/api/dashboards/${id}`);
    console.log("_dash: ", _dash);
    let widgets = _dash.data.widgets;
    console.log("widgets: ", widgets);

    if (Array.isArray(widgets)) {
        widgets.forEach(element => {
            try {
                let __id = element.id;

                const div = newDiv(n);
                load(__id, div.id);

                n = n + 1;
            } catch (ex) { apipost('/api/report', {
                error: {ex: ex, n: n, divid: div.id},
                location: "setUpDashboard_func@loader.js"
            })}
        });
    } else {
        throw new Error(`${typeof _dash.data.widgets} is not array (dash is of type ${typeof dash})`)
        
    }
    
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