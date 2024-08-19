import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/views/LandingPage.vue'
import EditorPage from '@/views/EditorPage.vue'
import AuthPage from '@/views/AuthPage.vue'
import CollectionPage from '@/views/CollectionPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: LandingPage,
    },
    {
      path: '/editor',
      component: EditorPage,
    },
    {
      path: '/editor/:id',
      component: EditorPage,
    },
    {
      path: '/auth',
      component: AuthPage,
    },
    {
      path: '/collection',
      component: CollectionPage,
    },
  ],
})

export default router
