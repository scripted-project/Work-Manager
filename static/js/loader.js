import fs from 'node:fs';
async function load(container, name) {
    const path = `./widgets/${name}/entry.html`;
    if (fs.existsSync(path)) {
        document.getElementById(container).outerHTML += `<iframe src="./widgets/${name}/entry.html"`
    }
    else {document.getElementById(container).outerHTML = '<h3>not found</h3>'}   
}

module.exports = {
    load
}