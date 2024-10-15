# SNMP MIB module (CISCOSB-rlFft) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-rlFft
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:16 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47)
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1)
)
_RlIpFftMibVersion_Type = Integer32
_RlIpFftMibVersion_Object = MibScalar
rlIpFftMibVersion = _RlIpFftMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 1),
    _RlIpFftMibVersion_Type()
)
rlIpFftMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftMibVersion.setStatus("current")
_RlInetMaxFftNumber_Type = Integer32
_RlInetMaxFftNumber_Object = MibScalar
rlInetMaxFftNumber = _RlInetMaxFftNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 2),
    _RlInetMaxFftNumber_Type()
)
rlInetMaxFftNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetMaxFftNumber.setStatus("current")


class _RlInetFftDynamicSupported_Type(Integer32):
    """Custom type rlInetFftDynamicSupported based on Integer32"""
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


_RlInetFftDynamicSupported_Type.__name__ = "Integer32"
_RlInetFftDynamicSupported_Object = MibScalar
rlInetFftDynamicSupported = _RlInetFftDynamicSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 3),
    _RlInetFftDynamicSupported_Type()
)
rlInetFftDynamicSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftDynamicSupported.setStatus("current")


class _RlInetFftSubnetSupported_Type(Integer32):
    """Custom type rlInetFftSubnetSupported based on Integer32"""
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


_RlInetFftSubnetSupported_Type.__name__ = "Integer32"
_RlInetFftSubnetSupported_Object = MibScalar
rlInetFftSubnetSupported = _RlInetFftSubnetSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 4),
    _RlInetFftSubnetSupported_Type()
)
rlInetFftSubnetSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubnetSupported.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 5),
    _RlIpFftUnknownAddrMsgUsed_Type()
)
rlIpFftUnknownAddrMsgUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftUnknownAddrMsgUsed.setStatus("current")


class _RlInetFftAgingTimeSupported_Type(Integer32):
    """Custom type rlInetFftAgingTimeSupported based on Integer32"""
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


_RlInetFftAgingTimeSupported_Type.__name__ = "Integer32"
_RlInetFftAgingTimeSupported_Object = MibScalar
rlInetFftAgingTimeSupported = _RlInetFftAgingTimeSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 6),
    _RlInetFftAgingTimeSupported_Type()
)
rlInetFftAgingTimeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftAgingTimeSupported.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 7),
    _RlIpFftSrcAddrSupported_Type()
)
rlIpFftSrcAddrSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpFftSrcAddrSupported.setStatus("current")
_RlInetFftAgingTimeout_Type = Integer32
_RlInetFftAgingTimeout_Object = MibScalar
rlInetFftAgingTimeout = _RlInetFftAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 8),
    _RlInetFftAgingTimeout_Type()
)
rlInetFftAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetFftAgingTimeout.setStatus("current")
_RlIpFftRedBoundary_Type = Percents
_RlIpFftRedBoundary_Object = MibScalar
rlIpFftRedBoundary = _RlIpFftRedBoundary_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 9),
    _RlIpFftRedBoundary_Type()
)
rlIpFftRedBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpFftRedBoundary.setStatus("current")
_RlIpFftYellowBoundary_Type = Percents
_RlIpFftYellowBoundary_Object = MibScalar
rlIpFftYellowBoundary = _RlIpFftYellowBoundary_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 10),
    _RlIpFftYellowBoundary_Type()
)
rlIpFftYellowBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpFftYellowBoundary.setStatus("current")
_RlInetFftNumTable_Object = MibTable
rlInetFftNumTable = _RlInetFftNumTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 12)
)
if mibBuilder.loadTexts:
    rlInetFftNumTable.setStatus("current")
_RlInetFftNumEntry_Object = MibTableRow
rlInetFftNumEntry = _RlInetFftNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 12, 1)
)
rlInetFftNumEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlInetFftNumIndex"),
    (0, "CISCOSB-rlFft", "rlInetFftNumAddressType"),
)
if mibBuilder.loadTexts:
    rlInetFftNumEntry.setStatus("current")
_RlInetFftNumIndex_Type = Integer32
_RlInetFftNumIndex_Object = MibTableColumn
rlInetFftNumIndex = _RlInetFftNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 12, 1, 1),
    _RlInetFftNumIndex_Type()
)
rlInetFftNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNumIndex.setStatus("current")
_RlInetFftNumAddressType_Type = InetAddressType
_RlInetFftNumAddressType_Object = MibTableColumn
rlInetFftNumAddressType = _RlInetFftNumAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 12, 1, 2),
    _RlInetFftNumAddressType_Type()
)
rlInetFftNumAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNumAddressType.setStatus("current")
_RlInetFftNumStnRoutesNumber_Type = Integer32
_RlInetFftNumStnRoutesNumber_Object = MibTableColumn
rlInetFftNumStnRoutesNumber = _RlInetFftNumStnRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 12, 1, 3),
    _RlInetFftNumStnRoutesNumber_Type()
)
rlInetFftNumStnRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNumStnRoutesNumber.setStatus("current")
_RlInetFftNumSubRoutesNumber_Type = Integer32
_RlInetFftNumSubRoutesNumber_Object = MibTableColumn
rlInetFftNumSubRoutesNumber = _RlInetFftNumSubRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 12, 1, 4),
    _RlInetFftNumSubRoutesNumber_Type()
)
rlInetFftNumSubRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNumSubRoutesNumber.setStatus("current")
_RlInetFftNumInetTomeRoutesNumber_Type = Integer32
_RlInetFftNumInetTomeRoutesNumber_Object = MibTableColumn
rlInetFftNumInetTomeRoutesNumber = _RlInetFftNumInetTomeRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 12, 1, 5),
    _RlInetFftNumInetTomeRoutesNumber_Type()
)
rlInetFftNumInetTomeRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNumInetTomeRoutesNumber.setStatus("current")
_RlInetFftStnTable_Object = MibTable
rlInetFftStnTable = _RlInetFftStnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13)
)
if mibBuilder.loadTexts:
    rlInetFftStnTable.setStatus("current")
_RlInetFftStnEntry_Object = MibTableRow
rlInetFftStnEntry = _RlInetFftStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1)
)
rlInetFftStnEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlInetFftStnIndex"),
    (0, "CISCOSB-rlFft", "rlInetFftStnMrid"),
    (0, "CISCOSB-rlFft", "rlInetFftStnDstInetAddressType"),
    (0, "CISCOSB-rlFft", "rlInetFftStnDstInetAddress"),
)
if mibBuilder.loadTexts:
    rlInetFftStnEntry.setStatus("current")
_RlInetFftStnIndex_Type = Integer32
_RlInetFftStnIndex_Object = MibTableColumn
rlInetFftStnIndex = _RlInetFftStnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 1),
    _RlInetFftStnIndex_Type()
)
rlInetFftStnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnIndex.setStatus("current")
_RlInetFftStnMrid_Type = Integer32
_RlInetFftStnMrid_Object = MibTableColumn
rlInetFftStnMrid = _RlInetFftStnMrid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 2),
    _RlInetFftStnMrid_Type()
)
rlInetFftStnMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnMrid.setStatus("current")
_RlInetFftStnDstInetAddressType_Type = InetAddressType
_RlInetFftStnDstInetAddressType_Object = MibTableColumn
rlInetFftStnDstInetAddressType = _RlInetFftStnDstInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 3),
    _RlInetFftStnDstInetAddressType_Type()
)
rlInetFftStnDstInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnDstInetAddressType.setStatus("current")
_RlInetFftStnDstInetAddress_Type = InetAddress
_RlInetFftStnDstInetAddress_Object = MibTableColumn
rlInetFftStnDstInetAddress = _RlInetFftStnDstInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 4),
    _RlInetFftStnDstInetAddress_Type()
)
rlInetFftStnDstInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnDstInetAddress.setStatus("current")
_RlInetFftStnDstRouteInetPrefix_Type = InetAddressPrefixLength
_RlInetFftStnDstRouteInetPrefix_Object = MibTableColumn
rlInetFftStnDstRouteInetPrefix = _RlInetFftStnDstRouteInetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 5),
    _RlInetFftStnDstRouteInetPrefix_Type()
)
rlInetFftStnDstRouteInetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnDstRouteInetPrefix.setStatus("current")


