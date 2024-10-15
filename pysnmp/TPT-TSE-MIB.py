# SNMP MIB module (TPT-TSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-TSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:15 2024
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

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_tse = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7)
)
tpt_tse.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PolicyState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 3),
          ("system-disabled", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TopTenAdaptFilterTable_Object = MibTable
topTenAdaptFilterTable = _TopTenAdaptFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    topTenAdaptFilterTable.setStatus("current")
_TopTenAdaptFilterEntry_Object = MibTableRow
topTenAdaptFilterEntry = _TopTenAdaptFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 1, 1)
)
topTenAdaptFilterEntry.setIndexNames(
    (0, "TPT-TSE-MIB", "topTenAdaptFilterRank"),
)
if mibBuilder.loadTexts:
    topTenAdaptFilterEntry.setStatus("current")


class _TopTenAdaptFilterRank_Type(Unsigned32):
    """Custom type topTenAdaptFilterRank based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TopTenAdaptFilterRank_Type.__name__ = "Unsigned32"
_TopTenAdaptFilterRank_Object = MibTableColumn
topTenAdaptFilterRank = _TopTenAdaptFilterRank_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 1, 1, 1),
    _TopTenAdaptFilterRank_Type()
)
topTenAdaptFilterRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topTenAdaptFilterRank.setStatus("current")


class _AdaptFilterName_Type(OctetString):
    """Custom type adaptFilterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdaptFilterName_Type.__name__ = "OctetString"
_AdaptFilterName_Object = MibTableColumn
adaptFilterName = _AdaptFilterName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 1, 1, 2),
    _AdaptFilterName_Type()
)
adaptFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptFilterName.setStatus("current")


class _AdaptFilterUUID_Type(OctetString):
    """Custom type adaptFilterUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdaptFilterUUID_Type.__name__ = "OctetString"
_AdaptFilterUUID_Object = MibTableColumn
adaptFilterUUID = _AdaptFilterUUID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 1, 1, 3),
    _AdaptFilterUUID_Type()
)
adaptFilterUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptFilterUUID.setStatus("current")


class _AdaptFilterSegment_Type(OctetString):
    """Custom type adaptFilterSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdaptFilterSegment_Type.__name__ = "OctetString"
_AdaptFilterSegment_Object = MibTableColumn
adaptFilterSegment = _AdaptFilterSegment_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 1, 1, 4),
    _AdaptFilterSegment_Type()
)
adaptFilterSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptFilterSegment.setStatus("deprecated")
_AdaptFilterEnabledState_Type = PolicyState
_AdaptFilterEnabledState_Object = MibTableColumn
adaptFilterEnabledState = _AdaptFilterEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 1, 1, 5),
    _AdaptFilterEnabledState_Type()
)
adaptFilterEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptFilterEnabledState.setStatus("current")


class _AdaptFilterSigID_Type(OctetString):
    """Custom type adaptFilterSigID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdaptFilterSigID_Type.__name__ = "OctetString"
_AdaptFilterSigID_Object = MibTableColumn
adaptFilterSigID = _AdaptFilterSigID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 1, 1, 7),
    _AdaptFilterSigID_Type()
)
adaptFilterSigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptFilterSigID.setStatus("current")


class _AdaptFilterProfile_Type(OctetString):
    """Custom type adaptFilterProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AdaptFilterProfile_Type.__name__ = "OctetString"
_AdaptFilterProfile_Object = MibTableColumn
adaptFilterProfile = _AdaptFilterProfile_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 1, 1, 8),
    _AdaptFilterProfile_Type()
)
adaptFilterProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptFilterProfile.setStatus("current")
_ConnectionBlockTable_Object = MibTable
connectionBlockTable = _ConnectionBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    connectionBlockTable.setStatus("current")
_ConnectionBlockEntry_Object = MibTableRow
connectionBlockEntry = _ConnectionBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1)
)
connectionBlockEntry.setIndexNames(
    (0, "TPT-TSE-MIB", "connectionBlockIndex"),
)
if mibBuilder.loadTexts:
    connectionBlockEntry.setStatus("current")


