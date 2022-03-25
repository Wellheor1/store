export default {
  state: {
    products: [
      {
        id: '1',
        title: 'Lenovo Legion Y250',
        vendor: 'Lenovo',
        color: 'black',
        material: 'metal/plasctic',
        description: 'Inter fsdfdsfdsfsdfsdfsdfsdfsdfsd sdfsdf sd sdfsdf sfsdf s fsdfs',
        price: 784,
        promo: false,
        imageSrc: 'https://trudogolik24.ru/pic/tov/bc/20200702205848157.jpg'
      },
      {
        id: '2',
        title: 'Asus FX503VD',
        vendor: 'Asus',
        color: 'white',
        material: 'plasctic',
        description: 'Inter fsdfdsfdsfsdfsdfsdfsdfsdfsd sdfsdf sd sdfsdf sfsdf s fsdfs',
        price: 9700,
        promo: true,
        imageSrc: 'https://pc-arena.ru/upload/iblock/90b/90bc58529eb99a680e5b136f87fc2bca.jpg'
      },
      {
        id: '3',
        title: 'ASUS TIF Gaming FX504GD',
        vendor: 'ASUS',
        color: 'black',
        material: 'metal/plasctic',
        description: 'Inter fsdfdsfdsfsdfsdfsdfsdfsdfsd sdfsdf sd sdfsdf sfsdf s fsdfs',
        price: 1220,
        promo: true,
        imageSrc: 'https://skl-trade.ru/d/89364.jpg'
      }
    ]
  },
  getters: {
    products (state) {
      return state.products
    },
    promoProducts (state) {
      return state.products.filter(product => {
        return product.promo
      })
    },
    myProducts (state) {
      return state.products
    },
    productById (state) {
      return productId => {
        return state.products.find(product => product.id === productId)
      }
    }
  },
  mutations: {
  },
  actions: {
  }
}
