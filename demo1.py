'''author: Shu YuTou Date:2021/5/8'''
from appium import webdriver
#打开酷狗音乐
# webdriver.Remote('appium服务器地址'，手机配置相关信息)
'''配置手机相关信息'''
caseInfo={
	"platformName":"Android",   #测试平台 Android、ios 大小写都可以
	"platformVersion":"7.1.2",  #平台版本：设置  关于平板电脑  Android版本
	"deviceName":"1",           #设备名称  随便填写，但不能为空
	"appPackage":"com.kugou.android", #包名，即需要测试的软件名称
	"appActivity":".app.splash.SplashActivity",#应用名，界面名  先启动APP，再在cmd中输入‘adb shell dumpsys window | findstr mCurrentFocus’命令获取
	"noReset":True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',caseInfo)
