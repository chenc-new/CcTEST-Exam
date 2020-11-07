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
#1- 获取excel数据---请求体+预期结果
# resList = get_excel_data('1-登录模块','login')
#2- 数据传入接口代码--请求体
#3- 写入测试结果  pass/fail   预期结果与实际结果对比
# testData={'username': '20154084', 'password': '123456'}
#1- 登录的测试类
'''
从excel获取请求体/响应的预期结果
'''

class TestLogin:
    #get_excel_data('1-登录模块','login')---[(),()]
    @pytest.mark.parametrize('inBody,expData',get_excel_data('1-登录模块','login'))#数据驱动---如果自己开发--一定会写一个for
    def test_login(self,inBody,expData):
        #2- 调用登录的接口代码
        res = Login().login(inBody,getToken=False)#获取响应数据---字典格式
        #3- 预期结果--excel里与实际结果对比
        assert res['msg'] == expData['msg']



if __name__ == '__main__':
    #1- 框架执行后的结果数据  --alluredir
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    #2- 使用allure  应用，去打开这个结果数据-并且 浏览器访问（使用火狐/谷歌--设置默认浏览器）
    os.system('allure serve ../report/tmp')

    '''
    -s  控制台显示打印信息
    F ---断言失败
    E   有异常
    .  成功
    '''

