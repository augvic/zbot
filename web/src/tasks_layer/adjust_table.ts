import { TableControllerComponent } from "../components/table_controller";

export class AdjustTableTask {
    
    tableController: TableControllerComponent
    
    constructor(tableController: TableControllerComponent) {
        this.tableController = tableController;
    }
    
    public execute(headerPosition: number, newCell: HTMLElement, columnName: string) {
        this.tableController.columns[columnName].push(newCell);
        this.tableController.adjustWitdh(headerPosition, columnName);
    }
    
}