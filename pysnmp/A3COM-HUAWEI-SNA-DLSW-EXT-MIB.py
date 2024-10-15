# SNMP MIB module (A3COM-HUAWEI-SNA-DLSW-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-SNA-DLSW-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:03 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cDlswExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62)
)
h3cDlswExt.setRevisions(
        ("2005-07-20 19:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDlswExtMIBObjects_ObjectIdentity = ObjectIdentity
h3cDlswExtMIBObjects = _H3cDlswExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1)
)
_H3cdeNode_ObjectIdentity = ObjectIdentity
h3cdeNode = _H3cdeNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1)
)


class _H3cdeNodeVendorID_Type(OctetString):
    """Custom type h3cdeNodeVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_H3cdeNodeVendorID_Type.__name__ = "OctetString"
_H3cdeNodeVendorID_Object = MibScalar
h3cdeNodeVendorID = _H3cdeNodeVendorID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 1),
    _H3cdeNodeVendorID_Type()
)
h3cdeNodeVendorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeVendorID.setStatus("current")
_H3cdeNodeIpAddrType_Type = InetAddressType
_H3cdeNodeIpAddrType_Object = MibScalar
h3cdeNodeIpAddrType = _H3cdeNodeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 2),
    _H3cdeNodeIpAddrType_Type()
)
h3cdeNodeIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeIpAddrType.setStatus("current")


class _H3cdeNodeLocalAddr_Type(InetAddress):
    """Custom type h3cdeNodeLocalAddr based on InetAddress"""
    defaultHexValue = ""


_H3cdeNodeLocalAddr_Object = MibScalar
h3cdeNodeLocalAddr = _H3cdeNodeLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 3),
    _H3cdeNodeLocalAddr_Type()
)
h3cdeNodeLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeLocalAddr.setStatus("current")


class _H3cdeNodePriority_Type(Integer32):
    """Custom type h3cdeNodePriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
        ValueRangeConstraint(65535, 65535),
    )


_H3cdeNodePriority_Type.__name__ = "Integer32"
_H3cdeNodePriority_Object = MibScalar
h3cdeNodePriority = _H3cdeNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 4),
    _H3cdeNodePriority_Type()
)
h3cdeNodePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodePriority.setStatus("current")


class _H3cdeNodeInitPacingWindow_Type(Integer32):
    """Custom type h3cdeNodeInitPacingWindow based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_H3cdeNodeInitPacingWindow_Type.__name__ = "Integer32"
_H3cdeNodeInitPacingWindow_Object = MibScalar
h3cdeNodeInitPacingWindow = _H3cdeNodeInitPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 5),
    _H3cdeNodeInitPacingWindow_Type()
)
h3cdeNodeInitPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeInitPacingWindow.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeNodeInitPacingWindow.setUnits("packets")


class _H3cdeNodeMaxPacingWindow_Type(Integer32):
    """Custom type h3cdeNodeMaxPacingWindow based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_H3cdeNodeMaxPacingWindow_Type.__name__ = "Integer32"
_H3cdeNodeMaxPacingWindow_Object = MibScalar
h3cdeNodeMaxPacingWindow = _H3cdeNodeMaxPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 6),
    _H3cdeNodeMaxPacingWindow_Type()
)
h3cdeNodeMaxPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeMaxPacingWindow.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeNodeMaxPacingWindow.setUnits("packets")


class _H3cdeNodeKeepAliveInterval_Type(Integer32):
    """Custom type h3cdeNodeKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_H3cdeNodeKeepAliveInterval_Type.__name__ = "Integer32"
_H3cdeNodeKeepAliveInterval_Object = MibScalar
h3cdeNodeKeepAliveInterval = _H3cdeNodeKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 7),
    _H3cdeNodeKeepAliveInterval_Type()
)
h3cdeNodeKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeNodeKeepAliveInterval.setUnits("seconds")


class _H3cdeNodePermitDynamic_Type(Integer32):
    """Custom type h3cdeNodePermitDynamic based on Integer32"""
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


_H3cdeNodePermitDynamic_Type.__name__ = "Integer32"
_H3cdeNodePermitDynamic_Object = MibScalar
h3cdeNodePermitDynamic = _H3cdeNodePermitDynamic_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 8),
    _H3cdeNodePermitDynamic_Type()
)
h3cdeNodePermitDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodePermitDynamic.setStatus("current")


class _H3cdeNodeConnTimeout_Type(Integer32):
    """Custom type h3cdeNodeConnTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cdeNodeConnTimeout_Type.__name__ = "Integer32"
_H3cdeNodeConnTimeout_Object = MibScalar
h3cdeNodeConnTimeout = _H3cdeNodeConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 9),
    _H3cdeNodeConnTimeout_Type()
)
h3cdeNodeConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeConnTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeNodeConnTimeout.setUnits("seconds")


class _H3cdeNodeLocalPendTimeout_Type(Integer32):
    """Custom type h3cdeNodeLocalPendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cdeNodeLocalPendTimeout_Type.__name__ = "Integer32"
_H3cdeNodeLocalPendTimeout_Object = MibScalar
h3cdeNodeLocalPendTimeout = _H3cdeNodeLocalPendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 10),
    _H3cdeNodeLocalPendTimeout_Type()
)
h3cdeNodeLocalPendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeLocalPendTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeNodeLocalPendTimeout.setUnits("seconds")


class _H3cdeNodeRemotePendTimeout_Type(Integer32):
    """Custom type h3cdeNodeRemotePendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cdeNodeRemotePendTimeout_Type.__name__ = "Integer32"
_H3cdeNodeRemotePendTimeout_Object = MibScalar
h3cdeNodeRemotePendTimeout = _H3cdeNodeRemotePendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 11),
    _H3cdeNodeRemotePendTimeout_Type()
)
h3cdeNodeRemotePendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeRemotePendTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeNodeRemotePendTimeout.setUnits("seconds")


class _H3cdeNodeSnaCacheTimeout_Type(Integer32):
    """Custom type h3cdeNodeSnaCacheTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cdeNodeSnaCacheTimeout_Type.__name__ = "Integer32"
_H3cdeNodeSnaCacheTimeout_Object = MibScalar
h3cdeNodeSnaCacheTimeout = _H3cdeNodeSnaCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 12),
    _H3cdeNodeSnaCacheTimeout_Type()
)
h3cdeNodeSnaCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeSnaCacheTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeNodeSnaCacheTimeout.setUnits("seconds")


class _H3cdeNodeExplorerTimeout_Type(Integer32):
    """Custom type h3cdeNodeExplorerTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cdeNodeExplorerTimeout_Type.__name__ = "Integer32"
_H3cdeNodeExplorerTimeout_Object = MibScalar
h3cdeNodeExplorerTimeout = _H3cdeNodeExplorerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 13),
    _H3cdeNodeExplorerTimeout_Type()
)
h3cdeNodeExplorerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeExplorerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeNodeExplorerTimeout.setUnits("seconds")


class _H3cdeNodeExplorerWaitTimeout_Type(Integer32):
    """Custom type h3cdeNodeExplorerWaitTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cdeNodeExplorerWaitTimeout_Type.__name__ = "Integer32"
_H3cdeNodeExplorerWaitTimeout_Object = MibScalar
h3cdeNodeExplorerWaitTimeout = _H3cdeNodeExplorerWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 14),
    _H3cdeNodeExplorerWaitTimeout_Type()
)
h3cdeNodeExplorerWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeExplorerWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeNodeExplorerWaitTimeout.setUnits("seconds")


class _H3cdeNodeConfigSapList_Type(OctetString):
    """Custom type h3cdeNodeConfigSapList based on OctetString"""
    defaultHexValue = "FF000000000000000000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_H3cdeNodeConfigSapList_Type.__name__ = "OctetString"
_H3cdeNodeConfigSapList_Object = MibScalar
h3cdeNodeConfigSapList = _H3cdeNodeConfigSapList_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 15),
    _H3cdeNodeConfigSapList_Type()
)
h3cdeNodeConfigSapList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeConfigSapList.setStatus("current")


class _H3cdeNodeMaxTransmission_Type(Integer32):
    """Custom type h3cdeNodeMaxTransmission based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_H3cdeNodeMaxTransmission_Type.__name__ = "Integer32"
