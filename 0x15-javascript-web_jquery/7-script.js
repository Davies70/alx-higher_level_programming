#!/usr/bin/node

const url = "https://swapi-api.hbtn.io/api/people/5/?format=json;"

$(function() {
    $.get(url, function(data, status) {
        $('#character').text(data.name);
    });
});