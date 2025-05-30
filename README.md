This is the official webpage of the paper "ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning". 

Link to the webpage: [ReinFlow.github.io](https://reinflow.github.io/)




    <h1>ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning</h1>
    <div class="figure-container">
        <img src="figs/jpgs/ReinFlow.jpg" alt="schematic">
        <div class="caption">
            <ul>
            <p>Fine-tuning flow matching policy with ReinFlow involves these steps:</p>
            <!-- <ul> -->
            <li><b>1. Online Rollout</b>: The robot interacts with the environment, gathers visual and proprioceptive observation. </li>
            <li><b>2. Extract Features</b>: A pre-trained policy backbone extracts features, feeds to the velocity field $v_\theta$, then guide the next action's changes.</li>
            <li><b>3. Add Noise</b>: The network $\sigma_{\theta^\prime}$ shares features with $v_\theta$, outputs Gaussian noise to smooth the ODE path for likelihood evaluation. </li>
            <li><b>4. Co-train and Discard</b>: The network $\sigma_{\theta^\prime}$ co-trains with $v_\theta$ during fine-tuning, but discarded afterward.</li>
            <!-- </ul>          -->
            </ul>
        </div>


        