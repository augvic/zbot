class MakeRequest {
    
    requestHandler!: RequestHandler
    
    constructor(requestHandler: RequestHandler) {
        this.requestHandler = requestHandler;
    }
    
    public async execute<T>(endPoint: string, contentType: string, data: T): Promise<{ success: boolean, message: string, data: any }> {
        return await this.requestHandler.post(endPoint, contentType, data);
    }
    
}