class Index {

    element!: HTMLElement
    menu!: Menu
    titleBar!: TitleBar
    module!: Module
    
    constructor(modulesAllowed: Array<{[key: string]: string}>) {
        if (window.localStorage.getItem("theme") == null) {
            window.localStorage.setItem("theme", "light");
        }
        if (window.localStorage.getItem("theme") == "light") {
            document.documentElement.classList.remove("dark");
            document.documentElement.classList.add("light");
        } else {
            document.documentElement.classList.remove("light");
            document.documentElement.classList.add("dark");
        }
        this.createSelf();
        this.createComponents(modulesAllowed);
        document.body.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-full w-full overflow-hidden flex flex-col bg-gray-300 dark:bg-gray-900 transition-colors duration-300 opacity-fade-in";
    }
    
    private createComponents(modulesAllowed: Array<{[key: string]: string}>) {
        this.module = new Module(this.element);
        this.menu = new Menu(this.element, modulesAllowed, this.module.element);
        this.titleBar = new TitleBar(this.element, this.menu.element);
    }
    
}

class TitleBar {
    
    element!: HTMLElement
    menuButton!: MenuButton
    themeButton!: DarkLightButton
    
    constructor(appendTo: HTMLElement, menu: HTMLElement) {
        this.createSelf();
        this.createComponents(menu);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "title_bar";
        this.element.className = "w-full bg-white dark:bg-gray-700 fixed z-50 h-[50px] flex items-center pl-3 transition-colors duration-300";
    }
    
    private createComponents(menu: HTMLElement) {
        this.menuButton = new MenuButton(this.element, menu);
        this.themeButton = new DarkLightButton(this.element, this.menuButton.icon.element);
    }
    
}

class MenuButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, menu: HTMLElement) {
        this.createSelf(menu);
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf(menu: HTMLElement) {
        this.element = document.createElement("button");
        this.element.id = "menu_button";
        this.element.className = "cursor-pointer w-auto h-auto rounded-md transition-colors duration-300 hover:bg-gray-300 dark:hover:bg-gray-900";
        this.element.addEventListener("click", () => {
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
    
    private createComponents() {
        if (document.documentElement.classList.contains("light")) {
            this.icon = new Icon("static/images/menu_light.png", this.element);
        } else {
            this.icon = new Icon("static/images/menu_dark.png", this.element);
        }
    }
    
}

class Icon {
    
    element!: HTMLImageElement
    
    constructor(src: string, appendTo: HTMLElement) {
        this.createSelf(src);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(src: string) {
        this.element = document.createElement("img");
        this.element.src = src;
        this.element.className = "size-7 opacity-fade-in";
    }
    
}

class Menu {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, modulesAllowed: Array<{[key: string]: string}>, modulesContainer: HTMLElement) {
        this.createSelf();
        this.createComponents(modulesAllowed, modulesContainer);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "menu";
        this.element.className = "w-[300px] flex-col fixed bg-white/30 dark:bg-gray-700/30 z-40 p-3 gap-y-3 bottom-0 rounded-br-lg rounded-tr-lg";
        this.element.style.height = "calc(100vh - 50px)";
        this.element.style.backdropFilter = "blur(6px)";
        this.element.style.display = "none";
    }
    
    private createComponents(modulesAllowed: Array<{[key: string]: string}>, moduleContainer: HTMLElement) {
        if (modulesAllowed == null) {
            return
        }
        modulesAllowed.forEach((element) => {
            new ModuleButton(this.element, element, moduleContainer, this.element);
        });   
    }
    
}

class ModulesAllowedGetter {
    
    async get() {
        const response = await fetch(`${window.location.origin}/modules-allowed`);
        const modulesAllowed = await response.json();
        return modulesAllowed;
    }
    
}

class ModuleButton {
    
    element!: HTMLElement
    button!: HTMLElement
    hoverSpan!: HoverSpan
    
    constructor(appendTo: HTMLElement, module: {[key: string]: string}, moduleContainer: HTMLElement, menu: HTMLElement) {
        this.createSelf(module.module, moduleContainer, menu);
        this.createComponents(module.description);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(moduleName: string, moduleContainer: HTMLElement, menu: HTMLElement) {
        this.element = document.createElement("div");
        this.element.className = "flex w-auto h-auto items-center justify-center";
        this.button = document.createElement("button");
        this.button.className = "w-full h-auto p-2 bg-blue-700 hover:bg-blue-900 cursor-pointer rounded-md text-white transition-colors duration-300";
        this.button.innerText = moduleName;
        this.element.appendChild(this.button);
        this.button.addEventListener("click", () => {
            this.button.dispatchEvent(new Event("mouseleave"));
            moduleContainer.classList.add("opacity-fade-out");
            moduleContainer.addEventListener("animationend", async () => {
                moduleContainer.classList.remove("opacity-fade-out");
                moduleContainer.innerHTML = "";
                let bundle = await import(`${window.location.origin}/modules/${moduleName}`);
                let bundleClass = bundle.default;
                new bundleClass(moduleContainer);
                menu.classList.add("fade-out-left");
                menu.addEventListener("animationend", () => {
                    menu.classList.remove("fade-out-left");
                    menu.style.display = "none";
                }, { once: true });
            }, { once: true });
        });
    }
    
    private createComponents(moduleDescription: string) {
        this.button.addEventListener("mouseenter", () => {
            let hoverSpan = new HoverSpan(this.element, moduleDescription);
            this.button.addEventListener("mouseleave", () => {
                hoverSpan.element.classList.remove("opacity-fade-in");
                hoverSpan.element.classList.add("opacity-fade-out");
                hoverSpan.element.addEventListener("animationend", () => {
                    hoverSpan.element.remove();
                }, { once: true });
            }, { once: true });
        });
    }
    
}

class Module {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "module";
        this.element.className = "w-full bg-gray-300 dark:bg-gray-900 transition-colors duration-300 justify-center items-center bottom-0 flex fixed cursor-default";
        this.element.style.height = "calc(100vh - 50px)";
        this.element.innerHTML = "<p class='text-black dark:text-white transition-colors duration-300'>✨ Selecione um módulo para começar.</p>"
    }
    
}

class NotificationPopUp {
    
    element!: HTMLElement
    
    constructor(message: string, color: string) {
        this.createSelf(message, color);
        document.body.appendChild(this.element);
        setTimeout(() => {
            this.element.classList.remove("fade-in-right");
            this.element.classList.add("fade-out-right");
            this.element.addEventListener("animationend", () => {
                this.element.remove()
            }, { once: true });
        }, 3000);
    }
    
    private createSelf(message: string, color: string) {
        this.element = document.createElement("div");
        this.element.className = "fixed z-50 bottom-4 right-5 py-3 px-6 text-white rounded-md cursor-default fade-in-right";
        if (color == "green") {
            this.element.classList.add("bg-green-400");
        } else if (color == "orange") {
            this.element.classList.add("bg-amber-400");
        } else if (color == "red") {
            this.element.classList.add("bg-red-400");
        }
        this.element.innerText = message;
    }
    
}

class HoverSpan {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("span");
        this.element.className = "text-nowrap opacity-fade-in z-50 bg-blue-900 text-white py-1 px-4 rounded-lg absolute ml-130 w-auto h-auto cursor-default";
        this.element.style.fontSize = "small";
        this.element.innerText = text;
    }
    
}

class DarkLightButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, menuIcon: HTMLImageElement) {
        this.createSelf(menuIcon);
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf(menuIcon: HTMLImageElement) {
        this.element = document.createElement("button");
        this.element.className = "cursor-pointer w-auto h-auto rounded-md transition-colors duration-300 hover:bg-gray-300 dark:hover:bg-gray-900 absolute right-3";
        this.element.addEventListener("click", () => {
            if (document.documentElement.classList.contains("light")) {
                document.documentElement.classList.remove("light");
                document.documentElement.classList.add("dark");
                window.localStorage.setItem("theme", "dark");
                this.icon.element.src = "static/images/sun.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
                menuIcon.src = "static/images/menu_dark.png";
                menuIcon.classList.remove("opacity-fade-in");
                void menuIcon.offsetWidth;
                menuIcon.classList.add("opacity-fade-in");
            } else {
                document.documentElement.classList.remove("dark");
                document.documentElement.classList.add("light");
                window.localStorage.setItem("theme", "light");
                this.icon.element.src = "static/images/moon.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
                menuIcon.src = "static/images/menu_light.png";
                menuIcon.classList.remove("opacity-fade-in");
                void menuIcon.offsetWidth;
                menuIcon.classList.add("opacity-fade-in");
            }
        });
    }
    
    private createComponents() {
        let iconSrc = "";
        if (window.localStorage.getItem("theme") == "light") {
            iconSrc = "static/images/moon.png";
        } else {
            iconSrc = "static/images/sun.png";
        }
        this.icon = new Icon(iconSrc, this.element);
    }
    
}

(async () => {
    const modulesAllowedGetter = new ModulesAllowedGetter();
    const modulesAllowed = await modulesAllowedGetter.get();
    new Index(modulesAllowed);
})();
