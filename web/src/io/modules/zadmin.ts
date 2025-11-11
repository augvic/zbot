import { Notification } from "../global/notification";
import { Icon } from "../global/icon";
import { MakeRequestTask } from "../../tasks/make_request";

export class zAdmin {
    
    element!: HTMLElement
    usersContainer!: Container
    
    public init(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zAdmin";
        this.element.className = "w-full h-full opacity-fade-in bg-gray-300 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.usersContainer = new Container(this.element, makeRequestTask);
    }
    
}

class Container {
    
    element!: HTMLElement
    usersSection!: UsersSection
    modulesSection!: ModulesSection
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "sections-container";
        this.element.className = "w-[95%] h-[95%] flex bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.usersSection = new UsersSection(this.element, makeRequestTask);
    }
    
}

class UsersSection {
    
    element!: HTMLElement
    titleBar!: UsersSectionTopBar
    tableContainer!: UsersTableContainer
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "users-section";
        this.element.className = "w-full h-full flex flex-col p-5 gap-3 opacity-fade-in";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.titleBar = new UsersSectionTopBar(this.element, makeRequestTask);
        this.tableContainer = new UsersTableContainer(this.element, makeRequestTask);
    }
    
}

class UsersSectionTopBar {
    
    element!: HTMLElement
    searchInput!: SearchUserInput
    searchButton!: SearchUserButton
    addUserButton!: AddUserButton
    goToModulesSection!: GoToModulesSection
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex items-center gap-2";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.searchInput = new SearchUserInput(this.element);
        this.searchButton = new SearchUserButton(this.element);
        this.addUserButton = new AddUserButton(this.element, makeRequestTask);
        this.goToModulesSection = new GoToModulesSection(this.element, makeRequestTask);
    }
    
}

class SearchUserInput {
    
    element!: HTMLInputElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("input");
        this.element.className = "h-[30px] w-[300px] bg-white rounded-md border border-gray-300 outline-none p-3";
        this.element.id = "search-user-input";
        this.element.placeholder = "Matrícula";
    }
    
}

class SearchUserButton {
    
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
            const toSearch = (document.getElementById("search-user-input")! as HTMLInputElement).value;
            const userRows = document.querySelectorAll(".user-row");
            if (toSearch == "") {
                userRows.forEach(element => {
                    const row = element as HTMLElement;
                    row.style.display = "flex";
                    row.offsetHeight;
                    row.style.height = "46px";   
                });
                return;
            }
            userRows.forEach(element => {
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

class AddUserButton {
    
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
            new UserModal(document.getElementById("zAdmin")!, {}, false, makeRequestTask);
        });
    }
    
}

class GoToModulesSection {
    
    element!: HTMLElement
    button!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-1 items-center justify-end";
        this.button = document.createElement("button");
        this.button.className = "h-auto w-auto px-2 py-1 bg-amber-700 text-white hover:bg-amber-900 cursor-pointer rounded-md transition-colors duration-300";
        this.button.innerText = "Alternar para módulos."
        this.element.appendChild(this.button);
    }
    
    private startListeners(makeRequestTask: MakeRequestTask) {
        this.button.addEventListener("click", () => {
            const sectionsContainer = document.getElementById("sections-container")!;
            const usersSection = document.getElementById("users-section")!;
            usersSection.classList.add("opacity-fade-out");
            usersSection.addEventListener("animationend", () => {
                usersSection.remove();
                new ModulesSection(sectionsContainer, makeRequestTask);
            }, { once: true });
        });
    }
    
}

class UsersTableContainer {
    
    element!: HTMLElement
    table!: UsersTable
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex-1 overflow-y-auto custom-scroll";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.table = new UsersTable(this.element, makeRequestTask);   
    }
    
}

class UsersTable {
    
