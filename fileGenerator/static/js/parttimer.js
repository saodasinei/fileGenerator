$(document).ready(function(){
    
    // edit parttimer
 $(".editParttimer").click(function(){
    var username = $(this).parent().siblings(".personName").text();
    $("#updateUsername").val(username);
 });

    // delete parttimer
  $(".deleteParttimer").click(function(){
       $("#id").val($(this).attr("data_id"));
   });
   $(".parttimerDeleteConfirm").click(function(){
      id = $("#id").val();
      console.log(id);
    $.ajax({
       method:"GET",
       url:'/file/manage/parttimer/delete/',
       data:{"id":id},
       success:function(res){
           location.reload();
          }
     });
   });




//    check form input
    $(":submit").click(function(){
        $(this).parent().addClass('was-validated');
    });



});