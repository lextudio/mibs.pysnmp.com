# SNMP MIB module (TOS-SYSSTATE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TOS-SYSSTATE
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:40 2024
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
 Gauge,
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
 Opaque,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge",
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(tosMib,) = mibBuilder.importSymbols(
    "TOS-SMI",
    "tosMib")


# MODULE-IDENTITY

sysRunning = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4)
)
sysRunning.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SystemDeviceName_Type(DisplayString):
    """Custom type systemDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemDeviceName_Type.__name__ = "DisplayString"
_SystemDeviceName_Object = MibScalar
systemDeviceName = _SystemDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 1),
    _SystemDeviceName_Type()
)
systemDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDeviceName.setStatus("current")


class _SystemTime_Type(DisplayString):
    """Custom type systemTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemTime_Type.__name__ = "DisplayString"
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 2),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_SystemUpTime_Type = TimeTicks
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 3),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("current")
_AdminOnline_Type = Integer32
_AdminOnline_Object = MibScalar
adminOnline = _AdminOnline_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 4),
    _AdminOnline_Type()
)
adminOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminOnline.setStatus("current")
_CpuLoad_Type = Integer32
_CpuLoad_Object = MibScalar
cpuLoad = _CpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 5),
    _CpuLoad_Type()
)
cpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad.setStatus("current")
_MemoryLoad_Type = Integer32
_MemoryLoad_Object = MibScalar
memoryLoad = _MemoryLoad_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 6),
    _MemoryLoad_Type()
)
memoryLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryLoad.setStatus("current")
_MemoryFree_Type = Integer32
_MemoryFree_Object = MibScalar
memoryFree = _MemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 7),
    _MemoryFree_Type()
)
memoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFree.setStatus("current")
_MemoryTotal_Type = Integer32
_MemoryTotal_Object = MibScalar
memoryTotal = _MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 8),
    _MemoryTotal_Type()
)
memoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotal.setStatus("current")
_CurrentConnections_Type = Integer32
_CurrentConnections_Object = MibScalar
currentConnections = _CurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 9),
    _CurrentConnections_Type()
)
currentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentConnections.setStatus("current")
_Cps_Type = Integer32
_Cps_Object = MibScalar
cps = _Cps_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 4, 10),
    _Cps_Type()
)
cps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOS-SYSSTATE",
    **{"sysRunning": sysRunning,
       "systemDeviceName": systemDeviceName,
       "systemTime": systemTime,
       "systemUpTime": systemUpTime,
       "adminOnline": adminOnline,
       "cpuLoad": cpuLoad,
       "memoryLoad": memoryLoad,
       "memoryFree": memoryFree,
       "memoryTotal": memoryTotal,
       "currentConnections": currentConnections,
       "cps": cps}
)
