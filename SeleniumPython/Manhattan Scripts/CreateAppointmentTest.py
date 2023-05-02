import os
import pandas as pd
import CreateData


def create_appointment_test(username, password, xmlVar, Asns, use_asns_from_file, driver, timeout, Steps, d):
    MHFunct.launch_manh(driver, 'devl')
    MHFunct.login(username, password, driver, timeout, Steps, d)

    if not use_asns_from_file:
        MHFunct.post_message_xml_and_verify(xmlVar, driver, timeout, Steps, d)

    MHFunct.search_menu('ASNs', driver, timeout, Steps, d)
    MHFunct.type_keys_enter(d['asns_menu_primary_fields_input_box'], 'ASN', True, driver, timeout, Steps)

    MHFunct.type_keys_enter(d['asns_menu_primary_fields_secondary_input_box'], Asns, True, driver, timeout, Steps)

    MHFunct.click(d['uni_apply_button'], driver, timeout, Steps)
    MHFunct.click(d['asns_menu_checkbox_all_button'], driver, timeout, Steps)

    MHFunct.click(d['uni_more_button'], driver, timeout, Steps)
    MHFunct.click(d['uni_create_appointment_button'], driver, timeout, Steps)

    MHFunct.switch_to_diff_iframe(d['schedule_appointment_menu_iframe'], driver, timeout, Steps)

    MHFunct.click(d['schedule_appointment_menu_dock_details_tab'], driver, timeout, Steps)

    MHFunct.type_keys_enter(d['schedule_appointment_menu_planned_dock_input_box'], 'SOUTH', True, driver, timeout, Steps)
    MHFunct.type_keys_enter(d['schedule_appointment_menu_planned_door_input_box'], '056', True, driver, timeout, Steps)
    MHFunct.click(d['schedule_appointment_menu_save_button'], driver, timeout, Steps)

    appointment_id = MHFunct.store_text_of_element(d['schedule_appointment_menu_appointment_id_field'], driver, timeout, Steps)
    appointment_type = MHFunct.store_text_of_element(d['schedule_appointment_menu_appointment_type_field'], driver, timeout, Steps)
    appointment_status = MHFunct.store_text_of_element(d['schedule_appointment_menu_appointment_status_field'], driver, timeout, Steps)

    MHFunct.switch_to_default_iframe(driver, Steps)
    MHFunct.logout(driver, timeout, Steps, d)

    return appointment_id, appointment_type, appointment_status


def main():
    driver = CreateData.create_driver()
    timeout = CreateData.set_timeout()
    Steps = CreateData.create_results_list()
    d = CreateData.create_dict()
    Steps, Status = CreateData.create_results_list()
    use_asns_from_file = True

    username, personal_access_token = CreateData.get_login_param('Github')
    part_number, qty = CreateData.get_data_param(username, personal_access_token, r'https://github.deere.com/raw'
                                                                                  r'/parts/manhattan-worksoftcertify'
                                                                                  r'/main/Input/data.csv')
    xmlVar, randomASNid = CreateData.create_xml(part_number, qty)

    if use_asns_from_file:
        Asns = CreateData.get_asns_from_file_one_line()
    else:
        Asns = randomASNid

    appointment_id = ''
    appointment_type = ''
    appointment_status = ''

    username, password = CreateData.get_login_param('Manhattan DEVL')

    try:
        appointment_id, appointment_type, appointment_status = \
            create_appointment_test(username, password, xmlVar, Asns, use_asns_from_file, driver, timeout, Steps, d)
    finally:
        date_stamp, time_stamp = CreateData.get_date_and_time()
        new_path = r'C:/Users/ebu312q/Documents/Selenium Script Results/Script Test Results for ' + date_stamp
        if not os.path.exists(new_path):
            os.makedirs(new_path)

        screenshot_path = r'C:/Users/ebu312q/Documents/Screenshots/screenshot_' + time_stamp + '.png'
        MHFunct.take_screenshot(driver, screenshot_path)

        for step in Steps:
            Status.append('PASSED')

        test_results = pd.DataFrame({'Steps': Steps, 'Status': Status})
        data = pd.DataFrame({'Part Number': [part_number], 'Qty': [qty], 'ASN': [randomASNid], 'Appointment ID':
            [appointment_id], 'Appointment Type': [appointment_type], 'Appointment Status': [appointment_status]})

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
