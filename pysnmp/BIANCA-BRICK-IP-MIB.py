# SNMP MIB module (BIANCA-BRICK-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:28 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_IpExtIfTable_Object = MibTable
ipExtIfTable = _IpExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3)
)
if mibBuilder.loadTexts:
    ipExtIfTable.setStatus("mandatory")
_IpExtIfEntry_Object = MibTableRow
ipExtIfEntry = _IpExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1)
)
ipExtIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipExtIfIndex"),
)
if mibBuilder.loadTexts:
    ipExtIfEntry.setStatus("mandatory")
_IpExtIfIndex_Type = Integer32
_IpExtIfIndex_Object = MibTableColumn
ipExtIfIndex = _IpExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 1),
    _IpExtIfIndex_Type()
)
ipExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipExtIfIndex.setStatus("mandatory")


class _IpExtIfRipSend_Type(Integer32):
    """Custom type ipExtIfRipSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("none", 4),
          ("ripV1", 1),
          ("ripV2", 2),
          ("ripV2mcast", 5))
    )


_IpExtIfRipSend_Type.__name__ = "Integer32"
_IpExtIfRipSend_Object = MibTableColumn
ipExtIfRipSend = _IpExtIfRipSend_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 3),
    _IpExtIfRipSend_Type()
)
ipExtIfRipSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfRipSend.setStatus("mandatory")


class _IpExtIfRipReceive_Type(Integer32):
    """Custom type ipExtIfRipReceive based on Integer32"""
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
        *(("both", 3),
          ("none", 4),
          ("ripV1", 1),
          ("ripV2", 2))
    )


_IpExtIfRipReceive_Type.__name__ = "Integer32"
_IpExtIfRipReceive_Object = MibTableColumn
ipExtIfRipReceive = _IpExtIfRipReceive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 4),
    _IpExtIfRipReceive_Type()
)
ipExtIfRipReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfRipReceive.setStatus("mandatory")


class _IpExtIfProxyArp_Type(Integer32):
    """Custom type ipExtIfProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("up-only", 3))
    )


_IpExtIfProxyArp_Type.__name__ = "Integer32"
_IpExtIfProxyArp_Object = MibScalar
ipExtIfProxyArp = _IpExtIfProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 5),
    _IpExtIfProxyArp_Type()
)
ipExtIfProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfProxyArp.setStatus("mandatory")


class _IpExtIfNat_Type(Integer32):
    """Custom type ipExtIfNat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("reverse", 3))
    )


_IpExtIfNat_Type.__name__ = "Integer32"
_IpExtIfNat_Object = MibTableColumn
ipExtIfNat = _IpExtIfNat_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 6),
    _IpExtIfNat_Type()
)
ipExtIfNat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfNat.setStatus("mandatory")


class _IpExtIfNatRmvFin_Type(Integer32):
    """Custom type ipExtIfNatRmvFin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpExtIfNatRmvFin_Type.__name__ = "Integer32"
_IpExtIfNatRmvFin_Object = MibTableColumn
ipExtIfNatRmvFin = _IpExtIfNatRmvFin_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 7),
    _IpExtIfNatRmvFin_Type()
)
ipExtIfNatRmvFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfNatRmvFin.setStatus("mandatory")


class _IpExtIfNatTcpTimeout_Type(Integer32):
    """Custom type ipExtIfNatTcpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpExtIfNatTcpTimeout_Type.__name__ = "Integer32"
_IpExtIfNatTcpTimeout_Object = MibTableColumn
ipExtIfNatTcpTimeout = _IpExtIfNatTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 8),
    _IpExtIfNatTcpTimeout_Type()
)
ipExtIfNatTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfNatTcpTimeout.setStatus("mandatory")


class _IpExtIfNatOtherTimeout_Type(Integer32):
    """Custom type ipExtIfNatOtherTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpExtIfNatOtherTimeout_Type.__name__ = "Integer32"
_IpExtIfNatOtherTimeout_Object = MibTableColumn
ipExtIfNatOtherTimeout = _IpExtIfNatOtherTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 9),
    _IpExtIfNatOtherTimeout_Type()
)
ipExtIfNatOtherTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfNatOtherTimeout.setStatus("mandatory")


class _IpExtIfNatOutXlat_Type(Integer32):
    """Custom type ipExtIfNatOutXlat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IpExtIfNatOutXlat_Type.__name__ = "Integer32"
_IpExtIfNatOutXlat_Object = MibTableColumn
ipExtIfNatOutXlat = _IpExtIfNatOutXlat_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 10),
    _IpExtIfNatOutXlat_Type()
)
ipExtIfNatOutXlat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfNatOutXlat.setStatus("mandatory")


class _IpExtIfAccounting_Type(Integer32):
    """Custom type ipExtIfAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpExtIfAccounting_Type.__name__ = "Integer32"
_IpExtIfAccounting_Object = MibTableColumn
ipExtIfAccounting = _IpExtIfAccounting_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 11),
    _IpExtIfAccounting_Type()
)
ipExtIfAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfAccounting.setStatus("mandatory")


class _IpExtIfTcpSpoofing_Type(Integer32):
    """Custom type ipExtIfTcpSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpExtIfTcpSpoofing_Type.__name__ = "Integer32"
_IpExtIfTcpSpoofing_Object = MibTableColumn
ipExtIfTcpSpoofing = _IpExtIfTcpSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 12),
    _IpExtIfTcpSpoofing_Type()
)
ipExtIfTcpSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfTcpSpoofing.setStatus("mandatory")


class _IpExtIfAccessAction_Type(Integer32):
    """Custom type ipExtIfAccessAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("refuse", 2))
    )


_IpExtIfAccessAction_Type.__name__ = "Integer32"
_IpExtIfAccessAction_Object = MibScalar
ipExtIfAccessAction = _IpExtIfAccessAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 13),
    _IpExtIfAccessAction_Type()
)
ipExtIfAccessAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfAccessAction.setStatus("mandatory")


class _IpExtIfAccessReport_Type(Integer32):
    """Custom type ipExtIfAccessReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dump", 3),
          ("info", 2),
          ("none", 1))
    )


_IpExtIfAccessReport_Type.__name__ = "Integer32"
_IpExtIfAccessReport_Object = MibScalar
ipExtIfAccessReport = _IpExtIfAccessReport_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 14),
    _IpExtIfAccessReport_Type()
)
ipExtIfAccessReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfAccessReport.setStatus("mandatory")


class _IpExtIfOspf_Type(Integer32):
    """Custom type ipExtIfOspf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("off", 3),
          ("passive", 1))
    )


_IpExtIfOspf_Type.__name__ = "Integer32"
_IpExtIfOspf_Object = MibTableColumn
ipExtIfOspf = _IpExtIfOspf_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 15),
    _IpExtIfOspf_Type()
)
ipExtIfOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfOspf.setStatus("mandatory")


class _IpExtIfOspfMetric_Type(Integer32):
    """Custom type ipExtIfOspfMetric based on Integer32"""
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
        *(("auto", 1),
          ("auto-adjust", 3),
          ("fixed", 2),
          ("fixed-adjust", 4))
    )


_IpExtIfOspfMetric_Type.__name__ = "Integer32"
_IpExtIfOspfMetric_Object = MibTableColumn
ipExtIfOspfMetric = _IpExtIfOspfMetric_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 16),
    _IpExtIfOspfMetric_Type()
)
ipExtIfOspfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfOspfMetric.setStatus("mandatory")


class _IpExtIfTcpCksum_Type(Integer32):
    """Custom type ipExtIfTcpCksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("check", 1),
          ("dont-check", 2))
    )


_IpExtIfTcpCksum_Type.__name__ = "Integer32"
_IpExtIfTcpCksum_Object = MibTableColumn
ipExtIfTcpCksum = _IpExtIfTcpCksum_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 17),
    _IpExtIfTcpCksum_Type()
)
ipExtIfTcpCksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfTcpCksum.setStatus("mandatory")


class _IpExtIfBackRtVerify_Type(Integer32):
    """Custom type ipExtIfBackRtVerify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpExtIfBackRtVerify_Type.__name__ = "Integer32"
_IpExtIfBackRtVerify_Object = MibTableColumn
ipExtIfBackRtVerify = _IpExtIfBackRtVerify_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 18),
    _IpExtIfBackRtVerify_Type()
)
ipExtIfBackRtVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfBackRtVerify.setStatus("mandatory")
_IpExtIfRuleIndex_Type = Integer32
_IpExtIfRuleIndex_Object = MibTableColumn
ipExtIfRuleIndex = _IpExtIfRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 19),
    _IpExtIfRuleIndex_Type()
)
ipExtIfRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfRuleIndex.setStatus("mandatory")


class _IpExtIfAuthentication_Type(Integer32):
    """Custom type ipExtIfAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("securID", 2))
    )


_IpExtIfAuthentication_Type.__name__ = "Integer32"
_IpExtIfAuthentication_Object = MibTableColumn
ipExtIfAuthentication = _IpExtIfAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 20),
    _IpExtIfAuthentication_Type()
)
ipExtIfAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfAuthentication.setStatus("mandatory")


class _IpExtIfAuthMode_Type(Integer32):
    """Custom type ipExtIfAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )


_IpExtIfAuthMode_Type.__name__ = "Integer32"
_IpExtIfAuthMode_Object = MibTableColumn
ipExtIfAuthMode = _IpExtIfAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 21),
    _IpExtIfAuthMode_Type()
)
ipExtIfAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfAuthMode.setStatus("mandatory")


