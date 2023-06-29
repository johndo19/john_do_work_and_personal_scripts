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


def read_value_from_element(selen_ob, element, info_list):
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
    info_list.append(var)


def read_sap_packspec_data(selen_ob, part_number, info_list):
    selen_ob.clear_input_box('ewm_packspec_sub_menu_product_input_box')
    selen_ob.type_keys_enter('ewm_packspec_sub_menu_product_input_box', part_number, True)
    selen_ob.click('ewm_packspec_sub_menu_perform_search_button')

    file_path = download_spreadsheet(selen_ob)
    last_index = find_last_index_from_excel_file(file_path)

    selen_ob.wait(3)
    date = selen_ob.store_field_from_ewm_table(last_index, '6')
    info_list.append(date)
    selen_ob.double_click_field_from_ewm_table(last_index, '0')

    selen_ob.set_timeout(8)
    if selen_ob.create_wait('ewm_menu_continue_button'):
        selen_ob.click('ewm_menu_continue_button')
    selen_ob.set_timeout(30)

    selen_ob.click('ewm_packspec_sub_menu_product_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_base_qty_field_input_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_length_input_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_width_input_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_height_input_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_vol_input_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_gross_weight_input_box', info_list)

    selen_ob.click('ewm_packspec_sub_menu_lvl_one_prod_pckging_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_target_qty_input_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_total_qty_input_box', info_list)

    pack_mat_1 = selen_ob.store_field_from_ewm_table('0', '1')
    print(pack_mat_1)
    info_list.append(pack_mat_1)

    selen_ob.click('ewm_packspec_sub_menu_wght_vol_dim_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_enter_weight_man_check_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_enter_vol_man_check_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_enter_dim_man_check_box', info_list)

    selen_ob.click('ewm_packspec_sub_menu_warehouse_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_external_step_input_box', info_list)

    selen_ob.click('ewm_packspec_sub_menu_rounding_option')

    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_min_pack_size_check_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_rnd_up_lim_input_box', info_list)
    read_value_from_element(selen_ob, 'ewm_packspec_sub_menu_round_up_circle', info_list)

    selen_ob.click('ewm_packspec_sub_menu_lvl_three_stor_lvl_option')
    selen_ob.click('ewm_packspec_sub_menu_assigned_elements_option')

    pack_mat_2 = selen_ob.store_field_from_ewm_table('0', '1')
    print(pack_mat_2)
    info_list.append(pack_mat_2)

    selen_ob.click('ewm_menu_back_button')
    selen_ob.wait(4)


def read_uom_table(selen_ob, part_number, post_info_list):
    selen_ob.choose_node('7')
    selen_ob.choose_folder_option('ewm_mon_menu_warehouse_attribute_folder_option_', '1')
    selen_ob.type_keys_enter('ewm_mon_menu_product_input_box', part_number, False)
    selen_ob.click('ewm_menu_execute_button')

    selen_ob.set_timeout(5)
    try:
        selen_ob.click('ewm_menu_continue_button')
    except AttributeError:
        selen_ob.set_timeout(30)

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


def choose_packspec_dropdown_option(selen_ob, element_name, choice):
    selen_ob.clear_input_box(element_name)
    selen_ob.type_keys_enter(element_name, choice, False)
    selen_ob.press_down(1)
    selen_ob.press_enter()


def enter_packspec_info(selen_ob, part_number, pkg_num):
    selen_ob.clear_input_box('packspec_menu_part_number_input_box')
    selen_ob.type_keys_enter('packspec_menu_part_number_input_box', part_number, True)
    selen_ob.click('packspec_menu_spec_view_button')

    choose_packspec_dropdown_option(selen_ob, 'packspec_menu_category_dropdown_input_box', '55 - ')
    choose_packspec_dropdown_option(selen_ob, 'packspec_menu_sub_category_dropdown_input_box', '55611 - ')
    choose_packspec_dropdown_option(selen_ob, 'packspec_menu_pack_bom_dropdown_input_box', 'O - ')

    selen_ob.delete_all_rows_in_pkg_bom_table()

    choose_packspec_dropdown_option(selen_ob, 'packspec_menu_uti_flex_dropdown_input_box', 'Show All')

    selen_ob.type_keys_enter('packspec_menu_pkg_num_table_input_box', pkg_num, True)
    selen_ob.choose_first_pkg_num_table_value(pkg_num)

    choose_packspec_dropdown_option(selen_ob, 'packspec_menu_dimensions_of_dropdown_input_box', 'DI - ')
    choose_packspec_dropdown_option(selen_ob, 'packspec_menu_dfc_dropdown_input_box', '00 - ')

    selen_ob.delete_all_rows_in_finished_cont_table()

    choose_packspec_dropdown_option(selen_ob, 'packspec_menu_finished_cont_dropdown_input_box', 'W - ')

    selen_ob.click('packspec_menu_submit_button')
    selen_ob.wait(12)


