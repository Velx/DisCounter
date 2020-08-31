import store from '../store'


export function authGuard(to, from, next) {
  if (store.getters.isUserLoggedIn) {
    next()
  } else {
    next('/login?loginError=true')
  }
}

export function notAuthGuard(to, from, next) {
  if (!store.getters.isUserLoggedIn) {
    next()
  } else {
    next('/')
  }
}

export function activate(to, from, next) {
  store.dispatch('activateAccount',{token: to.params.token})
      .then(() => {})
      .catch(() => {})
  next('/')
}

export function passwordResetPermission(to, from, next) {
  store.dispatch('resetPasswordPermission', {token: to.params.token})
      .then(() => {next()})
      .catch(() => {next('/')})
}