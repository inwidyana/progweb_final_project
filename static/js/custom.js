$('#search-input').keyup(function() {
    if($('#search-input').val()) {
        $('#suggestion-dropdown').html('');
        $.ajax({
            'url': '/search/book?q=' + $('#search-input').val(),
            'dataType': 'json',
            'method': 'GET',
            'success': function (data, status) {
                $.each(data.items, function(index, value) {
                    $('#suggestion-dropdown').append(''+
                        '<a class="dropdown-item" href="/book?q=' + value.id + '">' + value.volumeInfo.title + '</a>'
                    );
                })
            }
        });
    }
});

if($('#book-suggestion').length) {
    $.ajax({
        'url': '/search/book?q=' + $('#book-title').html().split(' ')[0],
        'dataType': 'json',
        'method': 'GET',
        'success': function (data, status) {
            $.each(data.items, function(index, value) {
                $('#book-suggestion').append(''+
                    '<div class="col col-md-auto">' +
                        '<a href="/book?q=' + value.id + '">' +
                        '<img src="' + value.volumeInfo.imageLinks.thumbnail + '">' +
                        '</a>' +
                    '</div>'
                );

                if(index === 4) {
                    return;
                }
            })
        }
    });
}

if($('#weather').length) {
    $.ajax({
        'url': '/weather/get',
        'dataType': 'json',
        'method': 'GET',
        'success': function (data, status) {
            $('#weather').html('' +
                'It\'s currently ' + Math.round(((data.data[0].temperature - 32) * 5) / 9) + 'C' +
            '')
            $('#weather').css('visibility', 'visible');
        }
    });
}