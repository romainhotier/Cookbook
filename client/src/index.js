import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router } from "react-router-dom"
import { Provider } from 'react-redux'

import * as serviceWorker from './serviceWorker.js'

import Layout from './components/Layout'
import store from './store.js'

import 'antd/dist/antd.less';
import './styles/core.scss';

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <Router>
        <Layout />
      </Router>
    </Provider>,
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
