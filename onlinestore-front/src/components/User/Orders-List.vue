<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card class="elevation-7">
          <v-card-title>
            Заказы
            <v-spacer></v-spacer>
            <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Поиск"
            >
            </v-text-field>
            <v-spacer></v-spacer>
            <v-dialog
            v-model="dialogAdd"
            width="600"
            >
              <template v-slot:activator="{ attrs }">
                <v-btn
                color="primary"
                dark
                v-bind="attrs"
                @click="addOrder"
                >
                  Добавить заказ</v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">Новый заказ</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-autocomplete
                      label="Поиск клиента"
                    :items="clients"
                    ></v-autocomplete>
                  </v-container>
                  <v-container>
                    <v-text-field
                    v-model="searchTree"
                    label="Поиск товара"
                    clearable
                    ></v-text-field>
                    <v-treeview
                    v-model="selection"
                    :selection-type="selectionType"
                    :items="productsTree"
                    :search="searchTree"
                    selectable
                    ></v-treeview>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                  >
                    Отмена
                  </v-btn>
                   <v-btn
                  color="blue darken-1"
                  text
                  @click="saveAdd"
                  >
                     Сохранить
                   </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-title>
          <v-dialog
            v-model="dialogEdit"
            width="600"
            >
              <v-card>
                <v-card-title>
                  <span class="text-h5">Редактирование заказа</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                      <v-text-field
                      v-model="editedItem.title"
                      label="Название товара"
                      clearable>
                      </v-text-field>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                  >
                    Отмена
                  </v-btn>
                   <v-btn
                  color="blue darken-1"
                  text
                  @click="saveAdd"
                  >
                     Сохранить
                   </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
            <v-dialog v-model="dialogDelete" width="650">
                  <v-card>
                    <v-card-title class="text-h5">Вы уверены что хотите удалить этот заказ?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="closeDelete">Отменить</v-btn>
                    <v-btn color="blue darken-1" text @click="deleteItemConfirm">Ок</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                 </v-card>
              </v-dialog>
           <v-dialog v-model="dialogDetail" width="600">
            <v-card>
              <v-data-table
              :headers="headersDetail"
              :items-per-page="10"
              :items="currentProducts['product']"
              :footer-props="{
                'items-per-page-text':'Товаров на странице:'
              }"
              >
                <template v-slot:[`item.count`]="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.count"
                    @save="save"
                    @cancel="cancel"
                    @open="open"
                    @close="close1"
                    large
                    save-text="Сохранить"
                    cancel-text="Отмена"
                  >
                    {{ props.item.count }}
                    <template v-slot:input>
                      <v-text-field
                        v-model="props.item.count"
                        :rules="[max25chars]"
                        label="Редактирование"
                        single-line
                        counter
                      ></v-text-field>
                    </template>
                  </v-edit-dialog>
                </template>
                <template v-slot:[`item.actions`]="{ item }">
                <v-icon
                  small
                  class="mr-2"
                  @click="deleteCurrentProduct(item)"
                >
                  mdi-delete
                </v-icon>
                </template>
              </v-data-table>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                color="blue darken-1"
                text
                @click="closeDetail"
                >Добавить товар
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="closeDetail"
                >
                  Отмена
                </v-btn>
              </v-card-actions>
             </v-card>
            </v-dialog>
            <v-data-table
          :headers="headers"
          :items="orders[`data`]"
          :items-per-page="5"
          multi-sort
          :search="search"
          :footer-props="{
            'items-per-page-text':'Заказов на странице:'
          }"
            >
              <template v-slot:[`item.actions`]="{ item }">
                <v-icon
                  small
                  class="mr-2"
                  @click="deleteItem(item)"
                >
                  mdi-delete
                </v-icon>
                <v-icon
                small
                @click="loadCurrentProducts(item)"
                >
                  mdi-eye
                </v-icon>
              </template>
            </v-data-table>
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
      searchTree: null,
      searchClients: '',
      dialogAdd: false,
      dialogEdit: false,
      dialogDelete: false,
      dialogDetail: false,
      currentItem: '',
      currentProducts: {},
      orders: {},
      selection: [],
      selectionType: 'leaf',
      max25chars: v => v.length <= 25 || 'Input too long!',
      productsTree: [],
      clients: [],
      headers: [
        { text: 'Номер заказа', value: 'id' },
        { text: 'Дата заказа', value: 'date_time' },
        { text: 'Клиент', value: 'name_client' },
        { text: 'Адрес клиента ', value: 'client_address' },
        { text: 'Действия', value: 'actions', sortable: false }
      ],
      headersDetail: [
        { text: 'Название товара', value: 'title' },
        { text: 'Производитель', value: 'manufacturer' },
        { text: 'Количество', value: 'count' },
        { text: 'Цена', value: 'price' },
        { text: 'Действия', value: 'actions', sortable: false }
      ],
      editedIndex: -1,
      editedItem: {
        title: '',
        manufacturer: '',
        count: '',
        price: ''
      },
      defaultItem: {
        date_time: '',
        name_client: '',
        client_address: '',
        products: '',
        manufacturer: '',
        price: '',
        count: ''
      }
    }
  },
  methods: {
    getOrders () {
      axios.get('http://localhost:8000/api/orders')
        .then((response) => {
          this.orders = response.data
        })
    },
    loadCurrentProducts (item) {
      axios.post('http://localhost:8000/api/current-product', { pk: item.id })
        .then((response) => {
          this.currentProducts = response.data
        })
      this.dialogDetail = true
    },
    addOrder () {
      axios.get('http://localhost:8000/api/clients-select')
        .then((response) => {
          this.clients = response.data
        })
      axios.get('http://localhost:8000/api/products-tree')
        .then((response) => {
          this.productsTree = response.data
        })
      this.dialogAdd = true
    },
    editItem (item) {
      this.editedIndex = this.orders.data.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogEdit = true
    },
    deleteItem (item) {
      this.editedIndex = this.orders.data.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteCurrentProduct (item) {
      this.editedIndex = this.currentProducts.product.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.currentProducts.product.splice(this.editedIndex, 1)
    },
    deleteItemConfirm () {
      this.orders.data.splice(this.editedIndex, 1)
      this.closeDelete()
    },
    close () {
      this.dialogAdd = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    closeDetail () {
      this.dialogDetail = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    saveAdd () {
      if (this.editedIndex > -1) {
        Object.assign(this.orders[this.editedIndex], this.editedItem)
      } else {
        this.orders.push(this.editedItem)
      }
      this.close()
    },
    save () {},
    cancel () {},
    open () {},
    close1 () {}
  },
  watch: {
    dialogAdd (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    },
    dialogDetail (val) {
      val || this.closeDetail()
    }
  },
  mounted () {
    this.getOrders()
  }
}
</script>

<style scoped>

</style>
