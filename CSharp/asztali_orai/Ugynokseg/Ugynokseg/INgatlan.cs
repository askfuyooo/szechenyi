using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ugynokseg
{
    class INgatlan
    {
        private int iranyar, telekmeret;
        private string cim;
        protected string tipus;

        //jellemző ami kivételt dob akkor, ha az ár kisebb mint 1M 
        public int Iranyar
        {
            get //olvasáskor fut le, visszaad értéket
            {
                return this.iranyar;
            }
            set //íráskor fut le, VALUE paraméterben lesz az átadandó érték
            {
                if (value <= 1000000)
                {
                    throw new Exception("Sajnos 1M Ft alatt nincs semmi :-(");
                }
                else
                {
                    this.iranyar = value;
                }
            }
        }

        public int Telekmeret
        {
            get
            {
                return this.telekmeret;
            }
            set
            {
                if (value < 10)
                {
                    throw new Exception("A telekméret legalább 10m2 kell legyen!");
                }
                else
                {
                    this.telekmeret = value;
                }
            }
        }

        public INgatlan(int iranyar, int telekmeret, string cim)
        {
            Iranyar = iranyar;
            Telekmeret = telekmeret;
            this.cim = cim;
        }

        public INgatlan(int telekmeret, string cim)
        {
            Telekmeret = telekmeret;
            this.cim = cim;
            this.iranyar = 1000000;
        }

        public override string ToString()
        {
            return $"{this.cim}-i, {this.telekmeret} m2-es {this.tipus} eladó {this.iranyar} Ft-ért";
        }
    }
}
