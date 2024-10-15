# SNMP MIB module (RADLAN-rlFft) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-rlFft
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:10 2024
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlFFT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 47)
)
rlFFT.setRevisions(
        ("2004-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Percents(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class NetNumber(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_RlIpFFT_ObjectIdentity = ObjectIdentity
rlIpFFT = _RlIpFFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 47, 1)
)
_RlIpFftMibVersion_Type = Integer32
_RlIpFftMibVersion_Object = MibScalar
rlIpFftMibVersion = _RlIpFftMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 1),
    _RlIpFftMibVersion_Type()
)
rlIpFftMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftMibVersion.setStatus("current")
_RlIpMaxFftNumber_Type = Integer32
_RlIpMaxFftNumber_Object = MibScalar
rlIpMaxFftNumber = _RlIpMaxFftNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 2),
    _RlIpMaxFftNumber_Type()
)
rlIpMaxFftNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpMaxFftNumber.setStatus("current")


class _RlIpFftDynamicSupported_Type(Integer32):
    """Custom type rlIpFftDynamicSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlIpFftDynamicSupported_Type.__name__ = "Integer32"
_RlIpFftDynamicSupported_Object = MibScalar
rlIpFftDynamicSupported = _RlIpFftDynamicSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 3),
    _RlIpFftDynamicSupported_Type()
)
rlIpFftDynamicSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftDynamicSupported.setStatus("current")


class _RlIpFftSubnetSupported_Type(Integer32):
    """Custom type rlIpFftSubnetSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlIpFftSubnetSupported_Type.__name__ = "Integer32"
_RlIpFftSubnetSupported_Object = MibScalar
rlIpFftSubnetSupported = _RlIpFftSubnetSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 4),
    _RlIpFftSubnetSupported_Type()
)
rlIpFftSubnetSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubnetSupported.setStatus("current")


class _RlIpFftUnknownAddrMsgUsed_Type(Integer32):
    """Custom type rlIpFftUnknownAddrMsgUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 2),
          ("used", 1))
    )


_RlIpFftUnknownAddrMsgUsed_Type.__name__ = "Integer32"
_RlIpFftUnknownAddrMsgUsed_Object = MibScalar
rlIpFftUnknownAddrMsgUsed = _RlIpFftUnknownAddrMsgUsed_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 5),
    _RlIpFftUnknownAddrMsgUsed_Type()
)
rlIpFftUnknownAddrMsgUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftUnknownAddrMsgUsed.setStatus("current")


class _RlIpFftAgingTimeSupported_Type(Integer32):
    """Custom type rlIpFftAgingTimeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlIpFftAgingTimeSupported_Type.__name__ = "Integer32"
_RlIpFftAgingTimeSupported_Object = MibScalar
rlIpFftAgingTimeSupported = _RlIpFftAgingTimeSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 6),
    _RlIpFftAgingTimeSupported_Type()
)
rlIpFftAgingTimeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftAgingTimeSupported.setStatus("current")


class _RlIpFftSrcAddrSupported_Type(Integer32):
    """Custom type rlIpFftSrcAddrSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlIpFftSrcAddrSupported_Type.__name__ = "Integer32"
_RlIpFftSrcAddrSupported_Object = MibScalar
rlIpFftSrcAddrSupported = _RlIpFftSrcAddrSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 7),
    _RlIpFftSrcAddrSupported_Type()
)
rlIpFftSrcAddrSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSrcAddrSupported.setStatus("current")
_RlIpFftAgingTimeout_Type = Integer32
_RlIpFftAgingTimeout_Object = MibScalar
rlIpFftAgingTimeout = _RlIpFftAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 8),
    _RlIpFftAgingTimeout_Type()
)
rlIpFftAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpFftAgingTimeout.setStatus("current")
_RlIpFftRedBoundary_Type = Percents
_RlIpFftRedBoundary_Object = MibScalar
rlIpFftRedBoundary = _RlIpFftRedBoundary_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 9),
    _RlIpFftRedBoundary_Type()
)
rlIpFftRedBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpFftRedBoundary.setStatus("current")
_RlIpFftYellowBoundary_Type = Percents
_RlIpFftYellowBoundary_Object = MibScalar
rlIpFftYellowBoundary = _RlIpFftYellowBoundary_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 10),
    _RlIpFftYellowBoundary_Type()
)
rlIpFftYellowBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpFftYellowBoundary.setStatus("current")
_RlIpFftNumTable_Object = MibTable
rlIpFftNumTable = _RlIpFftNumTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 12)
)
if mibBuilder.loadTexts:
    rlIpFftNumTable.setStatus("current")
_RlIpFftNumEntry_Object = MibTableRow
rlIpFftNumEntry = _RlIpFftNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 12, 1)
)
rlIpFftNumEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpFftNumIndex"),
)
if mibBuilder.loadTexts:
    rlIpFftNumEntry.setStatus("current")
_RlIpFftNumIndex_Type = Integer32
_RlIpFftNumIndex_Object = MibTableColumn
rlIpFftNumIndex = _RlIpFftNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 12, 1, 1),
    _RlIpFftNumIndex_Type()
)
rlIpFftNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNumIndex.setStatus("current")
_RlIpFftNumStnRoutesNumber_Type = Integer32
_RlIpFftNumStnRoutesNumber_Object = MibTableColumn
rlIpFftNumStnRoutesNumber = _RlIpFftNumStnRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 12, 1, 2),
    _RlIpFftNumStnRoutesNumber_Type()
)
rlIpFftNumStnRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNumStnRoutesNumber.setStatus("current")
_RlIpFftNumSubRoutesNumber_Type = Integer32
_RlIpFftNumSubRoutesNumber_Object = MibTableColumn
rlIpFftNumSubRoutesNumber = _RlIpFftNumSubRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 12, 1, 3),
    _RlIpFftNumSubRoutesNumber_Type()
)
rlIpFftNumSubRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNumSubRoutesNumber.setStatus("current")
_RlIpFftStnTable_Object = MibTable
rlIpFftStnTable = _RlIpFftStnTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13)
)
if mibBuilder.loadTexts:
    rlIpFftStnTable.setStatus("current")
_RlIpFftStnEntry_Object = MibTableRow
rlIpFftStnEntry = _RlIpFftStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1)
)
rlIpFftStnEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpFftStnIndex"),
    (0, "RADLAN-rlFft", "rlIpFftStnMrid"),
    (0, "RADLAN-rlFft", "rlIpFftStnDstIpAddress"),
)
if mibBuilder.loadTexts:
    rlIpFftStnEntry.setStatus("current")
_RlIpFftStnIndex_Type = Integer32
_RlIpFftStnIndex_Object = MibTableColumn
rlIpFftStnIndex = _RlIpFftStnIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 1),
    _RlIpFftStnIndex_Type()
)
rlIpFftStnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnIndex.setStatus("current")
_RlIpFftStnMrid_Type = Integer32
_RlIpFftStnMrid_Object = MibTableColumn
rlIpFftStnMrid = _RlIpFftStnMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 2),
    _RlIpFftStnMrid_Type()
)
rlIpFftStnMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnMrid.setStatus("current")
_RlIpFftStnDstIpAddress_Type = IpAddress
_RlIpFftStnDstIpAddress_Object = MibTableColumn
rlIpFftStnDstIpAddress = _RlIpFftStnDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 3),
    _RlIpFftStnDstIpAddress_Type()
)
rlIpFftStnDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnDstIpAddress.setStatus("current")
_RlIpFftStnDstRouteIpMask_Type = IpAddress
_RlIpFftStnDstRouteIpMask_Object = MibTableColumn
rlIpFftStnDstRouteIpMask = _RlIpFftStnDstRouteIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 4),
    _RlIpFftStnDstRouteIpMask_Type()
)
rlIpFftStnDstRouteIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnDstRouteIpMask.setStatus("current")


class _RlIpFftStnDstIpAddrType_Type(Integer32):
    """Custom type rlIpFftStnDstIpAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_RlIpFftStnDstIpAddrType_Type.__name__ = "Integer32"
_RlIpFftStnDstIpAddrType_Object = MibTableColumn
rlIpFftStnDstIpAddrType = _RlIpFftStnDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 5),
    _RlIpFftStnDstIpAddrType_Type()
)
rlIpFftStnDstIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnDstIpAddrType.setStatus("current")
_RlIpFftStnDstMacAddress_Type = PhysAddress
_RlIpFftStnDstMacAddress_Object = MibTableColumn
rlIpFftStnDstMacAddress = _RlIpFftStnDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 6),
    _RlIpFftStnDstMacAddress_Type()
)
rlIpFftStnDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnDstMacAddress.setStatus("current")
_RlIpFftStnSrcMacAddress_Type = PhysAddress
_RlIpFftStnSrcMacAddress_Object = MibTableColumn
rlIpFftStnSrcMacAddress = _RlIpFftStnSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 7),
    _RlIpFftStnSrcMacAddress_Type()
)
rlIpFftStnSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnSrcMacAddress.setStatus("current")
_RlIpFftStnOutIfIndex_Type = Integer32
_RlIpFftStnOutIfIndex_Object = MibTableColumn
rlIpFftStnOutIfIndex = _RlIpFftStnOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 8),
    _RlIpFftStnOutIfIndex_Type()
)
rlIpFftStnOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnOutIfIndex.setStatus("current")
_RlIpFftStnVid_Type = Integer32
_RlIpFftStnVid_Object = MibTableColumn
rlIpFftStnVid = _RlIpFftStnVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 9),
    _RlIpFftStnVid_Type()
)
rlIpFftStnVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnVid.setStatus("current")


