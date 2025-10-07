import { io } from "socket.io-client";

const socket = io(`${window.location.origin}`);

export default class zCredRpa {
    
    element!: HTMLElement
    container!: Container
    
    constructor(moduleContainer: HTMLElement) {
        this.createSelf();
        this.createComponents();
        moduleContainer.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zCredRpa";
        this.element.className = "w-full h-full opacity-fade-in bg-gray-300 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center";
    }
    
    private createComponents() {
        this.container = new Container(this.element)
    }
    
}

class Container {
    
    element!: HTMLElement
    topBar!: ContainerTopBar
    terminal!: ContainerTerminal
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[95%] h-[95%] p-3 gap-y-2 bg-white dark:bg-gray-700 transition-colors duration-300 flex flex-col items-center justify-center rounded-lg";
    }
    
    private createComponents() {
        this.topBar = new ContainerTopBar(this.element)
        this.terminal = new ContainerTerminal(this.element);
    }
    
}

class ContainerTopBar {
    
    element!: HTMLElement
    turnOnButton!: TurnOnButton
    turnOffButton!: TurnOffButton
    status!: RpaStatus
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[5%] flex items-center gap-x-2";
    }
    
    private createComponents() {
        this.turnOnButton = new TurnOnButton(this.element);
        this.turnOffButton = new TurnOffButton(this.element);
        this.status = new RpaStatus(this.element);
    }
    
}

class TurnOnButton {
    
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
        this.element.className = "w-auto h-auto p-1 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer";
    }
    
    private createComponents() {
        this.icon = new Icon("static/images/play.png", this.element);
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            socket.emit("start_credit_rpa");
        });
    }
    
}

class TurnOffButton {
    
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
        this.element.className = "w-auto h-auto p-1 bg-red-700 hover:bg-red-900 transition-colors duration-300 rounded-md cursor-pointer";
    }
    
    private createComponents() {
        this.icon = new Icon("static/images/stop.png", this.element);
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            socket.emit("stop_credit_rpa");
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
        this.element.className = "cursor-default text-black dark:text-white transition-colors duration-300";
        this.element.innerText = "Status:";
        socket.on("update_status", (response: {[key: string]: string}) => {
            this.element.innerText = `Status: ${response.status}`;
        });
    }
    
}

class ContainerTerminal {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[95%] flex bg-black text-white rounded-md";
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