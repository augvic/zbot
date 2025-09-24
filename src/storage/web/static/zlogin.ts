class Login {
    
    element!: HTMLElement
    loginContainer!: LoginContainer
    
    constructor() {
        this.createSelf();
        this.createComponents();
        document.body.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.id = "zlogin";
        this.element.className = "w-full h-full flex justify-center items-center bg-gray-300 dark:bg-gray-900 transition-colors duration-300";
    }
    
    private createComponents() {
        this.loginContainer = new LoginContainer(this.element);
    }
    
}

class LoginContainer {
    
    element!: HTMLElement
    title!: TitleContainer
    userInput!: Inputs
    passwordInput!: Inputs
    loginButton!: LoginButton
    
    constructor(appendTo: HTMLElement) {
        this.createSelf();
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createSelf() {
        this.element = document.createElement("div");
        this.element.className = "h-[200px] w-[400px] flex flex-col items-center justify-center bg-white dark:bg-gray-700 rounded-md gap-2 opacity-fade-in transition-colors duration-300";
        this.element.addEventListener("keydown", (event) => {
            if (event.key === "Enter") {
                this.loginButton.element.click();
            }
        });
    }
    
    private createComponents() {
        this.title = new TitleContainer(this.element);
        this.userInput = new Inputs(this.element, "user", "Matrícula", "text");
        this.passwordInput = new Inputs(this.element, "password", "Senha", "password");
        this.loginButton = new LoginButton(this.element);
    }
    
}

class TitleContainer {
    
    element!: HTMLElement
    label!: Label
    themeButton!: LoginDarkLightButton
    
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
        this.label = new Label(this.element);
        this.themeButton = new LoginDarkLightButton(this.element)
    }
    
}

class Inputs {
    
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

class Label {
    
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
                new LoginNotificationPopUp("Login inválido.", "red");
            } else {
                const loginPage = document.getElementById("zlogin")!;
                loginPage.classList.add("opacity-fade-out");
                loginPage.addEventListener("animationend", async () => {
                    document.body.innerHTML = "";
                    await import(`${window.location.origin}/index`);
                    new LoginNotificationPopUp("Logado com sucesso.", "green");
                });
            }
        });
    }
    
}

class LoginNotificationPopUp {
    
    element!: HTMLElement
    
    constructor(message: string, color: string) {
        this.createSelf(message, color);
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
        this.element.className = "fixed z-50 bottom-4 right-5 py-3 px-6 text-white rounded-md cursor-default fade-in-right";
        if (color == "green") {
            this.element.classList.add("bg-green-400");
        } else if (color == "orange") {
            this.element.classList.add("bg-amber-400");
        } else if (color == "red") {
            this.element.classList.add("bg-red-400");
        }
        this.element.innerText = message;
    }

}

class LoginDarkLightButton {
    
    element!: HTMLElement
    icon!: LoginIcon
    
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
            iconSrc = "static/images/moon.png";
        } else {
            iconSrc = "static/images/sun.png";
        }
        this.icon = new LoginIcon(this.element, iconSrc);
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            if (document.documentElement.classList.contains("light")) {
                document.documentElement.classList.remove("light");
                document.documentElement.classList.add("dark");
                window.localStorage.setItem("theme", "dark");
                this.icon.element.src = "static/images/sun.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
            } else {
                document.documentElement.classList.remove("dark");
                document.documentElement.classList.add("light");
                window.localStorage.setItem("theme", "light");
                this.icon.element.src = "static/images/moon.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
            }
        });
    }
    
}

class LoginIcon {
    
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

class Tasks {
    
    static setTheme() {
        if (window.localStorage.getItem("theme") == null) {
            window.localStorage.setItem("theme", "light");
        }
        if (window.localStorage.getItem("theme") == "light") {
            document.documentElement.classList.remove("dark");
            document.documentElement.classList.add("light");
        } else {
            document.documentElement.classList.remove("light");
            document.documentElement.classList.add("dark");
        }
    }
    
    static async loadLoginOrIndex() {
        const response = await fetch(`${window.location.origin}/zlogin`);
        const data = await response.json();
        if (data.logged_in) {
            document.body.innerHTML = "";
            await import(`${window.location.origin}/zindex`);
        } else {
            new Login();
        }
    }
    
}