class _RlIpFftStnTaggedMode_Type(Integer32):
    """Custom type rlIpFftStnTaggedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basedPortConfig", 3),
          ("tagged", 2),
          ("untagged", 1))
    )


_RlIpFftStnTaggedMode_Type.__name__ = "Integer32"
_RlIpFftStnTaggedMode_Object = MibTableColumn
rlIpFftStnTaggedMode = _RlIpFftStnTaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 10),
    _RlIpFftStnTaggedMode_Type()
)
rlIpFftStnTaggedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnTaggedMode.setStatus("current")
_RlIpFftStnAge_Type = Integer32
_RlIpFftStnAge_Object = MibTableColumn
rlIpFftStnAge = _RlIpFftStnAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 13, 1, 11),
    _RlIpFftStnAge_Type()
)
rlIpFftStnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftStnAge.setStatus("current")
_RlIpFftSubTable_Object = MibTable
rlIpFftSubTable = _RlIpFftSubTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14)
)
if mibBuilder.loadTexts:
    rlIpFftSubTable.setStatus("current")
_RlIpFftSubEntry_Object = MibTableRow
rlIpFftSubEntry = _RlIpFftSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1)
)
rlIpFftSubEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpFftSubMrid"),
    (0, "RADLAN-rlFft", "rlIpFftSubDstIpSubnet"),
    (0, "RADLAN-rlFft", "rlIpFftSubDstIpMask"),
)
if mibBuilder.loadTexts:
    rlIpFftSubEntry.setStatus("current")
_RlIpFftSubMrid_Type = Integer32
_RlIpFftSubMrid_Object = MibTableColumn
rlIpFftSubMrid = _RlIpFftSubMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 1),
    _RlIpFftSubMrid_Type()
)
rlIpFftSubMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubMrid.setStatus("current")
_RlIpFftSubDstIpSubnet_Type = IpAddress
_RlIpFftSubDstIpSubnet_Object = MibTableColumn
rlIpFftSubDstIpSubnet = _RlIpFftSubDstIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 2),
    _RlIpFftSubDstIpSubnet_Type()
)
rlIpFftSubDstIpSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubDstIpSubnet.setStatus("current")
_RlIpFftSubDstIpMask_Type = IpAddress
_RlIpFftSubDstIpMask_Object = MibTableColumn
rlIpFftSubDstIpMask = _RlIpFftSubDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 3),
    _RlIpFftSubDstIpMask_Type()
)
rlIpFftSubDstIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubDstIpMask.setStatus("current")
_RlIpFftSubAge_Type = Integer32
_RlIpFftSubAge_Object = MibTableColumn
rlIpFftSubAge = _RlIpFftSubAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 4),
    _RlIpFftSubAge_Type()
)
rlIpFftSubAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubAge.setStatus("current")
_RlIpFftSubNextHopSetRefCount_Type = Integer32
_RlIpFftSubNextHopSetRefCount_Object = MibTableColumn
rlIpFftSubNextHopSetRefCount = _RlIpFftSubNextHopSetRefCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 5),
    _RlIpFftSubNextHopSetRefCount_Type()
)
rlIpFftSubNextHopSetRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopSetRefCount.setStatus("current")
_RlIpFftSubNextHopCount_Type = Integer32
_RlIpFftSubNextHopCount_Object = MibTableColumn
rlIpFftSubNextHopCount = _RlIpFftSubNextHopCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 6),
    _RlIpFftSubNextHopCount_Type()
)
rlIpFftSubNextHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopCount.setStatus("current")
_RlIpFftSubNextHopIfindex1_Type = Integer32
_RlIpFftSubNextHopIfindex1_Object = MibTableColumn
rlIpFftSubNextHopIfindex1 = _RlIpFftSubNextHopIfindex1_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 7),
    _RlIpFftSubNextHopIfindex1_Type()
)
rlIpFftSubNextHopIfindex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIfindex1.setStatus("current")
_RlIpFftSubNextHopIpAddr1_Type = IpAddress
_RlIpFftSubNextHopIpAddr1_Object = MibTableColumn
rlIpFftSubNextHopIpAddr1 = _RlIpFftSubNextHopIpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 8),
    _RlIpFftSubNextHopIpAddr1_Type()
)
rlIpFftSubNextHopIpAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIpAddr1.setStatus("current")
_RlIpFftSubNextHopIfindex2_Type = Integer32
_RlIpFftSubNextHopIfindex2_Object = MibTableColumn
rlIpFftSubNextHopIfindex2 = _RlIpFftSubNextHopIfindex2_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 9),
    _RlIpFftSubNextHopIfindex2_Type()
)
rlIpFftSubNextHopIfindex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIfindex2.setStatus("current")
_RlIpFftSubNextHopIpAddr2_Type = IpAddress
_RlIpFftSubNextHopIpAddr2_Object = MibTableColumn
rlIpFftSubNextHopIpAddr2 = _RlIpFftSubNextHopIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 10),
    _RlIpFftSubNextHopIpAddr2_Type()
)
rlIpFftSubNextHopIpAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIpAddr2.setStatus("current")
_RlIpFftSubNextHopIfindex3_Type = Integer32
_RlIpFftSubNextHopIfindex3_Object = MibTableColumn
rlIpFftSubNextHopIfindex3 = _RlIpFftSubNextHopIfindex3_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 11),
    _RlIpFftSubNextHopIfindex3_Type()
)
rlIpFftSubNextHopIfindex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIfindex3.setStatus("current")
_RlIpFftSubNextHopIpAddr3_Type = IpAddress
_RlIpFftSubNextHopIpAddr3_Object = MibTableColumn
rlIpFftSubNextHopIpAddr3 = _RlIpFftSubNextHopIpAddr3_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 12),
    _RlIpFftSubNextHopIpAddr3_Type()
)
rlIpFftSubNextHopIpAddr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIpAddr3.setStatus("current")
_RlIpFftSubNextHopIfindex4_Type = Integer32
_RlIpFftSubNextHopIfindex4_Object = MibTableColumn
rlIpFftSubNextHopIfindex4 = _RlIpFftSubNextHopIfindex4_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 13),
    _RlIpFftSubNextHopIfindex4_Type()
)
rlIpFftSubNextHopIfindex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIfindex4.setStatus("current")
_RlIpFftSubNextHopIpAddr4_Type = IpAddress
_RlIpFftSubNextHopIpAddr4_Object = MibTableColumn
rlIpFftSubNextHopIpAddr4 = _RlIpFftSubNextHopIpAddr4_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 14),
    _RlIpFftSubNextHopIpAddr4_Type()
)
rlIpFftSubNextHopIpAddr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIpAddr4.setStatus("current")
_RlIpFftSubNextHopIfindex5_Type = Integer32
_RlIpFftSubNextHopIfindex5_Object = MibTableColumn
rlIpFftSubNextHopIfindex5 = _RlIpFftSubNextHopIfindex5_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 15),
    _RlIpFftSubNextHopIfindex5_Type()
)
rlIpFftSubNextHopIfindex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIfindex5.setStatus("current")
_RlIpFftSubNextHopIpAddr5_Type = IpAddress
_RlIpFftSubNextHopIpAddr5_Object = MibTableColumn
rlIpFftSubNextHopIpAddr5 = _RlIpFftSubNextHopIpAddr5_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 16),
    _RlIpFftSubNextHopIpAddr5_Type()
)
rlIpFftSubNextHopIpAddr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIpAddr5.setStatus("current")
_RlIpFftSubNextHopIfindex6_Type = Integer32
_RlIpFftSubNextHopIfindex6_Object = MibTableColumn
rlIpFftSubNextHopIfindex6 = _RlIpFftSubNextHopIfindex6_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 17),
    _RlIpFftSubNextHopIfindex6_Type()
)
rlIpFftSubNextHopIfindex6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIfindex6.setStatus("current")
_RlIpFftSubNextHopIpAddr6_Type = IpAddress
_RlIpFftSubNextHopIpAddr6_Object = MibTableColumn
rlIpFftSubNextHopIpAddr6 = _RlIpFftSubNextHopIpAddr6_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 18),
    _RlIpFftSubNextHopIpAddr6_Type()
)
rlIpFftSubNextHopIpAddr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIpAddr6.setStatus("current")
_RlIpFftSubNextHopIfindex7_Type = Integer32
_RlIpFftSubNextHopIfindex7_Object = MibTableColumn
rlIpFftSubNextHopIfindex7 = _RlIpFftSubNextHopIfindex7_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 19),
    _RlIpFftSubNextHopIfindex7_Type()
)
rlIpFftSubNextHopIfindex7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIfindex7.setStatus("current")
_RlIpFftSubNextHopIpAddr7_Type = IpAddress
_RlIpFftSubNextHopIpAddr7_Object = MibTableColumn
rlIpFftSubNextHopIpAddr7 = _RlIpFftSubNextHopIpAddr7_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 20),
    _RlIpFftSubNextHopIpAddr7_Type()
)
rlIpFftSubNextHopIpAddr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIpAddr7.setStatus("current")
_RlIpFftSubNextHopIfindex8_Type = Integer32
_RlIpFftSubNextHopIfindex8_Object = MibTableColumn
rlIpFftSubNextHopIfindex8 = _RlIpFftSubNextHopIfindex8_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 21),
    _RlIpFftSubNextHopIfindex8_Type()
)
rlIpFftSubNextHopIfindex8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIfindex8.setStatus("current")
_RlIpFftSubNextHopIpAddr8_Type = IpAddress
_RlIpFftSubNextHopIpAddr8_Object = MibTableColumn
rlIpFftSubNextHopIpAddr8 = _RlIpFftSubNextHopIpAddr8_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 14, 1, 22),
    _RlIpFftSubNextHopIpAddr8_Type()
)
rlIpFftSubNextHopIpAddr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSubNextHopIpAddr8.setStatus("current")
_RlIpFftCountersTable_Object = MibTable
rlIpFftCountersTable = _RlIpFftCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 15)
)
if mibBuilder.loadTexts:
    rlIpFftCountersTable.setStatus("current")
_RlIpFftCountersEntry_Object = MibTableRow
rlIpFftCountersEntry = _RlIpFftCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 15, 1)
)
rlIpFftCountersEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpFftCountersIndex"),
)
if mibBuilder.loadTexts:
    rlIpFftCountersEntry.setStatus("current")
_RlIpFftCountersIndex_Type = Integer32
_RlIpFftCountersIndex_Object = MibTableColumn
rlIpFftCountersIndex = _RlIpFftCountersIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 15, 1, 1),
    _RlIpFftCountersIndex_Type()
)
rlIpFftCountersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftCountersIndex.setStatus("current")
_RlIpFftInReceives_Type = Integer32
_RlIpFftInReceives_Object = MibTableColumn
rlIpFftInReceives = _RlIpFftInReceives_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 15, 1, 2),
    _RlIpFftInReceives_Type()
)
rlIpFftInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftInReceives.setStatus("current")
_RlIpFftForwDatagrams_Type = Integer32
_RlIpFftForwDatagrams_Object = MibTableColumn
rlIpFftForwDatagrams = _RlIpFftForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 15, 1, 3),
    _RlIpFftForwDatagrams_Type()
)
rlIpFftForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftForwDatagrams.setStatus("current")
_RlIpFftInDiscards_Type = Integer32
_RlIpFftInDiscards_Object = MibTableColumn
rlIpFftInDiscards = _RlIpFftInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 15, 1, 4),
    _RlIpFftInDiscards_Type()
)
rlIpFftInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftInDiscards.setStatus("current")
_RlIpFftNextHopTable_Object = MibTable
rlIpFftNextHopTable = _RlIpFftNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16)
)
if mibBuilder.loadTexts:
    rlIpFftNextHopTable.setStatus("current")
_RlIpFftNextHopEntry_Object = MibTableRow
rlIpFftNextHopEntry = _RlIpFftNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1)
)
rlIpFftNextHopEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpFftNextHopifindex"),
    (0, "RADLAN-rlFft", "rlIpFftNextHopIpAddress"),
)
if mibBuilder.loadTexts:
    rlIpFftNextHopEntry.setStatus("current")
_RlIpFftNextHopifindex_Type = Integer32
_RlIpFftNextHopifindex_Object = MibTableColumn
rlIpFftNextHopifindex = _RlIpFftNextHopifindex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1, 1),
    _RlIpFftNextHopifindex_Type()
)
rlIpFftNextHopifindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNextHopifindex.setStatus("current")
_RlIpFftNextHopIpAddress_Type = IpAddress
_RlIpFftNextHopIpAddress_Object = MibTableColumn
rlIpFftNextHopIpAddress = _RlIpFftNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1, 2),
    _RlIpFftNextHopIpAddress_Type()
)
rlIpFftNextHopIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNextHopIpAddress.setStatus("current")


class _RlIpFftNextHopValid_Type(Integer32):
    """Custom type rlIpFftNextHopValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_RlIpFftNextHopValid_Type.__name__ = "Integer32"