class _IpExtIfAuthLifeTime_Type(Integer32):
    """Custom type ipExtIfAuthLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 36000),
    )


_IpExtIfAuthLifeTime_Type.__name__ = "Integer32"
_IpExtIfAuthLifeTime_Object = MibTableColumn
ipExtIfAuthLifeTime = _IpExtIfAuthLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 22),
    _IpExtIfAuthLifeTime_Type()
)
ipExtIfAuthLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfAuthLifeTime.setStatus("mandatory")
_IpExtIfAuthKeepalive_Type = Integer32
_IpExtIfAuthKeepalive_Object = MibTableColumn
ipExtIfAuthKeepalive = _IpExtIfAuthKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 23),
    _IpExtIfAuthKeepalive_Type()
)
ipExtIfAuthKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfAuthKeepalive.setStatus("mandatory")


class _IpExtIfRouteAnnounce_Type(Integer32):
    """Custom type ipExtIfRouteAnnounce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 3),
          ("up-dormant", 2),
          ("up-only", 1))
    )


_IpExtIfRouteAnnounce_Type.__name__ = "Integer32"
_IpExtIfRouteAnnounce_Object = MibTableColumn
ipExtIfRouteAnnounce = _IpExtIfRouteAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 24),
    _IpExtIfRouteAnnounce_Type()
)
ipExtIfRouteAnnounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfRouteAnnounce.setStatus("mandatory")


class _IpExtIfIpFragmentation_Type(Integer32):
    """Custom type ipExtIfIpFragmentation based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("equal", 3),
          ("reverse", 4))
    )


_IpExtIfIpFragmentation_Type.__name__ = "Integer32"
_IpExtIfIpFragmentation_Object = MibTableColumn
ipExtIfIpFragmentation = _IpExtIfIpFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 25),
    _IpExtIfIpFragmentation_Type()
)
ipExtIfIpFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfIpFragmentation.setStatus("mandatory")


class _IpExtIfRerouting_Type(Integer32):
    """Custom type ipExtIfRerouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpExtIfRerouting_Type.__name__ = "Integer32"
_IpExtIfRerouting_Object = MibTableColumn
ipExtIfRerouting = _IpExtIfRerouting_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 26),
    _IpExtIfRerouting_Type()
)
ipExtIfRerouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfRerouting.setStatus("mandatory")
_IpExtIfBodRuleIndex_Type = Integer32
_IpExtIfBodRuleIndex_Object = MibTableColumn
ipExtIfBodRuleIndex = _IpExtIfBodRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 27),
    _IpExtIfBodRuleIndex_Type()
)
ipExtIfBodRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfBodRuleIndex.setStatus("mandatory")
_IpExtIfQosRuleIndex_Type = Integer32
_IpExtIfQosRuleIndex_Object = MibScalar
ipExtIfQosRuleIndex = _IpExtIfQosRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 28),
    _IpExtIfQosRuleIndex_Type()
)
ipExtIfQosRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfQosRuleIndex.setStatus("mandatory")


class _IpExtIfIpsecAccounting_Type(Integer32):
    """Custom type ipExtIfIpsecAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("clear", 2),
          ("ipsec", 1))
    )


_IpExtIfIpsecAccounting_Type.__name__ = "Integer32"
_IpExtIfIpsecAccounting_Object = MibTableColumn
ipExtIfIpsecAccounting = _IpExtIfIpsecAccounting_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 29),
    _IpExtIfIpsecAccounting_Type()
)
ipExtIfIpsecAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfIpsecAccounting.setStatus("mandatory")


class _IpExtIfMulticast_Type(Integer32):
    """Custom type ipExtIfMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpExtIfMulticast_Type.__name__ = "Integer32"
_IpExtIfMulticast_Object = MibTableColumn
ipExtIfMulticast = _IpExtIfMulticast_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 30),
    _IpExtIfMulticast_Type()
)
ipExtIfMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfMulticast.setStatus("mandatory")


class _IpExtIfNatSilentDeny_Type(Integer32):
    """Custom type ipExtIfNatSilentDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpExtIfNatSilentDeny_Type.__name__ = "Integer32"
_IpExtIfNatSilentDeny_Object = MibTableColumn
ipExtIfNatSilentDeny = _IpExtIfNatSilentDeny_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 3, 1, 31),
    _IpExtIfNatSilentDeny_Type()
)
ipExtIfNatSilentDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtIfNatSilentDeny.setStatus("mandatory")
_IpExtRtTable_Object = MibTable
ipExtRtTable = _IpExtRtTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4)
)
if mibBuilder.loadTexts:
    ipExtRtTable.setStatus("mandatory")
_IpExtRtEntry_Object = MibTableRow
ipExtRtEntry = _IpExtRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1)
)
ipExtRtEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipExtRtProtocol"),
)
if mibBuilder.loadTexts:
    ipExtRtEntry.setStatus("mandatory")


class _IpExtRtProtocol_Type(Integer32):
    """Custom type ipExtRtProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6,
              8,
              12,
              17,
              20,
              22,
              27,
              46,
              47,
              50,
              51,
              88,
              89,
              115,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("dont-verify", 256),
          ("egp", 8),
          ("esp", 50),
          ("ggp", 3),
          ("gre", 47),
          ("hmp", 20),
          ("icmp", 1),
          ("igrp", 88),
          ("l2tp", 115),
          ("ospf", 89),
          ("pup", 12),
          ("rdp", 27),
          ("rsvp", 46),
          ("tcp", 6),
          ("udp", 17),
          ("xns-idp", 22))
    )


_IpExtRtProtocol_Type.__name__ = "Integer32"
_IpExtRtProtocol_Object = MibTableColumn
ipExtRtProtocol = _IpExtRtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 1),
    _IpExtRtProtocol_Type()
)
ipExtRtProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtProtocol.setStatus("mandatory")
_IpExtRtSrcIfIndex_Type = Integer32
_IpExtRtSrcIfIndex_Object = MibTableColumn
ipExtRtSrcIfIndex = _IpExtRtSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 2),
    _IpExtRtSrcIfIndex_Type()
)
ipExtRtSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtSrcIfIndex.setStatus("mandatory")
_IpExtRtSrcAddr_Type = IpAddress
_IpExtRtSrcAddr_Object = MibTableColumn
ipExtRtSrcAddr = _IpExtRtSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 3),
    _IpExtRtSrcAddr_Type()
)
ipExtRtSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtSrcAddr.setStatus("mandatory")
_IpExtRtSrcMask_Type = IpAddress
_IpExtRtSrcMask_Object = MibTableColumn
ipExtRtSrcMask = _IpExtRtSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 4),
    _IpExtRtSrcMask_Type()
)
ipExtRtSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtSrcMask.setStatus("mandatory")


class _IpExtRtSrcPort_Type(Integer32):
    """Custom type ipExtRtSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpExtRtSrcPort_Type.__name__ = "Integer32"
_IpExtRtSrcPort_Object = MibTableColumn
ipExtRtSrcPort = _IpExtRtSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 5),
    _IpExtRtSrcPort_Type()
)
ipExtRtSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtSrcPort.setStatus("mandatory")


class _IpExtRtSrcPortRange_Type(Integer32):
    """Custom type ipExtRtSrcPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpExtRtSrcPortRange_Type.__name__ = "Integer32"
_IpExtRtSrcPortRange_Object = MibTableColumn
ipExtRtSrcPortRange = _IpExtRtSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 6),
    _IpExtRtSrcPortRange_Type()
)
ipExtRtSrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtSrcPortRange.setStatus("mandatory")
_IpExtRtDstAddr_Type = IpAddress
_IpExtRtDstAddr_Object = MibTableColumn
ipExtRtDstAddr = _IpExtRtDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 7),
    _IpExtRtDstAddr_Type()
)
ipExtRtDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtDstAddr.setStatus("mandatory")
_IpExtRtDstMask_Type = IpAddress
_IpExtRtDstMask_Object = MibTableColumn
ipExtRtDstMask = _IpExtRtDstMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 8),
    _IpExtRtDstMask_Type()
)
ipExtRtDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtDstMask.setStatus("mandatory")


class _IpExtRtDstPort_Type(Integer32):
    """Custom type ipExtRtDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpExtRtDstPort_Type.__name__ = "Integer32"
_IpExtRtDstPort_Object = MibTableColumn
ipExtRtDstPort = _IpExtRtDstPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 9),
    _IpExtRtDstPort_Type()
)
ipExtRtDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtDstPort.setStatus("mandatory")


class _IpExtRtDstPortRange_Type(Integer32):
    """Custom type ipExtRtDstPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpExtRtDstPortRange_Type.__name__ = "Integer32"
_IpExtRtDstPortRange_Object = MibTableColumn
ipExtRtDstPortRange = _IpExtRtDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 10),
    _IpExtRtDstPortRange_Type()
)
ipExtRtDstPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtDstPortRange.setStatus("mandatory")


class _IpExtRtTos_Type(Integer32):
    """Custom type ipExtRtTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpExtRtTos_Type.__name__ = "Integer32"
_IpExtRtTos_Object = MibTableColumn
ipExtRtTos = _IpExtRtTos_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 11),
    _IpExtRtTos_Type()
)
ipExtRtTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtTos.setStatus("mandatory")


class _IpExtRtTosMask_Type(Integer32):
    """Custom type ipExtRtTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpExtRtTosMask_Type.__name__ = "Integer32"
