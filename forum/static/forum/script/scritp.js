  $("#showModal").click(function() {
  $(".modal").addClass("is-active"); 
  console.log("click") 
});

$(".modal-close").click(function() {
   $(".modal").removeClass("is-active");
});
