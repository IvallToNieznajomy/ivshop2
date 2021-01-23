<template>
  <div class="PanelServer">
    <div class="text-center mt-12">
      <div class="text-2xl">Serwery</div>
      <div class="flex justify-center mt-8">
        <t-button type="button" @click="showModal=true">
          Utwórz nowy serwer
        </t-button>
      </div>
      <div class="inline-flex justify-center flex-col flex-wrap md:flex-row">
        <t-card v-for="server in servers" :key="server.id" :header="server.name" class="flex-auto max-w-sm my-10 m-5 w-80 transition-shadow duration-300 hover:shadow-md cursor-pointer">
          a tu nie wiem co dać :V
          <template v-slot:footer>
          <div class="flex justify-end">
            <router-link :to="{ name: 'Panel', params: { id: shop.id }}">
              <t-button type="button">
                Przejdź
              </t-button>
            </router-link>
          </div>
        </template>
        </t-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import {
  TButton
} from 'vue-tailwind/dist/components'

export default {
  name: 'PanelServers',
  components: {
    TButton
  },
  data: function () {
    return {
      servers: null,
      showModal: false,
      serverName: '',
      serverIp: 0,
      serverRconPort: 0,
      serverAdmins: ''
    }
  },
  async created () {
    this.getServers()
  },
  methods: {
    getServers () {
      axios.get('/panel/servers/user_servers/').then((response) => {
        this.servers = response.data
      }).catch((error) => {
        console.log(error); this.$router.push('/500')
      })
    },

    createServer () {
      const data = { name: this.shopName }
      axios.post('/panel/servers/create_shop/', data).then((response) => {
        this.showModal = false
        this.getShops()
        this.$message.success('Serwer został utworzony.')
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
