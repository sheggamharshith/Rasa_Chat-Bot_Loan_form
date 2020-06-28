var express = require('express');
const app = express();
var path = require('path')
const server = require('http').createServer(app);
var cors = require('cors')
const PORT = 8080;
const HOST = '127.0.0.1';
server.listen(PORT);
console.log(`Server is running on port ${PORT}`);

app.use(express.static(path.join(__dirname, 'Assets')));
app.use(cors())
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

console.log("Running on http: //${HOST}:${PORT}");