export class TableControllerComponent {
    
    columns: {[key: string]: HTMLElement[]}
    
    constructor(columns: {[key: string]: HTMLElement[]}) {
        this.columns = columns;
    }
    
    public adjustWitdh(headerPosition: number, columnName: string) {
        const header = document.getElementById(`header-${headerPosition}`)!;
        let width = header.offsetWidth;
        this.columns[columnName].forEach(cell => {
            if (cell.offsetWidth > width) {
                width = cell.offsetWidth;
            }
        });
        this.columns[columnName].forEach(cell => {
            cell.style.width = width + "px";
        });
        header.style.width = width + "px";
    }
    
}