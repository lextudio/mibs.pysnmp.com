# SNMP MIB module (HH3C-SNA-DLSW-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SNA-DLSW-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:53 2024
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

(LFSize,
 MacAddressNC,
 TAddress,
 dlswTConnConfigEntry,
 dlswTConnOperEntry,
 dlswTConnTcpConfigEntry) = mibBuilder.importSymbols(
    "DLSW-MIB",
    "LFSize",
    "MacAddressNC",
    "TAddress",
    "dlswTConnConfigEntry",
    "dlswTConnOperEntry",
    "dlswTConnTcpConfigEntry")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cDlswExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62)
)
hh3cDlswExt.setRevisions(
        ("2005-07-20 19:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDlswExtMIBObjects_ObjectIdentity = ObjectIdentity
hh3cDlswExtMIBObjects = _Hh3cDlswExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1)
)
_Hh3cdeNode_ObjectIdentity = ObjectIdentity
hh3cdeNode = _Hh3cdeNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1)
)


class _Hh3cdeNodeVendorID_Type(OctetString):
    """Custom type hh3cdeNodeVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hh3cdeNodeVendorID_Type.__name__ = "OctetString"
_Hh3cdeNodeVendorID_Object = MibScalar
hh3cdeNodeVendorID = _Hh3cdeNodeVendorID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 1),
    _Hh3cdeNodeVendorID_Type()
)
hh3cdeNodeVendorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeVendorID.setStatus("current")
_Hh3cdeNodeIpAddrType_Type = InetAddressType
_Hh3cdeNodeIpAddrType_Object = MibScalar
hh3cdeNodeIpAddrType = _Hh3cdeNodeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 2),
    _Hh3cdeNodeIpAddrType_Type()
)
hh3cdeNodeIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeIpAddrType.setStatus("current")


class _Hh3cdeNodeLocalAddr_Type(InetAddress):
    """Custom type hh3cdeNodeLocalAddr based on InetAddress"""
    defaultHexValue = ""


_Hh3cdeNodeLocalAddr_Object = MibScalar
hh3cdeNodeLocalAddr = _Hh3cdeNodeLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 3),
    _Hh3cdeNodeLocalAddr_Type()
)
hh3cdeNodeLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeLocalAddr.setStatus("current")


class _Hh3cdeNodePriority_Type(Integer32):
    """Custom type hh3cdeNodePriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cdeNodePriority_Type.__name__ = "Integer32"
_Hh3cdeNodePriority_Object = MibScalar
hh3cdeNodePriority = _Hh3cdeNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 4),
    _Hh3cdeNodePriority_Type()
)
hh3cdeNodePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodePriority.setStatus("current")


class _Hh3cdeNodeInitPacingWindow_Type(Integer32):
    """Custom type hh3cdeNodeInitPacingWindow based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cdeNodeInitPacingWindow_Type.__name__ = "Integer32"
_Hh3cdeNodeInitPacingWindow_Object = MibScalar
hh3cdeNodeInitPacingWindow = _Hh3cdeNodeInitPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 5),
    _Hh3cdeNodeInitPacingWindow_Type()
)
hh3cdeNodeInitPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeInitPacingWindow.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeNodeInitPacingWindow.setUnits("packets")


class _Hh3cdeNodeMaxPacingWindow_Type(Integer32):
    """Custom type hh3cdeNodeMaxPacingWindow based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cdeNodeMaxPacingWindow_Type.__name__ = "Integer32"
_Hh3cdeNodeMaxPacingWindow_Object = MibScalar
hh3cdeNodeMaxPacingWindow = _Hh3cdeNodeMaxPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 6),
    _Hh3cdeNodeMaxPacingWindow_Type()
)
hh3cdeNodeMaxPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeMaxPacingWindow.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeNodeMaxPacingWindow.setUnits("packets")


class _Hh3cdeNodeKeepAliveInterval_Type(Integer32):
    """Custom type hh3cdeNodeKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cdeNodeKeepAliveInterval_Type.__name__ = "Integer32"
_Hh3cdeNodeKeepAliveInterval_Object = MibScalar
hh3cdeNodeKeepAliveInterval = _Hh3cdeNodeKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 7),
    _Hh3cdeNodeKeepAliveInterval_Type()
)
hh3cdeNodeKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeNodeKeepAliveInterval.setUnits("seconds")


class _Hh3cdeNodePermitDynamic_Type(Integer32):
    """Custom type hh3cdeNodePermitDynamic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("forbidDynamic", 2),
          ("permitDynamic", 1),
          ("unknown", 65535))
    )


_Hh3cdeNodePermitDynamic_Type.__name__ = "Integer32"
_Hh3cdeNodePermitDynamic_Object = MibScalar
hh3cdeNodePermitDynamic = _Hh3cdeNodePermitDynamic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 8),
    _Hh3cdeNodePermitDynamic_Type()
)
hh3cdeNodePermitDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodePermitDynamic.setStatus("current")


class _Hh3cdeNodeConnTimeout_Type(Integer32):
    """Custom type hh3cdeNodeConnTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdeNodeConnTimeout_Type.__name__ = "Integer32"
_Hh3cdeNodeConnTimeout_Object = MibScalar
hh3cdeNodeConnTimeout = _Hh3cdeNodeConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 9),
    _Hh3cdeNodeConnTimeout_Type()
)
hh3cdeNodeConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeConnTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeNodeConnTimeout.setUnits("seconds")


class _Hh3cdeNodeLocalPendTimeout_Type(Integer32):
    """Custom type hh3cdeNodeLocalPendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdeNodeLocalPendTimeout_Type.__name__ = "Integer32"
_Hh3cdeNodeLocalPendTimeout_Object = MibScalar
hh3cdeNodeLocalPendTimeout = _Hh3cdeNodeLocalPendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 10),
    _Hh3cdeNodeLocalPendTimeout_Type()
)
hh3cdeNodeLocalPendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeLocalPendTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeNodeLocalPendTimeout.setUnits("seconds")


class _Hh3cdeNodeRemotePendTimeout_Type(Integer32):
    """Custom type hh3cdeNodeRemotePendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdeNodeRemotePendTimeout_Type.__name__ = "Integer32"
_Hh3cdeNodeRemotePendTimeout_Object = MibScalar
hh3cdeNodeRemotePendTimeout = _Hh3cdeNodeRemotePendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 11),
    _Hh3cdeNodeRemotePendTimeout_Type()
)
hh3cdeNodeRemotePendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeRemotePendTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeNodeRemotePendTimeout.setUnits("seconds")


class _Hh3cdeNodeSnaCacheTimeout_Type(Integer32):
    """Custom type hh3cdeNodeSnaCacheTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdeNodeSnaCacheTimeout_Type.__name__ = "Integer32"
_Hh3cdeNodeSnaCacheTimeout_Object = MibScalar
hh3cdeNodeSnaCacheTimeout = _Hh3cdeNodeSnaCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 12),
    _Hh3cdeNodeSnaCacheTimeout_Type()
)
hh3cdeNodeSnaCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeSnaCacheTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeNodeSnaCacheTimeout.setUnits("seconds")


class _Hh3cdeNodeExplorerTimeout_Type(Integer32):
    """Custom type hh3cdeNodeExplorerTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdeNodeExplorerTimeout_Type.__name__ = "Integer32"
_Hh3cdeNodeExplorerTimeout_Object = MibScalar
hh3cdeNodeExplorerTimeout = _Hh3cdeNodeExplorerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 13),
    _Hh3cdeNodeExplorerTimeout_Type()
)
hh3cdeNodeExplorerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeExplorerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeNodeExplorerTimeout.setUnits("seconds")


class _Hh3cdeNodeExplorerWaitTimeout_Type(Integer32):
    """Custom type hh3cdeNodeExplorerWaitTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdeNodeExplorerWaitTimeout_Type.__name__ = "Integer32"
