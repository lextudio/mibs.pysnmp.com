# SNMP MIB module (DC-RTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DC-RTM-MIB
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

(AdminDistance,
 AdminStatus,
 BfdSessionStatus,
 InetSubAddressType,
 NumericIndexOrZero,
 OperStatus,
 PathType,
 RouteAction) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "AdminDistance",
    "AdminStatus",
    "BfdSessionStatus",
    "InetSubAddressType",
    "NumericIndexOrZero",
    "OperStatus",
    "PathType",
    "RouteAction")

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rtmMib = ModuleIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1)
)
rtmMib.setRevisions(
        ("2014-04-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsIndexType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class FteIndex(Unsigned32, TextualConvention):
    status = "current"


class OspfTag(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class RtmMjStatus(Integer32, TextualConvention):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("mjFailed", 10),
          ("mjFailedToRegister", 8),
          ("mjFailingOver", 9),
          ("mjJoinActive", 4),
          ("mjJoinGone", 7),
          ("mjNotJoined", 1),
          ("mjSentAddJoin", 2),
          ("mjSentDelJoin", 5),
          ("mjSentRegister", 3),
          ("mjSentUnregister", 6))
    )



class RtmSjStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("sjFailed", 7),
          ("sjFailingOver", 6),
          ("sjJoinActive", 3),
          ("sjJoinGone", 5),
          ("sjJoinUnreg", 4),
          ("sjJoined", 2),
          ("sjNotJoined", 1))
    )



class InterfaceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifActiveRoutes", 1),
          ("ifRteProtInput", 2))
    )



class AriPrtnrType(Integer32, TextualConvention):
    status = "current"
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
        *(("ariPrtnrBgp", 4),
          ("ariPrtnrFt", 1),
          ("ariPrtnrLdf", 2),
          ("ariPrtnrPim", 5),
          ("ariPrtnrRsm", 3))
    )



class RdstSetFieldType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rdstSetBgpComm", 1),
          ("rdstSetBgpExtComm", 2))
    )



class EqualCostRouteOpts(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equalCostAll", 1),
          ("equalCostOne", 2))
    )



class MetricConversion(Integer32, TextualConvention):
    status = "current"
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
        *(("metricConvConstant", 2),
          ("metricConvInverse", 3),
          ("metricConvSame", 1),
          ("metricConvScaleDown", 5),
          ("metricConvScaleUp", 4),
          ("metricConvTruncate", 6))
    )



class InfoSourceDest(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              65536,
              131072,
              196608,
              262144,
              327680,
              393216,
              458752,
              524288,
              589824,
              655360,
              720896,
              786432,
              851968,
              917504,
              983040,
              1048576,
              1114112,
              1179648)
        )
    )
    namedValues = NamedValues(
        *(("infoSourceAll", 0),
          ("infoSourceAllInclConnected", 1),
          ("infoSourceBbnSpfIgp", 786432),
          ("infoSourceBgp", 917504),
          ("infoSourceConnected", 131072),
          ("infoSourceDvmrp", 1114112),
          ("infoSourceEgp", 327680),
          ("infoSourceEigrp", 1048576),
          ("infoSourceEnni", 1179648),
          ("infoSourceEsis", 655360),
          ("infoSourceHello", 458752),
          ("infoSourceIcmp", 262144),
          ("infoSourceIdpr", 983040),
          ("infoSourceIgrp", 720896),
          ("infoSourceIsis", 589824),
          ("infoSourceOspf", 851968),
          ("infoSourceOther", 65536),
          ("infoSourcePd", 393216),
          ("infoSourceRip", 524288),
          ("infoSourceStatic", 196608))
    )



class BgpOriginCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bgpOriginEgp", 1),
          ("bgpOriginIgp", 0),
          ("bgpOriginIncomplete", 2))
    )



class BgpCommunity(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class BgpExtendedCommunity(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class RouteInfo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("isisL1External", 8),
          ("isisL1ExternalDown", 10),
          ("isisL1Internal", 5),
          ("isisL1InternalDown", 7),
          ("isisL2External", 9),
          ("isisL2Internal", 6),
          ("none", 0),
          ("ospfExternalType1", 3),
          ("ospfExternalType2", 4),
          ("ospfInterArea", 2),
          ("ospfIntraArea", 1))
    )



class RouteType(Integer32, TextualConvention):
    status = "current"
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
        *(("local", 3),
          ("other", 1),
          ("reject", 2),
          ("remote", 4))
    )



class RtmBfdSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("desired", 2),
          ("none", 1),
          ("required", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RtmObjects_ObjectIdentity = ObjectIdentity
rtmObjects = _RtmObjects_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1)
)
_RtmEntityTable_Object = MibTable
rtmEntityTable = _RtmEntityTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rtmEntityTable.setStatus("current")
_RtmEntityEntry_Object = MibTableRow
rtmEntityEntry = _RtmEntityEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1)
)
rtmEntityEntry.setIndexNames(
    (0, "DC-RTM-MIB", "rtmEntityFteIndex"),
)
if mibBuilder.loadTexts:
    rtmEntityEntry.setStatus("current")
_RtmEntityFteIndex_Type = FteIndex
_RtmEntityFteIndex_Object = MibTableColumn
rtmEntityFteIndex = _RtmEntityFteIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 1),
    _RtmEntityFteIndex_Type()
)
rtmEntityFteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmEntityFteIndex.setStatus("current")
_RtmEntityRowStatus_Type = RowStatus
_RtmEntityRowStatus_Object = MibTableColumn
rtmEntityRowStatus = _RtmEntityRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 2),
    _RtmEntityRowStatus_Type()
)
rtmEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityRowStatus.setStatus("current")


class _RtmEntityAdminStat_Type(AdminStatus):
    """Custom type rtmEntityAdminStat based on AdminStatus"""


_RtmEntityAdminStat_Object = MibTableColumn
rtmEntityAdminStat = _RtmEntityAdminStat_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 3),
    _RtmEntityAdminStat_Type()
)
rtmEntityAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityAdminStat.setStatus("current")
_RtmEntityOperStatus_Type = OperStatus
_RtmEntityOperStatus_Object = MibTableColumn
rtmEntityOperStatus = _RtmEntityOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 4),
    _RtmEntityOperStatus_Type()
)
rtmEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmEntityOperStatus.setStatus("current")


class _RtmEntityDsConnctd_Type(AdminDistance):
    """Custom type rtmEntityDsConnctd based on AdminDistance"""
    defaultValue = 0


_RtmEntityDsConnctd_Object = MibTableColumn
rtmEntityDsConnctd = _RtmEntityDsConnctd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 5),
    _RtmEntityDsConnctd_Type()
)
rtmEntityDsConnctd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsConnctd.setStatus("current")


class _RtmEntityDsStatDf_Type(AdminDistance):
    """Custom type rtmEntityDsStatDf based on AdminDistance"""
    defaultValue = 1


_RtmEntityDsStatDf_Object = MibTableColumn
rtmEntityDsStatDf = _RtmEntityDsStatDf_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 6),
    _RtmEntityDsStatDf_Type()
)
rtmEntityDsStatDf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsStatDf.setStatus("current")


class _RtmEntityDsOspfInt_Type(AdminDistance):
    """Custom type rtmEntityDsOspfInt based on AdminDistance"""
    defaultValue = 30


_RtmEntityDsOspfInt_Object = MibTableColumn
rtmEntityDsOspfInt = _RtmEntityDsOspfInt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 7),
    _RtmEntityDsOspfInt_Type()
)
rtmEntityDsOspfInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsOspfInt.setStatus("current")


class _RtmEntityDsOspfExt_Type(AdminDistance):
    """Custom type rtmEntityDsOspfExt based on AdminDistance"""
    defaultValue = 110


_RtmEntityDsOspfExt_Object = MibTableColumn
rtmEntityDsOspfExt = _RtmEntityDsOspfExt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 8),
    _RtmEntityDsOspfExt_Type()
)
rtmEntityDsOspfExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsOspfExt.setStatus("current")


class _RtmEntityDsIntBgp_Type(AdminDistance):
    """Custom type rtmEntityDsIntBgp based on AdminDistance"""
    defaultValue = 200


_RtmEntityDsIntBgp_Object = MibTableColumn
rtmEntityDsIntBgp = _RtmEntityDsIntBgp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 9),
    _RtmEntityDsIntBgp_Type()
)
rtmEntityDsIntBgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsIntBgp.setStatus("current")


class _RtmEntityDsExtBgp_Type(AdminDistance):
    """Custom type rtmEntityDsExtBgp based on AdminDistance"""
    defaultValue = 20


_RtmEntityDsExtBgp_Object = MibTableColumn
rtmEntityDsExtBgp = _RtmEntityDsExtBgp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 10),
    _RtmEntityDsExtBgp_Type()
)
rtmEntityDsExtBgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsExtBgp.setStatus("current")


class _RtmEntityDsIsisInt1_Type(AdminDistance):
    """Custom type rtmEntityDsIsisInt1 based on AdminDistance"""
    defaultValue = 115


_RtmEntityDsIsisInt1_Object = MibTableColumn
rtmEntityDsIsisInt1 = _RtmEntityDsIsisInt1_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 11),
    _RtmEntityDsIsisInt1_Type()
)
rtmEntityDsIsisInt1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsIsisInt1.setStatus("current")


class _RtmEntityDsIsisInt2_Type(AdminDistance):
    """Custom type rtmEntityDsIsisInt2 based on AdminDistance"""
    defaultValue = 116


_RtmEntityDsIsisInt2_Object = MibTableColumn
rtmEntityDsIsisInt2 = _RtmEntityDsIsisInt2_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 12),
    _RtmEntityDsIsisInt2_Type()
)
rtmEntityDsIsisInt2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsIsisInt2.setStatus("current")


class _RtmEntityDsIsisExt1_Type(AdminDistance):
    """Custom type rtmEntityDsIsisExt1 based on AdminDistance"""
    defaultValue = 117


_RtmEntityDsIsisExt1_Object = MibTableColumn
rtmEntityDsIsisExt1 = _RtmEntityDsIsisExt1_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 13),
    _RtmEntityDsIsisExt1_Type()
)
rtmEntityDsIsisExt1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsIsisExt1.setStatus("current")


class _RtmEntityDsIsisExt2_Type(AdminDistance):
    """Custom type rtmEntityDsIsisExt2 based on AdminDistance"""
    defaultValue = 118


_RtmEntityDsIsisExt2_Object = MibTableColumn
rtmEntityDsIsisExt2 = _RtmEntityDsIsisExt2_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 14),
    _RtmEntityDsIsisExt2_Type()
)
rtmEntityDsIsisExt2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsIsisExt2.setStatus("current")


class _RtmEntityDsRip_Type(AdminDistance):
    """Custom type rtmEntityDsRip based on AdminDistance"""
    defaultValue = 120


_RtmEntityDsRip_Object = MibTableColumn
rtmEntityDsRip = _RtmEntityDsRip_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 15),
    _RtmEntityDsRip_Type()
)
rtmEntityDsRip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsRip.setStatus("current")


class _RtmEntityDsEgp_Type(AdminDistance):
    """Custom type rtmEntityDsEgp based on AdminDistance"""
    defaultValue = 205


_RtmEntityDsEgp_Object = MibTableColumn
rtmEntityDsEgp = _RtmEntityDsEgp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 16),
    _RtmEntityDsEgp_Type()
)
rtmEntityDsEgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsEgp.setStatus("current")


class _RtmEntityDsPd_Type(AdminDistance):
    """Custom type rtmEntityDsPd based on AdminDistance"""
    defaultValue = 2


_RtmEntityDsPd_Object = MibTableColumn
rtmEntityDsPd = _RtmEntityDsPd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 17),
    _RtmEntityDsPd_Type()
)
rtmEntityDsPd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsPd.setStatus("current")


class _RtmEntityDsHello_Type(AdminDistance):
    """Custom type rtmEntityDsHello based on AdminDistance"""
    defaultValue = 215


_RtmEntityDsHello_Object = MibTableColumn
rtmEntityDsHello = _RtmEntityDsHello_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 18),
    _RtmEntityDsHello_Type()
)
rtmEntityDsHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsHello.setStatus("current")


class _RtmEntityDsEsis_Type(AdminDistance):
    """Custom type rtmEntityDsEsis based on AdminDistance"""
    defaultValue = 225


_RtmEntityDsEsis_Object = MibTableColumn
rtmEntityDsEsis = _RtmEntityDsEsis_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 19),
    _RtmEntityDsEsis_Type()
)
rtmEntityDsEsis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsEsis.setStatus("current")


class _RtmEntityDsBbnspfigp_Type(AdminDistance):
    """Custom type rtmEntityDsBbnspfigp based on AdminDistance"""
    defaultValue = 225


_RtmEntityDsBbnspfigp_Object = MibTableColumn
rtmEntityDsBbnspfigp = _RtmEntityDsBbnspfigp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 20),
    _RtmEntityDsBbnspfigp_Type()
)
rtmEntityDsBbnspfigp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsBbnspfigp.setStatus("current")


class _RtmEntityDsIdpr_Type(AdminDistance):
    """Custom type rtmEntityDsIdpr based on AdminDistance"""
    defaultValue = 225


_RtmEntityDsIdpr_Object = MibTableColumn
rtmEntityDsIdpr = _RtmEntityDsIdpr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 21),
    _RtmEntityDsIdpr_Type()
)
rtmEntityDsIdpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsIdpr.setStatus("current")


class _RtmEntityDsIgrp_Type(AdminDistance):
    """Custom type rtmEntityDsIgrp based on AdminDistance"""
    defaultValue = 100


_RtmEntityDsIgrp_Object = MibTableColumn
rtmEntityDsIgrp = _RtmEntityDsIgrp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 22),
    _RtmEntityDsIgrp_Type()
)
rtmEntityDsIgrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsIgrp.setStatus("current")


class _RtmEntityDsEigrpSmm_Type(AdminDistance):
    """Custom type rtmEntityDsEigrpSmm based on AdminDistance"""
    defaultValue = 5


_RtmEntityDsEigrpSmm_Object = MibTableColumn
rtmEntityDsEigrpSmm = _RtmEntityDsEigrpSmm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 23),
    _RtmEntityDsEigrpSmm_Type()
)
rtmEntityDsEigrpSmm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsEigrpSmm.setStatus("current")


class _RtmEntityDsIntEigrp_Type(AdminDistance):
    """Custom type rtmEntityDsIntEigrp based on AdminDistance"""
    defaultValue = 90


_RtmEntityDsIntEigrp_Object = MibTableColumn
rtmEntityDsIntEigrp = _RtmEntityDsIntEigrp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 24),
    _RtmEntityDsIntEigrp_Type()
)
rtmEntityDsIntEigrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsIntEigrp.setStatus("current")


class _RtmEntityDsEigrpExt_Type(AdminDistance):
    """Custom type rtmEntityDsEigrpExt based on AdminDistance"""
    defaultValue = 170


_RtmEntityDsEigrpExt_Object = MibTableColumn
rtmEntityDsEigrpExt = _RtmEntityDsEigrpExt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 25),
    _RtmEntityDsEigrpExt_Type()
)
rtmEntityDsEigrpExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsEigrpExt.setStatus("current")


