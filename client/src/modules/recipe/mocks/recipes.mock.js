export const fileRecipe = ['recipe/5fdf4387e29e317ae857b5e6/pancake-banane.jpg']
export const fileRecipeStep = ['recipe/5fdf4387e29e317ae857b5e6/steps/5fdf4387e29e317ae857b5e2/pancake-banane.jpg']

export const recipes = {
  content: [
    {
      _id: '5fdf4387e29e317ae857b5e6',
      calories: 1856.88,
      cooking_time: '20',
      level: 0,
      nb_people: '28',
      note: '',
      preparation_time: '5',
      resume: '',
      files: [],
      slug: 'pancakes-a-la-banane',
      status: 'finished',
      title: 'Pancakes à la banane',
      categories: ['Sucrée', 'Healthy', 'Petit dej'],
      ingredients: [
        {
          _id: '5fdb8dbdc0749c35c039b43f',
          quantity: '4',
          unit: 'portion',
        },
        {
          _id: '6gtr48dc0749c35c039b43f',
          quantity: '4',
          unit: 'g',
        },
      ],
      steps: [
        {
          _id: '5fdf4387e29e317ae857b5e2',
          files: ['123.jpg', '456.jpg'],
          description:
            "Ecraser les bananes en purée et mélanger tous les ingrédients, jusqu'à l'obtention d'une pâte lisse. ",
        },
        {
          _id: '5fdf4387e29e317ae857b5e3',
          description:
            "Chauffer une poêle à feu moyen. Si la poêle n'est pas anti-adhésive, badigeonnez-la d'huile de coco (ou autres matières grasses). ",
        },
      ],
    },
    {
      _id: '5fdf490ce29e317ae857b60f',
      calories: 3374.98,
      cooking_time: '120',
      level: 0,
      nb_people: '12',
      files: ['recipes/12345/marbre.jpg'],
      note: '',
      preparation_time: '15',
      resume: '',
      slug: 'marbre-butternut',
      status: 'finished',
      title: 'Marbré Butternut',
      categories: ['Sucrée', 'Healthy', 'Petit dej'],
      ingredients: [
        {
          _id: '5fdb8dbdc0749c35c039b43f',
          quantity: '4',
          unit: 'portion',
        },
      ],
    },
    {
      _id: '602690f58c0ff36f9dbcc810',
      calories: 843.5,
      cooking_time: '15',
      level: 0,
      nb_people: '16',
      note: '',
      preparation_time: '20',
      resume: '',
      slug: 'samoussas-a-la-viande-hachee',
      status: 'in_progress',
      title: 'Samoussas à la viande hachée',
      categories: [],
      ingredients: [
        {
          _id: '5fdb8dbdc0749c35c039b43f',
          quantity: '4',
          unit: 'portion',
        },
      ],
    },
  ],
  loadingFetchRecipe: false,
}

export const recipeStep = [
  {
    _id: '5fdf4387e29e317ae857b5e2',
    files: ['123.jpg', '456.jpg'],
    description:
      "Ecraser les bananes en purée et mélanger tous les ingrédients, jusqu'à l'obtention d'une pâte lisse. ",
  },
  {
    _id: '5fdf4387e29e317ae857b5e3',
    description:
      "Chauffer une poêle à feu moyen. Si la poêle n'est pas anti-adhésive, badigeonnez-la d'huile de coco (ou autres matières grasses). ",
  },
]
