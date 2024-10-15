# SNMP MIB module (LISP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LISP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:04 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(MplsL3VpnName,) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "MplsL3VpnName")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

lispMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 220)
)
lispMIB.setRevisions(
        ("2013-10-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LispAddressType(OctetString, TextualConvention):
    status = "current"
    displayHint = "39a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 39),
    )



# MIB Managed Objects in the order of their OIDs

_LispObjects_ObjectIdentity = ObjectIdentity
lispObjects = _LispObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 220, 1)
)
_LispFeaturesTable_Object = MibTable
lispFeaturesTable = _LispFeaturesTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1)
)
if mibBuilder.loadTexts:
    lispFeaturesTable.setStatus("current")
_LispFeaturesEntry_Object = MibTableRow
lispFeaturesEntry = _LispFeaturesEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1)
)
lispFeaturesEntry.setIndexNames(
    (0, "LISP-MIB", "lispFeaturesInstanceID"),
    (0, "LISP-MIB", "lispFeaturesAddressFamily"),
)
if mibBuilder.loadTexts:
    lispFeaturesEntry.setStatus("current")


class _LispFeaturesInstanceID_Type(Unsigned32):
    """Custom type lispFeaturesInstanceID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_LispFeaturesInstanceID_Type.__name__ = "Unsigned32"
_LispFeaturesInstanceID_Object = MibTableColumn
lispFeaturesInstanceID = _LispFeaturesInstanceID_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 1),
    _LispFeaturesInstanceID_Type()
)
lispFeaturesInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispFeaturesInstanceID.setStatus("current")
_LispFeaturesAddressFamily_Type = AddressFamilyNumbers
_LispFeaturesAddressFamily_Object = MibTableColumn
lispFeaturesAddressFamily = _LispFeaturesAddressFamily_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 2),
    _LispFeaturesAddressFamily_Type()
)
lispFeaturesAddressFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispFeaturesAddressFamily.setStatus("current")
_LispFeaturesItrEnabled_Type = TruthValue
_LispFeaturesItrEnabled_Object = MibTableColumn
lispFeaturesItrEnabled = _LispFeaturesItrEnabled_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 3),
    _LispFeaturesItrEnabled_Type()
)
lispFeaturesItrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesItrEnabled.setStatus("current")
_LispFeaturesEtrEnabled_Type = TruthValue
_LispFeaturesEtrEnabled_Object = MibTableColumn
lispFeaturesEtrEnabled = _LispFeaturesEtrEnabled_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 4),
    _LispFeaturesEtrEnabled_Type()
)
lispFeaturesEtrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesEtrEnabled.setStatus("current")
_LispFeaturesProxyItrEnabled_Type = TruthValue
_LispFeaturesProxyItrEnabled_Object = MibTableColumn
lispFeaturesProxyItrEnabled = _LispFeaturesProxyItrEnabled_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 5),
    _LispFeaturesProxyItrEnabled_Type()
)
lispFeaturesProxyItrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesProxyItrEnabled.setStatus("current")
_LispFeaturesProxyEtrEnabled_Type = TruthValue
_LispFeaturesProxyEtrEnabled_Object = MibTableColumn
lispFeaturesProxyEtrEnabled = _LispFeaturesProxyEtrEnabled_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 6),
    _LispFeaturesProxyEtrEnabled_Type()
)
lispFeaturesProxyEtrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesProxyEtrEnabled.setStatus("current")
_LispFeaturesMapServerEnabled_Type = TruthValue
_LispFeaturesMapServerEnabled_Object = MibTableColumn
lispFeaturesMapServerEnabled = _LispFeaturesMapServerEnabled_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 7),
    _LispFeaturesMapServerEnabled_Type()
)
lispFeaturesMapServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesMapServerEnabled.setStatus("current")
_LispFeaturesMapResolverEnabled_Type = TruthValue
_LispFeaturesMapResolverEnabled_Object = MibTableColumn
lispFeaturesMapResolverEnabled = _LispFeaturesMapResolverEnabled_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 8),
    _LispFeaturesMapResolverEnabled_Type()
)
lispFeaturesMapResolverEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesMapResolverEnabled.setStatus("current")
_LispFeaturesMapCacheSize_Type = Unsigned32
_LispFeaturesMapCacheSize_Object = MibTableColumn
lispFeaturesMapCacheSize = _LispFeaturesMapCacheSize_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 9),
    _LispFeaturesMapCacheSize_Type()
)
lispFeaturesMapCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesMapCacheSize.setStatus("current")
_LispFeaturesMapCacheLimit_Type = Unsigned32
_LispFeaturesMapCacheLimit_Object = MibTableColumn
lispFeaturesMapCacheLimit = _LispFeaturesMapCacheLimit_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 10),
    _LispFeaturesMapCacheLimit_Type()
)
lispFeaturesMapCacheLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesMapCacheLimit.setStatus("current")
_LispFeaturesEtrMapCacheTtl_Type = Unsigned32
_LispFeaturesEtrMapCacheTtl_Object = MibTableColumn
lispFeaturesEtrMapCacheTtl = _LispFeaturesEtrMapCacheTtl_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 11),
    _LispFeaturesEtrMapCacheTtl_Type()
)
lispFeaturesEtrMapCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesEtrMapCacheTtl.setStatus("current")
_LispFeaturesRlocProbeEnabled_Type = TruthValue
_LispFeaturesRlocProbeEnabled_Object = MibTableColumn
lispFeaturesRlocProbeEnabled = _LispFeaturesRlocProbeEnabled_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 12),
    _LispFeaturesRlocProbeEnabled_Type()
)
lispFeaturesRlocProbeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesRlocProbeEnabled.setStatus("current")
_LispFeaturesEtrAcceptMapDataEnabled_Type = TruthValue
_LispFeaturesEtrAcceptMapDataEnabled_Object = MibTableColumn
lispFeaturesEtrAcceptMapDataEnabled = _LispFeaturesEtrAcceptMapDataEnabled_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 13),
    _LispFeaturesEtrAcceptMapDataEnabled_Type()
)
lispFeaturesEtrAcceptMapDataEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesEtrAcceptMapDataEnabled.setStatus("current")
_LispFeaturesEtrAcceptMapDataVerifyEnabled_Type = TruthValue
_LispFeaturesEtrAcceptMapDataVerifyEnabled_Object = MibTableColumn
lispFeaturesEtrAcceptMapDataVerifyEnabled = _LispFeaturesEtrAcceptMapDataVerifyEnabled_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 14),
    _LispFeaturesEtrAcceptMapDataVerifyEnabled_Type()
)
lispFeaturesEtrAcceptMapDataVerifyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesEtrAcceptMapDataVerifyEnabled.setStatus("current")


class _LispFeaturesRouterTimeStamp_Type(TimeStamp):
    """Custom type lispFeaturesRouterTimeStamp based on TimeStamp"""
    defaultValue = 0


_LispFeaturesRouterTimeStamp_Object = MibTableColumn
lispFeaturesRouterTimeStamp = _LispFeaturesRouterTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 1, 1, 15),
    _LispFeaturesRouterTimeStamp_Type()
)
lispFeaturesRouterTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispFeaturesRouterTimeStamp.setStatus("current")
_LispIidToVrfTable_Object = MibTable
lispIidToVrfTable = _LispIidToVrfTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 2)
)
if mibBuilder.loadTexts:
    lispIidToVrfTable.setStatus("current")
_LispIidToVrfEntry_Object = MibTableRow
lispIidToVrfEntry = _LispIidToVrfEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 2, 1)
)
lispIidToVrfEntry.setIndexNames(
    (0, "LISP-MIB", "lispFeaturesInstanceID"),
)
if mibBuilder.loadTexts:
    lispIidToVrfEntry.setStatus("current")
_LispIidToVrfName_Type = MplsL3VpnName
_LispIidToVrfName_Object = MibTableColumn
lispIidToVrfName = _LispIidToVrfName_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 2, 1, 1),
    _LispIidToVrfName_Type()
)
lispIidToVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispIidToVrfName.setStatus("current")
_LispGlobalStatsTable_Object = MibTable
lispGlobalStatsTable = _LispGlobalStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 3)
)
if mibBuilder.loadTexts:
    lispGlobalStatsTable.setStatus("current")
_LispGlobalStatsEntry_Object = MibTableRow
lispGlobalStatsEntry = _LispGlobalStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 3, 1)
)
lispGlobalStatsEntry.setIndexNames(
    (0, "LISP-MIB", "lispFeaturesInstanceID"),
    (0, "LISP-MIB", "lispFeaturesAddressFamily"),
)
if mibBuilder.loadTexts:
    lispGlobalStatsEntry.setStatus("current")
_LispGlobalStatsMapRequestsIn_Type = Counter64
_LispGlobalStatsMapRequestsIn_Object = MibTableColumn
lispGlobalStatsMapRequestsIn = _LispGlobalStatsMapRequestsIn_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 3, 1, 1),
    _LispGlobalStatsMapRequestsIn_Type()
)
lispGlobalStatsMapRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispGlobalStatsMapRequestsIn.setStatus("current")
_LispGlobalStatsMapRequestsOut_Type = Counter64
_LispGlobalStatsMapRequestsOut_Object = MibTableColumn
lispGlobalStatsMapRequestsOut = _LispGlobalStatsMapRequestsOut_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 3, 1, 2),
    _LispGlobalStatsMapRequestsOut_Type()
)
lispGlobalStatsMapRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispGlobalStatsMapRequestsOut.setStatus("current")
_LispGlobalStatsMapRepliesIn_Type = Counter64
_LispGlobalStatsMapRepliesIn_Object = MibTableColumn
lispGlobalStatsMapRepliesIn = _LispGlobalStatsMapRepliesIn_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 3, 1, 3),
    _LispGlobalStatsMapRepliesIn_Type()
)
lispGlobalStatsMapRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispGlobalStatsMapRepliesIn.setStatus("current")
_LispGlobalStatsMapRepliesOut_Type = Counter64
_LispGlobalStatsMapRepliesOut_Object = MibTableColumn
lispGlobalStatsMapRepliesOut = _LispGlobalStatsMapRepliesOut_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 3, 1, 4),
    _LispGlobalStatsMapRepliesOut_Type()
)
lispGlobalStatsMapRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispGlobalStatsMapRepliesOut.setStatus("current")
_LispGlobalStatsMapRegistersIn_Type = Counter64
_LispGlobalStatsMapRegistersIn_Object = MibTableColumn
lispGlobalStatsMapRegistersIn = _LispGlobalStatsMapRegistersIn_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 3, 1, 5),
    _LispGlobalStatsMapRegistersIn_Type()
)
lispGlobalStatsMapRegistersIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispGlobalStatsMapRegistersIn.setStatus("current")
_LispGlobalStatsMapRegistersOut_Type = Counter64
_LispGlobalStatsMapRegistersOut_Object = MibTableColumn
lispGlobalStatsMapRegistersOut = _LispGlobalStatsMapRegistersOut_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 3, 1, 6),
    _LispGlobalStatsMapRegistersOut_Type()
)
lispGlobalStatsMapRegistersOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispGlobalStatsMapRegistersOut.setStatus("current")
_LispMappingDatabaseTable_Object = MibTable
lispMappingDatabaseTable = _LispMappingDatabaseTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4)
)
if mibBuilder.loadTexts:
    lispMappingDatabaseTable.setStatus("current")
_LispMappingDatabaseEntry_Object = MibTableRow
lispMappingDatabaseEntry = _LispMappingDatabaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1)
)
lispMappingDatabaseEntry.setIndexNames(
    (0, "LISP-MIB", "lispMappingDatabaseEidLength"),
    (0, "LISP-MIB", "lispMappingDatabaseEid"),
)
if mibBuilder.loadTexts:
    lispMappingDatabaseEntry.setStatus("current")


class _LispMappingDatabaseEidLength_Type(Integer32):
    """Custom type lispMappingDatabaseEidLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispMappingDatabaseEidLength_Type.__name__ = "Integer32"
