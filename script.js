document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.section');
    const navItems = document.querySelectorAll('.sidebar a');
    
    // 1. Smooth Scroll for Navigation
    document.querySelectorAll('a.smooth-scroll').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // 2. Simple mechanism to handle sections: e.g., collapsing sections on mobile view
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.2
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            const section = entry.target;
            if (entry.isIntersecting) {
                // Simple active state logic (can be expanded)
                section.classList.add('is-visible');
            } else {
                // section.classList.remove('is-visible'); // Use sparingly
            }
        });
    }, observerOptions);

    // Observe all sections
    sections.forEach(section => {
        observer.observe(section);
    });
});