    element!: HTMLElement
    tableHead!: UsersTableHead
    tableBody!: UsersTableBody
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-auto w-full flex flex-col whitespace-nowrap cursor-default border-collapse text-center text-black dark:text-white transition-colors duration-300";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.tableHead = new UsersTableHead(this.element);
        this.tableBody = new UsersTableBody(this.element, makeRequestTask);
    }
    
}

class UsersTableHead {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "font-bold h-[46px] w-full flex bg-gray-300 dark:bg-gray-900 transition-colors duration-300 sticky top-0 rounded-tl-lg rounded-tr-lg";
    }
    
    private createComponents() {
        new UsersTableHeadRowCell(this.element, "Usuário");
        new UsersTableHeadRowCell(this.element, "Nome");
        new UsersTableHeadRowCell(this.element, "E-mail");
        new UsersTableHeadRowCell(this.element, "Senha");
        new UsersTableHeadRowCell(this.element, "");
    }
    
}

class UsersTableHeadRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("div");
        this.element.className = "p-2 flex h-auto w-[20%] items-center justify-center";
        this.element.innerText = text;
    }
    
}

class UsersTableBody {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "users-table-body";
        this.element.className = "w-auto h-auto flex flex-col";
    }
    
    private async createComponents(makeRequestTask: MakeRequestTask) {
        const response = await makeRequestTask.get("/users/all");
        if (!response.success) {
            new Notification(response.message, "red");
        }
        const users = response.data as [{}]
        users.forEach((user: {}) => {
            let row = new UsersTableBodyRow(this.element, user, makeRequestTask);
            row.element.offsetHeight;
            row.element.style.height = "46px";
        });
    }
    
}

class UsersTableBodyRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf(user.user);
        appendTo.appendChild(this.element);
        this.createComponents(user, makeRequestTask);
    }
    
    private createSelf(user: string) {
        this.element = document.createElement("div");
        this.element.id = `${user}-row`;
        this.element.className = "w-full h-[0px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 table-row-transitions user-row";
    }
    
    private createComponents(user: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        new UsersTableBodyRowCell(this.element, user.user, user.user, "user");
        new UsersTableBodyRowCell(this.element, user.name, user.user, "name");
        new UsersTableBodyRowCell(this.element, user.email, user.user, "email");
        new UsersTableBodyRowCell(this.element, user.password, user.user, "password");
        new UsersTableBodyRowButtonsCell(this.element, user, makeRequestTask);
    }
    
}

class UsersTableBodyRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string, user: string, type: string) {
        this.createSelf(text, user, type);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string, user: string, type: string) {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-[20%] flex items-center justify-center overflow-hidden custom-scroll";
        this.element.id = `${user}-${type}-cell`;
        this.element.innerText = text;
    }
    
}

class UsersTableBodyRowButtonsCell {
    
    element!: HTMLElement
    editButton!: UsersTableEditButton
    deleteButton!: UsersTableDeleteButton
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(user, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-[20%] flex gap-x-2 items-center justify-center";
    }
    
    private createComponents(user: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.editButton = new UsersTableEditButton(this.element, user, makeRequestTask);
        this.deleteButton = new UsersTableDeleteButton(this.element, user.user, makeRequestTask);
    }
    
}

class UsersTableEditButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
        this.startListeners(user, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-blue-700 rounded-md hover:bg-blue-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/edit.png", "5");
        
    }
    
    private startListeners(user: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", () => {
            new UserModal(document.getElementById("zAdmin")!, user, true, makeRequestTask);
        });
    }
    
}

class UsersTableDeleteButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, user: string, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
        this.startListeners(user, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-red-700 rounded-md hover:bg-red-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/delete.png", "5");
    }
    
    private startListeners(user: string, makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", async () => {
            const response = await makeRequestTask.delete(`/users/${user}`);
            if (!response.success) {
                new Notification(response.message, "red");
            } else {
                new Notification(response.message, "green");
                const userRow = document.getElementById(`${user}-row`)!;
                userRow.style.height = "0px";
                setTimeout(() => {
                    userRow.remove();
                }, 300);
            }
        });
    }
    
}

