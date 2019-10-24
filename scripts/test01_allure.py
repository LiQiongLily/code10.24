"""
 用例优先级  级别：
				1). blocker：有妨碍的
				2). critical：紧要的
				3). normal：一般
				4). minor：次要
				5). trivial：不重要
			提示：以上级别使用时，必须大写！

"""

import allure

import pytest

# @allure.step(title="步骤")     只能修饰函数名，不能修饰函数体
# allure.attach("描述","原因")

class Test01:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)  #添加的用例级别
    @allure.step(title="执行登录操作")    #添加步骤
    def test01(self):
        allure.attach("失败原因：", "密码错误")  #添加描述
        print("test01 被执行")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="退出登录")
    def test02(self):
        allure.attach("成功：", "成功退出")

    @allure.step(title="登录")
    def test03(self):
        allure.attach("失败原因：", "断言失败")
        print("test03 被执行")
        assert False

    def test04(self):
        #获取失败截图
        with open("./image/01.jpg","rb") as f:
            allure.attach("失败截图",f.read(),allure.attach_type.JPG)

        pass

