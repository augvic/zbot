export class Label {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("h1");
        this.element.className = "text-black dark:text-white font-bold text-2xl cursor-default transition-colors duration-300";
        this.element.innerText = "Login";
    }
    
}
