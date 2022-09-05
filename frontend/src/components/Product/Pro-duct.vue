<template>
  <v-container>
    <section class="product mt-3 elevation-10">
      <v-layout wrap>
        <v-flex xs12 lg6>
          <v-img class="product_img" :src="product.imageSrc"></v-img>
        </v-flex>
        <v-flex xs12 lg6>
          <div class="product_info">
            <h5 class="product_title display-1 mb-3 mt-3">{{ product.title }}</h5>
            <p class="product_category title">
              <span class="product_title">Поставщик: </span> {{ product.vendor.charAt(0).toUpperCase() + product.vendor.substring(1) }}
            </p>
            <p class="product_price title">
              <span class="product_title">Цена: </span>$ {{ product.price }}
            </p>
            <p class="product_color title">
              <span class="product_title">Цвет: </span>
              <span
                :title="product.color"
                :style="{ backgroundColor: product.color}"
                class="product_color__bg"
              >
              </span>
            </p>
            <p class="title">
              <span class="product_title">Материал: </span>{{ product.material.charAt(0).toUpperCase() + product.material.substring(1)  }}
            </p>
            <div class="title mb-3">
              <p class="product_title mb-2">Описание:</p>{{ product.description }}
            </div>
            <v-btn color="primary">Редактировать</v-btn>
            <v-btn color="primary">Купить</v-btn>
            <v-btn color="primary">Удалить</v-btn>
          </div>
        </v-flex>
      </v-layout>
    </section>
  </v-container>
</template>

<script>
export default {
  props: ['id'],
  computed: {
    product () {
      const id = this.id
      return this.$store.getters.productById(id)
    }
  }
}
</script>

<style scoped>
  .product {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    border: 1px solid #1c77ad;
    padding: 30px;
    margin-bottom: 100px;
  }
  .product_img {
    height: 100%;
    width: 550px;
  }
  .product_info {
    margin-left: 50px;
  }
  .product_title {
    font-size: 1.6rem;
    font-width: bold;
    color: #1875d0;
    margin-bottom: 0;
  }
  .product_price {
    color: red;
  }
  .product_color__bg {
    display: inline-block;
    width: 50px;
    height: 20px;
    border: 1px solid #2b2b2b;
    border-radius: 10px;
  }
</style>
