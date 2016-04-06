/**
 * Created by luoxiaotong on 2016/1/17.
 */

function renderKeyWords(links) {
    var tick = function() {
        link
            .attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node
            .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    }
//    var links = [
//        {source: "天津", target: "关键词", size: 0.7},
//        {source: "河南", target: "关键词", size: 0.6},
//        {source: "上海", target: "关键词", size: 0.3},
//        {source: "大爆炸", target: "关键词", size: 0.5}
//    ];

    var nodes = {};
    links.forEach(function(link) {
        link.source = nodes[link.source] || (nodes[link.source] = {name: link.source,size: link.size});
        link.target = nodes[link.target] || (nodes[link.target] = {name: link.target,size: link.size});
    });
    /*console.log(nodes);*/

    var keyDivObj = $('#keyWord');
    var width = keyDivObj.width(),
        height = keyDivObj.height();
    var force = d3.layout.force()
        .nodes(d3.values(nodes))
        .links(links)
        .size([width, height])
        .linkDistance(300)
        .charge(-300)
        .on("tick", tick)
        .start();

    var svg = d3.select("body #keyWord").append("svg")
        .attr('xmls', "http://www.w3.org/2000/svg")
        .attr("width", width)
        .attr("height", height);

    var link = svg.selectAll(".link")
        .data(force.links())
        .enter().append("line")
        .attr("class", "link"); //连接线的样式

    var node = svg.selectAll(".node")
        .data(force.nodes())
        .enter().append("g")
        .attr("class", "node")
        .call(force.drag);

    node.append("circle")
        .attr("r", function(d) {
            return d.size*50;
        });

    node.append("text").attr('style', function(d) {
        return 'font-size: ' + d.size*30 + 'px';
    })
        .attr('fill', '#ffffff')
        .attr("dy", ".35em")
        .text(function(d) { return d.name; });




}






/*
function getRandom(min, max){
    var aa = Math.floor(Math.random()*(max-min+1)+min);
    return aa;
}
function keyWord(positionX, data, height){
    for(var i = 0, length = data.length; i < length; i ++){
        var weight = data[i][1];
        var size = weight*43;
        if(size >= height){
            size = height;
        }
        var colorR = Math.round(25 - weight*10),
            colorG = Math.round(80 - weight*80),
            colorB = Math.round(222 - weight*135),
            color = 'rgb('+ colorR + ',' + colorG + ',' + colorB + ')';
        var txt = '<p style="height:'+ height + 'px;"><span style="color:' + color +';font-size:' + size + 'px; left:' + positionX[i] + 'px;">' + data[i][0] + '</span></p>';
        $('#keyword').append(txt);
    }
}
function renderKeyWords(data){
    var randomX = [],
        length = data.length;
    for(var i = 0; i <length; i ++){
        var aa =getRandom(60, 350);
        if($.inArray(aa, randomX)){
            randomX.push(aa);
        }
    }
    var height = $('#keyword').height(),
        averageH = height/length;

    keyWord(randomX, data, averageH);
}*/


