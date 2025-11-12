import { Icon } from "../global/icon";
import { Notification } from "../global/notification";
import { MakeRequestTask } from "../../tasks/make_request";

export class zRegRpa {
    
    element!: HTMLElement
    container!: Container
    
    public init(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zRegRpa";
        this.element.className = "w-full h-full opacity-fade-in bg-gray-300 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center";
    }
    
    private async createComponents(makeRequestTask: MakeRequestTask) {
        const response = await fetch(`${window.location.origin}/registrations-rpa`, {
            method: "GET"
        });
        const data = await response.json();
        this.container = new Container(this.element, data, makeRequestTask);
    }
    
}

class Container {
    
    element!: HTMLElement
    terminalSection!: TerminalSection
    registrationsSection!: RegistrationsSection
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        this.createComponents(data, makeRequestTask);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "container";
        this.element.className = "w-[95%] h-[95%] p-3 bg-white dark:bg-gray-700 transition-colors duration-300 flex rounded-lg";
    }
    
    private createComponents(data: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.terminalSection = new TerminalSection(this.element, data);
        this.registrationsSection = new RegistrationsSection(this.element, makeRequestTask);
    }
    
}

class TerminalSection {
    
    element!: HTMLElement
    topBar!: ContainerTopBar
    terminal!: Terminal
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(data);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "terminal-section";
        this.element.className = "w-full h-full gap-y-2 flex flex-col items-center justify-center transition-opacity duration-300";
    }
    
    private createComponents(data: {[key: string]: string}) {
        this.topBar = new ContainerTopBar(this.element, data)
        this.terminal = new Terminal(this.element, data);
    }
    
}

class ContainerTopBar {
    