class _RlInetFftStnDstInetAddrType_Type(Integer32):
    """Custom type rlInetFftStnDstInetAddrType based on Integer32"""
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


_RlInetFftStnDstInetAddrType_Type.__name__ = "Integer32"
_RlInetFftStnDstInetAddrType_Object = MibTableColumn
rlInetFftStnDstInetAddrType = _RlInetFftStnDstInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 6),
    _RlInetFftStnDstInetAddrType_Type()
)
rlInetFftStnDstInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnDstInetAddrType.setStatus("current")
_RlInetFftStnDstMacAddress_Type = PhysAddress
_RlInetFftStnDstMacAddress_Object = MibTableColumn
rlInetFftStnDstMacAddress = _RlInetFftStnDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 7),
    _RlInetFftStnDstMacAddress_Type()
)
rlInetFftStnDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnDstMacAddress.setStatus("current")
_RlInetFftStnSrcMacAddress_Type = PhysAddress
_RlInetFftStnSrcMacAddress_Object = MibTableColumn
rlInetFftStnSrcMacAddress = _RlInetFftStnSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 8),
    _RlInetFftStnSrcMacAddress_Type()
)
rlInetFftStnSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnSrcMacAddress.setStatus("current")
_RlInetFftStnOutIfIndex_Type = Integer32
_RlInetFftStnOutIfIndex_Object = MibTableColumn
rlInetFftStnOutIfIndex = _RlInetFftStnOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 9),
    _RlInetFftStnOutIfIndex_Type()
)
rlInetFftStnOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnOutIfIndex.setStatus("current")
_RlInetFftStnVid_Type = Integer32
_RlInetFftStnVid_Object = MibTableColumn
rlInetFftStnVid = _RlInetFftStnVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 10),
    _RlInetFftStnVid_Type()
)
rlInetFftStnVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnVid.setStatus("current")


class _RlInetFftStnTaggedMode_Type(Integer32):
    """Custom type rlInetFftStnTaggedMode based on Integer32"""
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


_RlInetFftStnTaggedMode_Type.__name__ = "Integer32"
_RlInetFftStnTaggedMode_Object = MibTableColumn
rlInetFftStnTaggedMode = _RlInetFftStnTaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 11),
    _RlInetFftStnTaggedMode_Type()
)
rlInetFftStnTaggedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnTaggedMode.setStatus("current")
_RlInetFftStnAge_Type = Integer32
_RlInetFftStnAge_Object = MibTableColumn
rlInetFftStnAge = _RlInetFftStnAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 13, 1, 12),
    _RlInetFftStnAge_Type()
)
rlInetFftStnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftStnAge.setStatus("current")
_RlInetFftSubTable_Object = MibTable
rlInetFftSubTable = _RlInetFftSubTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14)
)
if mibBuilder.loadTexts:
    rlInetFftSubTable.setStatus("current")
_RlInetFftSubEntry_Object = MibTableRow
rlInetFftSubEntry = _RlInetFftSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1)
)
rlInetFftSubEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlInetFftSubMrid"),
    (0, "CISCOSB-rlFft", "rlInetFftSubDstInetSubnetType"),
    (0, "CISCOSB-rlFft", "rlInetFftSubDstInetSubnet"),
    (0, "CISCOSB-rlFft", "rlInetFftSubDstInetPrefix"),
)
if mibBuilder.loadTexts:
    rlInetFftSubEntry.setStatus("current")
