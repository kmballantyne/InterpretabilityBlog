<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';

    export let forcePlotData;

    onMount(() => {
        if (forcePlotData) {
            createForcePlot(forcePlotData);
        }
    });

    function createForcePlot(data) {
    const svg = d3.select('#forcePlot')
        .attr('width', 800)
        .attr('height', 200);  // Increased height for label spacing

    const width = 700, height = 50;
    const margin = { top: 20, right: 20, bottom: 80, left: 20 }; // Adjusted bottom for more label space
    const plotWidth = width - margin.left - margin.right;

    // Scales for width and color
    const widthScale = d3.scaleLinear()
        .domain([Math.min(...data.shap_values), Math.max(...data.shap_values)])
        .range([0, plotWidth]);

    const colorScale = d3.scaleLinear()
        .domain([Math.min(...data.shap_values), Math.max(...data.shap_values)])
        .range(["#4169E1", "#FF6347"]);  // Blue to red range

    // Clear any existing content
    svg.selectAll('*').remove();

    // Adding Rectangles
    svg.selectAll('.shap-rect')
        .data(data.shap_values)
        .enter()
        .append('rect')
        .attr('class', 'shap-rect')
        // @ts-ignore
        .attr('x', (d, i) => margin.left + i * 10) // Example: space elements evenly
        .attr('y', margin.top + 20)
        .attr('width', d => Math.abs(widthScale(d)))
        .attr('height', 20)
        .attr('fill', d => colorScale(d));

    // Adding Feature Labels (positioned below rectangles)
    svg.selectAll('.feature-label')
        .data(data.feature_names)
        .enter()
        .append('text')
        .attr('class', 'feature-label')
        .attr('x', (d, i) => {
            const rectX = margin.left + d3.sum(data.shap_values.slice(0, i).map(val => Math.abs(widthScale(val))));
            const rectWidth = Math.abs(widthScale(data.shap_values[i]));
            return rectX + rectWidth / 2;  // Center of each rectangle
        })
        // .attr('x', (d, i) => margin.left + widthScale(data.shap_values.slice(0, i).reduce((a, b) => a + b, 0)) + 5)
        .attr('y', margin.top + 100)  // Position below rectangles
        // .attr('transform', (d, i) => {
        //     const x = margin.left + widthScale(data.shap_values.slice(0, i).reduce((a, b) => a + b, 0)) + 5;
        //     return `translate(${margin.left}, ${margin.top + 100}) rotate(-15)`; // Adjust rotation as needed
        // })
        .text((d, i) => `${d} = ${data.data_point[i]}`)
        .style('text-anchor', 'start');

    // Adding the X-axis with SHAP values range
    const xAxisScale = d3.scaleLinear()
        .domain([Math.min(...data.shap_values), Math.max(...data.shap_values)])
        .range([0, plotWidth]);

    const xAxis = d3.axisBottom(xAxisScale)
        .ticks(10)
        .tickFormat(d3.format(".2f"));

    svg.append('g')
        .attr('class', 'x-axis')
        .attr('transform', `translate(${margin.left}, ${margin.top - 20})`) // Positioned further down for better spacing
        .call(xAxis);

    // Adding "Higher" and "Lower" text labels
    svg.append('text')
        .attr('x', plotWidth / 4)
        .attr('y', margin.top - 30)
        .attr('class', 'higher-lower-label')
        .attr('fill', 'blue')
        .text("Higher");

    svg.append('text')
        .attr('x', (3 * plotWidth) / 4)
        .attr('y', margin.top - 30)
        .attr('class', 'higher-lower-label')
        .attr('fill', 'red')
        .text("Lower");
}


</script>

<svg id="forcePlot" viewBox="0 0 800 150" preserveAspectRatio="xMidYMid meet" width="100%" height="auto"></svg>
