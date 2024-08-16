<template>
  <input
    type="text"
    v-model="title"
    placeholder="New Document"
    class="col-span-full h-fit bg-transparent text-2xl font-semibold text-txt-editor outline-none"
  />
  <button class="rounded-lg bg-brand-main p-1 font-semibold" @click="createDocument">
    Upload Doc
  </button>
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
      title: 'document',
      parsed: '',
      userInput: '',
    }
  },
  methods: {
    async createDocument() {
      const response = await fetch('http://localhost:5001/createDocument', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: this.title,
          content: this.userInput,
        }),
      })

      if (response.ok) {
        console.log('created document')
      } else {
        console.log('failed to create doc')
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
