var express = require('express');
var router = express.Router();
const pool = require("./connection.js");


router.get('/getall',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        connection.query("select * from Manager",(error,result)=>{
            connection.release();
            if(error) throw error;
            res.json({managers:result})
        })
    })
});

router.post('/add',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        console.log(req.body);
        connection.query("insert into Manager (Phone , Email , CompanyName, FirstName,LastName,FName) values (?,?,?,?,?,?)",[
            req.body.Phone,
            req.body.Email,
            req.body['CompanyName'] ,
            req.body.FirstName,
            req.body.LastName,
            req.body.FName
        ],(error,result)=>{
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
    })
});

router.post('/delete',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        connection.query("delete from Manager where ManagerId=?",[req.body.id],(error,result)=>{
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
    })
});

router.post('/update',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        connection.query("update Manager set ? where ManagerId=?",[req.body,req.body.ManagerID],(error,result)=>{
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
    })
});

router.get('/find', function (req, res) {
    pool.getConnection((err,connection) => {
        if(err) throw err;
        connection.query("select * from Manager where LastName regexp ?",[req.query.LastName || '.'],(err,results) => {
            connection.release();
            // console.log(results);
            if(err) return res.json({ok:false,msg:err.code});
            res.json({ok:true,managers:results})
        })
    })
});

module.exports = router;