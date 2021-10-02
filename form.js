import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
    apiKey: "AIzaSyC7Y4NQcEyj1j3hm2xgf3jrN5kAW4B-vgc",
    authDomain: "modal-dbe5e.firebaseapp.com",
    databaseURL: "https://modal-dbe5e-default-rtdb.firebaseio.com",
    projectId: "modal-dbe5e",
    storageBucket: "modal-dbe5e.appspot.com",
    messagingSenderId: "696208452034",
    appId: "1:696208452034:web:00b4cae826d1a7c6cc8e5b",
    measurementId: "G-9STDBTTEC7"
  };
  
  const functions = require('firebase-functions');
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

function signUp(){
    var email = document.getElementById("email");
    var password = document.getElementById("password");

    const promise = auth.createUserWithEmailAndPassword(email.value, password.value);
    promise.catch(e=>alert(e.message));

    alert("Signed Up");

}

function signIn(){
    var email = document.getElementByEd("email");
    var password = document.getElementByEd("password");

    const promise = auth.createUserWithEmailAndPassword(email.value, password.value);
    promise.catch(e=>alert(e.message));


}

function singOut(){
    auth.signOut()
    alert("Signed Out");
}

auth.ouAuthStateChanged(function(user){
    if(user){
        var email = user.email;
        alert("Active User " + email);
    }else{
        alert("No Active User")
    }

})

