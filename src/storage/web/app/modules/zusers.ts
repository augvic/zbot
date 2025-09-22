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
    table!: Table
    
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
        this.table = new Table(this.element);
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

class Table {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("table");
        this.element.className = "h-auto w-full flex flex-1 bg-blue-300";
    }
    
    private createComponets() {

    }
    
}

class TableHead {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("thead");
        this.element.className = "h-auto w-full bg-green-300";
    }
    
    private createComponets() {

    }
    
}

class TableHeadRow {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("tr");
        this.element.className = "p-2 h-auto w-full";
    }
    
    private createComponets() {

    }
    
}

class TableColumn {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("tr");
        this.element.className = "p-2 h-auto w-full";
    }
    
    private createComponets() {

    }
    
}