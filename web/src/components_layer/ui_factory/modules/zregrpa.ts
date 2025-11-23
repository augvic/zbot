import { Icon } from "../global/icon";
import { Notification } from "../global/notification";
import { MakeRequestTask } from "../../tasks/make_request";
import { AdjustTableTask } from "../../tasks/adjust_table";

export class zRegRpa {
    
    element!: HTMLElement
    container!: Container
    
    public init(appendTo: HTMLElement, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask, adjustTableTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zRegRpa";
        this.element.className = "w-full h-full opacity-fade-in bg-gray-300 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center";
    }
    
    private async createComponents(makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        const response = await fetch(`${window.location.origin}/registrations-rpa`, {
            method: "GET"
        });
        const data = await response.json();
        this.container = new Container(this.element, data, makeRequestTask, adjustTableTask);
    }
    
}

class Container {
    
    element!: HTMLElement
    terminalSection!: TerminalSection
    registrationsSection!: RegistrationsSection
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        this.createComponents(data, makeRequestTask, adjustTableTask);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "container";
        this.element.className = "w-[95%] h-[95%] p-3 bg-white dark:bg-gray-700 transition-colors duration-300 flex rounded-lg";
    }
    
    private createComponents(data: {[key: string]: string}, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.terminalSection = new TerminalSection(this.element, data, makeRequestTask, adjustTableTask);
    }
    
}

class TerminalSection {
    
    element!: HTMLElement
    topBar!: ContainerTopBar
    terminal!: Terminal
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        this.createComponents(data, makeRequestTask, adjustTableTask);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "terminal-section";
        this.element.className = "w-full h-full gap-y-2 flex flex-col items-center justify-center transition-opacity duration-300";
    }
    
    private createComponents(data: {[key: string]: string}, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.topBar = new ContainerTopBar(this.element, data, makeRequestTask, adjustTableTask)
        this.terminal = new Terminal(this.element, data);
    }
    
}

class ContainerTopBar {
    
    element!: HTMLElement
    turnOnButton!: TurnOnButton
    turnOffButton!: TurnOffButton
    status!: RpaStatus
    goToRegistrationsSection!: GoToRegistrationsSection
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        this.createComponents(data, makeRequestTask, adjustTableTask);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[5%] flex items-center gap-x-2";
    }
    
    private createComponents(data: {[key: string]: string}, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.turnOnButton = new TurnOnButton(this.element, data);
        this.turnOffButton = new TurnOffButton(this.element, data);
        this.status = new RpaStatus(this.element, data);
        this.goToRegistrationsSection = new GoToRegistrationsSection(this.element, makeRequestTask, adjustTableTask);
    }
    
}

class TurnOnButton {
    
    element!: HTMLButtonElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf(data);
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf(data: {[key: string]: string}) {
        this.element = document.createElement("button");
        this.element.id = "turn-on-button";
        this.element.className = "w-auto h-auto p-1 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer";
        if (data.status == "Em processamento...") {
            this.element.disabled = true;
            this.element.style.backgroundColor = "#919191";
            this.element.style.cursor = "not-allowed";
        }
    }
    
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/play.png", "5");
    }
    
    private startListeners() {
        this.element.addEventListener("click", async () => {
            const response = await fetch(`${window.location.origin}/registrations-rpa`, {
                method: "POST" 
            });
            const data = await response.json();
            if (!data.success) {
                new Notification(data.message, "red");
            }
        });
    }
    
}

class TurnOffButton {
    
    element!: HTMLButtonElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf(data);
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf(data: {[key: string]: string}) {
        this.element = document.createElement("button");
        this.element.id = "turn-off-button";
        this.element.className = "w-auto h-auto p-1 bg-red-700 hover:bg-red-900 transition-colors duration-300 rounded-md cursor-pointer";
        if (data.status == "Desligado.") {
            this.element.disabled = true;
            this.element.style.backgroundColor = "#919191";
            this.element.style.cursor = "not-allowed";
        }
    }
    
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/stop.png", "5");
    }
    
    private startListeners() {
        this.element.addEventListener("click", async () => {
            const response = await fetch(`${window.location.origin}/registrations-rpa`, {
                method: "DELETE" 
            });
            const data = await response.json();
            if (!data.success) {
                new Notification(data.message, "red");
            }
        });
    }
    
}

