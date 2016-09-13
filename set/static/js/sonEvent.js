/**
 * Created by luoxiaotong on 2016/1/21.
 */

$(document).ready(function () {

    var searchItems = getSearchItem(),
        eventId = searchItems.eventId;
    /*var id = window.location.href;
    id = id.split('?')[1];*/

    var url1 = PATH + 'getBannerAndCharts?newsId=' + eventId,
        url2 = PATH + 'getKeywordAndComment?newsId=' + eventId;
    getAjaxData(url1, callBack1);
    getAjaxData(url2, callBack2);
    navDots.init();

});
function scrollToKeyWords(data) {
    var topDic = 0,
        winHeight = $(window).height();
    var keywordAnima = setInterval(function() {
        topDic = $(window).scrollTop();
        if(topDic > 2*winHeight/3) {
            clearInterval(keywordAnima);
            renderKeyWords(data);
        }
    }, 100)

}
function callBack2(data){
    var keyWords = data[0],
        comments = data[1],
        keyWordArr = [];
    renderComments(comments);

    for(var i = 0, len = keyWords.length; i < len; i ++) {
        var key = {
            source: keyWords[i][0],
            target: '关键词',
            size: keyWords[i][1]
        };

        keyWordArr.push(key);
    }
    scrollToKeyWords(keyWordArr);

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

    lineChart(lineData, '各大网站参与话题人数占比', '#lineChart');
    pieChart(dataPieOne, '', '#pieJoin');
    pieChart(dataPieSec, '', '#pieEmotion');
    var searchItems = getSearchItem(),
        navId = searchItems.navId;

    renderBannerNews(dataBanner, navId);
}

function renderBannerNews(data, navId){
    for(var i = 0, length = data.length; i < length; i ++){
        var bannerNews = new BannerNews(data[i], navId);
        var txt = render($('#bannerNews').html(), bannerNews);
        $('#banner').append(txt);
    }
}

$(window).resize(function() {
    navDots.winHeight = $(window).height();
});