_RlIpFftNextHopValid_Object = MibTableColumn
rlIpFftNextHopValid = _RlIpFftNextHopValid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1, 3),
    _RlIpFftNextHopValid_Type()
)
rlIpFftNextHopValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNextHopValid.setStatus("current")


class _RlIpFftNextHopType_Type(Integer32):
    """Custom type rlIpFftNextHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop", 4),
          ("local", 1),
          ("reject", 3),
          ("remote", 2))
    )


_RlIpFftNextHopType_Type.__name__ = "Integer32"
_RlIpFftNextHopType_Object = MibTableColumn
rlIpFftNextHopType = _RlIpFftNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1, 4),
    _RlIpFftNextHopType_Type()
)
rlIpFftNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNextHopType.setStatus("current")
_RlIpFftNextHopReferenceCount_Type = Integer32
_RlIpFftNextHopReferenceCount_Object = MibTableColumn
rlIpFftNextHopReferenceCount = _RlIpFftNextHopReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1, 5),
    _RlIpFftNextHopReferenceCount_Type()
)
rlIpFftNextHopReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNextHopReferenceCount.setStatus("current")
_RlIpFftNextHopNetAddress_Type = PhysAddress
_RlIpFftNextHopNetAddress_Object = MibTableColumn
rlIpFftNextHopNetAddress = _RlIpFftNextHopNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1, 6),
    _RlIpFftNextHopNetAddress_Type()
)
rlIpFftNextHopNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNextHopNetAddress.setStatus("current")
_RlIpFftNextHopVid_Type = Integer32
_RlIpFftNextHopVid_Object = MibTableColumn
rlIpFftNextHopVid = _RlIpFftNextHopVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1, 7),
    _RlIpFftNextHopVid_Type()
)
rlIpFftNextHopVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNextHopVid.setStatus("current")
_RlIpFftNextHopMacAddress_Type = PhysAddress
_RlIpFftNextHopMacAddress_Object = MibTableColumn
rlIpFftNextHopMacAddress = _RlIpFftNextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1, 8),
    _RlIpFftNextHopMacAddress_Type()
)
rlIpFftNextHopMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNextHopMacAddress.setStatus("current")
_RlIpFftNextHopOutIfIndex_Type = Integer32
_RlIpFftNextHopOutIfIndex_Object = MibTableColumn
rlIpFftNextHopOutIfIndex = _RlIpFftNextHopOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 16, 1, 9),
    _RlIpFftNextHopOutIfIndex_Type()
)
rlIpFftNextHopOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftNextHopOutIfIndex.setStatus("current")
_RlIpFftL2InfoTable_Object = MibTable
rlIpFftL2InfoTable = _RlIpFftL2InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17)
)
if mibBuilder.loadTexts:
    rlIpFftL2InfoTable.setStatus("current")
_RlIpFftL2InfoEntry_Object = MibTableRow
rlIpFftL2InfoEntry = _RlIpFftL2InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1)
)
rlIpFftL2InfoEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpFftL2InfoIfindex"),
    (0, "RADLAN-rlFft", "rlIpFftL2InfoDstMacAddress"),
)
if mibBuilder.loadTexts:
    rlIpFftL2InfoEntry.setStatus("current")
_RlIpFftL2InfoIfindex_Type = Integer32
_RlIpFftL2InfoIfindex_Object = MibTableColumn
rlIpFftL2InfoIfindex = _RlIpFftL2InfoIfindex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1, 1),
    _RlIpFftL2InfoIfindex_Type()
)
rlIpFftL2InfoIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftL2InfoIfindex.setStatus("current")
_RlIpFftL2InfoDstMacAddress_Type = PhysAddress
_RlIpFftL2InfoDstMacAddress_Object = MibTableColumn
rlIpFftL2InfoDstMacAddress = _RlIpFftL2InfoDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1, 2),
    _RlIpFftL2InfoDstMacAddress_Type()
)
rlIpFftL2InfoDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftL2InfoDstMacAddress.setStatus("current")


class _RlIpFftL2InfoValid_Type(Integer32):
    """Custom type rlIpFftL2InfoValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_RlIpFftL2InfoValid_Type.__name__ = "Integer32"
_RlIpFftL2InfoValid_Object = MibTableColumn
rlIpFftL2InfoValid = _RlIpFftL2InfoValid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1, 3),
    _RlIpFftL2InfoValid_Type()
)
rlIpFftL2InfoValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftL2InfoValid.setStatus("current")