_RlInetFftSubMrid_Type = Integer32
_RlInetFftSubMrid_Object = MibTableColumn
rlInetFftSubMrid = _RlInetFftSubMrid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 1),
    _RlInetFftSubMrid_Type()
)
rlInetFftSubMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubMrid.setStatus("current")
_RlInetFftSubDstInetSubnetType_Type = InetAddressType
_RlInetFftSubDstInetSubnetType_Object = MibTableColumn
rlInetFftSubDstInetSubnetType = _RlInetFftSubDstInetSubnetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 2),
    _RlInetFftSubDstInetSubnetType_Type()
)
rlInetFftSubDstInetSubnetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubDstInetSubnetType.setStatus("current")
_RlInetFftSubDstInetSubnet_Type = InetAddress
_RlInetFftSubDstInetSubnet_Object = MibTableColumn
rlInetFftSubDstInetSubnet = _RlInetFftSubDstInetSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 3),
    _RlInetFftSubDstInetSubnet_Type()
)
rlInetFftSubDstInetSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubDstInetSubnet.setStatus("current")
_RlInetFftSubDstInetPrefix_Type = InetAddressPrefixLength
_RlInetFftSubDstInetPrefix_Object = MibTableColumn
rlInetFftSubDstInetPrefix = _RlInetFftSubDstInetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 4),
    _RlInetFftSubDstInetPrefix_Type()
)
rlInetFftSubDstInetPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubDstInetPrefix.setStatus("current")
_RlInetFftSubNextHopSetRefCount_Type = Integer32
_RlInetFftSubNextHopSetRefCount_Object = MibTableColumn
rlInetFftSubNextHopSetRefCount = _RlInetFftSubNextHopSetRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 5),
    _RlInetFftSubNextHopSetRefCount_Type()
)
rlInetFftSubNextHopSetRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopSetRefCount.setStatus("current")
_RlInetFftSubNextHopCount_Type = Integer32
_RlInetFftSubNextHopCount_Object = MibTableColumn
rlInetFftSubNextHopCount = _RlInetFftSubNextHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 6),
    _RlInetFftSubNextHopCount_Type()
)
rlInetFftSubNextHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopCount.setStatus("current")
_RlInetFftSubNextHopIfindex1_Type = Integer32
_RlInetFftSubNextHopIfindex1_Object = MibTableColumn
rlInetFftSubNextHopIfindex1 = _RlInetFftSubNextHopIfindex1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 7),
    _RlInetFftSubNextHopIfindex1_Type()
)
rlInetFftSubNextHopIfindex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopIfindex1.setStatus("current")
_RlInetFftSubNextHopInetAddr1Type_Type = InetAddressType
_RlInetFftSubNextHopInetAddr1Type_Object = MibTableColumn
rlInetFftSubNextHopInetAddr1Type = _RlInetFftSubNextHopInetAddr1Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 8),
    _RlInetFftSubNextHopInetAddr1Type_Type()
)
rlInetFftSubNextHopInetAddr1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr1Type.setStatus("current")
_RlInetFftSubNextHopInetAddr1_Type = InetAddress
_RlInetFftSubNextHopInetAddr1_Object = MibTableColumn
rlInetFftSubNextHopInetAddr1 = _RlInetFftSubNextHopInetAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 9),
    _RlInetFftSubNextHopInetAddr1_Type()
)
rlInetFftSubNextHopInetAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr1.setStatus("current")
_RlInetFftSubNextHopIfindex2_Type = Integer32
_RlInetFftSubNextHopIfindex2_Object = MibTableColumn
rlInetFftSubNextHopIfindex2 = _RlInetFftSubNextHopIfindex2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 10),
    _RlInetFftSubNextHopIfindex2_Type()
)
rlInetFftSubNextHopIfindex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopIfindex2.setStatus("current")
_RlInetFftSubNextHopInetAddr2Type_Type = InetAddressType
_RlInetFftSubNextHopInetAddr2Type_Object = MibTableColumn
rlInetFftSubNextHopInetAddr2Type = _RlInetFftSubNextHopInetAddr2Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 11),
    _RlInetFftSubNextHopInetAddr2Type_Type()
)
rlInetFftSubNextHopInetAddr2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr2Type.setStatus("current")
_RlInetFftSubNextHopInetAddr2_Type = InetAddress
_RlInetFftSubNextHopInetAddr2_Object = MibTableColumn
rlInetFftSubNextHopInetAddr2 = _RlInetFftSubNextHopInetAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 12),
    _RlInetFftSubNextHopInetAddr2_Type()
)
rlInetFftSubNextHopInetAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr2.setStatus("current")
_RlInetFftSubNextHopIfindex3_Type = Integer32
_RlInetFftSubNextHopIfindex3_Object = MibTableColumn
rlInetFftSubNextHopIfindex3 = _RlInetFftSubNextHopIfindex3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 13),
    _RlInetFftSubNextHopIfindex3_Type()
)
rlInetFftSubNextHopIfindex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopIfindex3.setStatus("current")
_RlInetFftSubNextHopInetAddr3Type_Type = InetAddressType
_RlInetFftSubNextHopInetAddr3Type_Object = MibTableColumn
rlInetFftSubNextHopInetAddr3Type = _RlInetFftSubNextHopInetAddr3Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 14),
    _RlInetFftSubNextHopInetAddr3Type_Type()
)
rlInetFftSubNextHopInetAddr3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr3Type.setStatus("current")
_RlInetFftSubNextHopInetAddr3_Type = InetAddress
_RlInetFftSubNextHopInetAddr3_Object = MibTableColumn
rlInetFftSubNextHopInetAddr3 = _RlInetFftSubNextHopInetAddr3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 15),
    _RlInetFftSubNextHopInetAddr3_Type()
)
rlInetFftSubNextHopInetAddr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr3.setStatus("current")
_RlInetFftSubNextHopIfindex4_Type = Integer32
_RlInetFftSubNextHopIfindex4_Object = MibTableColumn
rlInetFftSubNextHopIfindex4 = _RlInetFftSubNextHopIfindex4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 16),
    _RlInetFftSubNextHopIfindex4_Type()
)
rlInetFftSubNextHopIfindex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopIfindex4.setStatus("current")
_RlInetFftSubNextHopInetAddr4Type_Type = InetAddressType
_RlInetFftSubNextHopInetAddr4Type_Object = MibTableColumn
rlInetFftSubNextHopInetAddr4Type = _RlInetFftSubNextHopInetAddr4Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 17),
    _RlInetFftSubNextHopInetAddr4Type_Type()
)
rlInetFftSubNextHopInetAddr4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr4Type.setStatus("current")
_RlInetFftSubNextHopInetAddr4_Type = InetAddress
_RlInetFftSubNextHopInetAddr4_Object = MibTableColumn
rlInetFftSubNextHopInetAddr4 = _RlInetFftSubNextHopInetAddr4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 18),
    _RlInetFftSubNextHopInetAddr4_Type()
)
rlInetFftSubNextHopInetAddr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr4.setStatus("current")
_RlInetFftSubNextHopIfindex5_Type = Integer32
_RlInetFftSubNextHopIfindex5_Object = MibTableColumn
rlInetFftSubNextHopIfindex5 = _RlInetFftSubNextHopIfindex5_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 19),
    _RlInetFftSubNextHopIfindex5_Type()
)
rlInetFftSubNextHopIfindex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopIfindex5.setStatus("current")
_RlInetFftSubNextHopInetAddr5Type_Type = InetAddressType
_RlInetFftSubNextHopInetAddr5Type_Object = MibTableColumn
rlInetFftSubNextHopInetAddr5Type = _RlInetFftSubNextHopInetAddr5Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 20),
    _RlInetFftSubNextHopInetAddr5Type_Type()
)
rlInetFftSubNextHopInetAddr5Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr5Type.setStatus("current")
_RlInetFftSubNextHopInetAddr5_Type = InetAddress
_RlInetFftSubNextHopInetAddr5_Object = MibTableColumn
rlInetFftSubNextHopInetAddr5 = _RlInetFftSubNextHopInetAddr5_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 21),
    _RlInetFftSubNextHopInetAddr5_Type()
)
rlInetFftSubNextHopInetAddr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr5.setStatus("current")
_RlInetFftSubNextHopIfindex6_Type = Integer32
_RlInetFftSubNextHopIfindex6_Object = MibTableColumn
rlInetFftSubNextHopIfindex6 = _RlInetFftSubNextHopIfindex6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 22),
    _RlInetFftSubNextHopIfindex6_Type()
)
rlInetFftSubNextHopIfindex6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopIfindex6.setStatus("current")
_RlInetFftSubNextHopInetAddr6Type_Type = InetAddressType
_RlInetFftSubNextHopInetAddr6Type_Object = MibTableColumn
rlInetFftSubNextHopInetAddr6Type = _RlInetFftSubNextHopInetAddr6Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 23),
    _RlInetFftSubNextHopInetAddr6Type_Type()
)
rlInetFftSubNextHopInetAddr6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr6Type.setStatus("current")
_RlInetFftSubNextHopInetAddr6_Type = InetAddress
_RlInetFftSubNextHopInetAddr6_Object = MibTableColumn
rlInetFftSubNextHopInetAddr6 = _RlInetFftSubNextHopInetAddr6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 24),
    _RlInetFftSubNextHopInetAddr6_Type()
)
rlInetFftSubNextHopInetAddr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr6.setStatus("current")
_RlInetFftSubNextHopIfindex7_Type = Integer32
_RlInetFftSubNextHopIfindex7_Object = MibTableColumn
rlInetFftSubNextHopIfindex7 = _RlInetFftSubNextHopIfindex7_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 25),
    _RlInetFftSubNextHopIfindex7_Type()
)
rlInetFftSubNextHopIfindex7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopIfindex7.setStatus("current")
_RlInetFftSubNextHopInetAddr7Type_Type = InetAddressType
_RlInetFftSubNextHopInetAddr7Type_Object = MibTableColumn
rlInetFftSubNextHopInetAddr7Type = _RlInetFftSubNextHopInetAddr7Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 26),
    _RlInetFftSubNextHopInetAddr7Type_Type()
)
rlInetFftSubNextHopInetAddr7Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr7Type.setStatus("current")
_RlInetFftSubNextHopInetAddr7_Type = InetAddress
_RlInetFftSubNextHopInetAddr7_Object = MibTableColumn
rlInetFftSubNextHopInetAddr7 = _RlInetFftSubNextHopInetAddr7_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 27),
    _RlInetFftSubNextHopInetAddr7_Type()
)
rlInetFftSubNextHopInetAddr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr7.setStatus("current")
_RlInetFftSubNextHopIfindex8_Type = Integer32
_RlInetFftSubNextHopIfindex8_Object = MibTableColumn
rlInetFftSubNextHopIfindex8 = _RlInetFftSubNextHopIfindex8_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 28),
    _RlInetFftSubNextHopIfindex8_Type()
)
rlInetFftSubNextHopIfindex8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopIfindex8.setStatus("current")
_RlInetFftSubNextHopInetAddr8Type_Type = InetAddressType
_RlInetFftSubNextHopInetAddr8Type_Object = MibTableColumn
rlInetFftSubNextHopInetAddr8Type = _RlInetFftSubNextHopInetAddr8Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 29),
    _RlInetFftSubNextHopInetAddr8Type_Type()
)
rlInetFftSubNextHopInetAddr8Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr8Type.setStatus("current")
_RlInetFftSubNextHopInetAddr8_Type = InetAddress
_RlInetFftSubNextHopInetAddr8_Object = MibTableColumn
rlInetFftSubNextHopInetAddr8 = _RlInetFftSubNextHopInetAddr8_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 30),
    _RlInetFftSubNextHopInetAddr8_Type()
)
rlInetFftSubNextHopInetAddr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubNextHopInetAddr8.setStatus("current")
_RlInetFftSubAge_Type = Integer32
_RlInetFftSubAge_Object = MibTableColumn
rlInetFftSubAge = _RlInetFftSubAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 14, 1, 31),
    _RlInetFftSubAge_Type()
)
rlInetFftSubAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftSubAge.setStatus("current")
_RlInetFftCountersTable_Object = MibTable
rlInetFftCountersTable = _RlInetFftCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 15)
)
if mibBuilder.loadTexts:
    rlInetFftCountersTable.setStatus("current")
_RlInetFftCountersEntry_Object = MibTableRow
rlInetFftCountersEntry = _RlInetFftCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 15, 1)
)
rlInetFftCountersEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlInetFftCountersIndex"),
)
if mibBuilder.loadTexts:
    rlInetFftCountersEntry.setStatus("current")
