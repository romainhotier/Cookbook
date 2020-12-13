const CracoAntDesignPlugin = require('craco-antd')
const sassResourcesLoader = require('craco-sass-resources-loader')

module.exports = {
  plugins: [
    {
      plugin: CracoAntDesignPlugin,
    },
    {
      plugin: sassResourcesLoader,
      options: {
        resources: './src/styles/_variables.scss',
      },
    },
  ],
}
