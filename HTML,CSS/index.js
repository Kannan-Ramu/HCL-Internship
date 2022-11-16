function slideleft(){
    document.querySelector('.three-column-images1').style.transform="translateX(0px)";
}
function slideright(){
    document.querySelector('.three-column-images1').style.transform="translateX(-8000px)";
}
document.querySelector(".menu-btn").addEventListener("click", abc);
function abc() {
  document.querySelector(".main-menu").classList.toggle("show");
 if( document.querySelector(".smallbody").style.display=="none"){
  document.querySelector(".smallbody").style.display="block";
  document.querySelector(".footer").style.display="block";
 }
 else{
  document.querySelector(".smallbody").style.display="none";
  document.querySelector(".footer").style.display="none";
 }

}
function movetologin(){
document.querySelector(".REGISTER").style.display="none";
document.querySelector(".LOGIN").style.display="block";
}
function movetoregister(){
  document.querySelector(".REGISTER").style.display="block";
  document.querySelector(".LOGIN").style.display="none";
  }