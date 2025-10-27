from win32com.client import GetObject
from ..errors import *

class SapGui:
    
    def init(self) -> None:
        try:
            gui = GetObject("SAPGUI")
            app = gui.GetScriptingEngine
            con = app.Children(0)
        except:
            raise NotLogged()
        for id in range(0, 7):
            try:
                session = con.Children(id)
                if "SAP Easy Access" in session.ActiveWindow.Text:
                    self.session = session
                    return
                else:
                    continue
            except:
                pass
        else:
            raise WindowBusy()
    
    def open_transaction(self, transaction: str) -> None:
        self.session.findById("wnd[0]/tbar[0]/okcd").text = "/N" + transaction
        self.session.findById("wnd[0]").sendVKey(0)
        status_bar = None
        status_bar = self.session.findById("wnd[0]/sbar").text
        if "Sem autorização" in status_bar:
            raise TransactionDennied(transaction)
    
    def go_home(self) -> None:
        while True:
            if self.session.ActiveWindow.Text == "SAP Easy Access":
                break
            else:
                try:
                    self.session.findById("wnd[1]").close()
                except:
                    pass
                try:
                    self.session.findById("wnd[0]").sendVKey(3)
                except:
                    pass
                try:
                    self.session.findById("wnd[1]/usr/btnSPOP-OPTION2").press()
                except:
                    pass
    
    def press_enter(self, index: str) -> None:
        self.session.findById(rf"wnd[{index}]").sendVKey(0)
    
    def press_back(self, index: str) -> None:
        self.session.findById(rf"wnd[{index}]/tbar[0]/btn[3]").press()
    
    def press_go(self, index: str) -> None:
        self.session.findById(rf"wnd[{index}]").sendVKey(2)
    
    def set_text(self, id: str, text: str) -> None:
        try:
            self.session.findById(id).text = text
        except:
            raise IdNotFound(id)
    
    def get_text(self, id: str) -> str:
        try:
            return self.session.findById(id).text
        except:
            raise IdNotFound(id)
    
    def set_key(self, id: str, key: str) -> None:
        try:
            self.session.findById(id).key = key
        except:
            raise IdNotFound(id)
    
    def get_key(self, id: str) -> str:
        try:
            return self.session.findById(id).key
        except:
            raise IdNotFound(id)
    
    def check_field(self, id: str) -> None:
        try:
            self.session.findById(id).Selected = True
        except:
            raise IdNotFound(id)
    
    def press_button(self, id: str) -> None:
        try:
            self.session.findById(id).press()
        except:
            raise IdNotFound(id)
    
    def focus(self, id: str) -> None:
        try:
            self.session.findById(id).setFocus()
        except:
            raise IdNotFound(id)
    
    def vertical_scroll_position(self, id: str, position: int) -> None:
        try:
            self.session.findById(id).verticalScrollbar.position = position
        except:
            raise IdNotFound(id)
    
    def select_tab(self, id: str) -> None:
        try:
            self.session.findById(id).select()
        except:
            raise IdNotFound(id)
    
    def open_search_window(self, index: str) -> None:
        self.session.findById(f"wnd[{index}]").sendVKey(4)
    
    def get_msg_bar_log(self, index: str) -> str:
        return self.session.findById(f"wnd[{index}]/sbar").text
    
    def get_icon_name(self, id: str) -> str:
        return self.session.findById(id).IconName
    
    def set_selection_indexes(self, id: str, indexes: tuple[int, int]) -> None:
        self.session.findById(id).setSelectionIndexes(*indexes)
    
    def select_item(self, id: str, indexes: tuple[str, str]) -> None:
        self.session.findById(id).selectItem(*indexes)
    
    def ensure_visible_horizontal_item(self, id: str, indexes: tuple[str, str]) -> None:
        self.session.findById(id).ensureVisibleHorizontalItem(*indexes)
    
    def double_click_item(self, id: str, indexes: tuple[str, str]) -> None:
        self.session.findById(id).doubleClickItem(*indexes)
