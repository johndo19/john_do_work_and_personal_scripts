import os
import sys

import pandas as pd
import CreateData
import ExportScriptResults
import os.path
from connection import connect


def enter_trans_code(selen_ob, code):
    selen_ob.type_keys_enter('ewm_menu_transaction_code_input_box', code, True)


def go_into_packspec_menu(selen_ob):
    enter_trans_code(selen_ob, '/n/scwm/packspec')
    selen_ob.click('ewm_packspec_sub_menu_options_arrow_2')
    selen_ob.click('ewm_packspec_sub_menu_product_option_text')


def go_into_mon_menu(selen_ob):
    enter_trans_code(selen_ob, '/n/scwm/mon')
    selen_ob.type_keys_enter('ewm_mon_menu_warehouse_no_input_box', 'D200', False)
    selen_ob.type_keys_enter('ewm_mon_menu_monitor_input_box', 'SAP', False)
    selen_ob.click('ewm_menu_execute_button')


def download_spreadsheet(selen_ob):
    selen_ob.click('ewm_mon_menu_export_button')
    selen_ob.wait(1)
    selen_ob.press_down(1)
    selen_ob.press_enter()
    selen_ob.wait(1)
    selen_ob.click('ewm_menu_continue_button')
    selen_ob.wait(1)
    selen_ob.clear_input_box('ewm_mon_menu_export_input_box')
    date_stamp, time_stamp = CreateData.get_date_and_time()
    file_name = date_stamp + '_' + time_stamp + '.xlsx'
    selen_ob.type_keys_enter('ewm_mon_menu_export_input_box', file_name, False)
    selen_ob.click('ewm_menu_download_button')

    download_folder = os.path.expanduser("~") + "/Downloads/"
    file_path = download_folder + file_name
    selen_ob.wait(8)

    return file_path


def find_last_index_from_excel_file(file_path):
    df = pd.read_excel(file_path, dtype=str)
    print('Found and set file to read\n')

    last_index = str(len(df.index) - 1)

    os.remove(file_path)
    return last_index


def read_value_from_element(selen_ob, element, post_info_list):
    if ('check_box' in element) or ('circle' in element):
        var = selen_ob.store_attribute_of_element(element, 'aria-checked')
        if var == 'true':
            var = 'checked'
        else:
            var = 'not checked'
    else:
        var = selen_ob.store_attribute_of_element(element, 'value')
    if var == '':
        var = 'blank'
    print(var)
    post_info_list.append(var)