class RpaStatus {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf(data);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(data: {[key: string]: string}) {
        this.element = document.createElement("p");
        this.element.className = "cursor-default text-black dark:text-white transition-colors transition-opacity duration-300";
        this.element.innerText = `Status: ${data.status}`;
    }
    
}

class GoToRegistrationsSection {
    
    wrapper!: HTMLElement
    button!: HTMLButtonElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        this.startListeners(makeRequestTask, adjustTableTask);
        appendTo.appendChild(this.wrapper);
    }
    
    private createSelf() {
        this.wrapper = document.createElement("div");
        this.wrapper.className = "w-auto h-auto flex flex-1 justify-end items-center";
        this.button = document.createElement("button");
        this.button.className = "w-auto h-auto py-1 px-2 bg-amber-700 hover:bg-amber-900 transition-colors duration-300 rounded-md cursor-pointer text-white";
        this.button.innerText = "Ir para cadastros.";
        this.wrapper.appendChild(this.button);
    }
    
    private startListeners(makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.button.addEventListener("click", () => {
            let terminalSection = document.getElementById("terminal-section")!;
            terminalSection.style.opacity = "0";
            setTimeout(() => {
                terminalSection.style.display = "none";
                new RegistrationsSection(document.getElementById("container")!, makeRequestTask, adjustTableTask);
            }, 300);
        });
    }
    
}

class Terminal {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf(data);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(data: {[key: string]: string}) {
        this.element = document.createElement("div");
        this.element.id = "terminal";
        this.element.className = "w-full h-[95%] flex flex-col gap-y-1 p-3 bg-black text-white rounded-md overflow-y-auto custom-scroll scroll-smooth";
        this.element.innerText = data.memory;
        setTimeout(() => {
            this.element.scrollTop = this.element.scrollHeight;
        }, 500);
    }
    
}

class RegistrationsSection {
    
    element!: HTMLElement
    titleBar!: RegistrationsSectionTopBar
    tableContainer!: RegistrationsTableContainer
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask, adjustTableTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "registrations-section";
        this.element.className = "w-full h-full flex flex-col gap-3 opacity-fade-in transition-opacity duration-300";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.titleBar = new RegistrationsSectionTopBar(this.element, makeRequestTask);
        this.tableContainer = new RegistrationsTableContainer(this.element, makeRequestTask, adjustTableTask);
    }
    
}

class RegistrationsSectionTopBar {
    
    element!: HTMLElement
    searchInput!: SearchRegistrationInput
    searchButton!: SearchRegistrationButton
    addRegistrationButton!: AddRegistrationButton
    goToTerminalSection!: GoToTerminalSection
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[5%] flex items-center gap-2";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.searchInput = new SearchRegistrationInput(this.element);
        this.searchButton = new SearchRegistrationButton(this.element);
        this.addRegistrationButton = new AddRegistrationButton(this.element, makeRequestTask);
        this.goToTerminalSection = new GoToTerminalSection(this.element);
    }
    
}

class SearchRegistrationInput {
    
    element!: HTMLInputElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("input");
        this.element.className = "h-[30px] w-[300px] bg-white rounded-md border border-gray-300 outline-none p-3";
        this.element.id = "search-registration-input";
        this.element.placeholder = "Pesquisar";
    }
    
}

class SearchRegistrationButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
        this.startListeners();
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "h-auto w-auto p-1 bg-blue-700 text-white hover:bg-blue-900 hover:text-black cursor-pointer rounded-md transition-colors duration-300";
    }
    
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/magnifying_glass.png", "5");
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            const toSearch = (document.getElementById("search-registration-input")! as HTMLInputElement).value;
            const registrationRows = document.querySelectorAll(".registration-row");
            if (toSearch == "") {
                registrationRows.forEach(element => {
                    const row = element as HTMLElement;
                    row.style.display = "flex";
                    row.offsetHeight;
                    row.style.height = "46px";   
                });
                return;
            }
            registrationRows.forEach(element => {
                const row = element as HTMLElement;
                if (!row.innerText.includes(toSearch)) {
                    row.style.height = "0px";
                    setTimeout(() => {
                        row.style.display = "none";
                    }, 300);
                } else {
                    row.style.display = "flex";
                    row.offsetHeight;
                    row.style.height = "46px";
                }
            });
        });
    }
    
}

class AddRegistrationButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
        this.startListeners(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "h-auto w-auto p-1 bg-green-700 text-white hover:bg-green-900 hover:text-black cursor-pointer rounded-md transition-colors duration-300";
    }
    
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/plus.png", "5");
    }
    
    private startListeners(makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", () => {
            new CreateRegistrationModal(document.getElementById("zRegRpa")!, makeRequestTask);
        });
    }
    
}

class GoToTerminalSection {
    
    element!: HTMLElement
    button!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-1 items-center justify-end";
        this.button = document.createElement("button");
        this.button.className = "h-auto w-auto px-2 py-1 bg-amber-700 text-white hover:bg-amber-900 cursor-pointer rounded-md transition-colors duration-300";
        this.button.innerText = "Alternar para terminal."
        this.element.appendChild(this.button);
    }
    
    private startListeners() {
        this.button.addEventListener("click", () => {
            let terminalSection = document.getElementById("terminal-section")!;
            let registrationsSection = document.getElementById("registrations-section")!
            registrationsSection.style.opacity = "0";
            setTimeout(() => {
                registrationsSection.remove();
                terminalSection.style.opacity = "0";
                terminalSection.style.display = "flex";
                terminalSection.offsetHeight;
                terminalSection.style.opacity = "1";
            }, 300);
        });
    }
    
}

class RegistrationsTableContainer {
    
    element!: HTMLElement
    table!: RegistrationsTable
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask, adjustTableTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[95%] flex overflow-auto custom-scroll rounded-tl-lg rounded-tr-lg";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.table = new RegistrationsTable(this.element, makeRequestTask, adjustTableTask);
    }
    
}

class RegistrationsTable {
    
    element!: HTMLElement
    tableHead!: RegistrationsTableHead
    tableBody!: RegistrationsTableBody
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask, adjustTableTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-auto w-auto flex flex-col whitespace-nowrap cursor-default border-collapse text-center text-black dark:text-white transition-colors duration-300";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.tableHead = new RegistrationsTableHead(this.element);
        this.tableBody = new RegistrationsTableBody(this.element, makeRequestTask, adjustTableTask);
    }
    
}

class RegistrationsTableHead {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "font-bold h-[46px] w-auto flex bg-gray-300 dark:bg-gray-900 transition-colors duration-300 sticky top-0 rounded-tl-lg rounded-tr-lg";
    }
    
    private createComponents() {
        new RegistrationsTableHeadRowCell(this.element, "Status", 1);
        new RegistrationsTableHeadRowCell(this.element, "CNPJ", 2);
        new RegistrationsTableHeadRowCell(this.element, "Abertura", 3);
        new RegistrationsTableHeadRowCell(this.element, "Situação Cadastral", 4);
        new RegistrationsTableHeadRowCell(this.element, "Razão Social", 5);
        new RegistrationsTableHeadRowCell(this.element, "Nome Fantasia", 6);
        new RegistrationsTableHeadRowCell(this.element, "Natureza Jurídica", 7);
        new RegistrationsTableHeadRowCell(this.element, "Natureza Jurídica ID", 8);
        new RegistrationsTableHeadRowCell(this.element, "Rua", 9);
        new RegistrationsTableHeadRowCell(this.element, "Número", 10);
        new RegistrationsTableHeadRowCell(this.element, "Complemento", 11);
        new RegistrationsTableHeadRowCell(this.element, "Bairro", 12);
        new RegistrationsTableHeadRowCell(this.element, "CEP", 13);
        new RegistrationsTableHeadRowCell(this.element, "Cidade", 14);
        new RegistrationsTableHeadRowCell(this.element, "Estado", 15);
        new RegistrationsTableHeadRowCell(this.element, "Telefone", 16);
        new RegistrationsTableHeadRowCell(this.element, "E-mail", 17);
        new RegistrationsTableHeadRowCell(this.element, "Regime Tributário", 18);
        new RegistrationsTableHeadRowCell(this.element, "Recebimento de Comissão", 19);
        new RegistrationsTableHeadRowCell(this.element, "Tipo do Cliente", 20);
        new RegistrationsTableHeadRowCell(this.element, "Limite Sugerido", 21);
        new RegistrationsTableHeadRowCell(this.element, "Vendedor", 22);
        new RegistrationsTableHeadRowCell(this.element, "CPF", 23);
        new RegistrationsTableHeadRowCell(this.element, "Representante Legal", 24);
        new RegistrationsTableHeadRowCell(this.element, "", 25);
    }
    
}

class RegistrationsTableHeadRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string, position: number) {
        this.createSelf(text, position);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string, position: number) {
        this.element = document.createElement("div");
        this.element.className = "p-4 flex h-auto w-auto items-center justify-center";
        this.element.innerText = text;
        this.element.id = `header-${position}`;
    }
    
}

class RegistrationsTableBody {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask, adjustTableTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "registrations-table-body";
        this.element.className = "w-auto h-auto flex flex-col";
    }
    
    private async createComponents(makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        const response = await makeRequestTask.get("/registrations/all");
        if (!response.success) {
            new Notification(response.message, "red");
        }
        const registrations = response.data as [{}]
        registrations.forEach((registration: {}) => {
            let row = new RegistrationsTableBodyRow(this.element, registration, makeRequestTask, adjustTableTask);
            row.element.offsetHeight;
            row.element.style.height = "46px";
        });
    }
    
}

class RegistrationsTableBodyRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        this.createSelf(registration.cnpj);
        appendTo.appendChild(this.element);
        this.createComponents(registration, makeRequestTask, adjustTableTask);
    }
    
    private createSelf(cnpj: string) {
        this.element = document.createElement("div");
        this.element.id = `${cnpj}-row`;
        this.element.className = "w-full h-[0px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 table-row-transitions registration-row";
    }
    
    private createComponents(registration: {[key: string]: string}, makeRequestTask: MakeRequestTask, adjustTableTask: AdjustTableTask) {
        new RegistrationsTableBodyRowCell(this.element, registration.status, registration.cnpj, "status", 1, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.cnpj, registration.cnpj, "cnpj", 2, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.opening, registration.cnpj, "opening", 3, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.registration_status, registration.cnpj, "registration_status", 4, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.company_name, registration.cnpj, "company_name", 5, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.trade_name, registration.cnpj, "trade_name", 6, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.legal_nature, registration.cnpj, "legal_nature", 7, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.legal_nature_id, registration.cnpj, "legal_nature_id", 8, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.street, registration.cnpj, "street", 9, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.number, registration.cnpj, "number", 10, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.complement, registration.cnpj, "complement", 11, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.neighborhood, registration.cnpj, "neighborhood", 12, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.pac, registration.cnpj, "pac", 13, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.city, registration.cnpj, "city", 14, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.state, registration.cnpj, "state", 15, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.fone, registration.cnpj, "fone", 16, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.email, registration.cnpj, "email", 17, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.tax_regime, registration.cnpj, "tax_regime", 18, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.comission_receipt, registration.cnpj, "comission_receipt", 19, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.client_type, registration.cnpj, "client_type", 20, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.suggested_limit, registration.cnpj, "suggested_limit", 21, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.seller, registration.cnpj, "seller", 22, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.cpf, registration.cnpj, "cpf", 23, adjustTableTask);
        new RegistrationsTableBodyRowCell(this.element, registration.cpf_person, registration.cnpj, "cpf_person", 24, adjustTableTask);
        new RegistrationsTableBodyRowButtonsCell(this.element, registration, makeRequestTask, 25, adjustTableTask);
    }
    
}

class RegistrationsTableBodyRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string, cnpj: string, type: string, position: number, adjustTableTask: AdjustTableTask) {
        this.createSelf(text, cnpj, type);
        appendTo.appendChild(this.element);
        adjustTableTask.execute(position, this.element, type);
    }
    
    private createSelf(text: string, cnpj: string, type: string) {
        this.element = document.createElement("div");
        this.element.className = "p-4 h-auto w-auto flex items-center justify-center overflow-hidden custom-scroll";
        this.element.id = `${cnpj}-${type}-cell`;
        this.element.innerText = text;
    }
    
}

class RegistrationsTableBodyRowButtonsCell {
    
    element!: HTMLElement
    editButton!: RegistrationsTableEditButton
    deleteButton!: RegistrationsTableDeleteButton
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, makeRequestTask: MakeRequestTask, position: number, adjustTableTask: AdjustTableTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(registration, makeRequestTask);
        adjustTableTask.execute(position, this.element, "buttons");
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-auto flex gap-x-2 items-center justify-center";
    }
    
    private createComponents(registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.editButton = new RegistrationsTableEditButton(this.element, registration, makeRequestTask);
        this.deleteButton = new RegistrationsTableDeleteButton(this.element, registration.cnpj, makeRequestTask);
    }
    
}

class RegistrationsTableEditButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
        this.startListeners(registration, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-blue-700 rounded-md hover:bg-blue-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/edit.png", "5");
        
    }
    
    private startListeners(registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", () => {
            new EditRegistrationModal(document.getElementById("zRegRpa")!, registration, makeRequestTask);
        });
    }
    
}

class RegistrationsTableDeleteButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, cnpj: string, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
        this.startListeners(cnpj, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-red-700 rounded-md hover:bg-red-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/delete.png", "5");
    }
    
    private startListeners(cnpj: string, makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", async () => {
            const response = await makeRequestTask.delete(`/registrations/${cnpj}`);
            if (!response.success) {
                new Notification(response.message, "red");
            } else {
                new Notification(response.message, "green");
                const userRow = document.getElementById(`${cnpj}-row`)!;
                userRow.style.height = "0px";
                setTimeout(() => {
                    userRow.remove();
                }, 300);
            }
        });
    }
    
}

class EditRegistrationModal {
    
    element!: HTMLElement
    modal!: EditRegistrationModalContainer
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(registration, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "registration-modal";
        this.element.className = "w-full h-full fixed flex items-center justify-center z-50 bg-black/80 opacity-fade-in";
    }
    private createComponents(registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.modal = new EditRegistrationModalContainer(this.element, registration, makeRequestTask);
    }
    
}

class EditRegistrationModalContainer {
    
    element!: HTMLElement
    closeButtonContainer!: EditRegistrationModalCloseButtonContainer
    inputsContainer!: EditRegistrationModalInputsContainer
    button!: EditRegistrationModalSaveButton
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(registration, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[30%] h-[60%] flex flex-col items-center p-3 bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg gap-y-2";
    }
    
    private createComponents(registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.closeButtonContainer = new EditRegistrationModalCloseButtonContainer(this.element);
        this.inputsContainer = new EditRegistrationModalInputsContainer(this.element, registration, makeRequestTask);
        this.button = new EditRegistrationModalSaveButton(this.element, makeRequestTask);
    }
    
}

class EditRegistrationModalInputsContainer {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(registration, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-full flex flex-col overflow-y-auto custom-scroll items-center p-3 gap-y-2 border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-tl-lg rounded-bl-lg";
    }
    
    private async createComponents(registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        const response = await makeRequestTask.get(`/registrations/${registration.cnpj}`)
        if (!response.success) {
            new Notification(response.message, "red");
        }
        const dataUpdated = response.data[0];
        new EditRegistrationModalInput(this.element, "text", "CNPJ", "registration-modal-cnpj", dataUpdated.cnpj);
        new EditRegistrationModalInput(this.element, "text", "Status", "registration-modal-status", dataUpdated.status);
        new EditRegistrationModalInput(this.element, "text", "Abertura", "registration-modal-opening", dataUpdated.opening);
        new EditRegistrationModalInput(this.element, "text", "Situação Cadastral", "registration-modal-registration_status", dataUpdated.registration_status);
        new EditRegistrationModalInput(this.element, "text", "Razão Social", "registration-modal-company_name", dataUpdated.company_name);
        new EditRegistrationModalInput(this.element, "text", "Nome Fantasia", "registration-modal-trade_name", dataUpdated.trade_name);
        new EditRegistrationModalInput(this.element, "text", "Natureza Jurídica", "registration-modal-legal_nature", dataUpdated.legal_nature);
        new EditRegistrationModalInput(this.element, "text", "Natureza Jurídica ID", "registration-modal-legal_nature_id", dataUpdated.legal_nature_id);
        new EditRegistrationModalInput(this.element, "text", "Rua", "registration-modal-street", dataUpdated.street);
        new EditRegistrationModalInput(this.element, "text", "Número", "registration-modal-number", dataUpdated.number);
        new EditRegistrationModalInput(this.element, "text", "Complemento", "registration-modal-complement", dataUpdated.complement);
        new EditRegistrationModalInput(this.element, "text", "Bairro", "registration-modal-neighborhood", dataUpdated.neighborhood);
        new EditRegistrationModalInput(this.element, "text", "CEP", "registration-modal-pac", dataUpdated.pac);
        new EditRegistrationModalInput(this.element, "text", "Cidade", "registration-modal-city", dataUpdated.city);
        new EditRegistrationModalInput(this.element, "text", "Estado", "registration-modal-state", dataUpdated.state);
        new EditRegistrationModalInput(this.element, "text", "Telefone", "registration-modal-fone", dataUpdated.fone);
        new EditRegistrationModalInput(this.element, "text", "E-mail", "registration-modal-email", dataUpdated.email,);
        new EditRegistrationModalInput(this.element, "text", "Regime Tributário", "registration-modal-tax_regime", dataUpdated.tax_regime);
        new EditRegistrationModalInput(this.element, "text", "Recebimento da Comissão", "registration-modal-comission_receipt", dataUpdated.comission_receipt);
        new EditRegistrationModalInput(this.element, "text", "Tipo do Cliente", "registration-modal-client_type", dataUpdated.client_type);
        new EditRegistrationModalInput(this.element, "text", "Limite Sugerido", "registration-modal-suggested_limit", dataUpdated.suggested_limit);
        new EditRegistrationModalInput(this.element, "text", "Vendedor", "registration-modal-seller", dataUpdated.seller);
        new EditRegistrationModalInput(this.element, "text", "CPF", "registration-modal-cpf", dataUpdated.cpf);
        new EditRegistrationModalInput(this.element, "text", "Representante Legal", "registration-modal-cpf_person", dataUpdated.cpf_person);
    }
    
}

