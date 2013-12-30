function draw(data)
{
nv.addGraph(function() {  
  var chart = nv.models.lineChart();

  chart.xAxis // chart sub-models (ie. xAxis, yAxis, etc) when accessed directly, return themselves, not the parent chart, so need to chain separately
      .tickFormat(function(d) { return d3.time.format('%d %b %H')(new Date(parseInt(d))); });

  chart.yAxis
      .axisLabel('Voltage (v)')
      .tickFormat(d3.format('n'));
  chart.margin({top: 50, right: 50, bottom: 50, left: 50});
  d3.select('#chart svg')
      .datum(data)
      .call(chart);

  //TODO: Figure out a good way to do this automatically
  nv.utils.windowResize(chart.update);
  //nv.utils.windowResize(function() { d3.select('#chart1 svg').call(chart) });

  return chart;
});
}
function redraw(data)
{
	draw(processData(limitData(data)));
}
function fullTime(data)
{
	draw(processData(data));
}
function transformDate(date)
{
	dateItems=date.split('/');
	return new Date(dateItems[2],dateItems[0],dateItems[1]);
}
function limitData(data) {
	
	 var start=document.getElementById('from').value;
	
	 var startdate=transformDate(start);
	 var end=document.getElementById('to').value;
	 var enddate=transformDate(end);
	 var data2=[];
	 for (var i=0;i<data.length;i++)
    {
	  var currentDate=new Date(parseInt(data[i].x));
	
		if (startdate<=currentDate&&currentDate<=enddate)
			data2.push(data[i]);
    }
	 return data2;
}