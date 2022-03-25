<template>
  <v-container>
    <v-layout>
      <v-flex xs12 sm6 offset-sm3>
        <h1 class="text--secondary mb-3">Мои Товары</h1>
        <v-card
          class="elevation-10 mb-2"
          v-for="(product, i) in products"
          :key="i"
        >
          <v-layout>
            <v-flex xs4>
              <v-img :src="product.imageSrc" ></v-img>
            </v-flex>
            <v-flex xs8>
              <v-card-text>
                <h2 class="text--primary">{{product.title}}</h2>
                <p>{{product.description}}</p>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn class="info" :to="'/product/' + product.id">Открыть</v-btn>
              </v-card-actions>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
    <v-btn color="primary" @click="refreshData">Привет</v-btn>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      products: []
    }
  },
  methods: {
    refreshData () {
      axios.get('http://127.0.0.1:8000/product')
        .then((response) => {
          this.products = response.data
        })
    }
  },
  computed: {
    myProducts (state) {
      return this.$store.getters.myProducts
    }
  },
  mounted () {
    return {
      refreshData () {
      }
    }
  }
}
</script>

<style scoped>

</style>
