$(function() {
	$(".leftBox ul li").hover(function() {
		$(".leftBox ul li .Lhover").eq($(this).index()).css("display","block");
	}, function() {
		$(".leftBox ul li .Lhover").eq($(this).index()).css("display","none");
	});
});

