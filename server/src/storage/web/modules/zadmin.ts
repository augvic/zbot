export default class zAdmin {
    
    element!: HTMLElement
    usersContainer!: Container
    
    constructor(moduleContainer: HTMLElement) {
        this.createSelf();
        this.createComponents();
        moduleContainer.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zAdmin";
        this.element.className = "w-full h-full opacity-fade-in bg-gray-300 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center";
    }
    
    private createComponents() {
        this.usersContainer = new Container(this.element);
    }
    
}

class Container {
    
    element!: HTMLElement
    titleBar!: ContainerTopBar
    tableContainer!: UsersTableContainer
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[95%] h-[95%] flex flex-col bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg p-5 gap-3";
    }
    
    private createComponents() {
        this.titleBar = new ContainerTopBar(this.element);
        this.tableContainer = new UsersTableContainer(this.element);
    }
    
}

class ContainerTopBar {
    
    element!: HTMLElement
    searchInput!: SearchUserInput
    searchButton!: SearchUserButton
    addUserButton!: AddUserButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex items-center gap-2";
    }
    
    private createComponents() {
        this.searchInput = new SearchUserInput(this.element);
        this.searchButton = new SearchUserButton(this.element);
        this.addUserButton = new AddUserButton(this.element);
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
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "h-auto w-auto p-1 bg-blue-700 text-white hover:bg-blue-900 hover:text-black cursor-pointer rounded-md transition-colors duration-300";
    }
    
    private createComponents() {
        this.icon = new Icon("/static/images/magnifying_glass.png", this.element);
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
    button!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-1 items-center justify-end";
        this.button = document.createElement("button");
        this.button.className = "h-auto w-auto p-1 bg-green-700 text-white hover:bg-green-900 hover:text-black cursor-pointer rounded-md transition-colors duration-300";
        this.element.appendChild(this.button);
    }
    
    private createComponents() {
        this.icon = new Icon("/static/images/plus.png", this.button);
    }
    
    private startListeners() {
        this.button.addEventListener("click", () => {
            new UserModal(document.getElementById("zAdmin")!, {}, false);
        });
    }
    
}

class UsersTableContainer {
    
    element!: HTMLElement
    table!: UsersTable
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex-1 overflow-y-auto custom-scroll";
    }
    
    private createComponents() {
        this.table = new UsersTable(this.element);   
    }
    
}

class UsersTable {
    
    element!: HTMLElement
    tableHead!: UsersTableHead
    tableBody!: UsersTableBody
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-auto w-full flex flex-col whitespace-nowrap cursor-default border-collapse text-center text-black dark:text-white transition-colors duration-300";
    }
    
    private createComponents() {
        this.tableHead = new UsersTableHead(this.element);
        this.tableBody = new UsersTableBody(this.element);
    }
    
}

class UsersTableHead {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
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
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "users-table-body";
        this.element.className = "w-auto h-auto flex flex-col";
    }
    
    private async createComponents() {
        const response = await fetch(`${window.location.origin}/users/all`);
        const data: {[key: string]: boolean | [{}] | string} = await response.json();
        if (!data.success) {
            new Notification(data.message as string, "red");
        }
        const users = data.users as [{}]
        users.forEach((user: {}) => {
            let row = new UsersTableBodyRow(this.element, user);
            row.element.offsetHeight;
            row.element.style.height = "46px";
        });
    }
    
}

class UsersTableBodyRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf(user.user);
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(user: string) {
        this.element = document.createElement("div");
        this.element.id = `${user}-row`;
        this.element.className = "w-full h-[0px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 table-row-transitions user-row";
    }
    
    private createComponents(user: {[key: string]: string}) {
        new UsersTableBodyRowCell(this.element, user.user, user.user, "user");
        new UsersTableBodyRowCell(this.element, user.name, user.user, "name");
        new UsersTableBodyRowCell(this.element, user.email, user.user, "email");
        new UsersTableBodyRowCell(this.element, user.password, user.user, "password");
        new UsersTableBodyRowButtonsCell(this.element, user);
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
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-[20%] flex gap-x-2 items-center justify-center";
    }
    
    private createComponents(user: {[key: string]: string}) {
        this.editButton = new UsersTableEditButton(this.element, user);
        this.deleteButton = new UsersTableDeleteButton(this.element, user.user);
    }
    
}

class UsersTableEditButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents();
        this.startListeners(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-blue-700 rounded-md hover:bg-blue-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new Icon("/static/images/edit.png", this.element);
    }
    
    private startListeners(user: {[key: string]: string}) {
        this.element.addEventListener("click", () => {
            new UserModal(document.getElementById("zAdmin")!, user, true);
        });
    }
    
}

class UsersTableDeleteButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, user: string) {
        this.createSelf();
        this.createComponents();
        this.startListeners(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-red-700 rounded-md hover:bg-red-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new Icon("/static/images/delete.png", this.element);
    }
    
    private startListeners(user: string) {
        this.element.addEventListener("click", async () => {
            const response = await fetch(`${window.location.origin}/users/${user}`, {
                method: "DELETE",
            });
            const data = await response.json();
            if (!data.success) {
                new Notification(data.message, "red");
            } else {
                new Notification(data.message, "green");
                const userRow = document.getElementById(`${user}-row`)!;
                userRow.style.height = "0px";
                setTimeout(() => {
                    userRow.remove();
                }, 300);
            }
        });
    }
    
}

class Icon {
    
    element!: HTMLImageElement
    
    constructor(src: string, appendTo: HTMLElement) {
        this.createSelf(src);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(src: string) {
        this.element = document.createElement("img");
        this.element.src = src;
        this.element.className = "size-5 opacity-fade-in";
    }
    
}

class Notification {
    
    element!: HTMLElement
    
    constructor(message: string, color: string) {
        this.createSelf(message, color);
        this.pushUpExistingNotifications();
        document.body.appendChild(this.element);
        setTimeout(() => {
            this.element.classList.remove("fade-in-right");
            this.element.classList.add("fade-out-right");
            this.element.addEventListener("animationend", () => {
                this.element.remove()
            }, { once: true });
        }, 3000);
    }
    
    private createSelf(message: string, color: string) {
        this.element = document.createElement("div");
        this.element.className = "notification fixed z-50 bottom-4 right-5 py-3 px-6 text-white rounded-md cursor-default fade-in-right transition-[bottom] duration-300 ease";
        if (color == "green") {
            this.element.classList.add("bg-green-400");
        } else if (color == "orange") {
            this.element.classList.add("bg-amber-400");
        } else if (color == "red") {
            this.element.classList.add("bg-red-400");
        }
        this.element.innerText = message;
    }
    
    private pushUpExistingNotifications() {
        const notifications = document.querySelectorAll<HTMLElement>(".notification");
        notifications.forEach(notification => {
            if (notification != this.element) {
                const currentBottom = parseInt(
                    getComputedStyle(notification).bottom.replace("px", "")
                );
                notification.style.bottom = (currentBottom + 60) + "px";
            }
        });
    }
    
}

class UserModal {
    
    element!: HTMLElement
    modal!: UserModalContainer
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean) {
        this.createSelf();
        this.createComponents(user, editModal);
        setTimeout(() => {
            appendTo.appendChild(this.element);
        }, 200);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "user-modal";
        this.element.className = "w-full h-full fixed flex items-center justify-center z-50 bg-black/80 opacity-fade-in";
    }
    private createComponents(user: {[key: string]: string}, editModal: boolean) {
        this.modal = new UserModalContainer(this.element, user, editModal);
    }
    
}

class UserModalContainer {
    
