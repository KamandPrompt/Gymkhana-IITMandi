var newsCont = document.getElementById("news-display");

var newsRequest = new XMLHttpRequest();
newsRequest.open('GET','/news/news.json');
newsRequest.onload = function() {
  var newsData = JSON.parse(newsRequest.responseText);
  renderHTML(newsData);
};
newsRequest.send();

function renderHTML(data){
  var newsString = "";
  var x="test";
  for(i=0;i<data.length;++i){
    newsString+= "<h3>" + data[i].title + " | " + "<span>" + data[i].date + "</span>" + "</h3>";
    newsString+= "<p >" + data[i].article + "</p>" + "<br><br>";
  }

    newsCont.insertAdjacentHTML('beforeend', newsString);
}
