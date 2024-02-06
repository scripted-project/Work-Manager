import * as fs from 'node:fs';
class WidgetActivationArgs {
    constructor() {}
}

function load(name) {
    if (!fs.existsSync(`/widgets/${name}`)) {
        return null;
    }
    else {
        let out = import(`./widgets/${}`);
    }
}