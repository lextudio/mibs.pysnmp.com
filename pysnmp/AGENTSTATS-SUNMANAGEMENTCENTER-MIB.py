# SNMP MIB module (AGENTSTATS-SUNMANAGEMENTCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AGENTSTATS-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:55 2024
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
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2)
)
_AgentStats_ObjectIdentity = ObjectIdentity
agentStats = _AgentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30)
)
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 1)
)
_ToeCount_ObjectIdentity = ObjectIdentity
toeCount = _ToeCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 1, 1)
)
_BobCount_ObjectIdentity = ObjectIdentity
bobCount = _BobCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 1, 2)
)
_Commands_ObjectIdentity = ObjectIdentity
commands = _Commands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 2)
)
_Total1_ObjectIdentity = ObjectIdentity
total1 = _Total1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 2, 1)
)
_Rate1_ObjectIdentity = ObjectIdentity
rate1 = _Rate1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 2, 2)
)
_Transactions_ObjectIdentity = ObjectIdentity
transactions = _Transactions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 3)
)
_Total2_ObjectIdentity = ObjectIdentity
total2 = _Total2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 3, 1)
)
_Rate2_ObjectIdentity = ObjectIdentity
rate2 = _Rate2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 3, 2)
)
_Procstats_ObjectIdentity = ObjectIdentity
procstats = _Procstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4)
)
_Pid_ObjectIdentity = ObjectIdentity
pid = _Pid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 1)
)
_Id_ObjectIdentity = ObjectIdentity
id = _Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 2)
)
_Name_ObjectIdentity = ObjectIdentity
name = _Name_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 3)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 4)
)
_State_ObjectIdentity = ObjectIdentity
state = _State_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 5)
)
_Uid_ObjectIdentity = ObjectIdentity
uid = _Uid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 6)
)
_Size2_ObjectIdentity = ObjectIdentity
size2 = _Size2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 7)
)
_Rss2_ObjectIdentity = ObjectIdentity
rss2 = _Rss2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 8)
)
_Starttime_ObjectIdentity = ObjectIdentity
starttime = _Starttime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 9)
)
_Startdatestring_ObjectIdentity = ObjectIdentity
startdatestring = _Startdatestring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 10)
)
_Starttimestring_ObjectIdentity = ObjectIdentity
starttimestring = _Starttimestring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 11)
)
_Cputime_ObjectIdentity = ObjectIdentity
cputime = _Cputime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 12)
)
_Pctcputime_ObjectIdentity = ObjectIdentity
pctcputime = _Pctcputime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 13)
)
_Context_ObjectIdentity = ObjectIdentity
context = _Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 14)
)
_Syscalls_ObjectIdentity = ObjectIdentity
syscalls = _Syscalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 15)
)
_Command_ObjectIdentity = ObjectIdentity
command = _Command_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 4, 16)
)
_Totalstats_ObjectIdentity = ObjectIdentity
totalstats = _Totalstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 5)
)
_Count_ObjectIdentity = ObjectIdentity
count = _Count_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 5, 1)
)
_Size1_ObjectIdentity = ObjectIdentity
size1 = _Size1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 5, 2)
)
_Rss1_ObjectIdentity = ObjectIdentity
rss1 = _Rss1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30, 5, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGENTSTATS-SUNMANAGEMENTCENTER-MIB",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "base": base,
       "modules": modules,
       "agentStats": agentStats,
       "objects": objects,
       "toeCount": toeCount,
       "bobCount": bobCount,
       "commands": commands,
       "total1": total1,
       "rate1": rate1,
       "transactions": transactions,
       "total2": total2,
       "rate2": rate2,
       "procstats": procstats,
       "pid": pid,
       "id": id,
       "name": name,
       "info": info,
       "state": state,
       "uid": uid,
       "size2": size2,
       "rss2": rss2,
       "starttime": starttime,
       "startdatestring": startdatestring,
       "starttimestring": starttimestring,
       "cputime": cputime,
       "pctcputime": pctcputime,
       "context": context,
       "syscalls": syscalls,
       "command": command,
       "totalstats": totalstats,
       "count": count,
       "size1": size1,
       "rss1": rss1}
)
