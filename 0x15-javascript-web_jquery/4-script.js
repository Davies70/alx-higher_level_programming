#!/usr/bin/node

$(function () {
$('#toggle_header').click( () => {
    $('header').toggleClass('red green');
});
});