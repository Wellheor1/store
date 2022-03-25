import { HTTP } from '@/api/common'

export const Customer = {
  create (config) {
    return HTTP.post('customer', config).then(response => {
      return response.data
    })
  },
  delete (Customer) {
    return HTTP.delete('customer/{customer.id}/')
  },
  list () {
    return HTTP.get('customer').then(response => {
      return response.data
    })
  }
}
