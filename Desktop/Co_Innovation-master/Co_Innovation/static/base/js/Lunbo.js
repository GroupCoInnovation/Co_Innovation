$(function() {
	var clone1 = $("#container #list a").first().clone();
	$("#list").append(clone1);
	var clone5 = $("#container #list a").eq(4).clone();
	$("#list").first().prepend(clone5);
	var clone4 = $("#container #list a").eq(4).clone();
	$("#list").first().prepend(clone4);

	var btnsize = $("#buttons span").size();

	var imgs = $("#container #list .LunboImg");
	var size = imgs.size();
	var viewWidth, base, pdis, imgsWidth;

	var i = 3;
	setopc(i);

	var sf = 0;
	adjust();

	window.onresize = function() {
		adjust();
	}

	function adjust() {
		base = document.body.clientWidth*0.09;
		pdis = document.body.clientWidth*0.84;
		for (var j = 0; j < size; j++) {
			imgs.eq(j).css({width: document.body.clientWidth*0.84});
			imgs.eq(j).css({height: 450});
		}
		imgsWidth = imgs.eq(0).width();
		$("#list").css({width:imgs.eq(0).width()*(imgs.length+1)});
		if (sf == 0) {
			$("#list").css({left: -(document.body.clientWidth*0.84)*3+document.body.clientWidth*0.08});
			sf = 1;
		} else {
			$("#list").css({left : -i*pdis+base});
		}
	}

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