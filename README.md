# 🏰 Labyrinthe - Jeu de Navigation Interactive

Un jeu de labyrinthe interactif développé en Python utilisant la bibliothèque Turtle Graphics, offrant une expérience de navigation immersive avec résolution automatique et contrôle manuel.

## 🎮 Fonctionnalités

### Modes de Jeu
- **Mode Manuel** : Contrôlez la tortue avec les flèches directionnelles
- **Mode Automatique** : Regardez l'IA résoudre le labyrinthe automatiquement

### Interface Graphique
- Affichage coloré du labyrinthe avec identification visuelle des types de cellules :
  - 🟫 **Murs** : Cases grises (#404040)
  - ⬜ **Passages** : Cases blanches (#FFFFFF)
  - 🟡 **Entrée** : Case jaune (#e7eca3)
  - 🟢 **Sortie** : Case verte (#9de19a)
  - 🔵 **Carrefours** : Cases cyan (#57F8C8)
  - 🟣 **Impasses** : Cases violettes (#bca9e1)

### Fonctionnalités Techniques
- Lecture de fichiers de labyrinthe personnalisés (format `.laby`)
- Détection automatique des types de cellules
- Système de navigation avec validation des mouvements
- Algorithme de résolution par exploration
- Effets sonores intégrés
- Interface de menu interactive

## 🚀 Installation et Lancement

### Prérequis
- Python 3.x
- Bibliothèques requises :
  - `turtle` (incluse dans Python)
  - `winsound` (Windows uniquement, pour les sons)
  - `math`
  - `time`

### Lancement
```bash
python Main.py
```

## 📁 Structure du Projet

```
labyrinthe/
├── Main.py              # Point d'entrée principal
├── Affichage.py         # Gestion de l'affichage graphique
├── navigation.py        # Logique de déplacement et résolution
├── Menu.py              # Interface du menu principal
├── dicoJeu.py          # Stockage des données de jeu
├── lireLaby.py         # Lecture des fichiers de labyrinthe
├── laby1.laby          # Fichier de labyrinthe exemple
├── assets/
│   ├── bg.gif          # Image de fond
│   ├── mainmenu.gif    # Logo du menu
│   ├── victory.gif     # Image de victoire
│   ├── mainsound.wav   # Musique de fond
│   ├── move.wav        # Son de déplacement
│   └── victory.wav     # Son de victoire
```

## 🎯 Utilisation

### 1. Menu Principal
Au lancement, vous accédez au menu principal avec trois options :
- **Manuelle** : Mode de jeu contrôlé par le joueur
- **Automatique** : Mode de résolution automatique
- **Quitter** : Fermer l'application

### 2. Contrôles (Mode Manuel)
- **↑** : Déplacement vers le haut
- **↓** : Déplacement vers le bas
- **←** : Déplacement vers la gauche
- **→** : Déplacement vers la droite

### 3. Format des Fichiers de Labyrinthe
Les fichiers `.laby` utilisent le format suivant :
```
#########
#x......#
#.####..#
#....#..#
#.##.#.X#
#########
```
- `#` : Mur
- `.` : Passage libre
- `x` : Entrée (minuscule)
- `X` : Sortie (majuscule)

## 🔧 Fonctionnalités Techniques Avancées

### Algorithme de Résolution
L'algorithme automatique utilise une approche d'exploration récursive :
- Détection des carrefours et impasses
- Mémorisation des chemins explorés
- Retour automatique en cas d'impasse
- Recherche du chemin optimal

### Système de Détection
- **Carrefours** : Cellules avec 3+ connexions
- **Impasses** : Cellules avec 1 seule connexion
- **Passages** : Cellules avec 2 connexions
- Validation des mouvements en temps réel

### Interface Interactive
- Conversion pixel ↔ cellule pour les clics souris
- Système de boutons personnalisés
- Gestion des événements clavier et souris

## 🎨 Personnalisation

### Modifier la Taille du Labyrinthe
Dans `Main.py`, ajustez la variable `cote` :
```python
cote = 60  # Taille des cellules en pixels
```

### Changer le Fichier de Labyrinthe
Modifiez la variable `fileName` dans `Main.py` :
```python
fileName = "votre_labyrinthe.laby"
```

### Personnaliser les Couleurs
Les couleurs sont définies dans `Affichage.py`, fonction `afficheGraphique()`.

## 🐛 Dépannage

### Problèmes Audio (Windows)
Si les sons ne fonctionnent pas, vérifiez que les fichiers audio sont présents dans le répertoire du projet.

### Problèmes d'Affichage
Assurez-vous que tous les fichiers image (.gif) sont présents et que Turtle Graphics est correctement installé.

## 👥 Crédits

**Développé par :** Chamberlan Quentin en 2022

## 📄 Licence

Ce projet est sous licence libre. Vous êtes libres de l'utiliser, le modifier et le distribuer.
