# SNMP MIB module (MIB-INTEL-OSPF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIB-INTEL-OSPF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:29 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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

_Ospf_ObjectIdentity = ObjectIdentity
ospf = _Ospf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 40)
)
_OspfIpRouteTable_Object = MibTable
ospfIpRouteTable = _OspfIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1)
)
if mibBuilder.loadTexts:
    ospfIpRouteTable.setStatus("optional")
_OspfIpRouteEntry_Object = MibTableRow
ospfIpRouteEntry = _OspfIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1)
)
ospfIpRouteEntry.setIndexNames(
    (0, "MIB-INTEL-OSPF", "ospfIpRouteChassis"),
    (0, "MIB-INTEL-OSPF", "ospfIpRouteModule"),
    (0, "MIB-INTEL-OSPF", "ospfIpRouteInst"),
    (0, "MIB-INTEL-OSPF", "ospfIpRouteDest"),
    (0, "MIB-INTEL-OSPF", "ospfIpRouteMask"),
    (0, "MIB-INTEL-OSPF", "ospfIpRouteIfIndex"),
    (0, "MIB-INTEL-OSPF", "ospfIpRouteNextHop"),
)
if mibBuilder.loadTexts:
    ospfIpRouteEntry.setStatus("optional")
_OspfIpRouteChassis_Type = Integer32
_OspfIpRouteChassis_Object = MibTableColumn
ospfIpRouteChassis = _OspfIpRouteChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 1),
    _OspfIpRouteChassis_Type()
)
ospfIpRouteChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteChassis.setStatus("optional")
_OspfIpRouteModule_Type = Integer32
_OspfIpRouteModule_Object = MibTableColumn
ospfIpRouteModule = _OspfIpRouteModule_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 2),
    _OspfIpRouteModule_Type()
)
ospfIpRouteModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteModule.setStatus("optional")
_OspfIpRouteInst_Type = Integer32
_OspfIpRouteInst_Object = MibTableColumn
ospfIpRouteInst = _OspfIpRouteInst_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 3),
    _OspfIpRouteInst_Type()
)
ospfIpRouteInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteInst.setStatus("optional")
_OspfIpRouteDest_Type = IpAddress
_OspfIpRouteDest_Object = MibTableColumn
ospfIpRouteDest = _OspfIpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 4),
    _OspfIpRouteDest_Type()
)
ospfIpRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteDest.setStatus("optional")
_OspfIpRouteMask_Type = IpAddress
_OspfIpRouteMask_Object = MibTableColumn
ospfIpRouteMask = _OspfIpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 5),
    _OspfIpRouteMask_Type()
)
ospfIpRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteMask.setStatus("optional")
_OspfIpRouteIfIndex_Type = Integer32
_OspfIpRouteIfIndex_Object = MibTableColumn
ospfIpRouteIfIndex = _OspfIpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 6),
    _OspfIpRouteIfIndex_Type()
)
ospfIpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteIfIndex.setStatus("optional")
_OspfIpRouteNextHop_Type = IpAddress
_OspfIpRouteNextHop_Object = MibTableColumn
ospfIpRouteNextHop = _OspfIpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 7),
    _OspfIpRouteNextHop_Type()
)
ospfIpRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteNextHop.setStatus("optional")
_OspfIpRoutePref_Type = Integer32
_OspfIpRoutePref_Object = MibTableColumn
ospfIpRoutePref = _OspfIpRoutePref_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 8),
    _OspfIpRoutePref_Type()
)
ospfIpRoutePref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRoutePref.setStatus("optional")
_OspfIpRouteCost_Type = Integer32
_OspfIpRouteCost_Object = MibTableColumn
ospfIpRouteCost = _OspfIpRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 9),
    _OspfIpRouteCost_Type()
)
ospfIpRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteCost.setStatus("optional")


