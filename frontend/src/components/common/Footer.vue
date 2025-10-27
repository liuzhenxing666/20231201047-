<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h3>简易百科</h3>
          <p>一个简单的百科知识分享平台</p>
        </div>
        <div class="footer-section">
          <h4>快速链接</h4>
          <router-link to="/" class="footer-link">首页</router-link>
          <router-link to="/entries" class="footer-link">词条列表</router-link>
        </div>
        <div class="footer-section">
          <h4>关于我们</h4>
          <p>致力于提供优质的百科知识服务</p>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2024 简易百科. 保留所有权利.</p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
.footer {
  background-color: #34495e;
  color: white;
  padding: 2rem 0 1rem;
  margin-top: auto;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.footer-section h3,
.footer-section h4 {
  margin-bottom: 1rem;
}

.footer-section p {
  color: #bdc3c7;
  line-height: 1.6;
}

.footer-link {
  display: block;
  color: #bdc3c7;
  text-decoration: none;
  margin-bottom: 0.5rem;
  transition: color 0.3s;
}

.footer-link:hover {
  color: white;
}

.footer-bottom {
  border-top: 1px solid #4a6278;
  padding-top: 1rem;
  text-align: center;
  color: #bdc3c7;
}
</style>