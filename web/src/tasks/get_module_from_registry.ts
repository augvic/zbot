import { ModuleClassRegistry } from "../components/module_class_registry";

export class GetModuleFromRegistry {
    
    moduleClassRegistry!: ModuleClassRegistry
    
    private setup() {
        this.moduleClassRegistry = new ModuleClassRegistry()
    }
    
    execute(moduleName: string): any {
        this.setup();
        return this.moduleClassRegistry.get_module_class(moduleName);
    }
    
}