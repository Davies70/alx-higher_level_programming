#!/usr/bin/node


const list = '<li>Item</li>';
$(function () {
    $('#add_item').click( () => {
        $('UL.my_list').append(list);   
    });
});