package com.dailycode.chat_app;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
@Service
public class WebSocketSessionManager {
    private final ArrayList<String> activeUsernames = new ArrayList<>();
    private final SimpMessagingTemplate messagingTemplate;
    @Autowired
    public WebSocketSessionManager(SimpMessagingTemplate messagingTemplate){
        this.messagingTemplate = messagingTemplate;
    }
    public void addUsername(String username) {
        if (!activeUsernames.contains(username)) {
            activeUsernames.add(username);
        }
    }
    public void removeUsername(String username) {
        activeUsernames.removeIf(user -> user.equals(username));
    }
    public void broadcastActiveUsernames(){
        messagingTemplate.convertAndSend("/topic/users", activeUsernames);
        System.out.println("Broadcasting active users to /topic/users" + activeUsernames);
    }
    public boolean isUsernameTaken(String username) {
        return activeUsernames.contains(username);
    }
}
