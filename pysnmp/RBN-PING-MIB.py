# SNMP MIB module (RBN-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:19 2024
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

(pingCtlEntry,
 pingCtlOwnerIndex,
 pingCtlTestName,
 pingResultsEntry) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "pingCtlEntry",
    "pingCtlOwnerIndex",
    "pingCtlTestName",
    "pingResultsEntry")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnPingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46)
)
rbnPingMib.setRevisions(
        ("2008-07-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnPingObjects_ObjectIdentity = ObjectIdentity
rbnPingObjects = _RbnPingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1)
)
_RbnPingGlobals_ObjectIdentity = ObjectIdentity
rbnPingGlobals = _RbnPingGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 1)
)
_RbnPingNumTests_Type = Gauge32
_RbnPingNumTests_Object = MibScalar
rbnPingNumTests = _RbnPingNumTests_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 1, 1),
    _RbnPingNumTests_Type()
)
rbnPingNumTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingNumTests.setStatus("current")
_RbnPingResults_ObjectIdentity = ObjectIdentity
rbnPingResults = _RbnPingResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2)
)
_RbnPingResultsTable_Object = MibTable
rbnPingResultsTable = _RbnPingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rbnPingResultsTable.setStatus("current")
_RbnPingResultsEntry_Object = MibTableRow
rbnPingResultsEntry = _RbnPingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnPingResultsEntry.setStatus("current")
_RbnPingResultsJitter_Type = Gauge32
_RbnPingResultsJitter_Object = MibTableColumn
rbnPingResultsJitter = _RbnPingResultsJitter_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 1, 1, 1),
    _RbnPingResultsJitter_Type()
)
rbnPingResultsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingResultsJitter.setStatus("current")
if mibBuilder.loadTexts:
    rbnPingResultsJitter.setUnits("milliseconds")
_RbnPingHistoryTable_Object = MibTable
rbnPingHistoryTable = _RbnPingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rbnPingHistoryTable.setStatus("current")
_RbnPingHistoryEntry_Object = MibTableRow
rbnPingHistoryEntry = _RbnPingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1)
)
rbnPingHistoryEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "RBN-PING-MIB", "rbnPingHistoryIndex"),
)
if mibBuilder.loadTexts:
    rbnPingHistoryEntry.setStatus("current")


class _RbnPingHistoryIndex_Type(Unsigned32):
    """Custom type rbnPingHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnPingHistoryIndex_Type.__name__ = "Unsigned32"
_RbnPingHistoryIndex_Object = MibTableColumn
rbnPingHistoryIndex = _RbnPingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 1),
    _RbnPingHistoryIndex_Type()
)
rbnPingHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnPingHistoryIndex.setStatus("current")


class _RbnPingHistoryIpTargetAddressType_Type(InetAddressType):
    """Custom type rbnPingHistoryIpTargetAddressType based on InetAddressType"""


_RbnPingHistoryIpTargetAddressType_Object = MibTableColumn
rbnPingHistoryIpTargetAddressType = _RbnPingHistoryIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 2),
    _RbnPingHistoryIpTargetAddressType_Type()
)
rbnPingHistoryIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistoryIpTargetAddressType.setStatus("current")


class _RbnPingHistoryIpTargetAddress_Type(InetAddress):
    """Custom type rbnPingHistoryIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_RbnPingHistoryIpTargetAddress_Object = MibTableColumn
rbnPingHistoryIpTargetAddress = _RbnPingHistoryIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 3),
    _RbnPingHistoryIpTargetAddress_Type()
)
rbnPingHistoryIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistoryIpTargetAddress.setStatus("current")
_RbnPingHistoryMinRtt_Type = Unsigned32
_RbnPingHistoryMinRtt_Object = MibTableColumn
rbnPingHistoryMinRtt = _RbnPingHistoryMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 4),
    _RbnPingHistoryMinRtt_Type()
)
rbnPingHistoryMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistoryMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    rbnPingHistoryMinRtt.setUnits("milliseconds")
_RbnPingHistoryMaxRtt_Type = Unsigned32
_RbnPingHistoryMaxRtt_Object = MibTableColumn
rbnPingHistoryMaxRtt = _RbnPingHistoryMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 5),
    _RbnPingHistoryMaxRtt_Type()
)
rbnPingHistoryMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistoryMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    rbnPingHistoryMaxRtt.setUnits("milliseconds")
_RbnPingHistoryAverageRtt_Type = Unsigned32
_RbnPingHistoryAverageRtt_Object = MibTableColumn
rbnPingHistoryAverageRtt = _RbnPingHistoryAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 6),
    _RbnPingHistoryAverageRtt_Type()
)
rbnPingHistoryAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistoryAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    rbnPingHistoryAverageRtt.setUnits("milliseconds")
_RbnPingHistoryProbeResponses_Type = Gauge32
_RbnPingHistoryProbeResponses_Object = MibTableColumn
rbnPingHistoryProbeResponses = _RbnPingHistoryProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 7),
    _RbnPingHistoryProbeResponses_Type()
)
rbnPingHistoryProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistoryProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    rbnPingHistoryProbeResponses.setUnits("responses")
_RbnPingHistorySentProbes_Type = Gauge32
_RbnPingHistorySentProbes_Object = MibTableColumn
rbnPingHistorySentProbes = _RbnPingHistorySentProbes_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 8),
    _RbnPingHistorySentProbes_Type()
)
rbnPingHistorySentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistorySentProbes.setStatus("current")
if mibBuilder.loadTexts:
    rbnPingHistorySentProbes.setUnits("probes")