class _RtmEntityDsUnknown_Type(AdminDistance):
    """Custom type rtmEntityDsUnknown based on AdminDistance"""
    defaultValue = 255


_RtmEntityDsUnknown_Object = MibTableColumn
rtmEntityDsUnknown = _RtmEntityDsUnknown_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 26),
    _RtmEntityDsUnknown_Type()
)
rtmEntityDsUnknown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsUnknown.setStatus("current")


class _RtmEntityEqlCostOpt_Type(EqualCostRouteOpts):
    """Custom type rtmEntityEqlCostOpt based on EqualCostRouteOpts"""


_RtmEntityEqlCostOpt_Object = MibTableColumn
rtmEntityEqlCostOpt = _RtmEntityEqlCostOpt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 27),
    _RtmEntityEqlCostOpt_Type()
)
rtmEntityEqlCostOpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityEqlCostOpt.setStatus("current")


class _RtmEntityDelDeadRte_Type(TruthValue):
    """Custom type rtmEntityDelDeadRte based on TruthValue"""


_RtmEntityDelDeadRte_Object = MibTableColumn
rtmEntityDelDeadRte = _RtmEntityDelDeadRte_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 28),
    _RtmEntityDelDeadRte_Type()
)
rtmEntityDelDeadRte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDelDeadRte.setStatus("current")


class _RtmEntityDeadRpmTmr_Type(Integer32):
    """Custom type rtmEntityDeadRpmTmr based on Integer32"""
    defaultValue = 0


_RtmEntityDeadRpmTmr_Object = MibTableColumn
rtmEntityDeadRpmTmr = _RtmEntityDeadRpmTmr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 29),
    _RtmEntityDeadRpmTmr_Type()
)
rtmEntityDeadRpmTmr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDeadRpmTmr.setStatus("current")


class _RtmEntityRouteNumber_Type(Integer32):
    """Custom type rtmEntityRouteNumber based on Integer32"""
    defaultValue = 0


_RtmEntityRouteNumber_Object = MibTableColumn
rtmEntityRouteNumber = _RtmEntityRouteNumber_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 30),
    _RtmEntityRouteNumber_Type()
)
rtmEntityRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmEntityRouteNumber.setStatus("current")


class _RtmEntityAddressFamily_Type(InetAddressType):
    """Custom type rtmEntityAddressFamily based on InetAddressType"""


_RtmEntityAddressFamily_Object = MibTableColumn
rtmEntityAddressFamily = _RtmEntityAddressFamily_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 31),
    _RtmEntityAddressFamily_Type()
)
rtmEntityAddressFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityAddressFamily.setStatus("current")


class _RtmEntityDsDvmrp_Type(AdminDistance):
    """Custom type rtmEntityDsDvmrp based on AdminDistance"""
    defaultValue = 225


_RtmEntityDsDvmrp_Object = MibTableColumn
rtmEntityDsDvmrp = _RtmEntityDsDvmrp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 32),
    _RtmEntityDsDvmrp_Type()
)
rtmEntityDsDvmrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityDsDvmrp.setStatus("current")


class _RtmEntityI3Index_Type(FteIndex):
    """Custom type rtmEntityI3Index based on FteIndex"""
    defaultValue = 1


_RtmEntityI3Index_Object = MibTableColumn
rtmEntityI3Index = _RtmEntityI3Index_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 33),
    _RtmEntityI3Index_Type()
)
rtmEntityI3Index.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityI3Index.setStatus("current")
_RtmEntityI3JoinStatus_Type = RtmMjStatus
_RtmEntityI3JoinStatus_Object = MibTableColumn
rtmEntityI3JoinStatus = _RtmEntityI3JoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 34),
    _RtmEntityI3JoinStatus_Type()
)
rtmEntityI3JoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmEntityI3JoinStatus.setStatus("current")


class _RtmEntityPartnerWaitTime_Type(Integer32):
    """Custom type rtmEntityPartnerWaitTime based on Integer32"""
    defaultValue = 30000


_RtmEntityPartnerWaitTime_Object = MibTableColumn
rtmEntityPartnerWaitTime = _RtmEntityPartnerWaitTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 35),
    _RtmEntityPartnerWaitTime_Type()
)
rtmEntityPartnerWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityPartnerWaitTime.setStatus("current")


class _RtmEntityStartupTime_Type(Integer32):
    """Custom type rtmEntityStartupTime based on Integer32"""
    defaultValue = 5000


_RtmEntityStartupTime_Object = MibTableColumn
rtmEntityStartupTime = _RtmEntityStartupTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 36),
    _RtmEntityStartupTime_Type()
)
rtmEntityStartupTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityStartupTime.setStatus("current")


class _RtmEntityRestartTime_Type(Integer32):
    """Custom type rtmEntityRestartTime based on Integer32"""
    defaultValue = 180000


_RtmEntityRestartTime_Object = MibTableColumn
rtmEntityRestartTime = _RtmEntityRestartTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 37),
    _RtmEntityRestartTime_Type()
)
rtmEntityRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityRestartTime.setStatus("current")


class _RtmEntityFtStateRetained_Type(TruthValue):
    """Custom type rtmEntityFtStateRetained based on TruthValue"""


_RtmEntityFtStateRetained_Object = MibTableColumn
rtmEntityFtStateRetained = _RtmEntityFtStateRetained_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 38),
    _RtmEntityFtStateRetained_Type()
)
rtmEntityFtStateRetained.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityFtStateRetained.setStatus("current")


class _RtmEntityUseUnidirectionalLinks_Type(TruthValue):
    """Custom type rtmEntityUseUnidirectionalLinks based on TruthValue"""


_RtmEntityUseUnidirectionalLinks_Object = MibTableColumn
rtmEntityUseUnidirectionalLinks = _RtmEntityUseUnidirectionalLinks_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 39),
    _RtmEntityUseUnidirectionalLinks_Type()
)
rtmEntityUseUnidirectionalLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityUseUnidirectionalLinks.setStatus("current")


class _RtmEntityBfdIndex_Type(NumericIndexOrZero):
    """Custom type rtmEntityBfdIndex based on NumericIndexOrZero"""
    defaultValue = 0


_RtmEntityBfdIndex_Object = MibTableColumn
rtmEntityBfdIndex = _RtmEntityBfdIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 40),
    _RtmEntityBfdIndex_Type()
)
rtmEntityBfdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityBfdIndex.setStatus("current")
_RtmEntityBfdJoinStatus_Type = RtmMjStatus
_RtmEntityBfdJoinStatus_Object = MibTableColumn
rtmEntityBfdJoinStatus = _RtmEntityBfdJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 41),
    _RtmEntityBfdJoinStatus_Type()
)
rtmEntityBfdJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmEntityBfdJoinStatus.setStatus("current")


class _RtmEntityEnableTrapSupport_Type(TruthValue):
    """Custom type rtmEntityEnableTrapSupport based on TruthValue"""


_RtmEntityEnableTrapSupport_Object = MibTableColumn
rtmEntityEnableTrapSupport = _RtmEntityEnableTrapSupport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 1, 1, 42),
    _RtmEntityEnableTrapSupport_Type()
)
rtmEntityEnableTrapSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmEntityEnableTrapSupport.setStatus("current")
_RtmRedistTable_Object = MibTable
rtmRedistTable = _RtmRedistTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rtmRedistTable.setStatus("current")
_RtmRedistEntry_Object = MibTableRow
rtmRedistEntry = _RtmRedistEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1)
)
rtmRedistEntry.setIndexNames(
    (0, "DC-RTM-MIB", "rtmRedistFteIndex"),
    (0, "DC-RTM-MIB", "rtmRedistEntryId"),
)
if mibBuilder.loadTexts:
    rtmRedistEntry.setStatus("current")
_RtmRedistFteIndex_Type = FteIndex
_RtmRedistFteIndex_Object = MibTableColumn
rtmRedistFteIndex = _RtmRedistFteIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 1),
    _RtmRedistFteIndex_Type()
)
rtmRedistFteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRedistFteIndex.setStatus("current")
_RtmRedistEntryId_Type = Unsigned32
_RtmRedistEntryId_Object = MibTableColumn
rtmRedistEntryId = _RtmRedistEntryId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 2),
    _RtmRedistEntryId_Type()
)
rtmRedistEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRedistEntryId.setStatus("current")
_RtmRedistRowStatus_Type = RowStatus
_RtmRedistRowStatus_Object = MibTableColumn
rtmRedistRowStatus = _RtmRedistRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 3),
    _RtmRedistRowStatus_Type()
)
rtmRedistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistRowStatus.setStatus("current")


class _RtmRedistAdminStat_Type(AdminStatus):
    """Custom type rtmRedistAdminStat based on AdminStatus"""


_RtmRedistAdminStat_Object = MibTableColumn
rtmRedistAdminStat = _RtmRedistAdminStat_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 4),
    _RtmRedistAdminStat_Type()
)
rtmRedistAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistAdminStat.setStatus("current")


class _RtmRedistPriority_Type(Integer32):
    """Custom type rtmRedistPriority based on Integer32"""
    defaultHexValue = 2147483647


_RtmRedistPriority_Object = MibTableColumn
rtmRedistPriority = _RtmRedistPriority_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 5),
    _RtmRedistPriority_Type()
)
rtmRedistPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistPriority.setStatus("current")


class _RtmRedistInfoSrc_Type(InfoSourceDest):
    """Custom type rtmRedistInfoSrc based on InfoSourceDest"""


_RtmRedistInfoSrc_Object = MibTableColumn
rtmRedistInfoSrc = _RtmRedistInfoSrc_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 6),
    _RtmRedistInfoSrc_Type()
)
rtmRedistInfoSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistInfoSrc.setStatus("current")


class _RtmRedistSrcInstFlt_Type(TruthValue):
    """Custom type rtmRedistSrcInstFlt based on TruthValue"""


_RtmRedistSrcInstFlt_Object = MibTableColumn
rtmRedistSrcInstFlt = _RtmRedistSrcInstFlt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 7),
    _RtmRedistSrcInstFlt_Type()
)
rtmRedistSrcInstFlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistSrcInstFlt.setStatus("current")


class _RtmRedistSrcInst_Type(FteIndex):
    """Custom type rtmRedistSrcInst based on FteIndex"""
    defaultValue = 0


_RtmRedistSrcInst_Object = MibTableColumn
rtmRedistSrcInst = _RtmRedistSrcInst_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 8),
    _RtmRedistSrcInst_Type()
)
rtmRedistSrcInst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistSrcInst.setStatus("current")


class _RtmRedistInfoDest_Type(InfoSourceDest):
    """Custom type rtmRedistInfoDest based on InfoSourceDest"""


_RtmRedistInfoDest_Object = MibTableColumn
rtmRedistInfoDest = _RtmRedistInfoDest_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 9),
    _RtmRedistInfoDest_Type()
)
rtmRedistInfoDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistInfoDest.setStatus("current")


class _RtmRedistDestInstFlt_Type(TruthValue):
    """Custom type rtmRedistDestInstFlt based on TruthValue"""


_RtmRedistDestInstFlt_Object = MibTableColumn
rtmRedistDestInstFlt = _RtmRedistDestInstFlt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 10),
    _RtmRedistDestInstFlt_Type()
)
rtmRedistDestInstFlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistDestInstFlt.setStatus("current")


class _RtmRedistDestInst_Type(FteIndex):
    """Custom type rtmRedistDestInst based on FteIndex"""
    defaultValue = 0


_RtmRedistDestInst_Object = MibTableColumn
rtmRedistDestInst = _RtmRedistDestInst_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 11),
    _RtmRedistDestInst_Type()
)
rtmRedistDestInst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistDestInst.setStatus("current")
_RtmRedistAddrFilterType_Type = InetAddressType
_RtmRedistAddrFilterType_Object = MibTableColumn
rtmRedistAddrFilterType = _RtmRedistAddrFilterType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 12),
    _RtmRedistAddrFilterType_Type()
)
rtmRedistAddrFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistAddrFilterType.setStatus("current")


class _RtmRedistAddrFilter_Type(InetAddress):
    """Custom type rtmRedistAddrFilter based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmRedistAddrFilter_Type.__name__ = "InetAddress"
_RtmRedistAddrFilter_Object = MibTableColumn
rtmRedistAddrFilter = _RtmRedistAddrFilter_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 13),
    _RtmRedistAddrFilter_Type()
)
rtmRedistAddrFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistAddrFilter.setStatus("current")


class _RtmRedistAddrFltLen_Type(Integer32):
    """Custom type rtmRedistAddrFltLen based on Integer32"""
    defaultValue = 0


_RtmRedistAddrFltLen_Object = MibTableColumn
rtmRedistAddrFltLen = _RtmRedistAddrFltLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 14),
    _RtmRedistAddrFltLen_Type()
)
rtmRedistAddrFltLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistAddrFltLen.setStatus("current")
_RtmRedistHopFltValType_Type = InetAddressType
_RtmRedistHopFltValType_Object = MibTableColumn
rtmRedistHopFltValType = _RtmRedistHopFltValType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 15),
    _RtmRedistHopFltValType_Type()
)
rtmRedistHopFltValType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistHopFltValType.setStatus("current")


class _RtmRedistHopFltVal_Type(InetAddress):
    """Custom type rtmRedistHopFltVal based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmRedistHopFltVal_Type.__name__ = "InetAddress"
_RtmRedistHopFltVal_Object = MibTableColumn
rtmRedistHopFltVal = _RtmRedistHopFltVal_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 16),
    _RtmRedistHopFltVal_Type()
)
rtmRedistHopFltVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistHopFltVal.setStatus("current")


class _RtmRedistHopFltLen_Type(Integer32):
    """Custom type rtmRedistHopFltLen based on Integer32"""
    defaultValue = 0


_RtmRedistHopFltLen_Object = MibTableColumn
rtmRedistHopFltLen = _RtmRedistHopFltLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 17),
    _RtmRedistHopFltLen_Type()
)
rtmRedistHopFltLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistHopFltLen.setStatus("current")


class _RtmRedistIfIndexFlt_Type(TruthValue):
    """Custom type rtmRedistIfIndexFlt based on TruthValue"""


_RtmRedistIfIndexFlt_Object = MibTableColumn
rtmRedistIfIndexFlt = _RtmRedistIfIndexFlt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 18),
    _RtmRedistIfIndexFlt_Type()
)
rtmRedistIfIndexFlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistIfIndexFlt.setStatus("current")


class _RtmRedistIfIndex_Type(Integer32):
    """Custom type rtmRedistIfIndex based on Integer32"""
    defaultValue = 0


_RtmRedistIfIndex_Object = MibTableColumn
rtmRedistIfIndex = _RtmRedistIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 19),
    _RtmRedistIfIndex_Type()
)
rtmRedistIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistIfIndex.setStatus("current")


class _RtmRedistPathTypeFlt_Type(TruthValue):
    """Custom type rtmRedistPathTypeFlt based on TruthValue"""


