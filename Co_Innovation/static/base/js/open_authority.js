(function($){
    $(window).on("load", function () {
        $("#input0").focusout(function(){
            var text =  $("#input0").val();
            if(text.length==8){
                $("#judge0").css("display","none");
                $("#judge0").attr("ref","0");
            }
            else{
                $("#judge0").css("display","block");
                $("#judge0").attr("ref","1");
            }
            if($("#judge0").attr("ref")=="0"&&$("#judge1").attr("ref")=="0"&&$("#judge2").attr("ref")=="0"&&$("#judge3").attr("ref")=="0"){
                $("#sub").removeAttr("disabled");
            }
            else{
                $("#sub").attr("disabled","true");
            }
        });

        $("#pw1").focusout(function(){
           var pw1 = $("#pw1").val();
           var pw2 = $("#pw2").val();
           if(pw1==pw2){
               $("#judge2").css("display","none");
               $("#judge2").attr("ref","0");
           }
           else{
               $("#judge2").css("display","block");
               $("#judge2").attr("ref","1");
           }
           if(pw1.length<6){
               $("#judge1").css("display","block");
               $("#judge1").attr("ref","1");
           }
           else{
               $("#judge1").css("display","none");
               $("#judge1").attr("ref","0");
           }
           if($("#judge0").attr("ref")=="0"&&$("#judge1").attr("ref")=="0"&&$("#judge2").attr("ref")=="0"&&$("#judge3").attr("ref")=="0"){
               $("#sub").removeAttr("disabled");
           }
           else{
               $("#sub").attr("disabled","true");
           }
        });

        $("#pw2").focusout(function(){
            var pw1 = $("#pw1").val();
            var pw2 = $("#pw2").val();
            if(pw1==pw2){
                $("#judge2").css("display","none");
                $("#judge2").attr("ref","0");
            }
            else{
                $("#judge2").css("display","block");
                $("#judge2").attr("ref","1");
            }
            if($("#judge0").attr("ref")=="0"&&$("#judge1").attr("ref")=="0"&&$("#judge2").attr("ref")=="0"&&$("#judge3").attr("ref")=="0"){
                $("#sub").removeAttr("disabled");
            }
            else{
                $("#sub").attr("disabled","true");
            }
        });

        $("#input3").focusout(function(){
            var text =  $("#input3").val();
            var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
            if(myreg.test(text)){
                $("#judge3").css("display","none");
                $("#judge3").attr("ref","0");
            }
            else{
                $("#judge3").css("display","block");
                $("#judge3").attr("ref","1");
            }
            if($("#judge0").attr("ref")=="0"&&$("#judge1").attr("ref")=="0"&&$("#judge2").attr("ref")=="0"&&$("#judge3").attr("ref")=="0"){
                $("#sub").removeAttr("disabled");
            }
            else{
                $("#sub").attr("disabled","true");
            }
        });

    });
})(jQuery);