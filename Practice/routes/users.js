var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('/user', function(req, res) {
    res.json({msg:'Hello, user'});
});

module.exports = router;
