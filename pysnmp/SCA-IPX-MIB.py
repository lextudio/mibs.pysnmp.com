# SNMP MIB module (SCA-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCA-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:53 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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

_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 25)
)
_IpxCounters_ObjectIdentity = ObjectIdentity
ipxCounters = _IpxCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 25, 1)
)
_IpxCntTxTotal_Type = Counter32
_IpxCntTxTotal_Object = MibScalar
ipxCntTxTotal = _IpxCntTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 1),
    _IpxCntTxTotal_Type()
)
ipxCntTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxTotal.setStatus("mandatory")
_IpxCntTxMcast_Type = Counter32
_IpxCntTxMcast_Object = MibScalar
ipxCntTxMcast = _IpxCntTxMcast_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 2),
    _IpxCntTxMcast_Type()
)
ipxCntTxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxMcast.setStatus("mandatory")
_IpxCntTxBcast_Type = Counter32
_IpxCntTxBcast_Object = MibScalar
ipxCntTxBcast = _IpxCntTxBcast_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 3),
    _IpxCntTxBcast_Type()
)
ipxCntTxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxBcast.setStatus("mandatory")
_IpxCntRxTotal_Type = Counter32
_IpxCntRxTotal_Object = MibScalar
ipxCntRxTotal = _IpxCntRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 4),
    _IpxCntRxTotal_Type()
)
ipxCntRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntRxTotal.setStatus("mandatory")
_IpxCntRxMcast_Type = Counter32
_IpxCntRxMcast_Object = MibScalar
ipxCntRxMcast = _IpxCntRxMcast_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 5),
    _IpxCntRxMcast_Type()
)
ipxCntRxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntRxMcast.setStatus("mandatory")
_IpxCntRxBcast_Type = Counter32
_IpxCntRxBcast_Object = MibScalar
ipxCntRxBcast = _IpxCntRxBcast_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 6),
    _IpxCntRxBcast_Type()
)
ipxCntRxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntRxBcast.setStatus("mandatory")
_IpxCntForward_Type = Counter32
_IpxCntForward_Object = MibScalar
ipxCntForward = _IpxCntForward_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 7),
    _IpxCntForward_Type()
)
ipxCntForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntForward.setStatus("mandatory")
_IpxCntFiltered_Type = Counter32
_IpxCntFiltered_Object = MibScalar
ipxCntFiltered = _IpxCntFiltered_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 8),
    _IpxCntFiltered_Type()
)
ipxCntFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntFiltered.setStatus("mandatory")
_IpxCntLocal_Type = Counter32
_IpxCntLocal_Object = MibScalar
ipxCntLocal = _IpxCntLocal_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 9),
    _IpxCntLocal_Type()
)
ipxCntLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntLocal.setStatus("mandatory")
_IpxCntUnknown_Type = Counter32
_IpxCntUnknown_Object = MibScalar
ipxCntUnknown = _IpxCntUnknown_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 10),
    _IpxCntUnknown_Type()
)
ipxCntUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntUnknown.setStatus("mandatory")
_IpxCntDiscarded_Type = Counter32
_IpxCntDiscarded_Object = MibScalar
ipxCntDiscarded = _IpxCntDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 11),
    _IpxCntDiscarded_Type()
)
ipxCntDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntDiscarded.setStatus("mandatory")
_IpxCntBadChksum_Type = Counter32
_IpxCntBadChksum_Object = MibScalar
ipxCntBadChksum = _IpxCntBadChksum_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 12),
    _IpxCntBadChksum_Type()
)
ipxCntBadChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntBadChksum.setStatus("mandatory")
_IpxCntBadLen_Type = Counter32
_IpxCntBadLen_Object = MibScalar
ipxCntBadLen = _IpxCntBadLen_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 13),
    _IpxCntBadLen_Type()
)
ipxCntBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntBadLen.setStatus("mandatory")
_IpxCntBadHop_Type = Counter32
_IpxCntBadHop_Object = MibScalar
ipxCntBadHop = _IpxCntBadHop_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 14),
    _IpxCntBadHop_Type()
)
ipxCntBadHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntBadHop.setStatus("mandatory")
_IpxCntNoRoute_Type = Counter32
_IpxCntNoRoute_Object = MibScalar
ipxCntNoRoute = _IpxCntNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 15),
    _IpxCntNoRoute_Type()
)
ipxCntNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntNoRoute.setStatus("mandatory")
_IpxCntTooBig_Type = Counter32
_IpxCntTooBig_Object = MibScalar
ipxCntTooBig = _IpxCntTooBig_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 16),
    _IpxCntTooBig_Type()
)
ipxCntTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTooBig.setStatus("mandatory")
_IpxCntRxSapReq_Type = Counter32
_IpxCntRxSapReq_Object = MibScalar
ipxCntRxSapReq = _IpxCntRxSapReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 17),
    _IpxCntRxSapReq_Type()
)
ipxCntRxSapReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntRxSapReq.setStatus("mandatory")
_IpxRxCntSapRsp_Type = Counter32
_IpxRxCntSapRsp_Object = MibScalar
ipxRxCntSapRsp = _IpxRxCntSapRsp_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 18),
    _IpxRxCntSapRsp_Type()
)
ipxRxCntSapRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRxCntSapRsp.setStatus("mandatory")
_IpxTxCntSapReq_Type = Counter32
_IpxTxCntSapReq_Object = MibScalar
ipxTxCntSapReq = _IpxTxCntSapReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 19),
    _IpxTxCntSapReq_Type()
)
ipxTxCntSapReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxTxCntSapReq.setStatus("mandatory")
_IpxCntTxSapRpl_Type = Counter32
_IpxCntTxSapRpl_Object = MibScalar
ipxCntTxSapRpl = _IpxCntTxSapRpl_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 20),
    _IpxCntTxSapRpl_Type()
)
ipxCntTxSapRpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxSapRpl.setStatus("mandatory")
_IpxCntSapInvalid_Type = Counter32
_IpxCntSapInvalid_Object = MibScalar
ipxCntSapInvalid = _IpxCntSapInvalid_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 21),
    _IpxCntSapInvalid_Type()
)
ipxCntSapInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntSapInvalid.setStatus("mandatory")
_IpxCntRxRipReq_Type = Counter32
_IpxCntRxRipReq_Object = MibScalar
ipxCntRxRipReq = _IpxCntRxRipReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 22),
    _IpxCntRxRipReq_Type()
)
ipxCntRxRipReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntRxRipReq.setStatus("mandatory")
_IpxCntRxRipRsp_Type = Counter32
_IpxCntRxRipRsp_Object = MibScalar
ipxCntRxRipRsp = _IpxCntRxRipRsp_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 23),
    _IpxCntRxRipRsp_Type()
)
ipxCntRxRipRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntRxRipRsp.setStatus("mandatory")
_IpxCntTxRipReq_Type = Counter32
_IpxCntTxRipReq_Object = MibScalar
ipxCntTxRipReq = _IpxCntTxRipReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 24),
    _IpxCntTxRipReq_Type()
)
ipxCntTxRipReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxRipReq.setStatus("mandatory")
_IpxCntTxRipRpl_Type = Counter32
_IpxCntTxRipRpl_Object = MibScalar
ipxCntTxRipRpl = _IpxCntTxRipRpl_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 25),
    _IpxCntTxRipRpl_Type()
)
ipxCntTxRipRpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxRipRpl.setStatus("mandatory")
_IpxCntRipInvalid_Type = Counter32
_IpxCntRipInvalid_Object = MibScalar
ipxCntRipInvalid = _IpxCntRipInvalid_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 26),
    _IpxCntRipInvalid_Type()
)
ipxCntRipInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntRipInvalid.setStatus("mandatory")
_IpxCntTxFailed_Type = Counter32
_IpxCntTxFailed_Object = MibScalar
ipxCntTxFailed = _IpxCntTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 27),
    _IpxCntTxFailed_Type()
)
ipxCntTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxFailed.setStatus("mandatory")
_IpxCntTxPrefFailed_Type = Counter32
_IpxCntTxPrefFailed_Object = MibScalar
ipxCntTxPrefFailed = _IpxCntTxPrefFailed_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 28),
    _IpxCntTxPrefFailed_Type()
)
ipxCntTxPrefFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxPrefFailed.setStatus("mandatory")
_IpxCntRxFiltered_Type = Counter32
_IpxCntRxFiltered_Object = MibScalar
ipxCntRxFiltered = _IpxCntRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 29),
    _IpxCntRxFiltered_Type()
)
ipxCntRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntRxFiltered.setStatus("mandatory")
_IpxCntTxFiltered_Type = Counter32
_IpxCntTxFiltered_Object = MibScalar
ipxCntTxFiltered = _IpxCntTxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 30),
    _IpxCntTxFiltered_Type()
)
ipxCntTxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxFiltered.setStatus("mandatory")
_IpxCntForwarded_Type = Counter32
_IpxCntForwarded_Object = MibScalar
ipxCntForwarded = _IpxCntForwarded_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 31),
    _IpxCntForwarded_Type()
)
ipxCntForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntForwarded.setStatus("mandatory")
_IpxCntCacheHits_Type = Counter32
_IpxCntCacheHits_Object = MibScalar
ipxCntCacheHits = _IpxCntCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 32),
    _IpxCntCacheHits_Type()
)
ipxCntCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntCacheHits.setStatus("mandatory")
_IpxCntSpoofed_Type = Counter32
_IpxCntSpoofed_Object = MibScalar
ipxCntSpoofed = _IpxCntSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 33),
    _IpxCntSpoofed_Type()
)
ipxCntSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntSpoofed.setStatus("mandatory")
_IpxCntSPXCacheHits_Type = Counter32
_IpxCntSPXCacheHits_Object = MibScalar
ipxCntSPXCacheHits = _IpxCntSPXCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 34),
    _IpxCntSPXCacheHits_Type()
)
ipxCntSPXCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntSPXCacheHits.setStatus("mandatory")
_IpxCntRxType20_Type = Counter32
_IpxCntRxType20_Object = MibScalar
ipxCntRxType20 = _IpxCntRxType20_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 35),
    _IpxCntRxType20_Type()
)
ipxCntRxType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntRxType20.setStatus("mandatory")
_IpxCntTxType20_Type = Counter32
_IpxCntTxType20_Object = MibScalar
ipxCntTxType20 = _IpxCntTxType20_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 36),
    _IpxCntTxType20_Type()
)
ipxCntTxType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntTxType20.setStatus("mandatory")
_IpxCntType20Disc_Type = Counter32
_IpxCntType20Disc_Object = MibScalar
ipxCntType20Disc = _IpxCntType20Disc_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 37),
    _IpxCntType20Disc_Type()
)
ipxCntType20Disc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntType20Disc.setStatus("mandatory")
_IpxCntConfigTimeStamp_Type = TimeTicks
_IpxCntConfigTimeStamp_Object = MibScalar
ipxCntConfigTimeStamp = _IpxCntConfigTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 1, 38),
    _IpxCntConfigTimeStamp_Type()
)
ipxCntConfigTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCntConfigTimeStamp.setStatus("mandatory")
_IpxSAP_ObjectIdentity = ObjectIdentity
ipxSAP = _IpxSAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 25, 2)
)
_IpxSAPTable_Object = MibTable
ipxSAPTable = _IpxSAPTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 2, 1)
)
if mibBuilder.loadTexts:
    ipxSAPTable.setStatus("mandatory")
_IpxSAPEntry_Object = MibTableRow
ipxSAPEntry = _IpxSAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 2, 1, 1)
)
ipxSAPEntry.setIndexNames(
    (0, "SCA-IPX-MIB", "ipxSAPServerNet"),
    (0, "SCA-IPX-MIB", "ipxSAPServerNode"),
    (0, "SCA-IPX-MIB", "ipxSAPServerSocket"),
    (0, "SCA-IPX-MIB", "ipxSAPServerType"),
)
if mibBuilder.loadTexts:
    ipxSAPEntry.setStatus("mandatory")


class _IpxSAPServerNet_Type(OctetString):
    """Custom type ipxSAPServerNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxSAPServerNet_Type.__name__ = "OctetString"
_IpxSAPServerNet_Object = MibTableColumn
ipxSAPServerNet = _IpxSAPServerNet_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 2, 1, 1, 1),
    _IpxSAPServerNet_Type()
)
ipxSAPServerNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPServerNet.setStatus("mandatory")


class _IpxSAPServerNode_Type(OctetString):
    """Custom type ipxSAPServerNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxSAPServerNode_Type.__name__ = "OctetString"
_IpxSAPServerNode_Object = MibTableColumn
ipxSAPServerNode = _IpxSAPServerNode_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 2, 1, 1, 2),
    _IpxSAPServerNode_Type()
)
ipxSAPServerNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPServerNode.setStatus("mandatory")