class EditRegistrationModalCloseButtonContainer {
    
    element!: HTMLElement
    closeButton!: EditRegistrationModalCloseButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex justify-end";
    }
    
    private createComponents() {
        this.closeButton = new EditRegistrationModalCloseButton(this.element);
    }
    
}

class EditRegistrationModalCloseButton {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners();
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto rounded-full px-2 bg-red-700 hover:bg-red-900 cursor-pointer text-white transition-colors duration-300";
        this.element.innerText = "x";
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            const modal = document.getElementById("registration-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
            }, { once: true });
        });
    }
    
}

class EditRegistrationModalInput {
    
    element!: HTMLInputElement
    container!: HTMLDivElement
    label!: HTMLLabelElement
    
    constructor(appendTo: HTMLElement, type: string, placeholder: string, id: string, value: string) {
        this.createSelf(placeholder, id, type, value);
        appendTo.appendChild(this.container);
    }
    
    private createSelf(placeholder: string, id: string, type: string, value: string) {
        this.container = document.createElement("div");
        this.container.className = "flex flex-col gap-y-2";
        this.label = document.createElement("label");
        this.label.className = "text-black dark:text-white transition-colors duration-300";
        this.label.innerText = `${placeholder}:`;
        this.element = document.createElement("input");
        this.element.id = id;
        this.element.type = type;
        this.element.className = "w-[300px] h-[30px] p-2 bg-white border border-gray-300 outline-none rounded-md";
        this.element.value = value;
        this.container.appendChild(this.label);
        this.container.appendChild(this.element);
        if (id == "registration-modal-cnpj") {
            this.element.readOnly = true;
            this.element.className = "w-[300px] h-[30px] p-2 border outline-none rounded-md cursor-default bg-gray-300 text-black border-gray-300 dark:bg-gray-900 dark:text-white dark:border-gray-900 transition-colors duration-300";
        }
    }
    
}

