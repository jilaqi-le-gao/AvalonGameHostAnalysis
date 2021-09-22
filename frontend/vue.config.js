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
}