class _RlIpFftL2InfoType_Type(Integer32):
    """Custom type rlIpFftL2InfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("vlan", 2))
    )


_RlIpFftL2InfoType_Type.__name__ = "Integer32"
_RlIpFftL2InfoType_Object = MibTableColumn
rlIpFftL2InfoType = _RlIpFftL2InfoType_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1, 4),
    _RlIpFftL2InfoType_Type()
)
rlIpFftL2InfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftL2InfoType.setStatus("current")
_RlIpFftL2InfoReferenceCount_Type = Integer32
_RlIpFftL2InfoReferenceCount_Object = MibTableColumn
rlIpFftL2InfoReferenceCount = _RlIpFftL2InfoReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1, 5),
    _RlIpFftL2InfoReferenceCount_Type()
)
rlIpFftL2InfoReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftL2InfoReferenceCount.setStatus("current")
_RlIpFftL2InfoVid_Type = Integer32
_RlIpFftL2InfoVid_Object = MibTableColumn
rlIpFftL2InfoVid = _RlIpFftL2InfoVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1, 6),
    _RlIpFftL2InfoVid_Type()
)
rlIpFftL2InfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftL2InfoVid.setStatus("current")
_RlIpFftL2InfoSrcMacAddress_Type = PhysAddress
_RlIpFftL2InfoSrcMacAddress_Object = MibTableColumn
rlIpFftL2InfoSrcMacAddress = _RlIpFftL2InfoSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1, 7),
    _RlIpFftL2InfoSrcMacAddress_Type()
)
rlIpFftL2InfoSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftL2InfoSrcMacAddress.setStatus("current")
_RlIpFftL2InfoOutIfIndex_Type = Integer32
_RlIpFftL2InfoOutIfIndex_Object = MibTableColumn
rlIpFftL2InfoOutIfIndex = _RlIpFftL2InfoOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1, 8),
    _RlIpFftL2InfoOutIfIndex_Type()
)
rlIpFftL2InfoOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftL2InfoOutIfIndex.setStatus("current")


class _RlIpFftL2InfoTaggedMode_Type(Integer32):
    """Custom type rlIpFftL2InfoTaggedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basedPortConfig", 3),
          ("tagged", 2),
          ("untagged", 1))
    )


_RlIpFftL2InfoTaggedMode_Type.__name__ = "Integer32"
_RlIpFftL2InfoTaggedMode_Object = MibTableColumn
rlIpFftL2InfoTaggedMode = _RlIpFftL2InfoTaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 1, 17, 1, 9),
    _RlIpFftL2InfoTaggedMode_Type()
)
rlIpFftL2InfoTaggedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftL2InfoTaggedMode.setStatus("current")
_RlIpxFFT_ObjectIdentity = ObjectIdentity
rlIpxFFT = _RlIpxFFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 47, 2)
)
_RlIpxFftMibVersion_Type = Integer32
_RlIpxFftMibVersion_Object = MibScalar
rlIpxFftMibVersion = _RlIpxFftMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 1),
    _RlIpxFftMibVersion_Type()
)
rlIpxFftMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftMibVersion.setStatus("current")
_RlIpxMaxFftNumber_Type = Integer32
_RlIpxMaxFftNumber_Object = MibScalar
rlIpxMaxFftNumber = _RlIpxMaxFftNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 2),
    _RlIpxMaxFftNumber_Type()
)
rlIpxMaxFftNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxMaxFftNumber.setStatus("current")


class _RlIpxFftDynamicSupported_Type(Integer32):
    """Custom type rlIpxFftDynamicSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlIpxFftDynamicSupported_Type.__name__ = "Integer32"
_RlIpxFftDynamicSupported_Object = MibScalar
rlIpxFftDynamicSupported = _RlIpxFftDynamicSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 3),
    _RlIpxFftDynamicSupported_Type()
)
rlIpxFftDynamicSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftDynamicSupported.setStatus("current")


class _RlIpxFftNetworkSupported_Type(Integer32):
    """Custom type rlIpxFftNetworkSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlIpxFftNetworkSupported_Type.__name__ = "Integer32"
_RlIpxFftNetworkSupported_Object = MibScalar
rlIpxFftNetworkSupported = _RlIpxFftNetworkSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 4),
    _RlIpxFftNetworkSupported_Type()
)
rlIpxFftNetworkSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftNetworkSupported.setStatus("current")


class _RlIpxFftUnknownAddrMsgUsed_Type(Integer32):
    """Custom type rlIpxFftUnknownAddrMsgUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 2),
          ("used", 1))
    )


_RlIpxFftUnknownAddrMsgUsed_Type.__name__ = "Integer32"
_RlIpxFftUnknownAddrMsgUsed_Object = MibScalar
rlIpxFftUnknownAddrMsgUsed = _RlIpxFftUnknownAddrMsgUsed_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 5),
    _RlIpxFftUnknownAddrMsgUsed_Type()
)
rlIpxFftUnknownAddrMsgUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftUnknownAddrMsgUsed.setStatus("current")


class _RlIpxFftAgingTimeSupported_Type(Integer32):
    """Custom type rlIpxFftAgingTimeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlIpxFftAgingTimeSupported_Type.__name__ = "Integer32"
_RlIpxFftAgingTimeSupported_Object = MibScalar
rlIpxFftAgingTimeSupported = _RlIpxFftAgingTimeSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 6),
    _RlIpxFftAgingTimeSupported_Type()
)
rlIpxFftAgingTimeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftAgingTimeSupported.setStatus("current")


class _RlIpxFftSrcAddrSupported_Type(Integer32):
    """Custom type rlIpxFftSrcAddrSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlIpxFftSrcAddrSupported_Type.__name__ = "Integer32"
_RlIpxFftSrcAddrSupported_Object = MibScalar
rlIpxFftSrcAddrSupported = _RlIpxFftSrcAddrSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 7),
    _RlIpxFftSrcAddrSupported_Type()
)
rlIpxFftSrcAddrSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSrcAddrSupported.setStatus("current")
_RlIpxFftAgingTimeout_Type = Integer32
_RlIpxFftAgingTimeout_Object = MibScalar
rlIpxFftAgingTimeout = _RlIpxFftAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 8),
    _RlIpxFftAgingTimeout_Type()
)
rlIpxFftAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpxFftAgingTimeout.setStatus("current")


class _RlIpxFftRedBoundary_Type(Integer32):
    """Custom type rlIpxFftRedBoundary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RlIpxFftRedBoundary_Type.__name__ = "Integer32"
_RlIpxFftRedBoundary_Object = MibScalar
rlIpxFftRedBoundary = _RlIpxFftRedBoundary_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 9),
    _RlIpxFftRedBoundary_Type()
)
rlIpxFftRedBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpxFftRedBoundary.setStatus("current")
_RlIpxFftYellowBoundary_Type = Percents
_RlIpxFftYellowBoundary_Object = MibScalar
rlIpxFftYellowBoundary = _RlIpxFftYellowBoundary_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 10),
    _RlIpxFftYellowBoundary_Type()
)
rlIpxFftYellowBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpxFftYellowBoundary.setStatus("current")
_RlIpxFftNumTable_Object = MibTable
rlIpxFftNumTable = _RlIpxFftNumTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 12)
)
if mibBuilder.loadTexts:
    rlIpxFftNumTable.setStatus("current")
_RlIpxFftNumEntry_Object = MibTableRow
rlIpxFftNumEntry = _RlIpxFftNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 12, 1)
)
rlIpxFftNumEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpxFftNumIndex"),
)
if mibBuilder.loadTexts:
    rlIpxFftNumEntry.setStatus("current")
_RlIpxFftNumIndex_Type = Integer32
_RlIpxFftNumIndex_Object = MibTableColumn
rlIpxFftNumIndex = _RlIpxFftNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 12, 1, 1),
    _RlIpxFftNumIndex_Type()
)
rlIpxFftNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftNumIndex.setStatus("current")
_RlIpxFftNumStnRoutesNumber_Type = Integer32
_RlIpxFftNumStnRoutesNumber_Object = MibTableColumn
rlIpxFftNumStnRoutesNumber = _RlIpxFftNumStnRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 12, 1, 2),
    _RlIpxFftNumStnRoutesNumber_Type()
)
rlIpxFftNumStnRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftNumStnRoutesNumber.setStatus("current")
_RlIpxFftNumSubRoutesNumber_Type = Integer32
_RlIpxFftNumSubRoutesNumber_Object = MibTableColumn
rlIpxFftNumSubRoutesNumber = _RlIpxFftNumSubRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 12, 1, 3),
    _RlIpxFftNumSubRoutesNumber_Type()
)
rlIpxFftNumSubRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftNumSubRoutesNumber.setStatus("current")
_RlIpxFftStnTable_Object = MibTable
rlIpxFftStnTable = _RlIpxFftStnTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13)
)
if mibBuilder.loadTexts:
    rlIpxFftStnTable.setStatus("current")