_H3cdeNodeMaxTransmission_Object = MibScalar
h3cdeNodeMaxTransmission = _H3cdeNodeMaxTransmission_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 16),
    _H3cdeNodeMaxTransmission_Type()
)
h3cdeNodeMaxTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeMaxTransmission.setStatus("current")


class _H3cdeNodeMulticastStatus_Type(Integer32):
    """Custom type h3cdeNodeMulticastStatus based on Integer32"""
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


_H3cdeNodeMulticastStatus_Type.__name__ = "Integer32"
_H3cdeNodeMulticastStatus_Object = MibScalar
h3cdeNodeMulticastStatus = _H3cdeNodeMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 17),
    _H3cdeNodeMulticastStatus_Type()
)
h3cdeNodeMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeMulticastStatus.setStatus("current")
_H3cdeNodeMulticastAddress_Type = InetAddress
_H3cdeNodeMulticastAddress_Object = MibScalar
h3cdeNodeMulticastAddress = _H3cdeNodeMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 18),
    _H3cdeNodeMulticastAddress_Type()
)
h3cdeNodeMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeMulticastAddress.setStatus("current")


class _H3cdeNodeResetTcpAll_Type(Integer32):
    """Custom type h3cdeNodeResetTcpAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_H3cdeNodeResetTcpAll_Type.__name__ = "Integer32"
_H3cdeNodeResetTcpAll_Object = MibScalar
h3cdeNodeResetTcpAll = _H3cdeNodeResetTcpAll_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 19),
    _H3cdeNodeResetTcpAll_Type()
)
h3cdeNodeResetTcpAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeResetTcpAll.setStatus("current")


class _H3cdeNodeStCapTcpNum_Type(Integer32):
    """Custom type h3cdeNodeStCapTcpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cdeNodeStCapTcpNum_Type.__name__ = "Integer32"
_H3cdeNodeStCapTcpNum_Object = MibScalar
h3cdeNodeStCapTcpNum = _H3cdeNodeStCapTcpNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 20),
    _H3cdeNodeStCapTcpNum_Type()
)
h3cdeNodeStCapTcpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeStCapTcpNum.setStatus("current")


class _H3cdeNodeTcpQueueMax_Type(Integer32):
    """Custom type h3cdeNodeTcpQueueMax based on Integer32"""
    defaultValue = 200


_H3cdeNodeTcpQueueMax_Object = MibScalar
h3cdeNodeTcpQueueMax = _H3cdeNodeTcpQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 1, 21),
    _H3cdeNodeTcpQueueMax_Type()
)
h3cdeNodeTcpQueueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cdeNodeTcpQueueMax.setStatus("current")
_H3cdeTConn_ObjectIdentity = ObjectIdentity
h3cdeTConn = _H3cdeTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2)
)
_H3cdeTConnConfigTable_Object = MibTable
h3cdeTConnConfigTable = _H3cdeTConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cdeTConnConfigTable.setStatus("current")
_H3cdeTConnConfigEntry_Object = MibTableRow
h3cdeTConnConfigEntry = _H3cdeTConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cdeTConnConfigEntry.setStatus("current")


class _H3cdeTConnConfigVersion_Type(OctetString):
    """Custom type h3cdeTConnConfigVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_H3cdeTConnConfigVersion_Type.__name__ = "OctetString"
_H3cdeTConnConfigVersion_Object = MibTableColumn
h3cdeTConnConfigVersion = _H3cdeTConnConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 1, 1, 1),
    _H3cdeTConnConfigVersion_Type()
)
h3cdeTConnConfigVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeTConnConfigVersion.setStatus("current")


class _H3cdeTConnConfigPriority_Type(Integer32):
    """Custom type h3cdeTConnConfigPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_H3cdeTConnConfigPriority_Type.__name__ = "Integer32"
_H3cdeTConnConfigPriority_Object = MibTableColumn
h3cdeTConnConfigPriority = _H3cdeTConnConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 1, 1, 2),
    _H3cdeTConnConfigPriority_Type()
)
h3cdeTConnConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeTConnConfigPriority.setStatus("current")
_H3cdeTConnConfigLfSize_Type = LFSize
_H3cdeTConnConfigLfSize_Object = MibTableColumn
h3cdeTConnConfigLfSize = _H3cdeTConnConfigLfSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 1, 1, 3),
    _H3cdeTConnConfigLfSize_Type()
)
h3cdeTConnConfigLfSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeTConnConfigLfSize.setStatus("current")


class _H3cdeTConnConfigKeepaliveIntval_Type(Integer32):
    """Custom type h3cdeTConnConfigKeepaliveIntval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_H3cdeTConnConfigKeepaliveIntval_Type.__name__ = "Integer32"
_H3cdeTConnConfigKeepaliveIntval_Object = MibTableColumn
h3cdeTConnConfigKeepaliveIntval = _H3cdeTConnConfigKeepaliveIntval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 1, 1, 4),
    _H3cdeTConnConfigKeepaliveIntval_Type()
)
h3cdeTConnConfigKeepaliveIntval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeTConnConfigKeepaliveIntval.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeTConnConfigKeepaliveIntval.setUnits("seconds")


class _H3cdeTConnConfigBackup_Type(Integer32):
    """Custom type h3cdeTConnConfigBackup based on Integer32"""
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


_H3cdeTConnConfigBackup_Type.__name__ = "Integer32"
_H3cdeTConnConfigBackup_Object = MibTableColumn
h3cdeTConnConfigBackup = _H3cdeTConnConfigBackup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 1, 1, 5),
    _H3cdeTConnConfigBackup_Type()
)
h3cdeTConnConfigBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeTConnConfigBackup.setStatus("current")
_H3cdeTConnConfigBackupTAddr_Type = TAddress
_H3cdeTConnConfigBackupTAddr_Object = MibTableColumn
h3cdeTConnConfigBackupTAddr = _H3cdeTConnConfigBackupTAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 1, 1, 6),
    _H3cdeTConnConfigBackupTAddr_Type()
)
h3cdeTConnConfigBackupTAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeTConnConfigBackupTAddr.setStatus("current")


class _H3cdeTConnConfigBackupLinger_Type(Integer32):
    """Custom type h3cdeTConnConfigBackupLinger based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_H3cdeTConnConfigBackupLinger_Type.__name__ = "Integer32"
_H3cdeTConnConfigBackupLinger_Object = MibTableColumn
h3cdeTConnConfigBackupLinger = _H3cdeTConnConfigBackupLinger_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 1, 1, 7),
    _H3cdeTConnConfigBackupLinger_Type()
)
h3cdeTConnConfigBackupLinger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeTConnConfigBackupLinger.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeTConnConfigBackupLinger.setUnits("minutes")
_H3cdeTConnOperTable_Object = MibTable
h3cdeTConnOperTable = _H3cdeTConnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cdeTConnOperTable.setStatus("current")
_H3cdeTConnOperEntry_Object = MibTableRow
h3cdeTConnOperEntry = _H3cdeTConnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cdeTConnOperEntry.setStatus("current")


