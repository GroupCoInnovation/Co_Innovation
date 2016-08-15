(function($){
	$(window).on("load",function(){
		var amount=Math.max.apply(Math,$("#content-1 li").map(function(){return $(this).outerWidth(true);}).get());
				
		$("#content-1").mCustomScrollbar({
			axis:"x",
			theme:"inset",
			advanced:{
				autoExpandHorizontalScroll:true
			},
			scrollButtons:{
				enable:true,
				scrollType:"stepped"
			},
			keyboard:{scrollType:"stepped"},
			snapAmount:amount,
			mouseWheel:{scrollAmount:amount}
		});
				
	});
})(jQuery);