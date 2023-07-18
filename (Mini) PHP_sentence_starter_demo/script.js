$(document).on('click', '.btn-rus', function() {
    $(this).closest('.sentence.rus').next('.sentence.eng').css('display', function(_, value) {
        return value === 'none' ? 'flex' : 'none';
    });
    $(this).parent().hide();
});

$(document).on('click', '.btn-eng', function() {
    $(this).closest('.sentence.eng').prev('.sentence.rus').css('display', function(_, value) {
        return value === 'none' ? 'flex' : 'none';
    });
    $(this).parent().hide();
});

$(document).ready(function() {

    let collectionCount = 1;
    $('.sentence.rus').css('display', 'flex');
    $('.sentence.eng').css('display', 'none');    

    $("#load-more").click(function() {
        $.ajax({
            type: "POST",
            url: "data.php",
            data: {
                collection_count: collectionCount
            },
            success: function(data) {
                if (data) {
                    $("#sentence-collection").html(data);
                    collectionCount += 1;
                } else {
                    console.log("Data is empty or not available.");
                    $("#load-more").hide();
                }
            }
        });
    });
});
