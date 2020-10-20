
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

  // filter parttimer
  $(".filter").change(function(){
      var id = $(this).val();
      console.log(id);
      url = '/file/manage/review/filter/?id=' + id
      window.location.href = url;

  });
  // change status
  // change uploadList status
  $(".uploadListStatus").change(function(){
      var status = $(this).val();
      var id = $(this).parent().siblings(".itemId").attr('id');
      
      console.log(id);
      console.log(status);

      $.ajax({
        method:"GET",
        url:"/file/manage/review/status/",
        data:{'id':id, 'status':status},
        success:function(){
            console.log("修改成功");
        }
      })
  });


  //  change file status
  $(".uploadFileStatus").change(function(){
      var status = $(this).val();
      var id = $(this).parent().siblings(".fileId").attr('id');
      
      console.log(id);
      console.log(status);
      $.ajax({
        method:"GET",
        url:"/file/manage/review/content/status/",
        data:{'id':id, 'status':status},
        success:function(){
            console.log("修改成功");
        }
      })
  });

    
  // show upload file content 
  $(".edit").click(function(){
        var uploadId = $(this).parent().siblings(".itemId").attr("id");
        var profileId = $(this).parent().siblings(".profileId").attr("name");
        url = '/file/manage/review/content?id=' + uploadId + '&profile='+profileId
        window.location.href = url;        
  });

  
  

});