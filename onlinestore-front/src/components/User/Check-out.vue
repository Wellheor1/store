<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
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
                @click="orderAdd"
                >
                  Добавить заказ</v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">Новый заказ</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-treeview
                    v-model="selection"
                    :items="itemsArray"
                    selectable
                    return-object
                    open-all
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
              >
                 <template v-slot:[`item.actions`]="{ item }">
                <v-icon
                small
                class="mr-2"
                @click="editItem(item)"
                >
                  mdi-pencil
                </v-icon>
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
          class="elevation-1"
          :search="search">
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
      dialogAdd: false,
      dialogEdit: false,
      dialogDelete: false,
      dialogDetail: false,
      currentItem: '',
      currentProducts: [],
      orders: {},
      selection: [],
      itemsArray: [
        {
          id: 1,
          name: 'Root',
          children: [
            { id: 2, name: 'child 1' },
            { id: 3, name: 'child 2' },
            {
              id: 4,
              name: 'child 3',
              children: [
                { id: 5, name: 'Grandchild #1' },
                { id: 6, name: 'Grandchild #2' }
              ]
            }
          ]
        }
      ],
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
        price: '',
        count: ''
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
    orderAdd () {
      axios.get('http://localhost:8000/api/order-add')
        .then((response) => {
          this.itemsArray = response.data
        })
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
      this.editedIndex = this.orders.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
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
    }
  },
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'Новый заказ' : 'Редактирование заказа'
    }
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
