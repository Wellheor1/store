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
            v-model="dialog"
            width="600"
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
                      <v-text-field
                      v-model="editedItem.date_time"
                      label="Дата заказа"
                      clearable>
                      </v-text-field>
                      <v-text-field
                      v-model="editedItem.name_client"
                      label="Клиент"
                      clearable
                      >
                      </v-text-field>
                      <v-text-field
                      v-model="editedItem.client_address"
                      label="Адрес клиента"
                      clearable
                      >
                      </v-text-field>
                      <v-text-field
                      v-model="editedItem.product"
                      label="Товары"
                      clearable
                      >
                      </v-text-field>
                      <v-text-field
                      v-model="editedItem.manufacturer"
                      label="Производитель"
                      clearable
                      >
                      </v-text-field>
                      <v-text-field
                      v-model="editedItem.price"
                      label="Цена"
                      clearable
                      >
                      </v-text-field>
                      <v-text-field
                      v-model="editedItem.count"
                      label="Количество"
                      clearable
                      >
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
                  @click="save"
                  >
                     Сохранить
                   </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-title>
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
              <v-card-title>
                  <span class="text-h5">Детали заказа</span>
                </v-card-title>
              <v-card-actions>
                <v-card-text>
                  <v-text-field
                disabled
                v-model="editedItem.name_client"
                  >
                </v-text-field>
                 <v-text-field
                disabled
                v-model="editedItem.client_address"
                 >
                </v-text-field>
                 <v-text-field
                v-model="editedItem.date_time"
                disabled
                 >
                </v-text-field>
                </v-card-text>
              </v-card-actions>
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
                  @click="editItem(item)"
                >
                  mdi-pencil
                </v-icon>
                <v-icon
                  small
                  class="mr-2"
                  @click="deleteItem(item)"
                >
                  mdi-delete
                </v-icon>
                <v-icon
                small
                @click="orderDetail(item)"
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
      dialog: false,
      dialogDelete: false,
      dialogDetail: false,
      headers: [
        { text: 'Номер заказа', value: 'id' },
        { text: 'Дата заказа', value: 'date_time' },
        { text: 'Клиент', value: 'name_client' },
        { text: 'Адрес клиента ', value: 'client_address' },
        { text: 'Товары', value: 'products' },
        { text: 'Производитель', value: 'manufacturer' },
        { text: 'Цена', value: 'price' },
        { text: 'Количество', value: 'count' },
        { text: 'Действия', value: 'actions', sortable: false }
      ],
      editedIndex: -1,
      editedItem: {
        date_time: '',
        name_client: '',
        client_address: '',
        products: '',
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
      },
      orders: {
      }
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
    editItem (item) {
      this.editedIndex = this.orders.data.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.orders.data.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    orderDetail (item) {
      this.editedIndex = this.orders.data.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDetail = true
    },
    deleteItemConfirm () {
      this.orders.data.splice(this.editedIndex, 1)
      this.closeDelete()
    },
    close () {
      this.dialog = false
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
    save () {
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
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    }
  },
  mounted () {
    this.get_orders()
  }
}
</script>

<style scoped>

</style>
