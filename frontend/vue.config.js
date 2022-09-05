const { defineConfig } = require('@vue/cli-service')
// Путь к приложению в котором храниться статика django
const staticDir = '../static/webpack_build/'
// Путь, относительно static_dir
// В него webpack положит шаблон Vue приложения
const templatePath = '../../templates/index.html'
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
  },
  // Paths
  // Рабочая директория сборки
  // Я обычно указываю директорию приложения django, которое отвечает за фронт
  outputDir: process.env.NODE_ENV === 'production' ? staticDir : 'dist/',
  // Куда пойдёт шаблон проекта
  indexPath: process.env.NODE_ENV === 'production' ? templatePath : 'index.html',
  // Куда пойдут ассеты (относительно outputDir)
  assetsDir: '', // ассеты храним там же, где и JS/CSS
  // Путь по которому можно достать статику
  // Нужно указать тот, который прописан в STATIC_URL настроек django
  publicPath: process.env.NODE_ENV === 'production' ? 'static/webpack_build/' : '/'
})
