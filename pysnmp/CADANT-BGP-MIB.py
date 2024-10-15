# SNMP MIB module (CADANT-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:22 2024
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

(cadLayer3,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadLayer3")

(BgpIpMatchType,
 bgpRmEntIndex,
 bgpRouteMapIndex,
 bgpRouteMapNumber) = mibBuilder.importSymbols(
    "DC-BGP-MIB",
    "BgpIpMatchType",
    "bgpRmEntIndex",
    "bgpRouteMapIndex",
    "bgpRouteMapNumber")

(FteIndex,) = mibBuilder.importSymbols(
    "DC-RTM-MIB",
    "FteIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadBgpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9)
)
cadBgpMib.setRevisions(
        ("2004-06-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadBgpRouteMapAuxTable_Object = MibTable
cadBgpRouteMapAuxTable = _CadBgpRouteMapAuxTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 17)
)
if mibBuilder.loadTexts:
    cadBgpRouteMapAuxTable.setStatus("current")
_CadBgpRouteMapAuxEntry_Object = MibTableRow
cadBgpRouteMapAuxEntry = _CadBgpRouteMapAuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 17, 1)
)
cadBgpRouteMapAuxEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpRouteMapIndex"),
    (0, "DC-BGP-MIB", "bgpRouteMapNumber"),
)
if mibBuilder.loadTexts:
    cadBgpRouteMapAuxEntry.setStatus("current")


class _CadBgpRouteMapAuxRouteMapName_Type(OctetString):
    """Custom type cadBgpRouteMapAuxRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadBgpRouteMapAuxRouteMapName_Type.__name__ = "OctetString"
_CadBgpRouteMapAuxRouteMapName_Object = MibTableColumn
cadBgpRouteMapAuxRouteMapName = _CadBgpRouteMapAuxRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 17, 1, 1),
    _CadBgpRouteMapAuxRouteMapName_Type()
)
cadBgpRouteMapAuxRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpRouteMapAuxRouteMapName.setStatus("current")


class _CadBgpRouteMapAuxPrefixListName_Type(OctetString):
    """Custom type cadBgpRouteMapAuxPrefixListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadBgpRouteMapAuxPrefixListName_Type.__name__ = "OctetString"
_CadBgpRouteMapAuxPrefixListName_Object = MibTableColumn
cadBgpRouteMapAuxPrefixListName = _CadBgpRouteMapAuxPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 17, 1, 2),
    _CadBgpRouteMapAuxPrefixListName_Type()
)
cadBgpRouteMapAuxPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpRouteMapAuxPrefixListName.setStatus("obsolete")
_CadBgpRouteMapAuxPreMatch_Type = BgpIpMatchType
_CadBgpRouteMapAuxPreMatch_Object = MibTableColumn
cadBgpRouteMapAuxPreMatch = _CadBgpRouteMapAuxPreMatch_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 17, 1, 3),
    _CadBgpRouteMapAuxPreMatch_Type()
)
cadBgpRouteMapAuxPreMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadBgpRouteMapAuxPreMatch.setStatus("obsolete")


class _CadBgpRouteMapAuxMaAddrName_Type(OctetString):
    """Custom type cadBgpRouteMapAuxMaAddrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadBgpRouteMapAuxMaAddrName_Type.__name__ = "OctetString"
_CadBgpRouteMapAuxMaAddrName_Object = MibTableColumn
cadBgpRouteMapAuxMaAddrName = _CadBgpRouteMapAuxMaAddrName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 17, 1, 4),
    _CadBgpRouteMapAuxMaAddrName_Type()
)
cadBgpRouteMapAuxMaAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpRouteMapAuxMaAddrName.setStatus("current")


class _CadBgpRouteMapAuxMaNextName_Type(OctetString):
    """Custom type cadBgpRouteMapAuxMaNextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadBgpRouteMapAuxMaNextName_Type.__name__ = "OctetString"
_CadBgpRouteMapAuxMaNextName_Object = MibTableColumn
cadBgpRouteMapAuxMaNextName = _CadBgpRouteMapAuxMaNextName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 17, 1, 5),
    _CadBgpRouteMapAuxMaNextName_Type()
)
cadBgpRouteMapAuxMaNextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpRouteMapAuxMaNextName.setStatus("current")


