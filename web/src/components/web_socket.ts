import { io, Socket } from "socket.io-client";

export class WebSocketComponent {
    
    webSocket!: Socket
    
    public init() {
        this.webSocket = io(window.location.origin, {
            withCredentials: true
        });
    }
    
}