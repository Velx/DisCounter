export default {
  state: {
    loading: false,
    error: null,
    errorColor: 'error',
    pageLoading: false
  },
  mutations: {
    setLoading (state, payload) {
      state.loading = payload
    },
    setError (state, payload) {
      state.error = payload
    },
    setColor (state, payload) {
      state.errorColor = payload
    },
    clearError (state) {
      state.error = null
      state.errorColor = 'error'
    },
    setPageLoading (state, payload) {
      state.pageLoading = payload
    }
  },
  actions: {
    setLoading ({ commit }, payload) {
      commit('setLoading', payload)
    },
    setError ({ commit }, payload) {
      commit('setError', payload)
    },
    clearError ({ commit }) {
      commit('clearError')
    },
    setPageLoading ({ commit }, payload) {
      commit('setPageLoading', payload)
    }
  },
  getters: {
    loading (state) {
      return state.loading
    },
    error (state) {
      return state.error
    },
    errorColor (state) {
      return state.errorColor
    },
    pageLoading (state) {
      return state.pageLoading
    }
  }
}