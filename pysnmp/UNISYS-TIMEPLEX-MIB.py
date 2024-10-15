# SNMP MIB module (UNISYS-TIMEPLEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UNISYS-TIMEPLEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:35 2024
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
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Unisys_timeplex_ObjectIdentity = ObjectIdentity
unisys_timeplex = _Unisys_timeplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16)
)
_Umgmt_ObjectIdentity = ObjectIdentity
umgmt = _Umgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2)
)
_Umib_ObjectIdentity = ObjectIdentity
umib = _Umib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1)
)
_Usystem_ObjectIdentity = ObjectIdentity
usystem = _Usystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 1)
)


class _UsystemAction_Type(Integer32):
    """Custom type usystemAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1),
          ("shutdown", 2))
    )


_UsystemAction_Type.__name__ = "Integer32"
_UsystemAction_Object = MibScalar
usystemAction = _UsystemAction_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 1, 1),
    _UsystemAction_Type()
)
usystemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usystemAction.setStatus("mandatory")
_UsystemReboots_Type = Integer32
_UsystemReboots_Object = MibScalar
usystemReboots = _UsystemReboots_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 1, 2),
    _UsystemReboots_Type()
)
usystemReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usystemReboots.setStatus("mandatory")
_UsystemErrorCode_Type = Integer32
_UsystemErrorCode_Object = MibScalar
usystemErrorCode = _UsystemErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 1, 3),
    _UsystemErrorCode_Type()
)
usystemErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usystemErrorCode.setStatus("mandatory")
_Uinterfaces_ObjectIdentity = ObjectIdentity
uinterfaces = _Uinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2)
)
_UifTable_Object = MibTable
uifTable = _UifTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    uifTable.setStatus("mandatory")
_UifEntry_Object = MibTableRow
uifEntry = _UifEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    uifEntry.setStatus("mandatory")


class _UifEthernetArpWait_Type(Integer32):
    """Custom type uifEthernetArpWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UifEthernetArpWait_Type.__name__ = "Integer32"
_UifEthernetArpWait_Object = MibTableColumn
uifEthernetArpWait = _UifEthernetArpWait_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 1),
    _UifEthernetArpWait_Type()
)
uifEthernetArpWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifEthernetArpWait.setStatus("mandatory")
_UifIpAddr_Type = IpAddress
_UifIpAddr_Object = MibTableColumn
uifIpAddr = _UifIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 2),
    _UifIpAddr_Type()
)
uifIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifIpAddr.setStatus("mandatory")
_UifSubnetMask_Type = IpAddress
_UifSubnetMask_Object = MibTableColumn
uifSubnetMask = _UifSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 3),
    _UifSubnetMask_Type()
)
uifSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifSubnetMask.setStatus("mandatory")


class _UifHdlcBaudRate_Type(Integer32):
    """Custom type uifHdlcBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_UifHdlcBaudRate_Type.__name__ = "Integer32"
_UifHdlcBaudRate_Object = MibTableColumn
uifHdlcBaudRate = _UifHdlcBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 4),
    _UifHdlcBaudRate_Type()
)
uifHdlcBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifHdlcBaudRate.setStatus("mandatory")


class _UifHdlcRto_Type(Integer32):
    """Custom type uifHdlcRto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_UifHdlcRto_Type.__name__ = "Integer32"
_UifHdlcRto_Object = MibTableColumn
uifHdlcRto = _UifHdlcRto_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 5),
    _UifHdlcRto_Type()
)
uifHdlcRto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifHdlcRto.setStatus("mandatory")


class _UifHdlcAckTo_Type(Integer32):
    """Custom type uifHdlcAckTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_UifHdlcAckTo_Type.__name__ = "Integer32"
_UifHdlcAckTo_Object = MibTableColumn
uifHdlcAckTo = _UifHdlcAckTo_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 6),
    _UifHdlcAckTo_Type()
)
uifHdlcAckTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifHdlcAckTo.setStatus("mandatory")


class _UifHdlcSabmInterval_Type(Integer32):
    """Custom type uifHdlcSabmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_UifHdlcSabmInterval_Type.__name__ = "Integer32"
_UifHdlcSabmInterval_Object = MibTableColumn
uifHdlcSabmInterval = _UifHdlcSabmInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 7),
    _UifHdlcSabmInterval_Type()
)
uifHdlcSabmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifHdlcSabmInterval.setStatus("mandatory")


class _UifHdlcRnrInterval_Type(Integer32):
    """Custom type uifHdlcRnrInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_UifHdlcRnrInterval_Type.__name__ = "Integer32"
_UifHdlcRnrInterval_Object = MibTableColumn
uifHdlcRnrInterval = _UifHdlcRnrInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 8),
    _UifHdlcRnrInterval_Type()
)
uifHdlcRnrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifHdlcRnrInterval.setStatus("mandatory")


class _UifHdlcClockType_Type(Integer32):
    """Custom type uifHdlcClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dce-generates-tx-and-rx-clocks", 4),
          ("dte-accepts-tx-and-rx-clocks", 3))
    )


_UifHdlcClockType_Type.__name__ = "Integer32"
_UifHdlcClockType_Object = MibTableColumn
uifHdlcClockType = _UifHdlcClockType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 9),
    _UifHdlcClockType_Type()
)
uifHdlcClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifHdlcClockType.setStatus("mandatory")
_UifHdlcDCE_Type = Integer32
_UifHdlcDCE_Object = MibTableColumn
uifHdlcDCE = _UifHdlcDCE_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 10),
    _UifHdlcDCE_Type()
)
uifHdlcDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifHdlcDCE.setStatus("mandatory")
_UifHdlcThrowaway_Type = Integer32
_UifHdlcThrowaway_Object = MibTableColumn
uifHdlcThrowaway = _UifHdlcThrowaway_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 11),
    _UifHdlcThrowaway_Type()
)
uifHdlcThrowaway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifHdlcThrowaway.setStatus("mandatory")


class _UifHdlcAckCount_Type(Integer32):
    """Custom type uifHdlcAckCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UifHdlcAckCount_Type.__name__ = "Integer32"
_UifHdlcAckCount_Object = MibTableColumn
uifHdlcAckCount = _UifHdlcAckCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 12),
    _UifHdlcAckCount_Type()
)
uifHdlcAckCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifHdlcAckCount.setStatus("mandatory")


class _UifFddiArpWait_Type(Integer32):
    """Custom type uifFddiArpWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UifFddiArpWait_Type.__name__ = "Integer32"
_UifFddiArpWait_Object = MibTableColumn
uifFddiArpWait = _UifFddiArpWait_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 2, 1, 1, 13),
    _UifFddiArpWait_Type()
)
uifFddiArpWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uifFddiArpWait.setStatus("mandatory")
_Uat_ObjectIdentity = ObjectIdentity
uat = _Uat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 3)
)
_Uip_ObjectIdentity = ObjectIdentity
uip = _Uip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4)
)
_UipLogicalDisconnect_Type = Integer32
_UipLogicalDisconnect_Object = MibScalar
uipLogicalDisconnect = _UipLogicalDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 1),
    _UipLogicalDisconnect_Type()
)
uipLogicalDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipLogicalDisconnect.setStatus("mandatory")
_UipLoopback_Type = Integer32
_UipLoopback_Object = MibScalar
uipLoopback = _UipLoopback_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 2),
    _UipLoopback_Type()
)
uipLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipLoopback.setStatus("mandatory")
_UipRemoteg1_Type = Integer32
_UipRemoteg1_Object = MibScalar
uipRemoteg1 = _UipRemoteg1_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 3),
    _UipRemoteg1_Type()
)
uipRemoteg1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipRemoteg1.setStatus("mandatory")
_UipRemoteg2_Type = Integer32
_UipRemoteg2_Object = MibScalar
uipRemoteg2 = _UipRemoteg2_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 4),
    _UipRemoteg2_Type()
)
uipRemoteg2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipRemoteg2.setStatus("mandatory")


class _UipNet1MaxPkt_Type(Integer32):
    """Custom type uipNet1MaxPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65, 65535),
    )


_UipNet1MaxPkt_Type.__name__ = "Integer32"
_UipNet1MaxPkt_Object = MibScalar
uipNet1MaxPkt = _UipNet1MaxPkt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 5),
    _UipNet1MaxPkt_Type()
)
uipNet1MaxPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipNet1MaxPkt.setStatus("mandatory")


class _UipNet2MaxPkt_Type(Integer32):
    """Custom type uipNet2MaxPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65, 65535),
    )


_UipNet2MaxPkt_Type.__name__ = "Integer32"
_UipNet2MaxPkt_Object = MibScalar
uipNet2MaxPkt = _UipNet2MaxPkt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 6),
    _UipNet2MaxPkt_Type()
)
uipNet2MaxPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipNet2MaxPkt.setStatus("mandatory")


class _UipRedirectTo_Type(Integer32):
    """Custom type uipRedirectTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UipRedirectTo_Type.__name__ = "Integer32"
_UipRedirectTo_Object = MibScalar
uipRedirectTo = _UipRedirectTo_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 7),
    _UipRedirectTo_Type()
)
uipRedirectTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipRedirectTo.setStatus("mandatory")
_UipMasker_Type = Integer32
_UipMasker_Object = MibScalar
uipMasker = _UipMasker_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 8),
    _UipMasker_Type()
)
uipMasker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipMasker.setStatus("mandatory")
_UipWellKnownGateway_Type = IpAddress
_UipWellKnownGateway_Object = MibScalar
uipWellKnownGateway = _UipWellKnownGateway_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 9),
    _UipWellKnownGateway_Type()
)
uipWellKnownGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipWellKnownGateway.setStatus("mandatory")
_UipMaxRoutePids_Type = Integer32
_UipMaxRoutePids_Object = MibScalar
uipMaxRoutePids = _UipMaxRoutePids_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 10),
    _UipMaxRoutePids_Type()
)
uipMaxRoutePids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uipMaxRoutePids.setStatus("mandatory")
_UipRoutePidsTable_Object = MibTable
uipRoutePidsTable = _UipRoutePidsTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 11)
)
if mibBuilder.loadTexts:
    uipRoutePidsTable.setStatus("mandatory")
_UipRoutePidsEntry_Object = MibTableRow
uipRoutePidsEntry = _UipRoutePidsEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 11, 1)
)
if mibBuilder.loadTexts:
    uipRoutePidsEntry.setStatus("mandatory")


class _UipRoutePid_Type(Integer32):
    """Custom type uipRoutePid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("exterior-gateway-protocol", 8),
          ("gateway-to-gateway-protocol", 3),
          ("internet-protocol", 1),
          ("routing-information-protocol", 7))
    )


_UipRoutePid_Type.__name__ = "Integer32"
_UipRoutePid_Object = MibTableColumn
uipRoutePid = _UipRoutePid_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 11, 1, 1),
    _UipRoutePid_Type()
)
uipRoutePid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipRoutePid.setStatus("mandatory")
_UipNbrStaticRoutes_Type = Integer32
_UipNbrStaticRoutes_Object = MibScalar
uipNbrStaticRoutes = _UipNbrStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 12),
    _UipNbrStaticRoutes_Type()
)
uipNbrStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uipNbrStaticRoutes.setStatus("mandatory")
_UipStaticRouteTable_Object = MibTable
uipStaticRouteTable = _UipStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 13)
)
if mibBuilder.loadTexts:
    uipStaticRouteTable.setStatus("mandatory")
_UipStaticRouteEntry_Object = MibTableRow
uipStaticRouteEntry = _UipStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 13, 1)
)
if mibBuilder.loadTexts:
    uipStaticRouteEntry.setStatus("mandatory")
_UipStaticRouteNetwork_Type = IpAddress
_UipStaticRouteNetwork_Object = MibTableColumn
uipStaticRouteNetwork = _UipStaticRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 13, 1, 1),
    _UipStaticRouteNetwork_Type()
)
uipStaticRouteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uipStaticRouteNetwork.setStatus("mandatory")
_UipStaticRouteGateway_Type = IpAddress
_UipStaticRouteGateway_Object = MibTableColumn
uipStaticRouteGateway = _UipStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 13, 1, 2),
    _UipStaticRouteGateway_Type()
)
uipStaticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipStaticRouteGateway.setStatus("mandatory")


class _UipStaticRouteCost_Type(Integer32):
    """Custom type uipStaticRouteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UipStaticRouteCost_Type.__name__ = "Integer32"
_UipStaticRouteCost_Object = MibTableColumn
uipStaticRouteCost = _UipStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 13, 1, 3),
    _UipStaticRouteCost_Type()
)
uipStaticRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipStaticRouteCost.setStatus("mandatory")
_UipStaticRouteOverride_Type = Integer32
_UipStaticRouteOverride_Object = MibTableColumn
uipStaticRouteOverride = _UipStaticRouteOverride_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 4, 13, 1, 4),
    _UipStaticRouteOverride_Type()
)
uipStaticRouteOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uipStaticRouteOverride.setStatus("mandatory")
_Uicmp_ObjectIdentity = ObjectIdentity
uicmp = _Uicmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 5)
)
_Utcp_ObjectIdentity = ObjectIdentity
utcp = _Utcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 6)
)


class _UtcpRetransTo_Type(Integer32):
    """Custom type utcpRetransTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UtcpRetransTo_Type.__name__ = "Integer32"
_UtcpRetransTo_Object = MibScalar
utcpRetransTo = _UtcpRetransTo_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 6, 1),
    _UtcpRetransTo_Type()
)
utcpRetransTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utcpRetransTo.setStatus("mandatory")


class _UtcpRtoMin_Type(Integer32):
    """Custom type utcpRtoMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UtcpRtoMin_Type.__name__ = "Integer32"
_UtcpRtoMin_Object = MibScalar
utcpRtoMin = _UtcpRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 6, 2),
    _UtcpRtoMin_Type()
)
utcpRtoMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utcpRtoMin.setStatus("mandatory")


class _UtcpRtoMax_Type(Integer32):
    """Custom type utcpRtoMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65635),
    )


_UtcpRtoMax_Type.__name__ = "Integer32"
_UtcpRtoMax_Object = MibScalar
utcpRtoMax = _UtcpRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 6, 3),
    _UtcpRtoMax_Type()
)
utcpRtoMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utcpRtoMax.setStatus("mandatory")


class _UtcpWakeup_Type(Integer32):
    """Custom type utcpWakeup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_UtcpWakeup_Type.__name__ = "Integer32"
_UtcpWakeup_Object = MibScalar
utcpWakeup = _UtcpWakeup_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 6, 4),
    _UtcpWakeup_Type()
)
utcpWakeup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utcpWakeup.setStatus("mandatory")


class _UtcpAckTime_Type(Integer32):
    """Custom type utcpAckTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_UtcpAckTime_Type.__name__ = "Integer32"
_UtcpAckTime_Object = MibScalar
utcpAckTime = _UtcpAckTime_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 6, 5),
    _UtcpAckTime_Type()
)
utcpAckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utcpAckTime.setStatus("mandatory")


class _UtcpTimeToLive_Type(Integer32):
    """Custom type utcpTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UtcpTimeToLive_Type.__name__ = "Integer32"
_UtcpTimeToLive_Object = MibScalar
utcpTimeToLive = _UtcpTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 6, 6),
    _UtcpTimeToLive_Type()
)
utcpTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utcpTimeToLive.setStatus("mandatory")


class _UtcpThruput_Type(Integer32):
    """Custom type utcpThruput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UtcpThruput_Type.__name__ = "Integer32"
_UtcpThruput_Object = MibScalar
utcpThruput = _UtcpThruput_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 6, 7),
    _UtcpThruput_Type()
)
utcpThruput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utcpThruput.setStatus("mandatory")
_UtcpFlowAck_Type = Integer32
_UtcpFlowAck_Object = MibScalar
utcpFlowAck = _UtcpFlowAck_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 6, 8),
    _UtcpFlowAck_Type()
)
utcpFlowAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utcpFlowAck.setStatus("mandatory")
_Uudp_ObjectIdentity = ObjectIdentity
uudp = _Uudp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 7)
)
_Uegp_ObjectIdentity = ObjectIdentity
uegp = _Uegp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8)
)
_UegpMaxNeighbors_Type = Integer32
_UegpMaxNeighbors_Object = MibScalar
uegpMaxNeighbors = _UegpMaxNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 1),
    _UegpMaxNeighbors_Type()
)
uegpMaxNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uegpMaxNeighbors.setStatus("mandatory")
_UegpNumberTrustedNeighbors_Type = Integer32
_UegpNumberTrustedNeighbors_Object = MibScalar
uegpNumberTrustedNeighbors = _UegpNumberTrustedNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 2),
    _UegpNumberTrustedNeighbors_Type()
)
uegpNumberTrustedNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpNumberTrustedNeighbors.setStatus("mandatory")
_UegpNumberNeighbors_Type = Integer32
_UegpNumberNeighbors_Object = MibScalar
uegpNumberNeighbors = _UegpNumberNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 3),
    _UegpNumberNeighbors_Type()
)
uegpNumberNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpNumberNeighbors.setStatus("mandatory")
_UegpNeighborTable_Object = MibTable
uegpNeighborTable = _UegpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    uegpNeighborTable.setStatus("mandatory")
_UegpNeighborEntry_Object = MibTableRow
uegpNeighborEntry = _UegpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    uegpNeighborEntry.setStatus("mandatory")
_UegpNeighbor_Type = IpAddress
_UegpNeighbor_Object = MibTableColumn
uegpNeighbor = _UegpNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 4, 1, 1),
    _UegpNeighbor_Type()
)
uegpNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpNeighbor.setStatus("mandatory")


class _UegpAutoSysNumber_Type(Integer32):
    """Custom type uegpAutoSysNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UegpAutoSysNumber_Type.__name__ = "Integer32"
_UegpAutoSysNumber_Object = MibScalar
uegpAutoSysNumber = _UegpAutoSysNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 5),
    _UegpAutoSysNumber_Type()
)
uegpAutoSysNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpAutoSysNumber.setStatus("mandatory")


class _UegpMinHelloInterval_Type(Integer32):
    """Custom type uegpMinHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_UegpMinHelloInterval_Type.__name__ = "Integer32"
_UegpMinHelloInterval_Object = MibScalar
uegpMinHelloInterval = _UegpMinHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 6),
    _UegpMinHelloInterval_Type()
)
uegpMinHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpMinHelloInterval.setStatus("mandatory")


class _UegpMinPollInterval_Type(Integer32):
    """Custom type uegpMinPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_UegpMinPollInterval_Type.__name__ = "Integer32"
_UegpMinPollInterval_Object = MibScalar
uegpMinPollInterval = _UegpMinPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 7),
    _UegpMinPollInterval_Type()
)
uegpMinPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpMinPollInterval.setStatus("mandatory")


class _UegpRequestCeaseInterval_Type(Integer32):
    """Custom type uegpRequestCeaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_UegpRequestCeaseInterval_Type.__name__ = "Integer32"
_UegpRequestCeaseInterval_Object = MibScalar
uegpRequestCeaseInterval = _UegpRequestCeaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 8),
    _UegpRequestCeaseInterval_Type()
)
uegpRequestCeaseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpRequestCeaseInterval.setStatus("mandatory")


class _UegpDeclareDownInterval_Type(Integer32):
    """Custom type uegpDeclareDownInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 65535),
    )


_UegpDeclareDownInterval_Type.__name__ = "Integer32"
_UegpDeclareDownInterval_Object = MibScalar
uegpDeclareDownInterval = _UegpDeclareDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 9),
    _UegpDeclareDownInterval_Type()
)
uegpDeclareDownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpDeclareDownInterval.setStatus("mandatory")


class _UegpAcquireCeaseInterval_Type(Integer32):
    """Custom type uegpAcquireCeaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 240),
    )


_UegpAcquireCeaseInterval_Type.__name__ = "Integer32"
_UegpAcquireCeaseInterval_Object = MibScalar
uegpAcquireCeaseInterval = _UegpAcquireCeaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 10),
    _UegpAcquireCeaseInterval_Type()
)
uegpAcquireCeaseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpAcquireCeaseInterval.setStatus("mandatory")


class _UegpEnoughInterval_Type(Integer32):
    """Custom type uegpEnoughInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_UegpEnoughInterval_Type.__name__ = "Integer32"
_UegpEnoughInterval_Object = MibScalar
uegpEnoughInterval = _UegpEnoughInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 11),
    _UegpEnoughInterval_Type()
)
uegpEnoughInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpEnoughInterval.setStatus("mandatory")


class _UegpPurgeInterval_Type(Integer32):
    """Custom type uegpPurgeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_UegpPurgeInterval_Type.__name__ = "Integer32"
_UegpPurgeInterval_Object = MibScalar
uegpPurgeInterval = _UegpPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 12),
    _UegpPurgeInterval_Type()
)
uegpPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpPurgeInterval.setStatus("mandatory")


class _UegpMode_Type(Integer32):
    """Custom type uegpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("both-active-and-passive", 0),
          ("passive", 2))
    )


_UegpMode_Type.__name__ = "Integer32"
_UegpMode_Object = MibScalar
uegpMode = _UegpMode_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 13),
    _UegpMode_Type()
)
uegpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpMode.setStatus("mandatory")


class _UegpErrorTreatment_Type(Integer32):
    """Custom type uegpErrorTreatment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UegpErrorTreatment_Type.__name__ = "Integer32"
_UegpErrorTreatment_Object = MibScalar
uegpErrorTreatment = _UegpErrorTreatment_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 14),
    _UegpErrorTreatment_Type()
)
uegpErrorTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpErrorTreatment.setStatus("mandatory")
_UegpSharedNetwork_Type = IpAddress
_UegpSharedNetwork_Object = MibScalar
uegpSharedNetwork = _UegpSharedNetwork_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 8, 15),
    _UegpSharedNetwork_Type()
)
uegpSharedNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uegpSharedNetwork.setStatus("mandatory")
_Uggp_ObjectIdentity = ObjectIdentity
uggp = _Uggp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 12)
)


class _UggpEchoInterval_Type(Integer32):
    """Custom type uggpEchoInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UggpEchoInterval_Type.__name__ = "Integer32"
_UggpEchoInterval_Object = MibScalar
uggpEchoInterval = _UggpEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 12, 1),
    _UggpEchoInterval_Type()
)
uggpEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uggpEchoInterval.setStatus("mandatory")
_UggpMaxNeighbors_Type = Integer32
_UggpMaxNeighbors_Object = MibScalar
uggpMaxNeighbors = _UggpMaxNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 12, 2),
    _UggpMaxNeighbors_Type()
)
uggpMaxNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uggpMaxNeighbors.setStatus("mandatory")
_UggpNumberNeighbors_Type = Integer32
_UggpNumberNeighbors_Object = MibScalar
uggpNumberNeighbors = _UggpNumberNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 12, 3),
    _UggpNumberNeighbors_Type()
)
uggpNumberNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uggpNumberNeighbors.setStatus("mandatory")
_UggpNeighborTable_Object = MibTable
uggpNeighborTable = _UggpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 12, 4)
)
if mibBuilder.loadTexts:
    uggpNeighborTable.setStatus("mandatory")
_UggpNeighborEntry_Object = MibTableRow
uggpNeighborEntry = _UggpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 12, 4, 1)
)
if mibBuilder.loadTexts:
    uggpNeighborEntry.setStatus("mandatory")
_UggpNeighbor_Type = IpAddress
_UggpNeighbor_Object = MibTableColumn
uggpNeighbor = _UggpNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 12, 4, 1, 1),
    _UggpNeighbor_Type()
)
uggpNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uggpNeighbor.setStatus("mandatory")
_Urip_ObjectIdentity = ObjectIdentity
urip = _Urip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 13)
)
_Usnmp_ObjectIdentity = ObjectIdentity
usnmp = _Usnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 14)
)
_UsnmpVersion_Type = Integer32
_UsnmpVersion_Object = MibScalar
usnmpVersion = _UsnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 14, 1),
    _UsnmpVersion_Type()
)
usnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usnmpVersion.setStatus("mandatory")
_UsnmpCommunity_Type = OctetString
_UsnmpCommunity_Object = MibScalar
usnmpCommunity = _UsnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 14, 2),
    _UsnmpCommunity_Type()
)
usnmpCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usnmpCommunity.setStatus("mandatory")
_UsnmpRequests_Type = Counter32
_UsnmpRequests_Object = MibScalar
usnmpRequests = _UsnmpRequests_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 14, 3),
    _UsnmpRequests_Type()
)
usnmpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usnmpRequests.setStatus("mandatory")
_UsnmpTraps_Type = Counter32
_UsnmpTraps_Object = MibScalar
usnmpTraps = _UsnmpTraps_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 14, 4),
    _UsnmpTraps_Type()
)
usnmpTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usnmpTraps.setStatus("mandatory")
_UsnmpForwardTraps_Type = Integer32
_UsnmpForwardTraps_Object = MibScalar
usnmpForwardTraps = _UsnmpForwardTraps_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 14, 5),
    _UsnmpForwardTraps_Type()
)
usnmpForwardTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usnmpForwardTraps.setStatus("mandatory")
_Uhfp_ObjectIdentity = ObjectIdentity
uhfp = _Uhfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 15)
)


class _UhfpMaxMsg_Type(Integer32):
    """Custom type uhfpMaxMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 1420),
    )


_UhfpMaxMsg_Type.__name__ = "Integer32"
_UhfpMaxMsg_Object = MibScalar
uhfpMaxMsg = _UhfpMaxMsg_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 15, 1),
    _UhfpMaxMsg_Type()
)
uhfpMaxMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uhfpMaxMsg.setStatus("mandatory")


class _UhfpPad_Type(Integer32):
    """Custom type uhfpPad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UhfpPad_Type.__name__ = "Integer32"
_UhfpPad_Object = MibScalar
uhfpPad = _UhfpPad_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 15, 2),
    _UhfpPad_Type()
)
uhfpPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uhfpPad.setStatus("mandatory")
_UhfpSwap_Type = Integer32
_UhfpSwap_Object = MibScalar
uhfpSwap = _UhfpSwap_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 15, 3),
    _UhfpSwap_Type()
)
uhfpSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uhfpSwap.setStatus("mandatory")
_Uddn_ObjectIdentity = ObjectIdentity
uddn = _Uddn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16)
)


class _UddnTimeout_Type(Integer32):
    """Custom type uddnTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UddnTimeout_Type.__name__ = "Integer32"
_UddnTimeout_Object = MibScalar
uddnTimeout = _UddnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 1),
    _UddnTimeout_Type()
)
uddnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uddnTimeout.setStatus("mandatory")


class _UddnMsgout_Type(Integer32):
    """Custom type uddnMsgout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_UddnMsgout_Type.__name__ = "Integer32"
_UddnMsgout_Object = MibScalar
uddnMsgout = _UddnMsgout_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 2),
    _UddnMsgout_Type()
)
uddnMsgout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uddnMsgout.setStatus("mandatory")
_UddnHipUp_Type = Integer32
_UddnHipUp_Object = MibScalar
uddnHipUp = _UddnHipUp_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 3),
    _UddnHipUp_Type()
)
uddnHipUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnHipUp.setStatus("mandatory")
_UddnHdhUp_Type = Integer32
_UddnHdhUp_Object = MibScalar
uddnHdhUp = _UddnHdhUp_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 4),
    _UddnHdhUp_Type()
)
uddnHdhUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnHdhUp.setStatus("mandatory")
_UddnLinkUp_Type = Integer32
_UddnLinkUp_Object = MibScalar
uddnLinkUp = _UddnLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 5),
    _UddnLinkUp_Type()
)
uddnLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnLinkUp.setStatus("mandatory")
_UddnTotalQ_Type = Gauge32
_UddnTotalQ_Object = MibScalar
uddnTotalQ = _UddnTotalQ_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 6),
    _UddnTotalQ_Type()
)
uddnTotalQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnTotalQ.setStatus("mandatory")
_UddnConnections_Type = Gauge32
_UddnConnections_Object = MibScalar
uddnConnections = _UddnConnections_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 7),
    _UddnConnections_Type()
)
uddnConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnConnections.setStatus("mandatory")
_UddnLinkDownTo_Type = Integer32
_UddnLinkDownTo_Object = MibScalar
uddnLinkDownTo = _UddnLinkDownTo_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 8),
    _UddnLinkDownTo_Type()
)
uddnLinkDownTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnLinkDownTo.setStatus("mandatory")
_UddnRcvIncomplete_Type = Counter32
_UddnRcvIncomplete_Object = MibScalar
uddnRcvIncomplete = _UddnRcvIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 9),
    _UddnRcvIncomplete_Type()
)
uddnRcvIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnRcvIncomplete.setStatus("mandatory")
_UddnConnectionsReused_Type = Counter32
_UddnConnectionsReused_Object = MibScalar
uddnConnectionsReused = _UddnConnectionsReused_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 10),
    _UddnConnectionsReused_Type()
)
uddnConnectionsReused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnConnectionsReused.setStatus("mandatory")
_UddnHdhWentDown_Type = Counter32
_UddnHdhWentDown_Object = MibScalar
uddnHdhWentDown = _UddnHdhWentDown_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 11),
    _UddnHdhWentDown_Type()
)
uddnHdhWentDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnHdhWentDown.setStatus("mandatory")
_UddnLinkWentDown_Type = Counter32
_UddnLinkWentDown_Object = MibScalar
uddnLinkWentDown = _UddnLinkWentDown_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 12),
    _UddnLinkWentDown_Type()
)
uddnLinkWentDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnLinkWentDown.setStatus("mandatory")
_UddnLeaderErrs_Type = Counter32
_UddnLeaderErrs_Object = MibScalar
uddnLeaderErrs = _UddnLeaderErrs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 13),
    _UddnLeaderErrs_Type()
)
uddnLeaderErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnLeaderErrs.setStatus("mandatory")
_UddnPSNGoingDown_Type = Counter32
_UddnPSNGoingDown_Object = MibScalar
uddnPSNGoingDown = _UddnPSNGoingDown_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 14),
    _UddnPSNGoingDown_Type()
)
uddnPSNGoingDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnPSNGoingDown.setStatus("mandatory")
_UddnDeadHostSTATUS_Type = Counter32
_UddnDeadHostSTATUS_Object = MibScalar
uddnDeadHostSTATUS = _UddnDeadHostSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 15),
    _UddnDeadHostSTATUS_Type()
)
uddnDeadHostSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnDeadHostSTATUS.setStatus("mandatory")
_UddnIfReset_Type = Counter32
_UddnIfReset_Object = MibScalar
uddnIfReset = _UddnIfReset_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 16, 16),
    _UddnIfReset_Type()
)
uddnIfReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uddnIfReset.setStatus("mandatory")
_Ux25_ObjectIdentity = ObjectIdentity
ux25 = _Ux25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 17)
)
_Ux25IfTable_Object = MibTable
ux25IfTable = _Ux25IfTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 17, 1)
)
if mibBuilder.loadTexts:
    ux25IfTable.setStatus("mandatory")
_Ux25IfEntry_Object = MibTableRow
ux25IfEntry = _Ux25IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 17, 1, 1)
)
if mibBuilder.loadTexts:
    ux25IfEntry.setStatus("mandatory")


class _Ux25Service_Type(Integer32):
    """Custom type ux25Service based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("basic-service", 0),
          ("standard-service", 7))
    )


_Ux25Service_Type.__name__ = "Integer32"
_Ux25Service_Object = MibTableColumn
ux25Service = _Ux25Service_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 17, 1, 1, 1),
    _Ux25Service_Type()
)
ux25Service.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25Service.setStatus("mandatory")


class _Ux25Window_Type(Integer32):
    """Custom type ux25Window based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_Ux25Window_Type.__name__ = "Integer32"
_Ux25Window_Object = MibTableColumn
ux25Window = _Ux25Window_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 17, 1, 1, 2),
    _Ux25Window_Type()
)
ux25Window.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25Window.setStatus("mandatory")


class _Ux25PktSize_Type(Integer32):
    """Custom type ux25PktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 11),
    )


_Ux25PktSize_Type.__name__ = "Integer32"
_Ux25PktSize_Object = MibTableColumn
ux25PktSize = _Ux25PktSize_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 17, 1, 1, 3),
    _Ux25PktSize_Type()
)
ux25PktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ux25PktSize.setStatus("mandatory")
_Ufddi_ObjectIdentity = ObjectIdentity
ufddi = _Ufddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18)
)
_UfddiSMT_ObjectIdentity = ObjectIdentity
ufddiSMT = _UfddiSMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1)
)
_UfddiSMTStationIdGrp_ObjectIdentity = ObjectIdentity
ufddiSMTStationIdGrp = _UfddiSMTStationIdGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 1)
)
_UfddiSMTStationId_Type = OctetString
_UfddiSMTStationId_Object = MibScalar
ufddiSMTStationId = _UfddiSMTStationId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 1, 1),
    _UfddiSMTStationId_Type()
)
ufddiSMTStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiSMTStationId.setStatus("mandatory")


class _UfddiSMTStationType_Type(Integer32):
    """Custom type ufddiSMTStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concentrator", 2),
          ("station", 1))
    )


_UfddiSMTStationType_Type.__name__ = "Integer32"
_UfddiSMTStationType_Object = MibScalar
ufddiSMTStationType = _UfddiSMTStationType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 1, 2),
    _UfddiSMTStationType_Type()
)
ufddiSMTStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiSMTStationType.setStatus("mandatory")
_UfddiSMTVersionId_Type = Integer32
_UfddiSMTVersionId_Object = MibScalar
ufddiSMTVersionId = _UfddiSMTVersionId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 1, 3),
    _UfddiSMTVersionId_Type()
)
ufddiSMTVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiSMTVersionId.setStatus("mandatory")
_UfddiSMTStationCfgGrp_ObjectIdentity = ObjectIdentity
ufddiSMTStationCfgGrp = _UfddiSMTStationCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 2)
)
_UfddiSMTMACCount_Type = Integer32
_UfddiSMTMACCount_Object = MibScalar
ufddiSMTMACCount = _UfddiSMTMACCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 2, 1),
    _UfddiSMTMACCount_Type()
)
ufddiSMTMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiSMTMACCount.setStatus("mandatory")
_UfddiSMTAttachCount_Type = Integer32
_UfddiSMTAttachCount_Object = MibScalar
ufddiSMTAttachCount = _UfddiSMTAttachCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 2, 2),
    _UfddiSMTAttachCount_Type()
)
ufddiSMTAttachCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiSMTAttachCount.setStatus("mandatory")
_UfddiSMTSpurCount_Type = Integer32
_UfddiSMTSpurCount_Object = MibScalar
ufddiSMTSpurCount = _UfddiSMTSpurCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 2, 3),
    _UfddiSMTSpurCount_Type()
)
ufddiSMTSpurCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiSMTSpurCount.setStatus("mandatory")
_UfddiSMTOperationalGrp_ObjectIdentity = ObjectIdentity
ufddiSMTOperationalGrp = _UfddiSMTOperationalGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 3)
)


class _UfddiSMTDasScmState_Type(Integer32):
    """Custom type ufddiSMTDasScmState based on Integer32"""
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
        *(("isolated", 1),
          ("thru", 4),
          ("wrap-a", 2),
          ("wrap-b", 3))
    )


_UfddiSMTDasScmState_Type.__name__ = "Integer32"
_UfddiSMTDasScmState_Object = MibScalar
ufddiSMTDasScmState = _UfddiSMTDasScmState_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 1, 3, 1),
    _UfddiSMTDasScmState_Type()
)
ufddiSMTDasScmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiSMTDasScmState.setStatus("mandatory")
_UfddiMACTable_ObjectIdentity = ObjectIdentity
ufddiMACTable = _UfddiMACTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2)
)
_UfddiMACEntry_ObjectIdentity = ObjectIdentity
ufddiMACEntry = _UfddiMACEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1)
)
_UfddiMACAddressGrp_ObjectIdentity = ObjectIdentity
ufddiMACAddressGrp = _UfddiMACAddressGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 1)
)


class _UfddiMACSMTLongAddr_Type(OctetString):
    """Custom type ufddiMACSMTLongAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_UfddiMACSMTLongAddr_Type.__name__ = "OctetString"
