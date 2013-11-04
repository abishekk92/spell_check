
/**
 * Module dependencies.
 */

var express = require('express');
var routes = require('./routes');
var path = require('path');
var app = express(),
    server = require('http').createServer(app),
    io = require('socket.io').listen(server);

var redis = require('redis'),
    redis_client = redis.createClient(); 


redis_client.on("pmessage", function(pattern,count,message){
    io.sockets.on('connection',function(socket){
        console.log({channel: count,
                 count: message});
        socket.emit('count',{channel: count,
                          count: message});
        });
});

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.bodyParser());
app.use(express.methodOverride());
app.use(app.router);
app.use(require('stylus').middleware(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'public')));

// development only
if ('development' == app.get('env')) {
    app.use(express.errorHandler());
}

app.get('/', routes.index);

redis_client.psubscribe("*_count");
server.listen(app.get('port'), function(){
    console.log('Express server listening on port ' + app.get('port'));
});