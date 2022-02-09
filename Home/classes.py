from os import link
import time
import mysql.connector
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

mydb = mysql.connector.connect(user = 'test',
                               host = 'localhost',
                              database = 'books',
                              password  = '9417079535bapu',
                                auth_plugin = 'mysql_native_password',)
print(mydb)

time.sleep(5)
mycursor = mydb.cursor()

# sql = "INSERT INTO officer (url, title) VALUES (%s, %s)"
# val = ("https://codewithharry.com", "data save")
# test = driver.find_element_by_tag_name("img")
# imgs = driver.find_element_by_tag_name('img').get_attribute("src")


# img = driver.find_element_by_xpath('//*[@id="__next"]/div[5]/section/div/div/div[1]/div/img')
# src = img.get_attribute('src')
driver.get("https://codewithharry.com/videos")
time.sleep(3)

# get_title = driver.title
# print(get_title)

main_content_div = driver.find_elements_by_class_name("rounded-2xl")

for content in main_content_div:
  img_tag = content.find_element_by_class_name('w-full')
  img_link = img_tag.get_attribute('src')
  course_tag = content.find_element_by_tag_name('a')
  course_link = course_tag.get_attribute('href')
  course_heading = course_tag.text


sql = "INSERT INTO class (url,links,title) VALUES (%s,%s,%s)"
val = (img_link,course_link,course_heading)
mycursor.execute(sql, val)




mydb.commit()

print(mycursor.rowcount, "record inserted.")




# for i in img:
#     imgs = i.find_element_by_tag_name('img')
#     src = imgs.get_attribute("src")

# print(src)


# likes = driver.find_elements_by_xpath("//*/div[5]/div[2]/div/div[1]/div/div[1]/div/a")
# print(likes,"likesssssssssssssssssss")
# time.sleep(5)
# for like in likes:
#   print(like)
#   p = like.get_attribute("title")
#   print(p)

  # title = i.find_element_by_class_name("text-lg")

  # titt_txt = title.text
  # get_title = i.find_element_by_tag_name('a')
    # print(get_title.text)

# lnks=driver.find_elements_by_tag_name("a")
# time.sleep(3)
# for lnk in lnks:

#   test = lnk.get_attribute('href')
#   print(test)

    

# get = driver.find_elements_by_xpath('//*/div[5]/div[2]/div/div[1]/div/div[1]/div/a')
# for i in get:
#   print(i.text)
  

# title = driver.find_elements_by_class_name("text-lg")
# time.sleep(3)
# for i in title:
#   get_title = i.find_element_by_tag_name('a')
#   print(get_title,'==============get_title')

#   print(get_title.text)
#   val = (src,test,get_title.text)
#   mycursor.execute(sql, val)

# time.sleep(5)


# mydb.commit()

# print(mycursor.rowcount, "record inserted.")




 

# driver.get("https://codewithharry.com/videos")


# test = driver.find_element_by_tag_name("img")

# img = driver.find_element_by_class_name("rounded-2xl")
# for x in img:
# imgs = img.find_element_by_tag_name('img').get_attribute("src")
# print(imgs)

#  print(img)

# img = test.get_attribute("src")

# print(img)
# 
# print(test)
# print(test.text)
# test = driver.find_element_by_xpath('//*[@id="wpcf7-f3838-o1"]/form/div[2]/span[1]/input')
# time.sleep(5)
# test.send_keys("test@gmail.com")
# time.sleep(5)
# print(test)


 