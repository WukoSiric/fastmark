import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/views/LandingPage.vue'
import EditorPage from '@/views/EditorPage.vue'
import AuthPage from '@/views/AuthPage.vue'

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
      path: '/auth',
      component: AuthPage,
    },
  ],
})

export default router
