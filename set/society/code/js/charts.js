/**
 * Created by luoxiaotong on 2016/1/20.
 */
//$(function(){
//    //折线图数据渲染
//    /*var dataLine =
//    [
//           ['2015.12.31', '2016.01.06', '2016.01.11', '2016.01.15'],
//           [
//               {
//                   name: '悲伤',
//                   data: [48, 78, 88, 101]
//               },{
//                   name: '愉快',
//                   data: [99, 150, 500, 999]
//               },{
//                   name: '愤怒',
//                   data: [120, 150, 155, 148]
//               },{
//                   name: '喜欢',
//                   data: [160, 180, 300, 312]
//               }
//           ]
//       ];
//
//    var dataPie = [
//        [
//           ['搜狐',  12.0],
//           ['新浪',  20.00],
//           ['网易',  30.00],
//           ['腾讯',  10.00],
//           ['凤凰',  28.00]
//       ],
//
//       [
//           ['悲伤',  12.0],
//           ['喜欢',  19.0],
//           ['愤怒',  20.0],
//           ['怨恨',  13.0],
//           ['愉快',  11.0],
//           ['激动',  5.0],
//           ['未知',  12.0],
//           ['爱你',  8.0]
//       ]
//    ];*/
//
//    lineChart(dataLine, 'title', '#lineChart');
//    pieChart(dataPie[0], '各大网站参与话题人数占比', '#pieJoin');
//    pieChart(dataPie[1], '主要情绪占比(%)', '#pieEmotion');
//})
//折线图
function lineChart(data, title, location){
    $(location).highcharts({
        chart: {
            backgroundColor: 'rgba(0,0,0,0)'
        },
        title: {
            text: title,
            x: -20, //center
            style: {
                fontFamily: "黑体",
                color: '#7d7d7d',
                fontSize: '0'
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
                text: '参与人数(人)'
//                align: 'high'
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
            plotShadow: false,
            backgroundColor: 'rgba(0,0,0,0)'
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
            pointFormat: '{series.name}:<b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                size: 260,
                innerSize: 220,
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
                    distance: 20,
                    color: '#666666',
                    connectorColor: '#3285c4',
                    format: '<b>{point.name}</b> {point.percentage:.1f} %'
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

