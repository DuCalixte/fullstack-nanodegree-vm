//'use strict';

define([],function() {
    var data = {
        url: 'http://ec2-52-36-126-192.us-west-2.compute.amazonaws.com'
    };
    return{
    	$get: function() {
        	return {
            	url: data['url']
        	}
    	}
	}
});
