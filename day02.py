from appium import webdriver
import sys
# 字典
#step1.设置终端的参数项
desired_caps={
	"platformName":"Android",
	"platformVersion":"7.1.2",
	"deviceName":"huawei",
	"appPackage":"com.tencent.mobileqq",
	"appActivity":"com.tencent.mobileqq.activity.SplashActivity",
	"noReset":True
}
#step2.appium server进行启动、模拟器/真机能够被电脑识别到,即用adb命令进行连接：adb connect 127.0.0.1:62001 、adb devices
#step3.发送指令给到appium server
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# 等待  三大等待：1、强制等待；2、隐式等待；3、显示等待
driver.implicitly_wait(10)
# 元素定位方法1：通过resourceid属性定位 find_element_by_id 返回的是WebElement对象
el_login=driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
el_login.click()
# el_QQaccount=driver.find_element_by_id("com.tencent.mobileqq:id/egw")
# el_QQaccount.send_keys("2459981500")
# driver.implicitly_wait(10)

# el_passwd=driver.find_element_by_id("com.tencent.mobileqq:id/password")
# el_passwd.send_keys("13337961728zqjp-")

# #元素定位方法2：find_element_by_android_uiautomator
# driver.find_element_by_android_uiautomator('new UiSelector().text("输入密码")')
#
# # 组合定位：可以结合多个属性进行定位
# driver.find_element_by_android_uiautomator('new UiSelector().text("输入密码").resourceId("com.tencent.mobileqq:id/password")')


# 元素定位方法3：
el_passwd=driver.find_element_by_accessibility_id("密码 安全")
driver.implicitly_wait(50)
el_passwd.send_keys("123456")
# driver.find_element_by_xpath('')
# asdfkjkds#
