$(document).ready(function(){
     
    $(".upload_list_item").mouseover(function(){
      
       $(this).addClass("mouseover");

    });
    $(".upload_list_item").mouseout(function(){
      
        $(this).removeClass("mouseover");
 
     });

    $(".upload_list_item").click(function(){
          
        $(this).addClass("selected");
        $(this).siblings().removeClass("selected");

    })

});