/**
 * Created by luoxiaotong on 2016/1/21.
 */

$(document).ready(function () {
    var id = window.location.href;
    id = id.split('?')[1];

    var url1 = PATH + 'getBannerAndCharts?newsId=' + id,
        url2 = PATH + 'getKeywordAndComment?newsId=' + id;
    getAjaxData(url1, callBack1);
    getAjaxData(url2, callBack2);

});
function callBack2(data){
    var keyWords = data[0],
        comments = data[1];
    renderComments(comments);
    renderKeyWords(keyWords);
}

function renderComments(data){
    for(var i = 0, length = data.length; i< length; i ++){
        var comment = new Commments(data[i]);
        var txt = render($('#commentLi').html(), comment);
        $('#comment ul').append(txt);
    }
}
function callBack1(data){

    var dataBanner = data[0],
        lineData = data[1],
        dataPieOne = data[2],
        dataPieSec = data[3];
    lineData = [
        ['2015.12.31', '2016.01.06', '2016.01.11', '2016.01.15'],
        [
            {
                name: '悲伤',
                data: [48, 78, 88, 101]
            },{
            name: '愉快',
            data: [99, 150, 500, 999]
        },{
            name: '愤怒',
            data: [120, 150, 155, 148]
        },{
            name: '喜欢',
            data: [160, 180, 300, 312]
        }
        ]
    ];

    //字符串转浮点数
    dataPieOne = arrayFloat(dataPieOne);
    dataPieSec = arrayFloat(dataPieSec);

        //dataPieOne = JSON.parse(data[2]),
        //dataPieSec = JSON.parse(data[3]);
    //字符串转浮点数

    lineChart(lineData, '各大网站参与话题人数占比', '#barChart');

    pieChart(dataPieOne, '', '#pieChart');
    emotionPie(dataPieSec, '', '#pieChart2');

    renderBannerNews(dataBanner);
}

function renderBannerNews(data){
    console.log(data);
    for(var i = 0, length = data.length; i < length; i ++){
        var bannerNews = new BannerNews(data[i]);
        var txt = render($('#bannerNews').html(), bannerNews);
        $('#banner').append(txt);
    }
}