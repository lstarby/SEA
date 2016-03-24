/**
 * Created by luoxiaotong on 2016/1/17.
 */

$(function () {

    var random = [],
       length = 10;
    for(var i = 0; i <length; i ++){
        var aa =getRandom(0, 460),
            bb = getRandom(0, 380);
        if($.inArray([aa, bb], random)){
            random.push([aa, bb]);
        }
    }
    renderKeyWord(random);
    //console.log(random);
});
function getRandom(min, max){
    var aa = Math.floor(Math.random()*(max-min+1)+min);
    return aa;
}
function renderKeyWord(position){
    var length = position.length;

    for(var i = 0; i < length; i ++){
        var size = getRandom(8, 30);
        var txt = '<span style="font-size:' + size + 'px; left:' + position[i][0] + 'px; top:' + position[i][1] + 'px;">大爆炸</span>';
        $('#keyword').append(txt);
    }
}