class _ConnectionBlockIndex_Type(Unsigned32):
    """Custom type connectionBlockIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ConnectionBlockIndex_Type.__name__ = "Unsigned32"
_ConnectionBlockIndex_Object = MibTableColumn
connectionBlockIndex = _ConnectionBlockIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 1),
    _ConnectionBlockIndex_Type()
)
connectionBlockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connectionBlockIndex.setStatus("current")


class _ConnectionBlockSrcAddr_Type(OctetString):
    """Custom type connectionBlockSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConnectionBlockSrcAddr_Type.__name__ = "OctetString"
_ConnectionBlockSrcAddr_Object = MibTableColumn
connectionBlockSrcAddr = _ConnectionBlockSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 2),
    _ConnectionBlockSrcAddr_Type()
)
connectionBlockSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockSrcAddr.setStatus("current")
_ConnectionBlockSrcPort_Type = Unsigned32
_ConnectionBlockSrcPort_Object = MibTableColumn
connectionBlockSrcPort = _ConnectionBlockSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 3),
    _ConnectionBlockSrcPort_Type()
)
connectionBlockSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockSrcPort.setStatus("current")


class _ConnectionBlockDestAddr_Type(OctetString):
    """Custom type connectionBlockDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConnectionBlockDestAddr_Type.__name__ = "OctetString"
_ConnectionBlockDestAddr_Object = MibTableColumn
connectionBlockDestAddr = _ConnectionBlockDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 4),
    _ConnectionBlockDestAddr_Type()
)
connectionBlockDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockDestAddr.setStatus("current")
_ConnectionBlockDestPort_Type = Unsigned32
_ConnectionBlockDestPort_Object = MibTableColumn
connectionBlockDestPort = _ConnectionBlockDestPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 5),
    _ConnectionBlockDestPort_Type()
)
connectionBlockDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockDestPort.setStatus("current")


class _ConnectionBlockProtocol_Type(OctetString):
    """Custom type connectionBlockProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConnectionBlockProtocol_Type.__name__ = "OctetString"
_ConnectionBlockProtocol_Object = MibTableColumn
connectionBlockProtocol = _ConnectionBlockProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 6),
    _ConnectionBlockProtocol_Type()
)
connectionBlockProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockProtocol.setStatus("current")


class _ConnectionBlockPort_Type(OctetString):
    """Custom type connectionBlockPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ConnectionBlockPort_Type.__name__ = "OctetString"
_ConnectionBlockPort_Object = MibTableColumn
connectionBlockPort = _ConnectionBlockPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 7),
    _ConnectionBlockPort_Type()
)
connectionBlockPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockPort.setStatus("current")


class _ConnectionBlockReason_Type(OctetString):
    """Custom type connectionBlockReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ConnectionBlockReason_Type.__name__ = "OctetString"
_ConnectionBlockReason_Object = MibTableColumn
connectionBlockReason = _ConnectionBlockReason_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 8),
    _ConnectionBlockReason_Type()
)
connectionBlockReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockReason.setStatus("current")


class _ConnectionBlockSrcAddrV6_Type(OctetString):
    """Custom type connectionBlockSrcAddrV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_ConnectionBlockSrcAddrV6_Type.__name__ = "OctetString"
_ConnectionBlockSrcAddrV6_Object = MibTableColumn
connectionBlockSrcAddrV6 = _ConnectionBlockSrcAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 9),
    _ConnectionBlockSrcAddrV6_Type()
)
connectionBlockSrcAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockSrcAddrV6.setStatus("current")


class _ConnectionBlockDestAddrV6_Type(OctetString):
    """Custom type connectionBlockDestAddrV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_ConnectionBlockDestAddrV6_Type.__name__ = "OctetString"
_ConnectionBlockDestAddrV6_Object = MibTableColumn
connectionBlockDestAddrV6 = _ConnectionBlockDestAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 2, 1, 10),
    _ConnectionBlockDestAddrV6_Type()
)
connectionBlockDestAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockDestAddrV6.setStatus("current")
_ConnectionBlockTotalCount_Type = Unsigned32
_ConnectionBlockTotalCount_Object = MibScalar
connectionBlockTotalCount = _ConnectionBlockTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 3),
    _ConnectionBlockTotalCount_Type()
)
connectionBlockTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionBlockTotalCount.setStatus("current")
_RateLimitStreamTable_Object = MibTable
rateLimitStreamTable = _RateLimitStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4)
)
if mibBuilder.loadTexts:
    rateLimitStreamTable.setStatus("current")