class _OspfIpRouteState_Type(Integer32):
    """Custom type ospfIpRouteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("dead", 3),
          ("inactive", 2))
    )


_OspfIpRouteState_Type.__name__ = "Integer32"
_OspfIpRouteState_Object = MibTableColumn
ospfIpRouteState = _OspfIpRouteState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 10),
    _OspfIpRouteState_Type()
)
ospfIpRouteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIpRouteState.setStatus("optional")
_OspfIpRouteAge_Type = Integer32
_OspfIpRouteAge_Object = MibTableColumn
ospfIpRouteAge = _OspfIpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 11),
    _OspfIpRouteAge_Type()
)
ospfIpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteAge.setStatus("optional")


class _OspfIpRouteProtoType_Type(Integer32):
    """Custom type ospfIpRouteProtoType based on Integer32"""
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
        *(("ext1", 3),
          ("ext2", 4),
          ("interArea", 2),
          ("intraArea", 1),
          ("other", 7),
          ("type3Discard", 5),
          ("type7Discard", 6))
    )


_OspfIpRouteProtoType_Type.__name__ = "Integer32"
_OspfIpRouteProtoType_Object = MibTableColumn
ospfIpRouteProtoType = _OspfIpRouteProtoType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 12),
    _OspfIpRouteProtoType_Type()
)
ospfIpRouteProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIpRouteProtoType.setStatus("optional")
_OspfIfCntTable_Object = MibTable
ospfIfCntTable = _OspfIfCntTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2)
)
if mibBuilder.loadTexts:
    ospfIfCntTable.setStatus("optional")
_OspfIfCntEntry_Object = MibTableRow
ospfIfCntEntry = _OspfIfCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1)
)
ospfIfCntEntry.setIndexNames(
    (0, "MIB-INTEL-OSPF", "ospfCntChassis"),
    (0, "MIB-INTEL-OSPF", "ospfCntModule"),
    (0, "MIB-INTEL-OSPF", "ospfCntIfIpAddress"),
    (0, "MIB-INTEL-OSPF", "ospfCntAddressLessIf"),
)
if mibBuilder.loadTexts:
    ospfIfCntEntry.setStatus("optional")
_OspfCntChassis_Type = Integer32
_OspfCntChassis_Object = MibTableColumn
ospfCntChassis = _OspfCntChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 1),
    _OspfCntChassis_Type()
)
ospfCntChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCntChassis.setStatus("optional")
_OspfCntModule_Type = Integer32
_OspfCntModule_Object = MibTableColumn
ospfCntModule = _OspfCntModule_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 2),
    _OspfCntModule_Type()
)
ospfCntModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCntModule.setStatus("optional")
_OspfCntIfIpAddress_Type = IpAddress
_OspfCntIfIpAddress_Object = MibTableColumn
ospfCntIfIpAddress = _OspfCntIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 3),
    _OspfCntIfIpAddress_Type()
)
ospfCntIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCntIfIpAddress.setStatus("optional")
_OspfCntAddressLessIf_Type = Integer32
_OspfCntAddressLessIf_Object = MibTableColumn
ospfCntAddressLessIf = _OspfCntAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 4),
    _OspfCntAddressLessIf_Type()
)
ospfCntAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCntAddressLessIf.setStatus("optional")
_OspfCntBadVer_Type = Counter32
_OspfCntBadVer_Object = MibTableColumn
ospfCntBadVer = _OspfCntBadVer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 5),
    _OspfCntBadVer_Type()
)
ospfCntBadVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntBadVer.setStatus("optional")
_OspfCntBadAreaId_Type = Counter32
_OspfCntBadAreaId_Object = MibTableColumn
ospfCntBadAreaId = _OspfCntBadAreaId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 6),
    _OspfCntBadAreaId_Type()
)
ospfCntBadAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntBadAreaId.setStatus("optional")
_OspfCntMaskMismatch_Type = Counter32
_OspfCntMaskMismatch_Object = MibTableColumn
ospfCntMaskMismatch = _OspfCntMaskMismatch_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 7),
    _OspfCntMaskMismatch_Type()
)
ospfCntMaskMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntMaskMismatch.setStatus("optional")
_OspfCntAuthMismatch_Type = Counter32
_OspfCntAuthMismatch_Object = MibTableColumn
ospfCntAuthMismatch = _OspfCntAuthMismatch_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 8),
    _OspfCntAuthMismatch_Type()
)
ospfCntAuthMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntAuthMismatch.setStatus("optional")
_OspfCntAuthFail_Type = Counter32
_OspfCntAuthFail_Object = MibTableColumn
ospfCntAuthFail = _OspfCntAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 9),
    _OspfCntAuthFail_Type()
)
ospfCntAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntAuthFail.setStatus("optional")
_OspfCntExtOptMismatch_Type = Counter32
_OspfCntExtOptMismatch_Object = MibTableColumn
ospfCntExtOptMismatch = _OspfCntExtOptMismatch_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 10),
    _OspfCntExtOptMismatch_Type()
)
ospfCntExtOptMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntExtOptMismatch.setStatus("optional")
_OspfCntNSSAOptMismatch_Type = Counter32
_OspfCntNSSAOptMismatch_Object = MibTableColumn
ospfCntNSSAOptMismatch = _OspfCntNSSAOptMismatch_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 11),
    _OspfCntNSSAOptMismatch_Type()
)
ospfCntNSSAOptMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntNSSAOptMismatch.setStatus("optional")
_OspfCntNBMANeighbor_Type = Counter32
_OspfCntNBMANeighbor_Object = MibTableColumn
ospfCntNBMANeighbor = _OspfCntNBMANeighbor_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 12),
    _OspfCntNBMANeighbor_Type()
)
ospfCntNBMANeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntNBMANeighbor.setStatus("optional")
_OspfCntVirtNeighbor_Type = Counter32
_OspfCntVirtNeighbor_Object = MibTableColumn
ospfCntVirtNeighbor = _OspfCntVirtNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 13),
    _OspfCntVirtNeighbor_Type()
)
ospfCntVirtNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntVirtNeighbor.setStatus("optional")
_OspfCntHelloMismatch_Type = Counter32
_OspfCntHelloMismatch_Object = MibTableColumn
ospfCntHelloMismatch = _OspfCntHelloMismatch_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 14),
    _OspfCntHelloMismatch_Type()
)
ospfCntHelloMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntHelloMismatch.setStatus("optional")
_OspfCntDeadMismatch_Type = Counter32
_OspfCntDeadMismatch_Object = MibTableColumn
ospfCntDeadMismatch = _OspfCntDeadMismatch_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 15),
    _OspfCntDeadMismatch_Type()
)
ospfCntDeadMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntDeadMismatch.setStatus("optional")
_OspfCntBadType_Type = Counter32
_OspfCntBadType_Object = MibTableColumn
ospfCntBadType = _OspfCntBadType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 16),
    _OspfCntBadType_Type()
)
ospfCntBadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntBadType.setStatus("optional")
_OspfCntBadChksum_Type = Counter32
_OspfCntBadChksum_Object = MibTableColumn
ospfCntBadChksum = _OspfCntBadChksum_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 17),
    _OspfCntBadChksum_Type()
)
ospfCntBadChksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntBadChksum.setStatus("optional")
_OspfCntBadLen_Type = Counter32
_OspfCntBadLen_Object = MibTableColumn
ospfCntBadLen = _OspfCntBadLen_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 18),
    _OspfCntBadLen_Type()
)
ospfCntBadLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntBadLen.setStatus("optional")
_OspfCntTooShort_Type = Counter32
_OspfCntTooShort_Object = MibTableColumn
ospfCntTooShort = _OspfCntTooShort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 19),
    _OspfCntTooShort_Type()
)
ospfCntTooShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntTooShort.setStatus("optional")
_OspfCntDRPktMismatch_Type = Counter32
_OspfCntDRPktMismatch_Object = MibTableColumn
ospfCntDRPktMismatch = _OspfCntDRPktMismatch_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 20),
    _OspfCntDRPktMismatch_Type()
)
ospfCntDRPktMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntDRPktMismatch.setStatus("optional")
_OspfCntMulticastVL_Type = Counter32
_OspfCntMulticastVL_Object = MibTableColumn
ospfCntMulticastVL = _OspfCntMulticastVL_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 21),
    _OspfCntMulticastVL_Type()
)
ospfCntMulticastVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntMulticastVL.setStatus("optional")
_OspfCntDestAddr_Type = Counter32
_OspfCntDestAddr_Object = MibTableColumn
ospfCntDestAddr = _OspfCntDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 22),
    _OspfCntDestAddr_Type()
)
ospfCntDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntDestAddr.setStatus("optional")
_OspfCntOwnAddr_Type = Counter32
_OspfCntOwnAddr_Object = MibTableColumn
ospfCntOwnAddr = _OspfCntOwnAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 23),
    _OspfCntOwnAddr_Type()
)
ospfCntOwnAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntOwnAddr.setStatus("optional")
_OspfCntHelloTx_Type = Counter32
_OspfCntHelloTx_Object = MibTableColumn
ospfCntHelloTx = _OspfCntHelloTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 24),
    _OspfCntHelloTx_Type()
)
ospfCntHelloTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntHelloTx.setStatus("optional")
_OspfCntHelloRx_Type = Counter32
_OspfCntHelloRx_Object = MibTableColumn
ospfCntHelloRx = _OspfCntHelloRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 25),
    _OspfCntHelloRx_Type()
)
ospfCntHelloRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntHelloRx.setStatus("optional")
_OspfCntLSReqTx_Type = Counter32
_OspfCntLSReqTx_Object = MibTableColumn
ospfCntLSReqTx = _OspfCntLSReqTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 26),
    _OspfCntLSReqTx_Type()
)
ospfCntLSReqTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntLSReqTx.setStatus("optional")
_OspfCntLSUpdateTx_Type = Counter32
_OspfCntLSUpdateTx_Object = MibTableColumn
ospfCntLSUpdateTx = _OspfCntLSUpdateTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 27),
    _OspfCntLSUpdateTx_Type()
)
ospfCntLSUpdateTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntLSUpdateTx.setStatus("optional")
_OspfCntLSAckTx_Type = Counter32
_OspfCntLSAckTx_Object = MibTableColumn
ospfCntLSAckTx = _OspfCntLSAckTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 28),
    _OspfCntLSAckTx_Type()
)
ospfCntLSAckTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntLSAckTx.setStatus("optional")
_OspfCntLSReqRx_Type = Counter32
_OspfCntLSReqRx_Object = MibTableColumn
ospfCntLSReqRx = _OspfCntLSReqRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 29),
    _OspfCntLSReqRx_Type()
)
ospfCntLSReqRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntLSReqRx.setStatus("optional")
_OspfCntLSUpdateRx_Type = Counter32
_OspfCntLSUpdateRx_Object = MibTableColumn
ospfCntLSUpdateRx = _OspfCntLSUpdateRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 30),
    _OspfCntLSUpdateRx_Type()
)
ospfCntLSUpdateRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntLSUpdateRx.setStatus("optional")
_OspfCntLSAckRx_Type = Counter32
_OspfCntLSAckRx_Object = MibTableColumn
ospfCntLSAckRx = _OspfCntLSAckRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 31),
    _OspfCntLSAckRx_Type()
)
ospfCntLSAckRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCntLSAckRx.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIB-INTEL-OSPF",
    **{"ospf": ospf,
       "ospfIpRouteTable": ospfIpRouteTable,
       "ospfIpRouteEntry": ospfIpRouteEntry,
       "ospfIpRouteChassis": ospfIpRouteChassis,
       "ospfIpRouteModule": ospfIpRouteModule,
       "ospfIpRouteInst": ospfIpRouteInst,
       "ospfIpRouteDest": ospfIpRouteDest,
       "ospfIpRouteMask": ospfIpRouteMask,
       "ospfIpRouteIfIndex": ospfIpRouteIfIndex,
       "ospfIpRouteNextHop": ospfIpRouteNextHop,
       "ospfIpRoutePref": ospfIpRoutePref,
       "ospfIpRouteCost": ospfIpRouteCost,
       "ospfIpRouteState": ospfIpRouteState,
       "ospfIpRouteAge": ospfIpRouteAge,
       "ospfIpRouteProtoType": ospfIpRouteProtoType,
       "ospfIfCntTable": ospfIfCntTable,
       "ospfIfCntEntry": ospfIfCntEntry,
       "ospfCntChassis": ospfCntChassis,
       "ospfCntModule": ospfCntModule,
       "ospfCntIfIpAddress": ospfCntIfIpAddress,
       "ospfCntAddressLessIf": ospfCntAddressLessIf,
       "ospfCntBadVer": ospfCntBadVer,
       "ospfCntBadAreaId": ospfCntBadAreaId,
       "ospfCntMaskMismatch": ospfCntMaskMismatch,
       "ospfCntAuthMismatch": ospfCntAuthMismatch,
       "ospfCntAuthFail": ospfCntAuthFail,
       "ospfCntExtOptMismatch": ospfCntExtOptMismatch,
       "ospfCntNSSAOptMismatch": ospfCntNSSAOptMismatch,
       "ospfCntNBMANeighbor": ospfCntNBMANeighbor,
       "ospfCntVirtNeighbor": ospfCntVirtNeighbor,
       "ospfCntHelloMismatch": ospfCntHelloMismatch,
       "ospfCntDeadMismatch": ospfCntDeadMismatch,
       "ospfCntBadType": ospfCntBadType,
       "ospfCntBadChksum": ospfCntBadChksum,
       "ospfCntBadLen": ospfCntBadLen,
       "ospfCntTooShort": ospfCntTooShort,
       "ospfCntDRPktMismatch": ospfCntDRPktMismatch,
       "ospfCntMulticastVL": ospfCntMulticastVL,
       "ospfCntDestAddr": ospfCntDestAddr,
       "ospfCntOwnAddr": ospfCntOwnAddr,
       "ospfCntHelloTx": ospfCntHelloTx,
       "ospfCntHelloRx": ospfCntHelloRx,
       "ospfCntLSReqTx": ospfCntLSReqTx,
       "ospfCntLSUpdateTx": ospfCntLSUpdateTx,
       "ospfCntLSAckTx": ospfCntLSAckTx,
       "ospfCntLSReqRx": ospfCntLSReqRx,
       "ospfCntLSUpdateRx": ospfCntLSUpdateRx,
       "ospfCntLSAckRx": ospfCntLSAckRx}
)