_LispMappingDatabaseEidLength_Object = MibTableColumn
lispMappingDatabaseEidLength = _LispMappingDatabaseEidLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1, 1),
    _LispMappingDatabaseEidLength_Type()
)
lispMappingDatabaseEidLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispMappingDatabaseEidLength.setStatus("current")
_LispMappingDatabaseEid_Type = LispAddressType
_LispMappingDatabaseEid_Object = MibTableColumn
lispMappingDatabaseEid = _LispMappingDatabaseEid_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1, 2),
    _LispMappingDatabaseEid_Type()
)
lispMappingDatabaseEid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispMappingDatabaseEid.setStatus("current")


class _LispMappingDatabaseLsb_Type(Unsigned32):
    """Custom type lispMappingDatabaseLsb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LispMappingDatabaseLsb_Type.__name__ = "Unsigned32"
_LispMappingDatabaseLsb_Object = MibTableColumn
lispMappingDatabaseLsb = _LispMappingDatabaseLsb_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1, 3),
    _LispMappingDatabaseLsb_Type()
)
lispMappingDatabaseLsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLsb.setStatus("current")
_LispMappingDatabaseEidPartitioned_Type = TruthValue
_LispMappingDatabaseEidPartitioned_Object = MibTableColumn
lispMappingDatabaseEidPartitioned = _LispMappingDatabaseEidPartitioned_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1, 4),
    _LispMappingDatabaseEidPartitioned_Type()
)
lispMappingDatabaseEidPartitioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseEidPartitioned.setStatus("current")


class _LispMappingDatabaseTimeStamp_Type(TimeStamp):
    """Custom type lispMappingDatabaseTimeStamp based on TimeStamp"""
    defaultValue = 0


_LispMappingDatabaseTimeStamp_Object = MibTableColumn
lispMappingDatabaseTimeStamp = _LispMappingDatabaseTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1, 5),
    _LispMappingDatabaseTimeStamp_Type()
)
lispMappingDatabaseTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseTimeStamp.setStatus("current")
_LispMappingDatabaseDecapOctets_Type = Counter64
_LispMappingDatabaseDecapOctets_Object = MibTableColumn
lispMappingDatabaseDecapOctets = _LispMappingDatabaseDecapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1, 6),
    _LispMappingDatabaseDecapOctets_Type()
)
lispMappingDatabaseDecapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseDecapOctets.setStatus("current")
_LispMappingDatabaseDecapPackets_Type = Counter64
_LispMappingDatabaseDecapPackets_Object = MibTableColumn
lispMappingDatabaseDecapPackets = _LispMappingDatabaseDecapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1, 7),
    _LispMappingDatabaseDecapPackets_Type()
)
lispMappingDatabaseDecapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseDecapPackets.setStatus("current")
_LispMappingDatabaseEncapOctets_Type = Counter64
_LispMappingDatabaseEncapOctets_Object = MibTableColumn
lispMappingDatabaseEncapOctets = _LispMappingDatabaseEncapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1, 8),
    _LispMappingDatabaseEncapOctets_Type()
)
lispMappingDatabaseEncapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseEncapOctets.setStatus("current")
_LispMappingDatabaseEncapPackets_Type = Counter64
_LispMappingDatabaseEncapPackets_Object = MibTableColumn
lispMappingDatabaseEncapPackets = _LispMappingDatabaseEncapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 4, 1, 9),
    _LispMappingDatabaseEncapPackets_Type()
)
lispMappingDatabaseEncapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseEncapPackets.setStatus("current")
_LispMappingDatabaseLocatorTable_Object = MibTable
lispMappingDatabaseLocatorTable = _LispMappingDatabaseLocatorTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5)
)
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorTable.setStatus("current")
_LispMappingDatabaseLocatorEntry_Object = MibTableRow
lispMappingDatabaseLocatorEntry = _LispMappingDatabaseLocatorEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1)
)
lispMappingDatabaseLocatorEntry.setIndexNames(
    (0, "LISP-MIB", "lispMappingDatabaseEidLength"),
    (0, "LISP-MIB", "lispMappingDatabaseEid"),
    (0, "LISP-MIB", "lispMappingDatabaseLocatorRlocLength"),
    (0, "LISP-MIB", "lispMappingDatabaseLocatorRloc"),
)
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorEntry.setStatus("current")


class _LispMappingDatabaseLocatorRlocLength_Type(Integer32):
    """Custom type lispMappingDatabaseLocatorRlocLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispMappingDatabaseLocatorRlocLength_Type.__name__ = "Integer32"
_LispMappingDatabaseLocatorRlocLength_Object = MibTableColumn
lispMappingDatabaseLocatorRlocLength = _LispMappingDatabaseLocatorRlocLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 1),
    _LispMappingDatabaseLocatorRlocLength_Type()
)
lispMappingDatabaseLocatorRlocLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocLength.setStatus("current")
_LispMappingDatabaseLocatorRloc_Type = LispAddressType
_LispMappingDatabaseLocatorRloc_Object = MibTableColumn
lispMappingDatabaseLocatorRloc = _LispMappingDatabaseLocatorRloc_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 2),
    _LispMappingDatabaseLocatorRloc_Type()
)
lispMappingDatabaseLocatorRloc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRloc.setStatus("current")


class _LispMappingDatabaseLocatorRlocPriority_Type(Integer32):
    """Custom type lispMappingDatabaseLocatorRlocPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LispMappingDatabaseLocatorRlocPriority_Type.__name__ = "Integer32"
_LispMappingDatabaseLocatorRlocPriority_Object = MibTableColumn
lispMappingDatabaseLocatorRlocPriority = _LispMappingDatabaseLocatorRlocPriority_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 3),
    _LispMappingDatabaseLocatorRlocPriority_Type()
)
lispMappingDatabaseLocatorRlocPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocPriority.setStatus("current")


class _LispMappingDatabaseLocatorRlocWeight_Type(Integer32):
    """Custom type lispMappingDatabaseLocatorRlocWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LispMappingDatabaseLocatorRlocWeight_Type.__name__ = "Integer32"
_LispMappingDatabaseLocatorRlocWeight_Object = MibTableColumn
lispMappingDatabaseLocatorRlocWeight = _LispMappingDatabaseLocatorRlocWeight_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 4),
    _LispMappingDatabaseLocatorRlocWeight_Type()
)
lispMappingDatabaseLocatorRlocWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocWeight.setStatus("current")


class _LispMappingDatabaseLocatorRlocMPriority_Type(Integer32):
    """Custom type lispMappingDatabaseLocatorRlocMPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LispMappingDatabaseLocatorRlocMPriority_Type.__name__ = "Integer32"
_LispMappingDatabaseLocatorRlocMPriority_Object = MibTableColumn
lispMappingDatabaseLocatorRlocMPriority = _LispMappingDatabaseLocatorRlocMPriority_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 5),
    _LispMappingDatabaseLocatorRlocMPriority_Type()
)
lispMappingDatabaseLocatorRlocMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocMPriority.setStatus("current")


class _LispMappingDatabaseLocatorRlocMWeight_Type(Integer32):
    """Custom type lispMappingDatabaseLocatorRlocMWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LispMappingDatabaseLocatorRlocMWeight_Type.__name__ = "Integer32"
_LispMappingDatabaseLocatorRlocMWeight_Object = MibTableColumn
lispMappingDatabaseLocatorRlocMWeight = _LispMappingDatabaseLocatorRlocMWeight_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 6),
    _LispMappingDatabaseLocatorRlocMWeight_Type()
)
lispMappingDatabaseLocatorRlocMWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocMWeight.setStatus("current")


class _LispMappingDatabaseLocatorRlocState_Type(Integer32):
    """Custom type lispMappingDatabaseLocatorRlocState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unreachable", 3),
          ("up", 1))
    )


_LispMappingDatabaseLocatorRlocState_Type.__name__ = "Integer32"
_LispMappingDatabaseLocatorRlocState_Object = MibTableColumn
lispMappingDatabaseLocatorRlocState = _LispMappingDatabaseLocatorRlocState_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 7),
    _LispMappingDatabaseLocatorRlocState_Type()
)
lispMappingDatabaseLocatorRlocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocState.setStatus("current")


class _LispMappingDatabaseLocatorRlocLocal_Type(Integer32):
    """Custom type lispMappingDatabaseLocatorRlocLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sitelocal", 2),
          ("siteself", 1))
    )


_LispMappingDatabaseLocatorRlocLocal_Type.__name__ = "Integer32"
_LispMappingDatabaseLocatorRlocLocal_Object = MibTableColumn
lispMappingDatabaseLocatorRlocLocal = _LispMappingDatabaseLocatorRlocLocal_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 8),
    _LispMappingDatabaseLocatorRlocLocal_Type()
)
lispMappingDatabaseLocatorRlocLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocLocal.setStatus("current")


class _LispMappingDatabaseLocatorRlocTimeStamp_Type(TimeStamp):
    """Custom type lispMappingDatabaseLocatorRlocTimeStamp based on TimeStamp"""
    defaultValue = 0


_LispMappingDatabaseLocatorRlocTimeStamp_Object = MibTableColumn
lispMappingDatabaseLocatorRlocTimeStamp = _LispMappingDatabaseLocatorRlocTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 9),
    _LispMappingDatabaseLocatorRlocTimeStamp_Type()
)
lispMappingDatabaseLocatorRlocTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocTimeStamp.setStatus("current")
_LispMappingDatabaseLocatorRlocDecapOctets_Type = Counter64
_LispMappingDatabaseLocatorRlocDecapOctets_Object = MibTableColumn
lispMappingDatabaseLocatorRlocDecapOctets = _LispMappingDatabaseLocatorRlocDecapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 10),
    _LispMappingDatabaseLocatorRlocDecapOctets_Type()
)
lispMappingDatabaseLocatorRlocDecapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocDecapOctets.setStatus("current")
_LispMappingDatabaseLocatorRlocDecapPackets_Type = Counter64
_LispMappingDatabaseLocatorRlocDecapPackets_Object = MibTableColumn
lispMappingDatabaseLocatorRlocDecapPackets = _LispMappingDatabaseLocatorRlocDecapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 11),
    _LispMappingDatabaseLocatorRlocDecapPackets_Type()
)
lispMappingDatabaseLocatorRlocDecapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocDecapPackets.setStatus("current")
_LispMappingDatabaseLocatorRlocEncapOctets_Type = Counter64
_LispMappingDatabaseLocatorRlocEncapOctets_Object = MibTableColumn
lispMappingDatabaseLocatorRlocEncapOctets = _LispMappingDatabaseLocatorRlocEncapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 12),
    _LispMappingDatabaseLocatorRlocEncapOctets_Type()
)
lispMappingDatabaseLocatorRlocEncapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocEncapOctets.setStatus("current")
_LispMappingDatabaseLocatorRlocEncapPackets_Type = Counter64
_LispMappingDatabaseLocatorRlocEncapPackets_Object = MibTableColumn
lispMappingDatabaseLocatorRlocEncapPackets = _LispMappingDatabaseLocatorRlocEncapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 5, 1, 13),
    _LispMappingDatabaseLocatorRlocEncapPackets_Type()
)
lispMappingDatabaseLocatorRlocEncapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMappingDatabaseLocatorRlocEncapPackets.setStatus("current")
_LispMapCacheTable_Object = MibTable
lispMapCacheTable = _LispMapCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6)
)
if mibBuilder.loadTexts:
    lispMapCacheTable.setStatus("current")