_RateLimitStreamEntry_Object = MibTableRow
rateLimitStreamEntry = _RateLimitStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1)
)
rateLimitStreamEntry.setIndexNames(
    (0, "TPT-TSE-MIB", "rateLimitStreamIndex"),
)
if mibBuilder.loadTexts:
    rateLimitStreamEntry.setStatus("current")


class _RateLimitStreamIndex_Type(Unsigned32):
    """Custom type rateLimitStreamIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_RateLimitStreamIndex_Type.__name__ = "Unsigned32"
_RateLimitStreamIndex_Object = MibTableColumn
rateLimitStreamIndex = _RateLimitStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 1),
    _RateLimitStreamIndex_Type()
)
rateLimitStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rateLimitStreamIndex.setStatus("current")


class _RateLimitStreamSrcAddr_Type(OctetString):
    """Custom type rateLimitStreamSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RateLimitStreamSrcAddr_Type.__name__ = "OctetString"
_RateLimitStreamSrcAddr_Object = MibTableColumn
rateLimitStreamSrcAddr = _RateLimitStreamSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 2),
    _RateLimitStreamSrcAddr_Type()
)
rateLimitStreamSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamSrcAddr.setStatus("current")
_RateLimitStreamSrcPort_Type = Unsigned32
_RateLimitStreamSrcPort_Object = MibTableColumn
rateLimitStreamSrcPort = _RateLimitStreamSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 3),
    _RateLimitStreamSrcPort_Type()
)
rateLimitStreamSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamSrcPort.setStatus("current")


class _RateLimitStreamDestAddr_Type(OctetString):
    """Custom type rateLimitStreamDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RateLimitStreamDestAddr_Type.__name__ = "OctetString"
_RateLimitStreamDestAddr_Object = MibTableColumn
rateLimitStreamDestAddr = _RateLimitStreamDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 4),
    _RateLimitStreamDestAddr_Type()
)
rateLimitStreamDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamDestAddr.setStatus("current")
_RateLimitStreamDestPort_Type = Unsigned32
_RateLimitStreamDestPort_Object = MibTableColumn
rateLimitStreamDestPort = _RateLimitStreamDestPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 5),
    _RateLimitStreamDestPort_Type()
)
rateLimitStreamDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamDestPort.setStatus("current")


class _RateLimitStreamProtocol_Type(OctetString):
    """Custom type rateLimitStreamProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RateLimitStreamProtocol_Type.__name__ = "OctetString"
_RateLimitStreamProtocol_Object = MibTableColumn
rateLimitStreamProtocol = _RateLimitStreamProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 6),
    _RateLimitStreamProtocol_Type()
)
rateLimitStreamProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamProtocol.setStatus("current")


class _RateLimitStreamPort_Type(OctetString):
    """Custom type rateLimitStreamPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_RateLimitStreamPort_Type.__name__ = "OctetString"
_RateLimitStreamPort_Object = MibTableColumn
rateLimitStreamPort = _RateLimitStreamPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 7),
    _RateLimitStreamPort_Type()
)
rateLimitStreamPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamPort.setStatus("current")


class _RateLimitStreamReason_Type(OctetString):
    """Custom type rateLimitStreamReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RateLimitStreamReason_Type.__name__ = "OctetString"
_RateLimitStreamReason_Object = MibTableColumn
rateLimitStreamReason = _RateLimitStreamReason_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 8),
    _RateLimitStreamReason_Type()
)
rateLimitStreamReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamReason.setStatus("current")


class _RateLimitStreamSrcAddrV6_Type(OctetString):
    """Custom type rateLimitStreamSrcAddrV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_RateLimitStreamSrcAddrV6_Type.__name__ = "OctetString"
_RateLimitStreamSrcAddrV6_Object = MibTableColumn
rateLimitStreamSrcAddrV6 = _RateLimitStreamSrcAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 9),
    _RateLimitStreamSrcAddrV6_Type()
)
rateLimitStreamSrcAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamSrcAddrV6.setStatus("current")


class _RateLimitStreamDestAddrV6_Type(OctetString):
    """Custom type rateLimitStreamDestAddrV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_RateLimitStreamDestAddrV6_Type.__name__ = "OctetString"
