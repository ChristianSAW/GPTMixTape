$(document).ready(function () {
    const chatWindow = $("#chat-window");
    const systemForm = $("#system-form");
    const userForm = $("#user-form");

    function appendMessage(message, className, initials) {
        const messageElement = $(`
            <div class="chat-message ${className}">
                <div class="initials">${initials}</div>
                <div class="content">${message}</div>
            </div>
        `);
        chatWindow.append(messageElement);
        chatWindow.scrollTop(chatWindow[0].scrollHeight);
    }

    systemForm.on('submit', function(event) {
        console.log('System form submitted!');
        event.preventDefault();
        const sysMessage = $('#system-input').val();
        appendMessage(sysMessage, 'system-message', 'SYS')
        $.ajax({
            type: 'POST',
            url: '/system-message',
            data: {
                system_message: sysMessage
            },
            success: function (response) {
                if (response.status === 'success') {
                    appendMessage(response.message, 'assistant-message', 'Chat');
                } else {
                    appendMessage('Error: Unable to get response from ChatGPT.', 'assistant-message', 'Err');
                }
            },
            error: function () {
                appendMessage('Error: Unable to connect to server.', 'assistant-message', 'Err');
            }
        });
        // $('#system-input').val('');
    });

    userForm.on('submit', function(event) {
        console.log('User form submitted!');
        event.preventDefault();
        const userMessage = $('#user-input').val();
        appendMessage(userMessage, 'user-input', 'User')
        $.ajax({
            type: 'POST',
            url: '/user-message',
            data: {
                user_message: userMessage
            },
            success: function (response) {
                if (response.status === 'success') {
                    appendMessage(response.message, 'user-message', 'Chat');
                } else {
                    appendMessage('Error: Unable to get response from ChatGPT.', 'user-message', 'Err');
                }
            },
            error: function () {
                appendMessage('Error: Unable to connect to server.', 'user-message', 'Err');
            }
        });
        $('#user-input').val('');
    });
});
