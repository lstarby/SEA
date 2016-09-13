
$(function(){
	var content1 = [
			{
				"label": "网易",
				"value": 5,
				"color": "#15ba63"
			},
			{
				"label": "搜狐",
				"value": 3,
				"color": "#3285c4"
			},
			{
				"label": "凤凰",
				"value": 4,
				"color": "#e9483e"
			},
			{
				"label": "腾讯",
				"value": 1,
				"color": "#fcd521"
			},
			{
				"label": "新浪",
				"value": 4,
				"color": "#fc6421"
			}
		];
	createPieChart('pieChart1', 'Top 15 Fears', '各大网站参与话题人数占比', content1);
	createPieChart('pieChart2', 'Top 14 Fears', '主要情绪占比（%）', content1);

})
function createPieChart(domId, title, subtitle, content){
	var pie = new d3pie(domId, {
	"header": {
		"title": {
			"text": title,
			"color": "#857777",
			"fontSize": 30,
			"font": "cinzel"
		},
		"subtitle": {
			"text": "【" + subtitle + "】",
			"color": "#9a8e8e",
			"fontSize": 10,
			"font": "courier"
		},
		"location": "pie-center",
		"titleSubtitlePadding": 10
	},
	"footer": {
		"color": "#999999",
		"fontSize": 10,
		"font": "open sans",
		"location": "bottom-left"
	},
	"size": {
		"canvasHeight": 450,
		"pieInnerRadius": "84%",
		"pieOuterRadius": "78%"
	},
	"data": {
		"sortOrder": "label-desc",
		"content": content
	},
	"labels": {
		"outer": {
			"format": "label-percentage1"
		},
		"inner": {
			"format": "none"
		},
		"mainLabel": {
			"color": "#898383",
			"font": "times new roman",
			"fontSize": 13
		},
		"percentage": {
			"color": "#664dc6",
			"font": "cinzel",
			"fontSize": 15,
			"decimalPlaces": 0
		},
		"value": {
			"color": "#cccc43",
			"fontSize": 11
		},
		"lines": {
			"enabled": true,
			"color": "#666262"
		},
		"truncation": {
			"enabled": true
		}
	},
	"effects": {
		"pullOutSegmentOnClick": {
			"speed": 400,
			"size": 30
		},
		"highlightSegmentOnMouseover": false,
		"highlightLuminosity": -0.18
	},
	"misc": {
		"colors": {
			"segmentStroke": "#000000"
		}
	}
});

}
