import sys
from os import path, system

def actualizar_repo(url_repo, path_repo):
    print '-' * 80
    print 'Actualizando repositorio'
    print 'Url:', url_repo
    print 'Path:', path_repo

    if path.exists(path_repo):
        comando = '(cd %s && hg pull -u)' % path_repo
    else:
        comando = 'hg clone %s %s' % (url_repo, path_repo)
    system(comando)

if __name__ == '__main__':
    raiz = sys.argv[1]
    for grupo in sys.argv[2:]:
        url_repo_code = 'https://bitbucket.org/ucsedar/%s' % grupo
        url_repo_wiki = url_repo_code + '/wiki'

        path_repo_code = path.join(raiz, grupo)
        path_repo_wiki = path_repo_code + '_wiki'

        actualizar_repo(url_repo_code, path_repo_code)
        actualizar_repo(url_repo_wiki, path_repo_wiki)



