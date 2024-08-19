<template>
  <div class="grid grid-cols-3 content-center justify-items-center gap-8 gap-y-10 py-4 lg:px-24">
    <DocumentPreview
      v-for="document in documents"
      :key="document._id"
      class="col-span-1"
      :title="document.title"
      :content="document.content"
      :id="document._id"
    />
  </div>
</template>

<script>
import DocumentPreview from '@/components/DocumentPreview.vue'

export default {
  components: {
    DocumentPreview,
  },
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
        this.documents = data
      } else {
        console.log(data)
      }
    },
  },
  mounted() {
    this.getDocuments()
  },
}
</script>
