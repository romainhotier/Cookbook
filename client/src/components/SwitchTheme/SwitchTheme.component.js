import React from 'react'
import { Switch } from 'antd'

import ThemeContext from 'context/Theme.context.js'

const SwitchTheme = () => {
  return (
    <ThemeContext.Consumer>
      {({ theme, setTheme }) => {
        const checked = theme === 'light' ? false : true
        return (
          <>
            <i className="fas fa-sun"></i>
            <Switch defaultChecked onChange={setTheme} checked={checked} />
            <i className="fas fa-moon"></i>
          </>
        )
      }}
    </ThemeContext.Consumer>
  )
}

export default SwitchTheme