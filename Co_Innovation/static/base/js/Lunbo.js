// $(function() {
// 	var clone1 = $("#container #list a").first().clone();
// 	$("#list").append(clone1);
// 	var clone5 = $("#container #list a").eq(4).clone();
// 	$("#list").first().prepend(clone5);
// 	var clone4 = $("#container #list a").eq(4).clone();
// 	$("#list").first().prepend(clone4);
//
// 	var imgs = $("#container #list a");
// 	var btnsize = $("#buttons span").size();
// 	var i = 3;
// 	imgs.eq(i).css("opacity", "1");
// 	var size = imgs.size();
// 	var imgsheight = $("#container").height();
// 	var base = 121;
// 	var pdis = 1138;
//
// 	//点击向左轮播
// 	$("#prev").click(function() {
// 		i--;
// 		if (i == 1) {
// 			$("#list").css({left: (-(size-2)*pdis)+base});
// 			i=size-3;
// 		}
// 		$("#list").stop().animate({left: -(i*pdis)+base}, 700);
// 		setopc(i);
// 		$("#buttons span").eq(i-2).addClass("on").siblings().removeClass("on");
// 	});
//
// 	//点击向右轮播
// 	$("#next").click(function() {
// 		moveR();
// 	});
//
// 	//向右轮播函数
// 	function moveR() {
// 		i++;
// 		if (i == size-1) {
// 			$("#list").css({left: -1*pdis+base});
// 			i = 2;
// 		}
// 		$("#list").stop().animate({left : -i*pdis+base}, 700);
// 		setopc(i);
// 		$("#buttons span").eq(i-2).addClass("on").siblings().removeClass("on");
// 	}
//
// 	function setopc(index) {
// 		for (var k = 0; k < size; k++) {
// 			if (k != index) imgs[k].style.opacity = 0.7;
// 			else imgs[k].style.opacity = 1;
// 		}
// 	}
//
// 	//鼠标滑过圆点
// 	$("#buttons span").hover(function() {
// 		var index = $(this).index();
// 		i = index+2;
// 		setopc(i);
// 		$("#list").stop().animate({left: (-i*pdis)+base}, 700);
// 		$(this).addClass("on").siblings().removeClass("on");
// 	});
//
// 	//定时自动轮播
// 	var t = setInterval(function() {
// 		moveR();
// 	}, 5000);
//
// 	//鼠标划过图片停止自动轮播
// 	$("#container").hover(function() {
// 		clearInterval(t);},
//
// 		function() {
// 			t = setInterval(function() {
// 				moveR();
// 			}, 5000);
// 		}
// 	);
// })

//以上是旧版本的

$(function() {
	var clone1 = $("#container #list a").first().clone();
	$("#list").append(clone1);
	var clone5 = $("#container #list a").eq(4).clone();
	$("#list").first().prepend(clone5);
	var clone4 = $("#container #list a").eq(4).clone();
	$("#list").first().prepend(clone4);

	var imgs = $("#container #list a");
	var btnsize = $("#buttons span").size();
	var i = 3;
	imgs.eq(i).css("opacity", "1");
	var size = imgs.size();
	var imgsheight = $("#container").height();
	var base = 121;
	var pdis = 1138;

	//点击向左轮播
	$("#prev").click(function() {
		i--;
		if (i == 1) {
			$("#list").css({left: (-(size-2)*pdis)+base});
			i=size-3;
		}
		$("#list").stop().animate({left: -(i*pdis)+base}, 700);
		setopc(i);
		$("#buttons span").eq(i-2).addClass("on").siblings().removeClass("on");
	});

	//点击向右轮播
	$("#next").click(function() {
		moveR();
	});

	//向右轮播函数
	function moveR() {
		i++;
		if (i == size-1) {
			$("#list").css({left: -1*pdis+base});
			i = 2;
		}
		$("#list").stop().animate({left : -i*pdis+base}, 700);
		setopc(i);
		$("#buttons span").eq(i-2).addClass("on").siblings().removeClass("on");
	}

	function setopc(index) {
		for (var k = 0; k < size; k++) {
			if (k != index) imgs[k].style.opacity = 0.7;
			else imgs[k].style.opacity = 1;
		}
	}

	//鼠标滑过圆点
	$("#buttons span").hover(function() {
		var index = $(this).index();
		i = index+2;
		setopc(i);
		$("#list").stop().animate({left: (-i*pdis)+base}, 700);
		$(this).addClass("on").siblings().removeClass("on");
	});

	//定时自动轮播
	var t = setInterval(function() {
		moveR();
	}, 5000);

	//鼠标划过图片停止自动轮播
	$("#container").hover(function() {
		clearInterval(t);},

		function() {
			t = setInterval(function() {
				moveR();
			}, 5000);
		}
	);
})
