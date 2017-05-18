/**
 * Created by lyy on 2017-05-18.
 */

$(function(){
    loadKpfxx();
    loadHpxx();

});

//读取缓存表中的开票方信息
function loadKpfxx(){
      var obj =  localforage.getItem("kpfxx",function(err,value){
        if(value){
            var kpfxx =  value[0];
            var xf_nsrsbh =  kpfxx.xf_nsrsbh;
            var xf_nsrmc = kpfxx.xf_nsrmc;
            var xf_dzdh =  kpfxx.xf_dzdh;
            var xf_yhzh =  kpfxx.xf_yhzh;
            $("#xf_mc").val(xf_nsrmc);
            $("#xf_nsrsbh").val(xf_nsrsbh);
            $("#xf_dz").val(xf_dzdh);
            $("#xf_khzh").val(xf_yhzh);
        }
      });
}

//读取缓存货品信息并加载货品提示组件数据
function loadHpxx(){
    var hpxxmc = [];
    var obj =  localforage.getItem("hpxx",function(err,value){
        if(value){
            $.each(value,function(i,v){
                hpxxmc.push(v.sp_mc);
            });

        }
        $("#hwmc_1").autocomplete({
                source: hpxxmc,
                select:function (event,ui) {
                    $.each(value,function (i,v) {
                            if(v.sp_mc == ui.item.value){
                                        $("#svl_1").val(v.svl);
                                        return;
                            }
                    });
                }
        });
         $("#hwmc_2").autocomplete({
                source: hpxxmc,
                select:function (event,ui) {
                    $.each(value,function (i,v) {
                            if(v.sp_mc == ui.item.value){
                                        $("#svl_2").val(v.svl);
                                        return;
                            }
                    });
                }
        });
         $("#hwmc_3").autocomplete({
                source: hpxxmc,
                select:function (event,ui) {
                    $.each(value,function (i,v) {
                            if(v.sp_mc == ui.item.value){
                                        $("#svl_3").val(v.svl);
                                        return;
                            }
                    });
                }
        });
         $("#hwmc_4").autocomplete({
                source: hpxxmc,
                select:function (event,ui) {
                    $.each(value,function (i,v) {
                            if(v.sp_mc == ui.item.value){
                                        $("#svl_4").val(v.svl);
                                        return;
                            }
                    });
                }
        });
         $("#hwmc_5").autocomplete({
                source: hpxxmc,
                select:function (event,ui) {
                    $.each(value,function (i,v) {
                            if(v.sp_mc == ui.item.value){
                                        $("#svl_5").val(v.svl);
                                        return;
                            }
                    });
                }
        });
         $("#hwmc_6").autocomplete({
                source: hpxxmc,
                select:function (event,ui) {
                    $.each(value,function (i,v) {
                            if(v.sp_mc == ui.item.value){
                                        $("#svl_6").val(v.svl);
                                        return;
                            }
                    });
                }
        });
    });
}

//获取表单开票数据
function getKpsj(){
    var gf_mc =  $("#gf_mc").val(); //购方名称
    var gf_nsrsbh = $("#gf_nsrsbh").val(); //购方识别号
    var gf_dz =  $("#gf_dz").val(); //购方地址
    var gf_khzh = $("#gf_khzh").val(); //购方开户行
    var gf_ywdh = $("#gf_ywdh").val(); //购方业务单号
    var gf_lxrmc = $("#gf_lxrmc").val(); //购方联系人名称
    var gf_lxrdh = $("#gf_lxrdh").val(); //购方联系人电话
    var gf_email = $("#gf_email").val(); //购方联系人电子邮件

    var hwList = []; //货物列表
    /*发票明细*/
    for(var i = 1;i<=6;i++){
        var hwmc =  $("#hwmc_"+i).val(); //货物名称
        if(Trim(hwmc) == ""){
            break;
        }
        var ggxh =  $("#ggxh_"+i).val(); //规格型号
        var dw =  $("#dw_"+i).val(); //单位
        var sl =  $("#sl_"+i).val(); //数量
        var dj =  $("#dj_"+i).val(); //单价
        var je =  $("#je_"+i).val(); //金额
        var svl = $("#svl_"+i).val(); //税率
        var se =  $("#se_"+i).val();  //税额

        var hwxx =  {"hwmc":hwmc,"ggxh":ggxh,"dw":dw,"sl":sl,"dj":dj,"je":je,"svl":svl,"se":se};
        hwList.push(hwxx);

    }
    var hjje = $("#hjje").text(); //合计金额
    var hjse = $("#hjse").text(); //合计税额

    var xf_mc =  $("#xf_mc").val(); //销方名称
    var xf_nsrsbh= $("#xf_nsrsbh").val(); //销方纳税人识别号
    var xf_dz =  $("#xf_dz").val(); //销方地址
    var xf_khzh =  $("#xf_khzh").val(); //销方开户行
    var bz =  $("#bz").val(); //备注
    var skr = $("#skr").val(); //收款人
    var fhr = $("#fhr").val(); //复核人
    var kpr = $("#kpr").val(); //开票人

}

