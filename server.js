const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const fetch = require('node-fetch'); // For making HTTP requests in Node.js

dotenv.config(); // Load environment variables from .env file

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(cors()); // Enable CORS for all origins (adjust in production for security)
app.use(express.json()); // Parse JSON request bodies

// Proxy endpoint for Gemini API
app.post('/generate-provocation', async (req, res) => {
    const { systemPrompt, userPrompt } = req.body;
    const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
    const GEMINI_API_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=${GEMINI_API_KEY}`;

    if (!GEMINI_API_KEY) {
        return res.status(500).json({ error: 'Gemini API key not configured on the server.' });
    }

    const payload = {
        contents: [{ parts: [{ text: userPrompt }] }],
        generationConfig: {
            responseMimeType: "application/json",
            responseSchema: {
                type: "OBJECT",
                properties: {
                    "setup": { "type": "STRING" },
                    "task": { "type": "STRING" }
                },
                required: ["setup", "task"]
            }
        },
        systemInstruction: { parts: [{ text: systemPrompt }] },
    };

    try {
        const response = await fetch(GEMINI_API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const errorBody = await response.text();
            console.error('Gemini API Error Response:', errorBody);
            throw new Error(`API error: ${response.status} ${errorBody}`);
        }

        const data = await response.json();
        res.json(data); // Send the Gemini API response back to the client

    } catch (error) {
        console.error('Error proxying Gemini API request:', error);
        res.status(500).json({ error: 'Failed to generate provocation via proxy.', details: error.message });
    }
});

// Serve static files (your example.html)
app.use(express.static(__dirname));

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
    console.log('Open your browser to http://localhost:3000/example.html');
});
