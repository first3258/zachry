import { createRouter, createWebHistory } from 'vue-router'
import Home from '../view/Home.vue'
import Login from '../view/Login.vue'

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
