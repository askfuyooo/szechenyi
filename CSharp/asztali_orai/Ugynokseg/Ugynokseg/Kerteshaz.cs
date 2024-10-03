using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ugynokseg
{
    class Kerteshaz : Telek
    {
        private int lakoterulet;

        public int Lakoterulet
        {
            get
            {
                return this.lakoterulet;
            }
            set
            {
                if (!(value > 10 && value < Telekmeret * 0.8))
                {
                    throw new Exception("A lakóterület nem lehet kisebb, mint 10m2, és nem lehet nagyobb, ");
                }

                this.lakoterulet = value;
            }
        }

        public Kerteshaz(string tipus, string cim, int telekmeret, int lakoterulet, int negyzetAr):
            base(cim, telekmeret, (lakoterulet < telekmeret * 0.8 ? true : false), negyzetAr)
        {
            Lakoterulet = lakoterulet;
            this.tipus = tipus;
        }

        public override string ToString()
        {
            return base.ToString() + $" lakóterület: {this.lakoterulet}m2.";
        }
    }
}