_UfddiMACSMTLongAddr_Object = MibScalar
ufddiMACSMTLongAddr = _UfddiMACSMTLongAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 1, 1),
    _UfddiMACSMTLongAddr_Type()
)
ufddiMACSMTLongAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufddiMACSMTLongAddr.setStatus("mandatory")


class _UfddiMACShortGrpAddr_Type(OctetString):
    """Custom type ufddiMACShortGrpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_UfddiMACShortGrpAddr_Type.__name__ = "OctetString"
_UfddiMACShortGrpAddr_Object = MibScalar
ufddiMACShortGrpAddr = _UfddiMACShortGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 1, 2),
    _UfddiMACShortGrpAddr_Type()
)
ufddiMACShortGrpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufddiMACShortGrpAddr.setStatus("mandatory")
_UfddiMACCfgGrp_ObjectIdentity = ObjectIdentity
ufddiMACCfgGrp = _UfddiMACCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 2)
)
_UfddiMACUpstreamNeighbor_Type = OctetString
_UfddiMACUpstreamNeighbor_Object = MibScalar
ufddiMACUpstreamNeighbor = _UfddiMACUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 2, 1),
    _UfddiMACUpstreamNeighbor_Type()
)
ufddiMACUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACUpstreamNeighbor.setStatus("mandatory")
_UfddiMACDownstreamNeighbor_Type = OctetString
_UfddiMACDownstreamNeighbor_Object = MibScalar
ufddiMACDownstreamNeighbor = _UfddiMACDownstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 2, 2),
    _UfddiMACDownstreamNeighbor_Type()
)
ufddiMACDownstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACDownstreamNeighbor.setStatus("mandatory")
_UfddiMACResourceIndex_Type = Integer32
_UfddiMACResourceIndex_Object = MibScalar
ufddiMACResourceIndex = _UfddiMACResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 2, 3),
    _UfddiMACResourceIndex_Type()
)
ufddiMACResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACResourceIndex.setStatus("mandatory")
_UfddiMACConnectedResId_Type = Integer32
_UfddiMACConnectedResId_Object = MibScalar
ufddiMACConnectedResId = _UfddiMACConnectedResId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 2, 4),
    _UfddiMACConnectedResId_Type()
)
ufddiMACConnectedResId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACConnectedResId.setStatus("mandatory")
_UfddiMACOperGrp_ObjectIdentity = ObjectIdentity
ufddiMACOperGrp = _UfddiMACOperGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 3)
)
_UfddiMACTReq_Type = Integer32
_UfddiMACTReq_Object = MibScalar
ufddiMACTReq = _UfddiMACTReq_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 3, 1),
    _UfddiMACTReq_Type()
)
ufddiMACTReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufddiMACTReq.setStatus("mandatory")
_UfddiMACTMax_Type = Integer32
_UfddiMACTMax_Object = MibScalar
ufddiMACTMax = _UfddiMACTMax_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 3, 2),
    _UfddiMACTMax_Type()
)
ufddiMACTMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufddiMACTMax.setStatus("mandatory")


class _UfddiMACTvxValue_Type(Integer32):
    """Custom type ufddiMACTvxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_UfddiMACTvxValue_Type.__name__ = "Integer32"
_UfddiMACTvxValue_Object = MibScalar
ufddiMACTvxValue = _UfddiMACTvxValue_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 3, 3),
    _UfddiMACTvxValue_Type()
)
ufddiMACTvxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufddiMACTvxValue.setStatus("mandatory")
_UfddiMACTMin_Type = Integer32
_UfddiMACTMin_Object = MibScalar
ufddiMACTMin = _UfddiMACTMin_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 3, 4),
    _UfddiMACTMin_Type()
)
ufddiMACTMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufddiMACTMin.setStatus("mandatory")
_UfddiMACCountersGrp_ObjectIdentity = ObjectIdentity
ufddiMACCountersGrp = _UfddiMACCountersGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 4)
)
_UfddiMACReceiveCt_Type = Counter32
_UfddiMACReceiveCt_Object = MibScalar
ufddiMACReceiveCt = _UfddiMACReceiveCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 4, 1),
    _UfddiMACReceiveCt_Type()
)
ufddiMACReceiveCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACReceiveCt.setStatus("mandatory")
_UfddiMACTransmitCt_Type = Counter32
_UfddiMACTransmitCt_Object = MibScalar
ufddiMACTransmitCt = _UfddiMACTransmitCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 4, 2),
    _UfddiMACTransmitCt_Type()
)
ufddiMACTransmitCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACTransmitCt.setStatus("mandatory")
_UfddiMACTokenCt_Type = Counter32
_UfddiMACTokenCt_Object = MibScalar
ufddiMACTokenCt = _UfddiMACTokenCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 4, 3),
    _UfddiMACTokenCt_Type()
)
ufddiMACTokenCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACTokenCt.setStatus("mandatory")
_UfddiMACErrorCntrsGrp_ObjectIdentity = ObjectIdentity
ufddiMACErrorCntrsGrp = _UfddiMACErrorCntrsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 5)
)
_UfddiMACTvxExpiredCt_Type = Counter32
_UfddiMACTvxExpiredCt_Object = MibScalar
ufddiMACTvxExpiredCt = _UfddiMACTvxExpiredCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 5, 1),
    _UfddiMACTvxExpiredCt_Type()
)
ufddiMACTvxExpiredCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACTvxExpiredCt.setStatus("mandatory")
_UfddiMACNotCopiedCt_Type = Counter32
_UfddiMACNotCopiedCt_Object = MibScalar
ufddiMACNotCopiedCt = _UfddiMACNotCopiedCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 5, 2),
    _UfddiMACNotCopiedCt_Type()
)
ufddiMACNotCopiedCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACNotCopiedCt.setStatus("mandatory")
_UfddiMACLateCt_Type = Counter32
_UfddiMACLateCt_Object = MibScalar
ufddiMACLateCt = _UfddiMACLateCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 5, 3),
    _UfddiMACLateCt_Type()
)
ufddiMACLateCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACLateCt.setStatus("mandatory")
_UfddiMACReceiveOverflowCt_Type = Counter32
_UfddiMACReceiveOverflowCt_Object = MibScalar
ufddiMACReceiveOverflowCt = _UfddiMACReceiveOverflowCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 5, 4),
    _UfddiMACReceiveOverflowCt_Type()
)
ufddiMACReceiveOverflowCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACReceiveOverflowCt.setStatus("mandatory")
_UfddiMACSTATUSGrp_ObjectIdentity = ObjectIdentity
ufddiMACSTATUSGrp = _UfddiMACSTATUSGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 6)
)
_UfddiMACRingOpCt_Type = Counter32
_UfddiMACRingOpCt_Object = MibScalar
ufddiMACRingOpCt = _UfddiMACRingOpCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 6, 1),
    _UfddiMACRingOpCt_Type()
)
ufddiMACRingOpCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACRingOpCt.setStatus("mandatory")
_UfddiMACEnteredBeaconCt_Type = Counter32
_UfddiMACEnteredBeaconCt_Object = MibScalar
ufddiMACEnteredBeaconCt = _UfddiMACEnteredBeaconCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 2, 1, 6, 2),
    _UfddiMACEnteredBeaconCt_Type()
)
ufddiMACEnteredBeaconCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiMACEnteredBeaconCt.setStatus("mandatory")
_UfddiPHYTable_ObjectIdentity = ObjectIdentity
ufddiPHYTable = _UfddiPHYTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3)
)
_UfddiPHYEntry_ObjectIdentity = ObjectIdentity
ufddiPHYEntry = _UfddiPHYEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3, 1)
)
_UfddiPHYCfgGrp_ObjectIdentity = ObjectIdentity
ufddiPHYCfgGrp = _UfddiPHYCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3, 1, 1)
)


class _UfddiPHYType_Type(Integer32):
    """Custom type ufddiPHYType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 3),
          ("s", 4))
    )


_UfddiPHYType_Type.__name__ = "Integer32"
_UfddiPHYType_Object = MibScalar
ufddiPHYType = _UfddiPHYType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3, 1, 1, 1),
    _UfddiPHYType_Type()
)
ufddiPHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiPHYType.setStatus("mandatory")


class _UfddiPHYConnectState_Type(Integer32):
    """Custom type ufddiPHYConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_UfddiPHYConnectState_Type.__name__ = "Integer32"
_UfddiPHYConnectState_Object = MibScalar
ufddiPHYConnectState = _UfddiPHYConnectState_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3, 1, 1, 2),
    _UfddiPHYConnectState_Type()
)
ufddiPHYConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiPHYConnectState.setStatus("mandatory")


class _UfddiPHYRemotePHYType_Type(Integer32):
    """Custom type ufddiPHYRemotePHYType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 3),
          ("s", 4),
          ("unknown", 5))
    )


_UfddiPHYRemotePHYType_Type.__name__ = "Integer32"
_UfddiPHYRemotePHYType_Object = MibScalar
ufddiPHYRemotePHYType = _UfddiPHYRemotePHYType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3, 1, 1, 3),
    _UfddiPHYRemotePHYType_Type()
)
ufddiPHYRemotePHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiPHYRemotePHYType.setStatus("mandatory")
_UfddiPHYRemoteMACIndicated_Type = Integer32
_UfddiPHYRemoteMACIndicated_Object = MibScalar
ufddiPHYRemoteMACIndicated = _UfddiPHYRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3, 1, 1, 4),
    _UfddiPHYRemoteMACIndicated_Type()
)
ufddiPHYRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiPHYRemoteMACIndicated.setStatus("mandatory")
_UfddiPHYResourceIndex_Type = Integer32
_UfddiPHYResourceIndex_Object = MibScalar
ufddiPHYResourceIndex = _UfddiPHYResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3, 1, 1, 5),
    _UfddiPHYResourceIndex_Type()
)
ufddiPHYResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiPHYResourceIndex.setStatus("mandatory")
_UfddiPHYConnectedResId_Type = Integer32
_UfddiPHYConnectedResId_Object = MibScalar
ufddiPHYConnectedResId = _UfddiPHYConnectedResId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3, 1, 1, 6),
    _UfddiPHYConnectedResId_Type()
)
ufddiPHYConnectedResId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufddiPHYConnectedResId.setStatus("mandatory")


class _UfddiPHYAction_Type(Integer32):
    """Custom type ufddiPHYAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_UfddiPHYAction_Type.__name__ = "Integer32"
_UfddiPHYAction_Object = MibScalar
ufddiPHYAction = _UfddiPHYAction_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 18, 3, 1, 2),
    _UfddiPHYAction_Type()
)
ufddiPHYAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufddiPHYAction.setStatus("mandatory")
_Tlip_ObjectIdentity = ObjectIdentity
tlip = _Tlip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19)
)
_TlipLogicalDisconnect_Type = Integer32
_TlipLogicalDisconnect_Object = MibScalar
tlipLogicalDisconnect = _TlipLogicalDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 1),
    _TlipLogicalDisconnect_Type()
)
tlipLogicalDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipLogicalDisconnect.setStatus("mandatory")
_TlipLoopback_Type = Integer32
_TlipLoopback_Object = MibScalar
tlipLoopback = _TlipLoopback_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 2),
    _TlipLoopback_Type()
)
tlipLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipLoopback.setStatus("mandatory")


class _TlipRedirectTo_Type(Integer32):
    """Custom type tlipRedirectTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TlipRedirectTo_Type.__name__ = "Integer32"
_TlipRedirectTo_Object = MibScalar
tlipRedirectTo = _TlipRedirectTo_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 3),
    _TlipRedirectTo_Type()
)
tlipRedirectTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipRedirectTo.setStatus("mandatory")
_TlipMasker_Type = Integer32
_TlipMasker_Object = MibScalar
tlipMasker = _TlipMasker_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 4),
    _TlipMasker_Type()
)
tlipMasker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipMasker.setStatus("mandatory")
_TlipWellKnownGateway_Type = IpAddress
_TlipWellKnownGateway_Object = MibScalar
tlipWellKnownGateway = _TlipWellKnownGateway_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 5),
    _TlipWellKnownGateway_Type()
)
tlipWellKnownGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipWellKnownGateway.setStatus("mandatory")
_TlipMaxRoutePids_Type = Integer32
_TlipMaxRoutePids_Object = MibScalar
tlipMaxRoutePids = _TlipMaxRoutePids_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 6),
    _TlipMaxRoutePids_Type()
)
tlipMaxRoutePids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlipMaxRoutePids.setStatus("mandatory")
_TlipRoutePidsTable_Object = MibTable
tlipRoutePidsTable = _TlipRoutePidsTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 7)
)
if mibBuilder.loadTexts:
    tlipRoutePidsTable.setStatus("mandatory")
_TlipRoutePidsEntry_Object = MibTableRow
tlipRoutePidsEntry = _TlipRoutePidsEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 7, 1)
)
if mibBuilder.loadTexts:
    tlipRoutePidsEntry.setStatus("mandatory")


class _TlipRoutePid_Type(Integer32):
    """Custom type tlipRoutePid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("exterior-gateway-protocol", 8),
          ("gateway-to-gateway-protocol", 3),
          ("internet-protocol", 1),
          ("routing-information-protocol", 7))
    )


_TlipRoutePid_Type.__name__ = "Integer32"
_TlipRoutePid_Object = MibTableColumn
tlipRoutePid = _TlipRoutePid_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 7, 1, 1),
    _TlipRoutePid_Type()
)
tlipRoutePid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipRoutePid.setStatus("mandatory")
_TlipNbrStaticRoutes_Type = Integer32
_TlipNbrStaticRoutes_Object = MibScalar
tlipNbrStaticRoutes = _TlipNbrStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 8),
    _TlipNbrStaticRoutes_Type()
)
tlipNbrStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlipNbrStaticRoutes.setStatus("mandatory")
_TlipStaticRouteTable_Object = MibTable
tlipStaticRouteTable = _TlipStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 9)
)
if mibBuilder.loadTexts:
    tlipStaticRouteTable.setStatus("mandatory")
_TlipStaticRouteEntry_Object = MibTableRow
tlipStaticRouteEntry = _TlipStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 9, 1)
)
if mibBuilder.loadTexts:
    tlipStaticRouteEntry.setStatus("mandatory")
_TlipStaticRouteNetwork_Type = IpAddress
_TlipStaticRouteNetwork_Object = MibTableColumn
tlipStaticRouteNetwork = _TlipStaticRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 9, 1, 1),
    _TlipStaticRouteNetwork_Type()
)
tlipStaticRouteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlipStaticRouteNetwork.setStatus("mandatory")
_TlipStaticRouteGateway_Type = IpAddress
_TlipStaticRouteGateway_Object = MibTableColumn
tlipStaticRouteGateway = _TlipStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 9, 1, 2),
    _TlipStaticRouteGateway_Type()
)
tlipStaticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipStaticRouteGateway.setStatus("mandatory")


class _TlipStaticRouteCost_Type(Integer32):
    """Custom type tlipStaticRouteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TlipStaticRouteCost_Type.__name__ = "Integer32"
_TlipStaticRouteCost_Object = MibTableColumn
tlipStaticRouteCost = _TlipStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 9, 1, 3),
    _TlipStaticRouteCost_Type()
)
tlipStaticRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipStaticRouteCost.setStatus("mandatory")
_TlipStaticRouteOverride_Type = Integer32
_TlipStaticRouteOverride_Object = MibTableColumn
tlipStaticRouteOverride = _TlipStaticRouteOverride_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 9, 1, 4),
    _TlipStaticRouteOverride_Type()
)
tlipStaticRouteOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipStaticRouteOverride.setStatus("mandatory")
_TlipRemotegTable_Object = MibTable
tlipRemotegTable = _TlipRemotegTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 10)
)
if mibBuilder.loadTexts:
    tlipRemotegTable.setStatus("mandatory")
_TlipRemotegEntry_Object = MibTableRow
tlipRemotegEntry = _TlipRemotegEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 10, 1)
)
if mibBuilder.loadTexts:
    tlipRemotegEntry.setStatus("mandatory")
_TlipRemoteg_Type = Integer32
_TlipRemoteg_Object = MibTableColumn
tlipRemoteg = _TlipRemoteg_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 10, 1, 1),
    _TlipRemoteg_Type()
)
tlipRemoteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipRemoteg.setStatus("mandatory")
_TlipNetMaxPktTable_Object = MibTable
tlipNetMaxPktTable = _TlipNetMaxPktTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 11)
)
if mibBuilder.loadTexts:
    tlipNetMaxPktTable.setStatus("mandatory")
_TlipNetMaxPktEntry_Object = MibTableRow
tlipNetMaxPktEntry = _TlipNetMaxPktEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 11, 1)
)
if mibBuilder.loadTexts:
    tlipNetMaxPktEntry.setStatus("mandatory")


class _TlipNetMaxPkt_Type(Integer32):
    """Custom type tlipNetMaxPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65, 65535),
    )


_TlipNetMaxPkt_Type.__name__ = "Integer32"
_TlipNetMaxPkt_Object = MibTableColumn
tlipNetMaxPkt = _TlipNetMaxPkt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 1, 19, 11, 1, 1),
    _TlipNetMaxPkt_Type()
)
tlipNetMaxPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlipNetMaxPkt.setStatus("mandatory")
_Tl1mib_ObjectIdentity = ObjectIdentity
tl1mib = _Tl1mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2)
)
_Tl1system_ObjectIdentity = ObjectIdentity
tl1system = _Tl1system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 1)
)


class _Tl1systemAction_Type(Integer32):
    """Custom type tl1systemAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1),
          ("shutdown", 2))
    )


_Tl1systemAction_Type.__name__ = "Integer32"
_Tl1systemAction_Object = MibScalar
tl1systemAction = _Tl1systemAction_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 1, 1),
    _Tl1systemAction_Type()
)
tl1systemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1systemAction.setStatus("mandatory")
_Tl1systemReboots_Type = Integer32
_Tl1systemReboots_Object = MibScalar
tl1systemReboots = _Tl1systemReboots_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 1, 2),
    _Tl1systemReboots_Type()
)
tl1systemReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1systemReboots.setStatus("mandatory")
_Tl1systemErrorCode_Type = Integer32
_Tl1systemErrorCode_Object = MibScalar
tl1systemErrorCode = _Tl1systemErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 1, 3),
    _Tl1systemErrorCode_Type()
)
tl1systemErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1systemErrorCode.setStatus("mandatory")
_Tl1interfaces_ObjectIdentity = ObjectIdentity
tl1interfaces = _Tl1interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 2)
)
_Tl1ifTable_Object = MibTable
tl1ifTable = _Tl1ifTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tl1ifTable.setStatus("mandatory")
_Tl1ifEntry_Object = MibTableRow
tl1ifEntry = _Tl1ifEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tl1ifEntry.setStatus("mandatory")
_Tl1ifIpAddr_Type = IpAddress
_Tl1ifIpAddr_Object = MibTableColumn
tl1ifIpAddr = _Tl1ifIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 2, 1, 1, 1),
    _Tl1ifIpAddr_Type()
)
tl1ifIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ifIpAddr.setStatus("mandatory")
_Tl1ifSubnetMask_Type = IpAddress
_Tl1ifSubnetMask_Object = MibTableColumn
tl1ifSubnetMask = _Tl1ifSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 2, 1, 1, 2),
    _Tl1ifSubnetMask_Type()
)
tl1ifSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ifSubnetMask.setStatus("mandatory")


class _Tl1ifProxyARP_Type(Integer32):
    """Custom type tl1ifProxyARP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_Tl1ifProxyARP_Type.__name__ = "Integer32"
_Tl1ifProxyARP_Object = MibTableColumn
tl1ifProxyARP = _Tl1ifProxyARP_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 2, 1, 1, 3),
    _Tl1ifProxyARP_Type()
)
tl1ifProxyARP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ifProxyARP.setStatus("mandatory")


class _Tl1ifType_Type(Integer32):
    """Custom type tl1ifType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-II", 1),
          ("fddi", 3),
          ("iso802-3", 2),
          ("lapb", 4),
          ("not-configured", 0),
          ("ppp", 6),
          ("token-ring", 7),
          ("x25", 5))
    )


_Tl1ifType_Type.__name__ = "Integer32"
_Tl1ifType_Object = MibTableColumn
tl1ifType = _Tl1ifType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 2, 1, 1, 4),
    _Tl1ifType_Type()
)
tl1ifType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ifType.setStatus("mandatory")


class _Tl1ifHardwareAddress_Type(OctetString):
    """Custom type tl1ifHardwareAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1ifHardwareAddress_Type.__name__ = "OctetString"
_Tl1ifHardwareAddress_Object = MibTableColumn
tl1ifHardwareAddress = _Tl1ifHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 2, 1, 1, 5),
    _Tl1ifHardwareAddress_Type()
)
tl1ifHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ifHardwareAddress.setStatus("mandatory")
_Tl1at_ObjectIdentity = ObjectIdentity
tl1at = _Tl1at_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 3)
)
_Tl1ip_ObjectIdentity = ObjectIdentity
tl1ip = _Tl1ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4)
)


class _Tl1ipLogicalDisconnect_Type(Integer32):
    """Custom type tl1ipLogicalDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1ipLogicalDisconnect_Type.__name__ = "Integer32"
_Tl1ipLogicalDisconnect_Object = MibScalar
tl1ipLogicalDisconnect = _Tl1ipLogicalDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 1),
    _Tl1ipLogicalDisconnect_Type()
)
tl1ipLogicalDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipLogicalDisconnect.setStatus("mandatory")


class _Tl1ipLoopback_Type(Integer32):
    """Custom type tl1ipLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1ipLoopback_Type.__name__ = "Integer32"
_Tl1ipLoopback_Object = MibScalar
tl1ipLoopback = _Tl1ipLoopback_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 2),
    _Tl1ipLoopback_Type()
)
tl1ipLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipLoopback.setStatus("mandatory")


class _Tl1ipRedirectTo_Type(Integer32):
    """Custom type tl1ipRedirectTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Tl1ipRedirectTo_Type.__name__ = "Integer32"
_Tl1ipRedirectTo_Object = MibScalar
tl1ipRedirectTo = _Tl1ipRedirectTo_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 3),
    _Tl1ipRedirectTo_Type()
)
tl1ipRedirectTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipRedirectTo.setStatus("mandatory")
_Tl1ipMaxRoutePids_Type = Integer32
_Tl1ipMaxRoutePids_Object = MibScalar
tl1ipMaxRoutePids = _Tl1ipMaxRoutePids_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 4),
    _Tl1ipMaxRoutePids_Type()
)
tl1ipMaxRoutePids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ipMaxRoutePids.setStatus("mandatory")
_Tl1ipRoutePidsTable_Object = MibTable
tl1ipRoutePidsTable = _Tl1ipRoutePidsTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    tl1ipRoutePidsTable.setStatus("mandatory")
_Tl1ipRoutePidsEntry_Object = MibTableRow
tl1ipRoutePidsEntry = _Tl1ipRoutePidsEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    tl1ipRoutePidsEntry.setStatus("mandatory")


class _Tl1ipRoutePid_Type(Integer32):
    """Custom type tl1ipRoutePid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              7,
              8,
              23)
        )
    )
    namedValues = NamedValues(
        *(("exterior-Gateway-Protocol", 8),
          ("internet-Protocol", 1),
          ("open-Shortest-Path-First", 23),
          ("routing-Information-Protocol", 7),
          ("static-Routes", 0))
    )


_Tl1ipRoutePid_Type.__name__ = "Integer32"
_Tl1ipRoutePid_Object = MibTableColumn
tl1ipRoutePid = _Tl1ipRoutePid_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 5, 1, 1),
    _Tl1ipRoutePid_Type()
)
tl1ipRoutePid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipRoutePid.setStatus("mandatory")
_Tl1ipNbrStaticRoutes_Type = Integer32
_Tl1ipNbrStaticRoutes_Object = MibScalar
tl1ipNbrStaticRoutes = _Tl1ipNbrStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 6),
    _Tl1ipNbrStaticRoutes_Type()
)
tl1ipNbrStaticRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipNbrStaticRoutes.setStatus("mandatory")
_Tl1ipStaticRouteTable_Object = MibTable
tl1ipStaticRouteTable = _Tl1ipStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 7)
)
if mibBuilder.loadTexts:
    tl1ipStaticRouteTable.setStatus("mandatory")
_Tl1ipStaticRouteEntry_Object = MibTableRow
tl1ipStaticRouteEntry = _Tl1ipStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 7, 1)
)
if mibBuilder.loadTexts:
    tl1ipStaticRouteEntry.setStatus("mandatory")
_Tl1ipStaticRouteNetwork_Type = IpAddress
_Tl1ipStaticRouteNetwork_Object = MibTableColumn
tl1ipStaticRouteNetwork = _Tl1ipStaticRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 7, 1, 1),
    _Tl1ipStaticRouteNetwork_Type()
)
tl1ipStaticRouteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ipStaticRouteNetwork.setStatus("mandatory")
_Tl1ipStaticRouteGateway_Type = IpAddress
_Tl1ipStaticRouteGateway_Object = MibTableColumn
tl1ipStaticRouteGateway = _Tl1ipStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 7, 1, 2),
    _Tl1ipStaticRouteGateway_Type()
)
tl1ipStaticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipStaticRouteGateway.setStatus("mandatory")


class _Tl1ipStaticRouteCost_Type(Integer32):
    """Custom type tl1ipStaticRouteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Tl1ipStaticRouteCost_Type.__name__ = "Integer32"
_Tl1ipStaticRouteCost_Object = MibTableColumn
tl1ipStaticRouteCost = _Tl1ipStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 7, 1, 3),
    _Tl1ipStaticRouteCost_Type()
)
tl1ipStaticRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipStaticRouteCost.setStatus("mandatory")


class _Tl1ipStaticRouteOverride_Type(Integer32):
    """Custom type tl1ipStaticRouteOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1ipStaticRouteOverride_Type.__name__ = "Integer32"
_Tl1ipStaticRouteOverride_Object = MibTableColumn
tl1ipStaticRouteOverride = _Tl1ipStaticRouteOverride_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 7, 1, 4),
    _Tl1ipStaticRouteOverride_Type()
)
tl1ipStaticRouteOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipStaticRouteOverride.setStatus("mandatory")
_Tl1ipStaticRouteMask_Type = IpAddress
_Tl1ipStaticRouteMask_Object = MibTableColumn
tl1ipStaticRouteMask = _Tl1ipStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 7, 1, 5),
    _Tl1ipStaticRouteMask_Type()
)
tl1ipStaticRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipStaticRouteMask.setStatus("mandatory")
_Tl1ipConfigIntfTable_Object = MibTable
tl1ipConfigIntfTable = _Tl1ipConfigIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 8)
)
if mibBuilder.loadTexts:
    tl1ipConfigIntfTable.setStatus("mandatory")
_Tl1ipConfigIntfEntry_Object = MibTableRow
tl1ipConfigIntfEntry = _Tl1ipConfigIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 8, 1)
)
if mibBuilder.loadTexts:
    tl1ipConfigIntfEntry.setStatus("mandatory")


class _Tl1ipRemoteg_Type(Integer32):
    """Custom type tl1ipRemoteg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1ipRemoteg_Type.__name__ = "Integer32"
_Tl1ipRemoteg_Object = MibTableColumn
tl1ipRemoteg = _Tl1ipRemoteg_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 8, 1, 1),
    _Tl1ipRemoteg_Type()
)
tl1ipRemoteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipRemoteg.setStatus("mandatory")


class _Tl1ipNetMaxPkt_Type(Integer32):
    """Custom type tl1ipNetMaxPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65, 65535),
    )


_Tl1ipNetMaxPkt_Type.__name__ = "Integer32"
_Tl1ipNetMaxPkt_Object = MibTableColumn
tl1ipNetMaxPkt = _Tl1ipNetMaxPkt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 8, 1, 2),
    _Tl1ipNetMaxPkt_Type()
)
tl1ipNetMaxPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipNetMaxPkt.setStatus("mandatory")
_Tl1ipMasker_Type = Integer32
_Tl1ipMasker_Object = MibTableColumn
tl1ipMasker = _Tl1ipMasker_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 8, 1, 3),
    _Tl1ipMasker_Type()
)
tl1ipMasker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipMasker.setStatus("mandatory")
_Tl1ipNumFilters_Type = Integer32
_Tl1ipNumFilters_Object = MibScalar
tl1ipNumFilters = _Tl1ipNumFilters_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 9),
    _Tl1ipNumFilters_Type()
)
tl1ipNumFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ipNumFilters.setStatus("mandatory")
_Tl1ipFilterTable_Object = MibTable
tl1ipFilterTable = _Tl1ipFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 10)
)
if mibBuilder.loadTexts:
    tl1ipFilterTable.setStatus("mandatory")
_Tl1ipFilterEntry_Object = MibTableRow
tl1ipFilterEntry = _Tl1ipFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 10, 1)
)
if mibBuilder.loadTexts:
    tl1ipFilterEntry.setStatus("mandatory")
_Tl1ipFilterSrcMask_Type = IpAddress
_Tl1ipFilterSrcMask_Object = MibTableColumn
tl1ipFilterSrcMask = _Tl1ipFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 10, 1, 1),
    _Tl1ipFilterSrcMask_Type()
)
tl1ipFilterSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipFilterSrcMask.setStatus("mandatory")
_Tl1ipFilterSrcNet_Type = IpAddress
_Tl1ipFilterSrcNet_Object = MibTableColumn
tl1ipFilterSrcNet = _Tl1ipFilterSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 10, 1, 2),
    _Tl1ipFilterSrcNet_Type()
)
tl1ipFilterSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipFilterSrcNet.setStatus("mandatory")
_Tl1ipFilterDstMask_Type = IpAddress
_Tl1ipFilterDstMask_Object = MibTableColumn
tl1ipFilterDstMask = _Tl1ipFilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 10, 1, 3),
    _Tl1ipFilterDstMask_Type()
)
tl1ipFilterDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipFilterDstMask.setStatus("mandatory")
_Tl1ipFilterDstNet_Type = IpAddress
_Tl1ipFilterDstNet_Object = MibTableColumn
tl1ipFilterDstNet = _Tl1ipFilterDstNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 10, 1, 4),
    _Tl1ipFilterDstNet_Type()
)
tl1ipFilterDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipFilterDstNet.setStatus("mandatory")
_Tl1ipFilterNbrExceptions_Type = Integer32
_Tl1ipFilterNbrExceptions_Object = MibTableColumn
tl1ipFilterNbrExceptions = _Tl1ipFilterNbrExceptions_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 10, 1, 5),
    _Tl1ipFilterNbrExceptions_Type()
)
tl1ipFilterNbrExceptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipFilterNbrExceptions.setStatus("mandatory")
_Tl1ipFilterExceptionTable_Object = MibTable
tl1ipFilterExceptionTable = _Tl1ipFilterExceptionTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 11)
)
if mibBuilder.loadTexts:
    tl1ipFilterExceptionTable.setStatus("mandatory")
_Tl1ipFilterExceptionEntry_Object = MibTableRow
tl1ipFilterExceptionEntry = _Tl1ipFilterExceptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 11, 1)
)
if mibBuilder.loadTexts:
    tl1ipFilterExceptionEntry.setStatus("mandatory")
_Tl1ipFilterExceptionSrcNet_Type = IpAddress
_Tl1ipFilterExceptionSrcNet_Object = MibTableColumn
tl1ipFilterExceptionSrcNet = _Tl1ipFilterExceptionSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 11, 1, 1),
    _Tl1ipFilterExceptionSrcNet_Type()
)
tl1ipFilterExceptionSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipFilterExceptionSrcNet.setStatus("mandatory")
_Tl1ipFilterExceptionDstNet_Type = IpAddress
_Tl1ipFilterExceptionDstNet_Object = MibTableColumn
tl1ipFilterExceptionDstNet = _Tl1ipFilterExceptionDstNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 4, 11, 1, 2),
    _Tl1ipFilterExceptionDstNet_Type()
)
tl1ipFilterExceptionDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ipFilterExceptionDstNet.setStatus("mandatory")
_Tl1icmp_ObjectIdentity = ObjectIdentity
tl1icmp = _Tl1icmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 5)
)
_Tl1tcp_ObjectIdentity = ObjectIdentity
tl1tcp = _Tl1tcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 6)
)


class _Tl1tcpRetransTo_Type(Integer32):
    """Custom type tl1tcpRetransTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Tl1tcpRetransTo_Type.__name__ = "Integer32"
_Tl1tcpRetransTo_Object = MibScalar
tl1tcpRetransTo = _Tl1tcpRetransTo_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 6, 1),
    _Tl1tcpRetransTo_Type()
)
tl1tcpRetransTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tcpRetransTo.setStatus("mandatory")


class _Tl1tcpRtoMin_Type(Integer32):
    """Custom type tl1tcpRtoMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Tl1tcpRtoMin_Type.__name__ = "Integer32"
_Tl1tcpRtoMin_Object = MibScalar
tl1tcpRtoMin = _Tl1tcpRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 6, 2),
    _Tl1tcpRtoMin_Type()
)
tl1tcpRtoMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tcpRtoMin.setStatus("mandatory")


