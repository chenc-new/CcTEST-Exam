#-*- coding: utf-8 -*-
#@File    : test_login.py
#@Time    : 2020/10/26 21:29
#@Author  : Cc
#@Email   : 498431861@qq.com
#@Software: PyCharm

import pytest
import os
from tools.ExcelDataCtl import get_excel_data
from lib.apiLib.login import Login
from lib.apiLib.msg import Msg



class TestMsg:
    #get_excel_data('1-登录模块','login')---[(),()]
    @pytest.mark.parametrize('inBody,expData',get_excel_data('3-查询模块','Job_query'))#数据驱动---如果自己开发--一定会写一个for
    def test_msg(self,inBody,expData):
        #2- 调用登录的接口代码
        inToken = Login().login({'username': 'admin', 'password': '123456'},getToken=True)
        res = Msg().add_msg(inToken,inBody)#获取响应数据---字典格式
        #3- 预期结果--excel里与实际结果对比
        assert res['msg'] == expData['msg']

if __name__ == '__main__':
    # 1- 框架执行后的结果数据  --alluredir
    pytest.main(['test_msg.py','-s','--alluredir','../report/tmp'])
    # 2- 使用allure  应用，去打开这个结果数据-并且 浏览器访问（使用火狐/谷歌--设置默认浏览器）
    os.system('allure serve ../report/tmp')