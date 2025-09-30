export class Button {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, width: string, height: string, color: string, text: string) {
        this.element = document.createElement("button");
        this.element.className = "rounded-md text-white cursor-pointer transition-colors duration-300";
        this.element.innerText = text;
        this.element.style.width = width;
        this.element.style.height = height;
        if (color == "green") {
            this.element.classList.add("bg-green-700");
            this.element.classList.add("hover:bg-green-900")
        } else if (color == "blue") {
            this.element.classList.add("bg-blue-700");
            this.element.classList.add("hover:bg-blue-900")
        } else if (color == "red") {
            this.element.classList.add("bg-red-700");
            this.element.classList.add("hover:bg-red-900")
        } else {
            this.element.classList.add("bg-green-700");
            this.element.classList.add("hover:bg-green-900")
        }
        appendTo.appendChild(this.element);
    }
    
}
