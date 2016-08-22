 // 头像 -  用户状态切换  开始
$(document).ready(function(){
	var ms = $("#vip");
  	var add = $("#_picture");
 	ms.mouseenter(function(){
	  	add.css("display",'block');
	    ms.css("display",'none');
	});
 	add.mouseleave(function(){
	  	add.css( "display",'none');
	    ms.css("display",'block');
	});
});