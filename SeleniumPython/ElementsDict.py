from selenium.webdriver.common.by import By
import sys


class ElementsDict:

    def __init__(self):
        self.d = {}

    def create_dict(self):
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH DEVL login objects
        username_input_box = ('xpath', '//input[@id="okta-signin-username" and @type="text" and @name="username"]')
        password_input_box = ('xpath', '//input[@id="input62" and @type="password" and @name="password"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH search menu objects
        search_menu = ('xpath', '//*[@id="button-1013-btnIconEl" and @data-ref="btnIconEl"]')
        search_menu_input_box = ('xpath', '//input[contains(@id, "mps_menusearch") and @data-ref="inputEl" and '
                                          '@type="text" and @role="combobox"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH user profile objects
        user_profile_button = ('xpath', '//*[@id="button-1028-btnIconEl"]')
        signout_button = ('xpath', '//*[text()="Sign out"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH post message objects
        post_message_menu_iframe = ('xpath', '//iframe[contains(@src, "PostTestMessage")]')
        post_message_menu_input_box = ('xpath', '//textarea[@id="dataForm:xmlString" and @name="dataForm:xmlString" '
                                                'and @class="textareaStyle"]')
        post_message_menu_send_button = ('xpath', '//input[@id="dataForm:postMessageCmdId"]')
        post_message_menu_results = ('xpath', '//textarea[@id="dataForm:resultString"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH windows objects
        window_close_button_1 = ('xpath', '(//*[text()="Close"])[1]')
        window_close_button_2 = ('xpath', '(//*[text()="Close"])[2]')
        windows_button = ('xpath', '//*[@id="button-1026-btnIconEl"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Universal MH objects
        uni_apply_button = ('xpath', '//*[text()="Apply"]')
        uni_more_button = ('xpath', '//*[text()="More"]')
        uni_create_appointment_button = ('xpath', '//*[text()="Create Appointment"]')
        uni_view_button = ('xpath', '//*[text()="View"]')
        uni_verify_asn_button = ('xpath', '//*[text()="Verify ASN"]')
        uni_edit_header_button = ('xpath', '//*[text()="Edit Header"]')
        uni_no_data_to_display_field = ('xpath', '//*[text()="No data to display"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH ASNs menu objects
        asns_menu_primary_fields_header = ('xpath', '//*[text()="Primary Fields"]')
        asns_menu_primary_fields_dropdown_box_1 = ('xpath', '(//input[@style="text-overflow:ellipsis"])[1]')
        asns_menu_primary_fields_dropdown_box_3 = ('xpath', '(//input[@style="text-overflow:ellipsis"])[3]')
        asns_menu_primary_fields_asn_id_input_box = ('xpath', '//input[@type="text" and @name="asnId" and '
                                                              '@role="combobox"]')
        asns_menu_checkbox_all_button = ('xpath', '//span[starts-with(@id, "gridcolumn-") and contains(@id, '
                                                  '"-textEl")]')
        asns_menu_page_next_button = ('xpath', '//*[contains(@id, "button") and @data-ref="btnIconEl" and '
                                               '@role="presentation" and contains(@class, "x-tbar-page-next")]')
        asns_menu_checkbox_button_ = ('xpath', '(//*[@class="x-grid-row-checker" and @role="presentation"])[')
        asns_menu_total_num_of_asns_field = ('xpath', '//*[contains(text(), "1 - ")]')
        asns_menu_cannot_verify_message = ('xpath', '//*[text()="ASN must not be verified or higher"]')

        # x - toolbar - text  x - box - item x - toolbar - item x - toolbar - text - default

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH Schedule appointment menu objects
        schedule_appointment_menu_iframe = ('xpath', '//iframe[contains(@src, "scheduleAppointment")]')
        schedule_appointment_menu_dock_details_tab = ('xpath', '//*[@id="tab3_lnk" and @name="tab3"]')
        schedule_appointment_menu_planned_dock_input_box = ('xpath', '//input[@id="dataForm:dockNameText1" and '
                                                                     '@type="text" and '
                                                                     '@name="dataForm:dockNameText1"]')
        schedule_appointment_menu_planned_door_input_box = ('xpath', '//input[@id="dataForm:dockDoorNameText1" and '
                                                                     '@type="text" and '
                                                                     '@name="dataForm:dockDoorNameText1"]')
        schedule_appointment_menu_save_button = ('xpath', '//input[@id="apptList_btn_12" and @type="button" and '
                                                          '@class="btn"]')
        schedule_appointment_menu_appointment_id_field = ('xpath', '//*[@id="dataForm:listView:dataTable:0:apptId"]')
        schedule_appointment_menu_appointment_type_field = ('xpath', '//*[@id="dataForm:listView:dataTable:0:type"]')
        schedule_appointment_menu_appointment_status_field = ('xpath', '//*[@id="dataForm:listView:dataTable:0'
                                                                       ':apptType"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Advance Ship Notice Menu objects
        advance_ship_notice_menu_iframe = ('xpath', '//iframe[contains(@src, "ASNDetails")]')
        advance_ship_notice_menu_edit_header_button = ('xpath', '//input['
                                                                '@id="dataForm:ASNDetail_commandbutton_EditASN" and '
                                                                '@type="submit" and @value="Edit Header" and '
                                                                '@class="btn"]')
        advance_ship_notice_menu_ASN_name = ('xpath', '//span[@id="dataForm:ASN_Details_ASN_TCASNIdString" and '
                                                      '@class="captionData"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Edit ASN Menu objects
        edit_ASN_menu_iframe = ('xpath', '//iframe[contains(@src, "EditASN")]')
        edit_ASN_menu_ASN_name = ('xpath', '//span[@id="dataForm:NewEditSummary_TCASNIdString_Edit" and '
                                           '@class="captionData"]')
        edit_ASN_menu_ref_field_10_input_box = ('xpath', '//input[@id="dataForm:RefField10" and '
                                                         '@type="text"]')
        edit_ASN_menu_save_button = ('xpath', '//input[@id="dataForm:save" and @type="submit" '
                                              'and @value="Save"]')
        edit_ASN_menu_ref_field_10_value = ('xpath', '//span[@id="dataForm:RefField10" and '
                                                     '@class="captionData"]')
        edit_ASN_menu_header_text = ('xpath', '//*[text()="Edit ASN"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Verify ASN Menu objects
        verify_asn_menu_iframe = ('xpath', '//iframe[contains(@src, "VerifyIBShipmentItems")]')
        verify_asn_menu_asn_name = ('xpath', '//*[@id="dataForm:asnValueInput" and @class="captionData"]')
        verify_asn_menu_total_num_of_items = ('xpath', '//*[@id="dataForm:lva:dataTable:pager:next" and @alt="Next" '
                                                       'and @type="image"]' + '//parent::span[1]//following::span[1]')
        verify_asn_menu_page_last_button = ('xpath', '//input[@id="dataForm:lva:dataTable:pager:last" and '
                                                     '@alt="Last" and @type="image"]')
        verify_asn_menu_page_next_button = ('xpath', '//input[@id="dataForm:lva:dataTable:pager:next" and '
                                                     '@alt="Next" and @type="image"]')
        verify_asn_menu_all_items_table_variance_field_ = ('xpath', '//*[contains(@id, ":variance5") and contains('
                                                                    '@id, "dataForm:lva:dataTable:")]')
        verify_asn_menu_verify_asn_button = ('xpath', '//input[@type="button" and @class="btn" and contains(@id, '
                                                      '"rmButton_1VerifyASN") and @value="Verify ASN"]')
        verify_asn_menu_warning_receiving_message = (
            'xpath', '//*[text()="Nothing has been received. Continue to verify?"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # SCI Report Menu objects
        sci_report_menu_refresh_button = (
            'xpath', '//button[@id="com.ibm.bi.authoring.refreshBtn" and @role="checkbox" '
                     'and @title="Refresh"]')
        sci_report_menu_run_button = ('xpath', '//button[@id="com.ibm.bi.authoring.runBtn.default" and '
                                               '@role="button" and @title="Run"]')
        sci_report_menu_run_submenu_button = ('xpath', '//button[@id="com.ibm.bi.authoring.runBtn.menu" and '
                                                       '@role="button" and @title="Run"]')
        sci_report_menu_run_excel_data_option = ('xpath', '//*[@title="Run Excel data" and text()="Run Excel data"]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Menu General Objects
        # EWM MENU INPUT BOXES---------------------------------------------------------------------------------------
        ewm_menu_transaction_code_input_box = ('xpath', '//input[@id="__field0-I" and @type="search" and '
                                                        '@placeholder="Transaction '
                                                        'code"]')

        # EWM MENU BUTTONS -----------------------------------------------------------------------------------------
        ewm_menu_yes_button = ('xpath', '//bdi[text()="Yes"]')
        ewm_menu_exit_button = ('xpath', '//bdi[text()="Exit"]')
        ewm_menu_back_button = ('xpath', '//button[@data-bgui-type="TitleBarButton" and '
                                         '@data-bgui-gui-type="GuiButton" '
                                         'and @title="Back"]')
        ewm_menu_execute_button = ('xpath', '//bdi[text()="Execute"]')
        ewm_menu_continue_button = ('xpath', '//bdi[text()="Continue"]')
        ewm_menu_download_button = ('xpath', '//bdi[text()="Download"]')
        ewm_menu_allow_button = ('xpath', '//bdi[text()="Allow"]')
        ewm_menu_close_button = ('xpath', '//bdi[text()="Close"]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM RF Menu Objects
        # EWM RF STARTUP------------------------------------------------------------------------------------------
        ewm_rf_menu_warehouse_no_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                 '@title="Warehouse Number/Warehouse Complex"]' +
                                        '//descendant::input[1]')
        ewm_rf_menu_resource_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                   '@title="Resource (Means of Transportation or User)"]' +
                                          '//descendant::input[1]')
        ewm_rf_menu_rf_device_input_box = ('xpath', '//div[@data-bgui-type="Input" and @title="Presentation Device"]' +
                                           '//descendant::input[1]')

        # EWM RF UI BUTTONS--------------------------------------------------------------------------------------
        ewm_rf_menu_inbound_process_button = ('xpath', '//bdi[contains(text(), "Inbound Process")]')
        ewm_rf_menu_receiving_of_hus_button = ('xpath', '//bdi[contains(text(), "Receiving of HUs")]')
        ewm_rf_menu_rec_hu_by_asn_button = ('xpath', '//bdi[contains(text(), "Rec. HU By ASN")]')
        ewm_rf_menu_putaway_button = ('xpath', '//bdi[contains(text(), "Putaway")]')
        ewm_rf_menu_putaway_by_hu_clust_button = ('xpath', '//bdi[contains(text(), "Putaway by HU clust.")]')
        ewm_rf_menu_next_button = ('xpath', '//bdi[text()="Next"]')
        ewm_rf_menu_create_button = ('xpath', '//bdi[text()="Create"]')
        ewm_rf_menu_pack_button = ('xpath', '//bdi[text()="Pack"]')
        ewm_rf_menu_unload_button = ('xpath', '//bdi[text()="Unload"]')
        ewm_rf_menu_post_gr_button = ('xpath', '//bdi[text()="Post GR"]')
        ewm_rf_menu_confirm_button = ('xpath', '//bdi[text()="Confirm"]')
        ewm_rf_menu_back_button = ('xpath', '//bdi[text()="Back"]')
        ewm_rf_menu_exit_button = ('xpath', '//bdi[text()="Exit"]')
        ewm_rf_menu_save_button = ('xpath', '//bdi[text()="Save"]')
        ewm_rf_menu_start_button = ('xpath', '//bdi[text()="Start"]')

        # EWM RF MENU INPUT BOXES-------------------------------------------------------------------------------
        ewm_rf_menu_enter_asn_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                    '@title="RF: ASN Number"]' +
                                           '//descendant::input[1]')
        ewm_rf_menu_product_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                  '@title="Product Verification"]' +
                                         '//descendant::input[1]')
        ewm_rf_menu_actual_qty_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                     '@title="Actual Destination Quantity in Alternative Unit of '
                                                     'Measure"]' +
                                            '//descendant::input[1]')
        ewm_rf_menu_actual_qty_type_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                          '@title="Alternative Unit of Measure"]' +
                                                 '//descendant::input[1]')
        ewm_rf_menu_packaging_material_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                             '@title="Packaging Materials"]' +
                                                    '//descendant::input[1]')
        ewm_rf_menu_putaway_hu_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                     '@title="RF HU Bar Code Field with Conversion Exit"]' +
                                            '//descendant::input[1]')
        ewm_rf_menu_destination_storage_bin_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                                  '@title="Verification of Destination Storage Bin"]' +
                                                         '//descendant::input[1]')
        ewm_rf_menu_destination_hu_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                         '@title="Verification of Destination Handling Unit"]' +
                                                '//descendant::input[1]')

        # EWM RF MENU FIELDS-----------------------------------------------------------------------------
        ewm_rf_menu_hu_info_field = ('xpath', '//div[@data-bgui-type="Input" and '
                                              '@title="Handling Unit Identification"]' +
                                     '//descendant::input[1]')
        ewm_rf_menu_destination_storage_bin_field = ('xpath', '//div[@data-bgui-type="Input" and '
                                                              '@title="Destination Storage Bin"]' +
                                                     '//descendant::input[1]')
        ewm_rf_menu_destination_hu_field = ('xpath', '//div[@data-bgui-type="Input" and '
                                                     '@title="Destination Handling Unit"]' +
                                            '//descendant::input[1]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Mon Menu Objects
        # EWM MON MENU INPUT BOXES-----------------------------------------------------------------------------
        ewm_mon_menu_warehouse_no_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                        '@data-bgui-sid="wnd[1]/usr/ctxtP_LGNUM"]' +
                                               '//descendant::input[1]')
        ewm_mon_menu_monitor_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                   '@data-bgui-sid="wnd[1]/usr/ctxtP_MONIT"]' +
                                          '//descendant::input[1]')
        ewm_mon_menu_storage_bin_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                       '@title="Storage Bin"]' +
                                              '//descendant::input[1]')
        ewm_mon_menu_product_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                   '@data-bgui-sid="wnd[1]/usr/ctxtS_MATNR-LOW"]' +
                                          '//descendant::input[1]')
        ewm_mon_menu_export_input_box = ('xpath', '//input[@placeholder="*.XLSX" and @type="text"]')
        ewm_mon_menu_asn_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                               '@data-bgui-sid="wnd[1]/usr/txtS_ASN-LOW"]' +
                                      '//descendant::input[1]')
        ewm_mon_menu_warehouse_task_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                          '@title="Warehouse Task"]' +
                                                 '//descendant::input[1]')

        # EWM MON MENU FOLDER OPTIONS ----------------------------------------------------------------------------
        ewm_mon_menu_expand_node_ = ('xpath', '(//*[@title="Expand Node" and @role="button"])[')
        ewm_mon_menu_handling_unit_folder_option_ = ('xpath', '(//bdi[text()="Handling Unit"])[')
        ewm_mon_menu_storage_bin_folder_option_ = ('xpath', '(//bdi[text()="Storage Bin"])[')
        ewm_mon_menu_physical_stock_folder_option_ = ('xpath', '(//bdi[text()="Physical Stock"])[')
        ewm_mon_menu_inbound_del_item_folder_option_ = ('xpath', '(//bdi[text()="Inbound Delivery Item])[')
        ewm_mon_menu_warehouse_task_folder_option_ = ('xpath', '(//bdi[text()="Warehouse Task"])[')
        ewm_mon_menu_warehouse_attribute_folder_option_ = ('xpath', '(//bdi[text()="Warehouse Attribute"])[')

        # EWM MON MENU BUTTONS-----------------------------------------------------------------------------------
        ewm_mon_menu_expand_all_button = ('xpath', '//bdi[text()="Expand All"]')
        ewm_mon_menu_collapse_all_button = ('xpath', '//bdi[text()="Collapse All"]')
        ewm_mon_scroll_bar = ('xpath', '(//div[@class="se-TableScrollBarDragger"])[1]')
        ewm_mon_menu_export_button = ('xpath', '//button[@title="Export" and @data-bgui-type="MenuButton" and '
                                               '@data-bgui-gui-type="GuiDropDownButton"]')
        ewm_mon_menu_more_methods_button = ('xpath', '(//button[@title="More Methods"])[2]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Binmat Menu Objects
        # EWM BINMAT INPUT BOXES--------------------------------------------------------------------------------------
        ewm_binmat_menu_product_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                      '@title="Product"]' +
                                             '//descendant::input[1]')
        ewm_binmat_menu_warehouse_no_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                           '@title="Warehouse Number/Warehouse Complex"]' +
                                                  '//descendant::input[1]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Storage Bin Sub Menu Objects
        # EWM STORAGE BIN SUB MENU INPUT BOXES-------------------------------------------------------------------------
        ewm_storage_bin_sub_menu_max_vol_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                               '@title="Maximum Volume"]' +
                                                      '//descendant::input[1]')
        ewm_storage_bin_sub_menu_load_vol_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                                '@title="Loading or Net Volume"]' +
                                                       '//descendant::input[1]')
        ewm_storage_bin_sub_menu_max_weight_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                                  '@title="Maximum Weight of Storage Bin"]' +
                                                         '//descendant::input[1]')
        ewm_storage_bin_sub_menu_weight_used_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                                   '@title="Weight of Materials in Storage Bin"]' +
                                                          '//descendant::input[1]')

        # EWM STORAGE BIN BUTTONS ------------------------------------------------------------------------------------
        ewm_storage_bin_sub_menu_stock_sect_button = ('xpath', '//span[text()="Stock"]')

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Pack Spec Sub Menu Objects
        # EWM PACKSPEC SUB MENU BUTTONS----------------------------------------------------------------------------
        ewm_packspec_sub_menu_options_arrow_2 = ('xpath', '(//span[contains(@id, "arrow") and @aria-label="Select '
                                                          'Options"])[2]')
        ewm_packspec_sub_menu_product_option_text = ('xpath', '//*[text()="Product"]')
        ewm_packspec_sub_menu_perform_search_button = ('xpath', '//button[@title="Perform Search" and '
                                                                '@data-bgui-type="Button"]')
        ewm_packspec_sub_menu_packaging_material_option_2 = ('xpath', '(//bdi[text()="Packaging Material"])[2]')
        ewm_packspec_sub_menu_product_option = ('xpath', '(//bdi[text()="Product"])[4]')
        ewm_packspec_sub_menu_wght_vol_dim_option = ('xpath', '//span[text()="Weight, Vol. & Dim."]')
        ewm_packspec_sub_menu_warehouse_option = ('xpath', '//span[text()="Warehouse"]')
        ewm_packspec_sub_menu_rounding_option = ('xpath', '//span[text()="Rounding"]')
        ewm_packspec_sub_menu_round_up_circle = ('xpath', '(//div[@data-bgui-gui-type="GuiRadioButton" and '
                                                          '@title="Single-Character Flag"])[3]')
        ewm_packspec_sub_menu_lvl_one_prod_pckging_option = (
            'xpath', '(//bdi[text()="Level One - Product packaging"])[1]')
        ewm_packspec_sub_menu_lvl_three_stor_lvl_option = ('xpath', '(//bdi[text()="Level Three - storage level"])[1]')
        ewm_packspec_sub_menu_assigned_elements_option = ('xpath', '//span[text()="Assigned Elements"]')
        ewm_packspec_sub_menu_uom_option = ('xpath', '//span[text()=" Units of Meas."]')

        # EWM PACKSPEC SUB MENU INPUT BOXES------------------------------------------------------------------------
        ewm_packspec_sub_menu_product_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                            '@title="Argument for Simple Search"]' +
                                                   '//descendant::input[1]')
        ewm_packspec_sub_menu_target_qty_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                               '@title="Target Quantity in Packaging Specification '
                                                               'Level"]' +
                                                      '//descendant::input[1]')
        ewm_packspec_sub_menu_total_qty_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                              '@title="Total Quantity on Packaging Specification '
                                                              'Level"]' +
                                                     '//descendant::input[1]')
        ewm_packspec_sub_menu_pack_mat_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                             '@title="Packaging Material"]' +
                                                    '//descendant::input[1]')
        ewm_packspec_sub_menu_base_qty_field_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                                   '@title="Quantity Field"]' +
                                                          '//descendant::input[1]')
        ewm_packspec_sub_menu_length_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                           '@title="Length"]' +
                                                  '//descendant::input[1]')
        ewm_packspec_sub_menu_width_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                          '@title="Width"]' +
                                                 '//descendant::input[1]')
        ewm_packspec_sub_menu_height_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                           '@title="Height"]' +
                                                  '//descendant::input[1]')
        ewm_packspec_sub_menu_vol_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                        '@title="Volume"]' +
                                               '//descendant::input[1]')
        ewm_packspec_sub_menu_gross_weight_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                                 '@title="Gross weight"]' +
                                                        '//descendant::input[1]')
        ewm_packspec_sub_menu_external_step_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                                  '@title="External Storage Process Step"]' +
                                                         '//descendant::input[1]')
        ewm_packspec_sub_menu_rnd_up_lim_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                               '@title="Round-Up Limit (Percentage of Pack Size)"]' +
                                                      '//descendant::input[1]')

        # EWM PACKSPEC SUB MENU CHECK BOXES----------------------------------------------------------------------------
        ewm_packspec_sub_menu_enter_weight_man_check_box = ('xpath', '//div[@data-bgui-type="CheckBox" and '
                                                                     '@title="Enter Weight Manually"]')
        ewm_packspec_sub_menu_enter_vol_man_check_box = ('xpath', '//div[@data-bgui-type="CheckBox" and '
                                                                  '@title="Enter Volume Manually"]')
        ewm_packspec_sub_menu_enter_dim_man_check_box = ('xpath', '//div[@data-bgui-type="CheckBox" and '
                                                                  '@title="Enter Dimensions Manually"]')
        ewm_packspec_sub_menu_min_pack_size_check_box = ('xpath', '//div[@data-bgui-type="CheckBox" and '
                                                                  '@title="Indicator: Minimum Allowed Pack Size"]')
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Warehouse Product Maintenance Sub Menu Objects
        # EWM WAREHOUSE PRODUCT MAINTENANCE SUB MENU FIELDS----------------------------------------------------------
        ewm_warehouse_prod_maint_sub_menu_st_type_data_field = ('xpath', '//span[text()="St. Type Data"]')

        # EWM WAREHOUSE PRODUCT MAINTENANCE SUB MENU INPUT BOXES-----------------------------------------------------
        ewm_warehouse_prod_maint_sub_menu_max_qty_input_box = ('xpath', '//div[@data-bgui-type="Input" and '
                                                                        '@title="Maximum Quantity"]' +
                                                               '//descendant::input[1]')

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////

        # PACKSPEC MENU OBJECTS
        # Packspec Menu Buttons
        packspec_menu_submit_button = ('xpath', '//b[text()="Submit"]')
        packspec_menu_spec_view_button = ('xpath', '//b[text()="spec View"]')
        packspec_menu_audit_override_button = ('xpath', '//button[text()="Audit Override"]')
        packspec_menu_error_ok_button = ('xpath', '//button[@id="closeErrorModal" and text()="OK"]')

        # Packspec Menu Input Boxes
        packspec_menu_part_number_input_box = ('xpath', '//input[@name="servPartNum" and @type="text"]')
        packspec_menu_pkg_num_table_input_box = ('xpath', '//input[@id="seachBox" and @type="text" and @placeholder="'
                                                          'Search for Pkg_Num..."]')

        # Packspec Menu Dropdown Arrows
        packspec_menu_category_dropdown_arrow = ('xpath', '(//td[@id="category-cell"]//descendant::span[3])[1]')
        packspec_menu_sub_category_dropdown_arrow = ('xpath', '(//td[@id="subCategory-cell"]//descendant::span[3])[1]')
        packspec_menu_pack_bom_dropdown_arrow = ('xpath', '(//td[@id="packagingBom-cell"]//descendant::span[3])[1]')
        packspec_menu_uti_flex_dropdown_arrow = ('xpath', '(//td[@id="utiflex-cell"]//descendant::span[3])[1]')
        packspec_menu_dimensions_of_dropdown_arrow = ('xpath', '(//td[@id="dimensionOf-cell"]//descendant::span[3])[1]')
        packspec_menu_dfc_dropdown_arrow = ('xpath', '(//td[@id="dfc-cell"]//descendant::span[3])[1]')
        packspec_menu_finished_cont_dropdown_arrow = ('xpath', '(//td[@id="finishedCont-cell"]//descendant::span[3])[1]')

        # Packspec Menu Dropdown Input Boxes
        packspec_menu_category_dropdown_input_box = ('xpath', '(//td[@id="category-cell"]//descendant::span[1])//descendant::input')
        packspec_menu_sub_category_dropdown_input_box = ('xpath', '(//td[@id="subCategory-cell"]//descendant::span[1])//descendant::input')
        packspec_menu_pack_bom_dropdown_input_box = ('xpath', '(//td[@id="packagingBom-cell"]//descendant::span[1])//descendant::input')
        packspec_menu_uti_flex_dropdown_input_box = ('xpath', '(//td[@id="utiflex-cell"]//descendant::span[1])//descendant::input')
        packspec_menu_dimensions_of_dropdown_input_box = ('xpath', '(//td[@id="dimensionOf-cell"]//descendant::span[1])//descendant::input')
        packspec_menu_dfc_dropdown_input_box = ('xpath', '(//td[@id="dfc-cell"]//descendant::span[1])//descendant::input')
        packspec_menu_finished_cont_dropdown_input_box = ('xpath', '(//td[@id="finishedCont-cell"]//descendant::span[1])//descendant::input')

        # Packspec Menu Table Values
        packspec_menu_finished_cont_table_row_1 = ('xpath', '(//img[@onclick="deleteFCRow(this)"])[1]')
        packspec_menu_pkg_bom_table_row_1 = ('xpath', '(//img[@onclick="deleterow(this)"])[1]')
        packspec_menu_error_message = ('xpath', '//p[@id="errorMessage"]')

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////

        # PIX TRANSACTIONS MENU OBJECTS
        # Pix Trans Menu iFrames------------------------------------------------------------------------------------
        pix_trans_menu_iframe = ('xpath', '//iframe[contains(@src, "PixTransaction")]')

        # Pix Trans Menu Fields-------------------------------------------------------------------------------------
        pix_trans_menu_header_field = ('xpath', '//div[text()="PIX Transactions"]')
        pix_trans_menu_displaying_num_field = ('xpath', '//span[contains(text(), "Displaying")]')
        pix_trans_menu_no_data_found_field = ('xpath', '//td[text()="No data found"]')

        # Pix Trans Menu Buttons-------------------------------------------------------------------------------
        pix_trans_menu_quick_filter_button = ('xpath', '//span[text()="Quick filter"]')
        pix_trans_menu_saved_filters_button = ('xpath', '//a[text()="Saved filters"]')
        pix_trans_menu_apply_button = ('xpath', '//input[@id="dataForm:lview:filterId:savedapply" and @value="Apply"'
                                                ' and @type="button"]')
        pix_trans_menu_saved_filters_submenu_apply_button = ('xpath', '//input[@id="dataForm:applyFltrBtnPopupAjax" '
                                                                      'and @value="Apply" and @type="button"]')
        pix_trans_menu_resend_button = ('xpath', '//input[@value="Resend" and @type="button" and @class="btn"]')
        pix_trans_menu_table_next_button = ('xpath', '//input[@alt="Next" and @type="image"]')

        # Pix Trans Menu Input Boxes--------------------------------------------------------------------------------
        pix_trans_menu_saved_filters_submenu_ilpn_input_box = ('xpath', '//input[@alt="Find Inbound LPN" and '
                                                                        '@type="text"]')
        pix_trans_menu_saved_filters_submenu_item_input_box = ('xpath', '//input[@id="dataForm:filterDetailId:itemLook'
                                                                        'UpId" and @type="text"]')
        pix_trans_menu_saved_filters_submenu_created_date_from_input_box = ('xpath', '(//input[@class="asbasinp"])[1]')
        pix_trans_menu_saved_filters_submenu_created_date_to_input_box = ('xpath', '(//input[@class="asbasinp"])[2]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        login_d = {
            'username_input_box': username_input_box,
            'password_input_box': password_input_box,
        }

        search_menu_d = {
            'search_menu': search_menu,
            'search_menu_input_box': search_menu_input_box,
        }

        user_profile_d = {
            'user_profile_button': user_profile_button,
            'signout_button': signout_button,
        }

        post_message_d = {
            'post_message_menu_iframe': post_message_menu_iframe,
            'post_message_menu_input_box': post_message_menu_input_box,
            'post_message_menu_send_button': post_message_menu_send_button,
            'post_message_menu_results': post_message_menu_results,
        }

        windows_d = {
            'window_close_button_1': window_close_button_1,
            'window_close_button_2': window_close_button_2,
            'windows_button': windows_button,
        }

        uni_d = {
            'uni_apply_button': uni_apply_button,
            'uni_more_button': uni_more_button,
            'uni_create_appointment_button': uni_create_appointment_button,
            'uni_view_button': uni_view_button,
            'uni_verify_asn_button': uni_verify_asn_button,
            'uni_edit_header_button': uni_edit_header_button,
            'uni_no_data_to_display_field': uni_no_data_to_display_field,
        }

        asns_menu_d = {
            'asns_menu_primary_fields_header': asns_menu_primary_fields_header,
            'asns_menu_primary_fields_dropdown_box_1': asns_menu_primary_fields_dropdown_box_1,
            'asns_menu_primary_fields_dropdown_box_3': asns_menu_primary_fields_dropdown_box_3,
            'asns_menu_primary_fields_asn_id_input_box': asns_menu_primary_fields_asn_id_input_box,
            'asns_menu_checkbox_all_button': asns_menu_checkbox_all_button,
            'asns_menu_page_next_button': asns_menu_page_next_button,
            'asns_menu_checkbox_button_': asns_menu_checkbox_button_,
            'asns_menu_total_num_of_asns_field': asns_menu_total_num_of_asns_field,
            'asns_menu_cannot_verify_message': asns_menu_cannot_verify_message,
        }

        schedule_appointment_menu_d = {
            'schedule_appointment_menu_iframe': schedule_appointment_menu_iframe,
            'schedule_appointment_menu_dock_details_tab': schedule_appointment_menu_dock_details_tab,
            'schedule_appointment_menu_planned_dock_input_box': schedule_appointment_menu_planned_dock_input_box,
            'schedule_appointment_menu_planned_door_input_box': schedule_appointment_menu_planned_door_input_box,
            'schedule_appointment_menu_save_button': schedule_appointment_menu_save_button,
            'schedule_appointment_menu_appointment_id_field': schedule_appointment_menu_appointment_id_field,
            'schedule_appointment_menu_appointment_type_field': schedule_appointment_menu_appointment_type_field,
            'schedule_appointment_menu_appointment_status_field': schedule_appointment_menu_appointment_status_field,
        }

        advance_ship_notice_menu_d = {
            'advance_ship_notice_menu_iframe': advance_ship_notice_menu_iframe,
            'advance_ship_notice_menu_edit_header_button': advance_ship_notice_menu_edit_header_button,
            'advance_ship_notice_menu_ASN_name': advance_ship_notice_menu_ASN_name,
        }

        edit_asn_menu_d = {
            'edit_ASN_menu_iframe': edit_ASN_menu_iframe,
            'edit_ASN_menu_ASN_name': edit_ASN_menu_ASN_name,
            'edit_ASN_menu_ref_field_10_input_box': edit_ASN_menu_ref_field_10_input_box,
            'edit_ASN_menu_save_button': edit_ASN_menu_save_button,
            'edit_ASN_menu_ref_field_10_value': edit_ASN_menu_ref_field_10_value,
            'edit_ASN_menu_header_text': edit_ASN_menu_header_text,
        }

        verify_asn_menu_d = {
            'verify_asn_menu_iframe': verify_asn_menu_iframe,
            'verify_asn_menu_asn_name': verify_asn_menu_asn_name,
            'verify_asn_menu_total_num_of_items': verify_asn_menu_total_num_of_items,
            'verify_asn_menu_page_last_button': verify_asn_menu_page_last_button,
            'verify_asn_menu_page_next_button': verify_asn_menu_page_next_button,
            'verify_asn_menu_all_items_table_variance_field_': verify_asn_menu_all_items_table_variance_field_,
            'verify_asn_menu_verify_asn_button': verify_asn_menu_verify_asn_button,
            'verify_asn_menu_warning_receiving_message': verify_asn_menu_warning_receiving_message,
        }

        pix_trans_menu_d = {
            # PIX TRANS MENU IFRAMES
            'pix_trans_menu_iframe': pix_trans_menu_iframe,

            # PIX TRANS MENU FIELDS
            'pix_trans_menu_header_field': pix_trans_menu_header_field,
            'pix_trans_menu_displaying_num_field': pix_trans_menu_displaying_num_field,
            'pix_trans_menu_no_data_found_field': pix_trans_menu_no_data_found_field,

            # PIX TRANS MENU BUTTONS
            'pix_trans_menu_quick_filter_button': pix_trans_menu_quick_filter_button,
            'pix_trans_menu_saved_filters_button': pix_trans_menu_saved_filters_button,
            'pix_trans_menu_apply_button': pix_trans_menu_apply_button,
            'pix_trans_menu_saved_filters_submenu_apply_button': pix_trans_menu_saved_filters_submenu_apply_button,
            'pix_trans_menu_resend_button': pix_trans_menu_resend_button,
            'pix_trans_menu_table_next_button': pix_trans_menu_table_next_button,

            # PIX TRANS MENU INPUT BOXES
            'pix_trans_menu_saved_filters_submenu_ilpn_input_box': pix_trans_menu_saved_filters_submenu_ilpn_input_box,
            'pix_trans_menu_saved_filters_submenu_item_input_box': pix_trans_menu_saved_filters_submenu_item_input_box,
            'pix_trans_menu_saved_filters_submenu_created_date_from_input_box': pix_trans_menu_saved_filters_submenu_created_date_from_input_box,
            'pix_trans_menu_saved_filters_submenu_created_date_to_input_box': pix_trans_menu_saved_filters_submenu_created_date_to_input_box,
        }

        sci_report_menu_d = {
            'sci_report_menu_refresh_button': sci_report_menu_refresh_button,
            'sci_report_menu_run_button': sci_report_menu_run_button,
            'sci_report_menu_run_submenu_button': sci_report_menu_run_submenu_button,
            'sci_report_menu_run_excel_data_option': sci_report_menu_run_excel_data_option,
        }

        ewm_menu_d = {
            # EWM MENU INPUT BOXES
            'ewm_menu_transaction_code_input_box': ewm_menu_transaction_code_input_box,

            # EWM MENU BUTTONS
            'ewm_menu_yes_button': ewm_menu_yes_button,
            'ewm_menu_back_button': ewm_menu_back_button,
            'ewm_menu_exit_button': ewm_menu_exit_button,
            'ewm_menu_execute_button': ewm_menu_execute_button,
            'ewm_menu_continue_button': ewm_menu_continue_button,
            'ewm_menu_download_button': ewm_menu_download_button,
            'ewm_menu_allow_button': ewm_menu_allow_button,
            'ewm_menu_close_button': ewm_menu_close_button,
        }

        ewm_rf_menu_d = {
            # EWM RF STARTUP
            'ewm_rf_menu_warehouse_no_box': ewm_rf_menu_warehouse_no_box,
            'ewm_rf_menu_resource_input_box': ewm_rf_menu_resource_input_box,
            'ewm_rf_menu_rf_device_input_box': ewm_rf_menu_rf_device_input_box,

            # EWM RF UI BUTTONS
            'ewm_rf_menu_inbound_process_button': ewm_rf_menu_inbound_process_button,
            'ewm_rf_menu_receiving_of_hus_button': ewm_rf_menu_receiving_of_hus_button,
            'ewm_rf_menu_rec_hu_by_asn_button': ewm_rf_menu_rec_hu_by_asn_button,
            'ewm_rf_menu_putaway_button': ewm_rf_menu_putaway_button,
            'ewm_rf_menu_putaway_by_hu_clust_button': ewm_rf_menu_putaway_by_hu_clust_button,
            'ewm_rf_menu_next_button': ewm_rf_menu_next_button,
            'ewm_rf_menu_create_button': ewm_rf_menu_create_button,
            'ewm_rf_menu_pack_button': ewm_rf_menu_pack_button,
            'ewm_rf_menu_unload_button': ewm_rf_menu_unload_button,
            'ewm_rf_menu_post_gr_button': ewm_rf_menu_post_gr_button,
            'ewm_rf_menu_confirm_button': ewm_rf_menu_confirm_button,
            'ewm_rf_menu_back_button': ewm_rf_menu_back_button,
            'ewm_rf_menu_exit_button': ewm_rf_menu_exit_button,
            'ewm_rf_menu_save_button': ewm_rf_menu_save_button,
            'ewm_rf_menu_start_button': ewm_rf_menu_start_button,

            # EWM RF MENU INPUT BOXES
            'ewm_rf_menu_enter_asn_input_box': ewm_rf_menu_enter_asn_input_box,
            'ewm_rf_menu_product_input_box': ewm_rf_menu_product_input_box,
            'ewm_rf_menu_actual_qty_input_box': ewm_rf_menu_actual_qty_input_box,
            'ewm_rf_menu_actual_qty_type_input_box': ewm_rf_menu_actual_qty_type_input_box,
            'ewm_rf_menu_packaging_material_input_box': ewm_rf_menu_packaging_material_input_box,
            'ewm_rf_menu_putaway_hu_input_box': ewm_rf_menu_putaway_hu_input_box,
            'ewm_rf_menu_destination_storage_bin_input_box': ewm_rf_menu_destination_storage_bin_input_box,
            'ewm_rf_menu_destination_hu_input_box': ewm_rf_menu_destination_hu_input_box,

            # EWM RF MENU FIELDS
            'ewm_rf_menu_hu_info_field': ewm_rf_menu_hu_info_field,
            'ewm_rf_menu_destination_storage_bin_field': ewm_rf_menu_destination_storage_bin_field,
            'ewm_rf_menu_destination_hu_field': ewm_rf_menu_destination_hu_field,
        }

        ewm_mon_menu_d = {
            # EWM MON MENU INPUT BOXES
            'ewm_mon_menu_warehouse_no_input_box': ewm_mon_menu_warehouse_no_input_box,
            'ewm_mon_menu_monitor_input_box': ewm_mon_menu_monitor_input_box,
            'ewm_mon_menu_storage_bin_input_box': ewm_mon_menu_storage_bin_input_box,
            'ewm_mon_menu_product_input_box': ewm_mon_menu_product_input_box,
            'ewm_mon_menu_export_input_box': ewm_mon_menu_export_input_box,
            'ewm_mon_menu_asn_input_box': ewm_mon_menu_asn_input_box,
            'ewm_mon_menu_warehouse_task_input_box': ewm_mon_menu_warehouse_task_input_box,

            # EWM MON MENU FOLDER OPTIONS
            'ewm_mon_menu_expand_node_': ewm_mon_menu_expand_node_,
            'ewm_mon_menu_handling_unit_folder_option_': ewm_mon_menu_handling_unit_folder_option_,
            'ewm_mon_menu_storage_bin_folder_option_': ewm_mon_menu_storage_bin_folder_option_,
            'ewm_mon_menu_physical_stock_folder_option_': ewm_mon_menu_physical_stock_folder_option_,
            'ewm_mon_menu_inbound_del_item_folder_option_': ewm_mon_menu_inbound_del_item_folder_option_,
            'ewm_mon_menu_warehouse_task_folder_option_': ewm_mon_menu_warehouse_task_folder_option_,
            'ewm_mon_menu_warehouse_attribute_folder_option_': ewm_mon_menu_warehouse_attribute_folder_option_,

            # EWM MON MENU BUTTONS
            'ewm_mon_menu_expand_all_button': ewm_mon_menu_expand_all_button,
            'ewm_mon_menu_collapse_all_button': ewm_mon_menu_collapse_all_button,
            'ewm_mon_scroll_bar': ewm_mon_scroll_bar,
            'ewm_mon_menu_export_button': ewm_mon_menu_export_button,
            'ewm_mon_menu_more_methods_button': ewm_mon_menu_more_methods_button,
        }

        ewm_binmat_menu_d = {
            # EWM BINMAT MENU INPUT BOXES
            'ewm_binmat_menu_product_input_box': ewm_binmat_menu_product_input_box,
            'ewm_binmat_menu_warehouse_no_input_box': ewm_binmat_menu_warehouse_no_input_box,
        }

        ewm_storage_bin_sub_menu_d = {
            # EWM STORAGE BIN SUB MENU INPUT BOXES
            'ewm_storage_bin_sub_menu_max_vol_input_box': ewm_storage_bin_sub_menu_max_vol_input_box,
            'ewm_storage_bin_sub_menu_load_vol_input_box': ewm_storage_bin_sub_menu_load_vol_input_box,
            'ewm_storage_bin_sub_menu_max_weight_input_box': ewm_storage_bin_sub_menu_max_weight_input_box,
            'ewm_storage_bin_sub_menu_weight_used_input_box': ewm_storage_bin_sub_menu_weight_used_input_box,

            # EWM STORAGE BIN SUB MENU BUTTONS
            'ewm_storage_bin_sub_menu_stock_sect_button': ewm_storage_bin_sub_menu_stock_sect_button,
        }

        ewm_packspec_sub_menu_d = {
            # EWM PACKSPEC SUB MENU BUTTONS
            'ewm_packspec_sub_menu_options_arrow_2': ewm_packspec_sub_menu_options_arrow_2,
            'ewm_packspec_sub_menu_product_option_text': ewm_packspec_sub_menu_product_option_text,
            'ewm_packspec_sub_menu_perform_search_button': ewm_packspec_sub_menu_perform_search_button,
            'ewm_packspec_sub_menu_packaging_material_option_2': ewm_packspec_sub_menu_packaging_material_option_2,
            'ewm_packspec_sub_menu_product_option': ewm_packspec_sub_menu_product_option,
            'ewm_packspec_sub_menu_wght_vol_dim_option': ewm_packspec_sub_menu_wght_vol_dim_option,
            'ewm_packspec_sub_menu_warehouse_option': ewm_packspec_sub_menu_warehouse_option,
            'ewm_packspec_sub_menu_rounding_option': ewm_packspec_sub_menu_rounding_option,
            'ewm_packspec_sub_menu_round_up_circle': ewm_packspec_sub_menu_round_up_circle,
            'ewm_packspec_sub_menu_lvl_one_prod_pckging_option': ewm_packspec_sub_menu_lvl_one_prod_pckging_option,
            'ewm_packspec_sub_menu_lvl_three_stor_lvl_option': ewm_packspec_sub_menu_lvl_three_stor_lvl_option,
            'ewm_packspec_sub_menu_assigned_elements_option': ewm_packspec_sub_menu_assigned_elements_option,
            'ewm_packspec_sub_menu_uom_option': ewm_packspec_sub_menu_uom_option,

            # EWM PACKSPEC SUB MENU INPUT BOXES
            'ewm_packspec_sub_menu_product_input_box': ewm_packspec_sub_menu_product_input_box,
            'ewm_packspec_sub_menu_target_qty_input_box': ewm_packspec_sub_menu_target_qty_input_box,
            'ewm_packspec_sub_menu_total_qty_input_box': ewm_packspec_sub_menu_total_qty_input_box,
            'ewm_packspec_sub_menu_pack_mat_input_box': ewm_packspec_sub_menu_pack_mat_input_box,
            'ewm_packspec_sub_menu_base_qty_field_input_box': ewm_packspec_sub_menu_base_qty_field_input_box,
            'ewm_packspec_sub_menu_length_input_box': ewm_packspec_sub_menu_length_input_box,
            'ewm_packspec_sub_menu_width_input_box': ewm_packspec_sub_menu_width_input_box,
            'ewm_packspec_sub_menu_height_input_box': ewm_packspec_sub_menu_height_input_box,
            'ewm_packspec_sub_menu_vol_input_box': ewm_packspec_sub_menu_vol_input_box,
            'ewm_packspec_sub_menu_gross_weight_input_box': ewm_packspec_sub_menu_gross_weight_input_box,
            'ewm_packspec_sub_menu_external_step_input_box': ewm_packspec_sub_menu_external_step_input_box,
            'ewm_packspec_sub_menu_rnd_up_lim_input_box': ewm_packspec_sub_menu_rnd_up_lim_input_box,

            # EWM PACKSPEC SUB MENU CHECK BOXES
            'ewm_packspec_sub_menu_enter_weight_man_check_box': ewm_packspec_sub_menu_enter_weight_man_check_box,
            'ewm_packspec_sub_menu_enter_vol_man_check_box': ewm_packspec_sub_menu_enter_vol_man_check_box,
            'ewm_packspec_sub_menu_enter_dim_man_check_box': ewm_packspec_sub_menu_enter_dim_man_check_box,
            'ewm_packspec_sub_menu_min_pack_size_check_box': ewm_packspec_sub_menu_min_pack_size_check_box,
        }

        ewm_warehouse_prod_maint_sub_menu_d = {
            # EWM WAREHOUSE PRODUCT MAINTENANCE SUB MENU FIELDS
            'ewm_warehouse_prod_maint_sub_menu_st_type_data_field': ewm_warehouse_prod_maint_sub_menu_st_type_data_field,
            'ewm_warehouse_prod_maint_sub_menu_max_qty_input_box': ewm_warehouse_prod_maint_sub_menu_max_qty_input_box,
        }

        packspec_menu_d = {
            # Packspec Menu Buttons
            'packspec_menu_submit_button': packspec_menu_submit_button,
            'packspec_menu_spec_view_button': packspec_menu_spec_view_button,
            'packspec_menu_audit_override_button': packspec_menu_audit_override_button,
            'packspec_menu_error_ok_button': packspec_menu_error_ok_button,

            # Packspec Menu Input Boxes
            'packspec_menu_part_number_input_box': packspec_menu_part_number_input_box,
            'packspec_menu_pkg_num_table_input_box': packspec_menu_pkg_num_table_input_box,

            # Packspec Menu Dropdown Arrows
            'packspec_menu_category_dropdown_arrow': packspec_menu_category_dropdown_arrow,
            'packspec_menu_sub_category_dropdown_arrow': packspec_menu_sub_category_dropdown_arrow,
            'packspec_menu_pack_bom_dropdown_arrow': packspec_menu_pack_bom_dropdown_arrow,
            'packspec_menu_uti_flex_dropdown_arrow': packspec_menu_uti_flex_dropdown_arrow,
            'packspec_menu_dimensions_of_dropdown_arrow': packspec_menu_dimensions_of_dropdown_arrow,
            'packspec_menu_dfc_dropdown_arrow': packspec_menu_dfc_dropdown_arrow,
            'packspec_menu_finished_cont_dropdown_arrow': packspec_menu_finished_cont_dropdown_arrow,

            # Packspec Menu Dropdown Input Boxes
            'packspec_menu_category_dropdown_input_box': packspec_menu_category_dropdown_input_box,
            'packspec_menu_sub_category_dropdown_input_box': packspec_menu_sub_category_dropdown_input_box,
            'packspec_menu_pack_bom_dropdown_input_box': packspec_menu_pack_bom_dropdown_input_box,
            'packspec_menu_uti_flex_dropdown_input_box': packspec_menu_uti_flex_dropdown_input_box,
            'packspec_menu_dimensions_of_dropdown_input_box': packspec_menu_dimensions_of_dropdown_input_box,
            'packspec_menu_dfc_dropdown_input_box': packspec_menu_dfc_dropdown_input_box,
            'packspec_menu_finished_cont_dropdown_input_box': packspec_menu_finished_cont_dropdown_input_box,

            # Packspec Menu Table Values
            'packspec_menu_finished_cont_table_row_1': packspec_menu_finished_cont_table_row_1,
            'packspec_menu_pkg_bom_table_row_1': packspec_menu_pkg_bom_table_row_1,
            'packspec_menu_error_message': packspec_menu_error_message,
        }

        self.d = login_d | search_menu_d | user_profile_d | post_message_d | windows_d | uni_d | asns_menu_d | \
                 schedule_appointment_menu_d | advance_ship_notice_menu_d | edit_asn_menu_d | verify_asn_menu_d | \
                 sci_report_menu_d | ewm_menu_d | ewm_rf_menu_d | ewm_mon_menu_d | ewm_binmat_menu_d | \
                 ewm_storage_bin_sub_menu_d | ewm_packspec_sub_menu_d | ewm_warehouse_prod_maint_sub_menu_d | \
                 pix_trans_menu_d | packspec_menu_d
        self.d.update()

        return self.d

