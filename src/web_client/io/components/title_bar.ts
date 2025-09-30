import { Bar } from "/component-bundle/bar.js";
import { Label } from "/component-bundle/label.js";
import { ThemeButton } from "/component-bundle/theme_button.js";

export class TitleBar extends Bar {
    
    element!: HTMLElement
    label!: Label
    themeButton!: ThemeButton
    
    constructor(appendTo: HTMLElement) {
        super(appendTo, "70%", "", "center");
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createComponents() {
        this.label = new Label(this.element);
        this.themeButton = new ThemeButton(this.element)
    }
    
}
