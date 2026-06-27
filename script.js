document.addEventListener('DOMContentLoaded', () => {
    const mainContent = document.getElementById('main-content');

    mainContent.innerHTML = `
        <h2 style="text-align: center; margin-bottom: 40px;">Professional Expertise</h2>
        
        <section id="skills-section">
            <h3 style="color: var(--dark-bg);">Technical Skills</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 15px;">
                <span class="skill-tag">Kubernetes</span>
                <span class="skill-tag">Terraform</span>
                <span class="skill-tag">LLMOps</span>
                <span class="skill-tag">GitOps</span>
                <span class="skill-tag">Python</span>
                <span class="skill-tag">Rust</span>
            </div>
        </section>

        <section id="experience-section">
            <h3 style="color: var(--dark-bg);">Experience</h3>
            
            <div class="card" style="border-left: 4px solid var(--accent-color); padding-left: 20px; margin-bottom: 30px; background: white; padding: 20px; border-radius: 8px;">
                <h4 style="margin: 0; color: var(--dark-bg);">Platform Engineer / Lead | 24x7Systems</h4>
                <p style="margin: 5px 0; font-size: 0.9em; font-style: italic;">Jan 2024 - Present</p>
                <p style="margin: 10px 0 0 0;">Integrated Vertex AI and Gemini for automated root-cause analysis in K8s networking and infrastructure drift.</p>
            </div>

            <div class="card" style="border-left: 4px solid var(--primary-color); padding-left: 20px; margin-bottom: 30px; background: white; padding: 20px; border-radius: 8px;">
                <h4 style="margin: 0; color: var(--dark-bg);">DevOps Engineer | CACI International</h4>
                <p style="margin: 5px 0; font-size: 0.9em; font-style: italic;">2023 - 2024</p>
                <p style="margin: 10px 0 0 0;">Orchestrated enterprise Kubernetes delivery via ArgoCD, achieving 100% state-sync across cloud environments.</p>
            </div>
        </section>
    `;
});
