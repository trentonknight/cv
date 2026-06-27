document.addEventListener('DOMContentLoaded', () => {
    const mainContent = document.getElementById('main-content');

    mainContent.innerHTML = `
        <h2 style="text-align: center; margin-bottom: 40px;">My Professional Experience</h2>
        
        <section id="skills-section">
            <h3>Technical Skills</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 15px;">
                <span class="skill-tag">JavaScript / TypeScript</span>
                <span class="skill-tag">React</span>
                <span class="skill-tag">Node.js</span>
            </div>
        </section>

        <section id="experience-section">
            <h3>Professional Experience</h3>
            <div style="border-left: 4px solid #007bff; padding-left: 20px; margin-bottom: 30px;">
                <h4>Senior Software Engineer at Tech Solutions Inc.</h4>
                <p>*Jan 2021 - Present</p>
                <p>Developed high-throughput microservices, reducing latency by 25%.</p>
            </div>
        </section>
    `;
});
