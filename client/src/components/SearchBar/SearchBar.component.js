import React from 'react'
import { Input } from 'antd'

const onSearch = value => console.log(value)

const SearchBar = () => (
  <div className="searchBar">
    <Input.Search placeholder="Rechercher une recette, un ingrédient, ..." onSearch={onSearch} enterButton />
  </div>
)

export default SearchBar
