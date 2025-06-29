# Paystack Payment Integration Setup Guide

## Overview
This guide explains how to set up and configure the Paystack payment integration for the SAJ Charity Foundation website.

## Files Added/Modified

### 1. Configuration Files
- `paystack-config.js` - Paystack API configuration and helper functions
- `payment-success.html` - Payment success page

### 2. Modified Files
- `index.html` - Added payment form and Paystack script
- `script.js` - Added payment processing logic
- `styles.css` - Added payment form styles

## Configuration

### Current Test Configuration
The integration is currently configured with **test credentials**:

```javascript
// Test Mode Configuration
api: {
    baseUrl: 'https://api.paystack.co',
    publicKey: 'pk_test_88e80028ebdac031d872e92f4b4d2867798a0da5',
    secretKey: 'sk_test_c6b416bf815a18da05efb89b2e16d082e1c52271',
    environment: 'test'
}
```

### Production Setup

#### 1. Get Production Credentials
1. Log in to your Paystack Dashboard
2. Go to Settings > API Keys & Webhooks
3. Generate new production keys
4. Replace the test keys in `paystack-config.js`:

```javascript
// Production Configuration
api: {
    baseUrl: 'https://api.paystack.co',
    publicKey: 'pk_live_YOUR_PRODUCTION_PUBLIC_KEY',
    secretKey: 'sk_live_YOUR_PRODUCTION_SECRET_KEY',
    environment: 'live'
}
```

#### 2. Update Callback URLs
Update the callback URLs in `paystack-config.js`:

```javascript
payment: {
    callbackUrl: 'https://yourdomain.com/payment-success.html',
    webhookUrl: 'https://yourdomain.com/payment-webhook',
}
```

#### 3. Configure Webhooks
1. In Paystack Dashboard, go to Settings > Webhooks
2. Add webhook URL: `https://yourdomain.com/payment-webhook`
3. Select events to listen for:
   - `charge.success`
   - `transfer.success`
   - `refund.processed`

## Features

### 1. Payment Form
- **Amount Selection**: Predefined amounts (₵25, ₵50, ₵100, ₵250) or custom amount
- **Frequency**: One-time or monthly donations
- **Donor Information**: Name, email, phone, country, optional message
- **Payment Summary**: Real-time summary of donation details
- **Security Notice**: Assures users about payment security

### 2. Payment Processing
- **Validation**: Client-side and server-side validation
- **Paystack Integration**: Direct integration with Paystack API
- **Error Handling**: Comprehensive error handling and user feedback
- **Loading States**: Visual feedback during payment processing

### 3. Payment Success Page
- **Transaction Details**: Shows payment confirmation details
- **Impact Message**: Personalized message based on donation amount
- **Navigation**: Easy return to home or donate again

## Testing

### Test Cards
Use these test cards for testing:

| Card Type | Number | Expiry | CVV |
|-----------|--------|--------|-----|
| Visa | 4084 0840 8408 4081 | Any future date | Any 3 digits |
| Mastercard | 5105 1051 0510 5100 | Any future date | Any 3 digits |
| Verve | 5061 4603 6000 0008 | Any future date | Any 3 digits |

### Test Scenarios
1. **Successful Payment**: Use any test card with valid details
2. **Failed Payment**: Use card number `4000 0000 0000 0002`
3. **Insufficient Funds**: Use card number `4000 0000 0000 9995`
4. **Expired Card**: Use card number `4000 0000 0000 0069`

## Security Considerations

### 1. API Key Security
- **Never expose secret keys** in client-side code
- Use environment variables for production
- Rotate keys regularly
- Monitor API usage

### 2. Data Validation
- Validate all input data
- Sanitize user inputs
- Implement rate limiting
- Use HTTPS in production

### 3. Payment Verification
- Always verify payments server-side
- Use webhooks for payment confirmation
- Store transaction references
- Implement idempotency

## Deployment Checklist

### Before Going Live
- [ ] Replace test keys with production keys
- [ ] Update callback URLs to production domain
- [ ] Configure webhooks
- [ ] Test with real payment methods
- [ ] Set up monitoring and logging
- [ ] Configure error handling
- [ ] Test payment success page
- [ ] Verify webhook endpoints

### Production Environment
- [ ] Use HTTPS
- [ ] Set up SSL certificates
- [ ] Configure CORS properly
- [ ] Set up monitoring
- [ ] Configure backups
- [ ] Set up logging

## Troubleshooting

### Common Issues

#### 1. Payment Initialization Fails
- Check API key configuration
- Verify network connectivity
- Check browser console for errors
- Ensure all required fields are filled

#### 2. Payment Verification Fails
- Check reference parameter
- Verify API key permissions
- Check transaction status in Paystack dashboard
- Review webhook configuration

#### 3. Callback Not Working
- Verify callback URL configuration
- Check domain SSL certificate
- Ensure URL is accessible
- Review Paystack dashboard logs

### Debug Mode
Enable debug mode by adding this to `paystack-config.js`:

```javascript
debug: true
```

This will log detailed information to the browser console.

## Support

### Paystack Support
- Documentation: https://paystack.com/docs
- API Reference: https://paystack.com/docs/api
- Support: support@paystack.com

### Technical Support
For technical issues with the integration:
1. Check browser console for errors
2. Review Paystack dashboard logs
3. Test with different payment methods
4. Verify configuration settings

## Updates and Maintenance

### Regular Tasks
- Monitor payment success rates
- Review error logs
- Update dependencies
- Test payment flow regularly
- Backup transaction data

### Version Updates
- Keep Paystack SDK updated
- Monitor for API changes
- Test after updates
- Update documentation

---

**Note**: This integration is configured for Ghana (GHS currency). For other countries, update the currency and country codes in the configuration. 