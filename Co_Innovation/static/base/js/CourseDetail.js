function(){
	var ms1div = $("#like");
	var ms1 = $("#like img");
	var ms2div = $("#dislike");
	var ms2 = $("#dislike img");
	ms1div.click(function(){
		ms1div.css({"border-color":"#29b06c", "color":"#29b06c"});
		ms1.css({"background-color":"#29b06c"});
		ms2div.css({"border-color":"#09aaed", "color":"#09aaed"});
		ms2.css({"background-color":"#09aaed"});
	});
	ms2div.click(function(){
		ms1div.css({"border-color":"#09aaed", "color":"#09aaed"});
		ms1.css({"background-color":"#09aaed"});
		ms2div.css({"border-color":"#29b06c", "color":"#29b06c"});
		ms2.css({"background-color":"#29b06c"});
	});
}