class UserModal {
    
    element!: HTMLElement
    modal!: UserModalContainer
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(user, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "user-modal";
        this.element.className = "w-full h-full fixed flex items-center justify-center z-50 bg-black/80 opacity-fade-in";
    }
    private createComponents(user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.modal = new UserModalContainer(this.element, user, editModal, makeRequestTask);
    }
    
}

class UserModalContainer {
    
    element!: HTMLElement
    closeButtonContainer!: UserModalCloseButtonContainer
    elementsContainer!: UserModalElements
    button!: UserModalSaveButton | UserModalCreateButton
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(user, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col items-center p-3 bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg gap-y-2";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.closeButtonContainer = new UserModalCloseButtonContainer(this.element);
        this.elementsContainer = new UserModalElements(this.element, user, editModal, makeRequestTask);
        if (editModal) {
            this.button = new UserModalSaveButton(this.element, makeRequestTask);
        } else {
            this.button = new UserModalCreateButton(this.element, makeRequestTask);
        }
    }
    
}

class UserModalElements {
    
    element!: HTMLElement
    inputsContainer!: UserModalInputsContainer
    tableContainer!: UserModalTableContainer
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(user, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex flex-1 gap-x-2";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.inputsContainer = new UserModalInputsContainer(this.element, user, editModal, makeRequestTask);
        this.tableContainer = new UserModalTableContainer(this.element, user, editModal, makeRequestTask);
    }
    
}

class UserModalInputsContainer {
    
    element!: HTMLElement
    userInput!: UserModalInput
    nameInput!: UserModalInput
    emailInput!: UserModalInput
    passwordInput!: UserModalInput
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(user, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col p-3 items-center justify-center gap-y-2 border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-lg";
    }
    
    private async createComponents(user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        if (editModal) {
            const response = await makeRequestTask.get(`/users/${user.user}`)
            if (!response.success) {
                new Notification(response.message, "red");
            }
            const userDataUpdated = response.data[0];
            this.userInput = new UserModalInput(this.element, "text", "Usuário", "user-modal-user", userDataUpdated.user, editModal);
            this.nameInput = new UserModalInput(this.element, "text", "Nome", "user-modal-name", userDataUpdated.name, editModal);
            this.emailInput = new UserModalInput(this.element, "text", "E-mail", "user-modal-email", userDataUpdated.email, editModal);
            this.passwordInput = new UserModalInput(this.element, "text", "Senha", "user-modal-password", userDataUpdated.password, editModal);
        } else {
            this.userInput = new UserModalInput(this.element, "text", "Usuário", "user-modal-user", "", editModal);
            this.nameInput = new UserModalInput(this.element, "text", "Nome", "user-modal-name", "", editModal);
            this.emailInput = new UserModalInput(this.element, "text", "E-mail", "user-modal-email", "", editModal);
            this.passwordInput = new UserModalInput(this.element, "text", "Senha", "user-modal-password", "", editModal);
        }
    }
    
}

class UserModalTableContainer {
    
    element!: HTMLElement
    permissionsTableContainer!: PermissionsTableContainer
    selectContainer!: UserModalModulesListContainer
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(user, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[300px] h-[300px] flex flex-col p-3 gap-y-2 items-center justify-center border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-lg";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.selectContainer = new UserModalModulesListContainer(this.element, makeRequestTask);
        this.permissionsTableContainer = new PermissionsTableContainer(this.element, user, editModal, makeRequestTask);
    }
    
}

class UserModalModulesListContainer {
    
    element!: HTMLElement
    select!: UserModalModulesList
    button!: UserModalAddModuleButton
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex gap-x-2";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.select = new UserModalModulesList(this.element, makeRequestTask);
        this.button = new UserModalAddModuleButton(this.element);
    }
    
}

