<template>
  <div class="grid h-5/6 w-full grid-cols-2 gap-5 p-6">
    <textarea
      v-model="userInput"
      @input="updatePreview"
      class="h-full w-full resize-none overflow-y-scroll rounded-2xl bg-background-main p-2 font-mono text-txt-editor shadow-xl active:border-none"
    ></textarea>
    <div
      class="prose box-border h-full min-w-full overflow-y-scroll rounded-2xl bg-background-main p-4 font-serif text-txt-editor shadow-xl prose-headings:text-txt-editor prose-blockquote:text-txt-editor prose-strong:text-txt-editor"
      v-html="parsed"
    ></div>
  </div>
</template>

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

<style>
body {
  background-color: var(--main-bg);
  background-image: var(--background-image);
  background-blend-mode: var(--blend-mode);
  background-repeat: repeat;
  background-size: 40%;
}
</style>
