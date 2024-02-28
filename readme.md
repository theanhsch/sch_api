## API list

### Lấy danh sách Users

- **Endpoint:** `/users`
- **Phương thức:** GET
- **Sử dụng:** Truy cập [http://localhost:2222/users](http://localhost:2222/users) bằng `trình duyệt` hoặc `Postman`

### Thêm

- **Endpoint:** `/users`
- **Phương thức:** POST
- **Mô tả:** Thêm 1 user
- **Sử dụng:** Dùng `Postman` để thực hiện yêu cầu POST tới [http://localhost:2222/users](http://localhost:2222/users) với `JSON`:

    ```json
    {
      "name": "Nguyen The Anh"
    }
    ```


### Xóa 1 User

- **End point:** `/users/{user_id}`
- **Phương thức:** DELETE
- **Mô tả:** Xóa user theo ID.
- **Sử dụng:**  Sử dụng `Postman` để thực hiện yêu cầu DELETE tới [http://localhost:2222/users/{user_id}](http://localhost:2222/users/{user_id}). Thay thế `{user_id}` bằng ID của người dùng bạn muốn xóa.
- **Ví dụ :**  http://localhost:2222/users/1
