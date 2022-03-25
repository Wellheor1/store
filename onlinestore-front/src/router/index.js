import Vue from 'vue'
// import VueRouter from 'vue-router'
import Router from 'vue-router'
import Home from '@/components/Home-page'
import Product from '@/components/Product/Pro-duct'
import NewProduct from '@/components/Product/New-Product'
import ProductList from '@/components/Product/Product-List'
import Checkout from '@/components/User/Check-out'
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
      path: '/list',
      name: 'list',
      component: ProductList
    },
    {
      path: '/new',
      name: 'new',
      component: NewProduct
    },
    {
      path: '/checkout',
      name: 'checkout',
      component: Checkout
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
