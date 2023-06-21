from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import time
import pandas as pd
import CreateAsnXML
import ElementsDict
import CommonSelenMethods
from datetime import date


def get_date_and_time():
    date_stamp = date.today().strftime("%b-%d-%Y")
    time_stamp = time.strftime("%H-%M-%S", time.localtime())
    return date_stamp, time_stamp


def set_timeout():
    timeout = 240
    return timeout


def create_results_list():
    Steps = []
    Status = []
    return Steps, Status


def create_dict():
    dict_object = ElementsDict.ElementsDict()
    d = dict_object.create_dict()
    return d


def create_actions(driver):
    actions = ActionChains(driver)
    return actions


def create_driver():
    chromeOptions = Options()
    chromeOptions.add_experimental_option('detach', True)
    chromeOptions.add_argument('start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)
    return driver


def find_files(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    # for f in files:
    #     if f.find(filename) >= 0:
    #         print(root)
    #         print(f)
    # files = [x for x in os.listdir('C:/') if x.startswith(filename)]
    # newest = max(files, key=os.path.getctime)
    # print("Recently modified Docs", newest)


def get_login_param(sheet_name):
    login_params = pd.read_excel(r'C:\Users\ebu312q\Documents\login_param.xlsx', sheet_name)

    # [row][column] first row of excel file does not count
    # starts from 0 for row and column
    # change number values to change username and password - can change ///
    username = login_params.values[0][0]
    password = login_params.values[0][1]
    environ = login_params.values[0][2]

    return username, password, environ


# def get_data_param(username, personal_access_token, data_csv_url):
#     # username and personal access token for github private repo
#     github_session = requests.Session()
#     github_session.auth = (username, personal_access_token)
#
#     # providing raw url to download csv from github
#     download = github_session.get(data_csv_url).content
#     dataFile = pd.read_csv(io.StringIO(download.decode('utf-8')))
#
#     # [row][column] first row of excel file does not count
#     # starts from 0 for row and column
#     part_number = dataFile.values[0][0]
#     qty = dataFile.values[0][1]
#
#     return part_number, qty


def get_asns_from_file_one_line():
    asnFile = pd.read_csv(r'C:\Users\ebu312q\Documents\asns.csv')
    asn_long_text = ''

    for i in range(len(asnFile)):
        asn = asnFile.values[i][0]
        if i == 0:
            asn_long_text = asn
        else:
            asn_long_text = asn_long_text + ', ' + asn

    return asn_long_text


def create_asns(params_for_asns_file, num_of_asns):
    xml_first_part = '<?xml version="1.0" ?><tXML><Header><Source>Host</Source><Action_Type>create</Action_Type>' \
                     '<Message_Type>ASN</Message_Type><Company_ID>1</Company_ID></Header><Message>'
    xml_last_part = '</Message></tXML>'
    complete_asn_xml = xml_first_part
    asn_list = []

    for i in range(num_of_asns):
        asn_xml_object = CreateAsnXML.ASNxml(params_for_asns_file.values[i][0], params_for_asns_file.values[i][1])
        asn_xml = asn_xml_object.create_asn_xml()
        complete_asn_xml = complete_asn_xml + asn_xml
        asn = asn_xml_object.get_random_ASN_id()
        asn_list.append(asn)

    complete_asn_xml = complete_asn_xml + xml_last_part
    return complete_asn_xml, asn_list


def create_selen_object():
    # create main param to create object of MHMethodsClass - can change ///
    driver = create_driver()
    timeout = set_timeout()
    Steps, Status = create_results_list()
    d = create_dict()
    actions = create_actions(driver)

    selen_ob = CommonSelenMethods.SelenMethodsClass(driver, timeout, Steps, d, actions)
    return selen_ob, Status
