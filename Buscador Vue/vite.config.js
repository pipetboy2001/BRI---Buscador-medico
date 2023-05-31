import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { createServer } from 'vite'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/elasticsearch': {
        target: 'http://localhost:9200',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/elasticsearch/, '')
      }
    }
  }
})
