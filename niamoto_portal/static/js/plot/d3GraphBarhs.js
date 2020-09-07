'use strict'

import * as d3GraphBarhSimple from '../d3GraphBarhSimple'
import * as d3Graph from '../d3Graph'
import color from '../../css/source/partials/_color_js.scss'
import * as d3 from 'd3'

export function init(data) {

    // strates
    var strates = new d3GraphBarhSimple.GraphBarhSimple({
        width: $('#stratesHisto').width(),
        height: $('#stratesHisto').height(),
        container: '#stratesHisto',
        yDomain: ['Emergent', 'Canopée', 'Sous-Canopée', 'Sous-bois'],
        value: [100, 0],
        xLabel: 'Pourcentage du peuplement (%)',
        color: [color.emerging, color.canopy, color.undercanopy, color.undergrowth],
        maxValue: '',
        yDomainShow: 0,
        marginLeft: 0.02,
        yTextDomain: 1
    })

     // speciesTop10
     var speciesTop = new d3GraphBarhSimple.GraphBarhSimple({
        width: $('#speciesTop10').width(),
        height: $('#speciesTop10').height(),
        container: '#speciesTop10',
        xLabel: 'Pourcentage du peuplement (%)',
        color: ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"],
        maxValue: '',
        yDomainShow: 0,
        marginLeft: 0.02,
        yTextDomain: 1,
        tooltip: 1
    })

    // Update Data for trigger
    $('#plot_select').on('plotSelected', function (event, data) {
        updateData(data.properties.frequencies)
    })

    function updateData(data) {

        const strate = d3Graph.dataFilter(data, 'strates')
        const strateData = d3Graph.dataJson(strate)
        strates.config.maxValue = ''
        strates.update(strateData.reverse())

        const specieTop = d3Graph.dataFilter(data, 'speciesTop10')
        const specieTopdata = d3Graph.dataJson(specieTop)
        speciesTop.config.yDomain=''
        speciesTop.config.maxValue=''
        speciesTop.update(specieTopdata)




    };
};