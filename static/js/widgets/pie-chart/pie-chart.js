import load from '../../loader.js';

function entryPoint() {
    new Chart(document.getElementById('pie-chart'), {
    type: 'pie',
    data: {
        labels: ["HTML", "CSS", "JavaScript", "PHP", "MySql"],
        datasets: [{
        backgroundColor: ["#e63946", "#254BDD",
            "#ffbe0b", "#1d3557", "#326998"
        ],
        data: [418, 263, 434, 586, 332]
        }]
    },
    options: {
        title: {
        display: true,
        text: 'Pie Chart for admin panel'
        },
        responsive: true
    }
    });

}
