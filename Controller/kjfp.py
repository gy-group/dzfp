from flask import render_template
from flask import session,request,abort,Blueprint
import json
from  datetime  import  *
import pymysql

kjfp =  Blueprint('kjfp',__name__,template_folder='templates')

@kjfp.route('/kpsq',methods=['GET', 'POST'])
def kpsq():

    try:
        conn = pymysql.connect(host='47.92.37.219', port=3306, user='root', passwd='13Yeyepaodecha',
                    db='dzfp', charset='utf8')
        cur = conn.cursor(pymysql.cursors.DictCursor)

        fpsj = json.loads(request.values.get("fpsj"))
        gf_mc = fpsj.get("gfmc")
        gf_nsrsbh = fpsj.get("gf_nsrsbh")
        gf_dz = fpsj.get("gf_dz")
        gf_khzh = fpsj.get("gf_khzh")
        gf_ywdh = fpsj.get("gf_ywdh")
        gf_lxrmc = fpsj.get("gf_lxrmc")
        gf_lxrdh = fpsj.get("gf_lxrdh")
        gf_email = fpsj.get("gf_email")
        hjje = fpsj.get("hjje")
        hjse = fpsj.get("hjse")
        xf_mc = fpsj.get("xf_mc")
        xf_nsrsbh = fpsj.get("xf_nsrsbh")
        xf_dz = fpsj.get("xf_dz")
        xf_khzh = fpsj.get("xf_khzh")
        bz = fpsj.get("bz")
        skr = fpsj.get("skr")
        fhr = fpsj.get("fhr")
        kpr = fpsj.get("kpr")
        hwxxList = fpsj.get("hwxx")

        for hwxx in hwxxList:
            hwmc = hwxx["hwmc"]
            ggxh = hwxx["ggxh"]
            dw = hwxx["dw"]
            sl = hwxx["sl"]
            dj = hwxx["dj"]
            je = hwxx["je"]
            svl = hwxx["svl"]
            se = hwxx["se"]
            sql = "insert into T_FP_FPXX_MX(YWDH,XF_NSRSBH,SP_MC,SP_SWDM,SP_DM,GG_XH,DW,SL,DJ,JE,SVL,SE) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}'" \
                  ",'{8}','{9}','{10}','{11}')".format(gf_ywdh, xf_nsrsbh, hwmc, "", "", ggxh, dw, sl, dj, je, svl, se)
            cur.execute(sql)
        kpsj = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fpxx_zb = "insert into T_FP_FPXX(XF_NSRSBH,GF_NSRSBH,YWDH,HSJE,SE,GF_MC,GF_DZDH,GF_YHZH,GF_LXRMC,GF_LXRDH,GF_LXRDZYJ,SKR,FHR,KPR,BZ,KPRQ,ZT) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}'," \
                  "'{14}','{15}','{16}')".format(xf_nsrsbh, gf_nsrsbh, gf_ywdh, hjje, se, gf_mc, gf_dz, gf_khzh,
                                                 gf_lxrmc, gf_lxrdh, gf_email, skr, fhr, kpr, bz, kpsj, '0')
        cur.execute(fpxx_zb)
        conn.commit()
    except Exception as e:
        cur.close()
        conn.rollback()
    return "开票申请成功！"


