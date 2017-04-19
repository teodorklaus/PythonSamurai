/**
 * Created by Ihor on 26.03.2017.
 */
    var map;
    function initMap() {
        var LAT_DEFAULT = 12;
        var LNG_DEFAULT = 12;
            map = new google.maps.Map(
                $('#map')[0], {
                center: {lat: LAT_DEFAULT , lng:  LNG_DEFAULT},
                zoom: 13
        });

    }
