#test_demo.py
import pytest
import allure

from steps import step1, step2, step3


@allure.feature("用户管理模块")
class TestDemo():
    @allure.story("测试用例标题")
    @allure.issue("http://bug.html")
    @allure.testcase("http://testcase.html")
    def test_update(self):
        """测试更新接口"""
        print("测试更新接口")
        step1()
        step2()
        step3()

    @allure.story("测试用例标题1")
    @allure.issue("http://bug1.html")
    @allure.testcase("http://testcase1.html")
    def test_del(self):
        """测试删除接口"""
        print("测试删除接口")
        step1()
        step2()
        step3()


@allure.feature("商品管理模块")
class TestDemo1():
    @allure.story("测试用例标题")
    @allure.issue("http://bug.html")
    @allure.testcase("http://testcase.html")
    @allure.severity("blocker")
    def test_update(self):
        """测试更新接口"""
        print("测试更新接口")
        step1()
        step2()
        step3()

    @allure.story("测试用例标题1")
    @allure.issue("http://bug1.html")
    @allure.testcase("http://testcase1.html")
    @allure.severity("critical")
    def test_del(self):
        """测试删除接口"""
        print("测试删除接口")
        step1()
        step2()
        step3()