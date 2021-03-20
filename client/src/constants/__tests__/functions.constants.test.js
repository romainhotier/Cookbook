import { slugify, slugifyResponse, searchInListIcons, worldConnector } from '../functions.constants'

describe('functions.constants', () => {
  describe('slugify', () => {
    it('should render good slug', () => {
      const slugOne = slugify('Pancake à la banane')
      expect(slugOne).toEqual('pancake-a-la-banane')

      const slugTwo = slugify('Beurre de cacahuètes (Nu3)')
      expect(slugTwo).toEqual('beurre-de-cacahuetes-nu3')
    })
  })

  describe('slugifyResponse', () => {
    it('should render good slug', () => {
      const slugOne = slugifyResponse('Pancake à la banane')
      expect(slugOne).toEqual('pancake_a_la_banane')

      const slugTwo = slugifyResponse('Beurre de cacahuètes (Nu3)')
      expect(slugTwo).toEqual('beurre_de_cacahuetes_nu3')
    })
  })

  describe('searchInListIcons', () => {
    it('should render good icon', () => {
      const iconOne = searchInListIcons('beurre-de-cacahuetes-nu3')
      expect(iconOne).toEqual('cacahuete.svg')

      const iconTwo = searchInListIcons('beurre')
      expect(iconTwo).toEqual('beurre.svg')

      const iconThree = searchInListIcons('citron')
      expect(iconThree).toEqual('citron-jaune.svg')

      const iconFour = searchInListIcons('labelo')
      expect(iconFour).toEqual('')
    })
  })

  describe('worldConnector', () => {
    it('should render good connector', () => {
      const connectorOne = worldConnector('beurre')
      expect(connectorOne).toEqual('de beurre')

      const connectorTwo = worldConnector('oeuf')
      expect(connectorTwo).toEqual("d'oeuf")
    })
  })
})
