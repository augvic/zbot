from .sap_gui import SapGui
from src.infrastructure.sap_clients.models import *
from datetime import datetime, timedelta, date
from re import sub
from pandas import DataFrame, concat
from ..types import *

class FinancialDataGetter(SapGui):
    
    def _set_defaults_variables(self) -> None:
        self.payment_ways_to_ignore = [
            "7",
            "2",
            "M",
            "G",
            "J",
            "Z",
            "V",
            "A",
            "P",
            "S",
            "*"
        ]
        self.payment_conditions_to_ignore = [
            "0001",
            "0002",
            "Z576",
            "Z577"
        ]
        self.strings_to_ignore = [
            "NEGOCIADO",
            "negociado",
            "CONCILIACAO",
            "conciliacao",
            "CONCILIAÇÃO",
            "conciliação",
            "CONCILIAÇÃO CR",
            "conciliação cr",
            "CONCILIACAO CR",
            "conciliacao cr",
            "NAO COBRAR",
            "nao cobrar",
            "NÃO COBRAR",
            "não cobrar",
            "EXTRAVIO",
            "extravio",
            "DEVOLUÇÃO",
            "devolução",
            "DEVOLUCAO",
            "devolucao",
            "EM DEVOLUCAO",
            "em devolucao",
            "EM DEVOLUÇÃO",
            "em devolução",
            "EM DEV",
            "em dev"
        ]
    
    def _get_data(self, cnpj_root: str) -> FinancialDict:
        limit, maturity = self._get_fd33_data(cnpj_root=cnpj_root)
        fbl5n_table = self._get_fbl5n_data(cnpj_root=cnpj_root)
        dict: FinancialDict = {
            "limit": limit,
            "maturity": maturity,
            "fbl5n_table": fbl5n_table
        }
        return dict
    
    def _fill_out_fd33_form(self, cnpj_root: str) -> None:
        self.open_search_window("0")
        self.select_tab("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB006")
        i = 1
        while True:
            self.set_text("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB006/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[0,24]", "")
            self.set_text("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB006/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[0,24]", f"{cnpj_root}000{i}*")
            self.press_button("wnd[1]/tbar[0]/btn[0]")
            msg_bar = self.get_msg_bar_log("0")
            if "Nenhum value para esta seleção" in msg_bar:
                i += 1
            else:
                break
        self.press_go("1")
        self.set_text("wnd[0]/usr/ctxtRF02L-KKBER", "1000")
        self.check_field("wnd[0]/usr/chkRF02L-D0210")
        self.press_enter("0")
    
    def _get_fd33_data(self, cnpj_root: str) -> tuple[float, date | str]:
        self.open_transaction("FD33")
        self._fill_out_fd33_form(cnpj_root=cnpj_root)
        limit = self.get_text("wnd[0]/usr/txtKNKK-KLIMK")
        limit = limit.replace(".", "").replace(",", ".")
        limit = float(limit)
        maturity = self.get_text("wnd[0]/usr/ctxtKNKK-NXTRV")
        if not maturity == "":
            maturity = datetime.strptime(maturity, "%d.%m.%Y").date()
        else:
            limit = 0.0
            maturity = "Sem limite ativo."
        return limit, maturity
    
    def _get_fbl5n_data(self, cnpj_root: str) -> list[dict[str, str]]:
        accounts = self._get_fbl5n_accounts(cnpj_root=cnpj_root)
        table = self._make_fbl5n_table(accounts=accounts, companies=["1000", "3500"])
        return table
    
    def _get_fbl5n_accounts(self, cnpj_root: str) -> list[str]:
        self.open_transaction("FBL5N")
        self.press_button("wnd[0]/tbar[1]/btn[17]")
        self.set_text("wnd[1]/usr/txtENAME-LOW", "72776")
        self.press_button("wnd[1]/tbar[0]/btn[8]")
        self.open_search_window("0")
        self.select_tab("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB006")
        self.set_text("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB006/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[0,24]", f"{cnpj_root}*")
        self.press_enter("1")
        accounts: list[str] = []
        for row in range(3, 50):
            try:
                account = self.get_text(f"wnd[1]/usr/lbl[119,{row}]")
            except:
                continue
            if account != "":
                accounts.append(account)
            else:
                break
        self.press_button("wnd[1]/tbar[0]/btn[0]")
        return accounts
    
    def _fill_out_fbl5n_initial(self, account: str, company: str) -> None:
        self.set_text("wnd[0]/usr/ctxtDD_KUNNR-LOW", account)
        self.set_text("wnd[0]/usr/ctxtDD_BUKRS-LOW", company)
    
    def _get_search_way(self) -> str:
        for row in range(10, 100):
            try:
                cell = self.get_text(f"wnd[0]/usr/lbl[0,{row}]")
                if cell == " Cliente":
                    return "ESTÁTICO"
            except:
                continue
        return "SCROLL"
    
    def _get_fbl5n_row(self, row: int, account: str) -> dict[str, str] | str:
        row_dict: dict[str, str] = {}
        try:
            situation = self.get_icon_name(f"wnd[0]/usr/lbl[6,{row}]")
        except:
            self.press_back("0")
            return "break"
        if situation != "S_LEDR":
            self.press_back("0")
            return "break"
        due_date = self.get_text(f"wnd[0]/usr/lbl[9,{row}]")
        due_date = self._extract_data(due_date)
        try:
            datetime.strptime(due_date, "%d/%m/%Y")
        except:
            due_date = self.get_text(f"wnd[0]/usr/lbl[28,{row}]")
            due_date = str(due_date).replace(".", "/")
        result = self._verify_bill_due(due_date)
        if result == "Vencido":
            situation = "Vencido"
        else:
            situation = "No prazo"
        nf = self.get_text(f"wnd[0]/usr/lbl[45,{row}]")
        assignment = self.get_text(f"wnd[0]/usr/lbl[9,{row}]")
        text = self.get_text(f"wnd[0]/usr/lbl[81,{row}]")
        if any(searched_text in assignment for searched_text in self.strings_to_ignore) or any(searched_text in text for searched_text in self.strings_to_ignore):
            situation = "Outros"
        value = self.get_text(f"wnd[0]/usr/lbl[62,{row}]")
        value = value.replace(" ", "")
        if value.endswith("-"):
            value = "-" + value[:-1]
            situation = "Crédito"
        payment_way = self.get_text(f"wnd[0]/usr/lbl[39,{row}]")
        payment_condition = self.get_text(f"wnd[0]/usr/lbl[132,{row}]")
        if payment_way in self.payment_ways_to_ignore or payment_condition in self.payment_conditions_to_ignore:
            if not situation == "Crédito":
                return "skip"
        row_dict["CONTA"] = account
        row_dict["SITUAÇÃO"] = situation
        row_dict["FRM_PAGAMENTO"] = payment_way
        row_dict["CND_PAGAMENTO"] = payment_condition
        row_dict["VENCIMENTO"] = due_date
        row_dict["NF"] = nf
        row_dict["VALOR"] = value
        return row_dict
    
    def _extract_data(self, due_date: str) -> str:
        numbers = sub(r"\D", "", due_date)
        if len(numbers) == 6:
            day, month, year = numbers[:2], numbers[2:4], numbers[4:]
            year = f"20{year}"
            return f"{day}/{month}/{year}"
        elif len(numbers) == 8:
            return f"{numbers[:2]}/{numbers[2:4]}/{numbers[4:]}"
        else:
            return due_date
    
    def _make_fbl5n_table(self, accounts: list[str], companies: list[str]) -> list[dict[str, str]]:
        fbl5n_table: list[dict[str, str]] = []
        for account in accounts:
            for company in companies:
                scroll_position = 0
                row = 10
                self._fill_out_fbl5n_initial(account=account, company=company)
                self.press_button("wnd[0]/tbar[1]/btn[8]")
                msg_bar = self.get_msg_bar_log("0")
                if msg_bar not in ["Nenhuma partida selecionada (ver texto descritivo)", "Nenhuma conta preenche as condições de seleção"]:
                    search_way = self._get_search_way()
                    while True:
                        self.vertical_scroll_position("wnd[0]/usr", scroll_position)
                        row_data = self._get_fbl5n_row(row=row, account=account)
                        if row_data == "break":
                            break
                        elif row_data != "skip":
                            if isinstance(row_data, dict):
                                fbl5n_table.append(row_data)
                        if search_way == "SCROLL":
                            scroll_position += 1
                        else:
                            row += 1
        return fbl5n_table
    
    def _convert_table_to_df(self, fbl5n_table: list[dict[str, str]]) -> DataFrame:
        df = DataFrame(fbl5n_table)
        df["VALOR"] = df["VALOR"].str.replace(".", "").str.replace(",", ".")
        df["VALOR"] = df["VALOR"].astype(float)
        total_sum = df.loc[df["SITUAÇÃO"] != "Outros", "VALOR"].sum()
        in_open = float(total_sum)
        in_open_str = f"R$ {in_open:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        df["VALOR"] = df["VALOR"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        new_line = DataFrame({"CONTA": [""], "SITUAÇÃO": [""], "FRM_PAGAMENTO": [""], "CND_PAGAMENTO": [""], "VENCIMENTO": [""], "NF": ["TOTAL"], "VALOR": [in_open_str]})
        df = concat([df, new_line])
        return df
    
    def _get_in_open_from_df(self, df: DataFrame) -> float:
        df["VALOR"] = df["VALOR"].apply(lambda x: float(x.replace("R$", "").replace(".", "").replace(",", ".")))
        in_open = float(df.loc[df["SITUAÇÃO"] != "Outros", "VALOR"].iloc[:-1].sum())
        df["VALOR"] = df["VALOR"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        return in_open
    
    def _get_overdue_nfs_from_df(self, df: DataFrame) -> str:
        overdue_nfs = ""
        total_rows = df.shape[0]
        for row in range(0, total_rows):
            if df.iloc[row]["SITUAÇÃO"] == "Vencido":
                if overdue_nfs == "":
                    overdue_nfs += df.iloc[row]["NF"]
                else:
                    overdue_nfs += " | " + df.iloc[row]["NF"]
        if overdue_nfs == "":
            overdue_nfs = "Sem vencidos."
        return overdue_nfs
    
    def _sanitize_financial_data(self, data: FinancialDict) -> CleanedFinancialDict:
        if data["fbl5n_table"]:
            fbl5n_table = self._convert_table_to_df(data["fbl5n_table"])
            in_open = self._get_in_open_from_df(fbl5n_table)
            overdue_nfs = self._get_overdue_nfs_from_df(fbl5n_table)
        else:
            fbl5n_table = None
            overdue_nfs = "Sem vencidos."
            in_open = 0.0
        margin = data["limit"] - in_open
        if data["limit"] == 0.0 or data["maturity"] == "Sem limite ativo.":
            limit = "Sem limite ativo."
            maturity = "Sem limite ativo."
        else:
            limit = data["limit"]
            maturity = data["maturity"]
        if in_open == 0.0:
            in_open = "Sem valores em aberto."
        if margin <= 0.0:
            margin = "Sem margem disponível."
        cleaned_dict: CleanedFinancialDict = {
            "fbl5n_table": fbl5n_table,
            "in_open": in_open,
            "overdue_nfs": overdue_nfs,
            "limit": limit,
            "maturity": maturity,
            "margin": margin
        }
        return cleaned_dict
    
    def _verify_bill_due(self, bill_date: str) -> str:
        new_bill_date = datetime.strptime(bill_date, "%d/%m/%Y").date()
        now = datetime.now().date()
        if new_bill_date < now:
            days_overdue = 0
            new_bill_date = new_bill_date + timedelta(days=1)
            while new_bill_date < now:
                if new_bill_date.weekday() < 5:
                    days_overdue += 1
                new_bill_date = new_bill_date + timedelta(days=1)
            if days_overdue >= 2:
                return "Vencido"
            else:
                return "Não vencido"
        else:
            return "Não vencido"
    
    def get_data(self, cnpj_root: str) -> FinancialData:
        self.init()
        self._set_defaults_variables()
        data = self._get_data(cnpj_root=cnpj_root)
        sanitized_data = self._sanitize_financial_data(data=data)
        self.go_home()
        return FinancialData(
            cnpj_root = cnpj_root,
            limit = sanitized_data["limit"],
            maturity = sanitized_data["maturity"],
            in_open = sanitized_data["in_open"],
            margin = sanitized_data["margin"],
            overdue_nfs = sanitized_data["overdue_nfs"],
            fbl5n_table = sanitized_data["fbl5n_table"]
        )
