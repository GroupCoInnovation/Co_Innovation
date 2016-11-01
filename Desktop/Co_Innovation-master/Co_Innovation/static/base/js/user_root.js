$(function() {
	var rootManages = $(".root_manage");
	var rmsize = rootManages.length;
	for (var j = 0; j < rmsize; j++) {
		let k = j;
		rootManages.eq(j).mouseover(function() {
			$(".chose_button").eq(k).css({"display":"block"});
		});
		rootManages.eq(j).mouseout(function() {
			$(".chose_button").eq(k).css({"display":"none"});
		});
	}
	var chose_open_btn = $(".chose_open");
	for (var j = 0; j < chose_open_btn.length; j++) {
		let k = j;
		chose_open_btn.eq(j).click(function() {
			if ($(".root_text").hasClass("gray_text") == false)
			$(".root_text").eq(k).text("开通");
		});
	}
	var chose_close_btn = $(".chose_close");
	for (var j = 0; j < chose_close_btn.length; j++) {
		let k = j;
		chose_close_btn.eq(j).click(function() {
			if ($(".root_text").hasClass("gray_text") == false)
			$(".root_text").eq(k).text("关闭");
		});
	}
});