_Hh3cdeNodeExplorerWaitTimeout_Object = MibScalar
hh3cdeNodeExplorerWaitTimeout = _Hh3cdeNodeExplorerWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 14),
    _Hh3cdeNodeExplorerWaitTimeout_Type()
)
hh3cdeNodeExplorerWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeExplorerWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeNodeExplorerWaitTimeout.setUnits("seconds")


class _Hh3cdeNodeConfigSapList_Type(OctetString):
    """Custom type hh3cdeNodeConfigSapList based on OctetString"""
    defaultHexValue = "FF000000000000000000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Hh3cdeNodeConfigSapList_Type.__name__ = "OctetString"
_Hh3cdeNodeConfigSapList_Object = MibScalar
hh3cdeNodeConfigSapList = _Hh3cdeNodeConfigSapList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 15),
    _Hh3cdeNodeConfigSapList_Type()
)
hh3cdeNodeConfigSapList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeConfigSapList.setStatus("current")


class _Hh3cdeNodeMaxTransmission_Type(Integer32):
    """Custom type hh3cdeNodeMaxTransmission based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cdeNodeMaxTransmission_Type.__name__ = "Integer32"
_Hh3cdeNodeMaxTransmission_Object = MibScalar
hh3cdeNodeMaxTransmission = _Hh3cdeNodeMaxTransmission_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 16),
    _Hh3cdeNodeMaxTransmission_Type()
)
hh3cdeNodeMaxTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeMaxTransmission.setStatus("current")


class _Hh3cdeNodeMulticastStatus_Type(Integer32):
    """Custom type hh3cdeNodeMulticastStatus based on Integer32"""
    defaultValue = 2

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


_Hh3cdeNodeMulticastStatus_Type.__name__ = "Integer32"
_Hh3cdeNodeMulticastStatus_Object = MibScalar
hh3cdeNodeMulticastStatus = _Hh3cdeNodeMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 17),
    _Hh3cdeNodeMulticastStatus_Type()
)
hh3cdeNodeMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeMulticastStatus.setStatus("current")
_Hh3cdeNodeMulticastAddress_Type = InetAddress
_Hh3cdeNodeMulticastAddress_Object = MibScalar
hh3cdeNodeMulticastAddress = _Hh3cdeNodeMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 18),
    _Hh3cdeNodeMulticastAddress_Type()
)
hh3cdeNodeMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeMulticastAddress.setStatus("current")


class _Hh3cdeNodeResetTcpAll_Type(Integer32):
    """Custom type hh3cdeNodeResetTcpAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cdeNodeResetTcpAll_Type.__name__ = "Integer32"
_Hh3cdeNodeResetTcpAll_Object = MibScalar
hh3cdeNodeResetTcpAll = _Hh3cdeNodeResetTcpAll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 19),
    _Hh3cdeNodeResetTcpAll_Type()
)
hh3cdeNodeResetTcpAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeResetTcpAll.setStatus("current")


class _Hh3cdeNodeStCapTcpNum_Type(Integer32):
    """Custom type hh3cdeNodeStCapTcpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cdeNodeStCapTcpNum_Type.__name__ = "Integer32"
_Hh3cdeNodeStCapTcpNum_Object = MibScalar
hh3cdeNodeStCapTcpNum = _Hh3cdeNodeStCapTcpNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 20),
    _Hh3cdeNodeStCapTcpNum_Type()
)
hh3cdeNodeStCapTcpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeStCapTcpNum.setStatus("current")


class _Hh3cdeNodeTcpQueueMax_Type(Integer32):
    """Custom type hh3cdeNodeTcpQueueMax based on Integer32"""
    defaultValue = 200


_Hh3cdeNodeTcpQueueMax_Object = MibScalar
hh3cdeNodeTcpQueueMax = _Hh3cdeNodeTcpQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 1, 21),
    _Hh3cdeNodeTcpQueueMax_Type()
)
hh3cdeNodeTcpQueueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdeNodeTcpQueueMax.setStatus("current")
_Hh3cdeTConn_ObjectIdentity = ObjectIdentity
hh3cdeTConn = _Hh3cdeTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2)
)
_Hh3cdeTConnConfigTable_Object = MibTable
hh3cdeTConnConfigTable = _Hh3cdeTConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cdeTConnConfigTable.setStatus("current")
_Hh3cdeTConnConfigEntry_Object = MibTableRow
hh3cdeTConnConfigEntry = _Hh3cdeTConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cdeTConnConfigEntry.setStatus("current")


class _Hh3cdeTConnConfigVersion_Type(OctetString):
    """Custom type hh3cdeTConnConfigVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hh3cdeTConnConfigVersion_Type.__name__ = "OctetString"
_Hh3cdeTConnConfigVersion_Object = MibTableColumn
hh3cdeTConnConfigVersion = _Hh3cdeTConnConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 1, 1, 1),
    _Hh3cdeTConnConfigVersion_Type()
)
hh3cdeTConnConfigVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeTConnConfigVersion.setStatus("current")


class _Hh3cdeTConnConfigPriority_Type(Integer32):
    """Custom type hh3cdeTConnConfigPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Hh3cdeTConnConfigPriority_Type.__name__ = "Integer32"
_Hh3cdeTConnConfigPriority_Object = MibTableColumn
hh3cdeTConnConfigPriority = _Hh3cdeTConnConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 1, 1, 2),
    _Hh3cdeTConnConfigPriority_Type()
)
hh3cdeTConnConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeTConnConfigPriority.setStatus("current")
_Hh3cdeTConnConfigLfSize_Type = LFSize
_Hh3cdeTConnConfigLfSize_Object = MibTableColumn
hh3cdeTConnConfigLfSize = _Hh3cdeTConnConfigLfSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 1, 1, 3),
    _Hh3cdeTConnConfigLfSize_Type()
)
hh3cdeTConnConfigLfSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeTConnConfigLfSize.setStatus("current")


class _Hh3cdeTConnConfigKeepaliveIntval_Type(Integer32):
    """Custom type hh3cdeTConnConfigKeepaliveIntval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_Hh3cdeTConnConfigKeepaliveIntval_Type.__name__ = "Integer32"
_Hh3cdeTConnConfigKeepaliveIntval_Object = MibTableColumn
hh3cdeTConnConfigKeepaliveIntval = _Hh3cdeTConnConfigKeepaliveIntval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 1, 1, 4),
    _Hh3cdeTConnConfigKeepaliveIntval_Type()
)
hh3cdeTConnConfigKeepaliveIntval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeTConnConfigKeepaliveIntval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeTConnConfigKeepaliveIntval.setUnits("seconds")


class _Hh3cdeTConnConfigBackup_Type(Integer32):
    """Custom type hh3cdeTConnConfigBackup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Hh3cdeTConnConfigBackup_Type.__name__ = "Integer32"
_Hh3cdeTConnConfigBackup_Object = MibTableColumn
hh3cdeTConnConfigBackup = _Hh3cdeTConnConfigBackup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 1, 1, 5),
    _Hh3cdeTConnConfigBackup_Type()
)
hh3cdeTConnConfigBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeTConnConfigBackup.setStatus("current")
_Hh3cdeTConnConfigBackupTAddr_Type = TAddress
_Hh3cdeTConnConfigBackupTAddr_Object = MibTableColumn
hh3cdeTConnConfigBackupTAddr = _Hh3cdeTConnConfigBackupTAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 1, 1, 6),
    _Hh3cdeTConnConfigBackupTAddr_Type()
)
hh3cdeTConnConfigBackupTAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeTConnConfigBackupTAddr.setStatus("current")


class _Hh3cdeTConnConfigBackupLinger_Type(Integer32):
    """Custom type hh3cdeTConnConfigBackupLinger based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Hh3cdeTConnConfigBackupLinger_Type.__name__ = "Integer32"
