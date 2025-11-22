import { ThemeButton } from "../global/theme_button";
import { Notification } from "../global/notification";
import { MakeRequestTask } from "../../tasks/make_request";

export class Page {
    
    element!: HTMLElement
    loginContainer!: Container
    
    constructor() {
        this.element = document.createElement("div");
        this.element.id = "zLogin";
        this.element.className = "w-full h-full flex justify-center items-center bg-gray-300 dark:bg-gray-900 transition-colors duration-300";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.loginContainer = new Container(this.element, makeRequestTask);
    }
    
    private startListeners() {
        this.element.addEventListener("keydown", (event) => {
            if (event.key === "Enter") {
                this.loginContainer.loginButton.element.click();
            }
        });
    }
    
}

export class Container {
    
    element!: HTMLElement
    title!: Title
    userInput!: Input
    passwordInput!: Input
    loginButton!: Button
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-[200px] w-[400px] flex flex-col items-center justify-center bg-white dark:bg-gray-700 rounded-md gap-2 opacity-fade-in transition-colors duration-300";
    }
    
    private createComponents(makeRequestTask: MakeRequestTask) {
        this.title = new Title(this.element);
        this.userInput = new Input(this.element, "user", "Matrícula", "text");
        this.passwordInput = new Input(this.element, "password", "Senha", "password");
        this.loginButton = new Button(this.element, makeRequestTask);
    }
    
}

export class Title {
    
    element!: HTMLElement
    label!: Label
    themeButton!: ThemeButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "w-[70%] h-auto flex gap-2 items-center justify-center";
    }
    
    private createComponents() {
        this.label = new Label(this.element);
        this.themeButton = new ThemeButton(this.element, false)
    }
    
}

export class Input {
    
    element!: HTMLInputElement
    
    constructor(appendTo: HTMLElement, id: string, placeholder: string, type: string) {
        this.createSelf(placeholder, type, id);
        appendTo.appendChild(this.element); 
    }
    
    private createSelf(placeholder: string, type: string, id: string) {
        this.element = document.createElement("input");
        this.element.className = "h-[30px] w-[70%] bg-white rounded-md border border-gray-300 outline-none p-3";
        this.element.type = type;
        this.element.id = id;
        this.element.placeholder = placeholder;
    }    
    
}

export class Label {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("h1");
        this.element.className = "text-black dark:text-white font-bold text-2xl cursor-default transition-colors duration-300";
        this.element.innerText = "Login";
    }
    
}

export class Button {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequestTask) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "h-[30px] w-[30%] rounded-md my-2 bg-blue-700 text-white hover:bg-blue-900 cursor-pointer transition-colors duration-300";
        this.element.innerText = "Acessar";
    }
    
    private startListeners(makeRequestTask: MakeRequestTask) {
        this.element.addEventListener("click", async () => {
            const user = (document.getElementById("user") as HTMLInputElement).value!;
            const password = (document.getElementById("password") as HTMLInputElement).value!;
            const response = await makeRequestTask.post("/login", "application/json", { user, password });
            if (!response.success) {
                new Notification(response.message, "red");
            } else {
                const loginPage = document.getElementById("zLogin")!;
                loginPage.classList.add("opacity-fade-out");
                loginPage.addEventListener("animationend", () => {
                    loginPage.remove();
                    document.dispatchEvent(new Event("load:index"));
                    new Notification(response.message, "green");
                });
            }
        });
    }
    
}
