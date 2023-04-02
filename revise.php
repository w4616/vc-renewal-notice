<?php

// 假设您的数据库连接信息如下：
$servername = "localhost";
$username = "111";
$password = "111";
$dbname = "111";

// 获取传递的参数
$id = $_GET["id"];
$date = $_GET["date"];

// 创建连接
$conn = mysqli_connect($servername, $username, $password, $dbname);

// 检查连接是否成功
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// 查询数据库中是否有对应的 id
$sql = "SELECT * FROM data WHERE id = $id";
$result = mysqli_query($conn, $sql);

// 如果有对应的 id，更新 date
if (mysqli_num_rows($result) > 0) {
    $sql = "UPDATE data SET date = '$date' WHERE id = $id";
    mysqli_query($conn, $sql);
    
    // 查询修改后的 date 并返回
    $sql = "SELECT date FROM data WHERE id = $id";
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_assoc($result);
    echo "修改成功到期时间" . $row["date"];
} 
// 如果没有对应的 id，创建新的记录
else {
    $sql = "INSERT INTO data (id, date) VALUES ($id, '$date')";
    mysqli_query($conn, $sql);
    
    // 查询创建的 date 并返回
    $sql = "SELECT date FROM data WHERE id = $id";
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_assoc($result);
    echo "创建成功到期时间" . $row["date"];
}

// 关闭连接
mysqli_close($conn);

?>