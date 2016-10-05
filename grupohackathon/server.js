var express = require('express');
var app = express();
var bodyParser =require('body-parser');

app.use(bodyParser.urlencoded() );

var port = process.env.PORT || 80;

app.get ('/', function(rec,res) {
	res.send("hahaha...")
});

app.listen(port,function() {
	console.log("Running server...");
}