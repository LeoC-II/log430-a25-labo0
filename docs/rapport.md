# Rapport laboratoire 0

## Question 1: Échec d'un test
Lors de l'échec d'un test, les détails de l'erreur sont affichés, incluant la différence entre la réponse attendue
et la réponse ici.
![Screenshot de l'échec](echec-pytest.jpg)

## Question 2: Étapes du CI
La première étape est celle du "setup" qui sert à mettre en place l'environnement
du runtime qui sera utilisée pour rouler le reste des étapes

![Set-up](set-up-ci.jpg)

La deuxième étape est celle du "checkout" qui sert à copier le commit qui vient
d'être commit et de l'importer dans l'environnement qui vient d'être
créé.

![Checkout](checkout-ci.jpg)