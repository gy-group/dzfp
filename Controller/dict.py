from flask import render_template
from flask import session,request,abort,Blueprint
import json
import pymysql

zdb =  Blueprint('zdb',__name__,template_folder='templates')

"""
    获取开票方所有货品信息
"""
@zdb.route('/getHpxx/<xfsbh>')
def getHpxx(xfsbh):

    conn = pymysql.connect(host='47.92.37.219', port=3306, user='root', passwd='13Yeyepaodecha',
                           db='dzfp',charset='utf8')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select sp_dm,sp_mc,sp_swdm,svl from T_FP_SPXX where xf_nsrsbh='{0}'".format(xfsbh)
    cur.execute(sql)
    rv = cur.fetchall()
    return json.dumps(rv)

"""
    获取开票方基本信息
"""
@zdb.route('/getKpfxx/<xfsbh>')
def getKpfxx(xfsbh):

    conn = pymysql.connect(host='47.92.37.219', port=3306, user='root', passwd='13Yeyepaodecha',
                           db='dzfp',charset='utf8')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select xf_nsrsbh,xf_nsrmc,xf_dzdh,xf_yhzh from T_FP_XFXX where xf_nsrsbh='{0}'".format(xfsbh)
    cur.execute(sql)
    rv = cur.fetchall()
    return json.dumps(rv)