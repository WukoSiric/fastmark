<template>
  <div class="h-screen">
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
