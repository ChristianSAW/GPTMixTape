// components/FormSection.jsx

import { useState } from "react";
import SendIcon from '@mui/icons-material/Send';

const FormSection = ({generateResponse}) => {
    const [newQuestion, setNewQuestion] = useState('');

    const getNumberOfLines = (text) => {
        const maxLines = 6;
        const lines = text.split('\n').length;
        return Math.min(lines, maxLines);
      };
      

    return (
        <div className="form-section">
            <div style={{ flexGrow: 1}}>
            <textarea
                rows={getNumberOfLines(newQuestion) || 1}
                className="form-control"
                placeholder="Ask me anything..."
                value={newQuestion}
                onChange={(e) => setNewQuestion(e.target.value)}
            ></textarea>
            </div>
            <div
                className="send-icon"
                onClick={() => generateResponse(newQuestion, setNewQuestion)}
            >
                <SendIcon />
                {/* <i className="fa-solid fa-copy"></i> */}
            </div>
            {/* <button className="btn" onClick={() => generateResponse(newQuestion, setNewQuestion)}>
                Generate Response 🤖
            </button> */}
        </div>
    )
}

export default FormSection;