<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card class="mb-2 elevation-7">
          <v-card-title>
            Клиенты
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
                  Добавить клиента</v-btn>
              </template>
          </v-dialog>
          </v-card-title>
             <v-data-table
              :headers="headers"
              :items-per-page="5"
              :items="clients.data"
              multi-sort
              :search="search"
              :footer-props="{
                'items-per-page-text':'Клиентов на странице:'
              }"
              >
              </v-data-table>
          <v-row justify="center">
          </v-row>
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
      headers: [
        { text: 'Номер клиента', value: 'id' },
        { text: 'Фамилия', value: 'last_name' },
        { text: 'Имя', value: 'first_name' },
        { text: 'Отчество', value: 'patronymic' },
        { text: 'Адрес', value: 'address' }
      ]
    }
  },
  methods: {
    getClients () {
      axios.get('http://localhost:8000/api/clients')
        .then((response) => {
          this.clients = response.data
        })
    }
  },
  mounted () {
    this.getClients()
  }
}
</script>

<style scoped>

</style>
