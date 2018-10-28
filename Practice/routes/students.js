var express = require('express');
var router = express.Router();
const con = require("./connection.js");


router.get('/', function (req, res) {
    con.getConnection((err,connection) => {
        if(err) throw err;
        connection.query("select * from Student",(err,results) => {
            // console.log(results);
            if(err) return res.json({ok:false,msg:err.code});
            res.json({ok:true,students:results})
        })
    })
});

router.post('/update',(req,res)=>{
    con.getConnection((err,connection) => {
        if(err) throw err;
        console.log(req.body);
        connection.query("update Student set FirstName=? ,LastName=? ,FName=? , Email=? , Entrance=? , Phone=? where StudentID=?",[
            req.body.FirstName,
            req.body.LastName,
            req.body.FName,
            req.body.Email,
            req.body.Entrance,
            req.body.Phone,
            req.body.StudentID
        ],(err,results) => {
            connection.release();
            if(err) return res.json({ok:false,msg:err.code});
            res.json({ok:true})
        })
    })
});

router.post('/addstudent',(req,res)=>{
    con.getConnection((err,connection) => {
        if(err) throw err;
        console.log(req.body);
        connection.query("insert into Student (FirstName,LastName ,FName , Email , Entrance , Phone , BirthDate) values (?,?,?,?,?,?,date(?))",[
            req.body.FirstName,
            req.body.LastName,
            req.body.FName || null,
            req.body.Email || null,
            req.body.Entrance,
            req.body.Phone || null,
            req.body.BirthDate
        ],(err,results) => {
            connection.release();
            if(err) return res.json({ok:false,msg:err.code});
            res.json({ok:true})
        })
    })
});

module.exports = router;