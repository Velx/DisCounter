import Vue from 'vue'
import Vuex from 'vuex'

import userStore from "./userStore";
import sharedStore from "./sharedStore";
import productsStore from "./productsStore";

import createPersisted from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'

import createPersistedState from "./presistent"

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    userStore,
    sharedStore,
    productsStore
  },
  plugins: [
    createPersistedState({
      paths: ['userStore'],
      getState: (key) => Cookies.getJSON(key),
      setState: (key, state) => Cookies.set(key, state, { expires: 3, secure: false, samesite: 'strict'})  //  TODO: secure: true after move to https
    }),
    createPersisted({
      strictMode: false,
      // Specify here which modules should be persistent:
      modules: [productsStore]
    })
  ],
  state: {
  },
  mutations: {
  },
  actions: {
  }
})
