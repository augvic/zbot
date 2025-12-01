export class Container {
    
    container: HTMLDivElement
    wrapper: HTMLDivElement
    
    constructor(
        orientation: string,
        width: string,
        height: string,
        verticalAlign: string,
        horizontalAlign: string,
        bgColor: boolean,
        blur: boolean,
        fixed: { verticalPosition: string, horizontalPosition: string } | null
    ) {
        this.container = document.createElement("div");
        this.container.className = "flex rounded-md gap-2 p-3 transition-colors duration-300";
        this.container.style.width = width;
        this.container.style.height = height;
        this.wrapper = document.createElement("div");
        this.wrapper.className = "flex w-full h-full";
        this.wrapper.style.justifyContent = horizontalAlign;
        this.wrapper.style.alignItems = verticalAlign;
        if (bgColor) {
            this.container.classList.add("bg-white");
            this.container.classList.add("dark:bg-gray-700");
        }
        if (orientation == "vertical") {
            this.wrapper.classList.add("flex-col");
        }
        if (blur) {
            this.container.classList.add("bg-white/30");
            this.container.classList.add("dark:bg-gray-700/30");
        }
        if (fixed && fixed.verticalPosition == "top") {
            this.container.classList.add("fixed z-50");
            this.container.classList.add("top-0");
        }
        if (fixed && fixed.verticalPosition == "mid") {
            this.container.classList.add("fixed z-50");
            this.container.classList.add("top-1/2");
        }
        if (fixed && fixed.verticalPosition == "bot") {
            this.container.classList.add("fixed z-50");
            this.container.classList.add("bottom-0");
        }
        if (fixed && fixed.horizontalPosition == "left") {
            this.container.classList.add("fixed z-50");
            this.container.classList.add("left-0");
        }
        if (fixed && fixed.horizontalPosition == "mid") {
            this.container.classList.add("fixed z-50");
            this.container.classList.add("left-1/2");
        }
        if (fixed && fixed.horizontalPosition == "right") {
            this.container.classList.add("fixed z-50");
            this.container.classList.add("right-0");
        }
        this.container.appendChild(this.wrapper);
    }
    
}

export class Input {
    
    input: HTMLInputElement
    
    constructor(
        placeholder: string,
        type: string,
        width: string,
        height: string
    ) {
        this.input = document.createElement("input");
        this.input.className = "bg-white rounded-md border border-gray-300 outline-none p-3";
        this.input.type = type;
        this.input.placeholder = placeholder;
        this.input.style.width = width;
        this.input.style.height = height;
    }
    
}

export class Label {
    
    label: HTMLLabelElement
    
    constructor(
        text: string,
        bold: boolean,
        size: string
    ) {
        this.label = document.createElement("label");
        this.label.className = "text-black dark:text-white cursor-default transition-colors duration-300 whitespace-nowrap";
        this.label.innerText = text;
        if (bold) {
            this.label.classList.add("font-bold");
        }
        if (size == "sm") {
            this.label.classList.add("text-sm");
        }
        if (size == "md") {
            this.label.classList.add("text-md");
        }
        if (size == "lg") {
            this.label.classList.add("text-2xl");
        }
    }
    
}

export class Button {
    
    container: HTMLDivElement
    button: HTMLButtonElement
    icon?: HTMLImageElement
    hoverSpan?: HTMLDivElement
    
