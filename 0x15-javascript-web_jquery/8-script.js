#!/usr/bin/node

const url =  'https://swapi-api.hbtn.io/api/films/?format=json';

$.getJSON(url, function(movies){
    $.each(movies.results, function(i, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');  
    });
});