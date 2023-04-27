// src/App.js
import { Configuration, OpenAIApi } from 'openai';

import FormSection from './components/FormSection';
import AnswerSection from './components/AnswerSection';

import React, { useState, useEffect } from 'react';

// import { makeStyles } from '@mui/system/make';
import Paper from '@mui/material/Paper'
import Grid from '@mui/material/Grid'
// import Box from '@mui/material/Box'
import Divider from '@mui/material/Divider'
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Avatar from '@mui/material/Avatar';
import Fab from '@mui/material/Fab';
import SendIcon from '@mui/icons-material/Send';

import "./App.css";

const App = () => {

  const [name, setName] = useState('');
  const [message, setMessage] = useState('');

  const generateResponse = async (newQuestion, setNewQuestion) => {
    const response = await fetch('api/send_user_message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ newQuestion }),
    });

    const data = await response.json();

    setStoredValues([
      {
        question: newQuestion,
        answer: data.content,
      },
      ...storedValues,
    ]);
    setNewQuestion('');
  }

  const { Configuration, OpenAIApi } = require("openai");

  const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
  });
  const openai = new OpenAIApi(configuration);

  const [storedValues, setStoredValues] = useState([]);

  return (
    <div className='app-container'>
      <div className="header-section">
        <h1>Imposter.AI 🤖</h1>
        <p>
          I am an automated question and answer system, designed to assist you
          in finding relevant information. You are welcome to ask me any queries
          you may have, and I will do my utmost to offer you a reliable
          response. Kindly keep in mind that I am a machine and operate solely
          based on programmed algorithms.
        </p>
      </div>
      <div className="content-wrapper">
        <div className="content-section">
          <AnswerSection storedValues={storedValues} />
        </div>
        <FormSection generateResponse={generateResponse} />
      </div>
    </div>
  );
};

export default App;