_RtmRedistPathTypeFlt_Object = MibTableColumn
rtmRedistPathTypeFlt = _RtmRedistPathTypeFlt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 20),
    _RtmRedistPathTypeFlt_Type()
)
rtmRedistPathTypeFlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistPathTypeFlt.setStatus("current")


class _RtmRedistPathType_Type(PathType):
    """Custom type rtmRedistPathType based on PathType"""


_RtmRedistPathType_Object = MibTableColumn
rtmRedistPathType = _RtmRedistPathType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 21),
    _RtmRedistPathType_Type()
)
rtmRedistPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistPathType.setStatus("current")


class _RtmRedistOspfAreaFlt_Type(TruthValue):
    """Custom type rtmRedistOspfAreaFlt based on TruthValue"""


_RtmRedistOspfAreaFlt_Object = MibTableColumn
rtmRedistOspfAreaFlt = _RtmRedistOspfAreaFlt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 22),
    _RtmRedistOspfAreaFlt_Type()
)
rtmRedistOspfAreaFlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistOspfAreaFlt.setStatus("current")


class _RtmRedistOspfArea_Type(IpAddress):
    """Custom type rtmRedistOspfArea based on IpAddress"""
    defaultHexValue = "00000000"


_RtmRedistOspfArea_Object = MibTableColumn
rtmRedistOspfArea = _RtmRedistOspfArea_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 23),
    _RtmRedistOspfArea_Type()
)
rtmRedistOspfArea.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistOspfArea.setStatus("current")


class _RtmRedistOspfTagFlt_Type(TruthValue):
    """Custom type rtmRedistOspfTagFlt based on TruthValue"""


_RtmRedistOspfTagFlt_Object = MibTableColumn
rtmRedistOspfTagFlt = _RtmRedistOspfTagFlt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 24),
    _RtmRedistOspfTagFlt_Type()
)
rtmRedistOspfTagFlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistOspfTagFlt.setStatus("current")


class _RtmRedistOspfTag_Type(OspfTag):
    """Custom type rtmRedistOspfTag based on OspfTag"""
    defaultValue = 0


_RtmRedistOspfTag_Object = MibTableColumn
rtmRedistOspfTag = _RtmRedistOspfTag_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 25),
    _RtmRedistOspfTag_Type()
)
rtmRedistOspfTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistOspfTag.setStatus("current")


class _RtmRedistCommunityFlt_Type(TruthValue):
    """Custom type rtmRedistCommunityFlt based on TruthValue"""


_RtmRedistCommunityFlt_Object = MibTableColumn
rtmRedistCommunityFlt = _RtmRedistCommunityFlt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 26),
    _RtmRedistCommunityFlt_Type()
)
rtmRedistCommunityFlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistCommunityFlt.setStatus("current")


class _RtmRedistCommunity_Type(BgpCommunity):
    """Custom type rtmRedistCommunity based on BgpCommunity"""
    defaultHexValue = "00000000"


_RtmRedistCommunity_Object = MibTableColumn
rtmRedistCommunity = _RtmRedistCommunity_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 27),
    _RtmRedistCommunity_Type()
)
rtmRedistCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistCommunity.setStatus("current")


class _RtmRedistExtCommFlt_Type(TruthValue):
    """Custom type rtmRedistExtCommFlt based on TruthValue"""


_RtmRedistExtCommFlt_Object = MibTableColumn
rtmRedistExtCommFlt = _RtmRedistExtCommFlt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 28),
    _RtmRedistExtCommFlt_Type()
)
rtmRedistExtCommFlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistExtCommFlt.setStatus("current")


class _RtmRedistExtComm_Type(BgpExtendedCommunity):
    """Custom type rtmRedistExtComm based on BgpExtendedCommunity"""
    defaultHexValue = "0000000000000000"


_RtmRedistExtComm_Object = MibTableColumn
rtmRedistExtComm = _RtmRedistExtComm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 29),
    _RtmRedistExtComm_Type()
)
rtmRedistExtComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistExtComm.setStatus("current")


class _RtmRedistRedistFlag_Type(TruthValue):
    """Custom type rtmRedistRedistFlag based on TruthValue"""


_RtmRedistRedistFlag_Object = MibTableColumn
rtmRedistRedistFlag = _RtmRedistRedistFlag_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 30),
    _RtmRedistRedistFlag_Type()
)
rtmRedistRedistFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistRedistFlag.setStatus("current")


class _RtmRedistMetricConv_Type(MetricConversion):
    """Custom type rtmRedistMetricConv based on MetricConversion"""


_RtmRedistMetricConv_Object = MibTableColumn
rtmRedistMetricConv = _RtmRedistMetricConv_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 31),
    _RtmRedistMetricConv_Type()
)
rtmRedistMetricConv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistMetricConv.setStatus("current")


class _RtmRedistMetricValue_Type(Unsigned32):
    """Custom type rtmRedistMetricValue based on Unsigned32"""
    defaultValue = 1


_RtmRedistMetricValue_Object = MibTableColumn
rtmRedistMetricValue = _RtmRedistMetricValue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 32),
    _RtmRedistMetricValue_Type()
)
rtmRedistMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistMetricValue.setStatus("current")


class _RtmRedistNwPathType_Type(PathType):
    """Custom type rtmRedistNwPathType based on PathType"""


_RtmRedistNwPathType_Object = MibTableColumn
rtmRedistNwPathType = _RtmRedistNwPathType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 33),
    _RtmRedistNwPathType_Type()
)
rtmRedistNwPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistNwPathType.setStatus("current")


class _RtmRedistNwOspfTag_Type(OspfTag):
    """Custom type rtmRedistNwOspfTag based on OspfTag"""
    defaultValue = 0


_RtmRedistNwOspfTag_Object = MibTableColumn
rtmRedistNwOspfTag = _RtmRedistNwOspfTag_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 34),
    _RtmRedistNwOspfTag_Type()
)
rtmRedistNwOspfTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistNwOspfTag.setStatus("current")


class _RtmRedistOspfPropagate_Type(TruthValue):
    """Custom type rtmRedistOspfPropagate based on TruthValue"""


_RtmRedistOspfPropagate_Object = MibTableColumn
rtmRedistOspfPropagate = _RtmRedistOspfPropagate_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 35),
    _RtmRedistOspfPropagate_Type()
)
rtmRedistOspfPropagate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistOspfPropagate.setStatus("current")


class _RtmRedistAddCommunity_Type(TruthValue):
    """Custom type rtmRedistAddCommunity based on TruthValue"""


_RtmRedistAddCommunity_Object = MibTableColumn
rtmRedistAddCommunity = _RtmRedistAddCommunity_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 36),
    _RtmRedistAddCommunity_Type()
)
rtmRedistAddCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistAddCommunity.setStatus("obsolete")


class _RtmRedistNwCommunity_Type(BgpCommunity):
    """Custom type rtmRedistNwCommunity based on BgpCommunity"""
    defaultHexValue = "00000000"


_RtmRedistNwCommunity_Object = MibTableColumn
rtmRedistNwCommunity = _RtmRedistNwCommunity_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 37),
    _RtmRedistNwCommunity_Type()
)
rtmRedistNwCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistNwCommunity.setStatus("obsolete")


class _RtmRedistAddExtComm_Type(TruthValue):
    """Custom type rtmRedistAddExtComm based on TruthValue"""


_RtmRedistAddExtComm_Object = MibTableColumn
rtmRedistAddExtComm = _RtmRedistAddExtComm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 38),
    _RtmRedistAddExtComm_Type()
)
rtmRedistAddExtComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistAddExtComm.setStatus("obsolete")


class _RtmRedistNwExtComm_Type(BgpExtendedCommunity):
    """Custom type rtmRedistNwExtComm based on BgpExtendedCommunity"""
    defaultHexValue = "0000000000000000"


_RtmRedistNwExtComm_Object = MibTableColumn
rtmRedistNwExtComm = _RtmRedistNwExtComm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 39),
    _RtmRedistNwExtComm_Type()
)
rtmRedistNwExtComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistNwExtComm.setStatus("obsolete")


class _RtmRedistNwOrigin_Type(BgpOriginCode):
    """Custom type rtmRedistNwOrigin based on BgpOriginCode"""


_RtmRedistNwOrigin_Object = MibTableColumn
rtmRedistNwOrigin = _RtmRedistNwOrigin_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 40),
    _RtmRedistNwOrigin_Type()
)
rtmRedistNwOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistNwOrigin.setStatus("current")


class _RtmRedistAddMed_Type(TruthValue):
    """Custom type rtmRedistAddMed based on TruthValue"""


_RtmRedistAddMed_Object = MibTableColumn
rtmRedistAddMed = _RtmRedistAddMed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 41),
    _RtmRedistAddMed_Type()
)
rtmRedistAddMed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistAddMed.setStatus("current")


class _RtmRedistNwMed_Type(Integer32):
    """Custom type rtmRedistNwMed based on Integer32"""
    defaultValue = 0


_RtmRedistNwMed_Object = MibTableColumn
rtmRedistNwMed = _RtmRedistNwMed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 42),
    _RtmRedistNwMed_Type()
)
rtmRedistNwMed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistNwMed.setStatus("current")


class _RtmRedistAddLocalPref_Type(TruthValue):
    """Custom type rtmRedistAddLocalPref based on TruthValue"""


_RtmRedistAddLocalPref_Object = MibTableColumn
rtmRedistAddLocalPref = _RtmRedistAddLocalPref_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 43),
    _RtmRedistAddLocalPref_Type()
)
rtmRedistAddLocalPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistAddLocalPref.setStatus("current")


class _RtmRedistNwLocalPref_Type(Integer32):
    """Custom type rtmRedistNwLocalPref based on Integer32"""
    defaultValue = 0


_RtmRedistNwLocalPref_Object = MibTableColumn
rtmRedistNwLocalPref = _RtmRedistNwLocalPref_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 44),
    _RtmRedistNwLocalPref_Type()
)
rtmRedistNwLocalPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistNwLocalPref.setStatus("current")


class _RtmRedistSetListId_Type(Unsigned32):
    """Custom type rtmRedistSetListId based on Unsigned32"""
    defaultValue = 0


_RtmRedistSetListId_Object = MibTableColumn
rtmRedistSetListId = _RtmRedistSetListId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 45),
    _RtmRedistSetListId_Type()
)
rtmRedistSetListId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistSetListId.setStatus("current")


class _RtmRedistAddAsLimUpper_Type(TruthValue):
    """Custom type rtmRedistAddAsLimUpper based on TruthValue"""


_RtmRedistAddAsLimUpper_Object = MibTableColumn
rtmRedistAddAsLimUpper = _RtmRedistAddAsLimUpper_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 46),
    _RtmRedistAddAsLimUpper_Type()
)
rtmRedistAddAsLimUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistAddAsLimUpper.setStatus("current")


class _RtmRedistNwAsLimUpper_Type(Unsigned32):
    """Custom type rtmRedistNwAsLimUpper based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RtmRedistNwAsLimUpper_Type.__name__ = "Unsigned32"
_RtmRedistNwAsLimUpper_Object = MibTableColumn
rtmRedistNwAsLimUpper = _RtmRedistNwAsLimUpper_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 47),
    _RtmRedistNwAsLimUpper_Type()
)
rtmRedistNwAsLimUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistNwAsLimUpper.setStatus("current")


class _RtmRedistOspfVpnPeCeSupport_Type(TruthValue):
    """Custom type rtmRedistOspfVpnPeCeSupport based on TruthValue"""


_RtmRedistOspfVpnPeCeSupport_Object = MibTableColumn
rtmRedistOspfVpnPeCeSupport = _RtmRedistOspfVpnPeCeSupport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 2, 1, 48),
    _RtmRedistOspfVpnPeCeSupport_Type()
)
rtmRedistOspfVpnPeCeSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRedistOspfVpnPeCeSupport.setStatus("current")
_RtmStaticRtTable_Object = MibTable
rtmStaticRtTable = _RtmStaticRtTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rtmStaticRtTable.setStatus("current")
_RtmStaticRtEntry_Object = MibTableRow
rtmStaticRtEntry = _RtmStaticRtEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1)
)
rtmStaticRtEntry.setIndexNames(
    (0, "DC-RTM-MIB", "rtmStaticRtFteIndex"),
    (0, "DC-RTM-MIB", "rtmStaticRtPathType"),
    (0, "DC-RTM-MIB", "rtmStaticRtDestAddrType"),
    (0, "DC-RTM-MIB", "rtmStaticRtDestAddr"),
    (0, "DC-RTM-MIB", "rtmStaticRtDestLen"),
    (0, "DC-RTM-MIB", "rtmStaticRtNextHopType"),
    (0, "DC-RTM-MIB", "rtmStaticRtNextHop"),
    (0, "DC-RTM-MIB", "rtmStaticRtIfIndex"),
)
if mibBuilder.loadTexts:
    rtmStaticRtEntry.setStatus("current")
_RtmStaticRtFteIndex_Type = FteIndex
_RtmStaticRtFteIndex_Object = MibTableColumn
rtmStaticRtFteIndex = _RtmStaticRtFteIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 1),
    _RtmStaticRtFteIndex_Type()
)
rtmStaticRtFteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmStaticRtFteIndex.setStatus("current")
_RtmStaticRtDestAddrType_Type = InetAddressType
_RtmStaticRtDestAddrType_Object = MibTableColumn
rtmStaticRtDestAddrType = _RtmStaticRtDestAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 2),
    _RtmStaticRtDestAddrType_Type()
)
rtmStaticRtDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmStaticRtDestAddrType.setStatus("current")


class _RtmStaticRtDestAddr_Type(InetAddress):
    """Custom type rtmStaticRtDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmStaticRtDestAddr_Type.__name__ = "InetAddress"
_RtmStaticRtDestAddr_Object = MibTableColumn
rtmStaticRtDestAddr = _RtmStaticRtDestAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 3),
    _RtmStaticRtDestAddr_Type()
)
rtmStaticRtDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmStaticRtDestAddr.setStatus("current")


class _RtmStaticRtDestLen_Type(Integer32):
    """Custom type rtmStaticRtDestLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RtmStaticRtDestLen_Type.__name__ = "Integer32"
_RtmStaticRtDestLen_Object = MibTableColumn
rtmStaticRtDestLen = _RtmStaticRtDestLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 4),
    _RtmStaticRtDestLen_Type()
)
rtmStaticRtDestLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmStaticRtDestLen.setStatus("current")
_RtmStaticRtNextHopType_Type = InetAddressType
_RtmStaticRtNextHopType_Object = MibTableColumn
rtmStaticRtNextHopType = _RtmStaticRtNextHopType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 5),
    _RtmStaticRtNextHopType_Type()
)
rtmStaticRtNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmStaticRtNextHopType.setStatus("current")


class _RtmStaticRtNextHop_Type(InetAddress):
    """Custom type rtmStaticRtNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmStaticRtNextHop_Type.__name__ = "InetAddress"
_RtmStaticRtNextHop_Object = MibTableColumn
rtmStaticRtNextHop = _RtmStaticRtNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 6),
    _RtmStaticRtNextHop_Type()
)
rtmStaticRtNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmStaticRtNextHop.setStatus("current")


