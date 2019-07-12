/* Vanilla Javascript */



/* Jquery */
/* Mobile Navigation Class */

$(document).ready(function() {
 $('.sidenav').sidenav();
 $('.tooltipped').tooltip();
 $('select').formSelect();

 var clicks = 0;
 $("#like").click(function() {
  clicks++;
  $('.figure').html(clicks);
 });
});
