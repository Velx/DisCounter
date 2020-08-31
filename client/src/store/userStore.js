import axios from "../../axiosConfig";

class User {
  constructor (token, emailNotification) {
    this.token = token
    this.emailNotification = emailNotification
  }
}

export default {
  state: {
    user: null
  },
  mutations: {
    setUser (state, payload) {
      state.user = payload
    },
    logout (state) {
      state.user = null
    },
    setEmailNotification (state, payload) {
      state.user.emailNotification = payload
    },
    setBrowserNotification (state, payload) {
      state.user.browserNotification = payload
    }
  },
  actions: {
    async register ({ commit }, { login, email, password }) {
      commit('clearError')
      commit('setLoading', true)
      try {
        await axios.post(
            'users/',
            {
              username: login,
              email: email,
              password: password
            })
        commit('setLoading', false)
      } catch (err) {
        commit('setLoading', false)
        // commit('setError', err.message)
        commit('setError', err.response.status)
        throw err
      }
    },
    async login ({ commit, dispatch }, { login, password }) {
      commit('clearError')
      commit('setLoading', true)
      try {
        const resp = await axios.post(
            'login/',
            {
              username: login,
              password: password
            })
        commit('setUser', new User(resp.data.token, resp.data.e_notifications))
        dispatch('loadProducts')
        commit('setLoading', false)
      } catch (err) {
        commit('setLoading', false)
        commit('setError', err.response.status)
        // commit('setError', err.message)
        throw err
      }
    },
    async activateAccount({ commit }, { token }) {
      commit('clearError')
      commit('setLoading', true)
      try {
        await axios.get(
            `users/${token}/activate`
        )
        commit('setError', 'Your account was activated')
        commit('setColor', 'success')
        commit('setLoading', false)
      } catch (err) {
        if (err.response.status === 404) {
          commit('setError', 'Your activation token is expired. Perform registration again')
          commit('setLoading', false)
        } else {
          commit('setError', err.response.status)
          commit('setLoading', false)
          // commit('setError', err.message)
          throw err
        }
      }
    },
    async updateUser ({commit, state}, {email, password, emailNotification}) {
      commit('clearError')
      commit('setLoading', true)
      try {
        await axios.patch(
            `users/partial/`,
            {email: email,
              password: password,
              e_notifications: emailNotification
            },
            {
              headers : {
                'Authorization': 'Token ' + state.user.token
              }
            }
        )
        commit('setLoading', false)
      } catch (err) {
        commit('setError', err.response.status)
        commit('setLoading', false)
        // commit('setError', err.message)
        throw err
      }
    },
    logout ({ commit }) {
      commit('logout')
      commit('setProducts', [])
    },
    async resetRequest({ commit }, { email }) {
      commit('clearError')
      commit('setLoading', true)
      try {
        await axios.post(
            `password-reset`,
            {email: email}
        )
        commit('setError', 'Email was sent')
        commit('setColor', 'success')
        commit('setLoading', false)
      } catch (err) {
        commit('setError', err.response.status)
        commit('setLoading', false)
        // commit('setError', err.message)
        throw err
      }
    },
    async resetPasswordPermission ({ commit }, { token }) {
      commit('clearError')
      commit('setLoading', true)
      try {
        await axios.get(
            `password-reset/${token}`
        )
        commit('setLoading', false)
      } catch (err) {
        if (err.response.status === 404) {
          commit('setError', 'Your activation token is expired.')
          commit('setLoading', false)
        } else {
          commit('setError', err.response.status)
          commit('setLoading', false)
          // commit('setError', err.message)
        }
        throw err
      }
    },
    async resetPasswordSet({ commit }, { token, password }) {
      commit('clearError')
      commit('setLoading', true)
      try {
        await axios.post(
            `password-reset/${token}`,
            {password: password}
        )
        commit('setLoading', false)
      } catch (err) {
        if (err.response.status === 404) {
          commit('setError', 'Your activation token is expired.')
          commit('setLoading', false)
        } else {
          commit('setError', err.response.status)
          commit('setLoading', false)
          // commit('setError', err.message)
        }
        throw err
      }
    },
    async saveNotificationToken({ commit, state }, { token }) {
      const payload = {
        registration_id: token,
        type: 'web'
      }
      commit('clearError')
      commit('setLoading', true)
      await axios.post("notification-token/",
          payload,
          {
            headers : {
              'Authorization': 'Token ' + state.user.token
            }
          })
          .then(() => {
            console.log('Successfully saved notification token!')
          })
          .catch((error) => {
            console.log('Error: could not save notification token')
            if (error.response) {
              console.log(error.response.status)
              // Most of the time a "this field must be unique" error will be returned,
              // meaning that the token already exists in db, which is good.
              if (error.response.data.registration_id) {
                for (let err of error.response.data.registration_id) {
                  console.log(err)
                }
              } else {
                console.log('No reason returned by backend')
              }
              // If the request could not be sent because of a network error for example
            } else if (error.request) {
              console.log('A network error occurred.')
              // For any other kind of error
            } else {
              console.log(error.message)
            }
          })
      commit('setLoading', false)
    }
  },
  getters: {
    user (state) {
      return state.user
    },
    isUserLoggedIn (state) {
      return state.user !== null
    },
    emailNotification (state) {
      try {
        return state.user.emailNotification
      } catch (err) {
        return null
      }
    }
  }
}