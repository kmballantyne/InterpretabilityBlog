<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';

    let shaptoyData = [
        { feature: 'Feature 1', shap: 0.1 },
        { feature: 'Feature 2', shap: 0.2 },
        { feature: 'Feature 3', shap: 0.3 },
        { feature: 'Feature 4', shap: 0.4 },
        { feature: 'Feature 5', shap: 0.5 }
    ];

    let selectedPrediction = 'Prediction 1';

    function updateSHAP(){
        shaptoyData = shaptoyData.map(d => ({...d, shap: d.shap * Math.random()}));
        drawChart();
    }

    function drawChart() {
        const svg = d3.select('#shap-chart');
        svg.selectAll('*').remove(); // Clear the existing chart

        const width = 400, height = 200, margin = { top: 20, right: 50, bottom: 50, left: 100 };
        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;

        const x = d3.scaleLinear()
            .domain([0, d3.max(shaptoyData, d => d.shap)])
            .range([0, innerWidth]);
        
        const y = d3.scaleBand()
            .domain(shaptoyData.map(d => d.feature))
            .range([0, innerHeight])
            .padding(0.1);

        svg.attr('width', width).attr('height', height);

        const chartGroup = svg.append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        // Bars
        chartGroup.selectAll('rect')
            .data(shaptoyData)
            .join('rect')
            .attr('x', 0)
            .attr('y', d => y(d.feature))
            .attr('width', d => x(d.shap))
            .attr('height', y.bandwidth())
            .attr('fill', 'steelblue');

        // Bar labels
        chartGroup.selectAll('text')
            .data(shaptoyData)
            .join('text')
            .attr('x', d => x(d.shap) + 5)
            .attr('y', d => y(d.feature) + y.bandwidth() / 2)
            .attr('dy', '0.35em')
            .text(d => d.shap.toFixed(2));

        // X-axis
        const xAxis = d3.axisBottom(x).ticks(5);
        chartGroup.append('g')
            .attr('transform', `translate(0,${innerHeight})`)
            .call(xAxis);

        // Y-axis
        const yAxis = d3.axisLeft(y);
        chartGroup.append('g').call(yAxis);

        // X-axis label
        svg.append('text')
            .attr('x', width / 2)
            .attr('y', height - 10)
            .attr('text-anchor', 'middle')
            .attr('class', 'axis-label')
            .text('SHAP Value');

        // Y-axis label
        svg.append('text')
            .attr('x', -height / 2)
            .attr('y', 15)
            .attr('transform', 'rotate(-90)')
            .attr('text-anchor', 'middle')
            .attr('class', 'axis-label')
            .text('Features');
    }

    onMount(drawChart);
</script>

<label>
    Select Prediction:
    <select bind:value={selectedPrediction} on:change={updateSHAP}>
        <option>Prediction 1</option>
        <option>Prediction 2</option>
        <option>Prediction 3</option>
    </select>
</label>

<svg id="shap-chart"></svg>