class _IpxSAPServerSocket_Type(OctetString):
    """Custom type ipxSAPServerSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxSAPServerSocket_Type.__name__ = "OctetString"
_IpxSAPServerSocket_Object = MibTableColumn
ipxSAPServerSocket = _IpxSAPServerSocket_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 2, 1, 1, 3),
    _IpxSAPServerSocket_Type()
)
ipxSAPServerSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPServerSocket.setStatus("mandatory")


class _IpxSAPServerType_Type(Integer32):
    """Custom type ipxSAPServerType based on Integer32"""
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
              33,
              34,
              35,
              36,
              38,
              39,
              40,
              41,
              42,
              44,
              45,
              46,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              80,
              83,
              84,
              85,
              86,
              87,
              88,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              172,
              173,
              256,
              257,
              258,
              259,
              261,
              262,
              263,
              268,
              271,
              272,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              306,
              307,
              311,
              319,
              320,
              321,
              323,
              324,
              325,
              327,
              329,
              330,
              331,
              337,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              360,
              361,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              392,
              393,
              398,
              399,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              417,
              418,
              419,
              420,
              421,
              422,
              423,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              432,
              433,
              434,
              435,
              436,
              437,
              438,
              439,
              440,
              441,
              443,
              444,
              445,
              446,
              448,
              449,
              450,
              451,
              452,
              453,
              454,
              455,
              456,
              457,
              458,
              459,
              460,
              461,
              462,
              463,
              464,
              465,
              469,
              470,
              471,
              472,
              473,
              474,
              475,
              476,
              477,
              478,
              479,
              480,
              481,
              482,
              483,
              484,
              487,
              488,
              489,
              490,
              491,
              493,
              494,
              495,
              496,
              497,
              498,
              499,
              500,
              501,
              502,
              504,
              505,
              507,
              508,
              509,
              512,
              513,
              514,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              528,
              529,
              530,
              531,
              532,
              533,
              538,
              541,
              546,
              563,
              564,
              566,
              567,
              568,
              569,
              570,
              571,
              572,
              573,
              574,
              575,
              576,
              577,
              578,
              579,
              580,
              581,
              582,
              583,
              584,
              585,
              586,
              587,
              588,
              589,
              606,
              607,
              608,
              609,
              610,
              611,
              612,
              613,
              614,
              615,
              616,
              617,
              618,
              619,
              621,
              626,
              627,
              628,
              629,
              631,
              632,
              640,
              641,
              642,
              643,
              644,
              645,
              646,
              647,
              648,
              767,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              780,
              800,
              801,
              802,
              803,
              804,
              805,
              806,
              807,
              808,
              809,
              810,
              811,
              812,
              813,
              814,
              816,
              817,
              818,
              819,
              820,
              821,
              822,
              823,
              824,
              825,
              826,
              827,
              828,
              829,
              830,
              831,
              832,
              833,
              834,
              835,
              836,
              837,
              838,
              839,
              840,
              841,
              842,
              843,
              844,
              845,
              846,
              847,
              848,
              849,
              850,
              851,
              852,
              853,
              854,
              855,
              856,
              858,
              859,
              860,
              861,
              862,
              863,
              864,
              867,
              868,
              869,
              870,
              871,
              872,
              873,
              874,
              875,
              876,
              877,
              878,
              879,
              882,
              883,
              884,
              885,
              886,
              887,
              888,
              889,
              890,
              891,
              892,
              893,
              894,
              895,
              896,
              899,
              900,
              901,
              902,
              903,
              904,
              905,
              922,
              923,
              924,
              925,
              926,
              927,
              928,
              929,
              930,
              931,
              932,
              933,
              934,
              935,
              936,
              937,
              938,
              939,
              940,
              941,
              942,
              943,
              944,
              945,
              946,
              947,
              948,
              949,
              950,
              952,
              953,
              954,
              955,
              956,
              957,
              958,
              959,
              960,
              961,
              962,
              963,
              964,
              967,
              968,
              970,
              971,
              975,
              976,
              977,
              978,
              979,
              980,
              981,
              982,
              983,
              984,
              985,
              986,
              987,
              988,
              989,
              990,
              991,
              992,
              993,
              994,
              995,
              996,
              997,
              998,
              999,
              1000,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1011,
              1012,
              1013,
              1014,
              1015,
              1016,
              1017,
              1018,
              1019,
              1020,
              1021,
              1022,
              1023,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036,
              1037,
              1038,
              1039,
              1040,
              1041,
              1042,
              1043,
              1044,
              1045,
              1046,
              1047,
              1048,
              1049,
              1050,
              1051,
              1052,
              1053,
              1054,
              1055,
              1056,
              1057,
              1058,
              1059,
              1060,
              1061,
              1062,
              1063,
              1064,
              1065,
              1066,
              1067,
              1068,
              1069,
              1070,
              1071,
              1072,
              1074,
              1075,
              1076,
              1077,
              1078,
              1079,
              1080,
              1081,
              1082,
              1083,
              1084,
              1085,
              1086,
              1087,
              1088,
              1089,
              1090,
              1091,
              1092,
              1093,
              1094,
              1095,
              1101,
              1102,
              1103,
              1104,
              1105,
              1106,
              1107,
              1108,
              1109,
              1110,
              1111,
              1112,
              1113,
              1114,
              1115,
              1116,
              1117,
              1118,
              1119,
              1120,
              1121,
              1122,
              1124,
              1125,
              1126,
              1128,
              1130,
              1136,
              1137,
              1138,
              1140,
              1141,
              1142,
              1143,
              1144,
              1145,
              1148,
              1149,
              1150,
              1151,
              1152,
              1153,
              1154,
              1155,
              1156,
              1157,
              1158,
              1159,
              1160,
              1161,
              1162,
              1163,
              1164,
              1165,
              1166,
              1167,
              1168,
              1169,
              1173,
              1174,
              1175,
              1176,
              1177,
              1178,
              1179,
              1180,
              1181,
              1182,
              1183,
              1185,
              1186,
              1187,
              1188,
              1189,
              1190,
              1191,
              1192,
              1193,
              1194,
              1195,
              1196,
              1198,
              1200,
              1201,
              1202,
              1203,
              1204,
              1205,
              1206,
              1207,
              1208,
              1209,
              1210,
              1211,
              1212,
              1213,
              1214,
              1215,
              1216,
              1217,
              1218,
              1219,
              1220,
              1221,
              1222,
              1223,
              1224,
              1225,
              1226,
              1227,
              1228,
              1229,
              1231,
              1232,
              1233,
              1234,
              1235,
              1236,
              1237,
              1239,
              1240,
              1241,
              1242,
              1243,
              1244,
              1245,
              1246,
              1247,
              1248,
              1249,
              1250,
              1251,
              1252,
              1253,
              1254,
              1255,
              1256,
              1257,
              1258,
              1259,
              1260,
              1261,
              1262,
              1263,
              1264,
              1265,
              1266,
              1267,
              1268,
              1269,
              1270,
              1271,
              1272,
              1273,
              1274,
              1275,
              1276,
              1277,
              1278,
              1279,
              1280,
              1281,
              1282,
              1283,
              1284,
              1285,
              1286,
              1287,
              1288,
              1289,
              1290,
              1291,
              1292,
              1293,
              1294,
              1295,
              1296,
              1297,
              1298,
              1299,
              1300,
              1301,
              1302,
              1303,
              1304,
              1305,
              1306,
              1307,
              1308,
              1309,
              1310,
              1311,
              1312,
              1313,
              1314,
              1317,
              1318,
              1319,
              1320,
              1321,
              1322,
              1324,
              1325,
              1326,
              1327,
              1328,
              1329,
              1330,
              1331,
              1332,
              1333,
              1334,
              1335,
              1336,
              1337,
              1338,
              1339,
              1340,
              1341,
              1342,
              1343,
              1344,
              1345,
              1346,
              1347,
              1348,
              1349,
              1350,
              1351,
              1352,
              1353,
              1354,
              1355,
              1357,
              1358,
              1359,
              1360,
              1365,
              1366,
              1367,
              1368,
              1369,
              1370,
              1371,
              1372,
              1373,
              1374,
              1375,
              1376,
              1377,
              1378,
              1379,
              1380,
              1381,
              1382,
              1383,
              1384,
              1385,
              1386,
              1387,
              1388,
              1389,
              1391,
              1392,
              1393,
              1394,
              1395,
              1396,
              1398,
              1399,
              1400,
              1401,
              1402,
              1403,
              1404,
              1405,
              1406,
              1407,
              1408,
              1409,
              1410,
              1411,
              1412,
              1413,
              1414,
              1415,
              1417,
              1418,
              1419,
              1420,
              1421,
              1422,
              1423,
              1424,
              1425,
              1426,
              1427,
              1428,
              1429,
              1431,
              1432,
              1436,
              1440,
              1441,
              1442,
              1443,
              1444,
              1445,
              1446,
              1447,
              1448,
              1449,
              1450,
              1451,
              1452,
              1453,
              1454,
              1455,
              1456,
              1457,
              1458,
              1459,
              1460,
              1462,
              1463,
              1464,
              1465,
              1466,
              1472,
              1473,
              1474,
              1475,
              1476,
              1477,
              1478,
              1497,
              1508,
              1509,
              1510,
              1515,
              1516,
              1517,
              1518,
              1519,
              1522,
              1523,
              1524,
              1525,
              1528,
              1530,
              1539,
              1542,
              1543,
              1544,
              1545,
              1546,
              1548,
              1549,
              1552,
              1553,
              1555,
              1556,
              1557,
              1558,
              1564,
              1565,
              1566,
              1567,
              1568,
              1573,
              1583,
              1590,
              1591,
              1853,
              1854,
              1855,
              1856,
              1857,
              1858,
              1859,
              1860,
              1861,
              1862,
              1863,
              1864,
              1865,
              1869,
              1870,
              1871,
              1872,
              1875,
              1876,
              1877,
              1878,
              1879,
              1880,
              1881,
              1882,
              1883,
              1884,
              1885,
              1886,
              1887,
              1898,
              1899,
              1901,
              1904,
              1905,
              1907,
              1908,
              1909,
              1915,
              1919,
              1920,
              1921,
              1922,
              1923,
              1931,
              1944,
              1945,
              1946,
              1951,
              1952,
              1959,
              1960,
              1961,
              1964,
              1967,
              1968,
              1971,
              1972,
              1976,
              1978,
              1983,
              1984,
              1985,
              1998,
              2001,
              2002,
              2003,
              2004,
              2009,
              2010,
              2011,
              2012,
              2013,
              2016,
              2017,
              2018,
              2019,
              2020,
              2022,
              2028,
              2029,
              2030,
              2032,
              2034,
              2040,
              2041,
              2044,
              2045,
              2047,
              2049,
              2061,
              2062,
              2064,
              2065,
              2067,
              2068,
              2070,
              2071,
              2072,
              2077,
              2087,
              2089,
              2090,
              2091,
              2095,
              2096,
              2098,
              2099,
              2100,
              2101,
              2102,
              2103,
              2109,
              2110,
              2112,
              2113,
              2124,
              2125,
              2128,
              2131,
              2132,
              2133,
              2136,
              2138,
              2140,
              2143,
              2144,
              2152,
              2153,
              2160,
              3113,
              3114,
              3116,
              3121,
              9100,
              9101,
              9102,
              38432,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("aNonNamePipePipeServer", 1931),
          ("aSynchronousCommunication", 2001),
          ("accessServerForModemSharing", 1330),
          ("addressServer", 589),
          ("administrationServer", 1077),
          ("adminsitration", 11),
          ("advantageXBaseServer", 1915),
          ("advertisingJobServer", 621),
          ("advertisingMediaDbServer", 1385),
          ("advertisingNetmodemServer", 1394),
          ("advertisingNetworkModems", 1310),
          ("advertisingPrintServer", 71),
          ("advertisingRemoteServer329", 329),
          ("advertisingRemoteServer353", 353),
          ("agentForHubManagement", 1317),
          ("agentRouterProxy", 2143),
          ("alarmManagerNlm", 1898),
          ("allKalpanaSwitches", 1877),
          ("allTypes", 65535),
          ("aplinkgate", 2131),
          ("aplinkterm", 2128),
          ("applicationAdvertisement", 1984),
          ("applicationPrograms", 1311),
          ("applicationRightsProgram", 615),
          ("applicationServer1325", 1325),
          ("applicationServer814", 814),
          ("applicationServerForNt", 2109),
          ("appmeter2LicensingProduct", 2098),
          ("appmeterForSuites", 1432),
          ("aptNetRemote411", 411),
          ("aptNetRemote412", 412),
          ("aptNetRemote413", 413),
          ("aptNetRemote414", 414),
          ("arcServe40", 964),
          ("archiveQueue", 8),
          ("archiveServer165", 165),
          ("archiveServer9", 9),
          ("archiveServerSAP", 46),
          ("areaCodeAndExchangeLookUpServer", 482),
          ("arrayMonitorServer", 1163),
          ("artsGenericServer", 1544),
          ("artsRlogindServer", 1543),
          ("artsRuupdAreYouUpDaemon", 1545),
          ("ascomAdvertisingFaxServer", 1151),
          ("ascomFaxQueue", 1152),
          ("ascomFaxServer", 1150),
          ("associativeIndexServer", 1287),
          ("astSnmpInstrumentedServer", 1510),
          ("asynchCommSvrMvdFrm", 1079),
          ("asynchronousAccessServer", 1235),
          ("asynchronousCommunicationsServers", 1217),
          ("asynchronousSerialCommunications1014", 1014),
          ("asynchronousSerialCommunications1015", 1015),
          ("asynchronousSerialCommunications1016", 1016),
          ("asynchronousSerialCommunications1017", 1017),
          ("atAndTJointVentureTelephonyServer1369", 1369),
          ("atAndTJointVentureTelephonyServer1370", 1370),
          ("atAndTJointVentureTelephonyServer1371", 1371),
          ("atAndTJointVentureTelephonyServer1372", 1372),
          ("atlanta3PrintServer", 2103),
          ("auditorPackage", 162),
          ("autoOnOffControlNlm", 1149),
          ("automationInformationRouter", 1185),
          ("automationProtocolServer", 2132),
          ("axisPrinterServer", 1548),
          ("backUpProduct1080", 1080),
          ("backUpProduct1081", 1081),
          ("backupExecJobManager", 1960),
          ("backupExecJobQueue", 1959),
          ("backupExecJobService", 1961),
          ("batchfilerApplication", 1124),
          ("bbsServer", 778),
          ("binderyFile", 1518),
          ("binderyForProgramMeteringDatabase", 1190),
          ("binderyObjectType", 856),
          ("binderyObjectTypes1024", 1024),
          ("binderyObjectTypes1025", 1025),
          ("binderyObjectTypes1026", 1026),
          ("binderyObjectTypes1027", 1027),
          ("binderyObjectTypes1028", 1028),
          ("binderyObjectTypes1029", 1029),
          ("binderyObjectTypes1030", 1030),
          ("binderyObjectTypes1031", 1031),
          ("binderyObjectTypes1032", 1032),
          ("binderyObjectTypes1033", 1033),
          ("binderyService1192", 1192),
          ("binderyService1193", 1193),
          ("binderyType455", 455),
          ("binderyType834", 834),
          ("binderyType835", 835),
          ("binderyType836", 836),
          ("binderyType837", 837),
          ("binderyType838", 838),
          ("binderyType839", 839),
          ("binderyType840", 840),
          ("binderyType841", 841),
          ("binderyType850", 850),
          ("binderyType851", 851),
          ("binderyType852", 852),
          ("binderyType875", 875),
          ("binderyType879", 879),
          ("binderyTypeApplicationDefinition", 1116),
          ("binderyTypeForBroadcast", 571),
          ("binderyTypeForCdServer", 928),
          ("bloombergAudioServer", 1312),
          ("bloombergProcessServer", 1313),
          ("bootwareMsd", 807),
          ("boxRouterSupportingIpIpxAndAppleT", 2017),
          ("boxTypeHdwrRouterSupptsAppletalk", 2124),
          ("btX25", 306),
          ("btriveVAP411", 80),
          ("btriveVAP50", 75),
          ("bullHnSdm", 1178),
          ("bvncsEnterpriseWan", 2067),
          ("calendarServer1196", 1196),
          ("calendarServer1472", 1472),
          ("camHost", 1886),
          ("canonPeripheralServer", 1111),
          ("casperGhost", 1222),
          ("casperQueue", 1221),
          ("catalogServer", 2144),
          ("cbtServer", 1425),
          ("cdRomServer", 1227),
          ("cdnetServer", 1200),
          ("cdrom", 323),
          ("chatServer", 1878),
          ("chgdFrm", 123),
          ("clientServerArrayMonitorProgram", 1523),
          ("clientServerDriverForIpxSpx", 1069),
          ("clientServerMonitoringUtility", 1115),
          ("cometFileServer", 1591),
          ("cometTerminalServer", 1590),
          ("comgateCommGatewayForIbmAs400", 2030),
          ("commSvrNetBiosIpxMvdFrm273411", 887),
          ("commonCommunicationInterface", 1103),
          ("communicationBetweenClientAndServer", 1160),
          ("communicationProcessor", 325),
          ("communicationServer1242", 1242),
          ("communicationServer1243", 1243),
          ("communicationServer1244", 1244),
          ("communicationServer1245", 1245),
          ("communicationServer1246", 1246),
          ("communicationServer1247", 1247),
          ("communicationServer1248", 1248),
          ("communicationServer1249", 1249),
          ("communicationServer1250", 1250),
          ("communicationServer1251", 1251),
          ("communicationServer1252", 1252),
          ("communicationServer1253", 1253),
          ("communicationServer1254", 1254),
          ("communicationServer1255", 1255),
          ("communicationServer1256", 1256),
          ("communicationServer1257", 1257),
          ("communicationServer1258", 1258),
          ("communicationServer1259", 1259),
          ("communicationServer1260", 1260),
          ("communicationServer1261", 1261),
          ("communicationServer1399", 1399),
          ("communicationServer2099", 2099),
          ("communicationServer275", 275),
          ("communicationServer276", 276),
          ("communicationServer277", 277),
          ("communicationServer278", 278),
          ("communicationServer279", 279),
          ("communicationServer280", 280),
          ("communicationServer281", 281),
          ("communicationServer282", 282),
          ("communicationServer283", 283),
          ("communicationServer285", 285),
          ("communicationServer286", 286),
          ("communicationServer287", 287),
          ("communicationServer288", 288),
          ("communicationServer289", 289),
          ("communicationServer290", 290),
          ("communicationServer291", 291),
          ("communicationServer292", 292),
          ("communicationServer293", 293),
          ("communicationServer294", 294),
          ("communicationServer295", 295),
          ("communicationServer296", 296),
          ("communicationServer297", 297),
          ("communicationServer298", 298),
          ("communicationServer300", 300),
          ("communicationSoftwareNlm1556", 1556),
          ("communicationSoftwareNlm1557", 1557),
          ("communicationsGatewayOsi", 1121),
          ("communicationsGatewaySna", 1122),
          ("communicationsServer301", 301),
          ("communicationsServer302", 302),
          ("communicationsServer303", 303),
          ("communicationsServer304", 304),
          ("communicationsServer821", 821),
          ("communicationsServer822", 822),
          ("communicationsServerBindery", 924),
          ("communicationsServerSap", 925),
          ("communicationsServerSddSynthesizer", 1104),
          ("companyAetnaLifeAndCasualty809", 809),
          ("companyAetnaLifeAndCasualty810", 810),
          ("companyAetnaLifeAndCasualty820", 820),
          ("companyAndersenConsultingChicago", 502),
          ("companyArcadaSoftware", 853),
          ("companyArchetype818", 818),
          ("companyArchetype819", 819),
          ("companyArtefactNetworkSupport", 272),
          ("companyAttachmateCorporation", 800),
          ("companyBonsaiTechnologies441", 441),
          ("companyBonsaiTechnologies443", 443),
          ("companyBonsaiTechnologies444", 444),
          ("companyBonsaiTechnologies445", 445),
          ("companyBusinessRecordsCorp73", 73),
          ("companyBusinessRecordsCorp90", 90),
          ("companyBusinessRecordsCorp91", 91),
          ("companyBusinessRecordsCorp92", 92),
          ("companyBusinessRecordsCorp93", 93),
          ("companyBusinessRecordsCorp94", 94),
          ("companyBusinessRecordsCorp95", 95),
          ("companyCastelleInc472", 472),
          ("companyCastelleInc473", 473),
          ("companyCastelleInc474", 474),
          ("companyCastelleInc475", 475),
          ("companyCastelleInc476", 476),
          ("companyCastelleInc477", 477),
          ("companyCastelleInc478", 478),
          ("companyCastelleInc479", 479),
          ("companyCastelleInc480", 480),
          ("companyCastelleInc481", 481),
          ("companyCentersForDiseaseControl", 469),
          ("companyChiCorp", 42),
          ("companyChicagoResearchAndTrading", 801),
          ("companyComputerLogics", 38),
          ("companyComputervisionServices", 927),
          ("companyDatanexCorporation", 905),
          ("companyDeInternationalLtd", 1094),
          ("companyDigitalEquipmentMerrimack", 882),
          ("companyExcaliburTechnologiesCorp871", 871),
          ("companyExcaliburTechnologiesCorp872", 872),
          ("companyExcaliburTechnologiesCorp873", 873),
          ("companyExcaliburTechnologiesCorp874", 874),
          ("companyExtendedSystems", 508),
          ("companyFelsinaSoftware", 495),
          ("companyFryeComputerSystems", 802),
          ("companyHyprotechLtd", 930),
          ("companyIbmEndicott", 509),
          ("companyIntegralisLtd493", 493),
          ("companyIntegralisLtd494", 494),
          ("companyIntegratedTechnologiesInc", 406),
          ("companyIntelAmericanFork258", 258),
          ("companyIntelAmericanFork44", 44),
          ("companyInteractiveFinancialSolInc100", 100),
          ("companyInteractiveFinancialSolInc101", 101),
          ("companyInteractiveFinancialSolInc102", 102),
          ("companyInteractiveFinancialSolInc103", 103),
          ("companyInteractiveFinancialSolInc104", 104),
          ("companyInteractiveFinancialSolInc105", 105),
          ("companyInteractiveFinancialSolInc106", 106),
          ("companyInteractiveFinancialSolInc107", 107),
          ("companyInteractiveFinancialSolInc108", 108),
          ("companyInteractiveFinancialSolInc124", 124),
          ("companyInteractiveFinancialSolInc125", 125),
          ("companyInteractiveFinancialSolInc126", 126),
          ("companyInteractiveFinancialSolInc127", 127),
          ("companyInteractiveFinancialSolInc128", 128),
          ("companyInteractiveFinancialSolInc129", 129),
          ("companyInteractiveFinancialSolInc130", 130),
          ("companyInteractiveFinancialSolInc131", 131),
          ("companyInteractiveFinancialSolInc132", 132),
          ("companyInteractiveFinancialSolInc133", 133),
          ("companyInteractiveFinancialSolInc134", 134),
          ("companyInteractiveFinancialSolInc135", 135),
          ("companyInteractiveFinancialSolInc136", 136),
          ("companyInteractiveFinancialSolInc137", 137),
          ("companyInteractiveFinancialSolInc138", 138),
          ("companyInteractiveFinancialSolInc139", 139),
          ("companyInteractiveFinancialSolInc140", 140),
          ("companyInteractiveFinancialSolInc99", 99),
          ("companyIntrakInc", 1070),
          ("companyIrisAssociates", 923),
          ("companyKyoceraCorpYohagaOffice931", 931),
          ("companyKyoceraCorpYohagaOffice932", 932),
          ("companyKyoceraCorpYohagaOffice933", 933),
          ("companyKyoceraCorpYohagaOffice934", 934),
          ("companyLanovation854", 854),
          ("companyLanovation855", 855),
          ("companyLantechServices", 950),
          ("companyLegatoSystems496", 496),
          ("companyLegatoSystems497", 497),
          ("companyLegatoSystems498", 498),
          ("companyLegatoSystems499", 499),
          ("companyLegatoSystems500", 500),
          ("companyLegatoSystems501", 501),
          ("companyMageeEnterprisesInc823", 823),
          ("companyMageeEnterprisesInc824", 824),
          ("companyMageeEnterprisesInc825", 825),
          ("companyMageeEnterprisesInc826", 826),
          ("companyMageeEnterprisesInc827", 827),
          ("companyMageeEnterprisesInc828", 828),
          ("companyMageeEnterprisesInc829", 829),
          ("companyMageeEnterprisesInc830", 830),
          ("companyMageeEnterprisesInc831", 831),
          ("companyMageeEnterprisesInc832", 832),
          ("companyMbac", 858),
          ("companyMediaTouchSystems435", 435),
          ("companyMediaTouchSystems491", 491),
          ("companyMicroDataBaseSystems", 150),
          ("companyMicroIntegration", 877),
          ("companyModularSoftwareCorporation", 1023),
          ("companyMultitech", 1267),
          ("companyNetwiseInc", 324),
          ("companyNetworkComputingIncNci348", 348),
          ("companyNetworkComputingIncNci349", 349),
          ("companyNetworkComputingIncNci350", 350),
          ("companyNetworkComputingIncNci351", 351),
          ("companyNetworkComputingIncNci352", 352),
          ("companyNetworkDesignersLtd", 319),
          ("companyNeumeierAndWalchSystemtechnik", 929),
          ("companyNortheastBroadcastConsultant", 507),
          ("companyNovellProvo", 546),
          ("companyNovellProvoCorpHq115", 115),
          ("companyNovellProvoCorpHq116", 116),
          ("companyNovellProvoCorpHq119", 119),
          ("companyNovellProvoCorpHq120", 120),
          ("companyNovellProvoCorpHq121", 121),
          ("companyNovellProvoCorpHq331", 331),
          ("companyNovellProvoCorpHq516", 516),
          ("companyNovellProvoCorpHq517", 517),
          ("companyNovellProvoCorpHq518", 518),
          ("companyNovellProvoCorpHq519", 519),
          ("companyNovellProvoCorpHq520", 520),
          ("companyNovellProvoCorpHq521", 521),
          ("companyNovellProvoCorpHq522", 522),
          ("companyNovellProvoCorpHq523", 523),
          ("companyNovellProvoCorpHq524", 524),
          ("companyNovellProvoCorpHq525", 525),
          ("companyNovellProvoCorpHq526", 526),
          ("companyNovellProvoCorpHq527", 527),
          ("companyNovellProvoCorpHq528", 528),
          ("companyNovellProvoCorpHq529", 529),
          ("companyNovellProvoCorpHq530", 530),
          ("companyNovellProvoCorpHq531", 531),
          ("companyNovellProvoCorpHq532", 532),
          ("companyNovellProvoCorpHq533", 533),
          ("companyNovellProvoCorpHq767", 767),
          ("companyNovellSaltLakeCity", 566),
          ("companyNovellSanJose576", 576),
          ("companyNovellSanJose577", 577),
          ("companyNovellSanJose578", 578),
          ("companyNovellSanJose616", 616),
          ("companyNovellWalnutCreek", 640),
          ("companyParadataComputerNetworks", 74),
          ("companyPeerLogic256", 256),
          ("companyPeerLogic361", 361),
          ("companyPreferredSystemsInc842", 842),
          ("companyPreferredSystemsInc843", 843),
          ("companyPreferredSystemsInc844", 844),
          ("companyPreferredSystemsInc845", 845),
          ("companyPreferredSystemsInc846", 846),
          ("companyPreferredSystemsInc847", 847),
          ("companyPreferredSystemsInc848", 848),
          ("companyPreferredSystemsInc849", 849),
          ("companyRaimaCorp", 942),
          ("companyRationalDataSystems142", 142),
          ("companyRationalDataSystems487", 487),
          ("companyRationalDataSystems488", 488),
          ("companyRationalDataSystems489", 489),
          ("companyRationalDataSystems490", 490),
          ("companyRaylynnKnight", 156),
          ("companyShivaCorp459", 459),
          ("companyShivaCorp460", 460),
          ("companyShivaCorp461", 461),
          ("companyShivaCorp462", 462),
          ("companySperryCorpComputerSystems", 34),
          ("companySytronCorp", 504),
          ("companyThinkSystemsCorp", 1159),
          ("companyUdsMotorola938", 938),
          ("companyUdsMotorola939", 939),
          ("companyUdsMotorola940", 940),
          ("companyUdsMotorola941", 941),
          ("companyWallData", 484),
          ("companyWangLaboratories803", 803),
          ("companyWangLaboratories804", 804),
          ("companyWatcom147", 147),
          ("companyWatcom808", 808),
          ("companyZenithDataSystems408", 408),
          ("companyZenithDataSystems409", 409),
          ("companyZenithDataSystems410", 410),
          ("computerSupportedTelephonyApps", 1998),
          ("conferencingService", 1223),
          ("connectDirectNlmServer1853", 1853),
          ("connectDirectNlmServer1854", 1854),
          ("connectDirectNlmServer1855", 1855),
          ("connectDirectNlmServer1856", 1856),
          ("connectDirectNlmServer1857", 1857),
          ("connectDirectNlmServer1858", 1858),
          ("connectionStationServiceType1084", 1084),
          ("connectionStationServiceType1085", 1085),
          ("connectionStationServiceType1086", 1086),
          ("connectionStationServiceType1087", 1087),
          ("connectionStationServiceType1088", 1088),
          ("connectionStationServiceType1089", 1089),
          ("connectionStationServiceType1090", 1090),
          ("connectionStationServiceType1091", 1091),
          ("copyProtectionServer", 943),
          ("corelDriverProductUnderNovell386", 164),
          ("costRecoveryServer", 1228),
          ("cq3270Lan", 157),
          ("cubixCommServer", 1972),
          ("cubixQlClient", 1240),
          ("cubixQlServer", 1239),
          ("customAuthenticationLoadBalancing", 2110),
          ("dart", 151),
          ("dataServiceToWorkstationSchoolAdmin", 833),
          ("databaseEngine", 975),
          ("databaseLockServer", 1175),
          ("databaseManagementServices", 1464),
          ("databaseServer1218", 1218),
          ("databaseServer1297", 1297),
          ("databaseServer1983", 1983),
          ("databaseServerRunningAsNlm", 1216),
          ("datafileAccessHandler", 1402),
          ("datalinkSwitchingDlsw", 626),
          ("datastarNlm", 1462),
          ("dbExpress", 2140),
          ("dbServer", 417),
          ("dbServer3X", 2095),
          ("dcsSystemServer", 337),
          ("dealingRoomServers1046", 1046),
          ("dealingRoomServers1047", 1047),
          ("dealingRoomServers1048", 1048),
          ("dealingRoomServers1049", 1049),
          ("dealingRoomServers1050", 1050),
          ("dealingRoomServers1051", 1051),
          ("dealingRoomServers1052", 1052),
          ("dealingRoomServers1053", 1053),
          ("dealingRoomServers1054", 1054),
          ("dealingRoomServers1055", 1055),
          ("dealingRoomServers1056", 1056),
          ("dealingRoomServers1057", 1057),
          ("dealingRoomServers1058", 1058),
          ("dealingRoomServers1059", 1059),
          ("dealingRoomServers1060", 1060),
          ("dealingRoomServers1061", 1061),
          ("dealingRoomServers1062", 1062),
          ("dealingRoomServers1063", 1063),
          ("dealingRoomServers1064", 1064),
          ("dealingRoomServers1065", 1065),
          ("delvryOfValuableInfoWUsageTracking", 1188),
          ("desktopManagementNlm", 1901),
          ("deskviewXBinderyType", 1284),
          ("developingServerPerformanceAnalizer", 989),
          ("deviceLocationViaRemoteConfigTool1332", 1332),
          ("deviceLocationViaRemoteConfigTool1333", 1333),
          ("deviceLocationViaRemoteConfigTool1334", 1334),
          ("deviceLocationViaRemoteConfigTool1335", 1335),
          ("deviceLocationViaRemoteConfigTool1336", 1336),
          ("deviceLocationViaRemoteConfigTool1337", 1337),
          ("deviceLocationViaRemoteConfigTool1338", 1338),
          ("deviceLocationViaRemoteConfigTool1339", 1339),
          ("deviceLocationViaRemoteConfigTool1340", 1340),
          ("deviceLocationViaRemoteConfigTool1341", 1341),
          ("directoryServer", 632),
          ("discDisasterRecoverySWScheduler", 1971),
          ("diskMonitor", 1137),
          ("distribtionJobServer", 2009),
          ("distributedApplication", 454),
          ("distributionFeedbackJobServer", 2011),
          ("distributionQue", 2010),
          ("distributionServicesDiscovery", 1465),
          ("distributiveCacheProduct", 1095),
          ("districtCommunicationGateway", 1358),
          ("districtLink", 1359),
          ("docraClientServerDocMgmtSystem", 1350),
          ("documentManagementPackage", 777),
          ("documentManagementService", 1294),
          ("documentProcessingServerNlm1164", 1164),
          ("documentProcessingServerNlm1165", 1165),
          ("documentProcessingServerNlm1166", 1166),
          ("documentProcessingServerNlm1167", 1167),
          ("domainApplicationServices641", 641),
          ("domainApplicationServices642", 642),
          ("domainApplicationServices643", 643),
          ("domainApplicationServices644", 644),
          ("domainApplicationServices645", 645),
          ("domainApplicationServices646", 646),
          ("domainApplicationServices647", 647),
          ("domainApplicationServices648", 648),
          ("dosTargetServiceAgent", 572),
          ("dpcServerBindery", 1885),
          ("dpcServerSap", 1884),
          ("dpsSv", 2160),
          ("dsLccLogicalLinkController", 1463),
          ("eMailQueueObjectType", 463),
          ("eMailServerObjectType", 464),
          ("edmClientPc", 1360),
          ("elanLicenseServer", 2065),
          ("elanLicenseServerDemo", 2064),
          ("emailAndCalendaringCommunicationServer", 1183),
          ("embeddedInOemPlotterProduct960", 960),
          ("embeddedInOemPlotterProduct961", 961),
          ("embeddedInOemPlotterProduct962", 962),
          ("embeddedInOemPlotterProduct963", 963),
          ("enterpriseDescriptionObject", 1236),
          ("enterpriseEcs", 885),
          ("enterpriseInMaintenanceMode", 1083),
          ("enterpriseInitializationMode", 886),
          ("enterpriseNetworkServices", 1138),
          ("erlDatabaseServer", 1379),
          ("erlDirectoryServer", 1380),
          ("ethernetLanControllerForNetware", 945),
          ("ethernetManagedStackableHub", 1497),
          ("eventManagerNlm", 1899),
          ("evergreenManagementAgent", 1524),
          ("evergreenWindcapManagementAgent", 2068),
          ("failSafeAnalysis", 1158),
          ("faxAndVoiceServer", 1322),
          ("faxGatewayServer", 1558),
          ("faxMergeServer", 862),
          ("faxPrintServer", 861),
          ("faxServer1117", 1117),
          ("faxServer1118", 1118),
          ("faxServer1119", 1119),
          ("faxServer1120", 1120),
          ("faxServer1130", 1130),
          ("faxServer811", 811),
          ("faxServer860", 860),
          ("faxServer889", 889),
          ("faxServer890", 890),
          ("faxServer891", 891),
          ("faxServer892", 892),
          ("faxServer896", 896),
          ("faxServer926", 926),
          ("faxServices1366", 1366),
          ("faxServices1367", 1367),
          ("faxServices1368", 1368),
          ("faxWorkstationObject", 1519),
          ("fileManagementServices", 947),
          ("fileServer", 4),
          ("fileShare370", 370),
          ("fileShare371", 371),
          ("fileShare372", 372),
          ("fileShare373", 373),
          ("fileShare374", 374),
          ("fileTransferBetweenLanMainframe", 1978),
          ("filemakerPro", 1074),
          ("filenetNetworkClearinghouse", 1508),
          ("finance", 1155),
          ("financialDataServer", 2028),
          ("financialMarketInformationServer", 1291),
          ("finderBinderyType", 1072),
          ("firstCall", 1009),
          ("forUnibaseBvBasedInHolland", 505),
          ("forcasting", 1156),
          ("formsCapability340", 340),
          ("formsCapability341", 341),
          ("formsCapability342", 342),
          ("formsCapability343", 343),
          ("formsCapability344", 344),
          ("formsCapability345", 345),
          ("formsCapability346", 346),
          ("formsCapability347", 347),
          ("ftanalyzer", 2100),
          ("ftmanagerControlsNetwareServer", 2044),
          ("fullScreenLogin", 1422),
          ("fullTextRetrievalClientServerDbEng", 1066),
          ("gateway", 6),
          ("gatewayBetweenNetworkAndVisaPosPort", 1331),
          ("gatewayCompositePageAndEtcServers419", 419),
          ("gatewayCompositePageAndEtcServers420", 420),
          ("gatewayCompositePageAndEtcServers421", 421),
          ("gatewayCompositePageAndEtcServers422", 422),
          ("gatewayCompositePageAndEtcServers423", 423),
          ("gatewayCompositePageAndEtcServers424", 424),
          ("gatewayCompositePageAndEtcServers425", 425),
          ("gatewayCompositePageAndEtcServers426", 426),
          ("gatewayCompositePageAndEtcServers427", 427),
          ("gatewayCompositePageAndEtcServers428", 428),
          ("gatewayManagement", 893),
          ("gatewayServer", 1517),
          ("gatewaySoftware1067", 1067),
          ("gatewaySoftware1068", 1068),
          ("gatewayToUnisys", 261),
          ("gatewaysToUnisys", 262),
          ("genericJobServer", 514),
          ("genericNwManagementProduct", 2003),
          ("globalInfoApplicationExecEnvironment", 953),
          ("globalLicenseSap", 3116),
          ("globalMhs", 612),
          ("goodallVirtualProtocolAdaptor", 1530),
          ("groupwiseMessageMultipleServers", 628),
          ("guptaSequelBaseServer", 990),
          ("guptaSqlBaseServer", 160),
          ("hewlettPackardBridges", 902),
          ("hewlettPackardHubs", 903),
          ("highSpeedCommunicationServer", 2102),
          ("hitecsoftApiManager", 1907),
          ("hitecsoftPhoneServer", 1909),
          ("hitecsoftPublicLibrary", 1908),
          ("homeRouter", 541),
          ("hopsDatabaseServer", 1401),
          ("hostviewUtility", 1373),
          ("hpNsUtil", 776),
          ("hpOpenMailAndPortableNetware", 922),
          ("hpcsDataBasedProducts", 1509),
          ("hubAgent10121300", 1300),
          ("hubAgent10121301", 1301),
          ("hubAgent10121302", 1302),
          ("hubAgent10121303", 1303),
          ("hubAgent10121304", 1304),
          ("hubAgent10121305", 1305),
          ("hubAgent10121306", 1306),
          ("hubAgent10121307", 1307),
          ("hubAgent10121308", 1308),
          ("hubAgent10121309", 1309),
          ("hubServices", 610),
          ("hyperdeskDatabaseType", 1418),
          ("hyperdeskDistributeObjectMgmtSystem", 1417),
          ("i4LsNamingService", 1352),
          ("ibmHostGateway", 1101),
          ("icotSnaGateway", 1180),
          ("id5001WeatherStation", 330),
          ("idaStatusUtilMvdFrm", 172),
          ("identifyServerVendorForNms", 1976),
          ("ifonyFlowForNetware", 2061),
          ("imageApplication1034", 1034),
          ("imageApplication1035", 1035),
          ("imageApplication1036", 1036),
          ("imageApplication1037", 1037),
          ("imageApplication1038", 1038),
          ("imageApplication1039", 1039),
          ("imageApplication1040", 1040),
          ("imageApplication1041", 1041),
          ("imageApplication1042", 1042),
          ("imageApplication1043", 1043),
          ("imageManagementService", 1295),
          ("imageServerAddressLookUp", 1542),
          ("imagesolveOfs", 1357),
          ("indFileFileTranasferAgtCsaIndfile", 1876),
          ("indexSequentialAccessNlm", 1286),
          ("instantInternet", 2101),
          ("integratedRemoteAccessForEthernet", 1388),
          ("integratedRemoteAccessForTokenring", 1389),
          ("internetAppsOnNwPcs", 1985),
          ("internetGateway", 1182),
          ("interprocessExchangeServer", 813),
          ("interserverFileCopying", 1321),
          ("ipToIpxGateway", 2112),
          ("ipxCommunicationServer", 1329),
          ("ipxLayerPeerToPeerCommunications", 876),
          ("ipxNamedPipesCommunicationService", 1431),
          ("isdnSoftwareSharingOfIsdnBoards", 2029),
          ("jetnetDriverForNovellIpxProtocols", 1215),
          ("jobQueue10", 10),
          ("jobQueue1154", 1154),
          ("jobQueue2091", 2091),
          ("jobServer1153", 1153),
          ("jobServer1241", 1241),
          ("jobServer155", 155),
          ("jobServer5", 5),
          ("jobServer977", 977),
          ("jukeboxUserGroup", 1421),
          ("laaServerBindery", 1012),
          ("lan1Router", 168),
          ("lanAssistPlusRemoteControl1207", 1207),
          ("lanAssistPlusRemoteControl1208", 1208),
          ("lanAssistPlusRemoteControl1209", 1209),
          ("lanAssistPlusRemoteControl1210", 1210),
          ("lanCdServer", 1396),
          ("lanLensProbe", 2090),
          ("lanLensServer", 2089),
          ("lanProductServer", 1424),
          ("lanSpool35", 967),
          ("lancorpEoms", 1177),
          ("landeepServerMonitor", 1905),
          ("lanfaxRedirector", 369),
          ("lanlordProduct", 465),
          ("lanportVirtualExtensionOfPorts", 173),
          ("lanternRmon", 585),
          ("lanwareMvdFrm375", 375),
          ("lanwareMvdFrm376", 376),
          ("lanwareMvdFrm377", 377),
          ("lanwareMvdFrm378", 378),
          ("lanwareMvdFrm379", 379),
          ("lanwareMvdFrm380", 380),
          ("lanwareMvdFrm381", 381),
          ("lanwareMvdFrm382", 382),
          ("lanwareMvdFrm383", 383),
          ("latNetworkFromNetware", 588),
          ("latSessionManager", 587),
          ("latTransportServiceProvider", 586),
          ("ledServer", 1198),
          ("lgs", 1404),
          ("lgsPft", 1405),
          ("lgsPps", 1406),
          ("licenseProfile", 3113),
          ("licenseProfileAdministrator", 38432),
          ("licenseReportDefinition", 3121),
          ("licensingRestrictionsBinderyType433", 433),
          ("licensingRestrictionsBinderyType434", 434),
          ("listenerDos", 1344),
          ("listenerMac", 1347),
          ("listenerNetware", 1343),
          ("listenerOs2", 1346),
          ("listenerUnix", 1348),
          ("listenerWindows", 1345),
          ("loaderBinderyType", 1071),
          ("ltAuditor400Plus", 1191),
          ("macProject", 83),
          ("magixDatabaseServer", 954),
          ("mailServer", 141),
          ("mailSystemQueueService", 1224),
          ("mailSystems", 901),
          ("mailslotsChgdFrom", 415),
          ("mainNlmServerForCalendarManager", 1162),
          ("managingHardwareRouters", 1466),
          ("mapAssistPeerToPeer1211", 1211),
          ("mapAssistPeerToPeer1212", 1212),
          ("mapAssistPeerToPeer1213", 1213),
          ("mapAssistPeerToPeer1214", 1214),
          ("massStorageService", 1296),
          ("maxserv3270", 1859),
          ("maxservMacs", 1862),
          ("maxservMail", 1861),
          ("maxservPrice", 1860),
          ("maxservReserved1863", 1863),
          ("maxservReserved1864", 1864),
          ("maxway500", 404),
          ("mcafeeVirusPatternServer", 1408),
          ("measureserversAndMeasureclients", 1136),
          ("medStationServer", 1391),
          ("meetingMakerXp", 9100),
          ("meetingSpaceServer", 1423),
          ("menuProgram166", 166),
          ("menuProgram429", 429),
          ("menuProgram430", 430),
          ("messageExpressProduct", 1226),
          ("meterServer", 1176),
          ("meteringProgram", 1583),
          ("mgateCommunicationGatewayLansVax", 870),
          ("micSnaDfvServer", 112),
          ("microcomRemoteAccessServer", 1327),
          ("microsoftSqlServerIpxSpxSupport", 1013),
          ("miscellaneousSoftwareCommunications", 1082),
          ("modemProtocallSharingSerialPorts", 952),
          ("modemSharingSoftware", 1400),
          ("moneyCenterDataServer", 1546),
          ("multiPoint", 41),
          ("multiPointX25", 88),
          ("multiServerMetoring", 2020),
          ("multiSystemManagerNetviewInterface", 1459),
          ("multipleServicesAndApplications986", 986),
          ("multipleServicesAndApplications987", 987),
          ("multipleServicesAndApplications988", 988),
          ("mvdFrm111", 111),
          ("mvdFrm895", 895),
          ("nacs110", 110),
          ("nacs35", 35),
          ("namedPipeCommunicationsService", 1318),
          ("namedPipesServer", 154),
          ("nasSnaGateway", 33),
          ("ndsGatewayForOce", 580),
          ("nestDevice", 627),
          ("net3270", 268),
          ("netModemServer", 1314),
          ("netTraxAlarmMonitor", 1411),
          ("netTraxBridgeAgent", 1414),
          ("netTraxFileServerAgent", 1412),
          ("netTraxWorkstationAgent", 1413),
          ("netTuneService", 1426),
          ("netWare386PrintQueue", 311),
          ("netblazerCommunicationServer", 1169),
          ("nethopperClient", 1946),
          ("nethopperClientRouter", 1945),
          ("nethopperRouter", 1944),
          ("netlynxCommunicationServer1268", 1268),
          ("netlynxCommunicationServer1269", 1269),
          ("netlynxCommunicationServer1270", 1270),
          ("netlynxCommunicationServer1271", 1271),
          ("netlynxCommunicationServer1272", 1272),
          ("netlynxCommunicationServer1273", 1273),
          ("netlynxCommunicationServer1274", 1274),
          ("netlynxCommunicationServer1275", 1275),
          ("netlynxCommunicationServer1276", 1276),
          ("netlynxCommunicationServer1277", 1277),
          ("netlynxCommunicationServer1278", 1278),
          ("netlynxCommunicationServer1279", 1279),
          ("netlynxCommunicationServer1280", 1280),
          ("netlynxCommunicationServer1281", 1281),
          ("netlynxCommunicationServer1282", 1282),
          ("netlynxCommunicationServer1283", 1283),
          ("netmagicBinderyId", 1290),
          ("netportAdvertising1019", 1019),
          ("netportAdvertising1020", 1020),
          ("netportAdvertising1021", 1021),
          ("netportAdvertising1022", 1022),
          ("netportAdvertising956", 956),
          ("netscribeServer", 1288),
          ("netsprint", 1044),
          ("netware386", 263),
          ("netwareAccessServer", 152),
          ("netwareBtrieve", 117),
          ("netwareManagement569", 569),
          ("netwareManagement570", 570),
          ("netwareManagementAgent", 611),
          ("netwareManagementLantern567", 567),
          ("netwareManagementLantern568", 568),
          ("netwareServerProduct", 1112),
          ("netwareSql", 118),
          ("netwareToInternetGateway", 2136),
          ("netway2000", 402),
          ("netwaySna", 403),
          ("networkCourier", 153),
          ("networkDynamicDataExchange", 1078),
          ("networkManagement", 968),
          ("networkManagementAgent1179", 1179),
          ("networkManagementAgent563", 563),
          ("networkManagementApplication1473", 1473),
          ("networkManagementApplication1474", 1474),
          ("networkManagementApplication1475", 1475),
          ("networkManagementApplication1476", 1476),
          ("networkManagementApplication1477", 1477),
          ("networkManagementApplication1478", 1478),
          ("networkManagementInfoServer", 564),
          ("networkManagementProduct436", 436),
          ("networkManagementProduct437", 437),
          ("networkManagementProduct438", 438),
          ("networkManagementProduct439", 439),
          ("networkManagementProduct440", 440),
          ("networkManagementServer", 863),
          ("networkManagementServices", 618),
          ("networkManagementSystem", 320),
          ("networkModem1292", 1292),
          ("networkModem1293", 1293),
          ("networkTerminalEmulator", 1076),
          ("networkingHub", 1075),
          ("newswireNotification", 1381),
          ("nlm386", 167),
          ("nlm9101", 9101),
          ("nlm9102", 9102),
          ("nlmAdvertisingForUpsInfo883", 883),
          ("nlmAdvertisingForUpsInfo888", 888),
          ("nlmApplications1869", 1869),
          ("nlmApplications1870", 1870),
          ("nlmApplications1871", 1871),
          ("nlmApplications1872", 1872),
          ("nlmOnFileServer", 1125),
          ("nlmServer1393", 1393),
          ("nlmServer878", 878),
          ("nmsIcons1441", 1441),
          ("nmsIcons1442", 1442),
          ("nmsIcons1443", 1443),
          ("nmsIcons1444", 1444),
          ("nmsIcons1445", 1445),
          ("nmsIcons1446", 1446),
          ("nmsIcons1447", 1447),
          ("nmsIcons1448", 1448),
          ("nmsIcons1449", 1449),
          ("nmsIcons1450", 1450),
          ("nmsIcons1451", 1451),
          ("nmsIcons1452", 1452),
          ("nmsIcons1453", 1453),
          ("nmsIcons1454", 1454),
          ("nmsIcons1455", 1455),
          ("nmsIcons1456", 1456),
          ("nmsIcons1457", 1457),
          ("nmsIcons1458", 1458),
          ("nnsDomain", 307),
          ("nortonAntiVirusClientServerComm", 2034),
          ("novellMhsDsGatewayForOce", 579),
          ("novellRemoteIsdnRouter", 806),
          ("novusGatewayProduct", 1403),
          ("npSqlServer", 512),
          ("npsNetwarePrintServices", 774),
          ("npsSpoolClient", 775),
          ("nvtRemoteLoginOverSpx", 583),
          ("nwManagement", 358),
          ("objectBinderyType", 456),
          ("objectOrientedDatabaseSystem", 1113),
          ("objectStoreServer", 992),
          ("objectType169", 169),
          ("objectType170", 170),
          ("objectType448", 448),
          ("objectType864", 864),
          ("objectType949", 949),
          ("objectType978", 978),
          ("objectType979", 979),
          ("objectTypeForAGroup", 935),
          ("objectTypeForAQueue", 936),
          ("objectTypeForAServer", 937),
          ("objectTypeForGarpServer", 432),
          ("objectTypes449", 449),
          ("objectTypes450", 450),
          ("objectTypes451", 451),
          ("objectTypes452", 452),
          ("objectTypes453", 453),
          ("objectTypes457", 457),
          ("objectTypes458", 458),
          ("ocsSafeserver", 1420),
          ("oemRemoteAccessForEthernet", 1386),
          ("oemRemoteAccessForTokenring", 1387),
          ("offLineCopying", 2077),
          ("officeExtendServer", 1515),
          ("onQueueTaskQueue", 470),
          ("onQueueTaskServer", 471),
          ("onlineTransactionTransportationSystem", 1460),
          ("opticalServer", 1409),
          ("otBloomberg", 1326),
          ("otEllipseServer", 1234),
          ("otMessagingServer", 538),
          ("palindromeServiceBroker", 2087),
          ("pcBasedSnaGateway", 1229),
          ("pcCommunicationPartnerBindery", 1883),
          ("pcCommunicationPartnerSap1881", 1881),
          ("pcCommunicationPartnerSap1882", 1882),
          ("pcMetro398", 398),
          ("pcMetro399", 399),
          ("peerCommunicationsTool", 1398),
          ("peerToPeerFileRedirection", 2153),
          ("performanceMonitor", 955),
          ("pickitCommServer", 360),
          ("piggybackLoginNetInc", 327),
          ("pin64", 2096),
          ("pointOfSaleServer", 970),
          ("pointPoint", 40),
          ("policyEngine1201", 1201),
          ("policyEngine1202", 1202),
          ("policyEngine1203", 1203),
          ("policyEngine1204", 1204),
          ("policyEngine1205", 1205),
          ("policyEngine1206", 1206),
          ("policyEngine2070", 2070),
          ("policyEngine2071", 2071),
          ("policyEngine2072", 2072),
          ("powerProductForFileServer", 1168),
          ("powerchuteAdministrative", 899),
          ("powerchuteAlertUpsMonitoring", 894),
          ("powerchuteVapNlmServerPowerSupply", 161),
          ("printQueue", 3),
          ("printServer1237", 1237),
          ("printServer1299", 1299),
          ("printServer1320", 1320),
          ("printServer1374", 1374),
          ("printServer1375", 1375),
          ("printServer1376", 1376),
          ("printServer1377", 1377),
          ("printServer1427", 1427),
          ("printServer1564", 1564),
          ("printServer1565", 1565),
          ("printServer1566", 1566),
          ("printServer1567", 1567),
          ("printServer1568", 1568),
          ("printServer2016", 2016),
          ("printServer274", 274),
          ("printServer7", 7),
          ("printServerAddOn", 1285),
          ("printServerForNw3X", 2062),
          ("printServerForRemoteWorkstations", 1289),
          ("printServerLaserJet", 867),
          ("printServerRemotePrinter", 1319),
          ("printServers981", 981),
          ("printServers982", 982),
          ("printServers983", 983),
          ("printServers984", 984),
          ("printersPlottersAndRouters", 1365),
          ("progressDatabase", 159),
          ("projectId", 1102),
          ("prorideX500LdapSupport", 1410),
          ("proxyAgentSiteMter", 1968),
          ("qmsPrinterRemoteConfiguration", 1114),
          ("queueManagementServices", 948),
          ("queueServerForIbmPsf2", 584),
          ("queueTypeForLanTimesJapanArticle", 869),
          ("queueTypes", 143),
          ("quickSilver", 780),
          ("r21px", 257),
          ("rdb7000", 2113),
          ("rdb7000ServerForNw", 2138),
          ("realTimeIntegrationServices", 1904),
          ("remarkVoiceServer", 1328),
          ("remoteAccessServer1189", 1189),
          ("remoteAccessServer1262", 1262),
          ("remoteAccessServer1952", 1952),
          ("remoteBackUpDevice", 1173),
          ("remoteBridgeServer", 36),
          ("remoteControlSoftware1265", 1265),
          ("remoteControlSoftware1266", 1266),
          ("remoteDatabaseServices", 991),
          ("remoteDatabaseServicesBindery", 1045),
          ("remoteLoginTerminal", 1324),
          ("remoteManagementOfRemoteAccessServ", 2041),
          ("remotePrinter", 1428),
          ("remotePrinterConsole", 1148),
          ("remoteProcedureCallSystem", 1187),
          ("remotedSmsServer", 1342),
          ("reportEngine", 976),
          ("rightHandManEMailSchedulingPkg", 859),
          ("rm3Configuration", 1354),
          ("rmAuditorMonitoringNwUsage", 2002),
          ("routerAdministrationServer", 1522),
          ("saaDataLinkAgent", 284),
          ("sampleCodeFromDevSupport", 629),
          ("sap", 271),
          ("sapAdvertisingOnPrintServer", 1233),
          ("sapForAudittrackVs20", 2045),
          ("sapForOnguard", 2049),
          ("sapServerType", 631),
          ("sapService1194", 1194),
          ("sapService1195", 1195),
          ("sasConnect", 817),
          ("sasShareServer", 816),
          ("satelliteConnections", 1395),
          ("schema", 1157),
          ("scsiManagement", 1552),
          ("scsiMngmt", 2004),
          ("security", 163),
          ("securityAuditor", 1919),
          ("sequelLinkClientServerMiddleware", 900),
          ("sequelnet", 259),
          ("serverIdForNlm", 946),
          ("serverMnitoringApplication", 1887),
          ("serverMonitoringProgram", 985),
          ("serverType", 446),
          ("serverTypeForLanTimesJapanArticle", 868),
          ("serverlog", 1436),
          ("serviceLocationProtocol", 1440),
          ("serviceNwConnectPwServer", 1964),
          ("servicePoint400", 400),
          ("servicePoint401", 401),
          ("setupManagerAccessControl", 1573),
          ("shareMaster", 407),
          ("sharewareCommunicationsServer", 884),
          ("silaComSoftware", 148),
          ("siteMeterServer", 1967),
          ("slathpStatusNlm", 1429),
          ("smsTestingAndDevelopment574", 574),
          ("smsTestingAndDevelopment575", 575),
          ("smsWorkstationNameObject", 573),
          ("snaGateway", 1092),
          ("snadsProtocolAccessModule", 608),
          ("snapInToolForNms", 2125),
          ("snmp", 613),
          ("snmpConfiguration", 1355),
          ("softTubAgentProxyForTriComAdaptor", 2047),
          ("softwareAccessControlServer", 971),
          ("softwareEntertainment", 2040),
          ("softwareGmbh", 321),
          ("softwareNlmMvdFrm0086794", 1181),
          ("sortingServer", 483),
          ("soundbyteServer", 2152),
          ("spare", 418),
          ("sqlServerIpxSpxHiddenServer", 1174),
          ("sqlVAP", 76),
          ("statisticManagement1263", 1263),
          ("statisticManagement1264", 1264),
          ("statisticsGatheringAgent", 1378),
          ("stealthEventCaptureEngine", 1553),
          ("stocknetBrokerSapType", 86),
          ("stocknetBrokerStatic", 96),
          ("stocknetExchangeStatic", 109),
          ("stocknetExchangerSapType", 87),
          ("stocknetPlayerType", 98),
          ("stocknetQueueType", 97),
          ("storeNameOfSpecialFileOnFileserver", 1161),
          ("stpProtocolServiceAgentCsaFtp", 1875),
          ("stressMagicInstallationUtilityHandle", 2022),
          ("superSnaAgent", 299),
          ("superlabAutomationServer", 617),
          ("superlabFileDistributionServer", 581),
          ("superlabNetworkSwitchServer", 609),
          ("sybaseOpenServer", 1144),
          ("sybaseOpenServerConsole", 1145),
          ("sybaseSqlServer", 1140),
          ("sybaseSqlServerBackUp", 1143),
          ("sybaseSqlServerConsole", 1141),
          ("sybaseSqlServerMonitor", 1142),
          ("sysmLan2", 392),
          ("system9354", 354),
          ("system9355", 355),
          ("system9356", 356),
          ("system9357", 357),
          ("tapeBackUpForNlmApplications1105", 1105),
          ("tapeBackUpForNlmApplications1106", 1106),
          ("tapeBackUpForNlmApplications1107", 1107),
          ("tapeBackUpForNlmApplications1108", 1108),
          ("tapeBackUpForNlmApplications1109", 1109),
          ("tapeBackUpForNlmApplications1110", 1110),
          ("tapeDriveServer", 113),
          ("tapeIdServer", 2133),
          ("taskingIpxLwsiGateway", 1865),
          ("taurusDatabaseServer", 1219),
          ("taurusSerialServer", 1220),
          ("tcpIpGateway39", 39),
          ("tcpIpGateway405", 405),
          ("tcpIpGateway72", 72),
          ("tcpSuperlatHostPrintSap", 1419),
          ("tcsCommunicationServer", 1880),
          ("teamOfficeProduct", 1415),
          ("techraClientServerRdbms", 1349),
          ("telServe", 2018),
          ("telemarketingLibrary", 2019),
          ("telephoneAnsweringSystem", 1128),
          ("telephonyServerMonitor", 2013),
          ("teliLinkVoiceServer", 1298),
          ("telnetIpxRouter", 1392),
          ("termEmulator", 85),
          ("tesNetwareVms", 122),
          ("theMakeServer", 513),
          ("timbuktuAddressResolutions", 1951),
          ("timeCardServer", 1539),
          ("timeServerNlm", 1383),
          ("timeSynchronization", 619),
          ("timeSynchronizationServer", 1126),
          ("timeSynchronizationVap", 45),
          ("titaniumDatabaseEngine", 1879),
          ("tn3270Gateway", 1407),
          ("tnaCommunicationWith2NlmS", 944),
          ("tnetX21Bridge", 145),
          ("tnetX21IdaBridge", 144),
          ("tnsiNetworkUtilities", 1353),
          ("txd", 368),
          ("uOfWisconsinUtilities1920", 1920),
          ("uOfWisconsinUtilities1921", 1921),
          ("uOfWisconsinUtilities1922", 1922),
          ("uOfWisconsinUtilities1923", 1923),
          ("univelServerType1000", 1000),
          ("univelServerType1001", 1001),
          ("univelServerType1002", 1002),
          ("univelServerType1003", 1003),
          ("univelServerType1004", 1004),
          ("univelServerType1005", 1005),
          ("univelServerType1006", 1006),
          ("univelServerType1007", 1007),
          ("univelServerType1008", 1008),
          ("univelServerType993", 993),
          ("univelServerType994", 994),
          ("univelServerType995", 995),
          ("univelServerType996", 996),
          ("univelServerType997", 997),
          ("univelServerType998", 998),
          ("univelServerType999", 999),
          ("universalDataTransporter", 1555),
          ("unixMailServer", 1549),
          ("unixPortableGroup", 158),
          ("upsSnmpMonitorNlm", 1528),
          ("user", 1),
          ("userGroup", 2),
          ("userRestrictions1231", 1231),
          ("userRestrictions1232", 1232),
          ("valueAddedFileSystem", 84),
          ("vapAdvertisingServices768", 768),
          ("vapAdvertisingServices769", 769),
          ("vapAdvertisingServices770", 770),
          ("vapAdvertisingServices771", 771),
          ("vapAdvertisingServices772", 772),
          ("vapAdvertisingServices773", 773),
          ("versionControlQueue", 582),
          ("versionControlServer", 614),
          ("videoServer", 1225),
          ("virusFileList", 3114),
          ("visinetNlmId", 980),
          ("vitalSignsLanServer", 1011),
          ("vmsRouterControl", 149),
          ("voiceFaxRespondingMachine", 1351),
          ("voiceProcessingServer", 2012),
          ("voiceServer", 812),
          ("wanConnectionServer", 957),
          ("wancopyUtility", 114),
          ("watsonCommunicationsServer", 1018),
          ("wicat", 958),
          ("wicatServer", 959),
          ("windowsBulletinBoardSystem", 1525),
          ("windowsNtNamedPipeServer", 1516),
          ("workstationPeerToPeerCommunications", 904),
          ("workstationTerminalAccess", 1093),
          ("x400ProtocolAccessModule", 607),
          ("x500DsaServer", 805),
          ("xBaseDatabaseServer", 1384),
          ("xapiaInterfaceForNw311", 606),
          ("xbaseRecordEngine", 1186),
          ("xtreeNetworkVersion", 77),
          ("xtreeServrMvdFrm", 393),
          ("ziffProprietaryServices", 1382),
          ("zipCodeServer", 2032))
    )


_IpxSAPServerType_Type.__name__ = "Integer32"
_IpxSAPServerType_Object = MibTableColumn
ipxSAPServerType = _IpxSAPServerType_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 2, 1, 1, 4),
    _IpxSAPServerType_Type()
)
ipxSAPServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPServerType.setStatus("mandatory")


class _IpxSAPServerName_Type(DisplayString):
    """Custom type ipxSAPServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_IpxSAPServerName_Type.__name__ = "DisplayString"
