<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>{{ editingEntry ? '编辑词条' : '创建新词条' }}</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="title">标题</label>
          <input type="text" id="title" v-model="form.title" required>
        </div>
        
        <div class="form-group">
          <label for="summary">摘要</label>
          <textarea id="summary" v-model="form.summary" rows="3"></textarea>
        </div>
        
        <div class="form-group">
          <label for="content">内容</label>
          <textarea id="content" v-model="form.content" rows="10" required></textarea>
        </div>
        
        <div class="form-group">
          <label>分类</label>
          <div class="categories-list">
            <div v-for="category in categories" :key="category.id" class="category-checkbox">
              <input 
                type="checkbox" 
                :id="'cat-' + category.id" 
                :value="category.id" 
                v-model="form.categories"
              >
              <label :for="'cat-' + category.id">{{ category.name }}</label>
            </div>
          </div>
        </div>
        
        <div class="form-actions">
          <button type="button" @click="$emit('close')" class="btn-secondary">取消</button>
          <button type="submit" class="btn-primary">保存</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { createEntry, updateEntry, fetchCategories } from '@/services/api'

export default {
  name: 'EntryForm',
  props: {
    editingEntry: Object
  },
  emits: ['close', 'saved'],
  setup(props, { emit }) {
    const form = ref({
      title: '',
      summary: '',
      content: '',
      categories: []
    })
    
    const categories = ref([])
    
    const loadCategories = async () => {
      try {
        categories.value = await fetchCategories()
      } catch (error) {
        console.error('加载分类失败:', error)
      }
    }
    
    const submitForm = async () => {
      try {
        if (props.editingEntry) {
          await updateEntry(props.editingEntry.id, form.value)
        } else {
          await createEntry(form.value)
        }
        emit('saved')
      } catch (error) {
        console.error('保存词条失败:', error)
      }
    }
    
    onMounted(() => {
      loadCategories()
      
      if (props.editingEntry) {
        form.value = {
          title: props.editingEntry.title,
          summary: props.editingEntry.summary,
          content: props.editingEntry.content,
          categories: props.editingEntry.categories.map(cat => cat.id)
        }
      }
    })
    
    return {
      form,
      categories,
      submitForm
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.categories-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.category-checkbox {
  display: flex;
  align-items: center;
}

.category-checkbox input {
  width: auto;
  margin-right: 5px;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 1rem;
}

.form-actions button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.btn-secondary {
  background: #f0f0f0;
  color: #333;
}

.btn-secondary:hover {
  background: #e0e0e0;
}

.btn-primary {
  background: #4CAF50;
  color: white;
}

.btn-primary:hover {
  background: #45a049;
}
</style>