import * as elements from "../io/elements";

export class IO {
    
    global: Global
    zLogin: Zlogin
    zIndex: Zindex
    
    constructor() {
        this.global = new Global();
        this.zLogin = new Zlogin();
        this.zIndex = new Zindex();
    }
    
    public createButton(text: string, bgColor: string) {
        return new elements.Button(text, bgColor);
    }
    
    public createNotification(message: string, color: string) {
        return new elements.Notification(message, color);
    }
    
    public createHoverSpan(text: string) {
        return new elements.HoverSpan(text);
    }
    
}

class Global {
    
    themeButton: elements.IconButton
    app: elements.App
    
    constructor() {
        let themeButtonIcon = "";
        if (window.localStorage.getItem("theme") == "light") {
            themeButtonIcon = "/storage/images/moon.png";
            
        } else {
            themeButtonIcon = "/storage/images/sun.png";
        }
        this.themeButton = new elements.IconButton(themeButtonIcon, 7, "");
        this.app = new elements.App();
    }
    
}

class Zlogin {
    
    page: elements.Page
    container: elements.VerticalContainer
    bar: elements.HorizontalContainerNoBg
    userInput: elements.Input
    passwordInput: elements.Input
    label: elements.Label
    button: elements.Button
    
    constructor() {
        this.page = new elements.Page();
        this.container = new elements.VerticalContainer("400px", "200px", "center", "center");
        this.bar = new elements.HorizontalContainerNoBg("", "", "center", "center");
        this.userInput = new elements.Input("Usuário", "text", "70%", "30px");
        this.passwordInput = new elements.Input("Senha", "password", "70%", "30px");
        this.label = new elements.LabelBold("Login");
        this.button = new elements.Button("Acessar", "blue");
    }
    
}

class Zindex {
    
    page: elements.Page
    titleBar: elements.HorizontalContainer
    menuButton: elements.IconButton
    userName: elements.Label
    logoutButton: elements.IconButton
    menu: elements.LeftMenu
    module: elements.VerticalContainerNoBg
    themeButtonContainer: elements.HorizontalContainerNoBg
    
    constructor() {
        let menuButtonIcon = "";
        if (window.localStorage.getItem("theme") == "light") {
            menuButtonIcon = "/storage/images/menu_light.png";
            
        } else {
            menuButtonIcon = "/storage/images/menu_dark.png";
        }
        this.page = new elements.Page();
        this.titleBar = new elements.HorizontalContainer("100%", "50px", "center", "");
        this.themeButtonContainer = new elements.HorizontalContainerNoBg("100%", "100%", "center", "end");
        this.menuButton = new elements.IconButton(menuButtonIcon, 5, "");
        this.userName = new elements.Label("");
        this.logoutButton = new elements.IconButton("/storage/images/logout.png", 5, "red");
        this.menu = new elements.LeftMenu();
        this.module = new elements.VerticalContainerNoBg("100%", "calc(100vh - 50px", "center", "center");
    }
    
}