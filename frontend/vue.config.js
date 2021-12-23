const path = require("path");

module.exports = {
  pages: {
    'GameRecordPage': {
      // entry for the page
      entry: 'src/pages/GameRecordPage/main.js',
      // the source template
      template: 'public/index.html',
      // output as dist/index.html
      filename: 'GameRecordPage.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'GameRecordPage',
      // chunks to include on this page, by default includes
      // extracted common chunks and vendor chunks.
      chunks: ['chunk-vendors', 'chunk-common', 'GameRecordPage']
    },
    'login': {
      // entry for the page
      entry: 'src/pages/login/main.js',
      // the source template
      template: 'public/index.html',
      // output as dist/index.html
      filename: 'login.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'login',
      // chunks to include on this page, by default includes
      // extracted common chunks and vendor chunks.
      chunks: ['chunk-vendors', 'chunk-common', 'login']
    },
    'logout': {
      // entry for the page
      entry: 'src/pages/logout/main.js',
      // the source template
      template: 'public/index.html',
      // output as dist/index.html
      filename: 'logout.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'logout',
      // chunks to include on this page, by default includes
      // extracted common chunks and vendor chunks.
      chunks: ['chunk-vendors', 'chunk-common', 'logout']
    },
    'ViewGameHistory': {
      // entry for the page
      entry: 'src/pages/ViewGameHistory/main.js',
      // the source template
      template: 'public/index.html',
      // output as dist/index.html
      filename: 'ViewGameHistory.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'ViewGameHistory',
      // chunks to include on this page, by default includes
      // extracted common chunks and vendor chunks.
      chunks: ['chunk-vendors', 'chunk-common', 'ViewGameHistory']
    },
  },
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    proxy: {
      '/proxy': {
        target: 'http://localhost:8010/',
        changeOrigin: true,
        pathRewrite: {
          '^/proxy': ''
        }
      }
    }
  },
  publicPath: process.env.VUE_APP_STATIC_URL,
  outputDir: path.resolve(__dirname, "../build/static", "FRONTEND"),
  indexPath: path.resolve(__dirname, "../build/templates/", "FRONTEND", "index.html"),
}
