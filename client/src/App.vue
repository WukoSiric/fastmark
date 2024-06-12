<script>
import { marked } from 'marked'

export default {
  data() {
    return {
      content: '',
      parsed: '',
      userInput: '',
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
    updatePreview() {
      this.parsed = marked(this.userInput)
    },
  },
}
</script>

<template>
  <div class="grid grid-cols-2">
    <textarea
      v-model="userInput"
      @input="updatePreview"
      class="h-48 bg-neutral-600 p-2 text-white"
    ></textarea>
    <div class="prose" v-html="parsed"></div>
  </div>
  <div class="grid h-screen place-content-center gap-3">
    <h1 class="flex text-5xl font-bold">Hello world</h1>
    <button @click="sendRequest" class="rounded-lg bg-blue-500 p-2 font-medium text-amber-100">
      Send Request
    </button>
    <div class="prose" v-html="content"></div>
  </div>
</template>

<style></style>
