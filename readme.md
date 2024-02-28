## API list

### Lấy danh sách Users

- **Endpoint:** `/users`
- **Phương thức:** GET
- **Sử dụng:** [http://localhost:2222/users](http://localhost:2222/users)

### Thêm

- **Endpoint:** `/users`
- **Phương thức:** POST
- **Mô tả:** Thêm 1 user
- **Sử dụng:** Sử dụng `Postman` để thực hiện yêu cầu POST tới [http://localhost:2222/users](http://localhost:2222/users) với `JSON`:

    ```json
    {
      "name": "The Anh"
    }
    ```


### Xóa 1 User

- **End point:** `/users/{user_id}`
- **Phương thức:** DELETE
- **Mô tả:** Xóa người dùng theo ID.
- **Sử dụng:**  Sử dụng `Postman` để thực hiện yêu cầu DELETE tới [http://localhost:2222/users/{user_id}](http://localhost:2222/users/{user_id}). Thay thế `{user_id}` bằng ID của người dùng bạn muốn xóa.

## Dừng API

Để dừng API và loại bỏ các container, chạy:

```bash
docker-compose down