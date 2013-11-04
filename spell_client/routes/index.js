
/*
 * GET home page.
 */
var redis = require('redis'),
    redis_client = redis.createClient();

exports.index = function(req, res){
    redis_client.zcard("incorrect", function(err, replies){
        incorrect_count = replies 
        redis_client.zrange("incorrect", -1, -1, function(err, replies){
            most_incorrect = replies[0]
            redis_client.zcard("new", function(err, replies){
                new_word_count = replies
                res.render('index',{incorrect_count : incorrect_count,
                    most_incorrect  : incorrect_count,
                    new_word_count  : new_word_count});
            });
        });
    });
};
