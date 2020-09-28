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
    $(".upload_list_item").mouseover(function(){
      
       $(this).addClass("mouseover");

    });
    $(".upload_list_item").mouseout(function(){
      
        $(this).removeClass("mouseover");
 
     });

    $(".upload_list_item").click(function(){
          
        $(this).addClass("selected");
        $(this).siblings().removeClass("selected");

    });



   

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
           method:"POSt",
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

    $(".upload_list_item").click(function(){
          upload_id = $(this).attr("id");
          console.log(upload_id);


          $.ajax({
          method:"GET",
          url:'/file/upload/content/',
          dataType:'json',
          data:{"id":upload_id},
          success:function(res){
              console.log(res);
              $("#tbody").empty();
              for(var i=0; i<res.length; i++){
              $("#tbody").append(
                   "<tr>"
                   +"<th scope='row'>"
                   +res[i].id
                   +"</th>"
                   +"<td>"
                   +res[i].template_id_id
                   +"</td>"
                   +"<td>"
                   +res[i].content
                   +"</td>"
                   +"<td>"
                   +res[i].status
                   +"</td>"
                   +"<td><a class='btn btn-primary' href=''>编辑</a></td>"
                   +"</tr>"
                 )

              }

          }

          });

    });


});