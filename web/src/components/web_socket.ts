import { io, Socket } from "socket.io-client";

export class WebSocketComponent {
    
    webSocket!: Socket
    connected!: boolean
    
    constructor() {
        this.connected = false;
    }
    
    public init() {
        this.webSocket = io(window.location.origin, {
            withCredentials: true
        });
        this.connected = true;
    }
    
    public disconnect() {
        this.webSocket.disconnect();
        this.connected = false;
    }
    
}
