import * as elements from "../io/elements";
import { Tasks } from "./tasks";

export class IO {
    
    global: Global
    zLogin: Zlogin
    zIndex: Zindex
    zAdmin: Zadmin
    
    constructor(tasks: Tasks) {
        this.global = new Global();
        this.zLogin = new Zlogin();
        this.zIndex = new Zindex();
        this.zAdmin = new Zadmin(tasks);
    }
    
    public createButton(text: string, bgColor: string, width: string, height: string) {
        return new elements.Button(text, bgColor, width, height);
    }
    
    public createNotification(message: string, color: string) {
        return new elements.Notification(message, color);
    }
    
    public createHoverSpan(text: string) {
        return new elements.HoverSpan(text);
    }
    
    public createTable(width: string, height: string, rows: [{}]) {
        return new elements.Table(width, height, rows);
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
    container: elements.Container
    bar: elements.Wrapper
    userInput: elements.Input
    passwordInput: elements.Input
    label: elements.Label
    button: elements.Button
    
    constructor() {
        this.page = new elements.Page("vertical");
        this.container = new elements.Container("vertical", "400px", "200px", "center", "center");
        this.bar = new elements.Wrapper("horizontal", "", "", "center", "center");
        this.userInput = new elements.Input("Usuário", "text", "70%", "30px");
        this.passwordInput = new elements.Input("Senha", "password", "70%", "30px");
        this.label = new elements.Label("Login", true, "lg");
        this.button = new elements.Button("Acessar", "blue", "40%", "");
    }
    
}

class Zindex {
    
    page: elements.Page
    titleBar: elements.Container
    menuButton: elements.IconButton
    userName: elements.Label
    logoutButton: elements.IconButton
    menu: elements.BlurContainer
    menuWrapper: elements.Wrapper
    module: elements.Wrapper
    themeButtonContainer: elements.Wrapper
    
    constructor() {
        let menuButtonIcon = "";
        if (window.localStorage.getItem("theme") == "light") {
            menuButtonIcon = "/storage/images/menu_light.png";
            
        } else {
            menuButtonIcon = "/storage/images/menu_dark.png";
        }
        this.page = new elements.Page("vertical");
        this.titleBar = new elements.Container("horizontal", "100%", "60px", "center", "");
        this.themeButtonContainer = new elements.Wrapper("horizontal", "100%", "100%", "center", "end");
        this.menuButton = new elements.IconButton(menuButtonIcon, 5, "");
        this.userName = new elements.Label("", false, "md");
        this.logoutButton = new elements.IconButton("/storage/images/logout.png", 5, "red");
        this.menu = new elements.BlurContainer("vertical", "300px", "calc(100vh - 60px)", "bottom", "left");
        this.menuWrapper = new elements.Wrapper("vertical", "100%", "100%", "", "")
        this.module = new elements.Wrapper("vertical", "100%", "calc(100vh - 60px)", "center", "center");
    }
    
}

class Zadmin {
    
    moduleWrapper: elements.Wrapper
    optionsContainer: elements.Container
    optionsContainerWrapper: elements.Wrapper
    viewContainer: elements.Container
    usersSection: elements.Wrapper
    usersSectionTopBar: elements.Wrapper
    searchUserInput: elements.Input
    searchUserButton: elements.IconButton
    selectUsersSectionButton: elements.Button
    usersSectionTable!: elements.Table
    
    constructor(tasks: Tasks) {
        this.mountUserTableRows(tasks);    
        this.moduleWrapper = new elements.Wrapper("horizontal", "100%", "100%", "center", "center");
        this.optionsContainer = new elements.Container("vertical", "10%", "500px", "center", "center");
        this.optionsContainerWrapper = new elements.Wrapper("vertical", "100%", "100%", "center", "center");
        this.viewContainer = new elements.Container("vertical", "85%", "90%", "center", "center");
        this.usersSection = new elements.Wrapper("vertical", "100%", "100%", "", "");
        this.usersSectionTopBar = new elements.Wrapper("horizontal", "100%", "5%", "center", "start");
        this.searchUserInput = new elements.Input("Pesquisar", "text", "300px", "30px");
        this.searchUserButton = new elements.IconButton("/storage/images/magnifying_glass.png", 5, "blue");
        this.selectUsersSectionButton = new elements.Button("Usuários", "orange", "100%", "");
        
    }
    
    private async mountUserTableRows(tasks: Tasks) {
        const usersTableRows = ((await tasks.makeRequestTask.get("/users/all")).data as [{}]);
        usersTableRows.unshift({ email: "E-mail", name: "Nome", password: "Senha", user: "Usuário" });
        this.usersSectionTable = new elements.Table("100%", "95%", usersTableRows);
    }
    
}