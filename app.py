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
        'title': 'Federated Learning with Blockchain & IPFS',
        'description': 'A decentralized, auditable, and transparent AI training ecosystem.',
        'details_page': 'project_blockchain_ai'
    },
    {
        'title': 'AI-driven Economic Stress-Testing Twins for SMEs',
        'description': 'Create a synthetic-digital twin that simulates an SME under economic shocks so lenders and policymakers can stress test resilience.',
        'details_page': 'project_sme_twins'
    },
    {
        'title': 'Neuro-symbolic AI for Explainable Creditworthiness',
        'description': 'Combine symbolic reasoning with deep models to yield credit decisions that are transparent, auditable, and defensible.',
        'details_page': 'project_creditworthiness'
    },
    {
        'title': 'Self-healing Distributed Systems',
        'description': 'Detect failures and automatically remediate faults across cloud, edge, IoT, and blockchain networks.',
        'details_page': 'project_self_healing'
    },
    {
        'title': 'Predictive Resilience System for Supply Chains',
        'description': 'Forecast disruptions from geopolitics, weather, cyber incidents, and suggest mitigation routes.',
        'details_page': 'project_supply_chain'
    },
    {
        'title': 'AI for Dynamic Carbon Capture Optimization',
        'description': 'Optimize operation schedule for CCS or DAC units to maximize captured CO₂ per cost and minimize grid impact.',
        'details_page': 'project_carbon_capture'
    },
    {
        'title': 'Adversarial ML Defense Systems',
        'description': 'Detect and mitigate adversarial attacks against deployed ML models across perception and NLP systems.',
        'details_page': 'project_adversarial_ml'
    },
    {
        'title': 'AI Policy Sandbox Simulator',
        'description': 'Provide a sandbox to simulate public policy outcomes using AI models before real-world rollout.',
        'details_page': 'project_policy_sandbox'
    },
    {
        'title': 'Biodiversity Early Warning AI',
        'description': 'Detect early signs of ecosystem collapse using multimodal sensing and predictive models to trigger conservation actions.',
        'details_page': 'project_biodiversity_ai'
    },
]

research_data = [
    {
        'title': 'Federated Learning for Privacy-Preserving Credit Scoring Across Financial Institutions',
        'description': 'Builds a federated learning system enabling banks to collaboratively train robust credit models without sharing raw data, enhancing fairness and generalizability.',
        'details_page': 'paper_federated_credit'
    },
    {
        'title': 'Energy-Aware Neural Architecture Search for Edge AI Deployment',
        'description': 'Introduces energy-optimized NAS frameworks to design lightweight yet powerful AI models for IoT/edge computing.',
        'details_page': 'paper_edge_ai_nas'
    },
    {
        'title': 'Causal Representation Learning for Predicting Long-Term Treatment Outcomes in Multi-Disease Patients',
        'description': 'Uses causal ML to model treatment interactions across chronic diseases for personalized long-term outcome prediction.',
        'details_page': 'paper_causal_health'
    },
    {
        'title': 'Adversarial Machine Learning for Cybersecurity in Military IoT Systems',
        'description': 'Develops adversarial-resilient ML defenses tailored to defense IoT networks.',
        'details_page': 'paper_adversarial_cybersecurity'
    },
    {
        'title': 'AI-Driven Multimodal Risk Modeling for Decentralized Finance (DeFi) Systems',
        'description': 'Introduces multimodal ML models that fuse blockchain transaction graphs, social sentiment, and liquidity flow for risk prediction.',
        'details_page': 'paper_defi_risk'
    },
    {
        'title': 'Low-Resource Medical Imaging Diagnosis Using Generative Self-Supervised Learning',
        'description': 'Develops generative SSL techniques for accurate diagnosis in low-resource settings, democratizing AI healthcare access.',
        'details_page': 'paper_low_resource_med'
    },
    {
        'title': 'Quantum-Inspired Machine Learning for Scalable Graph Neural Networks',
        'description': 'Applies quantum-inspired algorithms to improve efficiency and scalability of GNNs.',
        'details_page': 'paper_quantum_gnn'
    },
    {
        'title': 'AI-Driven Dynamic Carbon Capture Optimization Using Real-Time Energy and Weather Data',
        'description': 'Builds AI systems to optimize carbon capture timing for efficiency and cost savings.',
        'details_page': 'paper_carbon_capture_opt'
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

@app.route('/project/blockchain_ai')
def project_blockchain_ai():
    return render_template('blockchain_ai.html')

@app.route('/project/default')
def project_default():
    return render_template('project_default.html')

@app.route('/project/sme_twins')
def project_sme_twins():
    return render_template('project_sme_twins.html')

@app.route('/project/creditworthiness')
def project_creditworthiness():
    return render_template('project_creditworthiness.html')

@app.route('/project/self_healing')
def project_self_healing():
    return render_template('project_self_healing.html')

@app.route('/project/supply_chain')
def project_supply_chain():
    return render_template('project_supply_chain.html')

@app.route('/project/carbon_capture')
def project_carbon_capture():
    return render_template('project_carbon_capture.html')

@app.route('/project/adversarial_ml')
def project_adversarial_ml():
    return render_template('project_adversarial_ml.html')

@app.route('/project/policy_sandbox')
def project_policy_sandbox():
    return render_template('project_policy_sandbox.html')

@app.route('/project/biodiversity_ai')
def project_biodiversity_ai():
    return render_template('project_biodiversity_ai.html')

@app.route('/research/default')
def research_default():
    return render_template('research_default.html')

@app.route('/paper/federated_credit')
def paper_federated_credit():
    return render_template('paper_federated_credit.html')

@app.route('/paper/causal_health')
def paper_causal_health():
    return render_template('paper_causal_health.html')

@app.route('/paper/edge_ai_nas')
def paper_edge_ai_nas():
    return render_template('paper_edge_ai_nas.html')

@app.route('/paper/adversarial_cybersecurity')
def paper_adversarial_cybersecurity():
    return render_template('paper_adversarial_cybersecurity.html')

@app.route('/paper/defi_risk')
def paper_defi_risk():
    return render_template('paper_defi_risk.html')

@app.route('/paper/low_resource_med')
def paper_low_resource_med():
    return render_template('paper_low_resource_med.html')

@app.route('/paper/quantum_gnn')
def paper_quantum_gnn():
    return render_template('paper_quantum_gnn.html')

@app.route('/paper/carbon_capture_opt')
def paper_carbon_capture_opt():
    return render_template('paper_carbon_capture_opt.html')

@app.route('/api_docs')
def api_docs():
    return render_template('api_docs.html')

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


