# SNMP MIB module (BENU-HTTP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-HTTP-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:54 2024
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

benuHttpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11)
)
benuHttpClientMIB.setRevisions(
        ("2015-10-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BHttpClientObjects_ObjectIdentity = ObjectIdentity
bHttpClientObjects = _BHttpClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    bHttpClientObjects.setStatus("current")
_BHttpClientLatencyTable_Object = MibTable
bHttpClientLatencyTable = _BHttpClientLatencyTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    bHttpClientLatencyTable.setStatus("current")
_BHttpClientLatencyEntry_Object = MibTableRow
bHttpClientLatencyEntry = _BHttpClientLatencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1)
)
bHttpClientLatencyEntry.setIndexNames(
    (0, "BENU-HTTP-CLIENT-MIB", "bHttpClientLatencyStatsInterval"),
)
if mibBuilder.loadTexts:
    bHttpClientLatencyEntry.setStatus("current")
_BHttpClientLatencyStatsInterval_Type = Integer32
_BHttpClientLatencyStatsInterval_Object = MibTableColumn
bHttpClientLatencyStatsInterval = _BHttpClientLatencyStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 1),
    _BHttpClientLatencyStatsInterval_Type()
)
bHttpClientLatencyStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bHttpClientLatencyStatsInterval.setStatus("current")
_BHttpClientLatencyStatsIntervalDuration_Type = Integer32
_BHttpClientLatencyStatsIntervalDuration_Object = MibTableColumn
bHttpClientLatencyStatsIntervalDuration = _BHttpClientLatencyStatsIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 2),
    _BHttpClientLatencyStatsIntervalDuration_Type()
)
bHttpClientLatencyStatsIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientLatencyStatsIntervalDuration.setStatus("current")
_BHttpClientLatencyTotalPktCount_Type = Unsigned32
_BHttpClientLatencyTotalPktCount_Object = MibTableColumn
bHttpClientLatencyTotalPktCount = _BHttpClientLatencyTotalPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 3),
    _BHttpClientLatencyTotalPktCount_Type()
)
bHttpClientLatencyTotalPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientLatencyTotalPktCount.setStatus("current")
_BHttpClientLatencyMaxProcessingTime_Type = Unsigned32
_BHttpClientLatencyMaxProcessingTime_Object = MibTableColumn
bHttpClientLatencyMaxProcessingTime = _BHttpClientLatencyMaxProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 4),
    _BHttpClientLatencyMaxProcessingTime_Type()
)
bHttpClientLatencyMaxProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientLatencyMaxProcessingTime.setStatus("current")
_BHttpClientLatencyMinProcessingTime_Type = Unsigned32
_BHttpClientLatencyMinProcessingTime_Object = MibTableColumn
bHttpClientLatencyMinProcessingTime = _BHttpClientLatencyMinProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 5),
    _BHttpClientLatencyMinProcessingTime_Type()
)
bHttpClientLatencyMinProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientLatencyMinProcessingTime.setStatus("current")
_BHttpClientLatencyAvgProcessingTime_Type = Unsigned32
_BHttpClientLatencyAvgProcessingTime_Object = MibTableColumn
bHttpClientLatencyAvgProcessingTime = _BHttpClientLatencyAvgProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 6),
    _BHttpClientLatencyAvgProcessingTime_Type()
)
bHttpClientLatencyAvgProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientLatencyAvgProcessingTime.setStatus("current")
_BHttpClientLatencyProcessTimeMorethan10MSPktCount_Type = Unsigned32
_BHttpClientLatencyProcessTimeMorethan10MSPktCount_Object = MibTableColumn
bHttpClientLatencyProcessTimeMorethan10MSPktCount = _BHttpClientLatencyProcessTimeMorethan10MSPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 7),
    _BHttpClientLatencyProcessTimeMorethan10MSPktCount_Type()
)
bHttpClientLatencyProcessTimeMorethan10MSPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientLatencyProcessTimeMorethan10MSPktCount.setStatus("current")
_BHttpClientServReqLatencyTotalPktCount_Type = Unsigned32
_BHttpClientServReqLatencyTotalPktCount_Object = MibTableColumn
bHttpClientServReqLatencyTotalPktCount = _BHttpClientServReqLatencyTotalPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 8),
    _BHttpClientServReqLatencyTotalPktCount_Type()
)
bHttpClientServReqLatencyTotalPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientServReqLatencyTotalPktCount.setStatus("current")
_BHttpClientServReqLatencyMaxProcessingTime_Type = Unsigned32
_BHttpClientServReqLatencyMaxProcessingTime_Object = MibTableColumn
bHttpClientServReqLatencyMaxProcessingTime = _BHttpClientServReqLatencyMaxProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 9),
    _BHttpClientServReqLatencyMaxProcessingTime_Type()
)
bHttpClientServReqLatencyMaxProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientServReqLatencyMaxProcessingTime.setStatus("current")
_BHttpClientServReqLatencyMinProcessingTime_Type = Unsigned32
_BHttpClientServReqLatencyMinProcessingTime_Object = MibTableColumn
bHttpClientServReqLatencyMinProcessingTime = _BHttpClientServReqLatencyMinProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 10),
    _BHttpClientServReqLatencyMinProcessingTime_Type()
)
bHttpClientServReqLatencyMinProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientServReqLatencyMinProcessingTime.setStatus("current")
_BHttpClientServReqLatencyAvgProcessingTime_Type = Unsigned32
_BHttpClientServReqLatencyAvgProcessingTime_Object = MibTableColumn
bHttpClientServReqLatencyAvgProcessingTime = _BHttpClientServReqLatencyAvgProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 11),
    _BHttpClientServReqLatencyAvgProcessingTime_Type()
)
bHttpClientServReqLatencyAvgProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientServReqLatencyAvgProcessingTime.setStatus("current")
_BHttpClientServReqLatencyProcessTimeMorethan10MSPktCount_Type = Unsigned32
_BHttpClientServReqLatencyProcessTimeMorethan10MSPktCount_Object = MibTableColumn
bHttpClientServReqLatencyProcessTimeMorethan10MSPktCount = _BHttpClientServReqLatencyProcessTimeMorethan10MSPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 12),
    _BHttpClientServReqLatencyProcessTimeMorethan10MSPktCount_Type()
)
bHttpClientServReqLatencyProcessTimeMorethan10MSPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientServReqLatencyProcessTimeMorethan10MSPktCount.setStatus("current")
_BHttpClientJsonParsingLatencyTotalPktCount_Type = Unsigned32
_BHttpClientJsonParsingLatencyTotalPktCount_Object = MibTableColumn
bHttpClientJsonParsingLatencyTotalPktCount = _BHttpClientJsonParsingLatencyTotalPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 13),
    _BHttpClientJsonParsingLatencyTotalPktCount_Type()
)
bHttpClientJsonParsingLatencyTotalPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientJsonParsingLatencyTotalPktCount.setStatus("current")
_BHttpClientJsonParsingLatencyMaxProcessingTime_Type = Unsigned32
_BHttpClientJsonParsingLatencyMaxProcessingTime_Object = MibTableColumn
bHttpClientJsonParsingLatencyMaxProcessingTime = _BHttpClientJsonParsingLatencyMaxProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 14),
    _BHttpClientJsonParsingLatencyMaxProcessingTime_Type()
)
bHttpClientJsonParsingLatencyMaxProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientJsonParsingLatencyMaxProcessingTime.setStatus("current")
_BHttpClientJsonParsingLatencyMinProcessingTime_Type = Unsigned32
_BHttpClientJsonParsingLatencyMinProcessingTime_Object = MibTableColumn
bHttpClientJsonParsingLatencyMinProcessingTime = _BHttpClientJsonParsingLatencyMinProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 15),
    _BHttpClientJsonParsingLatencyMinProcessingTime_Type()
)
bHttpClientJsonParsingLatencyMinProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientJsonParsingLatencyMinProcessingTime.setStatus("current")
_BHttpClientJsonParsingLatencyAvgProcessingTime_Type = Unsigned32
_BHttpClientJsonParsingLatencyAvgProcessingTime_Object = MibTableColumn
bHttpClientJsonParsingLatencyAvgProcessingTime = _BHttpClientJsonParsingLatencyAvgProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 16),
    _BHttpClientJsonParsingLatencyAvgProcessingTime_Type()
)
bHttpClientJsonParsingLatencyAvgProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientJsonParsingLatencyAvgProcessingTime.setStatus("current")
_BHttpClientJsonParsingLatencyProcessTimeMorethan10MS_Type = Unsigned32
_BHttpClientJsonParsingLatencyProcessTimeMorethan10MS_Object = MibTableColumn
bHttpClientJsonParsingLatencyProcessTimeMorethan10MS = _BHttpClientJsonParsingLatencyProcessTimeMorethan10MS_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 11, 1, 1, 1, 17),
    _BHttpClientJsonParsingLatencyProcessTimeMorethan10MS_Type()
)
bHttpClientJsonParsingLatencyProcessTimeMorethan10MS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHttpClientJsonParsingLatencyProcessTimeMorethan10MS.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-HTTP-CLIENT-MIB",
    **{"benuHttpClientMIB": benuHttpClientMIB,
       "bHttpClientObjects": bHttpClientObjects,
       "bHttpClientLatencyTable": bHttpClientLatencyTable,
       "bHttpClientLatencyEntry": bHttpClientLatencyEntry,
       "bHttpClientLatencyStatsInterval": bHttpClientLatencyStatsInterval,
       "bHttpClientLatencyStatsIntervalDuration": bHttpClientLatencyStatsIntervalDuration,
       "bHttpClientLatencyTotalPktCount": bHttpClientLatencyTotalPktCount,
       "bHttpClientLatencyMaxProcessingTime": bHttpClientLatencyMaxProcessingTime,
       "bHttpClientLatencyMinProcessingTime": bHttpClientLatencyMinProcessingTime,
       "bHttpClientLatencyAvgProcessingTime": bHttpClientLatencyAvgProcessingTime,
       "bHttpClientLatencyProcessTimeMorethan10MSPktCount": bHttpClientLatencyProcessTimeMorethan10MSPktCount,
       "bHttpClientServReqLatencyTotalPktCount": bHttpClientServReqLatencyTotalPktCount,
       "bHttpClientServReqLatencyMaxProcessingTime": bHttpClientServReqLatencyMaxProcessingTime,
       "bHttpClientServReqLatencyMinProcessingTime": bHttpClientServReqLatencyMinProcessingTime,
       "bHttpClientServReqLatencyAvgProcessingTime": bHttpClientServReqLatencyAvgProcessingTime,
       "bHttpClientServReqLatencyProcessTimeMorethan10MSPktCount": bHttpClientServReqLatencyProcessTimeMorethan10MSPktCount,
       "bHttpClientJsonParsingLatencyTotalPktCount": bHttpClientJsonParsingLatencyTotalPktCount,
       "bHttpClientJsonParsingLatencyMaxProcessingTime": bHttpClientJsonParsingLatencyMaxProcessingTime,
       "bHttpClientJsonParsingLatencyMinProcessingTime": bHttpClientJsonParsingLatencyMinProcessingTime,
       "bHttpClientJsonParsingLatencyAvgProcessingTime": bHttpClientJsonParsingLatencyAvgProcessingTime,
       "bHttpClientJsonParsingLatencyProcessTimeMorethan10MS": bHttpClientJsonParsingLatencyProcessTimeMorethan10MS}
)
