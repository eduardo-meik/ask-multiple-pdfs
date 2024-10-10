css = '''
<style>
/* Contenedor principal */
.chat-container {
    display: flex;
    flex-direction: column;
    height: 80vh;
    border: 1px solid #ccc;
    border-radius: 10px;
    overflow: hidden;
}

/* Barra de entrada de chat */
.chat-input {
    position: sticky;
    top: 0;
    background: #f9f9f9;
    padding: 10px;
    border-bottom: 1px solid #ccc;
    z-index: 1000;
}

/* Historial de chat */
.chat-history {
    flex: 1;
    overflow-y: auto;
    padding: 10px;
    background-color: #ffffff;
}

/* Mensajes de chat */
.chat-message {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
}

.chat-message.user {
    background-color: #dcf8c6;
    flex-direction: row-reverse;
}

.chat-message.bot {
    background-color: #ececec;
}

.chat-message .avatar {
    width: 40px;
    height: 40px;
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    max-width: 80%;
    margin: 0 10px;
    word-wrap: break-word;
    color: #000000;
}

/* Estilos adicionales */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://www.meiklabs.com/wp-content/uploads/2023/09/robot.png">
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

