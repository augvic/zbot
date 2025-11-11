export class HoverSpan {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("span");
        this.element.className = "text-nowrap opacity-fade-in z-50 bg-blue-900 text-white py-1 px-4 rounded-lg absolute left-80 w-auto h-auto cursor-default";
        this.element.style.fontSize = "small";
        this.element.innerText = text;
    }
    
}
