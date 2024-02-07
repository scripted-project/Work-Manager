import fs from 'node:fs';
async function load(container, name) {
    const path = `./widgets/${name}/entry.html`;
    if (fs.existsSync(path)) {
        document.getElementById(container).innerHTML = fs.readFile(path);
    }
}

module.exports = {
    load
}