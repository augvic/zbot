export class Icon {
    
    element!: HTMLImageElement
    
    constructor(appendTo: HTMLElement, src: string, size: number) {
        this.createSelf(src, size);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(src: string, size: number) {
        this.element = document.createElement("img");
        this.element.src = src;
        this.element.className = "opacity-fade-in";
        if (size == 5) {
            this.element.classList.add("size-5");
        } else if (size == 6) {
            this.element.classList.add("size-6");
        } else if (size == 7) {
            this.element.classList.add("size-7");
        } else {
            this.element.classList.add("size-5");
        }
    }
    
}
