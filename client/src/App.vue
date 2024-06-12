<script>
export default {
  data() {
    return {
      content: '',
    }
  },
  methods: {
    async sendRequest() {
      const response = await fetch('http://localhost:5001/markdown')
      if (response.ok) {
        this.content = await response.text()
      } else {
        this.content = 'Error'
      }
    },
  },
}
</script>

<template>
  <div class="grid h-screen place-content-center gap-3">
    <h1 class="flex text-5xl font-bold">Hello world</h1>
    <button @click="sendRequest" class="rounded-lg bg-blue-500 p-2 font-medium text-amber-100">
      Send Request
    </button>
    <div class="prose" v-html="content"></div>
  </div>
</template>

<style></style>
