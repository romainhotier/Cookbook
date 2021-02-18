import React, { useState } from 'react'
import PropTypes from 'prop-types'
import { Drawer, Button } from 'antd'

import { Nav } from './Nav.component'

import './_Menu.scss'

export const MobileMenu = ({ className }) => {
  const [visibleDrawer, setVisibleDrawer] = useState(false)
  return (
    <div className={`${className}`}>
      <nav className="layout_menu">
        <div className="layout_logo">
          <h1>Cook</h1>
        </div>

        <Button className="barsMenu" type="primary" onClick={() => setVisibleDrawer(true)}>
          <i className="fas fa-bars"></i>
        </Button>
        <Drawer
          title="Basic Drawer"
          placement="left"
          closable={false}
          onClose={() => setVisibleDrawer(false)}
          visible={visibleDrawer}
        >
          <div className="layout_menu_items">
            <Nav />
          </div>
        </Drawer>
      </nav>
    </div>
  )
}

MobileMenu.propTypes = {
  className: PropTypes.string,
}
