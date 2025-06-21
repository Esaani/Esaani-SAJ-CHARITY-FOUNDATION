// DOM Elements
const navbar = document.getElementById('navbar');
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');
const navLinks = document.querySelectorAll('.nav-link');
const statNumbers = document.querySelectorAll('.stat-number');
const amountBtns = document.querySelectorAll('.amount-btn');
const frequencyOptions = document.querySelectorAll('input[name="frequency"]');

// Lightbox elements
const lightbox = document.getElementById('lightbox');
const lightboxImage = document.getElementById('lightbox-image');
const lightboxTitle = document.getElementById('lightbox-title');
const lightboxDescription = document.getElementById('lightbox-description');
const lightboxClose = document.querySelector('.lightbox-close');
const lightboxPrev = document.querySelector('.lightbox-prev');
const lightboxNext = document.querySelector('.lightbox-next');
const galleryItems = document.querySelectorAll('.gallery-item');

// Lightbox state
let currentImageIndex = 0;
let galleryImages = [];

// Initialize gallery images
function initGallery() {
    galleryImages = Array.from(galleryItems).map((item, index) => ({
        index: index,
        src: item.querySelector('img').src,
        alt: item.querySelector('img').alt,
        title: item.querySelector('.gallery-content h4').textContent,
        description: item.querySelector('.gallery-content p').textContent
    }));
}

// Open lightbox
function openLightbox(index) {
    currentImageIndex = index;
    const image = galleryImages[index];
    
    lightboxImage.src = image.src;
    lightboxImage.alt = image.alt;
    lightboxTitle.textContent = image.title;
    lightboxDescription.textContent = image.description;
    
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// Close lightbox
function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
}

// Navigate to previous image
function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + galleryImages.length) % galleryImages.length;
    openLightbox(currentImageIndex);
}

// Navigate to next image
function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % galleryImages.length;
    openLightbox(currentImageIndex);
}

// Navigation functionality
function toggleMenu() {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
}

function closeMenu() {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
}

// Smooth scrolling for navigation links
function smoothScroll(e) {
    e.preventDefault();
    const targetId = this.getAttribute('href');
    const targetSection = document.querySelector(targetId);
    
    if (targetSection) {
        const offsetTop = targetSection.offsetTop - 80; // Account for fixed navbar
        window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
        });
    }
    
    closeMenu();
}

// Navbar scroll effect
function handleScroll() {
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
}

// Animate stats when in viewport
function animateStats() {
    statNumbers.forEach(stat => {
        const rect = stat.getBoundingClientRect();
        const isInViewport = rect.top <= window.innerHeight && rect.bottom >= 0;
        
        if (isInViewport && !stat.classList.contains('animated')) {
            const target = parseInt(stat.parentElement.dataset.target);
            animateNumber(stat, target);
            stat.classList.add('animated');
        }
    });
}

// Animate number counting
function animateNumber(element, target) {
    let current = 0;
    const increment = target / 50; // 50 steps for smooth animation
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current);
    }, 30);
}

// Intersection Observer for animations
function createIntersectionObserver() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.project-card, .contact-item, .gallery-item, .stat-item');
    animateElements.forEach(el => observer.observe(el));
}

// Donation amount selection
function selectAmount() {
    amountBtns.forEach(btn => btn.classList.remove('active'));
    this.classList.add('active');
    
    if (this.dataset.amount === 'custom') {
        // Show custom amount input
        showCustomAmountInput();
    }
}

function showCustomAmountInput() {
    // Create custom amount input if it doesn't exist
    let customInput = document.querySelector('.custom-amount-input');
    if (!customInput) {
        customInput = document.createElement('input');
        customInput.type = 'number';
        customInput.placeholder = 'Enter amount';
        customInput.className = 'custom-amount-input';
        customInput.style.cssText = `
            padding: 0.75rem 1.5rem;
            border: 2px solid var(--primary-blue);
            border-radius: 8px;
            font-size: 1rem;
            width: 100%;
            margin-top: 1rem;
        `;
        
        const customBtn = document.querySelector('.amount-btn.custom');
        customBtn.parentElement.appendChild(customInput);
    }
    customInput.style.display = 'block';
    customInput.focus();
}

