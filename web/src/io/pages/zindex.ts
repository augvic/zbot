import { HoverSpan } from "../global/hover_span";
import { Icon } from "../global/icon";
import { ThemeButton } from "../global/theme_button";
import { Notification } from "../global/notification";

export class zIndex {
    
    element!: HTMLElement
    menu!: Menu
    titleBar!: TitleBar
    module!: Module
    
    public init(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zIndex";
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
    user!: UserName
    logoutButton!: LogoutButton
    themeButton!: ThemeButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "title_bar";
        this.element.className = "w-full bg-white dark:bg-gray-700 fixed z-50 h-[50px] flex items-center pl-3 transition-colors duration-300 gap-2";
    }
    
    private createComponents() {
        this.menuButton = new MenuButton(this.element);
        this.user = new UserName(this.element);
        this.logoutButton = new LogoutButton(this.element);
        this.themeButton = new ThemeButton(this.element, true);
    }
    
}

class UserName {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private async createSelf() {
        this.element = document.createElement("p");
        this.element.id = "user";
        this.element.className = "text-black dark:text-white transition-colors duration-300 cursor-default";
        const response = await fetch(`${window.location.origin}/session-user`);
        const user = await response.json();
        this.element.innerText = `Usuário: ${user}`;
    }
    
}

class LogoutButton {
    
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
        this.element.id = "logout_button";
        this.element.className = "cursor-pointer w-auto h-auto rounded-md transition-colors duration-300 bg-red-700 hover:bg-red-900 p-1";
    }
    
    private createComponents() {
        this.icon = new Icon(this.element, "logout-icon", "/storage/images/logout.png", "5");
    }
    
    private startListeners() {
        this.element.addEventListener("click", async () => {
            const response = await fetch(`${window.location.origin}/login`, {
                method: "DELETE"
            });
            const data = await response.json();
            if (!data.success) {
                new Notification("Erro ao deslogar.", "red");
                return;
            }
            const page = document.getElementById("zIndex")!;
            page.classList.remove("opacity-fade-in");
            page.classList.add("opacity-fade-out");
            page.addEventListener("animationend", async () => {
                page.remove();
                document.dispatchEvent(new Event("load:login"));
                new Notification("Logout realizado.", "green");
            });
        });
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
            this.icon = new Icon(this.element, "menu-icon", "/storage/images/menu_light.png", "7");
        } else {
            this.icon = new Icon(this.element, "menu-icon", "/storage/images/menu_dark.png", "7");
        }
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            const menu = document.getElementById("menu")!;
            if (menu.style.display == "none") {
                menu.classList.add("fade-in-left");
                menu.style.display = "flex";
                setTimeout(() => {
                    menu.classList.remove("fade-in-left");
                }, 500);
            } else {
                menu.classList.add("fade-out-left");
                setTimeout(() => {
                    menu.classList.remove("fade-out-left");
                    menu.style.display = "none";                    
                }, 400);
            }
        });
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
        const response = await fetch(`${window.location.origin}/session-modules`);
        const modulesAllowed = await response.json();
        if (modulesAllowed == null) {
            return
        }
        modulesAllowed.forEach((module: {[key: string]: string}) => {
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
                menu.classList.add("fade-out-left");
                menu.addEventListener("animationend", () => {
                    menu.classList.remove("fade-out-left");
                    menu.style.display = "none";
                }, { once: true });
                document.dispatchEvent(new Event(`load:${moduleName}`));
            }, { once: true });
        });
        this.button.addEventListener("mouseenter", () => {
            let hoverSpan = new HoverSpan(this.element, moduleDescription);
            this.button.addEventListener("mouseleave", () => {
                hoverSpan.element.classList.remove("opacity-fade-in");
                hoverSpan.element.classList.add("opacity-fade-out");
                setTimeout(() => {
                    hoverSpan.element.remove();
                }, 300);
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
