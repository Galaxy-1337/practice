import subprocess


def list_vms():
    """Выводит список доступных виртуальных машин."""
    try:
        result = subprocess.run(['VBoxManage', 'list', 'vms'], capture_output=True, text=True, check=True)
        print("Список виртуальных машин:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {e}")


def start_vm(DBA1):
    """Запускает виртуальную машину."""
    try:
        result = subprocess.run(['VBoxManage', 'startvm', DBA1], capture_output=True, text=True, check=True)
        print(f"Виртуальная машина '{DBA1}' запущена.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске виртуальной машины: {e}")


def stop_vm(DBA1):
    """Останавливает виртуальную машину."""
    try:
        result = subprocess.run(['VBoxManage', 'controlvm', DBA1, 'acpipowerbutton'], capture_output=True, text=True, check=True)
        print(f"Виртуальная машина '{DBA1}' остановлена.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при остановке виртуальной машины: {e}")


def reset_vm(DBA1):
    """Перезагружает виртуальную машину."""
    try:
        result = subprocess.run(['VBoxManage', 'controlvm', DBA1, 'reset'], capture_output=True, text=True, check=True)
        print(f"Виртуальная машина '{DBA1}' перезагружена.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при перезагрузке виртуальной машины: {e}")


def list_running_vms():
    """Выводит список запущенных виртуальных машин."""
    try:
        result = subprocess.run(['VBoxManage', 'list', 'runningvms'], capture_output=True, text=True, check=True)
        print("Список запущенных виртуальных машин:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {e}")

if __name__ == '__main__':

    list_vms()

    vm_name = 'DBA1-16-20240621'

    start_vm(vm_name)
    list_running_vms()

    import time
    time.sleep(10)

    reset_vm(vm_name)
    time.sleep(10) 
    stop_vm(vm_name)
