# File: README.md
# Non-Bank Loan Landing Page

This project contains a simple landing page for non-bank loans, implemented using Flask.

## Installation

1. Ensure you have Python installed on your computer.
2. Install the requirements using the command:
   ```
   pip install -r requirements.txt
   ```

## Running

Run the application using the command:
```
python app.py
```

Navigate to `http://127.0.0.1:5000` in your browser to view the landing page.

---

# File: requirements.txt
flask==2.0.1

---

# File: .gitignore
__pycache__/
*.pyc
.env
venv/

---

# File: app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

---

# File: templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Non-Bank Loans - Fast and Flexible Financing Solutions</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <div class="container">
            <h1>Non-Bank Loans <span class="highlight">Fast and Flexible</span></h1>
        </div>
    </header>

    <div class="container">
        <div class="main-content">
            <h2>Personalized Financing Solutions for Every Need</h2>
            <p>We offer non-bank loans with convenient terms and lightning speed. No unnecessary bureaucracy, no long waiting times. The perfect solution for your financing needs.</p>
            
            <div class="image-container">
                <img src="{{ url_for('static', filename='images/happy-customers.jpg') }}" alt="Image showing satisfied loan recipients" />
            </div>

            <a href="#contact-form" class="cta-button">Request a Loan Now</a>

            <div class="features">
                <div class="feature">
                    <h3>Fast Approval</h3>
                    <p>Get an answer within 24 hours. We understand that time is a valuable resource.</p>
                </div>
                <div class="feature">
                    <h3>Flexible Amounts</h3>
                    <p>Loans from $1,000 to $100,000, tailored to your needs.</p>
                </div>
                <div class="feature">
                    <h3>Convenient Terms</h3>
                    <p>Attractive interest rates and comfortable repayment schedules. Full transparency at every stage.</p>
                </div>
            </div>

            <div class="testimonial">
                <p>"The loan I received allowed me to expand my business exactly when I needed it. The process was simple and fast, and the team was professional and courteous."</p>
                <p><strong>- John Smith, Business Owner</strong></p>
            </div>

            <div class="image-container">
                <img src="{{ url_for('static', filename='images/loan-benefits.jpg') }}" alt="Graph showing the benefits of non-bank loans" />
            </div>

            <h2>Why Choose Us?</h2>
            <ul>
                <li>Over 10 years of experience in the loan market</li>
                <li>Professional and dedicated team that will tailor the perfect loan for you</li>
                <li>Secure and convenient digital process</li>
                <li>Personal guidance throughout the entire journey</li>
            </ul>

            <div id="contact-form" class="contact-form">
                <h2>Leave Your Details and We'll Get Back to You Soon</h2>
                <form>
                    <input type="text" placeholder="Full Name" required>
                    <input type="tel" placeholder="Phone" required>
                    <input type="email" placeholder="Email" required>
                    <textarea placeholder="Brief description of your loan needs" rows="4"></textarea>
                    <button type="submit">Send Request</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>

---

# File: static/css/style.css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
}
.container {
    width: 90%;
    max-width: 1200px;
    margin: auto;
    overflow: hidden;
    padding: 20px;
}
header {
    background: linear-gradient(to right, #35424a, #2c3e50);
    color: #ffffff;
    padding: 1rem 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
header h1 {
    margin: 0;
    text-align: center;
    font-size: 2.5rem;
}
.highlight {
    color: #e74c3c;
}
.main-content {
    background: #ffffff;
    padding: 2rem;
    margin-top: 2rem;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
}
.cta-button {
    display: inline-block;
    padding: 15px 30px;
    background: #e74c3c;
    color: #ffffff;
    text-align: center;
    text-decoration: none;
    margin: 20px 0;
    border-radius: 5px;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
.cta-button:hover {
    background: #c0392b;
}
.features {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin-top: 2rem;
}
.feature {
    flex-basis: calc(33.333% - 20px);
    background: #ecf0f1;
    color: #2c3e50;
    padding: 1.5rem;
    margin-bottom: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}
.feature:hover {
    transform: translateY(-5px);
}
.feature h3 {
    color: #e74c3c;
}
.testimonial {
    background: #2c3e50;
    color: #ecf0f1;
    padding: 2rem;
    margin-top: 2rem;
    border-radius: 8px;
    position: relative;
}
.testimonial:before {
    content: '"';
    font-size: 5rem;
    position: absolute;
    top: -20px;
    left: 20px;
    color: #e74c3c;
    opacity: 0.5;
}
.contact-form {
    margin-top: 2rem;
    background: #ecf0f1;
    padding: 2rem;
    border-radius: 8px;
}
.contact-form input, .contact-form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 1rem;
    border: 1px solid #bdc3c7;
    border-radius: 4px;
}
.contact-form button {
    background: #e74c3c;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
}
.image-container {
    text-align: center;
    margin: 2rem 0;
}
.image-container img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
@media (max-width: 768px) {
    .feature {
        flex-basis: 100%;
    }
}
