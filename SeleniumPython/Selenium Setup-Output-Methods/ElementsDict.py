from selenium.webdriver.common.by import By
import sys


class ElementsDict:

    def __init__(self):
        self.d = {}

    def create_dict(self):
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH DEVL login objects
        username_input_box = (By.XPATH, '//input[@id="okta-signin-username" and @type="text" and @name="username"]')
        password_input_box = (By.XPATH, '//input[@id="input62" and @type="password" and @name="password"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH search menu objects
        search_menu = (By.XPATH, '//*[@id="button-1013-btnIconEl" and @data-ref="btnIconEl"]')
        search_menu_input_box = (By.XPATH, '//input[contains(@id, "mps_menusearch") and @data-ref="inputEl" and '
                                           '@type="text" and @role="combobox"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH user profile objects
        user_profile_button = (By.XPATH, '//*[@id="button-1028-btnIconEl"]')
        signout_button = (By.XPATH, '//*[text()="Sign out"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH post message objects
        post_message_menu_iframe = (By.XPATH, '//iframe[contains(@src, "PostTestMessage")]')
        post_message_menu_input_box = (By.XPATH, '//textarea[@id="dataForm:xmlString" and @name="dataForm:xmlString" '
                                                 'and @class="textareaStyle"]')
        post_message_menu_send_button = (By.XPATH, '//input[@id="dataForm:postMessageCmdId"]')
        post_message_menu_results = (By.XPATH, '//textarea[@id="dataForm:resultString"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH windows objects
        window_close_button_1 = (By.XPATH, '(//*[text()="Close"])[1]')
        window_close_button_2 = (By.XPATH, '(//*[text()="Close"])[2]')
        windows_button = (By.XPATH, '//*[@id="button-1026-btnIconEl"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Universal MH objects
        uni_apply_button = (By.XPATH, '//*[text()="Apply"]')
        uni_more_button = (By.XPATH, '//*[text()="More"]')
        uni_create_appointment_button = (By.XPATH, '//*[text()="Create Appointment"]')
        uni_view_button = (By.XPATH, '//*[text()="View"]')
        uni_verify_asn_button = (By.XPATH, '//*[text()="Verify ASN"]')
        uni_edit_header_button = (By.XPATH, '//*[text()="Edit Header"]')
        uni_no_data_to_display_field = (By.XPATH, '//*[text()="No data to display"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH ASNs menu objects
        asns_menu_primary_fields_header = (By.XPATH, '//*[text()="Primary Fields"]')
        asns_menu_primary_fields_dropdown_box_1 = (By.XPATH, '(//input[@style="text-overflow:ellipsis"])[1]')
        asns_menu_primary_fields_dropdown_box_3 = (By.XPATH, '(//input[@style="text-overflow:ellipsis"])[3]')
        asns_menu_primary_fields_asn_id_input_box = (By.XPATH, '//input[@type="text" and @name="asnId" and '
                                                               '@role="combobox"]')
        asns_menu_checkbox_all_button = (By.XPATH, '//span[starts-with(@id, "gridcolumn-") and contains(@id, '
                                                   '"-textEl")]')
        asns_menu_page_next_button = (By.XPATH, '//*[contains(@id, "button") and @data-ref="btnIconEl" and '
                                                '@role="presentation" and contains(@class, "x-tbar-page-next")]')
        asns_menu_checkbox_button_ = (By.XPATH, '(//*[@class="x-grid-row-checker" and @role="presentation"])[')
        asns_menu_total_num_of_asns_field = (By.XPATH, '//*[contains(text(), "1 - ")]')
        asns_menu_cannot_verify_message = (By.XPATH, '//*[text()="ASN must not be verified or higher"]')

        # x - toolbar - text  x - box - item x - toolbar - item x - toolbar - text - default

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # MH Schedule appointment menu objects
        schedule_appointment_menu_iframe = (By.XPATH, '//iframe[contains(@src, "scheduleAppointment")]')
        schedule_appointment_menu_dock_details_tab = (By.XPATH, '//*[@id="tab3_lnk" and @name="tab3"]')
        schedule_appointment_menu_planned_dock_input_box = (By.XPATH, '//input[@id="dataForm:dockNameText1" and '
                                                                      '@type="text" and '
                                                                      '@name="dataForm:dockNameText1"]')
        schedule_appointment_menu_planned_door_input_box = (By.XPATH, '//input[@id="dataForm:dockDoorNameText1" and '
                                                                      '@type="text" and '
                                                                      '@name="dataForm:dockDoorNameText1"]')
        schedule_appointment_menu_save_button = (By.XPATH, '//input[@id="apptList_btn_12" and @type="button" and '
                                                           '@class="btn"]')
        schedule_appointment_menu_appointment_id_field = (By.XPATH, '//*[@id="dataForm:listView:dataTable:0:apptId"]')
        schedule_appointment_menu_appointment_type_field = (By.XPATH, '//*[@id="dataForm:listView:dataTable:0:type"]')
        schedule_appointment_menu_appointment_status_field = (By.XPATH, '//*[@id="dataForm:listView:dataTable:0'
                                                                        ':apptType"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Advance Ship Notice Menu objects
        advance_ship_notice_menu_iframe = (By.XPATH, '//iframe[contains(@src, "ASNDetails")]')
        advance_ship_notice_menu_edit_header_button = (By.XPATH, '//input['
                                                                 '@id="dataForm:ASNDetail_commandbutton_EditASN" and '
                                                                 '@type="submit" and @value="Edit Header" and '
                                                                 '@class="btn"]')
        advance_ship_notice_menu_ASN_name = (By.XPATH, '//span[@id="dataForm:ASN_Details_ASN_TCASNIdString" and '
                                                       '@class="captionData"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Edit ASN Menu objects
        edit_ASN_menu_iframe = (By.XPATH, '//iframe[contains(@src, "EditASN")]')
        edit_ASN_menu_ASN_name = (By.XPATH, '//span[@id="dataForm:NewEditSummary_TCASNIdString_Edit" and '
                                            '@class="captionData"]')
        edit_ASN_menu_ref_field_10_input_box = (By.XPATH, '//input[@id="dataForm:RefField10" and '
                                                          '@type="text"]')
        edit_ASN_menu_save_button = (By.XPATH, '//input[@id="dataForm:save" and @type="submit" '
                                               'and @value="Save"]')
        edit_ASN_menu_ref_field_10_value = (By.XPATH, '//span[@id="dataForm:RefField10" and '
                                                      '@class="captionData"]')
        edit_ASN_menu_header_text = (By.XPATH, '//*[text()="Edit ASN"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # Verify ASN Menu objects
        verify_asn_menu_iframe = (By.XPATH, '//iframe[contains(@src, "VerifyIBShipmentItems")]')
        verify_asn_menu_asn_name = (By.XPATH, '//*[@id="dataForm:asnValueInput" and @class="captionData"]')
        verify_asn_menu_total_num_of_items = (By.XPATH, '//*[@id="dataForm:lva:dataTable:pager:next" and @alt="Next" '
                                                        'and @type="image"]' + '//parent::span[1]//following::span[1]')
        verify_asn_menu_page_last_button = (By.XPATH, '//input[@id="dataForm:lva:dataTable:pager:last" and '
                                                      '@alt="Last" and @type="image"]')
        verify_asn_menu_page_next_button = (By.XPATH, '//input[@id="dataForm:lva:dataTable:pager:next" and '
                                                      '@alt="Next" and @type="image"]')
        verify_asn_menu_all_items_table_variance_field_ = (By.XPATH, '//*[contains(@id, ":variance5") and contains('
                                                                     '@id, "dataForm:lva:dataTable:")]')
        verify_asn_menu_verify_asn_button = (By.XPATH, '//input[@type="button" and @class="btn" and contains(@id, '
                                                       '"rmButton_1VerifyASN") and @value="Verify ASN"]')
        verify_asn_menu_warning_receiving_message = (
            By.XPATH, '//*[text()="Nothing has been received. Continue to verify?"]')

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # SCI Report Menu objects
        sci_report_menu_refresh_button = (
            By.XPATH, '//button[@id="com.ibm.bi.authoring.refreshBtn" and @role="checkbox" '
                      'and @title="Refresh"]')
        sci_report_menu_run_button = (By.XPATH, '//button[@id="com.ibm.bi.authoring.runBtn.default" and '
                                                '@role="button" and @title="Run"]')
        sci_report_menu_run_submenu_button = (By.XPATH, '//button[@id="com.ibm.bi.authoring.runBtn.menu" and '
                                                        '@role="button" and @title="Run"]')
        sci_report_menu_run_excel_data_option = (By.XPATH, '//*[@title="Run Excel data" and text()="Run Excel data"]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Menu General Objects
        # EWM MENU INPUT BOXES---------------------------------------------------------------------------------------
        ewm_menu_transaction_code_input_box = (By.XPATH, '//input[@id="__field0-I" and @type="search" and '
                                                         '@placeholder="Transaction '
                                                         'code"]')

        # EWM MENU BUTTONS -----------------------------------------------------------------------------------------
        ewm_menu_yes_button = (By.XPATH, '//bdi[text()="Yes"]')
        ewm_menu_exit_button = (By.XPATH, '//bdi[text()="Exit"]')
        ewm_menu_back_button = (By.XPATH, '//button[@data-bgui-type="TitleBarButton" and '
                                          '@data-bgui-gui-type="GuiButton" '
                                          'and @title="Back"]')
        ewm_menu_execute_button = (By.XPATH, '//bdi[text()="Execute"]')
        ewm_menu_continue_button = (By.XPATH, '//bdi[text()="Continue"]')
        ewm_menu_download_button = (By.XPATH, '//bdi[text()="Download"]')
        ewm_menu_allow_button = (By.XPATH, '//bdi[text()="Allow"]')
        ewm_menu_close_button = (By.XPATH, '//bdi[text()="Close"]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM RF Menu Objects
        # EWM RF STARTUP------------------------------------------------------------------------------------------
        ewm_rf_menu_warehouse_no_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                  '@title="Warehouse Number/Warehouse Complex"]' +
                                                  '//descendant::input[1]')
        ewm_rf_menu_resource_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                    '@title="Resource (Means of Transportation or User)"]' +
                                                    '//descendant::input[1]')
        ewm_rf_menu_rf_device_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and @title="Presentation Device"]' +
                                                     '//descendant::input[1]')

        # EWM RF UI BUTTONS--------------------------------------------------------------------------------------
        ewm_rf_menu_inbound_process_button = (By.XPATH, '//bdi[contains(text(), "Inbound Process")]')
        ewm_rf_menu_receiving_of_hus_button = (By.XPATH, '//bdi[contains(text(), "Receiving of HUs")]')
        ewm_rf_menu_rec_hu_by_asn_button = (By.XPATH, '//bdi[contains(text(), "Rec. HU By ASN")]')
        ewm_rf_menu_putaway_button = (By.XPATH, '//bdi[contains(text(), "Putaway")]')
        ewm_rf_menu_putaway_by_hu_clust_button = (By.XPATH, '//bdi[contains(text(), "Putaway by HU clust.")]')
        ewm_rf_menu_next_button = (By.XPATH, '//bdi[text()="Next"]')
        ewm_rf_menu_create_button = (By.XPATH, '//bdi[text()="Create"]')
        ewm_rf_menu_pack_button = (By.XPATH, '//bdi[text()="Pack"]')
        ewm_rf_menu_unload_button = (By.XPATH, '//bdi[text()="Unload"]')
        ewm_rf_menu_post_gr_button = (By.XPATH, '//bdi[text()="Post GR"]')
        ewm_rf_menu_confirm_button = (By.XPATH, '//bdi[text()="Confirm"]')
        ewm_rf_menu_back_button = (By.XPATH, '//bdi[text()="Back"]')
        ewm_rf_menu_exit_button = (By.XPATH, '//bdi[text()="Exit"]')
        ewm_rf_menu_save_button = (By.XPATH, '//bdi[text()="Save"]')
        ewm_rf_menu_start_button = (By.XPATH, '//bdi[text()="Start"]')

        # EWM RF MENU INPUT BOXES-------------------------------------------------------------------------------
        ewm_rf_menu_enter_asn_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                     '@title="RF: ASN Number"]' +
                                                     '//descendant::input[1]')
        ewm_rf_menu_product_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                   '@title="Product Verification"]' +
                                                   '//descendant::input[1]')
        ewm_rf_menu_actual_qty_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                      '@title="Actual Destination Quantity in Alternative Unit of '
                                                      'Measure"]' +
                                                      '//descendant::input[1]')
        ewm_rf_menu_actual_qty_type_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                           '@title="Alternative Unit of Measure"]' +
                                                           '//descendant::input[1]')
        ewm_rf_menu_packaging_material_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                              '@title="Packaging Materials"]' +
                                                              '//descendant::input[1]')
        ewm_rf_menu_putaway_hu_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                      '@title="RF HU Bar Code Field with Conversion Exit"]' +
                                                      '//descendant::input[1]')
        ewm_rf_menu_destination_storage_bin_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                                   '@title="Verification of Destination Storage Bin"]' +
                                                                   '//descendant::input[1]')
        ewm_rf_menu_destination_hu_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                          '@title="Verification of Destination Handling Unit"]' +
                                                          '//descendant::input[1]')

        # EWM RF MENU FIELDS-----------------------------------------------------------------------------
        ewm_rf_menu_hu_info_field = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                               '@title="Handling Unit Identification"]' +
                                               '//descendant::input[1]')
        ewm_rf_menu_destination_storage_bin_field = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                               '@title="Destination Storage Bin"]' +
                                                               '//descendant::input[1]')
        ewm_rf_menu_destination_hu_field = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                      '@title="Destination Handling Unit"]' +
                                                      '//descendant::input[1]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Mon Menu Objects
        # EWM MON MENU INPUT BOXES-----------------------------------------------------------------------------
        ewm_mon_menu_warehouse_no_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                         '@data-bgui-sid="wnd[1]/usr/ctxtP_LGNUM"]' +
                                                         '//descendant::input[1]')
        ewm_mon_menu_monitor_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                    '@data-bgui-sid="wnd[1]/usr/ctxtP_MONIT"]' +
                                                    '//descendant::input[1]')
        ewm_mon_menu_storage_bin_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                        '@title="Storage Bin"]' +
                                                        '//descendant::input[1]')
        ewm_mon_menu_product_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                    '@data-bgui-sid="wnd[1]/usr/ctxtS_MATNR-LOW"]' +
                                                    '//descendant::input[1]')
        ewm_mon_menu_export_input_box = (By.XPATH, '//input[@placeholder="*.XLSX" and @type="text"]')
        ewm_mon_menu_asn_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                '@data-bgui-sid="wnd[1]/usr/txtS_ASN-LOW"]' +
                                                '//descendant::input[1]')
        ewm_mon_menu_warehouse_task_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                           '@title="Warehouse Task"]' +
                                                           '//descendant::input[1]')

        # EWM MON MENU FOLDER OPTIONS ----------------------------------------------------------------------------
        ewm_mon_menu_expand_node_ = (By.XPATH, '(//*[@title="Expand Node" and @role="button"])[')
        ewm_mon_menu_handling_unit_folder_option_ = (By.XPATH, '(//bdi[text()="Handling Unit"])[')
        ewm_mon_menu_storage_bin_folder_option_ = (By.XPATH, '(//bdi[text()="Storage Bin"])[')
        ewm_mon_menu_physical_stock_folder_option_ = (By.XPATH, '(//bdi[text()="Physical Stock"])[')
        ewm_mon_menu_inbound_del_item_folder_option_ = (By.XPATH, '(//bdi[text()="Inbound Delivery Item])[')
        ewm_mon_menu_warehouse_task_folder_option_ = (By.XPATH, '(//bdi[text()="Warehouse Task"])[')
        ewm_mon_menu_warehouse_attribute_folder_option_ = (By.XPATH, '(//bdi[text()="Warehouse Attribute"])[')

        # EWM MON MENU BUTTONS-----------------------------------------------------------------------------------
        ewm_mon_menu_expand_all_button = (By.XPATH, '//bdi[text()="Expand All"]')
        ewm_mon_menu_collapse_all_button = (By.XPATH, '//bdi[text()="Collapse All"]')
        ewm_mon_scroll_bar = (By.XPATH, '(//div[@class="se-TableScrollBarDragger"])[1]')
        ewm_mon_menu_export_button = (By.XPATH, '//button[@title="Export" and @data-bgui-type="MenuButton" and '
                                                '@data-bgui-gui-type="GuiDropDownButton"]')
        ewm_mon_menu_more_methods_button = (By.XPATH, '(//button[@title="More Methods"])[2]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Binmat Menu Objects
        # EWM BINMAT INPUT BOXES--------------------------------------------------------------------------------------
        ewm_binmat_menu_product_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                       '@title="Product"]' +
                                                       '//descendant::input[1]')
        ewm_binmat_menu_warehouse_no_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                            '@title="Warehouse Number/Warehouse Complex"]' +
                                                            '//descendant::input[1]')

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Storage Bin Sub Menu Objects
        # EWM STORAGE BIN SUB MENU INPUT BOXES-------------------------------------------------------------------------
        ewm_storage_bin_sub_menu_max_vol_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                                '@title="Maximum Volume"]' +
                                                                '//descendant::input[1]')
        ewm_storage_bin_sub_menu_load_vol_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                                 '@title="Loading or Net Volume"]' +
                                                                 '//descendant::input[1]')
        ewm_storage_bin_sub_menu_max_weight_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                                   '@title="Maximum Weight of Storage Bin"]' +
                                                                   '//descendant::input[1]')
        ewm_storage_bin_sub_menu_weight_used_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                                    '@title="Weight of Materials in Storage Bin"]' +
                                                                    '//descendant::input[1]')

        # EWM STORAGE BIN BUTTONS ------------------------------------------------------------------------------------
        ewm_storage_bin_sub_menu_stock_sect_button = (By.XPATH, '//span[text()="Stock"]')

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Pack Spec Sub Menu Objects
        # EWM PACKSPEC SUB MENU BUTTONS----------------------------------------------------------------------------
        ewm_packspec_sub_menu_options_arrow_2 = (By.XPATH, '(//span[contains(@id, "arrow") and @aria-label="Select '
                                                           'Options"])[2]')
        ewm_packspec_sub_menu_product_option_text = (By.XPATH, '//*[text()="Product"]')
        ewm_packspec_sub_menu_perform_search_button = (By.XPATH, '//button[@title="Perform Search" and '
                                                                 '@data-bgui-type="Button"]')
        ewm_packspec_sub_menu_packaging_material_option_2 = (By.XPATH, '(//bdi[text()="Packaging Material"])[2]')

        # EWM PACKSPEC SUB MENU INPUT BOXES------------------------------------------------------------------------
        ewm_packspec_sub_menu_product_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                             '@title="Argument for Simple Search"]' +
                                                             '//descendant::input[1]')
        ewm_packspec_sub_menu_target_qty_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                                '@title="Target Quantity in Packaging Specification '
                                                                'Level"]' +
                                                                '//descendant::input[1]')
        ewm_packspec_sub_menu_pack_mat_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                              '@title="Packaging Material"]' +
                                                              '//descendant::input[1]')

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////

        # EWM Warehouse Product Maintenance Sub Menu Objects
        # EWM WAREHOUSE PRODUCT MAINTENANCE SUB MENU FIELDS----------------------------------------------------------
        ewm_warehouse_prod_maint_sub_menu_st_type_data_field = (By.XPATH, '//span[text()="St. Type Data"]')

        # EWM WAREHOUSE PRODUCT MAINTENANCE SUB MENU INPUT BOXES-----------------------------------------------------
        ewm_warehouse_prod_maint_sub_menu_max_qty_input_box = (By.XPATH, '//div[@data-bgui-type="Input" and '
                                                                         '@title="Maximum Quantity"]' +
                                                                         '//descendant::input[1]')

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////

        # PIX TRANSACTIONS MENU OBJECTS------------------------------------------------

        # Pix Trans Menu iFrames
        pix_trans_menu_iframe = (By.XPATH, '//iframe[contains(@src, "PixTransaction")]')

        # Pix Trans Menu Fields
        pix_trans_menu_header_field = (By.XPATH, '//div[text()="PIX Transactions"]')
        pix_trans_menu_displaying_num_field = (By.XPATH, '//span[contains(text(), "Displaying")]')
        pix_trans_menu_no_data_found_field = (By.XPATH, '//td[text()="No data found"]')

        # Pix Trans Menu Buttons
        pix_trans_menu_quick_filter_button = (By.XPATH, '//span[text()="Quick filter"]')
        pix_trans_menu_saved_filters_button = (By.XPATH, '//a[text()="Saved filters"]')
        pix_trans_menu_apply_button = (By.XPATH, '//input[@id="dataForm:lview:filterId:savedapply" and @value="Apply"'
                                                 ' and @type="button"]')
        pix_trans_menu_saved_filters_submenu_apply_button = (By.XPATH, '//input[@id="dataForm:applyFltrBtnPopupAjax" '
                                                                       'and @value="Apply" and @type="button"]')
        pix_trans_menu_resend_button = (By.XPATH, '//input[@value="Resend" and @type="button" and @class="btn"]')
        pix_trans_menu_table_next_button = (By.XPATH, '//input[@alt="Next" and @type="image"]')

        # Pix Trans Menu Input Boxes
        pix_trans_menu_saved_filters_submenu_ilpn_input_box = (By.XPATH, '//input[@alt="Find Inbound LPN" and '
                                                                         '@type="text"]')
        pix_trans_menu_saved_filters_submenu_item_input_box = (By.XPATH, '//input[@id="dataForm:filterDetailId:itemLook'
                                                                         'UpId" and @type="text"]')
        pix_trans_menu_saved_filters_submenu_created_date_from_input_box = (By.XPATH, '(//input[@class="asbasinp"])[1]')
        pix_trans_menu_saved_filters_submenu_created_date_to_input_box = (By.XPATH, '(//input[@class="asbasinp"])[2]')

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

            # EWM PACKSPEC SUB MENU INPUT BOXES
            'ewm_packspec_sub_menu_product_input_box': ewm_packspec_sub_menu_product_input_box,
            'ewm_packspec_sub_menu_target_qty_input_box': ewm_packspec_sub_menu_target_qty_input_box,
            'ewm_packspec_sub_menu_pack_mat_input_box': ewm_packspec_sub_menu_pack_mat_input_box,
        }

        ewm_warehouse_prod_maint_sub_menu_d = {
            # EWM WAREHOUSE PRODUCT MAINTENANCE SUB MENU FIELDS
            'ewm_warehouse_prod_maint_sub_menu_st_type_data_field': ewm_warehouse_prod_maint_sub_menu_st_type_data_field,
            'ewm_warehouse_prod_maint_sub_menu_max_qty_input_box': ewm_warehouse_prod_maint_sub_menu_max_qty_input_box,
        }

        self.d = login_d | search_menu_d | user_profile_d | post_message_d | windows_d | uni_d | asns_menu_d | \
            schedule_appointment_menu_d | advance_ship_notice_menu_d | edit_asn_menu_d | verify_asn_menu_d | \
            sci_report_menu_d | ewm_menu_d | ewm_rf_menu_d | ewm_mon_menu_d | ewm_binmat_menu_d | \
            ewm_storage_bin_sub_menu_d | ewm_packspec_sub_menu_d | ewm_warehouse_prod_maint_sub_menu_d | \
            pix_trans_menu_d

        return self.d