_IpExtRtTosMask_Object = MibTableColumn
ipExtRtTosMask = _IpExtRtTosMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 12),
    _IpExtRtTosMask_Type()
)
ipExtRtTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtTosMask.setStatus("mandatory")


class _IpExtRtDstIfMode_Type(Integer32):
    """Custom type ipExtRtDstIfMode based on Integer32"""
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
        *(("always", 4),
          ("dialup-continue", 2),
          ("dialup-wait", 1),
          ("up-only", 3))
    )


_IpExtRtDstIfMode_Type.__name__ = "Integer32"
_IpExtRtDstIfMode_Object = MibTableColumn
ipExtRtDstIfMode = _IpExtRtDstIfMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 13),
    _IpExtRtDstIfMode_Type()
)
ipExtRtDstIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtDstIfMode.setStatus("mandatory")
_IpExtRtDstIfIndex_Type = Integer32
_IpExtRtDstIfIndex_Object = MibTableColumn
ipExtRtDstIfIndex = _IpExtRtDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 14),
    _IpExtRtDstIfIndex_Type()
)
ipExtRtDstIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtDstIfIndex.setStatus("mandatory")
_IpExtRtNextHop_Type = IpAddress
_IpExtRtNextHop_Object = MibTableColumn
ipExtRtNextHop = _IpExtRtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 15),
    _IpExtRtNextHop_Type()
)
ipExtRtNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtNextHop.setStatus("mandatory")


class _IpExtRtType_Type(Integer32):
    """Custom type ipExtRtType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_IpExtRtType_Type.__name__ = "Integer32"
_IpExtRtType_Object = MibTableColumn
ipExtRtType = _IpExtRtType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 16),
    _IpExtRtType_Type()
)
ipExtRtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtType.setStatus("mandatory")
_IpExtRtMetric1_Type = Integer32
_IpExtRtMetric1_Object = MibTableColumn
ipExtRtMetric1 = _IpExtRtMetric1_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 17),
    _IpExtRtMetric1_Type()
)
ipExtRtMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtMetric1.setStatus("mandatory")
_IpExtRtMetric2_Type = Integer32
_IpExtRtMetric2_Object = MibTableColumn
ipExtRtMetric2 = _IpExtRtMetric2_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 18),
    _IpExtRtMetric2_Type()
)
ipExtRtMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtMetric2.setStatus("mandatory")
_IpExtRtMetric3_Type = Integer32
_IpExtRtMetric3_Object = MibTableColumn
ipExtRtMetric3 = _IpExtRtMetric3_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 19),
    _IpExtRtMetric3_Type()
)
ipExtRtMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtMetric3.setStatus("mandatory")
_IpExtRtMetric4_Type = Integer32
_IpExtRtMetric4_Object = MibTableColumn
ipExtRtMetric4 = _IpExtRtMetric4_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 20),
    _IpExtRtMetric4_Type()
)
ipExtRtMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtMetric4.setStatus("mandatory")
_IpExtRtMetric5_Type = Integer32
_IpExtRtMetric5_Object = MibTableColumn
ipExtRtMetric5 = _IpExtRtMetric5_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 21),
    _IpExtRtMetric5_Type()
)
ipExtRtMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtMetric5.setStatus("mandatory")


class _IpExtRtProto_Type(Integer32):
    """Custom type ipExtRtProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_IpExtRtProto_Type.__name__ = "Integer32"
_IpExtRtProto_Object = MibTableColumn
ipExtRtProto = _IpExtRtProto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 22),
    _IpExtRtProto_Type()
)
ipExtRtProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtProto.setStatus("mandatory")
_IpExtRtAge_Type = TimeTicks
_IpExtRtAge_Object = MibTableColumn
ipExtRtAge = _IpExtRtAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 4, 1, 23),
    _IpExtRtAge_Type()
)
ipExtRtAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipExtRtAge.setStatus("mandatory")
_IpNatTable_Object = MibTable
ipNatTable = _IpNatTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5)
)
if mibBuilder.loadTexts:
    ipNatTable.setStatus("mandatory")
_IpNatEntry_Object = MibTableRow
ipNatEntry = _IpNatEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1)
)
ipNatEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipNatIfIndex"),
    (0, "BIANCA-BRICK-IP-MIB", "ipNatProtocol"),
    (0, "BIANCA-BRICK-IP-MIB", "ipNatIntAddr"),
    (0, "BIANCA-BRICK-IP-MIB", "ipNatIntPort"),
)
if mibBuilder.loadTexts:
    ipNatEntry.setStatus("mandatory")
_IpNatIfIndex_Type = Integer32
_IpNatIfIndex_Object = MibTableColumn
ipNatIfIndex = _IpNatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 1),
    _IpNatIfIndex_Type()
)
ipNatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatIfIndex.setStatus("mandatory")


class _IpNatProtocol_Type(Integer32):
    """Custom type ipNatProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17,
              47,
              50,
              51,
              89,
              115)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("l2tp", 115),
          ("ospf", 89),
          ("tcp", 6),
          ("udp", 17))
    )


_IpNatProtocol_Type.__name__ = "Integer32"
_IpNatProtocol_Object = MibTableColumn
ipNatProtocol = _IpNatProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 2),
    _IpNatProtocol_Type()
)
ipNatProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatProtocol.setStatus("mandatory")
_IpNatIntAddr_Type = IpAddress
_IpNatIntAddr_Object = MibTableColumn
ipNatIntAddr = _IpNatIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 3),
    _IpNatIntAddr_Type()
)
ipNatIntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatIntAddr.setStatus("mandatory")


class _IpNatIntPort_Type(Integer32):
    """Custom type ipNatIntPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpNatIntPort_Type.__name__ = "Integer32"
_IpNatIntPort_Object = MibTableColumn
ipNatIntPort = _IpNatIntPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 4),
    _IpNatIntPort_Type()
)
ipNatIntPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatIntPort.setStatus("mandatory")
_IpNatExtAddr_Type = IpAddress
_IpNatExtAddr_Object = MibTableColumn
ipNatExtAddr = _IpNatExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 5),
    _IpNatExtAddr_Type()
)
ipNatExtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatExtAddr.setStatus("mandatory")


class _IpNatExtPort_Type(Integer32):
    """Custom type ipNatExtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpNatExtPort_Type.__name__ = "Integer32"
_IpNatExtPort_Object = MibTableColumn
ipNatExtPort = _IpNatExtPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 6),
    _IpNatExtPort_Type()
)
ipNatExtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatExtPort.setStatus("mandatory")
_IpNatRemoteAddr_Type = IpAddress
_IpNatRemoteAddr_Object = MibTableColumn
ipNatRemoteAddr = _IpNatRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 7),
    _IpNatRemoteAddr_Type()
)
ipNatRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatRemoteAddr.setStatus("mandatory")


class _IpNatRemotePort_Type(Integer32):
    """Custom type ipNatRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpNatRemotePort_Type.__name__ = "Integer32"
_IpNatRemotePort_Object = MibTableColumn
ipNatRemotePort = _IpNatRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 8),
    _IpNatRemotePort_Type()
)
ipNatRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatRemotePort.setStatus("mandatory")


class _IpNatDirection_Type(Integer32):
    """Custom type ipNatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_IpNatDirection_Type.__name__ = "Integer32"
_IpNatDirection_Object = MibTableColumn
ipNatDirection = _IpNatDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 9),
    _IpNatDirection_Type()
)
ipNatDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatDirection.setStatus("mandatory")
_IpNatAge_Type = TimeTicks
_IpNatAge_Object = MibTableColumn
ipNatAge = _IpNatAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 5, 1, 10),
    _IpNatAge_Type()
)
ipNatAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatAge.setStatus("mandatory")
_IpNatPresetTable_Object = MibTable
ipNatPresetTable = _IpNatPresetTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6)
)
if mibBuilder.loadTexts:
    ipNatPresetTable.setStatus("mandatory")
_IpNatPresetEntry_Object = MibTableRow
ipNatPresetEntry = _IpNatPresetEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1)
)
ipNatPresetEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipNatPrIfIndex"),
    (0, "BIANCA-BRICK-IP-MIB", "ipNatPrProtocol"),
    (0, "BIANCA-BRICK-IP-MIB", "ipNatPrExtPort"),
)
if mibBuilder.loadTexts:
    ipNatPresetEntry.setStatus("mandatory")
_IpNatPrIfIndex_Type = Integer32
_IpNatPrIfIndex_Object = MibTableColumn
ipNatPrIfIndex = _IpNatPrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 1),
    _IpNatPrIfIndex_Type()
)
ipNatPrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrIfIndex.setStatus("mandatory")


class _IpNatPrProtocol_Type(Integer32):
    """Custom type ipNatPrProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17,
              47,
              50,
              51,
              89,
              94,
              115,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("delete", 256),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("ipinip", 94),
          ("l2tp", 115),
          ("ospf", 89),
          ("tcp", 6),
          ("udp", 17))
    )


