const firstdata = document.getElementById("first-data");


var xValues = [firstdata.innerText];
var yValues = [seconddata.innerText];
var barColors = [red, yellow, green, orange, blue];

new Chart("myChart", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  }
});