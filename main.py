from catalog import Category, Product, load_catalog_from_json


def main() -> None:
    categories = load_catalog_from_json("products.json")

    for category in categories:
        print(f"{category.name}: {category.description}")
        for product in category.products:
            print(f"  - {product.name} — {product.price} руб. ({product.quantity} шт.)")

    print()
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
