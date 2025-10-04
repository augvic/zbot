export default class zLogin {
    
    element!: HTMLElement
    loginContainer!: LoginContainer
    
    constructor() {
        this.createSelf();
        this.createComponents();
        this.startListeners();
        document.body.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zLogin";
        this.element.className = "w-full h-full flex justify-center items-center bg-gray-300 dark:bg-gray-900 transition-colors duration-300";
    }
    
    private createComponents() {
        this.loginContainer = new LoginContainer(this.element);
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
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-[200px] w-[400px] flex flex-col items-center justify-center bg-white dark:bg-gray-700 rounded-md gap-2 opacity-fade-in transition-colors duration-300";
    }
    
    private createComponents() {
        this.title = new TitleContainer(this.element);
        this.userInput = new LoginInput(this.element, "user", "Matrícula", "text");
        this.passwordInput = new LoginInput(this.element, "password", "Senha", "password");
        this.loginButton = new LoginButton(this.element);
    }
    
}

class TitleContainer {
    
    element!: HTMLElement
    label!: LoginLabel
    themeButton!: ThemeButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
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
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("button");
        this.element.className = "h-[30px] w-[30%] rounded-md my-2 bg-blue-700 text-white hover:bg-blue-900 cursor-pointer transition-colors duration-300";
        this.element.innerText = "Acessar";
    }
    
    private startListeners() {
        this.element.addEventListener("click", async () => {
            const user = (document.getElementById("user") as HTMLInputElement).value!;
            const password = (document.getElementById("password") as HTMLInputElement).value!;
            const response = await fetch(`${window.location.origin}/login`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user, password })
            });
            const responseDict = await response.json()
            if (!responseDict.success) {
                new Notification("Login inválido.", "red");
            } else {
                const loginPage = document.getElementById("zLogin")!;
                loginPage.classList.add("opacity-fade-out");
                loginPage.addEventListener("animationend", async () => {
                    document.body.innerHTML = "";
                    let bundle = await import(`${window.location.origin}/page-bundle/zindex.js`);
                    let bundleClass = bundle.default;
                    document.body.innerHTML = "";
                    new bundleClass();
                    new Notification("Logado com sucesso.", "green");
                });
            }
        });
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

class ThemeButton {
    
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
        this.element.className = "cursor-pointer w-auto h-auto rounded-md transition-colors duration-300 hover:bg-gray-300 dark:hover:bg-gray-900 absolute ml-25 transition-colors duration-300";
    }
    
    private createComponents() {
        let iconSrc = "";
        if (window.localStorage.getItem("theme") == "light") {
            iconSrc = "/static/images/moon.png";
        } else {
            iconSrc = "/static/images/sun.png";
        }
        this.icon = new Icon(this.element, iconSrc);
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            if (document.documentElement.classList.contains("light")) {
                document.documentElement.classList.remove("light");
                document.documentElement.classList.add("dark");
                window.localStorage.setItem("theme", "dark");
                this.icon.element.src = "/static/images/sun.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
            } else {
                document.documentElement.classList.remove("dark");
                document.documentElement.classList.add("light");
                window.localStorage.setItem("theme", "light");
                this.icon.element.src = "/static/images/moon.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
            }
        });
    }
    
}

class Icon {
    
    element!: HTMLImageElement
    
    constructor(appendTo: HTMLElement, src: string) {
        this.createSelf(src);
        appendTo.appendChild(this.element);
    }
    
    private createSelf(src: string) {
        this.element = document.createElement("img");
        this.element.src = src;
        this.element.className = "size-7 opacity-fade-in";
    }
}
