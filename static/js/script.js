$(document).ready(function(){
  $('.sidenav').sidenav({edge: "right"});
  $('.tooltipped').tooltip();
  $('select').formSelect();
  $('.datepicker').datepicker({
      format: "dd mmm, yyyy",
      yearRange: 1,
      showClearBtn: true,
      autoClose: true,
      i18n: {
        done: "select"
      }
  });
});
