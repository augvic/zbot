import { zAdmin } from "./src/io/modules/zadmin"
import { zRegRpa } from "./src/io/modules/zregrpa"
import { MakeRequest } from "./src/tasks/make_request"
import { RequestHandler } from "./src/components/request_handler"

class CompositionRoot {
    
    requestHandler!: RequestHandler
    makeRequest!: MakeRequest
    
    constructor() {
        this.initComponents();
        this.initTasks();
        this.initIo();
    }
    
    private initComponents() {
        this.requestHandler = new RequestHandler();
    }
    
    private initTasks() {
        this.makeRequest = new MakeRequest(
            this.requestHandler
        )
    }
    
    private initIo() {
        const modules: {[key: string]: any} = {
            "zAdmin": zAdmin,
            "zRegRpa": zRegRpa
        }

    }
    
}