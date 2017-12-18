$(document).ready(function(){
	$('#PageRefresh').click(function() {
 
        location.reload();//重新載入頁面
 
    });
    $("#input1").keydown(function(event){//當在#input1按下ENTER 即觸發#send
        if(event.keyCode == 13){
            $("#send").click();
        }
    });
    $("#input_custom_limit").keydown(function(event){//當在#input_custom_limit").按下ENTER 即觸發#send
        if(event.keyCode == 13){
            $("#send").click();
        }
    });

    $('#averagecheckbox').click(function() {//點averagecheckbox即打開textarea
        if($("#averagecheckbox").prop("checked")){
            $("#textarea").prop("disabled",false);
        }
        else {
            $("#textarea").prop("disabled",true).val("");
        };
 
    });
}); 