_IpNatPrProtocol_Type.__name__ = "Integer32"
_IpNatPrProtocol_Object = MibTableColumn
ipNatPrProtocol = _IpNatPrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 2),
    _IpNatPrProtocol_Type()
)
ipNatPrProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrProtocol.setStatus("mandatory")
_IpNatPrRemoteAddr_Type = IpAddress
_IpNatPrRemoteAddr_Object = MibTableColumn
ipNatPrRemoteAddr = _IpNatPrRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 3),
    _IpNatPrRemoteAddr_Type()
)
ipNatPrRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrRemoteAddr.setStatus("mandatory")
_IpNatPrRemoteMask_Type = IpAddress
_IpNatPrRemoteMask_Object = MibTableColumn
ipNatPrRemoteMask = _IpNatPrRemoteMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 4),
    _IpNatPrRemoteMask_Type()
)
ipNatPrRemoteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrRemoteMask.setStatus("mandatory")
_IpNatPrExtAddr_Type = IpAddress
_IpNatPrExtAddr_Object = MibTableColumn
ipNatPrExtAddr = _IpNatPrExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 5),
    _IpNatPrExtAddr_Type()
)
ipNatPrExtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrExtAddr.setStatus("mandatory")
_IpNatPrExtMask_Type = IpAddress
_IpNatPrExtMask_Object = MibTableColumn
ipNatPrExtMask = _IpNatPrExtMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 6),
    _IpNatPrExtMask_Type()
)
ipNatPrExtMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrExtMask.setStatus("mandatory")


class _IpNatPrExtPort_Type(Integer32):
    """Custom type ipNatPrExtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpNatPrExtPort_Type.__name__ = "Integer32"
_IpNatPrExtPort_Object = MibTableColumn
ipNatPrExtPort = _IpNatPrExtPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 7),
    _IpNatPrExtPort_Type()
)
ipNatPrExtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrExtPort.setStatus("mandatory")


class _IpNatPrExtPortRange_Type(Integer32):
    """Custom type ipNatPrExtPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpNatPrExtPortRange_Type.__name__ = "Integer32"
_IpNatPrExtPortRange_Object = MibTableColumn
ipNatPrExtPortRange = _IpNatPrExtPortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 8),
    _IpNatPrExtPortRange_Type()
)
ipNatPrExtPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrExtPortRange.setStatus("mandatory")
_IpNatPrIntAddr_Type = IpAddress
_IpNatPrIntAddr_Object = MibTableColumn
ipNatPrIntAddr = _IpNatPrIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 9),
    _IpNatPrIntAddr_Type()
)
ipNatPrIntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrIntAddr.setStatus("mandatory")


class _IpNatPrIntPort_Type(Integer32):
    """Custom type ipNatPrIntPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpNatPrIntPort_Type.__name__ = "Integer32"
_IpNatPrIntPort_Object = MibTableColumn
ipNatPrIntPort = _IpNatPrIntPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 6, 1, 10),
    _IpNatPrIntPort_Type()
)
ipNatPrIntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatPrIntPort.setStatus("mandatory")
_IpSessionTable_Object = MibTable
ipSessionTable = _IpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7)
)
if mibBuilder.loadTexts:
    ipSessionTable.setStatus("mandatory")
_IpSessionEntry_Object = MibTableRow
ipSessionEntry = _IpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1)
)
ipSessionEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipSessionProtocol"),
    (0, "BIANCA-BRICK-IP-MIB", "ipSessionSrcAddr"),
    (0, "BIANCA-BRICK-IP-MIB", "ipSessionSrcPort"),
    (0, "BIANCA-BRICK-IP-MIB", "ipSessionDstAddr"),
    (0, "BIANCA-BRICK-IP-MIB", "ipSessionDstPort"),
)
if mibBuilder.loadTexts:
    ipSessionEntry.setStatus("mandatory")
_IpSessionSrcAddr_Type = IpAddress
_IpSessionSrcAddr_Object = MibTableColumn
ipSessionSrcAddr = _IpSessionSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 1),
    _IpSessionSrcAddr_Type()
)
ipSessionSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionSrcAddr.setStatus("mandatory")


class _IpSessionSrcPort_Type(Integer32):
    """Custom type ipSessionSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpSessionSrcPort_Type.__name__ = "Integer32"
_IpSessionSrcPort_Object = MibTableColumn
ipSessionSrcPort = _IpSessionSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 2),
    _IpSessionSrcPort_Type()
)
ipSessionSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionSrcPort.setStatus("mandatory")
_IpSessionDstAddr_Type = IpAddress
_IpSessionDstAddr_Object = MibTableColumn
ipSessionDstAddr = _IpSessionDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 3),
    _IpSessionDstAddr_Type()
)
ipSessionDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionDstAddr.setStatus("mandatory")


class _IpSessionDstPort_Type(Integer32):
    """Custom type ipSessionDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpSessionDstPort_Type.__name__ = "Integer32"
_IpSessionDstPort_Object = MibTableColumn
ipSessionDstPort = _IpSessionDstPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 4),
    _IpSessionDstPort_Type()
)
ipSessionDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionDstPort.setStatus("mandatory")
_IpSessionOutPkts_Type = Counter32
_IpSessionOutPkts_Object = MibTableColumn
ipSessionOutPkts = _IpSessionOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 5),
    _IpSessionOutPkts_Type()
)
ipSessionOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionOutPkts.setStatus("mandatory")
_IpSessionOutOctets_Type = Counter32
_IpSessionOutOctets_Object = MibTableColumn
ipSessionOutOctets = _IpSessionOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 6),
    _IpSessionOutOctets_Type()
)
ipSessionOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionOutOctets.setStatus("mandatory")
_IpSessionInPkts_Type = Counter32
_IpSessionInPkts_Object = MibTableColumn
ipSessionInPkts = _IpSessionInPkts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 7),
    _IpSessionInPkts_Type()
)
ipSessionInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionInPkts.setStatus("mandatory")
_IpSessionInOctets_Type = Counter32
_IpSessionInOctets_Object = MibTableColumn
ipSessionInOctets = _IpSessionInOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 8),
    _IpSessionInOctets_Type()
)
ipSessionInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionInOctets.setStatus("mandatory")


class _IpSessionProtocol_Type(Integer32):
    """Custom type ipSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6,
              8,
              12,
              17,
              20,
              22,
              27,
              46,
              47,
              50,
              51,
              88,
              89,
              115)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("egp", 8),
          ("esp", 50),
          ("ggp", 3),
          ("gre", 47),
          ("hmp", 20),
          ("icmp", 1),
          ("igrp", 88),
          ("l2tp", 115),
          ("ospf", 89),
          ("pup", 12),
          ("rdp", 27),
          ("rsvp", 46),
          ("tcp", 6),
          ("udp", 17),
          ("xns-idp", 22))
    )


_IpSessionProtocol_Type.__name__ = "Integer32"
_IpSessionProtocol_Object = MibTableColumn
ipSessionProtocol = _IpSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 9),
    _IpSessionProtocol_Type()
)
ipSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionProtocol.setStatus("mandatory")
_IpSessionAge_Type = TimeTicks
_IpSessionAge_Object = MibTableColumn
ipSessionAge = _IpSessionAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 10),
    _IpSessionAge_Type()
)
ipSessionAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionAge.setStatus("mandatory")
_IpSessionIdle_Type = TimeTicks
_IpSessionIdle_Object = MibTableColumn
ipSessionIdle = _IpSessionIdle_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 11),
    _IpSessionIdle_Type()
)
ipSessionIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionIdle.setStatus("mandatory")
_IpSessionSrcIfIndex_Type = Integer32
_IpSessionSrcIfIndex_Object = MibTableColumn
ipSessionSrcIfIndex = _IpSessionSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 12),
    _IpSessionSrcIfIndex_Type()
)
ipSessionSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionSrcIfIndex.setStatus("mandatory")
_IpSessionDstIfIndex_Type = Integer32
_IpSessionDstIfIndex_Object = MibTableColumn
ipSessionDstIfIndex = _IpSessionDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 7, 1, 13),
    _IpSessionDstIfIndex_Type()
)
ipSessionDstIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSessionDstIfIndex.setStatus("mandatory")
_IpImportTable_Object = MibTable
ipImportTable = _IpImportTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12)
)
if mibBuilder.loadTexts:
    ipImportTable.setStatus("mandatory")
_IpImportEntry_Object = MibTableRow
ipImportEntry = _IpImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12, 1)
)
ipImportEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipImportSrcProto"),
    (0, "BIANCA-BRICK-IP-MIB", "ipImportDstProto"),
)
if mibBuilder.loadTexts:
    ipImportEntry.setStatus("mandatory")


class _IpImportSrcProto_Type(Integer32):
    """Custom type ipImportSrcProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default-route", 1),
          ("direct", 2),
          ("ospf", 5),
          ("radius", 7),
          ("rip", 4),
          ("special", 6),
          ("static", 3))
    )


_IpImportSrcProto_Type.__name__ = "Integer32"
_IpImportSrcProto_Object = MibTableColumn
ipImportSrcProto = _IpImportSrcProto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12, 1, 1),
    _IpImportSrcProto_Type()
)
ipImportSrcProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipImportSrcProto.setStatus("mandatory")


class _IpImportDstProto_Type(Integer32):
    """Custom type ipImportDstProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("ospf", 3),
          ("rip", 2))
    )


_IpImportDstProto_Type.__name__ = "Integer32"
_IpImportDstProto_Object = MibTableColumn
ipImportDstProto = _IpImportDstProto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12, 1, 2),
    _IpImportDstProto_Type()
)
ipImportDstProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipImportDstProto.setStatus("mandatory")
_IpImportMetric1_Type = Integer32
_IpImportMetric1_Object = MibTableColumn
ipImportMetric1 = _IpImportMetric1_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12, 1, 3),
    _IpImportMetric1_Type()
)
ipImportMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipImportMetric1.setStatus("mandatory")
_IpImportType_Type = Integer32
_IpImportType_Object = MibTableColumn
ipImportType = _IpImportType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12, 1, 4),
    _IpImportType_Type()
)
ipImportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipImportType.setStatus("mandatory")
_IpImportAddr_Type = IpAddress
_IpImportAddr_Object = MibTableColumn
ipImportAddr = _IpImportAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12, 1, 5),
    _IpImportAddr_Type()
)
ipImportAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipImportAddr.setStatus("mandatory")
_IpImportMask_Type = IpAddress
_IpImportMask_Object = MibTableColumn
ipImportMask = _IpImportMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12, 1, 6),
    _IpImportMask_Type()
)
ipImportMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipImportMask.setStatus("mandatory")