_RlInetFftCountersIndex_Type = Integer32
_RlInetFftCountersIndex_Object = MibTableColumn
rlInetFftCountersIndex = _RlInetFftCountersIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 15, 1, 1),
    _RlInetFftCountersIndex_Type()
)
rlInetFftCountersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftCountersIndex.setStatus("current")
_RlInetFftInReceives_Type = Integer32
_RlInetFftInReceives_Object = MibTableColumn
rlInetFftInReceives = _RlInetFftInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 15, 1, 2),
    _RlInetFftInReceives_Type()
)
rlInetFftInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftInReceives.setStatus("current")
_RlInetFftForwDatagrams_Type = Integer32
_RlInetFftForwDatagrams_Object = MibTableColumn
rlInetFftForwDatagrams = _RlInetFftForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 15, 1, 3),
    _RlInetFftForwDatagrams_Type()
)
rlInetFftForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftForwDatagrams.setStatus("current")
_RlInetFftInDiscards_Type = Integer32
_RlInetFftInDiscards_Object = MibTableColumn
rlInetFftInDiscards = _RlInetFftInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 15, 1, 4),
    _RlInetFftInDiscards_Type()
)
rlInetFftInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftInDiscards.setStatus("current")
_RlInetFftNextHopTable_Object = MibTable
rlInetFftNextHopTable = _RlInetFftNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16)
)
if mibBuilder.loadTexts:
    rlInetFftNextHopTable.setStatus("current")
_RlInetFftNextHopEntry_Object = MibTableRow
rlInetFftNextHopEntry = _RlInetFftNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1)
)
rlInetFftNextHopEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlInetFftNextHopifindex"),
    (0, "CISCOSB-rlFft", "rlInetFftNextHopInetAddressType"),
    (0, "CISCOSB-rlFft", "rlInetFftNextHopInetAddress"),
)
if mibBuilder.loadTexts:
    rlInetFftNextHopEntry.setStatus("current")
_RlInetFftNextHopifindex_Type = Integer32
_RlInetFftNextHopifindex_Object = MibTableColumn
rlInetFftNextHopifindex = _RlInetFftNextHopifindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 1),
    _RlInetFftNextHopifindex_Type()
)
rlInetFftNextHopifindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopifindex.setStatus("current")
_RlInetFftNextHopInetAddressType_Type = InetAddressType
_RlInetFftNextHopInetAddressType_Object = MibTableColumn
rlInetFftNextHopInetAddressType = _RlInetFftNextHopInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 2),
    _RlInetFftNextHopInetAddressType_Type()
)
rlInetFftNextHopInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopInetAddressType.setStatus("current")
_RlInetFftNextHopInetAddress_Type = InetAddress
_RlInetFftNextHopInetAddress_Object = MibTableColumn
rlInetFftNextHopInetAddress = _RlInetFftNextHopInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 3),
    _RlInetFftNextHopInetAddress_Type()
)
rlInetFftNextHopInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopInetAddress.setStatus("current")


class _RlInetFftNextHopValid_Type(Integer32):
    """Custom type rlInetFftNextHopValid based on Integer32"""
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


_RlInetFftNextHopValid_Type.__name__ = "Integer32"
_RlInetFftNextHopValid_Object = MibTableColumn
rlInetFftNextHopValid = _RlInetFftNextHopValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 4),
    _RlInetFftNextHopValid_Type()
)
rlInetFftNextHopValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopValid.setStatus("current")


class _RlInetFftNextHopType_Type(Integer32):
    """Custom type rlInetFftNextHopType based on Integer32"""
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


_RlInetFftNextHopType_Type.__name__ = "Integer32"
_RlInetFftNextHopType_Object = MibTableColumn
rlInetFftNextHopType = _RlInetFftNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 5),
    _RlInetFftNextHopType_Type()
)
rlInetFftNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopType.setStatus("current")
_RlInetFftNextHopReferenceCount_Type = Integer32
_RlInetFftNextHopReferenceCount_Object = MibTableColumn
rlInetFftNextHopReferenceCount = _RlInetFftNextHopReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 6),
    _RlInetFftNextHopReferenceCount_Type()
)
rlInetFftNextHopReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopReferenceCount.setStatus("current")
_RlInetFftNextHopNetAddress_Type = PhysAddress
_RlInetFftNextHopNetAddress_Object = MibTableColumn
rlInetFftNextHopNetAddress = _RlInetFftNextHopNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 7),
    _RlInetFftNextHopNetAddress_Type()
)
rlInetFftNextHopNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopNetAddress.setStatus("current")
_RlInetFftNextHopVid_Type = Integer32
_RlInetFftNextHopVid_Object = MibTableColumn
rlInetFftNextHopVid = _RlInetFftNextHopVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 8),
    _RlInetFftNextHopVid_Type()
)
rlInetFftNextHopVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopVid.setStatus("current")
_RlInetFftNextHopMacAddress_Type = PhysAddress
_RlInetFftNextHopMacAddress_Object = MibTableColumn
rlInetFftNextHopMacAddress = _RlInetFftNextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 9),
    _RlInetFftNextHopMacAddress_Type()
)
rlInetFftNextHopMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopMacAddress.setStatus("current")
_RlInetFftNextHopOutIfIndex_Type = Integer32
_RlInetFftNextHopOutIfIndex_Object = MibTableColumn
rlInetFftNextHopOutIfIndex = _RlInetFftNextHopOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 16, 1, 10),
    _RlInetFftNextHopOutIfIndex_Type()
)
rlInetFftNextHopOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftNextHopOutIfIndex.setStatus("current")
_RlInetFftL2InfoTable_Object = MibTable
rlInetFftL2InfoTable = _RlInetFftL2InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17)
)
if mibBuilder.loadTexts:
    rlInetFftL2InfoTable.setStatus("current")
_RlInetFftL2InfoEntry_Object = MibTableRow
rlInetFftL2InfoEntry = _RlInetFftL2InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1)
)
rlInetFftL2InfoEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlInetFftL2InfoIfindex"),
    (0, "CISCOSB-rlFft", "rlInetFftL2InfoDstMacAddress"),
)
if mibBuilder.loadTexts:
    rlInetFftL2InfoEntry.setStatus("current")
_RlInetFftL2InfoIfindex_Type = Integer32
_RlInetFftL2InfoIfindex_Object = MibTableColumn
rlInetFftL2InfoIfindex = _RlInetFftL2InfoIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1, 1),
    _RlInetFftL2InfoIfindex_Type()
)
rlInetFftL2InfoIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftL2InfoIfindex.setStatus("current")
_RlInetFftL2InfoDstMacAddress_Type = PhysAddress
_RlInetFftL2InfoDstMacAddress_Object = MibTableColumn
rlInetFftL2InfoDstMacAddress = _RlInetFftL2InfoDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1, 2),
    _RlInetFftL2InfoDstMacAddress_Type()
)
rlInetFftL2InfoDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftL2InfoDstMacAddress.setStatus("current")


class _RlInetFftL2InfoValid_Type(Integer32):
    """Custom type rlInetFftL2InfoValid based on Integer32"""
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


_RlInetFftL2InfoValid_Type.__name__ = "Integer32"
_RlInetFftL2InfoValid_Object = MibTableColumn
rlInetFftL2InfoValid = _RlInetFftL2InfoValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1, 3),
    _RlInetFftL2InfoValid_Type()
)
rlInetFftL2InfoValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftL2InfoValid.setStatus("current")


class _RlInetFftL2InfoType_Type(Integer32):
    """Custom type rlInetFftL2InfoType based on Integer32"""
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


_RlInetFftL2InfoType_Type.__name__ = "Integer32"
_RlInetFftL2InfoType_Object = MibTableColumn
rlInetFftL2InfoType = _RlInetFftL2InfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1, 4),
    _RlInetFftL2InfoType_Type()
)
rlInetFftL2InfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftL2InfoType.setStatus("current")
_RlInetFftL2InfoReferenceCount_Type = Integer32
_RlInetFftL2InfoReferenceCount_Object = MibTableColumn
rlInetFftL2InfoReferenceCount = _RlInetFftL2InfoReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1, 5),
    _RlInetFftL2InfoReferenceCount_Type()
)
rlInetFftL2InfoReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftL2InfoReferenceCount.setStatus("current")
_RlInetFftL2InfoVid_Type = Integer32
_RlInetFftL2InfoVid_Object = MibTableColumn
rlInetFftL2InfoVid = _RlInetFftL2InfoVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1, 6),
    _RlInetFftL2InfoVid_Type()
)
rlInetFftL2InfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftL2InfoVid.setStatus("current")
_RlInetFftL2InfoSrcMacAddress_Type = PhysAddress
_RlInetFftL2InfoSrcMacAddress_Object = MibTableColumn
rlInetFftL2InfoSrcMacAddress = _RlInetFftL2InfoSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1, 7),
    _RlInetFftL2InfoSrcMacAddress_Type()
)
rlInetFftL2InfoSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftL2InfoSrcMacAddress.setStatus("current")
_RlInetFftL2InfoOutIfIndex_Type = Integer32
_RlInetFftL2InfoOutIfIndex_Object = MibTableColumn
rlInetFftL2InfoOutIfIndex = _RlInetFftL2InfoOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1, 8),
    _RlInetFftL2InfoOutIfIndex_Type()
)
rlInetFftL2InfoOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftL2InfoOutIfIndex.setStatus("current")


