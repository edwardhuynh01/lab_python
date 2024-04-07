def tinh_tong_chuoi(chuoi):
    so_duong = 0
    so_am = 0

    so = ''
    for ky_tu in chuoi:
        if ky_tu.isdigit() or (ky_tu == '-' and so == ''):  
            so += ky_tu
        elif so != '':
            if int(so) > 0:
                so_duong += int(so)
            else:
                so_am += int(so)
            so = ''

  
    if so != '':
        if int(so) > 0:
            so_duong += int(so)
        else:
            so_am += int(so)

    return so_duong, so_am


chuoi = "-100#^sdfkj8902w3ir021@swf-20"


tong_duong, tong_am = tinh_tong_chuoi(chuoi)

print("Giá trị dương:", tong_duong)
print("Giá trị âm:", tong_am)
