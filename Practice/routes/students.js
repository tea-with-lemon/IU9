var express = require('express');
var router = express.Router();
const con = require("./connection.js");


router.get('/', function (req, res) {
    con.getConnection((err,connection) => {
        if(err) throw err;
        connection.query("select * from Student",(err,results) => {
            connection.release();
            // console.log(results);
            if(err) return res.json({ok:false,msg:err.code});
            res.json({ok:true,students:results})
        })
    })
});

router.get('/find', function (req, res) {
    con.getConnection((err,connection) => {
        if(err) throw err;
        connection.query("select * from Student where LastName regexp ?",[req.query.LastName || '.'],(err,results) => {
            connection.release();
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
        connection.query("update Student set FirstName=? ,LastName=? ,FName=? , Email=? , Entrance=? , Phone=? , `Course`=? , `Group`=? where StudentID=?",[
            req.body.FirstName,
            req.body.LastName,
            req.body.FName,
            req.body.Email,
            req.body.Entrance,
            req.body.Phone,
            req.body.Course,
            req.body.Group,
            req.body.StudentID
        ],(err,results) => {
            connection.release();
            if(err) throw err;
            res.json({ok:true})
        })
    })
});

router.post('/delete',(req,res)=>{
    con.getConnection((err,connection) => {
        if(err) throw err;
        connection.query("delete from Student where StudentID=?",[
            req.body.id,
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
        connection.query("insert into Student (FirstName,LastName ,FName , Email , Entrance , Phone , BirthDate, Course,`Group`) values (?,?,?,?,?,?,date(?),?,?)",[
            req.body.FirstName,
            req.body.LastName,
            req.body.FName || null,
            req.body.Email || null,
            req.body.Entrance,
            req.body.Phone || null,
            req.body.BirthDate,
            req.body.Course || null,
            req.body.Group || null,
        ],(err,results) => {
            connection.release();
            if(err) return res.json({ok:false,msg:err.code});
            res.json({ok:true})
        })
    })
});

module.exports = router;