$(document).ready(function() {
    $.getJSON('/ping', function(data) {
        $.each(data, function(index, obj) {
            var square = $('#square-' + (index + 1));
            square.css('background-color', obj.status === 'online' ? 'green' : 'red');
            square.find('p').text(obj.ip);

            var ipLength = obj.ip.length;
            var fontSize = Math.floor(200 / ipLength) + 'px';
            square.find('p').css('font-size', fontSize);
        });
    });
});