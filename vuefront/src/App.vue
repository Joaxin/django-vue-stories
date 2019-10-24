<template>
  <div id="app" v-cloak>
    <HelloMessage/>
    <el-footer>
    <small>
      <br>
      
      Inspired from <el-link :underline="false"  type="primary" target="_blank" href="https://mxh-mini-apps.github.io/mxh-cp-stories/">https://mxh-mini-apps.github.io/mxh-cp-stories/.</el-link><br>
    </small>
    </el-footer>
  </div>
</template>

<script>
import HelloMessage from './components/HelloMessage.vue'

export default {
  name: 'app',
  components: {
    HelloMessage
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