    element!: HTMLElement
    closeButtonContainer!: UserModalCloseButtonContainer
    elementsContainer!: UserModalElements
    button!: UserModalSaveButton | UserModalCreateButton
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean) {
        this.createSelf();
        this.createComponents(user, editModal);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col items-center p-3 bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg gap-y-2";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean) {
        this.closeButtonContainer = new UserModalCloseButtonContainer(this.element);
        this.elementsContainer = new UserModalElements(this.element, user, editModal);
        if (editModal) {
            this.button = new UserModalSaveButton(this.element);
        } else {
            this.button = new UserModalCreateButton(this.element);
        }
    }
    
}

class UserModalElements {
    
    element!: HTMLElement
    inputsContainer!: UserModalInputsContainer
    tableContainer!: UserModalTableContainer
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean) {
        this.createSelf();
        this.createComponents(user, editModal);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex flex-1 gap-x-2";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean) {
        this.inputsContainer = new UserModalInputsContainer(this.element, user, editModal);
        this.tableContainer = new UserModalTableContainer(this.element, user, editModal);
    }
    
}

class UserModalInputsContainer {
    
    element!: HTMLElement
    userInput!: UserModalInput
    nameInput!: UserModalInput
    emailInput!: UserModalInput
    passwordInput!: UserModalInput
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean) {
        this.createSelf();
        this.createComponents(user, editModal);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col p-3 items-center justify-center gap-y-2 border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-lg";
    }
    
    private async createComponents(user: {[key: string]: string}, editModal: boolean) {
        if (editModal) {
            const response = await fetch(`${window.location.origin}/users/${user.user}`);
            const data = await response.json();
            if (!data.success) {
                new Notification(data.message, "red");
            }
            const userDataUpdated = data.users;
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
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean) {
        this.createSelf();
        this.createComponents(user, editModal);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[300px] h-[300px] flex flex-col p-3 gap-y-2 items-center justify-center border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-lg";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean) {
        this.selectContainer = new UserModalModulesListContainer(this.element);
        this.permissionsTableContainer = new PermissionsTableContainer(this.element, user, editModal);
    }
    
}

class UserModalModulesListContainer {
    
    element!: HTMLElement
    select!: UserModalModulesList
    button!: UserModalAddModuleButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex gap-x-2";
    }
    
    private createComponents() {
        this.select = new UserModalModulesList(this.element);
        this.button = new UserModalAddModuleButton(this.element);
    }
    
}

class UserModalModulesList {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("select");
        this.element.id = "modules-list";
        this.element.className = "h-auto w-auto bg-white border border-gray-300 rounded-md p-1";
    }
    
    private async createComponents() {
        const response = await fetch(`${window.location.origin}/modules-list`);
        const data: {[key: string]: string | boolean | [{}]} = await response.json();
        if (!data.success) {
            new Notification(data.message as string, "red");
        }
        const modules = data.modules as [{[key: string]: string}]
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
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "h-auto w-auto p-1 bg-green-700 text-white hover:bg-green-900 hover:text-black cursor-pointer rounded-md transition-colors duration-300";
    }
    
    private createComponents() {
        this.icon = new Icon("/static/images/plus.png", this.element);
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
        this.createComponents();
        appendTo.appendChild(this.element);
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
        this.startListeners();
        appendTo.appendChild(this.element);
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
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto p-2 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer text-white";
        this.element.innerText = "Criar";
    }
    
    private startListeners() {
        this.element.addEventListener("click", async () => {
            const tableBody = document.getElementById("users-table-body")!;
            const user = (document.getElementById("user-modal-user") as HTMLInputElement).value!;
            const name = (document.getElementById("user-modal-name") as HTMLInputElement).value!;
            const email = (document.getElementById("user-modal-email") as HTMLInputElement).value!;
            const password = (document.getElementById("user-modal-password") as HTMLInputElement).value!;
            const response = await fetch(`${window.location.origin}/users`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user, name, email, password })
            });
            const data = await response.json();
            if (!data.success) {
                new Notification(data.message, "red");
                return;
            }
            const permissionsToCreate = document.querySelectorAll<HTMLElement>(".permission-to-create");
            permissionsToCreate.forEach(async permission => {
                const response = await fetch(`${window.location.origin}/permissions/${user}/${permission.innerText}`, {
                    method: "POST"
                });
                const data = await response.json();
                if (!data.success) {
                    new Notification(data.message, "red");
                    return;
                }
            });
            new Notification("Usuário criado.", "green");
            const modal = document.getElementById("user-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
                let row = new UsersTableBodyRow(tableBody, { user: user, name: name, email: email, password: password });
                row.element.offsetHeight;
                row.element.style.height = "46px";
            }, { once: true });
        });
    }
    
}

