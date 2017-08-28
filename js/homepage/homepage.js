import ol from 'openlayers';
import {getDefaultMap, makeGeoJSONLayer, Popup} from '../map_utils';

var map = getDefaultMap();
map.setTarget('map');

function hidePreloader() {
    document.getElementById('preloader').style.display = 'none';
};

$(document).ready(function() {
    // Load data
    var nb_layer_loaded = 0;
    $.ajax({
        type: 'GET',
        url: rapid_inventories_url,
        success: function (result) {
            let rapid_inventories_geojson = result.results;
            addInventoriesLayer(
                rapid_inventories_geojson,
                '#e2bc15',
                '#fff1ae'
            );
            nb_layer_loaded += 1;
            if (nb_layer_loaded == 2) {
                hidePreloader();
            }
        }
    });
    $.ajax({
        xhr: function () {
            var xhr = new window.XMLHttpRequest();
            xhr.addEventListener("progress", function (evt) {
                if (evt.lengthComputable) {
                    let progr = (evt.loaded / evt.total * 100).toFixed(1);
                    progress_bar.setValue(progr);
                    progress_bar.setLabel(progr + "%");
                }
            }, false);
            return xhr;
        },
        type: 'GET',
        url: taxa_inventories_url,
        success: function (result) {
            let taxa_inventories_geojson = result.results;
            addInventoriesLayer(
                taxa_inventories_geojson,
                '#e25515',
                '#d67f57'
            );
            nb_layer_loaded += 1;
            if (nb_layer_loaded == 2) {
                hidePreloader();
            }
        }
    });

    function addInventoriesLayer(inventories_geojson,
                                 fill_color, stroke_color) {
        // Create and add massif layer
        let inventories_layer = makeGeoJSONLayer(
            inventories_geojson, {
                style: new ol.style.Style({
                    image: new ol.style.Circle({
                        radius: 5,
                        fill: new ol.style.Fill({
                            color: fill_color
                        }),
                        stroke: new ol.style.Stroke({
                            color: stroke_color,
                            width: 1
                        }),
                    })
                })
        });
        map.addLayer(inventories_layer);
        let hover_interaction = new ol.interaction.Select({
            condition: ol.events.condition.pointerMove,
            layers: [inventories_layer],
            updateWhileInteracting: true,
            style: new ol.style.Style({
                image: new ol.style.Circle({
                    radius: 6,
                    fill: new ol.style.Fill({
                        color: "#66a3ff"
                    }),
                    stroke: new ol.style.Stroke({
                        color: "#cce0ff",
                        width: 2
                    }),
                })
            })
        });
        map.addInteraction(hover_interaction);
        addPopupOverlay(inventories_layer);
    };

    function addPopupOverlay(layer) {
        let popup = new Popup({
            'positioning': 'bottom-center',
            'autoPan': true,
            'autoPanAnimation': {
                'duration': 250
            }
        });
        map.addOverlay(popup);
        let point_select = new ol.interaction.Select({
            'condition': ol.events.condition.click,
            'layers': [layer],

        });
        point_select.on('select', function(evt) {
            let selection = point_select.getFeatures();
            if (selection.getLength() > 0) {
                let point = selection.item(0);
                let coord = point.getGeometry().getCoordinates();
                let title = point.get('observer_full_name');
                let content = point.get('inventory_date')
                        + ' - '
                        + point.get('location_description');
                popup.show(
                    coord,
                    title,
                    content
                );
            } else {
                popup.hide();
            }
        });
        $('.olext-popup-closer').click(function() {
            point_select.getFeatures().clear();
        });
        map.addInteraction(point_select);
    };
});
