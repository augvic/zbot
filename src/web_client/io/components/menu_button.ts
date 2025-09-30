class MenuButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.id = "menu_button";
        this.element.className = "cursor-pointer w-auto h-auto rounded-md transition-colors duration-300 hover:bg-gray-300 dark:hover:bg-gray-900";
    }
    
    private createComponents() {
        if (document.documentElement.classList.contains("light")) {
            this.icon = new Icon(this.element, "menu-icon", "/static/images/menu_light.png");
        } else {
            this.icon = new Icon(this.element, "menu-icon", "/static/images/menu_dark.png");
        }
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            const menu = document.getElementById("menu")!;
            if (menu.style.display == "none") {
                menu.classList.add("fade-in-left");
                menu.style.display = "flex";
                menu.addEventListener("animationend", () => {
                    menu.classList.remove("fade-in-left");
                }, { once: true });
            } else {
                menu.classList.add("fade-out-left");
                menu.addEventListener("animationend", () => {
                    menu.classList.remove("fade-out-left");
                    menu.style.display = "none";
                }, { once: true });
            }
        });
    }
    
}