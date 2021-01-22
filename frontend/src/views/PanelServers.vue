<template>
  <div class="PanelServer">

  </div>
</template>

<script>
import axios from 'axios'

import {
  TButton, TModal, TInput
} from 'vue-tailwind/dist/components'

export default {
  name: 'SelectShop',
  components: {
    TButton, TModal, TInput
  },
  data: function () {
    return {
      shops: null,
      showModal: false,
      shopName: ''
    }
  },
  async created () {
    this.getServers()
  },
  methods: {
    getServers () {
      if (!localStorage.getItem('accessToken')) {
        this.$router.push('500')
      }

      axios.get('/panel/user_servers/').then((response) => {
        this.shops = response.data
      }).catch((error) => {
        console.log(error); this.$router.push('/500')
      })
    },

    createShop () {
      const data = { name: this.shopName }
      axios.post('/panel/shops/create_shop/', data).then((response) => {
        this.showModal = false
        this.getShops()
        this.$message.success('Sklep został utworzony.')
        this.shopName = ''
      }).catch((error) => {
        if (error.response.status === 411) {
          this.$message.error('Uzupełnij dane.')
        } else {
          console.log(error.response)
          this.$router.push('/500')
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
