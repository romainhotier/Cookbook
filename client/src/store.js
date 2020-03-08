import { createStore, applyMiddleware, compose } from 'redux'
import thunk from 'redux-thunk'
import { createLogger } from 'redux-logger'
import rootReducer from './redux/rootReducer'

const logger = createLogger()
const composeEnhancers = (typeof window !== "undefined" && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__) || compose;

const store = createStore(rootReducer,
  {},
  composeEnhancers(
    applyMiddleware(thunk, logger),
  )
)

export default store
