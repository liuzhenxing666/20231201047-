<template>
  <div class="entries-view">
    <EntryList />
  </div>
</template>

<script>
import EntryList from '../components/entries/EntryList.vue'

export default {
  name: 'Entries',
  components: {
    EntryList
  }
}
</script>

<style scoped>
.entries-view {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}
</style>