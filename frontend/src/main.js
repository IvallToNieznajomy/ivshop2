import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import VueTailwind from 'vue-tailwind'
import { settings } from './vue-tailwind-config'
import axios from 'axios'
import Message from 'vue-m-message'
import 'vue-m-message/dist/index.css'

Vue.config.productionTip = false

Message.globals.options.showClose = true
Message.globals.options.position = 'top-right'

Vue.use(VueTailwind, settings)
Vue.use(Message)

axios.defaults.headers.Authorization = localStorage.accessToken
axios.defaults.baseURL = 'http://localhost:8000/'

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
