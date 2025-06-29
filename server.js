const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// POST endpoint for contact forms
app.post('/api/contact', async (req, res) => {
  const { name, email, phone, subject, message } = req.body;

  // Configure your email transport (use an App Password for Gmail)
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'sajfoundation23@gmail.com',
      pass: 'YOUR_APP_PASSWORD' // <-- Replace with your Gmail App Password
    }
  });

  const mailOptions = {
    from: email,
    to: 'sajfoundation23@gmail.com',
    subject: `Contact Form: ${subject || 'General Inquiry'}`,
    text: `
      Name: ${name}
      Email: ${email}
      Phone: ${phone || 'N/A'}
      Subject: ${subject}
      Message: ${message}
    `
  };

  try {
    await transporter.sendMail(mailOptions);
    res.status(200).json({ message: 'Message sent successfully!' });
  } catch (err) {
    res.status(500).json({ message: 'Failed to send message.', error: err.toString() });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));