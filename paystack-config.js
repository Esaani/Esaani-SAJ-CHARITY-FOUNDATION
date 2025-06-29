// Paystack Payment Configuration
const PAYSTACK_CONFIG = {
    // Paystack API Configuration
    api: {
        baseUrl: 'https://api.paystack.co',
        publicKey: 'pk_test_88e80028ebdac031d872e92f4b4d2867798a0da5',
        secretKey: 'sk_test_c6b416bf815a18da05efb89b2e16d082e1c52271',
        environment: 'test', // 'test' or 'live'
    },
    
    // Payment Settings
    payment: {
        currency: 'GHS',
        country: 'GH',
        language: 'en',
        callbackUrl: 'https://sajfoundation.org/payment-success',
        webhookUrl: 'https://sajfoundation.org/payment-webhook',
    },
    
    // Donation Settings
    donation: {
        minAmount: 1,
        maxAmount: 10000,
        defaultAmounts: [25, 50, 100, 250],
        supportedFrequencies: ['one-time', 'monthly'],
    },
    
    // UI Settings
    ui: {
        buttonText: {
            processing: 'Processing Payment...',
            success: 'Payment Successful!',
            error: 'Payment Failed',
            default: 'Donate Now'
        },
        messages: {
            amountRequired: 'Please select or enter a donation amount',
            amountInvalid: 'Please enter a valid amount between ₵1 and ₵10,000',
            formIncomplete: 'Please fill in all required fields',
            paymentProcessing: 'Redirecting to secure payment page...',
            paymentSuccess: 'Thank you for your donation!',
            paymentError: 'Payment failed. Please try again.',
            networkError: 'Network error. Please check your connection and try again.'
        }
    }
};

// Paystack API Helper Functions
class PaystackAPI {
    constructor(config) {
        this.config = config;
        this.baseUrl = config.api.baseUrl;
        this.publicKey = config.api.publicKey;
        this.secretKey = config.api.secretKey;
    }

    // Initialize Paystack payment
    async initializePayment(paymentData) {
        try {
            const response = await fetch(`${this.baseUrl}/transaction/initialize`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${this.publicKey}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    amount: Math.round(paymentData.amount * 100), // Convert to kobo
                    email: paymentData.donorEmail,
                    currency: this.config.payment.currency,
                    callback_url: this.config.payment.callbackUrl,
                    reference: this.generateReference(),
                    metadata: {
                        donor_name: paymentData.donorName,
                        donor_email: paymentData.donorEmail,
                        donor_phone: paymentData.donorPhone,
                        donor_country: paymentData.donorCountry,
                        donor_message: paymentData.donorMessage,
                        frequency: paymentData.frequency,
                        foundation: 'SAJ Foundation',
                        custom_fields: [
                            {
                                display_name: "Donor Name",
                                variable_name: "donor_name",
                                value: paymentData.donorName
                            },
                            {
                                display_name: "Donation Frequency",
                                variable_name: "frequency",
                                value: paymentData.frequency
                            }
                        ]
                    }
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.status && data.data) {
                return {
                    success: true,
                    authorizationUrl: data.data.authorization_url,
                    reference: data.data.reference,
                    accessCode: data.data.access_code
                };
            } else {
                throw new Error(data.message || 'Payment initialization failed');
            }
        } catch (error) {
            console.error('Payment initialization error:', error);
            return {
                success: false,
                error: error.message
            };
        }
    }

    // Verify payment transaction
    async verifyPayment(reference) {
        try {
            const response = await fetch(`${this.baseUrl}/transaction/verify/${reference}`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${this.publicKey}`,
                    'Content-Type': 'application/json',
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.status && data.data) {
                return {
                    success: true,
                    status: data.data.status,
                    amount: data.data.amount / 100, // Convert from kobo to cedis
                    currency: data.data.currency,
                    reference: data.data.reference,
                    gateway_response: data.data.gateway_response,
                    paid_at: data.data.paid_at,
                    metadata: data.data.metadata
                };
            } else {
                throw new Error(data.message || 'Payment verification failed');
            }
        } catch (error) {
            console.error('Payment verification error:', error);
            return {
                success: false,
                error: error.message
            };
        }
    }

    // Generate unique reference
    generateReference() {
        const timestamp = Date.now();
        const random = Math.random().toString(36).substring(2, 15);
        return `SAJ_DONATION_${timestamp}_${random}`.toUpperCase();
    }

    // Validate payment data
    validatePaymentData(paymentData) {
        const errors = [];

        if (!paymentData.amount || paymentData.amount < this.config.donation.minAmount) {
            errors.push(this.config.ui.messages.amountRequired);
        }

        if (paymentData.amount > this.config.donation.maxAmount) {
            errors.push(this.config.ui.messages.amountInvalid);
        }

        if (!paymentData.donorName || !paymentData.donorEmail) {
            errors.push(this.config.ui.messages.formIncomplete);
        }

        if (!this.isValidEmail(paymentData.donorEmail)) {
            errors.push('Please enter a valid email address');
        }

        if (!this.isValidPhone(paymentData.donorPhone)) {
            errors.push('Please enter a valid phone number');
        }

        return {
            isValid: errors.length === 0,
            errors: errors
        };
    }

    // Email validation
    isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Phone validation (Ghana format)
    isValidPhone(phone) {
        if (!phone) return true; // Phone is optional
        const phoneRegex = /^(\+233|0)[0-9]{9}$/;
        return phoneRegex.test(phone.replace(/\s/g, ''));
    }

    // Format amount for display
    formatAmount(amount) {
        return new Intl.NumberFormat('en-GH', {
            style: 'currency',
            currency: 'GHS'
        }).format(amount);
    }

    // Redirect to Paystack payment page
    redirectToPayment(authorizationUrl) {
        if (authorizationUrl) {
            window.location.href = authorizationUrl;
        } else {
            throw new Error('No authorization URL provided');
        }
    }

    // Get payment status text
    getPaymentStatus(status) {
        switch (status) {
            case 'success':
                return { status: 'success', message: 'Payment successful' };
            case 'failed':
                return { status: 'failed', message: 'Payment failed' };
            case 'abandoned':
                return { status: 'abandoned', message: 'Payment abandoned' };
            case 'pending':
                return { status: 'pending', message: 'Payment pending' };
            default:
                return { status: 'unknown', message: 'Unknown payment status' };
        }
    }
}

// Initialize Paystack API
const paystack = new PaystackAPI(PAYSTACK_CONFIG);

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { PAYSTACK_CONFIG, PaystackAPI };
} 