class _RlInetFftL2InfoTaggedMode_Type(Integer32):
    """Custom type rlInetFftL2InfoTaggedMode based on Integer32"""
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


_RlInetFftL2InfoTaggedMode_Type.__name__ = "Integer32"
_RlInetFftL2InfoTaggedMode_Object = MibTableColumn
rlInetFftL2InfoTaggedMode = _RlInetFftL2InfoTaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 17, 1, 9),
    _RlInetFftL2InfoTaggedMode_Type()
)
rlInetFftL2InfoTaggedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetFftL2InfoTaggedMode.setStatus("current")
_RlIpv6FftRedBoundary_Type = Percents
_RlIpv6FftRedBoundary_Object = MibScalar
rlIpv6FftRedBoundary = _RlIpv6FftRedBoundary_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 18),
    _RlIpv6FftRedBoundary_Type()
)
rlIpv6FftRedBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6FftRedBoundary.setStatus("current")
_RlIpv6FftYellowBoundary_Type = Percents
_RlIpv6FftYellowBoundary_Object = MibScalar
rlIpv6FftYellowBoundary = _RlIpv6FftYellowBoundary_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 1, 19),
    _RlIpv6FftYellowBoundary_Type()
)
rlIpv6FftYellowBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6FftYellowBoundary.setStatus("current")
_RlIpxFFT_ObjectIdentity = ObjectIdentity
rlIpxFFT = _RlIpxFFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2)
)
_RlIpxFftMibVersion_Type = Integer32
_RlIpxFftMibVersion_Object = MibScalar
rlIpxFftMibVersion = _RlIpxFftMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 1),
    _RlIpxFftMibVersion_Type()
)
rlIpxFftMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftMibVersion.setStatus("current")
_RlIpxMaxFftNumber_Type = Integer32
_RlIpxMaxFftNumber_Object = MibScalar
rlIpxMaxFftNumber = _RlIpxMaxFftNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 7),
    _RlIpxFftSrcAddrSupported_Type()
)
rlIpxFftSrcAddrSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSrcAddrSupported.setStatus("current")
_RlIpxFftAgingTimeout_Type = Integer32
_RlIpxFftAgingTimeout_Object = MibScalar
rlIpxFftAgingTimeout = _RlIpxFftAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 9),
    _RlIpxFftRedBoundary_Type()
)
rlIpxFftRedBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpxFftRedBoundary.setStatus("current")
_RlIpxFftYellowBoundary_Type = Percents
_RlIpxFftYellowBoundary_Object = MibScalar
rlIpxFftYellowBoundary = _RlIpxFftYellowBoundary_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 10),
    _RlIpxFftYellowBoundary_Type()
)
rlIpxFftYellowBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpxFftYellowBoundary.setStatus("current")
_RlIpxFftNumTable_Object = MibTable
rlIpxFftNumTable = _RlIpxFftNumTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 12)
)
if mibBuilder.loadTexts:
    rlIpxFftNumTable.setStatus("current")
_RlIpxFftNumEntry_Object = MibTableRow
rlIpxFftNumEntry = _RlIpxFftNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 12, 1)
)
rlIpxFftNumEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlIpxFftNumIndex"),
)
if mibBuilder.loadTexts:
    rlIpxFftNumEntry.setStatus("current")
_RlIpxFftNumIndex_Type = Integer32
_RlIpxFftNumIndex_Object = MibTableColumn
rlIpxFftNumIndex = _RlIpxFftNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 12, 1, 1),
    _RlIpxFftNumIndex_Type()
)
rlIpxFftNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftNumIndex.setStatus("current")
_RlIpxFftNumStnRoutesNumber_Type = Integer32
_RlIpxFftNumStnRoutesNumber_Object = MibTableColumn
rlIpxFftNumStnRoutesNumber = _RlIpxFftNumStnRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 12, 1, 2),
    _RlIpxFftNumStnRoutesNumber_Type()
)
rlIpxFftNumStnRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftNumStnRoutesNumber.setStatus("current")
_RlIpxFftNumSubRoutesNumber_Type = Integer32
_RlIpxFftNumSubRoutesNumber_Object = MibTableColumn
rlIpxFftNumSubRoutesNumber = _RlIpxFftNumSubRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 12, 1, 3),
    _RlIpxFftNumSubRoutesNumber_Type()
)
rlIpxFftNumSubRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftNumSubRoutesNumber.setStatus("current")
_RlIpxFftStnTable_Object = MibTable
rlIpxFftStnTable = _RlIpxFftStnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13)
)
if mibBuilder.loadTexts:
    rlIpxFftStnTable.setStatus("current")
_RlIpxFftStnEntry_Object = MibTableRow
rlIpxFftStnEntry = _RlIpxFftStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1)
)
rlIpxFftStnEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlIpxFftStnIndex"),
    (0, "CISCOSB-rlFft", "rlIpxFftStnDstNetid"),
    (0, "CISCOSB-rlFft", "rlIpxFftStnDstNode"),
    (0, "CISCOSB-rlFft", "rlIpxFftStnSrcNetid"),
    (0, "CISCOSB-rlFft", "rlIpxFftStnSrcNode"),
)
if mibBuilder.loadTexts:
    rlIpxFftStnEntry.setStatus("current")
_RlIpxFftStnIndex_Type = Integer32
_RlIpxFftStnIndex_Object = MibTableColumn
rlIpxFftStnIndex = _RlIpxFftStnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 1),
    _RlIpxFftStnIndex_Type()
)
rlIpxFftStnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnIndex.setStatus("current")
_RlIpxFftStnDstNetid_Type = NetNumber
_RlIpxFftStnDstNetid_Object = MibTableColumn
rlIpxFftStnDstNetid = _RlIpxFftStnDstNetid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 2),
    _RlIpxFftStnDstNetid_Type()
)
rlIpxFftStnDstNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnDstNetid.setStatus("current")
_RlIpxFftStnDstNode_Type = PhysAddress
_RlIpxFftStnDstNode_Object = MibTableColumn
rlIpxFftStnDstNode = _RlIpxFftStnDstNode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 3),
    _RlIpxFftStnDstNode_Type()
)
rlIpxFftStnDstNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnDstNode.setStatus("current")
_RlIpxFftStnSrcNetid_Type = NetNumber
_RlIpxFftStnSrcNetid_Object = MibTableColumn
rlIpxFftStnSrcNetid = _RlIpxFftStnSrcNetid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 4),
    _RlIpxFftStnSrcNetid_Type()
)
rlIpxFftStnSrcNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnSrcNetid.setStatus("current")
_RlIpxFftStnSrcNode_Type = PhysAddress
_RlIpxFftStnSrcNode_Object = MibTableColumn
rlIpxFftStnSrcNode = _RlIpxFftStnSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 7),
    _RlIpxFftStnEncapsulation_Type()
)
rlIpxFftStnEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnEncapsulation.setStatus("current")
_RlIpxFftStnDstMacAddress_Type = PhysAddress
_RlIpxFftStnDstMacAddress_Object = MibTableColumn
rlIpxFftStnDstMacAddress = _RlIpxFftStnDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 8),
    _RlIpxFftStnDstMacAddress_Type()
)
rlIpxFftStnDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnDstMacAddress.setStatus("current")
_RlIpxFftStnSrcMacAddress_Type = PhysAddress
_RlIpxFftStnSrcMacAddress_Object = MibTableColumn
rlIpxFftStnSrcMacAddress = _RlIpxFftStnSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 9),
    _RlIpxFftStnSrcMacAddress_Type()
)
rlIpxFftStnSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnSrcMacAddress.setStatus("current")
_RlIpxFftStnOutIfIndex_Type = Integer32
_RlIpxFftStnOutIfIndex_Object = MibTableColumn
rlIpxFftStnOutIfIndex = _RlIpxFftStnOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 10),
    _RlIpxFftStnOutIfIndex_Type()
)
rlIpxFftStnOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnOutIfIndex.setStatus("current")
_RlIpxFftStnTci_Type = Integer32
_RlIpxFftStnTci_Object = MibTableColumn
rlIpxFftStnTci = _RlIpxFftStnTci_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 11),
    _RlIpxFftStnTci_Type()
)
rlIpxFftStnTci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnTci.setStatus("current")
_RlIpxFftStnFacsIndex_Type = Integer32
_RlIpxFftStnFacsIndex_Object = MibTableColumn
rlIpxFftStnFacsIndex = _RlIpxFftStnFacsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 12),
    _RlIpxFftStnFacsIndex_Type()
)
rlIpxFftStnFacsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnFacsIndex.setStatus("current")
_RlIpxFftStnAge_Type = Integer32
_RlIpxFftStnAge_Object = MibTableColumn
rlIpxFftStnAge = _RlIpxFftStnAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 13, 1, 13),
    _RlIpxFftStnAge_Type()
)
rlIpxFftStnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftStnAge.setStatus("current")
_RlIpxFftSubTable_Object = MibTable
rlIpxFftSubTable = _RlIpxFftSubTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14)
)
if mibBuilder.loadTexts:
    rlIpxFftSubTable.setStatus("current")