_RbnPingHistoryRttSumOfSquares_Type = Unsigned32
_RbnPingHistoryRttSumOfSquares_Object = MibTableColumn
rbnPingHistoryRttSumOfSquares = _RbnPingHistoryRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 9),
    _RbnPingHistoryRttSumOfSquares_Type()
)
rbnPingHistoryRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistoryRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    rbnPingHistoryRttSumOfSquares.setUnits("milliseconds")
_RbnPingHistoryLastGoodProbe_Type = DateAndTime
_RbnPingHistoryLastGoodProbe_Object = MibTableColumn
rbnPingHistoryLastGoodProbe = _RbnPingHistoryLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 10),
    _RbnPingHistoryLastGoodProbe_Type()
)
rbnPingHistoryLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistoryLastGoodProbe.setStatus("current")
_RbnPingHistoryJitter_Type = Gauge32
_RbnPingHistoryJitter_Object = MibTableColumn
rbnPingHistoryJitter = _RbnPingHistoryJitter_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 2, 2, 1, 11),
    _RbnPingHistoryJitter_Type()
)
rbnPingHistoryJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPingHistoryJitter.setStatus("current")
if mibBuilder.loadTexts:
    rbnPingHistoryJitter.setUnits("milliseconds")
_RbnPingControl_ObjectIdentity = ObjectIdentity
rbnPingControl = _RbnPingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 3)
)
_RbnPingCtlTable_Object = MibTable
rbnPingCtlTable = _RbnPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rbnPingCtlTable.setStatus("current")
_RbnPingCtlEntry_Object = MibTableRow
rbnPingCtlEntry = _RbnPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rbnPingCtlEntry.setStatus("current")


class _RbnPingCtlMaxHistoryRows_Type(Unsigned32):
    """Custom type rbnPingCtlMaxHistoryRows based on Unsigned32"""
    defaultValue = 12


_RbnPingCtlMaxHistoryRows_Object = MibTableColumn
rbnPingCtlMaxHistoryRows = _RbnPingCtlMaxHistoryRows_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 3, 1, 1, 1),
    _RbnPingCtlMaxHistoryRows_Type()
)
rbnPingCtlMaxHistoryRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnPingCtlMaxHistoryRows.setStatus("current")
_RbnPingIp_ObjectIdentity = ObjectIdentity
rbnPingIp = _RbnPingIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 4)
)
_RbnPingCtlIpTable_Object = MibTable
rbnPingCtlIpTable = _RbnPingCtlIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rbnPingCtlIpTable.setStatus("current")
_RbnPingCtlIpEntry_Object = MibTableRow
rbnPingCtlIpEntry = _RbnPingCtlIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rbnPingCtlIpEntry.setStatus("current")


class _RbnPingCtlIpDontFragment_Type(TruthValue):
    """Custom type rbnPingCtlIpDontFragment based on TruthValue"""


_RbnPingCtlIpDontFragment_Object = MibTableColumn
rbnPingCtlIpDontFragment = _RbnPingCtlIpDontFragment_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 4, 1, 1, 1),
    _RbnPingCtlIpDontFragment_Type()
)
rbnPingCtlIpDontFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnPingCtlIpDontFragment.setStatus("current")