// Form submission
function handleFormSubmit(e) {
    e.preventDefault();
    
    // Get form data
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData);
    
    // Show success message
    showNotification('Thank you! Your message has been sent successfully.', 'success');
    
    // Reset form
    e.target.reset();
}

// Newsletter subscription
function handleNewsletterSubmit(e) {
    e.preventDefault();
    
    const email = e.target.querySelector('input[type="email"]').value;
    
    if (email) {
        showNotification('Thank you for subscribing to our newsletter!', 'success');
        e.target.reset();
    }
}

// Show notification
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-info-circle'}"></i>
            <span>${message}</span>
            <button class="notification-close">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#48BB78' : '#4299E1'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 300px;
    `;
    
    // Add to page
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        removeNotification(notification);
    }, 5000);
    
    // Close button functionality
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.addEventListener('click', () => removeNotification(notification));
}

function removeNotification(notification) {
    notification.style.transform = 'translateX(100%)';
    setTimeout(() => {
        if (notification.parentElement) {
            notification.remove();
        }
    }, 300);
}

// Parallax effect for hero section
function handleParallax() {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    const heroBackground = document.querySelector('.hero-background');
    
    if (heroBackground) {
        const rate = scrolled * -0.5;
        heroBackground.style.transform = `translateY(${rate}px)`;
    }
}

// Keyboard navigation for lightbox
function handleKeydown(e) {
    if (!lightbox.classList.contains('active')) return;
    
    switch(e.key) {
        case 'Escape':
            closeLightbox();
            break;
        case 'ArrowLeft':
            prevImage();
            break;
        case 'ArrowRight':
            nextImage();
            break;
    }
}

// Add CSS for animations
function addAnimationStyles() {
    const style = document.createElement('style');
    style.textContent = `
        .animate-in {
            animation: fadeInUp 0.6s ease-out forwards;
        }
        
        .notification-content {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .notification-close {
            background: none;
            border: none;
            color: white;
            cursor: pointer;
            margin-left: auto;
            padding: 0;
            font-size: 0.9rem;
        }
        
        .notification-close:hover {
            opacity: 0.8;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .project-card,
        .contact-item,
        .gallery-item,
        .stat-item {
            opacity: 0;
            transform: translateY(30px);
        }
        
        .project-card.animate-in,
        .contact-item.animate-in,
        .gallery-item.animate-in,
        .stat-item.animate-in {
            opacity: 1;
            transform: translateY(0);
        }
    `;
    document.head.appendChild(style);
}

// Initialize all functionality
function init() {
    // Add animation styles
    addAnimationStyles();
    
    // Initialize gallery
    initGallery();
    
    // Event listeners
    hamburger.addEventListener('click', toggleMenu);
    navLinks.forEach(link => link.addEventListener('click', smoothScroll));
    
    // Gallery lightbox events
    galleryItems.forEach((item, index) => {
        item.addEventListener('click', () => openLightbox(index));
    });
    
    lightboxClose.addEventListener('click', closeLightbox);
    lightboxPrev.addEventListener('click', prevImage);
    lightboxNext.addEventListener('click', nextImage);
    
    // Close lightbox when clicking outside
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });
    
    // Keyboard navigation
    document.addEventListener('keydown', handleKeydown);
    
    // Scroll events
    window.addEventListener('scroll', handleScroll);
    window.addEventListener('scroll', animateStats);
    window.addEventListener('scroll', handleParallax);
    
    // Donation amount buttons
    amountBtns.forEach(btn => btn.addEventListener('click', selectAmount));
    
    // Form submissions
    const contactForm = document.querySelector('.form');
    if (contactForm) {
        contactForm.addEventListener('submit', handleFormSubmit);
    }
    
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', handleNewsletterSubmit);
    }
    
    // Create intersection observer
    createIntersectionObserver();
    
    // Initialize stats animation on page load
    setTimeout(animateStats, 1000);
}

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', init);

// Add loading animation
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});

// Add CSS for loading state
const loadingStyle = document.createElement('style');
loadingStyle.textContent = `
    body:not(.loaded) {
        overflow: hidden;
    }
    
    body:not(.loaded)::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: var(--primary-blue);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    body:not(.loaded)::after {
        content: 'SAJ Foundation';
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-family: var(--font-heading);
        font-size: 2rem;
        font-weight: 700;
        z-index: 10000;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }
`;
document.head.appendChild(loadingStyle); 