def read_rt3_data(part_number):
    session = connect('RT3')
    session.findById("wnd[0]/tbar[0]/okcd").text = "mm03"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = part_number
    session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").caretPosition = 6
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[1]/usr/tblSAPLMGMMTC_VIEW").getAbsoluteRow(0).selected = True
    session.findById("wnd[1]/tbar[0]/btn[0]").press()
    session.findById("wnd[0]/tbar[1]/btn[30]").press()
    session.findById("wnd[0]/usr/tabsTABSPR1/tabpZU03").select()

    not_found_qdy_row = True
    row = 0
    while not_found_qdy_row:
        auom = session.findById(
            "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
            "/ctxtSMEINH-MEINH[1," + str(row) + "]").text
        if auom == 'QDY':
            not_found_qdy_row = False
        else:
            row = row + 1

    row = str(row)

    length = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtSMEINH-LAENG[11," + row + "]").text
    width = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtSMEINH-BREIT[12," + row + "]").text
    height = session.findById(
        "wnd[0]/usr/tabsTABSPR1/tabpZU03/ssubTABFRA1:SAPLMGMM:2110/subSUB2:SAPLMGD1:8020/tblSAPLMGD1TC_ME_8020"
        "/txtSMEINH-HOEHE[13," + row + "]").text

    print(length)
    print(width)
    print(height)

    session.findbyid("wnd[0]").close()
    session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()


