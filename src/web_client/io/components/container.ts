export class Container {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, width: string, height: string) {
        this.createSelf(width, height);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(width: string, height: string) {
        this.element = document.createElement("div");
        this.element.className = "flex flex-col items-center justify-center bg-white dark:bg-gray-700 rounded-md gap-2 opacity-fade-in transition-colors duration-300";
        this.element.style.width = width;
        this.element.style.height = height;
    }
    
}