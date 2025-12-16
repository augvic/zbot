from win32com.client import GetObject

from ..errors import *

class SapGuiClient:
    
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
    
    def init_force(self) -> None:
        try:
            gui = GetObject("SAPGUI")
            app = gui.GetScriptingEngine
            con = app.Children(0)
            session = con.Children(0)
            self.session = session
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (init_force) method: {error}.")
    
    def open_transaction(self, transaction: str) -> None:
        try:
            self.session.findById("wnd[0]/tbar[0]/okcd").text = "/N" + transaction
            self.session.findById("wnd[0]").sendVKey(0)
            status_bar = None
            status_bar = self.session.findById("wnd[0]/sbar").text
            if "Sem autorização" in status_bar:
                raise TransactionDennied(transaction)
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (open_transaction) method: {error}.")
    
    def go_home(self) -> None:
        try:
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
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (go_home) method: {error}.")
    
    def press_enter(self, index: str) -> None:
        try:
            self.session.findById(rf"wnd[{index}]").sendVKey(0)
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (press_enter) method: {error}.")
    
    def press_back(self, index: str) -> None:
        try:
            self.session.findById(rf"wnd[{index}]/tbar[0]/btn[3]").press()
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (press_back) method: {error}.")
    
    def press_go(self, index: str) -> None:
        try:
            self.session.findById(rf"wnd[{index}]").sendVKey(2)
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (press_go) method: {error}.")
    
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
        try:
            self.session.findById(f"wnd[{index}]").sendVKey(4)
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (open_search_window) method: {error}.")
    
    def get_msg_bar_log(self, index: str) -> str:
        try:
            return self.session.findById(f"wnd[{index}]/sbar").text
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (get_msg_bar_log) method: {error}.")
    
    def get_icon_name(self, id: str) -> str:
        try:
            return self.session.findById(id).IconName
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (get_icon_name) method: {error}.")
    
    def set_selection_indexes(self, id: str, indexes: tuple[int, int]) -> None:
        try:
            self.session.findById(id).setSelectionIndexes(*indexes)
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (set_selection_indexes) method: {error}.")
    
    def select_item(self, id: str, indexes: tuple[str, str]) -> None:
        try:
            self.session.findById(id).selectItem(*indexes)
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (select_item) method: {error}.")
    
    def ensure_visible_horizontal_item(self, id: str, indexes: tuple[str, str]) -> None:
        try:
            self.session.findById(id).ensureVisibleHorizontalItem(*indexes)
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (ensure_visible_horizontal_item) method: {error}.")
    
    def double_click_item(self, id: str, indexes: tuple[str, str]) -> None:
        try:
            self.session.findById(id).doubleClickItem(*indexes)
        except Exception as error:
            raise Exception(f"❌ Error in (SapGuiClient) in (double_click_item) method: {error}.")
