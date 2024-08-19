<template>
  <div>
    <p
      class="prose box-border h-full w-full overflow-clip rounded-2xl bg-background-main p-4 font-serif text-txt-editor shadow-xl prose-headings:text-txt-editor prose-blockquote:text-txt-editor prose-strong:text-txt-editor"
      v-html="markdown"
    ></p>
    <h1 class="select-none font-sans text-2xl font-normal text-txt-editor">
      {{ title }}
    </h1>
  </div>
</template>

<script>
import { marked } from 'marked'
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    content: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      markdown: '',
    }
  },
  methods: {},
  mounted() {
    this.markdown = marked(this.content)
  },
}
</script>
