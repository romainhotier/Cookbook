import React from 'react'
import { Switch } from 'antd'

import ThemeContext from 'context/Theme.context.js'

const SwitchTheme = () => {
  return (
    <ThemeContext.Consumer>
      {({ theme, setTheme }) => {
        const checked = theme === 'light' ? false : true

        return <Switch defaultChecked onChange={setTheme} checked={checked} />
      }}
    </ThemeContext.Consumer>
  )
}

export default SwitchTheme
