export class Page {
    
    element!: HTMLElement
    
    
    constructor(id: string) {
        this.createSelf(id);
        document.body.appendChild(this.element);
    }
    
    private createSelf(id: string) {
        this.element = document.createElement("div");
        this.element.id = id;
        this.element.className = "w-full h-full flex justify-center items-center bg-gray-300 dark:bg-gray-900 transition-colors duration-300";
    }
    
}