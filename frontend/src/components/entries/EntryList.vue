<template>
  <div class="entry-list">
    <div class="header">
      <h1>百科词条</h1>
      <button @click="showCreateForm = true" class="btn-primary">创建新词条</button>
    </div>
    
    <div class="search-section">
      <input 
        type="text" 
        v-model="searchQuery" 
        placeholder="搜索词条..." 
        class="search-input"
      >
    </div>
    
    <div class="entries-grid">
      <div 
        v-for="entry in filteredEntries" 
        :key="entry.id" 
        class="entry-card" 
        @click="viewEntry(entry.id)"
      >
        <h3>{{ entry.title }}</h3>
        <p>{{ entry.summary || entry.content.substring(0, 100) + '...' }}</p>
        <div class="entry-meta">
          <span class="category" v-for="cat in entry.categories" :key="cat.id">
            {{ cat.name }}
          </span>
          <span class="date">{{ formatDate(entry.created_at) }}</span>
        </div>
      </div>
    </div>
    
    <!-- 创建表单模态框 -->
    <EntryForm 
      v-if="showCreateForm"
      @close="showCreateForm = false"
      @saved="handleEntrySaved"
    />
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import EntryForm from './EntryForm.vue'
import { fetchEntries } from '@/services/api'

export default {
  name: 'EntryList',
  components: {
    EntryForm
  },
  setup() {
    const router = useRouter()
    const entries = ref([])
    const searchQuery = ref('')
    const showCreateForm = ref(false)
    
    const filteredEntries = computed(() => {
      if (!searchQuery.value) return entries.value
      return entries.value.filter(entry => 
        entry.title.toLowerCase().includes(searchQuery.value.toLowerCase()) || 
        entry.content.toLowerCase().includes(searchQuery.value.toLowerCase())
      )
    })
    
    const loadEntries = async () => {
      try {
        entries.value = await fetchEntries()
      } catch (error) {
        console.error('加载词条失败:', error)
      }
    }
    
    const viewEntry = (id) => {
      router.push(`/entry/${id}`)
    }
    
    const handleEntrySaved = () => {
      showCreateForm.value = false
      loadEntries() // 刷新列表
    }
    
    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString('zh-CN')
    }
    
    onMounted(() => {
      loadEntries()
    })
    
    return {
      entries,
      searchQuery,
      showCreateForm,
      filteredEntries,
      viewEntry,
      handleEntrySaved,
      formatDate
    }
  }
}
</script>

<style scoped>
.entry-list {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.entries-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.entry-card {
  border: 1px solid #e1e1e1;
  border-radius: 8px;
  padding: 15px;
  cursor: pointer;
  transition: box-shadow 0.3s;
  background: white;
}

.entry-card:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.entry-card h3 {
  margin-bottom: 10px;
  color: #2c3e50;
}

.entry-card p {
  color: #666;
  margin-bottom: 10px;
  line-height: 1.4;
}

.entry-meta {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
  font-size: 0.8rem;
  color: #666;
}

.category {
  background: #f0f0f0;
  padding: 2px 8px;
  border-radius: 12px;
  margin-right: 5px;
}

.btn-primary {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.btn-primary:hover {
  background: #45a049;
}
</style>