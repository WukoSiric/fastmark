<template>
  <div class="h-screen overflow-hidden">
    <NavBar />
    <RouterView />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  components: {
    NavBar,
  },
  mounted() {
    document.documentElement.setAttribute('data-theme', 'dark')
  },
}
</script>
