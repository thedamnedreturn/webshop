// Ultimate анимации для магазина
class UltimateAnimations {
    constructor() {
        this.init();
    }

    init() {
        this.createParticles();
        this.initScrollAnimations();
        this.init3DEffects();
        this.initParallax();
        this.initLoadingStates();
    }

    // Создание частиц фона
    createParticles() {
        const container = document.createElement('div');
        container.className = 'particles-container';
        document.body.prepend(container);

        for (let i = 0; i < 50; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';

            // Случайные свойства
            const size = Math.random() * 4 + 2;
            const left = Math.random() * 100;
            const animationDuration = Math.random() * 20 + 10;
            const animationDelay = Math.random() * 5;

            particle.style.cssText = `
                width: ${size}px;
                height: ${size}px;
                left: ${left}%;
                animation-duration: ${animationDuration}s;
                animation-delay: ${animationDelay}s;
                background: hsl(${Math.random() * 360}, 100%, 70%);
            `;

            container.appendChild(particle);
        }
    }

    // Анимации при скролле
    initScrollAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');

                    // Добавляем задержку для дочерних элементов
                    if (entry.target.dataset.animateStagger) {
                        const children = entry.target.children;
                        Array.from(children).forEach((child, index) => {
                            child.style.animationDelay = `${index * 0.1}s`;
                        });
                    }
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.animate-on-scroll').forEach(el => {
            observer.observe(el);
        });
    }

    // 3D эффекты для карточек
    init3DEffects() {
        document.querySelectorAll('.product-card-3d').forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;

                const centerX = rect.width / 2;
                const centerY = rect.height / 2;

                const rotateY = (x - centerX) / 25;
                const rotateX = (centerY - y) / 25;

                card.style.transform = `
                    perspective(1000px)
                    rotateX(${rotateX}deg)
                    rotateY(${rotateY}deg)
                    scale3d(1.05, 1.05, 1.05)
                `;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
            });
        });
    }

    // Параллакс эффекты
    initParallax() {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const parallaxElements = document.querySelectorAll('[data-parallax]');

            parallaxElements.forEach(el => {
                const speed = el.dataset.parallaxSpeed || 0.5;
                const yPos = -(scrolled * speed);
                el.style.transform = `translateY(${yPos}px)`;
            });
        });
    }

    // Анимации загрузки
    initLoadingStates() {
        // Показываем скелетоны при загрузке
        this.showSkeletons();

        // Имитируем загрузку данных
        setTimeout(() => {
            this.hideSkeletons();
        }, 2000);
    }

    showSkeletons() {
        // Можно добавить скелетоны для контента
        console.log('Showing loading states...');
    }

    hideSkeletons() {
        console.log('Hiding loading states...');
    }
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    new UltimateAnimations();

    // Дополнительные интерактивные эффекты
    const buttons = document.querySelectorAll('.btn-neon');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Создаем эффект ripple
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.cssText = `
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(0, 242, 254, 0.6);
                border-radius: 50%;
                position: absolute;
                transform: scale(0);
                animation: ripple 0.6s linear;
            `;

            this.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);
        });
    });

    // Добавляем стиль для ripple анимации
    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
        .btn-neon {
            position: relative;
            overflow: hidden;
        }
    `;
    document.head.appendChild(style);

    console.log('🚀 Ultimate animations loaded!');
});