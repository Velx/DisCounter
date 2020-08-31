const CompressionPlugin = require('compression-webpack-plugin');

module.exports = {
  publicPath: "/",
  "transpileDependencies": [
    "vuetify"
  ],
  chainWebpack(config) {
    config.plugins.delete('prefetch');
    config.optimization.splitChunks({chunks: 'all'})
    config.plugin('CompressionPlugin').use(CompressionPlugin);
  }
}