class _H3cdeTConnOperPeerType_Type(Integer32):
    """Custom type h3cdeTConnOperPeerType based on Integer32"""
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


_H3cdeTConnOperPeerType_Type.__name__ = "Integer32"
_H3cdeTConnOperPeerType_Object = MibTableColumn
h3cdeTConnOperPeerType = _H3cdeTConnOperPeerType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1, 1),
    _H3cdeTConnOperPeerType_Type()
)
h3cdeTConnOperPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeTConnOperPeerType.setStatus("current")
_H3cdeTConnOperVendorID_Type = OctetString
_H3cdeTConnOperVendorID_Object = MibTableColumn
h3cdeTConnOperVendorID = _H3cdeTConnOperVendorID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1, 2),
    _H3cdeTConnOperVendorID_Type()
)
h3cdeTConnOperVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeTConnOperVendorID.setStatus("current")
_H3cdeTConnOperVersionString_Type = OctetString
_H3cdeTConnOperVersionString_Object = MibTableColumn
h3cdeTConnOperVersionString = _H3cdeTConnOperVersionString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1, 3),
    _H3cdeTConnOperVersionString_Type()
)
h3cdeTConnOperVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeTConnOperVersionString.setStatus("current")
_H3cdeTConnOperUpTime_Type = TimeTicks
_H3cdeTConnOperUpTime_Object = MibTableColumn
h3cdeTConnOperUpTime = _H3cdeTConnOperUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1, 4),
    _H3cdeTConnOperUpTime_Type()
)
h3cdeTConnOperUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeTConnOperUpTime.setStatus("current")
_H3cdeTConnOperMulticastAddress_Type = TAddress
_H3cdeTConnOperMulticastAddress_Object = MibTableColumn
h3cdeTConnOperMulticastAddress = _H3cdeTConnOperMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1, 5),
    _H3cdeTConnOperMulticastAddress_Type()
)
h3cdeTConnOperMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeTConnOperMulticastAddress.setStatus("current")
_H3cdeTConnOperStCapTcpNumber_Type = Integer32
_H3cdeTConnOperStCapTcpNumber_Object = MibTableColumn
h3cdeTConnOperStCapTcpNumber = _H3cdeTConnOperStCapTcpNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1, 6),
    _H3cdeTConnOperStCapTcpNumber_Type()
)
h3cdeTConnOperStCapTcpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeTConnOperStCapTcpNumber.setStatus("current")
_H3cdeTConnOperRecvPkts_Type = Counter32
_H3cdeTConnOperRecvPkts_Object = MibTableColumn
h3cdeTConnOperRecvPkts = _H3cdeTConnOperRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1, 7),
    _H3cdeTConnOperRecvPkts_Type()
)
h3cdeTConnOperRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeTConnOperRecvPkts.setStatus("current")
_H3cdeTConnOperSendPkts_Type = Counter32
_H3cdeTConnOperSendPkts_Object = MibTableColumn
h3cdeTConnOperSendPkts = _H3cdeTConnOperSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1, 8),
    _H3cdeTConnOperSendPkts_Type()
)
h3cdeTConnOperSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeTConnOperSendPkts.setStatus("current")
_H3cdeTConnOperDropPkts_Type = Counter32
_H3cdeTConnOperDropPkts_Object = MibTableColumn
h3cdeTConnOperDropPkts = _H3cdeTConnOperDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 2, 1, 9),
    _H3cdeTConnOperDropPkts_Type()
)
h3cdeTConnOperDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeTConnOperDropPkts.setStatus("current")
_H3cdeTConnTcpConfigTable_Object = MibTable
h3cdeTConnTcpConfigTable = _H3cdeTConnTcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cdeTConnTcpConfigTable.setStatus("current")
_H3cdeTConnTcpConfigEntry_Object = MibTableRow
h3cdeTConnTcpConfigEntry = _H3cdeTConnTcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    h3cdeTConnTcpConfigEntry.setStatus("current")


class _H3cdeTConnTcpConfigQueueMax_Type(Integer32):
    """Custom type h3cdeTConnTcpConfigQueueMax based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 2000),
    )


_H3cdeTConnTcpConfigQueueMax_Type.__name__ = "Integer32"
_H3cdeTConnTcpConfigQueueMax_Object = MibTableColumn
h3cdeTConnTcpConfigQueueMax = _H3cdeTConnTcpConfigQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 2, 3, 1, 1),
    _H3cdeTConnTcpConfigQueueMax_Type()
)
h3cdeTConnTcpConfigQueueMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeTConnTcpConfigQueueMax.setStatus("current")
_H3cdeBridge_ObjectIdentity = ObjectIdentity
h3cdeBridge = _H3cdeBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 3)
)
_H3cdeBridgeTable_Object = MibTable
h3cdeBridgeTable = _H3cdeBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cdeBridgeTable.setStatus("current")
_H3cdeBridgeEntry_Object = MibTableRow
h3cdeBridgeEntry = _H3cdeBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 3, 1, 1)
)
h3cdeBridgeEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SNA-DLSW-EXT-MIB", "h3cdeBridgeNumIndex"),
)
if mibBuilder.loadTexts:
    h3cdeBridgeEntry.setStatus("current")


class _H3cdeBridgeNumIndex_Type(Integer32):
    """Custom type h3cdeBridgeNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cdeBridgeNumIndex_Type.__name__ = "Integer32"
_H3cdeBridgeNumIndex_Object = MibTableColumn
h3cdeBridgeNumIndex = _H3cdeBridgeNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 3, 1, 1, 1),
    _H3cdeBridgeNumIndex_Type()
)
h3cdeBridgeNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cdeBridgeNumIndex.setStatus("current")
_H3cdeBridgeRowStatus_Type = RowStatus
_H3cdeBridgeRowStatus_Object = MibTableColumn
h3cdeBridgeRowStatus = _H3cdeBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 3, 1, 1, 2),
    _H3cdeBridgeRowStatus_Type()
)
h3cdeBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeBridgeRowStatus.setStatus("current")
_H3cdeBridgeIfTable_Object = MibTable
h3cdeBridgeIfTable = _H3cdeBridgeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cdeBridgeIfTable.setStatus("current")
_H3cdeBridgeIfEntry_Object = MibTableRow
h3cdeBridgeIfEntry = _H3cdeBridgeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 3, 2, 1)
)
h3cdeBridgeIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cdeBridgeIfEntry.setStatus("current")


class _H3cdeBridgeIfBrgGrp_Type(Integer32):
    """Custom type h3cdeBridgeIfBrgGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cdeBridgeIfBrgGrp_Type.__name__ = "Integer32"
_H3cdeBridgeIfBrgGrp_Object = MibTableColumn
h3cdeBridgeIfBrgGrp = _H3cdeBridgeIfBrgGrp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 3, 2, 1, 1),
    _H3cdeBridgeIfBrgGrp_Type()
)
h3cdeBridgeIfBrgGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeBridgeIfBrgGrp.setStatus("current")
_H3cdeBridgeIfRowStatus_Type = RowStatus
_H3cdeBridgeIfRowStatus_Object = MibTableColumn
h3cdeBridgeIfRowStatus = _H3cdeBridgeIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 3, 2, 1, 2),
    _H3cdeBridgeIfRowStatus_Type()
)
h3cdeBridgeIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeBridgeIfRowStatus.setStatus("current")
_H3cdeQllc_ObjectIdentity = ObjectIdentity
h3cdeQllc = _H3cdeQllc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 4)
)
_H3cdeQllcTable_Object = MibTable
h3cdeQllcTable = _H3cdeQllcTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3cdeQllcTable.setStatus("current")
_H3cdeQllcEntry_Object = MibTableRow
h3cdeQllcEntry = _H3cdeQllcEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 4, 1, 1)
)
h3cdeQllcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cdeQllcEntry.setStatus("current")
_H3cQllcX121Address_Type = Integer32
_H3cQllcX121Address_Object = MibTableColumn
h3cQllcX121Address = _H3cQllcX121Address_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 4, 1, 1, 1),
    _H3cQllcX121Address_Type()
)
h3cQllcX121Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQllcX121Address.setStatus("current")
_H3cQllcLocalMac_Type = MacAddressNC
_H3cQllcLocalMac_Object = MibTableColumn
h3cQllcLocalMac = _H3cQllcLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 4, 1, 1, 2),
    _H3cQllcLocalMac_Type()
)
h3cQllcLocalMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQllcLocalMac.setStatus("current")


class _H3cQllcLocalSap_Type(OctetString):
    """Custom type h3cQllcLocalSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_H3cQllcLocalSap_Type.__name__ = "OctetString"
