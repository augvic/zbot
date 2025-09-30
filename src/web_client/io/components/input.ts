export class Input {
    
    element!: HTMLInputElement
    
    constructor(appendTo: HTMLElement, id: string, placeholder: string, type: string, width: string, height: string) {
        this.createSelf(placeholder, type, id, width, height);
        appendTo.appendChild(this.element); 
    }
    
    private createSelf(placeholder: string, type: string, id: string, width: string, height: string) {
        this.element = document.createElement("input");
        this.element.className = "h-[30px] w-[70%] bg-white rounded-md border border-gray-300 outline-none p-3";
        this.element.type = type;
        this.element.id = id;
        this.element.placeholder = placeholder;
    }    
    
}
