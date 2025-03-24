# Dự án kiểm thử hệ thống đăng nhập

Em làm dự án này để kiểm thử hệ thống đăng nhập, gồm 2 phần chính:  
- **API**: Test API `https://reqres.in/api/login` bằng Postman.  
- **Giao diện**: Test giao diện trên web `https://the-internet.herokuapp.com/login` bằng Selenium.  

## Nội dung dự án
- **Kiểm thử API**:  
  - Test 10 trường hợp (đăng nhập đúng, email/mật khẩu trống, email sai, v.v.).  
  - Kết quả: 18/18 test Pass (có chỉnh kỳ vọng vài chỗ).  
  - File: `LoginAPI_TestCases.xlsx` (Test Case), `Login_API_Testing.json` (Collection Postman).  

- **Kiểm thử giao diện**:  
  - Test 2 trường hợp: đăng nhập đúng và sai.  
  - Kết quả: Đều Pass, giao diện chạy ổn.  
  - File: `login_test.py`,login_fail.py (script Selenium).  

## Hướng dẫn chạy
- **API**: Import file `Login_API_Testing.json` vào Postman, chạy Collection `Login API Testing`.  
- **Giao diện**: Mở file `login_test.py`, chạy bằng Python (cần cài Selenium và `webdriver-manager`).  

## Liên hệ
Nếu anh/chị cần thêm thông tin, cứ liên hệ em nhé: [duongtrung110103@gmail.com].  
