var refresh_rate = 10000;
var current_count = 0;
var i = 1;
var y = 1;

function start_updates(){
    
$.ajax({
    url: "/api/superfeedr/view_superfeedr_updates/",
    success: function (data, textStatus) {
       $('#updates').val(data);
    }
});

setTimeout('get_update()', refresh_rate);
      
}

function get_update(){

$.ajax({
    url: "/api/superfeedr/view_superfeedr_updates/",
    success: function (data, textStatus) {
       $('#updates').val(data);
    }
});

setTimeout('get_update()', refresh_rate);
      
}

$(document).ready(function(){
 $("form#rsssubmit").submit(function(){ 
            $.post("/api/superfeedr/add_feed_subscription/",{  
                   feed_url: $("#rss").val(),  
                 }, function(data) {  
                    $("#subbed").append("<li>"+data+"</li>");
                 
             });  
             return false; 
            
        });
});

