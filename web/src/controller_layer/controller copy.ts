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
    }
    
    private lifeCycle() {
        document.addEventListener("load:index", () => {
            this.webSocketComponent.init();
            this.zIndex.init(this.app, this.makeRequestTask);
            this.module = document.getElementById("module")!;
        });
        document.addEventListener("load:zlogin", () => {
            this.zLogin.init(this.app, this.makeRequestTask);
        });
        document.addEventListener("load:zAdmin", () => {
            this.webSocketComponent.webSocket.removeAllListeners();
            this.zAdmin.init(this.module, this.makeRequestTask);
        });
        document.addEventListener("load:zRegRpa", () => {
            this.webSocketComponent.webSocket.removeAllListeners();
            this.zRegRpa.init(this.module, this.makeRequestTask, this.adjustRegistrationsTableTask);
            const turnOffMouseLeave = () => {
                this.zRegRpa.container.terminalSection.topBar.turnOffButton.element.style.backgroundColor = "oklch(50.5% 0.213 27.518)";
            };
            const turnOffMouseEnter = () => {
                this.zRegRpa.container.terminalSection.topBar.turnOffButton.element.style.backgroundColor = "oklch(39.6% 0.141 25.723)";
            };
            const turnOnMouseLeave = () => {
                this.zRegRpa.container.terminalSection.topBar.turnOnButton.element.style.backgroundColor = "oklch(52.7% 0.154 150.069)";
            };
            const turnOnMouseEnter = () => {
                this.zRegRpa.container.terminalSection.topBar.turnOnButton.element.style.backgroundColor = "oklch(39.3% 0.095 152.535)";
            };
            this.webSocketComponent.webSocket.on("regrpa_terminal", (response: {[key: string]: string}) => {
                const terminal = this.zRegRpa.container.terminalSection.terminal.element;
                const distanceFromBottom = terminal.scrollHeight - (terminal.scrollTop + terminal.clientHeight);
                const text = document.createElement("p");
                text.className = "cursor-default text-white transition-opacity duration-300";
                text.style.opacity = "0";
                text.innerText = response.message;
                terminal.appendChild(text);
                text.style.opacity = "1";
                if (distanceFromBottom <= 50) {
                    terminal.scrollTop = terminal.scrollHeight;
                }
            });
            this.webSocketComponent.webSocket.on("regrpa_notification", (response: {[key: string]: string | boolean}) => {
                if (response.success) {
                    new Notification(response.message as string, "green");
                } else {
                    new Notification(response.message as string, "red");
                }
            });
            this.webSocketComponent.webSocket.on("regrpa_status", (response: {[key: string]: string}) => {
                const status = this.zRegRpa.container.terminalSection.topBar.status.element;
                const turnOffButton = this.zRegRpa.container.terminalSection.topBar.turnOffButton.element;
                const turnOnButton = this.zRegRpa.container.terminalSection.topBar.turnOnButton.element;
                status.style.opacity = "0";
                setTimeout(() => {
                    status.innerText = `Status: ${response.message}`;
                    status.style.opacity = "1";   
                }, 300);
                if (response.message == "Em processamento...") {
                    turnOffButton.disabled = false;
                    turnOffButton.style.backgroundColor = "oklch(50.5% 0.213 27.518)";
                    turnOffButton.addEventListener("mouseleave", turnOffMouseLeave);
                    turnOffButton.addEventListener("mouseenter", turnOffMouseEnter);
                    turnOffButton.style.cursor = "pointer";
                    turnOnButton.disabled = true;
                    turnOnButton.style.backgroundColor = "#919191";
                    turnOnButton.style.cursor = "not-allowed";
                    turnOnButton.removeEventListener("mouseenter", turnOnMouseEnter);
                    turnOnButton.removeEventListener("mouseleave", turnOnMouseLeave);
                }
                if (response.message == "Desligado.") {
                    turnOnButton.disabled = false;
                    turnOnButton.style.backgroundColor = "oklch(52.7% 0.154 150.069)";
                    turnOnButton.addEventListener("mouseleave", turnOnMouseLeave);
                    turnOnButton.addEventListener("mouseenter", turnOnMouseEnter);
                    turnOnButton.style.cursor = "pointer";
                    turnOffButton.disabled = true;
                    turnOffButton.style.backgroundColor = "#919191";
                    turnOffButton.style.cursor = "not-allowed";
                    turnOffButton.removeEventListener("mouseenter", turnOffMouseEnter);
                    turnOffButton.removeEventListener("mouseleave", turnOffMouseLeave);
                }
            });
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
        const response = await this.makeRequestTask.get("/login");
        if (response.success) {
            this.app.innerHTML = "";
            document.dispatchEvent(new Event("load:index"));
        } else {
            document.dispatchEvent(new Event("load:login"));
        }
    }
    
}
