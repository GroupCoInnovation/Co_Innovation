$(function() {
	// 修改岗位
	var initial="前端工程师";
	$(".name_member").each(function(){
		$(this).children(".change_name").click(function(){
			var ms=$(this).children(".input_name");
			alert(ms.val());
			ms.focus();
			ms.val("");
			ms.attr("readOnly",false);
			$(this).children(".change_name").css("display","none");
			$(this).children(".confirm_name").css("display","block");
		});
		$(".name_member .confirm_name").click(function(){
			var ms=$(this).children(".input_name");
			$(this).children(".confirm_name").css("display","none");
			$(this).children(".change_name").css("display","block");
			if (ms.val()!=""){
				ms.attr("readOnly",true);
				initial=ms.val();
			}
			else if (ms.val()==""){
				ms.val(initial);
			}
		});
	});
	// 状态切换
	$("#current_task").click(function(){
		$("#current_task").css("color","rgb(0, 179, 89)");
		$("#done_task").css("color","#000");
		$(".doing").css("display","block");
		$(".done").css("display","none");
	});
	$("#done_task").click(function(){
		$("#done_task").css("color","rgb(0, 179, 89)");
		$("#current_task").css("color","#000");
		$(".done").css("display","block");
		$(".doing").css("display","none");
	});
	// 弹窗1
	    $('.end_project').click(function() {
	        $('#code1').center();
	        $('#goodcover').show();
	        $('#code1').fadeIn();
	    });
	    $('#closebt1').click(function() {
	        $('#code1').hide();
	        $('#goodcover').hide();
	    });
		$('#goodcover').click(function() {
	        $('#code1').hide();
	        $('#goodcover').hide();
	    });
	// 弹窗2
	    $('.noWork').mouseover(function(){
	    	$('.noWork .delete_member').css({"display":"block","cursor":"pointer"});
	    });
	    $('.noWork').mouseout(function(){
	    	$('.noWork .delete_member').css("display","none");
	    });
	    $('.delete_member').click(function() {
	        $('#code2').center();
	        $('#goodcover').show();
	        $('#code2').fadeIn();
	        $('.noWork .delete_member').css({"display":"block","cursor":"pointer"});
	    });
	    $('#closebt2').click(function() {
	        $('#code2').hide();
	        $('#goodcover').hide();
	        $('.noWork .delete_member').css("display","none");
	    });
		$('#goodcover').click(function() {
	        $('#code2').hide();
	        $('#goodcover').hide();
	        $('.noWork .delete_member').css("display","none");
	    });
	// 弹窗3
		$('.add_new_member').click(function() {
	        $('#code3').center();
	        $('#goodcover').show();
	        $('#code3').fadeIn();
	    });
	    $('#closebt3').click(function() {
	        $('#code3').hide();
	        $('#goodcover').hide();
	    });
		$('#goodcover').click(function() {
	        $('#code3').hide();
	        $('#goodcover').hide();
	    });
	// 弹窗4
	    // $('.code4 .input4 .time').datepicker({ dateFormat: "yyyy.mm.dd --:-- --"});
		$('.tableList .add_work').click(function(){
			$('#code4').center();
	        $('#goodcover').show();
	        $('#code4').fadeIn();
	    });
	    $('#closebt4').click(function() {
	        $('#code4').hide();
	        $('#goodcover').hide();
	    });
		$('#goodcover').click(function() {
	        $('#code4').hide();
	        $('#goodcover').hide();
	    });
    // 所有弹窗
	    jQuery.fn.center = function(loaded) {
	        var obj = this;
	        body_width = parseInt($(window).width());
	        body_height = parseInt($(window).height());
	        block_width = parseInt(obj.width());
	        block_height = parseInt(obj.height());

	        left_position = parseInt((body_width / 2) - (block_width / 2) + $(window).scrollLeft());
	        if (body_width < block_width) {
	            left_position = 0 + $(window).scrollLeft();
	        };

	        top_position = parseInt((body_height / 2) - (block_height / 2) + $(window).scrollTop());
	        if (body_height < block_height) {
	            top_position = 0 + $(window).scrollTop();
	        };

	        if (!loaded) {
	            obj.css({
	                'position': 'absolute'
	            });
	            obj.css({
	                'top': ($(window).height() - $('#code').height()) * 0.5,
	                'left': left_position
	            });
	            $(window).bind('resize', function() {
	                obj.center(!loaded);
	            });
	            $(window).bind('scroll', function() {
	                obj.center(!loaded);
	            });
	        } else {
	            obj.stop();
	            obj.css({
	                'position': 'absolute'
	            });
	            obj.animate({
	                'top': top_position
	            }, 200, 'linear');
	        }
	    }
})
