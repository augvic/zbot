export class Icon {
    
    element!: HTMLImageElement
    
    constructor(appendTo: HTMLElement, id: string, src: string, size: string) {
        this.createSelf(src, id, size);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(src: string, id: string, size: string) {
        this.element = document.createElement("img");
        this.element.src = src;
        this.element.id = id;
        this.element.className = "opacity-fade-in";
        if (size == "7") {
            this.element.classList.add("size-7");
        } else {
            this.element.classList.add("size-5");
        }
    }
    
}