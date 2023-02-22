const express = require('express');
const http = require('http')

const app = express();
const port = 3000;

server = http.createServer(app);
io = require('socket.io')(server);

app.use(express.static('public')); //index.html 자동실행


app.get('/', (req, res) =>{
    res.send('<h2> SeSAC Talk </h2>');
});


io.sockets.on('connection', function(socket){
    socket.on('hello', (data) =>{
        io.sockets.emit('sendBroad', data);
    });
});

server.listen(port, () => {
    console.log('http://localhost:3000');
});