class _RtmStaticRtIfIndex_Type(Integer32):
    """Custom type rtmStaticRtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmStaticRtIfIndex_Type.__name__ = "Integer32"
_RtmStaticRtIfIndex_Object = MibTableColumn
rtmStaticRtIfIndex = _RtmStaticRtIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 7),
    _RtmStaticRtIfIndex_Type()
)
rtmStaticRtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmStaticRtIfIndex.setStatus("current")


class _RtmStaticRtOutIfIndex_Type(Integer32):
    """Custom type rtmStaticRtOutIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmStaticRtOutIfIndex_Type.__name__ = "Integer32"
_RtmStaticRtOutIfIndex_Object = MibTableColumn
rtmStaticRtOutIfIndex = _RtmStaticRtOutIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 8),
    _RtmStaticRtOutIfIndex_Type()
)
rtmStaticRtOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmStaticRtOutIfIndex.setStatus("current")
_RtmStaticRtRowStatus_Type = RowStatus
_RtmStaticRtRowStatus_Object = MibTableColumn
rtmStaticRtRowStatus = _RtmStaticRtRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 9),
    _RtmStaticRtRowStatus_Type()
)
rtmStaticRtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtRowStatus.setStatus("current")


class _RtmStaticRtAdminStat_Type(AdminStatus):
    """Custom type rtmStaticRtAdminStat based on AdminStatus"""


_RtmStaticRtAdminStat_Object = MibTableColumn
rtmStaticRtAdminStat = _RtmStaticRtAdminStat_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 10),
    _RtmStaticRtAdminStat_Type()
)
rtmStaticRtAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtAdminStat.setStatus("current")


class _RtmStaticRtOverride_Type(TruthValue):
    """Custom type rtmStaticRtOverride based on TruthValue"""


_RtmStaticRtOverride_Object = MibTableColumn
rtmStaticRtOverride = _RtmStaticRtOverride_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 11),
    _RtmStaticRtOverride_Type()
)
rtmStaticRtOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtOverride.setStatus("current")


class _RtmStaticRtAdminDist_Type(AdminDistance):
    """Custom type rtmStaticRtAdminDist based on AdminDistance"""
    defaultValue = 1


_RtmStaticRtAdminDist_Object = MibTableColumn
rtmStaticRtAdminDist = _RtmStaticRtAdminDist_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 12),
    _RtmStaticRtAdminDist_Type()
)
rtmStaticRtAdminDist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtAdminDist.setStatus("current")


class _RtmStaticRtAction_Type(RouteAction):
    """Custom type rtmStaticRtAction based on RouteAction"""


_RtmStaticRtAction_Object = MibTableColumn
rtmStaticRtAction = _RtmStaticRtAction_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 13),
    _RtmStaticRtAction_Type()
)
rtmStaticRtAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtAction.setStatus("current")


class _RtmStaticRtFwdAddrType_Type(InetAddressType):
    """Custom type rtmStaticRtFwdAddrType based on InetAddressType"""


_RtmStaticRtFwdAddrType_Object = MibTableColumn
rtmStaticRtFwdAddrType = _RtmStaticRtFwdAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 14),
    _RtmStaticRtFwdAddrType_Type()
)
rtmStaticRtFwdAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtFwdAddrType.setStatus("current")


class _RtmStaticRtForwardingAddr_Type(InetAddress):
    """Custom type rtmStaticRtForwardingAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmStaticRtForwardingAddr_Type.__name__ = "InetAddress"
_RtmStaticRtForwardingAddr_Object = MibTableColumn
rtmStaticRtForwardingAddr = _RtmStaticRtForwardingAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 15),
    _RtmStaticRtForwardingAddr_Type()
)
rtmStaticRtForwardingAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtForwardingAddr.setStatus("current")
_RtmStaticRtPathType_Type = PathType
_RtmStaticRtPathType_Object = MibTableColumn
rtmStaticRtPathType = _RtmStaticRtPathType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 16),
    _RtmStaticRtPathType_Type()
)
rtmStaticRtPathType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmStaticRtPathType.setStatus("current")


class _RtmStaticRtUsePathCost_Type(TruthValue):
    """Custom type rtmStaticRtUsePathCost based on TruthValue"""


_RtmStaticRtUsePathCost_Object = MibTableColumn
rtmStaticRtUsePathCost = _RtmStaticRtUsePathCost_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 17),
    _RtmStaticRtUsePathCost_Type()
)
rtmStaticRtUsePathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtUsePathCost.setStatus("current")


class _RtmStaticRtPathCost_Type(Integer32):
    """Custom type rtmStaticRtPathCost based on Integer32"""
    defaultValue = 0


_RtmStaticRtPathCost_Object = MibTableColumn
rtmStaticRtPathCost = _RtmStaticRtPathCost_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 18),
    _RtmStaticRtPathCost_Type()
)
rtmStaticRtPathCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtPathCost.setStatus("current")


class _RtmStaticRtUserData_Type(OctetString):
    """Custom type rtmStaticRtUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RtmStaticRtUserData_Type.__name__ = "OctetString"
_RtmStaticRtUserData_Object = MibTableColumn
rtmStaticRtUserData = _RtmStaticRtUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 19),
    _RtmStaticRtUserData_Type()
)
rtmStaticRtUserData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtUserData.setStatus("current")
_RtmStaticRtLooseNextHop_Type = TruthValue
_RtmStaticRtLooseNextHop_Object = MibTableColumn
rtmStaticRtLooseNextHop = _RtmStaticRtLooseNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 20),
    _RtmStaticRtLooseNextHop_Type()
)
rtmStaticRtLooseNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmStaticRtLooseNextHop.setStatus("current")


class _RtmStaticRtBfdSupport_Type(RtmBfdSupport):
    """Custom type rtmStaticRtBfdSupport based on RtmBfdSupport"""


_RtmStaticRtBfdSupport_Object = MibTableColumn
rtmStaticRtBfdSupport = _RtmStaticRtBfdSupport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 21),
    _RtmStaticRtBfdSupport_Type()
)
rtmStaticRtBfdSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmStaticRtBfdSupport.setStatus("current")
_RtmStaticRtBfdStatus_Type = BfdSessionStatus
_RtmStaticRtBfdStatus_Object = MibTableColumn
rtmStaticRtBfdStatus = _RtmStaticRtBfdStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 3, 1, 22),
    _RtmStaticRtBfdStatus_Type()
)
rtmStaticRtBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmStaticRtBfdStatus.setStatus("current")
_RtmMjTable_Object = MibTable
rtmMjTable = _RtmMjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rtmMjTable.setStatus("current")
_RtmMjEntry_Object = MibTableRow
rtmMjEntry = _RtmMjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1)
)
rtmMjEntry.setIndexNames(
    (0, "DC-RTM-MIB", "rtmMjRtmFteIndex"),
    (0, "DC-RTM-MIB", "rtmMjSlaveFteId"),
    (0, "DC-RTM-MIB", "rtmMjSlaveType"),
)
if mibBuilder.loadTexts:
    rtmMjEntry.setStatus("current")
_RtmMjRtmFteIndex_Type = FteIndex
_RtmMjRtmFteIndex_Object = MibTableColumn
rtmMjRtmFteIndex = _RtmMjRtmFteIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1, 1),
    _RtmMjRtmFteIndex_Type()
)
rtmMjRtmFteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmMjRtmFteIndex.setStatus("current")
_RtmMjSlaveFteId_Type = FteIndex
_RtmMjSlaveFteId_Object = MibTableColumn
rtmMjSlaveFteId = _RtmMjSlaveFteId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1, 2),
    _RtmMjSlaveFteId_Type()
)
rtmMjSlaveFteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmMjSlaveFteId.setStatus("current")


class _RtmMjIfType_Type(InterfaceType):
    """Custom type rtmMjIfType based on InterfaceType"""


_RtmMjIfType_Object = MibTableColumn
rtmMjIfType = _RtmMjIfType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1, 3),
    _RtmMjIfType_Type()
)
rtmMjIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmMjIfType.setStatus("current")
_RtmMjRowStatus_Type = RowStatus
_RtmMjRowStatus_Object = MibTableColumn
rtmMjRowStatus = _RtmMjRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1, 4),
    _RtmMjRowStatus_Type()
)
rtmMjRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmMjRowStatus.setStatus("current")


class _RtmMjAdminStatus_Type(AdminStatus):
    """Custom type rtmMjAdminStatus based on AdminStatus"""


_RtmMjAdminStatus_Object = MibTableColumn
rtmMjAdminStatus = _RtmMjAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1, 5),
    _RtmMjAdminStatus_Type()
)
rtmMjAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmMjAdminStatus.setStatus("current")
_RtmMjOperStatus_Type = OperStatus
_RtmMjOperStatus_Object = MibTableColumn
rtmMjOperStatus = _RtmMjOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1, 6),
    _RtmMjOperStatus_Type()
)
rtmMjOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmMjOperStatus.setStatus("current")
_RtmMjJoinStatus_Type = RtmMjStatus
_RtmMjJoinStatus_Object = MibTableColumn
rtmMjJoinStatus = _RtmMjJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1, 7),
    _RtmMjJoinStatus_Type()
)
rtmMjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmMjJoinStatus.setStatus("current")
_RtmMjSlaveType_Type = AriPrtnrType
_RtmMjSlaveType_Object = MibTableColumn
rtmMjSlaveType = _RtmMjSlaveType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1, 8),
    _RtmMjSlaveType_Type()
)
rtmMjSlaveType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmMjSlaveType.setStatus("current")


class _RtmMjSafi_Type(InetSubAddressType):
    """Custom type rtmMjSafi based on InetSubAddressType"""


_RtmMjSafi_Object = MibTableColumn
rtmMjSafi = _RtmMjSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 4, 1, 9),
    _RtmMjSafi_Type()
)
rtmMjSafi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmMjSafi.setStatus("current")
_RtmSjTable_Object = MibTable
rtmSjTable = _RtmSjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rtmSjTable.setStatus("current")
_RtmSjEntry_Object = MibTableRow
rtmSjEntry = _RtmSjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 5, 1)
)
rtmSjEntry.setIndexNames(
    (0, "DC-RTM-MIB", "rtmSjRtmFteIndex"),
    (0, "DC-RTM-MIB", "rtmSjRtmRpmIndex"),
)
if mibBuilder.loadTexts:
    rtmSjEntry.setStatus("current")
_RtmSjRtmFteIndex_Type = FteIndex
_RtmSjRtmFteIndex_Object = MibTableColumn
rtmSjRtmFteIndex = _RtmSjRtmFteIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 5, 1, 1),
    _RtmSjRtmFteIndex_Type()
)
rtmSjRtmFteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmSjRtmFteIndex.setStatus("current")


class _RtmSjRtmRpmIndex_Type(Integer32):
    """Custom type rtmSjRtmRpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmSjRtmRpmIndex_Type.__name__ = "Integer32"
_RtmSjRtmRpmIndex_Object = MibTableColumn
rtmSjRtmRpmIndex = _RtmSjRtmRpmIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 5, 1, 2),
    _RtmSjRtmRpmIndex_Type()
)
rtmSjRtmRpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmSjRtmRpmIndex.setStatus("current")
_RtmSjIfType_Type = InterfaceType
_RtmSjIfType_Object = MibTableColumn
rtmSjIfType = _RtmSjIfType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 5, 1, 3),
    _RtmSjIfType_Type()
)
rtmSjIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmSjIfType.setStatus("current")
_RtmSjMastFteType_Type = Integer32
_RtmSjMastFteType_Object = MibTableColumn
rtmSjMastFteType = _RtmSjMastFteType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 5, 1, 4),
    _RtmSjMastFteType_Type()
)
rtmSjMastFteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmSjMastFteType.setStatus("current")
_RtmSjMastFteId_Type = FteIndex
_RtmSjMastFteId_Object = MibTableColumn
rtmSjMastFteId = _RtmSjMastFteId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 5, 1, 5),
    _RtmSjMastFteId_Type()
)
rtmSjMastFteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmSjMastFteId.setStatus("current")
_RtmSjJoinStatus_Type = RtmSjStatus
_RtmSjJoinStatus_Object = MibTableColumn
rtmSjJoinStatus = _RtmSjJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 5, 1, 6),
    _RtmSjJoinStatus_Type()
)
rtmSjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmSjJoinStatus.setStatus("current")
_RtmRouteTable_Object = MibTable
rtmRouteTable = _RtmRouteTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rtmRouteTable.setStatus("current")
_RtmRouteEntry_Object = MibTableRow
rtmRouteEntry = _RtmRouteEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1)
)
rtmRouteEntry.setIndexNames(
    (0, "DC-RTM-MIB", "rtmRouteFteIndex"),
    (0, "DC-RTM-MIB", "rtmRouteDestType"),
    (0, "DC-RTM-MIB", "rtmRouteDest"),
    (0, "DC-RTM-MIB", "rtmRouteDestLen"),
    (0, "DC-RTM-MIB", "rtmRouteTos"),
    (0, "DC-RTM-MIB", "rtmRouteNextHopType"),
    (0, "DC-RTM-MIB", "rtmRouteNextHop"),
    (0, "DC-RTM-MIB", "rtmRouteIfIndex"),
)
if mibBuilder.loadTexts:
    rtmRouteEntry.setStatus("current")
_RtmRouteFteIndex_Type = FteIndex
_RtmRouteFteIndex_Object = MibTableColumn
rtmRouteFteIndex = _RtmRouteFteIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 1),
    _RtmRouteFteIndex_Type()
)
rtmRouteFteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRouteFteIndex.setStatus("current")
_RtmRouteStatus_Type = RowStatus
_RtmRouteStatus_Object = MibTableColumn
rtmRouteStatus = _RtmRouteStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 2),
    _RtmRouteStatus_Type()
)
rtmRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteStatus.setStatus("current")
_RtmRouteDestType_Type = InetAddressType
_RtmRouteDestType_Object = MibTableColumn
rtmRouteDestType = _RtmRouteDestType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 3),
    _RtmRouteDestType_Type()
)
rtmRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRouteDestType.setStatus("current")


class _RtmRouteDest_Type(InetAddress):
    """Custom type rtmRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmRouteDest_Type.__name__ = "InetAddress"
_RtmRouteDest_Object = MibTableColumn
rtmRouteDest = _RtmRouteDest_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 4),
    _RtmRouteDest_Type()
)
rtmRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRouteDest.setStatus("current")


class _RtmRouteDestLen_Type(Integer32):
    """Custom type rtmRouteDestLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RtmRouteDestLen_Type.__name__ = "Integer32"
_RtmRouteDestLen_Object = MibTableColumn
rtmRouteDestLen = _RtmRouteDestLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 5),
    _RtmRouteDestLen_Type()
)
rtmRouteDestLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRouteDestLen.setStatus("current")


class _RtmRouteTos_Type(Integer32):
    """Custom type rtmRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RtmRouteTos_Type.__name__ = "Integer32"
