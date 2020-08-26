$(document).ready(function(){
     // 文案全选
     $("#fileall").click(function(){
        if($(".file-input").prop("checked") == false){
            $(".file-input").prop("checked","true")
        }else{
            $(".file-input").prop("checked","")
        }
    });

    // 人设全选
    $("#profileall").click(function(){
       if($(".profile-input").prop("checked") == false){
            $(".profile-input").prop("checked","true")
        }else{
            $(".profile-input").prop("checked","")
        }
    });
//       新文案全选
     $("#newfileall").on('click',function(){
        if($(".newfile-input").prop("checked") == false){
            $(".newfile-input").prop("checked","true")
        }else{
            $(".newfile-input").prop("checked","")
        }
     });


      //       django ajax csrf
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
      //       django ajax csrf



    // 获取选择的文案并生成新文案

    $("#newfile").click(function(){
       var files = $(".file-input:checked").parent().siblings("th");
       var profiles = $(".profile-input:checked").parent().siblings("th");
       var fileID = new Array();
       var profileID = new Array();
       var data = new Array();
//       console.log(files);
//       console.log(profiles);
       for (var i=0; i < files.length; i++){
           fileID.push(files[i].innerText);
       }
         for (var i=0; i < profiles.length; i++){
           profileID.push(profiles[i].innerText);
       }
       data.push(fileID);
       data.push(profileID);

       $.ajax({
       method:"POST",
       url:'/generate/',
       port: 8000,
       dataType:'json',
       data: JSON.stringify(data),
       success:function(res){
           console.log("新文案生成成功");
           $("#tbody").empty();
           for (i=0; i<res.length; i++){
               $("#tbody").append(
                "<tr>"
                +"<th scope='row'>"
                +(i+1)
                +"</th>"
                +"<td>"
                +res[i].file_template
                +"</td>"
                +"<td>"
                +res[i].profile_template
                +"</td>"
                +"<td>"
                +res[i].newfile_content
                +"</td>"
                +"<td><input class='newfile-input' name='newfile_"+(i+1)+"' type='checkbox'></td>"
                +"</tr>"
               )
           }
       },
       error:function(data, type, err){
           console.log("ajax错误类型" + type);
           console.log(err);
       }
       });

    })

//    保存

    $("#save").click(function(){
        var newfiles = $(".newfile-input:checked").parent().siblings();
         console.log(newfiles);



        $.ajax({
           method:"POST",
           url:'/savenewfile/',
           port:8000,
           dataType:'json',
           data:"1",
           success:function(res){
            console.log(("新文案保存成功"));

           },
           error:function(data, type, err){
              console.log("ajax错误类型" + type);
              console.log(err);
           }

        });


    })



});
