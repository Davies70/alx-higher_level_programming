#!/usr/bin/node

$(function() {
    const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    $.get(url, function(data, status){
        $('#hello').text(data.hello);
    });
});