_LispMapCacheEntry_Object = MibTableRow
lispMapCacheEntry = _LispMapCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1)
)
lispMapCacheEntry.setIndexNames(
    (0, "LISP-MIB", "lispMapCacheEidLength"),
    (0, "LISP-MIB", "lispMapCacheEid"),
)
if mibBuilder.loadTexts:
    lispMapCacheEntry.setStatus("current")


class _LispMapCacheEidLength_Type(Integer32):
    """Custom type lispMapCacheEidLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispMapCacheEidLength_Type.__name__ = "Integer32"
_LispMapCacheEidLength_Object = MibTableColumn
lispMapCacheEidLength = _LispMapCacheEidLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 1),
    _LispMapCacheEidLength_Type()
)
lispMapCacheEidLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispMapCacheEidLength.setStatus("current")
_LispMapCacheEid_Type = LispAddressType
_LispMapCacheEid_Object = MibTableColumn
lispMapCacheEid = _LispMapCacheEid_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 2),
    _LispMapCacheEid_Type()
)
lispMapCacheEid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispMapCacheEid.setStatus("current")


class _LispMapCacheEidTimeStamp_Type(TimeStamp):
    """Custom type lispMapCacheEidTimeStamp based on TimeStamp"""
    defaultValue = 0


_LispMapCacheEidTimeStamp_Object = MibTableColumn
lispMapCacheEidTimeStamp = _LispMapCacheEidTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 3),
    _LispMapCacheEidTimeStamp_Type()
)
lispMapCacheEidTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheEidTimeStamp.setStatus("current")
_LispMapCacheEidExpiryTime_Type = TimeTicks
_LispMapCacheEidExpiryTime_Object = MibTableColumn
lispMapCacheEidExpiryTime = _LispMapCacheEidExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 4),
    _LispMapCacheEidExpiryTime_Type()
)
lispMapCacheEidExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheEidExpiryTime.setStatus("current")
_LispMapCacheEidState_Type = TruthValue
_LispMapCacheEidState_Object = MibTableColumn
lispMapCacheEidState = _LispMapCacheEidState_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 5),
    _LispMapCacheEidState_Type()
)
lispMapCacheEidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheEidState.setStatus("current")
_LispMapCacheEidAuthoritative_Type = TruthValue
_LispMapCacheEidAuthoritative_Object = MibTableColumn
lispMapCacheEidAuthoritative = _LispMapCacheEidAuthoritative_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 6),
    _LispMapCacheEidAuthoritative_Type()
)
lispMapCacheEidAuthoritative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheEidAuthoritative.setStatus("current")
_LispMapCacheEidDecapOctets_Type = Counter64
_LispMapCacheEidDecapOctets_Object = MibTableColumn
lispMapCacheEidDecapOctets = _LispMapCacheEidDecapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 7),
    _LispMapCacheEidDecapOctets_Type()
)
lispMapCacheEidDecapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheEidDecapOctets.setStatus("current")
_LispMapCacheEidDecapPackets_Type = Counter64
_LispMapCacheEidDecapPackets_Object = MibTableColumn
lispMapCacheEidDecapPackets = _LispMapCacheEidDecapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 8),
    _LispMapCacheEidDecapPackets_Type()
)
lispMapCacheEidDecapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheEidDecapPackets.setStatus("current")
_LispMapCacheEidEncapOctets_Type = Counter64
_LispMapCacheEidEncapOctets_Object = MibTableColumn
lispMapCacheEidEncapOctets = _LispMapCacheEidEncapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 9),
    _LispMapCacheEidEncapOctets_Type()
)
lispMapCacheEidEncapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheEidEncapOctets.setStatus("current")
_LispMapCacheEidEncapPackets_Type = Counter64
_LispMapCacheEidEncapPackets_Object = MibTableColumn
lispMapCacheEidEncapPackets = _LispMapCacheEidEncapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 6, 1, 10),
    _LispMapCacheEidEncapPackets_Type()
)
lispMapCacheEidEncapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheEidEncapPackets.setStatus("current")
_LispMapCacheLocatorTable_Object = MibTable
lispMapCacheLocatorTable = _LispMapCacheLocatorTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7)
)
if mibBuilder.loadTexts:
    lispMapCacheLocatorTable.setStatus("current")
_LispMapCacheLocatorEntry_Object = MibTableRow
lispMapCacheLocatorEntry = _LispMapCacheLocatorEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1)
)
lispMapCacheLocatorEntry.setIndexNames(
    (0, "LISP-MIB", "lispMapCacheEidLength"),
    (0, "LISP-MIB", "lispMapCacheEid"),
    (0, "LISP-MIB", "lispMapCacheLocatorRlocLength"),
    (0, "LISP-MIB", "lispMapCacheLocatorRloc"),
)
if mibBuilder.loadTexts:
    lispMapCacheLocatorEntry.setStatus("current")


class _LispMapCacheLocatorRlocLength_Type(Integer32):
    """Custom type lispMapCacheLocatorRlocLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispMapCacheLocatorRlocLength_Type.__name__ = "Integer32"
_LispMapCacheLocatorRlocLength_Object = MibTableColumn
lispMapCacheLocatorRlocLength = _LispMapCacheLocatorRlocLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 1),
    _LispMapCacheLocatorRlocLength_Type()
)
lispMapCacheLocatorRlocLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocLength.setStatus("current")
_LispMapCacheLocatorRloc_Type = LispAddressType
_LispMapCacheLocatorRloc_Object = MibTableColumn
lispMapCacheLocatorRloc = _LispMapCacheLocatorRloc_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 2),
    _LispMapCacheLocatorRloc_Type()
)
lispMapCacheLocatorRloc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRloc.setStatus("current")


class _LispMapCacheLocatorRlocPriority_Type(Integer32):
    """Custom type lispMapCacheLocatorRlocPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LispMapCacheLocatorRlocPriority_Type.__name__ = "Integer32"
_LispMapCacheLocatorRlocPriority_Object = MibTableColumn
lispMapCacheLocatorRlocPriority = _LispMapCacheLocatorRlocPriority_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 3),
    _LispMapCacheLocatorRlocPriority_Type()
)
lispMapCacheLocatorRlocPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocPriority.setStatus("current")


class _LispMapCacheLocatorRlocWeight_Type(Integer32):
    """Custom type lispMapCacheLocatorRlocWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LispMapCacheLocatorRlocWeight_Type.__name__ = "Integer32"
_LispMapCacheLocatorRlocWeight_Object = MibTableColumn
lispMapCacheLocatorRlocWeight = _LispMapCacheLocatorRlocWeight_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 4),
    _LispMapCacheLocatorRlocWeight_Type()
)
lispMapCacheLocatorRlocWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocWeight.setStatus("current")


class _LispMapCacheLocatorRlocMPriority_Type(Integer32):
    """Custom type lispMapCacheLocatorRlocMPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LispMapCacheLocatorRlocMPriority_Type.__name__ = "Integer32"
_LispMapCacheLocatorRlocMPriority_Object = MibTableColumn
lispMapCacheLocatorRlocMPriority = _LispMapCacheLocatorRlocMPriority_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 5),
    _LispMapCacheLocatorRlocMPriority_Type()
)
lispMapCacheLocatorRlocMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocMPriority.setStatus("current")


class _LispMapCacheLocatorRlocMWeight_Type(Integer32):
    """Custom type lispMapCacheLocatorRlocMWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LispMapCacheLocatorRlocMWeight_Type.__name__ = "Integer32"
_LispMapCacheLocatorRlocMWeight_Object = MibTableColumn
lispMapCacheLocatorRlocMWeight = _LispMapCacheLocatorRlocMWeight_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 6),
    _LispMapCacheLocatorRlocMWeight_Type()
)
lispMapCacheLocatorRlocMWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocMWeight.setStatus("current")


