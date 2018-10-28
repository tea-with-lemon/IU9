var express = require('express');
var router = express.Router();
const pool = require("./connection.js");


router.get('/getall',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        connection.query("select * from Practice",(error,result)=>{
            connection.release();
            if(error) throw error;
            res.json({practice:result})
        })
    })
});

router.post('/update',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        console.log(req.body);
        let query = connection.query("update Practice set ? where TreatmentNumber=?",[req.body.practice,req.body.number],(error,result)=>{
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
        console.log(query.sql)
    })
});

router.post('/delete',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        connection.query("delete from Practice where TreatmentNumber=?",[req.body.number],(error,result)=>{
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
    })
});

router.post('/add',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        console.log(req.body);
        connection.query("insert into Practice (TreatmentNumber , StartDate , EndDate, Mark,RecomendedMark,Task,Report,Student,Head,ManagerCompany,ManagerBMSTU) values (?,?,?,?,?,?,?,?,?,?,?)",[
            req.body.TreatmentNumber ,
            req.body.StartDate ,
            req.body.EndDate,
            req.body.Mark,
            req.body.RecomendedMark,
            req.body.Task,
            req.body.Report,
            req.body.Student,
            req.body.Head,
            req.body.ManagerCompany,
            req.body.ManagerBMSTU
        ],(error,result)=>{
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
    })
});

module.exports = router;