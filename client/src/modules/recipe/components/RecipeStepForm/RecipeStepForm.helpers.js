export const reorder = (list, startIndex, endIndex) => {
  const result = Array.from(list)
  const [removed] = result.splice(startIndex, 1)
  result.splice(endIndex, 0, removed)
  return result
}

export const getListStyle = (isDraggingOver, elementLength) => ({
  border: '1px solid',
  borderColor: isDraggingOver ? 'lightblue' : 'transparent',
  padding: elementLength,
  display: 'flex',
  flexDirection: 'column',
})

// export const getItemStyle = (isDragging, draggableStyle, elementLength) => ({
//   // some basic styles to make the items look a bit nicer
//   userSelect: 'none',
//   padding: elementLength * 2,
//   margin: `0 0 ${elementLength}px 0`,

//   // change background colour if dragging
//   background: isDragging ? 'lightgrey' : '',

//   // styles we need to apply on draggables
//   ...draggableStyle,
// });
