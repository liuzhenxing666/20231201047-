<template>
  <div class="entry-detail" v-if="entry">
    <div class="header">
      <h1>{{ entry.title }}</h1>
      <button @click="editEntry" class="btn-primary">编辑</button>
    </div>
    
    <div class="entry-meta">
      <span>创建者: {{ entry.created_by }}</span>
      <span>创建时间: {{ formatDate(entry.created_at) }}</span>
      <span v-if="entry.categories.length">分类: 
        <span class="category" v-for="cat in entry.categories" :key="cat.id">
          {{ cat.name }}
        </span>
      </span>
    </div>
    
    <div class="entry-content">
      <p>{{ entry.content }}</p>
    </div>
    
    <!-- 编辑表单模态框 -->
    <EntryForm 
      v-if="showEditForm"
      :editing-entry="entry"
      @close="showEditForm = false"
      @saved="handleEntrySaved"
    />
  </div>
  <div v-else>
    加载中...
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import EntryForm from '../components/entries/EntryForm.vue'
import { fetchEntry } from '@/services/api'

export default {
  name: 'EntryDetail',
  components: {
    EntryForm
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const entry = ref(null)
    const showEditForm = ref(false)
    
    const loadEntry = async () => {
      try {
        entry.value = await fetchEntry(route.params.id)
      } catch (error) {
        console.error('加载词条详情失败:', error)
      }
    }
    
    const editEntry = () => {
      showEditForm.value = true
    }
    
    const handleEntrySaved = () => {
      showEditForm.value = false
      loadEntry() // 刷新详情
    }
    
    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString('zh-CN')
    }
    
    onMounted(() => {
      loadEntry()
    })
    
    return {
      entry,
      showEditForm,
      editEntry,
      handleEntrySaved,
      formatDate
    }
  }
}
</script>

<style scoped>
.entry-detail {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.entry-meta {
  margin-bottom: 2rem;
  color: #666;
  font-size: 0.9rem;
}

.entry-meta span {
  margin-right: 1rem;
}

.category {
  background: #f0f0f0;
  padding: 2px 8px;
  border-radius: 12px;
  margin-right: 5px;
}

.entry-content {
  line-height: 1.6;
  font-size: 1.1rem;
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