_IpxSAPServerName_Object = MibTableColumn
ipxSAPServerName = _IpxSAPServerName_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 2, 1, 1, 5),
    _IpxSAPServerName_Type()
)
ipxSAPServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPServerName.setStatus("mandatory")
_IpxSAPhops_Type = Integer32
_IpxSAPhops_Object = MibTableColumn
ipxSAPhops = _IpxSAPhops_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 2, 1, 1, 6),
    _IpxSAPhops_Type()
)
ipxSAPhops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPhops.setStatus("mandatory")
_IpxRIP_ObjectIdentity = ObjectIdentity
ipxRIP = _IpxRIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 25, 3)
)
_IpxRIPTable_Object = MibTable
ipxRIPTable = _IpxRIPTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 3, 1)
)
if mibBuilder.loadTexts:
    ipxRIPTable.setStatus("mandatory")
_IpxRIPEntry_Object = MibTableRow
ipxRIPEntry = _IpxRIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 3, 1, 1)
)
ipxRIPEntry.setIndexNames(
    (0, "SCA-IPX-MIB", "ipxRIPnet"),
)
if mibBuilder.loadTexts:
    ipxRIPEntry.setStatus("mandatory")


class _IpxRIPnet_Type(OctetString):
    """Custom type ipxRIPnet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRIPnet_Type.__name__ = "OctetString"
_IpxRIPnet_Object = MibTableColumn
ipxRIPnet = _IpxRIPnet_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 3, 1, 1, 1),
    _IpxRIPnet_Type()
)
ipxRIPnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRIPnet.setStatus("mandatory")


class _IpxRIPRouterNet_Type(OctetString):
    """Custom type ipxRIPRouterNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRIPRouterNet_Type.__name__ = "OctetString"
