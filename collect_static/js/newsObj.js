/**
 * Created by luoxiaotong on 2016/1/18.
 */
DEFAULT_PIC = '/static/images/banner/3.jpg'
var BannerNews = function (result, nav) {
    this.navId = nav;
    this.newsId = result.event_id;
    this.title = result.event_name;
    this.picSrc = result.image;
    this.abstract = result.event_abstract;
    this.dateTime = result.event_datetime;
    this.parentId = result.parent_event_id;
    this.parentNews = result.parent_event_name;
    if(!this.parentId){
        this.parentId = this.newsId;
        this.parentNews = this.title;
    }
    if(!this.picSrc){
        this.picSrc =DEFAULT_PIC;;
    }
};
var News = function (result, nav) {
    var parent = result[0],
        son1= result[1];
    this.navId = nav;
    this.parentId = parent.event_id;
    this.parTitle = parent.event_name;
    this.parPic = parent.image;
    this.parTime = parent.event_datetime;
    this.parAbstract = parent.event_abstract;
    if(!this.parPic){
        this.parPic = DEFAULT_PIC;
    }

    this.sonOneId = son1.event_id;
    this.sonTitleOne = son1.event_name;
    this.sonPicOne = son1.image;
    this.sonTimeOne = son1.event_datetime;
    this.sonAbstractOne = son1.event_abstract;
    if(!this.sonPicOne){
        this.sonPicOne = DEFAULT_PIC;
    }
    if(result.length == 3){
        var son2 = result[2];
        this.sonSecId = son2.event_id;
        this.sonTitleSec = son2.event_name;
        this.sonPicSec = son2.image;
        this.sonTimeSec = son2.event_datetime;
        this.sonAbstractSec = son2.event_abstract;
        if(!this.sonPicSec){
            this.sonPicSec = DEFAULT_PIC;
        }
    }


};
var NewsWithoutSon = function (result, nav) {
    this.navId = nav;
    this.parentId = result[0].event_id;
    this.parTitle = result[0].event_name;
    this.parPic = result[0].image;
    this.parTime = result[0].event_datetime;
    this.parAbstract = result[0].event_abstract;
    if(!this.parPic){
        this.parPic = DEFAULT_PIC;
    }
}
var SonNews = function (result, nav) {
    this.navId = nav;
    this.id = result.event_id;
    this.title = result.event_name;
    this.dateTime = result.event_datetime;
    this.pic = result.image;
    this.abstract = result.event_abstract;
    if(!this.pic){
        this.pic = DEFAULT_PIC;
    }
    this.joinNum = result.comment_num;
};

var Commments = function (result) {
    this.time = result.news_comment_datetime;
    this.comment = result.news_comment_content;
}