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
        this.content = marked(this.content)
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
  <div class="bg-orange-100">
    <div class="grid grid-cols-2 gap-2 p-8">
      <textarea
        v-model="userInput"
        @input="updatePreview"
        class="min-h-96 rounded-lg bg-neutral-600 p-2 font-mono text-white"
      ></textarea>
      <div class="prose font-serif" v-html="parsed"></div>
    </div>
    <div class="grid place-content-center gap-3">
      <h1 class="flex text-5xl font-bold">Hello world</h1>
      <button @click="sendRequest" class="rounded-lg bg-blue-500 p-2 font-medium text-amber-100">
        Send Request
      </button>
      <div class="prose" v-html="content"></div>
    </div>
  </div>
</template>

<style>
body {
  margin: 0;
  padding: 0;
}
</style>
