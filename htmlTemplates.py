css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.65rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: 0.125rem solid #39c0ed
}
.chat-message.bot {
    background-color: 0.125rem solid #bfbfbf
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
  color: #fff;
}
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