_H3cQllcLocalSap_Object = MibTableColumn
h3cQllcLocalSap = _H3cQllcLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 4, 1, 1, 3),
    _H3cQllcLocalSap_Type()
)
h3cQllcLocalSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQllcLocalSap.setStatus("current")


class _H3cQllcRemoteMac_Type(MacAddressNC):
    """Custom type h3cQllcRemoteMac based on MacAddressNC"""
    defaultHexValue = ""


_H3cQllcRemoteMac_Object = MibTableColumn
h3cQllcRemoteMac = _H3cQllcRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 4, 1, 1, 4),
    _H3cQllcRemoteMac_Type()
)
h3cQllcRemoteMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQllcRemoteMac.setStatus("current")


class _H3cQllcRemoteSap_Type(OctetString):
    """Custom type h3cQllcRemoteSap based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_H3cQllcRemoteSap_Type.__name__ = "OctetString"
_H3cQllcRemoteSap_Object = MibTableColumn
h3cQllcRemoteSap = _H3cQllcRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 4, 1, 1, 5),
    _H3cQllcRemoteSap_Type()
)
h3cQllcRemoteSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQllcRemoteSap.setStatus("current")
_H3cQllcRowStatus_Type = RowStatus
_H3cQllcRowStatus_Object = MibTableColumn
h3cQllcRowStatus = _H3cQllcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 4, 1, 1, 6),
    _H3cQllcRowStatus_Type()
)
h3cQllcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQllcRowStatus.setStatus("current")
_H3cdeSdlc_ObjectIdentity = ObjectIdentity
h3cdeSdlc = _H3cdeSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5)
)
_H3cdeSdlcPortTable_Object = MibTable
h3cdeSdlcPortTable = _H3cdeSdlcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1)
)
if mibBuilder.loadTexts:
    h3cdeSdlcPortTable.setStatus("current")
_H3cdeSdlcPortEntry_Object = MibTableRow
h3cdeSdlcPortEntry = _H3cdeSdlcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1)
)
h3cdeSdlcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cdeSdlcPortEntry.setStatus("current")


class _H3cdeSdlcPortRole_Type(Integer32):
    """Custom type h3cdeSdlcPortRole based on Integer32"""
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


_H3cdeSdlcPortRole_Type.__name__ = "Integer32"
_H3cdeSdlcPortRole_Object = MibTableColumn
h3cdeSdlcPortRole = _H3cdeSdlcPortRole_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 1),
    _H3cdeSdlcPortRole_Type()
)
h3cdeSdlcPortRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortRole.setStatus("current")


class _H3cdeSdlcPortSendWindow_Type(Integer32):
    """Custom type h3cdeSdlcPortSendWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_H3cdeSdlcPortSendWindow_Type.__name__ = "Integer32"
_H3cdeSdlcPortSendWindow_Object = MibTableColumn
h3cdeSdlcPortSendWindow = _H3cdeSdlcPortSendWindow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 2),
    _H3cdeSdlcPortSendWindow_Type()
)
h3cdeSdlcPortSendWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortSendWindow.setStatus("current")


class _H3cdeSdlcPortModulo_Type(Integer32):
    """Custom type h3cdeSdlcPortModulo based on Integer32"""
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


_H3cdeSdlcPortModulo_Type.__name__ = "Integer32"
_H3cdeSdlcPortModulo_Object = MibTableColumn
h3cdeSdlcPortModulo = _H3cdeSdlcPortModulo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 3),
    _H3cdeSdlcPortModulo_Type()
)
h3cdeSdlcPortModulo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortModulo.setStatus("current")


class _H3cdeSdlcPortMaxPdu_Type(Integer32):
    """Custom type h3cdeSdlcPortMaxPdu based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17600),
    )


_H3cdeSdlcPortMaxPdu_Type.__name__ = "Integer32"
_H3cdeSdlcPortMaxPdu_Object = MibTableColumn
h3cdeSdlcPortMaxPdu = _H3cdeSdlcPortMaxPdu_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 4),
    _H3cdeSdlcPortMaxPdu_Type()
)
h3cdeSdlcPortMaxPdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortMaxPdu.setStatus("current")


class _H3cdeSdlcPortMaxSendQueue_Type(Integer32):
    """Custom type h3cdeSdlcPortMaxSendQueue based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_H3cdeSdlcPortMaxSendQueue_Type.__name__ = "Integer32"
_H3cdeSdlcPortMaxSendQueue_Object = MibTableColumn
h3cdeSdlcPortMaxSendQueue = _H3cdeSdlcPortMaxSendQueue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 5),
    _H3cdeSdlcPortMaxSendQueue_Type()
)
h3cdeSdlcPortMaxSendQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortMaxSendQueue.setStatus("current")


class _H3cdeSdlcPortMaxTransmission_Type(Integer32):
    """Custom type h3cdeSdlcPortMaxTransmission based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cdeSdlcPortMaxTransmission_Type.__name__ = "Integer32"
_H3cdeSdlcPortMaxTransmission_Object = MibTableColumn
h3cdeSdlcPortMaxTransmission = _H3cdeSdlcPortMaxTransmission_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 6),
    _H3cdeSdlcPortMaxTransmission_Type()
)
h3cdeSdlcPortMaxTransmission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortMaxTransmission.setStatus("current")


class _H3cdeSdlcPortSimultaneousEnable_Type(Integer32):
    """Custom type h3cdeSdlcPortSimultaneousEnable based on Integer32"""
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


_H3cdeSdlcPortSimultaneousEnable_Type.__name__ = "Integer32"
_H3cdeSdlcPortSimultaneousEnable_Object = MibTableColumn
h3cdeSdlcPortSimultaneousEnable = _H3cdeSdlcPortSimultaneousEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 7),
    _H3cdeSdlcPortSimultaneousEnable_Type()
)
h3cdeSdlcPortSimultaneousEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortSimultaneousEnable.setStatus("current")


class _H3cdeSdlcPortTimerACK_Type(Integer32):
    """Custom type h3cdeSdlcPortTimerACK based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_H3cdeSdlcPortTimerACK_Type.__name__ = "Integer32"
_H3cdeSdlcPortTimerACK_Object = MibTableColumn
h3cdeSdlcPortTimerACK = _H3cdeSdlcPortTimerACK_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 8),
    _H3cdeSdlcPortTimerACK_Type()
)
h3cdeSdlcPortTimerACK.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortTimerACK.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeSdlcPortTimerACK.setUnits("milliseconds")


