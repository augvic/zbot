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
        this.io = new IO(this.tasks)
        document.body.appendChild(this.io.global.app.element);
        this.events();
    }
    
    private globalEvents() {
        this.io.global.themeButton.element.addEventListener("click", () => {
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
        });
    }
    
    private zLoginEvents() {
        document.addEventListener("load:zLogin", () => {
            this.io.zLogin.page.element.classList.add("opacity-fade-in");
            setTimeout(() => {
                this.io.zLogin.page.element.classList.remove("opacity-fade-in");
            }, 300);
            this.io.global.app.element.appendChild(this.io.zLogin.page.element);
            this.io.zLogin.page.element.appendChild(this.io.zLogin.container.element);
            this.io.zLogin.container.element.appendChild(this.io.zLogin.bar.element);
            this.io.zLogin.container.element.appendChild(this.io.zLogin.userInput.element);
            this.io.zLogin.container.element.appendChild(this.io.zLogin.passwordInput.element);
            this.io.zLogin.container.element.appendChild(this.io.zLogin.button.element);
            this.io.zLogin.bar.element.appendChild(this.io.zLogin.label.element);
            this.io.zLogin.bar.element.appendChild(this.io.global.themeButton.element);
        });
        this.io.zLogin.button.element.addEventListener("click", async () => {
            const user = this.io.zLogin.userInput.element.value;                
            const password = this.io.zLogin.passwordInput.element.value;
            const response = await this.tasks.makeRequestTask.post("/login", "application/json", { user, password });
            if (!response.success) {
                this.io.global.notification.pop(response.message, "red");
            } else {
                this.io.zLogin.page.element.classList.add("opacity-fade-out");
                setTimeout(() => {
                    this.io.zLogin.page.element.classList.remove("opacity-fade-out");
                    this.io.zLogin.page.element.remove();
                    document.dispatchEvent(new Event("load:zIndex"));
                    this.io.global.notification.pop(response.message, "green");                
                }, 300);
            }
        });
    }
    
    private zIndexEvents() {
        document.addEventListener("load:zIndex", () => {
            if (!this.components.webSocketComponent.connected) {
                this.components.webSocketComponent.init();
            }
            this.io.zIndex.page.element.classList.add("opacity-fade-in");
            setTimeout(() => {
                this.io.zIndex.page.element.classList.remove("opacity-fade-in");
            }, 300);
            this.io.global.app.element.appendChild(this.io.zIndex.page.element);
            this.io.zIndex.page.element.appendChild(this.io.zIndex.titleBar.element);
            this.io.zIndex.page.element.appendChild(this.io.zIndex.module.element);
            this.io.zIndex.page.element.appendChild(this.io.zIndex.menu.element);
            this.io.zIndex.menu.element.appendChild(this.io.zIndex.menuWrapper.element);
            this.io.zIndex.titleBar.element.appendChild(this.io.zIndex.menuButton.element);
            this.io.zIndex.titleBar.element.appendChild(this.io.zIndex.userName.element);
            this.io.zIndex.titleBar.element.appendChild(this.io.zIndex.logoutButton.element);
            this.io.zIndex.themeButtonContainer.element.appendChild(this.io.global.themeButton.element);
            this.io.zIndex.titleBar.element.appendChild(this.io.zIndex.themeButtonContainer.element);
            this.io.zIndex.menuWrapper.element.innerHTML = "";
            this.io.zIndex.modulesButtons.forEach(button => {
                this.io.zIndex.menuWrapper.element.appendChild(button.button.element);
                button.button.element.addEventListener("click", () => {
                    button.button.element.dispatchEvent(new Event("mouseleave"));
                    this.io.zIndex.module.element.classList.add("opacity-fade-out");
                    setTimeout(() => {
                        this.io.zIndex.module.element.classList.remove("opacity-fade-out");
                        this.io.zIndex.module.element.innerHTML = "";
                        this.io.zIndex.menu.element.classList.add("fade-out-left");
                        setTimeout(() => {
                            this.io.zIndex.menu.element.classList.remove("fade-out-left");
                            this.io.zIndex.menu.element.style.display = "none";                
                            document.dispatchEvent(new Event(`load:${button.moduleName}`));
                        }, 400);
                    }, 300);
                });
                button.button.element.addEventListener("mouseenter", () => {
                    button.hoverSpan.element.classList.add("opacity-fade-in");
                    button.button.element.appendChild(button.hoverSpan.element);
                    button.button.element.addEventListener("mouseleave", () => {
                        button.hoverSpan.element.classList.remove("opacity-fade-in");
                        button.hoverSpan.element.classList.add("opacity-fade-out");
                        setTimeout(() => {
                            button.hoverSpan.element.remove();
                        }, 300);
                    }, { once: true });
                });
            });
        });
        this.io.zIndex.logoutButton.element.addEventListener("click", async () => {
            const response = await this.tasks.makeRequestTask.delete("/login");
            if (!response.success) {
                this.io.global.notification.pop(response.message, "red");
                return;
            } else {
                this.io.global.notification.pop(response.message, "green");
            }
            this.io.zIndex.page.element.classList.add("opacity-fade-out");
            setTimeout(() => {
                this.io.zIndex.page.element.classList.remove("opacity-fade-out");
                this.io.zIndex.page.element.remove();
                document.dispatchEvent(new Event("load:zLogin"));
            }, 300);
        });
        this.io.zIndex.menuButton.element.addEventListener("click", () => {
            if (this.io.zIndex.menu.element.style.display == "none") {
                this.io.zIndex.menu.element.classList.add("fade-in-left");
                this.io.zIndex.menu.element.style.display = "flex";
                setTimeout(() => {
                    this.io.zIndex.menu.element.classList.remove("fade-in-left");
                }, 500);
            } else {
                this.io.zIndex.menu.element.classList.add("fade-out-left");
                setTimeout(() => {
                    this.io.zIndex.menu.element.style.display = "none";
                    this.io.zIndex.menu.element.classList.remove("fade-out-left");
                }, 400);
            }
        });
    }
    
    private zAdminEvents() {
        document.addEventListener("load:zAdmin", () => {
            this.io.zAdmin.moduleWrapper.element.classList.add("opacity-fade-in");
            setTimeout(() => {
                this.io.zAdmin.moduleWrapper.element.classList.remove("opacity-fade-in");
            }, 300);
            this.io.zIndex.module.element.appendChild(this.io.zAdmin.moduleWrapper.element);
            this.io.zAdmin.moduleWrapper.element.appendChild(this.io.zAdmin.optionsContainer.element);
            this.io.zAdmin.moduleWrapper.element.appendChild(this.io.zAdmin.viewContainer.element);
            this.io.zAdmin.optionsContainer.element.appendChild(this.io.zAdmin.optionsContainerWrapper.element);
            this.io.zAdmin.optionsContainerWrapper.element.appendChild(this.io.zAdmin.selectUsersSectionButton.element);
            this.io.zAdmin.selectUsersSectionButton.element.addEventListener("click", () => {
                this.io.zAdmin.usersSection.element.classList.add("opacity-fade-in");
                setTimeout(() => {
                    this.io.zAdmin.usersSection.element.classList.remove("opacity-fade-in");
                }, 300);
                this.io.zAdmin.viewContainer.element.appendChild(this.io.zAdmin.usersSection.element);
                this.io.zAdmin.usersSection.element.appendChild(this.io.zAdmin.usersSectionTopBar.element);
                this.io.zAdmin.usersSectionTopBar.element.appendChild(this.io.zAdmin.searchUserInput.element);
                this.io.zAdmin.usersSectionTopBar.element.appendChild(this.io.zAdmin.searchUserButton.element);
                this.io.zAdmin.usersSection.element.appendChild(this.io.zAdmin.usersSectionTable.wrapper);
                this.io.zAdmin.usersSectionTable.adjustColumns();
            });
        });
    }
    
    private events() {
        this.globalEvents();
        this.zLoginEvents();
        this.zIndexEvents();
        this.zAdminEvents();
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
        setTimeout(async () => {
            const response = await this.tasks.makeRequestTask.get("/login");
            if (response.success) {
                document.dispatchEvent(new Event("load:zIndex"));
            } else {
                document.dispatchEvent(new Event("load:zLogin"));
            }
        }, 500);
    }
    
}