_RtmRouteTos_Object = MibTableColumn
rtmRouteTos = _RtmRouteTos_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 6),
    _RtmRouteTos_Type()
)
rtmRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRouteTos.setStatus("current")
_RtmRouteNextHopType_Type = InetAddressType
_RtmRouteNextHopType_Object = MibTableColumn
rtmRouteNextHopType = _RtmRouteNextHopType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 7),
    _RtmRouteNextHopType_Type()
)
rtmRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRouteNextHopType.setStatus("current")


class _RtmRouteNextHop_Type(InetAddress):
    """Custom type rtmRouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmRouteNextHop_Type.__name__ = "InetAddress"
_RtmRouteNextHop_Object = MibTableColumn
rtmRouteNextHop = _RtmRouteNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 8),
    _RtmRouteNextHop_Type()
)
rtmRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRouteNextHop.setStatus("current")


class _RtmRouteIfIndex_Type(Integer32):
    """Custom type rtmRouteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmRouteIfIndex_Type.__name__ = "Integer32"
_RtmRouteIfIndex_Object = MibTableColumn
rtmRouteIfIndex = _RtmRouteIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 9),
    _RtmRouteIfIndex_Type()
)
rtmRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRouteIfIndex.setStatus("current")
_RtmRouteType_Type = RouteType
_RtmRouteType_Object = MibTableColumn
rtmRouteType = _RtmRouteType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 10),
    _RtmRouteType_Type()
)
rtmRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteType.setStatus("current")
_RtmRouteProto_Type = IANAipRouteProtocol
_RtmRouteProto_Object = MibTableColumn
rtmRouteProto = _RtmRouteProto_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 11),
    _RtmRouteProto_Type()
)
rtmRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteProto.setStatus("current")


class _RtmRouteAge_Type(Integer32):
    """Custom type rtmRouteAge based on Integer32"""
    defaultValue = 0


_RtmRouteAge_Object = MibTableColumn
rtmRouteAge = _RtmRouteAge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 12),
    _RtmRouteAge_Type()
)
rtmRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteAge.setStatus("current")


class _RtmRouteInfo_Type(RouteInfo):
    """Custom type rtmRouteInfo based on RouteInfo"""


_RtmRouteInfo_Object = MibTableColumn
rtmRouteInfo = _RtmRouteInfo_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 13),
    _RtmRouteInfo_Type()
)
rtmRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteInfo.setStatus("current")


class _RtmRouteNextHopAS_Type(Integer32):
    """Custom type rtmRouteNextHopAS based on Integer32"""
    defaultValue = 0


_RtmRouteNextHopAS_Object = MibTableColumn
rtmRouteNextHopAS = _RtmRouteNextHopAS_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 14),
    _RtmRouteNextHopAS_Type()
)
rtmRouteNextHopAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteNextHopAS.setStatus("current")


class _RtmRouteMetric1_Type(Integer32):
    """Custom type rtmRouteMetric1 based on Integer32"""
    defaultValue = -1


_RtmRouteMetric1_Object = MibTableColumn
rtmRouteMetric1 = _RtmRouteMetric1_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 15),
    _RtmRouteMetric1_Type()
)
rtmRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteMetric1.setStatus("current")


class _RtmRouteMetric2_Type(Integer32):
    """Custom type rtmRouteMetric2 based on Integer32"""
    defaultValue = -1


_RtmRouteMetric2_Object = MibTableColumn
rtmRouteMetric2 = _RtmRouteMetric2_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 16),
    _RtmRouteMetric2_Type()
)
rtmRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteMetric2.setStatus("current")


class _RtmRouteMetric3_Type(Integer32):
    """Custom type rtmRouteMetric3 based on Integer32"""
    defaultValue = -1


_RtmRouteMetric3_Object = MibTableColumn
rtmRouteMetric3 = _RtmRouteMetric3_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 17),
    _RtmRouteMetric3_Type()
)
rtmRouteMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteMetric3.setStatus("current")


class _RtmRouteMetric4_Type(Integer32):
    """Custom type rtmRouteMetric4 based on Integer32"""
    defaultValue = -1


_RtmRouteMetric4_Object = MibTableColumn
rtmRouteMetric4 = _RtmRouteMetric4_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 18),
    _RtmRouteMetric4_Type()
)
rtmRouteMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteMetric4.setStatus("current")


class _RtmRouteMetric5_Type(Integer32):
    """Custom type rtmRouteMetric5 based on Integer32"""
    defaultValue = -1


_RtmRouteMetric5_Object = MibTableColumn
rtmRouteMetric5 = _RtmRouteMetric5_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 19),
    _RtmRouteMetric5_Type()
)
rtmRouteMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteMetric5.setStatus("current")
_RtmRouteConnected_Type = TruthValue
_RtmRouteConnected_Object = MibTableColumn
rtmRouteConnected = _RtmRouteConnected_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 20),
    _RtmRouteConnected_Type()
)
rtmRouteConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteConnected.setStatus("current")
_RtmRouteXCIndex_Type = MplsIndexType
_RtmRouteXCIndex_Object = MibTableColumn
rtmRouteXCIndex = _RtmRouteXCIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 21),
    _RtmRouteXCIndex_Type()
)
rtmRouteXCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteXCIndex.setStatus("current")


class _RtmRouteLocalDestIfIndex_Type(Integer32):
    """Custom type rtmRouteLocalDestIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmRouteLocalDestIfIndex_Type.__name__ = "Integer32"
_RtmRouteLocalDestIfIndex_Object = MibTableColumn
rtmRouteLocalDestIfIndex = _RtmRouteLocalDestIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 6, 1, 22),
    _RtmRouteLocalDestIfIndex_Type()
)
rtmRouteLocalDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRouteLocalDestIfIndex.setStatus("current")
_RtmRibTable_Object = MibTable
rtmRibTable = _RtmRibTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7)
)
if mibBuilder.loadTexts:
    rtmRibTable.setStatus("current")
_RtmRibEntry_Object = MibTableRow
rtmRibEntry = _RtmRibEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1)
)
rtmRibEntry.setIndexNames(
    (0, "DC-RTM-MIB", "rtmRibFteIndex"),
    (0, "DC-RTM-MIB", "rtmRibDestType"),
    (0, "DC-RTM-MIB", "rtmRibDest"),
    (0, "DC-RTM-MIB", "rtmRibDestLen"),
    (0, "DC-RTM-MIB", "rtmRibTos"),
    (0, "DC-RTM-MIB", "rtmRibNextHopType"),
    (0, "DC-RTM-MIB", "rtmRibNextHop"),
    (0, "DC-RTM-MIB", "rtmRibIfIndex"),
    (0, "DC-RTM-MIB", "rtmRibProto"),
    (0, "DC-RTM-MIB", "rtmRibRpmIndex"),
)
if mibBuilder.loadTexts:
    rtmRibEntry.setStatus("current")
_RtmRibFteIndex_Type = FteIndex
_RtmRibFteIndex_Object = MibTableColumn
rtmRibFteIndex = _RtmRibFteIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 1),
    _RtmRibFteIndex_Type()
)
rtmRibFteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibFteIndex.setStatus("current")
_RtmRibStatus_Type = RowStatus
_RtmRibStatus_Object = MibTableColumn
rtmRibStatus = _RtmRibStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 2),
    _RtmRibStatus_Type()
)
rtmRibStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibStatus.setStatus("current")
_RtmRibDestType_Type = InetAddressType
_RtmRibDestType_Object = MibTableColumn
rtmRibDestType = _RtmRibDestType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 3),
    _RtmRibDestType_Type()
)
rtmRibDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibDestType.setStatus("current")


class _RtmRibDest_Type(InetAddress):
    """Custom type rtmRibDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmRibDest_Type.__name__ = "InetAddress"
_RtmRibDest_Object = MibTableColumn
rtmRibDest = _RtmRibDest_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 4),
    _RtmRibDest_Type()
)
rtmRibDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibDest.setStatus("current")


class _RtmRibDestLen_Type(Integer32):
    """Custom type rtmRibDestLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RtmRibDestLen_Type.__name__ = "Integer32"
_RtmRibDestLen_Object = MibTableColumn
rtmRibDestLen = _RtmRibDestLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 5),
    _RtmRibDestLen_Type()
)
rtmRibDestLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibDestLen.setStatus("current")


class _RtmRibTos_Type(Integer32):
    """Custom type rtmRibTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RtmRibTos_Type.__name__ = "Integer32"
_RtmRibTos_Object = MibTableColumn
rtmRibTos = _RtmRibTos_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 6),
    _RtmRibTos_Type()
)
rtmRibTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibTos.setStatus("current")
_RtmRibNextHopType_Type = InetAddressType
_RtmRibNextHopType_Object = MibTableColumn
rtmRibNextHopType = _RtmRibNextHopType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 7),
    _RtmRibNextHopType_Type()
)
rtmRibNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibNextHopType.setStatus("current")


class _RtmRibNextHop_Type(InetAddress):
    """Custom type rtmRibNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmRibNextHop_Type.__name__ = "InetAddress"
_RtmRibNextHop_Object = MibTableColumn
rtmRibNextHop = _RtmRibNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 8),
    _RtmRibNextHop_Type()
)
rtmRibNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibNextHop.setStatus("current")


class _RtmRibIfIndex_Type(Integer32):
    """Custom type rtmRibIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmRibIfIndex_Type.__name__ = "Integer32"
_RtmRibIfIndex_Object = MibTableColumn
rtmRibIfIndex = _RtmRibIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 9),
    _RtmRibIfIndex_Type()
)
rtmRibIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibIfIndex.setStatus("current")
_RtmRibType_Type = RouteType
_RtmRibType_Object = MibTableColumn
rtmRibType = _RtmRibType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 10),
    _RtmRibType_Type()
)
rtmRibType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibType.setStatus("current")
_RtmRibProto_Type = IANAipRouteProtocol
_RtmRibProto_Object = MibTableColumn
rtmRibProto = _RtmRibProto_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 11),
    _RtmRibProto_Type()
)
rtmRibProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibProto.setStatus("current")


class _RtmRibAge_Type(Integer32):
    """Custom type rtmRibAge based on Integer32"""
    defaultValue = 0


_RtmRibAge_Object = MibTableColumn
rtmRibAge = _RtmRibAge_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 12),
    _RtmRibAge_Type()
)
rtmRibAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibAge.setStatus("current")


class _RtmRibInfo_Type(RouteInfo):
    """Custom type rtmRibInfo based on RouteInfo"""


_RtmRibInfo_Object = MibTableColumn
rtmRibInfo = _RtmRibInfo_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 13),
    _RtmRibInfo_Type()
)
rtmRibInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibInfo.setStatus("current")


class _RtmRibNextHopAS_Type(Integer32):
    """Custom type rtmRibNextHopAS based on Integer32"""
    defaultValue = 0


_RtmRibNextHopAS_Object = MibTableColumn
rtmRibNextHopAS = _RtmRibNextHopAS_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 14),
    _RtmRibNextHopAS_Type()
)
rtmRibNextHopAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibNextHopAS.setStatus("current")


class _RtmRibMetric1_Type(Integer32):
    """Custom type rtmRibMetric1 based on Integer32"""
    defaultValue = -1


_RtmRibMetric1_Object = MibTableColumn
rtmRibMetric1 = _RtmRibMetric1_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 15),
    _RtmRibMetric1_Type()
)
rtmRibMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibMetric1.setStatus("current")


class _RtmRibMetric2_Type(Integer32):
    """Custom type rtmRibMetric2 based on Integer32"""
    defaultValue = -1


_RtmRibMetric2_Object = MibTableColumn
rtmRibMetric2 = _RtmRibMetric2_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 16),
    _RtmRibMetric2_Type()
)
rtmRibMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibMetric2.setStatus("current")


class _RtmRibMetric3_Type(Integer32):
    """Custom type rtmRibMetric3 based on Integer32"""
    defaultValue = -1


_RtmRibMetric3_Object = MibTableColumn
rtmRibMetric3 = _RtmRibMetric3_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 17),
    _RtmRibMetric3_Type()
)
rtmRibMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibMetric3.setStatus("current")


class _RtmRibMetric4_Type(Integer32):
    """Custom type rtmRibMetric4 based on Integer32"""
    defaultValue = -1


_RtmRibMetric4_Object = MibTableColumn
rtmRibMetric4 = _RtmRibMetric4_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 18),
    _RtmRibMetric4_Type()
)
rtmRibMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibMetric4.setStatus("current")


class _RtmRibMetric5_Type(Integer32):
    """Custom type rtmRibMetric5 based on Integer32"""
    defaultValue = -1


_RtmRibMetric5_Object = MibTableColumn
rtmRibMetric5 = _RtmRibMetric5_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 19),
    _RtmRibMetric5_Type()
)
rtmRibMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibMetric5.setStatus("current")
_RtmRibFibRoute_Type = TruthValue
_RtmRibFibRoute_Object = MibTableColumn
rtmRibFibRoute = _RtmRibFibRoute_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 20),
    _RtmRibFibRoute_Type()
)
rtmRibFibRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibFibRoute.setStatus("current")


class _RtmRibRpmIndex_Type(Integer32):
    """Custom type rtmRibRpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmRibRpmIndex_Type.__name__ = "Integer32"
_RtmRibRpmIndex_Object = MibTableColumn
rtmRibRpmIndex = _RtmRibRpmIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 21),
    _RtmRibRpmIndex_Type()
)
rtmRibRpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRibRpmIndex.setStatus("current")
_RtmRibConnected_Type = TruthValue
_RtmRibConnected_Object = MibTableColumn
rtmRibConnected = _RtmRibConnected_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 22),
    _RtmRibConnected_Type()
)
rtmRibConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibConnected.setStatus("current")
_RtmRibLooseNextHop_Type = TruthValue
_RtmRibLooseNextHop_Object = MibTableColumn
rtmRibLooseNextHop = _RtmRibLooseNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 23),
    _RtmRibLooseNextHop_Type()
)
rtmRibLooseNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibLooseNextHop.setStatus("current")


class _RtmRibLocalDestIfIndex_Type(Integer32):
    """Custom type rtmRibLocalDestIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmRibLocalDestIfIndex_Type.__name__ = "Integer32"
_RtmRibLocalDestIfIndex_Object = MibTableColumn
rtmRibLocalDestIfIndex = _RtmRibLocalDestIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 7, 1, 24),
    _RtmRibLocalDestIfIndex_Type()
)
rtmRibLocalDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmRibLocalDestIfIndex.setStatus("current")
_RtmRdstSetFieldTable_Object = MibTable
rtmRdstSetFieldTable = _RtmRdstSetFieldTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 8)
)
if mibBuilder.loadTexts:
    rtmRdstSetFieldTable.setStatus("current")
_RtmRdstSetFieldEntry_Object = MibTableRow
rtmRdstSetFieldEntry = _RtmRdstSetFieldEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 8, 1)
)
rtmRdstSetFieldEntry.setIndexNames(
    (0, "DC-RTM-MIB", "rtmRdstSetFieldFteIndex"),
    (0, "DC-RTM-MIB", "rtmRdstSetFieldListId"),
    (0, "DC-RTM-MIB", "rtmRdstSetFieldNumber"),
)
if mibBuilder.loadTexts:
    rtmRdstSetFieldEntry.setStatus("current")
