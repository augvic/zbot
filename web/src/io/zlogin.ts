import { UiFactory } from "../modules/ui_factory/ui_factory";
import * as components from "../modules/ui_factory/components";

export class Zlogin {
    
    page: components.Container
    container: components.Container
    titleBar: components.Container
    userInput: components.Input
    passwordInput: components.Input
    label: components.Label
    loginButton: components.Button
    
    constructor(ui_factory: UiFactory) {
        this.page = ui_factory.createContainer(
            "vertical",
            "100%",
            "100%",
            "center",
            "center",
            false,
            false,
            null
        )
        this.container = ui_factory.createContainer(
            "vertical", 
            "400px",
            "200px",
            "center",
            "center",
            true,
            false,
            null
        );
        this.titleBar = ui_factory.createContainer(
            "horizontal",
            "",
            "",
            "center", 
            "center",
            false,
            false,
            null
        );
        this.userInput = ui_factory.createInput(
            "Usuário",
            "text",
            "70%",
            "30px"
        );
        this.passwordInput = ui_factory.createInput(
            "Senha",
            "password",
            "70%",
            "30px"
        );
        this.label = ui_factory.createLabel(
            "Login",
            true,
            "lg"
        );
        this.loginButton = ui_factory.createButton(
            "Acessar",
            "blue",
            "40%",
            "",
            null,
            null
        );
    }
    
}