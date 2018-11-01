document.onreadystatechange = function () {
  if(document.readyState === "complete"){
    document.getElementById('wrap').style.display = 'block';
    document.getElementById('loader').style.display = 'none';
  }
}
