<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card class="mb-2 elevation-7">
          <v-card-title>
            Товары
            <v-spacer></v-spacer>
            <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Поиск"
            >
            </v-text-field>
            <v-spacer></v-spacer>
            <v-dialog>
            <template v-slot:activator="{ attrs }">
                <v-btn
                color="primary"
                dark
                v-bind="attrs"
                >
                  Добавить товар</v-btn>
              </template>
          </v-dialog>
          </v-card-title>
             <v-data-table
              :headers="headers"
              :items-per-page="5"
              :items="products[`data`]"
              multi-sort
              :search="search"
              :footer-props="{
                'items-per-page-text':'Товаров на странице:'
              }"
              >
               <template v-slot:[`item.actions`]="{ item }">
                 <v-btn
                   small
                   color="success"
                   @click="addProductToOrder(item)"
                 ><v-icon small>mdi-basket-plus-outline</v-icon></v-btn>
              </template>
              </v-data-table>
          <v-row justify="center">
            <v-alert
        v-model="alertIncludeCart"
        type="error"
        width="350"
        transition="scale-transition"
        >Товар уже есть в корзине
          <v-btn
          @click="alertIncludeCart = false"
          >Ок</v-btn>
        </v-alert>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card class="elevation-7">
          <v-card-title>
            Корзина
            <v-spacer></v-spacer>
            <v-text-field
            v-model="searchCart"
            append-icon="mdi-magnify"
            label="Поиск"
            >
            </v-text-field>
            <v-spacer class="ma-16"></v-spacer>
          </v-card-title>
             <v-data-table
              :headers="headersCart"
              :items-per-page="5"
              :items="productsCart"
              multi-sort
              :search="searchCart"
              :footer-props="{
                'items-per-page-text':'Товаров на странице:'
              }"
              ><template v-slot:[`item.actions`]="{ item }">
                <v-icon
                  small
                  class="mr-2"
                  @click="deleteCurrentProductInCurt(item)"
                >
                  mdi-delete
                </v-icon>
                </template>
              </v-data-table>
          <v-row justify="center">
            <v-col cols="12" xs="12" sm="6" md="4">
            <v-autocomplete
            @click="addClientToOrder"
            label="Поиск клиента"
            :items="clients"
            item-text="name"
            item-value="id"
            return-object
            v-model="selectClient"
          >
            </v-autocomplete>
              <v-btn
                color="primary"
              @click="toOrder"
              >Заказать</v-btn>
          </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      search: '',
      searchCart: '',
      products: [],
      productsCart: [],
      currentProductId: [],
      alertIncludeCart: false,
      deleteIndex: '',
      clients: [],
      orderData: [],
      selectClient: null,
      headers: [
        { text: 'Номер товара', value: 'id' },
        { text: 'Название', value: 'title' },
        { text: 'Производитель', value: 'manufacturer' },
        { text: 'Категория', value: 'group' },
        { text: 'Количество', value: 'count' },
        { text: 'Цена за шт', value: 'price' },
        { text: 'Действия', value: 'actions', sortable: false }
      ],
      headersCart: [
        { text: 'Номер товара', value: 'id' },
        { text: 'Название', value: 'title' },
        { text: 'Производитель', value: 'manufacturer' },
        { text: 'Категория', value: 'group' },
        { text: 'Количество', value: 'count' },
        { text: 'Цена', value: 'price' },
        { text: 'Действия', value: 'actions', sortable: false }
      ]
    }
  },
  methods: {
    getProducts () {
      axios.get('http://localhost:8000/api/products')
        .then((response) => {
          this.products = response.data
        })
    },
    addProductToOrder: function (currentItem) {
      if (!this.currentProductId.includes(currentItem.id)) {
        this.currentProductId.push(currentItem.id)
        this.productsCart.push(currentItem)
      } else this.alertIncludeCart = true
    },
    addClientToOrder () {
      axios.get('http://localhost:8000/api/clients-name')
        .then((response) => {
          this.clients = response.data
        })
    },
    toOrder () {
      axios.post('http://localhost:8000/api/add-order', { Products: this.productsCart, Client: this.selectClient.id })
    },
    deleteCurrentProductInCurt (item) {
      this.productsCart.splice(this.productsCart.indexOf(item), 1)
      this.currentProductId.splice(this.currentProductId.indexOf(item), 1)
    }
  },
  mounted () {
    this.getProducts()
  }
}
</script>

<style scoped>

</style>
