$(document).ready(function () {
    const chatWindow = $("#chat-window");
    const chatForm = $("#chat-form");

    function appendMessage(message, className) {
        const messageElement = $(`<div class="chat-message ${className}">${message}</div>`);
        chatWindow.append(messageElement);
        chatWindow.scrollTop(chatWindow[0].scrollHeight);
    }

    chatForm.on('submit', function (event) {
        event.preventDefault();
        const userMessage = $('#chat-input').val();

        if (userMessage.trim() !== '') {
            appendMessage(userMessage, 'user-message');
            $('#chat-input').val('');

            $.ajax({
                type: 'POST',
                url: '/message',
                data: {message: userMessage},
                success: function (response) {
                    if (response.status === 'success') {
                        appendMessage(response.message, 'assistant-message');
                    } else {
                        appendMessage('Error: Unable to get response from ChatGPT.', 'assistant-message');
                    }
                },
                error: function () {
                    appendMessage('Error: Unable to connect to server.', 'assistant-message');
                }
            });
        }
    });
});