_RlIpxFftSubEntry_Object = MibTableRow
rlIpxFftSubEntry = _RlIpxFftSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1)
)
rlIpxFftSubEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlIpxFftSubIndex"),
    (0, "CISCOSB-rlFft", "rlIpxFftSubDstNetid"),
)
if mibBuilder.loadTexts:
    rlIpxFftSubEntry.setStatus("current")
_RlIpxFftSubIndex_Type = Integer32
_RlIpxFftSubIndex_Object = MibTableColumn
rlIpxFftSubIndex = _RlIpxFftSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1, 1),
    _RlIpxFftSubIndex_Type()
)
rlIpxFftSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubIndex.setStatus("current")
_RlIpxFftSubDstNetid_Type = NetNumber
_RlIpxFftSubDstNetid_Object = MibTableColumn
rlIpxFftSubDstNetid = _RlIpxFftSubDstNetid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1, 3),
    _RlIpxFftSubEncapsulation_Type()
)
rlIpxFftSubEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubEncapsulation.setStatus("current")
_RlIpxFftSubDstMacAddress_Type = PhysAddress
_RlIpxFftSubDstMacAddress_Object = MibTableColumn
rlIpxFftSubDstMacAddress = _RlIpxFftSubDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1, 4),
    _RlIpxFftSubDstMacAddress_Type()
)
rlIpxFftSubDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubDstMacAddress.setStatus("current")
_RlIpxFftSubSrcMacAddress_Type = PhysAddress
_RlIpxFftSubSrcMacAddress_Object = MibTableColumn
rlIpxFftSubSrcMacAddress = _RlIpxFftSubSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1, 5),
    _RlIpxFftSubSrcMacAddress_Type()
)
rlIpxFftSubSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubSrcMacAddress.setStatus("current")
_RlIpxFftSubOutIfIndex_Type = Integer32
_RlIpxFftSubOutIfIndex_Object = MibTableColumn
rlIpxFftSubOutIfIndex = _RlIpxFftSubOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1, 6),
    _RlIpxFftSubOutIfIndex_Type()
)
rlIpxFftSubOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubOutIfIndex.setStatus("current")
_RlIpxFftSubTci_Type = Integer32
_RlIpxFftSubTci_Object = MibTableColumn
rlIpxFftSubTci = _RlIpxFftSubTci_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1, 7),
    _RlIpxFftSubTci_Type()
)
rlIpxFftSubTci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubTci.setStatus("current")
_RlIpxFftSubFacsIndex_Type = Integer32
_RlIpxFftSubFacsIndex_Object = MibTableColumn
rlIpxFftSubFacsIndex = _RlIpxFftSubFacsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1, 8),
    _RlIpxFftSubFacsIndex_Type()
)
rlIpxFftSubFacsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubFacsIndex.setStatus("current")
_RlIpxFftSubAge_Type = Integer32
_RlIpxFftSubAge_Object = MibTableColumn
rlIpxFftSubAge = _RlIpxFftSubAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 14, 1, 9),
    _RlIpxFftSubAge_Type()
)
rlIpxFftSubAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftSubAge.setStatus("current")
_RlIpxFftCountersTable_Object = MibTable
rlIpxFftCountersTable = _RlIpxFftCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 15)
)
if mibBuilder.loadTexts:
    rlIpxFftCountersTable.setStatus("current")
_RlIpxFftCountersEntry_Object = MibTableRow
rlIpxFftCountersEntry = _RlIpxFftCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 15, 1)
)
rlIpxFftCountersEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlIpxFftCountersIndex"),
)
if mibBuilder.loadTexts:
    rlIpxFftCountersEntry.setStatus("current")
_RlIpxFftCountersIndex_Type = Integer32
_RlIpxFftCountersIndex_Object = MibTableColumn
rlIpxFftCountersIndex = _RlIpxFftCountersIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 15, 1, 1),
    _RlIpxFftCountersIndex_Type()
)
rlIpxFftCountersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftCountersIndex.setStatus("current")
_RlIpxFftInReceives_Type = Integer32
_RlIpxFftInReceives_Object = MibTableColumn
rlIpxFftInReceives = _RlIpxFftInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 15, 1, 2),
    _RlIpxFftInReceives_Type()
)
rlIpxFftInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftInReceives.setStatus("current")
_RlIpxFftForwDatagrams_Type = Integer32
_RlIpxFftForwDatagrams_Object = MibTableColumn
rlIpxFftForwDatagrams = _RlIpxFftForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 15, 1, 3),
    _RlIpxFftForwDatagrams_Type()
)
rlIpxFftForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftForwDatagrams.setStatus("current")
_RlIpxFftInDiscards_Type = Integer32
_RlIpxFftInDiscards_Object = MibTableColumn
rlIpxFftInDiscards = _RlIpxFftInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 2, 15, 1, 4),
    _RlIpxFftInDiscards_Type()
)
rlIpxFftInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpxFftInDiscards.setStatus("current")
_RlIpmFFT_ObjectIdentity = ObjectIdentity
rlIpmFFT = _RlIpmFFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3)
)
_RlIpmFftMibVersion_Type = Integer32
_RlIpmFftMibVersion_Object = MibScalar
rlIpmFftMibVersion = _RlIpmFftMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 1),
    _RlIpmFftMibVersion_Type()
)
rlIpmFftMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftMibVersion.setStatus("current")
_RlIpmMaxFftNumber_Type = Integer32
_RlIpmMaxFftNumber_Object = MibScalar
rlIpmMaxFftNumber = _RlIpmMaxFftNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 4),
    _RlIpmFftUnknownAddrMsgUsed_Type()
)
rlIpmFftUnknownAddrMsgUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftUnknownAddrMsgUsed.setStatus("current")
_RlIpmFftUserAgingTimeout_Type = Unsigned32
_RlIpmFftUserAgingTimeout_Object = MibScalar
rlIpmFftUserAgingTimeout = _RlIpmFftUserAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 5),
    _RlIpmFftUserAgingTimeout_Type()
)
rlIpmFftUserAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpmFftUserAgingTimeout.setStatus("current")
_RlIpmFftRouterAgingTimeout_Type = Integer32
_RlIpmFftRouterAgingTimeout_Object = MibScalar
rlIpmFftRouterAgingTimeout = _RlIpmFftRouterAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 6),
    _RlIpmFftRouterAgingTimeout_Type()
)
rlIpmFftRouterAgingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftRouterAgingTimeout.setStatus("current")
_RlIpmFftNumTable_Object = MibTable
rlIpmFftNumTable = _RlIpmFftNumTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 8)
)
if mibBuilder.loadTexts:
    rlIpmFftNumTable.setStatus("current")
_RlIpmFftNumEntry_Object = MibTableRow
rlIpmFftNumEntry = _RlIpmFftNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 8, 1)
)
rlIpmFftNumEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlIpmFftNumIndex"),
)
if mibBuilder.loadTexts:
    rlIpmFftNumEntry.setStatus("current")
