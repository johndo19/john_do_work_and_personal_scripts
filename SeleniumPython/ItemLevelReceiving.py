import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from datetime import date

use_asns_from_file = False

date = date.today().strftime("%b-%d-%Y")
time_stamp = time.strftime("%H-%M-%S", time.localtime())


def get_login_param():
    loginFile = pd.read_csv(r'C:\Users\ebu312q\Documents\username_password.csv')
    # [row][column] first row of excel file does not count
    # starts from 0 for row and column
    usernameVar = loginFile.values[0][0]
    passwordVar = loginFile.values[0][1]
    # print(usernameVar)
    # print(passwordVar)

    return usernameVar, passwordVar


def get_data():
    # user = 'EBU312Q'
    # pat = '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'
    #
    # github_session = requests.Session()
    # github_session.auth = (user, pat)
    #
    # # providing raw url to download csv from github
    # csv_url = 'https://github.deere.com/raw/parts/manhattan-worksoftcertify/main/Input/data.csv'
    #
    # download = github_session.get(csv_url).content
    #
    # downloaded_csv = pd.read_csv(io.StringIO(download.decode('utf-8')), error_bad_lines=False)

    dataFile = pd.read_csv(r'C:\Users\ebu312q\Documents\data.csv')
    # [row][column] first row of excel file does not count
    # starts from 0 for row and column
    part_number = dataFile.values[0][0]
    qty = dataFile.values[0][1]
    # part_number = downloaded_csv.values[0][0]
    # qty = downloaded_csv.values[0][1]

    return part_number, qty


def get_asns_from_file():
    asnFile = pd.read_csv(r'C:\Users\ebu312q\Documents\asns.csv')
    asn_long_text = ''

    for i in range(len(asnFile)):
        asn = asnFile.values[i][0]
        if i == 0:
            asn_long_text = asn
        else:
            asn_long_text = asn_long_text + ', ' + asn

    print('ASNs from file: ' + asn_long_text)
    print()

    return asn_long_text


def create_xml(part_number, qty):
    print('Creating xml...')
    print()
    xml_object = CreateXML.XML(part_number, qty)
    xmlVar = xml_object.createXML()
    randomASNid = xml_object.get_randomASNid()
    print('Randomly generated XML: ' + xmlVar)
    print()
    print('Randomly generated ASN: ' + randomASNid)
    print()

    return xmlVar, randomASNid


def launch_manh():
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.delete_all_cookies()
    driver.get('https://partswmawsdevl.tal.deere.com/')
    time.sleep(5)
    print(driver.title)
    print(driver.current_url)
    print()

    return driver


def logout(driver, Steps):
    user_profile_button = driver.find_element(By.XPATH, '//*[@id="button-1028-btnIconEl"]')
    user_profile_button.click()
    time.sleep(3)
    Steps.append('Clicked on user profile button')

    signout_button = driver.find_element(By.XPATH, '//*[text()="Sign out"]')
    signout_button.click()
    time.sleep(3)
    Steps.append('Clicked on signout button')


