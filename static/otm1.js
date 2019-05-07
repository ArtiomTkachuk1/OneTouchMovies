var v3key="2b74b570522df71a473c99f27febe37f";
var v4key="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYjc0YjU3MDUyMmRmNzFhNDczYzk5ZjI3ZmViZTM3ZiIsInN1YiI6IjVjZDA1MWEyMGUwYTI2MjdhYTAxNWY2OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.A--UkTPY6IN7McdEjPYvGiy6yGoOFLprLYn1P1KfkbQ";


var s=document.getElementById("data").innerHTML;
document.getElementById("data").innerHTML="";
s=JSON.parse(s);
for(var i=0;i<s.length;i++){
	while(s[i].length<7)
		s[i]="0"+s[i];
}

/*var request = new XMLHttpRequest()
request.open('GET',
			"https://api.themoviedb.org/3/find/tt"+"0816692"+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[i]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request.send();*/


var request0 = new XMLHttpRequest()
request0.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[0]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request0.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[0]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request0.send();

var request1 = new XMLHttpRequest()
request1.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[1]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request1.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[1]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request1.send();
var request2 = new XMLHttpRequest()
request2.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[2]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request2.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[2]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request2.send();
var request3 = new XMLHttpRequest()
request3.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[3]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request3.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[3]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request3.send();
var request4 = new XMLHttpRequest()
request4.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[4]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request4.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[4]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request4.send();
var request5 = new XMLHttpRequest()
request5.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[5]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request5.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[5]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request5.send();

var request6 = new XMLHttpRequest()
request6.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[6]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request6.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[6]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request6.send();
var request7 = new XMLHttpRequest()
request7.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[7]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request7.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[7]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request7.send();
var request8 = new XMLHttpRequest()
request8.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[8]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request8.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[8]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request8.send();
var request9 = new XMLHttpRequest()
request9.open('GET',
			"https://api.themoviedb.org/3/find/tt"+s[9]+
			"?api_key="+v3key+"&language=en-US&external_source=imdb_id"
			, true);
 
request9.onload = function () {
	var data = JSON.parse(this.response);
	var maindiv=document.getElementById("root");
	var titlediv=document.createElement("div");
	titlediv.className="titlediv";
	titlediv.innerHTML=data.movie_results[0].title;
	maindiv.appendChild(titlediv);
	maindiv.innerHTML+="<a href="+
	"https://www.imdb.com/title/tt"+s[9]+"/"+"><img src="+
	"https://image.tmdb.org/t/p/w500"+data.movie_results[0].poster_path+" ></a><hr color="+"red"+">";
}


request9.send();