class _LispMapCacheLocatorRlocState_Type(Integer32):
    """Custom type lispMapCacheLocatorRlocState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unreachable", 3),
          ("up", 1))
    )


_LispMapCacheLocatorRlocState_Type.__name__ = "Integer32"
_LispMapCacheLocatorRlocState_Object = MibTableColumn
lispMapCacheLocatorRlocState = _LispMapCacheLocatorRlocState_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 7),
    _LispMapCacheLocatorRlocState_Type()
)
lispMapCacheLocatorRlocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocState.setStatus("current")


class _LispMapCacheLocatorRlocTimeStamp_Type(TimeStamp):
    """Custom type lispMapCacheLocatorRlocTimeStamp based on TimeStamp"""
    defaultValue = 0


_LispMapCacheLocatorRlocTimeStamp_Object = MibTableColumn
lispMapCacheLocatorRlocTimeStamp = _LispMapCacheLocatorRlocTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 8),
    _LispMapCacheLocatorRlocTimeStamp_Type()
)
lispMapCacheLocatorRlocTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocTimeStamp.setStatus("current")
_LispMapCacheLocatorRlocLastPriorityChange_Type = TimeTicks
_LispMapCacheLocatorRlocLastPriorityChange_Object = MibTableColumn
lispMapCacheLocatorRlocLastPriorityChange = _LispMapCacheLocatorRlocLastPriorityChange_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 9),
    _LispMapCacheLocatorRlocLastPriorityChange_Type()
)
lispMapCacheLocatorRlocLastPriorityChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocLastPriorityChange.setStatus("current")
_LispMapCacheLocatorRlocLastWeightChange_Type = TimeTicks
_LispMapCacheLocatorRlocLastWeightChange_Object = MibTableColumn
lispMapCacheLocatorRlocLastWeightChange = _LispMapCacheLocatorRlocLastWeightChange_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 10),
    _LispMapCacheLocatorRlocLastWeightChange_Type()
)
lispMapCacheLocatorRlocLastWeightChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocLastWeightChange.setStatus("current")
_LispMapCacheLocatorRlocLastMPriorityChange_Type = TimeTicks
_LispMapCacheLocatorRlocLastMPriorityChange_Object = MibTableColumn
lispMapCacheLocatorRlocLastMPriorityChange = _LispMapCacheLocatorRlocLastMPriorityChange_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 11),
    _LispMapCacheLocatorRlocLastMPriorityChange_Type()
)
lispMapCacheLocatorRlocLastMPriorityChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocLastMPriorityChange.setStatus("current")
_LispMapCacheLocatorRlocLastMWeightChange_Type = TimeTicks
_LispMapCacheLocatorRlocLastMWeightChange_Object = MibTableColumn
lispMapCacheLocatorRlocLastMWeightChange = _LispMapCacheLocatorRlocLastMWeightChange_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 12),
    _LispMapCacheLocatorRlocLastMWeightChange_Type()
)
lispMapCacheLocatorRlocLastMWeightChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocLastMWeightChange.setStatus("current")
_LispMapCacheLocatorRlocLastStateChange_Type = TimeTicks
_LispMapCacheLocatorRlocLastStateChange_Object = MibTableColumn
lispMapCacheLocatorRlocLastStateChange = _LispMapCacheLocatorRlocLastStateChange_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 13),
    _LispMapCacheLocatorRlocLastStateChange_Type()
)
lispMapCacheLocatorRlocLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocLastStateChange.setStatus("current")
_LispMapCacheLocatorRlocRtt_Type = TimeTicks
_LispMapCacheLocatorRlocRtt_Object = MibTableColumn
lispMapCacheLocatorRlocRtt = _LispMapCacheLocatorRlocRtt_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 14),
    _LispMapCacheLocatorRlocRtt_Type()
)
lispMapCacheLocatorRlocRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocRtt.setStatus("current")
_LispMapCacheLocatorRlocDecapOctets_Type = Counter64
_LispMapCacheLocatorRlocDecapOctets_Object = MibTableColumn
lispMapCacheLocatorRlocDecapOctets = _LispMapCacheLocatorRlocDecapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 15),
    _LispMapCacheLocatorRlocDecapOctets_Type()
)
lispMapCacheLocatorRlocDecapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocDecapOctets.setStatus("current")
_LispMapCacheLocatorRlocDecapPackets_Type = Counter64
_LispMapCacheLocatorRlocDecapPackets_Object = MibTableColumn
lispMapCacheLocatorRlocDecapPackets = _LispMapCacheLocatorRlocDecapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 16),
    _LispMapCacheLocatorRlocDecapPackets_Type()
)
lispMapCacheLocatorRlocDecapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocDecapPackets.setStatus("current")
_LispMapCacheLocatorRlocEncapOctets_Type = Counter64
_LispMapCacheLocatorRlocEncapOctets_Object = MibTableColumn
lispMapCacheLocatorRlocEncapOctets = _LispMapCacheLocatorRlocEncapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 17),
    _LispMapCacheLocatorRlocEncapOctets_Type()
)
lispMapCacheLocatorRlocEncapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocEncapOctets.setStatus("current")
_LispMapCacheLocatorRlocEncapPackets_Type = Counter64
_LispMapCacheLocatorRlocEncapPackets_Object = MibTableColumn
lispMapCacheLocatorRlocEncapPackets = _LispMapCacheLocatorRlocEncapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 7, 1, 18),
    _LispMapCacheLocatorRlocEncapPackets_Type()
)
lispMapCacheLocatorRlocEncapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispMapCacheLocatorRlocEncapPackets.setStatus("current")
_LispConfiguredLocatorTable_Object = MibTable
lispConfiguredLocatorTable = _LispConfiguredLocatorTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8)
)
if mibBuilder.loadTexts:
    lispConfiguredLocatorTable.setStatus("current")
_LispConfiguredLocatorEntry_Object = MibTableRow
lispConfiguredLocatorEntry = _LispConfiguredLocatorEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1)
)
lispConfiguredLocatorEntry.setIndexNames(
    (0, "LISP-MIB", "lispConfiguredLocatorRlocLength"),
    (0, "LISP-MIB", "lispConfiguredLocatorRloc"),
)
if mibBuilder.loadTexts:
    lispConfiguredLocatorEntry.setStatus("current")


class _LispConfiguredLocatorRlocLength_Type(Integer32):
    """Custom type lispConfiguredLocatorRlocLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispConfiguredLocatorRlocLength_Type.__name__ = "Integer32"
_LispConfiguredLocatorRlocLength_Object = MibTableColumn
lispConfiguredLocatorRlocLength = _LispConfiguredLocatorRlocLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1, 1),
    _LispConfiguredLocatorRlocLength_Type()
)
lispConfiguredLocatorRlocLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispConfiguredLocatorRlocLength.setStatus("current")
_LispConfiguredLocatorRloc_Type = LispAddressType
_LispConfiguredLocatorRloc_Object = MibTableColumn
lispConfiguredLocatorRloc = _LispConfiguredLocatorRloc_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1, 2),
    _LispConfiguredLocatorRloc_Type()
)
lispConfiguredLocatorRloc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispConfiguredLocatorRloc.setStatus("current")


class _LispConfiguredLocatorRlocState_Type(Integer32):
    """Custom type lispConfiguredLocatorRlocState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unreachable", 3),
          ("up", 1))
    )


_LispConfiguredLocatorRlocState_Type.__name__ = "Integer32"
_LispConfiguredLocatorRlocState_Object = MibTableColumn
lispConfiguredLocatorRlocState = _LispConfiguredLocatorRlocState_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1, 3),
    _LispConfiguredLocatorRlocState_Type()
)
lispConfiguredLocatorRlocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispConfiguredLocatorRlocState.setStatus("current")


class _LispConfiguredLocatorRlocLocal_Type(Integer32):
    """Custom type lispConfiguredLocatorRlocLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sitelocal", 2),
          ("siteself", 1))
    )


_LispConfiguredLocatorRlocLocal_Type.__name__ = "Integer32"
_LispConfiguredLocatorRlocLocal_Object = MibTableColumn
lispConfiguredLocatorRlocLocal = _LispConfiguredLocatorRlocLocal_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1, 4),
    _LispConfiguredLocatorRlocLocal_Type()
)
lispConfiguredLocatorRlocLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispConfiguredLocatorRlocLocal.setStatus("current")


class _LispConfiguredLocatorRlocTimeStamp_Type(TimeStamp):
    """Custom type lispConfiguredLocatorRlocTimeStamp based on TimeStamp"""
    defaultValue = 0


_LispConfiguredLocatorRlocTimeStamp_Object = MibTableColumn
lispConfiguredLocatorRlocTimeStamp = _LispConfiguredLocatorRlocTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1, 5),
    _LispConfiguredLocatorRlocTimeStamp_Type()
)
lispConfiguredLocatorRlocTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispConfiguredLocatorRlocTimeStamp.setStatus("current")
_LispConfiguredLocatorRlocDecapOctets_Type = Counter64
_LispConfiguredLocatorRlocDecapOctets_Object = MibTableColumn
lispConfiguredLocatorRlocDecapOctets = _LispConfiguredLocatorRlocDecapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1, 6),
    _LispConfiguredLocatorRlocDecapOctets_Type()
)
lispConfiguredLocatorRlocDecapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispConfiguredLocatorRlocDecapOctets.setStatus("current")
_LispConfiguredLocatorRlocDecapPackets_Type = Counter64
_LispConfiguredLocatorRlocDecapPackets_Object = MibTableColumn
lispConfiguredLocatorRlocDecapPackets = _LispConfiguredLocatorRlocDecapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1, 7),
    _LispConfiguredLocatorRlocDecapPackets_Type()
)
lispConfiguredLocatorRlocDecapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispConfiguredLocatorRlocDecapPackets.setStatus("current")
_LispConfiguredLocatorRlocEncapOctets_Type = Counter64
_LispConfiguredLocatorRlocEncapOctets_Object = MibTableColumn
lispConfiguredLocatorRlocEncapOctets = _LispConfiguredLocatorRlocEncapOctets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1, 8),
    _LispConfiguredLocatorRlocEncapOctets_Type()
)
lispConfiguredLocatorRlocEncapOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispConfiguredLocatorRlocEncapOctets.setStatus("current")
_LispConfiguredLocatorRlocEncapPackets_Type = Counter64
_LispConfiguredLocatorRlocEncapPackets_Object = MibTableColumn
lispConfiguredLocatorRlocEncapPackets = _LispConfiguredLocatorRlocEncapPackets_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 8, 1, 9),
    _LispConfiguredLocatorRlocEncapPackets_Type()
)
lispConfiguredLocatorRlocEncapPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispConfiguredLocatorRlocEncapPackets.setStatus("current")
_LispEidRegistrationTable_Object = MibTable
lispEidRegistrationTable = _LispEidRegistrationTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9)
)
if mibBuilder.loadTexts:
    lispEidRegistrationTable.setStatus("current")
_LispEidRegistrationEntry_Object = MibTableRow
lispEidRegistrationEntry = _LispEidRegistrationEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1)
)
lispEidRegistrationEntry.setIndexNames(
    (0, "LISP-MIB", "lispEidRegistrationEidLength"),
    (0, "LISP-MIB", "lispEidRegistrationEid"),
)
if mibBuilder.loadTexts:
    lispEidRegistrationEntry.setStatus("current")


class _LispEidRegistrationEidLength_Type(Integer32):
    """Custom type lispEidRegistrationEidLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispEidRegistrationEidLength_Type.__name__ = "Integer32"
_LispEidRegistrationEidLength_Object = MibTableColumn
lispEidRegistrationEidLength = _LispEidRegistrationEidLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 1),
    _LispEidRegistrationEidLength_Type()
)
lispEidRegistrationEidLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispEidRegistrationEidLength.setStatus("current")
_LispEidRegistrationEid_Type = LispAddressType
_LispEidRegistrationEid_Object = MibTableColumn
lispEidRegistrationEid = _LispEidRegistrationEid_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 2),
    _LispEidRegistrationEid_Type()
)
lispEidRegistrationEid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispEidRegistrationEid.setStatus("current")


class _LispEidRegistrationSiteName_Type(OctetString):
    """Custom type lispEidRegistrationSiteName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LispEidRegistrationSiteName_Type.__name__ = "OctetString"
_LispEidRegistrationSiteName_Object = MibTableColumn
lispEidRegistrationSiteName = _LispEidRegistrationSiteName_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 3),
    _LispEidRegistrationSiteName_Type()
)
lispEidRegistrationSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationSiteName.setStatus("current")


class _LispEidRegistrationSiteDescription_Type(OctetString):
    """Custom type lispEidRegistrationSiteDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LispEidRegistrationSiteDescription_Type.__name__ = "OctetString"
_LispEidRegistrationSiteDescription_Object = MibTableColumn
lispEidRegistrationSiteDescription = _LispEidRegistrationSiteDescription_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 4),
    _LispEidRegistrationSiteDescription_Type()
)
lispEidRegistrationSiteDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationSiteDescription.setStatus("current")
_LispEidRegistrationIsRegistered_Type = TruthValue
_LispEidRegistrationIsRegistered_Object = MibTableColumn
lispEidRegistrationIsRegistered = _LispEidRegistrationIsRegistered_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 5),
    _LispEidRegistrationIsRegistered_Type()
)
lispEidRegistrationIsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationIsRegistered.setStatus("current")


class _LispEidRegistrationFirstTimeStamp_Type(TimeStamp):
    """Custom type lispEidRegistrationFirstTimeStamp based on TimeStamp"""
    defaultValue = 0


_LispEidRegistrationFirstTimeStamp_Object = MibTableColumn
lispEidRegistrationFirstTimeStamp = _LispEidRegistrationFirstTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 6),
    _LispEidRegistrationFirstTimeStamp_Type()
)
lispEidRegistrationFirstTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationFirstTimeStamp.setStatus("current")


class _LispEidRegistrationLastTimeStamp_Type(TimeStamp):
    """Custom type lispEidRegistrationLastTimeStamp based on TimeStamp"""
    defaultValue = 0


_LispEidRegistrationLastTimeStamp_Object = MibTableColumn
lispEidRegistrationLastTimeStamp = _LispEidRegistrationLastTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 7),
    _LispEidRegistrationLastTimeStamp_Type()
)
lispEidRegistrationLastTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationLastTimeStamp.setStatus("current")


class _LispEidRegistrationLastRegisterSenderLength_Type(Integer32):
    """Custom type lispEidRegistrationLastRegisterSenderLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispEidRegistrationLastRegisterSenderLength_Type.__name__ = "Integer32"
