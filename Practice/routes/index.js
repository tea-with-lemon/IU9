var express = require('express');
var router = express.Router();
const con = require("./connection.js");

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/test', function (req, res) {
    con.getConnection(function (err,connection) {
        if(err) throw err;
        console.log("connected");
        connection.query("select User , plugin from mysql.user",function (err, result) {
            connection.release();
            if(err) throw err;
            console.log(result);
            res.json({data:result})
        })
    })
});

module.exports = router;