_RtmRdstSetFieldFteIndex_Type = FteIndex
_RtmRdstSetFieldFteIndex_Object = MibTableColumn
rtmRdstSetFieldFteIndex = _RtmRdstSetFieldFteIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 8, 1, 1),
    _RtmRdstSetFieldFteIndex_Type()
)
rtmRdstSetFieldFteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRdstSetFieldFteIndex.setStatus("current")


class _RtmRdstSetFieldListId_Type(Unsigned32):
    """Custom type rtmRdstSetFieldListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RtmRdstSetFieldListId_Type.__name__ = "Unsigned32"
_RtmRdstSetFieldListId_Object = MibTableColumn
rtmRdstSetFieldListId = _RtmRdstSetFieldListId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 8, 1, 2),
    _RtmRdstSetFieldListId_Type()
)
rtmRdstSetFieldListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRdstSetFieldListId.setStatus("current")


class _RtmRdstSetFieldNumber_Type(Unsigned32):
    """Custom type rtmRdstSetFieldNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RtmRdstSetFieldNumber_Type.__name__ = "Unsigned32"
_RtmRdstSetFieldNumber_Object = MibTableColumn
rtmRdstSetFieldNumber = _RtmRdstSetFieldNumber_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 8, 1, 3),
    _RtmRdstSetFieldNumber_Type()
)
rtmRdstSetFieldNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtmRdstSetFieldNumber.setStatus("current")
_RtmRdstSetFieldRowStatus_Type = RowStatus
_RtmRdstSetFieldRowStatus_Object = MibTableColumn
rtmRdstSetFieldRowStatus = _RtmRdstSetFieldRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 8, 1, 4),
    _RtmRdstSetFieldRowStatus_Type()
)
rtmRdstSetFieldRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRdstSetFieldRowStatus.setStatus("current")
_RtmRdstSetFieldType_Type = RdstSetFieldType
_RtmRdstSetFieldType_Object = MibTableColumn
rtmRdstSetFieldType = _RtmRdstSetFieldType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 8, 1, 5),
    _RtmRdstSetFieldType_Type()
)
rtmRdstSetFieldType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRdstSetFieldType.setStatus("current")


class _RtmRdstSetFieldValue_Type(OctetString):
    """Custom type rtmRdstSetFieldValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_RtmRdstSetFieldValue_Type.__name__ = "OctetString"
_RtmRdstSetFieldValue_Object = MibTableColumn
rtmRdstSetFieldValue = _RtmRdstSetFieldValue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 1, 8, 1, 6),
    _RtmRdstSetFieldValue_Type()
)
rtmRdstSetFieldValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtmRdstSetFieldValue.setStatus("current")
_RtmTrap_ObjectIdentity = ObjectIdentity
rtmTrap = _RtmTrap_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2)
)
_RtmTraps_ObjectIdentity = ObjectIdentity
rtmTraps = _RtmTraps_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 0)
)
_RtmTrapControl_ObjectIdentity = ObjectIdentity
rtmTrapControl = _RtmTrapControl_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1)
)


class _RtmStaticRtTrapReason_Type(Integer32):
    """Custom type rtmStaticRtTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 1),
          ("ineligible", 2))
    )


_RtmStaticRtTrapReason_Type.__name__ = "Integer32"
_RtmStaticRtTrapReason_Object = MibScalar
rtmStaticRtTrapReason = _RtmStaticRtTrapReason_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 1),
    _RtmStaticRtTrapReason_Type()
)
rtmStaticRtTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmStaticRtTrapReason.setStatus("current")


class _RtmPathTrapReason_Type(Integer32):
    """Custom type rtmPathTrapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RtmPathTrapReason_Type.__name__ = "Integer32"
_RtmPathTrapReason_Object = MibScalar
rtmPathTrapReason = _RtmPathTrapReason_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 2),
    _RtmPathTrapReason_Type()
)
rtmPathTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtmPathTrapReason.setStatus("current")
_RtmTrapEntityFteIndex_Type = FteIndex
_RtmTrapEntityFteIndex_Object = MibScalar
rtmTrapEntityFteIndex = _RtmTrapEntityFteIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 3),
    _RtmTrapEntityFteIndex_Type()
)
rtmTrapEntityFteIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapEntityFteIndex.setStatus("current")
_RtmTrapStaticRtDestAddrType_Type = InetAddressType
_RtmTrapStaticRtDestAddrType_Object = MibScalar
rtmTrapStaticRtDestAddrType = _RtmTrapStaticRtDestAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 4),
    _RtmTrapStaticRtDestAddrType_Type()
)
rtmTrapStaticRtDestAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapStaticRtDestAddrType.setStatus("current")


class _RtmTrapStaticRtDestAddr_Type(InetAddress):
    """Custom type rtmTrapStaticRtDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmTrapStaticRtDestAddr_Type.__name__ = "InetAddress"
_RtmTrapStaticRtDestAddr_Object = MibScalar
rtmTrapStaticRtDestAddr = _RtmTrapStaticRtDestAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 5),
    _RtmTrapStaticRtDestAddr_Type()
)
rtmTrapStaticRtDestAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapStaticRtDestAddr.setStatus("current")


class _RtmTrapStaticRtDestLen_Type(Integer32):
    """Custom type rtmTrapStaticRtDestLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RtmTrapStaticRtDestLen_Type.__name__ = "Integer32"
_RtmTrapStaticRtDestLen_Object = MibScalar
rtmTrapStaticRtDestLen = _RtmTrapStaticRtDestLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 6),
    _RtmTrapStaticRtDestLen_Type()
)
rtmTrapStaticRtDestLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapStaticRtDestLen.setStatus("current")
_RtmTrapStaticRtNextHopType_Type = InetAddressType
_RtmTrapStaticRtNextHopType_Object = MibScalar
rtmTrapStaticRtNextHopType = _RtmTrapStaticRtNextHopType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 7),
    _RtmTrapStaticRtNextHopType_Type()
)
rtmTrapStaticRtNextHopType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapStaticRtNextHopType.setStatus("current")


class _RtmTrapStaticRtNextHop_Type(InetAddress):
    """Custom type rtmTrapStaticRtNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmTrapStaticRtNextHop_Type.__name__ = "InetAddress"
_RtmTrapStaticRtNextHop_Object = MibScalar
rtmTrapStaticRtNextHop = _RtmTrapStaticRtNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 8),
    _RtmTrapStaticRtNextHop_Type()
)
rtmTrapStaticRtNextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapStaticRtNextHop.setStatus("current")


class _RtmTrapStaticRtIfIndex_Type(Integer32):
    """Custom type rtmTrapStaticRtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmTrapStaticRtIfIndex_Type.__name__ = "Integer32"
_RtmTrapStaticRtIfIndex_Object = MibScalar
rtmTrapStaticRtIfIndex = _RtmTrapStaticRtIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 9),
    _RtmTrapStaticRtIfIndex_Type()
)
rtmTrapStaticRtIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapStaticRtIfIndex.setStatus("current")
_RtmTrapRibDestType_Type = InetAddressType
_RtmTrapRibDestType_Object = MibScalar
rtmTrapRibDestType = _RtmTrapRibDestType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 10),
    _RtmTrapRibDestType_Type()
)
rtmTrapRibDestType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapRibDestType.setStatus("current")


class _RtmTrapRibDest_Type(InetAddress):
    """Custom type rtmTrapRibDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmTrapRibDest_Type.__name__ = "InetAddress"
_RtmTrapRibDest_Object = MibScalar
rtmTrapRibDest = _RtmTrapRibDest_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 11),
    _RtmTrapRibDest_Type()
)
rtmTrapRibDest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapRibDest.setStatus("current")


class _RtmTrapRibDestLen_Type(Integer32):
    """Custom type rtmTrapRibDestLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RtmTrapRibDestLen_Type.__name__ = "Integer32"
_RtmTrapRibDestLen_Object = MibScalar
rtmTrapRibDestLen = _RtmTrapRibDestLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 12),
    _RtmTrapRibDestLen_Type()
)
rtmTrapRibDestLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapRibDestLen.setStatus("current")


class _RtmTrapRibTos_Type(Integer32):
    """Custom type rtmTrapRibTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RtmTrapRibTos_Type.__name__ = "Integer32"
_RtmTrapRibTos_Object = MibScalar
rtmTrapRibTos = _RtmTrapRibTos_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 13),
    _RtmTrapRibTos_Type()
)
rtmTrapRibTos.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapRibTos.setStatus("current")
_RtmTrapRibNextHopType_Type = InetAddressType
_RtmTrapRibNextHopType_Object = MibScalar
rtmTrapRibNextHopType = _RtmTrapRibNextHopType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 14),
    _RtmTrapRibNextHopType_Type()
)
rtmTrapRibNextHopType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapRibNextHopType.setStatus("current")


class _RtmTrapRibNextHop_Type(InetAddress):
    """Custom type rtmTrapRibNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RtmTrapRibNextHop_Type.__name__ = "InetAddress"
_RtmTrapRibNextHop_Object = MibScalar
rtmTrapRibNextHop = _RtmTrapRibNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 15),
    _RtmTrapRibNextHop_Type()
)
rtmTrapRibNextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapRibNextHop.setStatus("current")


class _RtmTrapRibIfIndex_Type(Integer32):
    """Custom type rtmTrapRibIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmTrapRibIfIndex_Type.__name__ = "Integer32"
_RtmTrapRibIfIndex_Object = MibScalar
rtmTrapRibIfIndex = _RtmTrapRibIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 16),
    _RtmTrapRibIfIndex_Type()
)
rtmTrapRibIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapRibIfIndex.setStatus("current")
_RtmTrapRibProto_Type = IANAipRouteProtocol
_RtmTrapRibProto_Object = MibScalar
rtmTrapRibProto = _RtmTrapRibProto_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 17),
    _RtmTrapRibProto_Type()
)
rtmTrapRibProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapRibProto.setStatus("current")


