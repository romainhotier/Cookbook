const CracoAntDesignPlugin = require('craco-antd')
const sassResourcesLoader = require('craco-sass-resources-loader')

module.exports = {
  jest: {
    configure: {
      verbose: true,
      testEnvironment: 'jsdom',
      collectCoverageFrom: ['src/**/*.{js}', '!**/__tests__/**', '!**/__mocks__/**', '!src/**/index.js', '!src/*.js'],
      setupFiles: ['<rootDir>/src/setupTests.js'],
    },
  },
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
