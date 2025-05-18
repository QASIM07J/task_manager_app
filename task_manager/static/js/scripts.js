document.addEventListener('DOMContentLoaded', () => {
    const taskItems = document.querySelectorAll('.task-item');
    taskItems.forEach(item => {
        item.addEventListener('click', () => {
            item.classList.add('bounce');
            setTimeout(() => item.classList.remove('bounce'), 300);
        });
    });
});