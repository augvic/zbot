export class LoadWebApp {
    
    static async execute() {
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
        const response = await fetch(`${window.location.origin}/login`);
        const data = await response.json();
        let bundle = null;
        let bundleClass = null;
        if (data.logged_in) {
            bundle = await import(`${window.location.origin}/page-bundle/zindex.js`);
        } else {
            bundle = await import(`${window.location.origin}/page-bundle/zlogin.js`);
        }
        bundleClass = bundle.default;
        document.body.innerHTML = "";
        new bundleClass();
    }
    
}
