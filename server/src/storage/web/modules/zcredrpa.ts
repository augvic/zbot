export default class zCredRpa {
    
    element!: HTMLElement
    container!: Container
    
    constructor(moduleContainer: HTMLElement, socket: any) {
        this.createSelf();
        this.createComponents(socket);
        this.startListeners(socket);
        moduleContainer.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zCredRpa";
        this.element.className = "w-full h-full opacity-fade-in bg-gray-300 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center";
    }
    
    private createComponents(socket: any) {
        this.container = new Container(this.element, socket)
    }
    
    private startListeners(socket: any) {
        socket.emit("zcredrpa_refresh");
        socket.off("zcredrpa_notification");
        socket.on("zcredrpa_notification", (response: {[key: string]: string | boolean}) => {
            if (response.success) {
                new Notification(response.message as string, "green");
            } else {
                new Notification(response.message as string, "red");
            }
        });
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
        this.terminal = new Terminal(this.element, socket);
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
        this.status = new RpaStatus(this.element, socket);
    }
    
}

class TurnOnButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, socket: any) {
        this.createSelf();
        this.createComponents();
        this.startListeners(socket);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto p-1 bg-green-700 hover:bg-green-900 transition-colors duration-300 rounded-md cursor-pointer";
    }
    
    private createComponents() {
        this.icon = new Icon("static/images/play.png", this.element);
    }
    
    private startListeners(socket: any) {
        this.element.addEventListener("click", () => {
            socket.emit("zcredrpa_start");
        });
    }
    
}

class TurnOffButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, socket: any) {
        this.createSelf();
        this.createComponents();
        this.startListeners(socket);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "w-auto h-auto p-1 bg-red-700 hover:bg-red-900 transition-colors duration-300 rounded-md cursor-pointer";
    }
    
    private createComponents() {
        this.icon = new Icon("static/images/stop.png", this.element);
    }
    
    private startListeners(socket: any) {
        this.element.addEventListener("click", () => {
            socket.emit("zcredrpa_stop");
        });
    }
    
}

class RpaStatus {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, socket: any) {
        this.createSelf();
        this.startListeners(socket);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("p");
        this.element.className = "cursor-default text-black dark:text-white transition-colors duration-300 transition-opacity duration-300";
    }
    
    private startListeners(socket: any) {
        socket.off("zcredrpa_status");
        socket.on("zcredrpa_status", (response: {[key: string]: string}) => {
            this.element.style.opacity = "0";
            setTimeout(() => {
                this.element.innerText = `Status: ${response.status}`;
                this.element.style.opacity = "1";                
            }, 300);
        });
    }
    
}

class Terminal {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, socket: any) {
        this.createSelf();
        this.startListeners(socket);
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-[95%] flex flex-col gap-y-1 p-3 bg-black text-white rounded-md overflow-y-auto custom-scroll scroll-smooth";
    }
    
    private startListeners(socket: any) {
        socket.off("zcredrpa_terminal");
        socket.on("zcredrpa_terminal", (response: {[key: string]: string}) => {
            const distanceFromBottom = this.element.scrollHeight - (this.element.scrollTop + this.element.clientHeight);
            new TerminalText(this.element, response.message);
            if (distanceFromBottom <= 20) {
                this.element.scrollTop = this.element.scrollHeight;
            }
        });
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