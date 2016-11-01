(function($)
{
	var i;// 总人数
	var Delete_man;// 待删除的当前成员
	var this_new_work;// 待添加任务的当成员
	var this_work_list;//待添加任务对应的workList
	var this_change_mem;//待修改任务的当前成员
	var this_change_work;//待修改的当前任务
	var initial="前端工程师";
	var pass_work_that;
	var delete_work_that;
	var revamp_work_that;
	var job_name;
	var say_yes;
	var say_change;
	$(window).on("load", function(){
		i = $(".doing").children().length-1;
		// 可编辑项目简介
		$("#change_text").click(function(){
			$("#change_text").css("display","none");
			$("#true_text").css("display","inline-block");
			$("#titles").attr("readOnly",false);
			$("#titlebi").attr("readOnly",false);
			$("#titles").css("border","1px solid #d0d0d0");
			$("#titlebi").css("border","1px solid #d0d0d0");
		});
		$("#true_text").click(function(){
			$("#true_text").css("display","none");
			$("#change_text").css("display","inline-block");
			$("#titles").attr("readOnly",true);
			$("#titlebi").attr("readOnly",true);
			$("#titles").css("border","solid 0px");
			$("#titlebi").css("border","solid 0px");
			$(".text_shadow").html($("#titles").val());
		});
		// 弹窗1 结束项目
		$('.end_project').click(function() {
			$('#code1').center();
			$('#goodcover').show();
			$('#code1').fadeIn();
		});
		$('#goodcover').click(function() {
			$('#code1').hide();
			$('#goodcover').hide();
		});
		$('.close1').click(function() {
			$('#code1').hide();
			$('#goodcover').hide();
		});
		$(".yes1").click(function(){
			var text = $("#yes_or_no1").val();
			if(text=="确认结束项目"){
				window.open("http://www.baidu.com");
				// $(".yes1 a").attr("href","http://www.baidu.com");
			}
		});
		// 弹窗2 删除成员
		$('.doing .noWork').mouseover(function(){
			Delete_man=$(this);
			Delete_man.children('.delete_member').css({"display":"block","cursor":"pointer"});
		});
		$('.doing .noWork').mouseout(function(){
			Delete_man.children('.delete_member').css({"display":"none"});
		});
		$('.delete_member').click(function() {
			$('.member_name2').val(Delete_man.find(".person div input[name='memberID']").val());
			$('#code2').center();
			$('#goodcover').show();
			$('#code2').fadeIn();
			$(this).css({"display":"block","cursor":"pointer"});
		});
		$('.close2').click(function() {
			$('#code2').hide();
			$('#goodcover').hide();
			$('.delete_member').css("display","none");
		});
		$('#goodcover').click(function() {
			$('#code2').hide();
			$('#goodcover').hide();
			$('.delete_member').css("display","none");
		});
		$('.yes2').click(function(){
				var done_mem_name=Delete_man.attr("class").substring(0,8);
				if (done_mem_name[0]==" "){
					done_mem_name[0]="m";
				}
				$("."+done_mem_name).remove();
				$('#code2').hide();
				$('#goodcover').hide();
			});
		// 弹窗3 添加新成员
		$('.add_new_member').click(function() {
			$('#code3').center();
			$('#goodcover').show();
			$('#code3').fadeIn();
		});
		$('.close3').click(function() {
			$('#code3').hide();
			$('#goodcover').hide();
		});
		$('#goodcover').click(function() {
			$('#code3').hide();
			$('#goodcover').hide();
		});
		$('.yes3').click(function(){
			i++;
			$(".doing .add_new_member").before("<div class='member_"+i+" row member member_num noWork'><div class='delete_member'><img src='img/picture/x.png'></div><div class='person col-xs-2 col-md-2 col-lg-2'><div><img src='img/projectManage-personal/head_pic.png'></div><div><input type='text' name='memberID' readonly='true' value='程序猿'/></div><div class='name_member'><input type='text' value='前端工程师' class='input_name' readonly='true'/><span class='change_name'>修改</span><span class='confirm_name'>确认</span></div></div><div class='col-xs-8 col-md-8 col-lg-8'><div class='table_th row'><div class='col-xs-3 col-md-3 col-lg-3' style='width:27%'>任务名称</div><div class='col-xs-3 col-md-3 col-lg-3'>开始时间</div><div class='col-xs-3 col-md-3 col-lg-3'>截止时间</div><div class='col-xs-3 col-md-3 col-lg-3'  style='width:23%'>金币数</div></div><div class='workList'></div><div class='newWork row'><div class='col-xs-3 col-md-3 col-lg-3'  style='width:27%' ><p class='add_work'>添加任务...</p></div></div></div><div class='moneyLinst col-xs-2 col-md-2 col-lg-2'><div class='static_bar'><div class='progress_bar' style='width:50%'></div></div><p class='money_percent'>所获金币总数占50%</p></div></div>");
			$(".done").append("<div class='member_"+i+" row member member_num noWork'><div class='delete_member'><img src='img/picture/x.png'></div><div class='person col-xs-2 col-md-2 col-lg-2'><div><img src='img/projectManage-personal/head_pic.png'></div><div><input id='memberID' type='text' name='memberID' readonly='true' value='程序猿'/></div><div class='name_member'><input type='text' value='前端工程师' class='input_name' readonly='true'/><span class='change_name'>修改</span><span class='confirm_name'>确认</span></div></div><div class='col-xs-8 col-md-8 col-lg-8'><div class='table_th row'><div class='col-xs-3 col-md-3 col-lg-3'  style='width:27%'>任务名称</div><div class='col-xs-3 col-md-3 col-lg-3'>开始时间</div><div class='col-xs-3 col-md-3 col-lg-3'>截止时间</div><div class='col-xs-3 col-md-3 col-lg-3'  style='width:23%'>金币数</div></div><div class='workList'></div><div class='newWork row'><div class='col-xs-3 col-md-3 col-lg-3' style='width:27%'><p class='add_work'>添加任务...</p></div></div></div><div class='moneyLinst col-xs-2 col-md-2 col-lg-2'><div class='static_bar'><div class='progress_bar' style='width:50%'></div></div><p class='money_percent'>所获金币总数占50%</p></div></div>");
			var ID=$("#ID_input3").val();
			$(".member_"+i).find(".person div input[name='memberID']").val(ID);
			//  删除成员
			$('.doing .noWork').mouseover(function(){
				Delete_man=$(this);
				Delete_man.children('.delete_member').css({"display":"block","cursor":"pointer"});
			});
			$('.doing .noWork').mouseout(function(){
				Delete_man.children('.delete_member').css({"display":"none"});
			});
			$('.delete_member').click(function() {
				$('.member_name2').val(Delete_man.find(".person div input[name='memberID']").val());
				$('#code2').center();
				$('#goodcover').show();
				$('#code2').fadeIn();
				$(this).css({"display":"block","cursor":"pointer"});
			});
			$('#code3').hide();
			$('#goodcover').hide();
			// 添加任务
			$(".member_"+i).find('.add_work').click(function () {
				this_new_work = $(".member_"+i);//得到当前成员的obj
				$('.member_name4').val(this_new_work.find("input[name='memberID']").val());// 得到当前成员的ID显示在弹窗上
				$('#code4').center();
				$('#goodcover').show();
				$('#code4').fadeIn();
				this_work_list = $(this).closest('.member_num').find(".workList");// 找到当前成员的任务列表workList
			});
			// 修改岗位
			$(".member_"+i).find(".change_name").click(function(){
				say_change=$(this);
				say_yes = $(this).next();
				job_name = $(this).prev();
				job_name.focus();
				job_name.val("");
				job_name.attr("readOnly",false);
				say_change.css("display","none");
				say_yes.css("display","block");
			});
			$(".member_"+i).find(".name_member .confirm_name").click(function(){
				say_yes.css("display","none");
				say_change.css("display","block");
				if (job_name.val()!=""){
					job_name.attr("readOnly",true);
					initial=job_name.val();
				}
				if (job_name.val()==""){
					job_name.val(initial);
				}
				//同步修改“已完成”对应的成员的岗位
				var new_mem=$(this).closest(".member_num").attr("class").substring(31,39);
				$(".done ." + new_mem + " .input_name").val(job_name.val());
			});
		});
		// 弹窗4 添加任务
		$('.add_work').click(function () {
			this_new_work = $(this).closest('.member_num');//得到当前成员的obj
			$('.member_name4').val(this_new_work.find("input[name='memberID']").val());// 得到当前成员的ID显示在弹窗上
			$('#name4').val(this_new_work.find("input[name='memberID']").val());// 得到当前成员的ID显示在弹窗上
			$('#code4').center();
			$('#goodcover').show();
			$('#code4').fadeIn();
			this_work_list = $(this).closest('.member_num').find(".workList");// 找到当前成员的任务列表workList
		});
		$('.close4').click(function () {
			$('#code4').hide();
			$('#goodcover').hide();
		});
		$('#goodcover').click(function () {
			$('#code4').hide();
			$('#goodcover').hide();
		});
		$('.yes4').click(function () {
			if (($('#Project_name4').val() != "") && ($('#Project_strat4').val() != "") && ($('#Project_end4').val() != "") && ($('#Project_money4').val() != "") && (isNaN($('#Project_money4').val()) == false) && ($('#Project_money4').val() >= 0)) {
				// 给当前成员的任务列表末尾添加新任务
				this_work_list.append("<div class='work row'><div class='task col-xs-3 col-md-3 col-lg-3' style='width:27%'><p class='no-change'><input class='labelWork' value='任务3'/><span class='extra'><span class='pass_work'>签收</span><span class='revamp_work'>修改</span><span class='delete_work'>删除</span></span></p></div><div class='start_time col-xs-3 col-md-3 col-lg-3'><input type='text' name='start_time' value='2016.8.9 15:00'/></div><div class='finish_time col-xs-3 col-md-3 col-lg-3'><input type='text' name='finish_time' value='2016.8.9 15:00'/></div><div class='money_num col-xs-3 col-md-3 col-lg-3' style='width:23%'><input type='text' name='money_num' value='5'/></div></div>");
				if (this_new_work.hasClass('noWork')) {
					this_new_work.find(".delete_member").remove();
					this_new_work.removeClass("noWork").addClass("haveWork");
				}
				var obj = this_work_list.children().last();
				obj.attr("href", this_work_list.children().length);
				obj.find('.labelWork').val($('#Project_name4').val());
				obj.find('.start_time input').val($('#Project_strat4').val());
				obj.find('.finish_time input').val($('#Project_end4').val());
				obj.find('.money_num input').val($('#Project_money4').val());
				obj.find('.extra span').css({
					"padding":"0px",
					"margin-left":"-1px",
				});
				// 弹窗5 签收任务
				obj.find(".pass_work").click(function () {
					pass_work_that = $(this);
					$('#code5').center();
					$('#goodcover').show();
					$('#code5').fadeIn();
				});
				// 弹窗6 修改任务
				obj.find(".revamp_work").click(function () {
					revamp_work_that = $(this);
					this_change_mem = revamp_work_that.closest('.member_num');
					this_change_work = revamp_work_that.closest('.work');
					$('.member_name6').val(this_change_mem.find(".person div input[name='memberID']").val());// 得到当前成员的ID显示在弹窗上
					$('#code6').center();
					$('#goodcover').show();
					$('#code6').fadeIn();
					$('#Project_name6').val(this_change_work.find(".labelWork").val());
					$('#Project_strat6').val(this_change_work.find(".start_time input").val());
					$('#Project_end6').val(this_change_work.find(".finish_time input").val());
					$('#Project_money6').val(this_change_work.find(".money_num input").val());
				});
				// 弹窗7 删除任务
				obj.find('.delete_work').click(function () {
					delete_work_that = $(this);
					$('#code7').center();
					$('#goodcover').show();
					$('#code7').fadeIn();
				});
				$('#code4').hide();
				$('#goodcover').hide();
			}
		});
		// 弹窗5 签收任务
		$(".pass_work").each(function(){
			$('.pass_work').click(function(){
				pass_work_that=$(this);
				$('#code5').center();
				$('#goodcover').show();
				$('#code5').fadeIn();
			});
			$('.yes5').click(function() {
				$('#code5').hide();
				$('#goodcover').hide();
				// 将已签收任务发到 已完成 栏目中
				$(".done ."+pass_work_that.closest('.member_num').attr("class").substr(0,8)+" .workList").append(pass_work_that.closest('.work'));
				$("#general_Income").val(parseInt($("#general_Income").val())+parseInt(pass_work_that.closest('.work').find(".money_num input").val()));
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
		$(".revamp_work").each(function(){
			$(".revamp_work").click(function(){
				revamp_work_that=$(this);
				this_change_mem=revamp_work_that.closest('.member_num');
				this_change_work=revamp_work_that.closest('.work');
				$('.member_name6').val(this_change_mem.find(".person div input[name='memberID']").val());// 得到当前成员的ID显示在弹窗上
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
		});
		// 弹窗7 删除任务
		$(".delete_work").each(function(){
				$('.delete_work').click(function(){
					delete_work_that=$(this);
					$('#code7').center();
			        $('#goodcover').show();
			        $('#code7').fadeIn();
				});
				$('.yes7').click(function() {
			        $('#code7').hide();
			        $('#goodcover').hide();
			        var this_mem=delete_work_that.closest('.member_num');
					delete_work_that.closest('.work').remove();
			        var done_mem_name= this_mem.attr("class").substring(0,8);
			    	if (done_mem_name[0]!='m'){
			    		done_mem_name[0]="m";
			    	}
			        var this_mem_doing_work = this_mem.find('.workList').children().length;
			    	var done_num_work=$(".done ."+done_mem_name+" .workList").children().length;
			    	if (done_num_work==0 && this_mem_doing_work==0){
						this_mem.prepend("<div class='delete_member'><img src='img/picture/x.png'></div>");
			    		this_mem.removeClass("haveWork").addClass("noWork");
						this_mem.mouseover(function(){
							$(this).children('.delete_member').css({"display":"block","cursor":"pointer"});
						});
						this_mem.mouseout(function(){
							$('.delete_member').css({"display":"none"});
						});
						this_mem.find("delete_member").click(function() {
							$('.member_name2').val(this_mem.find(".person div input[name='memberID']").val());
							$('#code2').center();
							$('#goodcover').show();
							$('#code2').fadeIn();
							$(this).css({"display":"block","cursor":"pointer"});
						});
						$('.close2').click(function() {
							$('#code2').hide();
							$('#goodcover').hide();
							$('.delete_member').css("display","none");
						});
						$('#goodcover').click(function() {
							$('#code2').hide();
							$('#goodcover').hide();
							$('.delete_member').css("display","none");
						});
						$('.yes2').click(function(){
							var done_mem_name=Delete_man.attr("class").substring(0,8);
							if (done_mem_name[0]==" "){
								done_mem_name[0]="m";
							}
							$("."+done_mem_name).remove();
							$('#code2').hide();
							$('#goodcover').hide();
						});
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
		// 修改岗位

		$(".change_name").click(function(){
			say_change=$(this);
			say_yes = $(this).next();
			job_name = $(this).prev();
			job_name.focus();
			job_name.val("");
			job_name.attr("readOnly",false);
			say_change.css("display","none");
			say_yes.css("display","block");
		});
		$(".name_member .confirm_name").click(function(){

			
			
			say_yes.css("display","none");
			say_change.css("display","block");

			if (job_name.val()!=""){
				job_name.attr("readOnly",true);
				initial=job_name.val();
			}
			if (job_name.val()==""){
				job_name.val(initial);
			}
			//同步修改“已完成”对应的成员的岗位
			var new_mem=$(this).closest(".member_num").attr("class").substring(31,39);
			$(".done ." + new_mem + " .input_name").val(job_name.val());

			var role = job_name.val();
            var user = $(this).next().val();
			var pid = $(this).next().next().val();
			alert(pid);
            $.get("/ProjectShow/change_role",{'role':role, 'user':user, 'pid':pid}, function(ret){
				//alert(ret);
                //$('#role').val(ret);
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
	
