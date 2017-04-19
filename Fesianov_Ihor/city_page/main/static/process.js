/**
 * Created by Ihor on 26.03.2017.
 */
$(function () {
    $("#get_info").click(function (event) {

        showLoader = function () {
            $('#loader').removeClass('hide');
        };

        hideLoader = function () {
            $('#loader').addClass('hide');
        };

        postWeatherInfo = function (data) {
            $('#info').empty();
            var weather = data.weather_info;
            for (var key in weather) {
                property = '<h3>' + key + ':</h3>';
                value = '<p>' + weather[key] + '</p>';
                $('#info').append(property + value);
                $('#weather').removeClass('hide');
            }
        };

        postPhotos = function (data) {
            $("#urls").empty();
            data.pictures_urls.forEach(function (url) {
                img = '<img src=' + url + '>';
                $('#urls').append(img);
                $('#pictures').removeClass('hide');

            });
        };

        postMap = function (data) {
            $('#map').removeClass('hide');
            map.setCenter(new google.maps.LatLng(data.coord.lat, data.coord.lon));
            google.maps.event.trigger(map, 'resize');
        };

        showLoader();

        $.ajax({
            data: {
                city_name: $('#city_name').val()
            },
            type: 'POST',
            url: '/process'
        })
            .done(function (data) {
                hideLoader();

                console.log(data);

                postWeatherInfo(data);
                postPhotos(data);
                postMap(data);
            });

        event.preventDefault();
    });
});