export class App {
    
    element: HTMLDivElement
    
    constructor() {
        this.element = document.createElement("div");
        this.element.className = "w-full h-full";
    }
    
}

export class Page {
    
    element: HTMLDivElement
    
    constructor(orientation: string) {
        this.element = document.createElement("div");
        this.element.className = "w-full h-full flex justify-center overflow-hidden items-center bg-gray-300 dark:bg-gray-900 transition-colors duration-300";
        if (orientation == "vertical") {
            this.element.classList.add("flex-col");
        }
    }
    
}

export class Container {
    
    element: HTMLDivElement
    
    constructor(orientation: string, width: string, height: string, items: string, justify: string) {
        this.element = document.createElement("div");
        this.element.className = "flex bg-white dark:bg-gray-700 rounded-md gap-2 p-3 transition-colors duration-300";
        this.element.style.width = width;
        this.element.style.height = height;
        this.element.style.justifyContent = justify;
        this.element.style.alignItems = items;
        if (orientation == "vertical") {
            this.element.classList.add("flex-col");
        }
    }
    
}

export class Wrapper {
    
    element: HTMLDivElement
    
    constructor(orientation: string, width: string, height: string, items: string, justify: string) {
        this.element = document.createElement("div");
        this.element.className = "flex gap-2 overflow-auto custom-scroll";
        this.element.style.width = width;
        this.element.style.height = height;
        this.element.style.justifyContent = justify;
        this.element.style.alignItems = items;
        if (orientation == "vertical") {
            this.element.classList.add("flex-col");
        }
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
    
    constructor(text: string, bold: boolean, size: string) {
        this.element = document.createElement("label");
        this.element.className = "text-black dark:text-white cursor-default transition-colors duration-300 whitespace-nowrap";
        this.element.innerText = text;
        if (bold) {
            this.element.classList.add("font-bold");
        }
        if (size == "sm") {
            this.element.classList.add("text-sm");
        }
        if (size == "md") {
            this.element.classList.add("text-md");
        }
        if (size == "lg") {
            this.element.classList.add("text-2xl");
        }
    }
    
}

export class Button {
    
    element: HTMLButtonElement
    
    constructor(text: string, bgColor: string, width: string, height: string) {
        this.element = document.createElement("button");
        this.element.className = "rounded-md text-white cursor-pointer transition-colors duration-300 p-2";
        this.element.innerText = text;
        this.element.style.width = width;
        this.element.style.height = height;
        if (bgColor == "blue") {
            this.element.classList.add("bg-blue-700");
            this.element.classList.add("hover:bg-blue-900");
        } else if (bgColor == "green") {
            this.element.classList.add("bg-green-700");
            this.element.classList.add("hover:bg-green-900");
        } else if (bgColor == "orange") {
            this.element.classList.add("bg-amber-700");
            this.element.classList.add("hover:bg-amber-900");
        } else if (bgColor == "red") {
            this.element.classList.add("bg-red-700");
            this.element.classList.add("hover:bg-red-900");
        } else {
            this.element.classList.add("hover:bg-gray-300");
        }
    }
    
}

export class IconButton {
    
    element: HTMLButtonElement
    icon: HTMLImageElement
    
    constructor(src: string, iconSize: number, bgColor: string) {
        this.element = document.createElement("button");
        this.element.className = "rounded-md text-white cursor-pointer transition-colors duration-300 p-1";
        this.icon = document.createElement("img");
        this.icon.src = src;
        if (iconSize == 5) {
            this.icon.classList.add("size-5");
        } else if (iconSize == 7) {
            this.icon.classList.add("size-7");
        } else {
            this.icon.classList.add("size-5");
        }
        if (bgColor == "blue") {
            this.element.classList.add("bg-blue-700");
            this.element.classList.add("hover:bg-blue-900");
        } else if (bgColor == "green") {
            this.element.classList.add("bg-green-700");
            this.element.classList.add("hover:bg-green-900");
        } else if (bgColor == "orange") {
            this.element.classList.add("bg-amber-700");
            this.element.classList.add("hover:bg-amber-900");
        } else if (bgColor == "red") {
            this.element.classList.add("bg-red-700");
            this.element.classList.add("hover:bg-red-900");
        } else {
            this.element.classList.add("hover:bg-gray-300");
        }
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
            setTimeout(() => {
                this.element.remove()
            }, 400);
        }, 3000);
    }
    
}