class _Tl1tcpRtoMax_Type(Integer32):
    """Custom type tl1tcpRtoMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65635),
    )


_Tl1tcpRtoMax_Type.__name__ = "Integer32"
_Tl1tcpRtoMax_Object = MibScalar
tl1tcpRtoMax = _Tl1tcpRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 6, 3),
    _Tl1tcpRtoMax_Type()
)
tl1tcpRtoMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tcpRtoMax.setStatus("mandatory")


class _Tl1tcpWakeup_Type(Integer32):
    """Custom type tl1tcpWakeup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_Tl1tcpWakeup_Type.__name__ = "Integer32"
_Tl1tcpWakeup_Object = MibScalar
tl1tcpWakeup = _Tl1tcpWakeup_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 6, 4),
    _Tl1tcpWakeup_Type()
)
tl1tcpWakeup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tcpWakeup.setStatus("mandatory")


class _Tl1tcpAckTime_Type(Integer32):
    """Custom type tl1tcpAckTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_Tl1tcpAckTime_Type.__name__ = "Integer32"
_Tl1tcpAckTime_Object = MibScalar
tl1tcpAckTime = _Tl1tcpAckTime_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 6, 5),
    _Tl1tcpAckTime_Type()
)
tl1tcpAckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tcpAckTime.setStatus("mandatory")


class _Tl1tcpTimeToLive_Type(Integer32):
    """Custom type tl1tcpTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Tl1tcpTimeToLive_Type.__name__ = "Integer32"
_Tl1tcpTimeToLive_Object = MibScalar
tl1tcpTimeToLive = _Tl1tcpTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 6, 6),
    _Tl1tcpTimeToLive_Type()
)
tl1tcpTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tcpTimeToLive.setStatus("mandatory")


class _Tl1tcpThruput_Type(Integer32):
    """Custom type tl1tcpThruput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Tl1tcpThruput_Type.__name__ = "Integer32"
_Tl1tcpThruput_Object = MibScalar
tl1tcpThruput = _Tl1tcpThruput_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 6, 7),
    _Tl1tcpThruput_Type()
)
tl1tcpThruput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tcpThruput.setStatus("mandatory")


class _Tl1tcpFlowAck_Type(Integer32):
    """Custom type tl1tcpFlowAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Tl1tcpFlowAck_Type.__name__ = "Integer32"
_Tl1tcpFlowAck_Object = MibScalar
tl1tcpFlowAck = _Tl1tcpFlowAck_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 6, 8),
    _Tl1tcpFlowAck_Type()
)
tl1tcpFlowAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tcpFlowAck.setStatus("mandatory")
_Tl1udp_ObjectIdentity = ObjectIdentity
tl1udp = _Tl1udp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 7)
)
_Tl1egp_ObjectIdentity = ObjectIdentity
tl1egp = _Tl1egp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8)
)
_Tl1egpMaxNbrs_Type = Integer32
_Tl1egpMaxNbrs_Object = MibScalar
tl1egpMaxNbrs = _Tl1egpMaxNbrs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 1),
    _Tl1egpMaxNbrs_Type()
)
tl1egpMaxNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1egpMaxNbrs.setStatus("mandatory")


class _Tl1egpNumberTrustedNbrs_Type(Integer32):
    """Custom type tl1egpNumberTrustedNbrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Tl1egpNumberTrustedNbrs_Type.__name__ = "Integer32"
_Tl1egpNumberTrustedNbrs_Object = MibScalar
tl1egpNumberTrustedNbrs = _Tl1egpNumberTrustedNbrs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 2),
    _Tl1egpNumberTrustedNbrs_Type()
)
tl1egpNumberTrustedNbrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpNumberTrustedNbrs.setStatus("mandatory")


class _Tl1egpNumberNbrs_Type(Integer32):
    """Custom type tl1egpNumberNbrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Tl1egpNumberNbrs_Type.__name__ = "Integer32"
_Tl1egpNumberNbrs_Object = MibScalar
tl1egpNumberNbrs = _Tl1egpNumberNbrs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 3),
    _Tl1egpNumberNbrs_Type()
)
tl1egpNumberNbrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpNumberNbrs.setStatus("mandatory")
_Tl1egpNbrTable_Object = MibTable
tl1egpNbrTable = _Tl1egpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 4)
)
if mibBuilder.loadTexts:
    tl1egpNbrTable.setStatus("mandatory")
_Tl1egpNbrEntry_Object = MibTableRow
tl1egpNbrEntry = _Tl1egpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    tl1egpNbrEntry.setStatus("mandatory")
_Tl1egpNbr_Type = IpAddress
_Tl1egpNbr_Object = MibTableColumn
tl1egpNbr = _Tl1egpNbr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 4, 1, 1),
    _Tl1egpNbr_Type()
)
tl1egpNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpNbr.setStatus("mandatory")


class _Tl1egpAutoSysNumber_Type(Integer32):
    """Custom type tl1egpAutoSysNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tl1egpAutoSysNumber_Type.__name__ = "Integer32"
_Tl1egpAutoSysNumber_Object = MibScalar
tl1egpAutoSysNumber = _Tl1egpAutoSysNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 5),
    _Tl1egpAutoSysNumber_Type()
)
tl1egpAutoSysNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpAutoSysNumber.setStatus("mandatory")


class _Tl1egpMinHelloInterval_Type(Integer32):
    """Custom type tl1egpMinHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_Tl1egpMinHelloInterval_Type.__name__ = "Integer32"
_Tl1egpMinHelloInterval_Object = MibScalar
tl1egpMinHelloInterval = _Tl1egpMinHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 6),
    _Tl1egpMinHelloInterval_Type()
)
tl1egpMinHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpMinHelloInterval.setStatus("mandatory")


class _Tl1egpMinPollInterval_Type(Integer32):
    """Custom type tl1egpMinPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_Tl1egpMinPollInterval_Type.__name__ = "Integer32"
_Tl1egpMinPollInterval_Object = MibScalar
tl1egpMinPollInterval = _Tl1egpMinPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 7),
    _Tl1egpMinPollInterval_Type()
)
tl1egpMinPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpMinPollInterval.setStatus("mandatory")


class _Tl1egpRequestCeaseInterval_Type(Integer32):
    """Custom type tl1egpRequestCeaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 65535),
    )


_Tl1egpRequestCeaseInterval_Type.__name__ = "Integer32"
_Tl1egpRequestCeaseInterval_Object = MibScalar
tl1egpRequestCeaseInterval = _Tl1egpRequestCeaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 8),
    _Tl1egpRequestCeaseInterval_Type()
)
tl1egpRequestCeaseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpRequestCeaseInterval.setStatus("mandatory")


class _Tl1egpDeclareDownInterval_Type(Integer32):
    """Custom type tl1egpDeclareDownInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 65535),
    )


_Tl1egpDeclareDownInterval_Type.__name__ = "Integer32"
_Tl1egpDeclareDownInterval_Object = MibScalar
tl1egpDeclareDownInterval = _Tl1egpDeclareDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 9),
    _Tl1egpDeclareDownInterval_Type()
)
tl1egpDeclareDownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpDeclareDownInterval.setStatus("mandatory")


class _Tl1egpAcquireCeaseInterval_Type(Integer32):
    """Custom type tl1egpAcquireCeaseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 240),
    )


_Tl1egpAcquireCeaseInterval_Type.__name__ = "Integer32"
_Tl1egpAcquireCeaseInterval_Object = MibScalar
tl1egpAcquireCeaseInterval = _Tl1egpAcquireCeaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 10),
    _Tl1egpAcquireCeaseInterval_Type()
)
tl1egpAcquireCeaseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpAcquireCeaseInterval.setStatus("mandatory")


class _Tl1egpEnoughInterval_Type(Integer32):
    """Custom type tl1egpEnoughInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_Tl1egpEnoughInterval_Type.__name__ = "Integer32"
_Tl1egpEnoughInterval_Object = MibScalar
tl1egpEnoughInterval = _Tl1egpEnoughInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 11),
    _Tl1egpEnoughInterval_Type()
)
tl1egpEnoughInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpEnoughInterval.setStatus("mandatory")


class _Tl1egpPurgeInterval_Type(Integer32):
    """Custom type tl1egpPurgeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_Tl1egpPurgeInterval_Type.__name__ = "Integer32"
_Tl1egpPurgeInterval_Object = MibScalar
tl1egpPurgeInterval = _Tl1egpPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 12),
    _Tl1egpPurgeInterval_Type()
)
tl1egpPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpPurgeInterval.setStatus("mandatory")


class _Tl1egpMode_Type(Integer32):
    """Custom type tl1egpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("active-and-passive", 0),
          ("passive", 2))
    )


_Tl1egpMode_Type.__name__ = "Integer32"
_Tl1egpMode_Object = MibScalar
tl1egpMode = _Tl1egpMode_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 13),
    _Tl1egpMode_Type()
)
tl1egpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpMode.setStatus("mandatory")


class _Tl1egpErrorTreatment_Type(Integer32):
    """Custom type tl1egpErrorTreatment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Tl1egpErrorTreatment_Type.__name__ = "Integer32"
_Tl1egpErrorTreatment_Object = MibScalar
tl1egpErrorTreatment = _Tl1egpErrorTreatment_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 14),
    _Tl1egpErrorTreatment_Type()
)
tl1egpErrorTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpErrorTreatment.setStatus("mandatory")
_Tl1egpSharedNetwork_Type = IpAddress
_Tl1egpSharedNetwork_Object = MibScalar
tl1egpSharedNetwork = _Tl1egpSharedNetwork_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 8, 15),
    _Tl1egpSharedNetwork_Type()
)
tl1egpSharedNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1egpSharedNetwork.setStatus("mandatory")
_Tl1snmp_ObjectIdentity = ObjectIdentity
tl1snmp = _Tl1snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11)
)
_Tl1snmpVersion_Type = Integer32
_Tl1snmpVersion_Object = MibScalar
tl1snmpVersion = _Tl1snmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11, 1),
    _Tl1snmpVersion_Type()
)
tl1snmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1snmpVersion.setStatus("mandatory")
_Tl1snmpTrapTable_Object = MibTable
tl1snmpTrapTable = _Tl1snmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11, 2)
)
if mibBuilder.loadTexts:
    tl1snmpTrapTable.setStatus("mandatory")
_Tl1snmpTrapEntry_Object = MibTableRow
tl1snmpTrapEntry = _Tl1snmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    tl1snmpTrapEntry.setStatus("mandatory")
_Tl1snmpTrapAddress_Type = IpAddress
_Tl1snmpTrapAddress_Object = MibTableColumn
tl1snmpTrapAddress = _Tl1snmpTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11, 2, 1, 1),
    _Tl1snmpTrapAddress_Type()
)
tl1snmpTrapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1snmpTrapAddress.setStatus("mandatory")


class _Tl1snmpForwardTraps_Type(Integer32):
    """Custom type tl1snmpForwardTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-forward", 1),
          ("forward", 2))
    )


_Tl1snmpForwardTraps_Type.__name__ = "Integer32"
_Tl1snmpForwardTraps_Object = MibScalar
tl1snmpForwardTraps = _Tl1snmpForwardTraps_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11, 3),
    _Tl1snmpForwardTraps_Type()
)
tl1snmpForwardTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1snmpForwardTraps.setStatus("mandatory")


class _Tl1snmpLastTrapMessage_Type(OctetString):
    """Custom type tl1snmpLastTrapMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Tl1snmpLastTrapMessage_Type.__name__ = "OctetString"
_Tl1snmpLastTrapMessage_Object = MibScalar
tl1snmpLastTrapMessage = _Tl1snmpLastTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11, 4),
    _Tl1snmpLastTrapMessage_Type()
)
tl1snmpLastTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1snmpLastTrapMessage.setStatus("mandatory")
_Tl1snmpNMSTable_Object = MibTable
tl1snmpNMSTable = _Tl1snmpNMSTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11, 5)
)
if mibBuilder.loadTexts:
    tl1snmpNMSTable.setStatus("mandatory")
_Tl1snmpNMSEntry_Object = MibTableRow
tl1snmpNMSEntry = _Tl1snmpNMSEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11, 5, 1)
)
if mibBuilder.loadTexts:
    tl1snmpNMSEntry.setStatus("mandatory")
_Tl1snmpNMSAddress_Type = IpAddress
_Tl1snmpNMSAddress_Object = MibTableColumn
tl1snmpNMSAddress = _Tl1snmpNMSAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 11, 5, 1, 1),
    _Tl1snmpNMSAddress_Type()
)
tl1snmpNMSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1snmpNMSAddress.setStatus("mandatory")
_Tl1bre_ObjectIdentity = ObjectIdentity
tl1bre = _Tl1bre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12)
)
_Tl1breConfigParams_ObjectIdentity = ObjectIdentity
tl1breConfigParams = _Tl1breConfigParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 1)
)


class _Tl1breBridgeNumber_Type(Integer32):
    """Custom type tl1breBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Tl1breBridgeNumber_Type.__name__ = "Integer32"
_Tl1breBridgeNumber_Object = MibScalar
tl1breBridgeNumber = _Tl1breBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 1, 1),
    _Tl1breBridgeNumber_Type()
)
tl1breBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1breBridgeNumber.setStatus("mandatory")
_Tl1breBridgeIpAddress_Type = IpAddress
_Tl1breBridgeIpAddress_Object = MibScalar
tl1breBridgeIpAddress = _Tl1breBridgeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 1, 2),
    _Tl1breBridgeIpAddress_Type()
)
tl1breBridgeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1breBridgeIpAddress.setStatus("mandatory")
_Tl1breForwardTableAgeingTime_Type = Integer32
_Tl1breForwardTableAgeingTime_Object = MibScalar
tl1breForwardTableAgeingTime = _Tl1breForwardTableAgeingTime_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 1, 3),
    _Tl1breForwardTableAgeingTime_Type()
)
tl1breForwardTableAgeingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1breForwardTableAgeingTime.setStatus("mandatory")


class _Tl1breNumConfigBrdgLstEntries_Type(Integer32):
    """Custom type tl1breNumConfigBrdgLstEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Tl1breNumConfigBrdgLstEntries_Type.__name__ = "Integer32"
_Tl1breNumConfigBrdgLstEntries_Object = MibScalar
tl1breNumConfigBrdgLstEntries = _Tl1breNumConfigBrdgLstEntries_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 1, 4),
    _Tl1breNumConfigBrdgLstEntries_Type()
)
tl1breNumConfigBrdgLstEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1breNumConfigBrdgLstEntries.setStatus("mandatory")
_Tl1breConfigBridgeListTable_Object = MibTable
tl1breConfigBridgeListTable = _Tl1breConfigBridgeListTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 2)
)
if mibBuilder.loadTexts:
    tl1breConfigBridgeListTable.setStatus("mandatory")
_Tl1breCBridgeListEntry_Object = MibTableRow
tl1breCBridgeListEntry = _Tl1breCBridgeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    tl1breCBridgeListEntry.setStatus("mandatory")


class _Tl1breCblBridgeNumber_Type(Integer32):
    """Custom type tl1breCblBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Tl1breCblBridgeNumber_Type.__name__ = "Integer32"
_Tl1breCblBridgeNumber_Object = MibTableColumn
tl1breCblBridgeNumber = _Tl1breCblBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 2, 1, 1),
    _Tl1breCblBridgeNumber_Type()
)
tl1breCblBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1breCblBridgeNumber.setStatus("mandatory")


class _Tl1breCblVLanId_Type(Integer32):
    """Custom type tl1breCblVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Tl1breCblVLanId_Type.__name__ = "Integer32"
_Tl1breCblVLanId_Object = MibTableColumn
tl1breCblVLanId = _Tl1breCblVLanId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 2, 1, 2),
    _Tl1breCblVLanId_Type()
)
tl1breCblVLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1breCblVLanId.setStatus("mandatory")


class _Tl1breCblSrBridgeNumber_Type(Integer32):
    """Custom type tl1breCblSrBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Tl1breCblSrBridgeNumber_Type.__name__ = "Integer32"
_Tl1breCblSrBridgeNumber_Object = MibTableColumn
tl1breCblSrBridgeNumber = _Tl1breCblSrBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 2, 1, 3),
    _Tl1breCblSrBridgeNumber_Type()
)
tl1breCblSrBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1breCblSrBridgeNumber.setStatus("mandatory")
_Tl1breCblIpAddress_Type = IpAddress
_Tl1breCblIpAddress_Object = MibTableColumn
tl1breCblIpAddress = _Tl1breCblIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 2, 1, 4),
    _Tl1breCblIpAddress_Type()
)
tl1breCblIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1breCblIpAddress.setStatus("mandatory")
_Tl1breBridgeListTable_Object = MibTable
tl1breBridgeListTable = _Tl1breBridgeListTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 3)
)
if mibBuilder.loadTexts:
    tl1breBridgeListTable.setStatus("mandatory")
_Tl1breBridgeListEntry_Object = MibTableRow
tl1breBridgeListEntry = _Tl1breBridgeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 3, 1)
)
if mibBuilder.loadTexts:
    tl1breBridgeListEntry.setStatus("mandatory")


class _Tl1breBlBridgeNumber_Type(Integer32):
    """Custom type tl1breBlBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Tl1breBlBridgeNumber_Type.__name__ = "Integer32"
_Tl1breBlBridgeNumber_Object = MibTableColumn
tl1breBlBridgeNumber = _Tl1breBlBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 3, 1, 1),
    _Tl1breBlBridgeNumber_Type()
)
tl1breBlBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breBlBridgeNumber.setStatus("mandatory")


class _Tl1breBlVLanId_Type(Integer32):
    """Custom type tl1breBlVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Tl1breBlVLanId_Type.__name__ = "Integer32"
_Tl1breBlVLanId_Object = MibTableColumn
tl1breBlVLanId = _Tl1breBlVLanId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 3, 1, 2),
    _Tl1breBlVLanId_Type()
)
tl1breBlVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breBlVLanId.setStatus("mandatory")


class _Tl1breBlSrBridgeNumber_Type(Integer32):
    """Custom type tl1breBlSrBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Tl1breBlSrBridgeNumber_Type.__name__ = "Integer32"
_Tl1breBlSrBridgeNumber_Object = MibTableColumn
tl1breBlSrBridgeNumber = _Tl1breBlSrBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 3, 1, 3),
    _Tl1breBlSrBridgeNumber_Type()
)
tl1breBlSrBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breBlSrBridgeNumber.setStatus("mandatory")
_Tl1breBlIpAddress_Type = IpAddress
_Tl1breBlIpAddress_Object = MibTableColumn
tl1breBlIpAddress = _Tl1breBlIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 3, 1, 4),
    _Tl1breBlIpAddress_Type()
)
tl1breBlIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breBlIpAddress.setStatus("mandatory")
_Tl1breForwardTable_Object = MibTable
tl1breForwardTable = _Tl1breForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 4)
)
if mibBuilder.loadTexts:
    tl1breForwardTable.setStatus("mandatory")
_Tl1breForwardTableEntry_Object = MibTableRow
tl1breForwardTableEntry = _Tl1breForwardTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 4, 1)
)
if mibBuilder.loadTexts:
    tl1breForwardTableEntry.setStatus("mandatory")


class _Tl1breFtMacAddress_Type(OctetString):
    """Custom type tl1breFtMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1breFtMacAddress_Type.__name__ = "OctetString"
_Tl1breFtMacAddress_Object = MibTableColumn
tl1breFtMacAddress = _Tl1breFtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 4, 1, 1),
    _Tl1breFtMacAddress_Type()
)
tl1breFtMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breFtMacAddress.setStatus("mandatory")
_Tl1breFtIpAddress_Type = IpAddress
_Tl1breFtIpAddress_Object = MibTableColumn
tl1breFtIpAddress = _Tl1breFtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 4, 1, 2),
    _Tl1breFtIpAddress_Type()
)
tl1breFtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breFtIpAddress.setStatus("mandatory")
_Tl1breStatTable_Object = MibTable
tl1breStatTable = _Tl1breStatTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5)
)
if mibBuilder.loadTexts:
    tl1breStatTable.setStatus("mandatory")
_Tl1breStatEntry_Object = MibTableRow
tl1breStatEntry = _Tl1breStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1)
)
if mibBuilder.loadTexts:
    tl1breStatEntry.setStatus("mandatory")
_Tl1breInTSFs_Type = Counter32
_Tl1breInTSFs_Object = MibTableColumn
tl1breInTSFs = _Tl1breInTSFs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1, 1),
    _Tl1breInTSFs_Type()
)
tl1breInTSFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breInTSFs.setStatus("mandatory")
_Tl1breInSRFs_Type = Counter32
_Tl1breInSRFs_Object = MibTableColumn
tl1breInSRFs = _Tl1breInSRFs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1, 2),
    _Tl1breInSRFs_Type()
)
tl1breInSRFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breInSRFs.setStatus("mandatory")
_Tl1breInEFs_Type = Counter32
_Tl1breInEFs_Object = MibTableColumn
tl1breInEFs = _Tl1breInEFs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1, 3),
    _Tl1breInEFs_Type()
)
tl1breInEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breInEFs.setStatus("mandatory")
_Tl1breInBPDUs_Type = Counter32
_Tl1breInBPDUs_Object = MibTableColumn
tl1breInBPDUs = _Tl1breInBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1, 4),
    _Tl1breInBPDUs_Type()
)
tl1breInBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breInBPDUs.setStatus("mandatory")
_Tl1breInErrors_Type = Counter32
_Tl1breInErrors_Object = MibTableColumn
tl1breInErrors = _Tl1breInErrors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1, 5),
    _Tl1breInErrors_Type()
)
tl1breInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breInErrors.setStatus("mandatory")
_Tl1breOutTSFs_Type = Counter32
_Tl1breOutTSFs_Object = MibTableColumn
tl1breOutTSFs = _Tl1breOutTSFs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1, 6),
    _Tl1breOutTSFs_Type()
)
tl1breOutTSFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breOutTSFs.setStatus("mandatory")
_Tl1breOutSRFs_Type = Counter32
_Tl1breOutSRFs_Object = MibTableColumn
tl1breOutSRFs = _Tl1breOutSRFs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1, 7),
    _Tl1breOutSRFs_Type()
)
tl1breOutSRFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breOutSRFs.setStatus("mandatory")
_Tl1breOutEFs_Type = Counter32
_Tl1breOutEFs_Object = MibTableColumn
tl1breOutEFs = _Tl1breOutEFs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1, 8),
    _Tl1breOutEFs_Type()
)
tl1breOutEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breOutEFs.setStatus("mandatory")
_Tl1breOutBPDUs_Type = Counter32
_Tl1breOutBPDUs_Object = MibTableColumn
tl1breOutBPDUs = _Tl1breOutBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 12, 5, 1, 9),
    _Tl1breOutBPDUs_Type()
)
tl1breOutBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1breOutBPDUs.setStatus("mandatory")
_Tl1rip_ObjectIdentity = ObjectIdentity
tl1rip = _Tl1rip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13)
)
_Tl1ripInPkts_Type = Counter32
_Tl1ripInPkts_Object = MibScalar
tl1ripInPkts = _Tl1ripInPkts_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 1),
    _Tl1ripInPkts_Type()
)
tl1ripInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripInPkts.setStatus("mandatory")
_Tl1ripOutPkts_Type = Counter32
_Tl1ripOutPkts_Object = MibScalar
tl1ripOutPkts = _Tl1ripOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 2),
    _Tl1ripOutPkts_Type()
)
tl1ripOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripOutPkts.setStatus("mandatory")
_Tl1ripBadSize_Type = Counter32
_Tl1ripBadSize_Object = MibScalar
tl1ripBadSize = _Tl1ripBadSize_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 3),
    _Tl1ripBadSize_Type()
)
tl1ripBadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripBadSize.setStatus("mandatory")
_Tl1ripBadVersion_Type = Counter32
_Tl1ripBadVersion_Object = MibScalar
tl1ripBadVersion = _Tl1ripBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 4),
    _Tl1ripBadVersion_Type()
)
tl1ripBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripBadVersion.setStatus("mandatory")
_Tl1ripNonZero_Type = Counter32
_Tl1ripNonZero_Object = MibScalar
tl1ripNonZero = _Tl1ripNonZero_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 5),
    _Tl1ripNonZero_Type()
)
tl1ripNonZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripNonZero.setStatus("mandatory")
_Tl1ripBadFamily_Type = Counter32
_Tl1ripBadFamily_Object = MibScalar
tl1ripBadFamily = _Tl1ripBadFamily_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 6),
    _Tl1ripBadFamily_Type()
)
tl1ripBadFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripBadFamily.setStatus("mandatory")
_Tl1ripBadPort_Type = Counter32
_Tl1ripBadPort_Object = MibScalar
tl1ripBadPort = _Tl1ripBadPort_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 7),
    _Tl1ripBadPort_Type()
)
tl1ripBadPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripBadPort.setStatus("mandatory")
_Tl1ripBadMetric_Type = Counter32
_Tl1ripBadMetric_Object = MibScalar
tl1ripBadMetric = _Tl1ripBadMetric_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 8),
    _Tl1ripBadMetric_Type()
)
tl1ripBadMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripBadMetric.setStatus("mandatory")
_Tl1ripBadAddr_Type = Counter32
_Tl1ripBadAddr_Object = MibScalar
tl1ripBadAddr = _Tl1ripBadAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 9),
    _Tl1ripBadAddr_Type()
)
tl1ripBadAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripBadAddr.setStatus("mandatory")
_Tl1ripBadCommand_Type = Counter32
_Tl1ripBadCommand_Object = MibScalar
tl1ripBadCommand = _Tl1ripBadCommand_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 10),
    _Tl1ripBadCommand_Type()
)
tl1ripBadCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripBadCommand.setStatus("mandatory")
_Tl1ripBadClass_Type = Counter32
_Tl1ripBadClass_Object = MibScalar
tl1ripBadClass = _Tl1ripBadClass_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 11),
    _Tl1ripBadClass_Type()
)
tl1ripBadClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripBadClass.setStatus("mandatory")
_Tl1ripBadNbr_Type = Counter32
_Tl1ripBadNbr_Object = MibScalar
tl1ripBadNbr = _Tl1ripBadNbr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 12),
    _Tl1ripBadNbr_Type()
)
tl1ripBadNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripBadNbr.setStatus("mandatory")
_Tl1ripOwnAddr_Type = Counter32
_Tl1ripOwnAddr_Object = MibScalar
tl1ripOwnAddr = _Tl1ripOwnAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 13),
    _Tl1ripOwnAddr_Type()
)
tl1ripOwnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ripOwnAddr.setStatus("mandatory")
_Tl1ripConfigTable_Object = MibTable
tl1ripConfigTable = _Tl1ripConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 14)
)
if mibBuilder.loadTexts:
    tl1ripConfigTable.setStatus("mandatory")
_Tl1ripConfigEntry_Object = MibTableRow
tl1ripConfigEntry = _Tl1ripConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 14, 1)
)
if mibBuilder.loadTexts:
    tl1ripConfigEntry.setStatus("mandatory")


class _Tl1ripMode_Type(Integer32):
    """Custom type tl1ripMode based on Integer32"""
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
        *(("deaf", 4),
          ("disabled", 1),
          ("fully-operational", 3),
          ("silent", 2))
    )


_Tl1ripMode_Type.__name__ = "Integer32"
_Tl1ripMode_Object = MibTableColumn
tl1ripMode = _Tl1ripMode_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 14, 1, 1),
    _Tl1ripMode_Type()
)
tl1ripMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ripMode.setStatus("mandatory")


class _Tl1ripSimple_Type(Integer32):
    """Custom type tl1ripSimple based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("poisoned-reverse", 1),
          ("simple-split-horizon", 2))
    )


_Tl1ripSimple_Type.__name__ = "Integer32"
_Tl1ripSimple_Object = MibTableColumn
tl1ripSimple = _Tl1ripSimple_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 14, 1, 2),
    _Tl1ripSimple_Type()
)
tl1ripSimple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ripSimple.setStatus("mandatory")


class _Tl1ripAdverStatic_Type(Integer32):
    """Custom type tl1ripAdverStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("dont-advertise", 1))
    )


_Tl1ripAdverStatic_Type.__name__ = "Integer32"
_Tl1ripAdverStatic_Object = MibTableColumn
tl1ripAdverStatic = _Tl1ripAdverStatic_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 14, 1, 3),
    _Tl1ripAdverStatic_Type()
)
tl1ripAdverStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ripAdverStatic.setStatus("mandatory")


class _Tl1ripAdverIntf_Type(Integer32):
    """Custom type tl1ripAdverIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("dont-advertise", 1))
    )


_Tl1ripAdverIntf_Type.__name__ = "Integer32"
_Tl1ripAdverIntf_Object = MibTableColumn
tl1ripAdverIntf = _Tl1ripAdverIntf_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 14, 1, 4),
    _Tl1ripAdverIntf_Type()
)
tl1ripAdverIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ripAdverIntf.setStatus("mandatory")
_Tl1ripHolddown_Type = Integer32
_Tl1ripHolddown_Object = MibTableColumn
tl1ripHolddown = _Tl1ripHolddown_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 13, 14, 1, 5),
    _Tl1ripHolddown_Type()
)
tl1ripHolddown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ripHolddown.setStatus("mandatory")
_Tl1x25_ObjectIdentity = ObjectIdentity
tl1x25 = _Tl1x25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14)
)
_Tl1x25IfTable_Object = MibTable
tl1x25IfTable = _Tl1x25IfTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1)
)
if mibBuilder.loadTexts:
    tl1x25IfTable.setStatus("mandatory")
_Tl1x25IfEntry_Object = MibTableRow
tl1x25IfEntry = _Tl1x25IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    tl1x25IfEntry.setStatus("mandatory")
_Tl1x25InPkts_Type = Counter32
_Tl1x25InPkts_Object = MibTableColumn
tl1x25InPkts = _Tl1x25InPkts_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 1),
    _Tl1x25InPkts_Type()
)
tl1x25InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25InPkts.setStatus("mandatory")
_Tl1x25OutPkts_Type = Counter32
_Tl1x25OutPkts_Object = MibTableColumn
tl1x25OutPkts = _Tl1x25OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 2),
    _Tl1x25OutPkts_Type()
)
tl1x25OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25OutPkts.setStatus("mandatory")
_Tl1x25GFI_Type = Counter32
_Tl1x25GFI_Object = MibTableColumn
tl1x25GFI = _Tl1x25GFI_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 3),
    _Tl1x25GFI_Type()
)
tl1x25GFI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25GFI.setStatus("mandatory")
_Tl1x25PktInv_Type = Counter32
_Tl1x25PktInv_Object = MibTableColumn
tl1x25PktInv = _Tl1x25PktInv_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 4),
    _Tl1x25PktInv_Type()
)
tl1x25PktInv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PktInv.setStatus("mandatory")
_Tl1x25PinvR1_Type = Counter32
_Tl1x25PinvR1_Object = MibTableColumn
tl1x25PinvR1 = _Tl1x25PinvR1_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 5),
    _Tl1x25PinvR1_Type()
)
tl1x25PinvR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvR1.setStatus("mandatory")
_Tl1x25PinvR2_Type = Counter32
_Tl1x25PinvR2_Object = MibTableColumn
tl1x25PinvR2 = _Tl1x25PinvR2_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 6),
    _Tl1x25PinvR2_Type()
)
tl1x25PinvR2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvR2.setStatus("mandatory")
_Tl1x25PinvR3_Type = Counter32
_Tl1x25PinvR3_Object = MibTableColumn
tl1x25PinvR3 = _Tl1x25PinvR3_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 7),
    _Tl1x25PinvR3_Type()
)
tl1x25PinvR3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvR3.setStatus("mandatory")
_Tl1x25PinvP1_Type = Counter32
_Tl1x25PinvP1_Object = MibTableColumn
tl1x25PinvP1 = _Tl1x25PinvP1_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 8),
    _Tl1x25PinvP1_Type()
)
tl1x25PinvP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvP1.setStatus("mandatory")
_Tl1x25PinvP2_Type = Counter32
_Tl1x25PinvP2_Object = MibTableColumn
tl1x25PinvP2 = _Tl1x25PinvP2_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 9),
    _Tl1x25PinvP2_Type()
)
tl1x25PinvP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvP2.setStatus("mandatory")
_Tl1x25PinvP3_Type = Counter32
_Tl1x25PinvP3_Object = MibTableColumn
tl1x25PinvP3 = _Tl1x25PinvP3_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 10),
    _Tl1x25PinvP3_Type()
)
tl1x25PinvP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvP3.setStatus("mandatory")
_Tl1x25PinvP4_Type = Counter32
_Tl1x25PinvP4_Object = MibTableColumn
tl1x25PinvP4 = _Tl1x25PinvP4_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 11),
    _Tl1x25PinvP4_Type()
)
tl1x25PinvP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvP4.setStatus("mandatory")
_Tl1x25PinvP5_Type = Counter32
_Tl1x25PinvP5_Object = MibTableColumn
tl1x25PinvP5 = _Tl1x25PinvP5_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 12),
    _Tl1x25PinvP5_Type()
)
tl1x25PinvP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvP5.setStatus("mandatory")
_Tl1x25PinvP6_Type = Counter32
_Tl1x25PinvP6_Object = MibTableColumn
tl1x25PinvP6 = _Tl1x25PinvP6_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 13),
    _Tl1x25PinvP6_Type()
)
tl1x25PinvP6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvP6.setStatus("mandatory")
_Tl1x25PinvP7_Type = Counter32
_Tl1x25PinvP7_Object = MibTableColumn
tl1x25PinvP7 = _Tl1x25PinvP7_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 14),
    _Tl1x25PinvP7_Type()
)
tl1x25PinvP7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvP7.setStatus("mandatory")
_Tl1x25PinvD1_Type = Counter32
_Tl1x25PinvD1_Object = MibTableColumn
tl1x25PinvD1 = _Tl1x25PinvD1_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 15),
    _Tl1x25PinvD1_Type()
)
tl1x25PinvD1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvD1.setStatus("mandatory")
_Tl1x25PinvD2_Type = Counter32
_Tl1x25PinvD2_Object = MibTableColumn
tl1x25PinvD2 = _Tl1x25PinvD2_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 16),
    _Tl1x25PinvD2_Type()
)
tl1x25PinvD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvD2.setStatus("mandatory")
_Tl1x25PinvD3_Type = Counter32
_Tl1x25PinvD3_Object = MibTableColumn
tl1x25PinvD3 = _Tl1x25PinvD3_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 17),
    _Tl1x25PinvD3_Type()
)
tl1x25PinvD3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PinvD3.setStatus("mandatory")
_Tl1x25PktLong_Type = Counter32
_Tl1x25PktLong_Object = MibTableColumn
tl1x25PktLong = _Tl1x25PktLong_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 18),
    _Tl1x25PktLong_Type()
)
tl1x25PktLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PktLong.setStatus("mandatory")
_Tl1x25PktShort_Type = Counter32
_Tl1x25PktShort_Object = MibTableColumn
tl1x25PktShort = _Tl1x25PktShort_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 19),
    _Tl1x25PktShort_Type()
)
tl1x25PktShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25PktShort.setStatus("mandatory")
_Tl1x25CallingAddr_Type = Counter32
_Tl1x25CallingAddr_Object = MibTableColumn
tl1x25CallingAddr = _Tl1x25CallingAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 20),
    _Tl1x25CallingAddr_Type()
)
tl1x25CallingAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25CallingAddr.setStatus("mandatory")
_Tl1x25CalledAddr_Type = Counter32
_Tl1x25CalledAddr_Object = MibTableColumn
tl1x25CalledAddr = _Tl1x25CalledAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 21),
    _Tl1x25CalledAddr_Type()
)
tl1x25CalledAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25CalledAddr.setStatus("mandatory")
_Tl1x25CallBad_Type = Counter32
_Tl1x25CallBad_Object = MibTableColumn
tl1x25CallBad = _Tl1x25CallBad_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 22),
    _Tl1x25CallBad_Type()
)
tl1x25CallBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25CallBad.setStatus("mandatory")
_Tl1x25FacParam_Type = Counter32
_Tl1x25FacParam_Object = MibTableColumn
tl1x25FacParam = _Tl1x25FacParam_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 23),
    _Tl1x25FacParam_Type()
)
tl1x25FacParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25FacParam.setStatus("mandatory")
_Tl1x25FacCode_Type = Counter32
_Tl1x25FacCode_Object = MibTableColumn
tl1x25FacCode = _Tl1x25FacCode_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 24),
    _Tl1x25FacCode_Type()
)
tl1x25FacCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25FacCode.setStatus("mandatory")
_Tl1x25BadPkt_Type = Counter32
_Tl1x25BadPkt_Object = MibTableColumn
tl1x25BadPkt = _Tl1x25BadPkt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 25),
    _Tl1x25BadPkt_Type()
)
tl1x25BadPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25BadPkt.setStatus("mandatory")
_Tl1x25RejInv_Type = Counter32
_Tl1x25RejInv_Object = MibTableColumn
tl1x25RejInv = _Tl1x25RejInv_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 26),
    _Tl1x25RejInv_Type()
)
tl1x25RejInv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25RejInv.setStatus("mandatory")
_Tl1x25LcRestr_Type = Counter32
_Tl1x25LcRestr_Object = MibTableColumn
tl1x25LcRestr = _Tl1x25LcRestr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 27),
    _Tl1x25LcRestr_Type()
)
tl1x25LcRestr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25LcRestr.setStatus("mandatory")
_Tl1x25IntrCPkt_Type = Counter32
_Tl1x25IntrCPkt_Object = MibTableColumn
tl1x25IntrCPkt = _Tl1x25IntrCPkt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 28),
    _Tl1x25IntrCPkt_Type()
)
tl1x25IntrCPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25IntrCPkt.setStatus("mandatory")
_Tl1x25CallTimer_Type = Counter32
_Tl1x25CallTimer_Object = MibTableColumn
tl1x25CallTimer = _Tl1x25CallTimer_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 29),
    _Tl1x25CallTimer_Type()
)
tl1x25CallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25CallTimer.setStatus("mandatory")
_Tl1x25ResetTimer_Type = Counter32
_Tl1x25ResetTimer_Object = MibTableColumn
tl1x25ResetTimer = _Tl1x25ResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 30),
    _Tl1x25ResetTimer_Type()
)
tl1x25ResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1x25ResetTimer.setStatus("mandatory")


