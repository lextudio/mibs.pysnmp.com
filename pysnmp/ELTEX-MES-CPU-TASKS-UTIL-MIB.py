# SNMP MIB module (ELTEX-MES-CPU-TASKS-UTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-CPU-TASKS-UTIL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:34 2024
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

(eltMesCpuTasksUtilMIB,) = mibBuilder.importSymbols(
    "ELTEX-MES-MNG-MIB",
    "eltMesCpuTasksUtilMIB")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesCpuTasksUtilObjects_ObjectIdentity = ObjectIdentity
eltMesCpuTasksUtilObjects = _EltMesCpuTasksUtilObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1)
)
_EltMesCpuTasksUtilConfig_ObjectIdentity = ObjectIdentity
eltMesCpuTasksUtilConfig = _EltMesCpuTasksUtilConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 1)
)


class _EltCpuTasksUtilEnable_Type(TruthValue):
    """Custom type eltCpuTasksUtilEnable based on TruthValue"""


_EltCpuTasksUtilEnable_Object = MibScalar
eltCpuTasksUtilEnable = _EltCpuTasksUtilEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 1, 1),
    _EltCpuTasksUtilEnable_Type()
)
eltCpuTasksUtilEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCpuTasksUtilEnable.setStatus("current")
_EltMesCpuTasksUtilStatistics_ObjectIdentity = ObjectIdentity
eltMesCpuTasksUtilStatistics = _EltMesCpuTasksUtilStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2)
)
_EltCpuTasksUtilStatisticsTable_Object = MibTable
eltCpuTasksUtilStatisticsTable = _EltCpuTasksUtilStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltCpuTasksUtilStatisticsTable.setStatus("current")
_EltCpuTasksUtilStatisticsEntry_Object = MibTableRow
eltCpuTasksUtilStatisticsEntry = _EltCpuTasksUtilStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1)
)
eltCpuTasksUtilStatisticsEntry.setIndexNames(
    (0, "ELTEX-MES-CPU-TASKS-UTIL-MIB", "eltCpuTasksUtilStatisticsTaskIndex"),
)
if mibBuilder.loadTexts:
    eltCpuTasksUtilStatisticsEntry.setStatus("current")
_EltCpuTasksUtilStatisticsTaskIndex_Type = Integer32
_EltCpuTasksUtilStatisticsTaskIndex_Object = MibTableColumn
eltCpuTasksUtilStatisticsTaskIndex = _EltCpuTasksUtilStatisticsTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 1),
    _EltCpuTasksUtilStatisticsTaskIndex_Type()
)
eltCpuTasksUtilStatisticsTaskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuTasksUtilStatisticsTaskIndex.setStatus("current")
_EltCpuTasksUtilStatisticsTaskName_Type = DisplayString
_EltCpuTasksUtilStatisticsTaskName_Object = MibTableColumn
eltCpuTasksUtilStatisticsTaskName = _EltCpuTasksUtilStatisticsTaskName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 2),
    _EltCpuTasksUtilStatisticsTaskName_Type()
)
eltCpuTasksUtilStatisticsTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuTasksUtilStatisticsTaskName.setStatus("current")


class _EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Type(Integer32):
    """Custom type eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Type.__name__ = "Integer32"
_EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Object = MibTableColumn
eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds = _EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 3),
    _EltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds_Type()
)
eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds.setStatus("current")


class _EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Type(Integer32):
    """Custom type eltCpuTasksUtilStatisticsUtilizationDuringLastMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Type.__name__ = "Integer32"
_EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Object = MibTableColumn
eltCpuTasksUtilStatisticsUtilizationDuringLastMinute = _EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 4),
    _EltCpuTasksUtilStatisticsUtilizationDuringLastMinute_Type()
)
eltCpuTasksUtilStatisticsUtilizationDuringLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuTasksUtilStatisticsUtilizationDuringLastMinute.setStatus("current")


class _EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Type(Integer32):
    """Custom type eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Type.__name__ = "Integer32"
_EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Object = MibTableColumn
eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes = _EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 5),
    _EltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes_Type()
)
eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-CPU-TASKS-UTIL-MIB",
    **{"eltMesCpuTasksUtilObjects": eltMesCpuTasksUtilObjects,
       "eltMesCpuTasksUtilConfig": eltMesCpuTasksUtilConfig,
       "eltCpuTasksUtilEnable": eltCpuTasksUtilEnable,
       "eltMesCpuTasksUtilStatistics": eltMesCpuTasksUtilStatistics,
       "eltCpuTasksUtilStatisticsTable": eltCpuTasksUtilStatisticsTable,
       "eltCpuTasksUtilStatisticsEntry": eltCpuTasksUtilStatisticsEntry,
       "eltCpuTasksUtilStatisticsTaskIndex": eltCpuTasksUtilStatisticsTaskIndex,
       "eltCpuTasksUtilStatisticsTaskName": eltCpuTasksUtilStatisticsTaskName,
       "eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds": eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds,
       "eltCpuTasksUtilStatisticsUtilizationDuringLastMinute": eltCpuTasksUtilStatisticsUtilizationDuringLastMinute,
       "eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes": eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes}
)
