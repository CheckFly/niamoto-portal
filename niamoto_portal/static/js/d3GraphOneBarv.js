'use strict'

import * as d3 from 'd3'
import d3Legend from 'd3-svg-legend'

/**
 * Represents a graph one bar.
 * @constructor
 * @param {object} configuration - configuration default constains member config.
 */

// todo diviser en 2 graphs
export class GraphOneBarV {

  /**
   * default configuration settings
   * @type {object}
   * @property {number} height - height svg.
   * @property {number} with - with svg.
   * @property {number} margin - margin svg.
   * @property {number} minValue - minimum value y.
   * @property {number} maxValue - maximum value y
   * @property {array} color  - color for rectangle
   * @property {number} transitionMs - time of transition ms
   * @property {string} container - container name
   * @property {string} title - title svg
   * @property {string} xLabel - label axis x
   * @property {string} yLabel - label axis y
   * @property {array} value - values flux
   * @property {array} legend - legend text
   * @property {array} yDomain - mininimum and maximum value y
   * @property {number} marginLeft - margin left svg default
   * @property {array} colorText - corlor text  inside rectangle
   * @property {array} yTickValue - tick value axis y
   * @property {number} typeLegend - 1 horizontale -2 verticals
   */

  config = {
    height: 200,
    width: 200,
    margin: 10,
    minValue: 0,
    maxValue: 100,
    color: ['#444', '#aaa', '#eee'],
    transitionMs: 1000,
    container: '',
    title: '',
    xLabel: '',
    yLabel: '',
    value: '',
    legend: '',
    yDomain: [0, 100],
    marginLeft: 0.15,
    colorText: ['#222', '#222', '#222'],
    yTickValue: ['0', '25', '50', '75', '100'],
    typeLegend: 2
  }

  constructor(configuration) {

    this.config = Object.assign(this.config, configuration)

    /**
     * default margin settings
     * @type {object}
     * @property {number} top
     * @property {number} right
     * @property {number} bottom
     * @property {number} left
     */
    this.margin = {
      top: this.config.height * 0.08,
      right: this.config.width * 0.00,
      bottom: this.config.height * 0.1,
      left: this.config.width * this.config.marginLeft
    }
    /**
     * height without margins
     * @type {number}
     */
    this.mheight = this.config.height - this.margin.top - this.margin.bottom
    /**
     * width without margins
     * @type {number}
     */
    this.mwidth = this.config.width - this.margin.left - this.margin.right
    /**
     * main svg
     * @type {array}
     */
    this.svg = d3.select(this.config.container).append('svg')
      .attr('width', this.config.width)
      .attr('height', this.config.height)
    /**
     * YAxis svg
     * @type {array}
     */
    this.yAxis = this.svg.append('g')
      .attr('class', 'yAxis')
      .attr('transform', 'translate(' + this.margin.left + ',' + this.margin.top + ')')

    /**
     * container element
     * @type {array}
     */
    this.g = this.svg.append('g')
      .attr('transform', 'translate(' + this.margin.left + ',' + this.margin.top + ')')

    /**
     * label svg
     * @type {array}
     */
    this.svgLabel = this.svg.append('g')
      .attr('class', 'label')

    this.svgLabel.append('text')
      .attr('class', 'yLabel')
      .attr('transform', 'rotate(-90)')
      .attr('y', 5)
      .attr('x', 0 - this.config.height * 0.5)
      .attr('dy', '.71em')
      .style('text-anchor', 'middle')
      .text(this.config.yLabel)

    /**
     * legend svg
     * @type {array}
     */
    this.svgLegend = d3.select(this.config.container + 'Legend').append('svg')
      .attr('width', this.mwidth * 1.2)
      .attr('height', this.mheight * 0.3)

    if (this.config.typeLengend === 1) {
      this.svgLegend.append('g')
        .attr('class', 'legend')
        .attr('transform', 'translate(' + this.mwidth * 0.1 + ', ' + 0 + ')')
    } else {
      this.svgLegend.append('g')
        .attr('class', 'legend')
        .attr('transform', 'translate(' + this.mwidth * 0.1 + ', ' + 0 + ')')
        .attr('dy', '.5em')
        .attr('dx', '.5em')
    }

    this.legend()
  }