_RlIpxFftStnEntry_Object = MibTableRow
rlIpxFftStnEntry = _RlIpxFftStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1)
)
rlIpxFftStnEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpxFftStnIndex"),
    (0, "RADLAN-rlFft", "rlIpxFftStnDstNetid"),
    (0, "RADLAN-rlFft", "rlIpxFftStnDstNode"),
    (0, "RADLAN-rlFft", "rlIpxFftStnSrcNetid"),
    (0, "RADLAN-rlFft", "rlIpxFftStnSrcNode"),
)
if mibBuilder.loadTexts:
    rlIpxFftStnEntry.setStatus("current")
_RlIpxFftStnIndex_Type = Integer32
_RlIpxFftStnIndex_Object = MibTableColumn
rlIpxFftStnIndex = _RlIpxFftStnIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 1),
    _RlIpxFftStnIndex_Type()
)
rlIpxFftStnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnIndex.setStatus("current")
_RlIpxFftStnDstNetid_Type = NetNumber
_RlIpxFftStnDstNetid_Object = MibTableColumn
rlIpxFftStnDstNetid = _RlIpxFftStnDstNetid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 2),
    _RlIpxFftStnDstNetid_Type()
)
rlIpxFftStnDstNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnDstNetid.setStatus("current")
_RlIpxFftStnDstNode_Type = PhysAddress
_RlIpxFftStnDstNode_Object = MibTableColumn
rlIpxFftStnDstNode = _RlIpxFftStnDstNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 3),
    _RlIpxFftStnDstNode_Type()
)
rlIpxFftStnDstNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnDstNode.setStatus("current")
_RlIpxFftStnSrcNetid_Type = NetNumber
_RlIpxFftStnSrcNetid_Object = MibTableColumn
rlIpxFftStnSrcNetid = _RlIpxFftStnSrcNetid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 4),
    _RlIpxFftStnSrcNetid_Type()
)
rlIpxFftStnSrcNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnSrcNetid.setStatus("current")
_RlIpxFftStnSrcNode_Type = PhysAddress
_RlIpxFftStnSrcNode_Object = MibTableColumn
rlIpxFftStnSrcNode = _RlIpxFftStnSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 5),
    _RlIpxFftStnSrcNode_Type()
)
rlIpxFftStnSrcNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnSrcNode.setStatus("current")


class _RlIpxFftStnDstIpxAddrType_Type(Integer32):
    """Custom type rlIpxFftStnDstIpxAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_RlIpxFftStnDstIpxAddrType_Type.__name__ = "Integer32"
_RlIpxFftStnDstIpxAddrType_Object = MibTableColumn
rlIpxFftStnDstIpxAddrType = _RlIpxFftStnDstIpxAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 6),
    _RlIpxFftStnDstIpxAddrType_Type()
)
rlIpxFftStnDstIpxAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnDstIpxAddrType.setStatus("current")


class _RlIpxFftStnEncapsulation_Type(Integer32):
    """Custom type rlIpxFftStnEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("llc", 3),
          ("novell", 1),
          ("snap", 4))
    )


_RlIpxFftStnEncapsulation_Type.__name__ = "Integer32"
_RlIpxFftStnEncapsulation_Object = MibTableColumn
rlIpxFftStnEncapsulation = _RlIpxFftStnEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 7),
    _RlIpxFftStnEncapsulation_Type()
)
rlIpxFftStnEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnEncapsulation.setStatus("current")
_RlIpxFftStnDstMacAddress_Type = PhysAddress
_RlIpxFftStnDstMacAddress_Object = MibTableColumn
rlIpxFftStnDstMacAddress = _RlIpxFftStnDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 8),
    _RlIpxFftStnDstMacAddress_Type()
)
rlIpxFftStnDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnDstMacAddress.setStatus("current")
_RlIpxFftStnSrcMacAddress_Type = PhysAddress
_RlIpxFftStnSrcMacAddress_Object = MibTableColumn
rlIpxFftStnSrcMacAddress = _RlIpxFftStnSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 9),
    _RlIpxFftStnSrcMacAddress_Type()
)
rlIpxFftStnSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnSrcMacAddress.setStatus("current")
_RlIpxFftStnOutIfIndex_Type = Integer32
_RlIpxFftStnOutIfIndex_Object = MibTableColumn
rlIpxFftStnOutIfIndex = _RlIpxFftStnOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 10),
    _RlIpxFftStnOutIfIndex_Type()
)
rlIpxFftStnOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnOutIfIndex.setStatus("current")
_RlIpxFftStnTci_Type = Integer32
_RlIpxFftStnTci_Object = MibTableColumn
rlIpxFftStnTci = _RlIpxFftStnTci_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 11),
    _RlIpxFftStnTci_Type()
)
rlIpxFftStnTci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnTci.setStatus("current")
_RlIpxFftStnFacsIndex_Type = Integer32
_RlIpxFftStnFacsIndex_Object = MibTableColumn
rlIpxFftStnFacsIndex = _RlIpxFftStnFacsIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 12),
    _RlIpxFftStnFacsIndex_Type()
)
rlIpxFftStnFacsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnFacsIndex.setStatus("current")
_RlIpxFftStnAge_Type = Integer32
_RlIpxFftStnAge_Object = MibTableColumn
rlIpxFftStnAge = _RlIpxFftStnAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 13, 1, 13),
    _RlIpxFftStnAge_Type()
)
rlIpxFftStnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnAge.setStatus("current")
_RlIpxFftSubTable_Object = MibTable
rlIpxFftSubTable = _RlIpxFftSubTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14)
)
if mibBuilder.loadTexts:
    rlIpxFftSubTable.setStatus("current")
_RlIpxFftSubEntry_Object = MibTableRow
rlIpxFftSubEntry = _RlIpxFftSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1)
)
rlIpxFftSubEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpxFftSubIndex"),
    (0, "RADLAN-rlFft", "rlIpxFftSubDstNetid"),
)
if mibBuilder.loadTexts:
    rlIpxFftSubEntry.setStatus("current")
_RlIpxFftSubIndex_Type = Integer32
_RlIpxFftSubIndex_Object = MibTableColumn
rlIpxFftSubIndex = _RlIpxFftSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1, 1),
    _RlIpxFftSubIndex_Type()
)
rlIpxFftSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubIndex.setStatus("current")
_RlIpxFftSubDstNetid_Type = NetNumber
_RlIpxFftSubDstNetid_Object = MibTableColumn
rlIpxFftSubDstNetid = _RlIpxFftSubDstNetid_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1, 2),
    _RlIpxFftSubDstNetid_Type()
)
rlIpxFftSubDstNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubDstNetid.setStatus("current")


class _RlIpxFftSubEncapsulation_Type(Integer32):
    """Custom type rlIpxFftSubEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("llc", 3),
          ("novell", 1),
          ("snap", 4))
    )


_RlIpxFftSubEncapsulation_Type.__name__ = "Integer32"
_RlIpxFftSubEncapsulation_Object = MibTableColumn
rlIpxFftSubEncapsulation = _RlIpxFftSubEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1, 3),
    _RlIpxFftSubEncapsulation_Type()
)
rlIpxFftSubEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubEncapsulation.setStatus("current")
_RlIpxFftSubDstMacAddress_Type = PhysAddress
_RlIpxFftSubDstMacAddress_Object = MibTableColumn
rlIpxFftSubDstMacAddress = _RlIpxFftSubDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1, 4),
    _RlIpxFftSubDstMacAddress_Type()
)
rlIpxFftSubDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubDstMacAddress.setStatus("current")
_RlIpxFftSubSrcMacAddress_Type = PhysAddress
_RlIpxFftSubSrcMacAddress_Object = MibTableColumn
rlIpxFftSubSrcMacAddress = _RlIpxFftSubSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1, 5),
    _RlIpxFftSubSrcMacAddress_Type()
)
rlIpxFftSubSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubSrcMacAddress.setStatus("current")
_RlIpxFftSubOutIfIndex_Type = Integer32
_RlIpxFftSubOutIfIndex_Object = MibTableColumn
rlIpxFftSubOutIfIndex = _RlIpxFftSubOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1, 6),
    _RlIpxFftSubOutIfIndex_Type()
)
rlIpxFftSubOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubOutIfIndex.setStatus("current")
_RlIpxFftSubTci_Type = Integer32
_RlIpxFftSubTci_Object = MibTableColumn
rlIpxFftSubTci = _RlIpxFftSubTci_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1, 7),
    _RlIpxFftSubTci_Type()
)
rlIpxFftSubTci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubTci.setStatus("current")
_RlIpxFftSubFacsIndex_Type = Integer32
_RlIpxFftSubFacsIndex_Object = MibTableColumn
rlIpxFftSubFacsIndex = _RlIpxFftSubFacsIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1, 8),
    _RlIpxFftSubFacsIndex_Type()
)
rlIpxFftSubFacsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubFacsIndex.setStatus("current")
_RlIpxFftSubAge_Type = Integer32
_RlIpxFftSubAge_Object = MibTableColumn
rlIpxFftSubAge = _RlIpxFftSubAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 14, 1, 9),
    _RlIpxFftSubAge_Type()
)
rlIpxFftSubAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubAge.setStatus("current")
_RlIpxFftCountersTable_Object = MibTable
rlIpxFftCountersTable = _RlIpxFftCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 15)
)
if mibBuilder.loadTexts:
    rlIpxFftCountersTable.setStatus("current")
_RlIpxFftCountersEntry_Object = MibTableRow
rlIpxFftCountersEntry = _RlIpxFftCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 15, 1)
)
rlIpxFftCountersEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpxFftCountersIndex"),
)
if mibBuilder.loadTexts:
    rlIpxFftCountersEntry.setStatus("current")
_RlIpxFftCountersIndex_Type = Integer32
_RlIpxFftCountersIndex_Object = MibTableColumn
rlIpxFftCountersIndex = _RlIpxFftCountersIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 15, 1, 1),
    _RlIpxFftCountersIndex_Type()
)
rlIpxFftCountersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftCountersIndex.setStatus("current")
_RlIpxFftInReceives_Type = Integer32
_RlIpxFftInReceives_Object = MibTableColumn
rlIpxFftInReceives = _RlIpxFftInReceives_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 15, 1, 2),
    _RlIpxFftInReceives_Type()
)
rlIpxFftInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftInReceives.setStatus("current")
_RlIpxFftForwDatagrams_Type = Integer32
_RlIpxFftForwDatagrams_Object = MibTableColumn
rlIpxFftForwDatagrams = _RlIpxFftForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 15, 1, 3),
    _RlIpxFftForwDatagrams_Type()
)
rlIpxFftForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftForwDatagrams.setStatus("current")
_RlIpxFftInDiscards_Type = Integer32
_RlIpxFftInDiscards_Object = MibTableColumn
rlIpxFftInDiscards = _RlIpxFftInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 2, 15, 1, 4),
    _RlIpxFftInDiscards_Type()
)
rlIpxFftInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftInDiscards.setStatus("current")
_RlIpmFFT_ObjectIdentity = ObjectIdentity
rlIpmFFT = _RlIpmFFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 47, 3)
)
_RlIpmFftMibVersion_Type = Integer32
_RlIpmFftMibVersion_Object = MibScalar
rlIpmFftMibVersion = _RlIpmFftMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 1),
    _RlIpmFftMibVersion_Type()
)
rlIpmFftMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftMibVersion.setStatus("current")
_RlIpmMaxFftNumber_Type = Integer32
_RlIpmMaxFftNumber_Object = MibScalar
rlIpmMaxFftNumber = _RlIpmMaxFftNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 2),
    _RlIpmMaxFftNumber_Type()
)
rlIpmMaxFftNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmMaxFftNumber.setStatus("current")


class _RlIpmFftDynamicSupported_Type(Integer32):
    """Custom type rlIpmFftDynamicSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlIpmFftDynamicSupported_Type.__name__ = "Integer32"
