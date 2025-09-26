export default class Zadmin {
    
    element!: HTMLElement
    usersContainer!: UsersContainer
    
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
        this.usersContainer = new UsersContainer(this.element);
    }
    
}

class UsersContainer {
    
    element!: HTMLElement
    titleBar!: ContainerTitleBar
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
        this.titleBar = new ContainerTitleBar(this.element);
        this.tableContainer = new UsersTableContainer(this.element);
    }
    
}

class ContainerTitleBar {
    
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
        this.element.placeholder = "Matrícula";
    }
    
}

class SearchUserButton {
    
    element!: HTMLElement
    icon!: ZadminIcon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "h-auto w-auto p-1 bg-blue-700 text-white hover:bg-blue-900 hover:text-black cursor-pointer rounded-md transition-colors duration-300";
    }
    
    private createComponents() {
        this.icon = new ZadminIcon("/storage/images/magnifying_glass.png", this.element);
    }
    
}

class AddUserButton {
    
    element!: HTMLElement
    button!: HTMLElement
    icon!: ZadminIcon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-1 items-center justify-end";
        this.button = document.createElement("button");
        this.button.className = "h-auto w-auto p-1 bg-green-700 text-white hover:bg-green-900 hover:text-black cursor-pointer rounded-md transition-colors duration-300";
        this.element.appendChild(this.button);
        this.button.addEventListener("click", () => {
            
        });
    }
    
    private createComponents() {
        this.icon = new ZadminIcon("/storage/images/plus.png", this.button);
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
        const users: [{[key: string]: string}] = await ZadminTasks.getUser("all");
        users.forEach((user) => {
            new UsersTableBodyRow(this.element, user);
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
        this.element.className = "w-full h-[46px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 opacity-fade-in table-row-transitions";
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
        this.element.className = "p-2 h-auto w-[20%] flex items-center justify-center overflow-x-auto custom-scroll";
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
    icon!: ZadminIcon
    
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
        this.icon = new ZadminIcon("/storage/images/edit.png", this.element);
    }
    
    private startListeners(user: {[key: string]: string}) {
        this.element.addEventListener("click", () => {
            new EditUserModal(document.getElementById("zAdmin")!, user);
        });
    }
    
}

class UsersTableDeleteButton {
    
    element!: HTMLElement
    icon!: ZadminIcon
    
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
        this.icon = new ZadminIcon("/storage/images/delete.png", this.element);
    }
    
    private startListeners(user: string) {
        this.element.addEventListener("click", async () => {
            const response = await fetch(`${window.location.origin}/users/${user}`, {
                method: "DELETE",
            });
            const data = await response.json();
            if (!data.success) {
                new ZadminNotificationPopUp(data.message, "red");
            } else {
                new ZadminNotificationPopUp(data.message, "green");
                const userRow = document.getElementById(`${user}-row`)!;
                userRow.classList.add("opacity-fade-out");
                userRow.addEventListener("animationend", () => {
                    userRow.style.opacity = "0";
                    userRow.style.height = "0px";
                    userRow.addEventListener("transitionend", () => {
                        userRow.remove();
                    }, { once: true });
                }, { once: true });
            }
        });
    }
    
}

class ZadminIcon {
    
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

class ZadminNotificationPopUp {
    
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

class EditUserModal {
    
    element!: HTMLElement
    modal!: EditUserModalContainer
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "edit-user-modal";
        this.element.className = "w-full h-full fixed flex items-center justify-center z-50 bg-black/80 opacity-fade-in";
    }
    private createComponents(user: {[key: string]: string}) {
        this.modal = new EditUserModalContainer(this.element, user);
    }
    
}

class EditUserModalContainer {
    
    element!: HTMLElement
    closeButtonContainer!: EditUserModalCloseButtonContainer
    elementsContainer!: EditUserModalElements
    button!: EditUserModalSaveButton
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col items-center p-3 bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg gap-y-2";
    }
    
    private createComponents(user: {[key: string]: string}) {
        this.closeButtonContainer = new EditUserModalCloseButtonContainer(this.element);
        this.elementsContainer = new EditUserModalElements(this.element, user);
        this.button = new EditUserModalSaveButton(this.element);
    }
    
}

class EditUserModalElements {
    
    element!: HTMLElement
    inputsContainer!: EditUserModalInputsContainer
    tableContainer!: EditUserModalTableContainer
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-auto flex flex-1 gap-x-2";
    }
    
    private createComponents(user: {[key: string]: string}) {
        this.inputsContainer = new EditUserModalInputsContainer(this.element, user);
        this.tableContainer = new EditUserModalTableContainer(this.element, user);
    }
    
}

class EditUserModalInputsContainer {
    