_IpxRIPRouterNet_Object = MibTableColumn
ipxRIPRouterNet = _IpxRIPRouterNet_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 3, 1, 1, 2),
    _IpxRIPRouterNet_Type()
)
ipxRIPRouterNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRIPRouterNet.setStatus("mandatory")


class _IpxRIPRouterNode_Type(OctetString):
    """Custom type ipxRIPRouterNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxRIPRouterNode_Type.__name__ = "OctetString"
_IpxRIPRouterNode_Object = MibTableColumn
ipxRIPRouterNode = _IpxRIPRouterNode_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 3, 1, 1, 3),
    _IpxRIPRouterNode_Type()
)
ipxRIPRouterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRIPRouterNode.setStatus("mandatory")


class _IpxRIPRouterSocket_Type(OctetString):
    """Custom type ipxRIPRouterSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxRIPRouterSocket_Type.__name__ = "OctetString"
_IpxRIPRouterSocket_Object = MibTableColumn
ipxRIPRouterSocket = _IpxRIPRouterSocket_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 3, 1, 1, 4),
    _IpxRIPRouterSocket_Type()
)
ipxRIPRouterSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRIPRouterSocket.setStatus("mandatory")
_IpxRIPhops_Type = Integer32
_IpxRIPhops_Object = MibTableColumn
ipxRIPhops = _IpxRIPhops_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 3, 1, 1, 5),
    _IpxRIPhops_Type()
)
ipxRIPhops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRIPhops.setStatus("mandatory")
_IpxRIPdelay_Type = Integer32
_IpxRIPdelay_Object = MibTableColumn
ipxRIPdelay = _IpxRIPdelay_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 3, 1, 1, 6),
    _IpxRIPdelay_Type()
)
ipxRIPdelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRIPdelay.setStatus("mandatory")
_IpxLink_ObjectIdentity = ObjectIdentity
ipxLink = _IpxLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 25, 4)
)
_IpxLinkTable_Object = MibTable
ipxLinkTable = _IpxLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1)
)
if mibBuilder.loadTexts:
    ipxLinkTable.setStatus("mandatory")
