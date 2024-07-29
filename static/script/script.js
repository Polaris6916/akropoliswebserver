// Obsolète, car maintenant c'est la requête au serveur getComputeScore qui est utilisée
function onSubmitForm() {
  encodeArray(); // Refresh de l'encodage des valeurs du tableau
  return true; // Renvoyer true permet d'autoriser la soumession du formulaire normalement
}

async function getConfig() {
  const response = await fetch('/config');
  const config = await response.json();
  return config.serverUrl;
}

// encode le tableau en une chaîne de caractères
function encodeArray() {
  // Init
  var boucle = true;
  let n = 0;
  var quartier="";
  var quartiersStr = ""

  while (boucle) {
    n++;
    quartier = "q" + n;

    const quartierNiv = document.getElementsByName(quartier); //Récupère l'ensemble des valeurs d'une ligne d'un tableau (grâce à leur nom q?) 
    
    if (quartierNiv.length > 0) { // Vérifie si la ligne est vide ou pas
      var line = encodeLine(quartierNiv);
      
      //Encodage par niveau -> ajout du séparateur ';' entre 2 niveaux
      if (n==1) {
        quartiersStr += line;
      } else {
        quartiersStr += ";" + line;
      }
    } else {
      boucle=false; // la ligne est vide, nous sommes donc arrivés à la fin du tableau
    }
  }

  document.getElementById("QuartiersStr").value = quartiersStr; //Assigne le champ caché avec le tableau encodé
}

// encode la ligne du tableau en une chaîne de caractères
function encodeLine(row) {
  var strLine = "";

  // Encode par Quartier -> ajoute le séparateur ',' entre 2 valeurs
  row.forEach((item, index) => {
    if (index == 0 ) {
      // Cas particulier de la valeur de la première colonne
      // C'est une balise TH et seule sa valeur textuelle nous intéresse
      strLine += item.innerText + "," ;
    } 
    else if (index == 5) {
      // Cas particulier de la valeur de la dernière colonne
      // il n'y a pas besoin d'ajouter un séparateur
      strLine += item.value;
    }
    else {
      // Cas standard
      // ajout de la valeur et du séparateur ','
      strLine += item.value + ",";
    }
  })

  return strLine;
}

// Supprime la dernière ligne du tableau
function deleteRow(){
  const table = document.getElementById("Quartiers");
  const rowToDelete = table.rows.length-1; // On cherche à supprimer la dernière ligne du tableau

  if (rowToDelete > 1) {          // Vérifie si il y a assez de ligne dans le tableau
    table.deleteRow(rowToDelete); // Permet de supprimer la ligne du tableau

    //Permet de desactiver le bouton si 1 seul niveau restant
    if(rowToDelete == 2){
      const btn = document.getElementById("DeleteRow"); 
      btn.setAttribute("disabled", true);
    }
  }

}

// Ajouter une ligne supplémentaire au tableau
function addRow(){
  const table = document.getElementById("Quartiers");
  const rowToAdd = table.rows.length;

  const newRow = table.insertRow(rowToAdd); //Création d'une nouvelle ligne vide en dernière position
  const rowName = "q" + (rowToAdd); // définition du name de la nouvelle ligne
  
  //Construction d'une nouvelle ligne d'un tableau
  var cells ="";
  for (let i = 0; i < 5; i++) {
    cells += newCell(rowName);
  }
  const rowContent = '<tr>'
                        + '<th scope="row" name="' + rowName + '">' + (rowToAdd) + '</th>'
                        + cells
                    + '</tr>';
  
  newRow.innerHTML = rowContent; // Assigne le contenu HTML de la nouvelle ligne

  //Permet de réactiver le bouton moins
  const btn = document.getElementById("DeleteRow");
  btn.removeAttribute("disabled");
}

//Fonction qui permet de créer le code HTML des différentes cellules de la nouvelle ligne pour le tableau
function newCell(rowName){
  return '<td><input type="number" name="' + rowName + '" class="form-control" min="0" max="30" value="0"></td>'
}

// Appel au serveur de la méthode permettant d'évaluer le score à partir des paramètres transmis
async function getComputeScore() {
  const SERVER_URL = await getConfig();

  encodeArray(); // Refresh de l'encodage des valeurs du tableau

  //création de l'url avec les parametres dans la route
  var url = SERVER_URL + "/getScore.html/" + document.getElementById("Username").value //Il faut remplacer par l'adresse ip du fichier js
          + "/" + document.getElementById("Stones").value                                         //(pour une utilisation uniquement local : http://localhost:5400/) 
          + "/" + document.getElementById("Stars").value
          + "/" + document.getElementById("QuartiersStr").value;
  
  
  const response = await fetch(url);
  const myScore = await response.text(); //extract text answer from the http response
  console.log(myScore);
  document.getElementById("scoreAffichage").innerText = "Bravo "+ document.getElementById("Username").value + ", votre score est de : " + myScore; //Affichage du score au joueur

}