class _Tl1x25Service_Type(Integer32):
    """Custom type tl1x25Service based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic-service", 1),
          ("standard-service", 2))
    )


_Tl1x25Service_Type.__name__ = "Integer32"
_Tl1x25Service_Object = MibTableColumn
tl1x25Service = _Tl1x25Service_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 31),
    _Tl1x25Service_Type()
)
tl1x25Service.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1x25Service.setStatus("mandatory")


class _Tl1x25Window_Type(Integer32):
    """Custom type tl1x25Window based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_Tl1x25Window_Type.__name__ = "Integer32"
_Tl1x25Window_Object = MibTableColumn
tl1x25Window = _Tl1x25Window_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 32),
    _Tl1x25Window_Type()
)
tl1x25Window.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1x25Window.setStatus("mandatory")


class _Tl1x25PktSize_Type(Integer32):
    """Custom type tl1x25PktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 11),
    )


_Tl1x25PktSize_Type.__name__ = "Integer32"
_Tl1x25PktSize_Object = MibTableColumn
tl1x25PktSize = _Tl1x25PktSize_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 14, 1, 1, 33),
    _Tl1x25PktSize_Type()
)
tl1x25PktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1x25PktSize.setStatus("mandatory")
_Tl1fddi_ObjectIdentity = ObjectIdentity
tl1fddi = _Tl1fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15)
)
_Tl1fddiMACStatTable_Object = MibTable
tl1fddiMACStatTable = _Tl1fddiMACStatTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1)
)
if mibBuilder.loadTexts:
    tl1fddiMACStatTable.setStatus("mandatory")
_Tl1fddiMACStatEntry_Object = MibTableRow
tl1fddiMACStatEntry = _Tl1fddiMACStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1)
)
if mibBuilder.loadTexts:
    tl1fddiMACStatEntry.setStatus("mandatory")
_Tl1fddiMACRcvAbort_Type = Counter32
_Tl1fddiMACRcvAbort_Object = MibTableColumn
tl1fddiMACRcvAbort = _Tl1fddiMACRcvAbort_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 1),
    _Tl1fddiMACRcvAbort_Type()
)
tl1fddiMACRcvAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACRcvAbort.setStatus("mandatory")
_Tl1fddiMACRcvOverflow_Type = Counter32
_Tl1fddiMACRcvOverflow_Object = MibTableColumn
tl1fddiMACRcvOverflow = _Tl1fddiMACRcvOverflow_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 2),
    _Tl1fddiMACRcvOverflow_Type()
)
tl1fddiMACRcvOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACRcvOverflow.setStatus("mandatory")
_Tl1fddiMACRcvUnderflow_Type = Counter32
_Tl1fddiMACRcvUnderflow_Object = MibTableColumn
tl1fddiMACRcvUnderflow = _Tl1fddiMACRcvUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 3),
    _Tl1fddiMACRcvUnderflow_Type()
)
tl1fddiMACRcvUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACRcvUnderflow.setStatus("mandatory")
_Tl1fddiMACRbcCollision_Type = Counter32
_Tl1fddiMACRbcCollision_Object = MibTableColumn
tl1fddiMACRbcCollision = _Tl1fddiMACRbcCollision_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 4),
    _Tl1fddiMACRbcCollision_Type()
)
tl1fddiMACRbcCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACRbcCollision.setStatus("mandatory")
_Tl1fddiMACTxSyncChain_Type = Counter32
_Tl1fddiMACTxSyncChain_Object = MibTableColumn
tl1fddiMACTxSyncChain = _Tl1fddiMACTxSyncChain_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 5),
    _Tl1fddiMACTxSyncChain_Type()
)
tl1fddiMACTxSyncChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTxSyncChain.setStatus("mandatory")
_Tl1fddiMACTxAsyncChain_Type = Counter32
_Tl1fddiMACTxAsyncChain_Object = MibTableColumn
tl1fddiMACTxAsyncChain = _Tl1fddiMACTxAsyncChain_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 6),
    _Tl1fddiMACTxAsyncChain_Type()
)
tl1fddiMACTxAsyncChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTxAsyncChain.setStatus("mandatory")
_Tl1fddiMACTxSyncFrm_Type = Counter32
_Tl1fddiMACTxSyncFrm_Object = MibTableColumn
tl1fddiMACTxSyncFrm = _Tl1fddiMACTxSyncFrm_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 7),
    _Tl1fddiMACTxSyncFrm_Type()
)
tl1fddiMACTxSyncFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTxSyncFrm.setStatus("mandatory")
_Tl1fddiMACTxAsyncFrm_Type = Counter32
_Tl1fddiMACTxAsyncFrm_Object = MibTableColumn
tl1fddiMACTxAsyncFrm = _Tl1fddiMACTxAsyncFrm_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 8),
    _Tl1fddiMACTxAsyncFrm_Type()
)
tl1fddiMACTxAsyncFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTxAsyncFrm.setStatus("mandatory")
_Tl1fddiMACTxSyncDone_Type = Counter32
_Tl1fddiMACTxSyncDone_Object = MibTableColumn
tl1fddiMACTxSyncDone = _Tl1fddiMACTxSyncDone_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 9),
    _Tl1fddiMACTxSyncDone_Type()
)
tl1fddiMACTxSyncDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTxSyncDone.setStatus("mandatory")
_Tl1fddiMACTxAsyncDone_Type = Counter32
_Tl1fddiMACTxAsyncDone_Object = MibTableColumn
tl1fddiMACTxAsyncDone = _Tl1fddiMACTxAsyncDone_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 10),
    _Tl1fddiMACTxAsyncDone_Type()
)
tl1fddiMACTxAsyncDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTxAsyncDone.setStatus("mandatory")
_Tl1fddiMACTxBufEmpty_Type = Counter32
_Tl1fddiMACTxBufEmpty_Object = MibTableColumn
tl1fddiMACTxBufEmpty = _Tl1fddiMACTxBufEmpty_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 11),
    _Tl1fddiMACTxBufEmpty_Type()
)
tl1fddiMACTxBufEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTxBufEmpty.setStatus("mandatory")
_Tl1fddiMACTxAbort_Type = Counter32
_Tl1fddiMACTxAbort_Object = MibTableColumn
tl1fddiMACTxAbort = _Tl1fddiMACTxAbort_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 12),
    _Tl1fddiMACTxAbort_Type()
)
tl1fddiMACTxAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTxAbort.setStatus("mandatory")
_Tl1fddiMACRxFrmsRcvd_Type = Counter32
_Tl1fddiMACRxFrmsRcvd_Object = MibTableColumn
tl1fddiMACRxFrmsRcvd = _Tl1fddiMACRxFrmsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 13),
    _Tl1fddiMACRxFrmsRcvd_Type()
)
tl1fddiMACRxFrmsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACRxFrmsRcvd.setStatus("mandatory")
_Tl1fddiMACRxSmallGap_Type = Counter32
_Tl1fddiMACRxSmallGap_Object = MibTableColumn
tl1fddiMACRxSmallGap = _Tl1fddiMACRxSmallGap_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 14),
    _Tl1fddiMACRxSmallGap_Type()
)
tl1fddiMACRxSmallGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACRxSmallGap.setStatus("mandatory")
_Tl1fddiMACDpcCollision_Type = Counter32
_Tl1fddiMACDpcCollision_Object = MibTableColumn
tl1fddiMACDpcCollision = _Tl1fddiMACDpcCollision_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 15),
    _Tl1fddiMACDpcCollision_Type()
)
tl1fddiMACDpcCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACDpcCollision.setStatus("mandatory")
_Tl1fddiMACBadSyncPtr_Type = Counter32
_Tl1fddiMACBadSyncPtr_Object = MibTableColumn
tl1fddiMACBadSyncPtr = _Tl1fddiMACBadSyncPtr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 16),
    _Tl1fddiMACBadSyncPtr_Type()
)
tl1fddiMACBadSyncPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACBadSyncPtr.setStatus("mandatory")
_Tl1fddiMACBadAsyncPtr_Type = Counter32
_Tl1fddiMACBadAsyncPtr_Object = MibTableColumn
tl1fddiMACBadAsyncPtr = _Tl1fddiMACBadAsyncPtr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 17),
    _Tl1fddiMACBadAsyncPtr_Type()
)
tl1fddiMACBadAsyncPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACBadAsyncPtr.setStatus("mandatory")
_Tl1fddiMACOtherBecRcvd_Type = Counter32
_Tl1fddiMACOtherBecRcvd_Object = MibTableColumn
tl1fddiMACOtherBecRcvd = _Tl1fddiMACOtherBecRcvd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 18),
    _Tl1fddiMACOtherBecRcvd_Type()
)
tl1fddiMACOtherBecRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACOtherBecRcvd.setStatus("mandatory")
_Tl1fddiMACOwnBecRcvd_Type = Counter32
_Tl1fddiMACOwnBecRcvd_Object = MibTableColumn
tl1fddiMACOwnBecRcvd = _Tl1fddiMACOwnBecRcvd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 19),
    _Tl1fddiMACOwnBecRcvd_Type()
)
tl1fddiMACOwnBecRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACOwnBecRcvd.setStatus("mandatory")
_Tl1fddiMACHighClmRcvd_Type = Counter32
_Tl1fddiMACHighClmRcvd_Object = MibTableColumn
tl1fddiMACHighClmRcvd = _Tl1fddiMACHighClmRcvd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 20),
    _Tl1fddiMACHighClmRcvd_Type()
)
tl1fddiMACHighClmRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACHighClmRcvd.setStatus("mandatory")
_Tl1fddiMACLowClmRcvd_Type = Counter32
_Tl1fddiMACLowClmRcvd_Object = MibTableColumn
tl1fddiMACLowClmRcvd = _Tl1fddiMACLowClmRcvd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 21),
    _Tl1fddiMACLowClmRcvd_Type()
)
tl1fddiMACLowClmRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACLowClmRcvd.setStatus("mandatory")
_Tl1fddiMACWonClaimBid_Type = Counter32
_Tl1fddiMACWonClaimBid_Object = MibTableColumn
tl1fddiMACWonClaimBid = _Tl1fddiMACWonClaimBid_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 22),
    _Tl1fddiMACWonClaimBid_Type()
)
tl1fddiMACWonClaimBid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACWonClaimBid.setStatus("mandatory")
_Tl1fddiMACPktsDetected_Type = Counter32
_Tl1fddiMACPktsDetected_Object = MibTableColumn
tl1fddiMACPktsDetected = _Tl1fddiMACPktsDetected_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 23),
    _Tl1fddiMACPktsDetected_Type()
)
tl1fddiMACPktsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACPktsDetected.setStatus("mandatory")
_Tl1fddiMACTokenCt_Type = Counter32
_Tl1fddiMACTokenCt_Object = MibTableColumn
tl1fddiMACTokenCt = _Tl1fddiMACTokenCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 24),
    _Tl1fddiMACTokenCt_Type()
)
tl1fddiMACTokenCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTokenCt.setStatus("mandatory")
_Tl1fddiMACLateCt_Type = Counter32
_Tl1fddiMACLateCt_Object = MibTableColumn
tl1fddiMACLateCt = _Tl1fddiMACLateCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 25),
    _Tl1fddiMACLateCt_Type()
)
tl1fddiMACLateCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACLateCt.setStatus("mandatory")
_Tl1fddiMACTvxExpiredCt_Type = Counter32
_Tl1fddiMACTvxExpiredCt_Object = MibTableColumn
tl1fddiMACTvxExpiredCt = _Tl1fddiMACTvxExpiredCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 26),
    _Tl1fddiMACTvxExpiredCt_Type()
)
tl1fddiMACTvxExpiredCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTvxExpiredCt.setStatus("mandatory")
_Tl1fddiMACEnterBeacontCt_Type = Counter32
_Tl1fddiMACEnterBeacontCt_Object = MibTableColumn
tl1fddiMACEnterBeacontCt = _Tl1fddiMACEnterBeacontCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 27),
    _Tl1fddiMACEnterBeacontCt_Type()
)
tl1fddiMACEnterBeacontCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACEnterBeacontCt.setStatus("mandatory")
_Tl1fddiMACEnterClaimCt_Type = Counter32
_Tl1fddiMACEnterClaimCt_Object = MibTableColumn
tl1fddiMACEnterClaimCt = _Tl1fddiMACEnterClaimCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 28),
    _Tl1fddiMACEnterClaimCt_Type()
)
tl1fddiMACEnterClaimCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACEnterClaimCt.setStatus("mandatory")
_Tl1fddiMACMultiTokens_Type = Counter32
_Tl1fddiMACMultiTokens_Object = MibTableColumn
tl1fddiMACMultiTokens = _Tl1fddiMACMultiTokens_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 29),
    _Tl1fddiMACMultiTokens_Type()
)
tl1fddiMACMultiTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACMultiTokens.setStatus("mandatory")
_Tl1fddiMACNotCopiedCt_Type = Counter32
_Tl1fddiMACNotCopiedCt_Object = MibTableColumn
tl1fddiMACNotCopiedCt = _Tl1fddiMACNotCopiedCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 30),
    _Tl1fddiMACNotCopiedCt_Type()
)
tl1fddiMACNotCopiedCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACNotCopiedCt.setStatus("mandatory")
_Tl1fddiMACDuplicateAddr_Type = Counter32
_Tl1fddiMACDuplicateAddr_Object = MibTableColumn
tl1fddiMACDuplicateAddr = _Tl1fddiMACDuplicateAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 31),
    _Tl1fddiMACDuplicateAddr_Type()
)
tl1fddiMACDuplicateAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACDuplicateAddr.setStatus("mandatory")
_Tl1fddiMACRingOpCt_Type = Counter32
_Tl1fddiMACRingOpCt_Object = MibTableColumn
tl1fddiMACRingOpCt = _Tl1fddiMACRingOpCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 32),
    _Tl1fddiMACRingOpCt_Type()
)
tl1fddiMACRingOpCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACRingOpCt.setStatus("mandatory")
_Tl1fddiMACFrameCt_Type = Counter32
_Tl1fddiMACFrameCt_Object = MibTableColumn
tl1fddiMACFrameCt = _Tl1fddiMACFrameCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 33),
    _Tl1fddiMACFrameCt_Type()
)
tl1fddiMACFrameCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACFrameCt.setStatus("mandatory")
_Tl1fddiMACLostCt_Type = Counter32
_Tl1fddiMACLostCt_Object = MibTableColumn
tl1fddiMACLostCt = _Tl1fddiMACLostCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 34),
    _Tl1fddiMACLostCt_Type()
)
tl1fddiMACLostCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACLostCt.setStatus("mandatory")
_Tl1fddiMACErrorCt_Type = Counter32
_Tl1fddiMACErrorCt_Object = MibTableColumn
tl1fddiMACErrorCt = _Tl1fddiMACErrorCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 35),
    _Tl1fddiMACErrorCt_Type()
)
tl1fddiMACErrorCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACErrorCt.setStatus("mandatory")
_Tl1fddiMACOutOfBuf_Type = Counter32
_Tl1fddiMACOutOfBuf_Object = MibTableColumn
tl1fddiMACOutOfBuf = _Tl1fddiMACOutOfBuf_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 36),
    _Tl1fddiMACOutOfBuf_Type()
)
tl1fddiMACOutOfBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACOutOfBuf.setStatus("mandatory")
_Tl1fddiMACReceiveCt_Type = Counter32
_Tl1fddiMACReceiveCt_Object = MibTableColumn
tl1fddiMACReceiveCt = _Tl1fddiMACReceiveCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 37),
    _Tl1fddiMACReceiveCt_Type()
)
tl1fddiMACReceiveCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACReceiveCt.setStatus("mandatory")
_Tl1fddiMACTransmitCt_Type = Counter32
_Tl1fddiMACTransmitCt_Object = MibTableColumn
tl1fddiMACTransmitCt = _Tl1fddiMACTransmitCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 38),
    _Tl1fddiMACTransmitCt_Type()
)
tl1fddiMACTransmitCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTransmitCt.setStatus("mandatory")
_Tl1fddiMACInternalErrorCt_Type = Counter32
_Tl1fddiMACInternalErrorCt_Object = MibTableColumn
tl1fddiMACInternalErrorCt = _Tl1fddiMACInternalErrorCt_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 39),
    _Tl1fddiMACInternalErrorCt_Type()
)
tl1fddiMACInternalErrorCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACInternalErrorCt.setStatus("mandatory")
_Tl1fddiMACTneg_Type = Integer32
_Tl1fddiMACTneg_Object = MibTableColumn
tl1fddiMACTneg = _Tl1fddiMACTneg_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 1, 1, 40),
    _Tl1fddiMACTneg_Type()
)
tl1fddiMACTneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiMACTneg.setStatus("mandatory")
_Tl1fddiSMTStnStateTable_Object = MibTable
tl1fddiSMTStnStateTable = _Tl1fddiSMTStnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 2)
)
if mibBuilder.loadTexts:
    tl1fddiSMTStnStateTable.setStatus("mandatory")
_Tl1fddiSMTStnStateEntry_Object = MibTableRow
tl1fddiSMTStnStateEntry = _Tl1fddiSMTStnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    tl1fddiSMTStnStateEntry.setStatus("mandatory")


class _Tl1fddiSMTStnType_Type(Integer32):
    """Custom type tl1fddiSMTStnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concentrator", 2),
          ("station", 1))
    )


_Tl1fddiSMTStnType_Type.__name__ = "Integer32"
_Tl1fddiSMTStnType_Object = MibTableColumn
tl1fddiSMTStnType = _Tl1fddiSMTStnType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 2, 1, 1),
    _Tl1fddiSMTStnType_Type()
)
tl1fddiSMTStnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiSMTStnType.setStatus("mandatory")
_Tl1fddiSMTVersionId_Type = Integer32
_Tl1fddiSMTVersionId_Object = MibTableColumn
tl1fddiSMTVersionId = _Tl1fddiSMTVersionId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 2, 1, 2),
    _Tl1fddiSMTVersionId_Type()
)
tl1fddiSMTVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiSMTVersionId.setStatus("mandatory")
_Tl1fddiSMTMACCount_Type = Integer32
_Tl1fddiSMTMACCount_Object = MibTableColumn
tl1fddiSMTMACCount = _Tl1fddiSMTMACCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 2, 1, 3),
    _Tl1fddiSMTMACCount_Type()
)
tl1fddiSMTMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiSMTMACCount.setStatus("mandatory")
_Tl1fddiSMTAttachCount_Type = Integer32
_Tl1fddiSMTAttachCount_Object = MibTableColumn
tl1fddiSMTAttachCount = _Tl1fddiSMTAttachCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 2, 1, 4),
    _Tl1fddiSMTAttachCount_Type()
)
tl1fddiSMTAttachCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiSMTAttachCount.setStatus("mandatory")
_Tl1fddiSMTMasterCount_Type = Integer32
_Tl1fddiSMTMasterCount_Object = MibTableColumn
tl1fddiSMTMasterCount = _Tl1fddiSMTMasterCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 2, 1, 5),
    _Tl1fddiSMTMasterCount_Type()
)
tl1fddiSMTMasterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiSMTMasterCount.setStatus("mandatory")


class _Tl1fddiSMTDasScmState_Type(Integer32):
    """Custom type tl1fddiSMTDasScmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cleave-a", 6),
          ("cleave-b", 7),
          ("isolated", 1),
          ("thru", 4),
          ("wrap-a", 2),
          ("wrap-b", 3))
    )


_Tl1fddiSMTDasScmState_Type.__name__ = "Integer32"
_Tl1fddiSMTDasScmState_Object = MibTableColumn
tl1fddiSMTDasScmState = _Tl1fddiSMTDasScmState_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 2, 1, 6),
    _Tl1fddiSMTDasScmState_Type()
)
tl1fddiSMTDasScmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiSMTDasScmState.setStatus("mandatory")


class _Tl1fddiSMTStnId_Type(OctetString):
    """Custom type tl1fddiSMTStnId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1fddiSMTStnId_Type.__name__ = "OctetString"
_Tl1fddiSMTStnId_Object = MibTableColumn
tl1fddiSMTStnId = _Tl1fddiSMTStnId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 2, 1, 7),
    _Tl1fddiSMTStnId_Type()
)
tl1fddiSMTStnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiSMTStnId.setStatus("mandatory")
_Tl1fddiPHYStateTable_Object = MibTable
tl1fddiPHYStateTable = _Tl1fddiPHYStateTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 3)
)
if mibBuilder.loadTexts:
    tl1fddiPHYStateTable.setStatus("mandatory")
_Tl1fddiPHYStateEntry_Object = MibTableRow
tl1fddiPHYStateEntry = _Tl1fddiPHYStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 3, 1)
)
if mibBuilder.loadTexts:
    tl1fddiPHYStateEntry.setStatus("mandatory")


class _Tl1fddiPHYType_Type(Integer32):
    """Custom type tl1fddiPHYType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("s", 3))
    )


_Tl1fddiPHYType_Type.__name__ = "Integer32"
_Tl1fddiPHYType_Object = MibTableColumn
tl1fddiPHYType = _Tl1fddiPHYType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 3, 1, 1),
    _Tl1fddiPHYType_Type()
)
tl1fddiPHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiPHYType.setStatus("mandatory")


class _Tl1fddiPHYConnectState_Type(Integer32):
    """Custom type tl1fddiPHYConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Tl1fddiPHYConnectState_Type.__name__ = "Integer32"
_Tl1fddiPHYConnectState_Object = MibTableColumn
tl1fddiPHYConnectState = _Tl1fddiPHYConnectState_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 3, 1, 2),
    _Tl1fddiPHYConnectState_Type()
)
tl1fddiPHYConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiPHYConnectState.setStatus("mandatory")


class _Tl1fddiPHYRemotePHYType_Type(Integer32):
    """Custom type tl1fddiPHYRemotePHYType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("s", 3),
          ("unknown", 5))
    )


_Tl1fddiPHYRemotePHYType_Type.__name__ = "Integer32"
_Tl1fddiPHYRemotePHYType_Object = MibTableColumn
tl1fddiPHYRemotePHYType = _Tl1fddiPHYRemotePHYType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 3, 1, 3),
    _Tl1fddiPHYRemotePHYType_Type()
)
tl1fddiPHYRemotePHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiPHYRemotePHYType.setStatus("mandatory")
_Tl1fddiPHYRemoteMACIndicated_Type = Integer32
_Tl1fddiPHYRemoteMACIndicated_Object = MibTableColumn
tl1fddiPHYRemoteMACIndicated = _Tl1fddiPHYRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 3, 1, 4),
    _Tl1fddiPHYRemoteMACIndicated_Type()
)
tl1fddiPHYRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiPHYRemoteMACIndicated.setStatus("mandatory")
_Tl1fddiPHYResourceIndex_Type = Integer32
_Tl1fddiPHYResourceIndex_Object = MibTableColumn
tl1fddiPHYResourceIndex = _Tl1fddiPHYResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 3, 1, 5),
    _Tl1fddiPHYResourceIndex_Type()
)
tl1fddiPHYResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiPHYResourceIndex.setStatus("mandatory")
_Tl1fddiPHYConnectedResId_Type = Integer32
_Tl1fddiPHYConnectedResId_Object = MibTableColumn
tl1fddiPHYConnectedResId = _Tl1fddiPHYConnectedResId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 3, 1, 6),
    _Tl1fddiPHYConnectedResId_Type()
)
tl1fddiPHYConnectedResId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiPHYConnectedResId.setStatus("mandatory")
_Tl1fddiSMTOperationalTable_Object = MibTable
tl1fddiSMTOperationalTable = _Tl1fddiSMTOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 4)
)
if mibBuilder.loadTexts:
    tl1fddiSMTOperationalTable.setStatus("mandatory")
_Tl1fddiSMTOperationalEntry_Object = MibTableRow
tl1fddiSMTOperationalEntry = _Tl1fddiSMTOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 4, 1)
)
if mibBuilder.loadTexts:
    tl1fddiSMTOperationalEntry.setStatus("mandatory")


class _Tl1fddiSMTLinkErrorRateCutoff_Type(Integer32):
    """Custom type tl1fddiSMTLinkErrorRateCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Tl1fddiSMTLinkErrorRateCutoff_Type.__name__ = "Integer32"
_Tl1fddiSMTLinkErrorRateCutoff_Object = MibTableColumn
tl1fddiSMTLinkErrorRateCutoff = _Tl1fddiSMTLinkErrorRateCutoff_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 4, 1, 1),
    _Tl1fddiSMTLinkErrorRateCutoff_Type()
)
tl1fddiSMTLinkErrorRateCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiSMTLinkErrorRateCutoff.setStatus("mandatory")


class _Tl1fddiSMTLinkErrorRateAlarm_Type(Integer32):
    """Custom type tl1fddiSMTLinkErrorRateAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Tl1fddiSMTLinkErrorRateAlarm_Type.__name__ = "Integer32"
_Tl1fddiSMTLinkErrorRateAlarm_Object = MibTableColumn
tl1fddiSMTLinkErrorRateAlarm = _Tl1fddiSMTLinkErrorRateAlarm_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 4, 1, 2),
    _Tl1fddiSMTLinkErrorRateAlarm_Type()
)
tl1fddiSMTLinkErrorRateAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiSMTLinkErrorRateAlarm.setStatus("mandatory")


class _Tl1fddiSMTByPassSwitchPresent_Type(Integer32):
    """Custom type tl1fddiSMTByPassSwitchPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1fddiSMTByPassSwitchPresent_Type.__name__ = "Integer32"
_Tl1fddiSMTByPassSwitchPresent_Object = MibTableColumn
tl1fddiSMTByPassSwitchPresent = _Tl1fddiSMTByPassSwitchPresent_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 4, 1, 3),
    _Tl1fddiSMTByPassSwitchPresent_Type()
)
tl1fddiSMTByPassSwitchPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiSMTByPassSwitchPresent.setStatus("mandatory")


class _Tl1fddiSMTAttachConfiguration_Type(Integer32):
    """Custom type tl1fddiSMTAttachConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleave-A", 1),
          ("cleave-B", 2),
          ("dualattach", 3))
    )


_Tl1fddiSMTAttachConfiguration_Type.__name__ = "Integer32"
_Tl1fddiSMTAttachConfiguration_Object = MibTableColumn
tl1fddiSMTAttachConfiguration = _Tl1fddiSMTAttachConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 4, 1, 4),
    _Tl1fddiSMTAttachConfiguration_Type()
)
tl1fddiSMTAttachConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiSMTAttachConfiguration.setStatus("mandatory")
_Tl1fddiMACOperationalTable_Object = MibTable
tl1fddiMACOperationalTable = _Tl1fddiMACOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 5)
)
if mibBuilder.loadTexts:
    tl1fddiMACOperationalTable.setStatus("mandatory")
_Tl1fddiMACOperationalEntry_Object = MibTableRow
tl1fddiMACOperationalEntry = _Tl1fddiMACOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 5, 1)
)
if mibBuilder.loadTexts:
    tl1fddiMACOperationalEntry.setStatus("mandatory")


class _Tl1fddiMACTReq_Type(Integer32):
    """Custom type tl1fddiMACTReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 335540),
    )


_Tl1fddiMACTReq_Type.__name__ = "Integer32"
_Tl1fddiMACTReq_Object = MibTableColumn
tl1fddiMACTReq = _Tl1fddiMACTReq_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 5, 1, 1),
    _Tl1fddiMACTReq_Type()
)
tl1fddiMACTReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiMACTReq.setStatus("mandatory")


class _Tl1fddiMACTMax_Type(Integer32):
    """Custom type tl1fddiMACTMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 335540),
    )


_Tl1fddiMACTMax_Type.__name__ = "Integer32"
_Tl1fddiMACTMax_Object = MibTableColumn
tl1fddiMACTMax = _Tl1fddiMACTMax_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 5, 1, 2),
    _Tl1fddiMACTMax_Type()
)
tl1fddiMACTMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiMACTMax.setStatus("mandatory")


class _Tl1fddiMACTvxValue_Type(Integer32):
    """Custom type tl1fddiMACTvxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_Tl1fddiMACTvxValue_Type.__name__ = "Integer32"
_Tl1fddiMACTvxValue_Object = MibTableColumn
tl1fddiMACTvxValue = _Tl1fddiMACTvxValue_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 5, 1, 3),
    _Tl1fddiMACTvxValue_Type()
)
tl1fddiMACTvxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiMACTvxValue.setStatus("mandatory")


class _Tl1fddiMACTMin_Type(Integer32):
    """Custom type tl1fddiMACTMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 335540),
    )


_Tl1fddiMACTMin_Type.__name__ = "Integer32"
_Tl1fddiMACTMin_Object = MibTableColumn
tl1fddiMACTMin = _Tl1fddiMACTMin_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 5, 1, 4),
    _Tl1fddiMACTMin_Type()
)
tl1fddiMACTMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiMACTMin.setStatus("mandatory")
_Tl1fddiMACRcvThrot_Type = Integer32
_Tl1fddiMACRcvThrot_Object = MibTableColumn
tl1fddiMACRcvThrot = _Tl1fddiMACRcvThrot_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 5, 1, 5),
    _Tl1fddiMACRcvThrot_Type()
)
tl1fddiMACRcvThrot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiMACRcvThrot.setStatus("mandatory")
_Tl1fddiPHYOperationalTable_Object = MibTable
tl1fddiPHYOperationalTable = _Tl1fddiPHYOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 6)
)
if mibBuilder.loadTexts:
    tl1fddiPHYOperationalTable.setStatus("mandatory")
_Tl1fddiPHYOperationalEntry_Object = MibTableRow
tl1fddiPHYOperationalEntry = _Tl1fddiPHYOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 6, 1)
)
if mibBuilder.loadTexts:
    tl1fddiPHYOperationalEntry.setStatus("mandatory")


class _Tl1fddiPHYAction_Type(Integer32):
    """Custom type tl1fddiPHYAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_Tl1fddiPHYAction_Type.__name__ = "Integer32"
_Tl1fddiPHYAction_Object = MibTableColumn
tl1fddiPHYAction = _Tl1fddiPHYAction_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 6, 1, 1),
    _Tl1fddiPHYAction_Type()
)
tl1fddiPHYAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1fddiPHYAction.setStatus("mandatory")
_Tl1fddiSMTNeighborTable_Object = MibTable
tl1fddiSMTNeighborTable = _Tl1fddiSMTNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 7)
)
if mibBuilder.loadTexts:
    tl1fddiSMTNeighborTable.setStatus("mandatory")
_Tl1fddiSMTNeighborEntry_Object = MibTableRow
tl1fddiSMTNeighborEntry = _Tl1fddiSMTNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 7, 1)
)
if mibBuilder.loadTexts:
    tl1fddiSMTNeighborEntry.setStatus("mandatory")


