<template>
  <v-container style="height: 90vh;">
    <v-row justify="center" align="center" class="fill-height">
      <v-col cols="12" sm="6" md="6" lg="4" class="rounded-lg elevation-24">
          <v-form ref="form" v-model="valid" lazy-validation class="ma-9">
            <v-text-field
              name="login"
              v-model="login"
              :rules="loginRules"
              placeholder="Имя пользователя"
              prepend-icon="mdi-account"
              maxlength="20"
              required
            >
            </v-text-field>
            <v-text-field
              name="password"
              v-model="password"
              :rules="passRules"
              placeholder="Пароль"
              prepend-icon="mdi-lock"
              :append-icon="passVisibleOne ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="() => (passVisibleOne = !passVisibleOne)"
              :type="passVisibleOne ? 'password' : 'text'"
              required
            >
            </v-text-field>
            <v-text-field
              name="confirmPassword"
              v-model="confirmPassword"
              :rules="confirmPasswordRules"
              placeholder="Подтверждение пароля"
              prepend-icon="mdi-repeat"
              :append-icon="passVisibleTwo ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="() => (passVisibleTwo = !passVisibleTwo)"
              :type="passVisibleTwo ? 'password' : 'text'"
            >
            </v-text-field>
            <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="onSubmit"
            >
              Создать аккаунт
            </v-btn>
          </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  data: function () {
    return {
      valid: false,
      login: '',
      loginRules: [
        v => !!v || 'Обязательное поле',
        v => (v && v.length <= 19) || 'Не более 20 символов'
      ],
      password: '',

      passRules: [
        v => !!v || 'Обязательное поле'
      ],
      confirmPassword: '',
      confirmPasswordRules: [
        v => !!v || 'Обязательное поле',
        v => v === this.password || 'Пароли должны совпадать'
      ],
      checkbox: false,
      passVisibleOne: true,
      passVisibleTwo: true
    }
  },
  methods: {
    onSubmit () {
      if (this.$refs.form.validate()) {
        const user = {
          login: this.login,
          password: this.password
        }
        console.log(user)
      }
    }
  }
}
</script>

<style scoped>
</style>
