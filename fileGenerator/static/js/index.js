$(document).ready(function(){
    //  django ajax csrf
    var csrftoken = $.cookie('csrftoken');
    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
         return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
      }
    $.ajaxSetup({
       beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
       }
     }
    });
   //  django ajax csrf


 //  login



 //  fileupload
 $("#saveupload").click(function(){

       number = $('#number').text();
       file_id = $('.file_id');
       new_file = $('.new_file');

       var data = new Array();
       data.push(number);
       for (var i=0; i<file_id.length; i++){
           var arr = new Array();
           arr.push(file_id[i].innerText);
           arr.push(new_file[i].innerText);
           data.push(arr);
       }
       console.log(data);
//          console.log(file_id);
//          console.log(new_file);
//          console.log(number);
     $.ajax({
        method:"POST",
        url:'/file/upload/save/',
        port:8000,
        dataTYpe:'json',
        data:JSON.stringify(data),
        success:function(res){
          console.log("文案保存成功!");
          alert("文案保存成功！")
        }

     });
 });
 


//  uploadlist_content
 $(".h_edit").click(function(){
       upload_id = $(this).attr("data_id");
       console.log(upload_id);

       $.ajax({
       method:"GET",
       url:'/file/upload/content/',
       dataType:'json',
       data:{"id":upload_id},
       success:function(res){
           console.log("查询成功");
           console.log(res);
         
           
         }
       });
    });
    
    // uploadlist_delete
    $('.h_delete').click(function(){
         $("#id").val($(this).attr("data_id"));
    });

     $(".h_delete_confirm").click(function(){
         id = $("#id").val();
         console.log(id);
         $.ajax({
            method:"GET",
            url:'/file/upload/delete/',
            dataType:'json',
            data:{"id":id},
            success:function(res){
                location.reload();
               }
          });
      });


});