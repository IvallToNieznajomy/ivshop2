<template>
  <div class="login">
    <div class="text-center m-12">
      <div class="text-2xl">Wybierz metodę logowania.</div>
      <div class="inline-flex justify-center flex-col md:flex-row">
        <t-card @click.native="login('discord')" class="flex-1 max-w-sm my-10 m-5 transition-shadow duration-300 hover:shadow-md cursor-pointer">
          <img class="w-96" src="https://discord.com/assets/bb408e0343ddedc0967f246f7e89cebf.svg" alt="discord">
        </t-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  methods: {
    login (loginMethod) {
      const url = '/users/login/' + loginMethod

      axios.get(url).then((response) => {
        const url = response.data.url
        window.location.href = url
      }).catch((error) => {
        console.log(error); this.$router.push('/500')
      })
    }
  }
}
</script>

<style scoped>
</style>
