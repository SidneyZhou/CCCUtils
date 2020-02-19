import os
import json
import zipfile
import qiniu

# 根目录
rootPath = os.path.dirname(__file__)

# print(rootPath)

# 打包配置文件, 参见 packages\res_packer\main.js 中的 "子包配置文件" 说明
cfgPath = rootPath + '/res_packer_cfg.json'
f = open(cfgPath, 'r')
cfgs = json.load(f)
# print(cfgs)

# 七牛key配置文件
'''
/res_upload_qiniu_key.json
{
    "ak": "app_key",
    "sk": "secret_key",
    "bucket": "bucket_name"
}
'''
qnKeys = json.load(open(rootPath + '/res_upload_qiniu_key.json'))
print(qnKeys)

q = qiniu.Auth(qnKeys['ak'], qnKeys['sk'])

# 微信工程目录
wechatgameRoot = rootPath + '/build/wechatgame/'

def createZip(folder):
    '''创建zip'''
    # 生成zip
    zipPath = wechatgameRoot + '../' + folder + '.zip'
    '''
    w模式为覆盖, r为只读, x为仅新建并写入新的文件(若文件已存在会抛出FileExistsError), a为添加文件
    不使用ZIP_LZMA等压缩制式是为了提高兼容性
    '''
    zFile = zipfile.ZipFile(zipPath, 'w', zipfile.ZIP_DEFLATED)
    
    fileDict = {}
    dirPath = wechatgameRoot + folder
    # 读取微信文件夹下的目录文件
    for root, dirnames, filenames in os.walk(dirPath):
        # print(root, dirnames, filenames)
        filePrefix = root.replace(dirPath, 'res').replace('\\', '-') # 根据creator的wx-download修改文件名和路径
        for filename in filenames:
            newFileName = filePrefix + '-' + filename
            zFile.write(os.path.join(root, filename), newFileName)
            fileDict[newFileName] = 1
    # 写入文件列表
    zFile.writestr(folder + '.json', json.dumps(fileDict))
    zFile.close()
    print('created zip ' + folder)
    token = q.upload_token(qnKeys['bucket'], folder + '.zip')
    qiniu.put_file(token, folder + '.zip', zipPath)

for cfg in cfgs:
    # print(cfg)
    if not cfg.get('isStartScene'): # 用get避免KeyError错误
        createZip(cfg['targetDir'])

