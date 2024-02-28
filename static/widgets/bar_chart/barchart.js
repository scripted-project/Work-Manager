import Chart from 'chart.js';

const form = document.getElementById('form');

function start() {
  const firstdata = document.getElementById("first-data");
  const seconddata = document.getElementById("second-data");

  var xValues = [1, 2, 3, 4, 5];
  var yValues = [2, 3, 4, 5, 6];
  var barColors = [red, yellow, green, orange, blue];

  new Chart("barchart", {
    type: "bar",
    data: {
      labels: xValues,
      datasets: [{
        backgroundColor: barColors,
        data: yValues
      }]
    }
  });  
}