def read_sap_packspec_data(selen_ob, part_number, post_info_list):
    selen_ob.clear_input_box('ewm_packspec_sub_menu_product_input_box')
    selen_ob.type_keys_enter('ewm_packspec_sub_menu_product_input_box', part_number, True)
    selen_ob.click('ewm_packspec_sub_menu_perform_search_button')

    # file_path = download_spreadsheet(selen_ob)
    # last_index = find_last_index_from_excel_file(file_path)

    selen_ob.wait(3)
    selen_ob.double_click_field_from_ewm_table('0', '0')

    selen_ob.set_timeout(8)
    if selen_ob.create_wait('ewm_menu_continue_button'):
        selen_ob.click('ewm_menu_continue_button')
    selen_ob.set_timeout(30)

    selen_ob.click('ewm_packspec_sub_menu_product_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_base_qty_field_input_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_length_input_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_width_input_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_height_input_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_vol_input_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_gross_weight_input_box', post_info_list)

    selen_ob.click('ewm_packspec_sub_menu_lvl_one_prod_pckging_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_target_qty_input_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_total_qty_input_box', post_info_list)

    pack_mat_1 = selen_ob.store_field_from_ewm_table('0', '1')
    print(pack_mat_1)
    post_info_list.append(pack_mat_1)

    selen_ob.click('ewm_packspec_sub_menu_wght_vol_dim_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_enter_weight_man_check_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_enter_vol_man_check_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_enter_dim_man_check_box', post_info_list)

    selen_ob.click('ewm_packspec_sub_menu_warehouse_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_external_step_input_box', post_info_list)

    selen_ob.click('ewm_packspec_sub_menu_rounding_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_min_pack_size_check_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_rnd_up_lim_input_box', post_info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_round_up_circle', post_info_list)

    selen_ob.click('ewm_packspec_sub_menu_lvl_three_stor_lvl_option')
    selen_ob.click('ewm_packspec_sub_menu_assigned_elements_option')

    pack_mat_2 = selen_ob.store_field_from_ewm_table('0', '1')
    print(pack_mat_2)
    post_info_list.append(pack_mat_2)

    selen_ob.click('ewm_menu_back_button')
    selen_ob.wait(4)


def read_uom_table(selen_ob, part_number, post_info_list):
    selen_ob.choose_node('7')
    selen_ob.choose_folder_option('ewm_mon_menu_warehouse_attribute_folder_option_', '1')
    selen_ob.type_keys_enter('ewm_mon_menu_product_input_box', part_number, False)
    selen_ob.click('ewm_menu_execute_button')
    selen_ob.double_click_field_from_ewm_table('0', '0')
    selen_ob.click('ewm_packspec_sub_menu_uom_option')

    not_found_qdy_row = True
    row_num = '0'
    while not_found_qdy_row:
        auom = selen_ob.store_field_from_ewm_table(row_num, '1')
        if auom == 'QDY':
            not_found_qdy_row = False
        else:
            row_num = int(row_num) + 1
            row_num = str(row_num)

    for column in range(9, 18):
        if column in [11, 13, 14]:
            continue
        var = selen_ob.store_field_from_ewm_table(row_num, str(column))
        print(var)
        post_info_list.append(var)


def enter_packspec_info(selen_ob, part_number):
    selen_ob.clear_input_box('packspec_menu_part_number_input_box')
    selen_ob.type_keys_enter('packspec_menu_part_number_input_box', part_number, True)
    selen_ob.click('packspec_menu_spec_view_button')
    selen_ob.click('packspec_menu_submit_button')

    # selen_ob.set_timeout(10)
    # if selen_ob.create_wait('packspec_menu_audit_override_button'):
    #     selen_ob.click('packspec_menu_audit_override_button')
    # selen_ob.set_timeout(30)


def main():
    # create Status list and main selen_ob object to call common methods on - don't change
    selen_ob, Status = CreateData.create_selen_object()
    print('Created main selen_ob object for testing\n')

    # create unique data param to pass into main selen_ob funct - can change ///
    environ = 'EWM_wd3'
    resource = 'EBU312Q'

    download_folder = os.path.expanduser("~") + "/Downloads/"
    packspec_testing_file_path = download_folder + 'packspec_testing.xlsx'
    pre_df = pd.read_excel(packspec_testing_file_path, sheet_name='Pre_Info', dtype=str)
    pre_df_length = len(pre_df.index)
    pre_temp_df = pre_df.loc[pre_df.isna().any(axis=1)].head(1)
    pre_df_row_to_start_index = pre_temp_df.index[0]

    post_df = pd.read_excel(packspec_testing_file_path, sheet_name='Post_Info', dtype=str)
    post_df_length = len(post_df.index)
    post_temp_df = post_df.loc[post_df.isna().any(axis=1)].head(1)
    post_df_row_to_start_index = post_temp_df.index[0]

    if (pre_df_row_to_start_index == post_df_row_to_start_index) and (pre_df_length == post_df_length):
        print("rows to start and length are the same")
    else:
        print("rows to start and length are not the same")
        sys.exit()

    pre_info_df = pd.DataFrame(columns=['Base Qty', 'Length', 'Width', 'Height', 'Vol.', 'Gross Wght', 'Target Qty',
                                        'Total Qty', 'Pack Mat 1', 'Enter Wght Man. Checked',
                                        'Enter Vol. Man. Checked', 'Enter Dim. Man. Checked', 'Ext. Step',
                                        'Min. Pack Size Checked', 'Rnd Up Lim.', 'Round Up Checked', 'Pack Mat 2',
                                        'UoM - Gross Weight', 'UoM - Net Weight', 'UoM - Vol.', 'UoM - Length',
                                        'UoM - Width', 'UoM - Height'])

    post_info_df = pd.DataFrame(columns=['Base Qty', 'Length', 'Width', 'Height', 'Vol.', 'Gross Wght', 'Target Qty',
                                         'Total Qty', 'Pack Mat 1', 'Enter Wght Man. Checked',
                                         'Enter Vol. Man. Checked', 'Enter Dim. Man. Checked', 'Ext. Step',
                                         'Min. Pack Size Checked', 'Rnd Up Lim.', 'Round Up Checked', 'Pack Mat 2',
                                         'UoM - Gross Weight', 'UoM - Net Weight', 'UoM - Vol.', 'UoM - Length',
                                         'UoM - Width', 'UoM - Height'])

    print('Set pre-parameters\n')

    try:
        # main function for interacting with selen_ob - change based on what funct want to do ///
        print('Beginning main script process\n')

        selen_ob.open_two_tabs_and_switch(
            "http://wd3app01.sap.johndeerecloud.com:8000/sap/bc/personas3/314_rel/mainapp/ClientBin/index.html",
            "https://packspecqual.tal.deere.com/packagingspec/PackagingSpec")

        num = 0
        for row in range(pre_df_row_to_start_index, pre_df_length):

            part_number = str(pre_df['Part Number'].iloc[row])
            pre_info_list = []
            post_info_list = []

            print("pre-info ===================")

            if num == 0:
                go_into_packspec_menu(selen_ob)
            else:
                enter_trans_code(selen_ob, '/n/scwm/packspec')
            read_sap_packspec_data(selen_ob, part_number, pre_info_list)

            if num == 0:
                go_into_mon_menu(selen_ob)
            else:
                enter_trans_code(selen_ob, '/n/scwm/mon')

            read_uom_table(selen_ob, part_number, pre_info_list)

            pre_info_df.loc[len(pre_info_df.index)] = pre_info_list

            selen_ob.switch_to_window_2()

            part_number = str(post_df['Part Number'].iloc[row])

            enter_packspec_info(selen_ob, part_number)

            selen_ob.switch_to_window_1()

            print("post-info ================")

            enter_trans_code(selen_ob, '/n/scwm/packspec')
            read_sap_packspec_data(selen_ob, part_number, post_info_list)

            enter_trans_code(selen_ob, '/n/scwm/mon')

            read_uom_table(selen_ob, part_number, post_info_list)

            post_info_df.loc[len(post_info_df.index)] = post_info_list

            num = num + 1
            print('end ========================')

    finally:
        # first setup for exporting script results, get time stamp, directory and screenshot paths - don't change
        time_stamp, directory_path = ExportScriptResults.export_setup()

        # create data dataframe based on what data you want to save and set a unique script results path - can change
        script_results_path = directory_path + r'/Packspec_Testing_Script Results at ' + time_stamp + '.xlsx'

        # export excel file for script results - don't change
        ExportScriptResults.create_and_export_excel_results(selen_ob, Status, time_stamp, pre_df, script_results_path)

        with pd.ExcelWriter(packspec_testing_file_path, mode="a", engine="openpyxl",
                            if_sheet_exists="overlay") as writer:
            pre_info_df.style.set_properties(**{'background-color': '#B4C6E7', 'color': 'black'}).to_excel \
                (writer, sheet_name="Pre_Info", header=False, startrow=pre_df_row_to_start_index + 1, startcol=1,
                 index=False)

        with pd.ExcelWriter(packspec_testing_file_path, mode="a", engine="openpyxl",
                            if_sheet_exists="overlay") as writer:
            post_info_df.style.set_properties(**{'background-color': '#C6E0B4', 'color': 'black'}).to_excel \
                (writer, sheet_name="Post_Info", header=False, startrow=post_df_row_to_start_index + 1, startcol=1,
                 index=False)

        # selen_ob.get_driver().quit()
        # print('Closed automated browser window\n')
        print('SCRIPT HAS FINISHED RUNNING\n')
        print('Exported results in excel file, please check in the Scripts Results folder in your C drive\n')
        print('Make sure to close the console window before running script again')


main()
