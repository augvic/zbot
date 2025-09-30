import { Container } from "/component-bundle/container.js";
import { Input } from "/component-bundle/input.js";
import { TitleBar } from "/component-bundle/title_bar.js";
import { LoginButton } from "/component-bundle/login_button.js";

export class LoginContainer extends Container {
    
    element!: HTMLElement
    title!: TitleBar
    userInput!: Input
    passwordInput!: Input
    loginButton!: LoginButton
    
    constructor(appendTo: HTMLElement) {
        super(appendTo, "400px", "200px");
        this.createComponents();
        appendTo.appendChild(this.element);
    }
    
    private createComponents() {
        this.title = new TitleBar(this.element);
        this.userInput = new Input(this.element, "user", "Matrícula", "text", "70%", "30px");
        this.passwordInput = new Input(this.element, "password", "Senha", "password", "70%", "30px");
        this.loginButton = new LoginButton(this.element);
    } 
    
}
