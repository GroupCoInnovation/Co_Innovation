
(function ($) {
	var Delete_man;// 待删除的当前成员
	var this_new_work;// 待添加任务的当成员
	var this_work_list;//待添加任务对应的workList
	var this_change_mem;//待修改任务的当前成员
	var this_change_work;//待修改的当前任务
	var initial="前端工程师";
	$(window).on("load", function(){
		// 弹窗4 添加任务
			$('.add_work').click(function(){
				this_new_work=$(this).closest('.member_num');//得到当前成员的obj
		    	$('.member_name4').val(this_new_work.find('#memberID').val());// 得到当前成员的ID显示在弹窗上
				$('#code4').center();
		        $('#goodcover').show();
		        $('#code4').fadeIn();
		        this_work_list=$(this).closest('.member_num').find(".workList");// 找到当前成员的任务列表workList
		     });
		    $('.close4').click(function(){
		        $('#code4').hide();
		        $('#goodcover').hide();
		    });
			$('#goodcover').click(function() {
		        $('#code4').hide();
		        $('#goodcover').hide();
		    });
		    $('.yes4').click(function(){
		    	if (($('#Project_name4').val()!="") && ($('#Project_strat4').val()!="") && ($('#Project_end4').val()!="") && ($('#Project_money4').val()!="") && (isNaN($('#Project_money4').val())==false) && ($('#Project_money4').val()>=0)) {
			    	// 给当前成员的任务列表末尾添加新任务
			    	this_work_list.append("<div class='work row'><div class='task col-xs-3 col-md-3 col-lg-3'><p class='no-change'><input class='labelWork' value='任务1' readonly='true'><span class='extra'><span class='pass_work'>签收</span><span class='revamp_work'>修改</span><span class='delete_work'>删除</span></span></p></div><div class='start_time col-xs-3 col-md-3 col-lg-3'><input type='text' name='start_time' value='1996.8.7 20:30' readonly='true'/></div><div class='finish_time col-xs-3 col-md-3 col-lg-3'><input type='text' name='finish_time' value='1996.8.7 20:30' readonly='true'/></div><div class='money_num col-xs-3 col-md-3 col-lg-3'><input type='text' name='money_num' value='10' readonly='true'/></div></div>");
			    	this_work_list.attr("href",this_work_list.children().length);// 获取当前所有的任务数量
			    	if (this_new_work.hasClass('noWork')){
			    		this_new_work.removeClass("noWork").addClass("haveWork");// 无任务成员的noWork标志消失，无法被删除
			    		alert(this_new_work.attr("class"));
			    	}
			    	var obj=this_work_list.children().last();// 获得最新添加的任务
			    	obj.attr("href",this_work_list.children().length);// 修改workList的任务数量显示标志			    
			    	// 将弹窗中的数据赋值到新添加任务栏中
		    		obj.find('.labelWork').val($('#Project_name4').val());		    		    	
		    		obj.find('.start_time input').val($('#Project_strat4').val());			    		    	
		    		obj.find('.finish_time input').val($('#Project_end4').val());    	
			    	obj.find('.money_num input').val($('#Project_money4').val());
			    	$('#code4').hide();
		        	$('#goodcover').hide();
			    }
		    });
		// 弹窗5 签收任务
			$(".pass_work").each(function(){
				var that;
				$('.pass_work').click(function(){
					that=$(this);
					$('#code5').center();
			        $('#goodcover').show();
			        $('#code5').fadeIn();
				});
				$('.yes5').click(function() {
			        $('#code5').hide();
			        $('#goodcover').hide();
			        // 将已签收任务发到 已完成 栏目中
			        alert(that.closest('.member_num').attr("class").Replace(SpaceChar.ToString(),"."));
					$(".done ."+"'"+that.closest('.member_num').attr("class").Replace(SpaceChar.ToString(),".")+"' .workList").append(that.closest('.work'));
			    });
				$('.close5').click(function() {
			        $('#code5').hide();
			        $('#goodcover').hide();
			    });
				$('#goodcover').click(function() {
			        $('#code5').hide();
			        $('#goodcover').hide();
			    });
			});
		// 弹窗6 修改任务
			$(".revamp_work").click(function(){
				this_change_mem=$(this).closest('.member_num');
				this_change_work=$(this).closest('.work');
		    	$('.member_name6').val(this_change_mem.find('#memberID').val());// 得到当前成员的ID显示在弹窗上
				$('#code6').center();
		        $('#goodcover').show();
		        $('#code6').fadeIn();  
		        $('#Project_name6').val(this_change_work.find(".labelWork").val());
		    	$('#Project_strat6').val(this_change_work.find(".start_time input").val());
		    	$('#Project_end6').val(this_change_work.find(".finish_time input").val());
		    	$('#Project_money6').val(this_change_work.find(".money_num input").val());  
		    });
		    $('.close6').click(function(){
		        $('#code6').hide();
		        $('#goodcover').hide();
		    });
			$('#goodcover').click(function() {
		        $('#code6').hide();
		        $('#goodcover').hide();
		    });
		    $('.yes6').click(function(){
		    	if ( ($('#Project_name6').val()!="") && ($('#Project_strat6').val()!="") && ($('#Project_end6').val()!="") && ($('#Project_money6').val()!="") && (isNaN($('#Project_money6').val())==false) && ($('#Project_money6').val()>=0) )
		    	{	
			    	this_change_work.find(".labelWork").val($('#Project_name6').val());    
			    	this_change_work.find(".start_time input").val($('#Project_strat6').val());
			    	this_change_work.find(".finish_time input").val($('#Project_end6').val()); 
				    this_change_work.find(".money_num input").val($('#Project_money6').val());
			    	$('#code6').hide();
		        	$('#goodcover').hide();
			    }
			});
		// 弹窗7 删除任务
			$(".delete_work").each(function(){
				var that;
				$('.delete_work').click(function(){
					that=$(this);
					$('#code7').center();
			        $('#goodcover').show();
			        $('#code7').fadeIn();
				});
				$('.yes7').click(function() {
			        $('#code7').hide();
			        $('#goodcover').hide();
			        that.closest('.work').remove();
			        var this_mem=that.closet('.member_num');
			        var this_mem_doing_work = that.closet('.workList').children().length;
			        var this_mem_done_work = ($(".done").find(this_mem.attr("id")+'.workList').children()).length;
			        if (this_mem.hasClass('haveWork') && this_mem.find('.workList').children().length==0 ){
			    		that.closet('.member_num').removeClass("haveWork").addClass("noWork");// 无任务成员的noWork标志消失，无法被删除
			    		alert(that.closet('.member_num').attr("class"));
			    	}
				});
				$('.close7').click(function() {
			        $('#code7').hide();
			        $('#goodcover').hide();
			    });
				$('#goodcover').click(function() {
			        $('#code7').hide();
			        $('#goodcover').hide();
			    });
			});
	    // 所有弹窗
		    jQuery.fn.center = function(loaded) {
		        var obj = $(this);
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
	});
})(jQuery);
	