_RateLimitStreamDestAddrV6_Object = MibTableColumn
rateLimitStreamDestAddrV6 = _RateLimitStreamDestAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 4, 1, 10),
    _RateLimitStreamDestAddrV6_Type()
)
rateLimitStreamDestAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamDestAddrV6.setStatus("current")
_RateLimitStreamTotalCount_Type = Unsigned32
_RateLimitStreamTotalCount_Object = MibScalar
rateLimitStreamTotalCount = _RateLimitStreamTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 5),
    _RateLimitStreamTotalCount_Type()
)
rateLimitStreamTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitStreamTotalCount.setStatus("current")
_ConnectionTrustTable_Object = MibTable
connectionTrustTable = _ConnectionTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6)
)
if mibBuilder.loadTexts:
    connectionTrustTable.setStatus("current")
_ConnectionTrustEntry_Object = MibTableRow
connectionTrustEntry = _ConnectionTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1)
)
connectionTrustEntry.setIndexNames(
    (0, "TPT-TSE-MIB", "connectionTrustIndex"),
)
if mibBuilder.loadTexts:
    connectionTrustEntry.setStatus("current")


class _ConnectionTrustIndex_Type(Unsigned32):
    """Custom type connectionTrustIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ConnectionTrustIndex_Type.__name__ = "Unsigned32"
_ConnectionTrustIndex_Object = MibTableColumn
connectionTrustIndex = _ConnectionTrustIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 1),
    _ConnectionTrustIndex_Type()
)
connectionTrustIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connectionTrustIndex.setStatus("current")


class _ConnectionTrustSrcAddr_Type(OctetString):
    """Custom type connectionTrustSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConnectionTrustSrcAddr_Type.__name__ = "OctetString"
_ConnectionTrustSrcAddr_Object = MibTableColumn
connectionTrustSrcAddr = _ConnectionTrustSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 2),
    _ConnectionTrustSrcAddr_Type()
)
connectionTrustSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustSrcAddr.setStatus("current")
_ConnectionTrustSrcPort_Type = Unsigned32
_ConnectionTrustSrcPort_Object = MibTableColumn
connectionTrustSrcPort = _ConnectionTrustSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 3),
    _ConnectionTrustSrcPort_Type()
)
connectionTrustSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustSrcPort.setStatus("current")


class _ConnectionTrustDestAddr_Type(OctetString):
    """Custom type connectionTrustDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConnectionTrustDestAddr_Type.__name__ = "OctetString"
_ConnectionTrustDestAddr_Object = MibTableColumn
connectionTrustDestAddr = _ConnectionTrustDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 4),
    _ConnectionTrustDestAddr_Type()
)
connectionTrustDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustDestAddr.setStatus("current")
_ConnectionTrustDestPort_Type = Unsigned32
_ConnectionTrustDestPort_Object = MibTableColumn
connectionTrustDestPort = _ConnectionTrustDestPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 5),
    _ConnectionTrustDestPort_Type()
)
connectionTrustDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustDestPort.setStatus("current")


class _ConnectionTrustProtocol_Type(OctetString):
    """Custom type connectionTrustProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConnectionTrustProtocol_Type.__name__ = "OctetString"
_ConnectionTrustProtocol_Object = MibTableColumn
connectionTrustProtocol = _ConnectionTrustProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 6),
    _ConnectionTrustProtocol_Type()
)
connectionTrustProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustProtocol.setStatus("current")


class _ConnectionTrustPort_Type(OctetString):
    """Custom type connectionTrustPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ConnectionTrustPort_Type.__name__ = "OctetString"
_ConnectionTrustPort_Object = MibTableColumn
connectionTrustPort = _ConnectionTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 7),
    _ConnectionTrustPort_Type()
)
connectionTrustPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustPort.setStatus("current")


class _ConnectionTrustReason_Type(OctetString):
    """Custom type connectionTrustReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ConnectionTrustReason_Type.__name__ = "OctetString"
_ConnectionTrustReason_Object = MibTableColumn
connectionTrustReason = _ConnectionTrustReason_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 8),
    _ConnectionTrustReason_Type()
)
connectionTrustReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustReason.setStatus("current")


