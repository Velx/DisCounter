import Vue from 'vue'
import VueRouter from 'vue-router'
import multiguard from 'vue-router-multiguard'

import {activate, passwordResetPermission, authGuard, notAuthGuard} from './guards'

import List from '../views/Products/List'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: List,
  },
  {
    path: '/add',
    name: 'Add',
    component: () => import("../views/Products/Add"),
    beforeEnter: authGuard
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import("../views/Auth/Login"),
    beforeEnter: notAuthGuard
  },
  {
    path: '/registration',
    name: 'Registration',
    component: () => import("../views/Auth/Registration"),
    beforeEnter: notAuthGuard
  },
  {
    path: '/activate/:token',
    name: 'Activation',
    beforeEnter: multiguard([activate, notAuthGuard])
  },
  {
    path: '/password-reset',
    name: 'Password reset',
    component: () => import("../views/Auth/PasswordReset"),
    beforeEnter: notAuthGuard
  },
  {
    path: '/password-reset/:token',
    name: 'Password set',
    component: () => import("../views/Auth/PasswordSet"),
    beforeEnter: multiguard([passwordResetPermission, notAuthGuard])
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
