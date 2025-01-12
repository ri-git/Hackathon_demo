from datetime import date

#import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re



baseUrl = 'https://moodle.iitd.ac.in/login/index.php'
locationChromeDriver ='../drivers/chromedriver'

entryno = input("enter your entry number: ")
pwd = input("enter your moodle password: ")
mclass= input("enter monday's class: ")
mstime= input("enter start time: ")
tclass= input("enter tuesday's class: ")
tstime= input("enter start time: ")
wclass= input("enter wednesday's class: ")
wstime= input("enter start time: ")
thclass= input("enter thursday's class: ")
thstime= input("enter start time: ")
fclass= input("enter friday's class: ")
fstime= input("enter start time: ")


drive = webdriver.Chrome(executable_path=locationChromeDriver)
drive.get(baseUrl)

search = drive.find_element_by_name('username')
search.send_keys(entryno)
spwd= drive.find_element_by_id('password')
spwd.send_keys(pwd)
#spwd.send_keys(Keys.RETURN)

text = drive.find_element_by_id('login').text
temp = re.findall(r'\d+', text)
res= list(map(int, temp))
if 'first' in text:
    ans = res[0]

if 'second' in text:
    ans = res[1]

if 'add' in text:
    ans = res[0] + res[1]

if 'subtract' in text:
    ans = res[0] - res[1]

cap = drive.find_element_by_name('valuepkg3')
cap.send_keys(ans)
cap.send_keys(Keys.RETURN)
time.sleep(2)
drive.find_element_by_link_text('3').click()


noc = 1
if date.today().weekday() == 0:
    print("MY BOT is checking MONDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        i=2
        for x in range(0, noc):
            if time.strftime('%H:%M') == mstime:
                if mclass == "COL100":
                    drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
                    drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                if mclass == "ELL101":
                    el=drive.find_element_by_xpath('//*[@id="course-info-container-11053"]/div/div[2]/h4/a')
                    drive.execute_script("scrollBy(0,-1000);")
                    time.sleep(3)
                    el.click()
                    drive.find_element_by_xpath('//*[@id="module-56737"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                else:
                    print("That wasn't expected")
                print("MY BOT : Its time for the class")
                #classjoin(day1, x, endclass)
                continue

if date.today().weekday() == 1:
    print("MY BOT is checking TUESDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        i=2
        for x in range(0, noc):
            if time.strftime('%H:%M') == tstime:
                if tclass == "COL100":
                    drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
                    drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                if tclass == "ELL101":
                    el=drive.find_element_by_xpath('//*[@id="course-info-container-11053"]/div/div[2]/h4/a')
                    drive.execute_script("scrollBy(0,-1000);")
                    time.sleep(3)
                    el.click()
                    drive.find_element_by_xpath('//*[@id="module-56737"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                else:
                    print("That wasn't expected")
                print("MY BOT : Its time for the class")
                #classjoin(day1, x, endclass)
                continue

if date.today().weekday() == 2:
    print("MY BOT is checking WEDNESDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        i=2
        for x in range(0, noc):
            if time.strftime('%H:%M') == wstime:
                if wclass == "COL100":
                    drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
                    drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                if wclass == "ELL101":
                    el=drive.find_element_by_xpath('//*[@id="course-info-container-11053"]/div/div[2]/h4/a')
                    drive.execute_script("scrollBy(0,-1000);")
                    time.sleep(3)
                    el.click()
                    drive.find_element_by_xpath('//*[@id="module-56737"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                else:
                    print("That wasn't expected")
                print("MY BOT : Its time for the class")
                #classjoin(day1, x, endclass)
                continue

if date.today().weekday() == 3:
    print("MY BOT is checking THURSDAY Timetable")
    i = 0
    while i <= 1:
        print("Looking for class...")
        i=2
        for x in range(0, noc):
            if time.strftime('%H:%M') == thstime:
                if thclass == "COL100":
                    drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
                    drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                if thclass == "ELL101":
                    el=drive.find_element_by_xpath('//*[@id="course-info-container-11053"]/div/div[2]/h4/a')
                    drive.execute_script("scrollBy(0,-1000);")
                    time.sleep(3)
                    el.click()
                    drive.find_element_by_xpath('//*[@id="module-56737"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                else:
                    print("That wasn't expected")
                print("MY BOT : Its time for the class")
                #classjoin(day1, x, endclass)
                continue

if date.today().weekday() == 4:
    print("MY BOT is checking FRIDAY Timetable")
    i = 0
    time.sleep(2)
    while i <= 1:
        print("Looking for class...")
        i=2
        for x in range(0, noc):
            print(time.strftime('%H:%M'))
            if time.strftime('%H:%M') == fstime:
                if fclass == "COL100":
                    drive.find_element_by_xpath('//*[@id="course-info-container-10887"]/div/div[2]/h4/a').click()
                    drive.find_element_by_xpath('//*[@id="module-56927"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                elif fclass == "ELL101":
                    el=drive.find_element_by_xpath('//*[@id="course-info-container-11053"]/div/div[2]/h4/a')
                    drive.execute_script("scrollBy(0,-1000);")
                    time.sleep(3)
                    el.click()
                    drive.find_element_by_xpath('//*[@id="module-56737"]/div/div/div[2]/div/a/span').click()
                    drive.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[2]/div/md-content/live-streaming-lectures/md-card/md-list/div[1]/div/div[2]/button/span').click()
                    time.sleep(7200)#duration of a class?
                    drive.switch_to.window(drive.window_handles[1])
                    drive.close()
                    drive.switch_to.window(drive.window_handles[0])
                    drive.find_element_by_xpath('//*[ @ id = "label_3_22"] / span').click()
                    drive.find_element_by_link_text('3').click()
                else:
                    print("That wasn't expected")
                print("MY BOT : Its time for the class")
                #classjoin(day1, x, endclass)
                continue

  while True: 
  
        # Checks whether a scheduled task is pending to run or not 
        schedule.run_pending() 
        time.sleep(1)               
                




































