
namespace Ugynokseg
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnLoad = new System.Windows.Forms.Button();
            this.listBox1 = new System.Windows.Forms.ListBox();
            this.lblError = new System.Windows.Forms.Label();
            this.listBox2 = new System.Windows.Forms.ListBox();
            this.lblKerteshaz = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnLoad
            // 
            this.btnLoad.Location = new System.Drawing.Point(12, 12);
            this.btnLoad.Name = "btnLoad";
            this.btnLoad.Size = new System.Drawing.Size(776, 41);
            this.btnLoad.TabIndex = 0;
            this.btnLoad.Text = "Adatok betöltése";
            this.btnLoad.UseVisualStyleBackColor = true;
            this.btnLoad.Click += new System.EventHandler(this.btnLoad_Click);
            // 
            // listBox1
            // 
            this.listBox1.FormattingEnabled = true;
            this.listBox1.Location = new System.Drawing.Point(15, 72);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(219, 368);
            this.listBox1.TabIndex = 1;
            // 
            // lblError
            // 
            this.lblError.AutoSize = true;
            this.lblError.Location = new System.Drawing.Point(12, 56);
            this.lblError.Name = "lblError";
            this.lblError.Size = new System.Drawing.Size(111, 13);
            this.lblError.TabIndex = 2;
            this.lblError.Text = "Hibák az állományban";
            // 
            // listBox2
            // 
            this.listBox2.FormattingEnabled = true;
            this.listBox2.Location = new System.Drawing.Point(240, 72);
            this.listBox2.Name = "listBox2";
            this.listBox2.Size = new System.Drawing.Size(548, 368);
            this.listBox2.TabIndex = 3;
            // 
            // lblKerteshaz
            // 
            this.lblKerteshaz.AutoSize = true;
            this.lblKerteshaz.Location = new System.Drawing.Point(240, 56);
            this.lblKerteshaz.Name = "lblKerteshaz";
            this.lblKerteshaz.Size = new System.Drawing.Size(144, 13);
            this.lblKerteshaz.TabIndex = 4;
            this.lblKerteshaz.Text = "Kertesházak és telkek adatai";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.lblKerteshaz);
            this.Controls.Add(this.listBox2);
            this.Controls.Add(this.lblError);
            this.Controls.Add(this.listBox1);
            this.Controls.Add(this.btnLoad);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnLoad;
        private System.Windows.Forms.ListBox listBox1;
        private System.Windows.Forms.Label lblError;
        private System.Windows.Forms.ListBox listBox2;
        private System.Windows.Forms.Label lblKerteshaz;
    }
}