    element!: HTMLElement
    turnOnButton!: TurnOnButton
    turnOffButton!: TurnOffButton
    status!: RpaStatus
    goToRegistrationsSection!: GoToRegistrationsSection
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(data);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[5%] flex items-center gap-x-2";
    }
    
    private createComponents(data: {[key: string]: string}) {
        this.turnOnButton = new TurnOnButton(this.element, data);
        this.turnOffButton = new TurnOffButton(this.element, data);
        this.status = new RpaStatus(this.element, data);
        this.goToRegistrationsSection = new GoToRegistrationsSection(this.element);
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
        if (data.status == "Em processamento.") {
            this.element.disabled = true;
            this.element.style.backgroundColor = "#919191";
            this.element.style.cursor = "not-allowed";
        }
        if (data.status == "Desligado.") {
            this.element.disabled = false;
            this.element.style.backgroundColor = "oklch(52.7% 0.154 150.069)";
            this.element.style.cursor = "pointer";
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
        if (data.status == "Em processamento.") {
            this.element.disabled = false;
            this.element.style.backgroundColor = "oklch(50.5% 0.213 27.518)";
            this.element.style.cursor = "pointer";
        }
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
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.startListeners();
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
    
    private startListeners() {
        this.button.addEventListener("click", () => {
            let terminalSection = document.getElementById("terminal-section")!;
            let registrationsSection = document.getElementById("registrations-section")!
            terminalSection.style.opacity = "0";
            setTimeout(() => {
                terminalSection.style.display = "none";
                registrationsSection.style.opacity = "0";
                registrationsSection.style.display = "flex";
                registrationsSection.offsetHeight;
                registrationsSection.style.opacity = "1";
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
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "registrations-section";
        this.element.className = "w-full h-full flex flex-col gap-3 opacity-fade-in transition-opacity duration-300";
        this.element.style.display = "none"
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.titleBar = new RegistrationsSectionTopBar(this.element, makeRequestTask);
        this.tableContainer = new RegistrationsTableContainer(this.element, makeRequestTask);
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
        this.element.placeholder = "CNPJ";
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
                if (!row.id.includes(toSearch)) {
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
            new RegistrationModal(document.getElementById("zRegRpa")!, {}, false, makeRequestTask);
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
                registrationsSection.style.display = "none";
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
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[95%] flex overflow-auto custom-scroll";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.table = new RegistrationsTable(this.element, makeRequestTask);   
    }
    
}

class RegistrationsTable {
    
    element!: HTMLElement
    tableHead!: RegistrationsTableHead
    tableBody!: RegistrationsTableBody
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-auto w-auto flex flex-col whitespace-nowrap cursor-default border-collapse text-center text-black dark:text-white transition-colors duration-300";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.tableHead = new RegistrationsTableHead(this.element);
        this.tableBody = new RegistrationsTableBody(this.element, makeRequestTask);
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
        new RegistrationsTableHeadRowCell(this.element, "Usuário", 1);
        new RegistrationsTableHeadRowCell(this.element, "Nome", 2);
        new RegistrationsTableHeadRowCell(this.element, "E-mail", 3);
        new RegistrationsTableHeadRowCell(this.element, "Senha", 4);
        new RegistrationsTableHeadRowCell(this.element, "", 5);
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
        this.element.className = "p-2 flex h-auto w-auto items-center justify-center";
        this.element.innerText = text;
        this.element.id = `header-${position}`;
    }
    
}

class RegistrationsTableBody {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "registrations-table-body";
        this.element.className = "w-auto h-auto flex flex-col";
    }
    
    private async createComponents(makeRequestTask: MakeRequestTask) {
        // const response = await makeRequestTask.get("/users/all");
        // if (!response.success) {
        //     new Notification(response.message, "red");
        // }
        // const users = response.data as [{}]
        // users.forEach((user: {}) => {
        //     let row = new RegistrationsTableBodyRow(this.element, user, makeRequestTask);
        //     row.element.offsetHeight;
        //     row.element.style.height = "46px";
        // });
        const registration = { user: "Augusto", name: "Augusto-name", email: "email", password: "senhahehe" }
        let row = new RegistrationsTableBodyRow(this.element, registration, makeRequestTask);
        row.element.offsetHeight;
        row.element.style.height = "46px";
    }
    
}

class RegistrationsTableBodyRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf(registration.user);
        appendTo.appendChild(this.element);
        this.createComponents(registration, makeRequestTask);
    }
    
    private createSelf(cnpj: string) {
        this.element = document.createElement("div");
        this.element.id = `${cnpj}-row`;
        this.element.className = "w-full h-[0px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 table-row-transitions user-row";
    }
    
    private createComponents(registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        new RegistrationsTableBodyRowCell(this.element, registration.user, registration.user, "user");
        new RegistrationsTableBodyRowCell(this.element, registration.name, registration.user, "name");
        new RegistrationsTableBodyRowCell(this.element, registration.email, registration.user, "email");
        new RegistrationsTableBodyRowCell(this.element, registration.password, registration.user, "password");
        new RegistrationsTableBodyRowButtonsCell(this.element, registration, makeRequestTask);
    }
    
}

class RegistrationsTableBodyRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string, cnpj: string, type: string) {
        this.createSelf(text, cnpj, type);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string, cnpj: string, type: string) {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-auto flex items-center justify-center overflow-hidden custom-scroll";
        this.element.id = `${cnpj}-${type}-cell`;
        this.element.innerText = text;
    }
    
}

class RegistrationsTableBodyRowButtonsCell {
    
    element!: HTMLElement
    editButton!: RegistrationsTableEditButton
    deleteButton!: RegistrationsTableDeleteButton
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(registration, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-auto flex gap-x-2 items-center justify-center";
    }
    
    private createComponents(registration: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.editButton = new RegistrationsTableEditButton(this.element, registration, makeRequestTask);
        this.deleteButton = new RegistrationsTableDeleteButton(this.element, registration.user, makeRequestTask);
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
            new RegistrationModal(document.getElementById("zRegRpa")!, registration, true, makeRequestTask);
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
        // this.element.addEventListener("click", async () => {
        //     const response = await makeRequestTask.delete(`/registrations/${cnpj}`);
        //     if (!response.success) {
        //         new Notification(response.message, "red");
        //     } else {
        //         new Notification(response.message, "green");
        //         const userRow = document.getElementById(`${cnpj}-row`)!;
        //         userRow.style.height = "0px";
        //         setTimeout(() => {
        //             userRow.remove();
        //         }, 300);
        //     }
        // });
    }
    
}

class RegistrationModal {
    
    element!: HTMLElement
    modal!: RegistrationModalContainer
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(registration, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "registration-modal";
        this.element.className = "w-full h-full fixed flex items-center justify-center z-50 bg-black/80 opacity-fade-in";
    }
    private createComponents(registration: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.modal = new RegistrationModalContainer(this.element, registration, editModal, makeRequestTask);
    }
    
}

