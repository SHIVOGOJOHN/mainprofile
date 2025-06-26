from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
import dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") # Change this to a strong, random key

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'techbidmarketplace@gmail.com' # Replace with your email
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD") # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'techbidmarketplace@gmail.com' # Replace with your email

mail = Mail(app)

# Dummy data for projects and research papers
projects_data = [
    {
        'title': 'Project 1: Predictive Maintenance for Industrial Machinery',
        'description': 'Developed a system to predict machine failures using sensor data, reducing downtime by 20%.',
        'view_system_link': '#',
        'view_code_link': '#'
    },
    {
        'title': 'Project 2: Real-time Object Detection for Autonomous Vehicles',
        'description': 'Built a deep learning model for real-time object detection, achieving 95% accuracy on a custom dataset.',
        'view_system_link': '#',
        'view_code_link': '#'
    },
    {
        'title': 'Project 3: Customer Churn Prediction',
        'description': 'Implemented a machine learning model to predict customer churn, leading to a 15% reduction in customer attrition.',
        'view_system_link': '#',
        'view_code_link': '#'
    },
    {
        'title': 'Project 4: Natural Language Processing for Sentiment Analysis',
        'description': 'Developed an NLP model to analyze social media sentiment, providing insights for marketing campaigns.',
        'view_system_link': '#',
        'view_code_link': '#'
    },
]

research_data = [
    {
        'title': 'Paper 1: A Novel Approach to Time-Series Forecasting using LSTMs',
        'description': 'Published in the Journal of Machine Learning Research, this paper introduces a new architecture for LSTMs that improves forecasting accuracy.',
        'view_system_link': '#',
        'view_code_link': '#',
        'read_paper_link': '#'
    },
    {
        'title': 'Paper 2: Unsupervised Anomaly Detection in High-Dimensional Data',
        'description': 'This paper, presented at the International Conference on Machine Learning, proposes a new algorithm for anomaly detection in large datasets.',
        'view_system_link': '#',
        'view_code_link': '#',
        'read_paper_link': '#'
    },
    {
        'title': 'Paper 3: Reinforcement Learning for Resource Optimization',
        'description': 'Explored the application of reinforcement learning to optimize resource allocation in cloud computing environments.',
        'view_system_link': '#',
        'view_code_link': '#',
        'read_paper_link': '#'
    },
    {
        'title': 'Paper 4: Federated Learning for Privacy-Preserving AI',
        'description': 'Investigated federated learning techniques to enable collaborative AI model training without compromising data privacy.',
        'view_system_link': '#',
        'view_code_link': '#',
        'read_paper_link': '#'
    },
]

@app.route('/')
def index():
    # Display only the first 2 projects and research papers on the homepage
    return render_template('index.html', projects=projects_data[:2], research_papers=research_data[:2])

@app.route('/projects')
def all_projects():
    return render_template('projects.html', projects=projects_data)

@app.route('/research')
def all_research():
    return render_template('research.html', research_papers=research_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            msg = Message(subject=f"New Message from {name}",
                        sender=app.config['MAIL_DEFAULT_SENDER'],
                        recipients=[app.config['MAIL_USERNAME']]) 
            msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error sending message: {e}', 'error')

    return render_template('index.html') # Render index.html for GET requests to /contact or if there's an error

if __name__ == '__main__':
    app.run()