class _Tl1fddiSMTStnUpstreamNbr_Type(OctetString):
    """Custom type tl1fddiSMTStnUpstreamNbr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1fddiSMTStnUpstreamNbr_Type.__name__ = "OctetString"
_Tl1fddiSMTStnUpstreamNbr_Object = MibTableColumn
tl1fddiSMTStnUpstreamNbr = _Tl1fddiSMTStnUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 7, 1, 1),
    _Tl1fddiSMTStnUpstreamNbr_Type()
)
tl1fddiSMTStnUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiSMTStnUpstreamNbr.setStatus("mandatory")


class _Tl1fddiSMTStnDownstreamNbr_Type(OctetString):
    """Custom type tl1fddiSMTStnDownstreamNbr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1fddiSMTStnDownstreamNbr_Type.__name__ = "OctetString"
_Tl1fddiSMTStnDownstreamNbr_Object = MibTableColumn
tl1fddiSMTStnDownstreamNbr = _Tl1fddiSMTStnDownstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 15, 7, 1, 2),
    _Tl1fddiSMTStnDownstreamNbr_Type()
)
tl1fddiSMTStnDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1fddiSMTStnDownstreamNbr.setStatus("mandatory")
_Tl1stap_ObjectIdentity = ObjectIdentity
tl1stap = _Tl1stap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16)
)
_Tl1stapBridgeConfig_ObjectIdentity = ObjectIdentity
tl1stapBridgeConfig = _Tl1stapBridgeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 1)
)


class _Tl1stapSpanningTreeEnabled_Type(Integer32):
    """Custom type tl1stapSpanningTreeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Tl1stapSpanningTreeEnabled_Type.__name__ = "Integer32"
_Tl1stapSpanningTreeEnabled_Object = MibScalar
tl1stapSpanningTreeEnabled = _Tl1stapSpanningTreeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 1, 1),
    _Tl1stapSpanningTreeEnabled_Type()
)
tl1stapSpanningTreeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapSpanningTreeEnabled.setStatus("mandatory")


class _Tl1stapCMaxBridgeTransDelay_Type(Integer32):
    """Custom type tl1stapCMaxBridgeTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Tl1stapCMaxBridgeTransDelay_Type.__name__ = "Integer32"
_Tl1stapCMaxBridgeTransDelay_Object = MibScalar
tl1stapCMaxBridgeTransDelay = _Tl1stapCMaxBridgeTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 1, 3),
    _Tl1stapCMaxBridgeTransDelay_Type()
)
tl1stapCMaxBridgeTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapCMaxBridgeTransDelay.setStatus("mandatory")


class _Tl1stapCMaxBpduTransDelay_Type(Integer32):
    """Custom type tl1stapCMaxBpduTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Tl1stapCMaxBpduTransDelay_Type.__name__ = "Integer32"
_Tl1stapCMaxBpduTransDelay_Object = MibScalar
tl1stapCMaxBpduTransDelay = _Tl1stapCMaxBpduTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 1, 4),
    _Tl1stapCMaxBpduTransDelay_Type()
)
tl1stapCMaxBpduTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapCMaxBpduTransDelay.setStatus("mandatory")


class _Tl1stapCBridgeHelloTime_Type(Integer32):
    """Custom type tl1stapCBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Tl1stapCBridgeHelloTime_Type.__name__ = "Integer32"
_Tl1stapCBridgeHelloTime_Object = MibScalar
tl1stapCBridgeHelloTime = _Tl1stapCBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 1, 6),
    _Tl1stapCBridgeHelloTime_Type()
)
tl1stapCBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapCBridgeHelloTime.setStatus("mandatory")


class _Tl1stapCBridgeMaxAge_Type(Integer32):
    """Custom type tl1stapCBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Tl1stapCBridgeMaxAge_Type.__name__ = "Integer32"
_Tl1stapCBridgeMaxAge_Object = MibScalar
tl1stapCBridgeMaxAge = _Tl1stapCBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 1, 7),
    _Tl1stapCBridgeMaxAge_Type()
)
tl1stapCBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapCBridgeMaxAge.setStatus("mandatory")


class _Tl1stapCForwardDelay_Type(Integer32):
    """Custom type tl1stapCForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Tl1stapCForwardDelay_Type.__name__ = "Integer32"
_Tl1stapCForwardDelay_Object = MibScalar
tl1stapCForwardDelay = _Tl1stapCForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 1, 8),
    _Tl1stapCForwardDelay_Type()
)
tl1stapCForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapCForwardDelay.setStatus("mandatory")


class _Tl1stapCBridgePriority_Type(Integer32):
    """Custom type tl1stapCBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tl1stapCBridgePriority_Type.__name__ = "Integer32"
_Tl1stapCBridgePriority_Object = MibScalar
tl1stapCBridgePriority = _Tl1stapCBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 1, 9),
    _Tl1stapCBridgePriority_Type()
)
tl1stapCBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapCBridgePriority.setStatus("mandatory")
_Tl1stapPortConfigTable_Object = MibTable
tl1stapPortConfigTable = _Tl1stapPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 2)
)
if mibBuilder.loadTexts:
    tl1stapPortConfigTable.setStatus("mandatory")
_Tl1stapPortConfigEntry_Object = MibTableRow
tl1stapPortConfigEntry = _Tl1stapPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 2, 1)
)
if mibBuilder.loadTexts:
    tl1stapPortConfigEntry.setStatus("mandatory")


class _Tl1stapCPortState_Type(Integer32):
    """Custom type tl1stapCPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_Tl1stapCPortState_Type.__name__ = "Integer32"
_Tl1stapCPortState_Object = MibTableColumn
tl1stapCPortState = _Tl1stapCPortState_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 2, 1, 1),
    _Tl1stapCPortState_Type()
)
tl1stapCPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapCPortState.setStatus("mandatory")


class _Tl1stapCPortPriority_Type(Integer32):
    """Custom type tl1stapCPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Tl1stapCPortPriority_Type.__name__ = "Integer32"
_Tl1stapCPortPriority_Object = MibTableColumn
tl1stapCPortPriority = _Tl1stapCPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 2, 1, 2),
    _Tl1stapCPortPriority_Type()
)
tl1stapCPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapCPortPriority.setStatus("mandatory")


class _Tl1stapCPathCost_Type(Integer32):
    """Custom type tl1stapCPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Tl1stapCPathCost_Type.__name__ = "Integer32"
_Tl1stapCPathCost_Object = MibTableColumn
tl1stapCPathCost = _Tl1stapCPathCost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 2, 1, 3),
    _Tl1stapCPathCost_Type()
)
tl1stapCPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1stapCPathCost.setStatus("mandatory")
_Tl1stapBridgeState_ObjectIdentity = ObjectIdentity
tl1stapBridgeState = _Tl1stapBridgeState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3)
)


class _Tl1stapBridgeIdentifier_Type(OctetString):
    """Custom type tl1stapBridgeIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Tl1stapBridgeIdentifier_Type.__name__ = "OctetString"
_Tl1stapBridgeIdentifier_Object = MibScalar
tl1stapBridgeIdentifier = _Tl1stapBridgeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 1),
    _Tl1stapBridgeIdentifier_Type()
)
tl1stapBridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapBridgeIdentifier.setStatus("mandatory")
_Tl1stapTimeSinceTopChange_Type = TimeTicks
_Tl1stapTimeSinceTopChange_Object = MibScalar
tl1stapTimeSinceTopChange = _Tl1stapTimeSinceTopChange_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 2),
    _Tl1stapTimeSinceTopChange_Type()
)
tl1stapTimeSinceTopChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapTimeSinceTopChange.setStatus("mandatory")
_Tl1stapTopologyChangeCount_Type = Counter32
_Tl1stapTopologyChangeCount_Object = MibScalar
tl1stapTopologyChangeCount = _Tl1stapTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 3),
    _Tl1stapTopologyChangeCount_Type()
)
tl1stapTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapTopologyChangeCount.setStatus("mandatory")


class _Tl1stapTopologyChange_Type(Integer32):
    """Custom type tl1stapTopologyChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1stapTopologyChange_Type.__name__ = "Integer32"
_Tl1stapTopologyChange_Object = MibScalar
tl1stapTopologyChange = _Tl1stapTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 4),
    _Tl1stapTopologyChange_Type()
)
tl1stapTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapTopologyChange.setStatus("mandatory")


class _Tl1stapDesignatedRoot_Type(OctetString):
    """Custom type tl1stapDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Tl1stapDesignatedRoot_Type.__name__ = "OctetString"
_Tl1stapDesignatedRoot_Object = MibScalar
tl1stapDesignatedRoot = _Tl1stapDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 5),
    _Tl1stapDesignatedRoot_Type()
)
tl1stapDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapDesignatedRoot.setStatus("mandatory")
_Tl1stapRootPathCost_Type = Integer32
_Tl1stapRootPathCost_Object = MibScalar
tl1stapRootPathCost = _Tl1stapRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 6),
    _Tl1stapRootPathCost_Type()
)
tl1stapRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapRootPathCost.setStatus("mandatory")
_Tl1stapRootPort_Type = Integer32
_Tl1stapRootPort_Object = MibScalar
tl1stapRootPort = _Tl1stapRootPort_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 7),
    _Tl1stapRootPort_Type()
)
tl1stapRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapRootPort.setStatus("mandatory")


class _Tl1stapMaxAge_Type(Integer32):
    """Custom type tl1stapMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Tl1stapMaxAge_Type.__name__ = "Integer32"
_Tl1stapMaxAge_Object = MibScalar
tl1stapMaxAge = _Tl1stapMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 8),
    _Tl1stapMaxAge_Type()
)
tl1stapMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapMaxAge.setStatus("mandatory")


class _Tl1stapHelloTime_Type(Integer32):
    """Custom type tl1stapHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Tl1stapHelloTime_Type.__name__ = "Integer32"
_Tl1stapHelloTime_Object = MibScalar
tl1stapHelloTime = _Tl1stapHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 9),
    _Tl1stapHelloTime_Type()
)
tl1stapHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapHelloTime.setStatus("mandatory")


class _Tl1stapForwardDelay_Type(Integer32):
    """Custom type tl1stapForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Tl1stapForwardDelay_Type.__name__ = "Integer32"
_Tl1stapForwardDelay_Object = MibScalar
tl1stapForwardDelay = _Tl1stapForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 10),
    _Tl1stapForwardDelay_Type()
)
tl1stapForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapForwardDelay.setStatus("mandatory")


class _Tl1stapBridgeMaxAge_Type(Integer32):
    """Custom type tl1stapBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Tl1stapBridgeMaxAge_Type.__name__ = "Integer32"
_Tl1stapBridgeMaxAge_Object = MibScalar
tl1stapBridgeMaxAge = _Tl1stapBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 11),
    _Tl1stapBridgeMaxAge_Type()
)
tl1stapBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapBridgeMaxAge.setStatus("mandatory")


class _Tl1stapBridgeHelloTime_Type(Integer32):
    """Custom type tl1stapBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Tl1stapBridgeHelloTime_Type.__name__ = "Integer32"
_Tl1stapBridgeHelloTime_Object = MibScalar
tl1stapBridgeHelloTime = _Tl1stapBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 12),
    _Tl1stapBridgeHelloTime_Type()
)
tl1stapBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapBridgeHelloTime.setStatus("mandatory")


class _Tl1stapBridgeForwardDelay_Type(Integer32):
    """Custom type tl1stapBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Tl1stapBridgeForwardDelay_Type.__name__ = "Integer32"
_Tl1stapBridgeForwardDelay_Object = MibScalar
tl1stapBridgeForwardDelay = _Tl1stapBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 13),
    _Tl1stapBridgeForwardDelay_Type()
)
tl1stapBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapBridgeForwardDelay.setStatus("mandatory")
_Tl1stapHoldTime_Type = Integer32
_Tl1stapHoldTime_Object = MibScalar
tl1stapHoldTime = _Tl1stapHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 3, 14),
    _Tl1stapHoldTime_Type()
)
tl1stapHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapHoldTime.setStatus("mandatory")
_Tl1stapPortStateTable_Object = MibTable
tl1stapPortStateTable = _Tl1stapPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4)
)
if mibBuilder.loadTexts:
    tl1stapPortStateTable.setStatus("mandatory")
_Tl1stapPortStateEntry_Object = MibTableRow
tl1stapPortStateEntry = _Tl1stapPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1)
)
if mibBuilder.loadTexts:
    tl1stapPortStateEntry.setStatus("mandatory")
_Tl1stapPortIdentifier_Type = Integer32
_Tl1stapPortIdentifier_Object = MibTableColumn
tl1stapPortIdentifier = _Tl1stapPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1, 1),
    _Tl1stapPortIdentifier_Type()
)
tl1stapPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapPortIdentifier.setStatus("mandatory")


class _Tl1stapPortState_Type(Integer32):
    """Custom type tl1stapPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 4),
          ("disabled", 0),
          ("forwarding", 3),
          ("learning", 2),
          ("listening", 1))
    )


_Tl1stapPortState_Type.__name__ = "Integer32"
_Tl1stapPortState_Object = MibTableColumn
tl1stapPortState = _Tl1stapPortState_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1, 2),
    _Tl1stapPortState_Type()
)
tl1stapPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapPortState.setStatus("mandatory")


class _Tl1stapPathCost_Type(Integer32):
    """Custom type tl1stapPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Tl1stapPathCost_Type.__name__ = "Integer32"
_Tl1stapPathCost_Object = MibTableColumn
tl1stapPathCost = _Tl1stapPathCost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1, 3),
    _Tl1stapPathCost_Type()
)
tl1stapPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapPathCost.setStatus("mandatory")


class _Tl1stapPDesignatedRoot_Type(OctetString):
    """Custom type tl1stapPDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Tl1stapPDesignatedRoot_Type.__name__ = "OctetString"
_Tl1stapPDesignatedRoot_Object = MibTableColumn
tl1stapPDesignatedRoot = _Tl1stapPDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1, 4),
    _Tl1stapPDesignatedRoot_Type()
)
tl1stapPDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapPDesignatedRoot.setStatus("mandatory")
_Tl1stapPDesignatedCost_Type = Integer32
_Tl1stapPDesignatedCost_Object = MibTableColumn
tl1stapPDesignatedCost = _Tl1stapPDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1, 5),
    _Tl1stapPDesignatedCost_Type()
)
tl1stapPDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapPDesignatedCost.setStatus("mandatory")


class _Tl1stapPDesignatedBridge_Type(OctetString):
    """Custom type tl1stapPDesignatedBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Tl1stapPDesignatedBridge_Type.__name__ = "OctetString"
_Tl1stapPDesignatedBridge_Object = MibTableColumn
tl1stapPDesignatedBridge = _Tl1stapPDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1, 6),
    _Tl1stapPDesignatedBridge_Type()
)
tl1stapPDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapPDesignatedBridge.setStatus("mandatory")
_Tl1stapPDesignatedPort_Type = Integer32
_Tl1stapPDesignatedPort_Object = MibTableColumn
tl1stapPDesignatedPort = _Tl1stapPDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1, 7),
    _Tl1stapPDesignatedPort_Type()
)
tl1stapPDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapPDesignatedPort.setStatus("mandatory")


class _Tl1stapPTopologyChangeAck_Type(Integer32):
    """Custom type tl1stapPTopologyChangeAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1stapPTopologyChangeAck_Type.__name__ = "Integer32"
_Tl1stapPTopologyChangeAck_Object = MibTableColumn
tl1stapPTopologyChangeAck = _Tl1stapPTopologyChangeAck_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1, 8),
    _Tl1stapPTopologyChangeAck_Type()
)
tl1stapPTopologyChangeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapPTopologyChangeAck.setStatus("mandatory")


class _Tl1stapPConfigPending_Type(Integer32):
    """Custom type tl1stapPConfigPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1stapPConfigPending_Type.__name__ = "Integer32"
_Tl1stapPConfigPending_Object = MibTableColumn
tl1stapPConfigPending = _Tl1stapPConfigPending_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 16, 4, 1, 9),
    _Tl1stapPConfigPending_Type()
)
tl1stapPConfigPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1stapPConfigPending.setStatus("mandatory")
_Tl1idp_ObjectIdentity = ObjectIdentity
tl1idp = _Tl1idp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17)
)
_Tl1idpInterfaceTable_Object = MibTable
tl1idpInterfaceTable = _Tl1idpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 1)
)
if mibBuilder.loadTexts:
    tl1idpInterfaceTable.setStatus("mandatory")
_Tl1idpInterfaceEntry_Object = MibTableRow
tl1idpInterfaceEntry = _Tl1idpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    tl1idpInterfaceEntry.setStatus("mandatory")


class _Tl1idpRouteSupplier_Type(Integer32):
    """Custom type tl1idpRouteSupplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1idpRouteSupplier_Type.__name__ = "Integer32"
_Tl1idpRouteSupplier_Object = MibTableColumn
tl1idpRouteSupplier = _Tl1idpRouteSupplier_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 1, 1, 1),
    _Tl1idpRouteSupplier_Type()
)
tl1idpRouteSupplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpRouteSupplier.setStatus("mandatory")


class _Tl1idpGenChecksum_Type(Integer32):
    """Custom type tl1idpGenChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1idpGenChecksum_Type.__name__ = "Integer32"
_Tl1idpGenChecksum_Object = MibTableColumn
tl1idpGenChecksum = _Tl1idpGenChecksum_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 1, 1, 2),
    _Tl1idpGenChecksum_Type()
)
tl1idpGenChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpGenChecksum.setStatus("mandatory")
_Tl1idpBroadcastInterval_Type = Integer32
_Tl1idpBroadcastInterval_Object = MibScalar
tl1idpBroadcastInterval = _Tl1idpBroadcastInterval_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 2),
    _Tl1idpBroadcastInterval_Type()
)
tl1idpBroadcastInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpBroadcastInterval.setStatus("mandatory")
_Tl1idpRouteTimeout_Type = Integer32
_Tl1idpRouteTimeout_Object = MibScalar
tl1idpRouteTimeout = _Tl1idpRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 3),
    _Tl1idpRouteTimeout_Type()
)
tl1idpRouteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpRouteTimeout.setStatus("mandatory")
_Tl1idpWellKnownGatewayNet_Type = Integer32
_Tl1idpWellKnownGatewayNet_Object = MibScalar
tl1idpWellKnownGatewayNet = _Tl1idpWellKnownGatewayNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 4),
    _Tl1idpWellKnownGatewayNet_Type()
)
tl1idpWellKnownGatewayNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpWellKnownGatewayNet.setStatus("mandatory")


class _Tl1idpWellKnownGatewayHost_Type(OctetString):
    """Custom type tl1idpWellKnownGatewayHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1idpWellKnownGatewayHost_Type.__name__ = "OctetString"
_Tl1idpWellKnownGatewayHost_Object = MibScalar
tl1idpWellKnownGatewayHost = _Tl1idpWellKnownGatewayHost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 5),
    _Tl1idpWellKnownGatewayHost_Type()
)
tl1idpWellKnownGatewayHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpWellKnownGatewayHost.setStatus("mandatory")
_Tl1idpNbrStaticRoutes_Type = Integer32
_Tl1idpNbrStaticRoutes_Object = MibScalar
tl1idpNbrStaticRoutes = _Tl1idpNbrStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 6),
    _Tl1idpNbrStaticRoutes_Type()
)
tl1idpNbrStaticRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpNbrStaticRoutes.setStatus("mandatory")
_Tl1idpStaticRouteTable_Object = MibTable
tl1idpStaticRouteTable = _Tl1idpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 7)
)
if mibBuilder.loadTexts:
    tl1idpStaticRouteTable.setStatus("mandatory")
_Tl1idpStaticRouteEntry_Object = MibTableRow
tl1idpStaticRouteEntry = _Tl1idpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 7, 1)
)
if mibBuilder.loadTexts:
    tl1idpStaticRouteEntry.setStatus("mandatory")
_Tl1idpStaticRouteNetwork_Type = Integer32
_Tl1idpStaticRouteNetwork_Object = MibTableColumn
tl1idpStaticRouteNetwork = _Tl1idpStaticRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 7, 1, 1),
    _Tl1idpStaticRouteNetwork_Type()
)
tl1idpStaticRouteNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpStaticRouteNetwork.setStatus("mandatory")
_Tl1idpStaticRouteGatewayNet_Type = Integer32
_Tl1idpStaticRouteGatewayNet_Object = MibTableColumn
tl1idpStaticRouteGatewayNet = _Tl1idpStaticRouteGatewayNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 7, 1, 2),
    _Tl1idpStaticRouteGatewayNet_Type()
)
tl1idpStaticRouteGatewayNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpStaticRouteGatewayNet.setStatus("mandatory")


class _Tl1idpStaticRouteGatewayHost_Type(OctetString):
    """Custom type tl1idpStaticRouteGatewayHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1idpStaticRouteGatewayHost_Type.__name__ = "OctetString"
_Tl1idpStaticRouteGatewayHost_Object = MibTableColumn
tl1idpStaticRouteGatewayHost = _Tl1idpStaticRouteGatewayHost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 7, 1, 3),
    _Tl1idpStaticRouteGatewayHost_Type()
)
tl1idpStaticRouteGatewayHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpStaticRouteGatewayHost.setStatus("mandatory")


class _Tl1idpStaticRouteCost_Type(Integer32):
    """Custom type tl1idpStaticRouteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Tl1idpStaticRouteCost_Type.__name__ = "Integer32"
_Tl1idpStaticRouteCost_Object = MibTableColumn
tl1idpStaticRouteCost = _Tl1idpStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 7, 1, 4),
    _Tl1idpStaticRouteCost_Type()
)
tl1idpStaticRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpStaticRouteCost.setStatus("mandatory")


class _Tl1idpStaticRouteOverride_Type(Integer32):
    """Custom type tl1idpStaticRouteOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1idpStaticRouteOverride_Type.__name__ = "Integer32"
_Tl1idpStaticRouteOverride_Object = MibTableColumn
tl1idpStaticRouteOverride = _Tl1idpStaticRouteOverride_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 7, 1, 5),
    _Tl1idpStaticRouteOverride_Type()
)
tl1idpStaticRouteOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpStaticRouteOverride.setStatus("mandatory")
_Tl1idpNbrFilters_Type = Integer32
_Tl1idpNbrFilters_Object = MibScalar
tl1idpNbrFilters = _Tl1idpNbrFilters_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 8),
    _Tl1idpNbrFilters_Type()
)
tl1idpNbrFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpNbrFilters.setStatus("mandatory")
_Tl1idpFilterTable_Object = MibTable
tl1idpFilterTable = _Tl1idpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 9)
)
if mibBuilder.loadTexts:
    tl1idpFilterTable.setStatus("mandatory")
_Tl1idpFilterEntry_Object = MibTableRow
tl1idpFilterEntry = _Tl1idpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 9, 1)
)
if mibBuilder.loadTexts:
    tl1idpFilterEntry.setStatus("mandatory")
_Tl1idpFilterSourceMask_Type = Integer32
_Tl1idpFilterSourceMask_Object = MibTableColumn
tl1idpFilterSourceMask = _Tl1idpFilterSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 9, 1, 1),
    _Tl1idpFilterSourceMask_Type()
)
tl1idpFilterSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterSourceMask.setStatus("mandatory")
_Tl1idpFilterSourceNet_Type = Integer32
_Tl1idpFilterSourceNet_Object = MibTableColumn
tl1idpFilterSourceNet = _Tl1idpFilterSourceNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 9, 1, 2),
    _Tl1idpFilterSourceNet_Type()
)
tl1idpFilterSourceNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterSourceNet.setStatus("mandatory")


class _Tl1idpFilterSourceHost_Type(OctetString):
    """Custom type tl1idpFilterSourceHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1idpFilterSourceHost_Type.__name__ = "OctetString"
_Tl1idpFilterSourceHost_Object = MibTableColumn
tl1idpFilterSourceHost = _Tl1idpFilterSourceHost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 9, 1, 3),
    _Tl1idpFilterSourceHost_Type()
)
tl1idpFilterSourceHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterSourceHost.setStatus("mandatory")
_Tl1idpFilterDestinationMask_Type = Integer32
_Tl1idpFilterDestinationMask_Object = MibTableColumn
tl1idpFilterDestinationMask = _Tl1idpFilterDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 9, 1, 4),
    _Tl1idpFilterDestinationMask_Type()
)
tl1idpFilterDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterDestinationMask.setStatus("mandatory")
_Tl1idpFilterDestinationNet_Type = Integer32
_Tl1idpFilterDestinationNet_Object = MibTableColumn
tl1idpFilterDestinationNet = _Tl1idpFilterDestinationNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 9, 1, 5),
    _Tl1idpFilterDestinationNet_Type()
)
tl1idpFilterDestinationNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterDestinationNet.setStatus("mandatory")


class _Tl1idpFilterDestinationHost_Type(OctetString):
    """Custom type tl1idpFilterDestinationHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1idpFilterDestinationHost_Type.__name__ = "OctetString"
_Tl1idpFilterDestinationHost_Object = MibTableColumn
tl1idpFilterDestinationHost = _Tl1idpFilterDestinationHost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 9, 1, 6),
    _Tl1idpFilterDestinationHost_Type()
)
tl1idpFilterDestinationHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterDestinationHost.setStatus("mandatory")
_Tl1idpFilterNbrExceptions_Type = Integer32
_Tl1idpFilterNbrExceptions_Object = MibTableColumn
tl1idpFilterNbrExceptions = _Tl1idpFilterNbrExceptions_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 9, 1, 7),
    _Tl1idpFilterNbrExceptions_Type()
)
tl1idpFilterNbrExceptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterNbrExceptions.setStatus("mandatory")
_Tl1idpFilterExceptionTable_Object = MibTable
tl1idpFilterExceptionTable = _Tl1idpFilterExceptionTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 10)
)
if mibBuilder.loadTexts:
    tl1idpFilterExceptionTable.setStatus("mandatory")
_Tl1idpFilterExceptionEntry_Object = MibTableRow
tl1idpFilterExceptionEntry = _Tl1idpFilterExceptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 10, 1)
)
if mibBuilder.loadTexts:
    tl1idpFilterExceptionEntry.setStatus("mandatory")
_Tl1idpFilterExceptionSrcNet_Type = Integer32
_Tl1idpFilterExceptionSrcNet_Object = MibTableColumn
tl1idpFilterExceptionSrcNet = _Tl1idpFilterExceptionSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 10, 1, 1),
    _Tl1idpFilterExceptionSrcNet_Type()
)
tl1idpFilterExceptionSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterExceptionSrcNet.setStatus("mandatory")


class _Tl1idpFilterExceptionSrcHost_Type(OctetString):
    """Custom type tl1idpFilterExceptionSrcHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1idpFilterExceptionSrcHost_Type.__name__ = "OctetString"
_Tl1idpFilterExceptionSrcHost_Object = MibTableColumn
tl1idpFilterExceptionSrcHost = _Tl1idpFilterExceptionSrcHost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 10, 1, 2),
    _Tl1idpFilterExceptionSrcHost_Type()
)
tl1idpFilterExceptionSrcHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterExceptionSrcHost.setStatus("mandatory")
_Tl1idpFilterExceptionDstNet_Type = Integer32
_Tl1idpFilterExceptionDstNet_Object = MibTableColumn
tl1idpFilterExceptionDstNet = _Tl1idpFilterExceptionDstNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 10, 1, 3),
    _Tl1idpFilterExceptionDstNet_Type()
)
tl1idpFilterExceptionDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterExceptionDstNet.setStatus("mandatory")


class _Tl1idpFilterExceptionDstHost_Type(OctetString):
    """Custom type tl1idpFilterExceptionDstHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1idpFilterExceptionDstHost_Type.__name__ = "OctetString"
_Tl1idpFilterExceptionDstHost_Object = MibTableColumn
tl1idpFilterExceptionDstHost = _Tl1idpFilterExceptionDstHost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 10, 1, 4),
    _Tl1idpFilterExceptionDstHost_Type()
)
tl1idpFilterExceptionDstHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpFilterExceptionDstHost.setStatus("mandatory")


class _Tl1idpForwarding_Type(Integer32):
    """Custom type tl1idpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gateway-thus-forward", 1),
          ("host-thus-dont-forward", 2))
    )


_Tl1idpForwarding_Type.__name__ = "Integer32"
_Tl1idpForwarding_Object = MibScalar
tl1idpForwarding = _Tl1idpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 11),
    _Tl1idpForwarding_Type()
)
tl1idpForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpForwarding.setStatus("mandatory")
_Tl1idpInReceives_Type = Counter32
_Tl1idpInReceives_Object = MibScalar
tl1idpInReceives = _Tl1idpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 12),
    _Tl1idpInReceives_Type()
)
tl1idpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpInReceives.setStatus("mandatory")
_Tl1idpInHdrErrors_Type = Counter32
_Tl1idpInHdrErrors_Object = MibScalar
tl1idpInHdrErrors = _Tl1idpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 13),
    _Tl1idpInHdrErrors_Type()
)
tl1idpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpInHdrErrors.setStatus("mandatory")
_Tl1idpForwDatagrams_Type = Counter32
_Tl1idpForwDatagrams_Object = MibScalar
tl1idpForwDatagrams = _Tl1idpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 14),
    _Tl1idpForwDatagrams_Type()
)
tl1idpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpForwDatagrams.setStatus("mandatory")
_Tl1idpOutNoRoutes_Type = Counter32
_Tl1idpOutNoRoutes_Object = MibScalar
tl1idpOutNoRoutes = _Tl1idpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 15),
    _Tl1idpOutNoRoutes_Type()
)
tl1idpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpOutNoRoutes.setStatus("mandatory")
_Tl1idpNumStatic_Type = Counter32
_Tl1idpNumStatic_Object = MibScalar
tl1idpNumStatic = _Tl1idpNumStatic_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 16),
    _Tl1idpNumStatic_Type()
)
tl1idpNumStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpNumStatic.setStatus("mandatory")
_Tl1idpBadSize_Type = Counter32
_Tl1idpBadSize_Object = MibScalar
tl1idpBadSize = _Tl1idpBadSize_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 17),
    _Tl1idpBadSize_Type()
)
tl1idpBadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpBadSize.setStatus("mandatory")
_Tl1idpInMsgs_Type = Counter32
_Tl1idpInMsgs_Object = MibScalar
tl1idpInMsgs = _Tl1idpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 18),
    _Tl1idpInMsgs_Type()
)
tl1idpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpInMsgs.setStatus("mandatory")
_Tl1idpErrInEchos_Type = Counter32
_Tl1idpErrInEchos_Object = MibScalar
tl1idpErrInEchos = _Tl1idpErrInEchos_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 19),
    _Tl1idpErrInEchos_Type()
)
tl1idpErrInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrInEchos.setStatus("mandatory")
_Tl1idpInEchos_Type = Counter32
_Tl1idpInEchos_Object = MibScalar
tl1idpInEchos = _Tl1idpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 20),
    _Tl1idpInEchos_Type()
)
tl1idpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpInEchos.setStatus("mandatory")
_Tl1idpInEchoReply_Type = Counter32
_Tl1idpInEchoReply_Object = MibScalar
tl1idpInEchoReply = _Tl1idpInEchoReply_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 21),
    _Tl1idpInEchoReply_Type()
)
tl1idpInEchoReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpInEchoReply.setStatus("mandatory")
_Tl1idpOutEchoReps_Type = Counter32
_Tl1idpOutEchoReps_Object = MibScalar
tl1idpOutEchoReps = _Tl1idpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 22),
    _Tl1idpOutEchoReps_Type()
)
tl1idpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpOutEchoReps.setStatus("mandatory")
_Tl1idpErrInUnspecified_Type = Counter32
_Tl1idpErrInUnspecified_Object = MibScalar
tl1idpErrInUnspecified = _Tl1idpErrInUnspecified_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 23),
    _Tl1idpErrInUnspecified_Type()
)
tl1idpErrInUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrInUnspecified.setStatus("mandatory")
_Tl1idpErrInChecksum_Type = Counter32
_Tl1idpErrInChecksum_Object = MibScalar
tl1idpErrInChecksum = _Tl1idpErrInChecksum_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 24),
    _Tl1idpErrInChecksum_Type()
)
tl1idpErrInChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrInChecksum.setStatus("mandatory")
_Tl1idpErrInSocket_Type = Counter32
_Tl1idpErrInSocket_Object = MibScalar
tl1idpErrInSocket = _Tl1idpErrInSocket_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 25),
    _Tl1idpErrInSocket_Type()
)
tl1idpErrInSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrInSocket.setStatus("mandatory")
_Tl1idpErrInResources_Type = Counter32
_Tl1idpErrInResources_Object = MibScalar
tl1idpErrInResources = _Tl1idpErrInResources_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 26),
    _Tl1idpErrInResources_Type()
)
tl1idpErrInResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrInResources.setStatus("mandatory")
_Tl1idpErrInNohost_Type = Counter32
_Tl1idpErrInNohost_Object = MibScalar
tl1idpErrInNohost = _Tl1idpErrInNohost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 27),
    _Tl1idpErrInNohost_Type()
)
tl1idpErrInNohost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrInNohost.setStatus("mandatory")
_Tl1idpErrInMaxhops_Type = Counter32
_Tl1idpErrInMaxhops_Object = MibScalar
tl1idpErrInMaxhops = _Tl1idpErrInMaxhops_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 28),
    _Tl1idpErrInMaxhops_Type()
)
tl1idpErrInMaxhops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrInMaxhops.setStatus("mandatory")
_Tl1idpErrInSizetoobig_Type = Counter32
_Tl1idpErrInSizetoobig_Object = MibScalar
tl1idpErrInSizetoobig = _Tl1idpErrInSizetoobig_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 29),
    _Tl1idpErrInSizetoobig_Type()
)
tl1idpErrInSizetoobig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrInSizetoobig.setStatus("mandatory")
_Tl1idpErrInErrors_Type = Counter32
_Tl1idpErrInErrors_Object = MibScalar
tl1idpErrInErrors = _Tl1idpErrInErrors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 30),
    _Tl1idpErrInErrors_Type()
)
tl1idpErrInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrInErrors.setStatus("mandatory")
_Tl1idpInErrors_Type = Counter32
_Tl1idpInErrors_Object = MibScalar
tl1idpInErrors = _Tl1idpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 31),
    _Tl1idpInErrors_Type()
)
tl1idpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpInErrors.setStatus("mandatory")
_Tl1idpErrOutMsgs_Type = Counter32
_Tl1idpErrOutMsgs_Object = MibScalar
tl1idpErrOutMsgs = _Tl1idpErrOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 32),
    _Tl1idpErrOutMsgs_Type()
)
tl1idpErrOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrOutMsgs.setStatus("mandatory")
_Tl1idpErrOutErrors_Type = Counter32
_Tl1idpErrOutErrors_Object = MibScalar
tl1idpErrOutErrors = _Tl1idpErrOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 33),
    _Tl1idpErrOutErrors_Type()
)
tl1idpErrOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrOutErrors.setStatus("mandatory")
_Tl1idpErrOutUnspecified_Type = Counter32
_Tl1idpErrOutUnspecified_Object = MibScalar
tl1idpErrOutUnspecified = _Tl1idpErrOutUnspecified_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 34),
    _Tl1idpErrOutUnspecified_Type()
)
tl1idpErrOutUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrOutUnspecified.setStatus("mandatory")
_Tl1idpErrOutChecksum_Type = Counter32
_Tl1idpErrOutChecksum_Object = MibScalar
tl1idpErrOutChecksum = _Tl1idpErrOutChecksum_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 35),
    _Tl1idpErrOutChecksum_Type()
)
tl1idpErrOutChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrOutChecksum.setStatus("mandatory")
_Tl1idpErrOutSocket_Type = Counter32
_Tl1idpErrOutSocket_Object = MibScalar
tl1idpErrOutSocket = _Tl1idpErrOutSocket_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 36),
    _Tl1idpErrOutSocket_Type()
)
tl1idpErrOutSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrOutSocket.setStatus("mandatory")
_Tl1idpErrOutResources_Type = Counter32
_Tl1idpErrOutResources_Object = MibScalar
tl1idpErrOutResources = _Tl1idpErrOutResources_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 37),
    _Tl1idpErrOutResources_Type()
)
tl1idpErrOutResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrOutResources.setStatus("mandatory")
_Tl1idpErrOutNohost_Type = Counter32
_Tl1idpErrOutNohost_Object = MibScalar
tl1idpErrOutNohost = _Tl1idpErrOutNohost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 38),
    _Tl1idpErrOutNohost_Type()
)
tl1idpErrOutNohost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrOutNohost.setStatus("mandatory")
_Tl1idpErrOutMaxhops_Type = Counter32
_Tl1idpErrOutMaxhops_Object = MibScalar
tl1idpErrOutMaxhops = _Tl1idpErrOutMaxhops_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 39),
    _Tl1idpErrOutMaxhops_Type()
)
tl1idpErrOutMaxhops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrOutMaxhops.setStatus("mandatory")
_Tl1idpErrOutSizetoobig_Type = Counter32
_Tl1idpErrOutSizetoobig_Object = MibScalar
tl1idpErrOutSizetoobig = _Tl1idpErrOutSizetoobig_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 40),
    _Tl1idpErrOutSizetoobig_Type()
)
tl1idpErrOutSizetoobig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpErrOutSizetoobig.setStatus("mandatory")
_Tl1idpInOwnAddr_Type = Counter32
_Tl1idpInOwnAddr_Object = MibScalar
tl1idpInOwnAddr = _Tl1idpInOwnAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 41),
    _Tl1idpInOwnAddr_Type()
)
tl1idpInOwnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpInOwnAddr.setStatus("mandatory")
_Tl1idpInNoRoutes_Type = Counter32
_Tl1idpInNoRoutes_Object = MibScalar
tl1idpInNoRoutes = _Tl1idpInNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 42),
    _Tl1idpInNoRoutes_Type()
)
tl1idpInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpInNoRoutes.setStatus("mandatory")
_Tl1idpFilter_Type = Counter32
_Tl1idpFilter_Object = MibScalar
tl1idpFilter = _Tl1idpFilter_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 43),
    _Tl1idpFilter_Type()
)
tl1idpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpFilter.setStatus("mandatory")
_Tl1idpHashHit_Type = Counter32
_Tl1idpHashHit_Object = MibScalar
tl1idpHashHit = _Tl1idpHashHit_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 44),
    _Tl1idpHashHit_Type()
)
tl1idpHashHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpHashHit.setStatus("mandatory")
_Tl1idpHashMiss_Type = Counter32
_Tl1idpHashMiss_Object = MibScalar
tl1idpHashMiss = _Tl1idpHashMiss_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 45),
    _Tl1idpHashMiss_Type()
)
tl1idpHashMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpHashMiss.setStatus("mandatory")
_Tl1idpBadMetric_Type = Counter32
_Tl1idpBadMetric_Object = MibScalar
tl1idpBadMetric = _Tl1idpBadMetric_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 46),
    _Tl1idpBadMetric_Type()
)
tl1idpBadMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpBadMetric.setStatus("mandatory")
_Tl1idpBadAlloc_Type = Counter32
_Tl1idpBadAlloc_Object = MibScalar
tl1idpBadAlloc = _Tl1idpBadAlloc_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 47),
    _Tl1idpBadAlloc_Type()
)
tl1idpBadAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpBadAlloc.setStatus("mandatory")
_Tl1idpBadNbr_Type = Counter32
_Tl1idpBadNbr_Object = MibScalar
tl1idpBadNbr = _Tl1idpBadNbr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 48),
    _Tl1idpBadNbr_Type()
)
tl1idpBadNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpBadNbr.setStatus("mandatory")
_Tl1idpBadCommand_Type = Counter32
_Tl1idpBadCommand_Object = MibScalar
tl1idpBadCommand = _Tl1idpBadCommand_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 49),
    _Tl1idpBadCommand_Type()
)
tl1idpBadCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpBadCommand.setStatus("mandatory")
_Tl1idpBadAddr_Type = Counter32
_Tl1idpBadAddr_Object = MibScalar
tl1idpBadAddr = _Tl1idpBadAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 50),
    _Tl1idpBadAddr_Type()
)
tl1idpBadAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1idpBadAddr.setStatus("mandatory")
_Tl1idpNetworkIntfTable_Object = MibTable
tl1idpNetworkIntfTable = _Tl1idpNetworkIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 51)
)
if mibBuilder.loadTexts:
    tl1idpNetworkIntfTable.setStatus("mandatory")
