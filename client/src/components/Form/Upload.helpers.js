import last from 'lodash/last'

export const displayFile = (url, index) => {
  if (url === undefined) {
    return
  }
  const urlSplited = url.split('/')
  return {
    uid: index,
    name: `${last(urlSplited)}`,
    status: 'done',
    url: `${url}`,
    thumbUrl: `${process.env.REACT_APP_IMAGES_SERVER}/${url}`,
  }
}
