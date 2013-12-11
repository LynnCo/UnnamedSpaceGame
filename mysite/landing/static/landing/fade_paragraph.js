//words passed as an array
function displayText(eid,writeTo)
    {
    var words = writeTo
    $.each(words.split(""),function(i,letter)
        {
        setTimeout(function()
            {
            lc = "<span>"+letter+"<span>";
            $(lc).appendTo(eid).hide().fadeIn(speed=1000);
            },20*i);
        });
    };