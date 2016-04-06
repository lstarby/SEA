/**
 * Created by luoxiaotong on 2016/1/19.
 */
function getNavId() {
    var url = window.location.href,
        navId = url.split('?')[1];
    navId = navId.split('=')[1];
    return navId;
}
//渲染导航的全部情绪
$(document).ready(function () {
    var navId = getNavId();
    getAllNews(navId);
    //callBack();//之后删掉，上面注释部分恢复
});

function getAllNews(type){
    var url = PATH + 'getHomeNews/?navId=' + type;
    getAjaxData(url, callBack);
}

function callBack(dataObj){
    var navId = getNavId();
    //先对result做处理先
    var bannerData = dataObj[0],
        allNewsData = dataObj[1];
    renderBannerNews(bannerData, navId);
    console.log(allNewsData);
    renderAllNews(allNewsData, navId);
    //alert(result[0][0]['event_abstract'])
}
function renderBannerNews(data, navId){
    for(var i = 0, length = data.length; i < length; i ++){
        var news = new BannerNews(data[i], navId);
        var txt = render($('#carouseLi').html(), news);
        $('#carouse ul').append(txt);
    }
    bannerCarouse();
}
function renderAllNews(data, navId){
    for(var i = 0, length = data.length; i < length; i ++){
        var aa = data[i].length;
        if(aa == 3){
            var news = new News(data[i], navId);
            var txt = render($('#newsLi').html(), news);
        }else if(aa == 1){
            var news = new NewsWithoutSon(data[i], navId);
            var txt = render($('#newsLiNoSon').html(), news);
        }else if(aa == 2){
            var news = new News(data[i], navId);
            var txt = render($('#newsLiOneSon').html(), news);
        }
        $('#main ul').append(txt);
    }
}