import axios from "../../axiosConfig";

export default {
  state: {
    products: [],
    product: null
  },
  mutations: {
    setProducts (state, payload) {
      state.products = payload
    },
    setProduct (state, payload) {
      state.products.push(payload)
      state.product = payload
    },
    delProduct (state, payload) {
      state.products = state.products.filter(product => product.api_id === payload)
      state.product = null
    }
  },
  actions: {
    async addProduct ({commit, rootState}, {aliUrl}) {
      commit('clearError')
      commit('setLoading', true)
      try {
        const resp = await axios.post(
            'products/',
            {
              ali_url: aliUrl
            },
            {
              headers : {
                'Authorization': 'Token ' + rootState.userStore.user.token
              }
            })
        commit('setProduct', resp.data)
        commit('setLoading', false)
      } catch (err) {
        console.log(err.response)
        commit('setLoading', false)
        commit('setError', err.response.status)
        throw err
      }
    },
    async loadProducts ({commit, rootState}) {
      commit('clearError')
      commit('setLoading', true)
      try {
        const resp = await axios.get(
            'products/',
            {
              headers : {
                'Authorization': 'Token ' + rootState.userStore.user.token
              }
            })
        commit('setProducts', resp.data)
        commit('setLoading', false)
      } catch (err) {
        commit('setLoading', false)
        commit('setError', err.response.status)
        throw err
      }
    },
    async deleteProduct ({ commit, rootState }, { api_id }) {
      commit('clearError')
      commit('setLoading', true)
      try {
        await axios.delete(
            'products/' + api_id + '/',
            {
              headers : {
                'Authorization': 'Token ' + rootState.userStore.user.token
              }
            })
        commit('delProduct', api_id)
        commit('setLoading', false)
      } catch (err) {
        commit('setLoading', false)
        commit('setError', err.response.status)
        throw err
      }
    }
  },
  getters: {
    getDiscountedProducts (state) {
      return state.products.filter(product => product.current_price !== null)
    },
    getNormalProducts (state) {
      return state.products.filter(product => product.current_price === null && product.price !== null)
    },
    getNAProducts(state) {
      return state.products.filter(product => product.price === null)
    },
    getProduct (state) {
      return state.product
    }
  }
}