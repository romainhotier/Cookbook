import forEach from 'lodash/forEach'

import * as listIconsIngredients from 'ressources/iconsIngredients/Icons'

export const slugify = (str, charUse = '-') => {
  str = str.replace(/^\s+|\s+$/g, '')

  // Make the string lowercase
  str = str.toLowerCase()

  // Remove accents, swap ñ for n, etc
  var from = 'ÁÄÂÀÃÅČÇĆĎÉĚËÈÊẼĔȆÍÌÎÏŇÑÓÖÒÔÕØŘŔŠŤÚŮÜÙÛÝŸŽáäâàãåčçćďéěëèêẽĕȇíìîïňñóöòôõøðřŕšťúůüùûýÿžþÞĐđßÆa·/_,:;'
  var to = 'AAAAAACCCDEEEEEEEEIIIINNOOOOOORRSTUUUUUYYZaaaaaacccdeeeeeeeeiiiinnooooooorrstuuuuuyyzbBDdBAa------'
  for (var i = 0, l = from.length; i < l; i++) {
    str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i))
  }

  // Remove invalid chars
  str = str
    .replace(/[^a-z0-9 -]/g, '')
    // Collapse whitespace and replace by -
    .replace(/\s+/g, charUse)
    // Collapse dashes
    .replace(/-+/g, charUse)

  return str
}

export const slugifyResponse = str => {
  return slugify(str, '_')
}

export const searchInListIcons = slug => {
  const icon = listIconsIngredients[`${slug}`]

  if (icon !== undefined) {
    return icon
  }

  const data = []
  forEach(listIconsIngredients, icon => {
    if (icon.includes(slug)) {
      data.push(icon)
    }
  })

  if (data.length > 0) {
    return data[0]
  }

  const slugArray = slug.split('-')

  forEach(listIconsIngredients, icon => {
    slugArray.filter(word => {
      if (word.length >= 3 && icon.includes(word)) {
        data.push(icon)
      }
      return ''
    })
  })

  if (data.length > 0) {
    return data.length > 0 ? data[0] : ''
  }
}
