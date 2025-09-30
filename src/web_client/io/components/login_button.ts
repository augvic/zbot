import { Button } from "/component-bundle/button.js";
import { Notification } from "/component-bundle/notification.js";

export class LoginButton extends Button {
    
    element!: HTMLElement
    
    constructor(appendTo: HTMLElement) {
        super(appendTo, "30%", "30px", "blue", "Acessar");
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private startListeners() {
        this.element.addEventListener("click", async () => {
            const user = (document.getElementById("user") as HTMLInputElement).value!;
            const password = (document.getElementById("password") as HTMLInputElement).value!;
            const response = await fetch(`${window.location.origin}/zlogin`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user, password })
            });
            const responseDict = await response.json()
            if (!responseDict.success) {
                new Notification("Login inválido.", "red");
            } else {
                const loginPage = document.getElementById("zlogin")!;
                loginPage.classList.add("opacity-fade-out");
                loginPage.addEventListener("animationend", async () => {
                    document.body.innerHTML = "";
                    await import(`${window.location.origin}/zindex`);
                    new Notification("Logado com sucesso.", "green");
                });
            }
        });
    }
    
}
