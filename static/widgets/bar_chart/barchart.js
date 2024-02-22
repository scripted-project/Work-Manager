const form = document.getElementById('form');

function start() {
  const firstdata = document.getElementById("first-data");
  const seconddata = document.getElementById("second-data");

  var xValues = [firstdata.innerText];
  var yValues = [seconddata.innerText];
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
