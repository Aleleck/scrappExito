#"cerveza, aguardiente, ron, whisky"=https://www.exito.com/mercado/vinos-y-licores/aguardiente/cervezas/ron/whisky?fuzzy=0&initialMap=c,c&initialQuery=mercado/vinos-y-licores&map=category-1,category-2,category-3,category-3,category-3,category-3&operator=and&order=OrderByBestDiscountDESC&page=
#""
#
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem')))

productos = driver.find_elements(By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem')

for producto in productos:
    nombre = producto.find_element(By.XPATH, './/h3/span').text
 
    precios = producto.find_elements(By.XPATH, './/div[contains(@class, "price")]/div/span')
    precios_lista = [precio.text for precio in precios]
        
    imagenes = producto.find_elements(By.XPATH, './/div[contains(@class, "vtex-product-summary-2-x-imageContainer")]/div/img')
    img_urls = [imagen.get_attribute("src") for imagen in imagenes]
        
    df = pd.concat([df, pd.DataFrame({"Imagen": [img_urls],
                                          "nombre": [nombre], 
                                          "Precios": [precios_lista] 
                                          })], ignore_index=True)

# Imprimir el DataFrame con todos los nombres de productos
st.table(df)
