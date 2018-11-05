using RepositorioClases;
using Servicios;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace Comunidad.Controllers
{
    public class UsersController : ApiController
    {
        public IHttpActionResult Get(int id)
        {
            var user = UserService.Get(id).Select(u => new User()
            {
                Email = u.Email,
                Id = u.Id,
                Name = u.Name,
                Password = u.Password,
                IdRol = u.IdRol
            }).FirstOrDefault();

            return Ok(user);
        }

        [HttpPost]
        public IHttpActionResult Post(User user)
        {
            UserService.Create(new RepositorioClases.User()
            {
                Email = user.Email,
                Name = user.Name,
                Password = user.Password,
                IdRol = user.IdRol
            });

            return Ok();
        }
    }
}
