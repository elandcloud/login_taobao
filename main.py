import unittest
import os
import req,gui_,login,file_,utils

# python.exe main.py -s

"""
如果成功，会打印如下信息：
=============================
cookies过期，删除cookies文件！
是否需要滑块验证：False
验证用户名密码成功，st码申请地址：https://passport.alibaba.com/mini_apply_st.js?site=0&token=1j8AxxxK_xxGO04FXxx&callback=callback
获取st码成功，st码：1qip-xxxx
登录淘宝成功，跳转链接：http://i.taobao.com/my_taobao.htm?nekot=xxxzAwMQ%3D%3D1xxx476965xxx
保存cookies文件成功！
"""

class main:
    def __init__(self):
        pass
    def start(self):
        header,param,err =gui_.Gui().copyHTMLPostLoop(name="login.jhtml")
        if err !=None:
            return err
        err=file_.write(utils.DATA_PATH,utils.DATA_PATH_HEADER,header)
        if err !=None:
            return err

        err=file_.write(utils.DATA_PATH,utils.DATA_PATH_PARAM,param)
        if err !=None:
            return err
        data=req.Req().readParamPost(param)
        ul = login.UsernameLogin(data["TPL_username"], data["ua"], data["TPL_password_2"])
        err=ul.login()
        if err !=None:
            return err
if __name__ == '__main__':
    err=main().start()
    if err != None:
        print(err)
    else:
        print("login success!")
    
