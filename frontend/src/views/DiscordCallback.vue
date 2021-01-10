<template>
  <div class="DiscordCallback">
    <div class="text-center">
      Trwa logowanie...
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DiscordCallback',
  async created () {
    const data = { code: this.$route.query.code }

    axios.post('/users/login/discord/callback/', data).then((response) => {
      localStorage.accessToken = response.data.jwt_token
      axios.defaults.headers.Authorization = localStorage.accessToken

      axios.get('/users/me/').then((response) => {
        localStorage.username = response.data.username
        localStorage.avatar_url = response.data.avatar_url
        window.location.replace('/')
      }).catch((error) => {
        console.log(error); this.$router.push('/500')
      })
    }).catch((error) => {
      console.log(error); this.$router.push('/500')
    })
  }
}
</script>

<style scoped>

</style>
