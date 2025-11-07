import { zIndex } from "./zindex";
export { zIndex } from "./zindex";
import { ThemeButton } from "../global/theme_button";
import { Notification } from "../global/notification";

export class zLogin {
    
    element!: HTMLElement
    loginContainer!: LoginContainer
    
    constructor(makeRequestTask: MakeRequest) {
        this.createSelf();
        document.getElementById("application-content")!.appendChild(this.element);
        this.createComponents(makeRequestTask);
        this.startListeners();
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zLogin";
        this.element.className = "w-full h-full flex justify-center items-center bg-gray-300 dark:bg-gray-900 transition-colors duration-300";
    }
    
    private createComponents(makeRequestTask: MakeRequest) {
        this.loginContainer = new LoginContainer(this.element, makeRequestTask);
    }
    
    private startListeners() {
        this.element.addEventListener("keydown", (event) => {
            if (event.key === "Enter") {
                this.loginContainer.loginButton.element.click();
            }
        });
    }
    
}

class LoginContainer {
    
    element!: HTMLElement
    title!: TitleContainer
    userInput!: LoginInput
    passwordInput!: LoginInput
    loginButton!: LoginButton
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequest) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.createComponents(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-[200px] w-[400px] flex flex-col items-center justify-center bg-white dark:bg-gray-700 rounded-md gap-2 opacity-fade-in transition-colors duration-300";
    }
    
    private createComponents(makeRequestTask: MakeRequest) {
        this.title = new TitleContainer(this.element);
        this.userInput = new LoginInput(this.element, "user", "Matrícula", "text");
        this.passwordInput = new LoginInput(this.element, "password", "Senha", "password");
        this.loginButton = new LoginButton(this.element, makeRequestTask);
    }
    
}

class TitleContainer {
    
    element!: HTMLElement
    label!: LoginLabel
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
        this.label = new LoginLabel(this.element);
        this.themeButton = new ThemeButton(this.element)
    }
    
}

class LoginInput {
    
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

class LoginLabel {
    
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

class LoginButton {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement, makeRequestTask: MakeRequest) {
        this.createSelf();
        appendTo.appendChild(this.element);
        this.startListeners(makeRequestTask);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "h-[30px] w-[30%] rounded-md my-2 bg-blue-700 text-white hover:bg-blue-900 cursor-pointer transition-colors duration-300";
        this.element.innerText = "Acessar";
    }
    
    private startListeners(makeRequestTask: MakeRequest) {
        this.element.addEventListener("click", async () => {
            const user = (document.getElementById("user") as HTMLInputElement).value!;
            const password = (document.getElementById("password") as HTMLInputElement).value!;
            const response = await makeRequestTask.execute("/login", "application/json", { user, password });
            if (!response.success) {
                new Notification(response.message, "red");
            } else {
                const loginPage = document.getElementById("zLogin")!;
                loginPage.classList.add("opacity-fade-out");
                loginPage.addEventListener("animationend", () => {
                    loginPage.remove();
                    new zIndex();
                    new Notification(response.message, "green");
                });
            }
        });
    }
    
}
