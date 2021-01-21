import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Faq from '../views/Faq.vue'
import Login from '../views/Login.vue'
import Error500 from '../views/Error500.vue'
import DiscordCallback from '../views/DiscordCallback.vue'
import Panel from '../views/Panel.vue'
import SelectShop from '../views/SelectShop.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/faq',
    name: 'Faq',
    component: Faq
  },
  {
    path: '/login',
    name: 'Login page',
    component: Login
  },
  {
    path: '/500',
    name: 'Unexcepted error',
    component: Error500
  },
  {
    path: '/discord/callback',
    name: 'Discord oauth2 callback',
    component: DiscordCallback
  },
  {
    path: '/select_shop',
    name: 'Select shop to enter to panel',
    component: SelectShop,
    meta: { requiresAuth: true }
  },
  {
    path: '/panel/:id',
    name: 'Panel',
    component: Panel
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('accessToken')) {
      next()
    } else {
      next('/auth/not-allowed')
    }
  } else {
    next()
  }
})

export default router
