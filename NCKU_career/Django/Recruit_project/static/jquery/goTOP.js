

$(document).ready(function(){

    
    $(function(){//go top
        $("#gotop").click(function(){
            jQuery("html,body").animate({scrollTop:0},200);
        });
        $(window).scroll(function() {
            if ( $(this).scrollTop() > 300){
                $('#gotop').fadeIn("fast");
            } else {
                $('#gotop').stop().fadeOut("fast");
            }
        });

    });

    $(function(){//go top
        $("#refresh").click(function(){
            location.reload();
        });
        $(window).scroll(function() {
            if ( $(this).scrollTop() > 300){
                $('#refresh').fadeIn("fast");
            } else {
                $('#refresh').stop().fadeOut("fast");
            }
        });

    });

});