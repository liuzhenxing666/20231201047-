import axios from 'axios'

const api = axios.create({
  baseURL: '',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    // 可以在这里添加认证token等
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    console.error('API请求错误:', error)
    return Promise.reject(error)
  }
)

// 分类相关API
export const fetchCategories = () => api.get('/categories/')
export const createCategory = (data) => api.post('/categories/', data)
export const updateCategory = (id, data) => api.put(`/categories/${id}/`, data)
export const deleteCategory = (id) => api.delete(`/categories/${id}/`)

// 词条相关API
export const fetchEntries = () => api.get('/entries/')
export const fetchEntry = (id) => api.get(`/entries/${id}/`)
export const createEntry = (data) => api.post('/entries/', data)
export const updateEntry = (id, data) => api.put(`/entries/${id}/`, data)
export const deleteEntry = (id) => api.delete(`/entries/${id}/')
export const searchEntries = (query) => api.get(`/entries/search/?q=${encodeURIComponent(query)}`)
export const getEntriesByCategory = (categoryId) => api.get(`/entries/by_category/?category_id=${categoryId}`)

export default api