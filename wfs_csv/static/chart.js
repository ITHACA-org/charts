function update_link()
    {
    var url = '/table?lyrname={{ lyrname }}';
    url = url + '&category=' + document.f.category.value;
    url = url + '&quantity=' + document.f.quantity.value;
    document.getElementById('link').href = url;
    return;
    }

//create area for chart
var createChartArea =  function() {
    var chartArea = document.getElementById("area_grafico");
    chartArea.style= "display:table;";
};
createChartArea();

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function(){
    if (xhttp.readyState == 4 && xhttp.status == 200){
        var csv_link = xhttp.responseURL;

        replaceChart = function(){
        }
        barChart = function(){
        replaceChart();
        console.log(csv_link)
        getCsv(csv_link,0);
        };


        }
}