_Hh3cdeTConnConfigBackupLinger_Object = MibTableColumn
hh3cdeTConnConfigBackupLinger = _Hh3cdeTConnConfigBackupLinger_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 1, 1, 7),
    _Hh3cdeTConnConfigBackupLinger_Type()
)
hh3cdeTConnConfigBackupLinger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeTConnConfigBackupLinger.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeTConnConfigBackupLinger.setUnits("minutes")
_Hh3cdeTConnOperTable_Object = MibTable
hh3cdeTConnOperTable = _Hh3cdeTConnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cdeTConnOperTable.setStatus("current")
_Hh3cdeTConnOperEntry_Object = MibTableRow
hh3cdeTConnOperEntry = _Hh3cdeTConnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cdeTConnOperEntry.setStatus("current")


class _Hh3cdeTConnOperPeerType_Type(Integer32):
    """Custom type hh3cdeTConnOperPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("learningDynamic", 2),
          ("other", 3))
    )


_Hh3cdeTConnOperPeerType_Type.__name__ = "Integer32"
_Hh3cdeTConnOperPeerType_Object = MibTableColumn
hh3cdeTConnOperPeerType = _Hh3cdeTConnOperPeerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1, 1),
    _Hh3cdeTConnOperPeerType_Type()
)
hh3cdeTConnOperPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeTConnOperPeerType.setStatus("current")
_Hh3cdeTConnOperVendorID_Type = OctetString
_Hh3cdeTConnOperVendorID_Object = MibTableColumn
hh3cdeTConnOperVendorID = _Hh3cdeTConnOperVendorID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1, 2),
    _Hh3cdeTConnOperVendorID_Type()
)
hh3cdeTConnOperVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeTConnOperVendorID.setStatus("current")
_Hh3cdeTConnOperVersionString_Type = OctetString
_Hh3cdeTConnOperVersionString_Object = MibTableColumn
hh3cdeTConnOperVersionString = _Hh3cdeTConnOperVersionString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1, 3),
    _Hh3cdeTConnOperVersionString_Type()
)
hh3cdeTConnOperVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeTConnOperVersionString.setStatus("current")
_Hh3cdeTConnOperUpTime_Type = TimeTicks
_Hh3cdeTConnOperUpTime_Object = MibTableColumn
hh3cdeTConnOperUpTime = _Hh3cdeTConnOperUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1, 4),
    _Hh3cdeTConnOperUpTime_Type()
)
hh3cdeTConnOperUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeTConnOperUpTime.setStatus("current")
_Hh3cdeTConnOperMulticastAddress_Type = TAddress
_Hh3cdeTConnOperMulticastAddress_Object = MibTableColumn
hh3cdeTConnOperMulticastAddress = _Hh3cdeTConnOperMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1, 5),
    _Hh3cdeTConnOperMulticastAddress_Type()
)
hh3cdeTConnOperMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeTConnOperMulticastAddress.setStatus("current")
_Hh3cdeTConnOperStCapTcpNumber_Type = Integer32
_Hh3cdeTConnOperStCapTcpNumber_Object = MibTableColumn
hh3cdeTConnOperStCapTcpNumber = _Hh3cdeTConnOperStCapTcpNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1, 6),
    _Hh3cdeTConnOperStCapTcpNumber_Type()
)
hh3cdeTConnOperStCapTcpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeTConnOperStCapTcpNumber.setStatus("current")
_Hh3cdeTConnOperRecvPkts_Type = Counter32
_Hh3cdeTConnOperRecvPkts_Object = MibTableColumn
hh3cdeTConnOperRecvPkts = _Hh3cdeTConnOperRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1, 7),
    _Hh3cdeTConnOperRecvPkts_Type()
)
hh3cdeTConnOperRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeTConnOperRecvPkts.setStatus("current")
_Hh3cdeTConnOperSendPkts_Type = Counter32
_Hh3cdeTConnOperSendPkts_Object = MibTableColumn
hh3cdeTConnOperSendPkts = _Hh3cdeTConnOperSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1, 8),
    _Hh3cdeTConnOperSendPkts_Type()
)
hh3cdeTConnOperSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeTConnOperSendPkts.setStatus("current")
_Hh3cdeTConnOperDropPkts_Type = Counter32
_Hh3cdeTConnOperDropPkts_Object = MibTableColumn
hh3cdeTConnOperDropPkts = _Hh3cdeTConnOperDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 2, 1, 9),
    _Hh3cdeTConnOperDropPkts_Type()
)
hh3cdeTConnOperDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeTConnOperDropPkts.setStatus("current")
_Hh3cdeTConnTcpConfigTable_Object = MibTable
hh3cdeTConnTcpConfigTable = _Hh3cdeTConnTcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cdeTConnTcpConfigTable.setStatus("current")
_Hh3cdeTConnTcpConfigEntry_Object = MibTableRow
hh3cdeTConnTcpConfigEntry = _Hh3cdeTConnTcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cdeTConnTcpConfigEntry.setStatus("current")


class _Hh3cdeTConnTcpConfigQueueMax_Type(Integer32):
    """Custom type hh3cdeTConnTcpConfigQueueMax based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 2000),
    )


_Hh3cdeTConnTcpConfigQueueMax_Type.__name__ = "Integer32"
_Hh3cdeTConnTcpConfigQueueMax_Object = MibTableColumn
hh3cdeTConnTcpConfigQueueMax = _Hh3cdeTConnTcpConfigQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 2, 3, 1, 1),
    _Hh3cdeTConnTcpConfigQueueMax_Type()
)
hh3cdeTConnTcpConfigQueueMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeTConnTcpConfigQueueMax.setStatus("current")
_Hh3cdeBridge_ObjectIdentity = ObjectIdentity
hh3cdeBridge = _Hh3cdeBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 3)
)
_Hh3cdeBridgeTable_Object = MibTable
hh3cdeBridgeTable = _Hh3cdeBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cdeBridgeTable.setStatus("current")
_Hh3cdeBridgeEntry_Object = MibTableRow
hh3cdeBridgeEntry = _Hh3cdeBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 3, 1, 1)
)
hh3cdeBridgeEntry.setIndexNames(
    (0, "HH3C-SNA-DLSW-EXT-MIB", "hh3cdeBridgeNumIndex"),
)
if mibBuilder.loadTexts:
    hh3cdeBridgeEntry.setStatus("current")


class _Hh3cdeBridgeNumIndex_Type(Integer32):
    """Custom type hh3cdeBridgeNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cdeBridgeNumIndex_Type.__name__ = "Integer32"
_Hh3cdeBridgeNumIndex_Object = MibTableColumn
hh3cdeBridgeNumIndex = _Hh3cdeBridgeNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 3, 1, 1, 1),
    _Hh3cdeBridgeNumIndex_Type()
)
hh3cdeBridgeNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cdeBridgeNumIndex.setStatus("current")
_Hh3cdeBridgeRowStatus_Type = RowStatus
_Hh3cdeBridgeRowStatus_Object = MibTableColumn
hh3cdeBridgeRowStatus = _Hh3cdeBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 3, 1, 1, 2),
    _Hh3cdeBridgeRowStatus_Type()
)
hh3cdeBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeBridgeRowStatus.setStatus("current")
_Hh3cdeBridgeIfTable_Object = MibTable
hh3cdeBridgeIfTable = _Hh3cdeBridgeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cdeBridgeIfTable.setStatus("current")
_Hh3cdeBridgeIfEntry_Object = MibTableRow
hh3cdeBridgeIfEntry = _Hh3cdeBridgeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 3, 2, 1)
)
hh3cdeBridgeIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cdeBridgeIfEntry.setStatus("current")


class _Hh3cdeBridgeIfBrgGrp_Type(Integer32):
    """Custom type hh3cdeBridgeIfBrgGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cdeBridgeIfBrgGrp_Type.__name__ = "Integer32"
