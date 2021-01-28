Rails.application.routes.draw do
  resources :line_items
  resources :carts
  root 'store#index' , as: 'store_index'


  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
