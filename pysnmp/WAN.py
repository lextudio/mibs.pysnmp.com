# SNMP MIB module (WAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WAN
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:26 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

wan_status = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortSpeedType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fullDulplex10", 2),
          ("fullDulplex100", 4),
          ("fullDulplex1000", 6),
          ("halfDulplex10", 3),
          ("halfDulplex100", 5),
          ("halfDulplex1000", 7),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_Pepwave_ObjectIdentity = ObjectIdentity
pepwave = _Pepwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662)
)
_WanStatus_ObjectIdentity = ObjectIdentity
wanStatus = _WanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1)
)
_WanNum_Type = Integer32
_WanNum_Object = MibScalar
wanNum = _WanNum_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 1),
    _WanNum_Type()
)
wanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNum.setStatus("current")
_WanTable_Object = MibTable
wanTable = _WanTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wanTable.setStatus("current")
_WanEntry_Object = MibTableRow
wanEntry = _WanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1)
)
wanEntry.setIndexNames(
    (0, "WAN", "wanId"),
)
if mibBuilder.loadTexts:
    wanEntry.setStatus("current")
_WanId_Type = Integer32
_WanId_Object = MibTableColumn
wanId = _WanId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 1),
    _WanId_Type()
)
wanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanId.setStatus("current")


class _WanName_Type(OctetString):
    """Custom type wanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WanName_Type.__name__ = "OctetString"
_WanName_Object = MibTableColumn
wanName = _WanName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 2),
    _WanName_Type()
)
wanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanName.setStatus("current")


class _WanState_Type(Integer32):
    """Custom type wanState based on Integer32"""
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
        *(("activating", 5),
          ("connected", 3),
          ("connecting", 4),
          ("disabled", 1),
          ("disconnected", 2),
          ("disconnected-manually", 7),
          ("health-check-fail", 6),
          ("unknown", 0))
    )


_WanState_Type.__name__ = "Integer32"
_WanState_Object = MibTableColumn
wanState = _WanState_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 3),
    _WanState_Type()
)
wanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanState.setStatus("current")


class _WanHealthCheckState_Type(Integer32):
    """Custom type wanHealthCheckState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("success", 1))
    )


_WanHealthCheckState_Type.__name__ = "Integer32"
_WanHealthCheckState_Object = MibTableColumn
wanHealthCheckState = _WanHealthCheckState_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 4),
    _WanHealthCheckState_Type()
)
wanHealthCheckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanHealthCheckState.setStatus("current")
_WanSignal_Type = Integer32
_WanSignal_Object = MibTableColumn
wanSignal = _WanSignal_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 5),
    _WanSignal_Type()
)
wanSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanSignal.setStatus("current")
_WanCellID_Type = OctetString
_WanCellID_Object = MibTableColumn
wanCellID = _WanCellID_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 6),
    _WanCellID_Type()
)
wanCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanCellID.setStatus("current")


class _WanPdpConnection_Type(Integer32):
    """Custom type wanPdpConnection based on Integer32"""
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
        *(("pdp-ip", 1),
          ("pdp-ipv4v6", 4),
          ("pdp-ipv6", 3),
          ("pdp-ppp", 2),
          ("unknown", 0))
    )


_WanPdpConnection_Type.__name__ = "Integer32"
_WanPdpConnection_Object = MibTableColumn
wanPdpConnection = _WanPdpConnection_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 2, 1, 7),
    _WanPdpConnection_Type()
)
wanPdpConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanPdpConnection.setStatus("current")
_WanNetwork_ObjectIdentity = ObjectIdentity
wanNetwork = _WanNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3)
)
_WanNetworkIpTable_Object = MibTable
wanNetworkIpTable = _WanNetworkIpTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wanNetworkIpTable.setStatus("current")
_WanNetworkIpEntry_Object = MibTableRow
wanNetworkIpEntry = _WanNetworkIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1)
)
wanNetworkIpEntry.setIndexNames(
    (0, "WAN", "wanId"),
    (0, "WAN", "wanNetworkIpId"),
)
if mibBuilder.loadTexts:
    wanNetworkIpEntry.setStatus("current")
