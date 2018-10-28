const mysql = require("mysql");

// const con = mysql.createPool({
//     connectionLimit:10,
//     host: "localhost",
//     user: "root",
//     password: "36512010Alya!",
//     database: "PracticeBase",
//     multipleStatements: true,
//     dateStrings:true
// });

const con = mysql.createPool({
    connectionLimit:10,
    host: "192.168.10.102",
    user: "root",
    password: "7QgL12psp",
    database: "PracticeBase",
    multipleStatements: true,
    dateStrings:true
});

module.exports = con;
