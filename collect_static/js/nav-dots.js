/**
 * Created by luoxiaotong on 2016/3/20.
 */
var navDots = {
    blockNum: $('.chart-block').length,
    blockHeight: 580,
    bannerHeight: $('#banner').height(),
    curIndex: 0,
    dotsNum: 5,
    winHeight: $(window).height(),
    topDicArr : [0],

    init: function () {
        var self = this;
        var container = document.getElementById('navDots'),
            childList = container.getElementsByTagName('ul')[0].children;

        /*初始化 topDicArr 数组*/
        var arr = this.topDicArr,
            blockH = this.blockHeight;
        arr.push(this.bannerHeight);
        for(var i = 0, len = this.blockNum; i < len; i ++) {
            arr.push(blockH + arr[i+1]);
        }

        /*绑定连接点击事件*/
        $(childList).on('click', function() {
            var index = $(this).index(),
                topDic = arr[index];
            self.linkClickScrollTo(topDic);
        });

        window.onscroll = function () {
            self.locatePage(childList, self.winHeight);
        }
    },

    locatePage: function(childList) {
        var top = $(window).scrollTop();
        var current = 0;
        var bannerHeight = this.bannerHeight,
            blockH = this.blockHeight,
            blockNum = this.blockNum;
        if(top > 2*bannerHeight/3) {
            current = Math.round(top/blockH);
        }

        if(top > (bannerHeight + blockNum * blockH)) {
            current = blockNum + 1;

        }

        for(var i = 0, len = childList.length; i < len; i ++) {
            childList[i].className = '';
        }
        var addClass = childList[current].className;

        childList[current].className = 'current';


    },
    linkClickScrollTo: function(topDic) {
        $(window).scrollTop(topDic);
    }
};
