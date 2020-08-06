var express = require('express');
var router = express.Router();



/* GET users listing. */
router.post('/', function(req, res, next) {
  res.send(JSON.stringify(req.body, null, 4));
 // res.send('respond with a resource!!!'+ JSON.stringify(req.body));
  console.log(JSON.stringify(req.body));
});

module.exports = router;
