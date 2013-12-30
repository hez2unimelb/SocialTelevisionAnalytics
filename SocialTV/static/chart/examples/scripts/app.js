(function(window, undefined) {

  "use strict";

  var d3 = window.d3;
  var DataSrc = window.DataSrc;
  var BarChart = window.BarChart;
  var Chord = window.Chord;
  // From http://mkweb.bcgsc.ca/circos/guide/tables/
  var matrix = [
    [11975,  5871, 8916, 2868],
    [ 1951, 10048, 2060, 6171],
    [ 8010, 16145, 8090, 8045],
    [ 1013,   990,  940, 6907]
  ];

  var dataSrc = new DataSrc();
var barchart = d3.select("body")
  .append("svg")
  .attr("height", 300)
  .attr("width", 800)
  .chart("BarChart");

barchart.draw([
  { name : "January", value : 29 },
  { name : "February", value : 32 },
  { name : "March", value : 48 },
  { name : "April", value : 49 },
  { name : "May", value : 58 },
  { name : "June", value : 68 },
  { name : "July", value : 74 },
  { name : "August", value : 73 },
  { name : "September", value : 65 },
  { name : "October", value : 54 },
  { name : "November", value : 45 },
  { name : "December", value : 35 }
]);
  

 

}(this));
