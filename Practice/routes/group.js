var express = require('express');
var router = express.Router();
const pool = require("./connection.js");


router.get('/getall',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        connection.query("select * from `Group` join Student on Student.StudentID=`Group`.Student order by `Group`.PracticeYear desc,`Group`.CompanyName asc",(error,result)=>{
            connection.release();
            if(error) throw error;
            res.json({groups:result})
        })
    })
});

router.post('/add',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        console.log(req.body);
        connection.query("insert into `Group` (Student , PracticeYear , CompanyName, Head) values (?,?,?,?)",[
            req.body.Student,
            req.body.PracticeYear,
            req.body['CompanyName'] ,
            req.body.Head
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
        connection.query("delete from `Group` where Student=? and PracticeYear=?",[req.body.id,req.body.year],(error,result)=>{
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
    })
});

router.post('/update',(req,res)=>{
    pool.getConnection((err,connection)=>{
        if(err) throw err;
        connection.query("update `Group` set Head=?,PracticeYear=?,CompanyName=? where Student=? and PracticeYear=?",[
            req.body.group.Head,
            req.body.group.PracticeYear,
            req.body.group.CompanyName,
            req.body.group.Student,
            req.body.year],(error,result)=>{
            connection.release();
            if(error) return res.json({ok:false,msg:error.code});
            res.json({ok:true})
        })
    })
});

module.exports = router;