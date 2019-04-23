$(document).ready(
    $("#share").click(function() {
        $('#share-form').show()
        $('#to-share-choices').hide()
    }),
    $("#no-share").click(function() {
        location.href='/'
    }),
    console.log("ready!")
);