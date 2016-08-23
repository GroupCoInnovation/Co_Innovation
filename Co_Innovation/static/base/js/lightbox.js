$(function() {
	var imgs = $("#list div img");
	var i = 0;
	var size_ = imgs.length;
	var maxi = (size_ / 3) - 1;
	var pdis = 342;
	//点击向上轮播
	$("#toTop").click(function() {
		if (i != 0) {
			i--;
			$("#list").animate({top: -i*pdis}, 700);
		}
	});
	//点击向下轮播
	$("#toDown").click(function() {
		if (i < maxi) {
			i++;
			$("#list").animate({top: -i*pdis}, 700);
		}
	});
	$("#list .prePic").click(function() {
		var index = $(this).index();
		var str = "img/LightBoxPic/b" + (index+1) + ".png";
		$(".WraperLBigPic").css("background-image", "url("+str+")");
	});
})