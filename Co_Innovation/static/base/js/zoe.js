$("#not_done").click(function(){
	$("#not_done").css({
		"background-color": "#01a253",
		"color": "#FFF"
	});
	$("#not_done a").css({
		"background-color": "#01a253",
		"color": "#FFF"
	});
	$("#done").css({
		"background-color": "#FFF",
		"color": "#01a253"
	});
	$("#done a").css({
		"background-color": "#FFF",
		"color": "#01a253"
	});
	$("#rightbox1").css("display","block");
	$("#rightbox2").css("display","none");
});
$("#done").click(function(){
	$("#done").css({
		"background-color": "#01a253",
		"color": "#FFF"
	});
	$("#done a").css({
		"background-color": "#01a253",
		"color": "#FFF"
	});
	$("#not_done").css({
		"background-color": "#FFF",
		"color": "#01a253"
	});
	$("#not_done a").css({
		"background-color": "#FFF",
		"color": "#01a253"
	});
	$("#rightbox2").css("display","block");
	$("#rightbox1").css("display","none");
});