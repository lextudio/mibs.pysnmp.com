# SNMP MIB module (BENU-HTTP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-HTTP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:55 2024
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

(benuWAG,) = mibBuilder.importSymbols(
    "BENU-WAG-MIB",
    "benuWAG")

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


# MODULE-IDENTITY

benuHttpServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10)
)
benuHttpServerMIB.setRevisions(
        ("2015-10-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BHttpServerObjects_ObjectIdentity = ObjectIdentity
bHttpServerObjects = _BHttpServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    bHttpServerObjects.setStatus("current")
_BHttpServerLatencyTable_Object = MibTable
bHttpServerLatencyTable = _BHttpServerLatencyTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    bHttpServerLatencyTable.setStatus("current")
_BHttpServerLatencyEntry_Object = MibTableRow
bHttpServerLatencyEntry = _BHttpServerLatencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1)
)
bHttpServerLatencyEntry.setIndexNames(
    (0, "BENU-HTTP-SERVER-MIB", "bHttpServLatencyStatsInterval"),
)
if mibBuilder.loadTexts:
    bHttpServerLatencyEntry.setStatus("current")
_BHttpServLatencyStatsInterval_Type = Integer32
_BHttpServLatencyStatsInterval_Object = MibTableColumn
bHttpServLatencyStatsInterval = _BHttpServLatencyStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 1),
    _BHttpServLatencyStatsInterval_Type()
)
bHttpServLatencyStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bHttpServLatencyStatsInterval.setStatus("current")
_BHttpServLatencyStatsIntervalDuration_Type = Integer32
_BHttpServLatencyStatsIntervalDuration_Object = MibTableColumn
bHttpServLatencyStatsIntervalDuration = _BHttpServLatencyStatsIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 2),
    _BHttpServLatencyStatsIntervalDuration_Type()
)
bHttpServLatencyStatsIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyStatsIntervalDuration.setStatus("current")
_BHttpServLatencyTotalPktCount_Type = Unsigned32
_BHttpServLatencyTotalPktCount_Object = MibTableColumn
bHttpServLatencyTotalPktCount = _BHttpServLatencyTotalPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 3),
    _BHttpServLatencyTotalPktCount_Type()
)
bHttpServLatencyTotalPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyTotalPktCount.setStatus("current")
_BHttpServLatencyMaxProcessingTime_Type = Unsigned32
_BHttpServLatencyMaxProcessingTime_Object = MibTableColumn
bHttpServLatencyMaxProcessingTime = _BHttpServLatencyMaxProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 4),
    _BHttpServLatencyMaxProcessingTime_Type()
)
bHttpServLatencyMaxProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyMaxProcessingTime.setStatus("current")
_BHttpServLatencyMinProcessingTime_Type = Unsigned32
_BHttpServLatencyMinProcessingTime_Object = MibTableColumn
bHttpServLatencyMinProcessingTime = _BHttpServLatencyMinProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 5),
    _BHttpServLatencyMinProcessingTime_Type()
)
bHttpServLatencyMinProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyMinProcessingTime.setStatus("current")
_BHttpServLatencyAvgProcessingTime_Type = Unsigned32
_BHttpServLatencyAvgProcessingTime_Object = MibTableColumn
bHttpServLatencyAvgProcessingTime = _BHttpServLatencyAvgProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 6),
    _BHttpServLatencyAvgProcessingTime_Type()
)
bHttpServLatencyAvgProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyAvgProcessingTime.setStatus("current")
_BHttpServLatencyProcessTimeMorethan1MSPktCount_Type = Unsigned32
_BHttpServLatencyProcessTimeMorethan1MSPktCount_Object = MibTableColumn
bHttpServLatencyProcessTimeMorethan1MSPktCount = _BHttpServLatencyProcessTimeMorethan1MSPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 7),
    _BHttpServLatencyProcessTimeMorethan1MSPktCount_Type()
)
bHttpServLatencyProcessTimeMorethan1MSPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyProcessTimeMorethan1MSPktCount.setStatus("current")
_BHttpServLatencyGetTotalPktCount_Type = Unsigned32
_BHttpServLatencyGetTotalPktCount_Object = MibTableColumn
bHttpServLatencyGetTotalPktCount = _BHttpServLatencyGetTotalPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 8),
    _BHttpServLatencyGetTotalPktCount_Type()
)
bHttpServLatencyGetTotalPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyGetTotalPktCount.setStatus("current")
_BHttpServLatencyGetMaxProcessingTime_Type = Unsigned32
_BHttpServLatencyGetMaxProcessingTime_Object = MibTableColumn
bHttpServLatencyGetMaxProcessingTime = _BHttpServLatencyGetMaxProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 9),
    _BHttpServLatencyGetMaxProcessingTime_Type()
)
bHttpServLatencyGetMaxProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyGetMaxProcessingTime.setStatus("current")
_BHttpServLatencyGetMinProcessingTime_Type = Unsigned32
_BHttpServLatencyGetMinProcessingTime_Object = MibTableColumn
bHttpServLatencyGetMinProcessingTime = _BHttpServLatencyGetMinProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 10),
    _BHttpServLatencyGetMinProcessingTime_Type()
)
bHttpServLatencyGetMinProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyGetMinProcessingTime.setStatus("current")
_BHttpServLatencyGetAvgProcessingTime_Type = Unsigned32
_BHttpServLatencyGetAvgProcessingTime_Object = MibTableColumn
bHttpServLatencyGetAvgProcessingTime = _BHttpServLatencyGetAvgProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 11),
    _BHttpServLatencyGetAvgProcessingTime_Type()
)
bHttpServLatencyGetAvgProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyGetAvgProcessingTime.setStatus("current")
_BHttpServLatencyGetProcessTimeMorethan1MSPktCount_Type = Unsigned32
_BHttpServLatencyGetProcessTimeMorethan1MSPktCount_Object = MibTableColumn
bHttpServLatencyGetProcessTimeMorethan1MSPktCount = _BHttpServLatencyGetProcessTimeMorethan1MSPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 12),
    _BHttpServLatencyGetProcessTimeMorethan1MSPktCount_Type()
)
bHttpServLatencyGetProcessTimeMorethan1MSPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyGetProcessTimeMorethan1MSPktCount.setStatus("current")
_BHttpServLatencyPostTotalPktCount_Type = Unsigned32
_BHttpServLatencyPostTotalPktCount_Object = MibTableColumn
bHttpServLatencyPostTotalPktCount = _BHttpServLatencyPostTotalPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 13),
    _BHttpServLatencyPostTotalPktCount_Type()
)
bHttpServLatencyPostTotalPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyPostTotalPktCount.setStatus("current")
_BHttpServLatencyPostMaxProcessingTime_Type = Unsigned32
_BHttpServLatencyPostMaxProcessingTime_Object = MibTableColumn
bHttpServLatencyPostMaxProcessingTime = _BHttpServLatencyPostMaxProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 14),
    _BHttpServLatencyPostMaxProcessingTime_Type()
)
bHttpServLatencyPostMaxProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyPostMaxProcessingTime.setStatus("current")
_BHttpServLatencyPostMinProcessingTime_Type = Unsigned32
_BHttpServLatencyPostMinProcessingTime_Object = MibTableColumn
bHttpServLatencyPostMinProcessingTime = _BHttpServLatencyPostMinProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 15),
    _BHttpServLatencyPostMinProcessingTime_Type()
)
bHttpServLatencyPostMinProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyPostMinProcessingTime.setStatus("current")
_BHttpServLatencyPostAvgProcessingTime_Type = Unsigned32
_BHttpServLatencyPostAvgProcessingTime_Object = MibTableColumn
bHttpServLatencyPostAvgProcessingTime = _BHttpServLatencyPostAvgProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 16),
    _BHttpServLatencyPostAvgProcessingTime_Type()
)
bHttpServLatencyPostAvgProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyPostAvgProcessingTime.setStatus("current")
_BHttpServLatencyPostProcessTimeMorethan1MSPktCount_Type = Unsigned32
_BHttpServLatencyPostProcessTimeMorethan1MSPktCount_Object = MibTableColumn
bHttpServLatencyPostProcessTimeMorethan1MSPktCount = _BHttpServLatencyPostProcessTimeMorethan1MSPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 17),
    _BHttpServLatencyPostProcessTimeMorethan1MSPktCount_Type()
)
bHttpServLatencyPostProcessTimeMorethan1MSPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyPostProcessTimeMorethan1MSPktCount.setStatus("current")
_BHttpServLatencyDeleteTotalPktCount_Type = Unsigned32
_BHttpServLatencyDeleteTotalPktCount_Object = MibTableColumn
bHttpServLatencyDeleteTotalPktCount = _BHttpServLatencyDeleteTotalPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 18),
    _BHttpServLatencyDeleteTotalPktCount_Type()
)
bHttpServLatencyDeleteTotalPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyDeleteTotalPktCount.setStatus("current")
_BHttpServLatencyDeleteMaxProcessingTime_Type = Unsigned32
_BHttpServLatencyDeleteMaxProcessingTime_Object = MibTableColumn
bHttpServLatencyDeleteMaxProcessingTime = _BHttpServLatencyDeleteMaxProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 19),
    _BHttpServLatencyDeleteMaxProcessingTime_Type()
)
bHttpServLatencyDeleteMaxProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyDeleteMaxProcessingTime.setStatus("current")
_BHttpServLatencyDeleteMinProcessingTime_Type = Unsigned32
_BHttpServLatencyDeleteMinProcessingTime_Object = MibTableColumn
bHttpServLatencyDeleteMinProcessingTime = _BHttpServLatencyDeleteMinProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 20),
    _BHttpServLatencyDeleteMinProcessingTime_Type()
)
bHttpServLatencyDeleteMinProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyDeleteMinProcessingTime.setStatus("current")
_BHttpServLatencyDeleteAvgProcessingTime_Type = Unsigned32
_BHttpServLatencyDeleteAvgProcessingTime_Object = MibTableColumn
bHttpServLatencyDeleteAvgProcessingTime = _BHttpServLatencyDeleteAvgProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 21),
    _BHttpServLatencyDeleteAvgProcessingTime_Type()
)
bHttpServLatencyDeleteAvgProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyDeleteAvgProcessingTime.setStatus("current")
_BHttpServLatencyDeleteProcessTimeMorethan1MSPktCount_Type = Unsigned32
_BHttpServLatencyDeleteProcessTimeMorethan1MSPktCount_Object = MibTableColumn
bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount = _BHttpServLatencyDeleteProcessTimeMorethan1MSPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 22),
    _BHttpServLatencyDeleteProcessTimeMorethan1MSPktCount_Type()
)
bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-HTTP-SERVER-MIB",
    **{"benuHttpServerMIB": benuHttpServerMIB,
       "bHttpServerObjects": bHttpServerObjects,
       "bHttpServerLatencyTable": bHttpServerLatencyTable,
       "bHttpServerLatencyEntry": bHttpServerLatencyEntry,
       "bHttpServLatencyStatsInterval": bHttpServLatencyStatsInterval,
       "bHttpServLatencyStatsIntervalDuration": bHttpServLatencyStatsIntervalDuration,
       "bHttpServLatencyTotalPktCount": bHttpServLatencyTotalPktCount,
       "bHttpServLatencyMaxProcessingTime": bHttpServLatencyMaxProcessingTime,
       "bHttpServLatencyMinProcessingTime": bHttpServLatencyMinProcessingTime,
       "bHttpServLatencyAvgProcessingTime": bHttpServLatencyAvgProcessingTime,
       "bHttpServLatencyProcessTimeMorethan1MSPktCount": bHttpServLatencyProcessTimeMorethan1MSPktCount,
       "bHttpServLatencyGetTotalPktCount": bHttpServLatencyGetTotalPktCount,
       "bHttpServLatencyGetMaxProcessingTime": bHttpServLatencyGetMaxProcessingTime,
       "bHttpServLatencyGetMinProcessingTime": bHttpServLatencyGetMinProcessingTime,
       "bHttpServLatencyGetAvgProcessingTime": bHttpServLatencyGetAvgProcessingTime,
       "bHttpServLatencyGetProcessTimeMorethan1MSPktCount": bHttpServLatencyGetProcessTimeMorethan1MSPktCount,
       "bHttpServLatencyPostTotalPktCount": bHttpServLatencyPostTotalPktCount,
       "bHttpServLatencyPostMaxProcessingTime": bHttpServLatencyPostMaxProcessingTime,
       "bHttpServLatencyPostMinProcessingTime": bHttpServLatencyPostMinProcessingTime,
       "bHttpServLatencyPostAvgProcessingTime": bHttpServLatencyPostAvgProcessingTime,
       "bHttpServLatencyPostProcessTimeMorethan1MSPktCount": bHttpServLatencyPostProcessTimeMorethan1MSPktCount,
       "bHttpServLatencyDeleteTotalPktCount": bHttpServLatencyDeleteTotalPktCount,
       "bHttpServLatencyDeleteMaxProcessingTime": bHttpServLatencyDeleteMaxProcessingTime,
       "bHttpServLatencyDeleteMinProcessingTime": bHttpServLatencyDeleteMinProcessingTime,
       "bHttpServLatencyDeleteAvgProcessingTime": bHttpServLatencyDeleteAvgProcessingTime,
       "bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount": bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount}
)
