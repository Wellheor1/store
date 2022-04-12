<template>
  <div>
    <v-navigation-drawer v-model="drawer" app temporary>
      <v-list>
       <v-list-item v-for="(link, i) in links" :key="i" :to="link.url">
          <v-list-item-icon>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="link.title"></v-list-item-title>
          </v-list-item-content>
          </v-list-item>
    </v-list>
    </v-navigation-drawer>
    <v-app-bar app dark color="primary">
      <v-app-bar-nav-icon @click="drawer = !drawer"
      class="hidden-md-and-up"></v-app-bar-nav-icon>
      <v-app-bar-title>
        <router-link
          :to="'/'"
          tag="span"
          class="pointer"
        >ИС "Магазин"</router-link>
      </v-app-bar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items app class="hidden-sm-and-down">
        <v-btn depressed color="primary"
               v-for="(link, i) in links"
               :key="i"
               :to='link.url'>
          <v-icon left>{{ link.icon }}</v-icon>
            {{link.title}}
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </div>
</template>

<script>;
export default {
  name: 'Nav-bar',
  data () {
    return {
      drawer: null,
      links: [
        { title: 'Вход', icon: 'mdi-account-box', url: '/login' },
        { title: 'Заказы', icon: 'mdi-cart', url: '/orders' },
        { title: 'Клиенты', icon: 'mdi-account', url: '/clients' },
        { title: 'Товары', icon: 'mdi-format-list-bulleted', url: '/products' },
        { title: 'Отчёты', icon: 'mdi-chart-box', url: '/reports' }
      ]
    }
  }
}
</script>
<style scoped>
  .pointer {
    cursor: pointer;
  }
</style>
