<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card class="elevation-7">
          <v-card-title>
            Заказы
            <v-spacer></v-spacer>
            <v-text-field v-model="search" append-icon="mdi-magnify" label="Поиск"></v-text-field>
            <v-spacer></v-spacer>
          </v-card-title>
          <v-dialog v-model="dialogCancelOrder" width="650">
                  <v-card>
                    <v-card-title class="text-h5">Вы уверены что хотите отменить этот заказ?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="closeDialogCancel">Отменить</v-btn>
                    <v-btn color="blue darken-1" text @click="cancelOrderConfirm">Ок</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                 </v-card>
          </v-dialog>
           <v-dialog v-model="dialogCompetedOrder" width="400">
                  <v-card>
                    <v-card-title class="text-h5">Заказ исполнен?</v-card-title>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="closeDialogComleted">Отменить</v-btn>
                    <v-btn color="blue darken-1" text @click="completedOrderConfirm">Ок</v-btn>
                    <v-spacer></v-spacer>
                  </v-card-actions>
                 </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDetail" width="600">
            <v-card>
              <v-data-table :headers="headersDetail" :items-per-page="10" :items="currentProducts['product']"
                            :footer-props="{
                'items-per-page-text':'Товаров на странице:'
              }">
                <template v-slot:[`item.count`]="props">
                  <v-edit-dialog
                    :return-value.sync="props.item.count" @save="save(props)" @cancel="cancel" @open="open" @close="close"
                    large save-text="Сохранить" cancel-text="Отмена">
                    {{ props.item.count }}
                    <template v-slot:input>
                      <v-text-field type="number" v-model="props.item.count" label="Редактирование" single-line
                                    counter
                      ></v-text-field>
                    </template>
                  </v-edit-dialog>
                </template>
                <template v-slot:[`item.actions`]="{ item }">
                <v-icon small class="mr-2" @click="deleteCurrentProduct(item)">mdi-delete</v-icon>
                </template>
              </v-data-table>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDetail">Добавить товар</v-btn>
                <v-btn color="blue darken-1" text @click="closeDetail">Отмена</v-btn>
              </v-card-actions>
             </v-card>
          </v-dialog>
          <v-data-table :headers="headers" :items="orders[`data`]" :items-per-page="5" multi-sort :search="search"
                        :sort-desc=true sort-by="id"
                          :footer-props="{
              'items-per-page-text':'Заказов на странице:'
            }">
              <template v-slot:[`item.actions`]="{ item }">
                <v-icon small color="success" class="mr-2" @click="callDialogCompletedOrder(item)">mdi-check-bold</v-icon>
                <v-icon small class="mr-2" @click="loadCurrentProducts(item)">mdi-eye</v-icon>
                <v-icon small @click="callDialogCancelOrder(item)">mdi-delete</v-icon>
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
      dialogCancelOrder: false,
      dialogDetail: false,
      dialogCompetedOrder: false,
      currentProducts: {},
      orders: {},
      clients: [],
      headers: [
        { text: 'Номер заказа', value: 'id' },
        { text: 'Дата заказа', value: 'date_time' },
        { text: 'Клиент', value: 'name_client' },
        { text: 'Адрес клиента', value: 'client_address' },
        { text: 'Статус', value: 'status' },
        { text: 'Действия', value: 'actions', sortable: false }
      ],
      headersDetail: [
        { text: 'Название товара', value: 'title' },
        { text: 'Производитель', value: 'manufacturer' },
        { text: 'Количество', value: 'count' },
        { text: 'Цена', value: 'price' },
        { text: 'Действия', value: 'actions', sortable: false }
      ],
      itemIndex: -1,
      itemId: -1,
      orderId: -1,
      editedItem: {
        title: '',
        manufacturer: '',
        count: '',
        price: ''
      }
    }
  },
  methods: {
    getNewOrders () {
      axios.get('http://localhost:8000/api/orders')
        .then((response) => {
          this.orders = response.data
        })
    },
    loadCurrentProducts (item) {
      axios.post('http://localhost:8000/api/current-product', { pk: item.id })
        .then((response) => {
          this.currentProducts = response.data
          this.orderId = item.id
        })
      this.dialogDetail = true
    },
    callDialogCancelOrder (item) {
      this.itemId = item.id
      this.itemIndex = this.orders.data.indexOf(item)
      this.dialogCancelOrder = true
    },
    callDialogCompletedOrder (item) {
      this.itemId = item.id
      this.itemIndex = this.orders.data.indexOf(item)
      this.dialogCompetedOrder = true
    },
    deleteCurrentProduct (item) {
      axios.post('http://localhost:8000/api/delete-current-product', { id_product: item.id, id_order: this.orderId })
      this.itemIndex = this.currentProducts.product.indexOf(item)
      this.currentProducts.product.splice(this.editedIndex, 1)
    },
    cancelOrderConfirm () {
      axios.post('http://localhost:8000/api/cancel-order', { id: this.itemId, status: 'Отменён' })
      this.orders.data.splice(this.itemIndex, 1)
      this.dialogCancelOrder = false
    },
    completedOrderConfirm () {
      axios.post('http://localhost:8000/api/completed-order', { id: this.itemId, status: 'Выполнен' })
      this.orders.data.splice(this.itemIndex, 1)
      this.dialogCompetedOrder = false
    },
    closeDetail () {
      this.dialogDetail = false
    },
    closeDialogCancel () {
      this.dialogCancelOrder = false
    },
    closeDialogComleted () {
      this.dialogCompetedOrder = false
    },
    save (props) {
      axios.post('http://localhost:8000/api/change-count-product-order', { id: props.item.id, count: props.item.count })
    },
    cancel () {},
    open () {},
    close () {}
  },
  mounted () {
    this.getNewOrders()
  }
}
</script>
<style scoped>
</style>
