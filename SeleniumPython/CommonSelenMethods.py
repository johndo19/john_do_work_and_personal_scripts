from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys

def_wait = 0.25


class SelenMethodsClass:

    def __init__(self, driver, timeout, Steps, d, actions):
        self.driver = driver
        self.timeout = timeout
        self.Steps = Steps
        self.d = d
        self.actions = actions
        self.Steps.append('Created main MH object with driver, timeout, steps list, and dictionary for testing')

    def get_driver(self):
        return self.driver

    def get_timeout(self):
        return self.timeout

    def get_Steps(self):
        return self.Steps

    def get_d(self):
        return self.d

    def set_driver(self, driver):
        self.driver = driver

    def set_timeout(self, timeout):
        self.timeout = timeout

    def set_Steps(self, Steps):
        self.Steps = Steps

    def set_d(self, d):
        self.d = d

    def launch_environ(self, environ):
        self.driver.delete_all_cookies()
        self.Steps.append('Deleted driver browser cookies successfully')
        if environ == 'DEVL':
            link = "https://partswmawsdevl.tal.deere.com"
        elif environ == 'PROD':
            link = "https://partssawm.deere.com"
        elif environ == 'QUAL':
            link = "https://partssawmawsqual.tal.deere.com"
        elif environ == 'EWM_wd3':
            link = "http://wd3app01.sap.johndeerecloud.com:8000/sap/bc/personas3/314_rel/mainapp/ClientBin/index.html"
        elif environ == 'EWM_wd3_rfui':
            link = "https://wd3.deere.com/sap/bc/se/m/index.html?sap-client=410&sap-language=EN&sap-ui-version=personas" \
                   "&~transaction=/SCWM/RFUI&sap-personas-flavor=0A4387A111571EEDADCE70994AF99B59"
        elif environ == 'EWM_qwd':
            link = "http://qwdapp01.sap.johndeerecloud.com:8000/sap/bc/personas3/314_rel/mainapp/ClientBin/index.html"
        elif environ == 'EWM_qwd_rfui':
            link = "https://qwd.deere.com/sap/bc/se/m/index.html?sap-client=410&sap-language=EN&sap-ui-version=personas" \
                   "&~transaction=/SCWM/RFUI&sap-personas-flavor=0A4387A111571EEDADCE70994AF99B59"
        elif environ == 'QUAL_Packspec':
            link = 'https://packspecqual.tal.deere.com/packagingspec/PackagingSpec'
        else:
            link = environ

        # open a new tab
        self.driver.execute_script("window.open('" + link + "');")
        # close the current, old tab
        self.driver.close()
        # get the handle of the new, recently opened tab
        window_name = self.driver.window_handles[0]
        # switch to the recently opened tab
        self.driver.switch_to.window(window_name=window_name)
        # self.driver.get(link)
        self.Steps.append('Driver retrieved environ: ' + environ + ' link successfully')

    def launch_link(self, link):
        self.driver.delete_all_cookies()
        self.Steps.append('Deleted driver browser cookies successfully')
        self.driver.get(link)
        self.Steps.append('Driver retrieved link: ' + link + ' link successfully')

    def open_two_tabs_and_switch(self, link_1, link_2):
        self.launch_link(link_1)
        self.driver.execute_script("window.open('" + link_2 + "');")
        window_name_1 = self.driver.window_handles[0]
        self.driver.switch_to.window(window_name=window_name_1)

    def switch_to_window_2(self):
        window_name_2 = self.driver.window_handles[1]
        self.driver.switch_to.window(window_name=window_name_2)

    def switch_to_window_1(self):
        window_name_1 = self.driver.window_handles[0]
        self.driver.switch_to.window(window_name=window_name_1)

    def take_screenshot(self, screenshot_path):
        self.driver.save_screenshot(screenshot_path)
        self.Steps.append('Took screenshot successfully')

    def login(self, username, password):
        # username = str(username)
        # password = str(password)
        self.type_keys_enter('username_input_box', username, True)
        self.type_keys_enter('password_input_box', password, True)
        self.Steps.append('Logged in successfully')

    def logout(self):
        self.click('user_profile_button')
        self.click('signout_button')
        self.Steps.append('Logged out successfully')

    def search_menu(self, phrase):
        self.click('search_menu')
        self.type_keys_enter('search_menu_input_box', phrase, True)
        self.Steps.append('Searched for menu: ' + phrase + ' menu successfully')

    def search_menu_going_down(self, phrase, num):
        self.click('search_menu')
        self.type_keys_enter('search_menu_input_box', phrase, False)
        self.press_down(num)
        self.press_enter()
        self.Steps.append('Searched for menu: ' + phrase + ' menu successfully')

    def close_num_window(self, num):
        self.click('windows_button')
        self.click('window_close_button_' + num)
        self.click('windows_button')
        self.Steps.append('Successfully closed window number: ' + num)

    def change_position_value_of_element(self, element_name, num):
        converted_list = list(self.d[element_name])
        converted_list[1] = converted_list[1] + num + ']'
        converted_tuple = tuple(converted_list)
        self.d[element_name + num] = converted_tuple
        self.Steps.append('Changed position value of element: ' + element_name)

    def create_wait(self, element_name):
        # self.wait(def_wait)
        element = self.d[element_name]
        try:
            create_wait = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element))
            self.Steps.append('Created wait object for element: ' + element_name)
            return create_wait
        except TimeoutException:
            self.Steps.append('Timed out trying to find element: ' + element_name)
            return False
        # self.wait(def_wait)

    def create_wait_2(self, element_name):
        # self.wait(def_wait)
        element = self.d[element_name]
        try:
            create_wait = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element))
            self.Steps.append('Created wait object for element: ' + element_name)
            return create_wait
        except TimeoutException:
            self.Steps.append('Timed out trying to find element: ' + element_name)
            return False
        # self.wait(def_wait)

    def wait(self, wait):
        time.sleep(wait)
        self.Steps.append('Waited ' + str(wait) + ' seconds successfully')

    def click(self, element_name):
        self.wait(def_wait)
        try:
            self.create_wait(element_name).click()
            self.Steps.append('Clicked on element: ' + element_name + ' successfully')
        except ElementClickInterceptedException:
            self.wait(5)
            self.create_wait(element_name).click()
            self.Steps.append('Bypassed ElementClickInterceptedException and Clicked on element: ' + element_name +
                              ' successfully')

        self.wait(def_wait)

    def double_click(self, element_name):
        self.wait(def_wait)
        try:
            self.actions.double_click(self.create_wait(element_name)).perform()
            self.Steps.append('Double clicked on element: ' + element_name + ' successfully')
        except ElementClickInterceptedException:
            self.wait(5)
            self.actions.double_click(self.create_wait(element_name)).perform()
            self.Steps.append(
                'Bypassed ElementClickInterceptedException and double clicked on element: ' + element_name +
                ' successfully')

        self.wait(def_wait)

    def click_and_enter(self, element_name):
        self.wait(def_wait)
        try:
            self.create_wait(element_name).click()
            self.Steps.append('Clicked on element: ' + element_name + ' successfully')
            self.wait(def_wait)
            self.create_wait(element_name).send_keys(Keys.ENTER)
            self.Steps.append('Pressed enter in element: ' + element_name + ' successfully')
        except ElementClickInterceptedException:
            self.wait(5)
            self.create_wait(element_name).click()
            self.Steps.append('Bypassed ElementClickInterceptedException and Clicked on element: ' + element_name +
                              ' successfully')
            self.wait(def_wait)
            self.create_wait(element_name).send_keys(Keys.ENTER)
            self.Steps.append('Pressed enter in element: ' + element_name + ' successfully')

        self.wait(def_wait)

    def type_keys_enter(self, element_name, phrase, enter):
        self.wait(def_wait)
        self.create_wait(element_name).send_keys(phrase)
        if enter:
            self.wait(def_wait)
            self.create_wait(element_name).send_keys(Keys.ENTER)

        self.Steps.append('Typed keys in element: ' + element_name + ' with phrase: ' + str(phrase) + ' successfully')
        self.wait(def_wait)

    def press_enter(self):
        self.wait(def_wait)
        self.actions.send_keys(Keys.ENTER).perform()
        self.Steps.append('Pressed enter successfully')

        self.wait(def_wait)

    def press_down(self, num):
        self.wait(def_wait)
        for i in range(num):
            self.actions.send_keys(Keys.ARROW_DOWN).perform()
            self.Steps.append('Pressed down successfully')
            self.wait(def_wait)

    def clear_input_box(self, element_name):
        self.wait(def_wait)
        self.create_wait(element_name).clear()
        self.Steps.append('Cleared element: ' + element_name + ' successfully')
        self.wait(def_wait)

    def switch_to_diff_iframe(self, iframe_name):
        self.wait(def_wait)
        iframe = self.d[iframe_name]
        WebDriverWait(self.driver, self.timeout).until(EC.frame_to_be_available_and_switch_to_it(iframe))
        self.Steps.append('Switched to iframe: ' + iframe_name + ' successfully')
        self.wait(def_wait)

    def switch_to_default_iframe(self):
        self.wait(def_wait)
        self.driver.switch_to.default_content()
        self.Steps.append('Switched to default iframe successfully')
        self.wait(def_wait)

    def store_text_of_element(self, element_name):
        self.wait(def_wait)
        text = str(self.create_wait(element_name).text)
        self.Steps.append('Stored text: ' + text + ' of element: ' + element_name + ' successfully')
        self.wait(def_wait)
        return text

    def store_attribute_of_element(self, element_name, attribute):
        self.wait(def_wait)
        text = str(self.create_wait_2(element_name).get_dom_attribute(attribute))
        self.Steps.append('Stored attribute: ' + text + ' of element: ' + element_name + ' successfully')
        self.wait(def_wait)
        return text

    def split_text(self, text, where_to_split, item_num):
        text = text.split(where_to_split)[item_num]
        self.Steps.append('Split text: ' + text + ' successfully')
        return text

    def verify_text_of_element(self, element_name, text):
        if self.store_text_of_element(element_name) == text:
            self.Steps.append('Verified that element: ' + element_name + ' had text: ' + text)
            return True
        else:
            self.Steps.append('Could not verify that element: ' + element_name + ' had text: ' + text)
            return False

    def verify_attribute_of_element(self, element_name, attribute, text):
        if self.store_attribute_of_element(element_name, attribute) == text:
            self.Steps.append('Verified that element: ' + element_name + ' had attribute: ' + text)
            return True
        else:
            self.Steps.append('Could not verify that element: ' + element_name + ' had attribute: ' + text)
            return False

    def store_field_from_ewm_table(self, row_num, col_num):
        self.get_d().update({'Table_Value': ((By.XPATH, '//td[contains(@id, "rows-row' + row_num + '-col' + col_num +
                                              '")]' + '/descendant::input[1]'))})
        self.Steps.append('Added table_Value to dictionary')
        return self.store_attribute_of_element('Table_Value', 'value')

    def click_field_from_ewm_table(self, row_num, col_num):
        self.get_d().update({'Table_Value': ((By.XPATH, '//td[contains(@id, "rows-row' + row_num + '-col' + col_num
                                              + '")]' + '/descendant::div[3][contains(@id, "content")]'))})
        self.Steps.append('Added table_Value to dictionary')
        self.click('Table_Value')

    def double_click_field_from_ewm_table(self, row_num, col_num):
        self.get_d().update({'Table_Value': ((By.XPATH, '//td[contains(@id, "rows-row' + row_num + '-col' + col_num
                                              + '")]' + '/descendant::div[3][contains(@id, "content")]'))})
        self.Steps.append('Added table_Value to dictionary')
        self.double_click('Table_Value')

    def choose_node(self, num):
        self.change_position_value_of_element('ewm_mon_menu_expand_node_', num)
        self.click('ewm_mon_menu_expand_node_' + num)
        self.Steps.append('Clicked node: ' + num)

    def choose_folder_option(self, element_name, num):
        self.change_position_value_of_element(element_name, num)
        self.double_click(element_name + num)
        self.Steps.append('Chose folder option: ' + element_name + num)

    def choose_pix_trans_type_and_code_options(self, trans_type, trans_code):
        self.get_d().update({'pix_trans_menu_saved_filter_submenu_trans_type_option': (By.XPATH, '(//option[@value="' +
                                                                                       trans_type + '"])[1]')})
        self.get_d().update({'pix_trans_menu_saved_filter_submenu_trans_code_option': (By.XPATH, '(//option[@value="' +
                                                                                       trans_type + ' ' +
                                                                                       trans_code + '"])[1]')})

        converted_list = list(self.d['pix_trans_menu_saved_filter_submenu_trans_type_option'])
        converted_list[1] = converted_list[1] + '//parent::select[1]'
        converted_tuple = tuple(converted_list)
        self.d['pix_trans_menu_saved_filter_submenu_trans_type_select_dropdown'] = converted_tuple

        converted_list = list(self.d['pix_trans_menu_saved_filter_submenu_trans_code_option'])
        converted_list[1] = converted_list[1] + '//parent::select[1]'
        converted_tuple = tuple(converted_list)
        self.d['pix_trans_menu_saved_filter_submenu_trans_code_select_dropdown'] = converted_tuple

        self.Steps.append('Added pix_trans_type_option, pix_trans_code_option, and select buttons  to dictionary')
        self.click('pix_trans_menu_saved_filter_submenu_trans_type_select_dropdown')
        self.click('pix_trans_menu_saved_filter_submenu_trans_type_option')
        self.click('pix_trans_menu_saved_filter_submenu_trans_code_select_dropdown')
        self.click('pix_trans_menu_saved_filter_submenu_trans_code_option')

    def read_mh_pix_trans_table(self, trans_num, status_list):
        displaying_num_string = self.store_text_of_element('pix_trans_menu_displaying_num_field')

        list_for_total_num = displaying_num_string.split(" of ", 1)
        list_for_second_num = list_for_total_num[0].split(" - ", 1)
        list_for_first_num = list_for_second_num[0].split("Displaying ", 1)
        total_num = int(list_for_total_num[1])
        second_num = int(list_for_second_num[1])
        first_num = int(list_for_first_num[1])

        found_row_with_trans_num = False

        if total_num != 0 and second_num != 0 and first_num != 0:
            while not found_row_with_trans_num:
                displaying_num_string = self.store_text_of_element('pix_trans_menu_displaying_num_field')

                list_for_total_num = displaying_num_string.split(" of ", 1)
                list_for_second_num = list_for_total_num[0].split(" - ", 1)
                list_for_first_num = list_for_second_num[0].split("Displaying ", 1)
                second_num = int(list_for_second_num[1])
                first_num = int(list_for_first_num[1])

                num_of_rows_now = (second_num - first_num) + 1

                print('Reading through ' + str(num_of_rows_now) + ' rows\n')

                for row in range(num_of_rows_now):
                    xpath_string = '//tr[@ondblclick=\"return doDefaultAction (\'dataForm:lview:dataTable:' + str(row) + \
                                   ':defaultactionbutton\');\"]'

                    self.d['pix_trans_menu_table_trans_num'] = (By.XPATH, xpath_string + '//descendant::td[3]//descendant::span[1]')
                    table_row_trans_num = self.store_text_of_element('pix_trans_menu_table_trans_num')

                    if trans_num == table_row_trans_num:
                        self.d['pix_trans_menu_table_trans_check_box'] = (By.XPATH, xpath_string + '//descendant::td[1]//descendant::input[1]')

                        self.click('pix_trans_menu_table_trans_check_box')
                        self.click('pix_trans_menu_resend_button')
                        self.set_timeout(10)
                        self.d['pix_trans_menu_table_trans_status'] = (By.XPATH, '//descendant::td[12]//descendant::span[text()="Unprocessed"][1]')
                        self.create_wait('pix_trans_menu_table_trans_status')
                        self.set_timeout(60)

                        status_list.append('PASSED: Found and resent pix trans num')
                        print('Found correct pix trans num and resent it\n')
                        found_row_with_trans_num = True
                        break

                if found_row_with_trans_num:
                    break
                elif 'changeTableClicked' in self.store_attribute_of_element('pix_trans_menu_table_next_button', 'onclick'):
                    self.click('pix_trans_menu_table_next_button')
                    self.wait(3)
                    print('Going into next set of table rows\n')
                else:
                    status_list.append('FAILED: Could not find pix trans num')
                    print('Could not find pix trans num\n')
                    break
        else:
            status_list.append("FAILED: No data found for pix trans num")
            print('No data found for this pix trans num\n')

        return status_list

    # def scroll(self, element_name):
    #     # self.driver.execute_script('window.scrollTo(0, ' + height + ')')
    #     # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #     self.actions.click_and_hold(element_name).perform()
    #     self.actions.move_by_offset(0, 100).perform()
    #     self.actions.release()

    def post_message_xml_and_verify(self, xmlVar):
        self.search_menu('Post Message')
        self.switch_to_diff_iframe('post_message_menu_iframe')
        self.type_keys_enter('post_message_menu_input_box', xmlVar, False)
        self.click('post_message_menu_send_button')
        results = self.store_text_of_element('post_message_menu_results')

        if results is not None and '<Error_Type>0</Error_Type>' in results:
            self.Steps.append('Post message posted successfully' + xmlVar)
            self.Steps.append(results)
        else:
            self.Steps.append('Found error in post message' + xmlVar)
            self.Steps.append(results)

        self.switch_to_default_iframe()
        self.close_num_window('1')

    def change_window_size(self, width, height):
        self.wait(def_wait)
        self.driver.set_window_size(width, height)
        self.wait(def_wait)
