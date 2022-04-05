<template>
  <v-container>
    <v-row>
      <v-col>
      </v-col>
    </v-row>
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
