# SNMP MIB module (TPLINK-SYSMONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SYSMONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:46 2024
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkSysMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkSysMonitorMIBObjects_ObjectIdentity = ObjectIdentity
tplinkSysMonitorMIBObjects = _TplinkSysMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1)
)
_TpSysMonitorCpu_ObjectIdentity = ObjectIdentity
tpSysMonitorCpu = _TpSysMonitorCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 1)
)
_TpSysMonitorCpuTable_Object = MibTable
tpSysMonitorCpuTable = _TpSysMonitorCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpSysMonitorCpuTable.setStatus("current")
_TpSysMonitorCpuEntry_Object = MibTableRow
tpSysMonitorCpuEntry = _TpSysMonitorCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 1, 1, 1)
)
tpSysMonitorCpuEntry.setIndexNames(
    (0, "TPLINK-SYSMONITOR-MIB", "tpSysMonitorCpuUnitNumber"),
)
if mibBuilder.loadTexts:
    tpSysMonitorCpuEntry.setStatus("current")
_TpSysMonitorCpuUnitNumber_Type = Integer32
_TpSysMonitorCpuUnitNumber_Object = MibTableColumn
tpSysMonitorCpuUnitNumber = _TpSysMonitorCpuUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 1, 1, 1, 1),
    _TpSysMonitorCpuUnitNumber_Type()
)
tpSysMonitorCpuUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSysMonitorCpuUnitNumber.setStatus("current")


class _TpSysMonitorCpu5Seconds_Type(Integer32):
    """Custom type tpSysMonitorCpu5Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TpSysMonitorCpu5Seconds_Type.__name__ = "Integer32"
_TpSysMonitorCpu5Seconds_Object = MibTableColumn
tpSysMonitorCpu5Seconds = _TpSysMonitorCpu5Seconds_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 1, 1, 1, 2),
    _TpSysMonitorCpu5Seconds_Type()
)
tpSysMonitorCpu5Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSysMonitorCpu5Seconds.setStatus("current")


class _TpSysMonitorCpu1Minute_Type(Integer32):
    """Custom type tpSysMonitorCpu1Minute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TpSysMonitorCpu1Minute_Type.__name__ = "Integer32"
_TpSysMonitorCpu1Minute_Object = MibTableColumn
tpSysMonitorCpu1Minute = _TpSysMonitorCpu1Minute_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 1, 1, 1, 3),
    _TpSysMonitorCpu1Minute_Type()
)
tpSysMonitorCpu1Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSysMonitorCpu1Minute.setStatus("current")


class _TpSysMonitorCpu5Minutes_Type(Integer32):
    """Custom type tpSysMonitorCpu5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TpSysMonitorCpu5Minutes_Type.__name__ = "Integer32"
_TpSysMonitorCpu5Minutes_Object = MibTableColumn
tpSysMonitorCpu5Minutes = _TpSysMonitorCpu5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 1, 1, 1, 4),
    _TpSysMonitorCpu5Minutes_Type()
)
tpSysMonitorCpu5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSysMonitorCpu5Minutes.setStatus("current")
_TpSysMonitorMemory_ObjectIdentity = ObjectIdentity
tpSysMonitorMemory = _TpSysMonitorMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 2)
)
_TpSysMonitorMemoryTable_Object = MibTable
tpSysMonitorMemoryTable = _TpSysMonitorMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpSysMonitorMemoryTable.setStatus("current")
_TpSysMonitorMemoryEntry_Object = MibTableRow
tpSysMonitorMemoryEntry = _TpSysMonitorMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 2, 1, 1)
)
tpSysMonitorMemoryEntry.setIndexNames(
    (0, "TPLINK-SYSMONITOR-MIB", "tpSysMonitorMemoryUnitNumber"),
)
if mibBuilder.loadTexts:
    tpSysMonitorMemoryEntry.setStatus("current")
_TpSysMonitorMemoryUnitNumber_Type = Integer32
_TpSysMonitorMemoryUnitNumber_Object = MibTableColumn
tpSysMonitorMemoryUnitNumber = _TpSysMonitorMemoryUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 2, 1, 1, 1),
    _TpSysMonitorMemoryUnitNumber_Type()
)
tpSysMonitorMemoryUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSysMonitorMemoryUnitNumber.setStatus("current")


class _TpSysMonitorMemoryUtilization_Type(Integer32):
    """Custom type tpSysMonitorMemoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TpSysMonitorMemoryUtilization_Type.__name__ = "Integer32"
_TpSysMonitorMemoryUtilization_Object = MibTableColumn
tpSysMonitorMemoryUtilization = _TpSysMonitorMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 1, 2, 1, 1, 2),
    _TpSysMonitorMemoryUtilization_Type()
)
tpSysMonitorMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSysMonitorMemoryUtilization.setStatus("current")
_TplinkSysMonitorNotifications_ObjectIdentity = ObjectIdentity
tplinkSysMonitorNotifications = _TplinkSysMonitorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 2)
)

# Managed Objects groups


# Notification objects

tpSysMonitorCpuOverLoading = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tpSysMonitorCpuOverLoading.setStatus(
        "current"
    )

tpSysMonitorMemoryOverLoading = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 4, 2, 2)
)
if mibBuilder.loadTexts:
    tpSysMonitorMemoryOverLoading.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SYSMONITOR-MIB",
    **{"tplinkSysMonitorMIB": tplinkSysMonitorMIB,
       "tplinkSysMonitorMIBObjects": tplinkSysMonitorMIBObjects,
       "tpSysMonitorCpu": tpSysMonitorCpu,
       "tpSysMonitorCpuTable": tpSysMonitorCpuTable,
       "tpSysMonitorCpuEntry": tpSysMonitorCpuEntry,
       "tpSysMonitorCpuUnitNumber": tpSysMonitorCpuUnitNumber,
       "tpSysMonitorCpu5Seconds": tpSysMonitorCpu5Seconds,
       "tpSysMonitorCpu1Minute": tpSysMonitorCpu1Minute,
       "tpSysMonitorCpu5Minutes": tpSysMonitorCpu5Minutes,
       "tpSysMonitorMemory": tpSysMonitorMemory,
       "tpSysMonitorMemoryTable": tpSysMonitorMemoryTable,
       "tpSysMonitorMemoryEntry": tpSysMonitorMemoryEntry,
       "tpSysMonitorMemoryUnitNumber": tpSysMonitorMemoryUnitNumber,
       "tpSysMonitorMemoryUtilization": tpSysMonitorMemoryUtilization,
       "tplinkSysMonitorNotifications": tplinkSysMonitorNotifications,
       "tpSysMonitorCpuOverLoading": tpSysMonitorCpuOverLoading,
       "tpSysMonitorMemoryOverLoading": tpSysMonitorMemoryOverLoading}
)