class _H3cdeSdlcPortTimerLifeTime_Type(Integer32):
    """Custom type h3cdeSdlcPortTimerLifeTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_H3cdeSdlcPortTimerLifeTime_Type.__name__ = "Integer32"
_H3cdeSdlcPortTimerLifeTime_Object = MibTableColumn
h3cdeSdlcPortTimerLifeTime = _H3cdeSdlcPortTimerLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 9),
    _H3cdeSdlcPortTimerLifeTime_Type()
)
h3cdeSdlcPortTimerLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortTimerLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeSdlcPortTimerLifeTime.setUnits("milliseconds")


class _H3cdeSdlcPortTimerPollPause_Type(Integer32):
    """Custom type h3cdeSdlcPortTimerPollPause based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_H3cdeSdlcPortTimerPollPause_Type.__name__ = "Integer32"
_H3cdeSdlcPortTimerPollPause_Object = MibTableColumn
h3cdeSdlcPortTimerPollPause = _H3cdeSdlcPortTimerPollPause_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 10),
    _H3cdeSdlcPortTimerPollPause_Type()
)
h3cdeSdlcPortTimerPollPause.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortTimerPollPause.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeSdlcPortTimerPollPause.setUnits("milliseconds")
_H3cdeSdlcPortRowStatus_Type = RowStatus
_H3cdeSdlcPortRowStatus_Object = MibTableColumn
h3cdeSdlcPortRowStatus = _H3cdeSdlcPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 5, 1, 1, 11),
    _H3cdeSdlcPortRowStatus_Type()
)
h3cdeSdlcPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeSdlcPortRowStatus.setStatus("current")
_H3cdeLlc2_ObjectIdentity = ObjectIdentity
h3cdeLlc2 = _H3cdeLlc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6)
)
_H3cdeLlc2PortTable_Object = MibTable
h3cdeLlc2PortTable = _H3cdeLlc2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1)
)
if mibBuilder.loadTexts:
    h3cdeLlc2PortTable.setStatus("current")
_H3cdeLlc2PortEntry_Object = MibTableRow
h3cdeLlc2PortEntry = _H3cdeLlc2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1)
)
h3cdeLlc2PortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cdeLlc2PortEntry.setStatus("current")


class _H3cdeLlc2PortMaxAck_Type(Integer32):
    """Custom type h3cdeLlc2PortMaxAck based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_H3cdeLlc2PortMaxAck_Type.__name__ = "Integer32"
_H3cdeLlc2PortMaxAck_Object = MibTableColumn
h3cdeLlc2PortMaxAck = _H3cdeLlc2PortMaxAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 1),
    _H3cdeLlc2PortMaxAck_Type()
)
h3cdeLlc2PortMaxAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortMaxAck.setStatus("current")


class _H3cdeLlc2PortMaxPdu_Type(Integer32):
    """Custom type h3cdeLlc2PortMaxPdu based on Integer32"""
    defaultValue = 1493

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1700),
    )


_H3cdeLlc2PortMaxPdu_Type.__name__ = "Integer32"
_H3cdeLlc2PortMaxPdu_Object = MibTableColumn
h3cdeLlc2PortMaxPdu = _H3cdeLlc2PortMaxPdu_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 2),
    _H3cdeLlc2PortMaxPdu_Type()
)
h3cdeLlc2PortMaxPdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortMaxPdu.setStatus("current")


class _H3cdeLlc2PortMaxSendQueue_Type(Integer32):
    """Custom type h3cdeLlc2PortMaxSendQueue based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_H3cdeLlc2PortMaxSendQueue_Type.__name__ = "Integer32"
_H3cdeLlc2PortMaxSendQueue_Object = MibTableColumn
h3cdeLlc2PortMaxSendQueue = _H3cdeLlc2PortMaxSendQueue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 3),
    _H3cdeLlc2PortMaxSendQueue_Type()
)
h3cdeLlc2PortMaxSendQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortMaxSendQueue.setStatus("current")


class _H3cdeLlc2PortMaxTransmission_Type(Integer32):
    """Custom type h3cdeLlc2PortMaxTransmission based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cdeLlc2PortMaxTransmission_Type.__name__ = "Integer32"
_H3cdeLlc2PortMaxTransmission_Object = MibTableColumn
h3cdeLlc2PortMaxTransmission = _H3cdeLlc2PortMaxTransmission_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 4),
    _H3cdeLlc2PortMaxTransmission_Type()
)
h3cdeLlc2PortMaxTransmission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortMaxTransmission.setStatus("current")


class _H3cdeLlc2PortModulo_Type(Integer32):
    """Custom type h3cdeLlc2PortModulo based on Integer32"""
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


_H3cdeLlc2PortModulo_Type.__name__ = "Integer32"
_H3cdeLlc2PortModulo_Object = MibTableColumn
h3cdeLlc2PortModulo = _H3cdeLlc2PortModulo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 5),
    _H3cdeLlc2PortModulo_Type()
)
h3cdeLlc2PortModulo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortModulo.setStatus("current")


class _H3cdeLlc2PortReceiveWindow_Type(Integer32):
    """Custom type h3cdeLlc2PortReceiveWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_H3cdeLlc2PortReceiveWindow_Type.__name__ = "Integer32"
_H3cdeLlc2PortReceiveWindow_Object = MibTableColumn
h3cdeLlc2PortReceiveWindow = _H3cdeLlc2PortReceiveWindow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 6),
    _H3cdeLlc2PortReceiveWindow_Type()
)
h3cdeLlc2PortReceiveWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortReceiveWindow.setStatus("current")


class _H3cdeLlc2PortTimerAck_Type(Integer32):
    """Custom type h3cdeLlc2PortTimerAck based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_H3cdeLlc2PortTimerAck_Type.__name__ = "Integer32"
_H3cdeLlc2PortTimerAck_Object = MibTableColumn
h3cdeLlc2PortTimerAck = _H3cdeLlc2PortTimerAck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 7),
    _H3cdeLlc2PortTimerAck_Type()
)
h3cdeLlc2PortTimerAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerAck.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerAck.setUnits("milliseconds")


class _H3cdeLlc2PortTimerAckDelay_Type(Integer32):
    """Custom type h3cdeLlc2PortTimerAckDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_H3cdeLlc2PortTimerAckDelay_Type.__name__ = "Integer32"
_H3cdeLlc2PortTimerAckDelay_Object = MibTableColumn
h3cdeLlc2PortTimerAckDelay = _H3cdeLlc2PortTimerAckDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 8),
    _H3cdeLlc2PortTimerAckDelay_Type()
)
h3cdeLlc2PortTimerAckDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerAckDelay.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerAckDelay.setUnits("milliseconds")


class _H3cdeLlc2PortTimerDetect_Type(Integer32):
    """Custom type h3cdeLlc2PortTimerDetect based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_H3cdeLlc2PortTimerDetect_Type.__name__ = "Integer32"
_H3cdeLlc2PortTimerDetect_Object = MibTableColumn
h3cdeLlc2PortTimerDetect = _H3cdeLlc2PortTimerDetect_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 9),
    _H3cdeLlc2PortTimerDetect_Type()
)
h3cdeLlc2PortTimerDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerDetect.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerDetect.setUnits("milliseconds")


class _H3cdeLlc2PortTimerBusy_Type(Integer32):
    """Custom type h3cdeLlc2PortTimerBusy based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_H3cdeLlc2PortTimerBusy_Type.__name__ = "Integer32"
_H3cdeLlc2PortTimerBusy_Object = MibTableColumn
h3cdeLlc2PortTimerBusy = _H3cdeLlc2PortTimerBusy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 10),
    _H3cdeLlc2PortTimerBusy_Type()
)
h3cdeLlc2PortTimerBusy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerBusy.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerBusy.setUnits("milliseconds")


