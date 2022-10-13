'''author: Shu YuTou Date:2022/10/11'''
from appium import webdriver
# 字典
#step1.设置终端的参数项
desired_caps={
	"platformName":"Android",
	"platformVersion":"7.1.2",
	"deviceName":"huawei",
	"appPackage":"com.tal.kaoyan",
	"appActivity":"com.tal.kaoyan.ui.activity.SplashActivity",
	"noReset":True
}

#step2.appium server进行启动、模拟器/真机能够被电脑识别到,即用adb命令进行连接：adb connect 127.0.0.1:62001 、adb devices
#step3.发送指令给到appium server
webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

