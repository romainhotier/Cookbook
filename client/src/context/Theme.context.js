import React, { useState, useEffect } from 'react'

const ThemeContext = React.createContext({
  theme: 'light',
  setTheme: () => {},
})

export function ThemeProvider({ children, localStorage }) {
  const [theme, setTheme] = useState(localStorage)
  const nextTheme = theme === 'light' ? 'dark' : 'light'

  const toggleTheme = () => {
    setTheme(nextTheme)
    window.localStorage.setItem('theme', nextTheme)
  }

  useEffect(() => {
    document.body.dataset.theme = theme
  }, [theme])

  return <ThemeContext.Provider value={{ theme, setTheme: toggleTheme }}>{children}</ThemeContext.Provider>
}

export default ThemeContext
