import { Icon } from "./icon";

export class ThemeButton {
    
    element!: HTMLElement
    icon!: Icon
    
    constructor(appendTo: HTMLElement, right: boolean) {
        this.createSelf(right);
        this.createComponents();
        this.startListeners();
        appendTo.appendChild(this.element);
    }
    
    private createSelf(right: boolean) {
        this.element = document.createElement("button");
        this.element.className = "cursor-pointer w-auto h-auto rounded-md transition-colors duration-300 hover:bg-gray-300 dark:hover:bg-gray-900 absolute ml-25 transition-colors duration-300";
        if (right) {
            this.element.classList.add("absolute");
            this.element.classList.add("right-3");
        }
    }
    
    private createComponents() {
        let iconSrc = "";
        if (window.localStorage.getItem("theme") == "light") {
            iconSrc = "/storage/images/moon.png";
        } else {
            iconSrc = "/storage/images/sun.png";
        }
        this.icon = new Icon(this.element, "", iconSrc, "7");
    }
    
    private startListeners() {
        this.element.addEventListener("click", () => {
            const menuIcon = document.getElementById("menu-icon")! as HTMLImageElement;
            if (document.documentElement.classList.contains("light")) {
                document.documentElement.classList.remove("light");
                document.documentElement.classList.add("dark");
                window.localStorage.setItem("theme", "dark");
                this.icon.element.src = "/storage/images/sun.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
                menuIcon.src = "/storage/images/menu_dark.png";
                menuIcon.classList.remove("opacity-fade-in");
                void menuIcon.offsetWidth;
                menuIcon.classList.add("opacity-fade-in");
            } else {
                document.documentElement.classList.remove("dark");
                document.documentElement.classList.add("light");
                window.localStorage.setItem("theme", "light");
                this.icon.element.src = "/storage/images/moon.png";
                this.icon.element.classList.remove("opacity-fade-in");
                void this.icon.element.offsetWidth;
                this.icon.element.classList.add("opacity-fade-in");
                menuIcon.src = "/storage/images/menu_light.png";
                menuIcon.classList.remove("opacity-fade-in");
                void menuIcon.offsetWidth;
                menuIcon.classList.add("opacity-fade-in");
            }
        });
    }
    
}
