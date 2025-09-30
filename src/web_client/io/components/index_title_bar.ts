import { Bar } from "/component-bundle/bar.js";

class IndexTitleBar extends Bar {
    
    element!: HTMLElement
    menuButton!: MenuButton
    themeButton!: DarkLightButton
    
    constructor(appendTo: HTMLElement) {
        super(appendTo, "100%", "50px", "");
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createComponents() {
        this.menuButton = new MenuButton(this.element);
        this.themeButton = new DarkLightButton(this.element);
    }
    
}
