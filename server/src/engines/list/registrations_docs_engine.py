from os import makedirs, path
import sys

from werkzeug.datastructures import FileStorage

class RegistrationsDocsEngine:

    def save_docs(self, cnpj: str, docs: list[FileStorage]) -> None:
        try:
            if getattr(sys, 'frozen', False):
                base_path = path.dirname(sys.executable)
            else:
                base_path = path.join(path.dirname(__file__), "..", "..")
            dir_to_create = path.abspath(path.join(base_path, "storage", ".clients_docs", cnpj))
            makedirs(dir_to_create, exist_ok=True)
            for doc in docs:
                doc.save(f"{dir_to_create}/{doc.filename}")
        except Exception as error:
            raise Exception(f"❌ Error in (RegistrationsDocsEngine) in (save_docs) method: {error}")
