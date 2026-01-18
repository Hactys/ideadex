
# IdeaDex 🧠✨
_Le Tinder de l’innovation pour faciliter l’idéation et le brainstorming_

---

## ⚙️ Fonctionnement

Le projet est construit avec `hatch` s'il n'est pas installé, utiliser la commande :
```bash
python -m pip install hatch
```

Puis :
```bash
hatch -vv run cli
```
⚠️ Cette commande peut prendre beaucoup de temps la première fois, il faut être patient. Le flag `-vv` demande à `hatch` d'être "verbeux" et donc de logger ce qu'il fait, on pourra s'en dispenser pour les prochains appels.

---

## 🎯 Objectif du projet

**IdeaDex** est une application écrite en **Python** dont le but est de :
- manipuler une collection de **cartes d’innovation**,
- permettre aux utilisateurs de **liker**, **opposer** ou **relier** des idées,
- explorer les liens entre idées pour stimuler la créativité.

> ⚠️ Ce projet est avant tout **pédagogique** :
> **le chemin compte plus que la destination**.
> L’objectif principal est d’apprendre Python par la pratique, pas de produire une application parfaite.

---

## 🧩 Vision MVP (Minimum Viable Product)

Le MVP doit permettre :

1. Charger des cartes depuis un fichier
2. Afficher une carte à l’utilisateur
3. Permettre une interaction simple (like / oppose / passer)
4. Enregistrer cette interaction
5. Recommencer avec une autre carte

Rien de plus.

---

## 🗂️ Fonctionnalités attendues (découpées)

---

## 1️⃣ Cartes (Ideas)

### 1.1 Structure d’une carte
Une carte contient :
- un identifiant unique
- un titre
- une description
- un ou plusieurs thèmes
- d'autres champs que le V trouvera pertinant

### 1.2 Chargement des cartes
- Les cartes sont stockées dans un fichier `cards.json` (et plus tard dans une base de donnée SQLite)
- Le programme doit être capable de :
  - charger toutes les cartes
  - les convertir en objets Python
  - vérifier leur validité minimale (id, titre, description)

---

## 2️⃣ Navigation et affichage

### 2.1 Sélection d’une carte
- Une carte est choisie à afficher :
  - soit aléatoirement
  - soit selon un critère simple (ex: thème)
- Une carte déjà vue peut être ignorée (optionnel MVP+)

### 2.2 Affichage (MVP)
Dans le MVP, l’affichage se fait via :
- la console (CLI)

Exemple :
```text
--------------------------
Impression 3D béton
Construction automatisée de bâtiments
Thèmes : construction, robotique
--------------------------
[1] Like
[2] Opposer
[3] Passer
```

---

## 3️⃣ Interactions utilisateur

### 3.1 Actions possibles

Sur chaque carte, l’utilisateur peut :
* 👍 Like : l’idée lui semble intéressante
* 👎 Opposer : l’idée lui semble peu pertinente
* ⏭️ Passer : aucune action enregistrée

### 3.2 Validation des entrées

* Le programme doit :
  * refuser les entrées invalides
  * redemander une action si nécessaire

---

## 4️⃣ Relations entre cartes

### 4.1 Types de relations

Chaque interaction crée une **relation** :
* `like`
* `oppose`
* `link` (réservé aux évolutions futures)

Une relation relie :
* une carte source
* une carte cible
* un type de relation

### 4.2 Stockage des relations

* Les relations sont stockées :
  * en mémoire (MVP)
  * ou dans un fichier JSON simple
  * plus tard dans une table SQL

---

## 5️⃣ Persistance (MVP)

### 5.1 Sauvegarde

* Chaque interaction est enregistrée
* Le format doit être lisible et simple (JSON)
* Avec de la maturité on mettra les données dans une DB SQLite.

### 5.2 Chargement

* Les relations existantes peuvent être rechargées au lancement et ajouté pendant l'exécution.

---

## 6️⃣ Boucle principale de l’application

Le programme suit le cycle suivant :
1. Charger les cartes
2. Afficher une carte
3. Demander une action
4. Enregistrer la relation si nécessaire
5. Passer à la carte suivante
6. Quitter proprement sur demande utilisateur

---

## 7️⃣ Tests (initiation)

### 7.1 Tests attendus

Au minimum :
* création d’une carte valide
* création d’une relation valide
* chargement des cartes depuis un fichier

### 7.2 Objectif des tests

* Vérifier que le code fonctionne
* Apprendre les bases des tests automatisés
* Dédramatiser les erreurs, erreur = apprentissage

---

## 🔜 Évolutions possibles (hors MVP)

> Ces fonctionnalités ne sont **pas obligatoires** pour le MVP.

* Interface web avec Dash
* Multi-utilisateur
* Authentification légère
* Visualisation du graphe d’idées
* Filtrage avancé par thème
* Recommandation d’idées liées
* Base de données SQLite
* Export des graphes
* Visualisation des graphes

---

## 🧠 Approche pédagogique recommandée

* Travailler par petites briques
* Tester souvent
* Lire le code à voix haute
* Ne pas chercher la perfection
* Poser des questions avant d’optimiser

---

## 🏁 Critère de réussite du MVP

Le MVP est considéré comme **réussi** si :

* l’utilisateur peut parcourir plusieurs cartes,
* interagir avec elles,
* et que ces interactions sont enregistrées,
* sans crash ni confusion majeure.