_Hh3cdeBridgeIfBrgGrp_Object = MibTableColumn
hh3cdeBridgeIfBrgGrp = _Hh3cdeBridgeIfBrgGrp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 3, 2, 1, 1),
    _Hh3cdeBridgeIfBrgGrp_Type()
)
hh3cdeBridgeIfBrgGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeBridgeIfBrgGrp.setStatus("current")
_Hh3cdeBridgeIfRowStatus_Type = RowStatus
_Hh3cdeBridgeIfRowStatus_Object = MibTableColumn
hh3cdeBridgeIfRowStatus = _Hh3cdeBridgeIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 3, 2, 1, 2),
    _Hh3cdeBridgeIfRowStatus_Type()
)
hh3cdeBridgeIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeBridgeIfRowStatus.setStatus("current")
_Hh3cdeQllc_ObjectIdentity = ObjectIdentity
hh3cdeQllc = _Hh3cdeQllc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 4)
)
_Hh3cdeQllcTable_Object = MibTable
hh3cdeQllcTable = _Hh3cdeQllcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cdeQllcTable.setStatus("current")
_Hh3cdeQllcEntry_Object = MibTableRow
hh3cdeQllcEntry = _Hh3cdeQllcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 4, 1, 1)
)
hh3cdeQllcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cdeQllcEntry.setStatus("current")
_Hh3cQllcX121Address_Type = Integer32
_Hh3cQllcX121Address_Object = MibTableColumn
hh3cQllcX121Address = _Hh3cQllcX121Address_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 4, 1, 1, 1),
    _Hh3cQllcX121Address_Type()
)
hh3cQllcX121Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQllcX121Address.setStatus("current")
_Hh3cQllcLocalMac_Type = MacAddressNC
_Hh3cQllcLocalMac_Object = MibTableColumn
hh3cQllcLocalMac = _Hh3cQllcLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 4, 1, 1, 2),
    _Hh3cQllcLocalMac_Type()
)
hh3cQllcLocalMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQllcLocalMac.setStatus("current")


class _Hh3cQllcLocalSap_Type(OctetString):
    """Custom type hh3cQllcLocalSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Hh3cQllcLocalSap_Type.__name__ = "OctetString"
_Hh3cQllcLocalSap_Object = MibTableColumn
hh3cQllcLocalSap = _Hh3cQllcLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 4, 1, 1, 3),
    _Hh3cQllcLocalSap_Type()
)
hh3cQllcLocalSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQllcLocalSap.setStatus("current")


class _Hh3cQllcRemoteMac_Type(MacAddressNC):
    """Custom type hh3cQllcRemoteMac based on MacAddressNC"""
    defaultHexValue = ""


_Hh3cQllcRemoteMac_Object = MibTableColumn
hh3cQllcRemoteMac = _Hh3cQllcRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 4, 1, 1, 4),
    _Hh3cQllcRemoteMac_Type()
)
hh3cQllcRemoteMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQllcRemoteMac.setStatus("current")


class _Hh3cQllcRemoteSap_Type(OctetString):
    """Custom type hh3cQllcRemoteSap based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_Hh3cQllcRemoteSap_Type.__name__ = "OctetString"
_Hh3cQllcRemoteSap_Object = MibTableColumn
hh3cQllcRemoteSap = _Hh3cQllcRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 4, 1, 1, 5),
    _Hh3cQllcRemoteSap_Type()
)
hh3cQllcRemoteSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQllcRemoteSap.setStatus("current")
_Hh3cQllcRowStatus_Type = RowStatus
_Hh3cQllcRowStatus_Object = MibTableColumn
hh3cQllcRowStatus = _Hh3cQllcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 4, 1, 1, 6),
    _Hh3cQllcRowStatus_Type()
)
hh3cQllcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQllcRowStatus.setStatus("current")
_Hh3cdeSdlc_ObjectIdentity = ObjectIdentity
hh3cdeSdlc = _Hh3cdeSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5)
)
_Hh3cdeSdlcPortTable_Object = MibTable
hh3cdeSdlcPortTable = _Hh3cdeSdlcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cdeSdlcPortTable.setStatus("current")
_Hh3cdeSdlcPortEntry_Object = MibTableRow
hh3cdeSdlcPortEntry = _Hh3cdeSdlcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1)
)
hh3cdeSdlcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cdeSdlcPortEntry.setStatus("current")


class _Hh3cdeSdlcPortRole_Type(Integer32):
    """Custom type hh3cdeSdlcPortRole based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("norole", 3),
          ("primary", 1),
          ("seconday", 2))
    )


_Hh3cdeSdlcPortRole_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortRole_Object = MibTableColumn
hh3cdeSdlcPortRole = _Hh3cdeSdlcPortRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 1),
    _Hh3cdeSdlcPortRole_Type()
)
hh3cdeSdlcPortRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortRole.setStatus("current")


class _Hh3cdeSdlcPortSendWindow_Type(Integer32):
    """Custom type hh3cdeSdlcPortSendWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Hh3cdeSdlcPortSendWindow_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortSendWindow_Object = MibTableColumn
hh3cdeSdlcPortSendWindow = _Hh3cdeSdlcPortSendWindow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 2),
    _Hh3cdeSdlcPortSendWindow_Type()
)
hh3cdeSdlcPortSendWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortSendWindow.setStatus("current")


class _Hh3cdeSdlcPortModulo_Type(Integer32):
    """Custom type hh3cdeSdlcPortModulo based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              128)
        )
    )
    namedValues = NamedValues(
        *(("m128", 128),
          ("m8", 8))
    )


_Hh3cdeSdlcPortModulo_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortModulo_Object = MibTableColumn
hh3cdeSdlcPortModulo = _Hh3cdeSdlcPortModulo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 3),
    _Hh3cdeSdlcPortModulo_Type()
)
hh3cdeSdlcPortModulo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortModulo.setStatus("current")


class _Hh3cdeSdlcPortMaxPdu_Type(Integer32):
    """Custom type hh3cdeSdlcPortMaxPdu based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17600),
    )


_Hh3cdeSdlcPortMaxPdu_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortMaxPdu_Object = MibTableColumn
hh3cdeSdlcPortMaxPdu = _Hh3cdeSdlcPortMaxPdu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 4),
    _Hh3cdeSdlcPortMaxPdu_Type()
)
hh3cdeSdlcPortMaxPdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortMaxPdu.setStatus("current")


class _Hh3cdeSdlcPortMaxSendQueue_Type(Integer32):
    """Custom type hh3cdeSdlcPortMaxSendQueue based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_Hh3cdeSdlcPortMaxSendQueue_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortMaxSendQueue_Object = MibTableColumn
hh3cdeSdlcPortMaxSendQueue = _Hh3cdeSdlcPortMaxSendQueue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 5),
    _Hh3cdeSdlcPortMaxSendQueue_Type()
)
hh3cdeSdlcPortMaxSendQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortMaxSendQueue.setStatus("current")


class _Hh3cdeSdlcPortMaxTransmission_Type(Integer32):
    """Custom type hh3cdeSdlcPortMaxTransmission based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cdeSdlcPortMaxTransmission_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortMaxTransmission_Object = MibTableColumn
hh3cdeSdlcPortMaxTransmission = _Hh3cdeSdlcPortMaxTransmission_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 6),
    _Hh3cdeSdlcPortMaxTransmission_Type()
)
hh3cdeSdlcPortMaxTransmission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortMaxTransmission.setStatus("current")


class _Hh3cdeSdlcPortSimultaneousEnable_Type(Integer32):
    """Custom type hh3cdeSdlcPortSimultaneousEnable based on Integer32"""
    defaultValue = 1

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


_Hh3cdeSdlcPortSimultaneousEnable_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortSimultaneousEnable_Object = MibTableColumn
hh3cdeSdlcPortSimultaneousEnable = _Hh3cdeSdlcPortSimultaneousEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 7),
    _Hh3cdeSdlcPortSimultaneousEnable_Type()
)
hh3cdeSdlcPortSimultaneousEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortSimultaneousEnable.setStatus("current")


class _Hh3cdeSdlcPortTimerACK_Type(Integer32):
    """Custom type hh3cdeSdlcPortTimerACK based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdeSdlcPortTimerACK_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortTimerACK_Object = MibTableColumn
hh3cdeSdlcPortTimerACK = _Hh3cdeSdlcPortTimerACK_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 8),
    _Hh3cdeSdlcPortTimerACK_Type()
)
hh3cdeSdlcPortTimerACK.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortTimerACK.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortTimerACK.setUnits("milliseconds")


class _Hh3cdeSdlcPortTimerLifeTime_Type(Integer32):
    """Custom type hh3cdeSdlcPortTimerLifeTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdeSdlcPortTimerLifeTime_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortTimerLifeTime_Object = MibTableColumn
