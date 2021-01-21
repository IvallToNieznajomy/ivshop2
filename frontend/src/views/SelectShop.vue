<template>
  <div class="SelectShop">
    <TModal header="Tworzenie nowego sklepu" v-model="showModal">
      <div class="form">
        <t-input v-model="shopName" placeholder="Nazwa sklepu" />
      </div>
      <template v-slot:footer>
        <div class="flex justify-between">
          <t-button type="button" @click="showModal=false">
            Anuluj
          </t-button>
          <t-button type="button" @click="createShop()">
            Stwórz
          </t-button>
        </div>
      </template>
    </TModal>

    <div class="text-center mt-12">
      <div class="text-2xl">Wybierz sklep, którym chcesz zarządzać.</div>
      <div class="flex justify-center mt-8">
        <t-button type="button" @click="showModal=true">
          Utwórz nowy sklep
        </t-button>
      </div>
      <div class="inline-flex justify-center flex-col flex-wrap md:flex-row">
        <t-card v-for="shop in shops" :key="shop.id" :header="shop.name" class="flex-auto max-w-sm my-10 m-5 w-80 transition-shadow duration-300 hover:shadow-md cursor-pointer">
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
    this.getShops()
  },
  methods: {
    getShops () {
      if (!localStorage.getItem('accessToken')) {
        this.$router.push('500')
      }

      axios.get('/panel/shops/user_shops/').then((response) => {
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