class UserModalModulesList {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("select");
        this.element.id = "modules-list";
        this.element.className = "h-auto w-auto bg-white border border-gray-300 rounded-md p-1";
    }
    
    private async createComponents(makeRequestTask: MakeRequestTask) {
        const response = await makeRequestTask.get("/modules-list")
        if (!response.success) {
            new Notification(response.message, "red");
        }
        const modules = response.data as [{[key: string]: string}]
        modules.forEach(module => {
            new Option(this.element, module.module)
        });
    }
    
}

class Option {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("option");
        this.element.innerText = text;
    }
    
}

class UserModalAddModuleButton {
    
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
        this.element.className = "h-auto w-auto p-1 bg-green-700 text-white hover:bg-green-900 hover:text-black cursor-pointer rounded-md transition-colors duration-300";
    }
    
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/plus.png", "5");
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            const modulesList = document.getElementById("modules-list")! as HTMLSelectElement;
            const index = modulesList.selectedIndex;
            const selectedModule = modulesList.options[index].innerText;
            const rowExists = document.getElementById(`${selectedModule}-permission`);
            if (rowExists != null && !rowExists.classList.contains("permission-to-delete")) {
                new Notification("Módulo já adicionado.", "orange");
                return;
            }
            if (rowExists != null && rowExists.classList.contains("permission-to-delete")) {
                rowExists.style.display = "flex";
                rowExists.offsetHeight;
                rowExists.style.height = "46px";
                rowExists.classList.remove("permission-to-delete");
                return;
            }
            const permissionsTableBody = document.getElementById("permissions-table-body")!;
            let permissionRow = new PermissionsTableBodyRow(permissionsTableBody, { module: selectedModule });
            permissionRow.element.offsetHeight;
            permissionRow.element.style.height = "46px";
            permissionRow.element.classList.add("permission-to-create");
        });
    }
    
}

class UserModalCloseButtonContainer {
    
    element!: HTMLElement
    closeButton!: UserModalCloseButton
    
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
        this.closeButton = new UserModalCloseButton(this.element);
    }
    
}

class UserModalCloseButton {
    
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
            const modal = document.getElementById("user-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
            }, { once: true });
        });
    }
    
}

class UserModalInput {
    
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
        if (id == "user-modal-user" && editModal == true) {
            this.element.readOnly = true;
            this.element.className = "w-[300px] h-[30px] p-2 border outline-none rounded-md cursor-default bg-gray-300 text-black border-gray-300 dark:bg-gray-900 dark:text-white dark:border-gray-900 transition-colors duration-300";
        }
    }
    
}

class UserModalCreateButton {
    
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
        this.element.addEventListener("click", async () => {
            const tableBody = document.getElementById("users-table-body")!;
            const user = (document.getElementById("user-modal-user") as HTMLInputElement).value!;
            const name = (document.getElementById("user-modal-name") as HTMLInputElement).value!;
            const email = (document.getElementById("user-modal-email") as HTMLInputElement).value!;
            const password = (document.getElementById("user-modal-password") as HTMLInputElement).value!;
            const response = await makeRequestTask.post("/users", "application/json", { user, name, email, password });
            if (!response.success) {
                new Notification(response.message, "red");
                return;
            } else {
                new Notification(response.message, "green");
            }
            const permissionsToCreate = document.querySelectorAll<HTMLElement>(".permission-to-create");
            permissionsToCreate.forEach(async permission => {
                const response = await makeRequestTask.post(`/permissions/${user}/${permission.innerText}`, "", "");
                if (!response.success) {
                    new Notification(response.message, "red");
                } else {
                    new Notification(response.message, "green");
                }
            });
            const modal = document.getElementById("user-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
                let row = new UsersTableBodyRow(tableBody, { user: user, name: name, email: email, password: password }, makeRequestTask);
                row.element.offsetHeight;
                row.element.style.height = "46px";
            }, { once: true });
        });
    }
    
}