class EditRegistrationModalSaveButton {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto p-2 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer text-white";
        this.element.innerText = "Salvar";
    }
    
    private startListeners(makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", async () => {
            const status = (document.getElementById("registration-modal-status") as HTMLInputElement).value!;
            const registration_status = (document.getElementById("registration-modal-registration_status") as HTMLInputElement).value!;
            const cnpj = (document.getElementById("registration-modal-cnpj") as HTMLInputElement).value!;
            const opening = (document.getElementById("registration-modal-opening") as HTMLInputElement).value!;
            const company_name = (document.getElementById("registration-modal-company_name") as HTMLInputElement).value!;
            const trade_name = (document.getElementById("registration-modal-trade_name") as HTMLInputElement).value!;
            const legal_nature = (document.getElementById("registration-modal-legal_nature") as HTMLInputElement).value!;
            const legal_nature_id = (document.getElementById("registration-modal-legal_nature_id") as HTMLInputElement).value!;
            const street = (document.getElementById("registration-modal-street") as HTMLInputElement).value!;
            const number = (document.getElementById("registration-modal-number") as HTMLInputElement).value!;
            const complement = (document.getElementById("registration-modal-complement") as HTMLInputElement).value!;
            const neighborhood = (document.getElementById("registration-modal-neighborhood") as HTMLInputElement).value!;
            const pac = (document.getElementById("registration-modal-pac") as HTMLInputElement).value!;
            const city = (document.getElementById("registration-modal-city") as HTMLInputElement).value!;
            const state = (document.getElementById("registration-modal-state") as HTMLInputElement).value!;
            const fone = (document.getElementById("registration-modal-fone") as HTMLInputElement).value!;
            const email = (document.getElementById("registration-modal-email") as HTMLInputElement).value!;
            const tax_regime = (document.getElementById("registration-modal-tax_regime") as HTMLInputElement).value!;
            const comission_receipt = (document.getElementById("registration-modal-comission_receipt") as HTMLInputElement).value!;
            const client_type = (document.getElementById("registration-modal-client_type") as HTMLInputElement).value!;
            const suggested_limit = (document.getElementById("registration-modal-suggested_limit") as HTMLInputElement).value!;
            const seller = (document.getElementById("registration-modal-seller") as HTMLInputElement).value!;
            const cpf = (document.getElementById("registration-modal-cpf") as HTMLInputElement).value!;
            const cpf_person = (document.getElementById("registration-modal-cpf_person") as HTMLInputElement).value!;
            const response = await makeRequestTask.put("/registrations", "application/json", { 
                status,
                registration_status,
                cnpj,
                opening,
                company_name,
                trade_name,
                legal_nature,
                legal_nature_id,
                street,
                number,
                complement,
                neighborhood,
                pac,
                city,
                state,
                fone,
                email,
                tax_regime,
                comission_receipt,
                client_type,
                suggested_limit,
                seller,
                cpf,
                cpf_person
            });
            if (!response.success) {
                new Notification(response.message, "red");
                return;
            } else {
                new Notification(response.message, "green");
            }
            const modal = document.getElementById("registration-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
                let cnpjRow = document.getElementById(`${cnpj}-row`)!;
                const currentBgColor = cnpjRow.style.backgroundColor;
                cnpjRow.style.backgroundColor = "#abffb7";
                cnpjRow.addEventListener("transitionend", () => {
                    document.getElementById(`${cnpj}-status-cell`)!.innerText = status;
                    document.getElementById(`${cnpj}-registration_status-cell`)!.innerText = registration_status;
                    document.getElementById(`${cnpj}-cnpj-cell`)!.innerText = cnpj;
                    document.getElementById(`${cnpj}-opening-cell`)!.innerText = opening;
                    document.getElementById(`${cnpj}-company_name-cell`)!.innerText = company_name;
                    document.getElementById(`${cnpj}-trade_name-cell`)!.innerText = trade_name;
                    document.getElementById(`${cnpj}-legal_nature-cell`)!.innerText = legal_nature;
                    document.getElementById(`${cnpj}-legal_nature_id-cell`)!.innerText = legal_nature_id;
                    document.getElementById(`${cnpj}-street-cell`)!.innerText = street;
                    document.getElementById(`${cnpj}-number-cell`)!.innerText = number;
                    document.getElementById(`${cnpj}-complement-cell`)!.innerText = complement;
                    document.getElementById(`${cnpj}-neighborhood-cell`)!.innerText = neighborhood;
                    document.getElementById(`${cnpj}-pac-cell`)!.innerText = pac;
                    document.getElementById(`${cnpj}-city-cell`)!.innerText = city;
                    document.getElementById(`${cnpj}-state-cell`)!.innerText = state;
                    document.getElementById(`${cnpj}-fone-cell`)!.innerText = fone;
                    document.getElementById(`${cnpj}-email-cell`)!.innerText = email;
                    document.getElementById(`${cnpj}-tax_regime-cell`)!.innerText = tax_regime;
                    document.getElementById(`${cnpj}-comission_receipt-cell`)!.innerText = comission_receipt;
                    document.getElementById(`${cnpj}-client_type-cell`)!.innerText = client_type;
                    document.getElementById(`${cnpj}-suggested_limit-cell`)!.innerText = suggested_limit;
                    document.getElementById(`${cnpj}-seller-cell`)!.innerText = seller;
                    document.getElementById(`${cnpj}-cpf-cell`)!.innerText = cpf;
                    document.getElementById(`${cnpj}-cpf_person-cell`)!.innerText = cpf_person;
                    cnpjRow.style.backgroundColor = currentBgColor;
                }, { once: true });
            }, { once: true });
        });
    }
    
}

