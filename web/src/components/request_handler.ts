class RequestHandler {
    
    public async post<T>(endPoint: string, contentType: string, data: T): Promise<{ success: boolean, message: string, data: any }> {
        const response = await fetch(`${window.location.origin}${endPoint}`, {
            method: "POST",
            headers: { "Content-Type": contentType },
            body: JSON.stringify(data)
        });
        return await response.json() as { success: boolean, message: string, data: any };
    }
    
}
