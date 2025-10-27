import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Entries from '../views/Entries.vue'
import EntryDetail from '../views/EntryDetail.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/entries',
    name: 'Entries',
    component: Entries
  },
  {
    path: '/entry/:id',
    name: 'EntryDetail',
    component: EntryDetail,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router