export class Icon {
    
    element!: HTMLImageElement
    
    constructor(appendTo: HTMLElement, src: string) {
        this.createSelf(src);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(src: string) {
        this.element = document.createElement("img");
        this.element.src = src;
        this.element.className = "size-7 opacity-fade-in";
    }
}
