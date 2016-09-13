/*
* 折线图的延缓出场动画
*/
$(window).scroll(function(){
	var topDis = $(document).scrollTop();
	
	$('#header').css({
			top: topDis + 'px'
		})
	
	var winHeight = $(window).height();

	if(winHeight*2/3 < topDis){
		var barChart = $('#barChart');
		if(!barChart.hasClass('bar_show')){
			barChart.animate({
				top: '50%',
				opacity: 1
			}, 450);
			barChart.addClass('bar_show');
		}
		
	}
})



