<template>
  <div class="h-screen">
    <NavBar />
    <div class="grid h-5/6 w-full grid-cols-2 gap-5 p-6">
      <textarea
        v-model="userInput"
        @input="updatePreview"
        class="text-txt-editor bg-background-main h-full w-full resize-none overflow-y-scroll rounded-2xl p-2 font-mono active:border-none"
      ></textarea>
      <div
        class="bg-background-main prose-blockquote:text-txt-editor prose-strong:text-txt-editor prose-headings:text-txt-editor text-txt-editor prose box-border h-full min-w-full overflow-y-scroll rounded-2xl p-4 font-serif"
        v-html="parsed"
      ></div>
    </div>
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
  mounted() {
    document.documentElement.setAttribute('data-theme', 'light')
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
body {
  background-color: var(--main-bg);
  background-image: var(--background-image);
  background-blend-mode: var(--blend-mode);
  background-repeat: repeat;
  background-size: 40%;
}
</style>