_RlIpmFftDynamicSupported_Object = MibScalar
rlIpmFftDynamicSupported = _RlIpmFftDynamicSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 3),
    _RlIpmFftDynamicSupported_Type()
)
rlIpmFftDynamicSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftDynamicSupported.setStatus("current")


class _RlIpmFftUnknownAddrMsgUsed_Type(Integer32):
    """Custom type rlIpmFftUnknownAddrMsgUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 2),
          ("used", 1))
    )


_RlIpmFftUnknownAddrMsgUsed_Type.__name__ = "Integer32"
_RlIpmFftUnknownAddrMsgUsed_Object = MibScalar
rlIpmFftUnknownAddrMsgUsed = _RlIpmFftUnknownAddrMsgUsed_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 4),
    _RlIpmFftUnknownAddrMsgUsed_Type()
)
rlIpmFftUnknownAddrMsgUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftUnknownAddrMsgUsed.setStatus("current")
_RlIpmFftUserAgingTimeout_Type = Unsigned32
_RlIpmFftUserAgingTimeout_Object = MibScalar
rlIpmFftUserAgingTimeout = _RlIpmFftUserAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 5),
    _RlIpmFftUserAgingTimeout_Type()
)
rlIpmFftUserAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpmFftUserAgingTimeout.setStatus("current")
_RlIpmFftRouterAgingTimeout_Type = Integer32
_RlIpmFftRouterAgingTimeout_Object = MibScalar
rlIpmFftRouterAgingTimeout = _RlIpmFftRouterAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 6),
    _RlIpmFftRouterAgingTimeout_Type()
)
rlIpmFftRouterAgingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftRouterAgingTimeout.setStatus("current")
_RlIpmFftNumTable_Object = MibTable
rlIpmFftNumTable = _RlIpmFftNumTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 8)
)
if mibBuilder.loadTexts:
    rlIpmFftNumTable.setStatus("current")
_RlIpmFftNumEntry_Object = MibTableRow
rlIpmFftNumEntry = _RlIpmFftNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 8, 1)
)
rlIpmFftNumEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpmFftNumIndex"),
)
if mibBuilder.loadTexts:
    rlIpmFftNumEntry.setStatus("current")
_RlIpmFftNumIndex_Type = Integer32
_RlIpmFftNumIndex_Object = MibTableColumn
rlIpmFftNumIndex = _RlIpmFftNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 8, 1, 1),
    _RlIpmFftNumIndex_Type()
)
rlIpmFftNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftNumIndex.setStatus("current")
_RlIpmFftNumRoutesNumber_Type = Integer32
_RlIpmFftNumRoutesNumber_Object = MibTableColumn
rlIpmFftNumRoutesNumber = _RlIpmFftNumRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 8, 1, 2),
    _RlIpmFftNumRoutesNumber_Type()
)
rlIpmFftNumRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftNumRoutesNumber.setStatus("current")
_RlIpmFftTable_Object = MibTable
rlIpmFftTable = _RlIpmFftTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9)
)
if mibBuilder.loadTexts:
    rlIpmFftTable.setStatus("current")
_RlIpmFftEntry_Object = MibTableRow
rlIpmFftEntry = _RlIpmFftEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1)
)
rlIpmFftEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpmFftIndex"),
    (0, "RADLAN-rlFft", "rlIpmFftSrcIpAddress"),
    (0, "RADLAN-rlFft", "rlIpmFftDstIpAddress"),
)
if mibBuilder.loadTexts:
    rlIpmFftEntry.setStatus("current")
_RlIpmFftIndex_Type = Integer32
_RlIpmFftIndex_Object = MibTableColumn
rlIpmFftIndex = _RlIpmFftIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1, 1),
    _RlIpmFftIndex_Type()
)
rlIpmFftIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftIndex.setStatus("current")
_RlIpmFftSrcIpAddress_Type = IpAddress
_RlIpmFftSrcIpAddress_Object = MibTableColumn
rlIpmFftSrcIpAddress = _RlIpmFftSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1, 2),
    _RlIpmFftSrcIpAddress_Type()
)
rlIpmFftSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftSrcIpAddress.setStatus("current")
_RlIpmFftDstIpAddress_Type = IpAddress
_RlIpmFftDstIpAddress_Object = MibTableColumn
rlIpmFftDstIpAddress = _RlIpmFftDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1, 3),
    _RlIpmFftDstIpAddress_Type()
)
rlIpmFftDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftDstIpAddress.setStatus("current")
_RlIpmFftSrcIpMask_Type = IpAddress
_RlIpmFftSrcIpMask_Object = MibTableColumn
rlIpmFftSrcIpMask = _RlIpmFftSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1, 4),
    _RlIpmFftSrcIpMask_Type()
)
rlIpmFftSrcIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftSrcIpMask.setStatus("current")
_RlIpmFftInputIfIndex_Type = Integer32
_RlIpmFftInputIfIndex_Object = MibTableColumn
rlIpmFftInputIfIndex = _RlIpmFftInputIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1, 5),
    _RlIpmFftInputIfIndex_Type()
)
rlIpmFftInputIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftInputIfIndex.setStatus("current")
_RlIpmFftInputVlanTag_Type = Integer32
_RlIpmFftInputVlanTag_Object = MibTableColumn
rlIpmFftInputVlanTag = _RlIpmFftInputVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1, 6),
    _RlIpmFftInputVlanTag_Type()
)
rlIpmFftInputVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftInputVlanTag.setStatus("current")


class _RlIpmFftForwardAction_Type(Integer32):
    """Custom type rlIpmFftForwardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_RlIpmFftForwardAction_Type.__name__ = "Integer32"
_RlIpmFftForwardAction_Object = MibTableColumn
rlIpmFftForwardAction = _RlIpmFftForwardAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1, 7),
    _RlIpmFftForwardAction_Type()
)
rlIpmFftForwardAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftForwardAction.setStatus("current")


