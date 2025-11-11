import { Icon } from "../global/icon";
import { Notification } from "../global/notification";

export class zRegRpa {
    
    element!: HTMLElement
    container!: Container
    
    public init(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zRegRpa";
        this.element.className = "w-full h-full opacity-fade-in bg-gray-300 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center";
    }
    
    private async createComponents() {
        const response = await fetch(`${window.location.origin}/registrations-rpa`, {
            method: "GET"
        });
        const data = await response.json();
        this.container = new Container(this.element, data);
    }
    
}

class Container {
    
    element!: HTMLElement
    terminalSection!: TerminalSection
    registrationsSection!: RegistrationsSection
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(data);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "container";
        this.element.className = "w-[95%] h-[95%] p-3 bg-white dark:bg-gray-700 transition-colors duration-300 flex rounded-lg";
    }
    
    private createComponents(data: {[key: string]: string}) {
        this.terminalSection = new TerminalSection(this.element, data);
        this.registrationsSection = new RegistrationsSection(this.element);
    }
    
}

class TerminalSection {
    
    element!: HTMLElement
    topBar!: ContainerTopBar
    terminal!: Terminal
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(data);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "terminal-section";
        this.element.className = "w-full h-full gap-y-2 flex flex-col items-center justify-center transition-opacity duration-300";
    }
    
    private createComponents(data: {[key: string]: string}) {
        this.topBar = new ContainerTopBar(this.element, data)
        this.terminal = new Terminal(this.element, data);
    }
    
}

class ContainerTopBar {
    
    element!: HTMLElement
    turnOnButton!: TurnOnButton
    turnOffButton!: TurnOffButton
    status!: RpaStatus
    goToRegistrationsSection!: GoToRegistrationsSection
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf();
        this.createComponents(data);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[5%] flex items-center gap-x-2";
    }
    
    private createComponents(data: {[key: string]: string}) {
        this.turnOnButton = new TurnOnButton(this.element, data);
        this.turnOffButton = new TurnOffButton(this.element, data);
        this.status = new RpaStatus(this.element, data);
        this.goToRegistrationsSection = new GoToRegistrationsSection(this.element);
    }
    
}

class TurnOnButton {
    
    element!: HTMLButtonElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf(data);
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf(data: {[key: string]: string}) {
        this.element = document.createElement("button");
        this.element.id = "turn-on-button";
        this.element.className = "w-auto h-auto p-1 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer";
        if (data.status == "Em processamento.") {
            this.element.disabled = true;
            this.element.style.backgroundColor = "#919191";
            this.element.style.cursor = "not-allowed";
        }
        if (data.status == "Desligado.") {
            this.element.disabled = false;
            this.element.style.backgroundColor = "oklch(52.7% 0.154 150.069)";
            this.element.style.cursor = "pointer";
        }
    }
    
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/play.png", "7");
    }
    
    private startListeners() {
        this.element.addEventListener("click", async () => {
            const response = await fetch(`${window.location.origin}/registrations-rpa`, {
                method: "POST" 
            });
            const data = await response.json();
            if (!data.success) {
                new Notification(data.message, "red");
            }
        });
    }
    
}

class TurnOffButton {
    
    element!: HTMLButtonElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf(data);
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf(data: {[key: string]: string}) {
        this.element = document.createElement("button");
        this.element.id = "turn-off-button";
        this.element.className = "w-auto h-auto p-1 bg-red-700 hover:bg-red-900 transition-colors duration-300 rounded-md cursor-pointer";
        if (data.status == "Em processamento.") {
            this.element.disabled = false;
            this.element.style.backgroundColor = "oklch(50.5% 0.213 27.518)";
            this.element.style.cursor = "pointer";
        }
        if (data.status == "Desligado.") {
            this.element.disabled = true;
            this.element.style.backgroundColor = "#919191";
            this.element.style.cursor = "not-allowed";
        }
    }
    
    private createComponents() {
        this.icon = new Icon(this.element, "", "/storage/images/stop.png", "7");
    }
    
    private startListeners() {
        this.element.addEventListener("click", async () => {
            const response = await fetch(`${window.location.origin}/registrations-rpa`, {
                method: "DELETE" 
            });
            const data = await response.json();
            if (!data.success) {
                new Notification(data.message, "red");
            }
        });
    }
    
}