class _IpImportEffect_Type(Integer32):
    """Custom type ipImportEffect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotImport", 2),
          ("import", 1))
    )


_IpImportEffect_Type.__name__ = "Integer32"
_IpImportEffect_Object = MibScalar
ipImportEffect = _IpImportEffect_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12, 1, 7),
    _IpImportEffect_Type()
)
ipImportEffect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipImportEffect.setStatus("mandatory")
_IpImportIfIndex_Type = Integer32
_IpImportIfIndex_Object = MibTableColumn
ipImportIfIndex = _IpImportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 12, 1, 8),
    _IpImportIfIndex_Type()
)
ipImportIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipImportIfIndex.setStatus("mandatory")
_IpPriorityTable_Object = MibTable
ipPriorityTable = _IpPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 13)
)
if mibBuilder.loadTexts:
    ipPriorityTable.setStatus("mandatory")
_IpPriorityEntry_Object = MibTableRow
ipPriorityEntry = _IpPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 13, 1)
)
ipPriorityEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipPriorityProto"),
)
if mibBuilder.loadTexts:
    ipPriorityEntry.setStatus("mandatory")


class _IpPriorityProto_Type(Integer32):
    """Custom type ipPriorityProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("ospf", 4),
          ("ospf-ext", 5),
          ("rip", 3),
          ("static", 2))
    )


_IpPriorityProto_Type.__name__ = "Integer32"
_IpPriorityProto_Object = MibTableColumn
ipPriorityProto = _IpPriorityProto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 13, 1, 1),
    _IpPriorityProto_Type()
)
ipPriorityProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPriorityProto.setStatus("mandatory")


class _IpPriorityValue_Type(Integer32):
    """Custom type ipPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IpPriorityValue_Type.__name__ = "Integer32"
_IpPriorityValue_Object = MibTableColumn
ipPriorityValue = _IpPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 13, 1, 2),
    _IpPriorityValue_Type()
)
ipPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPriorityValue.setStatus("mandatory")
_IpFilterTable_Object = MibTable
ipFilterTable = _IpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15)
)
if mibBuilder.loadTexts:
    ipFilterTable.setStatus("mandatory")
_IpFilterEntry_Object = MibTableRow
ipFilterEntry = _IpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1)
)
ipFilterEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipFilterProtocol"),
)
if mibBuilder.loadTexts:
    ipFilterEntry.setStatus("mandatory")
_IpFilterIndex_Type = Integer32
_IpFilterIndex_Object = MibTableColumn
ipFilterIndex = _IpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 1),
    _IpFilterIndex_Type()
)
ipFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilterIndex.setStatus("mandatory")


class _IpFilterDescr_Type(DisplayString):
    """Custom type ipFilterDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpFilterDescr_Type.__name__ = "DisplayString"
_IpFilterDescr_Object = MibTableColumn
ipFilterDescr = _IpFilterDescr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 2),
    _IpFilterDescr_Type()
)
ipFilterDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterDescr.setStatus("mandatory")


class _IpFilterProtocol_Type(Integer32):
    """Custom type ipFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              6,
              8,
              9,
              12,
              16,
              17,
              20,
              22,
              27,
              46,
              47,
              50,
              51,
              56,
              57,
              65,
              80,
              88,
              89,
              94,
              111,
              112,
              115,
              255,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("chaos", 16),
          ("delete", 255),
          ("dont-verify", 256),
          ("egp", 8),
          ("esp", 50),
          ("ggp", 3),
          ("gre", 47),
          ("hmp", 20),
          ("icmp", 1),
          ("igp", 9),
          ("igrp", 88),
          ("ip", 4),
          ("ipip", 94),
          ("ipx-in-ip", 111),
          ("iso-ip", 80),
          ("kryptolan", 65),
          ("l2tp", 115),
          ("ospf", 89),
          ("pup", 12),
          ("rdp", 27),
          ("rsvp", 46),
          ("skip", 57),
          ("tcp", 6),
          ("tlsp", 56),
          ("udp", 17),
          ("vrrp", 112),
          ("xns-idp", 22))
    )


_IpFilterProtocol_Type.__name__ = "Integer32"
_IpFilterProtocol_Object = MibTableColumn
ipFilterProtocol = _IpFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 3),
    _IpFilterProtocol_Type()
)
ipFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterProtocol.setStatus("mandatory")
_IpFilterSrcAddr_Type = IpAddress
_IpFilterSrcAddr_Object = MibTableColumn
ipFilterSrcAddr = _IpFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 4),
    _IpFilterSrcAddr_Type()
)
ipFilterSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterSrcAddr.setStatus("mandatory")
_IpFilterSrcMask_Type = IpAddress
_IpFilterSrcMask_Object = MibTableColumn
ipFilterSrcMask = _IpFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 5),
    _IpFilterSrcMask_Type()
)
ipFilterSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterSrcMask.setStatus("mandatory")


class _IpFilterSrcPort_Type(Integer32):
    """Custom type ipFilterSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpFilterSrcPort_Type.__name__ = "Integer32"
_IpFilterSrcPort_Object = MibTableColumn
ipFilterSrcPort = _IpFilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 6),
    _IpFilterSrcPort_Type()
)
ipFilterSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterSrcPort.setStatus("mandatory")


class _IpFilterSrcPortRange_Type(Integer32):
    """Custom type ipFilterSrcPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpFilterSrcPortRange_Type.__name__ = "Integer32"
_IpFilterSrcPortRange_Object = MibTableColumn
ipFilterSrcPortRange = _IpFilterSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 7),
    _IpFilterSrcPortRange_Type()
)
ipFilterSrcPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterSrcPortRange.setStatus("mandatory")
_IpFilterDstAddr_Type = IpAddress
_IpFilterDstAddr_Object = MibTableColumn
ipFilterDstAddr = _IpFilterDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 8),
    _IpFilterDstAddr_Type()
)
ipFilterDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterDstAddr.setStatus("mandatory")
_IpFilterDstMask_Type = IpAddress
_IpFilterDstMask_Object = MibTableColumn
ipFilterDstMask = _IpFilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 9),
    _IpFilterDstMask_Type()
)
ipFilterDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterDstMask.setStatus("mandatory")


class _IpFilterDstPort_Type(Integer32):
    """Custom type ipFilterDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpFilterDstPort_Type.__name__ = "Integer32"
_IpFilterDstPort_Object = MibTableColumn
ipFilterDstPort = _IpFilterDstPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 10),
    _IpFilterDstPort_Type()
)
ipFilterDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterDstPort.setStatus("mandatory")


class _IpFilterDstPortRange_Type(Integer32):
    """Custom type ipFilterDstPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpFilterDstPortRange_Type.__name__ = "Integer32"
_IpFilterDstPortRange_Object = MibTableColumn
ipFilterDstPortRange = _IpFilterDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 11),
    _IpFilterDstPortRange_Type()
)
ipFilterDstPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterDstPortRange.setStatus("mandatory")


class _IpFilterTcpConnState_Type(Integer32):
    """Custom type ipFilterTcpConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("established", 2))
    )


_IpFilterTcpConnState_Type.__name__ = "Integer32"
_IpFilterTcpConnState_Object = MibTableColumn
ipFilterTcpConnState = _IpFilterTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 12),
    _IpFilterTcpConnState_Type()
)
ipFilterTcpConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterTcpConnState.setStatus("mandatory")


class _IpFilterIcmpType_Type(Integer32):
    """Custom type ipFilterIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              9,
              12,
              13,
              14,
              15,
              16,
              17,
              31)
        )
    )
    namedValues = NamedValues(
        *(("addrMask", 16),
          ("addrMaskRep", 17),
          ("destUnreach", 4),
          ("dont-verify", 31),
          ("echo", 9),
          ("echoRep", 1),
          ("parmProb", 13),
          ("redirect", 6),
          ("srcQuench", 5),
          ("timeExcds", 12),
          ("timestamp", 14),
          ("timestampRep", 15))
    )


_IpFilterIcmpType_Type.__name__ = "Integer32"
_IpFilterIcmpType_Object = MibTableColumn
ipFilterIcmpType = _IpFilterIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 13),
    _IpFilterIcmpType_Type()
)
ipFilterIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterIcmpType.setStatus("mandatory")


class _IpFilterTos_Type(Integer32):
    """Custom type ipFilterTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpFilterTos_Type.__name__ = "Integer32"
_IpFilterTos_Object = MibTableColumn
ipFilterTos = _IpFilterTos_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 14),
    _IpFilterTos_Type()
)
ipFilterTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterTos.setStatus("mandatory")


