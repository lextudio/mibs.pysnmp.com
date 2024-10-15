# SNMP MIB module (AVICI-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVICI-PROCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:44 2024
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

(aviciMibs,) = mibBuilder.importSymbols(
    "AVICI-SMI",
    "aviciMibs")

(aviciSysInventoryId,) = mibBuilder.importSymbols(
    "AVICI-SYSTEM-MIB",
    "aviciSysInventoryId")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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


# MODULE-IDENTITY

aviciProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7)
)
aviciProcessMIB.setRevisions(
        ("1970-01-01 00:00",
         "0009-07-12 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviciProcessObjects_ObjectIdentity = ObjectIdentity
aviciProcessObjects = _AviciProcessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 1)
)
_AviciCPUTotalTable_Object = MibTable
aviciCPUTotalTable = _AviciCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    aviciCPUTotalTable.setStatus("current")
_AviciCPUTotalEntry_Object = MibTableRow
aviciCPUTotalEntry = _AviciCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1)
)
aviciCPUTotalEntry.setIndexNames(
    (0, "AVICI-SYSTEM-MIB", "aviciSysInventoryId"),
)
if mibBuilder.loadTexts:
    aviciCPUTotalEntry.setStatus("current")


class _AviciCPUTotal5sec_Type(Gauge32):
    """Custom type aviciCPUTotal5sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AviciCPUTotal5sec_Type.__name__ = "Gauge32"
_AviciCPUTotal5sec_Object = MibTableColumn
aviciCPUTotal5sec = _AviciCPUTotal5sec_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1, 1),
    _AviciCPUTotal5sec_Type()
)
aviciCPUTotal5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciCPUTotal5sec.setStatus("current")


class _AviciCPUTotal1min_Type(Gauge32):
    """Custom type aviciCPUTotal1min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AviciCPUTotal1min_Type.__name__ = "Gauge32"
_AviciCPUTotal1min_Object = MibTableColumn
aviciCPUTotal1min = _AviciCPUTotal1min_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1, 2),
    _AviciCPUTotal1min_Type()
)
aviciCPUTotal1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciCPUTotal1min.setStatus("current")


class _AviciCPUTotal5min_Type(Gauge32):
    """Custom type aviciCPUTotal5min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AviciCPUTotal5min_Type.__name__ = "Gauge32"
_AviciCPUTotal5min_Object = MibTableColumn
aviciCPUTotal5min = _AviciCPUTotal5min_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 1, 1, 1, 3),
    _AviciCPUTotal5min_Type()
)
aviciCPUTotal5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciCPUTotal5min.setStatus("current")
_AviciProcessMIBConformance_ObjectIdentity = ObjectIdentity
aviciProcessMIBConformance = _AviciProcessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 2)
)
_AviciProcessMIBCompliances_ObjectIdentity = ObjectIdentity
aviciProcessMIBCompliances = _AviciProcessMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 1)
)
_AviciProcessMIBGroups_ObjectIdentity = ObjectIdentity
aviciProcessMIBGroups = _AviciProcessMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 2)
)

# Managed Objects groups

aviciProcessCPUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 2, 1)
)
aviciProcessCPUGroup.setObjects(
      *(("AVICI-PROCESS-MIB", "aviciCPUTotal5sec"),
        ("AVICI-PROCESS-MIB", "aviciCPUTotal1min"),
        ("AVICI-PROCESS-MIB", "aviciCPUTotal5min"))
)
if mibBuilder.loadTexts:
    aviciProcessCPUGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviciProcessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2474, 1, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aviciProcessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVICI-PROCESS-MIB",
    **{"aviciProcessMIB": aviciProcessMIB,
       "aviciProcessObjects": aviciProcessObjects,
       "aviciCPUTotalTable": aviciCPUTotalTable,
       "aviciCPUTotalEntry": aviciCPUTotalEntry,
       "aviciCPUTotal5sec": aviciCPUTotal5sec,
       "aviciCPUTotal1min": aviciCPUTotal1min,
       "aviciCPUTotal5min": aviciCPUTotal5min,
       "aviciProcessMIBConformance": aviciProcessMIBConformance,
       "aviciProcessMIBCompliances": aviciProcessMIBCompliances,
       "aviciProcessMIBCompliance": aviciProcessMIBCompliance,
       "aviciProcessMIBGroups": aviciProcessMIBGroups,
       "aviciProcessCPUGroup": aviciProcessCPUGroup}
)