class RegistrationModalContainer {
    
    element!: HTMLElement
    closeButtonContainer!: RegistrationModalCloseButtonContainer
    elementsContainer!: RegistrationModalElements
    button!: RegistrationModalSaveButton | RegistrationModalCreateButton
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(registration, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col items-center p-3 bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg gap-y-2";
    }
    
    private createComponents(registration: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.closeButtonContainer = new RegistrationModalCloseButtonContainer(this.element);
        this.elementsContainer = new RegistrationModalElements(this.element, registration, editModal, makeRequestTask);
        if (editModal) {
            this.button = new RegistrationModalSaveButton(this.element, makeRequestTask);
        } else {
            this.button = new RegistrationModalCreateButton(this.element, makeRequestTask);
        }
    }
    
}

class RegistrationModalElements {
    
    element!: HTMLElement
    inputsContainer!: RegistrationModalInputsContainer
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(registration, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex flex-1 gap-x-2";
    }
    
    private createComponents(registration: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.inputsContainer = new RegistrationModalInputsContainer(this.element, registration, editModal, makeRequestTask);
    }
    
}

class RegistrationModalInputsContainer {
    
    element!: HTMLElement
    userInput!: RegistrationModalInput
    nameInput!: RegistrationModalInput
    emailInput!: RegistrationModalInput
    passwordInput!: RegistrationModalInput
    
    constructor(appendTo: HTMLElement, registration: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(registration, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col p-3 items-center justify-center gap-y-2 border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-lg";
    }
    
    private async createComponents(registration: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
    //     if (editModal) {
    //         const response = await makeRequestTask.get(`/registrations/${registration.cnpj}`)
    //         if (!response.success) {
    //             new Notification(response.message, "red");
    //         }
    //         const userDataUpdated = response.data[0];
    //         this.userInput = new RegistrationModalInput(this.element, "text", "Usuário", "user-modal-user", userDataUpdated.user, editModal);
    //         this.nameInput = new RegistrationModalInput(this.element, "text", "Nome", "user-modal-name", userDataUpdated.name, editModal);
    //         this.emailInput = new RegistrationModalInput(this.element, "text", "E-mail", "user-modal-email", userDataUpdated.email, editModal);
    //         this.passwordInput = new RegistrationModalInput(this.element, "text", "Senha", "user-modal-password", userDataUpdated.password, editModal);
    //     } else {
    //         this.userInput = new RegistrationModalInput(this.element, "text", "Usuário", "user-modal-user", "", editModal);
    //         this.nameInput = new RegistrationModalInput(this.element, "text", "Nome", "user-modal-name", "", editModal);
    //         this.emailInput = new RegistrationModalInput(this.element, "text", "E-mail", "user-modal-email", "", editModal);
    //         this.passwordInput = new RegistrationModalInput(this.element, "text", "Senha", "user-modal-password", "", editModal);
    //     }
    }
    
}

class RegistrationModalCloseButtonContainer {
    
    element!: HTMLElement
    closeButton!: RegistrationModalCloseButton
    
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
        this.closeButton = new RegistrationModalCloseButton(this.element);
    }
    
}

class RegistrationModalCloseButton {
    
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

class RegistrationModalInput {
    
    element!: HTMLInputElement
    
    constructor(appendTo: HTMLElement, type: string, placeholder: string, id: string, value: string, editModal: boolean) {
        this.createSelf(placeholder, id, type, value, editModal);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(placeholder: string, id: string, type: string, value: string, editModal: boolean) {
        this.element = document.createElement("input");
        this.element.id = id;
        this.element.type = type;
        this.element.className = "w-[300px] h-[30px] p-2 bg-white border border-gray-300 outline-none rounded-md";
        this.element.placeholder = placeholder;
        this.element.value = value;
        if (id == "registration-modal-cnpj" && editModal == true) {
            this.element.readOnly = true;
            this.element.className = "w-[300px] h-[30px] p-2 border outline-none rounded-md cursor-default bg-gray-300 text-black border-gray-300 dark:bg-gray-900 dark:text-white dark:border-gray-900 transition-colors duration-300";
        }
    }
    
}

class RegistrationModalCreateButton {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto p-2 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer text-white";
        this.element.innerText = "Criar";
    }
    