_Tl1idpNetworkIntfEntry_Object = MibTableRow
tl1idpNetworkIntfEntry = _Tl1idpNetworkIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 51, 1)
)
if mibBuilder.loadTexts:
    tl1idpNetworkIntfEntry.setStatus("mandatory")
_Tl1idpNetworkMaximumPacket_Type = Integer32
_Tl1idpNetworkMaximumPacket_Object = MibTableColumn
tl1idpNetworkMaximumPacket = _Tl1idpNetworkMaximumPacket_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 51, 1, 1),
    _Tl1idpNetworkMaximumPacket_Type()
)
tl1idpNetworkMaximumPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpNetworkMaximumPacket.setStatus("mandatory")
_Tl1idpNetworkAddress_Type = Integer32
_Tl1idpNetworkAddress_Object = MibTableColumn
tl1idpNetworkAddress = _Tl1idpNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 17, 51, 1, 2),
    _Tl1idpNetworkAddress_Type()
)
tl1idpNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1idpNetworkAddress.setStatus("mandatory")
_Tl1ppp_ObjectIdentity = ObjectIdentity
tl1ppp = _Tl1ppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18)
)
_Tl1pppInfoTable_Object = MibTable
tl1pppInfoTable = _Tl1pppInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 1)
)
if mibBuilder.loadTexts:
    tl1pppInfoTable.setStatus("mandatory")
_Tl1pppInfoEntry_Object = MibTableRow
tl1pppInfoEntry = _Tl1pppInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 1, 1)
)
if mibBuilder.loadTexts:
    tl1pppInfoEntry.setStatus("mandatory")


class _Tl1pppLcpAO_Type(Integer32):
    """Custom type tl1pppLcpAO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1pppLcpAO_Type.__name__ = "Integer32"
_Tl1pppLcpAO_Object = MibTableColumn
tl1pppLcpAO = _Tl1pppLcpAO_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 1, 1, 1),
    _Tl1pppLcpAO_Type()
)
tl1pppLcpAO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1pppLcpAO.setStatus("mandatory")


class _Tl1pppIpcpAO_Type(Integer32):
    """Custom type tl1pppIpcpAO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1pppIpcpAO_Type.__name__ = "Integer32"
_Tl1pppIpcpAO_Object = MibTableColumn
tl1pppIpcpAO = _Tl1pppIpcpAO_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 1, 1, 2),
    _Tl1pppIpcpAO_Type()
)
tl1pppIpcpAO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1pppIpcpAO.setStatus("mandatory")


class _Tl1pppIdpcpAO_Type(Integer32):
    """Custom type tl1pppIdpcpAO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1pppIdpcpAO_Type.__name__ = "Integer32"
_Tl1pppIdpcpAO_Object = MibTableColumn
tl1pppIdpcpAO = _Tl1pppIdpcpAO_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 1, 1, 3),
    _Tl1pppIdpcpAO_Type()
)
tl1pppIdpcpAO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1pppIdpcpAO.setStatus("mandatory")


class _Tl1pppIpxcpAO_Type(Integer32):
    """Custom type tl1pppIpxcpAO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1pppIpxcpAO_Type.__name__ = "Integer32"
_Tl1pppIpxcpAO_Object = MibTableColumn
tl1pppIpxcpAO = _Tl1pppIpxcpAO_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 1, 1, 4),
    _Tl1pppIpxcpAO_Type()
)
tl1pppIpxcpAO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1pppIpxcpAO.setStatus("mandatory")
_Tl1pppLqdTimeout_Type = Integer32
_Tl1pppLqdTimeout_Object = MibTableColumn
tl1pppLqdTimeout = _Tl1pppLqdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 1, 1, 5),
    _Tl1pppLqdTimeout_Type()
)
tl1pppLqdTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1pppLqdTimeout.setStatus("mandatory")
_Tl1pppPhaseTable_Object = MibTable
tl1pppPhaseTable = _Tl1pppPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 2)
)
if mibBuilder.loadTexts:
    tl1pppPhaseTable.setStatus("mandatory")
_Tl1pppPhaseEntry_Object = MibTableRow
tl1pppPhaseEntry = _Tl1pppPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    tl1pppPhaseEntry.setStatus("mandatory")
_Tl1pppCrCount_Type = Integer32
_Tl1pppCrCount_Object = MibTableColumn
tl1pppCrCount = _Tl1pppCrCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 2, 1, 1),
    _Tl1pppCrCount_Type()
)
tl1pppCrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1pppCrCount.setStatus("mandatory")
_Tl1pppTrCount_Type = Integer32
_Tl1pppTrCount_Object = MibTableColumn
tl1pppTrCount = _Tl1pppTrCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 2, 1, 2),
    _Tl1pppTrCount_Type()
)
tl1pppTrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1pppTrCount.setStatus("mandatory")
_Tl1pppCtTimeout_Type = Integer32
_Tl1pppCtTimeout_Object = MibTableColumn
tl1pppCtTimeout = _Tl1pppCtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 2, 1, 3),
    _Tl1pppCtTimeout_Type()
)
tl1pppCtTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1pppCtTimeout.setStatus("mandatory")
_Tl1pppRsTimeout_Type = Integer32
_Tl1pppRsTimeout_Object = MibTableColumn
tl1pppRsTimeout = _Tl1pppRsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 2, 1, 4),
    _Tl1pppRsTimeout_Type()
)
tl1pppRsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1pppRsTimeout.setStatus("mandatory")
_Tl1pppStatTable_Object = MibTable
tl1pppStatTable = _Tl1pppStatTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3)
)
if mibBuilder.loadTexts:
    tl1pppStatTable.setStatus("mandatory")
_Tl1pppStatEntry_Object = MibTableRow
tl1pppStatEntry = _Tl1pppStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1)
)
if mibBuilder.loadTexts:
    tl1pppStatEntry.setStatus("mandatory")
_Tl1pppBadProtocol_Type = Counter32
_Tl1pppBadProtocol_Object = MibTableColumn
tl1pppBadProtocol = _Tl1pppBadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1, 1),
    _Tl1pppBadProtocol_Type()
)
tl1pppBadProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1pppBadProtocol.setStatus("mandatory")
_Tl1pppBadAddress_Type = Counter32
_Tl1pppBadAddress_Object = MibTableColumn
tl1pppBadAddress = _Tl1pppBadAddress_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1, 2),
    _Tl1pppBadAddress_Type()
)
tl1pppBadAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1pppBadAddress.setStatus("mandatory")
_Tl1pppBadLcp_Type = Counter32
_Tl1pppBadLcp_Object = MibTableColumn
tl1pppBadLcp = _Tl1pppBadLcp_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1, 3),
    _Tl1pppBadLcp_Type()
)
tl1pppBadLcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1pppBadLcp.setStatus("mandatory")
_Tl1pppBadIpcp_Type = Counter32
_Tl1pppBadIpcp_Object = MibTableColumn
tl1pppBadIpcp = _Tl1pppBadIpcp_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1, 4),
    _Tl1pppBadIpcp_Type()
)
tl1pppBadIpcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1pppBadIpcp.setStatus("mandatory")
_Tl1pppBadIdpcp_Type = Counter32
_Tl1pppBadIdpcp_Object = MibTableColumn
tl1pppBadIdpcp = _Tl1pppBadIdpcp_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1, 5),
    _Tl1pppBadIdpcp_Type()
)
tl1pppBadIdpcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1pppBadIdpcp.setStatus("mandatory")
_Tl1pppBadIpxcp_Type = Counter32
_Tl1pppBadIpxcp_Object = MibTableColumn
tl1pppBadIpxcp = _Tl1pppBadIpxcp_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1, 6),
    _Tl1pppBadIpxcp_Type()
)
tl1pppBadIpxcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1pppBadIpxcp.setStatus("mandatory")
_Tl1pppNumCrSent_Type = Counter32
_Tl1pppNumCrSent_Object = MibTableColumn
tl1pppNumCrSent = _Tl1pppNumCrSent_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1, 7),
    _Tl1pppNumCrSent_Type()
)
tl1pppNumCrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1pppNumCrSent.setStatus("mandatory")
_Tl1pppNumCrRecd_Type = Counter32
_Tl1pppNumCrRecd_Object = MibTableColumn
tl1pppNumCrRecd = _Tl1pppNumCrRecd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1, 8),
    _Tl1pppNumCrRecd_Type()
)
tl1pppNumCrRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1pppNumCrRecd.setStatus("mandatory")
_Tl1pppNumTrRecd_Type = Counter32
_Tl1pppNumTrRecd_Object = MibTableColumn
tl1pppNumTrRecd = _Tl1pppNumTrRecd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 18, 3, 1, 9),
    _Tl1pppNumTrRecd_Type()
)
tl1pppNumTrRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1pppNumTrRecd.setStatus("mandatory")
_Tl1srtb_ObjectIdentity = ObjectIdentity
tl1srtb = _Tl1srtb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19)
)


class _Tl1srtbInternalLanEnabled_Type(Integer32):
    """Custom type tl1srtbInternalLanEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Tl1srtbInternalLanEnabled_Type.__name__ = "Integer32"
_Tl1srtbInternalLanEnabled_Object = MibScalar
tl1srtbInternalLanEnabled = _Tl1srtbInternalLanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 1),
    _Tl1srtbInternalLanEnabled_Type()
)
tl1srtbInternalLanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbInternalLanEnabled.setStatus("mandatory")


class _Tl1srtbInternalLanId_Type(Integer32):
    """Custom type tl1srtbInternalLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Tl1srtbInternalLanId_Type.__name__ = "Integer32"
_Tl1srtbInternalLanId_Object = MibScalar
tl1srtbInternalLanId = _Tl1srtbInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 2),
    _Tl1srtbInternalLanId_Type()
)
tl1srtbInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbInternalLanId.setStatus("mandatory")
_Tl1srtbUpTime_Type = TimeTicks
_Tl1srtbUpTime_Object = MibScalar
tl1srtbUpTime = _Tl1srtbUpTime_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 3),
    _Tl1srtbUpTime_Type()
)
tl1srtbUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbUpTime.setStatus("mandatory")
_Tl1srtbPortParamsTable_Object = MibTable
tl1srtbPortParamsTable = _Tl1srtbPortParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 4)
)
if mibBuilder.loadTexts:
    tl1srtbPortParamsTable.setStatus("mandatory")
_Tl1srtbPortParamsEntry_Object = MibTableRow
tl1srtbPortParamsEntry = _Tl1srtbPortParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 4, 1)
)
if mibBuilder.loadTexts:
    tl1srtbPortParamsEntry.setStatus("mandatory")


class _Tl1srtbBridgeNumber_Type(Integer32):
    """Custom type tl1srtbBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Tl1srtbBridgeNumber_Type.__name__ = "Integer32"
_Tl1srtbBridgeNumber_Object = MibTableColumn
tl1srtbBridgeNumber = _Tl1srtbBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 4, 1, 1),
    _Tl1srtbBridgeNumber_Type()
)
tl1srtbBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbBridgeNumber.setStatus("mandatory")


class _Tl1srtbRoutingType_Type(Integer32):
    """Custom type tl1srtbRoutingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("sr", 2),
          ("srt", 1),
          ("tb", 0))
    )


_Tl1srtbRoutingType_Type.__name__ = "Integer32"
_Tl1srtbRoutingType_Object = MibTableColumn
tl1srtbRoutingType = _Tl1srtbRoutingType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 4, 1, 2),
    _Tl1srtbRoutingType_Type()
)
tl1srtbRoutingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbRoutingType.setStatus("mandatory")


class _Tl1srtbLanId_Type(Integer32):
    """Custom type tl1srtbLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Tl1srtbLanId_Type.__name__ = "Integer32"
_Tl1srtbLanId_Object = MibTableColumn
tl1srtbLanId = _Tl1srtbLanId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 4, 1, 3),
    _Tl1srtbLanId_Type()
)
tl1srtbLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbLanId.setStatus("mandatory")


class _Tl1srtbIsVLan_Type(Integer32):
    """Custom type tl1srtbIsVLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1srtbIsVLan_Type.__name__ = "Integer32"
_Tl1srtbIsVLan_Object = MibTableColumn
tl1srtbIsVLan = _Tl1srtbIsVLan_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 4, 1, 4),
    _Tl1srtbIsVLan_Type()
)
tl1srtbIsVLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbIsVLan.setStatus("mandatory")


class _Tl1srtbRdLimit_Type(Integer32):
    """Custom type tl1srtbRdLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_Tl1srtbRdLimit_Type.__name__ = "Integer32"
_Tl1srtbRdLimit_Object = MibTableColumn
tl1srtbRdLimit = _Tl1srtbRdLimit_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 4, 1, 5),
    _Tl1srtbRdLimit_Type()
)
tl1srtbRdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbRdLimit.setStatus("mandatory")


class _Tl1srtbOutUserPriority_Type(Integer32):
    """Custom type tl1srtbOutUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Tl1srtbOutUserPriority_Type.__name__ = "Integer32"
_Tl1srtbOutUserPriority_Object = MibTableColumn
tl1srtbOutUserPriority = _Tl1srtbOutUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 4, 1, 6),
    _Tl1srtbOutUserPriority_Type()
)
tl1srtbOutUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbOutUserPriority.setStatus("mandatory")


class _Tl1srtbOutAccessPriority_Type(Integer32):
    """Custom type tl1srtbOutAccessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Tl1srtbOutAccessPriority_Type.__name__ = "Integer32"
_Tl1srtbOutAccessPriority_Object = MibTableColumn
tl1srtbOutAccessPriority = _Tl1srtbOutAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 4, 1, 7),
    _Tl1srtbOutAccessPriority_Type()
)
tl1srtbOutAccessPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbOutAccessPriority.setStatus("mandatory")
_Tl1srtbPortCounterTable_Object = MibTable
tl1srtbPortCounterTable = _Tl1srtbPortCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5)
)
if mibBuilder.loadTexts:
    tl1srtbPortCounterTable.setStatus("mandatory")
_Tl1srtbPortCounterEntry_Object = MibTableRow
tl1srtbPortCounterEntry = _Tl1srtbPortCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1)
)
if mibBuilder.loadTexts:
    tl1srtbPortCounterEntry.setStatus("mandatory")
_Tl1srtbInTSFramesReceived_Type = Counter32
_Tl1srtbInTSFramesReceived_Object = MibTableColumn
tl1srtbInTSFramesReceived = _Tl1srtbInTSFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 1),
    _Tl1srtbInTSFramesReceived_Type()
)
tl1srtbInTSFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbInTSFramesReceived.setStatus("mandatory")
_Tl1srtbInTSFramesDiscarded_Type = Counter32
_Tl1srtbInTSFramesDiscarded_Object = MibTableColumn
tl1srtbInTSFramesDiscarded = _Tl1srtbInTSFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 2),
    _Tl1srtbInTSFramesDiscarded_Type()
)
tl1srtbInTSFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbInTSFramesDiscarded.setStatus("mandatory")
_Tl1srtbOutTSFramesFrwd_Type = Counter32
_Tl1srtbOutTSFramesFrwd_Object = MibTableColumn
tl1srtbOutTSFramesFrwd = _Tl1srtbOutTSFramesFrwd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 3),
    _Tl1srtbOutTSFramesFrwd_Type()
)
tl1srtbOutTSFramesFrwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbOutTSFramesFrwd.setStatus("mandatory")
_Tl1srtbDiscardBuffers_Type = Counter32
_Tl1srtbDiscardBuffers_Object = MibTableColumn
tl1srtbDiscardBuffers = _Tl1srtbDiscardBuffers_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 4),
    _Tl1srtbDiscardBuffers_Type()
)
tl1srtbDiscardBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbDiscardBuffers.setStatus("mandatory")
_Tl1srtbDiscardTransitDelay_Type = Counter32
_Tl1srtbDiscardTransitDelay_Object = MibTableColumn
tl1srtbDiscardTransitDelay = _Tl1srtbDiscardTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 5),
    _Tl1srtbDiscardTransitDelay_Type()
)
tl1srtbDiscardTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbDiscardTransitDelay.setStatus("mandatory")
_Tl1srtbDiscardOnError_Type = Counter32
_Tl1srtbDiscardOnError_Object = MibTableColumn
tl1srtbDiscardOnError = _Tl1srtbDiscardOnError_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 6),
    _Tl1srtbDiscardOnError_Type()
)
tl1srtbDiscardOnError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbDiscardOnError.setStatus("mandatory")
_Tl1srtbInvalidRi_Type = Counter32
_Tl1srtbInvalidRi_Object = MibTableColumn
tl1srtbInvalidRi = _Tl1srtbInvalidRi_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 7),
    _Tl1srtbInvalidRi_Type()
)
tl1srtbInvalidRi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbInvalidRi.setStatus("mandatory")
_Tl1srtbLanIdMismatch_Type = Counter32
_Tl1srtbLanIdMismatch_Object = MibTableColumn
tl1srtbLanIdMismatch = _Tl1srtbLanIdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 8),
    _Tl1srtbLanIdMismatch_Type()
)
tl1srtbLanIdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbLanIdMismatch.setStatus("mandatory")
_Tl1srtbDupLanIdOrTreeError_Type = Counter32
_Tl1srtbDupLanIdOrTreeError_Object = MibTableColumn
tl1srtbDupLanIdOrTreeError = _Tl1srtbDupLanIdOrTreeError_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 9),
    _Tl1srtbDupLanIdOrTreeError_Type()
)
tl1srtbDupLanIdOrTreeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbDupLanIdOrTreeError.setStatus("mandatory")
_Tl1srtbDiscardHopCountExcd_Type = Counter32
_Tl1srtbDiscardHopCountExcd_Object = MibTableColumn
tl1srtbDiscardHopCountExcd = _Tl1srtbDiscardHopCountExcd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 10),
    _Tl1srtbDiscardHopCountExcd_Type()
)
tl1srtbDiscardHopCountExcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbDiscardHopCountExcd.setStatus("mandatory")
_Tl1srtbExplorerFramesFrwd_Type = Counter32
_Tl1srtbExplorerFramesFrwd_Object = MibTableColumn
tl1srtbExplorerFramesFrwd = _Tl1srtbExplorerFramesFrwd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 11),
    _Tl1srtbExplorerFramesFrwd_Type()
)
tl1srtbExplorerFramesFrwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbExplorerFramesFrwd.setStatus("mandatory")
_Tl1srtbExplorerOctetsFrwd_Type = Counter32
_Tl1srtbExplorerOctetsFrwd_Object = MibTableColumn
tl1srtbExplorerOctetsFrwd = _Tl1srtbExplorerOctetsFrwd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 12),
    _Tl1srtbExplorerOctetsFrwd_Type()
)
tl1srtbExplorerOctetsFrwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbExplorerOctetsFrwd.setStatus("mandatory")
_Tl1srtbNonExplorFramesFrwd_Type = Counter32
_Tl1srtbNonExplorFramesFrwd_Object = MibTableColumn
tl1srtbNonExplorFramesFrwd = _Tl1srtbNonExplorFramesFrwd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 13),
    _Tl1srtbNonExplorFramesFrwd_Type()
)
tl1srtbNonExplorFramesFrwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbNonExplorFramesFrwd.setStatus("mandatory")
_Tl1srtbNonExplorOctetsFrwd_Type = Counter32
_Tl1srtbNonExplorOctetsFrwd_Object = MibTableColumn
tl1srtbNonExplorOctetsFrwd = _Tl1srtbNonExplorOctetsFrwd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 14),
    _Tl1srtbNonExplorOctetsFrwd_Type()
)
tl1srtbNonExplorOctetsFrwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbNonExplorOctetsFrwd.setStatus("mandatory")
_Tl1srtbTotalSRFrwd_Type = Counter32
_Tl1srtbTotalSRFrwd_Object = MibTableColumn
tl1srtbTotalSRFrwd = _Tl1srtbTotalSRFrwd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 15),
    _Tl1srtbTotalSRFrwd_Type()
)
tl1srtbTotalSRFrwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbTotalSRFrwd.setStatus("mandatory")
_Tl1srtbValidSRFramesReceived_Type = Counter32
_Tl1srtbValidSRFramesReceived_Object = MibTableColumn
tl1srtbValidSRFramesReceived = _Tl1srtbValidSRFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 16),
    _Tl1srtbValidSRFramesReceived_Type()
)
tl1srtbValidSRFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbValidSRFramesReceived.setStatus("mandatory")
_Tl1srtbValidExplorOctetsRcvd_Type = Counter32
_Tl1srtbValidExplorOctetsRcvd_Object = MibTableColumn
tl1srtbValidExplorOctetsRcvd = _Tl1srtbValidExplorOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 17),
    _Tl1srtbValidExplorOctetsRcvd_Type()
)
tl1srtbValidExplorOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbValidExplorOctetsRcvd.setStatus("mandatory")
_Tl1srtbValidSRDiscarded_Type = Counter32
_Tl1srtbValidSRDiscarded_Object = MibTableColumn
tl1srtbValidSRDiscarded = _Tl1srtbValidSRDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 18),
    _Tl1srtbValidSRDiscarded_Type()
)
tl1srtbValidSRDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbValidSRDiscarded.setStatus("mandatory")
_Tl1srtbTotalSRDiscarded_Type = Counter32
_Tl1srtbTotalSRDiscarded_Object = MibTableColumn
tl1srtbTotalSRDiscarded = _Tl1srtbTotalSRDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 5, 1, 19),
    _Tl1srtbTotalSRDiscarded_Type()
)
tl1srtbTotalSRDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbTotalSRDiscarded.setStatus("mandatory")
_Tl1srtbFilterDbParams_ObjectIdentity = ObjectIdentity
tl1srtbFilterDbParams = _Tl1srtbFilterDbParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 6)
)
_Tl1srtbFilterDbSize_Type = Integer32
_Tl1srtbFilterDbSize_Object = MibScalar
tl1srtbFilterDbSize = _Tl1srtbFilterDbSize_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 6, 1),
    _Tl1srtbFilterDbSize_Type()
)
tl1srtbFilterDbSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbFilterDbSize.setStatus("mandatory")
_Tl1srtbPermDbSize_Type = Integer32
_Tl1srtbPermDbSize_Object = MibScalar
tl1srtbPermDbSize = _Tl1srtbPermDbSize_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 6, 2),
    _Tl1srtbPermDbSize_Type()
)
tl1srtbPermDbSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbPermDbSize.setStatus("mandatory")
_Tl1srtbNumDynamicEntries_Type = Integer32
_Tl1srtbNumDynamicEntries_Object = MibScalar
tl1srtbNumDynamicEntries = _Tl1srtbNumDynamicEntries_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 6, 3),
    _Tl1srtbNumDynamicEntries_Type()
)
tl1srtbNumDynamicEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbNumDynamicEntries.setStatus("mandatory")
_Tl1srtbFilterDbAgeingTime_Type = Integer32
_Tl1srtbFilterDbAgeingTime_Object = MibScalar
tl1srtbFilterDbAgeingTime = _Tl1srtbFilterDbAgeingTime_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 6, 4),
    _Tl1srtbFilterDbAgeingTime_Type()
)
tl1srtbFilterDbAgeingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbFilterDbAgeingTime.setStatus("mandatory")
_Tl1srtbDynamicFilterDbTable_Object = MibTable
tl1srtbDynamicFilterDbTable = _Tl1srtbDynamicFilterDbTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 7)
)
if mibBuilder.loadTexts:
    tl1srtbDynamicFilterDbTable.setStatus("mandatory")
_Tl1srtbDynamicFilterDbEntry_Object = MibTableRow
tl1srtbDynamicFilterDbEntry = _Tl1srtbDynamicFilterDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 7, 1)
)
if mibBuilder.loadTexts:
    tl1srtbDynamicFilterDbEntry.setStatus("mandatory")


class _Tl1srtbDynamicMacAddr_Type(OctetString):
    """Custom type tl1srtbDynamicMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1srtbDynamicMacAddr_Type.__name__ = "OctetString"
_Tl1srtbDynamicMacAddr_Object = MibTableColumn
tl1srtbDynamicMacAddr = _Tl1srtbDynamicMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 7, 1, 1),
    _Tl1srtbDynamicMacAddr_Type()
)
tl1srtbDynamicMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbDynamicMacAddr.setStatus("mandatory")
_Tl1srtbDynamicPortNumber_Type = Integer32
_Tl1srtbDynamicPortNumber_Object = MibTableColumn
tl1srtbDynamicPortNumber = _Tl1srtbDynamicPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 7, 1, 2),
    _Tl1srtbDynamicPortNumber_Type()
)
tl1srtbDynamicPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1srtbDynamicPortNumber.setStatus("mandatory")
_Tl1srtbStaticFilterDbParams_ObjectIdentity = ObjectIdentity
tl1srtbStaticFilterDbParams = _Tl1srtbStaticFilterDbParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8)
)
_Tl1srtbStatEntMacAddrTable_Object = MibTable
tl1srtbStatEntMacAddrTable = _Tl1srtbStatEntMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8, 1)
)
if mibBuilder.loadTexts:
    tl1srtbStatEntMacAddrTable.setStatus("mandatory")
_Tl1srtbStatEntMacAddrEntry_Object = MibTableRow
tl1srtbStatEntMacAddrEntry = _Tl1srtbStatEntMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tl1srtbStatEntMacAddrEntry.setStatus("mandatory")


class _Tl1srtbStaticEntryMacAddr_Type(OctetString):
    """Custom type tl1srtbStaticEntryMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1srtbStaticEntryMacAddr_Type.__name__ = "OctetString"
_Tl1srtbStaticEntryMacAddr_Object = MibTableColumn
tl1srtbStaticEntryMacAddr = _Tl1srtbStaticEntryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8, 1, 1, 1),
    _Tl1srtbStaticEntryMacAddr_Type()
)
tl1srtbStaticEntryMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbStaticEntryMacAddr.setStatus("mandatory")
_Tl1srtbStatEntPortArrayTable_Object = MibTable
tl1srtbStatEntPortArrayTable = _Tl1srtbStatEntPortArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8, 2)
)
if mibBuilder.loadTexts:
    tl1srtbStatEntPortArrayTable.setStatus("mandatory")
_Tl1srtbStatEntPortArrayEntry_Object = MibTableRow
tl1srtbStatEntPortArrayEntry = _Tl1srtbStatEntPortArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8, 2, 1)
)
if mibBuilder.loadTexts:
    tl1srtbStatEntPortArrayEntry.setStatus("mandatory")


class _Tl1srtbStaticEntryPermit_Type(Integer32):
    """Custom type tl1srtbStaticEntryPermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_Tl1srtbStaticEntryPermit_Type.__name__ = "Integer32"
_Tl1srtbStaticEntryPermit_Object = MibTableColumn
tl1srtbStaticEntryPermit = _Tl1srtbStaticEntryPermit_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8, 2, 1, 1),
    _Tl1srtbStaticEntryPermit_Type()
)
tl1srtbStaticEntryPermit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbStaticEntryPermit.setStatus("mandatory")
_Tl1srtbStatEntSizeTable_Object = MibTable
tl1srtbStatEntSizeTable = _Tl1srtbStatEntSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8, 3)
)
if mibBuilder.loadTexts:
    tl1srtbStatEntSizeTable.setStatus("mandatory")
_Tl1srtbStatEntSizeEntry_Object = MibTableRow
tl1srtbStatEntSizeEntry = _Tl1srtbStatEntSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8, 3, 1)
)
if mibBuilder.loadTexts:
    tl1srtbStatEntSizeEntry.setStatus("mandatory")
_Tl1srtbNumStaticEntries_Type = Integer32
_Tl1srtbNumStaticEntries_Object = MibTableColumn
tl1srtbNumStaticEntries = _Tl1srtbNumStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 8, 3, 1, 1),
    _Tl1srtbNumStaticEntries_Type()
)
tl1srtbNumStaticEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbNumStaticEntries.setStatus("mandatory")
_Tl1srtbNumMacAddrAcfEntrs_Type = Integer32
_Tl1srtbNumMacAddrAcfEntrs_Object = MibScalar
tl1srtbNumMacAddrAcfEntrs = _Tl1srtbNumMacAddrAcfEntrs_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 9),
    _Tl1srtbNumMacAddrAcfEntrs_Type()
)
tl1srtbNumMacAddrAcfEntrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbNumMacAddrAcfEntrs.setStatus("mandatory")
_Tl1srtbMacAddrAcfTable_Object = MibTable
tl1srtbMacAddrAcfTable = _Tl1srtbMacAddrAcfTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 10)
)
if mibBuilder.loadTexts:
    tl1srtbMacAddrAcfTable.setStatus("mandatory")
_Tl1srtbMacAddrAcfEntry_Object = MibTableRow
tl1srtbMacAddrAcfEntry = _Tl1srtbMacAddrAcfEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 10, 1)
)
if mibBuilder.loadTexts:
    tl1srtbMacAddrAcfEntry.setStatus("mandatory")