class UserModalSaveButton {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto p-2 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer text-white";
        this.element.innerText = "Salvar";
    }
    
    private startListeners() {
        this.element.addEventListener("click", async () => {
            const user = (document.getElementById("user-modal-user") as HTMLInputElement).value!;
            const name = (document.getElementById("user-modal-name") as HTMLInputElement).value!;
            const email = (document.getElementById("user-modal-email") as HTMLInputElement).value!;
            const password = (document.getElementById("user-modal-password") as HTMLInputElement).value!;
            const response = await fetch(`${window.location.origin}/users/${user}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user, name, email, password })
            });
            const data = await response.json();
            if (!data.success) {
                new Notification(data.message, "red");
                return;
            }
            const permissionsToDelete = document.querySelectorAll<HTMLElement>(".permission-to-delete");
            permissionsToDelete.forEach(async permission => {
                const response = await fetch(`${window.location.origin}/permissions/${user}/${permission.innerText}`, {
                    method: "DELETE"
                });
                const data = await response.json();
                if (!data.success) {
                    new Notification(data.message, "red");
                    return;
                }
            });
            const permissionsToCreate = document.querySelectorAll<HTMLElement>(".permission-to-create");
            permissionsToCreate.forEach(async permission => {
                const response = await fetch(`${window.location.origin}/permissions/${user}/${permission.innerText}`, {
                    method: "POST"
                });
                const data = await response.json();
                if (!data.success) {
                    new Notification(data.message, "red");
                    return;
                }
            });
            new Notification("Usuário atualizado.", "green");
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
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean) {
        this.createSelf();
        this.createComponents(user, editModal);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-full flex-1 overflow-y-auto custom-scroll";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean) {
        this.modulesTable = new PermissionsTable(this.element, user, editModal);   
    }
    
}

class PermissionsTable {
    
    element!: HTMLElement
    tableHead!: PermissionsTableHead
    tableBody!: PermissionsTableBody
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean) {
        this.createSelf();
        this.createComponents(user, editModal);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-auto w-full flex flex-col whitespace-nowrap cursor-default border-collapse text-center text-black dark:text-white transition-colors duration-300";
    }
    
    private createComponents(user: {[key: string]: string}, editModal: boolean) {
        this.tableHead = new PermissionsTableHead(this.element);
        this.tableBody = new PermissionsTableBody(this.element, user, editModal);
    }
    
}

class PermissionsTableHead {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
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
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}, editModal: boolean) {
        this.createSelf();
        this.createComponents(user, editModal);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "permissions-table-body";
        this.element.className = "w-auto h-auto flex flex-col";
    }
    
    private async createComponents(user: {[key: string]: string}, editModal: boolean) {
        if (editModal) {
            const response = await fetch(`${window.location.origin}/permissions/${user.user}`);
            const data: {[key: string]: boolean | string | [string]} = await response.json();
            if (!data.success) {
                new Notification(data.message as string, "red");
            }
            const permissions = data.permissions as [{}]
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
        this.createComponents(permission);
        appendTo.appendChild(this.element);
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
        this.createComponents(permission);
        appendTo.appendChild(this.element);
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
        this.createComponents();
        this.startListeners(permission);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-red-700 rounded-md hover:bg-red-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new Icon("/static/images/delete.png", this.element);
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
