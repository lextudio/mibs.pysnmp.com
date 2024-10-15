# SNMP MIB module (MIBMANREMOTE-SUNMANAGEMENTCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIBMANREMOTE-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:34 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Sunsymon_ObjectIdentity = ObjectIdentity
sunsymon = _Sunsymon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2)
)
_Base_ObjectIdentity = ObjectIdentity
base = _Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1)
)
_Mibman_ObjectIdentity = ObjectIdentity
mibman = _Mibman_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1)
)
_Finder_ObjectIdentity = ObjectIdentity
finder = _Finder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 1)
)
_Loader_ObjectIdentity = ObjectIdentity
loader = _Loader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 2)
)
_BrowserRoot_ObjectIdentity = ObjectIdentity
browserRoot = _BrowserRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 3)
)
_Checker_ObjectIdentity = ObjectIdentity
checker = _Checker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 4)
)
_ModuleRegistry_ObjectIdentity = ObjectIdentity
moduleRegistry = _ModuleRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 5)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 6)
)
_RemoteSystem_ObjectIdentity = ObjectIdentity
remoteSystem = _RemoteSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 6, 4)
)
_Schedule_ObjectIdentity = ObjectIdentity
schedule = _Schedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7)
)
_ScheduleTable_ObjectIdentity = ObjectIdentity
scheduleTable = _ScheduleTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 1)
)
_ScheduleEntry_ObjectIdentity = ObjectIdentity
scheduleEntry = _ScheduleEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 1, 1)
)
_Rowstatus_ObjectIdentity = ObjectIdentity
rowstatus = _Rowstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 1, 1, 1)
)
_Modspec_ObjectIdentity = ObjectIdentity
modspec = _Modspec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 1, 1, 2)
)
_Enabletimewindow_ObjectIdentity = ObjectIdentity
enabletimewindow = _Enabletimewindow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 1, 1, 3)
)
_Enablestate_ObjectIdentity = ObjectIdentity
enablestate = _Enablestate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 1, 1, 4)
)
_Loadtimewindow_ObjectIdentity = ObjectIdentity
loadtimewindow = _Loadtimewindow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 1, 1, 5)
)
_Loadstate_ObjectIdentity = ObjectIdentity
loadstate = _Loadstate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 1, 1, 6)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 1, 1, 7)
)
_ScheduleRequest_ObjectIdentity = ObjectIdentity
scheduleRequest = _ScheduleRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 1, 7, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIBMANREMOTE-SUNMANAGEMENTCENTER-MIB",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "base": base,
       "mibman": mibman,
       "finder": finder,
       "loader": loader,
       "browserRoot": browserRoot,
       "checker": checker,
       "moduleRegistry": moduleRegistry,
       "modules": modules,
       "remoteSystem": remoteSystem,
       "schedule": schedule,
       "scheduleTable": scheduleTable,
       "scheduleEntry": scheduleEntry,
       "rowstatus": rowstatus,
       "modspec": modspec,
       "enabletimewindow": enabletimewindow,
       "enablestate": enablestate,
       "loadtimewindow": loadtimewindow,
       "loadstate": loadstate,
       "info": info,
       "scheduleRequest": scheduleRequest}
)
