# jwt_auth_by_phone_number

**jwt_auth_by_phone_number** — это проект для реализации аутентификации и регистрации пользователей через номер телефона с использованием JWT (JSON Web Token). Проект позволяет пользователям зарегистрироваться и аутентифицироваться с помощью их номера телефона.

## 🌐 О проекте

Проект **jwt_auth_by_phone_number** реализует систему аутентификации, которая позволяет пользователям:
- Зарегистрироваться через номер телефона.
- Войти в систему, используя свой номер телефона.
- Получить JWT токен для аутентификации в приложении.

### Основные функции:
- **Регистрация через номер телефона**: Пользователи могут зарегистрироваться, указав свой номер телефона, на который будет отправлен OTP (одноразовый пароль).
- **Аутентификация через номер телефона**: После регистрации пользователь может войти в систему, используя номер телефона и OTP.
- **JWT токены**: После успешной аутентификации пользователь получает JWT токен для дальнейшего использования в запросах.
