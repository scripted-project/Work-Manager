function load(containerID, name, settingsString, x, y) {
    try {
        const iframe = document.createElement('iframe');
        var src = `${baseUrl}/widgets/${name}/entry.html${settingsString}`;
        iframe.src = src;
        document.getElementById(containerID).appendChild(iframe);
    } catch {}
}

export { load };