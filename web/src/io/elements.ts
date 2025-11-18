export class App {
    
    element: HTMLDivElement
    
    constructor() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-full";
    }
    
}

export class Page {
    
    element: HTMLDivElement
    
    constructor() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-full flex justify-center overflow-hidden items-center bg-gray-300 dark:bg-gray-900 transition-colors duration-300";
    }
    
}

export class VerticalContainer {
    
    element: HTMLDivElement
    
    constructor(width: string, height: string, items: string, justify: string) {
        this.element = document.createElement("div");
        this.element.className = "flex flex-col bg-white dark:bg-gray-700 rounded-md gap-y-2 p-3 opacity-fade-in transition-colors duration-300";
        this.element.style.width = width;
        this.element.style.height = height;
        this.element.style.justifyContent = justify;
        this.element.style.alignItems = items;
    }
    
}

export class HorizontalContainer {
    
    element: HTMLDivElement
    
    constructor(width: string, height: string, items: string, justify: string) {
        this.element = document.createElement("div");
        this.element.className = "flex bg-white dark:bg-gray-700 rounded-md gap-x-2 p-3 opacity-fade-in transition-colors duration-300";
        this.element.style.width = width;
        this.element.style.height = height;
        this.element.style.justifyContent = justify;
        this.element.style.alignItems = items;
    }
    
}

export class HorizontalContainerNoBg {
    
    element: HTMLDivElement
    
    constructor(width: string, height: string, items: string, justify: string) {
        this.element = document.createElement("div");
        this.element.className = "flex gap-x-2 items-center";
        this.element.style.width = width;
        this.element.style.height = height;
        this.element.style.justifyContent = justify;
        this.element.style.alignItems = items;
    }
    
}

export class VerticalContainerNoBg {
    
    element: HTMLDivElement
    
    constructor(width: string, height: string, items: string, justify: string) {
        this.element = document.createElement("div");
        this.element.className = "flex flex-col gap-y-2 items-center";
        this.element.style.width = width;
        this.element.style.height = height;
        this.element.style.justifyContent = justify;
        this.element.style.alignItems = items;
    }
    
}

export class Input {
    
    element: HTMLInputElement
    
    constructor(placeholder: string, type: string, width: string, height: string) {
        this.element = document.createElement("input");
        this.element.className = "bg-white rounded-md border border-gray-300 outline-none p-3";
        this.element.type = type;
        this.element.placeholder = placeholder;
        this.element.style.width = width;
        this.element.style.height = height;
    }
    
}

export class Label {
    
    element: HTMLLabelElement
    
    constructor(text: string) {
        this.element = document.createElement("label");
        this.element.className = "text-black dark:text-white font-bold text-2xl cursor-default transition-colors duration-300";
        this.element.innerText = text;
    }
    
}

export class Button {
    
    element: HTMLButtonElement
    
    constructor(text: string, bgColor: string) {
        this.element = document.createElement("button");
        this.element.className = "rounded-md text-white cursor-pointer transition-colors duration-300";
        this.element.innerText = text;
        if (bgColor == "blue") {
            this.element.classList.add("bg-blue-700");
            this.element.classList.add("hover:bg-blue-900");
        }
        if (bgColor == "green") {
            this.element.classList.add("bg-green-700");
            this.element.classList.add("hover:bg-green-900");
        }
    }
    
}

export class IconButton {
    
    element: HTMLButtonElement
    icon: HTMLImageElement
    
    constructor(src: string) {
        this.element = document.createElement("button");
        this.element.className = "cursor-pointer w-auto h-auto rounded-md transition-colors duration-300 hover:bg-gray-300 dark:hover:bg-gray-900 absolute ml-25 transition-colors duration-300";
        this.icon = document.createElement("img");
        this.icon.src = src;
        this.icon.className = "opacity-fade-in";
        this.element.appendChild(this.icon);
    }
    
}

export class Notification {
    
    element: HTMLDivElement
    
    constructor(message: string, color: string) {
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
        const notifications = document.querySelectorAll<HTMLElement>(".notification");
        notifications.forEach(notification => {
            if (notification != this.element) {
                const currentBottom = parseInt(
                    getComputedStyle(notification).bottom.replace("px", "")
                );
                notification.style.bottom = (currentBottom + 60) + "px";
            }
        });
        document.body.appendChild(this.element);
        setTimeout(() => {
            this.element.classList.remove("fade-in-right");
            this.element.classList.add("fade-out-right");
            this.element.addEventListener("animationend", () => {
                this.element.remove()
            }, { once: true });
        }, 3000);
    }
    
}

export class LeftMenu {
    
    element!: HTMLElement
    
    constructor() {
        this.element = document.createElement("div");
        this.element.className = "w-[300px] flex-col fixed bg-white/30 dark:bg-gray-700/30 z-40 p-3 gap-y-3 bottom-0 rounded-br-lg rounded-tr-lg";
        this.element.style.height = "calc(100vh - 50px)";
        this.element.style.backdropFilter = "blur(6px)";
        this.element.style.display = "none";
    }
    
}

export class HoverSpan {
    
    element!: HTMLElement
    
    constructor(text: string) {
        this.element = document.createElement("span");
        this.element.className = "text-nowrap opacity-fade-in z-50 bg-blue-900 text-white py-1 px-4 rounded-lg absolute left-80 w-auto h-auto cursor-default";
        this.element.style.fontSize = "small";
        this.element.innerText = text;
    }
    
}
