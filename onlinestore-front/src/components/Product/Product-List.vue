<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card class="mb-2 elevation-7">
          <v-card-title>
            Товары
            <v-spacer></v-spacer>
            <v-text-field v-model="search" append-icon="mdi-magnify" label="Поиск"></v-text-field>
            <v-spacer></v-spacer>
            <v-dialog v-model="dialogAddProduct" width="400">
              <template v-slot:activator="{ attrs }">
                <v-btn color="primary" dark v-bind="attrs" @click="callDialogAddProduct">Добавить товар</v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">Новый товар</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-form ref="form" v-model="valid" lazy-validation>
                      <v-text-field :rules="newProductRules" label="Название" v-model="dataNewProduct.title" required>
                      </v-text-field>
                      <v-autocomplete :rules="newProductRules" label="Производитель" @click="loadManufacturer"
                                      v-model="dataNewProduct.manufacturer"
                                      required :items="manufacturers.data" item-text="title" item-value="id">
                      </v-autocomplete>
                      <v-autocomplete :rules="newProductRules" label="Категория" @click="loadGroups"
                                      v-model="dataNewProduct.group" required :items="groups.data"
                                      item-text="title" item-value="id">
                      </v-autocomplete>
                      <v-text-field :rules="newProductRules" label="Описание" v-model="dataNewProduct.description" required></v-text-field>
                      <v-text-field :rules="newProductRules" type="number" min="0" label="Количество" v-model="dataNewProduct.count" required>
                      </v-text-field>
                      <v-text-field :rules="newProductRules" suffix="Руб" min="0"  type="number" label="Цена за шт"
                                    v-model="dataNewProduct.price" required></v-text-field>
                    </v-form>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="closeDialogAddProduct">Отмена</v-btn>
                  <v-btn color="blue darken-1" text @click="saveNewProduct" :disabled="!valid">Сохранить</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-title>
             <v-data-table :headers="headers" :items-per-page="5" :items="products[`data`]" multi-sort :search="search"
                           :footer-props="{
               'items-per-page-text':'Товаров на странице:'
             }">
               <template v-slot:[`item.actions`]="{ item }">
                 <v-btn small color="success" @click="addProductToCart(item)">
                   <v-icon small>mdi-basket-plus-outline</v-icon>
                 </v-btn>
               </template>
             </v-data-table>
          <v-row justify="center">
            <v-alert v-model="alertIncludeCart" type="error" width="350" transition="scale-transition">
              Товар уже есть в корзине
              <v-btn @click="alertIncludeCart = false">Ок</v-btn>
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
            <v-text-field v-model="searchCart" append-icon="mdi-magnify" label="Поиск"></v-text-field>
            <v-spacer class="ma-16"></v-spacer>
          </v-card-title>
             <v-data-table :headers="headersCart" :items-per-page="5" :items="productsCart" multi-sort
                           :search="searchCart"
                           :footer-props="{
                             'items-per-page-text':'Товаров на странице:'
                           }">
               <template v-slot:[`item.actions`]="{ item }">
                <v-icon small class="mr-2" @click="deleteCurrentProductInCurt(item)">mdi-delete</v-icon>
               </template>
             </v-data-table>
          <v-row justify="center">
            <v-col cols="12" xs="12" sm="6" md="4">
            <v-autocomplete @click="loadClientToCart" label="Поиск клиента" :items="clients" item-text="name"
                            item-value="id" return-object v-model="selectClient">
            </v-autocomplete>
              <v-btn color="primary" @click="toOrder">Заказать</v-btn>
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
      dialogAddProduct: false,
      headers: [
        { text: 'Номер товара', value: 'id' },
        { text: 'Название', value: 'title' },
        { text: 'Производитель', value: 'manufacturer' },
        { text: 'Категория', value: 'group' },
        { text: 'Количество', value: 'count' },
        { text: 'Цена за шт', value: 'price' },
        { text: 'Описание', value: 'description' },
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
      ],
      dataNewProduct: {
        title: '',
        manufacturer: '',
        group: '',
        count: null,
        price: null,
        description: ''
      },
      groups: [],
      manufacturers: [],
      newProductRules: [
        v => !!v || 'Обязательное поле'
      ],
      valid: false
    }
  },
  methods: {
    getProducts () {
      axios.get('http://localhost:8000/api/nomenclature')
        .then((response) => {
          this.products = response.data
        })
    },
    addProductToCart: function (currentItem) {
      if (!this.currentProductId.includes(currentItem.id)) {
        this.currentProductId.push(currentItem.id)
        this.productsCart.push(currentItem)
      } else this.alertIncludeCart = true
    },
    loadClientToCart () {
      axios.get('http://localhost:8000/api/clients-name')
        .then((response) => {
          this.clients = response.data
        })
    },
    toOrder () {
      axios.post('http://localhost:8000/api/add-order',
        { products: this.productsCart, client: this.selectClient.id })
    },
    deleteCurrentProductInCurt (item) {
      this.productsCart.splice(this.productsCart.indexOf(item), 1)
      this.currentProductId.splice(this.currentProductId.indexOf(item), 1)
    },
    callDialogAddProduct () {
      this.dialogAddProduct = true
    },
    closeDialogAddProduct () {
      this.dialogAddProduct = false
    },
    saveNewProduct () {
      if (this.$refs.form.validate()) {
        axios.post('http://localhost:8000/api/add-nomenclature', this.dataNewProduct)
        this.dialogAddProduct = false
      }
    },
    loadManufacturer () {
      axios.get('http://localhost:8000/api/manufacturers')
        .then((response) => {
          this.manufacturers = response.data
        })
    },
    loadGroups () {
      axios.get('http://localhost:8000/api/groups')
        .then((response) => {
          this.groups = response.data
        })
    }
  },
  mounted () {
    this.getProducts()
  }
}
</script>

<style scoped>

</style>
