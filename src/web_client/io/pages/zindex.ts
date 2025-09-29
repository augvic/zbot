class Index {
    
    element!: HTMLElement
    menu!: Menu
    titleBar!: TitleBar
    module!: Module
    
    constructor() {
        this.createSelf();
        this.createComponents();
        document.body.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-full w-full overflow-hidden flex flex-col bg-gray-300 dark:bg-gray-900 transition-colors duration-300 opacity-fade-in";
    }
    
    private createComponents() {
        this.module = new Module(this.element);
        this.menu = new Menu(this.element);
        this.titleBar = new TitleBar(this.element);
    }
    
}

class TitleBar {
    
    element!: HTMLElement
    menuButton!: MenuButton
    themeButton!: DarkLightButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "title_bar";
        this.element.className = "w-full bg-white dark:bg-gray-700 fixed z-50 h-[50px] flex items-center pl-3 transition-colors duration-300";
    }
    
    private createComponents() {
        this.menuButton = new MenuButton(this.element);
        this.themeButton = new DarkLightButton(this.element);
    }
    
}

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
            this.icon = new Icon(this.element, "menu-icon", "/storage/images/menu_light.png");
        } else {
            this.icon = new Icon(this.element, "menu-icon", "/storage/images/menu_dark.png");
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

class Icon {
    
    element!: HTMLImageElement
    
    constructor(appendTo: HTMLElement, id: string, src: string) {
        this.createSelf(src, id);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(src: string, id: string) {
        this.element = document.createElement("img");
        this.element.src = src;
        this.element.id = id;
        this.element.className = "size-7 opacity-fade-in";
    }
    
}

class Menu {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
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
    
    private async createComponents() {
        const modulesAllowed: [{[key: string]: string}] = await ZindexTasks.getAllowedModules();
        if (modulesAllowed == null) {
            return
        }
        modulesAllowed.forEach((module) => {
            new ModuleButton(this.element, module);
        });   
    }
    
}

class ModuleButton {
    
    element!: HTMLElement
    button!: HTMLElement
    hoverSpan!: HoverSpan
    
    constructor(appendTo: HTMLElement, module: {[key: string]: string}) {
        this.createSelf(module.module);
        this.startListeners(module.module, module.description);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(moduleName: string) {
        this.element = document.createElement("div");
        this.element.className = "flex w-auto h-auto items-center justify-center";
        this.button = document.createElement("button");
        this.button.className = "w-full h-auto p-2 bg-blue-700 hover:bg-blue-900 cursor-pointer rounded-md text-white transition-colors duration-300";
        this.button.innerText = moduleName;
        this.element.appendChild(this.button);
    }
    
    private startListeners(moduleName:string, moduleDescription: string) {
        this.button.addEventListener("click", () => {
            const moduleContainer = document.getElementById("module")!;
            const menu = document.getElementById("menu")!;
            this.button.dispatchEvent(new Event("mouseleave"));
            moduleContainer.classList.add("opacity-fade-out");
            moduleContainer.addEventListener("animationend", async () => {
                moduleContainer.classList.remove("opacity-fade-out");
                moduleContainer.innerHTML = "";
                const bundle = await import(`${window.location.origin}/module-bundle/${moduleName.toLowerCase()}`);
                const bundleClass = bundle.default;
                new bundleClass(moduleContainer);
                menu.classList.add("fade-out-left");
                menu.addEventListener("animationend", () => {
                    menu.classList.remove("fade-out-left");
                    menu.style.display = "none";
                }, { once: true });
            }, { once: true });
        });
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
        this.pushUpExistingNotifications();
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
        this.element.className = "notification fixed z-50 bottom-4 right-5 py-3 px-6 text-white rounded-md cursor-default fade-in-right transition-[bottom] duration-300 ease";
        if (color == "green") {
            this.element.classList.add("bg-green-400");
        } else if (color == "orange") {
            this.element.classList.add("bg-amber-400");
        } else if (color == "red") {
            this.element.classList.add("bg-red-400");
        }
        this.element.innerText = message;
    }
    
    private pushUpExistingNotifications() {
        const notifications = document.querySelectorAll<HTMLElement>(".notification");
        notifications.forEach(notification => {
            if (notification != this.element) {
                const currentBottom = parseInt(
                    getComputedStyle(notification).bottom.replace("px", "")
                );
                notification.style.bottom = (currentBottom + 60) + "px";
            }
        });
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
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "cursor-pointer w-auto h-auto rounded-md transition-colors duration-300 hover:bg-gray-300 dark:hover:bg-gray-900 absolute right-3";
    }
    
    private createComponents() {
        let iconSrc = "";
        if (window.localStorage.getItem("theme") == "light") {
            iconSrc = "/storage/images/moon.png";
        } else {
            iconSrc = "/storage/images/sun.png";
        }
        this.icon = new Icon(this.element, "theme-button", iconSrc);
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            const menuIcon = document.getElementById("menu-icon")! as HTMLImageElement;
            if (document.documentElement.classList.contains("light")) {
                document.documentElement.classList.remove("light");
                document.documentElement.classList.add("dark");
                window.localStorage.setItem("theme", "dark");
                this.icon.element.src = "/storage/images/sun.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
                menuIcon.src = "/storage/images/menu_dark.png";
                menuIcon.classList.remove("opacity-fade-in");
                void menuIcon.offsetWidth;
                menuIcon.classList.add("opacity-fade-in");
            } else {
                document.documentElement.classList.remove("dark");
                document.documentElement.classList.add("light");
                window.localStorage.setItem("theme", "light");
                this.icon.element.src = "/storage/images/moon.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
                menuIcon.src = "/storage/images/menu_light.png";
                menuIcon.classList.remove("opacity-fade-in");
                void menuIcon.offsetWidth;
                menuIcon.classList.add("opacity-fade-in");
            }
        });
    }
    
}

class ZindexTasks {
    
    static setTheme() {
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
    }
    
    static async getAllowedModules() {
        const response = await fetch(`${window.location.origin}/session-modules`);
        const modulesAllowed = await response.json();
        return modulesAllowed;
    }
    
    static loadIndex() {
        new Index();
    }
    
}

ZindexTasks.setTheme();
ZindexTasks.loadIndex();
