<template>
  <div class="Navbar">
    <div class="antialiased">
      <div class="w-full text-gray-700 bg-white dark-mode:text-gray-200 dark-mode:bg-gray-800">
        <div class="flex flex-col px-4 mx-auto md:items-center md:justify-between md:flex-row md:px-6 lg:px-8">

          <div class="flex flex-row items-center justify-between p-4">
            <router-link to="/" class="text-lg font-semibold tracking-widest text-gray-900 rounded-lg dark-mode:text-white focus:outline-none focus:shadow-outline"><span class="text-purple-800 uppercase">IV</span>shop</router-link>
            <button class="rounded-lg md:hidden focus:outline-none focus:shadow-outline" v-on:click="open = !open">
              <svg fill="currentColor" viewBox="0 0 20 20" class="w-6 h-6">
                <path v-show="!open" fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM9 15a1 1 0 011-1h6a1 1 0 110 2h-6a1 1 0 01-1-1z" clip-rule="evenodd"></path>
                <path v-show="open" fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
              </svg>
            </button>
          </div>

          <nav :class="{'flex': open, 'hidden': !open}" class="flex-col flex-grow pb-4 md:pb-0 md:flex md:flex-row">
            <router-link to="/login" v-if="!loggedIn" class="px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg mode:hover:text-white md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline duration-150">Zaloguj się</router-link>
            <router-link to="/select_shop" v-if="loggedIn" class="px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg mode:hover:text-white md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline duration-150">Panel</router-link>
            <router-link to="/faq" class="px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg mode:hover:text-white md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline duration-150">Faq</router-link>
            <a class="px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg mode:hover:text-white md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline duration-150" href="#">Polityka prywatności</a>
            <a class="px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg mode:hover:text-white md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline duration-150" href="#">Wesprzyj</a>
          </nav>

          <nav v-if="loggedIn" :class="{'flex': open, 'hidden': !open}" class="flex-col flex-grow justify-end pb-4 md:pb-0 md:flex md:flex-row">
            <div v-on:="!open" class="relative">
              <button @click="open = !open" class="flex flex-row text-gray-900 items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline duration-150">
                <img :src="this.avatar_url" class="inline-block h-8 w-8 rounded-full ring-2 ring-white" alt="avatar">
                <span class="ml-2">{{this.username}}</span>
              </button>

              <div v-show="open" class="absolute right-0 w-48 mt-2 origin-top-right">
                <div class="px-2 pt-2 pb-4 bg-white rounded-md shadow-lg dark-mode:bg-gray-700">
                  <a class="flex flex row items-start rounded-lg bg-transparent p-2 dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" href="#">
                    <div class="ml-3">
                      <a v-on:click="logout()" class="px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg mode:hover:text-white md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline duration-150" href="#">Wyloguj się</a>
                    </div>
                  </a>
                </div>
              </div>
            </div>
          </nav>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data: function () {
    return {
      loggedIn: false,
      avatar_url: null,
      username: null,
      open: false
    }
  },
  created () {
    if (localStorage.getItem('accessToken')) {
      this.loggedIn = true
      this.avatar_url = localStorage.getItem('avatar_url')
      this.username = localStorage.getItem('username')
    }
  },
  methods: {
    logout () {
      if (localStorage.accessToken) {
        localStorage.clear()
        this.loggedIn = false
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
