export default class zRegRpa {
    
    element!: HTMLElement
    container!: Container
    websocketListeners!: WebSocketListeners
    
    constructor(moduleContainer: HTMLElement, socket: any) {
        this.createSelf();
        this.createComponents(socket);
        socket.emit("regrpa_refresh");
        moduleContainer.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zRegRpa";
        this.element.className = "w-full h-full opacity-fade-in bg-gray-300 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center";
    }
    
    private createComponents(socket: any) {
        this.container = new Container(this.element, socket)
        this.websocketListeners = new WebSocketListeners(this, socket);
    }
    
}

class Container {
    
    element!: HTMLElement
    topBar!: ContainerTopBar
    terminal!: Terminal
    
    constructor(appendTo: HTMLElement, socket: any) {
        this.createSelf();
        this.createComponents(socket);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[95%] h-[95%] p-3 gap-y-2 bg-white dark:bg-gray-700 transition-colors duration-300 flex flex-col items-center justify-center rounded-lg";
    }
    
    private createComponents(socket: any) {
        this.topBar = new ContainerTopBar(this.element, socket)
        this.terminal = new Terminal(this.element);
    }
    
}

class ContainerTopBar {
    
    element!: HTMLElement
    turnOnButton!: TurnOnButton
    turnOffButton!: TurnOffButton
    status!: RpaStatus
    
    constructor(appendTo: HTMLElement, socket: any) {
        this.createSelf();
        this.createComponents(socket);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[5%] flex items-center gap-x-2";
    }
    
    private createComponents(socket: any) {
        this.turnOnButton = new TurnOnButton(this.element, socket);
        this.turnOffButton = new TurnOffButton(this.element, socket);
        this.status = new RpaStatus(this.element);
    }
    
}

class TurnOnButton {
    
    element!: HTMLButtonElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, socket: any) {
        this.createSelf();
        this.createComponents();
        this.startListeners(socket);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.id = "turn-on-button";
        this.element.className = "w-auto h-auto p-1 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer";
    }
    
    private createComponents() {
        this.icon = new Icon("static/images/play.png", this.element);
    }
    
    private startListeners(socket: any) {
        this.element.addEventListener("click", () => {
            socket.emit("regrpa_start");
        });
    }
    
}

class TurnOffButton {
    
    element!: HTMLButtonElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, socket: any) {
        this.createSelf();
        this.createComponents();
        this.startListeners(socket);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.id = "turn-off-button";
        this.element.className = "w-auto h-auto p-1 bg-red-700 hover:bg-red-900 transition-colors duration-300 rounded-md cursor-pointer";
    }
    
    private createComponents() {
        this.icon = new Icon("static/images/stop.png", this.element);
    }
    
    private startListeners(socket: any) {
        this.element.addEventListener("click", () => {
            socket.emit("regrpa_stop");
        });
    }
    
}

class RpaStatus {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("p");
        this.element.className = "cursor-default text-black dark:text-white transition-colors transition-opacity duration-300";
    }
    
}

class Terminal {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[95%] flex flex-col gap-y-1 p-3 bg-black text-white rounded-md overflow-y-auto custom-scroll scroll-smooth";
    }
    
}

class TerminalText {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, text: string) {
        this.createSelf(text);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(text: string) {
        this.element = document.createElement("p");
        this.element.className = "cursor-default text-white";
        this.element.innerText = text;
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
        this.element.className = "size-5 opacity-fade-in";
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

class WebSocketListeners {
    
    constructor(page: zRegRpa, socket: any) {
        this.startListeners(page, socket);
    }
    
    private startListeners(page: zRegRpa, socket: any) {
        socket.off("regrpa_terminal");
        socket.off("regrpa_notification");
        socket.off("regrpa_status");
        socket.off("regrpa_terminal");
        socket.on("regrpa_terminal", (response: {[key: string]: string}) => {
            const distanceFromBottom = page.container.terminal.element.scrollHeight - (page.container.terminal.element.scrollTop + page.container.terminal.element.clientHeight);
            new TerminalText(page.container.terminal.element, response.message);
            if (distanceFromBottom <= 20) {
                page.container.terminal.element.scrollTop = page.container.terminal.element.scrollHeight;
            }
        });
        socket.on("regrpa_notification", (response: {[key: string]: string | boolean}) => {
            if (response.success) {
                new Notification(response.message as string, "green");
            } else {
                new Notification(response.message as string, "red");
            }
        });
        socket.on("regrpa_status", (response: {[key: string]: string}) => {
            page.container.topBar.status.element.style.opacity = "0";
            setTimeout(() => {
                page.container.topBar.status.element.innerText = `Status: ${response.status}`;
                page.container.topBar.status.element.style.opacity = "1";   
            }, 300);
            if (response.status == "Em processamento.") {
                page.container.topBar.turnOffButton.element.disabled = false;
                page.container.topBar.turnOffButton.element.style.backgroundColor = "oklch(50.5% 0.213 27.518)";
                page.container.topBar.turnOffButton.element.style.cursor = "pointer";
                page.container.topBar.turnOnButton.element.disabled = true;
                page.container.topBar.turnOnButton.element.style.backgroundColor = "#919191";
                page.container.topBar.turnOnButton.element.style.cursor = "not-allowed";
            }
            if (response.status == "Desligado.") {
                page.container.topBar.turnOnButton.element.disabled = false;
                page.container.topBar.turnOnButton.element.style.backgroundColor = "oklch(52.7% 0.154 150.069)";
                page.container.topBar.turnOnButton.element.style.cursor = "pointer";
                page.container.topBar.turnOffButton.element.disabled = true;
                page.container.topBar.turnOffButton.element.style.backgroundColor = "#919191";
                page.container.topBar.turnOffButton.element.style.cursor = "not-allowed";
            }
        });
    }
    
}