import getpass

class OsEnviron:
    
    def get_os_user(self) -> str:
        try:
            return getpass.getuser()
        except Exception as error:
            raise Exception(f"Erron in (OsEnviron) module in (get_os_user) method: {error}")
