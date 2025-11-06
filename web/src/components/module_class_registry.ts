import { zAdmin } from "../io/modules/zadmin.js";
import { zRegRpa } from "../io/modules/zregrpa.js";

export class ModuleRegistryComponent {
    
    public getModuleClass(moduleName: string):
    typeof zAdmin | 
    typeof zRegRpa {
        const modules: {[key: string]: any} = {
            "zAdmin": zAdmin,
            "zRegRpa": zRegRpa
        }
        return modules[moduleName];
    }
    
}
