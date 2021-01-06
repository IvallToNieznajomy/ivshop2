import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import VueTailwind from 'vue-tailwind'
import { settings } from './vue-tailwind-config'

Vue.config.productionTip = false

Vue.use(VueTailwind, settings)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