class RpaStatus {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf(data);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(data: {[key: string]: string}) {
        this.element = document.createElement("p");
        this.element.className = "cursor-default text-black dark:text-white transition-colors transition-opacity duration-300";
        this.element.innerText = `Status: ${data.status}`;
    }
    
}

class GoToRegistrationsSection {
    
    wrapper!: HTMLElement
    button!: HTMLButtonElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.startListeners();
        appendTo.appendChild(this.wrapper);
    }
    
    private createSelf() {
        this.wrapper = document.createElement("div");
        this.wrapper.className = "w-auto h-auto flex flex-1 justify-end items-center";
        this.button = document.createElement("button");
        this.button.className = "w-auto h-auto py-1 px-2 bg-amber-700 hover:bg-amber-900 transition-colors duration-300 rounded-md cursor-pointer text-white";
        this.button.innerText = "Ir para cadastros.";
        this.wrapper.appendChild(this.button);
    }
    
    private startListeners() {
        this.button.addEventListener("click", () => {
            let terminalSection = document.getElementById("terminal-section")!;
            let registrationsSection = document.getElementById("registrations-section")!
            terminalSection.style.opacity = "0";
            setTimeout(() => {
                terminalSection.style.display = "none";
                registrationsSection.style.opacity = "0";
                registrationsSection.style.display = "flex";
                registrationsSection.offsetHeight;
                registrationsSection.style.opacity = "1";
            }, 300);
        });
    }
    
}

class Terminal {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, data: {[key: string]: string}) {
        this.createSelf(data);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(data: {[key: string]: string}) {
        this.element = document.createElement("div");
        this.element.id = "terminal";
        this.element.className = "w-full h-[95%] flex flex-col gap-y-1 p-3 bg-black text-white rounded-md overflow-y-auto custom-scroll scroll-smooth";
        this.element.innerText = data.memory;
        setTimeout(() => {
            this.element.scrollTop = this.element.scrollHeight;
        }, 500);
    }
    
}

class RegistrationsSection {
    
    element!: HTMLElement
    includeNewRegistrationContainer!: IncludeNewRegistrationContainer
    registrationsContainer!: RegistrationsContainer
    goToTerminalSection!: GoToTerminalSection
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "registrations-section";
        this.element.className = "w-full h-full gap-x-2 flex items-center justify-center transition-opacity duration-300";
        this.element.style.display = "none";
    }
    
    private createComponents() {
        this.goToTerminalSection = new GoToTerminalSection(this.element);
        this.includeNewRegistrationContainer = new IncludeNewRegistrationContainer(this.element);
        this.registrationsContainer = new RegistrationsContainer(this.element);
    }
    
}

class IncludeNewRegistrationContainer {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[30%] h-full gap-y-2 p-1 flex flex-col items-center justify-center border border-gray-300 dark:border-gray-900 transition-colors duration-300";
    }
    
    private createComponents() {

    }
    
}

class RegistrationsContainer {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[70%] h-full gap-y-2 p-1 flex flex-col items-center justify-center border border-gray-300 dark:border-gray-900 transition-colors duration-300";
    }
    
    private createComponents() {

    }
    
}

class GoToTerminalSection {
    
    wrapper!: HTMLElement
    button!: HTMLButtonElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.startListeners();
        appendTo.appendChild(this.wrapper);
    }
    
    private createSelf() {
        this.wrapper = document.createElement("div");
        this.wrapper.className = "w-auto h-auto flex flex-1 justify-end items-center";
        this.button = document.createElement("button");
        this.button.className = "w-auto h-auto py-1 px-2 bg-amber-700 hover:bg-amber-900 transition-colors duration-300 rounded-md cursor-pointer text-white";
        this.button.innerText = "Ir para terminal.";
        this.wrapper.appendChild(this.button);
    }
    
    private startListeners() {
        this.button.addEventListener("click", () => {
            let terminalSection = document.getElementById("terminal-section")!;
            let registrationsSection = document.getElementById("registrations-section")!
            registrationsSection.style.opacity = "0";
            setTimeout(() => {
                registrationsSection.style.display = "none";
                terminalSection.style.opacity = "0";
                terminalSection.style.display = "flex";
                terminalSection.offsetHeight;
                terminalSection.style.opacity = "1";
            }, 300);
        });
    }
    
}