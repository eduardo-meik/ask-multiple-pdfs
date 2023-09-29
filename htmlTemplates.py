css = '''
<style>
/* Your existing styles... */
.chat-message {
    padding: 1.5rem; border-radius: 0.65rem; margin-bottom: 1rem; display: flex;
}

.chat-message.user {
    background-color: #E3E3E3;
    flex-direction: row-reverse;
}

.chat-message.bot {
    background-color: #D4D4D4;
}

.chat-message .avatar {
  width: 20%;
}

.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #000000;
}

/* New styles for chat positioning */
.chat-history {
    max-height: calc(100vh - 120px); /* Adjust based on the estimated height of the input */
    overflow-y: auto;
}

.chat-input {
    position: sticky;
    bottom: 10px;
    background: white;
    padding: 10px 0;
    border-top: 1px solid #ccc;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://www.meiklabs.com/wp-content/uploads/2023/09/robot.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.meiklabs.com/wp-content/uploads/2023/09/profile.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
