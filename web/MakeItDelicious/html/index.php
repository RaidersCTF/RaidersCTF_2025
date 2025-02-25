<?php
$cookie_name = "_sessionID_";

$cookie_value = isset($_COOKIE[$cookie_name]) ? $_COOKIE[$cookie_name] : null;

$expiry_time = time() + 3600;

if (!$cookie_value) {
    $cookie_value = base64_encode("Alexander Ivanov");
    setcookie($cookie_name, $cookie_value, $expiry_time, "/");
}
?>
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="./css/style.css">
  <title>yummy</title>
</head>
<body>
  <div>
    <table>
      <tr>
        <th>材料</th>
        <th>分量</th>
      </tr>
      <tr>
        <td>薄力粉</td>
        <td>150mg</td>
      </tr>
      <tr>
        <td>卵黄</td>
        <td>1個</td>
      </tr>
      <tr>
        <td>無塩バター</td>
        <td>50mg</td>
      </tr>
      <tr>
        <td>砂糖</td>
        <td>20mg</td>
      </tr>
    </table>
    <?php
      $decode = base64_decode($cookie_value);
      if ($decode === "admin") {
        echo $flag = "RaidersCTF{XXX}";
      }
    ?>
  </div>
</body>
</html>
