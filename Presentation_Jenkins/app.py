from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        "title": "Présentation de Jenkins",
        "header": "Découvrez Jenkins.",
        "subtitle_visible": "Jenkins permet :",
        "subtitle_hidden": "Jenkins c'est :",
        "items": [
            "Automatisation CI/CD.",
            "Intégration Continue.",
            "Livraison Continue.",
            "Configuration de Pipeline.",
            "Gestion des Plugins.",
            "Déploiement Automatisé.",
            "Tests Automatisés.",
            "Notifications.",
            "Monitoring.",
            "Sécurité.",
            "Collaboration.",
            "Documentation.",
            "Support Communautaire.",
            "Personnalisation.",
            "Rapports.",
            "Optimisation.",
            "Intégrations.",
            "Évolutivité.",
            "Innovation.",
            "Gestion des Versions.",
            "Support Multi-Platforme.",
            "Gestion des Environnements."
        ],
        "item_count": 22,
        "footer_title": "Fin.",
        "footer_text": "ʕ⊙ᴥ⊙ʔ Jenkins Présentation &copy; 2024",
        "jenkins_link": "https://www.jenkins.io/"
    }
    return render_template('template.html', **data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
