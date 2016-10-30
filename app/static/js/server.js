var app = require('http').createServer(handler),
io = require('socket.io').listen(app),
parser = new require('xml2json'),
fs = require('fs');

// creating the server ( localhost:8000 )
app.listen(8000, function(){
  console.log('litening on 8000')
});

// on server started we can load our client.html page
function handler(req, res) {
fs.readFile(__dirname + '/node.html', function(err, data) {
    if (err) {
        console.log(err);
        res.writeHead(500);
        return res.end('Error loading node.html');
    }
    res.writeHead(200);
    res.end(data);
});
}

// // File watcher
// io.sockets.on('connection', function(socket) {
// console.log(__dirname);
// // watching the xml file
// fs.watch(__dirname + '/cache/file.xml', function(curr, prev) {
//     // on file change we can read the new xml
//     fs.readFile(__dirname + '/cache/file.xml', function(err, data) {
//         if (err) throw err;
//         // parsing the new xml data and converting them into json file
//         var json = parser.toJson(data);
//         // adding the time of the last update
//         json.time = new Date();
//         // send the new data to the client
//         socket.volatile.emit('file', json);
//     });
// });
// });
