function get_chart(){

        // extract summary type
        var aggregates = document.f.aggregates;
        var agg = '';
        var i;
        for (i = 0; i < aggregates.length; i++){
            if (aggregates[i].checked){
                agg = agg + aggregates[i].value;
            }
        }

        // extract chart type
        var chartType = document.f.chart_type.value;

        // extract link
        var csv_link = document.getElementById('link').href;

        // extract category and quantity fieldnames
        var string = csv_link.split("&");
        var quantity = string[2].split("=")[1];
        var category = string[1].split("=")[1];

        //create area for chart
        var createChartArea =  function() {
            var chartArea = document.getElementById("chart_area");
            chartArea.style= "display:table; float:left; height:100%; width:70%";
        };

        // update chart
        var replaceChart = function(){
            doc_chart = document.getElementById('chart_area');
            if(doc_chart.childElementCount >= 1){
                 doc_chart.removeChild(doc_chart.childNodes[1]);
                 createChartArea();
                 };
        };

        replaceChart();
        getCsv(csv_link, category, quantity, agg, chartType);

};