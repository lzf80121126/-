from time import sleep

from appium import webdriver

# 建立字典
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 必填-且正确
desired_caps['platformName'] = 'Android'
# 必填-且正确
desired_caps['platformVersion'] = '6.0.1'
# 必填
desired_caps['deviceName'] = '192.168.41.37:7555'
# APP包名
desired_caps['appPackage'] = 'com.android.settings'
# 启动名
desired_caps['appActivity'] = '.Settings'
# 创建安卓实例
driver = webdriver.Remote("http://192.168.41.37:4723/wd/hub", desired_caps)
"""
 从存储滑到更多
"""
# start = driver.find_element_by_xpath("//*[contains(@text, '应用')]")
# end = driver.find_element_by_xpath("//*[contains(@text, 'WL')]")
# 滑动(基于坐标)
# driver.swipe(start.get("x"),start.get("y"),end.get("x"),end.get("y"))

# 滚动条滚动(一滑到底)
# driver.scroll(start,end)

# 拖拽(精准元素定位)*常用
# driver.drag_and_drop(start,end)

# 启动后置于后台10s
# driver.background_app(10)


"""
TouchAction类 高级手势操作
"""
# 轻敲
# TouchAction(driver).tap(end).perform()

"""
手机设备操作
"""
# 获取手机设备时间
print(driver.device_time)
print(driver.get_window_size())

sleep(5)
driver.quit()

