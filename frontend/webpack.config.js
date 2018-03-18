const webpack = require('webpack')
const path = require('path')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const BundleTracker = require('webpack-bundle-tracker')
const CleanWebpackPlugin = require('clean-webpack-plugin')

const inProduction = 'production' === process.env.NODE_ENV
const buildPath = path.resolve(__dirname, '.build/')

module.exports = {
  entry: {
    styles: './assets/sass/app.scss',
    fonts: './assets/sass/fonts.scss',
  },

  devtool: inProduction ? 'source-map' : 'eval-source-map',

  output: {
    path: buildPath,
    filename: './bundles/[name]-[hash].js',
  },

  plugins: [
    new CleanWebpackPlugin(['.build']),
    new BundleTracker({filename: './webpack-stats.json'}),
    new ExtractTextPlugin({
      filename: `css/[name]-[hash].css`,
      allChunks: true,
    }),
    new CopyWebpackPlugin([
      {
        from: 'assets/fonts/',
        to: `${buildPath}/fonts/`,
      },
    ]),
    new CopyWebpackPlugin([
      {
        from: 'node_modules/jquery/dist/',
        to: `${buildPath}/vendor/jquery/`,
      },
    ]),
    new CopyWebpackPlugin([
      {
        from: 'node_modules/bootstrap/dist/',
        to: `${buildPath}/vendor/bootstrap/`,
      },
    ]),
    new CopyWebpackPlugin([
      {
        from: 'node_modules/popper.js/dist/',
        to: `${buildPath}/vendor/popper.js/`,
      },
    ]),
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [/node_modules/],
        use: [{
          loader: 'babel-loader',
        }],
      },
      {
        test: /\.scss$/,
        exclude: [/node_modules/],
        use: ExtractTextPlugin.extract({
          use: [
            {
              loader: 'css-loader',
              options: {
                url: false,
              },
            },
            {
              loader: 'sass-loader',
              options: {
                outputStyle: 'compressed',
              },
            }
          ],
          fallback: 'style-loader',
        }),
      },
    ],
  },
}
