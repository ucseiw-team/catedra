using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Datos;
using RepositorioClases;

namespace Servicios
{
    public static class UserService
    {
        public static void Create(User user)
        {
            using (Entities context = new Entities())
            {
                context.Users.Add(new Users()
                {
                    Email = user.Email,
                    Name = user.Name,
                    Password = user.Password
                });

                context.SaveChanges();
            }
        }

        public static List<User> Get(int? id)
        {
            using (Entities context = new Entities())
            {
                // la propiedad HasValue de los objetos que son Nullables o permiten tomar valores nulos, equivale a hacer la pregunta if (valor != null)
                // la expresión id.HasValue ? id.Value == u.Id : true
                // equivale a (id.HasValue && id.Value == u.Id) || (!id.HasValue)
                // lo que hacen es filtrar solo cuando viene un valor en la variable, ahorrándonos hacer un if antes y repetir la consulta.
                return context.Users.Where(u => !u.DeleteDate.HasValue && (id.HasValue ? id.Value == u.Id : true)).Select(u => new User()
                {
                    Email = u.Email,
                    Id = u.Id,
                    Name = u.Name,
                    Password = u.Password
                }).ToList();
            }
        }

        public static void Edit(User user)
        {
            using (Entities context = new Entities())
            {
                Users users = context.Users.Where(u => u.Id == user.Id).FirstOrDefault();

                // FirstOrDefault va a intentar recuperar el registro que cumpla la condición
                // si no encuentra ninguno, devuelve NULL, de ahí el siguiente IF.
                if (users != null)
                {                                        
                    users.Email = user.Email;
                    users.Name = user.Name;
                    users.Password = user.Password;
                }

                // el objeto en memoria persiste los cambios en la base de datos cuando hago un save sobre el contexto.
                context.SaveChanges();
            }
        }

        public static void Delete(User user)
        {
            using (Entities context = new Entities())
            {
                Users users = context.Users.Where(u => u.Id == user.Id).FirstOrDefault();

                // FirstOrDefault va a intentar recuperar el registro que cumpla la condición
                // si no encuentra ninguno, devuelve NULL, de ahí el siguiente IF.
                if (users != null)
                    users.DeleteDate = DateTime.Now;            

                // el objeto en memoria persiste los cambios en la base de datos cuando hago un save sobre el contexto.
                context.SaveChanges();
            }
        }
    }
}
