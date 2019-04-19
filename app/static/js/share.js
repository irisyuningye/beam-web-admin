$(document).ready(
    $("#share").click(function() {
        $('#share-form').show()
    }),
    $("#no-share").click(function() {
        location.href='/'
    }),
    console.log("ready!")
);