class UserModalSaveButton {
    
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
            const user = (document.getElementById("user-modal-user") as HTMLInputElement).value!;
            const name = (document.getElementById("user-modal-name") as HTMLInputElement).value!;
            const email = (document.getElementById("user-modal-email") as HTMLInputElement).value!;
            const password = (document.getElementById("user-modal-password") as HTMLInputElement).value!;
            const response = await makeRequestTask.put(`/users/${user}`, "application/json", { user, name, email, password });
            if (!response.success) {
                new Notification(response.message, "red");
                return;
            } else {
                new Notification(response.message, "green");
            }
            const permissionsToDelete = document.querySelectorAll<HTMLElement>(".permission-to-delete");
            permissionsToDelete.forEach(async permission => {
                const response = await makeRequestTask.delete(`/permissions/${user}/${permission.innerText}`)
                if (!response.success) {
                    new Notification(response.message, "red");
                } else {
                    new Notification(response.message, "green");
                }
            });
            const permissionsToCreate = document.querySelectorAll<HTMLElement>(".permission-to-create");
            permissionsToCreate.forEach(async permission => {
                const response = await makeRequestTask.post(`/permissions/${user}/${permission.innerText}`, "", "")
                if (!response.success) {
                    new Notification(response.message, "red");
                } else {
                    new Notification(response.message, "green");
                }
            });
            const modal = document.getElementById("user-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
                let userRow = document.getElementById(`${user}-row`)!;
                const currentBgColor = userRow.style.backgroundColor;
                userRow.style.backgroundColor = "#abffb7";
                userRow.addEventListener("transitionend", () => {
                    document.getElementById(`${user}-user-cell`)!.innerText = user;
                    document.getElementById(`${user}-name-cell`)!.innerText = name;
                    document.getElementById(`${user}-email-cell`)!.innerText = email;
                    document.getElementById(`${user}-password-cell`)!.innerText = password;
                    userRow.style.backgroundColor = currentBgColor;
                }, { once: true });
            }, { once: true });
        });
    }
    
}

class PermissionsTableContainer {
    
    element!: HTMLElement
    modulesTable!: PermissionsTable
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(user, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-full flex-1 overflow-y-auto custom-scroll";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.modulesTable = new PermissionsTable(this.element, user, editModal, makeRequestTask);   
    }
    
}

class PermissionsTable {
    
    element!: HTMLElement
    tableHead!: PermissionsTableHead
    tableBody!: PermissionsTableBody
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(user, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-auto w-full flex flex-col whitespace-nowrap cursor-default border-collapse text-center text-black dark:text-white transition-colors duration-300";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.tableHead = new PermissionsTableHead(this.element);
        this.tableBody = new PermissionsTableBody(this.element, user, editModal, makeRequestTask);
    }
    
}

class PermissionsTableHead {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "font-bold h-[46px] w-full flex bg-gray-300 dark:bg-gray-900 transition-colors duration-300 sticky top-0 rounded-tl-lg rounded-tr-lg";
    }
    
    private createComponents() {
        new PermissionsTableHeadRowCell(this.element, "Módulos Liberados");
    }
    
}

class PermissionsTableHeadRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("div");
        this.element.className = "p-2 flex h-auto w-[100%] items-center justify-center";
        this.element.innerText = text;
    }
    
}

class PermissionsTableBody {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(user, editModal, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "permissions-table-body";
        this.element.className = "w-auto h-auto flex flex-col";
    }
    
    private async createComponents(user: {[key: string]: string}, editModal: boolean, makeRequestTask: MakeRequestTask) {
        if (editModal) {
            const response = await makeRequestTask.get(`/permissions/${user.user}`)
            if (!response.success) {
                new Notification(response.message as string, "red");
            }
            const permissions = response.data as [{}]
            permissions.forEach((permission) => {
                let row = new PermissionsTableBodyRow(this.element, permission);
                row.element.offsetHeight;
                row.element.style.height = "46px";
            });
        }
    }
    
}

class PermissionsTableBodyRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, permission: {[key: string]: string}) {
        this.createSelf(permission);
        appendTo.appendChild(this.element);
        this.createComponents(permission);
    }
    
    private createSelf(permission: {[key: string]: string}) {
        this.element = document.createElement("div");
        this.element.id = `${permission.module}-permission`;
        this.element.className = "w-full h-[0px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 table-row-transitions";
    }
    
    private createComponents(permission: {[key: string]: string}) {
        new PermissionsTableBodyRowCell(this.element, permission.module);
        new PermissionsTableBodyRowButtonsCell(this.element, permission);
    }
    
}

class PermissionsTableBodyRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("div");
        this.element.className = "permissions-cell p-2 h-auto w-[80%] flex items-center justify-center overflow-hidden custom-scroll";
        this.element.innerText = text;
    }
    
}

class PermissionsTableBodyRowButtonsCell {
    
    element!: HTMLElement
    deleteButton!: PermissionsTableDeleteButton
    
    constructor(appendTo: HTMLElement, permission: {[key: string]: string}) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(permission);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-[20%] flex gap-x-2 items-center justify-center";
    }
    
    private createComponents(permission: {[key: string]: string}) {
        this.deleteButton = new PermissionsTableDeleteButton(this.element, permission);
    }
    
}

class PermissionsTableDeleteButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, permission: {[key: string]: string}) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
        this.startListeners(permission);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-red-700 rounded-md hover:bg-red-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/delete.png", "5");
    }
    
    private startListeners(permission: {[key: string]: string}) {
        this.element.addEventListener("click", () => {
            let permissionRow = document.getElementById(`${permission.module}-permission`)!;
            permissionRow.style.height = "0px";
            setTimeout(() => {
                if (permissionRow.classList.contains("permission-to-create")) {
                    permissionRow.remove();
                } else {
                    permissionRow.classList.add("permission-to-delete");
                    permissionRow.style.display = "none";
                }
            }, 300);
        });
    }
    
}

class ModulesSection {
    
    element!: HTMLElement
    titleBar!: ModulesSectionTopBar
    tableContainer!: ModulesTableContainer
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "modules-section";
        this.element.className = "w-full h-full flex flex-col p-5 gap-3 opacity-fade-in";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.titleBar = new ModulesSectionTopBar(this.element, makeRequestTask);
        this.tableContainer = new ModulesTableContainer(this.element, makeRequestTask);
    }
    
}

class ModulesSectionTopBar {
    
    element!: HTMLElement
    searchInput!: SearchModuleInput
    searchButton!: SearchModuleButton
    AddModuleButton!: AddModuleButton
    GoToUsersSection!: GoToUsersSection
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex items-center gap-2";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.searchInput = new SearchModuleInput(this.element);
        this.searchButton = new SearchModuleButton(this.element);
        this.AddModuleButton = new AddModuleButton(this.element, makeRequestTask);
        this.GoToUsersSection = new GoToUsersSection(this.element, makeRequestTask);
    }
    
}

class SearchModuleInput {
    
    element!: HTMLInputElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("input");
        this.element.className = "h-[30px] w-[300px] bg-white rounded-md border border-gray-300 outline-none p-3";
        this.element.id = "search-module-input";
        this.element.placeholder = "Módulo";
    }
    
}

class SearchModuleButton {
    
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
            const toSearch = (document.getElementById("search-module-input")! as HTMLInputElement).value;
            const userRows = document.querySelectorAll(".user-row");
            if (toSearch == "") {
                userRows.forEach(element => {
                    const row = element as HTMLElement;
                    row.style.display = "flex";
                    row.offsetHeight;
                    row.style.height = "46px";   
                });
                return;
            }
            userRows.forEach(element => {
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

class AddModuleButton {
    
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
            new ModulesModal(document.getElementById("zAdmin")!, makeRequestTask);
        });
    }
    
}

class GoToUsersSection {
    
