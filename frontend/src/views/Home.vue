<template>
  <div class="home">
    <div class="hero">
      <h1>欢迎来到简易百科</h1>
      <p>一个简单的百科知识分享平台</p>
      <router-link to="/entries" class="btn">浏览词条</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.hero {
  text-align: center;
  padding: 4rem 0;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: #2c3e50;
}

.hero p {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  color: #7f8c8d;
}

.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-size: 1.1rem;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #45a049;
}
</style>