class CreateRegistrationModal {
    
    element!: HTMLElement
    modal!: CreateRegistrationModalContainer
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "registration-modal";
        this.element.className = "w-full h-full fixed flex items-center justify-center z-50 bg-black/80 opacity-fade-in";
    }
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.modal = new CreateRegistrationModalContainer(this.element, makeRequestTask);
    }
    
}

class CreateRegistrationModalContainer {
    
    element!: HTMLElement
    closeButtonContainer!: CreateRegistrationModalCloseButtonContainer
    inputsContainer!: CreateRegistrationModalInputsContainer
    button!: CreateRegistrationModalSaveButton
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[30%] h-[60%] flex flex-col items-center p-3 bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg gap-y-2";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.closeButtonContainer = new CreateRegistrationModalCloseButtonContainer(this.element);
        this.inputsContainer = new CreateRegistrationModalInputsContainer(this.element);
        this.button = new CreateRegistrationModalSaveButton(this.element, makeRequestTask);
    }
    
}

class CreateRegistrationModalInputsContainer {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-full flex flex-col overflow-y-auto custom-scroll items-center p-3 gap-y-2 border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-tl-lg rounded-bl-lg";
    }
    
    private async createComponents() {
        new CreateRegistrationModalInput(this.element, "text", "CNPJ", "registration-modal-cnpj");
        new CreateRegistrationModalInput(this.element, "text", "Vendedor", "registration-modal-seller");
        new CreateRegistrationModalInput(this.element, "text", "E-mail", "registration-modal-email");
        new CreateRegistrationModalInput(this.element, "text", "CPF", "registration-modal-cpf");
        new CreateRegistrationModalInput(this.element, "text", "Representante Legal", "registration-modal-cpf_person");
        new CreateRegistrationModalInput(this.element, "text", "Regime Tributário", "registration-modal-tax_regime");
        new CreateRegistrationModalInput(this.element, "text", "Tipo do Cliente", "registration-modal-client_type");
        new CreateRegistrationModalInput(this.element, "text", "Limite Sugerido", "registration-modal-suggested_limit");
    }
    
}

class CreateRegistrationModalCloseButtonContainer {
    
    element!: HTMLElement
    closeButton!: CreateRegistrationModalCloseButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex justify-end";
    }
    
    private createComponents() {
        this.closeButton = new CreateRegistrationModalCloseButton(this.element);
    }
    
}

class CreateRegistrationModalCloseButton {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners();
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto rounded-full px-2 bg-red-700 hover:bg-red-900 cursor-pointer text-white transition-colors duration-300";
        this.element.innerText = "x";
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            const modal = document.getElementById("registration-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
            }, { once: true });
        });
    }
    
}

class CreateRegistrationModalInput {
    
    element!: HTMLInputElement
    container!: HTMLDivElement
    label!: HTMLLabelElement
    
    constructor(appendTo: HTMLElement, type: string, placeholder: string, id: string) {
        this.createSelf(placeholder, id, type);
        appendTo.appendChild(this.container);
    }
    
    private createSelf(placeholder: string, id: string, type: string) {
        this.container = document.createElement("div");
        this.container.className = "flex flex-col gap-y-2";
        this.label = document.createElement("label");
        this.label.className = "text-black dark:text-white transition-colors duration-300";
        this.label.innerText = `${placeholder}:`;
        this.element = document.createElement("input");
        this.element.id = id;
        this.element.type = type;
        this.element.className = "w-[300px] h-[30px] p-2 bg-white border border-gray-300 outline-none rounded-md";
        this.container.appendChild(this.label);
        this.container.appendChild(this.element);
        if (id == "registration-modal-cnpj") {
            this.element.readOnly = true;
            this.element.className = "w-[300px] h-[30px] p-2 border outline-none rounded-md cursor-default bg-gray-300 text-black border-gray-300 dark:bg-gray-900 dark:text-white dark:border-gray-900 transition-colors duration-300";
        }
    }
    
}

class CreateRegistrationModalSaveButton {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto p-2 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer text-white";
        this.element.innerText = "Incluir";
    }
    
    private startListeners(makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", async () => {

        });
    }
    
}
