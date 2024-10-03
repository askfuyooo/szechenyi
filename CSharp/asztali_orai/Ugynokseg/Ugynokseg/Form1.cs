using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Ugynokseg
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            /*
            Kerteshaz hazacska = new Kerteshaz("Kerteshaz", "Bp.", 1000, 40, 500000);
            MessageBox.Show(hazacska.ToString());
            */
        }

        private void btnLoad_Click(object sender, EventArgs e)
        {
            OpenFileDialog ablak = new OpenFileDialog();
            ablak.Filter = "CSV (.csv)|*.csv|TXT (.txt)|*.txt";
            if (ablak.ShowDialog() == DialogResult.OK)
            {
                string fileLocation = ablak.FileName;
                var sorok = File.ReadAllLines(fileLocation).Skip(1);
                List<INgatlan> ingatlanok = new List<INgatlan>();

                int sor = 1;
                foreach (var item in sorok)
                {
                    try
                    {
                        string[] itemSplitted = item.Split(';');

                        string tipus = itemSplitted[0];
                        string cim = itemSplitted[1];
                        int telekmeret = int.Parse(itemSplitted[2]);
                        int negyzetAr = int.Parse(itemSplitted[3]);
                        bool beepitheto_e = itemSplitted[4] == "igen" ? true : false;
                        int lakoterulet = itemSplitted[5] != "-" ? int.Parse(itemSplitted[5]) : 0;

                        switch (itemSplitted[0])
                        {
                            case "telek":
                                ingatlanok.Add(new Telek(cim, telekmeret, beepitheto_e, negyzetAr));
                                break;

                            case "kerteshaz":
                                ingatlanok.Add(new Kerteshaz(tipus, cim, telekmeret, lakoterulet, negyzetAr));
                                break;
                        }

                        listBox2.Items.Add(ingatlanok.Last().ToString());
                    }
                    catch (Exception ex)
                    {
                        listBox1.Items.Add($"{sor}. sor: {ex.Message}");
                        //MessageBox.Show(ex.Message, "Hiba!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                    sor++;
                }
            }
        }
    }
}