    constructor(
        text: string,
        bgColor: string,
        width: string,
        height: string,
        icon: string | null,
        hoverSpan: { text: string, position: string, bgColor: string } | null
    ) {
        this.container = document.createElement("div");
        this.container.className = "flex gap-2";
        this.button = document.createElement("button");
        this.button.className = "flex items-center justify-center w-auto h-auto rounded-md text-white cursor-pointer transition-colors duration-300 p-2";
        this.button.innerText = text;
        this.button.style.width = width;
        this.button.style.height = height;
        if (bgColor == "blue") {
            this.button.classList.add("bg-blue-700");
            this.button.classList.add("hover:bg-blue-900");
        } else if (bgColor == "green") {
            this.button.classList.add("bg-green-700");
            this.button.classList.add("hover:bg-green-900");
        } else if (bgColor == "orange") {
            this.button.classList.add("bg-amber-700");
            this.button.classList.add("hover:bg-amber-900");
        } else if (bgColor == "red") {
            this.button.classList.add("bg-red-700");
            this.button.classList.add("hover:bg-red-900");
        } else {
            this.button.classList.add("hover:bg-gray-300");
        }
        if (icon) {
            this.icon = document.createElement("img");
            this.icon.src = icon;
            this.icon.className = "size-5";
            this.button.classList.remove("p-2");
            this.button.classList.add("p-1");
            this.button.appendChild(this.icon);
        }
        if (hoverSpan) {
            this.hoverSpan = document.createElement("div");
            this.hoverSpan.className = "text-nowrap z-49 p-2 rounded-lg absolute left-80 w-auto h-auto cursor-default";
            if (hoverSpan.bgColor == "blue") {
                this.hoverSpan.classList.add("bg-blue-700");
            } else if (hoverSpan.bgColor == "green") {
                this.hoverSpan.classList.add("bg-green-700");
            } else if (hoverSpan.bgColor == "orange") {
                this.hoverSpan.classList.add("bg-amber-700");
            } else if (hoverSpan.bgColor == "red") {
                this.hoverSpan.classList.add("bg-red-700");
            } else {
                this.hoverSpan.classList.add("bg-white");
                this.hoverSpan.classList.add("text-black");
                this.hoverSpan.classList.add("dark:bg-gray-700");
                this.hoverSpan.classList.add("dark:bg-white");
            }
        }
        if (hoverSpan && hoverSpan.position == "left") {
            this.container.appendChild(this.hoverSpan!);
            this.container.appendChild(this.button);
        } else if (hoverSpan && hoverSpan.position == "right") {
            this.container.appendChild(this.button);
            this.container.appendChild(this.hoverSpan!);
        } else if (hoverSpan && hoverSpan.position == "top") {
            this.container.classList.add("flex-col");
            this.container.appendChild(this.hoverSpan!);
            this.container.appendChild(this.button);
        } else if (hoverSpan && hoverSpan.position == "bot") {
            this.container.classList.add("flex-col");
            this.container.appendChild(this.button);
            this.container.appendChild(this.hoverSpan!);
        } else {
            this.container.appendChild(this.button);
        }
    }
    
}

export class Notification {
    
    constructor(
        message: string,
        color: string
    ) {
        const element = document.createElement("div");
        element.className = "notification fixed z-50 bottom-4 right-5 py-3 px-6 text-white rounded-md cursor-default fade-in-right transition-[bottom] duration-300 ease";
        if (color == "green") {
            element.classList.add("bg-green-400");
        } else if (color == "orange") {
            element.classList.add("bg-amber-400");
        } else if (color == "red") {
            element.classList.add("bg-red-400");
        }
        element.innerText = message;
        const notifications = document.querySelectorAll<HTMLElement>(".notification");
        notifications.forEach(notification => {
            if (notification != element) {
                const currentBottom = parseInt(
                    getComputedStyle(notification).bottom.replace("px", "")
                );
                notification.style.bottom = (currentBottom + 60) + "px";
            }
        });
        document.body.appendChild(element);
        setTimeout(() => {
            element.classList.remove("fade-in-right");
            element.classList.add("fade-out-right");
            setTimeout(() => {
                element.remove()
            }, 400);
        }, 3000);
    }
    
}

export class Table {
    
    wrapper: HTMLDivElement
    table: HTMLDivElement
    cells: {[key: string]: HTMLDivElement[]}
    
    constructor(
        width: string,
        height: string,
        rows: [{}]
    ) {
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