class _H3cdeLlc2PortTimerPoll_Type(Integer32):
    """Custom type h3cdeLlc2PortTimerPoll based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_H3cdeLlc2PortTimerPoll_Type.__name__ = "Integer32"
_H3cdeLlc2PortTimerPoll_Object = MibTableColumn
h3cdeLlc2PortTimerPoll = _H3cdeLlc2PortTimerPoll_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 11),
    _H3cdeLlc2PortTimerPoll_Type()
)
h3cdeLlc2PortTimerPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerPoll.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerPoll.setUnits("milliseconds")


class _H3cdeLlc2PortTimerReject_Type(Integer32):
    """Custom type h3cdeLlc2PortTimerReject based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_H3cdeLlc2PortTimerReject_Type.__name__ = "Integer32"
_H3cdeLlc2PortTimerReject_Object = MibTableColumn
h3cdeLlc2PortTimerReject = _H3cdeLlc2PortTimerReject_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 12),
    _H3cdeLlc2PortTimerReject_Type()
)
h3cdeLlc2PortTimerReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerReject.setStatus("current")
if mibBuilder.loadTexts:
    h3cdeLlc2PortTimerReject.setUnits("milliseconds")
_H3cdeLlc2PortRowStatus_Type = RowStatus
_H3cdeLlc2PortRowStatus_Object = MibTableColumn
h3cdeLlc2PortRowStatus = _H3cdeLlc2PortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 6, 1, 1, 13),
    _H3cdeLlc2PortRowStatus_Type()
)
h3cdeLlc2PortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeLlc2PortRowStatus.setStatus("current")
_H3cdeReachableCache_ObjectIdentity = ObjectIdentity
h3cdeReachableCache = _H3cdeReachableCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7)
)
_H3cdeRchCacheStat_ObjectIdentity = ObjectIdentity
h3cdeRchCacheStat = _H3cdeRchCacheStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 1)
)
_H3cdeRchCacheMaxIndex_Type = Integer32
_H3cdeRchCacheMaxIndex_Object = MibScalar
h3cdeRchCacheMaxIndex = _H3cdeRchCacheMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 1, 1),
    _H3cdeRchCacheMaxIndex_Type()
)
h3cdeRchCacheMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeRchCacheMaxIndex.setStatus("current")
_H3cdeRchCacheNextIndex_Type = Integer32
_H3cdeRchCacheNextIndex_Object = MibScalar
h3cdeRchCacheNextIndex = _H3cdeRchCacheNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 1, 2),
    _H3cdeRchCacheNextIndex_Type()
)
h3cdeRchCacheNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeRchCacheNextIndex.setStatus("current")
_H3cdeRchCacheTable_Object = MibTable
h3cdeRchCacheTable = _H3cdeRchCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 3)
)
if mibBuilder.loadTexts:
    h3cdeRchCacheTable.setStatus("current")
_H3cdeRchCacheEntry_Object = MibTableRow
h3cdeRchCacheEntry = _H3cdeRchCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 3, 1)
)
h3cdeRchCacheEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SNA-DLSW-EXT-MIB", "h3cdeRchCacheIndex"),
)
if mibBuilder.loadTexts:
    h3cdeRchCacheEntry.setStatus("current")
_H3cdeRchCacheIndex_Type = Integer32
_H3cdeRchCacheIndex_Object = MibTableColumn
h3cdeRchCacheIndex = _H3cdeRchCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 3, 1, 1),
    _H3cdeRchCacheIndex_Type()
)
h3cdeRchCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cdeRchCacheIndex.setStatus("current")


class _H3cdeRchCacheStatus_Type(Integer32):
    """Custom type h3cdeRchCacheStatus based on Integer32"""
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


_H3cdeRchCacheStatus_Type.__name__ = "Integer32"
_H3cdeRchCacheStatus_Object = MibTableColumn
h3cdeRchCacheStatus = _H3cdeRchCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 3, 1, 2),
    _H3cdeRchCacheStatus_Type()
)
h3cdeRchCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeRchCacheStatus.setStatus("current")
_H3cdeRchCacheRemainTime_Type = TimeTicks
_H3cdeRchCacheRemainTime_Object = MibTableColumn
h3cdeRchCacheRemainTime = _H3cdeRchCacheRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 3, 1, 3),
    _H3cdeRchCacheRemainTime_Type()
)
h3cdeRchCacheRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeRchCacheRemainTime.setStatus("current")
_H3cdeRchCacheMac_Type = MacAddressNC
_H3cdeRchCacheMac_Object = MibTableColumn
h3cdeRchCacheMac = _H3cdeRchCacheMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 3, 1, 4),
    _H3cdeRchCacheMac_Type()
)
h3cdeRchCacheMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeRchCacheMac.setStatus("current")
_H3cdeRchCacheRemoteIpAddrType_Type = InetAddressType
_H3cdeRchCacheRemoteIpAddrType_Object = MibTableColumn
h3cdeRchCacheRemoteIpAddrType = _H3cdeRchCacheRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 3, 1, 5),
    _H3cdeRchCacheRemoteIpAddrType_Type()
)
h3cdeRchCacheRemoteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeRchCacheRemoteIpAddrType.setStatus("current")
_H3cdeRchCacheRemoteIp_Type = InetAddress
_H3cdeRchCacheRemoteIp_Object = MibTableColumn
h3cdeRchCacheRemoteIp = _H3cdeRchCacheRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 3, 1, 6),
    _H3cdeRchCacheRemoteIp_Type()
)
h3cdeRchCacheRemoteIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeRchCacheRemoteIp.setStatus("current")
_H3cdeRchCacheRowStatus_Type = RowStatus
_H3cdeRchCacheRowStatus_Object = MibTableColumn
h3cdeRchCacheRowStatus = _H3cdeRchCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 7, 3, 1, 7),
    _H3cdeRchCacheRowStatus_Type()
)
h3cdeRchCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeRchCacheRowStatus.setStatus("current")
_H3cdeEthernetBackup_ObjectIdentity = ObjectIdentity
h3cdeEthernetBackup = _H3cdeEthernetBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8)
)
_H3cdeEBMacMapStat_ObjectIdentity = ObjectIdentity
h3cdeEBMacMapStat = _H3cdeEBMacMapStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 1)
)
_H3cdeEBMacMapMaxIndex_Type = Integer32
_H3cdeEBMacMapMaxIndex_Object = MibScalar
h3cdeEBMacMapMaxIndex = _H3cdeEBMacMapMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 1, 1),
    _H3cdeEBMacMapMaxIndex_Type()
)
h3cdeEBMacMapMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeEBMacMapMaxIndex.setStatus("current")
_H3cdeEBMacMapNextIndex_Type = Integer32
_H3cdeEBMacMapNextIndex_Object = MibScalar
h3cdeEBMacMapNextIndex = _H3cdeEBMacMapNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 1, 2),
    _H3cdeEBMacMapNextIndex_Type()
)
h3cdeEBMacMapNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cdeEBMacMapNextIndex.setStatus("current")
_H3cdeEBIfTable_Object = MibTable
h3cdeEBIfTable = _H3cdeEBIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 3)
)
if mibBuilder.loadTexts:
    h3cdeEBIfTable.setStatus("current")
_H3cdeEBIfEntry_Object = MibTableRow
h3cdeEBIfEntry = _H3cdeEBIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 3, 1)
)
h3cdeEBIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cdeEBIfEntry.setStatus("current")


class _H3cdeEBMulticastMac_Type(MacAddressNC):
    """Custom type h3cdeEBMulticastMac based on MacAddressNC"""
    defaultHexValue = "000000000000"


_H3cdeEBMulticastMac_Object = MibTableColumn
h3cdeEBMulticastMac = _H3cdeEBMulticastMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 3, 1, 1),
    _H3cdeEBMulticastMac_Type()
)
h3cdeEBMulticastMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeEBMulticastMac.setStatus("current")


