import { displayFile } from '../Upload.helpers'

describe('displayFile', () => {
  it('should displayFile without url return nothing', () => {
    const wrapper = displayFile()
    expect(wrapper).toBeUndefined()
  })
})