    element!: HTMLElement
    userInput!: EditUserModalInput
    nameInput!: EditUserModalInput
    emailInput!: EditUserModalInput
    passwordInput!: EditUserModalInput
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col p-3 items-center justify-center gap-y-2 border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-lg";
    }
    
    private async createComponents(user: {[key: string]: string}) {
        const userDataUpdated = await ZadminTasks.getUser(user.user)
        this.userInput = new EditUserModalInput(this.element, "text", "Usuário", "edit-user-modal-user", userDataUpdated);
        this.nameInput = new EditUserModalInput(this.element, "text", "Nome", "edit-user-modal-name", userDataUpdated);
        this.emailInput = new EditUserModalInput(this.element, "text", "E-mail", "edit-user-modal-email", userDataUpdated);
        this.passwordInput = new EditUserModalInput(this.element, "text", "Senha", "edit-user-modal-password", userDataUpdated);
    }
    
}

class EditUserModalTableContainer {
    
    element!: HTMLElement
    permissionsTableContainer!: PermissionsTableContainer
    selectContainer!: ModalModulesListContainer
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[300px] h-[300px] flex flex-col p-3 gap-y-2 items-center justify-center border border-gray-300 dark:border-gray-900 transition-colors duration-300 rounded-lg";
    }
    
    private createComponents(user: {[key: string]: string}) {
        this.selectContainer = new ModalModulesListContainer(this.element);
        this.permissionsTableContainer = new PermissionsTableContainer(this.element, user);
    }
    
}

class ModalModulesListContainer {
    
    element!: HTMLElement
    select!: ModalModulesList
    button!: AddModuleButton
    
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
        this.select = new ModalModulesList(this.element);
        this.button = new AddModuleButton(this.element);
    }
    
}

class ModalModulesList {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("select");
        this.element.className = "h-auto w-auto bg-white border border-gray-300 rounded-md p-1";
    }
    
    private async createComponents() {
        const modules: [{[key: string]: string}] = await ZadminTasks.getModulesList();
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

class AddModuleButton {
    
    element!: HTMLElement
    icon!: ZadminIcon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "h-auto w-auto p-1 bg-green-700 text-white hover:bg-green-900 hover:text-black cursor-pointer rounded-md transition-colors duration-300";
        this.element.addEventListener("click", () => {
            
        });
    }
    
    private createComponents() {
        this.icon = new ZadminIcon("/storage/images/plus.png", this.element);
    }
    
}

class EditUserModalCloseButtonContainer {
    
    element!: HTMLElement
    closeButton!: EditUserModalCloseButton
    
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
        this.closeButton = new EditUserModalCloseButton(this.element);
    }
    
}

class EditUserModalCloseButton {
    
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
            const modal = document.getElementById("edit-user-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
            }, { once: true });
        });
    }
    
}

class EditUserModalInput {
    
    element!: HTMLInputElement
    
    constructor(appendTo: HTMLElement, type: string, placeholder: string, id: string, user: {[key: string]: string}) {
        this.createSelf(placeholder, id, type, user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(placeholder: string, id: string, type: string, user: {[key: string]: string}) {
        this.element = document.createElement("input");
        this.element.id = id;
        this.element.type = type;
        this.element.className = "w-[300px] h-[30px] p-2 bg-white border border-gray-300 outline-none rounded-md";
        this.element.placeholder = placeholder;
        if (id == "edit-user-modal-user") {
            this.element.value = user.user;
        }
        if (id == "edit-user-modal-name") {
            this.element.value = user.name;
        }
        if (id == "edit-user-modal-email") {
            this.element.value = user.email;
        }
        if (id == "edit-user-modal-password") {
            this.element.value = user.password;
        }
    }
    
}

class CreateUserModalCreateButton {
    
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
            const user = (document.getElementById("create-user-modal-user") as HTMLInputElement).value!;
            const name = (document.getElementById("create-user-modal-name") as HTMLInputElement).value!;
            const email = (document.getElementById("create-user-modal-email") as HTMLInputElement).value!;
            const password = (document.getElementById("create-user-modal-password") as HTMLInputElement).value!;
            const response = await fetch(`${window.location.origin}/users`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user, name, email, password })
            });
            const data = await response.json();
            if (!data.success) {
                new ZadminNotificationPopUp(data.message, "red");
            } else {
                new ZadminNotificationPopUp(data.message, "green");
                const modal = document.getElementById("crate-user-modal")!;
                modal.classList.remove("opacity-fade-in");
                modal.classList.add("opacity-fade-out");
                modal.addEventListener("animationend", () => {
                    modal.remove();
                    new UsersTableBodyRow(tableBody, { user: user, name: name, email: email, password: password });
                }, { once: true });
            }
        });
    }
    
}