class _H3cdeEBPriority_Type(Integer32):
    """Custom type h3cdeEBPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_H3cdeEBPriority_Type.__name__ = "Integer32"
_H3cdeEBPriority_Object = MibTableColumn
h3cdeEBPriority = _H3cdeEBPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 3, 1, 2),
    _H3cdeEBPriority_Type()
)
h3cdeEBPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeEBPriority.setStatus("current")


class _H3cdeEBtimer_Type(Integer32):
    """Custom type h3cdeEBtimer based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_H3cdeEBtimer_Type.__name__ = "Integer32"
_H3cdeEBtimer_Object = MibTableColumn
h3cdeEBtimer = _H3cdeEBtimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 3, 1, 3),
    _H3cdeEBtimer_Type()
)
h3cdeEBtimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeEBtimer.setStatus("current")
_H3cdeEBRowStatus_Type = RowStatus
_H3cdeEBRowStatus_Object = MibTableColumn
h3cdeEBRowStatus = _H3cdeEBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 3, 1, 4),
    _H3cdeEBRowStatus_Type()
)
h3cdeEBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeEBRowStatus.setStatus("current")
_H3cdeEBMacMapTable_Object = MibTable
h3cdeEBMacMapTable = _H3cdeEBMacMapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 4)
)
if mibBuilder.loadTexts:
    h3cdeEBMacMapTable.setStatus("current")
_H3cdeEBMacMapEntry_Object = MibTableRow
h3cdeEBMacMapEntry = _H3cdeEBMacMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 4, 1)
)
h3cdeEBMacMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-SNA-DLSW-EXT-MIB", "h3cdeEBMacMapIndex"),
)
if mibBuilder.loadTexts:
    h3cdeEBMacMapEntry.setStatus("current")
