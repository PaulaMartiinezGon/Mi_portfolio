document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll("section");

    const revealOnScroll = () => {
        let scrollY = window.scrollY;

        sections.forEach(section => {
            if (scrollY + window.innerHeight - 100 > section.offsetTop) {
                section.classList.add("visible");
            }
        });
    };

    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll();
});
document.addEventListener("DOMContentLoaded", function() {
    const timelineItems = document.querySelectorAll(".timeline-item");

    const revealOnScroll = () => {
        let scrollY = window.scrollY;

        timelineItems.forEach(item => {
            if (scrollY + window.innerHeight - 50 > item.offsetTop) {
                item.classList.add("visible");
            }
        });
    };

    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll();
});