class _IpFilterTosMask_Type(Integer32):
    """Custom type ipFilterTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpFilterTosMask_Type.__name__ = "Integer32"
_IpFilterTosMask_Object = MibTableColumn
ipFilterTosMask = _IpFilterTosMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 15, 1, 15),
    _IpFilterTosMask_Type()
)
ipFilterTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterTosMask.setStatus("mandatory")
_IpRuleTable_Object = MibTable
ipRuleTable = _IpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 16)
)
if mibBuilder.loadTexts:
    ipRuleTable.setStatus("mandatory")
_IpRuleEntry_Object = MibTableRow
ipRuleEntry = _IpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 16, 1)
)
ipRuleEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipRuleFilterIndex"),
)
if mibBuilder.loadTexts:
    ipRuleEntry.setStatus("mandatory")
_IpRuleIndex_Type = Integer32
_IpRuleIndex_Object = MibTableColumn
ipRuleIndex = _IpRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 16, 1, 1),
    _IpRuleIndex_Type()
)
ipRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRuleIndex.setStatus("mandatory")
_IpRuleFilterIndex_Type = Integer32
_IpRuleFilterIndex_Object = MibTableColumn
ipRuleFilterIndex = _IpRuleFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 16, 1, 2),
    _IpRuleFilterIndex_Type()
)
ipRuleFilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRuleFilterIndex.setStatus("mandatory")


class _IpRuleAction_Type(Integer32):
    """Custom type ipRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("allow-if-not", 2),
          ("delete", 6),
          ("deny", 3),
          ("deny-if-not", 4),
          ("ignore", 5))
    )


_IpRuleAction_Type.__name__ = "Integer32"
_IpRuleAction_Object = MibTableColumn
ipRuleAction = _IpRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 16, 1, 3),
    _IpRuleAction_Type()
)
ipRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRuleAction.setStatus("mandatory")
_IpRuleNextRuleIndex_Type = Integer32
_IpRuleNextRuleIndex_Object = MibTableColumn
ipRuleNextRuleIndex = _IpRuleNextRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 16, 1, 4),
    _IpRuleNextRuleIndex_Type()
)
ipRuleNextRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRuleNextRuleIndex.setStatus("mandatory")
_IpNatOutTable_Object = MibTable
ipNatOutTable = _IpNatOutTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18)
)
if mibBuilder.loadTexts:
    ipNatOutTable.setStatus("mandatory")
_IpNatOutEntry_Object = MibTableRow
ipNatOutEntry = _IpNatOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1)
)
ipNatOutEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipNatOutIfIndex"),
    (0, "BIANCA-BRICK-IP-MIB", "ipNatOutIntAddr"),
    (0, "BIANCA-BRICK-IP-MIB", "ipNatOutExtAddr"),
)
if mibBuilder.loadTexts:
    ipNatOutEntry.setStatus("mandatory")
_IpNatOutIfIndex_Type = Integer32
_IpNatOutIfIndex_Object = MibTableColumn
ipNatOutIfIndex = _IpNatOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 1),
    _IpNatOutIfIndex_Type()
)
ipNatOutIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutIfIndex.setStatus("mandatory")


class _IpNatOutProtocol_Type(Integer32):
    """Custom type ipNatOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17,
              47,
              50,
              51,
              115,
              255,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("any", 255),
          ("delete", 256),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("l2tp", 115),
          ("tcp", 6),
          ("udp", 17))
    )


_IpNatOutProtocol_Type.__name__ = "Integer32"
_IpNatOutProtocol_Object = MibTableColumn
ipNatOutProtocol = _IpNatOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 2),
    _IpNatOutProtocol_Type()
)
ipNatOutProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutProtocol.setStatus("mandatory")
_IpNatOutRemoteAddr_Type = IpAddress
_IpNatOutRemoteAddr_Object = MibTableColumn
ipNatOutRemoteAddr = _IpNatOutRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 3),
    _IpNatOutRemoteAddr_Type()
)
ipNatOutRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutRemoteAddr.setStatus("mandatory")
_IpNatOutRemoteMask_Type = IpAddress
_IpNatOutRemoteMask_Object = MibTableColumn
ipNatOutRemoteMask = _IpNatOutRemoteMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 4),
    _IpNatOutRemoteMask_Type()
)
ipNatOutRemoteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutRemoteMask.setStatus("mandatory")
_IpNatOutExtAddr_Type = IpAddress
_IpNatOutExtAddr_Object = MibTableColumn
ipNatOutExtAddr = _IpNatOutExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 5),
    _IpNatOutExtAddr_Type()
)
ipNatOutExtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutExtAddr.setStatus("mandatory")


class _IpNatOutRemotePort_Type(Integer32):
    """Custom type ipNatOutRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpNatOutRemotePort_Type.__name__ = "Integer32"
_IpNatOutRemotePort_Object = MibTableColumn
ipNatOutRemotePort = _IpNatOutRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 6),
    _IpNatOutRemotePort_Type()
)
ipNatOutRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutRemotePort.setStatus("mandatory")


class _IpNatOutRemotePortRange_Type(Integer32):
    """Custom type ipNatOutRemotePortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpNatOutRemotePortRange_Type.__name__ = "Integer32"
_IpNatOutRemotePortRange_Object = MibTableColumn
ipNatOutRemotePortRange = _IpNatOutRemotePortRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 7),
    _IpNatOutRemotePortRange_Type()
)
ipNatOutRemotePortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutRemotePortRange.setStatus("mandatory")
_IpNatOutIntAddr_Type = IpAddress
_IpNatOutIntAddr_Object = MibTableColumn
ipNatOutIntAddr = _IpNatOutIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 8),
    _IpNatOutIntAddr_Type()
)
ipNatOutIntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutIntAddr.setStatus("mandatory")
_IpNatOutIntMask_Type = IpAddress
_IpNatOutIntMask_Object = MibTableColumn
ipNatOutIntMask = _IpNatOutIntMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 9),
    _IpNatOutIntMask_Type()
)
ipNatOutIntMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutIntMask.setStatus("mandatory")


class _IpNatOutIntPort_Type(Integer32):
    """Custom type ipNatOutIntPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpNatOutIntPort_Type.__name__ = "Integer32"
_IpNatOutIntPort_Object = MibTableColumn
ipNatOutIntPort = _IpNatOutIntPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 10),
    _IpNatOutIntPort_Type()
)
ipNatOutIntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutIntPort.setStatus("mandatory")


class _IpNatOutExtPort_Type(Integer32):
    """Custom type ipNatOutExtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpNatOutExtPort_Type.__name__ = "Integer32"
_IpNatOutExtPort_Object = MibTableColumn
ipNatOutExtPort = _IpNatOutExtPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 18, 1, 11),
    _IpNatOutExtPort_Type()
)
ipNatOutExtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatOutExtPort.setStatus("mandatory")
_IpHostsAliveTable_Object = MibTable
ipHostsAliveTable = _IpHostsAliveTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 19)
)
if mibBuilder.loadTexts:
    ipHostsAliveTable.setStatus("mandatory")
_IpHostsAliveEntry_Object = MibTableRow
ipHostsAliveEntry = _IpHostsAliveEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 19, 1)
)
ipHostsAliveEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipHostsAliveIPAddress"),
)
if mibBuilder.loadTexts:
    ipHostsAliveEntry.setStatus("mandatory")


class _IpHostsAliveGroup_Type(Integer32):
    """Custom type ipHostsAliveGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_IpHostsAliveGroup_Type.__name__ = "Integer32"
_IpHostsAliveGroup_Object = MibTableColumn
ipHostsAliveGroup = _IpHostsAliveGroup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 19, 1, 1),
    _IpHostsAliveGroup_Type()
)
ipHostsAliveGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostsAliveGroup.setStatus("mandatory")
_IpHostsAliveIPAddress_Type = IpAddress
_IpHostsAliveIPAddress_Object = MibTableColumn
ipHostsAliveIPAddress = _IpHostsAliveIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 19, 1, 2),
    _IpHostsAliveIPAddress_Type()
)
ipHostsAliveIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostsAliveIPAddress.setStatus("mandatory")


class _IpHostsAliveState_Type(Integer32):
    """Custom type ipHostsAliveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("down", 2))
    )


_IpHostsAliveState_Type.__name__ = "Integer32"
_IpHostsAliveState_Object = MibTableColumn
ipHostsAliveState = _IpHostsAliveState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 19, 1, 3),
    _IpHostsAliveState_Type()
)
ipHostsAliveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipHostsAliveState.setStatus("mandatory")


class _IpHostsAliveInterval_Type(Integer32):
    """Custom type ipHostsAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_IpHostsAliveInterval_Type.__name__ = "Integer32"
_IpHostsAliveInterval_Object = MibTableColumn
ipHostsAliveInterval = _IpHostsAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 19, 1, 4),
    _IpHostsAliveInterval_Type()
)
ipHostsAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostsAliveInterval.setStatus("mandatory")


class _IpHostsAliveDownAction_Type(Integer32):
    """Custom type ipHostsAliveDownAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("down", 2),
          ("up", 1))
    )


_IpHostsAliveDownAction_Type.__name__ = "Integer32"
_IpHostsAliveDownAction_Object = MibTableColumn
ipHostsAliveDownAction = _IpHostsAliveDownAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 19, 1, 5),
    _IpHostsAliveDownAction_Type()
)
ipHostsAliveDownAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostsAliveDownAction.setStatus("mandatory")
_IpHostsAliveFirstIfIndex_Type = Integer32
_IpHostsAliveFirstIfIndex_Object = MibTableColumn
ipHostsAliveFirstIfIndex = _IpHostsAliveFirstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 19, 1, 6),
    _IpHostsAliveFirstIfIndex_Type()
)
ipHostsAliveFirstIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostsAliveFirstIfIndex.setStatus("mandatory")


class _IpHostsAliveRange_Type(Integer32):
    """Custom type ipHostsAliveRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpHostsAliveRange_Type.__name__ = "Integer32"