_WanNetworkIpId_Type = Integer32
_WanNetworkIpId_Object = MibTableColumn
wanNetworkIpId = _WanNetworkIpId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1, 1),
    _WanNetworkIpId_Type()
)
wanNetworkIpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNetworkIpId.setStatus("current")


class _WanNetworkIpType_Type(Integer32):
    """Custom type wanNetworkIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 0),
          ("pppoe", 2),
          ("static", 1))
    )


_WanNetworkIpType_Type.__name__ = "Integer32"
_WanNetworkIpType_Object = MibTableColumn
wanNetworkIpType = _WanNetworkIpType_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1, 2),
    _WanNetworkIpType_Type()
)
wanNetworkIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNetworkIpType.setStatus("current")
_WanNetworkIpAddress_Type = IpAddress
_WanNetworkIpAddress_Object = MibTableColumn
wanNetworkIpAddress = _WanNetworkIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1, 3),
    _WanNetworkIpAddress_Type()
)
wanNetworkIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNetworkIpAddress.setStatus("current")
_WanNetworkSubnetMask_Type = IpAddress
_WanNetworkSubnetMask_Object = MibTableColumn
wanNetworkSubnetMask = _WanNetworkSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 1, 1, 4),
    _WanNetworkSubnetMask_Type()
)
wanNetworkSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNetworkSubnetMask.setStatus("current")
_WanNetworkDnsTable_Object = MibTable
wanNetworkDnsTable = _WanNetworkDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wanNetworkDnsTable.setStatus("current")
_WanNetworkDnsEntry_Object = MibTableRow
wanNetworkDnsEntry = _WanNetworkDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 2, 1)
)
wanNetworkDnsEntry.setIndexNames(
    (0, "WAN", "wanId"),
    (0, "WAN", "wanNetworkDnsId"),
)
if mibBuilder.loadTexts:
    wanNetworkDnsEntry.setStatus("current")
_WanNetworkDnsId_Type = Integer32
_WanNetworkDnsId_Object = MibTableColumn
wanNetworkDnsId = _WanNetworkDnsId_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 2, 1, 1),
    _WanNetworkDnsId_Type()
)
wanNetworkDnsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNetworkDnsId.setStatus("current")
_WanNetworkDnsServer_Type = IpAddress
_WanNetworkDnsServer_Object = MibTableColumn
wanNetworkDnsServer = _WanNetworkDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 2, 1, 2),
    _WanNetworkDnsServer_Type()
)
wanNetworkDnsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNetworkDnsServer.setStatus("current")
_WanNetworkTable_Object = MibTable
wanNetworkTable = _WanNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wanNetworkTable.setStatus("current")
_WanNetworkEntry_Object = MibTableRow
wanNetworkEntry = _WanNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 3, 1)
)
wanNetworkEntry.setIndexNames(
    (0, "WAN", "wanId"),
)
if mibBuilder.loadTexts:
    wanNetworkEntry.setStatus("current")
_WanNetworkGateway_Type = IpAddress
_WanNetworkGateway_Object = MibTableColumn
wanNetworkGateway = _WanNetworkGateway_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 3, 3, 1, 1),
    _WanNetworkGateway_Type()
)
wanNetworkGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanNetworkGateway.setStatus("current")
_WanDataUsageTable_Object = MibTable
wanDataUsageTable = _WanDataUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 4)
)
if mibBuilder.loadTexts:
    wanDataUsageTable.setStatus("current")
_WanDataUsageEntry_Object = MibTableRow
wanDataUsageEntry = _WanDataUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 4, 1)
)
wanDataUsageEntry.setIndexNames(
    (0, "WAN", "wanId"),
    (0, "WAN", "dataTypeID"),
)
if mibBuilder.loadTexts:
    wanDataUsageEntry.setStatus("current")


class _DataTypeID_Type(Integer32):
    """Custom type dataTypeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("daily", 0),
          ("monthly", 1))
    )