_LispEidRegistrationLastRegisterSenderLength_Object = MibTableColumn
lispEidRegistrationLastRegisterSenderLength = _LispEidRegistrationLastRegisterSenderLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 8),
    _LispEidRegistrationLastRegisterSenderLength_Type()
)
lispEidRegistrationLastRegisterSenderLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationLastRegisterSenderLength.setStatus("current")
_LispEidRegistrationLastRegisterSender_Type = LispAddressType
_LispEidRegistrationLastRegisterSender_Object = MibTableColumn
lispEidRegistrationLastRegisterSender = _LispEidRegistrationLastRegisterSender_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 9),
    _LispEidRegistrationLastRegisterSender_Type()
)
lispEidRegistrationLastRegisterSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationLastRegisterSender.setStatus("current")
_LispEidRegistrationAuthenticationErrors_Type = Counter64
_LispEidRegistrationAuthenticationErrors_Object = MibTableColumn
lispEidRegistrationAuthenticationErrors = _LispEidRegistrationAuthenticationErrors_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 10),
    _LispEidRegistrationAuthenticationErrors_Type()
)
lispEidRegistrationAuthenticationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationAuthenticationErrors.setStatus("current")
_LispEidRegistrationRlocsMismatch_Type = Counter64
_LispEidRegistrationRlocsMismatch_Object = MibTableColumn
lispEidRegistrationRlocsMismatch = _LispEidRegistrationRlocsMismatch_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 9, 1, 11),
    _LispEidRegistrationRlocsMismatch_Type()
)
lispEidRegistrationRlocsMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationRlocsMismatch.setStatus("current")
_LispEidRegistrationEtrTable_Object = MibTable
lispEidRegistrationEtrTable = _LispEidRegistrationEtrTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 10)
)
if mibBuilder.loadTexts:
    lispEidRegistrationEtrTable.setStatus("current")
_LispEidRegistrationEtrEntry_Object = MibTableRow
lispEidRegistrationEtrEntry = _LispEidRegistrationEtrEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 10, 1)
)
lispEidRegistrationEtrEntry.setIndexNames(
    (0, "LISP-MIB", "lispEidRegistrationEidLength"),
    (0, "LISP-MIB", "lispEidRegistrationEid"),
    (0, "LISP-MIB", "lispEidRegistrationEtrSenderLength"),
    (0, "LISP-MIB", "lispEidRegistrationEtrSender"),
)
if mibBuilder.loadTexts:
    lispEidRegistrationEtrEntry.setStatus("current")


class _LispEidRegistrationEtrSenderLength_Type(Integer32):
    """Custom type lispEidRegistrationEtrSenderLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispEidRegistrationEtrSenderLength_Type.__name__ = "Integer32"
_LispEidRegistrationEtrSenderLength_Object = MibTableColumn
lispEidRegistrationEtrSenderLength = _LispEidRegistrationEtrSenderLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 10, 1, 1),
    _LispEidRegistrationEtrSenderLength_Type()
)
lispEidRegistrationEtrSenderLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispEidRegistrationEtrSenderLength.setStatus("current")
_LispEidRegistrationEtrSender_Type = LispAddressType
_LispEidRegistrationEtrSender_Object = MibTableColumn
lispEidRegistrationEtrSender = _LispEidRegistrationEtrSender_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 10, 1, 2),
    _LispEidRegistrationEtrSender_Type()
)
lispEidRegistrationEtrSender.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispEidRegistrationEtrSender.setStatus("current")


class _LispEidRegistrationEtrLastTimeStamp_Type(TimeStamp):
    """Custom type lispEidRegistrationEtrLastTimeStamp based on TimeStamp"""
    defaultValue = 0


_LispEidRegistrationEtrLastTimeStamp_Object = MibTableColumn
lispEidRegistrationEtrLastTimeStamp = _LispEidRegistrationEtrLastTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 10, 1, 3),
    _LispEidRegistrationEtrLastTimeStamp_Type()
)
lispEidRegistrationEtrLastTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationEtrLastTimeStamp.setStatus("current")
_LispEidRegistrationEtrTtl_Type = Unsigned32
_LispEidRegistrationEtrTtl_Object = MibTableColumn
lispEidRegistrationEtrTtl = _LispEidRegistrationEtrTtl_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 10, 1, 4),
    _LispEidRegistrationEtrTtl_Type()
)
lispEidRegistrationEtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationEtrTtl.setStatus("current")
_LispEidRegistrationEtrProxyReply_Type = TruthValue
_LispEidRegistrationEtrProxyReply_Object = MibTableColumn
lispEidRegistrationEtrProxyReply = _LispEidRegistrationEtrProxyReply_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 10, 1, 5),
    _LispEidRegistrationEtrProxyReply_Type()
)
lispEidRegistrationEtrProxyReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationEtrProxyReply.setStatus("current")
_LispEidRegistrationEtrWantsMapNotify_Type = TruthValue
_LispEidRegistrationEtrWantsMapNotify_Object = MibTableColumn
lispEidRegistrationEtrWantsMapNotify = _LispEidRegistrationEtrWantsMapNotify_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 10, 1, 6),
    _LispEidRegistrationEtrWantsMapNotify_Type()
)
lispEidRegistrationEtrWantsMapNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationEtrWantsMapNotify.setStatus("current")
_LispEidRegistrationLocatorTable_Object = MibTable
lispEidRegistrationLocatorTable = _LispEidRegistrationLocatorTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11)
)
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorTable.setStatus("current")
_LispEidRegistrationLocatorEntry_Object = MibTableRow
lispEidRegistrationLocatorEntry = _LispEidRegistrationLocatorEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11, 1)
)
lispEidRegistrationLocatorEntry.setIndexNames(
    (0, "LISP-MIB", "lispEidRegistrationEidLength"),
    (0, "LISP-MIB", "lispEidRegistrationEid"),
    (0, "LISP-MIB", "lispEidRegistrationEtrSenderLength"),
    (0, "LISP-MIB", "lispEidRegistrationEtrSender"),
    (0, "LISP-MIB", "lispEidRegistrationLocatorRlocLength"),
    (0, "LISP-MIB", "lispEidRegistrationLocatorRloc"),
)
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorEntry.setStatus("current")


class _LispEidRegistrationLocatorRlocLength_Type(Integer32):
    """Custom type lispEidRegistrationLocatorRlocLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispEidRegistrationLocatorRlocLength_Type.__name__ = "Integer32"
_LispEidRegistrationLocatorRlocLength_Object = MibTableColumn
lispEidRegistrationLocatorRlocLength = _LispEidRegistrationLocatorRlocLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11, 1, 1),
    _LispEidRegistrationLocatorRlocLength_Type()
)
lispEidRegistrationLocatorRlocLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorRlocLength.setStatus("current")
_LispEidRegistrationLocatorRloc_Type = LispAddressType
_LispEidRegistrationLocatorRloc_Object = MibTableColumn
lispEidRegistrationLocatorRloc = _LispEidRegistrationLocatorRloc_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11, 1, 2),
    _LispEidRegistrationLocatorRloc_Type()
)
lispEidRegistrationLocatorRloc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorRloc.setStatus("current")


class _LispEidRegistrationLocatorRlocState_Type(Integer32):
    """Custom type lispEidRegistrationLocatorRlocState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LispEidRegistrationLocatorRlocState_Type.__name__ = "Integer32"
_LispEidRegistrationLocatorRlocState_Object = MibTableColumn
lispEidRegistrationLocatorRlocState = _LispEidRegistrationLocatorRlocState_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11, 1, 3),
    _LispEidRegistrationLocatorRlocState_Type()
)
lispEidRegistrationLocatorRlocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorRlocState.setStatus("current")
_LispEidRegistrationLocatorIsLocal_Type = TruthValue
_LispEidRegistrationLocatorIsLocal_Object = MibTableColumn
lispEidRegistrationLocatorIsLocal = _LispEidRegistrationLocatorIsLocal_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11, 1, 4),
    _LispEidRegistrationLocatorIsLocal_Type()
)
lispEidRegistrationLocatorIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorIsLocal.setStatus("current")


class _LispEidRegistrationLocatorPriority_Type(Integer32):
    """Custom type lispEidRegistrationLocatorPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LispEidRegistrationLocatorPriority_Type.__name__ = "Integer32"
_LispEidRegistrationLocatorPriority_Object = MibTableColumn
lispEidRegistrationLocatorPriority = _LispEidRegistrationLocatorPriority_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11, 1, 5),
    _LispEidRegistrationLocatorPriority_Type()
)
lispEidRegistrationLocatorPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorPriority.setStatus("current")


class _LispEidRegistrationLocatorWeight_Type(Integer32):
    """Custom type lispEidRegistrationLocatorWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LispEidRegistrationLocatorWeight_Type.__name__ = "Integer32"
_LispEidRegistrationLocatorWeight_Object = MibTableColumn
lispEidRegistrationLocatorWeight = _LispEidRegistrationLocatorWeight_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11, 1, 6),
    _LispEidRegistrationLocatorWeight_Type()
)
lispEidRegistrationLocatorWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorWeight.setStatus("current")


class _LispEidRegistrationLocatorMPriority_Type(Integer32):
    """Custom type lispEidRegistrationLocatorMPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LispEidRegistrationLocatorMPriority_Type.__name__ = "Integer32"
_LispEidRegistrationLocatorMPriority_Object = MibTableColumn
lispEidRegistrationLocatorMPriority = _LispEidRegistrationLocatorMPriority_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11, 1, 7),
    _LispEidRegistrationLocatorMPriority_Type()
)
lispEidRegistrationLocatorMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorMPriority.setStatus("current")


class _LispEidRegistrationLocatorMWeight_Type(Integer32):
    """Custom type lispEidRegistrationLocatorMWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LispEidRegistrationLocatorMWeight_Type.__name__ = "Integer32"
_LispEidRegistrationLocatorMWeight_Object = MibTableColumn
lispEidRegistrationLocatorMWeight = _LispEidRegistrationLocatorMWeight_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 11, 1, 8),
    _LispEidRegistrationLocatorMWeight_Type()
)
lispEidRegistrationLocatorMWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispEidRegistrationLocatorMWeight.setStatus("current")
_LispUseMapServerTable_Object = MibTable
lispUseMapServerTable = _LispUseMapServerTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 12)
)
if mibBuilder.loadTexts:
    lispUseMapServerTable.setStatus("current")
_LispUseMapServerEntry_Object = MibTableRow
lispUseMapServerEntry = _LispUseMapServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 12, 1)
)
lispUseMapServerEntry.setIndexNames(
    (0, "LISP-MIB", "lispUseMapServerAddressLength"),
    (0, "LISP-MIB", "lispUseMapServerAddress"),
)
if mibBuilder.loadTexts:
    lispUseMapServerEntry.setStatus("current")


class _LispUseMapServerAddressLength_Type(Integer32):
    """Custom type lispUseMapServerAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispUseMapServerAddressLength_Type.__name__ = "Integer32"
