import { io } from "socket.io-client";

const socket = io(`${window.location.origin}`);

export default class zIndex {
    
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
        this.themeButton = new ThemeButton(this.element);
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
        this.icon = new Icon(this.element, "logout-icon", "/static/images/logout.png", "5");
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
                document.body.innerHTML = "";
                let bundle = await import(`${window.location.origin}/page-bundle/zlogin.js`);
                let bundleClass = bundle.default;
                document.body.innerHTML = "";
                new bundleClass();
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
            this.icon = new Icon(this.element, "menu-icon", "/static/images/menu_light.png", "7");
        } else {
            this.icon = new Icon(this.element, "menu-icon", "/static/images/menu_dark.png", "7");
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

class Icon {
    
    element!: HTMLImageElement
    
    constructor(appendTo: HTMLElement, id: string, src: string, size: string) {
        this.createSelf(src, id, size);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(src: string, id: string, size: string) {
        this.element = document.createElement("img");
        this.element.src = src;
        this.element.id = id;
        this.element.className = "opacity-fade-in";
        if (size == "7") {
            this.element.classList.add("size-7");
        } else {
            this.element.classList.add("size-5");
        }
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
        modulesAllowed.forEach((module: { [key: string]: string; }) => {
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
                const bundle = await import(`${window.location.origin}/module-bundle/${moduleName.toLowerCase()}.js`);
                const bundleClass = bundle.default;
                new bundleClass(moduleContainer, socket);
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

class HoverSpan {
    
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

class ThemeButton {
    
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
            iconSrc = "/static/images/moon.png";
        } else {
            iconSrc = "/static/images/sun.png";
        }
        this.icon = new Icon(this.element, "theme-button", iconSrc, "7");
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            const menuIcon = document.getElementById("menu-icon")! as HTMLImageElement;
            if (document.documentElement.classList.contains("light")) {
                document.documentElement.classList.remove("light");
                document.documentElement.classList.add("dark");
                window.localStorage.setItem("theme", "dark");
                this.icon.element.src = "/static/images/sun.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
                menuIcon.src = "/static/images/menu_dark.png";
                menuIcon.classList.remove("opacity-fade-in");
                void menuIcon.offsetWidth;
                menuIcon.classList.add("opacity-fade-in");
            } else {
                document.documentElement.classList.remove("dark");
                document.documentElement.classList.add("light");
                window.localStorage.setItem("theme", "light");
                this.icon.element.src = "/static/images/moon.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
                menuIcon.src = "/static/images/menu_light.png";
                menuIcon.classList.remove("opacity-fade-in");
                void menuIcon.offsetWidth;
                menuIcon.classList.add("opacity-fade-in");
            }
        });
    }
    
}

class Notification {
    
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
