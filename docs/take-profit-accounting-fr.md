# Comptabilité du take-profit : que signifie réellement « +0,95 USDC net » ?

Cette note est la référence comptable du dépôt. Le rejeu historique par zones utilise une cible de **+0,95 USDC de profit net par mise de 1,00 USDC**. Le prototype visuel est séparé et utilise +0,96 USDC.

## La distinction essentielle

**Un TP « +0,95 net » désigne le profit conservé après récupération de la mise initiale et couverture des frais applicables. Ce n'est pas le montant total reçu lors de la vente.** Les recettes de vente doivent couvrir la sortie de trésorerie initiale et laisser 0,95 USDC supplémentaires dans le compte.

Polymarket ne rembourse pas littéralement les frais d'entrée. Ils sont récupérés économiquement uniquement si les recettes nettes de vente couvrent la mise **et** les frais d'entrée, plus le profit visé. Les frais de sortie sont déjà déduits des recettes nettes de vente.

## Exemple : mise de 1 USDC à un prix d'entrée de 0,20

Hypothèses propres à cet exemple :

- Mise : 1,0000 USDC
- Prix d'entrée : 0,20 USDC par part
- Parts achetées : `1,00 / 0,20 = 5,00`
- Taux du modèle de frais : `0,07`, avec `frais = parts × taux × prix × (1 − prix)`
- Profit net visé : +0,9500 USDC
- Aucun autre coût n'est inclus. Les frais réels applicables et les exécutions doivent être vérifiés pour le marché et l'ordre concernés.

### Argent qui sort du compte à l'achat

| Élément | Montant |
|---|---:|
| Mise utilisée pour acheter 5 parts | 1,0000 USDC |
| Frais d'entrée selon l'hypothèse indiquée | 0,0560 USDC |
| **Sortie de trésorerie initiale totale** | **1,0560 USDC** |

Calcul des frais d'entrée : `5 × 0,07 × 0,20 × (1 − 0,20) = 0,0560 USDC`.

### Recettes nettes de vente nécessaires pour réaliser +0,95

| Élément | Montant |
|---|---:|
| Récupération économique de la mise et du coût d'entrée (pas un remboursement séparé des frais) | 1,0560 USDC |
| Profit net supplémentaire visé | 0,9500 USDC |
| **Recettes de vente requises après frais de sortie** | **2,0060 USDC** |

Le flux de trésorerie est donc :

`P&L net = recettes de vente après frais de sortie − mise − frais d'entrée`

`P&L net = 2,0060 − 1,0000 − 0,0560 = +0,9500 USDC`

C'est le sens exact de « +0,95 net ». Les 2,0060 USDC sont crédités au solde de trésorerie **après déduction des frais de sortie**. Le produit brut de vente est supérieur du montant des frais de sortie.

Avec le même modèle de frais à 0,07, le prix de sortie calculé pour cet exemple est d'environ `0,418232` ; le produit brut serait d'environ `2,091160`, les frais de sortie d'environ `0,085160` et les recettes nettes de `2,006000`. Ce sont des résultats du modèle sous l'hypothèse de frais énoncée, pas la garantie qu'un ordre réel pourrait être exécuté à ce prix.

### Évolution du solde

| Étape | Solde de trésorerie |
|---|---:|
| Avant le trade | 4,7700 USDC |
| Après paiement de la mise et des frais d'entrée | 4,7700 − 1,0560 = 3,7140 USDC |
| Après la vente, avec 2,0060 USDC de recettes nettes | 3,7140 + 2,0060 = 5,7200 USDC |
| **Variation nette depuis le départ** | **+0,9500 USDC** |

## Et en cas de perte totale ?

Si la position expire sans valeur et qu'il n'y a aucune récupération par vente ou règlement, la mise et les frais d'entrée sont perdus. Dans cet exemple, la perte est donc `−1,0560 USDC`, et pas seulement `−1,00 USDC`.

**Ne considère pas automatiquement chaque trade qui n'atteint pas le TP comme une perte totale.** Dans la règle de rejeu « prendre le profit si la cible est atteinte, sinon conserver jusqu'à la résolution », un trade qui manque le TP peut quand même recevoir un paiement au règlement. Les sorties partielles et les autres règles de sortie produisent également des résultats différents. L'hypothèse de perte totale ne s'applique que si toute la position et les frais d'entrée sont effectivement perdus.

## Seuil de rentabilité simplifié

Si, et seulement si, chaque trade gagnant rapporte exactement `+0,9500 USDC` net et chaque trade perdant coûte exactement `−1,0560 USDC`, sans coût supplémentaire ni autre type de résultat, le taux de réussite théorique au seuil de rentabilité est :

`w × 0,95 − (1 − w) × 1,056 = 0`

`w = 1,056 / (0,95 + 1,056) = 0,52642… ≈ 52,64 %`

Dans ce modèle binaire simplifié :

- Au-dessus de 52,64 % : espérance arithmétique positive, avant les coûts omis et les erreurs d'exécution.
- À 52,64 % : espérance à l'équilibre.
- En dessous de 52,64 % : espérance arithmétique négative.

**Il ne faut pas comparer directement ce seuil de 52,64 % au taux de touchée historique de 46,7 % comme s'il s'agissait de la même mesure.** Le taux de touchée mesure la fréquence à laquelle le seuil de TP a été atteint dans une règle de rejeu. Ce n'est pas automatiquement le taux de réussite de la stratégie ; dans la règle « sinon conserver jusqu'à la résolution », les trades qui ne touchent pas la cible ne perdent pas tous nécessairement la totalité de la mise. Il faut calculer l'espérance empirique à partir du P&L net réellement modélisé pour chaque trade.

## Limites liées aux frais et à l'exécution

- Le taux `0,07` est une hypothèse employée dans le modèle de rejeu/prototype décrit. Il ne faut pas le traiter comme un taux universel ou permanent pour tous les marchés ou ordres Polymarket.
- Le prix du calcul n'est pas un prix d'exécution garanti. Le spread, la profondeur, la latence, les exécutions partielles, la position dans la file, le type d'ordre et les frais réels peuvent changer le résultat.
- Voir un prix cible sur un graphique ne prouve pas que la position aurait pu être vendue à ce prix et dans la quantité nécessaire.
- Dans la mesure du possible, publier séparément la valeur brute de vente, les frais de sortie, les recettes nettes de vente, la sortie initiale de trésorerie et le P&L net final.

## État de reproductibilité

Cet exemple est une illustration arithmétique explicite. Les tableaux historiques par zone dans `../data/` sont retranscrits de rapports antérieurs de l'auteur et n'ont pas été reproduits indépendamment par ce dépôt. L'espérance rapportée pour F45 était négative selon les deux règles de sortie comparées. Ces tableaux n'établissent aucun avantage rentable.
