import os
import platform
import subprocess
import time
from datetime import datetime

# Host target untuk pengujian (Menggunakan DNS umum yang stabil)
TARGET_HOSTS = {
    "Gerbang Utama (Google DNS)": "8.8.8.8",
    "Cloudflare DNS (Alternatif)": "1.1.1.1"
}

def ping_host(host):
    """Melakukan ping ke host tertentu tergantung pada OS yang digunakan."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '2', host]
    
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        if output.returncode == 0:
            return "NORMAL (Tersambung)"
        else:
            return "BUG/RTO (Request Time Out - Putus)"
    except subprocess.TimeoutExpired:
        return "TIMEOUT (Koneksi Terlalu Lambat)"

def run_traceroute(host):
    """Melacak rute lompatan (hop) jaringan untuk melihat lokasi bug/bottleneck."""
    print(f"\n[+] Melacak Rute Lompatan Jaringan ke {host}...")
    command = ['tracert', host] if platform.system().lower() == 'windows' else ['traceroute', host]
    
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        for line in iter(process.stdout.readline, ''):
            print(f"   {line.strip()}")
            if "ms" in line and "*" in line:
                print("   [!] Terdeteksi ketidakstabilan (ping spike/loss) di jalur ini.")
        process.stdout.close()
        process.wait()
    except Exception as e:
        print(f"Gagal menjalankan traceroute: {e}")

def main():
    print("=" * 60)
    print(f" ANALISIS GANGGUAN JARKOM DATA  - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ")
    print("=" * 60)
    
    print(" Memeriksa Stabilitas Koneksi Dasar...")
    for name, host in TARGET_HOSTS.items():
        status = ping_host(host)
        print(f" -> {name} [{host}]: {status}")
        time.sleep(1)
        
    print("\n Analisis Rute Jaringan Mendalam...")
    run_traceroute("8.8.8.8")
    
    print("\n" + "=" * 60)
    print(" Analisis Selesai. Jika banyak RTO, periksa APN atau jangkauan sinyal Tri Anda.")
    print("=" * 60)

if __name__ == "__main__":
    main()
