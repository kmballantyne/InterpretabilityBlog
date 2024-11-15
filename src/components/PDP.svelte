<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';

    let featureIndex = 0; // Start with the first feature

    // Define PDP data for multiple features
    let features = [
        { name: 'Feature 1', pdpData: Array.from({ length: 10 }, (_, i) => ({ x: i, y: Math.sin(i / 2) + 0.1 * Math.random() })) },
        { name: 'Feature 2', pdpData: Array.from({ length: 10 }, (_, i) => ({ x: i, y: Math.cos(i / 2) + 0.1 * Math.random() })) },
        { name: 'Feature 3', pdpData: Array.from({ length: 10 }, (_, i) => ({ x: i, y: Math.tan(i / 10) + 0.1 * Math.random() })) }
    ];

    function updatePDP() {
        drawChart();
    }

    function drawChart() {
        const svg = d3.select("#pdp-chart");
        svg.selectAll("*").remove(); // Clear previous chart

        const width = 500, height = 300;
        const margin = { top: 30, right: 30, bottom: 60, left: 80 };
        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;

        const x = d3.scaleLinear().domain([0, 10]).range([0, innerWidth]);
        const y = d3.scaleLinear().domain([-1, 1]).range([innerHeight, 0]);
    
        svg.attr("width", width).attr("height", height);
        const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);
    
        // Create the line path with animation
        const path = g.append("path")
            .datum(features[featureIndex].pdpData)
            .attr("fill", "none")
            .attr("stroke", "steelblue")
            .attr("stroke-width", 1.5)
            .attr("d", d3.line()
                .x(d => x(d.x))
                .y(d => y(d.y))
            )
            .attr("stroke-dasharray", function() {
                const length = this.getTotalLength();
                return `${length} ${length}`;
            })
            .attr("stroke-dashoffset", function() {
                return this.getTotalLength();
            });

        // X-axis
        g.append("g")
            .attr("transform", `translate(0,${innerHeight})`)
            .call(d3.axisBottom(x).ticks(5));
        
        // Y-axis
        g.append("g")
            .call(d3.axisLeft(y).ticks(5));
    
        // X-axis label
        g.append("text")
            .attr("x", innerWidth / 2)
            .attr("y", innerHeight + margin.bottom - 5)
            .attr("text-anchor", "middle")
            .attr("fill", "black")
            .text("Feature Value"); 
    
        // Y-axis label
        g.append("text")
            .attr("x", -innerHeight / 2)
            .attr("y", -margin.left + 20)
            .attr("text-anchor", "middle")
            .attr("fill", "black")
            .attr("transform", "rotate(-90)")
            .text("Partial Dependence"); 
        
        // Animate the line drawing from left to right
        path.transition()
            .duration(2000)
            .ease(d3.easeLinear)
            .attr("stroke-dashoffset", 0);
    }

    onMount(drawChart);
</script>

<div class="chart-wrapper">
    <label>
        Select Feature:
        <input type="range" min="0" max={features.length - 1} step="1" bind:value={featureIndex} on:input={updatePDP} />
        <span>{features[featureIndex].name}</span>
    </label>
    <svg id="pdp-chart" width="500" height="300"></svg>
</div>

<style>
    .chart-wrapper {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }

    label {
        margin-right: 20px;
    }
</style>
