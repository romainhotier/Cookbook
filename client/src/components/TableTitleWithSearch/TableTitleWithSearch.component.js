import React from 'react'
import { Input } from 'antd'

const TableTitleWithSearch = ({ title, filterName, placeholder, onChange }) => (
  <div className="tableTitleWithSearch">
    {title}
    <Input
      placeholder={placeholder}
      onChange={e => onChange(filterName, e.target.value)}
      onClick={e => e.stopPropagation()}
      style={{
        marginTop: '10px',
        fontSize: '10px',
        height: '30px',
        width: '160px',
      }}
    />
  </div>
)

export default TableTitleWithSearch
