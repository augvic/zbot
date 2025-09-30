export class Bar {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, width: string, height: string, align: string) {
        this.element = document.createElement("div");
        this.element.className = "flex gap-2 items-center";
        this.element.style.width = width;
        this.element.style.height = height;
        if (align == "left") {
            this.element.classList.add("justify-start");
        }
        if (align = "center") {
            this.element.classList.add("justify-center");
        } 
        if (align = "right") {
            this.element.classList.add("justify-end");
        }
        appendTo.appendChild(this.element);
    }
    
}