import { Components } from "./components";
import { Tasks } from "./tasks";
import { IO } from "./io";

export class Controller {
    
    components: Components
    tasks: Tasks
    io: IO
    
    constructor() {
        this.components = new Components();
        this.tasks = new Tasks(this.components);
        this.io = new IO()
        document.body.appendChild(this.io.global.app.element);
        this.events();
    }
    
    private async login() {
        const user = this.io.zLogin.userInput.element.value;                
        const password = this.io.zLogin.passwordInput.element.value;
        const response = await this.tasks.makeRequestTask.post("/login", "application/json", { user, password });
        if (!response.success) {
            this.io.createNotification(response.message, "red");
        } else {
            this.io.zLogin.page.element.classList.add("opacity-fade-out");
            setTimeout(() => {
                this.io.zLogin.page.element.remove();
                document.dispatchEvent(new Event("load:zIndex"));
                this.io.createNotification(response.message, "green");                
            }, 500);
        }
    }
    
    private async logout() {
        const response = await this.tasks.makeRequestTask.delete("/login");
        if (!response.success) {
            this.io.createNotification(response.message, "red");
            return;
        } else {
            this.io.createNotification(response.message, "green");
        }
        this.io.zIndex.page.element.classList.remove("opacity-fade-in");
        this.io.zIndex.page.element.classList.add("opacity-fade-out");
        setTimeout(() => {
            this.io.zIndex.page.element.remove();
            document.dispatchEvent(new Event("load:zLogin"));
        }, 500);
    }
    
    private changeTheme() {
        if (document.documentElement.classList.contains("light")) {
            document.documentElement.classList.remove("light");
            document.documentElement.classList.add("dark");
            window.localStorage.setItem("theme", "dark");
            this.io.global.themeButton.icon.src = "/storage/images/sun.png";
            this.io.global.themeButton.icon.classList.remove("opacity-fade-in");
            void this.io.global.themeButton.icon.offsetWidth;
            this.io.global.themeButton.icon.classList.add("opacity-fade-in");
            this.io.zIndex.menuButton.icon.src = "/storage/images/menu_dark.png";
            this.io.zIndex.menuButton.icon.classList.remove("opacity-fade-in");
            void this.io.zIndex.menuButton.icon.offsetWidth;
            this.io.zIndex.menuButton.icon.classList.add("opacity-fade-in");
        } else {
            document.documentElement.classList.remove("dark");
            document.documentElement.classList.add("light");
            window.localStorage.setItem("theme", "light");
            this.io.global.themeButton.icon.src = "/storage/images/moon.png";
            this.io.global.themeButton.icon.classList.remove("opacity-fade-in");
            void this.io.global.themeButton.icon.offsetWidth;
            this.io.global.themeButton.icon.classList.add("opacity-fade-in");
            this.io.zIndex.menuButton.icon.src = "/storage/images/menu_light.png";
            this.io.zIndex.menuButton.icon.classList.remove("opacity-fade-in");
            void this.io.zIndex.menuButton.icon.offsetWidth;
            this.io.zIndex.menuButton.icon.classList.add("opacity-fade-in");
        }
    }
    
    private changeModule(button: HTMLButtonElement, moduleName: string) {
        button.dispatchEvent(new Event("mouseleave"));
        this.io.zIndex.module.element.classList.add("opacity-fade-out");
        setTimeout(() => {
            this.io.zIndex.module.element.classList.remove("opacity-fade-out");
            this.io.zIndex.module.element.innerHTML = "";
            this.io.zIndex.menu.element.classList.add("fade-out-left");
            setTimeout(() => {
                this.io.zIndex.menu.element.classList.remove("fade-out-left");
                this.io.zIndex.menu.element.style.display = "none";                
                document.dispatchEvent(new Event(`load:${moduleName}`));
            }, 500);
        }, 500);
    }
    
    private events() {
        this.io.global.themeButton.element.addEventListener("click", this.changeTheme);
        document.addEventListener("load:zIndex", async () => {
            this.components.webSocketComponent.init();
            const modules = ((await this.tasks.makeRequestTask.get("/session-modules")).data as [{[key: string]: string}]);
            this.io.global.app.element.appendChild(this.io.zLogin.page.element);
            this.io.zIndex.page.element.appendChild(this.io.zIndex.titleBar.element);
            this.io.zIndex.page.element.appendChild(this.io.zIndex.module.element);
            this.io.zIndex.page.element.appendChild(this.io.zIndex.menu.element);
            this.io.zIndex.titleBar.element.appendChild(this.io.zIndex.menuButton.element);
            this.io.zIndex.titleBar.element.appendChild(this.io.zIndex.userName.element);
            this.io.zIndex.titleBar.element.appendChild(this.io.zIndex.logoutButton.element);
            this.io.zIndex.themeButtonContainer.element.appendChild(this.io.globals.themeButton.element);
            this.io.zIndex.titleBar.element.appendChild(this.io.zIndex.themeButtonContainer.element);
            modules.forEach(module => {
                const button = this.io.createButton(module.module, "blue").element;
                this.io.zIndex.menu.element.appendChild(button);
                button.addEventListener("click", () => {
                    this.changeModule(button, module.module);
                });
                button.addEventListener("mouseenter", () => {
                    let hoverSpan = this.io.createHoverSpan(module.description);
                    button.addEventListener("mouseleave", () => {
                        hoverSpan.element.classList.remove("opacity-fade-in");
                        hoverSpan.element.classList.add("opacity-fade-out");
                        setTimeout(() => {
                            hoverSpan.element.remove();
                        }, 300);
                    }, { once: true });
                });
            });
            this.io.zIndex.logoutButton.element.addEventListener("click", this.logout);
        });
        document.addEventListener("load:zLogin", () => {
            this.io.global.app.element.appendChild(this.io.zLogin.page.element);
            this.io.zLogin.page.element.appendChild(this.io.zLogin.container.element);
            this.io.zLogin.container.element.appendChild(this.io.zLogin.bar.element);
            this.io.zLogin.container.element.appendChild(this.io.zLogin.userInput.element);
            this.io.zLogin.container.element.appendChild(this.io.zLogin.passwordInput.element);
            this.io.zLogin.container.element.appendChild(this.io.zLogin.button.element);
            this.io.zLogin.bar.element.appendChild(this.io.zLogin.label.element);
            this.io.zLogin.bar.element.appendChild(this.io.global.themeButton.element);
            this.io.zLogin.button.element.addEventListener("click", this.login);
        });
    }
    
    public async run_process() {
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
        const response = await this.tasks.makeRequestTask.get("/login");
        if (response.success) {
            document.dispatchEvent(new Event("load:zIndex"));
        } else {
            document.dispatchEvent(new Event("load:zLogin"));
        }
    }
    
}