class _ConnectionTrustSrcAddrV6_Type(OctetString):
    """Custom type connectionTrustSrcAddrV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_ConnectionTrustSrcAddrV6_Type.__name__ = "OctetString"
_ConnectionTrustSrcAddrV6_Object = MibTableColumn
connectionTrustSrcAddrV6 = _ConnectionTrustSrcAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 9),
    _ConnectionTrustSrcAddrV6_Type()
)
connectionTrustSrcAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustSrcAddrV6.setStatus("current")


class _ConnectionTrustDestAddrV6_Type(OctetString):
    """Custom type connectionTrustDestAddrV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_ConnectionTrustDestAddrV6_Type.__name__ = "OctetString"
_ConnectionTrustDestAddrV6_Object = MibTableColumn
connectionTrustDestAddrV6 = _ConnectionTrustDestAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 6, 1, 10),
    _ConnectionTrustDestAddrV6_Type()
)
connectionTrustDestAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustDestAddrV6.setStatus("current")
_ConnectionTrustTotalCount_Type = Unsigned32
_ConnectionTrustTotalCount_Object = MibScalar
connectionTrustTotalCount = _ConnectionTrustTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 7, 7),
    _ConnectionTrustTotalCount_Type()
)
connectionTrustTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionTrustTotalCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-TSE-MIB",
    **{"PolicyState": PolicyState,
       "tpt-tse": tpt_tse,
       "topTenAdaptFilterTable": topTenAdaptFilterTable,
       "topTenAdaptFilterEntry": topTenAdaptFilterEntry,
       "topTenAdaptFilterRank": topTenAdaptFilterRank,
       "adaptFilterName": adaptFilterName,
       "adaptFilterUUID": adaptFilterUUID,
       "adaptFilterSegment": adaptFilterSegment,
       "adaptFilterEnabledState": adaptFilterEnabledState,
       "adaptFilterSigID": adaptFilterSigID,
       "adaptFilterProfile": adaptFilterProfile,
       "connectionBlockTable": connectionBlockTable,
       "connectionBlockEntry": connectionBlockEntry,
       "connectionBlockIndex": connectionBlockIndex,
       "connectionBlockSrcAddr": connectionBlockSrcAddr,
       "connectionBlockSrcPort": connectionBlockSrcPort,
       "connectionBlockDestAddr": connectionBlockDestAddr,
       "connectionBlockDestPort": connectionBlockDestPort,
       "connectionBlockProtocol": connectionBlockProtocol,
       "connectionBlockPort": connectionBlockPort,
       "connectionBlockReason": connectionBlockReason,
       "connectionBlockSrcAddrV6": connectionBlockSrcAddrV6,
       "connectionBlockDestAddrV6": connectionBlockDestAddrV6,
       "connectionBlockTotalCount": connectionBlockTotalCount,
       "rateLimitStreamTable": rateLimitStreamTable,
       "rateLimitStreamEntry": rateLimitStreamEntry,
       "rateLimitStreamIndex": rateLimitStreamIndex,
       "rateLimitStreamSrcAddr": rateLimitStreamSrcAddr,
       "rateLimitStreamSrcPort": rateLimitStreamSrcPort,
       "rateLimitStreamDestAddr": rateLimitStreamDestAddr,
       "rateLimitStreamDestPort": rateLimitStreamDestPort,
       "rateLimitStreamProtocol": rateLimitStreamProtocol,
       "rateLimitStreamPort": rateLimitStreamPort,
       "rateLimitStreamReason": rateLimitStreamReason,
       "rateLimitStreamSrcAddrV6": rateLimitStreamSrcAddrV6,
       "rateLimitStreamDestAddrV6": rateLimitStreamDestAddrV6,
       "rateLimitStreamTotalCount": rateLimitStreamTotalCount,
       "connectionTrustTable": connectionTrustTable,
       "connectionTrustEntry": connectionTrustEntry,
       "connectionTrustIndex": connectionTrustIndex,
       "connectionTrustSrcAddr": connectionTrustSrcAddr,
       "connectionTrustSrcPort": connectionTrustSrcPort,
       "connectionTrustDestAddr": connectionTrustDestAddr,
       "connectionTrustDestPort": connectionTrustDestPort,
       "connectionTrustProtocol": connectionTrustProtocol,
       "connectionTrustPort": connectionTrustPort,
       "connectionTrustReason": connectionTrustReason,
       "connectionTrustSrcAddrV6": connectionTrustSrcAddrV6,
       "connectionTrustDestAddrV6": connectionTrustDestAddrV6,
       "connectionTrustTotalCount": connectionTrustTotalCount}
)