class _CadBgpRouteMapAuxMaSourceName_Type(OctetString):
    """Custom type cadBgpRouteMapAuxMaSourceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadBgpRouteMapAuxMaSourceName_Type.__name__ = "OctetString"
_CadBgpRouteMapAuxMaSourceName_Object = MibTableColumn
cadBgpRouteMapAuxMaSourceName = _CadBgpRouteMapAuxMaSourceName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 17, 1, 6),
    _CadBgpRouteMapAuxMaSourceName_Type()
)
cadBgpRouteMapAuxMaSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpRouteMapAuxMaSourceName.setStatus("current")
_CadRtmRedistAuxTable_Object = MibTable
cadRtmRedistAuxTable = _CadRtmRedistAuxTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 18)
)
if mibBuilder.loadTexts:
    cadRtmRedistAuxTable.setStatus("current")
_CadRtmRedistAuxEntry_Object = MibTableRow
cadRtmRedistAuxEntry = _CadRtmRedistAuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 18, 1)
)
cadRtmRedistAuxEntry.setIndexNames(
    (0, "CADANT-BGP-MIB", "rtmRedistFteIndex"),
    (0, "CADANT-BGP-MIB", "rtmRedistEntryId"),
)
if mibBuilder.loadTexts:
    cadRtmRedistAuxEntry.setStatus("current")
_RtmRedistFteIndex_Type = FteIndex
_RtmRedistFteIndex_Object = MibTableColumn
rtmRedistFteIndex = _RtmRedistFteIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 18, 1, 1),
    _RtmRedistFteIndex_Type()
)
rtmRedistFteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRedistFteIndex.setStatus("current")
_RtmRedistEntryId_Type = Unsigned32
_RtmRedistEntryId_Object = MibTableColumn
rtmRedistEntryId = _RtmRedistEntryId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 18, 1, 2),
    _RtmRedistEntryId_Type()
)
rtmRedistEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRedistEntryId.setStatus("current")
_CadRtmRedistAuxRowStatus_Type = RowStatus
_CadRtmRedistAuxRowStatus_Object = MibTableColumn
cadRtmRedistAuxRowStatus = _CadRtmRedistAuxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 18, 1, 3),
    _CadRtmRedistAuxRowStatus_Type()
)
cadRtmRedistAuxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRtmRedistAuxRowStatus.setStatus("current")


class _CadRtmRedistAuxRouteMapIndex_Type(Unsigned32):
    """Custom type cadRtmRedistAuxRouteMapIndex based on Unsigned32"""
    defaultValue = 0


_CadRtmRedistAuxRouteMapIndex_Object = MibTableColumn
cadRtmRedistAuxRouteMapIndex = _CadRtmRedistAuxRouteMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 18, 1, 4),
    _CadRtmRedistAuxRouteMapIndex_Type()
)
cadRtmRedistAuxRouteMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRtmRedistAuxRouteMapIndex.setStatus("current")


class _CadRtmRedistAuxCommandLineMetric_Type(TruthValue):
    """Custom type cadRtmRedistAuxCommandLineMetric based on TruthValue"""


_CadRtmRedistAuxCommandLineMetric_Object = MibTableColumn
cadRtmRedistAuxCommandLineMetric = _CadRtmRedistAuxCommandLineMetric_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 9, 18, 1, 5),
    _CadRtmRedistAuxCommandLineMetric_Type()
)
cadRtmRedistAuxCommandLineMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadRtmRedistAuxCommandLineMetric.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-BGP-MIB",
    **{"cadBgpMib": cadBgpMib,
       "cadBgpRouteMapAuxTable": cadBgpRouteMapAuxTable,
       "cadBgpRouteMapAuxEntry": cadBgpRouteMapAuxEntry,
       "cadBgpRouteMapAuxRouteMapName": cadBgpRouteMapAuxRouteMapName,
       "cadBgpRouteMapAuxPrefixListName": cadBgpRouteMapAuxPrefixListName,
       "cadBgpRouteMapAuxPreMatch": cadBgpRouteMapAuxPreMatch,
       "cadBgpRouteMapAuxMaAddrName": cadBgpRouteMapAuxMaAddrName,
       "cadBgpRouteMapAuxMaNextName": cadBgpRouteMapAuxMaNextName,
       "cadBgpRouteMapAuxMaSourceName": cadBgpRouteMapAuxMaSourceName,
       "cadRtmRedistAuxTable": cadRtmRedistAuxTable,
       "cadRtmRedistAuxEntry": cadRtmRedistAuxEntry,
       "rtmRedistFteIndex": rtmRedistFteIndex,
       "rtmRedistEntryId": rtmRedistEntryId,
       "cadRtmRedistAuxRowStatus": cadRtmRedistAuxRowStatus,
       "cadRtmRedistAuxRouteMapIndex": cadRtmRedistAuxRouteMapIndex,
       "cadRtmRedistAuxCommandLineMetric": cadRtmRedistAuxCommandLineMetric}
)
