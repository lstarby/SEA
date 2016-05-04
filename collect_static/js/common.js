/**
 * Created by luoxiaotong on 2016/1/19.
 */
//var PATH = 'http://polls.nat123.net/';
var PATH = 'http://127.0.0.1:8081/';
//var PATH = 'http://192.168.235.12:8080/';
$(function () {
    getNavs();
});
function getNavs(){
    //虚拟数组
    //var data = [
    //    {
    //        "id" : 1,
    //        "emotion": '悲伤'
    //    },{
    //        "id" : 2,
    //        "emotion": '傻逼'
    //    },{
    //        "id" : 3,
    //        "emotion": '激动'
    //    },{
    //        "id" : 4,
    //        "emotion": '愤怒'
    //    },{
    //        "id" : 5,
    //        "emotion": '开心'
    //    },{
    //        "id" : 6,
    //        "emotion": '喜欢'
    //    },
    //];
    //for(var i = 0, length = data.length; i < length; i ++){
    //    var txt = '<li><a href="homepage.html?' + data[i].id + '">' + data[i].emotion + '</a></li>';
    //    $('#nav ul').append(txt);
    //}
    var url = PATH + 'getNavs/';
    getAjaxData(url, function (data) {
        //还要对返回的data做处理的
        for(var i = 0, length = data.length; i < length; i ++){
            var txt = '<li><a href="/homepage.html?navId=' + data[i].normal_event_type_id + '">' + data[i].normal_event_type_name + '</a></li>';
//            var txt = '<li><a href="homepage.html?navId=' + data[i].normal_event_type_id + '">' + data[i].normal_event_type_name + '</a></li>';
            $('#nav ul').append(txt);
        }
        navHighlight();
    });
}
function navHighlight(){
    var navs = $('#nav ul li a');
    navs.removeClass('current');
    var url = window.location.href;
    url = url.split('?')[1];
    var searchItems = getSearchItem(url),
        navId = searchItems.navId;
        navs.each(function () {
            var id = $(this).attr('href').split('navId=')[1];
            if(id == navId){
                $(this).addClass('current');
            }
        });
}

function getAjaxData(url, callback, data){
    $.ajax({
        type: 'GET',
        url : url,
        dataType: 'jsonp',
        data: data,
        success: function(ajson){
            console.log(ajson);

            callback(ajson);
        }
    })
}

function bannerCarouse(){
    var slidney = $('#carouse').unslider({
            speed: 500,               //  The speed to animate each slide (in milliseconds)
            delay: 3000,              //  The delay between slide animations (in milliseconds)
            complete: function() {},  //  A function that gets called after every slide animation
            keys: false,               //  Enable keyboard (left, right) arrow shortcuts
            dots: true,               //  Display dot navigation
            fluid: false              //  Support responsive design. May break non-responsive designs

        }),
        data = slidney.data('unslider');
    var startSlide = function(){
        data.start();
    };
    setInterval(startSlide, 5000);
    data.start();
}
function arrayFloat(arr){
    for(var i = 0, length = arr.length; i < length; i ++){
        arr[i][1] = parseFloat(arr[i][1]);
    }
    return arr;
}

/*
 * 将传过来的地址栏的search 字符串解析  然后 返回数组
 */
function getSearchItem(){
    var url = window.location.href;
    url = url.split('?')[1];
    url = url.split('&');
    var searchData = {};

    for(var i = 0, length = url.length; i < length; i ++){
        var items = url[i].split('=');
        searchData[items[0]] = items[1];
    }

    return searchData;
}