_IpxLinkEntry_Object = MibTableRow
ipxLinkEntry = _IpxLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1)
)
ipxLinkEntry.setIndexNames(
    (0, "SCA-IPX-MIB", "ipxLinkNet"),
    (0, "SCA-IPX-MIB", "ipxLinkIndex"),
)
if mibBuilder.loadTexts:
    ipxLinkEntry.setStatus("mandatory")
_IpxLinkNet_Type = Integer32
_IpxLinkNet_Object = MibTableColumn
ipxLinkNet = _IpxLinkNet_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 1),
    _IpxLinkNet_Type()
)
ipxLinkNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkNet.setStatus("mandatory")
_IpxLinkIndex_Type = Integer32
_IpxLinkIndex_Object = MibTableColumn
ipxLinkIndex = _IpxLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 2),
    _IpxLinkIndex_Type()
)
ipxLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkIndex.setStatus("mandatory")


class _IpxLinkFrameType_Type(Integer32):
    """Custom type ipxLinkFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ieee8022", 2),
          ("ieee8023", 5),
          ("snap", 4),
          ("type", 1),
          ("wan", 16))
    )


_IpxLinkFrameType_Type.__name__ = "Integer32"
_IpxLinkFrameType_Object = MibTableColumn
ipxLinkFrameType = _IpxLinkFrameType_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 3),
    _IpxLinkFrameType_Type()
)
ipxLinkFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkFrameType.setStatus("mandatory")


class _IpxLinkFrameParam_Type(OctetString):
    """Custom type ipxLinkFrameParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IpxLinkFrameParam_Type.__name__ = "OctetString"