  /**
   * update legend
   * @method
   */
  legend() {

    var colorScale = d3.scaleOrdinal()
      .domain(this.config.legend)
      .range(this.config.color)

    var legendColor = d3Legend.legendColor()
    if (this.config.typeLengend === 1) {
      legendColor.scale(colorScale)
        .shapeWidth(70)
        .shapeHeight(7)
        .orient('horizontal')
        .labelAlign('start')
        .labelWrap(30)
    } else {
      legendColor.shapePadding(0)
        .scale(colorScale)
        .shapeWidth(10)
        .shapeHeight(10)
    }

    this.svgLegend.select('.legend')
      .call(legendColor)
  }

  /**
   * update graph with new value
   * @method
   * @param {objet} response - json flux
   */
  update(response) {
    var data = response

    var yScale = d3.scaleLinear()
      .domain(this.config.yDomain)
      .range([this.mheight, 0])

    var yAxis = g => g
      .call(d3.axisLeft(yScale)
        .tickFormat(d => d + '%')
        .tickSizeInner(-this.mwidth)
        .tickPadding(10)
        .tickValues(this.config.yTickValue)
      )

    this.svg.selectAll('.yAxis')
      .call(yAxis)
      .select('.domain').remove()

    /**
     * function used to calculate the position
            from the top of the graph.
           add the size of each previous value
     * @func
     * @param {number} i - index data
     * @returns {number} - a number corresponding to the scale
     * @memberof GraphOneBarV
     */
    function definePosition(i) {
      if (i !== 0) {
        let height = 0
        for (let y = 0; y < i; y++) {
          height += data[y].value
        }
        return yScale(100 - height)
      } else {
        return 0
      }
    }

    /**
     * function used to calculate the position of the text
            from the top of the graph.
           add the size of each previous value
     * @func
     * @param {number} i - index data
     * @returns {number} - a number corresponding to the scale
     * @memberof GraphOneBarV
     */
    function definePositionText(i, domain) {
      let height = 0
      for (let y = i; y >= 0; y--) {
        if (y === i) {
          height += defineHeightRect(data[y], y, domain, false) / 2
        } else {
          height += data[y].value
        }
      }
      return yScale(100 - height)
    }

    /**
     * this function is used to calculate the height of each rectangle
          For the last value, we subtract the min value of the domain.
          Note that it is better that the list is ordered from the smallest to the largest
     * @func
     * @param {number} i - index data
     * @returns {number} - a number corresponding to the scale
     * @memberof GraphOneBarV
     */
    function defineHeightRect(d, i, domain, scale = true) {
      let height = 0
      if (i === data.length - 1) {
        height = d.value - domain[0]
      } else {
        height = d.value
      }
      if (scale === true) {
        return yScale(100 - height)
      } else {
        return height
      }
    }

    var rects = this.g.selectAll('rect')
      .data(data)
    rects.enter()
      .append('rect')
      .attr('class', (d, i) => this.config.value[i])
      .style('fill', (d, i) => this.config.color[i])
      .style('opacity', '1')
      .attr('width', this.mwidth * .5)
      .attr('x', this.mwidth * 0.25)
      .attr('y', (d, i) => definePosition(i))
      .attr('height', (d, i) => defineHeightRect(d, i, this.config.yDomain))
      .transition()
      .duration(500)

    rects.transition()
      .duration(500)
      .attr('y', (d, i) => definePosition(i))
      .attr('height', (d, i) => defineHeightRect(d, i, this.config.yDomain))

    rects.exit()
      .transition()
      .duration(500)
      .remove()

    var texts = this.g.selectAll('text')
      .data(data)

    texts.enter().append('text')
      .attr('class', 'label')
      .attr('text-anchor', 'middle')
      .attr('x', this.mwidth * 0.5)
      .attr('y', (d, i) => definePositionText(i, this.config.yDomain))
      .attr('dy', '.5em')
      .attr('dx', '.5em')
      .text(function (d) {
        if (d.value !== 0) {
          return d3.format('.1%')(d.value / 100)
        }
      })
      .attr('font-family', 'sans-serif')
      .attr('font-size', '20px')
      .attr('fill', (d, i) => this.config.colorText[i])
      .transition()
      .duration(500)

    texts.transition().duration(500)
      .attr('y', (d, i) => definePositionText(i, this.config.yDomain))
      .text(function (d) {
        if (d.value !== 0) {
          return d3.format('.1%')(d.value / 100)
        }
      })
      .attr('fill', (d, i) => this.config.colorText[i])

    texts.exit()
      .transition()
      .duration(500)
      .remove()
  }
}