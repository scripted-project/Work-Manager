import fs from 'node:fs';
import * as Flask from 'flask';
function load(container, name) {
    const path = `.js/widgets/${name}/entry.html`;
    if (fs.existsSync(path)) {
        let content = `<iframe src="${path}"></iframe>`;
        document.getElementById(container).innerHTML(content);
        return 200;
    }
    else {document.getElementById(container).outerHTML = '<h3>not found</h3>'; return 404;}
}

module.exports = {
    load
}