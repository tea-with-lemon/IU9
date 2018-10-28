var express = require('express');
var router = express.Router();
const pool = require("./connection.js");


router.get('/getall',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        connection.query("select * from Company",(error,result)=>{
            connection.release();
            if(error) throw error;
            res.json({companies:result})
        })
    })
});

router.get('/find',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        connection.query("select * from Company where CompanyName regexp ?",[req.query.CompanyName || '.'],(error,result)=>{
            connection.release();
            if(error) throw error;
            res.json({companies:result})
        })
    })
});

router.post('/add',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        console.log(req.body);
        connection.query("insert into Company (CompanyName , Description , Addres, Email) values (?,?,?,?)",[
            req.body.CompanyName,
            req.body.Description ,
            req.body.Addres,
            req.body.Email
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
        console.log(req.body);
        connection.query("delete from Company where CompanyName=?",[
            req.body['CompanyName']
        ],(error,result)=>{
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
    })
});

router.post('/update',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        console.log(req.body);
        connection.query("update Company set ? where CompanyName=?",[
            req.body.company,
            req.body.name
        ],(error,result)=>{
            console.log(connection.sql);
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
    })
});

module.exports = router;