_RlIpmFftNumIndex_Type = Integer32
_RlIpmFftNumIndex_Object = MibTableColumn
rlIpmFftNumIndex = _RlIpmFftNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 8, 1, 1),
    _RlIpmFftNumIndex_Type()
)
rlIpmFftNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftNumIndex.setStatus("current")
_RlIpmFftNumRoutesNumber_Type = Integer32
_RlIpmFftNumRoutesNumber_Object = MibTableColumn
rlIpmFftNumRoutesNumber = _RlIpmFftNumRoutesNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 8, 1, 2),
    _RlIpmFftNumRoutesNumber_Type()
)
rlIpmFftNumRoutesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftNumRoutesNumber.setStatus("current")
_RlIpmFftTable_Object = MibTable
rlIpmFftTable = _RlIpmFftTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9)
)
if mibBuilder.loadTexts:
    rlIpmFftTable.setStatus("current")
_RlIpmFftEntry_Object = MibTableRow
rlIpmFftEntry = _RlIpmFftEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1)
)
rlIpmFftEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlIpmFftIndex"),
    (0, "CISCOSB-rlFft", "rlIpmFftSrcIpAddress"),
    (0, "CISCOSB-rlFft", "rlIpmFftDstIpAddress"),
)
if mibBuilder.loadTexts:
    rlIpmFftEntry.setStatus("current")
_RlIpmFftIndex_Type = Integer32
_RlIpmFftIndex_Object = MibTableColumn
rlIpmFftIndex = _RlIpmFftIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1, 1),
    _RlIpmFftIndex_Type()
)
rlIpmFftIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftIndex.setStatus("current")
_RlIpmFftSrcIpAddress_Type = IpAddress
_RlIpmFftSrcIpAddress_Object = MibTableColumn
rlIpmFftSrcIpAddress = _RlIpmFftSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1, 2),
    _RlIpmFftSrcIpAddress_Type()
)
rlIpmFftSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftSrcIpAddress.setStatus("current")
_RlIpmFftDstIpAddress_Type = IpAddress
_RlIpmFftDstIpAddress_Object = MibTableColumn
rlIpmFftDstIpAddress = _RlIpmFftDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1, 3),
    _RlIpmFftDstIpAddress_Type()
)
rlIpmFftDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftDstIpAddress.setStatus("current")
_RlIpmFftSrcIpMask_Type = IpAddress
_RlIpmFftSrcIpMask_Object = MibTableColumn
rlIpmFftSrcIpMask = _RlIpmFftSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1, 4),
    _RlIpmFftSrcIpMask_Type()
)
rlIpmFftSrcIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftSrcIpMask.setStatus("current")
_RlIpmFftInputIfIndex_Type = Integer32
_RlIpmFftInputIfIndex_Object = MibTableColumn
rlIpmFftInputIfIndex = _RlIpmFftInputIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1, 5),
    _RlIpmFftInputIfIndex_Type()
)
rlIpmFftInputIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftInputIfIndex.setStatus("current")
_RlIpmFftInputVlanTag_Type = Integer32
_RlIpmFftInputVlanTag_Object = MibTableColumn
rlIpmFftInputVlanTag = _RlIpmFftInputVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1, 8),
    _RlIpmFftInportAction_Type()
)
rlIpmFftInportAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftInportAction.setStatus("current")
_RlIpmFftAge_Type = Integer32
_RlIpmFftAge_Object = MibTableColumn
rlIpmFftAge = _RlIpmFftAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 9, 1, 9),
    _RlIpmFftAge_Type()
)
rlIpmFftAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftAge.setStatus("current")
_RlIpmFftPortTagTable_Object = MibTable
rlIpmFftPortTagTable = _RlIpmFftPortTagTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 10)
)
if mibBuilder.loadTexts:
    rlIpmFftPortTagTable.setStatus("current")
_RlIpmFftPortTagEntry_Object = MibTableRow
rlIpmFftPortTagEntry = _RlIpmFftPortTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 10, 1)
)
rlIpmFftPortTagEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlIpmFftPortIndex"),
    (0, "CISCOSB-rlFft", "rlIpmFftPortSrcIpAddress"),
    (0, "CISCOSB-rlFft", "rlIpmFftPortDstIpAddress"),
    (0, "CISCOSB-rlFft", "rlIpmFftPortOutputifIndex"),
    (0, "CISCOSB-rlFft", "rlIpmFftPortOutputTag"),
)
if mibBuilder.loadTexts:
    rlIpmFftPortTagEntry.setStatus("current")
_RlIpmFftPortIndex_Type = Integer32
_RlIpmFftPortIndex_Object = MibTableColumn
rlIpmFftPortIndex = _RlIpmFftPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 10, 1, 1),
    _RlIpmFftPortIndex_Type()
)
rlIpmFftPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortIndex.setStatus("current")
_RlIpmFftPortSrcIpAddress_Type = IpAddress
_RlIpmFftPortSrcIpAddress_Object = MibTableColumn
rlIpmFftPortSrcIpAddress = _RlIpmFftPortSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 10, 1, 2),
    _RlIpmFftPortSrcIpAddress_Type()
)
rlIpmFftPortSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortSrcIpAddress.setStatus("current")
_RlIpmFftPortDstIpAddress_Type = IpAddress
_RlIpmFftPortDstIpAddress_Object = MibTableColumn
rlIpmFftPortDstIpAddress = _RlIpmFftPortDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 10, 1, 3),
    _RlIpmFftPortDstIpAddress_Type()
)
rlIpmFftPortDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortDstIpAddress.setStatus("current")
_RlIpmFftPortOutputifIndex_Type = Integer32
_RlIpmFftPortOutputifIndex_Object = MibTableColumn
rlIpmFftPortOutputifIndex = _RlIpmFftPortOutputifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 10, 1, 4),
    _RlIpmFftPortOutputifIndex_Type()
)
rlIpmFftPortOutputifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortOutputifIndex.setStatus("current")
_RlIpmFftPortOutputTag_Type = Integer32
_RlIpmFftPortOutputTag_Object = MibTableColumn
rlIpmFftPortOutputTag = _RlIpmFftPortOutputTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 10, 1, 5),
    _RlIpmFftPortOutputTag_Type()
)
rlIpmFftPortOutputTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftPortOutputTag.setStatus("current")
_RlIpmFftCountersTable_Object = MibTable
rlIpmFftCountersTable = _RlIpmFftCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 11)
)
if mibBuilder.loadTexts:
    rlIpmFftCountersTable.setStatus("current")
_RlIpmFftCountersEntry_Object = MibTableRow
rlIpmFftCountersEntry = _RlIpmFftCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 11, 1)
)
rlIpmFftCountersEntry.setIndexNames(
    (0, "CISCOSB-rlFft", "rlIpmFftCountersIndex"),
)
if mibBuilder.loadTexts:
    rlIpmFftCountersEntry.setStatus("current")