hh3cdeSdlcPortTimerLifeTime = _Hh3cdeSdlcPortTimerLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 9),
    _Hh3cdeSdlcPortTimerLifeTime_Type()
)
hh3cdeSdlcPortTimerLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortTimerLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortTimerLifeTime.setUnits("milliseconds")


class _Hh3cdeSdlcPortTimerPollPause_Type(Integer32):
    """Custom type hh3cdeSdlcPortTimerPollPause based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Hh3cdeSdlcPortTimerPollPause_Type.__name__ = "Integer32"
_Hh3cdeSdlcPortTimerPollPause_Object = MibTableColumn
hh3cdeSdlcPortTimerPollPause = _Hh3cdeSdlcPortTimerPollPause_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 10),
    _Hh3cdeSdlcPortTimerPollPause_Type()
)
hh3cdeSdlcPortTimerPollPause.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortTimerPollPause.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortTimerPollPause.setUnits("milliseconds")
_Hh3cdeSdlcPortRowStatus_Type = RowStatus
_Hh3cdeSdlcPortRowStatus_Object = MibTableColumn
hh3cdeSdlcPortRowStatus = _Hh3cdeSdlcPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 5, 1, 1, 11),
    _Hh3cdeSdlcPortRowStatus_Type()
)
hh3cdeSdlcPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeSdlcPortRowStatus.setStatus("current")
_Hh3cdeLlc2_ObjectIdentity = ObjectIdentity
hh3cdeLlc2 = _Hh3cdeLlc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6)
)
_Hh3cdeLlc2PortTable_Object = MibTable
hh3cdeLlc2PortTable = _Hh3cdeLlc2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTable.setStatus("current")
_Hh3cdeLlc2PortEntry_Object = MibTableRow
hh3cdeLlc2PortEntry = _Hh3cdeLlc2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1)
)
hh3cdeLlc2PortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cdeLlc2PortEntry.setStatus("current")


class _Hh3cdeLlc2PortMaxAck_Type(Integer32):
    """Custom type hh3cdeLlc2PortMaxAck based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Hh3cdeLlc2PortMaxAck_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortMaxAck_Object = MibTableColumn
hh3cdeLlc2PortMaxAck = _Hh3cdeLlc2PortMaxAck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 1),
    _Hh3cdeLlc2PortMaxAck_Type()
)
hh3cdeLlc2PortMaxAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortMaxAck.setStatus("current")


class _Hh3cdeLlc2PortMaxPdu_Type(Integer32):
    """Custom type hh3cdeLlc2PortMaxPdu based on Integer32"""
    defaultValue = 1493

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1700),
    )


_Hh3cdeLlc2PortMaxPdu_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortMaxPdu_Object = MibTableColumn
hh3cdeLlc2PortMaxPdu = _Hh3cdeLlc2PortMaxPdu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 2),
    _Hh3cdeLlc2PortMaxPdu_Type()
)
hh3cdeLlc2PortMaxPdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortMaxPdu.setStatus("current")


class _Hh3cdeLlc2PortMaxSendQueue_Type(Integer32):
    """Custom type hh3cdeLlc2PortMaxSendQueue based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_Hh3cdeLlc2PortMaxSendQueue_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortMaxSendQueue_Object = MibTableColumn
hh3cdeLlc2PortMaxSendQueue = _Hh3cdeLlc2PortMaxSendQueue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 3),
    _Hh3cdeLlc2PortMaxSendQueue_Type()
)
hh3cdeLlc2PortMaxSendQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortMaxSendQueue.setStatus("current")


class _Hh3cdeLlc2PortMaxTransmission_Type(Integer32):
    """Custom type hh3cdeLlc2PortMaxTransmission based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cdeLlc2PortMaxTransmission_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortMaxTransmission_Object = MibTableColumn
hh3cdeLlc2PortMaxTransmission = _Hh3cdeLlc2PortMaxTransmission_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 4),
    _Hh3cdeLlc2PortMaxTransmission_Type()
)
hh3cdeLlc2PortMaxTransmission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortMaxTransmission.setStatus("current")


class _Hh3cdeLlc2PortModulo_Type(Integer32):
    """Custom type hh3cdeLlc2PortModulo based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              128)
        )
    )
    namedValues = NamedValues(
        *(("m128", 128),
          ("m8", 8))
    )


_Hh3cdeLlc2PortModulo_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortModulo_Object = MibTableColumn
hh3cdeLlc2PortModulo = _Hh3cdeLlc2PortModulo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 5),
    _Hh3cdeLlc2PortModulo_Type()
)
hh3cdeLlc2PortModulo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortModulo.setStatus("current")


class _Hh3cdeLlc2PortReceiveWindow_Type(Integer32):
    """Custom type hh3cdeLlc2PortReceiveWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Hh3cdeLlc2PortReceiveWindow_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortReceiveWindow_Object = MibTableColumn
hh3cdeLlc2PortReceiveWindow = _Hh3cdeLlc2PortReceiveWindow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 6),
    _Hh3cdeLlc2PortReceiveWindow_Type()
)
hh3cdeLlc2PortReceiveWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortReceiveWindow.setStatus("current")


class _Hh3cdeLlc2PortTimerAck_Type(Integer32):
    """Custom type hh3cdeLlc2PortTimerAck based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdeLlc2PortTimerAck_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortTimerAck_Object = MibTableColumn
hh3cdeLlc2PortTimerAck = _Hh3cdeLlc2PortTimerAck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 7),
    _Hh3cdeLlc2PortTimerAck_Type()
)
hh3cdeLlc2PortTimerAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerAck.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerAck.setUnits("milliseconds")


class _Hh3cdeLlc2PortTimerAckDelay_Type(Integer32):
    """Custom type hh3cdeLlc2PortTimerAckDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdeLlc2PortTimerAckDelay_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortTimerAckDelay_Object = MibTableColumn
hh3cdeLlc2PortTimerAckDelay = _Hh3cdeLlc2PortTimerAckDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 8),
    _Hh3cdeLlc2PortTimerAckDelay_Type()
)
hh3cdeLlc2PortTimerAckDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerAckDelay.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerAckDelay.setUnits("milliseconds")


class _Hh3cdeLlc2PortTimerDetect_Type(Integer32):
    """Custom type hh3cdeLlc2PortTimerDetect based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdeLlc2PortTimerDetect_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortTimerDetect_Object = MibTableColumn
hh3cdeLlc2PortTimerDetect = _Hh3cdeLlc2PortTimerDetect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 9),
    _Hh3cdeLlc2PortTimerDetect_Type()
)
hh3cdeLlc2PortTimerDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerDetect.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerDetect.setUnits("milliseconds")


class _Hh3cdeLlc2PortTimerBusy_Type(Integer32):
    """Custom type hh3cdeLlc2PortTimerBusy based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdeLlc2PortTimerBusy_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortTimerBusy_Object = MibTableColumn
hh3cdeLlc2PortTimerBusy = _Hh3cdeLlc2PortTimerBusy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 10),
    _Hh3cdeLlc2PortTimerBusy_Type()
)
hh3cdeLlc2PortTimerBusy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerBusy.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerBusy.setUnits("milliseconds")


class _Hh3cdeLlc2PortTimerPoll_Type(Integer32):
    """Custom type hh3cdeLlc2PortTimerPoll based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdeLlc2PortTimerPoll_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortTimerPoll_Object = MibTableColumn
hh3cdeLlc2PortTimerPoll = _Hh3cdeLlc2PortTimerPoll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 11),
    _Hh3cdeLlc2PortTimerPoll_Type()
)
hh3cdeLlc2PortTimerPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerPoll.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerPoll.setUnits("milliseconds")


class _Hh3cdeLlc2PortTimerReject_Type(Integer32):
    """Custom type hh3cdeLlc2PortTimerReject based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdeLlc2PortTimerReject_Type.__name__ = "Integer32"
