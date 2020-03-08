import { connect } from 'react-redux'
import React, { Component } from 'react'
import { Table } from 'antd'

import { getAllCategories } from '../../thunks/categoryThunks'

import './_CategoryPageList.scss'

class CategoryPageList extends Component {

  componentDidMount() {
    this.props.getAllCategories()
  }

  render() {
    const { inProgress, categories } = this.props
    if (inProgress === true || Object.entries(categories).length === 0) {
      return 'Patientez'
    }
    const listCategories = Object.values(categories)

    const dataSourceCategories = listCategories.map(oneCategory => ({
      key: oneCategory.id,
      id: oneCategory.id,
      name: oneCategory.name,
      idXJours: oneCategory.id + ' jours', // on peut rajouter des choses en plus que l'on affiche pas forcément dans le tableau
    }))

    const columns = [{
      title: 'ID',
      dataIndex: 'idXJours',
      key: 'id',
      sorter: (a, b) => { console.log(a); console.log(b); return(a.id - b.id) },
      // on peut choisir quelle data afficher, et sur quelle data trier !
      // Ici j'affiche la idXJours mais je trie sur l'id
      // Le trie doit retourner un boolean entre 2 lignes
    }, {
      title: 'Catégorie',
      dataIndex: 'name',
      key: 'name',
      sorter: (a, b) => { return a.name.localeCompare(b.name)},
      // localeCompare est une fonction javascript permettant de trier dans l'ordre alphabétique
      filters: [
        { text: 'Dessert', value: 'Dessert' },
        { text: 'Plat', value: 'Plat' },
      ],
      onFilter: (value, record) => record.name.indexOf(value) === 0,
    }];

    return (
      <div className="BgWhite">
        <Table dataSource={dataSourceCategories} columns={columns} />
      </div>
    )
  }
}

const mapDispatchToProps = {
  getAllCategories,
}

const mapStateToProps = ({ categories: { isFetching, content } }) => {
  return {
    inProgress: isFetching,
    categories: content,
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(CategoryPageList)
