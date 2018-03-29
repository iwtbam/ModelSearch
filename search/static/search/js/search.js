$(document).ready(
    function(){
        
        word = $('#search_edt').attr('placeholder');
        count =parseInt($('.search_info span').text());
        source = 0
        start = 0
        num = 40

        SEARCH_URL = "/search/results/";

        String.prototype.format = function () {
            var args = [].slice.call(arguments);
            return this.replace(/(\{\d+\})/g, function (a){
                return args[+(a.substr(1,a.length-2))||0];
            });
        };


        function init(){

            $('li#source0 a').attr('href',SEARCH_URL+"?word="+word+"&source=0");
            $('li#source1 a').attr('href',SEARCH_URL+"?word="+word+"&source=1");
            $('li#source2 a').attr('href',SEARCH_URL+"?word="+word+"&source=2");
            $('li#source3 a').attr('href',SEARCH_URL+"?word="+word+"&source=3");
            $('li#source4 a').attr('href',SEARCH_URL+"?word="+word+"&source=4");

            var source = $('ul.nav-tabs').attr('tdsource');
            var selector = 'li#source'+source;
            $(selector).attr('class','active');
            console.log("init sucesss!")
        }
        
        $('#get_more').click(function(){

            if(start + num>count){
                start = count
                return;
            }
            start = start + num;
            console.log(start)

            $.get(SEARCH_URL, {'start':start,'word':word},
            function(ret){
                packages = ret['packages']
                for(var i = 0;packages.length;i++){
                    var package = packages[i]
                    var template = '<div class="display_item"> <a href={0}><img src="{1}"/></a><div class="info"><div class="title">{2}</div></div></div>'
                    var ele = template.format(package.url, package.img, package.name)
                    $('.search_content').append(ele)
                }
            })
        })


        init();
    }
)
