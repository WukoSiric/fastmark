import { createStore } from 'vuex'

const store = createStore({
  state: {
    user: null,
    currentDocument: null,
  },
  mutations: {
    changeUser(state, user) {
      state.user = user
    },
    selectDocument(state, document) {
      state.currentDocument = document
    },
  },
  getters: {
    user(state) {
      return state.user
    },
    currentDocument(state) {
      return state.current
    },
  },
})

export default store