_Hh3cdeLlc2PortTimerReject_Object = MibTableColumn
hh3cdeLlc2PortTimerReject = _Hh3cdeLlc2PortTimerReject_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 12),
    _Hh3cdeLlc2PortTimerReject_Type()
)
hh3cdeLlc2PortTimerReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerReject.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortTimerReject.setUnits("milliseconds")
_Hh3cdeLlc2PortRowStatus_Type = RowStatus
_Hh3cdeLlc2PortRowStatus_Object = MibTableColumn
hh3cdeLlc2PortRowStatus = _Hh3cdeLlc2PortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 6, 1, 1, 13),
    _Hh3cdeLlc2PortRowStatus_Type()
)
hh3cdeLlc2PortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeLlc2PortRowStatus.setStatus("current")
_Hh3cdeReachableCache_ObjectIdentity = ObjectIdentity
hh3cdeReachableCache = _Hh3cdeReachableCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7)
)
_Hh3cdeRchCacheStat_ObjectIdentity = ObjectIdentity
hh3cdeRchCacheStat = _Hh3cdeRchCacheStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 1)
)
_Hh3cdeRchCacheMaxIndex_Type = Integer32
_Hh3cdeRchCacheMaxIndex_Object = MibScalar
hh3cdeRchCacheMaxIndex = _Hh3cdeRchCacheMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 1, 1),
    _Hh3cdeRchCacheMaxIndex_Type()
)
hh3cdeRchCacheMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeRchCacheMaxIndex.setStatus("current")
_Hh3cdeRchCacheNextIndex_Type = Integer32
_Hh3cdeRchCacheNextIndex_Object = MibScalar
hh3cdeRchCacheNextIndex = _Hh3cdeRchCacheNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 1, 2),
    _Hh3cdeRchCacheNextIndex_Type()
)
hh3cdeRchCacheNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeRchCacheNextIndex.setStatus("current")
_Hh3cdeRchCacheTable_Object = MibTable
hh3cdeRchCacheTable = _Hh3cdeRchCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 3)
)
if mibBuilder.loadTexts:
    hh3cdeRchCacheTable.setStatus("current")
_Hh3cdeRchCacheEntry_Object = MibTableRow
hh3cdeRchCacheEntry = _Hh3cdeRchCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 3, 1)
)
hh3cdeRchCacheEntry.setIndexNames(
    (0, "HH3C-SNA-DLSW-EXT-MIB", "hh3cdeRchCacheIndex"),
)
if mibBuilder.loadTexts:
    hh3cdeRchCacheEntry.setStatus("current")
_Hh3cdeRchCacheIndex_Type = Integer32
_Hh3cdeRchCacheIndex_Object = MibTableColumn
hh3cdeRchCacheIndex = _Hh3cdeRchCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 3, 1, 1),
    _Hh3cdeRchCacheIndex_Type()
)
hh3cdeRchCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cdeRchCacheIndex.setStatus("current")


class _Hh3cdeRchCacheStatus_Type(Integer32):
    """Custom type hh3cdeRchCacheStatus based on Integer32"""
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
        *(("exploring", 4),
          ("found", 1),
          ("noCacheInfo", 3),
          ("verify", 2),
          ("waiting", 5))
    )


_Hh3cdeRchCacheStatus_Type.__name__ = "Integer32"
_Hh3cdeRchCacheStatus_Object = MibTableColumn
hh3cdeRchCacheStatus = _Hh3cdeRchCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 3, 1, 2),
    _Hh3cdeRchCacheStatus_Type()
)
hh3cdeRchCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeRchCacheStatus.setStatus("current")
_Hh3cdeRchCacheRemainTime_Type = TimeTicks
_Hh3cdeRchCacheRemainTime_Object = MibTableColumn
hh3cdeRchCacheRemainTime = _Hh3cdeRchCacheRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 3, 1, 3),
    _Hh3cdeRchCacheRemainTime_Type()
)
hh3cdeRchCacheRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeRchCacheRemainTime.setStatus("current")
_Hh3cdeRchCacheMac_Type = MacAddressNC
_Hh3cdeRchCacheMac_Object = MibTableColumn
hh3cdeRchCacheMac = _Hh3cdeRchCacheMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 3, 1, 4),
    _Hh3cdeRchCacheMac_Type()
)
hh3cdeRchCacheMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeRchCacheMac.setStatus("current")
_Hh3cdeRchCacheRemoteIpAddrType_Type = InetAddressType
_Hh3cdeRchCacheRemoteIpAddrType_Object = MibTableColumn
hh3cdeRchCacheRemoteIpAddrType = _Hh3cdeRchCacheRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 3, 1, 5),
    _Hh3cdeRchCacheRemoteIpAddrType_Type()
)
hh3cdeRchCacheRemoteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeRchCacheRemoteIpAddrType.setStatus("current")
_Hh3cdeRchCacheRemoteIp_Type = InetAddress
_Hh3cdeRchCacheRemoteIp_Object = MibTableColumn
hh3cdeRchCacheRemoteIp = _Hh3cdeRchCacheRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 3, 1, 6),
    _Hh3cdeRchCacheRemoteIp_Type()
)
hh3cdeRchCacheRemoteIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeRchCacheRemoteIp.setStatus("current")
_Hh3cdeRchCacheRowStatus_Type = RowStatus
_Hh3cdeRchCacheRowStatus_Object = MibTableColumn
hh3cdeRchCacheRowStatus = _Hh3cdeRchCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 7, 3, 1, 7),
    _Hh3cdeRchCacheRowStatus_Type()
)
hh3cdeRchCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeRchCacheRowStatus.setStatus("current")
_Hh3cdeEthernetBackup_ObjectIdentity = ObjectIdentity
hh3cdeEthernetBackup = _Hh3cdeEthernetBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8)
)
_Hh3cdeEBMacMapStat_ObjectIdentity = ObjectIdentity
hh3cdeEBMacMapStat = _Hh3cdeEBMacMapStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 1)
)
_Hh3cdeEBMacMapMaxIndex_Type = Integer32
_Hh3cdeEBMacMapMaxIndex_Object = MibScalar
hh3cdeEBMacMapMaxIndex = _Hh3cdeEBMacMapMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 1, 1),
    _Hh3cdeEBMacMapMaxIndex_Type()
)
hh3cdeEBMacMapMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeEBMacMapMaxIndex.setStatus("current")
_Hh3cdeEBMacMapNextIndex_Type = Integer32
_Hh3cdeEBMacMapNextIndex_Object = MibScalar
hh3cdeEBMacMapNextIndex = _Hh3cdeEBMacMapNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 1, 2),
    _Hh3cdeEBMacMapNextIndex_Type()
)
hh3cdeEBMacMapNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdeEBMacMapNextIndex.setStatus("current")
_Hh3cdeEBIfTable_Object = MibTable
hh3cdeEBIfTable = _Hh3cdeEBIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 3)
)
if mibBuilder.loadTexts:
    hh3cdeEBIfTable.setStatus("current")
_Hh3cdeEBIfEntry_Object = MibTableRow
hh3cdeEBIfEntry = _Hh3cdeEBIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 3, 1)
)
hh3cdeEBIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cdeEBIfEntry.setStatus("current")


class _Hh3cdeEBMulticastMac_Type(MacAddressNC):
    """Custom type hh3cdeEBMulticastMac based on MacAddressNC"""
    defaultHexValue = "000000000000"


_Hh3cdeEBMulticastMac_Object = MibTableColumn
hh3cdeEBMulticastMac = _Hh3cdeEBMulticastMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 3, 1, 1),
    _Hh3cdeEBMulticastMac_Type()
)
hh3cdeEBMulticastMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeEBMulticastMac.setStatus("current")