_IpHostsAliveRange_Object = MibTableColumn
ipHostsAliveRange = _IpHostsAliveRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 19, 1, 7),
    _IpHostsAliveRange_Type()
)
ipHostsAliveRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHostsAliveRange.setStatus("mandatory")
_IpBodRuleTable_Object = MibTable
ipBodRuleTable = _IpBodRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 21)
)
if mibBuilder.loadTexts:
    ipBodRuleTable.setStatus("mandatory")
_IpBodRuleEntry_Object = MibTableRow
ipBodRuleEntry = _IpBodRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 21, 1)
)
ipBodRuleEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipBodRuleFilterIndex"),
)
if mibBuilder.loadTexts:
    ipBodRuleEntry.setStatus("mandatory")
_IpBodRuleIndex_Type = Integer32
_IpBodRuleIndex_Object = MibTableColumn
ipBodRuleIndex = _IpBodRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 21, 1, 1),
    _IpBodRuleIndex_Type()
)
ipBodRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBodRuleIndex.setStatus("mandatory")
_IpBodRuleFilterIndex_Type = Integer32
_IpBodRuleFilterIndex_Object = MibTableColumn
ipBodRuleFilterIndex = _IpBodRuleFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 21, 1, 2),
    _IpBodRuleFilterIndex_Type()
)
ipBodRuleFilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBodRuleFilterIndex.setStatus("mandatory")


class _IpBodRuleAction_Type(Integer32):
    """Custom type ipBodRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("delete", 6),
          ("deny", 3),
          ("deny-if-not", 4),
          ("ignore", 5),
          ("invoke", 1),
          ("invoke-if-not", 2))
    )


_IpBodRuleAction_Type.__name__ = "Integer32"
_IpBodRuleAction_Object = MibTableColumn
ipBodRuleAction = _IpBodRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 21, 1, 3),
    _IpBodRuleAction_Type()
)
ipBodRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBodRuleAction.setStatus("mandatory")


class _IpBodRuleDirection_Type(Integer32):
    """Custom type ipBodRuleDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 2),
          ("outgoing", 1))
    )


_IpBodRuleDirection_Type.__name__ = "Integer32"
_IpBodRuleDirection_Object = MibTableColumn
ipBodRuleDirection = _IpBodRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 21, 1, 4),
    _IpBodRuleDirection_Type()
)
ipBodRuleDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBodRuleDirection.setStatus("mandatory")


class _IpBodRuleChannels_Type(Integer32):
    """Custom type ipBodRuleChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_IpBodRuleChannels_Type.__name__ = "Integer32"
_IpBodRuleChannels_Object = MibScalar
ipBodRuleChannels = _IpBodRuleChannels_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 21, 1, 5),
    _IpBodRuleChannels_Type()
)
ipBodRuleChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBodRuleChannels.setStatus("mandatory")
_IpBodRuleNextRuleIndex_Type = Integer32
_IpBodRuleNextRuleIndex_Object = MibTableColumn
ipBodRuleNextRuleIndex = _IpBodRuleNextRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 21, 1, 6),
    _IpBodRuleNextRuleIndex_Type()
)
ipBodRuleNextRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBodRuleNextRuleIndex.setStatus("mandatory")


class _IpBodRuleIdleTime_Type(Integer32):
    """Custom type ipBodRuleIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_IpBodRuleIdleTime_Type.__name__ = "Integer32"
_IpBodRuleIdleTime_Object = MibTableColumn
ipBodRuleIdleTime = _IpBodRuleIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 21, 1, 7),
    _IpBodRuleIdleTime_Type()
)
ipBodRuleIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBodRuleIdleTime.setStatus("mandatory")
_IpQoSTable_Object = MibTable
ipQoSTable = _IpQoSTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22)
)
if mibBuilder.loadTexts:
    ipQoSTable.setStatus("mandatory")
_IpQoSEntry_Object = MibTableRow
ipQoSEntry = _IpQoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1)
)
ipQoSEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-MIB", "ipQoSFilterIndex"),
)
if mibBuilder.loadTexts:
    ipQoSEntry.setStatus("mandatory")
_IpQoSIndex_Type = Integer32
_IpQoSIndex_Object = MibTableColumn
ipQoSIndex = _IpQoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 1),
    _IpQoSIndex_Type()
)
ipQoSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipQoSIndex.setStatus("mandatory")
_IpQoSFilterIndex_Type = Integer32
_IpQoSFilterIndex_Object = MibTableColumn
ipQoSFilterIndex = _IpQoSFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 2),
    _IpQoSFilterIndex_Type()
)
ipQoSFilterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipQoSFilterIndex.setStatus("mandatory")
_IpQoSNextRuleIndex_Type = Integer32
_IpQoSNextRuleIndex_Object = MibTableColumn
ipQoSNextRuleIndex = _IpQoSNextRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 3),
    _IpQoSNextRuleIndex_Type()
)
ipQoSNextRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipQoSNextRuleIndex.setStatus("mandatory")


class _IpQoSAction_Type(Integer32):
    """Custom type ipQoSAction based on Integer32"""
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
        *(("classify", 1),
          ("classify-if-not", 2),
          ("delete", 4),
          ("disabled", 3))
    )


_IpQoSAction_Type.__name__ = "Integer32"
_IpQoSAction_Object = MibTableColumn
ipQoSAction = _IpQoSAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 4),
    _IpQoSAction_Type()
)
ipQoSAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipQoSAction.setStatus("mandatory")


class _IpQoSTos_Type(Integer32):
    """Custom type ipQoSTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpQoSTos_Type.__name__ = "Integer32"
_IpQoSTos_Object = MibTableColumn
ipQoSTos = _IpQoSTos_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 5),
    _IpQoSTos_Type()
)
ipQoSTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipQoSTos.setStatus("mandatory")


class _IpQoSTosSetRate_Type(Integer32):
    """Custom type ipQoSTosSetRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpQoSTosSetRate_Type.__name__ = "Integer32"
_IpQoSTosSetRate_Object = MibScalar
ipQoSTosSetRate = _IpQoSTosSetRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 7),
    _IpQoSTosSetRate_Type()
)
ipQoSTosSetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipQoSTosSetRate.setStatus("mandatory")


class _IpQoSTosSetBurst_Type(Integer32):
    """Custom type ipQoSTosSetBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpQoSTosSetBurst_Type.__name__ = "Integer32"
_IpQoSTosSetBurst_Object = MibScalar
ipQoSTosSetBurst = _IpQoSTosSetBurst_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 8),
    _IpQoSTosSetBurst_Type()
)
ipQoSTosSetBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipQoSTosSetBurst.setStatus("mandatory")


class _IpQoSServiceClass_Type(Integer32):
    """Custom type ipQoSServiceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high-priority", 2),
          ("normal", 1))
    )


_IpQoSServiceClass_Type.__name__ = "Integer32"
_IpQoSServiceClass_Object = MibTableColumn
ipQoSServiceClass = _IpQoSServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 11),
    _IpQoSServiceClass_Type()
)
ipQoSServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipQoSServiceClass.setStatus("mandatory")


class _IpQoSClassId_Type(Integer32):
    """Custom type ipQoSClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpQoSClassId_Type.__name__ = "Integer32"
_IpQoSClassId_Object = MibTableColumn
ipQoSClassId = _IpQoSClassId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 12),
    _IpQoSClassId_Type()
)
ipQoSClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipQoSClassId.setStatus("mandatory")


class _IpQoSDirection_Type(Integer32):
    """Custom type ipQoSDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 2),
          ("outgoing", 1))
    )


