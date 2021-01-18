const CracoAntDesignPlugin = require('craco-antd')
const sassResourcesLoader = require('craco-sass-resources-loader')

module.exports = {
  plugins: [
    {
      plugin: CracoAntDesignPlugin,
      options: {
        customizeTheme: {
          '@primary-color': '#85b72c',
          '@link-color': '#85b72c',
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
