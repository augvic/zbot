import { Page } from "/component-bundle/page.js";
import { LoginContainer } from "/component-bundle/login_container.js";

export default class ZloginPage extends Page {
    
    loginContainer!: LoginContainer
    
    constructor() {
        super("zLogin");
        this.createComponents();
        this.startListeners();
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
