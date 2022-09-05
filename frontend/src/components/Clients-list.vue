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
                      <v-text-field label="Фамилия" v-model="dataNewClient.last_name" :rules="newClientRules" required>
                      </v-text-field>
                      <v-text-field label="Имя" v-model="dataNewClient.first_name" :rules="newClientRules" required>
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
            <v-dialog v-model="dialogEditClient" width="400">
              <v-card>
                <v-card-title>
                  <span class="text-h5">Редактирование клиента</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-form ref="formEdit" v-model="valid" lazy-validation>
                      <v-text-field v-model="editedItem.last_name" :rules="editClientRules" label="Фамилия"
                                    clearable></v-text-field>
                      <v-text-field v-model="editedItem.first_name" :rules="editClientRules" label="Имя"
                                    clearable></v-text-field>
                      <v-text-field v-model="editedItem.patronymic" :rules="editClientRules" label="Отчество"
                                    clearable></v-text-field>
                      <v-text-field v-model="editedItem.address" :rules="editClientRules" label="Адрес"
                                    clearable></v-text-field>
                    </v-form>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="closeDialogEditClient">Отмена</v-btn>
                   <v-btn color="blue darken-1" :disabled="!valid" text @click="saveChangeClient">Сохранить</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-title>
             <v-data-table :headers="headers" :items-per-page="5" :items="clients.data" multi-sort :search="search"
                           :sort-desc=true sort-by="id"
                           :footer-props="{
               'items-per-page-text':'Клиентов на странице:'
              }">
               <template v-slot:[`item.actions`]="{ item }">
                <v-icon small @click="callDialogEditClient(item)">mdi-pencil</v-icon>
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
      dialogEditClient: false,
      dataNewClient: {
        last_name: '',
        first_name: '',
        patronymic: '',
        address: ''
      },
      newClientRules: [
        v => !!v || 'Обязательное поле',
        v => (v && v.length <= 19) || 'Не более 20 символов'
      ],
      editClientRules: [
        v => !!v || 'Обязательное поле'
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
        first_name: '',
        patronymic: '',
        address: ''
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
        this.clients.data.push(this.dataNewClient)
        this.dialogAddClient = false
      }
    },
    callDialogEditClient (item) {
      this.editedIndex = this.clients.data.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogEditClient = true
    },
    closeDialogEditClient () {
      this.dialogEditClient = false
    },
    saveChangeClient () {
      if (this.$refs.formEdit.validate()) {
        Object.assign(this.clients.data[this.editedIndex], this.editedItem)
        axios.post('http://localhost:8000/api/change-client', this.editedItem)
        this.dialogEditClient = false
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
