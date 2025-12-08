import getpass

class EnvironEngine:
    
    def get_os_user(self) -> str:
        try:
            return getpass.getuser()
        except Exception as error:
            raise Exception(f"❌ Error in (EnvironEngine) engine in (get_os_user) method: {error}")