def create_appointment_test(usernameVar, passwordVar, driver, xmlVar, randomASNid, Steps):
    wait = WebDriverWait(driver, 20)

    username = (By.XPATH, '//input[@type="text" and @name="username" and @id="okta-signin-username"]')
    wait.until(EC.presence_of_element_located(username)).send_keys(usernameVar + Keys.ENTER)
    Steps.append('Entered in username and pressed enter')

    password = (By.XPATH, '//input[@type="password" and @name="password" and @id="input62"]')
    wait.until(EC.presence_of_element_located(password)).send_keys(passwordVar + Keys.ENTER)
    Steps.append('Entered in password and pressed enter')
    time.sleep(20)

    three_bars = (By.XPATH, '//*[@id="button-1013-btnIconEl" and @data-ref="btnIconEl"]')


    if not use_asns_from_file:
        wait.until(EC.presence_of_element_located(three_bars)).click()
        Steps.append('Clicked on three bars')
        time.sleep(3)

        search_menu = driver.find_element(By.XPATH,
                                          '//input[@type="text" and @role="combobox" and @data-ref="inputEl" and '
                                          '@id="mps_menusearch-1084-inputEl"]')
        search_menu.click()
        search_menu.send_keys('Post Message')
        search_menu.send_keys(Keys.ENTER)
        time.sleep(5)
        Steps.append('Entered in post message in search menu')

        post_message_iframe = (By.XPATH, '//iframe[contains(@src, "PostTestMessage")]')
        wait.until(EC.frame_to_be_available_and_switch_to_it(post_message_iframe))
        print('Switched to post message iframe successfully...')
        print()
        Steps.append('Switched to post message iframe')
        post_message = driver.find_element(By.XPATH,
                                           '//textarea[@id="dataForm:xmlString" and @name="dataForm:xmlString" '
                                           'and @class="textareaStyle"]')
        post_message.click()
        post_message.send_keys(xmlVar)
        time.sleep(3)
        Steps.append('Entered in xml into post message')

        send_button = driver.find_element(By.XPATH, '//input[@id="dataForm:postMessageCmdId"]')
        send_button.click()
        time.sleep(3)
        Steps.append('Clicked send in post message ui')

    driver.switch_to.default_content()

    asn_long_text = get_asns_from_file()

    wait.until(EC.presence_of_element_located(three_bars)).click()
    time.sleep(3)
    Steps.append('Clicked on three bars')

    search_menu = (By.XPATH, '//input[@type="text" and @role="combobox" and @data-ref="inputEl" and '
                                                '@id="mps_menusearch-1084-inputEl"]')
    wait.until(EC.presence_of_element_located(search_menu)).click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located(search_menu)).send_keys('Asns')
    time.sleep(1)
    wait.until(EC.presence_of_element_located(search_menu)).send_keys(Keys.ENTER)
    time.sleep(12)
    Steps.append('Entered in Asns in search menu')



    driver.switch_to.default_content()
    logout(driver, Steps)
    Steps.append('FULL SCRIPT RUN')


def main():
    Steps = []
    Status = []

    part_number, qty = get_data()

    appointment_id = ''
    appointment_type = ''
    appointment_status = ''

    xmlVar, randomASNid = create_xml(part_number, qty)

    usernameVar, passwordVar = get_login_param()
    driver = launch_manh()

    try:
        appointment_id, appointment_type, appointment_status = \
            create_appointment_test(usernameVar, passwordVar, driver, xmlVar, randomASNid, Steps)
    finally:
        new_path = r'C:/Users/ebu312q/Documents/Selenium Script Results/Script Test Results for ' + date
        if not os.path.exists(new_path):
            os.makedirs(new_path)

        screenshot_path = r'C:/Users/ebu312q/Documents/Screenshots/screenshot_' + time_stamp + '.png'
        driver.save_screenshot(screenshot_path)

        for step in Steps:
            Status.append('PASSED')

        test_results = pd.DataFrame({'Steps': Steps, 'Status': Status})
        data = pd.DataFrame({'Part Number': [part_number], 'Qty': [qty], 'ASN': [randomASNid], 'Appointment ID':
            [appointment_id], 'Appointment Type': [appointment_type], 'Appointment Status':
                                 [appointment_status]})

        screenshot = pd.DataFrame({'Screenshot': ['Last screen shown', '-->']})

        sheets = {'Test Results': test_results, 'Data': data, 'Screenshot': screenshot}
        test_results_path = new_path + r'/CreateAppointmentTest Results at ' + time_stamp + '.xlsx'
        writer = pd.ExcelWriter(test_results_path, engine='xlsxwriter')

        for sheet_name in sheets.keys():
            sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

        worksheet = writer.sheets['Screenshot']
        worksheet.insert_image('B1', screenshot_path)
        writer.save()
        driver.quit()


main()
