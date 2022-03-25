<template>
  <v-container>
    <v-layout>
      <v-flex xs12 sm6 offset-sm-3>
        <h1 class="text--secondary mb-3">Заказы</h1>
        <v-list
          flat
          subheader
          three-line
        >
          <v-list-item-group
            v-model="settings"
            multiple
            active-class=""
          >
            <v-list-item
              v-for="(order, i) in orders"
              :key="i"
            >
              <v-list-item-action>
                <v-checkbox
                  color="success"
                  :input-value="order.done"
                  @change="markDone(order)"
                >
                </v-checkbox>
              </v-list-item-action>
              <v-list-item-content >
                <v-list-item-title class="text-wrap">Имя покупателя: {{ order.name }}</v-list-item-title>
                <v-list-item-subtitle>Телефон: {{ order.phone}}</v-list-item-subtitle>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn class="primary" :to="'/product/' +order.productId">Открыть</v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-flex>
    </v-layout>
    <v-btn @click="getCustomers">Приветы</v-btn>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      Customers: [],
      orders: [
        {
          id: 'test',
          name: 'Gleb',
          phone: '8(952)638-64-43',
          productId: '1',
          done: false
        }
      ]
    }
  },
  methods: {
    markDone (order) {
      order.done = true
    },
    getCustomers () {
      axios.get('http://127.0.0.1:8000/api/customer')
        .then((response) => {
          this.Customers = response.data
          console.log(this.Customers)
        })
    }
  },
  mounted () {
    return {
      getCustomers () {
      }
    }
  }
}
</script>

<style scoped>

</style>
