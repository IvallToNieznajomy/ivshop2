<template>
  <div class="panel md:flex flex-col md:flex-row md:min-h-screen w-full">
  <PanelNavbar />
    <div class="container p-12">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import PanelNavbar from '@/components/PanelNavbar'

export default {
  name: 'Panel',
  components: {
    PanelNavbar
  }
}
</script>

<style scoped>

</style>