_DataTypeID_Type.__name__ = "Integer32"
_DataTypeID_Object = MibTableColumn
dataTypeID = _DataTypeID_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 4, 1, 1),
    _DataTypeID_Type()
)
dataTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataTypeID.setStatus("current")
_WanDataUsageTxByte_Type = Counter64
_WanDataUsageTxByte_Object = MibTableColumn
wanDataUsageTxByte = _WanDataUsageTxByte_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 4, 1, 2),
    _WanDataUsageTxByte_Type()
)
wanDataUsageTxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDataUsageTxByte.setStatus("current")
if mibBuilder.loadTexts:
    wanDataUsageTxByte.setUnits("MB")
_WanDataUsageRxByte_Type = Counter64
_WanDataUsageRxByte_Object = MibTableColumn
wanDataUsageRxByte = _WanDataUsageRxByte_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 4, 1, 3),
    _WanDataUsageRxByte_Type()
)
wanDataUsageRxByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDataUsageRxByte.setStatus("current")
if mibBuilder.loadTexts:
    wanDataUsageRxByte.setUnits("MB")
_PortWanSpeedTable_Object = MibTable
portWanSpeedTable = _PortWanSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 5)
)
if mibBuilder.loadTexts:
    portWanSpeedTable.setStatus("current")
_PortWanSpeedEntry_Object = MibTableRow
portWanSpeedEntry = _PortWanSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 5, 1)
)
portWanSpeedEntry.setIndexNames(
    (0, "WAN", "portWanSpeedIndex"),
)
if mibBuilder.loadTexts:
    portWanSpeedEntry.setStatus("current")
_PortWanSpeedIndex_Type = Integer32
_PortWanSpeedIndex_Object = MibTableColumn
portWanSpeedIndex = _PortWanSpeedIndex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 5, 1, 1),
    _PortWanSpeedIndex_Type()
)
portWanSpeedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portWanSpeedIndex.setStatus("current")
_PortWanSpeed_Type = PortSpeedType
_PortWanSpeed_Object = MibTableColumn
portWanSpeed = _PortWanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27662, 2, 1, 5, 1, 2),
    _PortWanSpeed_Type()
)
portWanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portWanSpeed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAN",
    **{"PortSpeedType": PortSpeedType,
       "pepwave": pepwave,
       "wan-status": wan_status,
       "wanStatus": wanStatus,
       "wanNum": wanNum,
       "wanTable": wanTable,
       "wanEntry": wanEntry,
       "wanId": wanId,
       "wanName": wanName,
       "wanState": wanState,
       "wanHealthCheckState": wanHealthCheckState,
       "wanSignal": wanSignal,
       "wanCellID": wanCellID,
       "wanPdpConnection": wanPdpConnection,
       "wanNetwork": wanNetwork,
       "wanNetworkIpTable": wanNetworkIpTable,
       "wanNetworkIpEntry": wanNetworkIpEntry,
       "wanNetworkIpId": wanNetworkIpId,
       "wanNetworkIpType": wanNetworkIpType,
       "wanNetworkIpAddress": wanNetworkIpAddress,
       "wanNetworkSubnetMask": wanNetworkSubnetMask,
       "wanNetworkDnsTable": wanNetworkDnsTable,
       "wanNetworkDnsEntry": wanNetworkDnsEntry,
       "wanNetworkDnsId": wanNetworkDnsId,
       "wanNetworkDnsServer": wanNetworkDnsServer,
       "wanNetworkTable": wanNetworkTable,
       "wanNetworkEntry": wanNetworkEntry,
       "wanNetworkGateway": wanNetworkGateway,
       "wanDataUsageTable": wanDataUsageTable,
       "wanDataUsageEntry": wanDataUsageEntry,
       "dataTypeID": dataTypeID,
       "wanDataUsageTxByte": wanDataUsageTxByte,
       "wanDataUsageRxByte": wanDataUsageRxByte,
       "portWanSpeedTable": portWanSpeedTable,
       "portWanSpeedEntry": portWanSpeedEntry,
       "portWanSpeedIndex": portWanSpeedIndex,
       "portWanSpeed": portWanSpeed}
)
