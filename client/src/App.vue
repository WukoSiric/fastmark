<template>
  <NavBar />
  <div class="h-screen">
    <textarea
      v-model="userInput"
      @input="updatePreview"
      class="min-h-2/3 bg-background-main resize-none rounded-lg bg-neutral-600 p-2 font-mono text-white"
    ></textarea>
    <div class="prose font-serif" v-html="parsed"></div>
  </div>
</template>

<script>
import { marked } from 'marked'
import NavBar from './components/NavBar.vue'

export default {
  components: {
    NavBar,
  },
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

<style>
/* Media backend */
body {
  margin: 0;
  padding: 0;
  background-image: url(https://img.freepik.com/free-vector/hand-drawn-blue-lined-paper-background_23-2151157575.jpg);
  background-repeat: repeat;
  background-blend-mode: normal;
}

@media (prefers-color-scheme: dark) {
  body {
    background-color: rgb(17, 17, 17);
    background-image: url(https://img.freepik.com/free-vector/hand-drawn-blue-lined-paper-background_23-2151157575.jpg);
    background-blend-mode: overlay;
    background-repeat: repeat;
  }
}

body[data-theme='dark'] {
  background-color: rgb(17, 17, 17);
  background-image: url(https://img.freepik.com/free-vector/hand-drawn-blue-lined-paper-background_23-2151157575.jpg);
  background-blend-mode: overlay;
  background-repeat: repeat;
}

body[data-theme='light'] {
  background-image: url(https://img.freepik.com/free-vector/hand-drawn-blue-lined-paper-background_23-2151157575.jpg);
  background-blend-mode: normal;
  background-repeat: repeat;
}
</style>
