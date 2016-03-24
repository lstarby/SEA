/**
 * Created by luoxiaotong on 2016/1/20.
 */

//折线图
function lineChart(data, title, location){
    $(location).highcharts({
        title: {
            text: title,
            x: -20, //center
            style: {
                fontFamily: "黑体",
                color: '#7d7d7d',
                fontSize: '0',
            }
        },
        subtitle: {
            text: '',
            x: -20
        },
        xAxis: {
            categories: data[0]
        },
        yAxis: {
            title: {
                text: '参与人数(人)',
                align: 'high'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        credits: {
            enabled:false
        },
        tooltip: {
            valueSuffix: '°C'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: data[1]
    });
}

function pieChart(data, title, location){

    $(location).highcharts({
        chart: {
            type: 'pie',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },

        title: {
            text: title,
            style: {
                fontSize: 0
            }
        },
        credits: {
            enabled:false
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                size: 210,
                innerSize: '130',
                colors: [
                    '#15ba63',
                    '#fc6421',
                    '#e9483e',
                    '#3285c4',
                    '#fcd521'
                ],
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    color: '#000000',
                    connectorColor: '#000000',
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
            }
        },
        legend: {
            layout: 'vertical',
            backgroundColor: '#FFFFFF',
            floating: true,
            align: 'left',
            verticalAlign: 'top',
            x: 90,
            y: 45,
            labelFormatter: function () {
                return this.name + '(' + this.percentage+'%)';
            }
        },
        series: [{
            type: 'pie',
            name: '',
            data: data
        }]
    });


}
function emotionPie(data, title, location){
    var Color = [
        '#15ba63',
        '#fc6421',
        '#e9483e',
        '#3285c4',
        '#fcd521',
        '#F205F5',
        '#03FAF2',
        '#24FC3B',
        '#8940E8'
    ];

    $(location).highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: title
        },
        colors: Color,
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        credits: {
            enabled:false
        },
        plotOptions: {
            pie: {
                size: 180,
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false,
                    color: '#000000',
                    connectorColor: '#000000',
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
            }
        },
        series: [{
            type: 'pie',
            name: '',
            data: data
        }]
    });
    //颜色标注
    for(var i = 0, length = data.length; i < length; i ++){
        data[i].push(Color[i]);
        var colorBar = new ColorBar(data[i]);
        var txt = render($('#colorBar').html(), colorBar);
        $('#color').append(txt);
    }

}
