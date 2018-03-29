$(document).ready(
    function(){

        var isShow = false;
        var login = $('div#login');
        var agree_container = $('#agree');
        var agreement = $('.agreement')
        var label = $('.checkbox label')
        var alert = $('.alert')

        function show(){
            agree_container.attr('class','col-sm-7');
            label.attr('class','label label-success');
            login.show();
            agreement.css('height','150px');
            isShow = true;
        };

        function hide(){
            agree_container.attr('class','col-sm-12');
            label.attr('class','label label-default');
            login.hide();
            agreement.css('height','');
            isShow = false;
        };

        function check(){
            var alertInfo = "";
            var rVal = true;
            if($("input[name='username'").val()===""){
                rVal = false;
                alertInfo += "用户名";
            }

            if($("input[name='password'").val()===""){
                if(rVal)
                    alertInfo += "密码";
                else
                    alertInfo +="和密码";
                rVal = false;
            }

            if(!rVal)
                alert(alertInfo);
             
        }

        if(!isShow){
            login.hide();
            console.log("hide");
        }

        agreement.load("/static/data/agreement.txt");

        $(".accept").change(function(){
            console.log("change");
            if(isShow){
                hide();
            }else{
                show();
            }
        })

        if(alert.length>0){
            $('.accept').attr('checked',true);
            show();

            $('.close').click(function(){
                alert.hide();
            })
        }

        // $('#register').click(function(){

        // })

    }
  
)

    