    element!: HTMLElement
    button!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-1 items-center justify-end";
        this.button = document.createElement("button");
        this.button.className = "h-auto w-auto px-2 py-1 bg-amber-700 text-white hover:bg-amber-900 cursor-pointer rounded-md transition-colors duration-300";
        this.button.innerText = "Alternar para usuários."
        this.element.appendChild(this.button);
    }
    
    private startListeners(makeRequestTask: MakeRequestTask) {
        this.button.addEventListener("click", () => {
            const sectionsContainer = document.getElementById("sections-container")!;
            const modulesSection = document.getElementById("modules-section")!;
            modulesSection.classList.add("opacity-fade-out");
            modulesSection.addEventListener("animationend", () => {
                modulesSection.remove();
                new UsersSection(sectionsContainer, makeRequestTask);
            }, { once: true });
        });
    }
    
}

class ModulesTableContainer {
    
    element!: HTMLElement
    table!: ModulesTable
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex-1 overflow-y-auto custom-scroll";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.table = new ModulesTable(this.element, makeRequestTask);   
    }
    
}

class ModulesTable {
    
    element!: HTMLElement
    tableHead!: ModulesTableHead
    tableBody!: ModulesTableBody
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-auto w-full flex flex-col whitespace-nowrap cursor-default border-collapse text-center text-black dark:text-white transition-colors duration-300";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.tableHead = new ModulesTableHead(this.element);
        this.tableBody = new ModulesTableBody(this.element, makeRequestTask);
    }
    
}

class ModulesTableHead {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "font-bold h-[46px] w-full flex bg-gray-300 dark:bg-gray-900 transition-colors duration-300 sticky top-0 rounded-tl-lg rounded-tr-lg";
    }
    
    private createComponents() {
        new ModulesTableHeadRowCell(this.element, "Módulo");
        new ModulesTableHeadRowCell(this.element, "Descrição");
        new ModulesTableHeadRowButtonCell(this.element, "");
    }
    
}

class ModulesTableHeadRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("div");
        this.element.className = "p-2 flex h-auto w-[40%] items-center justify-center";
        this.element.innerText = text;
    }
    
}

class ModulesTableHeadRowButtonCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("div");
        this.element.className = "p-2 flex h-auto w-[20%] items-center justify-center";
        this.element.innerText = text;
    }
    
}

class ModulesTableBody {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "modules-table-body";
        this.element.className = "w-auto h-auto flex flex-col";
    }
    
    private async createComponents(makeRequestTask: MakeRequestTask) {
        const response = await makeRequestTask.get("/modules-list");
        if (!response.success) {
            new Notification(response.message as string, "red");
        }
        const modules = response.data as [{}]
        modules.forEach((module) => {
            let row = new ModulesTableBodyRow(this.element, module, makeRequestTask);
            row.element.offsetHeight;
            row.element.style.height = "46px";
        });
    }
    
}

class ModulesTableBodyRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, module: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf(module);
        appendTo.appendChild(this.element);
        this.createComponents(module, makeRequestTask);
    }
    
    private createSelf(module: {[key: string]: string}) {
        this.element = document.createElement("div");
        this.element.id = `${module.module}-row`;
        this.element.className = "w-full h-[0px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 table-row-transitions user-row";
    }
    
    private createComponents(module: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        new ModulesTableBodyRowCell(this.element, module.module);
        new ModulesTableBodyRowCell(this.element, module.description);
        new ModulesTableBodyRowButtonsCell(this.element, module, makeRequestTask);
    }
    
}

class ModulesTableBodyRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-[40%] flex items-center justify-center overflow-hidden custom-scroll";
        this.element.innerText = text;
    }
    
}

class ModulesTableBodyRowButtonsCell {
    
    element!: HTMLElement
    deleteButton!: ModulesTableDeleteButton
    
    constructor(appendTo: HTMLElement, module: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(module, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-[20%] flex gap-x-2 items-center justify-center";
    }
    
    private createComponents(module: {[key: string]: string}, makeRequestTask: MakeRequestTask) {
        this.deleteButton = new ModulesTableDeleteButton(this.element, module.module, makeRequestTask);
    }
    
}

class ModulesTableDeleteButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, module: string, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
        this.startListeners(module, makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-red-700 rounded-md hover:bg-red-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/delete.png", "5");
    }
    
