export default class Zusers {
    
    element!: HTMLElement
    usersContainer!: UsersContainer
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zUsers";
        this.element.className = "w-full h-full opacity-fade-in bg-gray-300 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center";
    }
    
    private createComponents() {
        this.usersContainer = new UsersContainer(this.element);
    }
    
}

class UsersContainer {
    
    element!: HTMLElement
    titleBar!: TitleBar
    tableContainer!: TableContainer
    
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
        this.titleBar = new TitleBar(this.element);
        this.tableContainer = new TableContainer(this.element);
    }
    
}

class TitleBar {
    
    element!: HTMLElement
    searchInput!: SearchInput
    searchButton!: SearchButton
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
        this.searchInput = new SearchInput(this.element);
        this.searchButton = new SearchButton(this.element);
        this.addUserButton = new AddUserButton(this.element);
    }
    
}

class SearchInput {
    
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

class SearchButton {
    
    element!: HTMLElement
    icon!: Icon
    
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
        this.icon = new Icon("/storage/images/magnifying_glass.png", this.element);
    }
    
}

class AddUserButton {
    
    element!: HTMLElement
    button!: HTMLElement
    icon!: Icon
    
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
            new CreateUserModal(document.getElementById("zUsers")!);
        });
    }
    
    private createComponents() {
        this.icon = new Icon("/storage/images/plus.png", this.button);
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
        this.element.className = "size-6 opacity-fade-in";
    }
    
}

class TableContainer {
    
    element!: HTMLElement
    tableWrapper!: Table
    
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
        this.tableWrapper = new Table(this.element);   
    }
    
}

class Table {
    
    element!: HTMLElement
    tableHead!: TableHead
    tableBody!: TableBody
    
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
        this.tableHead = new TableHead(this.element);
        this.tableBody = new TableBody(this.element);
    }
    
}

class TableHead {
    
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
        new TableHeadRowCell(this.element, "Usuário");
        new TableHeadRowCell(this.element, "Nome");
        new TableHeadRowCell(this.element, "E-mail");
        new TableHeadRowCell(this.element, "Senha");
        new TableHeadRowCell(this.element, "");
    }
    
}

class TableHeadRowCell {
    
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

class TableBody {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "table-body";
        this.element.className = "w-auto h-auto flex flex-col";
    }
    
    private async createComponents() {
        const users: [{[key: string]: string}] = await ZusersTasks.getAllUsers();
        users.forEach((user) => {
            new TableBodyRow(this.element, user);
        });
    }
    
}

class TableBodyRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf(user.user);
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(user: string) {
        this.element = document.createElement("div");
        this.element.id = user;
        this.element.className = "w-full h-[46px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 opacity-fade-in table-row-transitions";
    }
    
    private createComponents(user: {[key: string]: string}) {
        new TableBodyRowCell(this.element, user.user);
        new TableBodyRowCell(this.element, user.name);
        new TableBodyRowCell(this.element, user.email);
        new TableBodyRowCell(this.element, user.password);
        new TableBodyRowButtonsCell(this.element, user.user);
    }
    
}

class TableBodyRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-[20%] flex items-center justify-center overflow-x-auto custom-scroll";
        this.element.innerText = text;
    }
    
}

class TableBodyRowButtonsCell {
    
    element!: HTMLElement
    editButton!: EditButton
    deleteButton!: DeleteButton
    
    constructor(appendTo: HTMLElement, user: string) {
        this.createSelf();
        this.createComponents(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "p-2 h-auto w-[20%] flex gap-x-2 items-center justify-center";
    }
    
    private createComponents(user: string) {
        this.editButton = new EditButton(this.element);
        this.deleteButton = new DeleteButton(this.element, user);
    }
    
}

class EditButton {
    
    element!: HTMLElement
    icon!: ZusersIcon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "p-1 h-auto w-auto h-auto bg-blue-700 rounded-md hover:bg-blue-900 transition-colors duration-300 cursor-pointer";
    }
    private createComponents() {
        this.icon = new ZusersIcon("/storage/images/edit.png", this.element);
    }
    
}

class DeleteButton {
    
    element!: HTMLElement
    icon!: ZusersIcon
    
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
        this.icon = new ZusersIcon("/storage/images/delete.png", this.element);
    }
    
    private startListeners(user: string) {
        this.element.addEventListener("click", async () => {
            const response = await fetch(`${window.location.origin}/users/${user}`, {
                method: "DELETE",
            });
            const data = await response.json();
            if (!data.success) {
                new NotificationPopUp(data.message, "red");
            } else {
                new NotificationPopUp(data.message, "green");
                const userRow = document.getElementById(user)!;
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

class ZusersIcon {
    
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

class CreateUserModal {
    
    element!: HTMLElement
    modal!: CreateUserModalForm
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "create-user-modal";
        this.element.className = "w-full h-full fixed flex items-center justify-center z-50 bg-black/80 opacity-fade-in";
    }
    private createComponents() {
        this.modal = new CreateUserModalForm(this.element);
    }
    
}

class CreateUserModalForm {
    
    element!: HTMLElement
    closeButtonContainer!: CreateUserModalFormCloseContainer
    userInput!: CreateUserModalFormInput
    nameInput!: CreateUserModalFormInput
    emailInput!: CreateUserModalFormInput
    passwordInput!: CreateUserModalFormInput
    createButton!: CreateUserModalFormButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex flex-col items-center justify-center p-3 bg-white dark:bg-gray-700 transition-colors duration-300 rounded-lg gap-y-2";
    }
    private createComponents() {
        this.closeButtonContainer = new CreateUserModalFormCloseContainer(this.element);
        this.userInput = new CreateUserModalFormInput(this.element, "text", "Usuário", "create-user-modal-user");
        this.nameInput = new CreateUserModalFormInput(this.element, "text", "Nome", "create-user-modal-name");
        this.emailInput = new CreateUserModalFormInput(this.element, "text", "E-mail", "create-user-modal-email");
        this.passwordInput = new CreateUserModalFormInput(this.element, "text", "Senha", "create-user-modal-password");
        this.createButton = new CreateUserModalFormButton(this.element);
    }
    
}

class CreateUserModalFormCloseContainer {
    
    element!: HTMLElement
    closeButton!: CreateUserModalFormCloseButton
    
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
        this.closeButton = new CreateUserModalFormCloseButton(this.element);
    }
    
}

class CreateUserModalFormCloseButton {
    
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
            const modal = document.getElementById("create-user-modal")!;
            modal.classList.remove("opacity-fade-in");
            modal.classList.add("opacity-fade-out");
            modal.addEventListener("animationend", () => {
                modal.remove();
            }, { once: true });
        });
    }
    
}

class CreateUserModalFormInput {
    
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

class CreateUserModalFormButton {
    
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
            const tableBody = document.getElementById("table-body")!;
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
                new NotificationPopUp(data.message, "red");
            } else {
                new NotificationPopUp(data.message, "green");
                const modal = document.getElementById("create-user-modal")!;
                modal.classList.remove("opacity-fade-in");
                modal.classList.add("opacity-fade-out");
                modal.addEventListener("animationend", () => {
                    modal.remove();
                    new TableBodyRow(tableBody, { user: user, name: name, email: email, password: password });
                }, { once: true });
            }
        });
    }
    
}

class NotificationPopUp {
    
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

class ZusersTasks {
    
    static async getAllUsers() {
        const response = await fetch(`${window.location.origin}/users/all`);
        const data = await response.json();
        return data;
    }
    
}
