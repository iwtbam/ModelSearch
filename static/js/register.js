$(document).ready(
    function(){

        var isShow = false;
        var login = $('div#login');
        var agree_container = $('#agree');
        var agreement = $('.agreement')
        var label = $('.checkbox label')

        

        function show(){
            agree_container.attr('class','col-md-7');
            label.attr('class','label label-success');
            login.show();
            agreement.css('height','150px');
            isShow = true;
        };

        function hide(){
            agree_container.attr('class','col-md-12');
            label.attr('class','label label-default');
            login.hide();
            agreement.css('height','');
            isShow = false;
        };

        if(!isShow){
            login.hide();
            console.log("hide");
        }

        agreement.load("data/agreement.txt");

        $(".accept").change(function(){
            console.log("change");
            if(isShow){
                hide();
            }else{
                show();
            }
        })

        // agree_container.attr('class', 'col-md-1');
        // agree_container.hide();
    }
  
)

    