_LispUseMapServerAddressLength_Object = MibTableColumn
lispUseMapServerAddressLength = _LispUseMapServerAddressLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 12, 1, 1),
    _LispUseMapServerAddressLength_Type()
)
lispUseMapServerAddressLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispUseMapServerAddressLength.setStatus("current")
_LispUseMapServerAddress_Type = LispAddressType
_LispUseMapServerAddress_Object = MibTableColumn
lispUseMapServerAddress = _LispUseMapServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 12, 1, 2),
    _LispUseMapServerAddress_Type()
)
lispUseMapServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispUseMapServerAddress.setStatus("current")


class _LispUseMapServerState_Type(Integer32):
    """Custom type lispUseMapServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unreachable", 3),
          ("up", 1))
    )


_LispUseMapServerState_Type.__name__ = "Integer32"
_LispUseMapServerState_Object = MibTableColumn
lispUseMapServerState = _LispUseMapServerState_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 12, 1, 3),
    _LispUseMapServerState_Type()
)
lispUseMapServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispUseMapServerState.setStatus("current")
_LispUseMapResolverTable_Object = MibTable
lispUseMapResolverTable = _LispUseMapResolverTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 13)
)
if mibBuilder.loadTexts:
    lispUseMapResolverTable.setStatus("current")
_LispUseMapResolverEntry_Object = MibTableRow
lispUseMapResolverEntry = _LispUseMapResolverEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 13, 1)
)
lispUseMapResolverEntry.setIndexNames(
    (0, "LISP-MIB", "lispUseMapResolverAddressLength"),
    (0, "LISP-MIB", "lispUseMapResolverAddress"),
)
if mibBuilder.loadTexts:
    lispUseMapResolverEntry.setStatus("current")


class _LispUseMapResolverAddressLength_Type(Integer32):
    """Custom type lispUseMapResolverAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispUseMapResolverAddressLength_Type.__name__ = "Integer32"
_LispUseMapResolverAddressLength_Object = MibTableColumn
lispUseMapResolverAddressLength = _LispUseMapResolverAddressLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 13, 1, 1),
    _LispUseMapResolverAddressLength_Type()
)
lispUseMapResolverAddressLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispUseMapResolverAddressLength.setStatus("current")
_LispUseMapResolverAddress_Type = LispAddressType
_LispUseMapResolverAddress_Object = MibTableColumn
lispUseMapResolverAddress = _LispUseMapResolverAddress_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 13, 1, 2),
    _LispUseMapResolverAddress_Type()
)
lispUseMapResolverAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispUseMapResolverAddress.setStatus("current")


class _LispUseMapResolverState_Type(Integer32):
    """Custom type lispUseMapResolverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LispUseMapResolverState_Type.__name__ = "Integer32"
_LispUseMapResolverState_Object = MibTableColumn
lispUseMapResolverState = _LispUseMapResolverState_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 13, 1, 3),
    _LispUseMapResolverState_Type()
)
lispUseMapResolverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispUseMapResolverState.setStatus("current")
_LispUseProxyEtrTable_Object = MibTable
lispUseProxyEtrTable = _LispUseProxyEtrTable_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 14)
)
if mibBuilder.loadTexts:
    lispUseProxyEtrTable.setStatus("current")
_LispUseProxyEtrEntry_Object = MibTableRow
lispUseProxyEtrEntry = _LispUseProxyEtrEntry_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 14, 1)
)
lispUseProxyEtrEntry.setIndexNames(
    (0, "LISP-MIB", "lispUseProxyEtrAddressLength"),
    (0, "LISP-MIB", "lispUseProxyEtrAddress"),
)
if mibBuilder.loadTexts:
    lispUseProxyEtrEntry.setStatus("current")


class _LispUseProxyEtrAddressLength_Type(Integer32):
    """Custom type lispUseProxyEtrAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 39),
    )


_LispUseProxyEtrAddressLength_Type.__name__ = "Integer32"
_LispUseProxyEtrAddressLength_Object = MibTableColumn
lispUseProxyEtrAddressLength = _LispUseProxyEtrAddressLength_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 14, 1, 1),
    _LispUseProxyEtrAddressLength_Type()
)
lispUseProxyEtrAddressLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispUseProxyEtrAddressLength.setStatus("current")
_LispUseProxyEtrAddress_Type = LispAddressType
_LispUseProxyEtrAddress_Object = MibTableColumn
lispUseProxyEtrAddress = _LispUseProxyEtrAddress_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 14, 1, 2),
    _LispUseProxyEtrAddress_Type()
)
lispUseProxyEtrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lispUseProxyEtrAddress.setStatus("current")


class _LispUseProxyEtrPriority_Type(Integer32):
    """Custom type lispUseProxyEtrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LispUseProxyEtrPriority_Type.__name__ = "Integer32"
_LispUseProxyEtrPriority_Object = MibTableColumn
lispUseProxyEtrPriority = _LispUseProxyEtrPriority_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 14, 1, 3),
    _LispUseProxyEtrPriority_Type()
)
lispUseProxyEtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispUseProxyEtrPriority.setStatus("current")


class _LispUseProxyEtrWeight_Type(Integer32):
    """Custom type lispUseProxyEtrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LispUseProxyEtrWeight_Type.__name__ = "Integer32"
_LispUseProxyEtrWeight_Object = MibTableColumn
lispUseProxyEtrWeight = _LispUseProxyEtrWeight_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 14, 1, 4),
    _LispUseProxyEtrWeight_Type()
)
lispUseProxyEtrWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispUseProxyEtrWeight.setStatus("current")


class _LispUseProxyEtrMPriority_Type(Integer32):
    """Custom type lispUseProxyEtrMPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LispUseProxyEtrMPriority_Type.__name__ = "Integer32"
_LispUseProxyEtrMPriority_Object = MibTableColumn
lispUseProxyEtrMPriority = _LispUseProxyEtrMPriority_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 14, 1, 5),
    _LispUseProxyEtrMPriority_Type()
)
lispUseProxyEtrMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispUseProxyEtrMPriority.setStatus("current")


class _LispUseProxyEtrMWeight_Type(Integer32):
    """Custom type lispUseProxyEtrMWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LispUseProxyEtrMWeight_Type.__name__ = "Integer32"
_LispUseProxyEtrMWeight_Object = MibTableColumn
lispUseProxyEtrMWeight = _LispUseProxyEtrMWeight_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 14, 1, 6),
    _LispUseProxyEtrMWeight_Type()
)
lispUseProxyEtrMWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispUseProxyEtrMWeight.setStatus("current")