    private startListeners(makeRequestTask: MakeRequestTask) {
        // this.element.addEventListener("click", async () => {
        //     const tableBody = document.getElementById("users-table-body")!;
        //     const user = (document.getElementById("user-modal-user") as HTMLInputElement).value!;
        //     const name = (document.getElementById("user-modal-name") as HTMLInputElement).value!;
        //     const email = (document.getElementById("user-modal-email") as HTMLInputElement).value!;
        //     const password = (document.getElementById("user-modal-password") as HTMLInputElement).value!;
        //     const response = await makeRequestTask.post("/users", "application/json", { user, name, email, password });
        //     if (!response.success) {
        //         new Notification(response.message, "red");
        //         return;
        //     } else {
        //         new Notification(response.message, "green");
        //     }
        //     const permissionsToCreate = document.querySelectorAll<HTMLElement>(".permission-to-create");
        //     permissionsToCreate.forEach(async permission => {
        //         const response = await makeRequestTask.post(`/permissions/${user}/${permission.innerText}`, "", "");
        //         if (!response.success) {
        //             new Notification(response.message, "red");
        //         } else {
        //             new Notification(response.message, "green");
        //         }
        //     });
        //     const modal = document.getElementById("user-modal")!;
        //     modal.classList.remove("opacity-fade-in");
        //     modal.classList.add("opacity-fade-out");
        //     modal.addEventListener("animationend", () => {
        //         modal.remove();
        //         let row = new RegistrationsTableBodyRow(tableBody, { user: user, name: name, email: email, password: password }, makeRequestTask);
        //         row.element.offsetHeight;
        //         row.element.style.height = "46px";
        //     }, { once: true });
        // });
    }
    
}

class RegistrationModalSaveButton {
    
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
        // this.element.addEventListener("click", async () => {
        //     const user = (document.getElementById("user-modal-user") as HTMLInputElement).value!;
        //     const name = (document.getElementById("user-modal-name") as HTMLInputElement).value!;
        //     const email = (document.getElementById("user-modal-email") as HTMLInputElement).value!;
        //     const password = (document.getElementById("user-modal-password") as HTMLInputElement).value!;
        //     const response = await makeRequestTask.put(`/users`, "application/json", { user, name, email, password });
        //     if (!response.success) {
        //         new Notification(response.message, "red");
        //         return;
        //     } else {
        //         new Notification(response.message, "green");
        //     }
        //     const permissionsToDelete = document.querySelectorAll<HTMLElement>(".permission-to-delete");
        //     permissionsToDelete.forEach(async permission => {
        //         const response = await makeRequestTask.delete(`/permissions/${user}/${permission.innerText}`)
        //         if (!response.success) {
        //             new Notification(response.message, "red");
        //         } else {
        //             new Notification(response.message, "green");
        //         }
        //     });
        //     const permissionsToCreate = document.querySelectorAll<HTMLElement>(".permission-to-create");
        //     permissionsToCreate.forEach(async permission => {
        //         const response = await makeRequestTask.post(`/permissions/${user}/${permission.innerText}`, "", "")
        //         if (!response.success) {
        //             new Notification(response.message, "red");
        //         } else {
        //             new Notification(response.message, "green");
        //         }
        //     });
        //     const modal = document.getElementById("user-modal")!;
        //     modal.classList.remove("opacity-fade-in");
        //     modal.classList.add("opacity-fade-out");
        //     modal.addEventListener("animationend", () => {
        //         modal.remove();
        //         let userRow = document.getElementById(`${user}-row`)!;
        //         const currentBgColor = userRow.style.backgroundColor;
        //         userRow.style.backgroundColor = "#abffb7";
        //         userRow.addEventListener("transitionend", () => {
        //             document.getElementById(`${user}-user-cell`)!.innerText = user;
        //             document.getElementById(`${user}-name-cell`)!.innerText = name;
        //             document.getElementById(`${user}-email-cell`)!.innerText = email;
        //             document.getElementById(`${user}-password-cell`)!.innerText = password;
        //             userRow.style.backgroundColor = currentBgColor;
        //         }, { once: true });
        //     }, { once: true });
        // });
    }
    
}