    private startListeners(module: string, makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", async () => {
            const response = await makeRequestTask.delete(`/modules-list/${module}`);
            if (!response.success) {
                new Notification(response.message, "red");
            } else {
                new Notification(response.message, "green");
                const userRow = document.getElementById(`${module}-row`)!;
                userRow.style.height = "0px";
                setTimeout(() => {
                    userRow.remove();
                }, 300);
            }
        });
    }
    
}

class ModulesModal {
    
    element!: HTMLElement
    modal!: ModulesModalContainer
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "modules-modal";
        this.element.className = "w-full h-full fixed flex items-center justify-center z-50 bg-black/80 opacity-fade-in";
    }
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.modal = new ModulesModalContainer(this.element, makeRequestTask);
    }
    
}

class ModulesModalContainer {
    
    element!: HTMLElement
    closeButtonContainer!: ModulesModalCloseButtonContainer
    elementsContainer!: ModulesModalElements
    button!: ModulesModalCreateButton
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col items-center p-3 bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg gap-y-2";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.closeButtonContainer = new ModulesModalCloseButtonContainer(this.element);
        this.elementsContainer = new ModulesModalElements(this.element);
        this.button = new ModulesModalCreateButton(this.element, makeRequestTask);
    }
    
}

class ModulesModalElements {
    
    element!: HTMLElement
    inputsContainer!: ModulesModalInputsContainer
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex flex-1 gap-x-2";
    }
    
    private createComponents() {
        this.inputsContainer = new ModulesModalInputsContainer(this.element);
    }
    
}

class ModulesModalInputsContainer {
    
    element!: HTMLElement
    moduleInput!: ModulesModalInput
    descriptionInput!: ModulesModalInput
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col p-3 items-center justify-center gap-y-2 border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-lg";
    }
    
    private async createComponents() {
        this.moduleInput = new ModulesModalInput(this.element, "text", "Módulo", "modules-modal-module");
        this.descriptionInput = new ModulesModalInput(this.element, "text", "Descrição", "modules-modal-description");
    }
    
}

class ModulesModalCloseButtonContainer {
    
    element!: HTMLElement
    closeButton!: ModulesModalCloseButton
    
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
        this.closeButton = new ModulesModalCloseButton(this.element);
    }
    
}

class ModulesModalCloseButton {
    
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
            const modal = document.getElementById("modules-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
            }, { once: true });
        });
    }
    
}

class ModulesModalInput {
    
    element!: HTMLInputElement
    
    constructor(appendTo: HTMLElement, type: string, placeholder: string, id: string) {
        this.createSelf(placeholder, id, type);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(placeholder: string, id: string, type: string) {
        this.element = document.createElement("input");
        this.element.id = id;
        this.element.type = type;
        this.element.className = "w-[300px] h-[30px] p-2 bg-white border border-gray-300 outline-none rounded-md";
        this.element.placeholder = placeholder;
    }
    
}

class ModulesModalCreateButton {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto p-2 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer text-white";
        this.element.innerText = "Adicionar";
    }
    
    private startListeners(makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", async () => {
            const tableBody = document.getElementById("modules-table-body")!;
            const module = (document.getElementById("modules-modal-module") as HTMLInputElement).value!;
            const description = (document.getElementById("modules-modal-description") as HTMLInputElement).value!;
            const response = await makeRequestTask.post("/modules-list", "application/json", { module, description });
            if (!response.success) {
                new Notification(response.message, "red");
                return;
            } else {
                new Notification(response.message, "green");
            }
            const modal = document.getElementById("modules-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
                let row = new ModulesTableBodyRow(tableBody, { module: module, description: description }, makeRequestTask);
                row.element.offsetHeight;
                row.element.style.height = "46px";
            }, { once: true });
        });
    }
    
}
