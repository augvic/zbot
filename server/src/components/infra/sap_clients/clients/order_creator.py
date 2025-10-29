from dateutil.relativedelta import relativedelta
from datetime import datetime
from .sap_gui import SapGui
from ..errors import *
from ..models import *

class OrderCreator(SapGui):
    
    def _open_transaction(self, order: Order, is_create_transaction: bool) -> None:
        if order.doc_type == "ZCOT":
            if is_create_transaction:
                self.open_transaction("VA21")
            else:
                self.open_transaction("VA22")
        else:
            if is_create_transaction:
                self.open_transaction("VA01")
            else:
                self.open_transaction("VA02")
    
    def _fill_out_the_creation_form(self, order: Order) -> None:
        self.set_text(r"wnd[0]/usr/ctxtVBAK-AUART", order.doc_type)
        self.set_text(r"wnd[0]/usr/ctxtVBAK-VKORG", order.organization) 
        self.set_text(r"wnd[0]/usr/ctxtVBAK-VTWEG", order.channel)
        self.set_text(r"wnd[0]/usr/ctxtVBAK-SPART", "00")
        self.set_text(r"wnd[0]/usr/ctxtVBAK-VKBUR", order.office)
        self.set_text(r"wnd[0]/usr/ctxtVBAK-VKGRP", order.team)
        self.press_enter("0")
    
    def _fill_out_sales_name(self, order: Order) -> None:
        self.set_text(r"wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/txtVBKD-BSTKD", order.order_name)
    
    def _fill_out_sales_date(self) -> None:
        self.set_text(r"wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/ctxtVBKD-BSTDK", datetime.now().strftime("%d.%m.%Y")) 
    
    def _fill_out_issuer(self, order: Order) -> None:
        self.set_text(r"wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/subPART-SUB:SAPMV45A:4701/ctxtKUAGV-KUNNR", order.issuer)
    
    def _fill_out_receiver(self, order: Order) -> None:
        self.set_text(r"wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/subPART-SUB:SAPMV45A:4701/ctxtKUWEV-KUNNR", order.receiver)
    
    def _fill_out_validity(self) -> None:
        validity = datetime.now() + relativedelta(months=1)
        validity = validity.strftime("%d.%m.%Y")
        self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\01/ssubSUBSCREEN_BODY:SAPMV45A:4400/ssubHEADER_FRAME:SAPMV45A:4440/ctxtVBAK-BNDDT", validity)
    
    def _fill_out_payment_condition(self, order: Order) -> None:
        self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\01/ssubSUBSCREEN_BODY:SAPMV45A:4400/ssubHEADER_FRAME:SAPMV45A:4440/ctxtVBKD-ZTERM", order.payment_condition)
    
    def _fill_out_incoterm(self, order: Order) -> None:
        self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\01/ssubSUBSCREEN_BODY:SAPMV45A:4400/ssubHEADER_FRAME:SAPMV45A:4440/ctxtVBKD-INCO1", order.incoterm) 
    
    def _fill_out_reason(self, order: Order) -> None:
        self.set_key(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\01/ssubSUBSCREEN_BODY:SAPMV45A:4400/ssubHEADER_FRAME:SAPMV45A:4440/cmbVBAK-AUGRU", order.reason)
    
    def _check_full_supply(self) -> None:
        self.check_field(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\01/ssubSUBSCREEN_BODY:SAPMV45A:4400/ssubHEADER_FRAME:SAPMV45A:4440/chkVBAK-AUTLF")
    
    def _go_to_header(self) -> None:
        self.press_button(r"wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/btnBT_HEAD")
    
    def _fill_out_table(self, order: Order) -> None:
        self.set_key(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\01/ssubSUBSCREEN_BODY:SAPMV45A:4301/cmbVBKD-PLTYP", order.table)
        self.press_enter("0")
    
    def _go_to_tab_expedition(self) -> None:
        self.select_tab(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\02")
    
    def _fill_out_expedition(self, order: Order) -> None:
        self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\02/ssubSUBSCREEN_BODY:SAPMV45A:4302/ctxtVBKD-VSART", order.expedition)
        self.press_enter("0")
    
    def _go_to_tab_contability(self) -> None:
        self.select_tab(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\05")
    
    def _fill_out_payment_way(self, order: Order) -> None:
        self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\05/ssubSUBSCREEN_BODY:SAPMV45A:4311/ctxtVBKD-ZLSCH", order.payment_way)
        self.press_enter("0")
    
    def _go_to_tab_partners(self) -> None:
        self.select_tab(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\08")
    
    def _fill_out_partners(self, order: Order) -> None:
        for partner in order.partners:
            for row in range(0, 20):
                key = self.get_key(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\08/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/cmbGVS_TC_DATA-REC-PARVW[0,{row}]")
                if key == " ":
                    self.set_key(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\08/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/cmbGVS_TC_DATA-REC-PARVW[0,{row}]", partner.key)
                    self.set_text(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\08/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,{row}]", partner.code)
                    break
        self.press_enter("0")
        self.press_enter("0")
    
    def _go_to_tab_additional_data(self) -> None:
        self.select_tab(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\09")
    
    def _fill_out_additional_data(self, order: Order) -> None:
        self.set_selection_indexes(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\09/ssubSUBSCREEN_BODY:SAPMV45A:4152/subSUBSCREEN_TEXT:SAPLV70T:2100/cntlSPLITTER_CONTAINER/shellcont/shellcont/shell/shellcont[1]/shell", (0, 0))
        self.select_item(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\09/ssubSUBSCREEN_BODY:SAPMV45A:4152/subSUBSCREEN_TEXT:SAPLV70T:2100/cntlSPLITTER_CONTAINER/shellcont/shellcont/shell/shellcont[0]/shell", ("9002", "Column1"))
        self.ensure_visible_horizontal_item(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\09/ssubSUBSCREEN_BODY:SAPMV45A:4152/subSUBSCREEN_TEXT:SAPLV70T:2100/cntlSPLITTER_CONTAINER/shellcont/shellcont/shell/shellcont[0]/shell", ("9002", "Column1"))
        self.double_click_item(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\09/ssubSUBSCREEN_BODY:SAPMV45A:4152/subSUBSCREEN_TEXT:SAPLV70T:2100/cntlSPLITTER_CONTAINER/shellcont/shellcont/shell/shellcont[0]/shell", ("9002", "Column1"))
        self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\09/ssubSUBSCREEN_BODY:SAPMV45A:4152/subSUBSCREEN_TEXT:SAPLV70T:2100/cntlSPLITTER_CONTAINER/shellcont/shellcont/shell/shellcont[1]/shell", order.additional_data)
        self.set_selection_indexes(r"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\09/ssubSUBSCREEN_BODY:SAPMV45A:4152/subSUBSCREEN_TEXT:SAPLV70T:2100/cntlSPLITTER_CONTAINER/shellcont/shellcont/shell/shellcont[1]/shell", (0, 0))
        self.press_enter("0")
    
    def _go_to_tab_items_summary(self) -> None:
        self.select_tab(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02")
    
    def _fill_out_items(self, order: Order) -> None:
        row = 0
        for item in order.items:
            if item.is_parent_item:
                self.set_text(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02/ssubSUBSCREEN_BODY:SAPMV45A:4401/subSUBSCREEN_TC:SAPMV45A:4900/tblSAPMV45ATCTRL_U_ERF_AUFTRAG/ctxtRV45A-MABNR[1,{row}]", item.sku)
                self.set_text(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02/ssubSUBSCREEN_BODY:SAPMV45A:4401/subSUBSCREEN_TC:SAPMV45A:4900/tblSAPMV45ATCTRL_U_ERF_AUFTRAG/txtRV45A-KWMENG[2,{row}]", item.quantity)
                self.set_text(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02/ssubSUBSCREEN_BODY:SAPMV45A:4401/subSUBSCREEN_TC:SAPMV45A:4900/tblSAPMV45ATCTRL_U_ERF_AUFTRAG/ctxtVBAP-WERKS[13,{row}]", item.center)
                self.set_text(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02/ssubSUBSCREEN_BODY:SAPMV45A:4401/subSUBSCREEN_TC:SAPMV45A:4900/tblSAPMV45ATCTRL_U_ERF_AUFTRAG/ctxtVBAP-LGORT[3,{row}]", item.deposit)
                row += 1
        self.press_enter("0")
    
    def _confirm_technical_list(self) -> None:
        self.focus(r"wnd[1]/usr/tblSAPMC29ACNTL/txtRC29K-STKTX[1,0]")
        self.press_go("1")
    
    def _access_item(self, item_row: int) -> None:
        self.focus(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02/ssubSUBSCREEN_BODY:SAPMV45A:4401/subSUBSCREEN_TC:SAPMV45A:4900/tblSAPMV45ATCTRL_U_ERF_AUFTRAG/ctxtRV45A-MABNR[1,{item_row}]")
        self.press_go("0")
    
    def _access_additional_data_b(self) -> None:
        self.select_tab(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\15")
    
    def _fill_out_guarantee(self, item: Item) -> None:
        self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\15/ssubSUBSCREEN_BODY:SAPMV45A:4462/subKUNDEN-SUBSCREEN_8459:SAPMV45A:8459/ctxtVBAP-ZZCDguaranteeEXT", item.guarantee)
    
    def _acess_tab_conditions(self) -> None:
        self.select_tab(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06")
    
    def _update_in_b(self) -> None:
        self.press_button(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/subSUBSCREEN_PUSHBUTTONS:SAPLV69A:1000/btnBT_KONY")
        self.focus(r"wnd[1]/usr/lbl[1,4]")
        self.press_go("1")
    
    def _fill_out_over(self, item: Item) -> None:
        self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,11]", item.over)
    
    def _fill_out_unit_value(self, value: str) -> None:
        self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,2]", value)
    
    def _fill_out_zd15(self, difference: float) -> None:
        if difference < 0:
            difference = abs(difference)
        else:
            difference = -abs(difference)
        for row in range(70, 90):
            self.vertical_scroll_position(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN", row)
            zd15 = self.get_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/ctxtKOMV-KSCHL[1,0]")
            if zd15 == "ZD15":
                field_value = self.get_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,0]").replace(".", "").replace(",", ".")
                if field_value !=  "":
                    field_value = str(field_value).replace(",", ".")
                    if field_value.endswith("-"):
                        field_value = field_value.split("-")[0]
                        field_value = f"-{field_value}"
                    field_value = float(field_value)
                    difference += field_value
                new_difference = str(difference).replace(".", ",")
                self.set_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,0]", new_difference)
                break
    
    def _unit_value_adjustment_loop(self, item: Item) -> None:
        self._fill_out_unit_value(str(item.unit_value).replace(".", ","))
        self.press_enter("0")
        while True:
            net_value = float(str(self.get_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/txtKOMP-NETWR")).replace(".", "").replace(",", ".").strip())
            tax_value = float(str(self.get_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/txtKOMP-MWSBP")).replace(".", "").replace(",", ".").strip())
            net_tax_sum = round((net_value + tax_value) / float(item.quantity), 2)
            if net_tax_sum != float(item.unit_value):
                difference = round(net_tax_sum - float(item.unit_value), 2)
                if 0 < difference <= 0.01 or -0.01 < difference <= 0:
                    self._fill_out_zd15(difference) 
                else:
                    field_value = float(str(self.get_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,2]")).replace(".", "").replace(",", ".").strip())
                    new_value = round(field_value - difference, 2)
                    self._fill_out_unit_value(str(new_value).replace(".", ",")) 
                self.press_enter("0")
            else:
                break
    
    def _total_value_adjustment_loop(self, item: Item) -> None:
        while True:
            net_value = float(str(self.get_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/txtKOMP-NETWR")).replace(".", "").replace(",", ".").strip())
            tax_value = float(str(self.get_text(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/txtKOMP-MWSBP")).replace(".", "").replace(",", ".").strip())
            net_tax_sum = round(net_value + tax_value, 2)
            if net_tax_sum != float(item.total_value):
                difference = round(net_tax_sum - float(item.total_value), 2)
                self._fill_out_zd15(difference)
                self.press_enter("0")
            else:
                break
    
    def _fill_out_items_values_guarantee(self, order: Order) -> None:
        row = 0
        for item in order.items:
            self._access_item(row)    
            self._access_additional_data_b()
            if item.guarantee:
                self._fill_out_guarantee(item)
                self.press_enter("0")
                self.press_enter("0")
            self._acess_tab_conditions()
            self._update_in_b()
            if item.over:
                self._fill_out_over(item)
            self._unit_value_adjustment_loop(item)
            self._total_value_adjustment_loop(item)
            self.press_back("0")
            row += 1
    
    def _add_comission_button(self) -> None:
        self.press_button(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\15/ssubSUBSCREEN_BODY:SAPMV45A:4462/subKUNDEN-SUBSCREEN_8459:SAPMV45A:8459/btnPB_ADD")
    
    def _reply_comission(self) -> None:
        self.press_button(r"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\15/ssubSUBSCREEN_BODY:SAPMV45A:4462/subKUNDEN-SUBSCREEN_8459:SAPMV45A:8459/btnBT_REPL_COMISS")
        self.press_button(r"wnd[1]/usr/btnBUTTON_1")
        self.press_button(r"wnd[1]/tbar[0]/btn[0]")
    
    def _fill_out_comission(self, order: Order) -> None:
        self._access_item(0)
        self._access_additional_data_b()
        row = 0
        for comission in order.comissions:
            self._add_comission_button()            
            self.set_key(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\15/ssubSUBSCREEN_BODY:SAPMV45A:4462/subKUNDEN-SUBSCREEN_8459:SAPMV45A:8459/tblSAPMV45ATC_TABCOMISS/cmbTG_TABCOM-PARVW[0,{row}]", comission.key)
            self.set_text(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\15/ssubSUBSCREEN_BODY:SAPMV45A:4462/subKUNDEN-SUBSCREEN_8459:SAPMV45A:8459/tblSAPMV45ATC_TABCOMISS/ctxtTG_TABCOM-LIFNR[1,{row}]", comission.code)
            self.set_text(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\15/ssubSUBSCREEN_BODY:SAPMV45A:4462/subKUNDEN-SUBSCREEN_8459:SAPMV45A:8459/tblSAPMV45ATC_TABCOMISS/txtTG_TABCOM-KBETR[3,{row}]", comission.percentage)
            row += 1
        self.press_enter("0")
        self._reply_comission()
    
    def _get_order_id(self, order: Order) -> str:
        self._open_transaction(order, is_create_transaction=False)
        return str(self.get_text(r"wnd[0]/usr/ctxtVBAK-VBELN"))
    
    def _save_order(self) -> None:
        self.press_button(r"wnd[0]/tbar[0]/btn[11]")
        try:
            self.press_button(r"wnd[0]/tbar[1]/btn[18]")
        except:
            pass
        msg_bar = self.get_text(r"wnd[0]/sbar")
        if "sem garantia" in msg_bar:
            raise GuaranteeError()
        elif "Não foi efetuada" in msg_bar:
            return
        elif "foi gravado" in msg_bar:
            return
        else:
            self.press_enter("0")
            try:
                self.press_button(r"wnd[1]/usr/btnSPOP-VAROPTION1")
            except:
                pass
            return
    
    def _fill_out_initial_data(self, order: Order) -> None:
        self._open_transaction(order, True)
        self._fill_out_the_creation_form(order)
    
    def _fill_out_sales_data(self, order: Order) -> None:
        self._fill_out_sales_name(order)
        self._fill_out_sales_date()
        self._fill_out_issuer(order)
        self._fill_out_receiver(order)
        try:
            self._fill_out_validity()    
        except:
            pass
        self._fill_out_payment_condition(order)
        self._fill_out_incoterm(order)
        self._fill_out_reason(order)
        self.press_enter("0")
        self.press_enter("0")
        self.press_enter("0")
        self._check_full_supply()
    
    def _fill_out_header(self, order: Order) -> None:
        self._go_to_header()
        if order.table:
            self._fill_out_table(order)        
        self._go_to_tab_expedition()
        self._fill_out_expedition(order)
        self._go_to_tab_contability()
        self._fill_out_payment_way(order)
        if order.partners:
            self._go_to_tab_partners()
            self._fill_out_partners(order)
        if order.additional_data:
            self._go_to_tab_additional_data()
            self._fill_out_additional_data(order)
        self.press_back("0")
    
    def _fill_out_items_summary(self, order: Order) -> None:
        self._go_to_tab_items_summary()
        self._fill_out_items(order)
        try:
            self._confirm_technical_list()
        except:
            pass
        self._fill_out_items_values_guarantee(order)
        self._fill_out_comission(order)
    
    def create(self, order: Order) -> str:
        self.init()
        self._fill_out_initial_data(order)
        self._fill_out_sales_data(order)
        self._fill_out_header(order)
        self._fill_out_items_summary(order)
        self._save_order()
        id = self._get_order_id(order)
        self.go_home()
        return id