_RlIpmFftCountersIndex_Type = Integer32
_RlIpmFftCountersIndex_Object = MibTableColumn
rlIpmFftCountersIndex = _RlIpmFftCountersIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 11, 1, 1),
    _RlIpmFftCountersIndex_Type()
)
rlIpmFftCountersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftCountersIndex.setStatus("current")
_RlIpmFftInReceives_Type = Integer32
_RlIpmFftInReceives_Object = MibTableColumn
rlIpmFftInReceives = _RlIpmFftInReceives_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 11, 1, 2),
    _RlIpmFftInReceives_Type()
)
rlIpmFftInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftInReceives.setStatus("current")
_RlIpmFftForwDatagrams_Type = Integer32
_RlIpmFftForwDatagrams_Object = MibTableColumn
rlIpmFftForwDatagrams = _RlIpmFftForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 11, 1, 3),
    _RlIpmFftForwDatagrams_Type()
)
rlIpmFftForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpmFftForwDatagrams.setStatus("current")
_RlIpmFftInDiscards_Type = Integer32
_RlIpmFftInDiscards_Object = MibTableColumn
rlIpmFftInDiscards = _RlIpmFftInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47, 3, 11, 1, 4),
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
    "CISCOSB-rlFft",
    **{"Percents": Percents,
       "NetNumber": NetNumber,
       "rlFFT": rlFFT,
       "rlIpFFT": rlIpFFT,
       "rlIpFftMibVersion": rlIpFftMibVersion,
       "rlInetMaxFftNumber": rlInetMaxFftNumber,
       "rlInetFftDynamicSupported": rlInetFftDynamicSupported,
       "rlInetFftSubnetSupported": rlInetFftSubnetSupported,
       "rlIpFftUnknownAddrMsgUsed": rlIpFftUnknownAddrMsgUsed,
       "rlInetFftAgingTimeSupported": rlInetFftAgingTimeSupported,
       "rlIpFftSrcAddrSupported": rlIpFftSrcAddrSupported,
       "rlInetFftAgingTimeout": rlInetFftAgingTimeout,
       "rlIpFftRedBoundary": rlIpFftRedBoundary,
       "rlIpFftYellowBoundary": rlIpFftYellowBoundary,
       "rlInetFftNumTable": rlInetFftNumTable,
       "rlInetFftNumEntry": rlInetFftNumEntry,
       "rlInetFftNumIndex": rlInetFftNumIndex,
       "rlInetFftNumAddressType": rlInetFftNumAddressType,
       "rlInetFftNumStnRoutesNumber": rlInetFftNumStnRoutesNumber,
       "rlInetFftNumSubRoutesNumber": rlInetFftNumSubRoutesNumber,
       "rlInetFftNumInetTomeRoutesNumber": rlInetFftNumInetTomeRoutesNumber,
       "rlInetFftStnTable": rlInetFftStnTable,
       "rlInetFftStnEntry": rlInetFftStnEntry,
       "rlInetFftStnIndex": rlInetFftStnIndex,
       "rlInetFftStnMrid": rlInetFftStnMrid,
       "rlInetFftStnDstInetAddressType": rlInetFftStnDstInetAddressType,
       "rlInetFftStnDstInetAddress": rlInetFftStnDstInetAddress,
       "rlInetFftStnDstRouteInetPrefix": rlInetFftStnDstRouteInetPrefix,
       "rlInetFftStnDstInetAddrType": rlInetFftStnDstInetAddrType,
       "rlInetFftStnDstMacAddress": rlInetFftStnDstMacAddress,
       "rlInetFftStnSrcMacAddress": rlInetFftStnSrcMacAddress,
       "rlInetFftStnOutIfIndex": rlInetFftStnOutIfIndex,
       "rlInetFftStnVid": rlInetFftStnVid,
       "rlInetFftStnTaggedMode": rlInetFftStnTaggedMode,
       "rlInetFftStnAge": rlInetFftStnAge,
       "rlInetFftSubTable": rlInetFftSubTable,
       "rlInetFftSubEntry": rlInetFftSubEntry,
       "rlInetFftSubMrid": rlInetFftSubMrid,
       "rlInetFftSubDstInetSubnetType": rlInetFftSubDstInetSubnetType,
       "rlInetFftSubDstInetSubnet": rlInetFftSubDstInetSubnet,
       "rlInetFftSubDstInetPrefix": rlInetFftSubDstInetPrefix,
       "rlInetFftSubNextHopSetRefCount": rlInetFftSubNextHopSetRefCount,
       "rlInetFftSubNextHopCount": rlInetFftSubNextHopCount,
       "rlInetFftSubNextHopIfindex1": rlInetFftSubNextHopIfindex1,
       "rlInetFftSubNextHopInetAddr1Type": rlInetFftSubNextHopInetAddr1Type,
       "rlInetFftSubNextHopInetAddr1": rlInetFftSubNextHopInetAddr1,
       "rlInetFftSubNextHopIfindex2": rlInetFftSubNextHopIfindex2,
       "rlInetFftSubNextHopInetAddr2Type": rlInetFftSubNextHopInetAddr2Type,
       "rlInetFftSubNextHopInetAddr2": rlInetFftSubNextHopInetAddr2,
       "rlInetFftSubNextHopIfindex3": rlInetFftSubNextHopIfindex3,
       "rlInetFftSubNextHopInetAddr3Type": rlInetFftSubNextHopInetAddr3Type,
       "rlInetFftSubNextHopInetAddr3": rlInetFftSubNextHopInetAddr3,
       "rlInetFftSubNextHopIfindex4": rlInetFftSubNextHopIfindex4,
       "rlInetFftSubNextHopInetAddr4Type": rlInetFftSubNextHopInetAddr4Type,
       "rlInetFftSubNextHopInetAddr4": rlInetFftSubNextHopInetAddr4,
       "rlInetFftSubNextHopIfindex5": rlInetFftSubNextHopIfindex5,
       "rlInetFftSubNextHopInetAddr5Type": rlInetFftSubNextHopInetAddr5Type,
       "rlInetFftSubNextHopInetAddr5": rlInetFftSubNextHopInetAddr5,
       "rlInetFftSubNextHopIfindex6": rlInetFftSubNextHopIfindex6,
       "rlInetFftSubNextHopInetAddr6Type": rlInetFftSubNextHopInetAddr6Type,
       "rlInetFftSubNextHopInetAddr6": rlInetFftSubNextHopInetAddr6,
       "rlInetFftSubNextHopIfindex7": rlInetFftSubNextHopIfindex7,
       "rlInetFftSubNextHopInetAddr7Type": rlInetFftSubNextHopInetAddr7Type,
       "rlInetFftSubNextHopInetAddr7": rlInetFftSubNextHopInetAddr7,
       "rlInetFftSubNextHopIfindex8": rlInetFftSubNextHopIfindex8,
       "rlInetFftSubNextHopInetAddr8Type": rlInetFftSubNextHopInetAddr8Type,
       "rlInetFftSubNextHopInetAddr8": rlInetFftSubNextHopInetAddr8,
       "rlInetFftSubAge": rlInetFftSubAge,
       "rlInetFftCountersTable": rlInetFftCountersTable,
       "rlInetFftCountersEntry": rlInetFftCountersEntry,
       "rlInetFftCountersIndex": rlInetFftCountersIndex,
       "rlInetFftInReceives": rlInetFftInReceives,
       "rlInetFftForwDatagrams": rlInetFftForwDatagrams,
       "rlInetFftInDiscards": rlInetFftInDiscards,
       "rlInetFftNextHopTable": rlInetFftNextHopTable,
       "rlInetFftNextHopEntry": rlInetFftNextHopEntry,
       "rlInetFftNextHopifindex": rlInetFftNextHopifindex,
       "rlInetFftNextHopInetAddressType": rlInetFftNextHopInetAddressType,
       "rlInetFftNextHopInetAddress": rlInetFftNextHopInetAddress,
       "rlInetFftNextHopValid": rlInetFftNextHopValid,
       "rlInetFftNextHopType": rlInetFftNextHopType,
       "rlInetFftNextHopReferenceCount": rlInetFftNextHopReferenceCount,
       "rlInetFftNextHopNetAddress": rlInetFftNextHopNetAddress,
       "rlInetFftNextHopVid": rlInetFftNextHopVid,
       "rlInetFftNextHopMacAddress": rlInetFftNextHopMacAddress,
       "rlInetFftNextHopOutIfIndex": rlInetFftNextHopOutIfIndex,
       "rlInetFftL2InfoTable": rlInetFftL2InfoTable,
       "rlInetFftL2InfoEntry": rlInetFftL2InfoEntry,
       "rlInetFftL2InfoIfindex": rlInetFftL2InfoIfindex,
       "rlInetFftL2InfoDstMacAddress": rlInetFftL2InfoDstMacAddress,
       "rlInetFftL2InfoValid": rlInetFftL2InfoValid,
       "rlInetFftL2InfoType": rlInetFftL2InfoType,
       "rlInetFftL2InfoReferenceCount": rlInetFftL2InfoReferenceCount,
       "rlInetFftL2InfoVid": rlInetFftL2InfoVid,
       "rlInetFftL2InfoSrcMacAddress": rlInetFftL2InfoSrcMacAddress,
       "rlInetFftL2InfoOutIfIndex": rlInetFftL2InfoOutIfIndex,
       "rlInetFftL2InfoTaggedMode": rlInetFftL2InfoTaggedMode,
       "rlIpv6FftRedBoundary": rlIpv6FftRedBoundary,
       "rlIpv6FftYellowBoundary": rlIpv6FftYellowBoundary,
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
