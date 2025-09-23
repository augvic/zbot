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
        this.icon = new Icon("/static/images/magnifying_glass.png", this.element);
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
    }
    
    private createComponents() {
        this.icon = new Icon("/static/images/plus.png", this.button);
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
    table!: Table
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponets();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-auto h-auto flex-1 overflow-y-auto custom-scroll";
    }
    
    private createComponets() {
        this.table = new Table(this.element);   
    }
    
}

class Table {
    
    element!: HTMLElement
    tableHead!: TableHead
    tableBody!: TableBody
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponets();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("table");
        this.element.className = "h-auto w-full whitespace-nowrap cursor-default border-collapse text-center text-black dark:text-white transition-colors duration-300";
    }
    
    private createComponets() {
        this.tableHead = new TableHead(this.element);
        this.tableBody = new TableBody(this.element);   
    }
    
}

class TableHead {
    
    element!: HTMLElement
    row!: TableHeadRow
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponets();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("thead");
        this.element.className = "h-auto w-auto";
    }
    
    private createComponets() {
        this.row = new TableHeadRow(this.element);
    }
    
}

class TableHeadRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponets();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("tr");
        this.element.className = "h-auto w-auto bg-gray-300 dark:bg-gray-900 transition-colors duration-300 sticky top-0";
    }
    
    private createComponets() {
        new TableHeadRowCell(this.element, "Usuário");
        new TableHeadRowCell(this.element, "Nome");
        new TableHeadRowCell(this.element, "E-mail");
        new TableHeadRowCell(this.element, "Senha");
    }
    
}

class TableHeadRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("th");
        this.element.className = "p-2 h-auto w-auto";
        this.element.innerText = text;
    }
    
}

class TableBody {
    
    element!: HTMLElement
    usersGetter!: UsersGetter
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("tbody");
        this.element.className = "h-auto w-auto";
    }
    
    private createComponents() {
        (async () => {
            this.usersGetter = new UsersGetter();
            const users: [{[key: string]: string}] = await this.usersGetter.getUsers()
            users.forEach((user) => {
                new TableBodyRow(this.element, user);
            });
        })();
    }
    
}

class TableBodyRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, user: {[key: string]: string}) {
        this.createSelf();
        this.createComponets(user);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("tr");
        this.element.className = "h-auto w-auto";
    }
    
    private createComponets(user: {[key: string]: string}) {
        new TableBodyRowCell(this.element, user.user);
        new TableBodyRowCell(this.element, user.name);
        new TableBodyRowCell(this.element, user.email);
        new TableBodyRowCell(this.element, user.password);
    }
    
}

class TableBodyRowCell {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("td");
        this.element.className = "p-2 h-auto w-auto";
        this.element.innerText = text;
    }
    
}

class UsersGetter {
    
    async getUsers() {
        const response = await fetch(`${window.location.origin}/users/all`);
        const data = await response.json();
        return data;
    }
    
}