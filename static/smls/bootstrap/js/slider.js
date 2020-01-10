
var myimg = document.getElementById('mypics');

imgarray = ['static/smls/assest/slider_1.jpg', 'static/smls/assest/slider_2.jpg', 'static/smls/assest/slider_3.jpg'];

imgindex = 0;

function changeImg(){
  myimg.setAttribute("src", imgarray[imgindex]);
  imgindex++;
  if(imgindex > imgarray.length){
    imgindex = 0;
  }
}

setInterval(changeImg, 15000)
