export class RequestHandler {
    
    public async post<T>(endPoint: string, contentType: string, data: T): Promise<{ success: boolean, message: string, data: any }> {
        const response = await fetch(`${window.location.origin}${endPoint}`, {
            method: "POST",
            headers: { "Content-Type": contentType },
            body: JSON.stringify(data)
        });
        return await response.json() as { success: boolean, message: string, data: any };
    }
    
    public async get(endPoint: string): Promise<{ success: boolean, message: string, data: any }> {
        const response = await fetch(`${window.location.origin}${endPoint}`, {
            method: "GET"
        });
        return await response.json() as { success: boolean, message: string, data: any };
    }
    
    public async delete(endPoint: string): Promise<{ success: boolean, message: string, data: any }> {
        const response = await fetch(`${window.location.origin}${endPoint}`, {
            method: "DELETE"
        });
        return await response.json() as { success: boolean, message: string, data: any };
    }
    
    public async put<T>(endPoint: string, contentType: string, data: T): Promise<{ success: boolean, message: string, data: any }> {
        const response = await fetch(`${window.location.origin}${endPoint}`, {
            method: "PUT",
            headers: { "Content-Type": contentType },
            body: JSON.stringify(data)
        });
        return await response.json() as { success: boolean, message: string, data: any };
    }
    
}
