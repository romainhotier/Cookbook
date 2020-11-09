const CracoAntDesignPlugin = require("craco-antd");
const sassResourcesLoader = require('craco-sass-resources-loader');
const path = require("path");

module.exports = {
  plugins: [
    {
      plugin: CracoAntDesignPlugin,
      // options: {
      //   customizeThemeLessPath: path.join(
      //     __dirname,
      //     "../antd.customize.less"
      //   ),
      // },
    },
    {
      plugin: sassResourcesLoader,
      options: {
        resources: './src/styles/_variables.scss',
      },
    },
  ]
};
