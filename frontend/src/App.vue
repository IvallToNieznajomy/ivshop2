<template>
  <div id="app">
    <Navbar v-if="!$route.params.id"/>
    <router-view/>
  </div>
</template>

<style>
body {
  height: 100%;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
<script>
import Navbar from '@/components/Navbar'

export default {
  components: {
    Navbar
  }
}
</script>