_IpxLinkFrameParam_Object = MibTableColumn
ipxLinkFrameParam = _IpxLinkFrameParam_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 4),
    _IpxLinkFrameParam_Type()
)
ipxLinkFrameParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkFrameParam.setStatus("mandatory")


class _IpxLinkState_Type(Integer32):
    """Custom type ipxLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_IpxLinkState_Type.__name__ = "Integer32"
_IpxLinkState_Object = MibTableColumn
ipxLinkState = _IpxLinkState_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 5),
    _IpxLinkState_Type()
)
ipxLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkState.setStatus("mandatory")
_IpxLinkRIPTimer_Type = TimeTicks
_IpxLinkRIPTimer_Object = MibTableColumn
ipxLinkRIPTimer = _IpxLinkRIPTimer_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 6),
    _IpxLinkRIPTimer_Type()
)
ipxLinkRIPTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkRIPTimer.setStatus("mandatory")


class _IpxLinkRIPTrigger_Type(Integer32):
    """Custom type ipxLinkRIPTrigger based on Integer32"""
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


_IpxLinkRIPTrigger_Type.__name__ = "Integer32"
_IpxLinkRIPTrigger_Object = MibTableColumn
ipxLinkRIPTrigger = _IpxLinkRIPTrigger_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 7),
    _IpxLinkRIPTrigger_Type()
)
ipxLinkRIPTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRIPTrigger.setStatus("mandatory")
_IpxLinkSAPTimer_Type = TimeTicks
_IpxLinkSAPTimer_Object = MibTableColumn
ipxLinkSAPTimer = _IpxLinkSAPTimer_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 8),
    _IpxLinkSAPTimer_Type()
)
ipxLinkSAPTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxLinkSAPTimer.setStatus("mandatory")


class _IpxLinkSAPTrigger_Type(Integer32):
    """Custom type ipxLinkSAPTrigger based on Integer32"""
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


_IpxLinkSAPTrigger_Type.__name__ = "Integer32"
_IpxLinkSAPTrigger_Object = MibTableColumn
ipxLinkSAPTrigger = _IpxLinkSAPTrigger_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 9),
    _IpxLinkSAPTrigger_Type()
)
ipxLinkSAPTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkSAPTrigger.setStatus("mandatory")
_IpxLinkCntTxTotal_Type = Counter32
_IpxLinkCntTxTotal_Object = MibTableColumn
ipxLinkCntTxTotal = _IpxLinkCntTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 10),
    _IpxLinkCntTxTotal_Type()
)
ipxLinkCntTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxTotal.setStatus("mandatory")
_IpxLinkCntTxMcast_Type = Counter32
_IpxLinkCntTxMcast_Object = MibTableColumn
ipxLinkCntTxMcast = _IpxLinkCntTxMcast_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 11),
    _IpxLinkCntTxMcast_Type()
)
ipxLinkCntTxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxMcast.setStatus("mandatory")
_IpxLinkCntTxBcast_Type = Counter32
_IpxLinkCntTxBcast_Object = MibTableColumn
ipxLinkCntTxBcast = _IpxLinkCntTxBcast_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 12),
    _IpxLinkCntTxBcast_Type()
)
ipxLinkCntTxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxBcast.setStatus("mandatory")
_IpxLinkCntRxTotal_Type = Counter32
_IpxLinkCntRxTotal_Object = MibTableColumn
ipxLinkCntRxTotal = _IpxLinkCntRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 13),
    _IpxLinkCntRxTotal_Type()
)
ipxLinkCntRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxTotal.setStatus("mandatory")
_IpxLinkCntRxMcast_Type = Counter32
_IpxLinkCntRxMcast_Object = MibTableColumn
ipxLinkCntRxMcast = _IpxLinkCntRxMcast_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 14),
    _IpxLinkCntRxMcast_Type()
)
ipxLinkCntRxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxMcast.setStatus("mandatory")
_IpxLinkCntRxBcast_Type = Counter32
_IpxLinkCntRxBcast_Object = MibTableColumn
ipxLinkCntRxBcast = _IpxLinkCntRxBcast_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 15),
    _IpxLinkCntRxBcast_Type()
)
ipxLinkCntRxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxBcast.setStatus("mandatory")
_IpxLinkCntForward_Type = Counter32
_IpxLinkCntForward_Object = MibTableColumn
ipxLinkCntForward = _IpxLinkCntForward_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 16),
    _IpxLinkCntForward_Type()
)
ipxLinkCntForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntForward.setStatus("mandatory")
_IpxLinkCntFiltered_Type = Counter32
_IpxLinkCntFiltered_Object = MibTableColumn
ipxLinkCntFiltered = _IpxLinkCntFiltered_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 17),
    _IpxLinkCntFiltered_Type()
)
ipxLinkCntFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntFiltered.setStatus("mandatory")
_IpxLinkCntLocal_Type = Counter32
_IpxLinkCntLocal_Object = MibTableColumn
ipxLinkCntLocal = _IpxLinkCntLocal_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 18),
    _IpxLinkCntLocal_Type()
)
ipxLinkCntLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntLocal.setStatus("mandatory")
_IpxLinkCntUnknown_Type = Counter32
_IpxLinkCntUnknown_Object = MibTableColumn
ipxLinkCntUnknown = _IpxLinkCntUnknown_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 19),
    _IpxLinkCntUnknown_Type()
)
ipxLinkCntUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntUnknown.setStatus("mandatory")
_IpxLinkCntDiscarded_Type = Counter32
_IpxLinkCntDiscarded_Object = MibTableColumn
ipxLinkCntDiscarded = _IpxLinkCntDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 20),
    _IpxLinkCntDiscarded_Type()
)
ipxLinkCntDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntDiscarded.setStatus("mandatory")
_IpxLinkCntBadChksum_Type = Counter32
_IpxLinkCntBadChksum_Object = MibTableColumn
ipxLinkCntBadChksum = _IpxLinkCntBadChksum_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 21),
    _IpxLinkCntBadChksum_Type()
)
ipxLinkCntBadChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntBadChksum.setStatus("mandatory")
_IpxLinkCntBadLen_Type = Counter32
_IpxLinkCntBadLen_Object = MibTableColumn
ipxLinkCntBadLen = _IpxLinkCntBadLen_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 22),
    _IpxLinkCntBadLen_Type()
)
ipxLinkCntBadLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntBadLen.setStatus("mandatory")
_IpxLinkCntBadHop_Type = Counter32
_IpxLinkCntBadHop_Object = MibTableColumn
ipxLinkCntBadHop = _IpxLinkCntBadHop_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 23),
    _IpxLinkCntBadHop_Type()
)
ipxLinkCntBadHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntBadHop.setStatus("mandatory")
_IpxLinkCntNoRoute_Type = Counter32
_IpxLinkCntNoRoute_Object = MibTableColumn
ipxLinkCntNoRoute = _IpxLinkCntNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 24),
    _IpxLinkCntNoRoute_Type()
)
ipxLinkCntNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntNoRoute.setStatus("mandatory")
_IpxLinkCntTooBig_Type = Counter32
_IpxLinkCntTooBig_Object = MibTableColumn
ipxLinkCntTooBig = _IpxLinkCntTooBig_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 25),
    _IpxLinkCntTooBig_Type()
)
ipxLinkCntTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTooBig.setStatus("mandatory")
_IpxLinkCntRxSapReq_Type = Counter32
_IpxLinkCntRxSapReq_Object = MibTableColumn
ipxLinkCntRxSapReq = _IpxLinkCntRxSapReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 26),
    _IpxLinkCntRxSapReq_Type()
)
ipxLinkCntRxSapReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxSapReq.setStatus("mandatory")
_IpxLinkCntRxSapRsp_Type = Counter32
_IpxLinkCntRxSapRsp_Object = MibTableColumn
ipxLinkCntRxSapRsp = _IpxLinkCntRxSapRsp_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 27),
    _IpxLinkCntRxSapRsp_Type()
)
ipxLinkCntRxSapRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxSapRsp.setStatus("mandatory")
_IpxLinkCntTxSapReq_Type = Counter32
_IpxLinkCntTxSapReq_Object = MibTableColumn
ipxLinkCntTxSapReq = _IpxLinkCntTxSapReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 28),
    _IpxLinkCntTxSapReq_Type()
)
ipxLinkCntTxSapReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxSapReq.setStatus("mandatory")
_IpxLinkCntTxSapRpl_Type = Counter32
_IpxLinkCntTxSapRpl_Object = MibTableColumn
ipxLinkCntTxSapRpl = _IpxLinkCntTxSapRpl_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 29),
    _IpxLinkCntTxSapRpl_Type()
)
ipxLinkCntTxSapRpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxSapRpl.setStatus("mandatory")
_IpxLinkCntSapInvalid_Type = Counter32
_IpxLinkCntSapInvalid_Object = MibTableColumn
ipxLinkCntSapInvalid = _IpxLinkCntSapInvalid_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 30),
    _IpxLinkCntSapInvalid_Type()
)
ipxLinkCntSapInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntSapInvalid.setStatus("mandatory")
_IpxLinkCntRxRipReq_Type = Counter32
_IpxLinkCntRxRipReq_Object = MibTableColumn
ipxLinkCntRxRipReq = _IpxLinkCntRxRipReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 31),
    _IpxLinkCntRxRipReq_Type()
)
ipxLinkCntRxRipReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxRipReq.setStatus("mandatory")
_IpxLinkCntRxRipRsp_Type = Counter32
_IpxLinkCntRxRipRsp_Object = MibTableColumn
ipxLinkCntRxRipRsp = _IpxLinkCntRxRipRsp_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 32),
    _IpxLinkCntRxRipRsp_Type()
)
ipxLinkCntRxRipRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRxRipRsp.setStatus("mandatory")
_IpxLinkCntTxRipReq_Type = Counter32
_IpxLinkCntTxRipReq_Object = MibTableColumn
ipxLinkCntTxRipReq = _IpxLinkCntTxRipReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 33),
    _IpxLinkCntTxRipReq_Type()
)
ipxLinkCntTxRipReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxRipReq.setStatus("mandatory")
_IpxLinkCntTxRipRpl_Type = Counter32
_IpxLinkCntTxRipRpl_Object = MibTableColumn
ipxLinkCntTxRipRpl = _IpxLinkCntTxRipRpl_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 34),
    _IpxLinkCntTxRipRpl_Type()
)
ipxLinkCntTxRipRpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntTxRipRpl.setStatus("mandatory")
_IpxLinkCntRipInvalid_Type = Counter32
_IpxLinkCntRipInvalid_Object = MibTableColumn
ipxLinkCntRipInvalid = _IpxLinkCntRipInvalid_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 35),
    _IpxLinkCntRipInvalid_Type()
)
ipxLinkCntRipInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCntRipInvalid.setStatus("mandatory")
_IpxLinkTxFailed_Type = Counter32
_IpxLinkTxFailed_Object = MibTableColumn
ipxLinkTxFailed = _IpxLinkTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 36),
    _IpxLinkTxFailed_Type()
)
ipxLinkTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxFailed.setStatus("mandatory")
_IpxLinkTxPrefFailed_Type = Counter32
_IpxLinkTxPrefFailed_Object = MibTableColumn
ipxLinkTxPrefFailed = _IpxLinkTxPrefFailed_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 37),
    _IpxLinkTxPrefFailed_Type()
)
ipxLinkTxPrefFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxPrefFailed.setStatus("mandatory")
_IpxLinkRxFiltered_Type = Counter32
_IpxLinkRxFiltered_Object = MibTableColumn
ipxLinkRxFiltered = _IpxLinkRxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 38),
    _IpxLinkRxFiltered_Type()
)
ipxLinkRxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRxFiltered.setStatus("mandatory")
_IpxLinkTxFiltered_Type = Counter32
_IpxLinkTxFiltered_Object = MibTableColumn
ipxLinkTxFiltered = _IpxLinkTxFiltered_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 39),
    _IpxLinkTxFiltered_Type()
)
ipxLinkTxFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxFiltered.setStatus("mandatory")
_IpxLinkForwarded_Type = Counter32
_IpxLinkForwarded_Object = MibTableColumn
ipxLinkForwarded = _IpxLinkForwarded_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 40),
    _IpxLinkForwarded_Type()
)
ipxLinkForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkForwarded.setStatus("mandatory")
_IpxLinkCacheHits_Type = Counter32
_IpxLinkCacheHits_Object = MibTableColumn
ipxLinkCacheHits = _IpxLinkCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 41),
    _IpxLinkCacheHits_Type()
)
ipxLinkCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkCacheHits.setStatus("mandatory")
_IpxLinkSpoofed_Type = Counter32
_IpxLinkSpoofed_Object = MibTableColumn
ipxLinkSpoofed = _IpxLinkSpoofed_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 42),
    _IpxLinkSpoofed_Type()
)
ipxLinkSpoofed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkSpoofed.setStatus("mandatory")
_IpxLinkSPXCacheHits_Type = Counter32
_IpxLinkSPXCacheHits_Object = MibTableColumn
ipxLinkSPXCacheHits = _IpxLinkSPXCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 43),
    _IpxLinkSPXCacheHits_Type()
)
ipxLinkSPXCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkSPXCacheHits.setStatus("mandatory")
_IpxLinkType20Rx_Type = Counter32
_IpxLinkType20Rx_Object = MibTableColumn
ipxLinkType20Rx = _IpxLinkType20Rx_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 44),
    _IpxLinkType20Rx_Type()
)
ipxLinkType20Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkType20Rx.setStatus("mandatory")
_IpxLinkType20Tx_Type = Counter32
_IpxLinkType20Tx_Object = MibTableColumn
ipxLinkType20Tx = _IpxLinkType20Tx_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 45),
    _IpxLinkType20Tx_Type()
)
ipxLinkType20Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkType20Tx.setStatus("mandatory")
_IpxLinkType20Disc_Type = Counter32
_IpxLinkType20Disc_Object = MibTableColumn
ipxLinkType20Disc = _IpxLinkType20Disc_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 46),
    _IpxLinkType20Disc_Type()
)
ipxLinkType20Disc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkType20Disc.setStatus("mandatory")
_IpxLinkRxBytesOther_Type = Counter32
_IpxLinkRxBytesOther_Object = MibTableColumn
ipxLinkRxBytesOther = _IpxLinkRxBytesOther_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 47),
    _IpxLinkRxBytesOther_Type()
)
ipxLinkRxBytesOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRxBytesOther.setStatus("mandatory")
_IpxLinkRxBytesNCP_Type = Counter32
_IpxLinkRxBytesNCP_Object = MibTableColumn
ipxLinkRxBytesNCP = _IpxLinkRxBytesNCP_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 48),
    _IpxLinkRxBytesNCP_Type()
)
ipxLinkRxBytesNCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRxBytesNCP.setStatus("mandatory")
_IpxLinkRxBytesSPX_Type = Counter32
_IpxLinkRxBytesSPX_Object = MibTableColumn
ipxLinkRxBytesSPX = _IpxLinkRxBytesSPX_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 49),
    _IpxLinkRxBytesSPX_Type()
)
ipxLinkRxBytesSPX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRxBytesSPX.setStatus("mandatory")
_IpxLinkRxBytesNetbios_Type = Counter32
_IpxLinkRxBytesNetbios_Object = MibTableColumn
ipxLinkRxBytesNetbios = _IpxLinkRxBytesNetbios_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 50),
    _IpxLinkRxBytesNetbios_Type()
)
ipxLinkRxBytesNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRxBytesNetbios.setStatus("mandatory")
_IpxLinkRxBytesRIP_Type = Counter32
_IpxLinkRxBytesRIP_Object = MibTableColumn
ipxLinkRxBytesRIP = _IpxLinkRxBytesRIP_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 51),
    _IpxLinkRxBytesRIP_Type()
)
ipxLinkRxBytesRIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRxBytesRIP.setStatus("mandatory")
_IpxLinkRxBytesSAP_Type = Counter32
_IpxLinkRxBytesSAP_Object = MibTableColumn
ipxLinkRxBytesSAP = _IpxLinkRxBytesSAP_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 52),
    _IpxLinkRxBytesSAP_Type()
)
ipxLinkRxBytesSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRxBytesSAP.setStatus("mandatory")
_IpxLinkRxBytesType20_Type = Counter32
_IpxLinkRxBytesType20_Object = MibTableColumn
ipxLinkRxBytesType20 = _IpxLinkRxBytesType20_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 53),
    _IpxLinkRxBytesType20_Type()
)
ipxLinkRxBytesType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRxBytesType20.setStatus("mandatory")
_IpxLinkTxBytesOther_Type = Counter32
_IpxLinkTxBytesOther_Object = MibTableColumn
ipxLinkTxBytesOther = _IpxLinkTxBytesOther_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 54),
    _IpxLinkTxBytesOther_Type()
)
ipxLinkTxBytesOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxBytesOther.setStatus("mandatory")
_IpxLinkTxBytesNCP_Type = Counter32
_IpxLinkTxBytesNCP_Object = MibTableColumn
ipxLinkTxBytesNCP = _IpxLinkTxBytesNCP_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 55),
    _IpxLinkTxBytesNCP_Type()
)
ipxLinkTxBytesNCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxBytesNCP.setStatus("mandatory")
_IpxLinkTxBytesSPX_Type = Counter32
_IpxLinkTxBytesSPX_Object = MibTableColumn
ipxLinkTxBytesSPX = _IpxLinkTxBytesSPX_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 56),
    _IpxLinkTxBytesSPX_Type()
)
ipxLinkTxBytesSPX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxBytesSPX.setStatus("mandatory")
_IpxLinkTxBytesNetbios_Type = Counter32
_IpxLinkTxBytesNetbios_Object = MibTableColumn
ipxLinkTxBytesNetbios = _IpxLinkTxBytesNetbios_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 57),
    _IpxLinkTxBytesNetbios_Type()
)
ipxLinkTxBytesNetbios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxBytesNetbios.setStatus("mandatory")
_IpxLinkTxBytesRIP_Type = Counter32
_IpxLinkTxBytesRIP_Object = MibTableColumn
ipxLinkTxBytesRIP = _IpxLinkTxBytesRIP_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 58),
    _IpxLinkTxBytesRIP_Type()
)
ipxLinkTxBytesRIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxBytesRIP.setStatus("mandatory")
_IpxLinkTxBytesSAP_Type = Counter32
_IpxLinkTxBytesSAP_Object = MibTableColumn
ipxLinkTxBytesSAP = _IpxLinkTxBytesSAP_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 59),
    _IpxLinkTxBytesSAP_Type()
)
ipxLinkTxBytesSAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxBytesSAP.setStatus("mandatory")
_IpxLinkTxBytesType20_Type = Counter32
_IpxLinkTxBytesType20_Object = MibTableColumn
ipxLinkTxBytesType20 = _IpxLinkTxBytesType20_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 60),
    _IpxLinkTxBytesType20_Type()
)
ipxLinkTxBytesType20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxBytesType20.setStatus("mandatory")
_IpxLinkRxBytesTotal_Type = Counter32
_IpxLinkRxBytesTotal_Object = MibTableColumn
ipxLinkRxBytesTotal = _IpxLinkRxBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 61),
    _IpxLinkRxBytesTotal_Type()
)
ipxLinkRxBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkRxBytesTotal.setStatus("mandatory")
_IpxLinkTxBytesTotal_Type = Counter32
_IpxLinkTxBytesTotal_Object = MibTableColumn
ipxLinkTxBytesTotal = _IpxLinkTxBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 4, 1, 1, 62),
    _IpxLinkTxBytesTotal_Type()
)
ipxLinkTxBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxLinkTxBytesTotal.setStatus("mandatory")
_IpxControl_ObjectIdentity = ObjectIdentity
ipxControl = _IpxControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 25, 5)
)
_IpxControlCommand_Type = Integer32
_IpxControlCommand_Object = MibScalar
ipxControlCommand = _IpxControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 208, 25, 5, 1),
    _IpxControlCommand_Type()
)
ipxControlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxControlCommand.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCA-IPX-MIB",
    **{"ipx": ipx,
       "ipxCounters": ipxCounters,
       "ipxCntTxTotal": ipxCntTxTotal,
       "ipxCntTxMcast": ipxCntTxMcast,
       "ipxCntTxBcast": ipxCntTxBcast,
       "ipxCntRxTotal": ipxCntRxTotal,
       "ipxCntRxMcast": ipxCntRxMcast,
       "ipxCntRxBcast": ipxCntRxBcast,
       "ipxCntForward": ipxCntForward,
       "ipxCntFiltered": ipxCntFiltered,
       "ipxCntLocal": ipxCntLocal,
       "ipxCntUnknown": ipxCntUnknown,
       "ipxCntDiscarded": ipxCntDiscarded,
       "ipxCntBadChksum": ipxCntBadChksum,
       "ipxCntBadLen": ipxCntBadLen,
       "ipxCntBadHop": ipxCntBadHop,
       "ipxCntNoRoute": ipxCntNoRoute,
       "ipxCntTooBig": ipxCntTooBig,
       "ipxCntRxSapReq": ipxCntRxSapReq,
       "ipxRxCntSapRsp": ipxRxCntSapRsp,
       "ipxTxCntSapReq": ipxTxCntSapReq,
       "ipxCntTxSapRpl": ipxCntTxSapRpl,
       "ipxCntSapInvalid": ipxCntSapInvalid,
       "ipxCntRxRipReq": ipxCntRxRipReq,
       "ipxCntRxRipRsp": ipxCntRxRipRsp,
       "ipxCntTxRipReq": ipxCntTxRipReq,
       "ipxCntTxRipRpl": ipxCntTxRipRpl,
       "ipxCntRipInvalid": ipxCntRipInvalid,
       "ipxCntTxFailed": ipxCntTxFailed,
       "ipxCntTxPrefFailed": ipxCntTxPrefFailed,
       "ipxCntRxFiltered": ipxCntRxFiltered,
       "ipxCntTxFiltered": ipxCntTxFiltered,
       "ipxCntForwarded": ipxCntForwarded,
       "ipxCntCacheHits": ipxCntCacheHits,
       "ipxCntSpoofed": ipxCntSpoofed,
       "ipxCntSPXCacheHits": ipxCntSPXCacheHits,
       "ipxCntRxType20": ipxCntRxType20,
       "ipxCntTxType20": ipxCntTxType20,
       "ipxCntType20Disc": ipxCntType20Disc,
       "ipxCntConfigTimeStamp": ipxCntConfigTimeStamp,
       "ipxSAP": ipxSAP,
       "ipxSAPTable": ipxSAPTable,
       "ipxSAPEntry": ipxSAPEntry,
       "ipxSAPServerNet": ipxSAPServerNet,
       "ipxSAPServerNode": ipxSAPServerNode,
       "ipxSAPServerSocket": ipxSAPServerSocket,
       "ipxSAPServerType": ipxSAPServerType,
       "ipxSAPServerName": ipxSAPServerName,
       "ipxSAPhops": ipxSAPhops,
       "ipxRIP": ipxRIP,
       "ipxRIPTable": ipxRIPTable,
       "ipxRIPEntry": ipxRIPEntry,
       "ipxRIPnet": ipxRIPnet,
       "ipxRIPRouterNet": ipxRIPRouterNet,
       "ipxRIPRouterNode": ipxRIPRouterNode,
       "ipxRIPRouterSocket": ipxRIPRouterSocket,
       "ipxRIPhops": ipxRIPhops,
       "ipxRIPdelay": ipxRIPdelay,
       "ipxLink": ipxLink,
       "ipxLinkTable": ipxLinkTable,
       "ipxLinkEntry": ipxLinkEntry,
       "ipxLinkNet": ipxLinkNet,
       "ipxLinkIndex": ipxLinkIndex,
       "ipxLinkFrameType": ipxLinkFrameType,
       "ipxLinkFrameParam": ipxLinkFrameParam,
       "ipxLinkState": ipxLinkState,
       "ipxLinkRIPTimer": ipxLinkRIPTimer,
       "ipxLinkRIPTrigger": ipxLinkRIPTrigger,
       "ipxLinkSAPTimer": ipxLinkSAPTimer,
       "ipxLinkSAPTrigger": ipxLinkSAPTrigger,
       "ipxLinkCntTxTotal": ipxLinkCntTxTotal,
       "ipxLinkCntTxMcast": ipxLinkCntTxMcast,
       "ipxLinkCntTxBcast": ipxLinkCntTxBcast,
       "ipxLinkCntRxTotal": ipxLinkCntRxTotal,
       "ipxLinkCntRxMcast": ipxLinkCntRxMcast,
       "ipxLinkCntRxBcast": ipxLinkCntRxBcast,
       "ipxLinkCntForward": ipxLinkCntForward,
       "ipxLinkCntFiltered": ipxLinkCntFiltered,
       "ipxLinkCntLocal": ipxLinkCntLocal,
       "ipxLinkCntUnknown": ipxLinkCntUnknown,
       "ipxLinkCntDiscarded": ipxLinkCntDiscarded,
       "ipxLinkCntBadChksum": ipxLinkCntBadChksum,
       "ipxLinkCntBadLen": ipxLinkCntBadLen,
       "ipxLinkCntBadHop": ipxLinkCntBadHop,
       "ipxLinkCntNoRoute": ipxLinkCntNoRoute,
       "ipxLinkCntTooBig": ipxLinkCntTooBig,
       "ipxLinkCntRxSapReq": ipxLinkCntRxSapReq,
       "ipxLinkCntRxSapRsp": ipxLinkCntRxSapRsp,
       "ipxLinkCntTxSapReq": ipxLinkCntTxSapReq,
       "ipxLinkCntTxSapRpl": ipxLinkCntTxSapRpl,
       "ipxLinkCntSapInvalid": ipxLinkCntSapInvalid,
       "ipxLinkCntRxRipReq": ipxLinkCntRxRipReq,
       "ipxLinkCntRxRipRsp": ipxLinkCntRxRipRsp,
       "ipxLinkCntTxRipReq": ipxLinkCntTxRipReq,
       "ipxLinkCntTxRipRpl": ipxLinkCntTxRipRpl,
       "ipxLinkCntRipInvalid": ipxLinkCntRipInvalid,
       "ipxLinkTxFailed": ipxLinkTxFailed,
       "ipxLinkTxPrefFailed": ipxLinkTxPrefFailed,
       "ipxLinkRxFiltered": ipxLinkRxFiltered,
       "ipxLinkTxFiltered": ipxLinkTxFiltered,
       "ipxLinkForwarded": ipxLinkForwarded,
       "ipxLinkCacheHits": ipxLinkCacheHits,
       "ipxLinkSpoofed": ipxLinkSpoofed,
       "ipxLinkSPXCacheHits": ipxLinkSPXCacheHits,
       "ipxLinkType20Rx": ipxLinkType20Rx,
       "ipxLinkType20Tx": ipxLinkType20Tx,
       "ipxLinkType20Disc": ipxLinkType20Disc,
       "ipxLinkRxBytesOther": ipxLinkRxBytesOther,
       "ipxLinkRxBytesNCP": ipxLinkRxBytesNCP,
       "ipxLinkRxBytesSPX": ipxLinkRxBytesSPX,
       "ipxLinkRxBytesNetbios": ipxLinkRxBytesNetbios,
       "ipxLinkRxBytesRIP": ipxLinkRxBytesRIP,
       "ipxLinkRxBytesSAP": ipxLinkRxBytesSAP,
       "ipxLinkRxBytesType20": ipxLinkRxBytesType20,
       "ipxLinkTxBytesOther": ipxLinkTxBytesOther,
       "ipxLinkTxBytesNCP": ipxLinkTxBytesNCP,
       "ipxLinkTxBytesSPX": ipxLinkTxBytesSPX,
       "ipxLinkTxBytesNetbios": ipxLinkTxBytesNetbios,
       "ipxLinkTxBytesRIP": ipxLinkTxBytesRIP,
       "ipxLinkTxBytesSAP": ipxLinkTxBytesSAP,
       "ipxLinkTxBytesType20": ipxLinkTxBytesType20,
       "ipxLinkRxBytesTotal": ipxLinkRxBytesTotal,
       "ipxLinkTxBytesTotal": ipxLinkTxBytesTotal,
       "ipxControl": ipxControl,
       "ipxControlCommand": ipxControlCommand}
)
