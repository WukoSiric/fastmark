<template>
  <div class="grid place-self-center">
    <button class="bg-slate-600 p-4 text-3xl font-bold text-white" @click="getDocuments">
      Get Documents
    </button>
  </div>
  <div v-for="document in documents">
    <div
      class="grid place-items-center gap-4 rounded-xl bg-background-sidebar py-12 drop-shadow-2xl"
    >
      <h1 class="text-4xl font-bold text-brand-main drop-shadow-md">{{ document.title }}</h1>
      <p class="text-txt-editor">{{ document.content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      documents: {},
    }
  },
  methods: {
    async getDocuments() {
      const response = await fetch('http://localhost:5001/viewDocuments', {
        method: 'GET',
        credentials: 'include',
      })

      const data = await response.json()
      if (response.ok) {
        console.log(data)
        this.documents = data
      } else {
        console.log(data)
      }
    },
  },
}
</script>
