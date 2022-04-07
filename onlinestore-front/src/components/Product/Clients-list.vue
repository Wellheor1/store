<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card class="mb-2 elevation-7">
          <v-card-title>
            Клиенты
            <v-spacer></v-spacer>
            <v-text-field v-model="search" append-icon="mdi-magnify" label="Поиск">
            </v-text-field>
            <v-spacer></v-spacer>
             <v-dialog v-model="dialogAddClient" width="400">
              <template v-slot:activator="{ attrs }">
                <v-btn color="primary" dark v-bind="attrs" @click="callDialogAddClient">Добавить клиента</v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="text-h5">Новый клиент</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-form ref="form" v-model="valid" lazy-validation>
                      <v-text-field label="Фамилия" v-model="dataNewClient.lastName" :rules="newClientRules" required>
                      </v-text-field>
                      <v-text-field label="Имя" v-model="dataNewClient.firstName" :rules="newClientRules" required>
                      </v-text-field>
                      <v-text-field label="Отчество" v-model="dataNewClient.patronymic" :rules="newClientRules" required>
                      </v-text-field>
                      <v-text-field label="Адрес" v-model="dataNewClient.address" :rules="newClientRules" required>
                      </v-text-field>
                    </v-form>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="closeDialogAddClient">Отмена</v-btn>
                   <v-btn color="blue darken-1" :disabled="!valid" text @click="saveNewClient">Сохранить</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-title>
             <v-data-table :headers="headers" :items-per-page="5" :items="clients.data" multi-sort :search="search"
                           :footer-props="{
               'items-per-page-text':'Клиентов на странице:'
              }">
               <template v-slot:[`item.actions`]="{ item }">
                <v-icon small @click="callEditDialog(item)">mdi-pencil</v-icon>
               </template>
             </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>r

<script>
import axios from 'axios'

export default {
  data () {
    return {
      search: '',
      clients: [],
      dialogDeleteClient: false,
      dialogAddClient: false,
      dataNewClient: {
        lastName: '',
        firstName: '',
        patronymic: '',
        address: ''
      },
      newClientRules: [
        v => !!v || 'Обязательное поле',
        v => (v && v.length <= 19) || 'Не более 20 символов'
      ],
      valid: false,
      headers: [
        { text: 'Номер клиента', value: 'id' },
        { text: 'Фамилия', value: 'last_name' },
        { text: 'Имя', value: 'first_name' },
        { text: 'Отчество', value: 'patronymic' },
        { text: 'Адрес', value: 'address' },
        { text: 'Действия', value: 'actions' }
      ],
      editedIndex: -1,
      editedItem: {
        last_name: '',
        manufacturer: '',
        count: '',
        price: ''
      }
    }
  },
  methods: {
    getClients () {
      axios.get('http://localhost:8000/api/clients')
        .then((response) => {
          this.clients = response.data
        })
    },
    callDialogAddClient () {
      this.dialogAddClient = true
    },
    closeDialogAddClient () {
      this.dialogAddClient = false
    },
    saveNewClient () {
      if (this.$refs.form.validate()) {
        axios.post('http://localhost:8000/api/add-client', this.dataNewClient)
        this.dialogAddClient = false
      }
    }
  },
  mounted () {
    this.getClients()
  }
}
</script>

<style scoped>

</style>
