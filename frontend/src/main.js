import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { createProvider } from './vue-apollo'

Vue.config.productionTip = false

new Vue({
  router,
  apolloProvider: createProvider({
    httpEndpoint: 'https://mezgoodle-django-vue-blog-pq645xr9c6gwr-8000.githubpreview.dev/graphql',
    wsEndpoint: null,
  }),
  render: h => h(App)
}).$mount('#app')
