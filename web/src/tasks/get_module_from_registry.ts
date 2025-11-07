import { ModuleRegistry } from "../components/module_class_registry";
import { zAdmin } from "../io/modules/zadmin";
import { zRegRpa } from "../io/modules/zregrpa";

export class GetModuleFromRegistry {
    
    moduleClassRegistry!: ModuleRegistry
    
    constructor(moduleRegistry: ModuleRegistry) {
        this.moduleClassRegistry = moduleRegistry;
    }
    
    public execute(moduleName: string):
    typeof zAdmin |
    typeof zRegRpa {
        return this.moduleClassRegistry.getModuleClass(moduleName);
    }
    
}