class _Hh3cdeEBPriority_Type(Integer32):
    """Custom type hh3cdeEBPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cdeEBPriority_Type.__name__ = "Integer32"
_Hh3cdeEBPriority_Object = MibTableColumn
hh3cdeEBPriority = _Hh3cdeEBPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 3, 1, 2),
    _Hh3cdeEBPriority_Type()
)
hh3cdeEBPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeEBPriority.setStatus("current")


class _Hh3cdeEBtimer_Type(Integer32):
    """Custom type hh3cdeEBtimer based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_Hh3cdeEBtimer_Type.__name__ = "Integer32"
_Hh3cdeEBtimer_Object = MibTableColumn
hh3cdeEBtimer = _Hh3cdeEBtimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 3, 1, 3),
    _Hh3cdeEBtimer_Type()
)
hh3cdeEBtimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeEBtimer.setStatus("current")
_Hh3cdeEBRowStatus_Type = RowStatus
_Hh3cdeEBRowStatus_Object = MibTableColumn
hh3cdeEBRowStatus = _Hh3cdeEBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 3, 1, 4),
    _Hh3cdeEBRowStatus_Type()
)
hh3cdeEBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeEBRowStatus.setStatus("current")
_Hh3cdeEBMacMapTable_Object = MibTable
hh3cdeEBMacMapTable = _Hh3cdeEBMacMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 4)
)
if mibBuilder.loadTexts:
    hh3cdeEBMacMapTable.setStatus("current")
_Hh3cdeEBMacMapEntry_Object = MibTableRow
hh3cdeEBMacMapEntry = _Hh3cdeEBMacMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 4, 1)
)
hh3cdeEBMacMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-SNA-DLSW-EXT-MIB", "hh3cdeEBMacMapIndex"),
)
if mibBuilder.loadTexts:
    hh3cdeEBMacMapEntry.setStatus("current")
