from appium import webdriver
import time

settup = {}

settup['platformName'] = 'Android'
settup['deviceName'] = 'Samsung A50'
settup['appPackage'] = 'surplus.surplus_apps_customer'
settup['appActivity'] = 'surplus.surplus_apps_customer.MainActivity'
settup['autoGrantPermissions'] = 'true'
settup['autoAcceptAlerts'] = 'true'
settup['autoDismissAlerts'] = 'true'
settup['enablePerformanceLogging'] = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', settup)
time.sleep(10)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView').click()
# driver.find_element_by_id('com.android.systemui:id/notification_stack_scroller').click()