class _RlIpmFftInportAction_Type(Integer32):
    """Custom type rlIpmFftInportAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("sentToCPU", 1))
    )


_RlIpmFftInportAction_Type.__name__ = "Integer32"
_RlIpmFftInportAction_Object = MibTableColumn
rlIpmFftInportAction = _RlIpmFftInportAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1, 8),
    _RlIpmFftInportAction_Type()
)
rlIpmFftInportAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftInportAction.setStatus("current")
_RlIpmFftAge_Type = Integer32
_RlIpmFftAge_Object = MibTableColumn
rlIpmFftAge = _RlIpmFftAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 9, 1, 9),
    _RlIpmFftAge_Type()
)
rlIpmFftAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftAge.setStatus("current")
_RlIpmFftPortTagTable_Object = MibTable
rlIpmFftPortTagTable = _RlIpmFftPortTagTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 10)
)
if mibBuilder.loadTexts:
    rlIpmFftPortTagTable.setStatus("current")
_RlIpmFftPortTagEntry_Object = MibTableRow
rlIpmFftPortTagEntry = _RlIpmFftPortTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 10, 1)
)
rlIpmFftPortTagEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpmFftPortIndex"),
    (0, "RADLAN-rlFft", "rlIpmFftPortSrcIpAddress"),
    (0, "RADLAN-rlFft", "rlIpmFftPortDstIpAddress"),
    (0, "RADLAN-rlFft", "rlIpmFftPortOutputifIndex"),
    (0, "RADLAN-rlFft", "rlIpmFftPortOutputTag"),
)
if mibBuilder.loadTexts:
    rlIpmFftPortTagEntry.setStatus("current")
_RlIpmFftPortIndex_Type = Integer32
_RlIpmFftPortIndex_Object = MibTableColumn
rlIpmFftPortIndex = _RlIpmFftPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 10, 1, 1),
    _RlIpmFftPortIndex_Type()
)
rlIpmFftPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortIndex.setStatus("current")
_RlIpmFftPortSrcIpAddress_Type = IpAddress
_RlIpmFftPortSrcIpAddress_Object = MibTableColumn
rlIpmFftPortSrcIpAddress = _RlIpmFftPortSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 10, 1, 2),
    _RlIpmFftPortSrcIpAddress_Type()
)
rlIpmFftPortSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortSrcIpAddress.setStatus("current")
_RlIpmFftPortDstIpAddress_Type = IpAddress
_RlIpmFftPortDstIpAddress_Object = MibTableColumn
rlIpmFftPortDstIpAddress = _RlIpmFftPortDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 10, 1, 3),
    _RlIpmFftPortDstIpAddress_Type()
)
rlIpmFftPortDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortDstIpAddress.setStatus("current")
_RlIpmFftPortOutputifIndex_Type = Integer32
_RlIpmFftPortOutputifIndex_Object = MibTableColumn
rlIpmFftPortOutputifIndex = _RlIpmFftPortOutputifIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 10, 1, 4),
    _RlIpmFftPortOutputifIndex_Type()
)
rlIpmFftPortOutputifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortOutputifIndex.setStatus("current")
_RlIpmFftPortOutputTag_Type = Integer32
_RlIpmFftPortOutputTag_Object = MibTableColumn
rlIpmFftPortOutputTag = _RlIpmFftPortOutputTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 10, 1, 5),
    _RlIpmFftPortOutputTag_Type()
)
rlIpmFftPortOutputTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortOutputTag.setStatus("current")
_RlIpmFftCountersTable_Object = MibTable
rlIpmFftCountersTable = _RlIpmFftCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 11)
)
if mibBuilder.loadTexts:
    rlIpmFftCountersTable.setStatus("current")
_RlIpmFftCountersEntry_Object = MibTableRow
rlIpmFftCountersEntry = _RlIpmFftCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 11, 1)
)
rlIpmFftCountersEntry.setIndexNames(
    (0, "RADLAN-rlFft", "rlIpmFftCountersIndex"),
)
if mibBuilder.loadTexts:
    rlIpmFftCountersEntry.setStatus("current")
_RlIpmFftCountersIndex_Type = Integer32
_RlIpmFftCountersIndex_Object = MibTableColumn
rlIpmFftCountersIndex = _RlIpmFftCountersIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 11, 1, 1),
    _RlIpmFftCountersIndex_Type()
)
rlIpmFftCountersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftCountersIndex.setStatus("current")
_RlIpmFftInReceives_Type = Integer32
_RlIpmFftInReceives_Object = MibTableColumn
rlIpmFftInReceives = _RlIpmFftInReceives_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 11, 1, 2),
    _RlIpmFftInReceives_Type()
)
rlIpmFftInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftInReceives.setStatus("current")
_RlIpmFftForwDatagrams_Type = Integer32
_RlIpmFftForwDatagrams_Object = MibTableColumn
rlIpmFftForwDatagrams = _RlIpmFftForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 11, 1, 3),
    _RlIpmFftForwDatagrams_Type()
)
rlIpmFftForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftForwDatagrams.setStatus("current")
_RlIpmFftInDiscards_Type = Integer32
_RlIpmFftInDiscards_Object = MibTableColumn
rlIpmFftInDiscards = _RlIpmFftInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 47, 3, 11, 1, 4),
    _RlIpmFftInDiscards_Type()
)
rlIpmFftInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftInDiscards.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-rlFft",
    **{"Percents": Percents,
       "NetNumber": NetNumber,
       "rlFFT": rlFFT,
       "rlIpFFT": rlIpFFT,
       "rlIpFftMibVersion": rlIpFftMibVersion,
       "rlIpMaxFftNumber": rlIpMaxFftNumber,
       "rlIpFftDynamicSupported": rlIpFftDynamicSupported,
       "rlIpFftSubnetSupported": rlIpFftSubnetSupported,
       "rlIpFftUnknownAddrMsgUsed": rlIpFftUnknownAddrMsgUsed,
       "rlIpFftAgingTimeSupported": rlIpFftAgingTimeSupported,
       "rlIpFftSrcAddrSupported": rlIpFftSrcAddrSupported,
       "rlIpFftAgingTimeout": rlIpFftAgingTimeout,
       "rlIpFftRedBoundary": rlIpFftRedBoundary,
       "rlIpFftYellowBoundary": rlIpFftYellowBoundary,
       "rlIpFftNumTable": rlIpFftNumTable,
       "rlIpFftNumEntry": rlIpFftNumEntry,
       "rlIpFftNumIndex": rlIpFftNumIndex,
       "rlIpFftNumStnRoutesNumber": rlIpFftNumStnRoutesNumber,
       "rlIpFftNumSubRoutesNumber": rlIpFftNumSubRoutesNumber,
       "rlIpFftStnTable": rlIpFftStnTable,
       "rlIpFftStnEntry": rlIpFftStnEntry,
       "rlIpFftStnIndex": rlIpFftStnIndex,
       "rlIpFftStnMrid": rlIpFftStnMrid,
       "rlIpFftStnDstIpAddress": rlIpFftStnDstIpAddress,
       "rlIpFftStnDstRouteIpMask": rlIpFftStnDstRouteIpMask,
       "rlIpFftStnDstIpAddrType": rlIpFftStnDstIpAddrType,
       "rlIpFftStnDstMacAddress": rlIpFftStnDstMacAddress,
       "rlIpFftStnSrcMacAddress": rlIpFftStnSrcMacAddress,
       "rlIpFftStnOutIfIndex": rlIpFftStnOutIfIndex,
       "rlIpFftStnVid": rlIpFftStnVid,
       "rlIpFftStnTaggedMode": rlIpFftStnTaggedMode,
       "rlIpFftStnAge": rlIpFftStnAge,
       "rlIpFftSubTable": rlIpFftSubTable,
       "rlIpFftSubEntry": rlIpFftSubEntry,
       "rlIpFftSubMrid": rlIpFftSubMrid,
       "rlIpFftSubDstIpSubnet": rlIpFftSubDstIpSubnet,
       "rlIpFftSubDstIpMask": rlIpFftSubDstIpMask,
       "rlIpFftSubAge": rlIpFftSubAge,
       "rlIpFftSubNextHopSetRefCount": rlIpFftSubNextHopSetRefCount,
       "rlIpFftSubNextHopCount": rlIpFftSubNextHopCount,
       "rlIpFftSubNextHopIfindex1": rlIpFftSubNextHopIfindex1,
       "rlIpFftSubNextHopIpAddr1": rlIpFftSubNextHopIpAddr1,
       "rlIpFftSubNextHopIfindex2": rlIpFftSubNextHopIfindex2,
       "rlIpFftSubNextHopIpAddr2": rlIpFftSubNextHopIpAddr2,
       "rlIpFftSubNextHopIfindex3": rlIpFftSubNextHopIfindex3,
       "rlIpFftSubNextHopIpAddr3": rlIpFftSubNextHopIpAddr3,
       "rlIpFftSubNextHopIfindex4": rlIpFftSubNextHopIfindex4,
       "rlIpFftSubNextHopIpAddr4": rlIpFftSubNextHopIpAddr4,
       "rlIpFftSubNextHopIfindex5": rlIpFftSubNextHopIfindex5,
       "rlIpFftSubNextHopIpAddr5": rlIpFftSubNextHopIpAddr5,
       "rlIpFftSubNextHopIfindex6": rlIpFftSubNextHopIfindex6,
       "rlIpFftSubNextHopIpAddr6": rlIpFftSubNextHopIpAddr6,
       "rlIpFftSubNextHopIfindex7": rlIpFftSubNextHopIfindex7,
       "rlIpFftSubNextHopIpAddr7": rlIpFftSubNextHopIpAddr7,
       "rlIpFftSubNextHopIfindex8": rlIpFftSubNextHopIfindex8,
       "rlIpFftSubNextHopIpAddr8": rlIpFftSubNextHopIpAddr8,
       "rlIpFftCountersTable": rlIpFftCountersTable,
       "rlIpFftCountersEntry": rlIpFftCountersEntry,
       "rlIpFftCountersIndex": rlIpFftCountersIndex,
       "rlIpFftInReceives": rlIpFftInReceives,
       "rlIpFftForwDatagrams": rlIpFftForwDatagrams,
       "rlIpFftInDiscards": rlIpFftInDiscards,
       "rlIpFftNextHopTable": rlIpFftNextHopTable,
       "rlIpFftNextHopEntry": rlIpFftNextHopEntry,
       "rlIpFftNextHopifindex": rlIpFftNextHopifindex,
       "rlIpFftNextHopIpAddress": rlIpFftNextHopIpAddress,
       "rlIpFftNextHopValid": rlIpFftNextHopValid,
       "rlIpFftNextHopType": rlIpFftNextHopType,
       "rlIpFftNextHopReferenceCount": rlIpFftNextHopReferenceCount,
       "rlIpFftNextHopNetAddress": rlIpFftNextHopNetAddress,
       "rlIpFftNextHopVid": rlIpFftNextHopVid,
       "rlIpFftNextHopMacAddress": rlIpFftNextHopMacAddress,
       "rlIpFftNextHopOutIfIndex": rlIpFftNextHopOutIfIndex,
       "rlIpFftL2InfoTable": rlIpFftL2InfoTable,
       "rlIpFftL2InfoEntry": rlIpFftL2InfoEntry,
       "rlIpFftL2InfoIfindex": rlIpFftL2InfoIfindex,
       "rlIpFftL2InfoDstMacAddress": rlIpFftL2InfoDstMacAddress,
       "rlIpFftL2InfoValid": rlIpFftL2InfoValid,
       "rlIpFftL2InfoType": rlIpFftL2InfoType,
       "rlIpFftL2InfoReferenceCount": rlIpFftL2InfoReferenceCount,
       "rlIpFftL2InfoVid": rlIpFftL2InfoVid,
       "rlIpFftL2InfoSrcMacAddress": rlIpFftL2InfoSrcMacAddress,
       "rlIpFftL2InfoOutIfIndex": rlIpFftL2InfoOutIfIndex,
       "rlIpFftL2InfoTaggedMode": rlIpFftL2InfoTaggedMode,
       "rlIpxFFT": rlIpxFFT,
       "rlIpxFftMibVersion": rlIpxFftMibVersion,
       "rlIpxMaxFftNumber": rlIpxMaxFftNumber,
       "rlIpxFftDynamicSupported": rlIpxFftDynamicSupported,
       "rlIpxFftNetworkSupported": rlIpxFftNetworkSupported,
       "rlIpxFftUnknownAddrMsgUsed": rlIpxFftUnknownAddrMsgUsed,
       "rlIpxFftAgingTimeSupported": rlIpxFftAgingTimeSupported,
       "rlIpxFftSrcAddrSupported": rlIpxFftSrcAddrSupported,
       "rlIpxFftAgingTimeout": rlIpxFftAgingTimeout,
       "rlIpxFftRedBoundary": rlIpxFftRedBoundary,
       "rlIpxFftYellowBoundary": rlIpxFftYellowBoundary,
       "rlIpxFftNumTable": rlIpxFftNumTable,
       "rlIpxFftNumEntry": rlIpxFftNumEntry,
       "rlIpxFftNumIndex": rlIpxFftNumIndex,
       "rlIpxFftNumStnRoutesNumber": rlIpxFftNumStnRoutesNumber,
       "rlIpxFftNumSubRoutesNumber": rlIpxFftNumSubRoutesNumber,
       "rlIpxFftStnTable": rlIpxFftStnTable,
       "rlIpxFftStnEntry": rlIpxFftStnEntry,
       "rlIpxFftStnIndex": rlIpxFftStnIndex,
       "rlIpxFftStnDstNetid": rlIpxFftStnDstNetid,
       "rlIpxFftStnDstNode": rlIpxFftStnDstNode,
       "rlIpxFftStnSrcNetid": rlIpxFftStnSrcNetid,
       "rlIpxFftStnSrcNode": rlIpxFftStnSrcNode,
       "rlIpxFftStnDstIpxAddrType": rlIpxFftStnDstIpxAddrType,
       "rlIpxFftStnEncapsulation": rlIpxFftStnEncapsulation,
       "rlIpxFftStnDstMacAddress": rlIpxFftStnDstMacAddress,
       "rlIpxFftStnSrcMacAddress": rlIpxFftStnSrcMacAddress,
       "rlIpxFftStnOutIfIndex": rlIpxFftStnOutIfIndex,
       "rlIpxFftStnTci": rlIpxFftStnTci,
       "rlIpxFftStnFacsIndex": rlIpxFftStnFacsIndex,
       "rlIpxFftStnAge": rlIpxFftStnAge,
       "rlIpxFftSubTable": rlIpxFftSubTable,
       "rlIpxFftSubEntry": rlIpxFftSubEntry,
       "rlIpxFftSubIndex": rlIpxFftSubIndex,
       "rlIpxFftSubDstNetid": rlIpxFftSubDstNetid,
       "rlIpxFftSubEncapsulation": rlIpxFftSubEncapsulation,
       "rlIpxFftSubDstMacAddress": rlIpxFftSubDstMacAddress,
       "rlIpxFftSubSrcMacAddress": rlIpxFftSubSrcMacAddress,
       "rlIpxFftSubOutIfIndex": rlIpxFftSubOutIfIndex,
       "rlIpxFftSubTci": rlIpxFftSubTci,
       "rlIpxFftSubFacsIndex": rlIpxFftSubFacsIndex,
       "rlIpxFftSubAge": rlIpxFftSubAge,
       "rlIpxFftCountersTable": rlIpxFftCountersTable,
       "rlIpxFftCountersEntry": rlIpxFftCountersEntry,
       "rlIpxFftCountersIndex": rlIpxFftCountersIndex,
       "rlIpxFftInReceives": rlIpxFftInReceives,
       "rlIpxFftForwDatagrams": rlIpxFftForwDatagrams,
       "rlIpxFftInDiscards": rlIpxFftInDiscards,
       "rlIpmFFT": rlIpmFFT,
       "rlIpmFftMibVersion": rlIpmFftMibVersion,
       "rlIpmMaxFftNumber": rlIpmMaxFftNumber,
       "rlIpmFftDynamicSupported": rlIpmFftDynamicSupported,
       "rlIpmFftUnknownAddrMsgUsed": rlIpmFftUnknownAddrMsgUsed,
       "rlIpmFftUserAgingTimeout": rlIpmFftUserAgingTimeout,
       "rlIpmFftRouterAgingTimeout": rlIpmFftRouterAgingTimeout,
       "rlIpmFftNumTable": rlIpmFftNumTable,
       "rlIpmFftNumEntry": rlIpmFftNumEntry,
       "rlIpmFftNumIndex": rlIpmFftNumIndex,
       "rlIpmFftNumRoutesNumber": rlIpmFftNumRoutesNumber,
       "rlIpmFftTable": rlIpmFftTable,
       "rlIpmFftEntry": rlIpmFftEntry,
       "rlIpmFftIndex": rlIpmFftIndex,
       "rlIpmFftSrcIpAddress": rlIpmFftSrcIpAddress,
       "rlIpmFftDstIpAddress": rlIpmFftDstIpAddress,
       "rlIpmFftSrcIpMask": rlIpmFftSrcIpMask,
       "rlIpmFftInputIfIndex": rlIpmFftInputIfIndex,
       "rlIpmFftInputVlanTag": rlIpmFftInputVlanTag,
       "rlIpmFftForwardAction": rlIpmFftForwardAction,
       "rlIpmFftInportAction": rlIpmFftInportAction,
       "rlIpmFftAge": rlIpmFftAge,
       "rlIpmFftPortTagTable": rlIpmFftPortTagTable,
       "rlIpmFftPortTagEntry": rlIpmFftPortTagEntry,
       "rlIpmFftPortIndex": rlIpmFftPortIndex,
       "rlIpmFftPortSrcIpAddress": rlIpmFftPortSrcIpAddress,
       "rlIpmFftPortDstIpAddress": rlIpmFftPortDstIpAddress,
       "rlIpmFftPortOutputifIndex": rlIpmFftPortOutputifIndex,
       "rlIpmFftPortOutputTag": rlIpmFftPortOutputTag,
       "rlIpmFftCountersTable": rlIpmFftCountersTable,
       "rlIpmFftCountersEntry": rlIpmFftCountersEntry,
       "rlIpmFftCountersIndex": rlIpmFftCountersIndex,
       "rlIpmFftInReceives": rlIpmFftInReceives,
       "rlIpmFftForwDatagrams": rlIpmFftForwDatagrams,
       "rlIpmFftInDiscards": rlIpmFftInDiscards}
)
