import { zAdmin } from "../io/modules/zadmin.js";
import { zRegRpa } from "../io/modules/zregrpa.js";

export class ModuleClassRegistry {
    
    get_module_class(moduleName: string): any {
        const modules: {[key: string]: any} = {
            "zAdmin": zAdmin,
            "zRegRpa": zRegRpa
        }
        return modules[moduleName];
    }
    
}