/**
 * Created by quxl on 16/1/20.
 */
$(function(){
　var arr = $("pre").html().split("\n");
  var text = "<ol>";
  for(var i=0;i<arr.length;i++){
    text += "<li>"+ arr[i] +"</li>";
  }
  text += "</ol>";
  console.info(text)
  $("pre").html(text);

});