class _Tl1srtbAcfSrcMacAddr_Type(OctetString):
    """Custom type tl1srtbAcfSrcMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1srtbAcfSrcMacAddr_Type.__name__ = "OctetString"
_Tl1srtbAcfSrcMacAddr_Object = MibTableColumn
tl1srtbAcfSrcMacAddr = _Tl1srtbAcfSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 10, 1, 1),
    _Tl1srtbAcfSrcMacAddr_Type()
)
tl1srtbAcfSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbAcfSrcMacAddr.setStatus("mandatory")


class _Tl1srtbAcfDestMacAddr_Type(OctetString):
    """Custom type tl1srtbAcfDestMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Tl1srtbAcfDestMacAddr_Type.__name__ = "OctetString"
_Tl1srtbAcfDestMacAddr_Object = MibTableColumn
tl1srtbAcfDestMacAddr = _Tl1srtbAcfDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 10, 1, 2),
    _Tl1srtbAcfDestMacAddr_Type()
)
tl1srtbAcfDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbAcfDestMacAddr.setStatus("mandatory")
_Tl1srtbMaskAcfInfo_ObjectIdentity = ObjectIdentity
tl1srtbMaskAcfInfo = _Tl1srtbMaskAcfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11)
)
_Tl1srtbMaskAcfParamsTable_Object = MibTable
tl1srtbMaskAcfParamsTable = _Tl1srtbMaskAcfParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11, 1)
)
if mibBuilder.loadTexts:
    tl1srtbMaskAcfParamsTable.setStatus("mandatory")
_Tl1srtbMaskAcfParamsEntry_Object = MibTableRow
tl1srtbMaskAcfParamsEntry = _Tl1srtbMaskAcfParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11, 1, 1)
)
if mibBuilder.loadTexts:
    tl1srtbMaskAcfParamsEntry.setStatus("mandatory")
_Tl1srtbNumMaskAcfEntries_Type = Integer32
_Tl1srtbNumMaskAcfEntries_Object = MibTableColumn
tl1srtbNumMaskAcfEntries = _Tl1srtbNumMaskAcfEntries_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11, 1, 1, 1),
    _Tl1srtbNumMaskAcfEntries_Type()
)
tl1srtbNumMaskAcfEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbNumMaskAcfEntries.setStatus("mandatory")


class _Tl1srtbMaskAcfPermit_Type(Integer32):
    """Custom type tl1srtbMaskAcfPermit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_Tl1srtbMaskAcfPermit_Type.__name__ = "Integer32"
_Tl1srtbMaskAcfPermit_Object = MibTableColumn
tl1srtbMaskAcfPermit = _Tl1srtbMaskAcfPermit_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11, 1, 1, 2),
    _Tl1srtbMaskAcfPermit_Type()
)
tl1srtbMaskAcfPermit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbMaskAcfPermit.setStatus("mandatory")
_Tl1srtbMaskAcfTable_Object = MibTable
tl1srtbMaskAcfTable = _Tl1srtbMaskAcfTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11, 2)
)
if mibBuilder.loadTexts:
    tl1srtbMaskAcfTable.setStatus("mandatory")
_Tl1srtbMaskAcfEntry_Object = MibTableRow
tl1srtbMaskAcfEntry = _Tl1srtbMaskAcfEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11, 2, 1)
)
if mibBuilder.loadTexts:
    tl1srtbMaskAcfEntry.setStatus("mandatory")
_Tl1srtbAcfValue_Type = Integer32
_Tl1srtbAcfValue_Object = MibTableColumn
tl1srtbAcfValue = _Tl1srtbAcfValue_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11, 2, 1, 1),
    _Tl1srtbAcfValue_Type()
)
tl1srtbAcfValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbAcfValue.setStatus("mandatory")
_Tl1srtbAcfMask_Type = Integer32
_Tl1srtbAcfMask_Object = MibTableColumn
tl1srtbAcfMask = _Tl1srtbAcfMask_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11, 2, 1, 2),
    _Tl1srtbAcfMask_Type()
)
tl1srtbAcfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbAcfMask.setStatus("mandatory")
_Tl1srtbAcfOffset_Type = Integer32
_Tl1srtbAcfOffset_Object = MibTableColumn
tl1srtbAcfOffset = _Tl1srtbAcfOffset_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 19, 11, 2, 1, 3),
    _Tl1srtbAcfOffset_Type()
)
tl1srtbAcfOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1srtbAcfOffset.setStatus("mandatory")
_Tl1ospf_ObjectIdentity = ObjectIdentity
tl1ospf = _Tl1ospf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20)
)
_Tl1ospfRtrId_Type = IpAddress
_Tl1ospfRtrId_Object = MibScalar
tl1ospfRtrId = _Tl1ospfRtrId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 1),
    _Tl1ospfRtrId_Type()
)
tl1ospfRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfRtrId.setStatus("mandatory")
_Tl1ospfAreaTable_Object = MibTable
tl1ospfAreaTable = _Tl1ospfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 2)
)
if mibBuilder.loadTexts:
    tl1ospfAreaTable.setStatus("mandatory")
_Tl1ospfAreaEntry_Object = MibTableRow
tl1ospfAreaEntry = _Tl1ospfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    tl1ospfAreaEntry.setStatus("mandatory")


class _Tl1ospfAreaID_Type(Integer32):
    """Custom type tl1ospfAreaID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_Tl1ospfAreaID_Type.__name__ = "Integer32"
_Tl1ospfAreaID_Object = MibTableColumn
tl1ospfAreaID = _Tl1ospfAreaID_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 2, 1, 1),
    _Tl1ospfAreaID_Type()
)
tl1ospfAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfAreaID.setStatus("mandatory")


class _Tl1ospfAuthType_Type(Integer32):
    """Custom type tl1ospfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Tl1ospfAuthType_Type.__name__ = "Integer32"
_Tl1ospfAuthType_Object = MibTableColumn
tl1ospfAuthType = _Tl1ospfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 2, 1, 2),
    _Tl1ospfAuthType_Type()
)
tl1ospfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfAuthType.setStatus("mandatory")


class _Tl1ospfNetCount_Type(Integer32):
    """Custom type tl1ospfNetCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Tl1ospfNetCount_Type.__name__ = "Integer32"
_Tl1ospfNetCount_Object = MibTableColumn
tl1ospfNetCount = _Tl1ospfNetCount_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 2, 1, 3),
    _Tl1ospfNetCount_Type()
)
tl1ospfNetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfNetCount.setStatus("mandatory")
_Tl1ospfAreaNetTable_Object = MibTable
tl1ospfAreaNetTable = _Tl1ospfAreaNetTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 3)
)
if mibBuilder.loadTexts:
    tl1ospfAreaNetTable.setStatus("mandatory")
_Tl1ospfAreaNetEntry_Object = MibTableRow
tl1ospfAreaNetEntry = _Tl1ospfAreaNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 3, 1)
)
if mibBuilder.loadTexts:
    tl1ospfAreaNetEntry.setStatus("mandatory")
_Tl1ospfNet_Type = IpAddress
_Tl1ospfNet_Object = MibTableColumn
tl1ospfNet = _Tl1ospfNet_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 3, 1, 1),
    _Tl1ospfNet_Type()
)
tl1ospfNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfNet.setStatus("mandatory")
_Tl1ospfMask_Type = IpAddress
_Tl1ospfMask_Object = MibTableColumn
tl1ospfMask = _Tl1ospfMask_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 3, 1, 2),
    _Tl1ospfMask_Type()
)
tl1ospfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfMask.setStatus("mandatory")
_Tl1ospfVirtualIfTable_Object = MibTable
tl1ospfVirtualIfTable = _Tl1ospfVirtualIfTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 4)
)
if mibBuilder.loadTexts:
    tl1ospfVirtualIfTable.setStatus("mandatory")
_Tl1ospfVirtualIfEntry_Object = MibTableRow
tl1ospfVirtualIfEntry = _Tl1ospfVirtualIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 4, 1)
)
if mibBuilder.loadTexts:
    tl1ospfVirtualIfEntry.setStatus("mandatory")
_Tl1ospfNbrId_Type = IpAddress
_Tl1ospfNbrId_Object = MibTableColumn
tl1ospfNbrId = _Tl1ospfNbrId_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 4, 1, 1),
    _Tl1ospfNbrId_Type()
)
tl1ospfNbrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfNbrId.setStatus("mandatory")


class _Tl1ospfTransArea_Type(Integer32):
    """Custom type tl1ospfTransArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65335),
    )


_Tl1ospfTransArea_Type.__name__ = "Integer32"
_Tl1ospfTransArea_Object = MibTableColumn
tl1ospfTransArea = _Tl1ospfTransArea_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 4, 1, 2),
    _Tl1ospfTransArea_Type()
)
tl1ospfTransArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfTransArea.setStatus("mandatory")


class _Tl1ospfTransDelay_Type(Integer32):
    """Custom type tl1ospfTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65335),
    )


_Tl1ospfTransDelay_Type.__name__ = "Integer32"
_Tl1ospfTransDelay_Object = MibTableColumn
tl1ospfTransDelay = _Tl1ospfTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 4, 1, 3),
    _Tl1ospfTransDelay_Type()
)
tl1ospfTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfTransDelay.setStatus("mandatory")


class _Tl1ospfRxmtIntvl_Type(Integer32):
    """Custom type tl1ospfRxmtIntvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65335),
    )


_Tl1ospfRxmtIntvl_Type.__name__ = "Integer32"
_Tl1ospfRxmtIntvl_Object = MibTableColumn
tl1ospfRxmtIntvl = _Tl1ospfRxmtIntvl_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 4, 1, 4),
    _Tl1ospfRxmtIntvl_Type()
)
tl1ospfRxmtIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfRxmtIntvl.setStatus("mandatory")


class _Tl1ospfHelloIntvl_Type(Integer32):
    """Custom type tl1ospfHelloIntvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65335),
    )


_Tl1ospfHelloIntvl_Type.__name__ = "Integer32"
_Tl1ospfHelloIntvl_Object = MibTableColumn
tl1ospfHelloIntvl = _Tl1ospfHelloIntvl_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 4, 1, 5),
    _Tl1ospfHelloIntvl_Type()
)
tl1ospfHelloIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfHelloIntvl.setStatus("mandatory")


class _Tl1ospfRtrDeadIntvl_Type(Integer32):
    """Custom type tl1ospfRtrDeadIntvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65335),
    )


_Tl1ospfRtrDeadIntvl_Type.__name__ = "Integer32"
_Tl1ospfRtrDeadIntvl_Object = MibTableColumn
tl1ospfRtrDeadIntvl = _Tl1ospfRtrDeadIntvl_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 4, 1, 6),
    _Tl1ospfRtrDeadIntvl_Type()
)
tl1ospfRtrDeadIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfRtrDeadIntvl.setStatus("mandatory")


class _Tl1ospfAuthKey_Type(OctetString):
    """Custom type tl1ospfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Tl1ospfAuthKey_Type.__name__ = "OctetString"
_Tl1ospfAuthKey_Object = MibTableColumn
tl1ospfAuthKey = _Tl1ospfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 4, 1, 7),
    _Tl1ospfAuthKey_Type()
)
tl1ospfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfAuthKey.setStatus("mandatory")
_Tl1ospfIntfTable_Object = MibTable
tl1ospfIntfTable = _Tl1ospfIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5)
)
if mibBuilder.loadTexts:
    tl1ospfIntfTable.setStatus("mandatory")
_Tl1ospfIntfEntry_Object = MibTableRow
tl1ospfIntfEntry = _Tl1ospfIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1)
)
if mibBuilder.loadTexts:
    tl1ospfIntfEntry.setStatus("mandatory")


class _Tl1ospfIntfRun_Type(Integer32):
    """Custom type tl1ospfIntfRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dont-run", 0),
          ("run", 1))
    )


_Tl1ospfIntfRun_Type.__name__ = "Integer32"
_Tl1ospfIntfRun_Object = MibTableColumn
tl1ospfIntfRun = _Tl1ospfIntfRun_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 1),
    _Tl1ospfIntfRun_Type()
)
tl1ospfIntfRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfRun.setStatus("mandatory")


class _Tl1ospfIntfAreaID_Type(Integer32):
    """Custom type tl1ospfIntfAreaID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65335),
    )


_Tl1ospfIntfAreaID_Type.__name__ = "Integer32"
_Tl1ospfIntfAreaID_Object = MibTableColumn
tl1ospfIntfAreaID = _Tl1ospfIntfAreaID_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 2),
    _Tl1ospfIntfAreaID_Type()
)
tl1ospfIntfAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfAreaID.setStatus("mandatory")


class _Tl1ospfIntfType_Type(Integer32):
    """Custom type tl1ospfIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Tl1ospfIntfType_Type.__name__ = "Integer32"
_Tl1ospfIntfType_Object = MibTableColumn
tl1ospfIntfType = _Tl1ospfIntfType_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 3),
    _Tl1ospfIntfType_Type()
)
tl1ospfIntfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfType.setStatus("mandatory")


class _Tl1ospfIntfTransDelay_Type(Integer32):
    """Custom type tl1ospfIntfTransDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65335),
    )


_Tl1ospfIntfTransDelay_Type.__name__ = "Integer32"
_Tl1ospfIntfTransDelay_Object = MibTableColumn
tl1ospfIntfTransDelay = _Tl1ospfIntfTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 4),
    _Tl1ospfIntfTransDelay_Type()
)
tl1ospfIntfTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfTransDelay.setStatus("mandatory")


class _Tl1ospfIntfRxmtIntvl_Type(Integer32):
    """Custom type tl1ospfIntfRxmtIntvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65335),
    )


_Tl1ospfIntfRxmtIntvl_Type.__name__ = "Integer32"
_Tl1ospfIntfRxmtIntvl_Object = MibTableColumn
tl1ospfIntfRxmtIntvl = _Tl1ospfIntfRxmtIntvl_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 5),
    _Tl1ospfIntfRxmtIntvl_Type()
)
tl1ospfIntfRxmtIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfRxmtIntvl.setStatus("mandatory")


class _Tl1ospfIntfHelloIntvl_Type(Integer32):
    """Custom type tl1ospfIntfHelloIntvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65335),
    )


_Tl1ospfIntfHelloIntvl_Type.__name__ = "Integer32"
_Tl1ospfIntfHelloIntvl_Object = MibTableColumn
tl1ospfIntfHelloIntvl = _Tl1ospfIntfHelloIntvl_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 6),
    _Tl1ospfIntfHelloIntvl_Type()
)
tl1ospfIntfHelloIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfHelloIntvl.setStatus("mandatory")


class _Tl1ospfIntfRtrDeadIntvl_Type(Integer32):
    """Custom type tl1ospfIntfRtrDeadIntvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65335),
    )


_Tl1ospfIntfRtrDeadIntvl_Type.__name__ = "Integer32"
_Tl1ospfIntfRtrDeadIntvl_Object = MibTableColumn
tl1ospfIntfRtrDeadIntvl = _Tl1ospfIntfRtrDeadIntvl_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 7),
    _Tl1ospfIntfRtrDeadIntvl_Type()
)
tl1ospfIntfRtrDeadIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfRtrDeadIntvl.setStatus("mandatory")


class _Tl1ospfIntfPriority_Type(Integer32):
    """Custom type tl1ospfIntfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Tl1ospfIntfPriority_Type.__name__ = "Integer32"
_Tl1ospfIntfPriority_Object = MibTableColumn
tl1ospfIntfPriority = _Tl1ospfIntfPriority_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 8),
    _Tl1ospfIntfPriority_Type()
)
tl1ospfIntfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfPriority.setStatus("mandatory")


class _Tl1ospfIntfAuthKey_Type(OctetString):
    """Custom type tl1ospfIntfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Tl1ospfIntfAuthKey_Type.__name__ = "OctetString"
_Tl1ospfIntfAuthKey_Object = MibTableColumn
tl1ospfIntfAuthKey = _Tl1ospfIntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 9),
    _Tl1ospfIntfAuthKey_Type()
)
tl1ospfIntfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfAuthKey.setStatus("mandatory")


class _Tl1ospfIntfPollIntvl_Type(Integer32):
    """Custom type tl1ospfIntfPollIntvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65335),
    )


_Tl1ospfIntfPollIntvl_Type.__name__ = "Integer32"
_Tl1ospfIntfPollIntvl_Object = MibTableColumn
tl1ospfIntfPollIntvl = _Tl1ospfIntfPollIntvl_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 10),
    _Tl1ospfIntfPollIntvl_Type()
)
tl1ospfIntfPollIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfPollIntvl.setStatus("mandatory")
_Tl1ospfIntfPtopIntAddr_Type = IpAddress
_Tl1ospfIntfPtopIntAddr_Object = MibScalar
tl1ospfIntfPtopIntAddr = _Tl1ospfIntfPtopIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 5, 1, 11),
    _Tl1ospfIntfPtopIntAddr_Type()
)
tl1ospfIntfPtopIntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIntfPtopIntAddr.setStatus("mandatory")
_Tl1ospfNBMATable_Object = MibTable
tl1ospfNBMATable = _Tl1ospfNBMATable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 6)
)
if mibBuilder.loadTexts:
    tl1ospfNBMATable.setStatus("mandatory")
_Tl1ospfNBMAEntry_Object = MibTableRow
tl1ospfNBMAEntry = _Tl1ospfNBMAEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 6, 1)
)
if mibBuilder.loadTexts:
    tl1ospfNBMAEntry.setStatus("mandatory")
_Tl1ospfAttRtrIpAddr_Type = IpAddress
_Tl1ospfAttRtrIpAddr_Object = MibTableColumn
tl1ospfAttRtrIpAddr = _Tl1ospfAttRtrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 6, 1, 1),
    _Tl1ospfAttRtrIpAddr_Type()
)
tl1ospfAttRtrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfAttRtrIpAddr.setStatus("mandatory")


class _Tl1ospfPriority_Type(Integer32):
    """Custom type tl1ospfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Tl1ospfPriority_Type.__name__ = "Integer32"
_Tl1ospfPriority_Object = MibScalar
tl1ospfPriority = _Tl1ospfPriority_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 6, 1, 2),
    _Tl1ospfPriority_Type()
)
tl1ospfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfPriority.setStatus("mandatory")
_Tl1ospfCumlogTable_Object = MibTable
tl1ospfCumlogTable = _Tl1ospfCumlogTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 7)
)
if mibBuilder.loadTexts:
    tl1ospfCumlogTable.setStatus("mandatory")
_Tl1ospfCumLogEntry_Object = MibTableRow
tl1ospfCumLogEntry = _Tl1ospfCumLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 7, 1)
)
if mibBuilder.loadTexts:
    tl1ospfCumLogEntry.setStatus("mandatory")
_Tl1ospfStat_Type = Counter32
_Tl1ospfStat_Object = MibTableColumn
tl1ospfStat = _Tl1ospfStat_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 7, 1, 1),
    _Tl1ospfStat_Type()
)
tl1ospfStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tl1ospfStat.setStatus("mandatory")
_Tl1ospfIntfTOSTable_Object = MibTable
tl1ospfIntfTOSTable = _Tl1ospfIntfTOSTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 8)
)
if mibBuilder.loadTexts:
    tl1ospfIntfTOSTable.setStatus("mandatory")
_Tl1ospfIntfTOSEntry_Object = MibTableRow
tl1ospfIntfTOSEntry = _Tl1ospfIntfTOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 8, 1)
)
if mibBuilder.loadTexts:
    tl1ospfIntfTOSEntry.setStatus("mandatory")


class _Tl1ospfIfTOSCost_Type(Integer32):
    """Custom type tl1ospfIfTOSCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65335),
    )


_Tl1ospfIfTOSCost_Type.__name__ = "Integer32"
_Tl1ospfIfTOSCost_Object = MibTableColumn
tl1ospfIfTOSCost = _Tl1ospfIfTOSCost_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 20, 8, 1, 1),
    _Tl1ospfIfTOSCost_Type()
)
tl1ospfIfTOSCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1ospfIfTOSCost.setStatus("mandatory")
_Tl1tok_ObjectIdentity = ObjectIdentity
tl1tok = _Tl1tok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 21)
)
_Tl1tokConfigTable_Object = MibTable
tl1tokConfigTable = _Tl1tokConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 21, 1)
)
if mibBuilder.loadTexts:
    tl1tokConfigTable.setStatus("mandatory")
_Tl1tokConfigEntry_Object = MibTableRow
tl1tokConfigEntry = _Tl1tokConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 21, 1, 1)
)
if mibBuilder.loadTexts:
    tl1tokConfigEntry.setStatus("mandatory")


class _Tl1tokEarlyTokenRelease_Type(Integer32):
    """Custom type tl1tokEarlyTokenRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Tl1tokEarlyTokenRelease_Type.__name__ = "Integer32"
_Tl1tokEarlyTokenRelease_Object = MibTableColumn
tl1tokEarlyTokenRelease = _Tl1tokEarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 21, 1, 1, 2),
    _Tl1tokEarlyTokenRelease_Type()
)
tl1tokEarlyTokenRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tokEarlyTokenRelease.setStatus("mandatory")


class _Tl1tokRingSpeed_Type(Integer32):
    """Custom type tl1tokRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("four-Mbps", 0),
          ("sixteen-Mbps", 1))
    )