class _RtmTrapRibRpmIndex_Type(Integer32):
    """Custom type rtmTrapRibRpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RtmTrapRibRpmIndex_Type.__name__ = "Integer32"
_RtmTrapRibRpmIndex_Object = MibScalar
rtmTrapRibRpmIndex = _RtmTrapRibRpmIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 1, 18),
    _RtmTrapRibRpmIndex_Type()
)
rtmTrapRibRpmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rtmTrapRibRpmIndex.setStatus("current")
_RtmConformance_ObjectIdentity = ObjectIdentity
rtmConformance = _RtmConformance_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3)
)
_RtmCompliances_ObjectIdentity = ObjectIdentity
rtmCompliances = _RtmCompliances_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 1)
)
_RtmGroups_ObjectIdentity = ObjectIdentity
rtmGroups = _RtmGroups_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2)
)

# Managed Objects groups

rtmEntityMandatoryGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 1)
)
rtmEntityMandatoryGroup.setObjects(
    ("DC-RTM-MIB", "rtmEntityRowStatus")
)
if mibBuilder.loadTexts:
    rtmEntityMandatoryGroup.setStatus("current")

rtmEntityGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 2)
)
rtmEntityGroup.setObjects(
      *(("DC-RTM-MIB", "rtmEntityAdminStat"),
        ("DC-RTM-MIB", "rtmEntityOperStatus"),
        ("DC-RTM-MIB", "rtmEntityDsConnctd"),
        ("DC-RTM-MIB", "rtmEntityDsStatDf"),
        ("DC-RTM-MIB", "rtmEntityDsOspfInt"),
        ("DC-RTM-MIB", "rtmEntityDsOspfExt"),
        ("DC-RTM-MIB", "rtmEntityDsIntBgp"),
        ("DC-RTM-MIB", "rtmEntityDsExtBgp"),
        ("DC-RTM-MIB", "rtmEntityDsIsisInt1"),
        ("DC-RTM-MIB", "rtmEntityDsIsisInt2"),
        ("DC-RTM-MIB", "rtmEntityDsIsisExt1"),
        ("DC-RTM-MIB", "rtmEntityDsIsisExt2"),
        ("DC-RTM-MIB", "rtmEntityDsRip"),
        ("DC-RTM-MIB", "rtmEntityDsEgp"),
        ("DC-RTM-MIB", "rtmEntityDsPd"),
        ("DC-RTM-MIB", "rtmEntityDsHello"),
        ("DC-RTM-MIB", "rtmEntityDsEsis"),
        ("DC-RTM-MIB", "rtmEntityDsBbnspfigp"),
        ("DC-RTM-MIB", "rtmEntityDsIdpr"),
        ("DC-RTM-MIB", "rtmEntityDsIgrp"),
        ("DC-RTM-MIB", "rtmEntityDsEigrpSmm"),
        ("DC-RTM-MIB", "rtmEntityDsIntEigrp"),
        ("DC-RTM-MIB", "rtmEntityDsEigrpExt"),
        ("DC-RTM-MIB", "rtmEntityDsUnknown"),
        ("DC-RTM-MIB", "rtmEntityEqlCostOpt"),
        ("DC-RTM-MIB", "rtmEntityDelDeadRte"),
        ("DC-RTM-MIB", "rtmEntityDeadRpmTmr"),
        ("DC-RTM-MIB", "rtmEntityRouteNumber"),
        ("DC-RTM-MIB", "rtmEntityAddressFamily"),
        ("DC-RTM-MIB", "rtmEntityDsDvmrp"),
        ("DC-RTM-MIB", "rtmEntityI3Index"),
        ("DC-RTM-MIB", "rtmEntityI3JoinStatus"),
        ("DC-RTM-MIB", "rtmEntityPartnerWaitTime"),
        ("DC-RTM-MIB", "rtmEntityStartupTime"),
        ("DC-RTM-MIB", "rtmEntityRestartTime"),
        ("DC-RTM-MIB", "rtmEntityFtStateRetained"),
        ("DC-RTM-MIB", "rtmEntityUseUnidirectionalLinks"),
        ("DC-RTM-MIB", "rtmEntityBfdIndex"),
        ("DC-RTM-MIB", "rtmEntityBfdJoinStatus"),
        ("DC-RTM-MIB", "rtmEntityEnableTrapSupport"))
)
if mibBuilder.loadTexts:
    rtmEntityGroup.setStatus("current")

rtmRedistMandatoryGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 3)
)
rtmRedistMandatoryGroup.setObjects(
    ("DC-RTM-MIB", "rtmRedistRowStatus")
)
if mibBuilder.loadTexts:
    rtmRedistMandatoryGroup.setStatus("current")

rtmRedistGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 4)
)
rtmRedistGroup.setObjects(
      *(("DC-RTM-MIB", "rtmRedistAdminStat"),
        ("DC-RTM-MIB", "rtmRedistPriority"),
        ("DC-RTM-MIB", "rtmRedistInfoSrc"),
        ("DC-RTM-MIB", "rtmRedistSrcInstFlt"),
        ("DC-RTM-MIB", "rtmRedistSrcInst"),
        ("DC-RTM-MIB", "rtmRedistInfoDest"),
        ("DC-RTM-MIB", "rtmRedistDestInstFlt"),
        ("DC-RTM-MIB", "rtmRedistDestInst"),
        ("DC-RTM-MIB", "rtmRedistAddrFilterType"),
        ("DC-RTM-MIB", "rtmRedistAddrFilter"),
        ("DC-RTM-MIB", "rtmRedistAddrFltLen"),
        ("DC-RTM-MIB", "rtmRedistHopFltValType"),
        ("DC-RTM-MIB", "rtmRedistHopFltVal"),
        ("DC-RTM-MIB", "rtmRedistHopFltLen"),
        ("DC-RTM-MIB", "rtmRedistIfIndexFlt"),
        ("DC-RTM-MIB", "rtmRedistIfIndex"),
        ("DC-RTM-MIB", "rtmRedistPathTypeFlt"),
        ("DC-RTM-MIB", "rtmRedistPathType"),
        ("DC-RTM-MIB", "rtmRedistOspfAreaFlt"),
        ("DC-RTM-MIB", "rtmRedistOspfArea"),
        ("DC-RTM-MIB", "rtmRedistOspfTagFlt"),
        ("DC-RTM-MIB", "rtmRedistOspfTag"),
        ("DC-RTM-MIB", "rtmRedistCommunityFlt"),
        ("DC-RTM-MIB", "rtmRedistCommunity"),
        ("DC-RTM-MIB", "rtmRedistExtCommFlt"),
        ("DC-RTM-MIB", "rtmRedistExtComm"),
        ("DC-RTM-MIB", "rtmRedistRedistFlag"),
        ("DC-RTM-MIB", "rtmRedistMetricConv"),
        ("DC-RTM-MIB", "rtmRedistMetricValue"),
        ("DC-RTM-MIB", "rtmRedistNwPathType"),
        ("DC-RTM-MIB", "rtmRedistNwOspfTag"),
        ("DC-RTM-MIB", "rtmRedistOspfPropagate"),
        ("DC-RTM-MIB", "rtmRedistNwOrigin"),
        ("DC-RTM-MIB", "rtmRedistAddMed"),
        ("DC-RTM-MIB", "rtmRedistNwMed"),
        ("DC-RTM-MIB", "rtmRedistAddLocalPref"),
        ("DC-RTM-MIB", "rtmRedistNwLocalPref"),
        ("DC-RTM-MIB", "rtmRedistSetListId"),
        ("DC-RTM-MIB", "rtmRedistAddAsLimUpper"),
        ("DC-RTM-MIB", "rtmRedistNwAsLimUpper"),
        ("DC-RTM-MIB", "rtmRedistOspfVpnPeCeSupport"))
)
if mibBuilder.loadTexts:
    rtmRedistGroup.setStatus("current")

rtmStaticRtMandatoryGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 5)
)
rtmStaticRtMandatoryGroup.setObjects(
    ("DC-RTM-MIB", "rtmStaticRtRowStatus")
)
if mibBuilder.loadTexts:
    rtmStaticRtMandatoryGroup.setStatus("current")

rtmStaticRtGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 6)
)
rtmStaticRtGroup.setObjects(
      *(("DC-RTM-MIB", "rtmStaticRtAdminStat"),
        ("DC-RTM-MIB", "rtmStaticRtOverride"),
        ("DC-RTM-MIB", "rtmStaticRtAdminDist"),
        ("DC-RTM-MIB", "rtmStaticRtAction"),
        ("DC-RTM-MIB", "rtmStaticRtFwdAddrType"),
        ("DC-RTM-MIB", "rtmStaticRtForwardingAddr"),
        ("DC-RTM-MIB", "rtmStaticRtUsePathCost"),
        ("DC-RTM-MIB", "rtmStaticRtPathCost"),
        ("DC-RTM-MIB", "rtmStaticRtUserData"),
        ("DC-RTM-MIB", "rtmStaticRtLooseNextHop"),
        ("DC-RTM-MIB", "rtmStaticRtBfdSupport"),
        ("DC-RTM-MIB", "rtmStaticRtBfdStatus"))
)
if mibBuilder.loadTexts:
    rtmStaticRtGroup.setStatus("current")

rtmMjMandatoryGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 7)
)
rtmMjMandatoryGroup.setObjects(
    ("DC-RTM-MIB", "rtmMjRowStatus")
)
if mibBuilder.loadTexts:
    rtmMjMandatoryGroup.setStatus("current")

rtmMjGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 8)
)
rtmMjGroup.setObjects(
      *(("DC-RTM-MIB", "rtmMjIfType"),
        ("DC-RTM-MIB", "rtmMjAdminStatus"),
        ("DC-RTM-MIB", "rtmMjOperStatus"),
        ("DC-RTM-MIB", "rtmMjJoinStatus"),
        ("DC-RTM-MIB", "rtmMjSafi"))
)
if mibBuilder.loadTexts:
    rtmMjGroup.setStatus("current")

rtmSjMandatoryGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 9)
)
rtmSjMandatoryGroup.setObjects(
      *(("DC-RTM-MIB", "rtmSjIfType"),
        ("DC-RTM-MIB", "rtmSjMastFteType"),
        ("DC-RTM-MIB", "rtmSjMastFteId"))
)
if mibBuilder.loadTexts:
    rtmSjMandatoryGroup.setStatus("current")

rtmSjGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 10)
)
rtmSjGroup.setObjects(
    ("DC-RTM-MIB", "rtmSjJoinStatus")
)
if mibBuilder.loadTexts:
    rtmSjGroup.setStatus("current")

rtmRouteGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 11)
)
rtmRouteGroup.setObjects(
      *(("DC-RTM-MIB", "rtmRouteStatus"),
        ("DC-RTM-MIB", "rtmRouteType"),
        ("DC-RTM-MIB", "rtmRouteProto"),
        ("DC-RTM-MIB", "rtmRouteAge"),
        ("DC-RTM-MIB", "rtmRouteInfo"),
        ("DC-RTM-MIB", "rtmRouteNextHopAS"),
        ("DC-RTM-MIB", "rtmRouteMetric1"),
        ("DC-RTM-MIB", "rtmRouteMetric2"),
        ("DC-RTM-MIB", "rtmRouteMetric3"),
        ("DC-RTM-MIB", "rtmRouteMetric4"),
        ("DC-RTM-MIB", "rtmRouteMetric5"),
        ("DC-RTM-MIB", "rtmRouteConnected"),
        ("DC-RTM-MIB", "rtmRouteXCIndex"),
        ("DC-RTM-MIB", "rtmRouteLocalDestIfIndex"))
)
if mibBuilder.loadTexts:
    rtmRouteGroup.setStatus("current")

rtmRibGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 12)
)
rtmRibGroup.setObjects(
      *(("DC-RTM-MIB", "rtmRibStatus"),
        ("DC-RTM-MIB", "rtmRibType"),
        ("DC-RTM-MIB", "rtmRibAge"),
        ("DC-RTM-MIB", "rtmRibInfo"),
        ("DC-RTM-MIB", "rtmRibNextHopAS"),
        ("DC-RTM-MIB", "rtmRibMetric1"),
        ("DC-RTM-MIB", "rtmRibMetric2"),
        ("DC-RTM-MIB", "rtmRibMetric3"),
        ("DC-RTM-MIB", "rtmRibMetric4"),
        ("DC-RTM-MIB", "rtmRibMetric5"),
        ("DC-RTM-MIB", "rtmRibFibRoute"),
        ("DC-RTM-MIB", "rtmRibConnected"),
        ("DC-RTM-MIB", "rtmRibLooseNextHop"),
        ("DC-RTM-MIB", "rtmRibLocalDestIfIndex"))
)
if mibBuilder.loadTexts:
    rtmRibGroup.setStatus("current")

rtmObsoleteGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 13)
)
rtmObsoleteGroup.setObjects(
      *(("DC-RTM-MIB", "rtmRedistAddCommunity"),
        ("DC-RTM-MIB", "rtmRedistNwCommunity"),
        ("DC-RTM-MIB", "rtmRedistAddExtComm"),
        ("DC-RTM-MIB", "rtmRedistNwExtComm"))
)
if mibBuilder.loadTexts:
    rtmObsoleteGroup.setStatus("obsolete")

rtmRdstSetFieldMandatoryGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 14)
)
rtmRdstSetFieldMandatoryGroup.setObjects(
      *(("DC-RTM-MIB", "rtmRdstSetFieldRowStatus"),
        ("DC-RTM-MIB", "rtmRdstSetFieldType"),
        ("DC-RTM-MIB", "rtmRdstSetFieldValue"))
)
if mibBuilder.loadTexts:
    rtmRdstSetFieldMandatoryGroup.setStatus("current")

rtmNotificationObjectGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 15)
)
rtmNotificationObjectGroup.setObjects(
      *(("DC-RTM-MIB", "rtmStaticRtTrapReason"),
        ("DC-RTM-MIB", "rtmPathTrapReason"),
        ("DC-RTM-MIB", "rtmTrapEntityFteIndex"),
        ("DC-RTM-MIB", "rtmTrapStaticRtDestAddrType"),
        ("DC-RTM-MIB", "rtmTrapStaticRtDestAddr"),
        ("DC-RTM-MIB", "rtmTrapStaticRtDestLen"),
        ("DC-RTM-MIB", "rtmTrapStaticRtNextHopType"),
        ("DC-RTM-MIB", "rtmTrapStaticRtNextHop"),
        ("DC-RTM-MIB", "rtmTrapStaticRtIfIndex"),
        ("DC-RTM-MIB", "rtmTrapRibDestType"),
        ("DC-RTM-MIB", "rtmTrapRibDest"),
        ("DC-RTM-MIB", "rtmTrapRibDestLen"),
        ("DC-RTM-MIB", "rtmTrapRibTos"),
        ("DC-RTM-MIB", "rtmTrapRibNextHopType"),
        ("DC-RTM-MIB", "rtmTrapRibNextHop"),
        ("DC-RTM-MIB", "rtmTrapRibIfIndex"),
        ("DC-RTM-MIB", "rtmTrapRibProto"),
        ("DC-RTM-MIB", "rtmTrapRibRpmIndex"))
)
if mibBuilder.loadTexts:
    rtmNotificationObjectGroup.setStatus("current")


# Notification objects

rtmOperStateChange = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 0, 1)
)
rtmOperStateChange.setObjects(
      *(("DC-RTM-MIB", "rtmTrapEntityFteIndex"),
        ("DC-RTM-MIB", "rtmEntityOperStatus"))
)
if mibBuilder.loadTexts:
    rtmOperStateChange.setStatus(
        "current"
    )

rtmStaticRouteChange = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 0, 2)
)
rtmStaticRouteChange.setObjects(
      *(("DC-RTM-MIB", "rtmTrapEntityFteIndex"),
        ("DC-RTM-MIB", "rtmTrapStaticRtDestAddrType"),
        ("DC-RTM-MIB", "rtmTrapStaticRtDestAddr"),
        ("DC-RTM-MIB", "rtmTrapStaticRtDestLen"),
        ("DC-RTM-MIB", "rtmTrapStaticRtNextHopType"),
        ("DC-RTM-MIB", "rtmTrapStaticRtNextHop"),
        ("DC-RTM-MIB", "rtmTrapStaticRtIfIndex"),
        ("DC-RTM-MIB", "rtmStaticRtTrapReason"),
        ("DC-RTM-MIB", "rtmStaticRtBfdSupport"),
        ("DC-RTM-MIB", "rtmStaticRtBfdStatus"))
)
if mibBuilder.loadTexts:
    rtmStaticRouteChange.setStatus(
        "current"
    )

rtmPathActivityChange = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 2, 0, 3)
)
rtmPathActivityChange.setObjects(
      *(("DC-RTM-MIB", "rtmTrapEntityFteIndex"),
        ("DC-RTM-MIB", "rtmTrapRibDestType"),
        ("DC-RTM-MIB", "rtmTrapRibDest"),
        ("DC-RTM-MIB", "rtmTrapRibDestLen"),
        ("DC-RTM-MIB", "rtmTrapRibTos"),
        ("DC-RTM-MIB", "rtmTrapRibNextHopType"),
        ("DC-RTM-MIB", "rtmTrapRibNextHop"),
        ("DC-RTM-MIB", "rtmTrapRibIfIndex"),
        ("DC-RTM-MIB", "rtmTrapRibProto"),
        ("DC-RTM-MIB", "rtmTrapRibRpmIndex"),
        ("DC-RTM-MIB", "rtmPathTrapReason"))
)
if mibBuilder.loadTexts:
    rtmPathActivityChange.setStatus(
        "current"
    )


# Notifications groups

rtmNotificationEventGroup = NotificationGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 2, 16)
)
rtmNotificationEventGroup.setObjects(
      *(("DC-RTM-MIB", "rtmOperStateChange"),
        ("DC-RTM-MIB", "rtmStaticRouteChange"),
        ("DC-RTM-MIB", "rtmPathActivityChange"))
)
if mibBuilder.loadTexts:
    rtmNotificationEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rtmCompliance = ModuleCompliance(
    (1, 2, 826, 0, 1, 1578918, 5, 61, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-RTM-MIB",
    **{"MplsIndexType": MplsIndexType,
       "FteIndex": FteIndex,
       "OspfTag": OspfTag,
       "RtmMjStatus": RtmMjStatus,
       "RtmSjStatus": RtmSjStatus,
       "InterfaceType": InterfaceType,
       "AriPrtnrType": AriPrtnrType,
       "RdstSetFieldType": RdstSetFieldType,
       "EqualCostRouteOpts": EqualCostRouteOpts,
       "MetricConversion": MetricConversion,
       "InfoSourceDest": InfoSourceDest,
       "BgpOriginCode": BgpOriginCode,
       "BgpCommunity": BgpCommunity,
       "BgpExtendedCommunity": BgpExtendedCommunity,
       "RouteInfo": RouteInfo,
       "RouteType": RouteType,
       "RtmBfdSupport": RtmBfdSupport,
       "rtmMib": rtmMib,
       "rtmObjects": rtmObjects,
       "rtmEntityTable": rtmEntityTable,
       "rtmEntityEntry": rtmEntityEntry,
       "rtmEntityFteIndex": rtmEntityFteIndex,
       "rtmEntityRowStatus": rtmEntityRowStatus,
       "rtmEntityAdminStat": rtmEntityAdminStat,
       "rtmEntityOperStatus": rtmEntityOperStatus,
       "rtmEntityDsConnctd": rtmEntityDsConnctd,
       "rtmEntityDsStatDf": rtmEntityDsStatDf,
       "rtmEntityDsOspfInt": rtmEntityDsOspfInt,
       "rtmEntityDsOspfExt": rtmEntityDsOspfExt,
       "rtmEntityDsIntBgp": rtmEntityDsIntBgp,
       "rtmEntityDsExtBgp": rtmEntityDsExtBgp,
       "rtmEntityDsIsisInt1": rtmEntityDsIsisInt1,
       "rtmEntityDsIsisInt2": rtmEntityDsIsisInt2,
       "rtmEntityDsIsisExt1": rtmEntityDsIsisExt1,
       "rtmEntityDsIsisExt2": rtmEntityDsIsisExt2,
       "rtmEntityDsRip": rtmEntityDsRip,
       "rtmEntityDsEgp": rtmEntityDsEgp,
       "rtmEntityDsPd": rtmEntityDsPd,
       "rtmEntityDsHello": rtmEntityDsHello,
       "rtmEntityDsEsis": rtmEntityDsEsis,
       "rtmEntityDsBbnspfigp": rtmEntityDsBbnspfigp,
       "rtmEntityDsIdpr": rtmEntityDsIdpr,
       "rtmEntityDsIgrp": rtmEntityDsIgrp,
       "rtmEntityDsEigrpSmm": rtmEntityDsEigrpSmm,
       "rtmEntityDsIntEigrp": rtmEntityDsIntEigrp,
       "rtmEntityDsEigrpExt": rtmEntityDsEigrpExt,
       "rtmEntityDsUnknown": rtmEntityDsUnknown,
       "rtmEntityEqlCostOpt": rtmEntityEqlCostOpt,
       "rtmEntityDelDeadRte": rtmEntityDelDeadRte,
       "rtmEntityDeadRpmTmr": rtmEntityDeadRpmTmr,
       "rtmEntityRouteNumber": rtmEntityRouteNumber,
       "rtmEntityAddressFamily": rtmEntityAddressFamily,
       "rtmEntityDsDvmrp": rtmEntityDsDvmrp,
       "rtmEntityI3Index": rtmEntityI3Index,
       "rtmEntityI3JoinStatus": rtmEntityI3JoinStatus,
       "rtmEntityPartnerWaitTime": rtmEntityPartnerWaitTime,
       "rtmEntityStartupTime": rtmEntityStartupTime,
       "rtmEntityRestartTime": rtmEntityRestartTime,
       "rtmEntityFtStateRetained": rtmEntityFtStateRetained,
       "rtmEntityUseUnidirectionalLinks": rtmEntityUseUnidirectionalLinks,
       "rtmEntityBfdIndex": rtmEntityBfdIndex,
       "rtmEntityBfdJoinStatus": rtmEntityBfdJoinStatus,
       "rtmEntityEnableTrapSupport": rtmEntityEnableTrapSupport,
       "rtmRedistTable": rtmRedistTable,
       "rtmRedistEntry": rtmRedistEntry,
       "rtmRedistFteIndex": rtmRedistFteIndex,
       "rtmRedistEntryId": rtmRedistEntryId,
       "rtmRedistRowStatus": rtmRedistRowStatus,
       "rtmRedistAdminStat": rtmRedistAdminStat,
       "rtmRedistPriority": rtmRedistPriority,
       "rtmRedistInfoSrc": rtmRedistInfoSrc,
       "rtmRedistSrcInstFlt": rtmRedistSrcInstFlt,
       "rtmRedistSrcInst": rtmRedistSrcInst,
       "rtmRedistInfoDest": rtmRedistInfoDest,
       "rtmRedistDestInstFlt": rtmRedistDestInstFlt,
       "rtmRedistDestInst": rtmRedistDestInst,
       "rtmRedistAddrFilterType": rtmRedistAddrFilterType,
       "rtmRedistAddrFilter": rtmRedistAddrFilter,
       "rtmRedistAddrFltLen": rtmRedistAddrFltLen,
       "rtmRedistHopFltValType": rtmRedistHopFltValType,
       "rtmRedistHopFltVal": rtmRedistHopFltVal,
       "rtmRedistHopFltLen": rtmRedistHopFltLen,
       "rtmRedistIfIndexFlt": rtmRedistIfIndexFlt,
       "rtmRedistIfIndex": rtmRedistIfIndex,
       "rtmRedistPathTypeFlt": rtmRedistPathTypeFlt,
       "rtmRedistPathType": rtmRedistPathType,
       "rtmRedistOspfAreaFlt": rtmRedistOspfAreaFlt,
       "rtmRedistOspfArea": rtmRedistOspfArea,
       "rtmRedistOspfTagFlt": rtmRedistOspfTagFlt,
       "rtmRedistOspfTag": rtmRedistOspfTag,
       "rtmRedistCommunityFlt": rtmRedistCommunityFlt,
       "rtmRedistCommunity": rtmRedistCommunity,
       "rtmRedistExtCommFlt": rtmRedistExtCommFlt,
       "rtmRedistExtComm": rtmRedistExtComm,
       "rtmRedistRedistFlag": rtmRedistRedistFlag,
       "rtmRedistMetricConv": rtmRedistMetricConv,
       "rtmRedistMetricValue": rtmRedistMetricValue,
       "rtmRedistNwPathType": rtmRedistNwPathType,
       "rtmRedistNwOspfTag": rtmRedistNwOspfTag,
       "rtmRedistOspfPropagate": rtmRedistOspfPropagate,
       "rtmRedistAddCommunity": rtmRedistAddCommunity,
       "rtmRedistNwCommunity": rtmRedistNwCommunity,
       "rtmRedistAddExtComm": rtmRedistAddExtComm,
       "rtmRedistNwExtComm": rtmRedistNwExtComm,
       "rtmRedistNwOrigin": rtmRedistNwOrigin,
       "rtmRedistAddMed": rtmRedistAddMed,
       "rtmRedistNwMed": rtmRedistNwMed,
       "rtmRedistAddLocalPref": rtmRedistAddLocalPref,
       "rtmRedistNwLocalPref": rtmRedistNwLocalPref,
       "rtmRedistSetListId": rtmRedistSetListId,
       "rtmRedistAddAsLimUpper": rtmRedistAddAsLimUpper,
       "rtmRedistNwAsLimUpper": rtmRedistNwAsLimUpper,
       "rtmRedistOspfVpnPeCeSupport": rtmRedistOspfVpnPeCeSupport,
       "rtmStaticRtTable": rtmStaticRtTable,
       "rtmStaticRtEntry": rtmStaticRtEntry,
       "rtmStaticRtFteIndex": rtmStaticRtFteIndex,
       "rtmStaticRtDestAddrType": rtmStaticRtDestAddrType,
       "rtmStaticRtDestAddr": rtmStaticRtDestAddr,
       "rtmStaticRtDestLen": rtmStaticRtDestLen,
       "rtmStaticRtNextHopType": rtmStaticRtNextHopType,
       "rtmStaticRtNextHop": rtmStaticRtNextHop,
       "rtmStaticRtIfIndex": rtmStaticRtIfIndex,
       "rtmStaticRtOutIfIndex": rtmStaticRtOutIfIndex,
       "rtmStaticRtRowStatus": rtmStaticRtRowStatus,
       "rtmStaticRtAdminStat": rtmStaticRtAdminStat,
       "rtmStaticRtOverride": rtmStaticRtOverride,
       "rtmStaticRtAdminDist": rtmStaticRtAdminDist,
       "rtmStaticRtAction": rtmStaticRtAction,
       "rtmStaticRtFwdAddrType": rtmStaticRtFwdAddrType,
       "rtmStaticRtForwardingAddr": rtmStaticRtForwardingAddr,
       "rtmStaticRtPathType": rtmStaticRtPathType,
       "rtmStaticRtUsePathCost": rtmStaticRtUsePathCost,
       "rtmStaticRtPathCost": rtmStaticRtPathCost,
       "rtmStaticRtUserData": rtmStaticRtUserData,
       "rtmStaticRtLooseNextHop": rtmStaticRtLooseNextHop,
       "rtmStaticRtBfdSupport": rtmStaticRtBfdSupport,
       "rtmStaticRtBfdStatus": rtmStaticRtBfdStatus,
       "rtmMjTable": rtmMjTable,
       "rtmMjEntry": rtmMjEntry,
       "rtmMjRtmFteIndex": rtmMjRtmFteIndex,
       "rtmMjSlaveFteId": rtmMjSlaveFteId,
       "rtmMjIfType": rtmMjIfType,
       "rtmMjRowStatus": rtmMjRowStatus,
       "rtmMjAdminStatus": rtmMjAdminStatus,
       "rtmMjOperStatus": rtmMjOperStatus,
       "rtmMjJoinStatus": rtmMjJoinStatus,
       "rtmMjSlaveType": rtmMjSlaveType,
       "rtmMjSafi": rtmMjSafi,
       "rtmSjTable": rtmSjTable,
       "rtmSjEntry": rtmSjEntry,
       "rtmSjRtmFteIndex": rtmSjRtmFteIndex,
       "rtmSjRtmRpmIndex": rtmSjRtmRpmIndex,
       "rtmSjIfType": rtmSjIfType,
       "rtmSjMastFteType": rtmSjMastFteType,
       "rtmSjMastFteId": rtmSjMastFteId,
       "rtmSjJoinStatus": rtmSjJoinStatus,
       "rtmRouteTable": rtmRouteTable,
       "rtmRouteEntry": rtmRouteEntry,
       "rtmRouteFteIndex": rtmRouteFteIndex,
       "rtmRouteStatus": rtmRouteStatus,
       "rtmRouteDestType": rtmRouteDestType,
       "rtmRouteDest": rtmRouteDest,
       "rtmRouteDestLen": rtmRouteDestLen,
       "rtmRouteTos": rtmRouteTos,
       "rtmRouteNextHopType": rtmRouteNextHopType,
       "rtmRouteNextHop": rtmRouteNextHop,
       "rtmRouteIfIndex": rtmRouteIfIndex,
       "rtmRouteType": rtmRouteType,
       "rtmRouteProto": rtmRouteProto,
       "rtmRouteAge": rtmRouteAge,
       "rtmRouteInfo": rtmRouteInfo,
       "rtmRouteNextHopAS": rtmRouteNextHopAS,
       "rtmRouteMetric1": rtmRouteMetric1,
       "rtmRouteMetric2": rtmRouteMetric2,
       "rtmRouteMetric3": rtmRouteMetric3,
       "rtmRouteMetric4": rtmRouteMetric4,
       "rtmRouteMetric5": rtmRouteMetric5,
       "rtmRouteConnected": rtmRouteConnected,
       "rtmRouteXCIndex": rtmRouteXCIndex,
       "rtmRouteLocalDestIfIndex": rtmRouteLocalDestIfIndex,
       "rtmRibTable": rtmRibTable,
       "rtmRibEntry": rtmRibEntry,
       "rtmRibFteIndex": rtmRibFteIndex,
       "rtmRibStatus": rtmRibStatus,
       "rtmRibDestType": rtmRibDestType,
       "rtmRibDest": rtmRibDest,
       "rtmRibDestLen": rtmRibDestLen,
       "rtmRibTos": rtmRibTos,
       "rtmRibNextHopType": rtmRibNextHopType,
       "rtmRibNextHop": rtmRibNextHop,
       "rtmRibIfIndex": rtmRibIfIndex,
       "rtmRibType": rtmRibType,
       "rtmRibProto": rtmRibProto,
       "rtmRibAge": rtmRibAge,
       "rtmRibInfo": rtmRibInfo,
       "rtmRibNextHopAS": rtmRibNextHopAS,
       "rtmRibMetric1": rtmRibMetric1,
       "rtmRibMetric2": rtmRibMetric2,
       "rtmRibMetric3": rtmRibMetric3,
       "rtmRibMetric4": rtmRibMetric4,
       "rtmRibMetric5": rtmRibMetric5,
       "rtmRibFibRoute": rtmRibFibRoute,
       "rtmRibRpmIndex": rtmRibRpmIndex,
       "rtmRibConnected": rtmRibConnected,
       "rtmRibLooseNextHop": rtmRibLooseNextHop,
       "rtmRibLocalDestIfIndex": rtmRibLocalDestIfIndex,
       "rtmRdstSetFieldTable": rtmRdstSetFieldTable,
       "rtmRdstSetFieldEntry": rtmRdstSetFieldEntry,
       "rtmRdstSetFieldFteIndex": rtmRdstSetFieldFteIndex,
       "rtmRdstSetFieldListId": rtmRdstSetFieldListId,
       "rtmRdstSetFieldNumber": rtmRdstSetFieldNumber,
       "rtmRdstSetFieldRowStatus": rtmRdstSetFieldRowStatus,
       "rtmRdstSetFieldType": rtmRdstSetFieldType,
       "rtmRdstSetFieldValue": rtmRdstSetFieldValue,
       "rtmTrap": rtmTrap,
       "rtmTraps": rtmTraps,
       "rtmOperStateChange": rtmOperStateChange,
       "rtmStaticRouteChange": rtmStaticRouteChange,
       "rtmPathActivityChange": rtmPathActivityChange,
       "rtmTrapControl": rtmTrapControl,
       "rtmStaticRtTrapReason": rtmStaticRtTrapReason,
       "rtmPathTrapReason": rtmPathTrapReason,
       "rtmTrapEntityFteIndex": rtmTrapEntityFteIndex,
       "rtmTrapStaticRtDestAddrType": rtmTrapStaticRtDestAddrType,
       "rtmTrapStaticRtDestAddr": rtmTrapStaticRtDestAddr,
       "rtmTrapStaticRtDestLen": rtmTrapStaticRtDestLen,
       "rtmTrapStaticRtNextHopType": rtmTrapStaticRtNextHopType,
       "rtmTrapStaticRtNextHop": rtmTrapStaticRtNextHop,
       "rtmTrapStaticRtIfIndex": rtmTrapStaticRtIfIndex,
       "rtmTrapRibDestType": rtmTrapRibDestType,
       "rtmTrapRibDest": rtmTrapRibDest,
       "rtmTrapRibDestLen": rtmTrapRibDestLen,
       "rtmTrapRibTos": rtmTrapRibTos,
       "rtmTrapRibNextHopType": rtmTrapRibNextHopType,
       "rtmTrapRibNextHop": rtmTrapRibNextHop,
       "rtmTrapRibIfIndex": rtmTrapRibIfIndex,
       "rtmTrapRibProto": rtmTrapRibProto,
       "rtmTrapRibRpmIndex": rtmTrapRibRpmIndex,
       "rtmConformance": rtmConformance,
       "rtmCompliances": rtmCompliances,
       "rtmCompliance": rtmCompliance,
       "rtmGroups": rtmGroups,
       "rtmEntityMandatoryGroup": rtmEntityMandatoryGroup,
       "rtmEntityGroup": rtmEntityGroup,
       "rtmRedistMandatoryGroup": rtmRedistMandatoryGroup,
       "rtmRedistGroup": rtmRedistGroup,
       "rtmStaticRtMandatoryGroup": rtmStaticRtMandatoryGroup,
       "rtmStaticRtGroup": rtmStaticRtGroup,
       "rtmMjMandatoryGroup": rtmMjMandatoryGroup,
       "rtmMjGroup": rtmMjGroup,
       "rtmSjMandatoryGroup": rtmSjMandatoryGroup,
       "rtmSjGroup": rtmSjGroup,
       "rtmRouteGroup": rtmRouteGroup,
       "rtmRibGroup": rtmRibGroup,
       "rtmObsoleteGroup": rtmObsoleteGroup,
       "rtmRdstSetFieldMandatoryGroup": rtmRdstSetFieldMandatoryGroup,
       "rtmNotificationObjectGroup": rtmNotificationObjectGroup,
       "rtmNotificationEventGroup": rtmNotificationEventGroup}
)