class EditUserModalSaveButton {
    
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
            const user = (document.getElementById("edit-user-modal-user") as HTMLInputElement).value!;
            const name = (document.getElementById("edit-user-modal-name") as HTMLInputElement).value!;
            const email = (document.getElementById("edit-user-modal-email") as HTMLInputElement).value!;
            const password = (document.getElementById("edit-user-modal-password") as HTMLInputElement).value!;
            const permissionsElements = document.querySelectorAll<HTMLElement>("permissions-cell");
            const permissionsList: string[] = [];
            permissionsElements.forEach(element => {
                permissionsList.push(element.innerText.toLowerCase());
            });
            const data = await ZadminTasks.updateUser(user, name, email, password);
            if (!data.success) {
                new ZadminNotificationPopUp(data.message, "red");
                return;
            } else {
                new ZadminNotificationPopUp(data.message, "green");
            }
            if (permissionsElements.length != 0) {
                const data = await ZadminTasks.updateUserPermissions(user, permissionsList);
                if (!data.success) {
                    new ZadminNotificationPopUp(data.message, "red");
                    return;
                } else {
                    new ZadminNotificationPopUp(data.message, "green");
                }
            }
            const modal = document.getElementById("edit-user-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
                let userRow = document.getElementById(`${user}-row`)!;
                userRow.classList.remove("opacity-fade-in");
                userRow.classList.add("opacity-fade-out");
                userRow.addEventListener("animationend", () => {
                    document.getElementById(`${user}-user-cell`)!.innerText = user;
                    document.getElementById(`${user}-name-cell`)!.innerText = name;
                    document.getElementById(`${user}-email-cell`)!.innerText = email;
                    document.getElementById(`${user}-password-cell`)!.innerText = password;
                    userRow.classList.remove("opacity-fade-out");
                    userRow.classList.add("opacity-fade-in");
                }, { once: true });
            }, { once: true });
        });
    }
    
}

class PermissionsTableContainer {
    
    element!: HTMLElement
    modulesTable!: PermissionsTable
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-full flex-1 overflow-y-auto custom-scroll";
    }
    
    private createComponents(user: {[key: string]: string}) {
        this.modulesTable = new PermissionsTable(this.element, user);   
    }
    
}

class PermissionsTable {
    
    element!: HTMLElement
    tableHead!: PermissionsTableHead
    tableBody!: PermissionsTableBody
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-auto w-full flex flex-col whitespace-nowrap cursor-default border-collapse text-center text-black dark:text-white transition-colors duration-300";
    }
    
    private createComponents(user: {[key: string]: string}) {
        this.tableHead = new PermissionsTableHead(this.element);
        this.tableBody = new PermissionsTableBody(this.element, user);
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
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "permissions-table-body";
        this.element.className = "w-auto h-auto flex flex-col";
    }
    
    private async createComponents(user: {[key: string]: string}) {
        const permissions: [{[key: string]: string}] = await ZadminTasks.getUserPermissions(user);
        permissions.forEach((permission) => {
            new PermissionsTableBodyRow(this.element, permission);
        });
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
        this.element.id = permission.module
        this.element.className = "w-full h-[46px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 opacity-fade-in table-row-transitions";
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
        this.element.className = "permissions-cell p-2 h-auto w-[80%] flex items-center justify-center overflow-x-auto custom-scroll";
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
    icon!: ZadminIcon
    
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
        this.icon = new ZadminIcon("/storage/images/delete.png", this.element);
    }
    
    private startListeners(permission: {[key: string]: string}) {
        this.element.addEventListener("click", async () => {
            const data = await ZadminTasks.deleteUserPermission(permission);
            if (!data.success) {
                new ZadminNotificationPopUp(data.message, "red");
            } else {
                new ZadminNotificationPopUp(data.message, "green");
                const permissionRow = document.getElementById(permission.module)!;
                permissionRow.classList.add("opacity-fade-out");
                permissionRow.addEventListener("animationend", () => {
                    permissionRow.style.opacity = "0";
                    permissionRow.style.height = "0px";
                    permissionRow.addEventListener("transitionend", () => {
                        permissionRow.remove();
                    }, { once: true });
                }, { once: true });
            }
        });
    }
    
}

class ZadminTasks {
    
    static async getUser(user: string) {
        const response = await fetch(`${window.location.origin}/users/${user}`);
        const data = await response.json();
        return data;
    }
    
    static async getUserPermissions(user: {[key: string]: string}) {
        const response = await fetch(`${window.location.origin}/permissions/${user.user}`);
        const data = await response.json();
        return data;
    }
    
    static async updateUserPermissions(user: string, permissionsList: string[]) {
        const response = await fetch(`${window.location.origin}/permissions/${user}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ permissionsList })
        });
        const data = await response.json();
        return data;
    }
    
    static async deleteUserPermission(permission: {[key: string]: string}) {
        const response = await fetch(`${window.location.origin}/permissions/${permission.user}/${permission.module.toLowerCase()}`, {
            method: "DELETE",
        });
        const data = await response.json();
        return data;
    }
    
    static async updateUser(user: string, name: string, email: string, password: string) {
        const response = await fetch(`${window.location.origin}/users/${user}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user, name, email, password })
        });
        const data = await response.json();
        return data;
    }
    
    static async getModulesList() {
        const response = await fetch(`${window.location.origin}/modules-list`);
        const data = await response.json();
        return data;
    }
    
}
