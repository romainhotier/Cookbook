const CracoAntDesignPlugin = require('craco-antd')
const sassResourcesLoader = require('craco-sass-resources-loader')

module.exports = {
  plugins: [
    {
      plugin: CracoAntDesignPlugin,
      options: {
        customizeTheme: {
          '@primary-color': '#9254de',
          '@link-color': '#9254de',
        },
      },
    },
    {
      plugin: sassResourcesLoader,
      options: {
        resources: './src/styles/_variables.scss',
      },
    },
  ],
}
