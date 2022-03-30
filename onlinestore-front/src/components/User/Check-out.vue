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
            label="Search"
            >
            </v-text-field>
            <v-spacer></v-spacer>
            <v-dialog
            v-model="dialog"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                color="primary"
                dark
                v-bind="attrs"
                v-on="on"
                >
                  Добавить заказ</v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">{{formTitle}}</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12"
                      sm="6"
                      md="4"
                      >
                      <v-text-field
                      v-model="editedItem.order_date"
                      label="Дата заказа">
                      </v-text-field>
                      </v-col>
                      <v-col cols="12"
                      sm="6"
                      md="4"
                      >
                      <v-text-field
                      v-model="editedItem.name_client"
                      label="Клиент"
                      >
                      </v-text-field>
                      </v-col>
                      <v-col cols="12"
                      sm="6"
                      md="4"
                      >
                      <v-text-field
                      v-model="editedItem.address_client"
                      label="Адрес клиента"
                      >
                      </v-text-field>
                      </v-col>
                      <v-col cols="12"
                      sm="6"
                      md="4"
                      >
                      <v-text-field
                      v-model="editedItem.product"
                      label="Товары">
                      </v-text-field>
                      </v-col>
                      <v-col cols="12"
                      sm="6"
                      md="4"
                      >
                      <v-text-field
                      v-model="editedItem.manufacturer"
                      label="Производитель">
                      </v-text-field>
                      </v-col>
                      <v-col cols="12"
                      sm="6"
                      md="4"
                      >
                      <v-text-field
                      v-model="editedItem.price"
                      label="Цена">
                      </v-text-field>
                      </v-col>
                      <v-col cols="12"
                      sm="6"
                      md="4"
                      >
                      <v-text-field
                      v-model="editedItem.count"
                      label="Количество">
                      </v-text-field>
                      </v-col>
                    </v-row>
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
                  @click="save"
                  >
                     Сохранить
                   </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-title>
          <v-dialog v-model="dialogDelete">
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
            <v-data-table
          :headers="headers"
          :items="order"
          :items-per-page="5"
          multi-sort
          :expanded.sync="expanded"
          item-key="id"
          show-expand
          class="elevation-1"
          :search="search">
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
                  @click="deleteItem(item)"
                >
                  mdi-delete
                </v-icon>
              </template>
              <template v-slot:expanded-item="{ headers, item }">
                <td :colspan="headers.length">
                  More info about {{ item.id }}
                </td>
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
      expanded: [],
      singleExpand: false,
      search: '',
      dialog: false,
      dialogDelete: false,
      headers: [
        { text: 'Номер заказа', value: 'id' },
        { text: 'Дата заказа', value: 'order_date' },
        { text: 'Клиент', value: 'name_client' },
        { text: 'Адрес клиента ', value: 'address_client' },
        { text: 'Товары', value: 'product' },
        { text: 'Производитель', value: 'manufacturer' },
        { text: 'Цена', value: 'price' },
        { text: 'Количество', value: 'count' },
        { text: 'Действия', value: 'actions', sortable: false }
      ],
      order: [],
      editedIndex: -1,
      editedItem: {
        order_date: '',
        name_client: '',
        address_client: '',
        product: '',
        manufacturer: '',
        price: '',
        count: ''
      },
      defaultItem: {
        order_date: '',
        name_client: '',
        address_client: '',
        product: '',
        manufacturer: '',
        price: '',
        count: ''
      },
      orders: [
      ]
    }
  },
  methods: {
    get_orders () {
      axios.get('http://localhost:8000/api/orders')
        .then((response) => {
          this.orders = response.data
          console.log(this.orders)
        })
    },
    initialize () {
      this.order = [
        {
          id: 1,
          order_date: '30.03.2022',
          name_client: 'Антонюк Глеб Родинович',
          address_client: 'Советская 57',
          product: 'Ноутбук Lenovo Y250 S7',
          manufacturer: 'Lenovo',
          price: 3501,
          count: '10'
        },
        {
          id: 2,
          order_date: '30.03.2021',
          name_client: 'Антонюк Глеб Родинович3',
          address_client: 'Советская 58',
          product: 'Ноутбук Lenovo Y250 S8',
          manufacturer: 'Lenovo',
          price: 3503,
          count: '5'
        }
      ]
    },
    editItem (item) {
      this.editedIndex = this.order.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.order.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      this.order.splice(this.editedIndex, 1)
      this.closeDelete()
    },
    close () {
      this.dialog = false
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
    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.order[this.editedIndex], this.editedItem)
      } else {
        this.order.push(this.editedItem)
      }
      this.close()
    }
  },
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    }
  },
  watch: {
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    }
  },
  created () {
    this.initialize()
  }
}
</script>

<style scoped>

</style>
