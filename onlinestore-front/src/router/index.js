import Vue from 'vue'
// import VueRouter from 'vue-router'
import Router from 'vue-router'
import Home from '@/components/Home-page'
import Product from '@/components/Product/Pro-duct'
import Clients from '@/components/Product/Clients-list'
import Products from '@/components/Product/Product-List'
import Orders from '@/components/User/Orders-List'
import Login from '@/components/Auth/Log-in'
import Register from '@/components/Auth/Regis-ter'

// Vue.use(VueRouter)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '',
      name: 'home',
      component: Home
    },
    {
      path: '/product/:id',
      props: true,
      name: 'product',
      component: Product
    },
    {
      path: '/products',
      name: 'products',
      component: Products
    },
    {
      path: '/clients',
      name: 'clients',
      component: Clients
    },
    {
      path: '/orders',
      name: 'orders',
      component: Orders
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    }
  ]
})
