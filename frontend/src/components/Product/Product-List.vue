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
                <v-btn color="primary" dark v-bind="attrs" @click="openDialogAddProduct">Добавить товар</v-btn>
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
                      <v-autocomplete :rules="newProductRules" label="Производитель" @click="getManufacturer"
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
             <v-dialog v-model="dialogConfirmAdd" width="650">
                  <v-card>
                    <v-card-title class="text-h5">Заказ добавлен</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="dialogConfirmAddClose">Ок</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                 </v-card>
          </v-dialog>
            <v-dialog v-model="dialogEditProduct" width="400">
              <v-card>
                <v-card-title>
                  <span class="text-h5">Редактирование товара</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-form ref="formEdit" v-model="valid" lazy-validation>
                      <v-text-field v-model="editedProductData.title" :rules="editProductRules" label="Модель"
                                    clearable></v-text-field>
                      <v-autocomplete v-model="editedProductData.manufacturer" :rules="editProductRules"
                                      label="Производитель" clearable :items="manufacturers.data" item-text="title"
                                      item-value="id" @click="getManufacturer"></v-autocomplete>
                      <v-autocomplete v-model="editedProductData.group" :rules="editProductRules"
                                      label="Категория" clearable :items="groups.data" item-text="title"
                                      item-value="id" @click="loadGroups"></v-autocomplete>
                      <v-text-field v-model="editedProductData.count" :rules="editProductRules" label="Количество"
                                    clearable></v-text-field>
                      <v-text-field v-model="editedProductData.price" :rules="editProductRules" label="Цена"
                                    clearable></v-text-field>
                      <v-text-field v-model="editedProductData.description" :rules="editProductRules" label="Описание"
                                    clearable></v-text-field>
                    </v-form>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="closeDialogEditProduct">Отмена</v-btn>
                   <v-btn color="blue darken-1" :disabled="!valid" text @click="saveChangeProduct">Сохранить</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-title>
             <v-data-table :headers="headers" :items-per-page="5" :items="products[`data`]" multi-sort :search="search"
                           :sort-desc=true sort-by="id"
                           :footer-props="{
               'items-per-page-text':'Товаров на странице:'
             }">
               <template v-slot:[`item.actions`]="{ item }">
                 <v-btn small class="mr-2" color="success" @click="addProductToCart(item)">
                   <v-icon small>mdi-basket-plus-outline</v-icon>
                 </v-btn>
                 <v-btn small @click="openDialogEditProduct(item)">
                   <v-icon small>mdi-pencil</v-icon>
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
                <template v-slot:[`item.count`]="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.count" @save="saveEditCount(props)" @cancel="cancel" @open="open" @close="close1"
                    large save-text="Сохранить" cancel-text="Отмена" type="number">
                    {{ props.item.count }}
                    <template v-slot:input>
                      <v-text-field type="number" v-model="props.item.count" label="Редактирование" single-line>
                      </v-text-field>
                    </template>
                  </v-edit-dialog>
                </template>
             </v-data-table>
          <v-row justify="center">
            <v-col cols="12" xs="12" sm="6" md="4">
            <v-autocomplete @click="getClient" label="Поиск клиента" :items="clients" item-text="name"
                            item-value="id" return-object v-model="selectClient">
            </v-autocomplete>
              <v-btn color="primary" @click="addOrder">Заказать</v-btn>
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
      productObject: {},
      clients: [],
      orderData: [],
      selectClient: null,
      dialogAddProduct: false,
      dialogEditProduct: false,
      dialogConfirmAdd: false,
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
      editedProductData: {
        title: '',
        manufacturer: '',
        group: '',
        count: null,
        price: null,
        description: ''
      },
      editedIndex: -1,
      groups: [],
      manufacturers: [],
      newProductRules: [
        v => !!v || 'Обязательное поле'
      ],
      editProductRules: [
        v => !!v || 'Обязательное поле'
      ],
      valid: false
    }
  },
  methods: {
    async getProducts () {
      const response = await axios.get('http://localhost:8000/api/nomenclature')
      this.products = response.data
    },
    addProductToCart: function (currentItem) {
      if (!this.currentProductId.includes(currentItem.id)) {
        this.currentProductId.push(currentItem.id)
        this.productObject = Object.assign({}, currentItem)
        this.productObject.count = 1
        this.productsCart.push(this.productObject)
      } else this.alertIncludeCart = true
    },
    openDialogEditProduct (item) {
      this.editedIndex = this.products.data.indexOf(item)
      // const currentProduct = this.product.data.find(product => product.id === item.id)
      // console.log(currentProduct)
      this.editedProductData = Object.assign({}, item)
      this.dialogEditProduct = true
    },
    closeDialogEditProduct () {
      this.dialogEditProduct = false
    },
    async saveChangeProduct () {
      if (this.$refs.formEdit.validate()) {
        await axios.post('http://localhost:8000/api/change-nomenclature', this.editedProductData)
        await this.getProducts()
        this.dialogEditProduct = false
      }
    },
    async getClient () {
      const response = await axios.get('http://localhost:8000/api/clients-name')
      this.clients = response.data
    },
    async addOrder () {
      await axios.post('http://localhost:8000/api/add-order',
        { products: this.productsCart, client: this.selectClient.id })
      await this.getProducts()
      this.dialogConfirmAdd = true
      this.productsCart = []
    },
    deleteCurrentProductInCurt (item) {
      this.productsCart.splice(this.productsCart.indexOf(item), 1)
      this.currentProductId.splice(this.currentProductId.indexOf(item), 1)
    },
    openDialogAddProduct () {
      this.dialogAddProduct = true
    },
    closeDialogAddProduct () {
      this.dialogAddProduct = false
    },
    async saveNewProduct () {
      if (this.$refs.form.validate()) {
        await axios.post('http://localhost:8000/api/add-nomenclature', this.dataNewProduct)
        this.dataNewProduct = ''
        await this.getProducts()
        this.dialogAddProduct = false
      }
    },
    async getManufacturer () {
      const response = await axios.get('http://localhost:8000/api/manufacturers')
      this.manufacturers = response.data
    },
    async loadGroups () {
      const response = await axios.get('http://localhost:8000/api/groups')
      this.groups = response.data
    },
    dialogConfirmAddClose () {
      this.dialogConfirmAdd = false
    },
    saveEditCount (props) {
      const startPrice = this.products.data.find(product => product.id === props.item.id).price
      props.item.price = props.item.count * startPrice
    },
    cancel () {},
    open () {},
    close1 () {}
  },
  mounted () {
    this.getProducts()
    this.getManufacturer()
  }
}
</script>

<style scoped>

</style>
