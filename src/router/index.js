import { createRouter, createWebHistory } from 'vue-router'
import Home from '../view/Home.vue'
import Page2 from '../view/Page2.vue'

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/page2',
    component: Page2
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
