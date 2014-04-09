using System;
using System.Data.Entity;
using System.Data.Entity.Infrastructure;
using System.Threading;
using System.Web.Mvc;
using WebMatrix.WebData;
using Comunidad.Models;

namespace Comunidad.Filters
{
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = false, Inherited = true)]
    public sealed class InitializeSimpleMembershipAttribute : ActionFilterAttribute
    {
        private static SimpleMembershipInitializer _initializer;
        private static object _initializerLock = new object();
        private static bool _isInitialized;

        public override void OnActionExecuting(ActionExecutingContext filterContext)
        {
            // Asegúrese de que ASP.NET Simple Membership se inicialice solo una vez por inicio de la aplicación
            LazyInitializer.EnsureInitialized(ref _initializer, ref _isInitialized, ref _initializerLock);
        }

        private class SimpleMembershipInitializer
        {
            public SimpleMembershipInitializer()
            {
                Database.SetInitializer<UsersContext>(null);

                try
                {
                    using (var context = new UsersContext())
                    {
                        if (!context.Database.Exists())
                        {
                            // Crear la base de datos SimpleMembership sin el esquema de migración de Entity Framework
                            ((IObjectContextAdapter)context).ObjectContext.CreateDatabase();
                        }
                    }

                    WebSecurity.InitializeDatabaseConnection("DefaultConnection", "UserProfile", "UserId", "UserName", autoCreateTables: true);
                }
                catch (Exception ex)
                {
                    throw new InvalidOperationException("No se pudo inicializar la base de datos de ASP.NET Simple Membership. Para obtener más información, consulte http://go.microsoft.com/fwlink/?LinkId=256588", ex);
                }
            }
        }
    }
}
