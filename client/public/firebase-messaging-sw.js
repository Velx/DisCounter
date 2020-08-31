// eslint-disable-next-line no-undef
importScripts('https://www.gstatic.com/firebasejs/7.15.0/firebase-app.js');
// eslint-disable-next-line no-undef
importScripts('https://www.gstatic.com/firebasejs/7.15.0/firebase-messaging.js');

const config = {
  apiKey: "AIzaSyBEj1Soso2Un1_9d-QnjQI7vLVYL6E4HqQ",
  authDomain: "discounter.firebaseapp.com",
  databaseURL: "https://discounter.firebaseio.com",
  projectId: "discounter",
  storageBucket: "discounter.appspot.com",
  messagingSenderId: "642427961332",
  appId: "1:642427961332:web:3ded7ef52f192355afc3a1",
  measurementId: "G-7YKGMVBD1R"
};
// eslint-disable-next-line no-undef
firebase.initializeApp(config);

// eslint-disable-next-line no-unused-vars,no-undef
const messaging = firebase.messaging();