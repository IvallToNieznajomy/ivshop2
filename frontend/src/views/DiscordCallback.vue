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
    console.log(data)

    axios.post('/users/login/discord/callback/', data).then((response) => {
      console.log(response)
    }).catch((error) => {
      console.log(error); this.$router.push('/500')
    })
  }
}
</script>

<style scoped>

</style>
