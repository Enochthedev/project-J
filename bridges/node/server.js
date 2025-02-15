const express = require('express');
const { exec } = require('child_process');

const app = express();

app.get('/run-python', (req, res) => {
    exec('python3 ../backend/core.py', (error, stdout, stderr) => {
        if (error) return res.status(500).send(stderr);
        res.send(stdout);
    });
});

app.listen(4000, () => console.log('Node.js API running on port 4000'));
