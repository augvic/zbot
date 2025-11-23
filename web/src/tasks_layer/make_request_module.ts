import { RequestHandlerComponent } from "../components_layer/request_handler_module";

export class MakeRequestTask {
    
    requestHandler!: RequestHandlerComponent
    
    constructor(requestHandler: RequestHandlerComponent) {
        this.requestHandler = requestHandler;
    }
    
    public async post<T>(endPoint: string, contentType: string, data: T): Promise<{ success: boolean, message: string, data: any }> {
        return await this.requestHandler.post(endPoint, contentType, data);
    }
    
    public async get(endPoint: string): Promise<{ success: boolean, message: string, data: any }> {
        return await this.requestHandler.get(endPoint);
    }
    
    public async delete(endPoint: string): Promise<{ success: boolean, message: string, data: any }> {
        return await this.requestHandler.delete(endPoint);
    }
    
    public async put<T>(endPoint: string, contentType: string, data: T): Promise<{ success: boolean, message: string, data: any }> {
        return await this.requestHandler.put(endPoint, contentType, data);
    }
    
}
