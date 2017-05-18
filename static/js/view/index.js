/**
 * Created by lyy on 2017-05-18.
 */

$(function(){
    loadKpfxx("310115123456789");
    loadHpxx("310115123456789");
});

//获取开票方信息
function loadKpfxx(xfsbh){
    $.ajax({
                type:"get",
                dataType: "json",
                url:"/getKpfxx/"+xfsbh,
                success:function(data,status){
                       if(data){
                           var kpfxxDmb =  localforage.getItem("kpfxx",function (err,value) {
                                if(!value){
                                      localforage.setItem('kpfxx',data,function(err){

                                    });
                                }
                           });

                       }
                },
                error:function(){

                }


          });
}
//获取货品信息
function loadHpxx(xfsbh){
    $.ajax({
                type:"get",
                dataType: "json",
                url:"/getHpxx/"+xfsbh,
                success:function(data,status){
                       if(data){
                           var hpxxDmb =  localforage.getItem("hpxx",function (err,value) {
                                if(!value){
                                      localforage.setItem('hpxx',data,function(err){

                                    });
                                }
                           });

                       }
                },
                error:function(){

                }


          });
}