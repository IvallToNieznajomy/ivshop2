import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import VueTailwind from 'vue-tailwind'
import { settings } from './vue-tailwind-config'
import axios from 'axios'

Vue.config.productionTip = false

Vue.use(VueTailwind, settings)

axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
