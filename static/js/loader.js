function load(container, name) {
    try {
        const iframe = document.createElement('iframe');
        iframe.src = `${baseUrl}/widgets/${name}/entry.html`;
        document.getElementById(container).appendChild(iframe);
    } catch {}
}

export { load };