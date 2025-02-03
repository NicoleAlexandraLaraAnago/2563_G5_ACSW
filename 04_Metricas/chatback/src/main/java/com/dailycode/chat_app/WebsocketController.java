package com.dailycode.chat_app;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Controller;
@Controller
public class WebsocketController {
    private final SimpMessagingTemplate messagingTemplate;
    private final WebSocketSessionManager sessionManager;
    @Autowired
    public WebsocketController(SimpMessagingTemplate messagingTemplate,  WebSocketSessionManager sessionManager) {
        this.sessionManager = sessionManager;
        this.messagingTemplate = messagingTemplate;
    }
    @MessageMapping("/message")
    public void handleMessage(com.dailycode.chat_app.Message message) {
        System.out.println("Received message from user: " + message.getUser() + ": " + message.getMessage());
        messagingTemplate.convertAndSend("/topic/messages", message);
        System.out.println("Sent message to /topic/messages: " + message.getUser() + ": " + message.getMessage());
    }
    @MessageMapping("/connect")
    public void connectUser(String username) {
        System.out.println("Handling connection for username: " + username); // Añadir log aquí
        if (sessionManager.isUsernameTaken(username)) {
            messagingTemplate.convertAndSend("/topic/connection-error", "Username '" + username + "' is already in use.");
            System.out.println("Connection rejected: " + username + " is already in use.");
            return;
        }
        sessionManager.addUsername(username);
        sessionManager.broadcastActiveUsernames();
        System.out.println(username + " connected");
    }
    @MessageMapping("/disconnect")
    public void disconnectUser(String username) {
        sessionManager.removeUsername(username); // Remover usuario
        messagingTemplate.convertAndSend("/topic/disconnected-users", username); // Notificar desconexión
        sessionManager.broadcastActiveUsernames(); // Actualizar usuarios activos
        System.out.println(username + " disconnected");
    }
    @MessageMapping("/request-users")
    public void requestUsers(){
        sessionManager.broadcastActiveUsernames();
        System.out.println("Requesting Users");
    }
}