def main():
    # create Status list and main selen_ob object to call common methods on - don't change
    selen_ob, Status = CreateData.create_selen_object()
    print('Created main selen_ob object for testing\n')

    # create unique data param to pass into main selen_ob funct - can change ///
    environ = 'EWM_wd3'
    resource = 'EBU312Q'

    download_folder = os.path.expanduser("~") + "/Downloads/"
    packspec_testing_file_path = download_folder + 'packspec_testing.xlsx'
    pre_info_df = pd.read_excel(packspec_testing_file_path, sheet_name='Pre_Info', dtype=str)
    post_info_df = pd.read_excel(packspec_testing_file_path, sheet_name='Post_Info', dtype=str)
    full_info_df = pd.concat([pre_info_df, post_info_df], axis=1)

    length = len(full_info_df.index)
    temp_df = full_info_df.loc[full_info_df.isna().any(axis=1)].head(1)
    row_to_start_index = temp_df.index[0]

    is_post_base_qty_cell_empty = pd.isna(temp_df['Base Qty'].iloc[:, 1].iloc[0])
    is_pre_base_qty_cell_filled = not (pd.isna(temp_df['Base Qty'].iloc[:, 0].iloc[0]))
    is_post_df_blank = is_post_base_qty_cell_empty and is_pre_base_qty_cell_filled

    pre_info_df = pd.DataFrame(columns=['Date', 'Base Qty', 'Length', 'Width', 'Height', 'Vol.', 'Gross Wght', 'Target Qty',
                                        'Total Qty', 'Pack Mat 1', 'Enter Wght Man. Checked',
                                        'Enter Vol. Man. Checked', 'Enter Dim. Man. Checked', 'Ext. Step',
                                        'Min. Pack Size Checked', 'Rnd Up Lim.', 'Round Up Checked', 'Pack Mat 2',
                                        'UoM - Gross Weight', 'UoM - Net Weight', 'UoM - Vol.', 'UoM - Length',
                                        'UoM - Width', 'UoM - Height'])

    post_info_df = pd.DataFrame(columns=['Date', 'Base Qty', 'Length', 'Width', 'Height', 'Vol.', 'Gross Wght', 'Target Qty',
                                         'Total Qty', 'Pack Mat 1', 'Enter Wght Man. Checked',
                                         'Enter Vol. Man. Checked', 'Enter Dim. Man. Checked', 'Ext. Step',
                                         'Min. Pack Size Checked', 'Rnd Up Lim.', 'Round Up Checked', 'Pack Mat 2',
                                         'UoM - Gross Weight', 'UoM - Net Weight', 'UoM - Vol.', 'UoM - Length',
                                         'UoM - Width', 'UoM - Height', 'Data Updated'])

    print('Set pre-parameters\n')

    try:
        # main function for interacting with selen_ob - change based on what funct want to do ///
        print('Beginning main script process\n')

        selen_ob.open_two_tabs_and_switch(
            "http://wd3app01.sap.johndeerecloud.com:8000/sap/bc/personas3/314_rel/mainapp/ClientBin/index.html",
            "https://packspecqual.tal.deere.com/packagingspec/PackagingSpec")

        num = 0
        for row in range(row_to_start_index, length):
            if not (is_post_df_blank is True and num == 0):
                part_number = str(full_info_df['Part Number'].iloc[:, 0].iloc[row])
                pkg_num = str(full_info_df['Pkg Num'].iloc[:, 0].iloc[row])
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

                enter_packspec_info(selen_ob, part_number, pkg_num)

                selen_ob.switch_to_window_1()

                print("post-info ================")

                enter_trans_code(selen_ob, '/n/scwm/packspec')
                read_sap_packspec_data(selen_ob, part_number, post_info_list)
                enter_trans_code(selen_ob, '/n/scwm/mon')
                read_uom_table(selen_ob, part_number, post_info_list)

                if pre_info_list[0] != post_info_list[0]:
                    post_info_list.append('Yes')
                else:
                    post_info_list.append('No')
                post_info_df.loc[len(post_info_df.index)] = post_info_list

                read_rt3_data(part_number)

                num = num + 1
                print('end ========================')

            else:
                part_number = str(full_info_df['Part Number'].iloc[:, 0].iloc[row])
                pkg_num = str(full_info_df['Pkg Num'].iloc[:, 0].iloc[row])
                post_info_list = []

                selen_ob.wait(10)
                selen_ob.switch_to_window_2()

                enter_packspec_info(selen_ob, part_number, pkg_num)

                selen_ob.switch_to_window_1()

                print("post-info ================")

                go_into_packspec_menu(selen_ob)
                read_sap_packspec_data(selen_ob, part_number, post_info_list)
                go_into_mon_menu(selen_ob)
                read_uom_table(selen_ob, part_number, post_info_list)

                before_change_date = str(full_info_df['Date'].iloc[:, 0].iloc[row])
                if before_change_date != post_info_list[0]:
                    post_info_list.append('Yes')
                else:
                    post_info_list.append('No')
                post_info_df.loc[len(post_info_df.index)] = post_info_list

                read_rt3_data(part_number)

                num = num + 1
                print('end ========================')

    finally:
        # first setup for exporting script results, get time stamp, directory and screenshot paths - don't change
        time_stamp, directory_path = ExportScriptResults.export_setup()

        # create data dataframe based on what data you want to save and set a unique script results path - can change
        script_results_path = directory_path + r'/Packspec_Testing_Script Results at ' + time_stamp + '.xlsx'

        # export excel file for script results - don't change
        ExportScriptResults.create_and_export_excel_results(selen_ob, Status, time_stamp, full_info_df, script_results_path)

        with pd.ExcelWriter(packspec_testing_file_path, mode="a", engine="openpyxl",
                            if_sheet_exists="overlay") as writer:
            pre_info_df.style.set_properties(**{'background-color': '#B4C6E7', 'color': 'black'}).to_excel \
                (writer, sheet_name="Pre_Info", header=False, startrow=row_to_start_index + 1, startcol=2,
                 index=False)

        with pd.ExcelWriter(packspec_testing_file_path, mode="a", engine="openpyxl",
                            if_sheet_exists="overlay") as writer:
            post_info_df.style.set_properties(**{'background-color': '#C6E0B4', 'color': 'black'}).to_excel \
                (writer, sheet_name="Post_Info", header=False, startrow=row_to_start_index + 1, startcol=2,
                 index=False)

        os.system(packspec_testing_file_path)

        # selen_ob.get_driver().quit()
        # print('Closed automated browser window\n')
        print('SCRIPT HAS FINISHED RUNNING\n')
        print('Exported results in excel file, please check in the Scripts Results folder in your C drive\n')
        print('Make sure to close the console window before running script again')


main()
