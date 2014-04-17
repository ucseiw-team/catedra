using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace RepositorioClases
{
    public class User
    {
        public int Id { get; set; }

        public string Name { get; set; }

        public string Email { get; set; }

        public string Password { get; set; }

        public DateTime DeletedDate { get; set; }

        public int IdRol { get; set; }
    }
}