_Hh3cdeEBMacMapIndex_Type = Integer32
_Hh3cdeEBMacMapIndex_Object = MibTableColumn
hh3cdeEBMacMapIndex = _Hh3cdeEBMacMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 4, 1, 1),
    _Hh3cdeEBMacMapIndex_Type()
)
hh3cdeEBMacMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cdeEBMacMapIndex.setStatus("current")
_Hh3cdeEBMacMapLocalMac_Type = MacAddressNC
_Hh3cdeEBMacMapLocalMac_Object = MibTableColumn
hh3cdeEBMacMapLocalMac = _Hh3cdeEBMacMapLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 4, 1, 2),
    _Hh3cdeEBMacMapLocalMac_Type()
)
hh3cdeEBMacMapLocalMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeEBMacMapLocalMac.setStatus("current")
_Hh3cdeEBMacMapRemoteMac_Type = MacAddressNC
_Hh3cdeEBMacMapRemoteMac_Object = MibTableColumn
hh3cdeEBMacMapRemoteMac = _Hh3cdeEBMacMapRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 4, 1, 3),
    _Hh3cdeEBMacMapRemoteMac_Type()
)
hh3cdeEBMacMapRemoteMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeEBMacMapRemoteMac.setStatus("current")
_Hh3cdeEBMacMapNeighbour_Type = MacAddressNC
_Hh3cdeEBMacMapNeighbour_Object = MibTableColumn
hh3cdeEBMacMapNeighbour = _Hh3cdeEBMacMapNeighbour_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 4, 1, 4),
    _Hh3cdeEBMacMapNeighbour_Type()
)
hh3cdeEBMacMapNeighbour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeEBMacMapNeighbour.setStatus("current")
_Hh3cdeEBMacMapRowStatus_Type = RowStatus
_Hh3cdeEBMacMapRowStatus_Object = MibTableColumn
hh3cdeEBMacMapRowStatus = _Hh3cdeEBMacMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62, 1, 8, 4, 1, 5),
    _Hh3cdeEBMacMapRowStatus_Type()
)
hh3cdeEBMacMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdeEBMacMapRowStatus.setStatus("current")
dlswTConnConfigEntry.registerAugmentions(
    ("HH3C-SNA-DLSW-EXT-MIB",
     "hh3cdeTConnConfigEntry")
)
hh3cdeTConnConfigEntry.setIndexNames(*dlswTConnConfigEntry.getIndexNames())
dlswTConnOperEntry.registerAugmentions(
    ("HH3C-SNA-DLSW-EXT-MIB",
     "hh3cdeTConnOperEntry")
)
hh3cdeTConnOperEntry.setIndexNames(*dlswTConnOperEntry.getIndexNames())
dlswTConnTcpConfigEntry.registerAugmentions(
    ("HH3C-SNA-DLSW-EXT-MIB",
     "hh3cdeTConnTcpConfigEntry")
)
hh3cdeTConnTcpConfigEntry.setIndexNames(*dlswTConnTcpConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SNA-DLSW-EXT-MIB",
    **{"hh3cDlswExt": hh3cDlswExt,
       "hh3cDlswExtMIBObjects": hh3cDlswExtMIBObjects,
       "hh3cdeNode": hh3cdeNode,
       "hh3cdeNodeVendorID": hh3cdeNodeVendorID,
       "hh3cdeNodeIpAddrType": hh3cdeNodeIpAddrType,
       "hh3cdeNodeLocalAddr": hh3cdeNodeLocalAddr,
       "hh3cdeNodePriority": hh3cdeNodePriority,
       "hh3cdeNodeInitPacingWindow": hh3cdeNodeInitPacingWindow,
       "hh3cdeNodeMaxPacingWindow": hh3cdeNodeMaxPacingWindow,
       "hh3cdeNodeKeepAliveInterval": hh3cdeNodeKeepAliveInterval,
       "hh3cdeNodePermitDynamic": hh3cdeNodePermitDynamic,
       "hh3cdeNodeConnTimeout": hh3cdeNodeConnTimeout,
       "hh3cdeNodeLocalPendTimeout": hh3cdeNodeLocalPendTimeout,
       "hh3cdeNodeRemotePendTimeout": hh3cdeNodeRemotePendTimeout,
       "hh3cdeNodeSnaCacheTimeout": hh3cdeNodeSnaCacheTimeout,
       "hh3cdeNodeExplorerTimeout": hh3cdeNodeExplorerTimeout,
       "hh3cdeNodeExplorerWaitTimeout": hh3cdeNodeExplorerWaitTimeout,
       "hh3cdeNodeConfigSapList": hh3cdeNodeConfigSapList,
       "hh3cdeNodeMaxTransmission": hh3cdeNodeMaxTransmission,
       "hh3cdeNodeMulticastStatus": hh3cdeNodeMulticastStatus,
       "hh3cdeNodeMulticastAddress": hh3cdeNodeMulticastAddress,
       "hh3cdeNodeResetTcpAll": hh3cdeNodeResetTcpAll,
       "hh3cdeNodeStCapTcpNum": hh3cdeNodeStCapTcpNum,
       "hh3cdeNodeTcpQueueMax": hh3cdeNodeTcpQueueMax,
       "hh3cdeTConn": hh3cdeTConn,
       "hh3cdeTConnConfigTable": hh3cdeTConnConfigTable,
       "hh3cdeTConnConfigEntry": hh3cdeTConnConfigEntry,
       "hh3cdeTConnConfigVersion": hh3cdeTConnConfigVersion,
       "hh3cdeTConnConfigPriority": hh3cdeTConnConfigPriority,
       "hh3cdeTConnConfigLfSize": hh3cdeTConnConfigLfSize,
       "hh3cdeTConnConfigKeepaliveIntval": hh3cdeTConnConfigKeepaliveIntval,
       "hh3cdeTConnConfigBackup": hh3cdeTConnConfigBackup,
       "hh3cdeTConnConfigBackupTAddr": hh3cdeTConnConfigBackupTAddr,
       "hh3cdeTConnConfigBackupLinger": hh3cdeTConnConfigBackupLinger,
       "hh3cdeTConnOperTable": hh3cdeTConnOperTable,
       "hh3cdeTConnOperEntry": hh3cdeTConnOperEntry,
       "hh3cdeTConnOperPeerType": hh3cdeTConnOperPeerType,
       "hh3cdeTConnOperVendorID": hh3cdeTConnOperVendorID,
       "hh3cdeTConnOperVersionString": hh3cdeTConnOperVersionString,
       "hh3cdeTConnOperUpTime": hh3cdeTConnOperUpTime,
       "hh3cdeTConnOperMulticastAddress": hh3cdeTConnOperMulticastAddress,
       "hh3cdeTConnOperStCapTcpNumber": hh3cdeTConnOperStCapTcpNumber,
       "hh3cdeTConnOperRecvPkts": hh3cdeTConnOperRecvPkts,
       "hh3cdeTConnOperSendPkts": hh3cdeTConnOperSendPkts,
       "hh3cdeTConnOperDropPkts": hh3cdeTConnOperDropPkts,
       "hh3cdeTConnTcpConfigTable": hh3cdeTConnTcpConfigTable,
       "hh3cdeTConnTcpConfigEntry": hh3cdeTConnTcpConfigEntry,
       "hh3cdeTConnTcpConfigQueueMax": hh3cdeTConnTcpConfigQueueMax,
       "hh3cdeBridge": hh3cdeBridge,
       "hh3cdeBridgeTable": hh3cdeBridgeTable,
       "hh3cdeBridgeEntry": hh3cdeBridgeEntry,
       "hh3cdeBridgeNumIndex": hh3cdeBridgeNumIndex,
       "hh3cdeBridgeRowStatus": hh3cdeBridgeRowStatus,
       "hh3cdeBridgeIfTable": hh3cdeBridgeIfTable,
       "hh3cdeBridgeIfEntry": hh3cdeBridgeIfEntry,
       "hh3cdeBridgeIfBrgGrp": hh3cdeBridgeIfBrgGrp,
       "hh3cdeBridgeIfRowStatus": hh3cdeBridgeIfRowStatus,
       "hh3cdeQllc": hh3cdeQllc,
       "hh3cdeQllcTable": hh3cdeQllcTable,
       "hh3cdeQllcEntry": hh3cdeQllcEntry,
       "hh3cQllcX121Address": hh3cQllcX121Address,
       "hh3cQllcLocalMac": hh3cQllcLocalMac,
       "hh3cQllcLocalSap": hh3cQllcLocalSap,
       "hh3cQllcRemoteMac": hh3cQllcRemoteMac,
       "hh3cQllcRemoteSap": hh3cQllcRemoteSap,
       "hh3cQllcRowStatus": hh3cQllcRowStatus,
       "hh3cdeSdlc": hh3cdeSdlc,
       "hh3cdeSdlcPortTable": hh3cdeSdlcPortTable,
       "hh3cdeSdlcPortEntry": hh3cdeSdlcPortEntry,
       "hh3cdeSdlcPortRole": hh3cdeSdlcPortRole,
       "hh3cdeSdlcPortSendWindow": hh3cdeSdlcPortSendWindow,
       "hh3cdeSdlcPortModulo": hh3cdeSdlcPortModulo,
       "hh3cdeSdlcPortMaxPdu": hh3cdeSdlcPortMaxPdu,
       "hh3cdeSdlcPortMaxSendQueue": hh3cdeSdlcPortMaxSendQueue,
       "hh3cdeSdlcPortMaxTransmission": hh3cdeSdlcPortMaxTransmission,
       "hh3cdeSdlcPortSimultaneousEnable": hh3cdeSdlcPortSimultaneousEnable,
       "hh3cdeSdlcPortTimerACK": hh3cdeSdlcPortTimerACK,
       "hh3cdeSdlcPortTimerLifeTime": hh3cdeSdlcPortTimerLifeTime,
       "hh3cdeSdlcPortTimerPollPause": hh3cdeSdlcPortTimerPollPause,
       "hh3cdeSdlcPortRowStatus": hh3cdeSdlcPortRowStatus,
       "hh3cdeLlc2": hh3cdeLlc2,
       "hh3cdeLlc2PortTable": hh3cdeLlc2PortTable,
       "hh3cdeLlc2PortEntry": hh3cdeLlc2PortEntry,
       "hh3cdeLlc2PortMaxAck": hh3cdeLlc2PortMaxAck,
       "hh3cdeLlc2PortMaxPdu": hh3cdeLlc2PortMaxPdu,
       "hh3cdeLlc2PortMaxSendQueue": hh3cdeLlc2PortMaxSendQueue,
       "hh3cdeLlc2PortMaxTransmission": hh3cdeLlc2PortMaxTransmission,
       "hh3cdeLlc2PortModulo": hh3cdeLlc2PortModulo,
       "hh3cdeLlc2PortReceiveWindow": hh3cdeLlc2PortReceiveWindow,
       "hh3cdeLlc2PortTimerAck": hh3cdeLlc2PortTimerAck,
       "hh3cdeLlc2PortTimerAckDelay": hh3cdeLlc2PortTimerAckDelay,
       "hh3cdeLlc2PortTimerDetect": hh3cdeLlc2PortTimerDetect,
       "hh3cdeLlc2PortTimerBusy": hh3cdeLlc2PortTimerBusy,
       "hh3cdeLlc2PortTimerPoll": hh3cdeLlc2PortTimerPoll,
       "hh3cdeLlc2PortTimerReject": hh3cdeLlc2PortTimerReject,
       "hh3cdeLlc2PortRowStatus": hh3cdeLlc2PortRowStatus,
       "hh3cdeReachableCache": hh3cdeReachableCache,
       "hh3cdeRchCacheStat": hh3cdeRchCacheStat,
       "hh3cdeRchCacheMaxIndex": hh3cdeRchCacheMaxIndex,
       "hh3cdeRchCacheNextIndex": hh3cdeRchCacheNextIndex,
       "hh3cdeRchCacheTable": hh3cdeRchCacheTable,
       "hh3cdeRchCacheEntry": hh3cdeRchCacheEntry,
       "hh3cdeRchCacheIndex": hh3cdeRchCacheIndex,
       "hh3cdeRchCacheStatus": hh3cdeRchCacheStatus,
       "hh3cdeRchCacheRemainTime": hh3cdeRchCacheRemainTime,
       "hh3cdeRchCacheMac": hh3cdeRchCacheMac,
       "hh3cdeRchCacheRemoteIpAddrType": hh3cdeRchCacheRemoteIpAddrType,
       "hh3cdeRchCacheRemoteIp": hh3cdeRchCacheRemoteIp,
       "hh3cdeRchCacheRowStatus": hh3cdeRchCacheRowStatus,
       "hh3cdeEthernetBackup": hh3cdeEthernetBackup,
       "hh3cdeEBMacMapStat": hh3cdeEBMacMapStat,
       "hh3cdeEBMacMapMaxIndex": hh3cdeEBMacMapMaxIndex,
       "hh3cdeEBMacMapNextIndex": hh3cdeEBMacMapNextIndex,
       "hh3cdeEBIfTable": hh3cdeEBIfTable,
       "hh3cdeEBIfEntry": hh3cdeEBIfEntry,
       "hh3cdeEBMulticastMac": hh3cdeEBMulticastMac,
       "hh3cdeEBPriority": hh3cdeEBPriority,
       "hh3cdeEBtimer": hh3cdeEBtimer,
       "hh3cdeEBRowStatus": hh3cdeEBRowStatus,
       "hh3cdeEBMacMapTable": hh3cdeEBMacMapTable,
       "hh3cdeEBMacMapEntry": hh3cdeEBMacMapEntry,
       "hh3cdeEBMacMapIndex": hh3cdeEBMacMapIndex,
       "hh3cdeEBMacMapLocalMac": hh3cdeEBMacMapLocalMac,
       "hh3cdeEBMacMapRemoteMac": hh3cdeEBMacMapRemoteMac,
       "hh3cdeEBMacMapNeighbour": hh3cdeEBMacMapNeighbour,
       "hh3cdeEBMacMapRowStatus": hh3cdeEBMacMapRowStatus}
)
