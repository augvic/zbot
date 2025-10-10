from src.infrastructure.go_deep_clients.models import *
from src.infrastructure.go_deep_clients.errors import *
from .go_deep_browser import GoDeepBrowser
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class OrderInteractor(GoDeepBrowser):
    
    def _get_seller_from_resalers(self, cnpj: str) -> str:
        self.get(url="https://www.revendedorpositivo.com.br/admin/clients")
        sleep(1)
        search_input = self.find_element(by=By.ID, value="keyword") 
        search_input.clear()
        search_input.send_keys(cnpj)
        search_input.send_keys(Keys.ENTER)
        sleep(1)
        client_link = self.find_elements(by=By.XPATH, value="//table/tbody/tr")[1].find_elements(By.XPATH, value=".//td")[10].find_element(By.XPATH, value=".//a") 
        client_link = client_link.get_attribute(name="href")
        self.get(url=str(client_link))
        sleep(1)
        wallet = self.find_element(by=By.XPATH, value="//section").find_elements(by=By.XPATH, value=".//ul/li")[10].find_element(by=By.XPATH, value=".//a")
        wallet.click()
        sleep(1)
        wallet = self.find_element(by=By.XPATH, value="(//select[@class='form-control select-multiple side2side-selected-options side2side-select-taller'])[1]")
        wallet = Select(wallet)
        wallet = wallet.options
        seller = wallet[0].text
        return seller
    
    def _get_seller_from_billing_clients(self, cnpj: str, active: bool) -> str:
        self.get(url="https://www.revendedorpositivo.com.br/admin/direct-billing-clients")
        sleep(1)
        search_input = self.find_element(by=By.ID, value="keyword") 
        search_input.clear() 
        search_input.send_keys(cnpj)
        if active:
            flag = self.find_element(by=By.ID, value="active-1")
        else:
            flag = self.find_element(by=By.ID, value="active-0")
        flag.click()
        search_input.send_keys(Keys.ENTER)
        sleep(1)
        client_link = self.find_elements(by=By.XPATH, value="//table/tbody/tr")[1].find_element(by=By.XPATH, value="//td[contains(@data-title, 'Ações')]/a").get_attribute(name="href")
        self.get(url=str(client_link))
        resale_cnpj = self.find_element(by=By.ID, value="resale_cnpj").get_attribute(name="value")
        self.get("https://www.revendedorpositivo.com.br/admin/clients")
        search_input = self.find_element(by=By.ID, value="keyword")
        search_input.clear()
        if resale_cnpj:
            search_input.send_keys(resale_cnpj) 
        search_input.send_keys(Keys.ENTER)
        sleep(1)
        client_link = self.find_elements(by=By.XPATH, value="//table/tbody/tr")[1].find_elements(by=By.XPATH, value=".//td")[10].find_element(by=By.XPATH, value=".//a") 
        client_link = client_link.get_attribute(name="href") 
        self.get(url=str(client_link)) 
        sleep(1)
        wallet = self.find_element(by=By.XPATH, value="//section").find_elements(by=By.XPATH, value=".//ul/li")[10].find_element(by=By.XPATH, value=".//a") 
        wallet.click() 
        wallet = self.find_element(by=By.XPATH, value="(//select[@class='form-control select-multiple side2side-selected-options side2side-select-taller'])[1]") 
        wallet = Select(wallet) 
        wallet = wallet.options 
        seller = wallet[0].text
        return seller
    
    def _extract_order_date(self) -> str:
        return self.find_element(by=By.XPATH, value="//label[@for='order_date']/following-sibling::div[@class='col-md-12']").text
    
    def _extract_order_payment_condition(self) -> str:
        try:
            payment_condition = self.find_element(by=By.XPATH, value="//label[@for='payment_slip_installments_description']/following-sibling::div[@class='col-md-12']").text
        except:
            payment_condition = self.find_element(by=By.XPATH, value="//label[@for='payment_card_installments_description']/following-sibling::div[@class='col-md-12']").text
        return payment_condition
    
    def _extract_order_payment_way(self) -> str:
        payment_way = self.find_element(by=By.XPATH, value="//label[@for='payment_name']/following-sibling::div[@class='col-md-12']").text
        payment_way_hyphen_list = ["Boleto à Vista - [Log MercadoPago] - [Log Loja] - Imprimir", "Elo - Log", "Visa - Log", "Master - Log", "Pix - Log"]
        if payment_way in payment_way_hyphen_list:
            payment_way = payment_way.split(" - ")[0]
        return payment_way
    
    def _extract_order_receiver_cnpj_cpf(self) -> str:
        return self.find_element(by=By.XPATH, value="//label[@for='client_cnpj']/following-sibling::div[@class='col-md-12']").text
    
    def _extract_order_total_value(self) -> str:
        value = self.find_element(by=By.XPATH, value="//label[@for='payment_value']/following-sibling::div[@class='col-md-12']").text 
        value = value.replace("R$", "").replace(".", "").replace(",", ".")
        return value
    
    def _extract_order_status(self) -> str:
        try: 
            status = self.find_element(by=By.NAME, value="distribution_centers[1][status]")
        except: 
            try:
                status = self.find_element(by=By.NAME, value="distribution_centers[2][status]")
            except:
                status = self.find_element(by=By.NAME, value="distribution_centers[3][status]") 
        status = Select(status) 
        status = status.first_selected_option.text
        return status
    
    def _extract_order_receiver(self) -> str:
        client = self.find_element(by=By.XPATH, value="//label[@for='client_name_corporate']/following-sibling::div[@class='col-md-12']").text
        try:
            client = str(client).split(" (")[0]
        except:
            pass
        return client
    
    def _extract_order_resaler(self) -> str:
        try:
            resaler = self.find_element(by=By.XPATH, value="//label[@for='resale_name_corporate']/following-sibling::div[@class='col-md-12']").text
        except:
            resaler = "-"
            return resaler
        try:
            resaler = str(resaler).split(" (")[0]
        except:
            pass
        return resaler
    
    def _extract_order_receiver_erp_code(self) -> str:
        erp_code = self.find_element(by=By.XPATH, value="//label[@for='client_name_corporate']/following-sibling::div[@class='col-md-12']").text
        try:
            erp_code = str(erp_code).split(" (")[1]
            erp_code = str(erp_code).replace(")", "")
        except:
            erp_code = "-"
        return erp_code
    
    def _extract_order_seller(self) -> str:
        seller = "-"
        cnpj = self.find_element(by=By.XPATH, value="//label[@for='client_cnpj']/following-sibling::div[@class='col-md-12']").text
        order_url = self.current_url
        try:
            seller = self._get_seller_from_resalers(cnpj=cnpj)
        except:
            try:
                seller = self._get_seller_from_billing_clients(cnpj=cnpj, active=True)
            except:
                seller = self._get_seller_from_billing_clients(cnpj=cnpj, active=False)
        self.get(order_url)
        return seller
    
    def _extract_order_centers(self) -> list[str]:
        centers: list[str] = []
        for i in range(1, 4):
            try:
                centers.append(self.find_element(by=By.XPATH, value=f"(//div[@class='panel distribution-center']/div[@class='panel-heading'])[{i}]").text)
            except:
                pass
        return centers
    
    def _extract_order_additional_data(self) -> str:
        observation = self.find_element(by=By.XPATH, value="//label[@for='client_comment']/following-sibling::div[@class='col-md-12']").text 
        if observation == "":
            observation = "-"
        return observation
    
    def _extract_order_sap_id(self) -> str:
        try:
            order_element = self.find_element(by=By.ID, value="distribution_centers-3-external_id")
        except:
            try:
                order_element = self.find_element(by=By.ID, value="distribution_centers-2-external_id")
            except:
                order_element = self.find_element(by=By.ID, value="distribution_centers-1-external_id")
        order_element = order_element.get_attribute(name="value")
        if order_element == "" or order_element == None:
            order_element = "-"
        return order_element
    
    def _extract_order_over(self) -> str:
        over = self.find_element(by=By.XPATH, value="//div[@class='panel distribution-center']").text 
        if "Comissão total (comissão unitários)" in over:
            over = "SIM"
        else: 
            over = "NÃO"
        return over
    
    def _extract_order_items(self) -> list[Item]:
        self.execute_script("document.body.style.zoom='50%'")
        items: list[Item] = []
        tables = self.find_elements(by=By.XPATH, value="//div[@class='panel distribution-center']")
        for table in tables:
            if "Ilhéus" in table.text:
                center = "3010"
            elif "Manaus" in table.text:
                center = "1910"
            else:
                center = "1099"
            footer = table.find_element(by=By.XPATH, value="./div[@class='panel-footer']/table[@class='table table-striped']")
            items_footer = footer.find_elements(by=By.XPATH, value=".//tbody/tr")
            for item in items_footer:
                center = center
                sku = item.find_elements(by=By.XPATH, value=".//td")[2].text
                sku = sku.lstrip("0")
                value = item.find_elements(by=By.XPATH, value=".//td")[17].text
                value = value.replace("R$", "").replace(".", "").replace(",", ".").strip()
                item_element = Item(sku=sku, center=center, unit_value=value)
                items.append(item_element)
        return items
    
    def _extract_order_seller_office_comission(self) -> tuple[str, str, str]:
        seller = self._extract_order_seller()
        office = self._extract_office(seller=seller)
        comission_percentage = self._extract_comission_percentage(office=office)
        return seller, office, comission_percentage
    
    def _extract_comission_percentage(self, office: str) -> str:
        if office == "1105":
            comission_percentage = "0,50"
        else:
            comission_percentage = "2,50"
        return comission_percentage
    
    def _extract_office(self, seller: str) -> str:
        sellers_1105_list = [
            "ANDRE MARQUES DE SOUSA",
            "DOUGLAS MACIEL CUER",
            "FELIPE CASTILHO FRANCA",
            "LUIS GUSTAVO COSTA",
            "MAIKON FELIPE MOHR BATISTELA",
            "MARCELO PINTO",
            "MARGARIDA MARIA HENRIQUES",
            "RAQUEL MARTINS RODRIGUES",
            "RENATA PRISCILA DA SILVA",
            "RONALDO OLIVEIRA SILVA",
            "YOUHANNA SABBAG SOBRINHO"
        ]
        if seller in sellers_1105_list:
            office = "1105"
        else:
            office = "1101"
        return office
    
    def _extract_order_organizations(self) -> list[str]:
        centers = self._extract_order_centers()
        organizations: list[str] = []
        for center in centers:
            if center == "Manaus":
                organizations.append("1600")
            if center == "Ilhéus":
                organizations.append("3100")
            if center == "Curitiba":
                organizations.append("1100")
        return organizations
    
    def _extract_order_expeditions(self) -> list[str]:
        centers = self._extract_order_centers()
        expeditions: list[str] = []
        for center in centers:
            if center == "Manaus":
                expeditions.append("14")
            if center == "Ilhéus":
                expeditions.append("01")
            if center == "Curitiba":
                expeditions.append("01")
        return expeditions
    
    def _extract_order_reason(self) -> str:
        reason = self.find_element(by=By.XPATH, value="//label[@for='order_type_id']/following-sibling::div[@class='col-md-12']").text 
        if reason == "Revender":
            reason = "600"
        else:
            reason = "601"
        return reason
    
    def _access_order(self, order: str) -> None:
        self.get(url=f"https://www.revendedorpositivo.com.br/admin/orders/edit/id/{order}")
        page_content = self.find_element(by=By.TAG_NAME, value="body").text
        if "Application error: Mysqli statement execute error" in page_content:
            raise OrderNotExistsError(order=order)
    
    def change_order(self, headless: bool, order: str, status: str = "", observation: str = "") -> None:
        self._init(headless=headless)
        self._access_order(order=order)
        if status:
            for i in range(1, 4):
                try: 
                    status_element = self.find_element(by=By.NAME, value=f"distribution_centers[{i}][status]")
                    status_element = Select(status_element)
                    status_element.select_by_visible_text(text=status)
                except:
                    continue
        if observation:
            observation_element = self.find_element(by=By.ID, value="comment")
            observation_element.clear()
            observation_element.send_keys(observation)
        save_button = self.find_element(by=By.ID, value="save")
        save_button.click()
        self.quit()
    
    def get_order_data_for_credit_analysis(self, headless: bool, order: str) -> Order:
        self._init(headless=headless)
        self._access_order(order=order)
        value = self._extract_order_total_value()
        cnpj_root = self._extract_order_receiver_cnpj_cpf()[:8]
        self.quit()
        return Order(
            order_site = order,
            receiver_cnpj_root = cnpj_root,
            total_value = value
        )
    
    def get_order_data(self, headless: bool, order: str) -> Order:
        self._init(headless=headless)
        self._access_order(order=order)
        date = self._extract_order_date()
        doc_type = "ZV11"
        centers = self._extract_order_centers()
        organization = self._extract_order_organizations()
        channel = "40"
        seller, office, comission_percentage = self._extract_order_seller_office_comission()
        team = "058"
        order_name = order
        order_site = order
        order_erp = self._extract_order_sap_id()
        resaler_name = self._extract_order_resaler()
        receiver_name = self._extract_order_receiver()
        resaler_erp = "-"
        receiver_erp = self._extract_order_receiver_erp_code()
        receiver_type = "-"
        payment_condition = self._extract_order_payment_condition()
        incoterm = "CIF"
        reason = self._extract_order_reason()
        table = "-"
        expedition = self._extract_order_expeditions()
        payment_way = self._extract_order_payment_way()
        additional_data = self._extract_order_additional_data()
        comissions = [Comission(key="-", code="-", percentage="-")]
        partners = [Partner(key="-", code="-")]
        items = self._extract_order_items()
        receiver_cnpj_cpf = self._extract_order_receiver_cnpj_cpf()
        receiver_cnpj_root = receiver_cnpj_cpf[:8]
        total_value = self._extract_order_total_value()
        status_site = self._extract_order_status()
        over = self._extract_order_over()
        self.quit()
        return Order(
            date = date,
            doc_type = doc_type,
            organization = organization,
            channel = channel,
            office = office,
            team = team,
            order_name = order_name,
            order_site = order_site,
            order_erp = order_erp,
            resaler_name = resaler_name,
            receiver_name = receiver_name,
            resaler_erp = resaler_erp,
            receiver_erp = receiver_erp,
            receiver_type = receiver_type,
            payment_condition = payment_condition,
            incoterm = incoterm,
            reason = reason,
            table = table,
            expedition = expedition,
            payment_way = payment_way,
            additional_data = additional_data,
            comissions = comissions,
            partners = partners,
            items = items,
            receiver_cnpj_cpf = receiver_cnpj_cpf,
            receiver_cnpj_root = receiver_cnpj_root,
            total_value = total_value,
            status_site = status_site,
            seller = seller,
            centers = centers,
            over = over,
            comission_percentage = comission_percentage
        )
