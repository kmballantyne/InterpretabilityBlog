<!-- src/routes/+page.svelte -->

<script>
    import { onMount } from 'svelte';

    import SHAP from '../components/SHAP.svelte';
    import PDP from '../components/PDP.svelte';
    import Attn from '../components/Attn.svelte';
    import ForcePlot from '../components/ForcePlot.svelte';

    let forcePlotData;
    onMount(async () => {
        const res = await fetch('/force_plot_data.json');
        forcePlotData = await res.json();
    });
</script>

<h1>Interactive Blog: Interpretability in Machine Learning and AI</h1>

<section>
    <!-- Introduction -->

    <h2>Introduction</h2>
    <p>Interpretability in Machine Learning and AI is a hot topic. It is a field that is gaining more and more attention as the use of machine learning models becomes more widespread. In this blog, we will explore the importance of interpretability in machine learning and AI, and discuss some of the techniques that are being used to make machine learning models more interpretable. Some of the interpretability methods that this blog will cover include:</p>

    <ul>
        <li>SHapley Additive exPlanations (SHAP)</li>
        <li>Partial Dependence Plots (PDP)</li>
        <li>Attention Interpretability (visualization to come later)</li>
    </ul>

</section>

<div class=content-container-1>
    <!-- SHAP -->

    <h2>SHapley Additive exPlanations (SHAP): Feature Importance</h2>
    <p class="paragraph-1">SHAP is a method for explaining individual predictions from machine learning models. It is based on the Shapley value, which is a concept from cooperative game theory. SHAP values provide a way to explain the output of a machine learning model by attributing the output to the input features. SHAP values can be used to explain the output of any machine learning model, including complex models like deep neural networks. Below is a demonstration of a feature importance plot that illustrates how much a given feature overall contributes to a given predicted output calculated as a SHAP value. Here as the SHAP value increases positively the amount a given feature contributes to a given model predicted output.</p>

    <SHAP />
</div>


<section>
    <div class="page-container">
    <!-- SHAP -->
        <div id="tooltip" style="position: absolute; visibility: hidden; background: #fff; border: 1px solid #ccc; padding: 8px; border-radius: 4px; pointer-events: none;"></div>

        <h2>SHapley Additive exPlanations (SHAP): Force Plot</h2>
        <p class="paragraph-2">A SHAP force plot visually represents how individual features contribute to a prediction for a specific instance by highlighting their individual SHAP values. This kind of plot has several components: a baseline value, SHAP values for each feature, and the predicted value. The baseline value is the average model predicted value across all samples. The final predicted value for the specific instance is where the baseline value has been adjusted by all SHAP values, resulting in the actual prediction. The SHAP values represents each feature’s contribution is represented as a bar or colored segment. These contributions (positive or negative) are the SHAP values for each feature. The length, direction, and color of each segment indicate the strength and direction of each feature’s impact where positive SHAP values are coded red and indicates that it strongly increases a predicted outcome whereas values coded as blue and negative means that it strongly decreases it.</p>

        {#if forcePlotData}
            <ForcePlot {forcePlotData} />
        {/if}
    </div> 
</section>

<section>
    <!-- PDP -->
    <h2>Partial Dependence Plots (PDP)</h2>
    <p class="paragraph-3">Partial dependence plots (PDP) show the relationship between a feature and the predicted outcome of a machine learning model, while accounting for the average effect of all other features. PDPs are a useful tool for understanding how a machine learning model makes predictions, and can help to identify relationships between features and the predicted outcome. PDPs can be used to visualize the effect of a single feature on the predicted outcome, or to explore interactions between multiple features. Below is an example of a partial dependence plot where the slider changes the feature from a given model. In this demonstration, as the outputted value of a given feature increases or decreases the PDP output may also increase or decrease. This allows users to interpret the feature importance, or how much a given feature (and its value) contributes to the predicted output of a model based on the PDP value. Here as the PDP value increases, how much the fature contributes to the predicted output also increases.</p>

    <PDP />
</section>

<section>
    <!-- Attention -->

    <h2>Attention Interpretability</h2>
    <p>Attention mechanisms are a key component of many deep learning models, including transformer models like BERT and GPT. Attention mechanisms allow the model to focus on different parts of the input sequence when making predictions, and can help to improve the performance of the model. Attention mechanisms can also be used to provide interpretability for the model, by visualizing the attention weights and showing which parts of the input sequence are being attended to by the model.</p>

    <Attn />
</section>

<style>
    .paragraph-1, .paragraph-2, .paragraph-3 {
        margin-bottom: 20px; /* Adjust this value as needed */
    }

    .content-container-1 {
    display: flex;
    flex-direction: column;
    gap: 20px; /* Space between paragraph and SVG */
    }

    .page-container {
        display: flex;
        flex-direction: column;
        gap: 20px; /* Adjust the gap as needed */
        padding: 20px; /* Optional padding for the page */
    }
</style>
