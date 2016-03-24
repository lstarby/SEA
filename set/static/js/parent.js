/**
 * Created by luoxiaotong on 2016/1/20.
 */
$(document).ready(function () {
    var url = window.location.href;
    url = url.split('?')[1];
    getNews(url);
    //callBack();//直接执行callback以测试， 这里删除，上面恢复
});

function getNews(newsid){
    var url = PATH + 'getBannerAndCharts?newsId=' + newsid;
    getAjaxData(url, callBack);
}

function callBack(data){
    //虚拟数据data
    //var dataaa = [
    //    //大事件页面和小事件页面banner非滚动图
    //    [
    //        {
    //            "id": 1,
    //            "title" : '巴萨SN互喂9饼梅西你眼红吗 苏牙1数据接班恩帅巴萨SN互喂9饼梅西你眼红吗 苏牙1数据接班恩帅',
    //            "pic" : '../images/banner/1.jpg',
    //            "website": '搜狐网',
    //            "abstract": '在本赛季中，梅西曾一度重伤两个月之久。巴萨不但没有掉队，而且三线都保持高度竞争力，这很大程度上要源于苏亚雷斯和内马尔之间的默契。在昨天梅西半场离场之后，内马尔和苏亚雷斯又成了巴萨主角。在连续不停球直接传球之后，内少又为苏神送出了一次保姆助攻。《每日体育报》指出，苏亚雷斯和内马尔19轮联赛中互相“喂饼”9次，这一数据冠绝欧洲。',
    //            "dateTime": '2016.01.19',
    //            "author": '是我是我就是我',
    //            "joinNum": '99999'
    //        },
    //        {
    //            "id": 2,
    //            "title" : '巴萨SN互喂9饼梅西你眼红吗 苏牙1数据接班恩帅苏牙1数据接班恩帅苏牙1数据接班恩帅苏牙1数据接班恩帅',
    //            "pic" : '../images/banner/2.jpg',
    //            "website": '网易网',
    //            "abstract": '在本赛季中，梅西曾一度重伤两个月之久。巴萨不但没有掉队，而且三线都保持高度竞争力，这很大程度上要源于苏亚雷斯和内马尔之间的默契。在昨天梅西半场离场之后，内马尔和苏亚雷斯又成了巴萨主角。在连续不停球直接传球之后，内少又为苏神送出了一次保姆助攻。《每日体育报》指出，苏亚雷斯和内马尔19轮联赛中互相“喂饼”9次，这一数据冠绝欧洲。',
    //            "dateTime": '2016.01.19',
    //            "author": '是我是我就是我',
    //            "joinNum": '99999'
    //        },
    //        {
    //            "id": 3,
    //            "title" : '巴萨SN互喂9饼梅西你眼红吗 苏牙1数据接班恩帅',
    //            "pic" : '../images/banner/3.jpg',
    //            "website": '新浪网',
    //            "abstract": '在本赛季中，梅西曾一度重伤两个月之久。巴萨不但没有掉队，而且三线都保持高度竞争力，这很大程度上要源于苏亚雷斯和内马尔之间的默契。在昨天梅西半场离场之后，内马尔和苏亚雷斯又成了巴萨主角。在连续不停球直接传球之后，内少又为苏神送出了一次保姆助攻。《每日体育报》指出，苏亚雷斯和内马尔19轮联赛中互相“喂饼”9次，这一数据冠绝欧洲。',
    //            "dateTime": '2016.01.19',
    //            "author": '是我是',
    //            "joinNum": '99999'
    //        },
    //        {
    //            "id": 4,
    //            "title" : '巴萨SN互喂9饼梅西你眼红吗 苏牙1数据接班恩帅',
    //            "pic" : '../images/banner/3.jpg',
    //            "website": '新浪网',
    //            "abstract": '在本赛季中，梅西曾一度重伤两个月之久。巴萨不但没有掉队，而且三线都保持高度竞争力，这很大程度上要源于苏亚雷斯和内马尔之间的默契。在昨天梅西半场离场之后，内马尔和苏亚雷斯又成了巴萨主角。在连续不停球直接传球之后，内少又为苏神送出了一次保姆助攻。《每日体育报》指出，苏亚雷斯和内马尔19轮联赛中互相“喂饼”9次，这一数据冠绝欧洲。',
    //            "dateTime": '2016.01.19',
    //            "author": '是我是',
    //            "joinNum": '9999999'
    //        },
    //        {
    //            "id": 5,
    //            "title" : '巴萨SN互喂9饼梅西你眼红吗 苏牙1数据接班恩帅',
    //            "pic" : '../images/banner/3.jpg',
    //            "website": '新浪网',
    //            "abstract": '在本赛季中，梅西曾一度重伤两个月之久。巴萨不但没有掉队，而且三线都保持高度竞争力，这很大程度上要源于苏亚雷斯和内马尔之间的默契。在昨天梅西半场离场之后，内马尔和苏亚雷斯又成了巴萨主角。在连续不停球直接传球之后，内少又为苏神送出了一次保姆助攻。《每日体育报》指出，苏亚雷斯和内马尔19轮联赛中互相“喂饼”9次，这一数据冠绝欧洲。',
    //            "dateTime": '2016.01.19',
    //            "author": '是我是',
    //            "joinNum": '99999'
    //        }
    //    ],
    //    //折线图数据渲染
    //    [
    //        ['2015.12.31', '2016.01.06', '2016.01.11', '2016.01.15'],
    //        [
    //            {
    //                name: '悲伤',
    //                data: [48, 78, 88, 101]
    //            },{
    //                name: '愉快',
    //                data: [99, 150, 500, 999]
    //            },{
    //                name: '愤怒',
    //                data: [120, 150, 155, 148]
    //            },{
    //                name: '喜欢',
    //                data: [160, 180, 300, 312]
    //            }
    //        ]
    //    ],
    //    //有关新闻来源的饼图数据
    //    [
    //        ['搜狐',  100.0],
    //        ['新浪',  0.00],
    //        ['网易',  0.00],
    //        ['腾讯',  0.00],
    //        ['凤凰',  0.00]
    //    ],
    //    //有关各种情绪比例的数据
    //    [
    //        ['悲伤',  12.0],
    //        ['喜欢',  19.0],
    //        ['愤怒',  20.0],
    //        ['怨恨',  13.0],
    //        ['愉快',  11.0],
    //        ['激动',  5.0],
    //        ['未知',  12.0],
    //        ['爱你',  8.0]
    //    ]
    //];
    //console.log(data);
    var dataNews = data[0],
        dataLine = data[1],
        dataPieOne = data[2],
        dataPieSec = data[3];

    //字符串转浮点数
    dataPieOne = arrayFloat(dataPieOne);
    dataPieSec = arrayFloat(dataPieSec);
    dataLine =
        [
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
    var lineTitle = '参与话题人数时间进度',
        pieTitle = '各大网站参与话题人数比例';
    lineChart(dataLine, lineTitle, '#barChart');
    pieChart(dataPieOne, pieTitle, '#leftPie');
    emotionPie(dataPieSec, pieTitle, '#rightPie');
    renderNews(dataNews);
}

function renderNews(data){
    //console.log(data);
    var bannerData = new BannerNews(data[0]);
    var bannerTxt =render($('#bannerNews').html(), bannerData);
    $('#banner').append(bannerTxt);
    for(var i        = 1, length = data.length; i <length; i ++){
        var news = new SonNews(data[i]);
        var txt = render($('#sonEventLi').html(), news);
        $('#sonEvent ul').append(txt);
    }
}