class _LispUseProxyEtrState_Type(Integer32):
    """Custom type lispUseProxyEtrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_LispUseProxyEtrState_Type.__name__ = "Integer32"
_LispUseProxyEtrState_Object = MibTableColumn
lispUseProxyEtrState = _LispUseProxyEtrState_Object(
    (1, 3, 6, 1, 2, 1, 220, 1, 14, 1, 7),
    _LispUseProxyEtrState_Type()
)
lispUseProxyEtrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lispUseProxyEtrState.setStatus("current")
_LispConformance_ObjectIdentity = ObjectIdentity
lispConformance = _LispConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 220, 2)
)
_LispCompliances_ObjectIdentity = ObjectIdentity
lispCompliances = _LispCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 220, 2, 1)
)
_LispGroups_ObjectIdentity = ObjectIdentity
lispGroups = _LispGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 220, 2, 2)
)

# Managed Objects groups

lispMIBEtrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 1)
)
lispMIBEtrGroup.setObjects(
      *(("LISP-MIB", "lispFeaturesEtrEnabled"),
        ("LISP-MIB", "lispMappingDatabaseLsb"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocPriority"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocWeight"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocMPriority"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocMWeight"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocState"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocLocal"),
        ("LISP-MIB", "lispConfiguredLocatorRlocState"),
        ("LISP-MIB", "lispConfiguredLocatorRlocLocal"),
        ("LISP-MIB", "lispUseMapServerState"))
)
if mibBuilder.loadTexts:
    lispMIBEtrGroup.setStatus("current")

lispMIBItrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 2)
)
lispMIBItrGroup.setObjects(
      *(("LISP-MIB", "lispFeaturesItrEnabled"),
        ("LISP-MIB", "lispFeaturesMapCacheSize"),
        ("LISP-MIB", "lispMappingDatabaseLsb"),
        ("LISP-MIB", "lispMapCacheLocatorRlocPriority"),
        ("LISP-MIB", "lispMapCacheLocatorRlocWeight"),
        ("LISP-MIB", "lispMapCacheLocatorRlocMPriority"),
        ("LISP-MIB", "lispMapCacheLocatorRlocMWeight"),
        ("LISP-MIB", "lispMapCacheLocatorRlocState"),
        ("LISP-MIB", "lispMapCacheEidTimeStamp"),
        ("LISP-MIB", "lispMapCacheEidExpiryTime"),
        ("LISP-MIB", "lispUseMapResolverState"),
        ("LISP-MIB", "lispUseProxyEtrPriority"),
        ("LISP-MIB", "lispUseProxyEtrWeight"),
        ("LISP-MIB", "lispUseProxyEtrMPriority"),
        ("LISP-MIB", "lispUseProxyEtrMWeight"),
        ("LISP-MIB", "lispUseProxyEtrState"))
)
if mibBuilder.loadTexts:
    lispMIBItrGroup.setStatus("current")

lispMIBPetrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 3)
)
lispMIBPetrGroup.setObjects(
    ("LISP-MIB", "lispFeaturesProxyEtrEnabled")
)
if mibBuilder.loadTexts:
    lispMIBPetrGroup.setStatus("current")

lispMIBPitrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 4)
)
lispMIBPitrGroup.setObjects(
      *(("LISP-MIB", "lispFeaturesProxyItrEnabled"),
        ("LISP-MIB", "lispConfiguredLocatorRlocState"),
        ("LISP-MIB", "lispConfiguredLocatorRlocLocal"))
)
if mibBuilder.loadTexts:
    lispMIBPitrGroup.setStatus("current")

lispMIBMapServerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 5)
)
lispMIBMapServerGroup.setObjects(
      *(("LISP-MIB", "lispFeaturesMapServerEnabled"),
        ("LISP-MIB", "lispEidRegistrationIsRegistered"),
        ("LISP-MIB", "lispEidRegistrationLocatorRlocState"))
)
if mibBuilder.loadTexts:
    lispMIBMapServerGroup.setStatus("current")

lispMIBMapResolverGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 6)
)
lispMIBMapResolverGroup.setObjects(
    ("LISP-MIB", "lispFeaturesMapResolverEnabled")
)
if mibBuilder.loadTexts:
    lispMIBMapResolverGroup.setStatus("current")

lispMIBEtrExtendedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 7)
)
lispMIBEtrExtendedGroup.setObjects(
      *(("LISP-MIB", "lispFeaturesRlocProbeEnabled"),
        ("LISP-MIB", "lispFeaturesEtrAcceptMapDataEnabled"),
        ("LISP-MIB", "lispFeaturesEtrAcceptMapDataVerifyEnabled"),
        ("LISP-MIB", "lispMappingDatabaseEidPartitioned"))
)
if mibBuilder.loadTexts:
    lispMIBEtrExtendedGroup.setStatus("current")

lispMIBItrExtendedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 8)
)
lispMIBItrExtendedGroup.setObjects(
      *(("LISP-MIB", "lispFeaturesRlocProbeEnabled"),
        ("LISP-MIB", "lispMapCacheEidState"),
        ("LISP-MIB", "lispMapCacheEidAuthoritative"),
        ("LISP-MIB", "lispMapCacheLocatorRlocTimeStamp"),
        ("LISP-MIB", "lispMapCacheLocatorRlocLastPriorityChange"),
        ("LISP-MIB", "lispMapCacheLocatorRlocLastWeightChange"),
        ("LISP-MIB", "lispMapCacheLocatorRlocLastMPriorityChange"),
        ("LISP-MIB", "lispMapCacheLocatorRlocLastMWeightChange"),
        ("LISP-MIB", "lispMapCacheLocatorRlocLastStateChange"),
        ("LISP-MIB", "lispMapCacheLocatorRlocRtt"))
)
if mibBuilder.loadTexts:
    lispMIBItrExtendedGroup.setStatus("current")

lispMIBMapServerExtendedGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 9)
)
lispMIBMapServerExtendedGroup.setObjects(
      *(("LISP-MIB", "lispEidRegistrationSiteName"),
        ("LISP-MIB", "lispEidRegistrationSiteDescription"),
        ("LISP-MIB", "lispEidRegistrationIsRegistered"),
        ("LISP-MIB", "lispEidRegistrationFirstTimeStamp"),
        ("LISP-MIB", "lispEidRegistrationLastTimeStamp"),
        ("LISP-MIB", "lispEidRegistrationLastRegisterSenderLength"),
        ("LISP-MIB", "lispEidRegistrationLastRegisterSender"),
        ("LISP-MIB", "lispEidRegistrationEtrLastTimeStamp"),
        ("LISP-MIB", "lispEidRegistrationEtrTtl"),
        ("LISP-MIB", "lispEidRegistrationEtrProxyReply"),
        ("LISP-MIB", "lispEidRegistrationEtrWantsMapNotify"),
        ("LISP-MIB", "lispEidRegistrationLocatorIsLocal"),
        ("LISP-MIB", "lispEidRegistrationLocatorPriority"),
        ("LISP-MIB", "lispEidRegistrationLocatorWeight"),
        ("LISP-MIB", "lispEidRegistrationLocatorMPriority"),
        ("LISP-MIB", "lispEidRegistrationLocatorMWeight"))
)
if mibBuilder.loadTexts:
    lispMIBMapServerExtendedGroup.setStatus("current")

lispMIBTuningParametersGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 10)
)
lispMIBTuningParametersGroup.setObjects(
      *(("LISP-MIB", "lispFeaturesMapCacheLimit"),
        ("LISP-MIB", "lispFeaturesEtrMapCacheTtl"))
)
if mibBuilder.loadTexts:
    lispMIBTuningParametersGroup.setStatus("current")

lispMIBEncapStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 11)
)
lispMIBEncapStatisticsGroup.setObjects(
      *(("LISP-MIB", "lispMappingDatabaseTimeStamp"),
        ("LISP-MIB", "lispMappingDatabaseEncapOctets"),
        ("LISP-MIB", "lispMappingDatabaseEncapPackets"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocTimeStamp"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocEncapOctets"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocEncapPackets"),
        ("LISP-MIB", "lispMapCacheEidTimeStamp"),
        ("LISP-MIB", "lispMapCacheEidEncapOctets"),
        ("LISP-MIB", "lispMapCacheEidEncapPackets"),
        ("LISP-MIB", "lispMapCacheLocatorRlocTimeStamp"),
        ("LISP-MIB", "lispMapCacheLocatorRlocEncapOctets"),
        ("LISP-MIB", "lispMapCacheLocatorRlocEncapPackets"),
        ("LISP-MIB", "lispConfiguredLocatorRlocTimeStamp"),
        ("LISP-MIB", "lispConfiguredLocatorRlocEncapOctets"),
        ("LISP-MIB", "lispConfiguredLocatorRlocEncapPackets"))
)
if mibBuilder.loadTexts:
    lispMIBEncapStatisticsGroup.setStatus("current")

lispMIBDecapStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 12)
)
lispMIBDecapStatisticsGroup.setObjects(
      *(("LISP-MIB", "lispMappingDatabaseTimeStamp"),
        ("LISP-MIB", "lispMappingDatabaseDecapOctets"),
        ("LISP-MIB", "lispMappingDatabaseDecapPackets"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocTimeStamp"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocDecapOctets"),
        ("LISP-MIB", "lispMappingDatabaseLocatorRlocDecapPackets"),
        ("LISP-MIB", "lispMapCacheEidTimeStamp"),
        ("LISP-MIB", "lispMapCacheEidDecapOctets"),
        ("LISP-MIB", "lispMapCacheEidDecapPackets"),
        ("LISP-MIB", "lispMapCacheLocatorRlocTimeStamp"),
        ("LISP-MIB", "lispMapCacheLocatorRlocDecapOctets"),
        ("LISP-MIB", "lispMapCacheLocatorRlocDecapPackets"),
        ("LISP-MIB", "lispConfiguredLocatorRlocTimeStamp"),
        ("LISP-MIB", "lispConfiguredLocatorRlocDecapOctets"),
        ("LISP-MIB", "lispConfiguredLocatorRlocDecapPackets"))
)
if mibBuilder.loadTexts:
    lispMIBDecapStatisticsGroup.setStatus("current")

lispMIBDiagnosticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 13)
)
lispMIBDiagnosticsGroup.setObjects(
      *(("LISP-MIB", "lispFeaturesRouterTimeStamp"),
        ("LISP-MIB", "lispGlobalStatsMapRequestsIn"),
        ("LISP-MIB", "lispGlobalStatsMapRequestsOut"),
        ("LISP-MIB", "lispGlobalStatsMapRepliesIn"),
        ("LISP-MIB", "lispGlobalStatsMapRepliesOut"),
        ("LISP-MIB", "lispGlobalStatsMapRegistersIn"),
        ("LISP-MIB", "lispGlobalStatsMapRegistersOut"),
        ("LISP-MIB", "lispEidRegistrationAuthenticationErrors"),
        ("LISP-MIB", "lispEidRegistrationRlocsMismatch"))
)
if mibBuilder.loadTexts:
    lispMIBDiagnosticsGroup.setStatus("current")

lispMIBVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 220, 2, 2, 14)
)
lispMIBVrfGroup.setObjects(
    ("LISP-MIB", "lispIidToVrfName")
)
if mibBuilder.loadTexts:
    lispMIBVrfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lispMIBComplianceEtr = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 220, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lispMIBComplianceEtr.setStatus(
        "current"
    )

lispMIBComplianceItr = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 220, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lispMIBComplianceItr.setStatus(
        "current"
    )

lispMIBCompliancePetr = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 220, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lispMIBCompliancePetr.setStatus(
        "current"
    )

lispMIBCompliancePitr = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 220, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lispMIBCompliancePitr.setStatus(
        "current"
    )

lispMIBComplianceMapServer = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 220, 2, 1, 5)
)
if mibBuilder.loadTexts:
    lispMIBComplianceMapServer.setStatus(
        "current"
    )

lispMIBComplianceMapResolver = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 220, 2, 1, 6)
)
if mibBuilder.loadTexts:
    lispMIBComplianceMapResolver.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LISP-MIB",
    **{"LispAddressType": LispAddressType,
       "lispMIB": lispMIB,
       "lispObjects": lispObjects,
       "lispFeaturesTable": lispFeaturesTable,
       "lispFeaturesEntry": lispFeaturesEntry,
       "lispFeaturesInstanceID": lispFeaturesInstanceID,
       "lispFeaturesAddressFamily": lispFeaturesAddressFamily,
       "lispFeaturesItrEnabled": lispFeaturesItrEnabled,
       "lispFeaturesEtrEnabled": lispFeaturesEtrEnabled,
       "lispFeaturesProxyItrEnabled": lispFeaturesProxyItrEnabled,
       "lispFeaturesProxyEtrEnabled": lispFeaturesProxyEtrEnabled,
       "lispFeaturesMapServerEnabled": lispFeaturesMapServerEnabled,
       "lispFeaturesMapResolverEnabled": lispFeaturesMapResolverEnabled,
       "lispFeaturesMapCacheSize": lispFeaturesMapCacheSize,
       "lispFeaturesMapCacheLimit": lispFeaturesMapCacheLimit,
       "lispFeaturesEtrMapCacheTtl": lispFeaturesEtrMapCacheTtl,
       "lispFeaturesRlocProbeEnabled": lispFeaturesRlocProbeEnabled,
       "lispFeaturesEtrAcceptMapDataEnabled": lispFeaturesEtrAcceptMapDataEnabled,
       "lispFeaturesEtrAcceptMapDataVerifyEnabled": lispFeaturesEtrAcceptMapDataVerifyEnabled,
       "lispFeaturesRouterTimeStamp": lispFeaturesRouterTimeStamp,
       "lispIidToVrfTable": lispIidToVrfTable,
       "lispIidToVrfEntry": lispIidToVrfEntry,
       "lispIidToVrfName": lispIidToVrfName,
       "lispGlobalStatsTable": lispGlobalStatsTable,
       "lispGlobalStatsEntry": lispGlobalStatsEntry,
       "lispGlobalStatsMapRequestsIn": lispGlobalStatsMapRequestsIn,
       "lispGlobalStatsMapRequestsOut": lispGlobalStatsMapRequestsOut,
       "lispGlobalStatsMapRepliesIn": lispGlobalStatsMapRepliesIn,
       "lispGlobalStatsMapRepliesOut": lispGlobalStatsMapRepliesOut,
       "lispGlobalStatsMapRegistersIn": lispGlobalStatsMapRegistersIn,
       "lispGlobalStatsMapRegistersOut": lispGlobalStatsMapRegistersOut,
       "lispMappingDatabaseTable": lispMappingDatabaseTable,
       "lispMappingDatabaseEntry": lispMappingDatabaseEntry,
       "lispMappingDatabaseEidLength": lispMappingDatabaseEidLength,
       "lispMappingDatabaseEid": lispMappingDatabaseEid,
       "lispMappingDatabaseLsb": lispMappingDatabaseLsb,
       "lispMappingDatabaseEidPartitioned": lispMappingDatabaseEidPartitioned,
       "lispMappingDatabaseTimeStamp": lispMappingDatabaseTimeStamp,
       "lispMappingDatabaseDecapOctets": lispMappingDatabaseDecapOctets,
       "lispMappingDatabaseDecapPackets": lispMappingDatabaseDecapPackets,
       "lispMappingDatabaseEncapOctets": lispMappingDatabaseEncapOctets,
       "lispMappingDatabaseEncapPackets": lispMappingDatabaseEncapPackets,
       "lispMappingDatabaseLocatorTable": lispMappingDatabaseLocatorTable,
       "lispMappingDatabaseLocatorEntry": lispMappingDatabaseLocatorEntry,
       "lispMappingDatabaseLocatorRlocLength": lispMappingDatabaseLocatorRlocLength,
       "lispMappingDatabaseLocatorRloc": lispMappingDatabaseLocatorRloc,
       "lispMappingDatabaseLocatorRlocPriority": lispMappingDatabaseLocatorRlocPriority,
       "lispMappingDatabaseLocatorRlocWeight": lispMappingDatabaseLocatorRlocWeight,
       "lispMappingDatabaseLocatorRlocMPriority": lispMappingDatabaseLocatorRlocMPriority,
       "lispMappingDatabaseLocatorRlocMWeight": lispMappingDatabaseLocatorRlocMWeight,
       "lispMappingDatabaseLocatorRlocState": lispMappingDatabaseLocatorRlocState,
       "lispMappingDatabaseLocatorRlocLocal": lispMappingDatabaseLocatorRlocLocal,
       "lispMappingDatabaseLocatorRlocTimeStamp": lispMappingDatabaseLocatorRlocTimeStamp,
       "lispMappingDatabaseLocatorRlocDecapOctets": lispMappingDatabaseLocatorRlocDecapOctets,
       "lispMappingDatabaseLocatorRlocDecapPackets": lispMappingDatabaseLocatorRlocDecapPackets,
       "lispMappingDatabaseLocatorRlocEncapOctets": lispMappingDatabaseLocatorRlocEncapOctets,
       "lispMappingDatabaseLocatorRlocEncapPackets": lispMappingDatabaseLocatorRlocEncapPackets,
       "lispMapCacheTable": lispMapCacheTable,
       "lispMapCacheEntry": lispMapCacheEntry,
       "lispMapCacheEidLength": lispMapCacheEidLength,
       "lispMapCacheEid": lispMapCacheEid,
       "lispMapCacheEidTimeStamp": lispMapCacheEidTimeStamp,
       "lispMapCacheEidExpiryTime": lispMapCacheEidExpiryTime,
       "lispMapCacheEidState": lispMapCacheEidState,
       "lispMapCacheEidAuthoritative": lispMapCacheEidAuthoritative,
       "lispMapCacheEidDecapOctets": lispMapCacheEidDecapOctets,
       "lispMapCacheEidDecapPackets": lispMapCacheEidDecapPackets,
       "lispMapCacheEidEncapOctets": lispMapCacheEidEncapOctets,
       "lispMapCacheEidEncapPackets": lispMapCacheEidEncapPackets,
       "lispMapCacheLocatorTable": lispMapCacheLocatorTable,
       "lispMapCacheLocatorEntry": lispMapCacheLocatorEntry,
       "lispMapCacheLocatorRlocLength": lispMapCacheLocatorRlocLength,
       "lispMapCacheLocatorRloc": lispMapCacheLocatorRloc,
       "lispMapCacheLocatorRlocPriority": lispMapCacheLocatorRlocPriority,
       "lispMapCacheLocatorRlocWeight": lispMapCacheLocatorRlocWeight,
       "lispMapCacheLocatorRlocMPriority": lispMapCacheLocatorRlocMPriority,
       "lispMapCacheLocatorRlocMWeight": lispMapCacheLocatorRlocMWeight,
       "lispMapCacheLocatorRlocState": lispMapCacheLocatorRlocState,
       "lispMapCacheLocatorRlocTimeStamp": lispMapCacheLocatorRlocTimeStamp,
       "lispMapCacheLocatorRlocLastPriorityChange": lispMapCacheLocatorRlocLastPriorityChange,
       "lispMapCacheLocatorRlocLastWeightChange": lispMapCacheLocatorRlocLastWeightChange,
       "lispMapCacheLocatorRlocLastMPriorityChange": lispMapCacheLocatorRlocLastMPriorityChange,
       "lispMapCacheLocatorRlocLastMWeightChange": lispMapCacheLocatorRlocLastMWeightChange,
       "lispMapCacheLocatorRlocLastStateChange": lispMapCacheLocatorRlocLastStateChange,
       "lispMapCacheLocatorRlocRtt": lispMapCacheLocatorRlocRtt,
       "lispMapCacheLocatorRlocDecapOctets": lispMapCacheLocatorRlocDecapOctets,
       "lispMapCacheLocatorRlocDecapPackets": lispMapCacheLocatorRlocDecapPackets,
       "lispMapCacheLocatorRlocEncapOctets": lispMapCacheLocatorRlocEncapOctets,
       "lispMapCacheLocatorRlocEncapPackets": lispMapCacheLocatorRlocEncapPackets,
       "lispConfiguredLocatorTable": lispConfiguredLocatorTable,
       "lispConfiguredLocatorEntry": lispConfiguredLocatorEntry,
       "lispConfiguredLocatorRlocLength": lispConfiguredLocatorRlocLength,
       "lispConfiguredLocatorRloc": lispConfiguredLocatorRloc,
       "lispConfiguredLocatorRlocState": lispConfiguredLocatorRlocState,
       "lispConfiguredLocatorRlocLocal": lispConfiguredLocatorRlocLocal,
       "lispConfiguredLocatorRlocTimeStamp": lispConfiguredLocatorRlocTimeStamp,
       "lispConfiguredLocatorRlocDecapOctets": lispConfiguredLocatorRlocDecapOctets,
       "lispConfiguredLocatorRlocDecapPackets": lispConfiguredLocatorRlocDecapPackets,
       "lispConfiguredLocatorRlocEncapOctets": lispConfiguredLocatorRlocEncapOctets,
       "lispConfiguredLocatorRlocEncapPackets": lispConfiguredLocatorRlocEncapPackets,
       "lispEidRegistrationTable": lispEidRegistrationTable,
       "lispEidRegistrationEntry": lispEidRegistrationEntry,
       "lispEidRegistrationEidLength": lispEidRegistrationEidLength,
       "lispEidRegistrationEid": lispEidRegistrationEid,
       "lispEidRegistrationSiteName": lispEidRegistrationSiteName,
       "lispEidRegistrationSiteDescription": lispEidRegistrationSiteDescription,
       "lispEidRegistrationIsRegistered": lispEidRegistrationIsRegistered,
       "lispEidRegistrationFirstTimeStamp": lispEidRegistrationFirstTimeStamp,
       "lispEidRegistrationLastTimeStamp": lispEidRegistrationLastTimeStamp,
       "lispEidRegistrationLastRegisterSenderLength": lispEidRegistrationLastRegisterSenderLength,
       "lispEidRegistrationLastRegisterSender": lispEidRegistrationLastRegisterSender,
       "lispEidRegistrationAuthenticationErrors": lispEidRegistrationAuthenticationErrors,
       "lispEidRegistrationRlocsMismatch": lispEidRegistrationRlocsMismatch,
       "lispEidRegistrationEtrTable": lispEidRegistrationEtrTable,
       "lispEidRegistrationEtrEntry": lispEidRegistrationEtrEntry,
       "lispEidRegistrationEtrSenderLength": lispEidRegistrationEtrSenderLength,
       "lispEidRegistrationEtrSender": lispEidRegistrationEtrSender,
       "lispEidRegistrationEtrLastTimeStamp": lispEidRegistrationEtrLastTimeStamp,
       "lispEidRegistrationEtrTtl": lispEidRegistrationEtrTtl,
       "lispEidRegistrationEtrProxyReply": lispEidRegistrationEtrProxyReply,
       "lispEidRegistrationEtrWantsMapNotify": lispEidRegistrationEtrWantsMapNotify,
       "lispEidRegistrationLocatorTable": lispEidRegistrationLocatorTable,
       "lispEidRegistrationLocatorEntry": lispEidRegistrationLocatorEntry,
       "lispEidRegistrationLocatorRlocLength": lispEidRegistrationLocatorRlocLength,
       "lispEidRegistrationLocatorRloc": lispEidRegistrationLocatorRloc,
       "lispEidRegistrationLocatorRlocState": lispEidRegistrationLocatorRlocState,
       "lispEidRegistrationLocatorIsLocal": lispEidRegistrationLocatorIsLocal,
       "lispEidRegistrationLocatorPriority": lispEidRegistrationLocatorPriority,
       "lispEidRegistrationLocatorWeight": lispEidRegistrationLocatorWeight,
       "lispEidRegistrationLocatorMPriority": lispEidRegistrationLocatorMPriority,
       "lispEidRegistrationLocatorMWeight": lispEidRegistrationLocatorMWeight,
       "lispUseMapServerTable": lispUseMapServerTable,
       "lispUseMapServerEntry": lispUseMapServerEntry,
       "lispUseMapServerAddressLength": lispUseMapServerAddressLength,
       "lispUseMapServerAddress": lispUseMapServerAddress,
       "lispUseMapServerState": lispUseMapServerState,
       "lispUseMapResolverTable": lispUseMapResolverTable,
       "lispUseMapResolverEntry": lispUseMapResolverEntry,
       "lispUseMapResolverAddressLength": lispUseMapResolverAddressLength,
       "lispUseMapResolverAddress": lispUseMapResolverAddress,
       "lispUseMapResolverState": lispUseMapResolverState,
       "lispUseProxyEtrTable": lispUseProxyEtrTable,
       "lispUseProxyEtrEntry": lispUseProxyEtrEntry,
       "lispUseProxyEtrAddressLength": lispUseProxyEtrAddressLength,
       "lispUseProxyEtrAddress": lispUseProxyEtrAddress,
       "lispUseProxyEtrPriority": lispUseProxyEtrPriority,
       "lispUseProxyEtrWeight": lispUseProxyEtrWeight,
       "lispUseProxyEtrMPriority": lispUseProxyEtrMPriority,
       "lispUseProxyEtrMWeight": lispUseProxyEtrMWeight,
       "lispUseProxyEtrState": lispUseProxyEtrState,
       "lispConformance": lispConformance,
       "lispCompliances": lispCompliances,
       "lispMIBComplianceEtr": lispMIBComplianceEtr,
       "lispMIBComplianceItr": lispMIBComplianceItr,
       "lispMIBCompliancePetr": lispMIBCompliancePetr,
       "lispMIBCompliancePitr": lispMIBCompliancePitr,
       "lispMIBComplianceMapServer": lispMIBComplianceMapServer,
       "lispMIBComplianceMapResolver": lispMIBComplianceMapResolver,
       "lispGroups": lispGroups,
       "lispMIBEtrGroup": lispMIBEtrGroup,
       "lispMIBItrGroup": lispMIBItrGroup,
       "lispMIBPetrGroup": lispMIBPetrGroup,
       "lispMIBPitrGroup": lispMIBPitrGroup,
       "lispMIBMapServerGroup": lispMIBMapServerGroup,
       "lispMIBMapResolverGroup": lispMIBMapResolverGroup,
       "lispMIBEtrExtendedGroup": lispMIBEtrExtendedGroup,
       "lispMIBItrExtendedGroup": lispMIBItrExtendedGroup,
       "lispMIBMapServerExtendedGroup": lispMIBMapServerExtendedGroup,
       "lispMIBTuningParametersGroup": lispMIBTuningParametersGroup,
       "lispMIBEncapStatisticsGroup": lispMIBEncapStatisticsGroup,
       "lispMIBDecapStatisticsGroup": lispMIBDecapStatisticsGroup,
       "lispMIBDiagnosticsGroup": lispMIBDiagnosticsGroup,
       "lispMIBVrfGroup": lispMIBVrfGroup}
)
