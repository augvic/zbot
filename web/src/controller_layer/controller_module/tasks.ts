import { MakeRequestTask } from "../../tasks_layer/make_request_module";
import { AdjustTableTask } from "../../tasks_layer/adjust_table";
import { Components } from "./components";

export class Tasks {
    
    makeRequestTask: MakeRequestTask
    adjustRegistrationsTableTask: AdjustTableTask
    components: Components
    
    constructor(components: Components) {
        this.components = components;
        this.makeRequestTask = new MakeRequestTask(
            this.components.requestHandlerComponent
        );
        this.adjustRegistrationsTableTask = new AdjustTableTask(
            this.components.registrationsTableController
        );
    }
    
}
