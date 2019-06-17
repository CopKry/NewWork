from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
import MySQLdb


def find_replay():
    js="var q=document.documentElement.scrollTop=1000"
    for x in range(0,50):
        driver.execute_script(js)
        time.sleep(5)
        if x==0:
            driver.execute_script(js)
            time.sleep(3)
            driver.find_element_by_xpath("//div[@class='hot-line']/span/a").click()
            time.sleep(3)
        comment_list=driver.find_elements_by_xpath("//div[@class='list-item reply-wrap ']")
        for comment in comment_list:
                try:
                    con=comment.find_element_by_xpath(".//div[@class='con ']")
                    info=con.find_element_by_xpath(".//div[@class='info']")
                    user=con.find_element_by_xpath(".//div[@class='user']/a[1]").text
                    reply=con.find_element_by_xpath(".//p[@class='text']").text
                    floor=info.find_element_by_xpath(".//span[@class='floor']").text
                    times=info.find_element_by_xpath(".//span[@class='time']").text
                    if reply!='':
                        print(user+"/"+reply+"/"+floor+"/"+times)
                        insql(user,reply,floor,times) 
                except:
                    continue
        next_page=driver.find_element_by_xpath("//a[@class='next']").click()


def insql(user,reply,floor,times):
    conn=MySQLdb.connect(host='localhost',user='root',passwd='admin',db='python',charset = "utf8")
    cur=conn.cursor()
    cur.execute('INSERT INTO bilibilireply_bilibili(user,reply,floor,time) VALUES("%s","%s","%s","%s")',(str(user),str(reply),str(floor),str(times)))
    
    cur.close()
    conn.commit()
    conn.close()


def run_search():
    js="var q=document.documentElement.scrollTop=1000"
    driver.find_element_by_css_selector('input.search-keyword').send_keys('一人之下')
    driver.execute_script(js)
    time.sleep(3)
    driver.find_element_by_xpath("//button[@class='search-submit']").click()


def in_object():
    js="var q=document.documentElement.scrollTop=300"
    driver.execute_script(js)
    wait=ui.WebDriverWait(driver,10)
    wait.until(lambda driver:driver.find_element_by_xpath("//div[@class='left-img']"))
    driver.find_element_by_xpath("//div[@class='left-img']").click()
    

def handles_next():
    handles=driver.window_handles
    driver.switch_to_window(handles[-1])


driver=webdriver.Firefox()
driver.get("https://www.bilibili.com/")
run_search()
handles_next()
in_object()
handles_next()
find_replay()
