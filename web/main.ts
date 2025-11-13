import { zLogin } from "./src/io/pages/zlogin";
import { zIndex } from "./src/io/pages/zindex";
import { zAdmin } from "./src/io/modules/zadmin";
import { zRegRpa } from "./src/io/modules/zregrpa";
import { Notification } from "./src/io/global/notification";
import { MakeRequestTask } from "./src/tasks/make_request";
import { AdjustTableTask } from "./src/tasks/adjust_table";
import { TableControllerComponent } from "./src/components/table_controller";
import { RequestHandlerComponent } from "./src/components/request_handler";
import { WebSocketComponent } from "./src/components/web_socket";

class CompositionRoot {
    
    app!: HTMLElement
    module!: HTMLElement
    zIndex!: zIndex
    zLogin!: zLogin
    zRegRpa!: zRegRpa
    zAdmin!: zAdmin
    makeRequestTask!: MakeRequestTask
    adjustRegistrationsTableTask!: AdjustTableTask
    registrationsTableController!: TableControllerComponent
    requestHandlerComponent!: RequestHandlerComponent
    webSocketComponent!: WebSocketComponent
    
    
    constructor() {
        this.app = document.getElementById("application-content")!;
        this.initComponents();
        this.initTasks();
        this.initIo();
    }
    
    private initComponents() {
        this.requestHandlerComponent = new RequestHandlerComponent();
        this.webSocketComponent = new WebSocketComponent();
        this.registrationsTableController = new TableControllerComponent({
            status: [] as HTMLElement[],
            cnpj: [] as HTMLElement[],
            opening: [] as HTMLElement[],
            registration_status: [] as HTMLElement[],
            company_name: [] as HTMLElement[],
            trade_name: [] as HTMLElement[],
            legal_nature: [] as HTMLElement[],
            legal_nature_id: [] as HTMLElement[],
            street: [] as HTMLElement[],
            number: [] as HTMLElement[],
            complement: [] as HTMLElement[],
            neighborhood: [] as HTMLElement[],
            pac: [] as HTMLElement[],
            city: [] as HTMLElement[],
            state: [] as HTMLElement[],
            fone: [] as HTMLElement[],
            email: [] as HTMLElement[],
            tax_regime: [] as HTMLElement[],
            comission_receipt: [] as HTMLElement[],
            client_type: [] as HTMLElement[],
            suggested_limit: [] as HTMLElement[],
            seller: [] as HTMLElement[],
            cpf: [] as HTMLElement[],
            cpf_person: [] as HTMLElement[],
            buttons: [] as HTMLElement[]
        });
    }
    
    private initTasks() {
        this.makeRequestTask = new MakeRequestTask(
            this.requestHandlerComponent
        );
        this.adjustRegistrationsTableTask = new AdjustTableTask(
            this.registrationsTableController
        );
    }
    
    private initIo() {
        this.zLogin = new zLogin();
        this.zIndex = new zIndex();
        this.zAdmin = new zAdmin();
        this.zRegRpa = new zRegRpa();
        document.addEventListener("load:index", () => {
            this.webSocketComponent.init();
            this.zIndex.init(this.app, this.makeRequestTask);
            this.module = document.getElementById("module")!;
        });
        document.addEventListener("load:login", () => {
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
    
    public async run() {
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

new CompositionRoot().run();