_Tl1tokRingSpeed_Type.__name__ = "Integer32"
_Tl1tokRingSpeed_Object = MibTableColumn
tl1tokRingSpeed = _Tl1tokRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 16, 2, 2, 21, 1, 1, 3),
    _Tl1tokRingSpeed_Type()
)
tl1tokRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1tokRingSpeed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UNISYS-TIMEPLEX-MIB",
    **{"unisys-timeplex": unisys_timeplex,
       "umgmt": umgmt,
       "umib": umib,
       "usystem": usystem,
       "usystemAction": usystemAction,
       "usystemReboots": usystemReboots,
       "usystemErrorCode": usystemErrorCode,
       "uinterfaces": uinterfaces,
       "uifTable": uifTable,
       "uifEntry": uifEntry,
       "uifEthernetArpWait": uifEthernetArpWait,
       "uifIpAddr": uifIpAddr,
       "uifSubnetMask": uifSubnetMask,
       "uifHdlcBaudRate": uifHdlcBaudRate,
       "uifHdlcRto": uifHdlcRto,
       "uifHdlcAckTo": uifHdlcAckTo,
       "uifHdlcSabmInterval": uifHdlcSabmInterval,
       "uifHdlcRnrInterval": uifHdlcRnrInterval,
       "uifHdlcClockType": uifHdlcClockType,
       "uifHdlcDCE": uifHdlcDCE,
       "uifHdlcThrowaway": uifHdlcThrowaway,
       "uifHdlcAckCount": uifHdlcAckCount,
       "uifFddiArpWait": uifFddiArpWait,
       "uat": uat,
       "uip": uip,
       "uipLogicalDisconnect": uipLogicalDisconnect,
       "uipLoopback": uipLoopback,
       "uipRemoteg1": uipRemoteg1,
       "uipRemoteg2": uipRemoteg2,
       "uipNet1MaxPkt": uipNet1MaxPkt,
       "uipNet2MaxPkt": uipNet2MaxPkt,
       "uipRedirectTo": uipRedirectTo,
       "uipMasker": uipMasker,
       "uipWellKnownGateway": uipWellKnownGateway,
       "uipMaxRoutePids": uipMaxRoutePids,
       "uipRoutePidsTable": uipRoutePidsTable,
       "uipRoutePidsEntry": uipRoutePidsEntry,
       "uipRoutePid": uipRoutePid,
       "uipNbrStaticRoutes": uipNbrStaticRoutes,
       "uipStaticRouteTable": uipStaticRouteTable,
       "uipStaticRouteEntry": uipStaticRouteEntry,
       "uipStaticRouteNetwork": uipStaticRouteNetwork,
       "uipStaticRouteGateway": uipStaticRouteGateway,
       "uipStaticRouteCost": uipStaticRouteCost,
       "uipStaticRouteOverride": uipStaticRouteOverride,
       "uicmp": uicmp,
       "utcp": utcp,
       "utcpRetransTo": utcpRetransTo,
       "utcpRtoMin": utcpRtoMin,
       "utcpRtoMax": utcpRtoMax,
       "utcpWakeup": utcpWakeup,
       "utcpAckTime": utcpAckTime,
       "utcpTimeToLive": utcpTimeToLive,
       "utcpThruput": utcpThruput,
       "utcpFlowAck": utcpFlowAck,
       "uudp": uudp,
       "uegp": uegp,
       "uegpMaxNeighbors": uegpMaxNeighbors,
       "uegpNumberTrustedNeighbors": uegpNumberTrustedNeighbors,
       "uegpNumberNeighbors": uegpNumberNeighbors,
       "uegpNeighborTable": uegpNeighborTable,
       "uegpNeighborEntry": uegpNeighborEntry,
       "uegpNeighbor": uegpNeighbor,
       "uegpAutoSysNumber": uegpAutoSysNumber,
       "uegpMinHelloInterval": uegpMinHelloInterval,
       "uegpMinPollInterval": uegpMinPollInterval,
       "uegpRequestCeaseInterval": uegpRequestCeaseInterval,
       "uegpDeclareDownInterval": uegpDeclareDownInterval,
       "uegpAcquireCeaseInterval": uegpAcquireCeaseInterval,
       "uegpEnoughInterval": uegpEnoughInterval,
       "uegpPurgeInterval": uegpPurgeInterval,
       "uegpMode": uegpMode,
       "uegpErrorTreatment": uegpErrorTreatment,
       "uegpSharedNetwork": uegpSharedNetwork,
       "uggp": uggp,
       "uggpEchoInterval": uggpEchoInterval,
       "uggpMaxNeighbors": uggpMaxNeighbors,
       "uggpNumberNeighbors": uggpNumberNeighbors,
       "uggpNeighborTable": uggpNeighborTable,
       "uggpNeighborEntry": uggpNeighborEntry,
       "uggpNeighbor": uggpNeighbor,
       "urip": urip,
       "usnmp": usnmp,
       "usnmpVersion": usnmpVersion,
       "usnmpCommunity": usnmpCommunity,
       "usnmpRequests": usnmpRequests,
       "usnmpTraps": usnmpTraps,
       "usnmpForwardTraps": usnmpForwardTraps,
       "uhfp": uhfp,
       "uhfpMaxMsg": uhfpMaxMsg,
       "uhfpPad": uhfpPad,
       "uhfpSwap": uhfpSwap,
       "uddn": uddn,
       "uddnTimeout": uddnTimeout,
       "uddnMsgout": uddnMsgout,
       "uddnHipUp": uddnHipUp,
       "uddnHdhUp": uddnHdhUp,
       "uddnLinkUp": uddnLinkUp,
       "uddnTotalQ": uddnTotalQ,
       "uddnConnections": uddnConnections,
       "uddnLinkDownTo": uddnLinkDownTo,
       "uddnRcvIncomplete": uddnRcvIncomplete,
       "uddnConnectionsReused": uddnConnectionsReused,
       "uddnHdhWentDown": uddnHdhWentDown,
       "uddnLinkWentDown": uddnLinkWentDown,
       "uddnLeaderErrs": uddnLeaderErrs,
       "uddnPSNGoingDown": uddnPSNGoingDown,
       "uddnDeadHostSTATUS": uddnDeadHostSTATUS,
       "uddnIfReset": uddnIfReset,
       "ux25": ux25,
       "ux25IfTable": ux25IfTable,
       "ux25IfEntry": ux25IfEntry,
       "ux25Service": ux25Service,
       "ux25Window": ux25Window,
       "ux25PktSize": ux25PktSize,
       "ufddi": ufddi,
       "ufddiSMT": ufddiSMT,
       "ufddiSMTStationIdGrp": ufddiSMTStationIdGrp,
       "ufddiSMTStationId": ufddiSMTStationId,
       "ufddiSMTStationType": ufddiSMTStationType,
       "ufddiSMTVersionId": ufddiSMTVersionId,
       "ufddiSMTStationCfgGrp": ufddiSMTStationCfgGrp,
       "ufddiSMTMACCount": ufddiSMTMACCount,
       "ufddiSMTAttachCount": ufddiSMTAttachCount,
       "ufddiSMTSpurCount": ufddiSMTSpurCount,
       "ufddiSMTOperationalGrp": ufddiSMTOperationalGrp,
       "ufddiSMTDasScmState": ufddiSMTDasScmState,
       "ufddiMACTable": ufddiMACTable,
       "ufddiMACEntry": ufddiMACEntry,
       "ufddiMACAddressGrp": ufddiMACAddressGrp,
       "ufddiMACSMTLongAddr": ufddiMACSMTLongAddr,
       "ufddiMACShortGrpAddr": ufddiMACShortGrpAddr,
       "ufddiMACCfgGrp": ufddiMACCfgGrp,
       "ufddiMACUpstreamNeighbor": ufddiMACUpstreamNeighbor,
       "ufddiMACDownstreamNeighbor": ufddiMACDownstreamNeighbor,
       "ufddiMACResourceIndex": ufddiMACResourceIndex,
       "ufddiMACConnectedResId": ufddiMACConnectedResId,
       "ufddiMACOperGrp": ufddiMACOperGrp,
       "ufddiMACTReq": ufddiMACTReq,
       "ufddiMACTMax": ufddiMACTMax,
       "ufddiMACTvxValue": ufddiMACTvxValue,
       "ufddiMACTMin": ufddiMACTMin,
       "ufddiMACCountersGrp": ufddiMACCountersGrp,
       "ufddiMACReceiveCt": ufddiMACReceiveCt,
       "ufddiMACTransmitCt": ufddiMACTransmitCt,
       "ufddiMACTokenCt": ufddiMACTokenCt,
       "ufddiMACErrorCntrsGrp": ufddiMACErrorCntrsGrp,
       "ufddiMACTvxExpiredCt": ufddiMACTvxExpiredCt,
       "ufddiMACNotCopiedCt": ufddiMACNotCopiedCt,
       "ufddiMACLateCt": ufddiMACLateCt,
       "ufddiMACReceiveOverflowCt": ufddiMACReceiveOverflowCt,
       "ufddiMACSTATUSGrp": ufddiMACSTATUSGrp,
       "ufddiMACRingOpCt": ufddiMACRingOpCt,
       "ufddiMACEnteredBeaconCt": ufddiMACEnteredBeaconCt,
       "ufddiPHYTable": ufddiPHYTable,
       "ufddiPHYEntry": ufddiPHYEntry,
       "ufddiPHYCfgGrp": ufddiPHYCfgGrp,
       "ufddiPHYType": ufddiPHYType,
       "ufddiPHYConnectState": ufddiPHYConnectState,
       "ufddiPHYRemotePHYType": ufddiPHYRemotePHYType,
       "ufddiPHYRemoteMACIndicated": ufddiPHYRemoteMACIndicated,
       "ufddiPHYResourceIndex": ufddiPHYResourceIndex,
       "ufddiPHYConnectedResId": ufddiPHYConnectedResId,
       "ufddiPHYAction": ufddiPHYAction,
       "tlip": tlip,
       "tlipLogicalDisconnect": tlipLogicalDisconnect,
       "tlipLoopback": tlipLoopback,
       "tlipRedirectTo": tlipRedirectTo,
       "tlipMasker": tlipMasker,
       "tlipWellKnownGateway": tlipWellKnownGateway,
       "tlipMaxRoutePids": tlipMaxRoutePids,
       "tlipRoutePidsTable": tlipRoutePidsTable,
       "tlipRoutePidsEntry": tlipRoutePidsEntry,
       "tlipRoutePid": tlipRoutePid,
       "tlipNbrStaticRoutes": tlipNbrStaticRoutes,
       "tlipStaticRouteTable": tlipStaticRouteTable,
       "tlipStaticRouteEntry": tlipStaticRouteEntry,
       "tlipStaticRouteNetwork": tlipStaticRouteNetwork,
       "tlipStaticRouteGateway": tlipStaticRouteGateway,
       "tlipStaticRouteCost": tlipStaticRouteCost,
       "tlipStaticRouteOverride": tlipStaticRouteOverride,
       "tlipRemotegTable": tlipRemotegTable,
       "tlipRemotegEntry": tlipRemotegEntry,
       "tlipRemoteg": tlipRemoteg,
       "tlipNetMaxPktTable": tlipNetMaxPktTable,
       "tlipNetMaxPktEntry": tlipNetMaxPktEntry,
       "tlipNetMaxPkt": tlipNetMaxPkt,
       "tl1mib": tl1mib,
       "tl1system": tl1system,
       "tl1systemAction": tl1systemAction,
       "tl1systemReboots": tl1systemReboots,
       "tl1systemErrorCode": tl1systemErrorCode,
       "tl1interfaces": tl1interfaces,
       "tl1ifTable": tl1ifTable,
       "tl1ifEntry": tl1ifEntry,
       "tl1ifIpAddr": tl1ifIpAddr,
       "tl1ifSubnetMask": tl1ifSubnetMask,
       "tl1ifProxyARP": tl1ifProxyARP,
       "tl1ifType": tl1ifType,
       "tl1ifHardwareAddress": tl1ifHardwareAddress,
       "tl1at": tl1at,
       "tl1ip": tl1ip,
       "tl1ipLogicalDisconnect": tl1ipLogicalDisconnect,
       "tl1ipLoopback": tl1ipLoopback,
       "tl1ipRedirectTo": tl1ipRedirectTo,
       "tl1ipMaxRoutePids": tl1ipMaxRoutePids,
       "tl1ipRoutePidsTable": tl1ipRoutePidsTable,
       "tl1ipRoutePidsEntry": tl1ipRoutePidsEntry,
       "tl1ipRoutePid": tl1ipRoutePid,
       "tl1ipNbrStaticRoutes": tl1ipNbrStaticRoutes,
       "tl1ipStaticRouteTable": tl1ipStaticRouteTable,
       "tl1ipStaticRouteEntry": tl1ipStaticRouteEntry,
       "tl1ipStaticRouteNetwork": tl1ipStaticRouteNetwork,
       "tl1ipStaticRouteGateway": tl1ipStaticRouteGateway,
       "tl1ipStaticRouteCost": tl1ipStaticRouteCost,
       "tl1ipStaticRouteOverride": tl1ipStaticRouteOverride,
       "tl1ipStaticRouteMask": tl1ipStaticRouteMask,
       "tl1ipConfigIntfTable": tl1ipConfigIntfTable,
       "tl1ipConfigIntfEntry": tl1ipConfigIntfEntry,
       "tl1ipRemoteg": tl1ipRemoteg,
       "tl1ipNetMaxPkt": tl1ipNetMaxPkt,
       "tl1ipMasker": tl1ipMasker,
       "tl1ipNumFilters": tl1ipNumFilters,
       "tl1ipFilterTable": tl1ipFilterTable,
       "tl1ipFilterEntry": tl1ipFilterEntry,
       "tl1ipFilterSrcMask": tl1ipFilterSrcMask,
       "tl1ipFilterSrcNet": tl1ipFilterSrcNet,
       "tl1ipFilterDstMask": tl1ipFilterDstMask,
       "tl1ipFilterDstNet": tl1ipFilterDstNet,
       "tl1ipFilterNbrExceptions": tl1ipFilterNbrExceptions,
       "tl1ipFilterExceptionTable": tl1ipFilterExceptionTable,
       "tl1ipFilterExceptionEntry": tl1ipFilterExceptionEntry,
       "tl1ipFilterExceptionSrcNet": tl1ipFilterExceptionSrcNet,
       "tl1ipFilterExceptionDstNet": tl1ipFilterExceptionDstNet,
       "tl1icmp": tl1icmp,
       "tl1tcp": tl1tcp,
       "tl1tcpRetransTo": tl1tcpRetransTo,
       "tl1tcpRtoMin": tl1tcpRtoMin,
       "tl1tcpRtoMax": tl1tcpRtoMax,
       "tl1tcpWakeup": tl1tcpWakeup,
       "tl1tcpAckTime": tl1tcpAckTime,
       "tl1tcpTimeToLive": tl1tcpTimeToLive,
       "tl1tcpThruput": tl1tcpThruput,
       "tl1tcpFlowAck": tl1tcpFlowAck,
       "tl1udp": tl1udp,
       "tl1egp": tl1egp,
       "tl1egpMaxNbrs": tl1egpMaxNbrs,
       "tl1egpNumberTrustedNbrs": tl1egpNumberTrustedNbrs,
       "tl1egpNumberNbrs": tl1egpNumberNbrs,
       "tl1egpNbrTable": tl1egpNbrTable,
       "tl1egpNbrEntry": tl1egpNbrEntry,
       "tl1egpNbr": tl1egpNbr,
       "tl1egpAutoSysNumber": tl1egpAutoSysNumber,
       "tl1egpMinHelloInterval": tl1egpMinHelloInterval,
       "tl1egpMinPollInterval": tl1egpMinPollInterval,
       "tl1egpRequestCeaseInterval": tl1egpRequestCeaseInterval,
       "tl1egpDeclareDownInterval": tl1egpDeclareDownInterval,
       "tl1egpAcquireCeaseInterval": tl1egpAcquireCeaseInterval,
       "tl1egpEnoughInterval": tl1egpEnoughInterval,
       "tl1egpPurgeInterval": tl1egpPurgeInterval,
       "tl1egpMode": tl1egpMode,
       "tl1egpErrorTreatment": tl1egpErrorTreatment,
       "tl1egpSharedNetwork": tl1egpSharedNetwork,
       "tl1snmp": tl1snmp,
       "tl1snmpVersion": tl1snmpVersion,
       "tl1snmpTrapTable": tl1snmpTrapTable,
       "tl1snmpTrapEntry": tl1snmpTrapEntry,
       "tl1snmpTrapAddress": tl1snmpTrapAddress,
       "tl1snmpForwardTraps": tl1snmpForwardTraps,
       "tl1snmpLastTrapMessage": tl1snmpLastTrapMessage,
       "tl1snmpNMSTable": tl1snmpNMSTable,
       "tl1snmpNMSEntry": tl1snmpNMSEntry,
       "tl1snmpNMSAddress": tl1snmpNMSAddress,
       "tl1bre": tl1bre,
       "tl1breConfigParams": tl1breConfigParams,
       "tl1breBridgeNumber": tl1breBridgeNumber,
       "tl1breBridgeIpAddress": tl1breBridgeIpAddress,
       "tl1breForwardTableAgeingTime": tl1breForwardTableAgeingTime,
       "tl1breNumConfigBrdgLstEntries": tl1breNumConfigBrdgLstEntries,
       "tl1breConfigBridgeListTable": tl1breConfigBridgeListTable,
       "tl1breCBridgeListEntry": tl1breCBridgeListEntry,
       "tl1breCblBridgeNumber": tl1breCblBridgeNumber,
       "tl1breCblVLanId": tl1breCblVLanId,
       "tl1breCblSrBridgeNumber": tl1breCblSrBridgeNumber,
       "tl1breCblIpAddress": tl1breCblIpAddress,
       "tl1breBridgeListTable": tl1breBridgeListTable,
       "tl1breBridgeListEntry": tl1breBridgeListEntry,
       "tl1breBlBridgeNumber": tl1breBlBridgeNumber,
       "tl1breBlVLanId": tl1breBlVLanId,
       "tl1breBlSrBridgeNumber": tl1breBlSrBridgeNumber,
       "tl1breBlIpAddress": tl1breBlIpAddress,
       "tl1breForwardTable": tl1breForwardTable,
       "tl1breForwardTableEntry": tl1breForwardTableEntry,
       "tl1breFtMacAddress": tl1breFtMacAddress,
       "tl1breFtIpAddress": tl1breFtIpAddress,
       "tl1breStatTable": tl1breStatTable,
       "tl1breStatEntry": tl1breStatEntry,
       "tl1breInTSFs": tl1breInTSFs,
       "tl1breInSRFs": tl1breInSRFs,
       "tl1breInEFs": tl1breInEFs,
       "tl1breInBPDUs": tl1breInBPDUs,
       "tl1breInErrors": tl1breInErrors,
       "tl1breOutTSFs": tl1breOutTSFs,
       "tl1breOutSRFs": tl1breOutSRFs,
       "tl1breOutEFs": tl1breOutEFs,
       "tl1breOutBPDUs": tl1breOutBPDUs,
       "tl1rip": tl1rip,
       "tl1ripInPkts": tl1ripInPkts,
       "tl1ripOutPkts": tl1ripOutPkts,
       "tl1ripBadSize": tl1ripBadSize,
       "tl1ripBadVersion": tl1ripBadVersion,
       "tl1ripNonZero": tl1ripNonZero,
       "tl1ripBadFamily": tl1ripBadFamily,
       "tl1ripBadPort": tl1ripBadPort,
       "tl1ripBadMetric": tl1ripBadMetric,
       "tl1ripBadAddr": tl1ripBadAddr,
       "tl1ripBadCommand": tl1ripBadCommand,
       "tl1ripBadClass": tl1ripBadClass,
       "tl1ripBadNbr": tl1ripBadNbr,
       "tl1ripOwnAddr": tl1ripOwnAddr,
       "tl1ripConfigTable": tl1ripConfigTable,
       "tl1ripConfigEntry": tl1ripConfigEntry,
       "tl1ripMode": tl1ripMode,
       "tl1ripSimple": tl1ripSimple,
       "tl1ripAdverStatic": tl1ripAdverStatic,
       "tl1ripAdverIntf": tl1ripAdverIntf,
       "tl1ripHolddown": tl1ripHolddown,
       "tl1x25": tl1x25,
       "tl1x25IfTable": tl1x25IfTable,
       "tl1x25IfEntry": tl1x25IfEntry,
       "tl1x25InPkts": tl1x25InPkts,
       "tl1x25OutPkts": tl1x25OutPkts,
       "tl1x25GFI": tl1x25GFI,
       "tl1x25PktInv": tl1x25PktInv,
       "tl1x25PinvR1": tl1x25PinvR1,
       "tl1x25PinvR2": tl1x25PinvR2,
       "tl1x25PinvR3": tl1x25PinvR3,
       "tl1x25PinvP1": tl1x25PinvP1,
       "tl1x25PinvP2": tl1x25PinvP2,
       "tl1x25PinvP3": tl1x25PinvP3,
       "tl1x25PinvP4": tl1x25PinvP4,
       "tl1x25PinvP5": tl1x25PinvP5,
       "tl1x25PinvP6": tl1x25PinvP6,
       "tl1x25PinvP7": tl1x25PinvP7,
       "tl1x25PinvD1": tl1x25PinvD1,
       "tl1x25PinvD2": tl1x25PinvD2,
       "tl1x25PinvD3": tl1x25PinvD3,
       "tl1x25PktLong": tl1x25PktLong,
       "tl1x25PktShort": tl1x25PktShort,
       "tl1x25CallingAddr": tl1x25CallingAddr,
       "tl1x25CalledAddr": tl1x25CalledAddr,
       "tl1x25CallBad": tl1x25CallBad,
       "tl1x25FacParam": tl1x25FacParam,
       "tl1x25FacCode": tl1x25FacCode,
       "tl1x25BadPkt": tl1x25BadPkt,
       "tl1x25RejInv": tl1x25RejInv,
       "tl1x25LcRestr": tl1x25LcRestr,
       "tl1x25IntrCPkt": tl1x25IntrCPkt,
       "tl1x25CallTimer": tl1x25CallTimer,
       "tl1x25ResetTimer": tl1x25ResetTimer,
       "tl1x25Service": tl1x25Service,
       "tl1x25Window": tl1x25Window,
       "tl1x25PktSize": tl1x25PktSize,
       "tl1fddi": tl1fddi,
       "tl1fddiMACStatTable": tl1fddiMACStatTable,
       "tl1fddiMACStatEntry": tl1fddiMACStatEntry,
       "tl1fddiMACRcvAbort": tl1fddiMACRcvAbort,
       "tl1fddiMACRcvOverflow": tl1fddiMACRcvOverflow,
       "tl1fddiMACRcvUnderflow": tl1fddiMACRcvUnderflow,
       "tl1fddiMACRbcCollision": tl1fddiMACRbcCollision,
       "tl1fddiMACTxSyncChain": tl1fddiMACTxSyncChain,
       "tl1fddiMACTxAsyncChain": tl1fddiMACTxAsyncChain,
       "tl1fddiMACTxSyncFrm": tl1fddiMACTxSyncFrm,
       "tl1fddiMACTxAsyncFrm": tl1fddiMACTxAsyncFrm,
       "tl1fddiMACTxSyncDone": tl1fddiMACTxSyncDone,
       "tl1fddiMACTxAsyncDone": tl1fddiMACTxAsyncDone,
       "tl1fddiMACTxBufEmpty": tl1fddiMACTxBufEmpty,
       "tl1fddiMACTxAbort": tl1fddiMACTxAbort,
       "tl1fddiMACRxFrmsRcvd": tl1fddiMACRxFrmsRcvd,
       "tl1fddiMACRxSmallGap": tl1fddiMACRxSmallGap,
       "tl1fddiMACDpcCollision": tl1fddiMACDpcCollision,
       "tl1fddiMACBadSyncPtr": tl1fddiMACBadSyncPtr,
       "tl1fddiMACBadAsyncPtr": tl1fddiMACBadAsyncPtr,
       "tl1fddiMACOtherBecRcvd": tl1fddiMACOtherBecRcvd,
       "tl1fddiMACOwnBecRcvd": tl1fddiMACOwnBecRcvd,
       "tl1fddiMACHighClmRcvd": tl1fddiMACHighClmRcvd,
       "tl1fddiMACLowClmRcvd": tl1fddiMACLowClmRcvd,
       "tl1fddiMACWonClaimBid": tl1fddiMACWonClaimBid,
       "tl1fddiMACPktsDetected": tl1fddiMACPktsDetected,
       "tl1fddiMACTokenCt": tl1fddiMACTokenCt,
       "tl1fddiMACLateCt": tl1fddiMACLateCt,
       "tl1fddiMACTvxExpiredCt": tl1fddiMACTvxExpiredCt,
       "tl1fddiMACEnterBeacontCt": tl1fddiMACEnterBeacontCt,
       "tl1fddiMACEnterClaimCt": tl1fddiMACEnterClaimCt,
       "tl1fddiMACMultiTokens": tl1fddiMACMultiTokens,
       "tl1fddiMACNotCopiedCt": tl1fddiMACNotCopiedCt,
       "tl1fddiMACDuplicateAddr": tl1fddiMACDuplicateAddr,
       "tl1fddiMACRingOpCt": tl1fddiMACRingOpCt,
       "tl1fddiMACFrameCt": tl1fddiMACFrameCt,
       "tl1fddiMACLostCt": tl1fddiMACLostCt,
       "tl1fddiMACErrorCt": tl1fddiMACErrorCt,
       "tl1fddiMACOutOfBuf": tl1fddiMACOutOfBuf,
       "tl1fddiMACReceiveCt": tl1fddiMACReceiveCt,
       "tl1fddiMACTransmitCt": tl1fddiMACTransmitCt,
       "tl1fddiMACInternalErrorCt": tl1fddiMACInternalErrorCt,
       "tl1fddiMACTneg": tl1fddiMACTneg,
       "tl1fddiSMTStnStateTable": tl1fddiSMTStnStateTable,
       "tl1fddiSMTStnStateEntry": tl1fddiSMTStnStateEntry,
       "tl1fddiSMTStnType": tl1fddiSMTStnType,
       "tl1fddiSMTVersionId": tl1fddiSMTVersionId,
       "tl1fddiSMTMACCount": tl1fddiSMTMACCount,
       "tl1fddiSMTAttachCount": tl1fddiSMTAttachCount,
       "tl1fddiSMTMasterCount": tl1fddiSMTMasterCount,
       "tl1fddiSMTDasScmState": tl1fddiSMTDasScmState,
       "tl1fddiSMTStnId": tl1fddiSMTStnId,
       "tl1fddiPHYStateTable": tl1fddiPHYStateTable,
       "tl1fddiPHYStateEntry": tl1fddiPHYStateEntry,
       "tl1fddiPHYType": tl1fddiPHYType,
       "tl1fddiPHYConnectState": tl1fddiPHYConnectState,
       "tl1fddiPHYRemotePHYType": tl1fddiPHYRemotePHYType,
       "tl1fddiPHYRemoteMACIndicated": tl1fddiPHYRemoteMACIndicated,
       "tl1fddiPHYResourceIndex": tl1fddiPHYResourceIndex,
       "tl1fddiPHYConnectedResId": tl1fddiPHYConnectedResId,
       "tl1fddiSMTOperationalTable": tl1fddiSMTOperationalTable,
       "tl1fddiSMTOperationalEntry": tl1fddiSMTOperationalEntry,
       "tl1fddiSMTLinkErrorRateCutoff": tl1fddiSMTLinkErrorRateCutoff,
       "tl1fddiSMTLinkErrorRateAlarm": tl1fddiSMTLinkErrorRateAlarm,
       "tl1fddiSMTByPassSwitchPresent": tl1fddiSMTByPassSwitchPresent,
       "tl1fddiSMTAttachConfiguration": tl1fddiSMTAttachConfiguration,
       "tl1fddiMACOperationalTable": tl1fddiMACOperationalTable,
       "tl1fddiMACOperationalEntry": tl1fddiMACOperationalEntry,
       "tl1fddiMACTReq": tl1fddiMACTReq,
       "tl1fddiMACTMax": tl1fddiMACTMax,
       "tl1fddiMACTvxValue": tl1fddiMACTvxValue,
       "tl1fddiMACTMin": tl1fddiMACTMin,
       "tl1fddiMACRcvThrot": tl1fddiMACRcvThrot,
       "tl1fddiPHYOperationalTable": tl1fddiPHYOperationalTable,
       "tl1fddiPHYOperationalEntry": tl1fddiPHYOperationalEntry,
       "tl1fddiPHYAction": tl1fddiPHYAction,
       "tl1fddiSMTNeighborTable": tl1fddiSMTNeighborTable,
       "tl1fddiSMTNeighborEntry": tl1fddiSMTNeighborEntry,
       "tl1fddiSMTStnUpstreamNbr": tl1fddiSMTStnUpstreamNbr,
       "tl1fddiSMTStnDownstreamNbr": tl1fddiSMTStnDownstreamNbr,
       "tl1stap": tl1stap,
       "tl1stapBridgeConfig": tl1stapBridgeConfig,
       "tl1stapSpanningTreeEnabled": tl1stapSpanningTreeEnabled,
       "tl1stapCMaxBridgeTransDelay": tl1stapCMaxBridgeTransDelay,
       "tl1stapCMaxBpduTransDelay": tl1stapCMaxBpduTransDelay,
       "tl1stapCBridgeHelloTime": tl1stapCBridgeHelloTime,
       "tl1stapCBridgeMaxAge": tl1stapCBridgeMaxAge,
       "tl1stapCForwardDelay": tl1stapCForwardDelay,
       "tl1stapCBridgePriority": tl1stapCBridgePriority,
       "tl1stapPortConfigTable": tl1stapPortConfigTable,
       "tl1stapPortConfigEntry": tl1stapPortConfigEntry,
       "tl1stapCPortState": tl1stapCPortState,
       "tl1stapCPortPriority": tl1stapCPortPriority,
       "tl1stapCPathCost": tl1stapCPathCost,
       "tl1stapBridgeState": tl1stapBridgeState,
       "tl1stapBridgeIdentifier": tl1stapBridgeIdentifier,
       "tl1stapTimeSinceTopChange": tl1stapTimeSinceTopChange,
       "tl1stapTopologyChangeCount": tl1stapTopologyChangeCount,
       "tl1stapTopologyChange": tl1stapTopologyChange,
       "tl1stapDesignatedRoot": tl1stapDesignatedRoot,
       "tl1stapRootPathCost": tl1stapRootPathCost,
       "tl1stapRootPort": tl1stapRootPort,
       "tl1stapMaxAge": tl1stapMaxAge,
       "tl1stapHelloTime": tl1stapHelloTime,
       "tl1stapForwardDelay": tl1stapForwardDelay,
       "tl1stapBridgeMaxAge": tl1stapBridgeMaxAge,
       "tl1stapBridgeHelloTime": tl1stapBridgeHelloTime,
       "tl1stapBridgeForwardDelay": tl1stapBridgeForwardDelay,
       "tl1stapHoldTime": tl1stapHoldTime,
       "tl1stapPortStateTable": tl1stapPortStateTable,
       "tl1stapPortStateEntry": tl1stapPortStateEntry,
       "tl1stapPortIdentifier": tl1stapPortIdentifier,
       "tl1stapPortState": tl1stapPortState,
       "tl1stapPathCost": tl1stapPathCost,
       "tl1stapPDesignatedRoot": tl1stapPDesignatedRoot,
       "tl1stapPDesignatedCost": tl1stapPDesignatedCost,
       "tl1stapPDesignatedBridge": tl1stapPDesignatedBridge,
       "tl1stapPDesignatedPort": tl1stapPDesignatedPort,
       "tl1stapPTopologyChangeAck": tl1stapPTopologyChangeAck,
       "tl1stapPConfigPending": tl1stapPConfigPending,
       "tl1idp": tl1idp,
       "tl1idpInterfaceTable": tl1idpInterfaceTable,
       "tl1idpInterfaceEntry": tl1idpInterfaceEntry,
       "tl1idpRouteSupplier": tl1idpRouteSupplier,
       "tl1idpGenChecksum": tl1idpGenChecksum,
       "tl1idpBroadcastInterval": tl1idpBroadcastInterval,
       "tl1idpRouteTimeout": tl1idpRouteTimeout,
       "tl1idpWellKnownGatewayNet": tl1idpWellKnownGatewayNet,
       "tl1idpWellKnownGatewayHost": tl1idpWellKnownGatewayHost,
       "tl1idpNbrStaticRoutes": tl1idpNbrStaticRoutes,
       "tl1idpStaticRouteTable": tl1idpStaticRouteTable,
       "tl1idpStaticRouteEntry": tl1idpStaticRouteEntry,
       "tl1idpStaticRouteNetwork": tl1idpStaticRouteNetwork,
       "tl1idpStaticRouteGatewayNet": tl1idpStaticRouteGatewayNet,
       "tl1idpStaticRouteGatewayHost": tl1idpStaticRouteGatewayHost,
       "tl1idpStaticRouteCost": tl1idpStaticRouteCost,
       "tl1idpStaticRouteOverride": tl1idpStaticRouteOverride,
       "tl1idpNbrFilters": tl1idpNbrFilters,
       "tl1idpFilterTable": tl1idpFilterTable,
       "tl1idpFilterEntry": tl1idpFilterEntry,
       "tl1idpFilterSourceMask": tl1idpFilterSourceMask,
       "tl1idpFilterSourceNet": tl1idpFilterSourceNet,
       "tl1idpFilterSourceHost": tl1idpFilterSourceHost,
       "tl1idpFilterDestinationMask": tl1idpFilterDestinationMask,
       "tl1idpFilterDestinationNet": tl1idpFilterDestinationNet,
       "tl1idpFilterDestinationHost": tl1idpFilterDestinationHost,
       "tl1idpFilterNbrExceptions": tl1idpFilterNbrExceptions,
       "tl1idpFilterExceptionTable": tl1idpFilterExceptionTable,
       "tl1idpFilterExceptionEntry": tl1idpFilterExceptionEntry,
       "tl1idpFilterExceptionSrcNet": tl1idpFilterExceptionSrcNet,
       "tl1idpFilterExceptionSrcHost": tl1idpFilterExceptionSrcHost,
       "tl1idpFilterExceptionDstNet": tl1idpFilterExceptionDstNet,
       "tl1idpFilterExceptionDstHost": tl1idpFilterExceptionDstHost,
       "tl1idpForwarding": tl1idpForwarding,
       "tl1idpInReceives": tl1idpInReceives,
       "tl1idpInHdrErrors": tl1idpInHdrErrors,
       "tl1idpForwDatagrams": tl1idpForwDatagrams,
       "tl1idpOutNoRoutes": tl1idpOutNoRoutes,
       "tl1idpNumStatic": tl1idpNumStatic,
       "tl1idpBadSize": tl1idpBadSize,
       "tl1idpInMsgs": tl1idpInMsgs,
       "tl1idpErrInEchos": tl1idpErrInEchos,
       "tl1idpInEchos": tl1idpInEchos,
       "tl1idpInEchoReply": tl1idpInEchoReply,
       "tl1idpOutEchoReps": tl1idpOutEchoReps,
       "tl1idpErrInUnspecified": tl1idpErrInUnspecified,
       "tl1idpErrInChecksum": tl1idpErrInChecksum,
       "tl1idpErrInSocket": tl1idpErrInSocket,
       "tl1idpErrInResources": tl1idpErrInResources,
       "tl1idpErrInNohost": tl1idpErrInNohost,
       "tl1idpErrInMaxhops": tl1idpErrInMaxhops,
       "tl1idpErrInSizetoobig": tl1idpErrInSizetoobig,
       "tl1idpErrInErrors": tl1idpErrInErrors,
       "tl1idpInErrors": tl1idpInErrors,
       "tl1idpErrOutMsgs": tl1idpErrOutMsgs,
       "tl1idpErrOutErrors": tl1idpErrOutErrors,
       "tl1idpErrOutUnspecified": tl1idpErrOutUnspecified,
       "tl1idpErrOutChecksum": tl1idpErrOutChecksum,
       "tl1idpErrOutSocket": tl1idpErrOutSocket,
       "tl1idpErrOutResources": tl1idpErrOutResources,
       "tl1idpErrOutNohost": tl1idpErrOutNohost,
       "tl1idpErrOutMaxhops": tl1idpErrOutMaxhops,
       "tl1idpErrOutSizetoobig": tl1idpErrOutSizetoobig,
       "tl1idpInOwnAddr": tl1idpInOwnAddr,
       "tl1idpInNoRoutes": tl1idpInNoRoutes,
       "tl1idpFilter": tl1idpFilter,
       "tl1idpHashHit": tl1idpHashHit,
       "tl1idpHashMiss": tl1idpHashMiss,
       "tl1idpBadMetric": tl1idpBadMetric,
       "tl1idpBadAlloc": tl1idpBadAlloc,
       "tl1idpBadNbr": tl1idpBadNbr,
       "tl1idpBadCommand": tl1idpBadCommand,
       "tl1idpBadAddr": tl1idpBadAddr,
       "tl1idpNetworkIntfTable": tl1idpNetworkIntfTable,
       "tl1idpNetworkIntfEntry": tl1idpNetworkIntfEntry,
       "tl1idpNetworkMaximumPacket": tl1idpNetworkMaximumPacket,
       "tl1idpNetworkAddress": tl1idpNetworkAddress,
       "tl1ppp": tl1ppp,
       "tl1pppInfoTable": tl1pppInfoTable,
       "tl1pppInfoEntry": tl1pppInfoEntry,
       "tl1pppLcpAO": tl1pppLcpAO,
       "tl1pppIpcpAO": tl1pppIpcpAO,
       "tl1pppIdpcpAO": tl1pppIdpcpAO,
       "tl1pppIpxcpAO": tl1pppIpxcpAO,
       "tl1pppLqdTimeout": tl1pppLqdTimeout,
       "tl1pppPhaseTable": tl1pppPhaseTable,
       "tl1pppPhaseEntry": tl1pppPhaseEntry,
       "tl1pppCrCount": tl1pppCrCount,
       "tl1pppTrCount": tl1pppTrCount,
       "tl1pppCtTimeout": tl1pppCtTimeout,
       "tl1pppRsTimeout": tl1pppRsTimeout,
       "tl1pppStatTable": tl1pppStatTable,
       "tl1pppStatEntry": tl1pppStatEntry,
       "tl1pppBadProtocol": tl1pppBadProtocol,
       "tl1pppBadAddress": tl1pppBadAddress,
       "tl1pppBadLcp": tl1pppBadLcp,
       "tl1pppBadIpcp": tl1pppBadIpcp,
       "tl1pppBadIdpcp": tl1pppBadIdpcp,
       "tl1pppBadIpxcp": tl1pppBadIpxcp,
       "tl1pppNumCrSent": tl1pppNumCrSent,
       "tl1pppNumCrRecd": tl1pppNumCrRecd,
       "tl1pppNumTrRecd": tl1pppNumTrRecd,
       "tl1srtb": tl1srtb,
       "tl1srtbInternalLanEnabled": tl1srtbInternalLanEnabled,
       "tl1srtbInternalLanId": tl1srtbInternalLanId,
       "tl1srtbUpTime": tl1srtbUpTime,
       "tl1srtbPortParamsTable": tl1srtbPortParamsTable,
       "tl1srtbPortParamsEntry": tl1srtbPortParamsEntry,
       "tl1srtbBridgeNumber": tl1srtbBridgeNumber,
       "tl1srtbRoutingType": tl1srtbRoutingType,
       "tl1srtbLanId": tl1srtbLanId,
       "tl1srtbIsVLan": tl1srtbIsVLan,
       "tl1srtbRdLimit": tl1srtbRdLimit,
       "tl1srtbOutUserPriority": tl1srtbOutUserPriority,
       "tl1srtbOutAccessPriority": tl1srtbOutAccessPriority,
       "tl1srtbPortCounterTable": tl1srtbPortCounterTable,
       "tl1srtbPortCounterEntry": tl1srtbPortCounterEntry,
       "tl1srtbInTSFramesReceived": tl1srtbInTSFramesReceived,
       "tl1srtbInTSFramesDiscarded": tl1srtbInTSFramesDiscarded,
       "tl1srtbOutTSFramesFrwd": tl1srtbOutTSFramesFrwd,
       "tl1srtbDiscardBuffers": tl1srtbDiscardBuffers,
       "tl1srtbDiscardTransitDelay": tl1srtbDiscardTransitDelay,
       "tl1srtbDiscardOnError": tl1srtbDiscardOnError,
       "tl1srtbInvalidRi": tl1srtbInvalidRi,
       "tl1srtbLanIdMismatch": tl1srtbLanIdMismatch,
       "tl1srtbDupLanIdOrTreeError": tl1srtbDupLanIdOrTreeError,
       "tl1srtbDiscardHopCountExcd": tl1srtbDiscardHopCountExcd,
       "tl1srtbExplorerFramesFrwd": tl1srtbExplorerFramesFrwd,
       "tl1srtbExplorerOctetsFrwd": tl1srtbExplorerOctetsFrwd,
       "tl1srtbNonExplorFramesFrwd": tl1srtbNonExplorFramesFrwd,
       "tl1srtbNonExplorOctetsFrwd": tl1srtbNonExplorOctetsFrwd,
       "tl1srtbTotalSRFrwd": tl1srtbTotalSRFrwd,
       "tl1srtbValidSRFramesReceived": tl1srtbValidSRFramesReceived,
       "tl1srtbValidExplorOctetsRcvd": tl1srtbValidExplorOctetsRcvd,
       "tl1srtbValidSRDiscarded": tl1srtbValidSRDiscarded,
       "tl1srtbTotalSRDiscarded": tl1srtbTotalSRDiscarded,
       "tl1srtbFilterDbParams": tl1srtbFilterDbParams,
       "tl1srtbFilterDbSize": tl1srtbFilterDbSize,
       "tl1srtbPermDbSize": tl1srtbPermDbSize,
       "tl1srtbNumDynamicEntries": tl1srtbNumDynamicEntries,
       "tl1srtbFilterDbAgeingTime": tl1srtbFilterDbAgeingTime,
       "tl1srtbDynamicFilterDbTable": tl1srtbDynamicFilterDbTable,
       "tl1srtbDynamicFilterDbEntry": tl1srtbDynamicFilterDbEntry,
       "tl1srtbDynamicMacAddr": tl1srtbDynamicMacAddr,
       "tl1srtbDynamicPortNumber": tl1srtbDynamicPortNumber,
       "tl1srtbStaticFilterDbParams": tl1srtbStaticFilterDbParams,
       "tl1srtbStatEntMacAddrTable": tl1srtbStatEntMacAddrTable,
       "tl1srtbStatEntMacAddrEntry": tl1srtbStatEntMacAddrEntry,
       "tl1srtbStaticEntryMacAddr": tl1srtbStaticEntryMacAddr,
       "tl1srtbStatEntPortArrayTable": tl1srtbStatEntPortArrayTable,
       "tl1srtbStatEntPortArrayEntry": tl1srtbStatEntPortArrayEntry,
       "tl1srtbStaticEntryPermit": tl1srtbStaticEntryPermit,
       "tl1srtbStatEntSizeTable": tl1srtbStatEntSizeTable,
       "tl1srtbStatEntSizeEntry": tl1srtbStatEntSizeEntry,
       "tl1srtbNumStaticEntries": tl1srtbNumStaticEntries,
       "tl1srtbNumMacAddrAcfEntrs": tl1srtbNumMacAddrAcfEntrs,
       "tl1srtbMacAddrAcfTable": tl1srtbMacAddrAcfTable,
       "tl1srtbMacAddrAcfEntry": tl1srtbMacAddrAcfEntry,
       "tl1srtbAcfSrcMacAddr": tl1srtbAcfSrcMacAddr,
       "tl1srtbAcfDestMacAddr": tl1srtbAcfDestMacAddr,
       "tl1srtbMaskAcfInfo": tl1srtbMaskAcfInfo,
       "tl1srtbMaskAcfParamsTable": tl1srtbMaskAcfParamsTable,
       "tl1srtbMaskAcfParamsEntry": tl1srtbMaskAcfParamsEntry,
       "tl1srtbNumMaskAcfEntries": tl1srtbNumMaskAcfEntries,
       "tl1srtbMaskAcfPermit": tl1srtbMaskAcfPermit,
       "tl1srtbMaskAcfTable": tl1srtbMaskAcfTable,
       "tl1srtbMaskAcfEntry": tl1srtbMaskAcfEntry,
       "tl1srtbAcfValue": tl1srtbAcfValue,
       "tl1srtbAcfMask": tl1srtbAcfMask,
       "tl1srtbAcfOffset": tl1srtbAcfOffset,
       "tl1ospf": tl1ospf,
       "tl1ospfRtrId": tl1ospfRtrId,
       "tl1ospfAreaTable": tl1ospfAreaTable,
       "tl1ospfAreaEntry": tl1ospfAreaEntry,
       "tl1ospfAreaID": tl1ospfAreaID,
       "tl1ospfAuthType": tl1ospfAuthType,
       "tl1ospfNetCount": tl1ospfNetCount,
       "tl1ospfAreaNetTable": tl1ospfAreaNetTable,
       "tl1ospfAreaNetEntry": tl1ospfAreaNetEntry,
       "tl1ospfNet": tl1ospfNet,
       "tl1ospfMask": tl1ospfMask,
       "tl1ospfVirtualIfTable": tl1ospfVirtualIfTable,
       "tl1ospfVirtualIfEntry": tl1ospfVirtualIfEntry,
       "tl1ospfNbrId": tl1ospfNbrId,
       "tl1ospfTransArea": tl1ospfTransArea,
       "tl1ospfTransDelay": tl1ospfTransDelay,
       "tl1ospfRxmtIntvl": tl1ospfRxmtIntvl,
       "tl1ospfHelloIntvl": tl1ospfHelloIntvl,
       "tl1ospfRtrDeadIntvl": tl1ospfRtrDeadIntvl,
       "tl1ospfAuthKey": tl1ospfAuthKey,
       "tl1ospfIntfTable": tl1ospfIntfTable,
       "tl1ospfIntfEntry": tl1ospfIntfEntry,
       "tl1ospfIntfRun": tl1ospfIntfRun,
       "tl1ospfIntfAreaID": tl1ospfIntfAreaID,
       "tl1ospfIntfType": tl1ospfIntfType,
       "tl1ospfIntfTransDelay": tl1ospfIntfTransDelay,
       "tl1ospfIntfRxmtIntvl": tl1ospfIntfRxmtIntvl,
       "tl1ospfIntfHelloIntvl": tl1ospfIntfHelloIntvl,
       "tl1ospfIntfRtrDeadIntvl": tl1ospfIntfRtrDeadIntvl,
       "tl1ospfIntfPriority": tl1ospfIntfPriority,
       "tl1ospfIntfAuthKey": tl1ospfIntfAuthKey,
       "tl1ospfIntfPollIntvl": tl1ospfIntfPollIntvl,
       "tl1ospfIntfPtopIntAddr": tl1ospfIntfPtopIntAddr,
       "tl1ospfNBMATable": tl1ospfNBMATable,
       "tl1ospfNBMAEntry": tl1ospfNBMAEntry,
       "tl1ospfAttRtrIpAddr": tl1ospfAttRtrIpAddr,
       "tl1ospfPriority": tl1ospfPriority,
       "tl1ospfCumlogTable": tl1ospfCumlogTable,
       "tl1ospfCumLogEntry": tl1ospfCumLogEntry,
       "tl1ospfStat": tl1ospfStat,
       "tl1ospfIntfTOSTable": tl1ospfIntfTOSTable,
       "tl1ospfIntfTOSEntry": tl1ospfIntfTOSEntry,
       "tl1ospfIfTOSCost": tl1ospfIfTOSCost,
       "tl1tok": tl1tok,
       "tl1tokConfigTable": tl1tokConfigTable,
       "tl1tokConfigEntry": tl1tokConfigEntry,
       "tl1tokEarlyTokenRelease": tl1tokEarlyTokenRelease,
       "tl1tokRingSpeed": tl1tokRingSpeed}
)
