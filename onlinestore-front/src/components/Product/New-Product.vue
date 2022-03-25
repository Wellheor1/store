<template>
  <v-container>
    <v-layout>
      <v-flex xs12 sm6 offset-sm3>
        <h1 class="text--secondary mb-3">Добавить новый товар</h1>
        <v-form ref="form" v-model="valid" lazy-validation class="mb-3">
          <v-text-field
            name="title"
            v-model="title"
            :rules="[v => !!v || 'Обязательное поле']"
            required
            label="Название"
          >
          </v-text-field>
          <v-text-field
            name="vendor"
            v-model="vendor"
            label="Продавец"
          >
          </v-text-field>
          <v-text-field
            name="color"
            v-model="color"
            label="Цвет"
          >
          </v-text-field>
          <v-text-field
            name="material"
            v-model="material"
            label="Материал"
          >
          </v-text-field>
          <v-text-field
            name="price"
            v-model="price"
            type="number"
            :rules="[v => !!v || 'Обязательное поле']"
            required
            label="Цена"
          >
          </v-text-field>
          <v-textarea
            name="description"
            v-model="description"
            label="Описание"
          >
          </v-textarea>
        </v-form>
        <v-layout class="mb-3">
          <v-flex xs12>
            <v-btn class="warning">
              Загрузить
              <v-icon right dark>mdi-cloud-upload</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>
        <v-layout>
          <v-flex xs12>
            <img src="" height="200">
          </v-flex>
        </v-layout>
        <v-layout>
          <v-switch
            color="primary"
            label="Участвует в акции"
            v-model="promo"
          >
          </v-switch>
        </v-layout>
        <v-layout>
          <v-spacer></v-spacer>
          <v-btn
            :disabled="!valid"
            class="success"
            @click="createProduct"
          >Добавить
          </v-btn>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>r

<script>
export default {
  data () {
    return {
      title: '',
      vendor: '',
      color: '',
      material: '',
      price: 0,
      description: '',
      promo: false,
      valid: false
    }
  },
  methods: {
    createProduct () {
      if (this.$refs.form.validate()) {
        const product = {
          title: this.title,
          vendor: this.vendor,
          color: this.color,
          material: this.material,
          price: this.price,
          description: this.description,
          promo: this.promo
        }

        console.log(product)
      }
    }
  }
}
</script>

<style scoped>

</style>
