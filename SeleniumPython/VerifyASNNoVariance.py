import pandas as pd
import CreateData
import ExportScriptResults
import sys


def verify_ASN_no_variance(MH, environ, asn_list, asn_pass_list):
    MH.launch_manh(environ)
    if environ == 'DEVL':
        print('Please manually type in username and password to login within 30 seconds and wait\n')
        MH.wait(30)

    print('Logged in successfully\n')
    MH.search_menu('ASNs')
    MH.type_keys_enter('asns_menu_primary_fields_dropdown_box_1', 'ASN Status', True)
    MH.type_keys_enter('asns_menu_primary_fields_dropdown_box_3', 'Receiving Started', True)
    MH.click('uni_apply_button')
    print('Beginning loop to verify all asns from file\n')

    try:
        MH.set_timeout(10)
        MH.click('uni_no_data_to_display_field')
        asn_list.append("There were no asns in receiving started status to be verified")
        print('There were no asns in receiving started status to be verified\n')
        return asn_list, asn_pass_list
    except AttributeError:
        total_num_of_asns = int(MH.split_text(MH.store_text_of_element('asns_menu_total_num_of_asns_field'), 'of ', 1))
        print('There are ' + str(total_num_of_asns) + ' asns to verify\n')

    MH.set_timeout(30)
    finished = False
    checkbox_num = 1
    while not finished:
        MH.change_position_value_of_element('asns_menu_checkbox_button_', checkbox_num, ']')
        MH.click('asns_menu_checkbox_button_' + str(checkbox_num))
        MH.click('uni_more_button')
        MH.click('uni_verify_asn_button')
        MH.switch_to_diff_iframe('verify_asn_menu_iframe')

        total_num_of_items = int(
            MH.split_text(MH.store_text_of_element('verify_asn_menu_total_num_of_items'), 'of ', 1))
        print('There are ' + str(total_num_of_items) + ' items to verify\n')
        # num_of_pages = math.ceil(total_num_of_items / 20)
        # print('There are ' + str(num_of_pages) + ' pages')

        asn = MH.store_text_of_element('verify_asn_menu_asn_name')
        print(asn)

        if asn not in asn_list:
            asn_list.append(asn)

        row_num = 1
        found_variance = False
        for i in range(1, total_num_of_items):
            MH.change_position_value_of_element('verify_asn_menu_all_items_table_variance_field_', row_num)
            variance = MH.store_text_of_element('verify_asn_menu_all_items_table_variance_field_' + str(row_num))
            print(variance)
            if variance != 0:
                found_variance = True
                break
            else:
                row_num = row_num + 1
                if row_num == 21:
                    row_num = 20
                    MH.click('verify_asn_menu_page_next_button')

        if found_variance:
            print('VARIANCE FOUND')
            asn_pass_list.append('VARAINCE FOUND, ASN NOT VERIFIED')
            MH.switch_to_default_iframe()
            MH.close_num_window(2)
            MH.click('asns_menu_checkbox_button_' + str(checkbox_num))
            checkbox_num = checkbox_num + 1
            MH.change_position_value_of_element('asns_menu_checkbox_button_', checkbox_num, ']')
        else:
            print('NO VARIANCE')
            asn_pass_list.append('NO VARIANCE FOUND, ASN VERIFIED')
            MH.click('verify_asn_menu_verify_asn_button')

        sys.exit()




def main():
    # create Status list and main MH object to call common methods on - don't change
    MH, Status = CreateData.create_MH_object()
    print('Created main MH object for testing\n')
    # get username and password to login - can change based on what login you want
    # username, password, environ = CreateData.get_login_param('MH')

    # create unique data param to pass into main MH funct - can change ///
    environ = 'DEVL'
    print('Set environment to ' + environ + '\n')
    # asn_file = pd.read_excel(r'C:\update_trailer_reference_field_asns.xlsx', dtype=str)
    # print('Found and set file to import asns to modify\n')
    # file_length = len(asn_file)
    asn_list = []
    asn_pass_list = []
    print('Set pre-parameters\n')

    try:
        # main function for interacting with MH - change based on what funct want to do ///
        print('Beginning main script process\n')
        asn_list, asn_pass_list = verify_ASN_no_variance(MH, environ, asn_list, asn_pass_list)
    finally:
        # first setup for exporting script results, get time stamp, directory and screenshot paths - don't change
        time_stamp, directory_path = ExportScriptResults.export_setup()

        # create data dataframe based on what data you want to save and set a unique script results path - can change ///
        data = pd.DataFrame({'ASNs': asn_list, 'STATUS': asn_pass_list})
        script_results_path = directory_path + r'/Verify_ASN_No_Variance Results at ' + time_stamp + '.xlsx'

        # export excel file for script results - don't change
        ExportScriptResults.create_and_export_excel_results(MH, Status, time_stamp, data, script_results_path)
        # MH.get_driver().quit()
        # print('Closed automated browser window\n')
        print('FULL SCRIPT RUN SUCCESS')
        print('Exported results in excel file, please check for results for script and asns that have been verified\n')
        # print('If you want to run script again with new asns, please modify the asn file and run script again\n')
        print('If you commented out the driver quit step, make sure to close the automated broswer window before '
              'running script again')


main()
