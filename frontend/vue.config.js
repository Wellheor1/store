const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],

  pluginOptions: {
    webpack: {
      dir: [
        './webpack'
      ]
    }
  }
})
