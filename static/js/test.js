import { get, load } from './loader.js'

document.getElementById('text').innerText = "Connected";

n = 0;
try {
    const iframe = get("example_widget", "");
    const p = document.createElement('p');
    p.innerText = "Success"
    document.getElementById('container').innerHTML += iframe;
    document.getElementById('text').innerText += p.innerText;
} catch (err) {
    var p = document.createElement('p');
    p.innerText = err;
    document.getElementById('text').innerText = p.innerText;
}