_IpQoSDirection_Type.__name__ = "Integer32"
_IpQoSDirection_Object = MibTableColumn
ipQoSDirection = _IpQoSDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 22, 1, 13),
    _IpQoSDirection_Type()
)
ipQoSDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipQoSDirection.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-IP-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "ipExtIfTable": ipExtIfTable,
       "ipExtIfEntry": ipExtIfEntry,
       "ipExtIfIndex": ipExtIfIndex,
       "ipExtIfRipSend": ipExtIfRipSend,
       "ipExtIfRipReceive": ipExtIfRipReceive,
       "ipExtIfProxyArp": ipExtIfProxyArp,
       "ipExtIfNat": ipExtIfNat,
       "ipExtIfNatRmvFin": ipExtIfNatRmvFin,
       "ipExtIfNatTcpTimeout": ipExtIfNatTcpTimeout,
       "ipExtIfNatOtherTimeout": ipExtIfNatOtherTimeout,
       "ipExtIfNatOutXlat": ipExtIfNatOutXlat,
       "ipExtIfAccounting": ipExtIfAccounting,
       "ipExtIfTcpSpoofing": ipExtIfTcpSpoofing,
       "ipExtIfAccessAction": ipExtIfAccessAction,
       "ipExtIfAccessReport": ipExtIfAccessReport,
       "ipExtIfOspf": ipExtIfOspf,
       "ipExtIfOspfMetric": ipExtIfOspfMetric,
       "ipExtIfTcpCksum": ipExtIfTcpCksum,
       "ipExtIfBackRtVerify": ipExtIfBackRtVerify,
       "ipExtIfRuleIndex": ipExtIfRuleIndex,
       "ipExtIfAuthentication": ipExtIfAuthentication,
       "ipExtIfAuthMode": ipExtIfAuthMode,
       "ipExtIfAuthLifeTime": ipExtIfAuthLifeTime,
       "ipExtIfAuthKeepalive": ipExtIfAuthKeepalive,
       "ipExtIfRouteAnnounce": ipExtIfRouteAnnounce,
       "ipExtIfIpFragmentation": ipExtIfIpFragmentation,
       "ipExtIfRerouting": ipExtIfRerouting,
       "ipExtIfBodRuleIndex": ipExtIfBodRuleIndex,
       "ipExtIfQosRuleIndex": ipExtIfQosRuleIndex,
       "ipExtIfIpsecAccounting": ipExtIfIpsecAccounting,
       "ipExtIfMulticast": ipExtIfMulticast,
       "ipExtIfNatSilentDeny": ipExtIfNatSilentDeny,
       "ipExtRtTable": ipExtRtTable,
       "ipExtRtEntry": ipExtRtEntry,
       "ipExtRtProtocol": ipExtRtProtocol,
       "ipExtRtSrcIfIndex": ipExtRtSrcIfIndex,
       "ipExtRtSrcAddr": ipExtRtSrcAddr,
       "ipExtRtSrcMask": ipExtRtSrcMask,
       "ipExtRtSrcPort": ipExtRtSrcPort,
       "ipExtRtSrcPortRange": ipExtRtSrcPortRange,
       "ipExtRtDstAddr": ipExtRtDstAddr,
       "ipExtRtDstMask": ipExtRtDstMask,
       "ipExtRtDstPort": ipExtRtDstPort,
       "ipExtRtDstPortRange": ipExtRtDstPortRange,
       "ipExtRtTos": ipExtRtTos,
       "ipExtRtTosMask": ipExtRtTosMask,
       "ipExtRtDstIfMode": ipExtRtDstIfMode,
       "ipExtRtDstIfIndex": ipExtRtDstIfIndex,
       "ipExtRtNextHop": ipExtRtNextHop,
       "ipExtRtType": ipExtRtType,
       "ipExtRtMetric1": ipExtRtMetric1,
       "ipExtRtMetric2": ipExtRtMetric2,
       "ipExtRtMetric3": ipExtRtMetric3,
       "ipExtRtMetric4": ipExtRtMetric4,
       "ipExtRtMetric5": ipExtRtMetric5,
       "ipExtRtProto": ipExtRtProto,
       "ipExtRtAge": ipExtRtAge,
       "ipNatTable": ipNatTable,
       "ipNatEntry": ipNatEntry,
       "ipNatIfIndex": ipNatIfIndex,
       "ipNatProtocol": ipNatProtocol,
       "ipNatIntAddr": ipNatIntAddr,
       "ipNatIntPort": ipNatIntPort,
       "ipNatExtAddr": ipNatExtAddr,
       "ipNatExtPort": ipNatExtPort,
       "ipNatRemoteAddr": ipNatRemoteAddr,
       "ipNatRemotePort": ipNatRemotePort,
       "ipNatDirection": ipNatDirection,
       "ipNatAge": ipNatAge,
       "ipNatPresetTable": ipNatPresetTable,
       "ipNatPresetEntry": ipNatPresetEntry,
       "ipNatPrIfIndex": ipNatPrIfIndex,
       "ipNatPrProtocol": ipNatPrProtocol,
       "ipNatPrRemoteAddr": ipNatPrRemoteAddr,
       "ipNatPrRemoteMask": ipNatPrRemoteMask,
       "ipNatPrExtAddr": ipNatPrExtAddr,
       "ipNatPrExtMask": ipNatPrExtMask,
       "ipNatPrExtPort": ipNatPrExtPort,
       "ipNatPrExtPortRange": ipNatPrExtPortRange,
       "ipNatPrIntAddr": ipNatPrIntAddr,
       "ipNatPrIntPort": ipNatPrIntPort,
       "ipSessionTable": ipSessionTable,
       "ipSessionEntry": ipSessionEntry,
       "ipSessionSrcAddr": ipSessionSrcAddr,
       "ipSessionSrcPort": ipSessionSrcPort,
       "ipSessionDstAddr": ipSessionDstAddr,
       "ipSessionDstPort": ipSessionDstPort,
       "ipSessionOutPkts": ipSessionOutPkts,
       "ipSessionOutOctets": ipSessionOutOctets,
       "ipSessionInPkts": ipSessionInPkts,
       "ipSessionInOctets": ipSessionInOctets,
       "ipSessionProtocol": ipSessionProtocol,
       "ipSessionAge": ipSessionAge,
       "ipSessionIdle": ipSessionIdle,
       "ipSessionSrcIfIndex": ipSessionSrcIfIndex,
       "ipSessionDstIfIndex": ipSessionDstIfIndex,
       "ipImportTable": ipImportTable,
       "ipImportEntry": ipImportEntry,
       "ipImportSrcProto": ipImportSrcProto,
       "ipImportDstProto": ipImportDstProto,
       "ipImportMetric1": ipImportMetric1,
       "ipImportType": ipImportType,
       "ipImportAddr": ipImportAddr,
       "ipImportMask": ipImportMask,
       "ipImportEffect": ipImportEffect,
       "ipImportIfIndex": ipImportIfIndex,
       "ipPriorityTable": ipPriorityTable,
       "ipPriorityEntry": ipPriorityEntry,
       "ipPriorityProto": ipPriorityProto,
       "ipPriorityValue": ipPriorityValue,
       "ipFilterTable": ipFilterTable,
       "ipFilterEntry": ipFilterEntry,
       "ipFilterIndex": ipFilterIndex,
       "ipFilterDescr": ipFilterDescr,
       "ipFilterProtocol": ipFilterProtocol,
       "ipFilterSrcAddr": ipFilterSrcAddr,
       "ipFilterSrcMask": ipFilterSrcMask,
       "ipFilterSrcPort": ipFilterSrcPort,
       "ipFilterSrcPortRange": ipFilterSrcPortRange,
       "ipFilterDstAddr": ipFilterDstAddr,
       "ipFilterDstMask": ipFilterDstMask,
       "ipFilterDstPort": ipFilterDstPort,
       "ipFilterDstPortRange": ipFilterDstPortRange,
       "ipFilterTcpConnState": ipFilterTcpConnState,
       "ipFilterIcmpType": ipFilterIcmpType,
       "ipFilterTos": ipFilterTos,
       "ipFilterTosMask": ipFilterTosMask,
       "ipRuleTable": ipRuleTable,
       "ipRuleEntry": ipRuleEntry,
       "ipRuleIndex": ipRuleIndex,
       "ipRuleFilterIndex": ipRuleFilterIndex,
       "ipRuleAction": ipRuleAction,
       "ipRuleNextRuleIndex": ipRuleNextRuleIndex,
       "ipNatOutTable": ipNatOutTable,
       "ipNatOutEntry": ipNatOutEntry,
       "ipNatOutIfIndex": ipNatOutIfIndex,
       "ipNatOutProtocol": ipNatOutProtocol,
       "ipNatOutRemoteAddr": ipNatOutRemoteAddr,
       "ipNatOutRemoteMask": ipNatOutRemoteMask,
       "ipNatOutExtAddr": ipNatOutExtAddr,
       "ipNatOutRemotePort": ipNatOutRemotePort,
       "ipNatOutRemotePortRange": ipNatOutRemotePortRange,
       "ipNatOutIntAddr": ipNatOutIntAddr,
       "ipNatOutIntMask": ipNatOutIntMask,
       "ipNatOutIntPort": ipNatOutIntPort,
       "ipNatOutExtPort": ipNatOutExtPort,
       "ipHostsAliveTable": ipHostsAliveTable,
       "ipHostsAliveEntry": ipHostsAliveEntry,
       "ipHostsAliveGroup": ipHostsAliveGroup,
       "ipHostsAliveIPAddress": ipHostsAliveIPAddress,
       "ipHostsAliveState": ipHostsAliveState,
       "ipHostsAliveInterval": ipHostsAliveInterval,
       "ipHostsAliveDownAction": ipHostsAliveDownAction,
       "ipHostsAliveFirstIfIndex": ipHostsAliveFirstIfIndex,
       "ipHostsAliveRange": ipHostsAliveRange,
       "ipBodRuleTable": ipBodRuleTable,
       "ipBodRuleEntry": ipBodRuleEntry,
       "ipBodRuleIndex": ipBodRuleIndex,
       "ipBodRuleFilterIndex": ipBodRuleFilterIndex,
       "ipBodRuleAction": ipBodRuleAction,
       "ipBodRuleDirection": ipBodRuleDirection,
       "ipBodRuleChannels": ipBodRuleChannels,
       "ipBodRuleNextRuleIndex": ipBodRuleNextRuleIndex,
       "ipBodRuleIdleTime": ipBodRuleIdleTime,
       "ipQoSTable": ipQoSTable,
       "ipQoSEntry": ipQoSEntry,
       "ipQoSIndex": ipQoSIndex,
       "ipQoSFilterIndex": ipQoSFilterIndex,
       "ipQoSNextRuleIndex": ipQoSNextRuleIndex,
       "ipQoSAction": ipQoSAction,
       "ipQoSTos": ipQoSTos,
       "ipQoSTosSetRate": ipQoSTosSetRate,
       "ipQoSTosSetBurst": ipQoSTosSetBurst,
       "ipQoSServiceClass": ipQoSServiceClass,
       "ipQoSClassId": ipQoSClassId,
       "ipQoSDirection": ipQoSDirection}
)