export class BlurContainer {
    
    element!: HTMLElement
    
    constructor(orientation: string, width: string, height: string, fixedTopBottom: string, fixedLeftRight: string) {
        this.element = document.createElement("div");
        this.element.className = "w-[300px] flex fixed bg-white/30 dark:bg-gray-700/30 z-40 p-3 gap-2";
        this.element.style.height = height;
        this.element.style.width = width;
        this.element.style.backdropFilter = "blur(6px)";
        this.element.style.display = "none";
        if (orientation == "vertical") {
            this.element.classList.add("flex-col");
        }
        if (fixedTopBottom == "bottom") {
            this.element.classList.add("bottom-0");
        } else {
            this.element.classList.add("top-0");
        }
        if (fixedLeftRight == "left") {
            this.element.classList.add("left-0");
            this.element.classList.add("rounded-br-lg");
            this.element.classList.add("rounded-tr-lg");
        } else {
            this.element.classList.add("right-0")
            this.element.classList.add("rounded-bl-lg");
            this.element.classList.add("rounded-tl-lg");
        }
    }
    
}

export class HoverSpan {
    
    element!: HTMLElement
    
    constructor(text: string) {
        this.element = document.createElement("span");
        this.element.className = "text-nowrap z-50 bg-blue-900 text-white py-1 px-4 rounded-lg absolute left-80 w-auto h-auto cursor-default";
        this.element.style.fontSize = "small";
        this.element.innerText = text;
    }
    
}

export class Table {
    
    wrapper: HTMLDivElement
    table: HTMLDivElement
    cells: {[key: string]: HTMLDivElement[]}
    
    constructor(width: string, height: string, rows: [{}]) {
        this.wrapper = document.createElement("div");
        this.wrapper.className = "overflow-auto custom-scroll";
        this.wrapper.style.width = width;
        this.wrapper.style.height = height;
        this.table = document.createElement("div");
        this.table.className = "h-auto w-auto flex flex-col whitespace-nowrap cursor-default text-center text-black dark:text-white transition-colors duration-300";
        let header = true;
        this.cells = {};
        rows.forEach(row => {
            const tableRow = document.createElement("div");
            if (header) {
                tableRow.className = "font-bold h-[46px] w-auto flex bg-gray-300 dark:bg-gray-900 transition-colors duration-300 sticky top-0 rounded-tl-lg rounded-tr-lg";
                header = false;
            } else {
                tableRow.className = "w-auto h-[46px] flex border-b-2 border-b-gray-300 dark:border-b-gray-900 table-row-transitions";
            }
            Object.entries(row).forEach(([key, value]) => {
                if (!this.cells[key]) {
                    this.cells[key] = [];
                }
                const cell = document.createElement("div");
                cell.className = `p-2 h-auto w-auto flex items-center justify-center`; 
                cell.innerText = value as string;
                tableRow.appendChild(cell);
                this.cells[key].push(cell);
            });
            this.table.appendChild(tableRow);
        });
        this.wrapper.appendChild(this.table);
    }
    
    public adjustColumns() {
        Object.entries(this.cells).forEach(([key, cells]) => {
            let width = 0;
            cells.forEach(cell => {
                if (cell.offsetWidth > width) {
                    width = cell.offsetWidth;
                }
            });
            cells.forEach(cell => {
                cell.style.width = width + "px";
            });
        });
    }
    
}