class _RbnPingCtlIpTtl_Type(Unsigned32):
    """Custom type rbnPingCtlIpTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbnPingCtlIpTtl_Type.__name__ = "Unsigned32"
_RbnPingCtlIpTtl_Object = MibTableColumn
rbnPingCtlIpTtl = _RbnPingCtlIpTtl_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 1, 4, 1, 1, 2),
    _RbnPingCtlIpTtl_Type()
)
rbnPingCtlIpTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnPingCtlIpTtl.setStatus("current")
_RbnPingConformance_ObjectIdentity = ObjectIdentity
rbnPingConformance = _RbnPingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 2)
)
_RbnPingCompliances_ObjectIdentity = ObjectIdentity
rbnPingCompliances = _RbnPingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 2, 1)
)
_RbnPingGroups_ObjectIdentity = ObjectIdentity
rbnPingGroups = _RbnPingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 2, 2)
)
_RbnPingNotifications_ObjectIdentity = ObjectIdentity
rbnPingNotifications = _RbnPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 3)
)
pingResultsEntry.registerAugmentions(
    ("RBN-PING-MIB",
     "rbnPingResultsEntry")
)
rbnPingResultsEntry.setIndexNames(*pingResultsEntry.getIndexNames())
pingCtlEntry.registerAugmentions(
    ("RBN-PING-MIB",
     "rbnPingCtlEntry")
)
rbnPingCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
pingCtlEntry.registerAugmentions(
    ("RBN-PING-MIB",
     "rbnPingCtlIpEntry")
)
rbnPingCtlIpEntry.setIndexNames(*pingCtlEntry.getIndexNames())

# Managed Objects groups

rbnPingGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 2, 2, 1)
)
rbnPingGlobalsGroup.setObjects(
    ("RBN-PING-MIB", "rbnPingNumTests")
)
if mibBuilder.loadTexts:
    rbnPingGlobalsGroup.setStatus("current")

rbnPingResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 2, 2, 2)
)
rbnPingResultsGroup.setObjects(
      *(("RBN-PING-MIB", "rbnPingResultsJitter"),
        ("RBN-PING-MIB", "rbnPingHistoryIpTargetAddressType"),
        ("RBN-PING-MIB", "rbnPingHistoryIpTargetAddress"),
        ("RBN-PING-MIB", "rbnPingHistoryMinRtt"),
        ("RBN-PING-MIB", "rbnPingHistoryMaxRtt"),
        ("RBN-PING-MIB", "rbnPingHistoryAverageRtt"),
        ("RBN-PING-MIB", "rbnPingHistoryProbeResponses"),
        ("RBN-PING-MIB", "rbnPingHistorySentProbes"),
        ("RBN-PING-MIB", "rbnPingHistoryRttSumOfSquares"),
        ("RBN-PING-MIB", "rbnPingHistoryLastGoodProbe"),
        ("RBN-PING-MIB", "rbnPingHistoryJitter"))
)
if mibBuilder.loadTexts:
    rbnPingResultsGroup.setStatus("current")

rbnPingCtlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 2, 2, 3)
)
rbnPingCtlGroup.setObjects(
    ("RBN-PING-MIB", "rbnPingCtlMaxHistoryRows")
)
if mibBuilder.loadTexts:
    rbnPingCtlGroup.setStatus("current")

rbnPingIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 2, 2, 4)
)
rbnPingIpGroup.setObjects(
      *(("RBN-PING-MIB", "rbnPingCtlIpDontFragment"),
        ("RBN-PING-MIB", "rbnPingCtlIpTtl"))
)
if mibBuilder.loadTexts:
    rbnPingIpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnPingIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 46, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnPingIpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-PING-MIB",
    **{"rbnPingMib": rbnPingMib,
       "rbnPingObjects": rbnPingObjects,
       "rbnPingGlobals": rbnPingGlobals,
       "rbnPingNumTests": rbnPingNumTests,
       "rbnPingResults": rbnPingResults,
       "rbnPingResultsTable": rbnPingResultsTable,
       "rbnPingResultsEntry": rbnPingResultsEntry,
       "rbnPingResultsJitter": rbnPingResultsJitter,
       "rbnPingHistoryTable": rbnPingHistoryTable,
       "rbnPingHistoryEntry": rbnPingHistoryEntry,
       "rbnPingHistoryIndex": rbnPingHistoryIndex,
       "rbnPingHistoryIpTargetAddressType": rbnPingHistoryIpTargetAddressType,
       "rbnPingHistoryIpTargetAddress": rbnPingHistoryIpTargetAddress,
       "rbnPingHistoryMinRtt": rbnPingHistoryMinRtt,
       "rbnPingHistoryMaxRtt": rbnPingHistoryMaxRtt,
       "rbnPingHistoryAverageRtt": rbnPingHistoryAverageRtt,
       "rbnPingHistoryProbeResponses": rbnPingHistoryProbeResponses,
       "rbnPingHistorySentProbes": rbnPingHistorySentProbes,
       "rbnPingHistoryRttSumOfSquares": rbnPingHistoryRttSumOfSquares,
       "rbnPingHistoryLastGoodProbe": rbnPingHistoryLastGoodProbe,
       "rbnPingHistoryJitter": rbnPingHistoryJitter,
       "rbnPingControl": rbnPingControl,
       "rbnPingCtlTable": rbnPingCtlTable,
       "rbnPingCtlEntry": rbnPingCtlEntry,
       "rbnPingCtlMaxHistoryRows": rbnPingCtlMaxHistoryRows,
       "rbnPingIp": rbnPingIp,
       "rbnPingCtlIpTable": rbnPingCtlIpTable,
       "rbnPingCtlIpEntry": rbnPingCtlIpEntry,
       "rbnPingCtlIpDontFragment": rbnPingCtlIpDontFragment,
       "rbnPingCtlIpTtl": rbnPingCtlIpTtl,
       "rbnPingConformance": rbnPingConformance,
       "rbnPingCompliances": rbnPingCompliances,
       "rbnPingIpCompliance": rbnPingIpCompliance,
       "rbnPingGroups": rbnPingGroups,
       "rbnPingGlobalsGroup": rbnPingGlobalsGroup,
       "rbnPingResultsGroup": rbnPingResultsGroup,
       "rbnPingCtlGroup": rbnPingCtlGroup,
       "rbnPingIpGroup": rbnPingIpGroup,
       "rbnPingNotifications": rbnPingNotifications}
)