_H3cdeEBMacMapIndex_Type = Integer32
_H3cdeEBMacMapIndex_Object = MibTableColumn
h3cdeEBMacMapIndex = _H3cdeEBMacMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 4, 1, 1),
    _H3cdeEBMacMapIndex_Type()
)
h3cdeEBMacMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cdeEBMacMapIndex.setStatus("current")
_H3cdeEBMacMapLocalMac_Type = MacAddressNC
_H3cdeEBMacMapLocalMac_Object = MibTableColumn
h3cdeEBMacMapLocalMac = _H3cdeEBMacMapLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 4, 1, 2),
    _H3cdeEBMacMapLocalMac_Type()
)
h3cdeEBMacMapLocalMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeEBMacMapLocalMac.setStatus("current")
_H3cdeEBMacMapRemoteMac_Type = MacAddressNC
_H3cdeEBMacMapRemoteMac_Object = MibTableColumn
h3cdeEBMacMapRemoteMac = _H3cdeEBMacMapRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 4, 1, 3),
    _H3cdeEBMacMapRemoteMac_Type()
)
h3cdeEBMacMapRemoteMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeEBMacMapRemoteMac.setStatus("current")
_H3cdeEBMacMapNeighbour_Type = MacAddressNC
_H3cdeEBMacMapNeighbour_Object = MibTableColumn
h3cdeEBMacMapNeighbour = _H3cdeEBMacMapNeighbour_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 4, 1, 4),
    _H3cdeEBMacMapNeighbour_Type()
)
h3cdeEBMacMapNeighbour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeEBMacMapNeighbour.setStatus("current")
_H3cdeEBMacMapRowStatus_Type = RowStatus
_H3cdeEBMacMapRowStatus_Object = MibTableColumn
h3cdeEBMacMapRowStatus = _H3cdeEBMacMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 62, 1, 8, 4, 1, 5),
    _H3cdeEBMacMapRowStatus_Type()
)
h3cdeEBMacMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cdeEBMacMapRowStatus.setStatus("current")
dlswTConnConfigEntry.registerAugmentions(
    ("A3COM-HUAWEI-SNA-DLSW-EXT-MIB",
     "h3cdeTConnConfigEntry")
)
h3cdeTConnConfigEntry.setIndexNames(*dlswTConnConfigEntry.getIndexNames())
dlswTConnOperEntry.registerAugmentions(
    ("A3COM-HUAWEI-SNA-DLSW-EXT-MIB",
     "h3cdeTConnOperEntry")
)
h3cdeTConnOperEntry.setIndexNames(*dlswTConnOperEntry.getIndexNames())
dlswTConnTcpConfigEntry.registerAugmentions(
    ("A3COM-HUAWEI-SNA-DLSW-EXT-MIB",
     "h3cdeTConnTcpConfigEntry")
)
h3cdeTConnTcpConfigEntry.setIndexNames(*dlswTConnTcpConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-SNA-DLSW-EXT-MIB",
    **{"h3cDlswExt": h3cDlswExt,
       "h3cDlswExtMIBObjects": h3cDlswExtMIBObjects,
       "h3cdeNode": h3cdeNode,
       "h3cdeNodeVendorID": h3cdeNodeVendorID,
       "h3cdeNodeIpAddrType": h3cdeNodeIpAddrType,
       "h3cdeNodeLocalAddr": h3cdeNodeLocalAddr,
       "h3cdeNodePriority": h3cdeNodePriority,
       "h3cdeNodeInitPacingWindow": h3cdeNodeInitPacingWindow,
       "h3cdeNodeMaxPacingWindow": h3cdeNodeMaxPacingWindow,
       "h3cdeNodeKeepAliveInterval": h3cdeNodeKeepAliveInterval,
       "h3cdeNodePermitDynamic": h3cdeNodePermitDynamic,
       "h3cdeNodeConnTimeout": h3cdeNodeConnTimeout,
       "h3cdeNodeLocalPendTimeout": h3cdeNodeLocalPendTimeout,
       "h3cdeNodeRemotePendTimeout": h3cdeNodeRemotePendTimeout,
       "h3cdeNodeSnaCacheTimeout": h3cdeNodeSnaCacheTimeout,
       "h3cdeNodeExplorerTimeout": h3cdeNodeExplorerTimeout,
       "h3cdeNodeExplorerWaitTimeout": h3cdeNodeExplorerWaitTimeout,
       "h3cdeNodeConfigSapList": h3cdeNodeConfigSapList,
       "h3cdeNodeMaxTransmission": h3cdeNodeMaxTransmission,
       "h3cdeNodeMulticastStatus": h3cdeNodeMulticastStatus,
       "h3cdeNodeMulticastAddress": h3cdeNodeMulticastAddress,
       "h3cdeNodeResetTcpAll": h3cdeNodeResetTcpAll,
       "h3cdeNodeStCapTcpNum": h3cdeNodeStCapTcpNum,
       "h3cdeNodeTcpQueueMax": h3cdeNodeTcpQueueMax,
       "h3cdeTConn": h3cdeTConn,
       "h3cdeTConnConfigTable": h3cdeTConnConfigTable,
       "h3cdeTConnConfigEntry": h3cdeTConnConfigEntry,
       "h3cdeTConnConfigVersion": h3cdeTConnConfigVersion,
       "h3cdeTConnConfigPriority": h3cdeTConnConfigPriority,
       "h3cdeTConnConfigLfSize": h3cdeTConnConfigLfSize,
       "h3cdeTConnConfigKeepaliveIntval": h3cdeTConnConfigKeepaliveIntval,
       "h3cdeTConnConfigBackup": h3cdeTConnConfigBackup,
       "h3cdeTConnConfigBackupTAddr": h3cdeTConnConfigBackupTAddr,
       "h3cdeTConnConfigBackupLinger": h3cdeTConnConfigBackupLinger,
       "h3cdeTConnOperTable": h3cdeTConnOperTable,
       "h3cdeTConnOperEntry": h3cdeTConnOperEntry,
       "h3cdeTConnOperPeerType": h3cdeTConnOperPeerType,
       "h3cdeTConnOperVendorID": h3cdeTConnOperVendorID,
       "h3cdeTConnOperVersionString": h3cdeTConnOperVersionString,
       "h3cdeTConnOperUpTime": h3cdeTConnOperUpTime,
       "h3cdeTConnOperMulticastAddress": h3cdeTConnOperMulticastAddress,
       "h3cdeTConnOperStCapTcpNumber": h3cdeTConnOperStCapTcpNumber,
       "h3cdeTConnOperRecvPkts": h3cdeTConnOperRecvPkts,
       "h3cdeTConnOperSendPkts": h3cdeTConnOperSendPkts,
       "h3cdeTConnOperDropPkts": h3cdeTConnOperDropPkts,
       "h3cdeTConnTcpConfigTable": h3cdeTConnTcpConfigTable,
       "h3cdeTConnTcpConfigEntry": h3cdeTConnTcpConfigEntry,
       "h3cdeTConnTcpConfigQueueMax": h3cdeTConnTcpConfigQueueMax,
       "h3cdeBridge": h3cdeBridge,
       "h3cdeBridgeTable": h3cdeBridgeTable,
       "h3cdeBridgeEntry": h3cdeBridgeEntry,
       "h3cdeBridgeNumIndex": h3cdeBridgeNumIndex,
       "h3cdeBridgeRowStatus": h3cdeBridgeRowStatus,
       "h3cdeBridgeIfTable": h3cdeBridgeIfTable,
       "h3cdeBridgeIfEntry": h3cdeBridgeIfEntry,
       "h3cdeBridgeIfBrgGrp": h3cdeBridgeIfBrgGrp,
       "h3cdeBridgeIfRowStatus": h3cdeBridgeIfRowStatus,
       "h3cdeQllc": h3cdeQllc,
       "h3cdeQllcTable": h3cdeQllcTable,
       "h3cdeQllcEntry": h3cdeQllcEntry,
       "h3cQllcX121Address": h3cQllcX121Address,
       "h3cQllcLocalMac": h3cQllcLocalMac,
       "h3cQllcLocalSap": h3cQllcLocalSap,
       "h3cQllcRemoteMac": h3cQllcRemoteMac,
       "h3cQllcRemoteSap": h3cQllcRemoteSap,
       "h3cQllcRowStatus": h3cQllcRowStatus,
       "h3cdeSdlc": h3cdeSdlc,
       "h3cdeSdlcPortTable": h3cdeSdlcPortTable,
       "h3cdeSdlcPortEntry": h3cdeSdlcPortEntry,
       "h3cdeSdlcPortRole": h3cdeSdlcPortRole,
       "h3cdeSdlcPortSendWindow": h3cdeSdlcPortSendWindow,
       "h3cdeSdlcPortModulo": h3cdeSdlcPortModulo,
       "h3cdeSdlcPortMaxPdu": h3cdeSdlcPortMaxPdu,
       "h3cdeSdlcPortMaxSendQueue": h3cdeSdlcPortMaxSendQueue,
       "h3cdeSdlcPortMaxTransmission": h3cdeSdlcPortMaxTransmission,
       "h3cdeSdlcPortSimultaneousEnable": h3cdeSdlcPortSimultaneousEnable,
       "h3cdeSdlcPortTimerACK": h3cdeSdlcPortTimerACK,
       "h3cdeSdlcPortTimerLifeTime": h3cdeSdlcPortTimerLifeTime,
       "h3cdeSdlcPortTimerPollPause": h3cdeSdlcPortTimerPollPause,
       "h3cdeSdlcPortRowStatus": h3cdeSdlcPortRowStatus,
       "h3cdeLlc2": h3cdeLlc2,
       "h3cdeLlc2PortTable": h3cdeLlc2PortTable,
       "h3cdeLlc2PortEntry": h3cdeLlc2PortEntry,
       "h3cdeLlc2PortMaxAck": h3cdeLlc2PortMaxAck,
       "h3cdeLlc2PortMaxPdu": h3cdeLlc2PortMaxPdu,
       "h3cdeLlc2PortMaxSendQueue": h3cdeLlc2PortMaxSendQueue,
       "h3cdeLlc2PortMaxTransmission": h3cdeLlc2PortMaxTransmission,
       "h3cdeLlc2PortModulo": h3cdeLlc2PortModulo,
       "h3cdeLlc2PortReceiveWindow": h3cdeLlc2PortReceiveWindow,
       "h3cdeLlc2PortTimerAck": h3cdeLlc2PortTimerAck,
       "h3cdeLlc2PortTimerAckDelay": h3cdeLlc2PortTimerAckDelay,
       "h3cdeLlc2PortTimerDetect": h3cdeLlc2PortTimerDetect,
       "h3cdeLlc2PortTimerBusy": h3cdeLlc2PortTimerBusy,
       "h3cdeLlc2PortTimerPoll": h3cdeLlc2PortTimerPoll,
       "h3cdeLlc2PortTimerReject": h3cdeLlc2PortTimerReject,
       "h3cdeLlc2PortRowStatus": h3cdeLlc2PortRowStatus,
       "h3cdeReachableCache": h3cdeReachableCache,
       "h3cdeRchCacheStat": h3cdeRchCacheStat,
       "h3cdeRchCacheMaxIndex": h3cdeRchCacheMaxIndex,
       "h3cdeRchCacheNextIndex": h3cdeRchCacheNextIndex,
       "h3cdeRchCacheTable": h3cdeRchCacheTable,
       "h3cdeRchCacheEntry": h3cdeRchCacheEntry,
       "h3cdeRchCacheIndex": h3cdeRchCacheIndex,
       "h3cdeRchCacheStatus": h3cdeRchCacheStatus,
       "h3cdeRchCacheRemainTime": h3cdeRchCacheRemainTime,
       "h3cdeRchCacheMac": h3cdeRchCacheMac,
       "h3cdeRchCacheRemoteIpAddrType": h3cdeRchCacheRemoteIpAddrType,
       "h3cdeRchCacheRemoteIp": h3cdeRchCacheRemoteIp,
       "h3cdeRchCacheRowStatus": h3cdeRchCacheRowStatus,
       "h3cdeEthernetBackup": h3cdeEthernetBackup,
       "h3cdeEBMacMapStat": h3cdeEBMacMapStat,
       "h3cdeEBMacMapMaxIndex": h3cdeEBMacMapMaxIndex,
       "h3cdeEBMacMapNextIndex": h3cdeEBMacMapNextIndex,
       "h3cdeEBIfTable": h3cdeEBIfTable,
       "h3cdeEBIfEntry": h3cdeEBIfEntry,
       "h3cdeEBMulticastMac": h3cdeEBMulticastMac,
       "h3cdeEBPriority": h3cdeEBPriority,
       "h3cdeEBtimer": h3cdeEBtimer,
       "h3cdeEBRowStatus": h3cdeEBRowStatus,
       "h3cdeEBMacMapTable": h3cdeEBMacMapTable,
       "h3cdeEBMacMapEntry": h3cdeEBMacMapEntry,
       "h3cdeEBMacMapIndex": h3cdeEBMacMapIndex,
       "h3cdeEBMacMapLocalMac": h3cdeEBMacMapLocalMac,
       "h3cdeEBMacMapRemoteMac": h3cdeEBMacMapRemoteMac,
       "h3cdeEBMacMapNeighbour": h3cdeEBMacMapNeighbour,
       "h3cdeEBMacMapRowStatus": h3cdeEBMacMapRowStatus}
)
