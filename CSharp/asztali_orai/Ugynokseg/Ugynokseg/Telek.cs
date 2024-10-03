using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ugynokseg
{
    class Telek : INgatlan
    {
        public bool beepitheto_e { private get; set; }

        public Telek(string cim, int telekmeret, bool beepitheto_e, int negyzetAr):
            base(telekmeret * negyzetAr, telekmeret, cim)
        {
            this.beepitheto_e = beepitheto_e;
        }

        public override string ToString()
        {
            return base.ToString() + $"{(this.beepitheto_e ? "" : " nem")} beépíthető";
        }
    }
}
