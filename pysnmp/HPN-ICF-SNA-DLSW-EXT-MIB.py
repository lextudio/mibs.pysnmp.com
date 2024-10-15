# SNMP MIB module (HPN-ICF-SNA-DLSW-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SNA-DLSW-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:50 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfDlswExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62)
)
hpnicfDlswExt.setRevisions(
        ("2005-07-20 19:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDlswExtMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfDlswExtMIBObjects = _HpnicfDlswExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1)
)
_HpnicfdeNode_ObjectIdentity = ObjectIdentity
hpnicfdeNode = _HpnicfdeNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1)
)


class _HpnicfdeNodeVendorID_Type(OctetString):
    """Custom type hpnicfdeNodeVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpnicfdeNodeVendorID_Type.__name__ = "OctetString"
_HpnicfdeNodeVendorID_Object = MibScalar
hpnicfdeNodeVendorID = _HpnicfdeNodeVendorID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 1),
    _HpnicfdeNodeVendorID_Type()
)
hpnicfdeNodeVendorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeVendorID.setStatus("current")
_HpnicfdeNodeIpAddrType_Type = InetAddressType
_HpnicfdeNodeIpAddrType_Object = MibScalar
hpnicfdeNodeIpAddrType = _HpnicfdeNodeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 2),
    _HpnicfdeNodeIpAddrType_Type()
)
hpnicfdeNodeIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeIpAddrType.setStatus("current")


class _HpnicfdeNodeLocalAddr_Type(InetAddress):
    """Custom type hpnicfdeNodeLocalAddr based on InetAddress"""
    defaultHexValue = ""


_HpnicfdeNodeLocalAddr_Object = MibScalar
hpnicfdeNodeLocalAddr = _HpnicfdeNodeLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 3),
    _HpnicfdeNodeLocalAddr_Type()
)
hpnicfdeNodeLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeLocalAddr.setStatus("current")


class _HpnicfdeNodePriority_Type(Integer32):
    """Custom type hpnicfdeNodePriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfdeNodePriority_Type.__name__ = "Integer32"
_HpnicfdeNodePriority_Object = MibScalar
hpnicfdeNodePriority = _HpnicfdeNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 4),
    _HpnicfdeNodePriority_Type()
)
hpnicfdeNodePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodePriority.setStatus("current")


class _HpnicfdeNodeInitPacingWindow_Type(Integer32):
    """Custom type hpnicfdeNodeInitPacingWindow based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfdeNodeInitPacingWindow_Type.__name__ = "Integer32"
_HpnicfdeNodeInitPacingWindow_Object = MibScalar
hpnicfdeNodeInitPacingWindow = _HpnicfdeNodeInitPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 5),
    _HpnicfdeNodeInitPacingWindow_Type()
)
hpnicfdeNodeInitPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeInitPacingWindow.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeNodeInitPacingWindow.setUnits("packets")


class _HpnicfdeNodeMaxPacingWindow_Type(Integer32):
    """Custom type hpnicfdeNodeMaxPacingWindow based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfdeNodeMaxPacingWindow_Type.__name__ = "Integer32"
_HpnicfdeNodeMaxPacingWindow_Object = MibScalar
hpnicfdeNodeMaxPacingWindow = _HpnicfdeNodeMaxPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 6),
    _HpnicfdeNodeMaxPacingWindow_Type()
)
hpnicfdeNodeMaxPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeMaxPacingWindow.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeNodeMaxPacingWindow.setUnits("packets")


class _HpnicfdeNodeKeepAliveInterval_Type(Integer32):
    """Custom type hpnicfdeNodeKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfdeNodeKeepAliveInterval_Type.__name__ = "Integer32"
_HpnicfdeNodeKeepAliveInterval_Object = MibScalar
hpnicfdeNodeKeepAliveInterval = _HpnicfdeNodeKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 7),
    _HpnicfdeNodeKeepAliveInterval_Type()
)
hpnicfdeNodeKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeNodeKeepAliveInterval.setUnits("seconds")


class _HpnicfdeNodePermitDynamic_Type(Integer32):
    """Custom type hpnicfdeNodePermitDynamic based on Integer32"""
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


_HpnicfdeNodePermitDynamic_Type.__name__ = "Integer32"
_HpnicfdeNodePermitDynamic_Object = MibScalar
hpnicfdeNodePermitDynamic = _HpnicfdeNodePermitDynamic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 8),
    _HpnicfdeNodePermitDynamic_Type()
)
hpnicfdeNodePermitDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodePermitDynamic.setStatus("current")


class _HpnicfdeNodeConnTimeout_Type(Integer32):
    """Custom type hpnicfdeNodeConnTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfdeNodeConnTimeout_Type.__name__ = "Integer32"
_HpnicfdeNodeConnTimeout_Object = MibScalar
hpnicfdeNodeConnTimeout = _HpnicfdeNodeConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 9),
    _HpnicfdeNodeConnTimeout_Type()
)
hpnicfdeNodeConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeConnTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeNodeConnTimeout.setUnits("seconds")


class _HpnicfdeNodeLocalPendTimeout_Type(Integer32):
    """Custom type hpnicfdeNodeLocalPendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfdeNodeLocalPendTimeout_Type.__name__ = "Integer32"
_HpnicfdeNodeLocalPendTimeout_Object = MibScalar
hpnicfdeNodeLocalPendTimeout = _HpnicfdeNodeLocalPendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 10),
    _HpnicfdeNodeLocalPendTimeout_Type()
)
hpnicfdeNodeLocalPendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeLocalPendTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeNodeLocalPendTimeout.setUnits("seconds")


class _HpnicfdeNodeRemotePendTimeout_Type(Integer32):
    """Custom type hpnicfdeNodeRemotePendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfdeNodeRemotePendTimeout_Type.__name__ = "Integer32"
_HpnicfdeNodeRemotePendTimeout_Object = MibScalar
hpnicfdeNodeRemotePendTimeout = _HpnicfdeNodeRemotePendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 11),
    _HpnicfdeNodeRemotePendTimeout_Type()
)
hpnicfdeNodeRemotePendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeRemotePendTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeNodeRemotePendTimeout.setUnits("seconds")


class _HpnicfdeNodeSnaCacheTimeout_Type(Integer32):
    """Custom type hpnicfdeNodeSnaCacheTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfdeNodeSnaCacheTimeout_Type.__name__ = "Integer32"
_HpnicfdeNodeSnaCacheTimeout_Object = MibScalar
hpnicfdeNodeSnaCacheTimeout = _HpnicfdeNodeSnaCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 12),
    _HpnicfdeNodeSnaCacheTimeout_Type()
)
hpnicfdeNodeSnaCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeSnaCacheTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeNodeSnaCacheTimeout.setUnits("seconds")


class _HpnicfdeNodeExplorerTimeout_Type(Integer32):
    """Custom type hpnicfdeNodeExplorerTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfdeNodeExplorerTimeout_Type.__name__ = "Integer32"
_HpnicfdeNodeExplorerTimeout_Object = MibScalar
hpnicfdeNodeExplorerTimeout = _HpnicfdeNodeExplorerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 13),
    _HpnicfdeNodeExplorerTimeout_Type()
)
hpnicfdeNodeExplorerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeExplorerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeNodeExplorerTimeout.setUnits("seconds")


class _HpnicfdeNodeExplorerWaitTimeout_Type(Integer32):
    """Custom type hpnicfdeNodeExplorerWaitTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfdeNodeExplorerWaitTimeout_Type.__name__ = "Integer32"
_HpnicfdeNodeExplorerWaitTimeout_Object = MibScalar
hpnicfdeNodeExplorerWaitTimeout = _HpnicfdeNodeExplorerWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 14),
    _HpnicfdeNodeExplorerWaitTimeout_Type()
)
hpnicfdeNodeExplorerWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeExplorerWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeNodeExplorerWaitTimeout.setUnits("seconds")


class _HpnicfdeNodeConfigSapList_Type(OctetString):
    """Custom type hpnicfdeNodeConfigSapList based on OctetString"""
    defaultHexValue = "FF000000000000000000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpnicfdeNodeConfigSapList_Type.__name__ = "OctetString"
_HpnicfdeNodeConfigSapList_Object = MibScalar
hpnicfdeNodeConfigSapList = _HpnicfdeNodeConfigSapList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 15),
    _HpnicfdeNodeConfigSapList_Type()
)
hpnicfdeNodeConfigSapList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeConfigSapList.setStatus("current")


class _HpnicfdeNodeMaxTransmission_Type(Integer32):
    """Custom type hpnicfdeNodeMaxTransmission based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpnicfdeNodeMaxTransmission_Type.__name__ = "Integer32"
_HpnicfdeNodeMaxTransmission_Object = MibScalar
hpnicfdeNodeMaxTransmission = _HpnicfdeNodeMaxTransmission_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 16),
    _HpnicfdeNodeMaxTransmission_Type()
)
hpnicfdeNodeMaxTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeMaxTransmission.setStatus("current")


class _HpnicfdeNodeMulticastStatus_Type(Integer32):
    """Custom type hpnicfdeNodeMulticastStatus based on Integer32"""
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


_HpnicfdeNodeMulticastStatus_Type.__name__ = "Integer32"
_HpnicfdeNodeMulticastStatus_Object = MibScalar
hpnicfdeNodeMulticastStatus = _HpnicfdeNodeMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 17),
    _HpnicfdeNodeMulticastStatus_Type()
)
hpnicfdeNodeMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeMulticastStatus.setStatus("current")
_HpnicfdeNodeMulticastAddress_Type = InetAddress
_HpnicfdeNodeMulticastAddress_Object = MibScalar
hpnicfdeNodeMulticastAddress = _HpnicfdeNodeMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 18),
    _HpnicfdeNodeMulticastAddress_Type()
)
hpnicfdeNodeMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeMulticastAddress.setStatus("current")


class _HpnicfdeNodeResetTcpAll_Type(Integer32):
    """Custom type hpnicfdeNodeResetTcpAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfdeNodeResetTcpAll_Type.__name__ = "Integer32"
_HpnicfdeNodeResetTcpAll_Object = MibScalar
hpnicfdeNodeResetTcpAll = _HpnicfdeNodeResetTcpAll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 19),
    _HpnicfdeNodeResetTcpAll_Type()
)
hpnicfdeNodeResetTcpAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeResetTcpAll.setStatus("current")


class _HpnicfdeNodeStCapTcpNum_Type(Integer32):
    """Custom type hpnicfdeNodeStCapTcpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfdeNodeStCapTcpNum_Type.__name__ = "Integer32"
_HpnicfdeNodeStCapTcpNum_Object = MibScalar
hpnicfdeNodeStCapTcpNum = _HpnicfdeNodeStCapTcpNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 20),
    _HpnicfdeNodeStCapTcpNum_Type()
)
hpnicfdeNodeStCapTcpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeStCapTcpNum.setStatus("current")


class _HpnicfdeNodeTcpQueueMax_Type(Integer32):
    """Custom type hpnicfdeNodeTcpQueueMax based on Integer32"""
    defaultValue = 200


_HpnicfdeNodeTcpQueueMax_Object = MibScalar
hpnicfdeNodeTcpQueueMax = _HpnicfdeNodeTcpQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 1, 21),
    _HpnicfdeNodeTcpQueueMax_Type()
)
hpnicfdeNodeTcpQueueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdeNodeTcpQueueMax.setStatus("current")
_HpnicfdeTConn_ObjectIdentity = ObjectIdentity
hpnicfdeTConn = _HpnicfdeTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2)
)
_HpnicfdeTConnConfigTable_Object = MibTable
hpnicfdeTConnConfigTable = _HpnicfdeTConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigTable.setStatus("current")
_HpnicfdeTConnConfigEntry_Object = MibTableRow
hpnicfdeTConnConfigEntry = _HpnicfdeTConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigEntry.setStatus("current")


class _HpnicfdeTConnConfigVersion_Type(OctetString):
    """Custom type hpnicfdeTConnConfigVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HpnicfdeTConnConfigVersion_Type.__name__ = "OctetString"
_HpnicfdeTConnConfigVersion_Object = MibTableColumn
hpnicfdeTConnConfigVersion = _HpnicfdeTConnConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 1),
    _HpnicfdeTConnConfigVersion_Type()
)
hpnicfdeTConnConfigVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigVersion.setStatus("current")


class _HpnicfdeTConnConfigPriority_Type(Integer32):
    """Custom type hpnicfdeTConnConfigPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HpnicfdeTConnConfigPriority_Type.__name__ = "Integer32"
_HpnicfdeTConnConfigPriority_Object = MibTableColumn
hpnicfdeTConnConfigPriority = _HpnicfdeTConnConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 2),
    _HpnicfdeTConnConfigPriority_Type()
)
hpnicfdeTConnConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigPriority.setStatus("current")
_HpnicfdeTConnConfigLfSize_Type = LFSize
_HpnicfdeTConnConfigLfSize_Object = MibTableColumn
hpnicfdeTConnConfigLfSize = _HpnicfdeTConnConfigLfSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 3),
    _HpnicfdeTConnConfigLfSize_Type()
)
hpnicfdeTConnConfigLfSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigLfSize.setStatus("current")


class _HpnicfdeTConnConfigKeepaliveIntval_Type(Integer32):
    """Custom type hpnicfdeTConnConfigKeepaliveIntval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_HpnicfdeTConnConfigKeepaliveIntval_Type.__name__ = "Integer32"
_HpnicfdeTConnConfigKeepaliveIntval_Object = MibTableColumn
hpnicfdeTConnConfigKeepaliveIntval = _HpnicfdeTConnConfigKeepaliveIntval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 4),
    _HpnicfdeTConnConfigKeepaliveIntval_Type()
)
hpnicfdeTConnConfigKeepaliveIntval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigKeepaliveIntval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigKeepaliveIntval.setUnits("seconds")


class _HpnicfdeTConnConfigBackup_Type(Integer32):
    """Custom type hpnicfdeTConnConfigBackup based on Integer32"""
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


_HpnicfdeTConnConfigBackup_Type.__name__ = "Integer32"
_HpnicfdeTConnConfigBackup_Object = MibTableColumn
hpnicfdeTConnConfigBackup = _HpnicfdeTConnConfigBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 5),
    _HpnicfdeTConnConfigBackup_Type()
)
hpnicfdeTConnConfigBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigBackup.setStatus("current")
_HpnicfdeTConnConfigBackupTAddr_Type = TAddress
_HpnicfdeTConnConfigBackupTAddr_Object = MibTableColumn
hpnicfdeTConnConfigBackupTAddr = _HpnicfdeTConnConfigBackupTAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 6),
    _HpnicfdeTConnConfigBackupTAddr_Type()
)
hpnicfdeTConnConfigBackupTAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigBackupTAddr.setStatus("current")


class _HpnicfdeTConnConfigBackupLinger_Type(Integer32):
    """Custom type hpnicfdeTConnConfigBackupLinger based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_HpnicfdeTConnConfigBackupLinger_Type.__name__ = "Integer32"
_HpnicfdeTConnConfigBackupLinger_Object = MibTableColumn
hpnicfdeTConnConfigBackupLinger = _HpnicfdeTConnConfigBackupLinger_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 1, 1, 7),
    _HpnicfdeTConnConfigBackupLinger_Type()
)
hpnicfdeTConnConfigBackupLinger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigBackupLinger.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeTConnConfigBackupLinger.setUnits("minutes")
_HpnicfdeTConnOperTable_Object = MibTable
hpnicfdeTConnOperTable = _HpnicfdeTConnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfdeTConnOperTable.setStatus("current")
_HpnicfdeTConnOperEntry_Object = MibTableRow
hpnicfdeTConnOperEntry = _HpnicfdeTConnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfdeTConnOperEntry.setStatus("current")


class _HpnicfdeTConnOperPeerType_Type(Integer32):
    """Custom type hpnicfdeTConnOperPeerType based on Integer32"""
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


_HpnicfdeTConnOperPeerType_Type.__name__ = "Integer32"
_HpnicfdeTConnOperPeerType_Object = MibTableColumn
hpnicfdeTConnOperPeerType = _HpnicfdeTConnOperPeerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 1),
    _HpnicfdeTConnOperPeerType_Type()
)
hpnicfdeTConnOperPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeTConnOperPeerType.setStatus("current")
_HpnicfdeTConnOperVendorID_Type = OctetString
_HpnicfdeTConnOperVendorID_Object = MibTableColumn
hpnicfdeTConnOperVendorID = _HpnicfdeTConnOperVendorID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 2),
    _HpnicfdeTConnOperVendorID_Type()
)
hpnicfdeTConnOperVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeTConnOperVendorID.setStatus("current")
_HpnicfdeTConnOperVersionString_Type = OctetString
_HpnicfdeTConnOperVersionString_Object = MibTableColumn
hpnicfdeTConnOperVersionString = _HpnicfdeTConnOperVersionString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 3),
    _HpnicfdeTConnOperVersionString_Type()
)
hpnicfdeTConnOperVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeTConnOperVersionString.setStatus("current")
_HpnicfdeTConnOperUpTime_Type = TimeTicks
_HpnicfdeTConnOperUpTime_Object = MibTableColumn
hpnicfdeTConnOperUpTime = _HpnicfdeTConnOperUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 4),
    _HpnicfdeTConnOperUpTime_Type()
)
hpnicfdeTConnOperUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeTConnOperUpTime.setStatus("current")
_HpnicfdeTConnOperMulticastAddress_Type = TAddress
_HpnicfdeTConnOperMulticastAddress_Object = MibTableColumn
hpnicfdeTConnOperMulticastAddress = _HpnicfdeTConnOperMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 5),
    _HpnicfdeTConnOperMulticastAddress_Type()
)
hpnicfdeTConnOperMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeTConnOperMulticastAddress.setStatus("current")
_HpnicfdeTConnOperStCapTcpNumber_Type = Integer32
_HpnicfdeTConnOperStCapTcpNumber_Object = MibTableColumn
hpnicfdeTConnOperStCapTcpNumber = _HpnicfdeTConnOperStCapTcpNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 6),
    _HpnicfdeTConnOperStCapTcpNumber_Type()
)
hpnicfdeTConnOperStCapTcpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeTConnOperStCapTcpNumber.setStatus("current")
_HpnicfdeTConnOperRecvPkts_Type = Counter32
_HpnicfdeTConnOperRecvPkts_Object = MibTableColumn
hpnicfdeTConnOperRecvPkts = _HpnicfdeTConnOperRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 7),
    _HpnicfdeTConnOperRecvPkts_Type()
)
hpnicfdeTConnOperRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeTConnOperRecvPkts.setStatus("current")
_HpnicfdeTConnOperSendPkts_Type = Counter32
_HpnicfdeTConnOperSendPkts_Object = MibTableColumn
hpnicfdeTConnOperSendPkts = _HpnicfdeTConnOperSendPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 8),
    _HpnicfdeTConnOperSendPkts_Type()
)
hpnicfdeTConnOperSendPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeTConnOperSendPkts.setStatus("current")
_HpnicfdeTConnOperDropPkts_Type = Counter32
_HpnicfdeTConnOperDropPkts_Object = MibTableColumn
hpnicfdeTConnOperDropPkts = _HpnicfdeTConnOperDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 2, 1, 9),
    _HpnicfdeTConnOperDropPkts_Type()
)
hpnicfdeTConnOperDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeTConnOperDropPkts.setStatus("current")
_HpnicfdeTConnTcpConfigTable_Object = MibTable
hpnicfdeTConnTcpConfigTable = _HpnicfdeTConnTcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfdeTConnTcpConfigTable.setStatus("current")
_HpnicfdeTConnTcpConfigEntry_Object = MibTableRow
hpnicfdeTConnTcpConfigEntry = _HpnicfdeTConnTcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfdeTConnTcpConfigEntry.setStatus("current")


class _HpnicfdeTConnTcpConfigQueueMax_Type(Integer32):
    """Custom type hpnicfdeTConnTcpConfigQueueMax based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 2000),
    )


_HpnicfdeTConnTcpConfigQueueMax_Type.__name__ = "Integer32"
_HpnicfdeTConnTcpConfigQueueMax_Object = MibTableColumn
hpnicfdeTConnTcpConfigQueueMax = _HpnicfdeTConnTcpConfigQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 2, 3, 1, 1),
    _HpnicfdeTConnTcpConfigQueueMax_Type()
)
hpnicfdeTConnTcpConfigQueueMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeTConnTcpConfigQueueMax.setStatus("current")
_HpnicfdeBridge_ObjectIdentity = ObjectIdentity
hpnicfdeBridge = _HpnicfdeBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3)
)
_HpnicfdeBridgeTable_Object = MibTable
hpnicfdeBridgeTable = _HpnicfdeBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfdeBridgeTable.setStatus("current")
_HpnicfdeBridgeEntry_Object = MibTableRow
hpnicfdeBridgeEntry = _HpnicfdeBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 1, 1)
)
hpnicfdeBridgeEntry.setIndexNames(
    (0, "HPN-ICF-SNA-DLSW-EXT-MIB", "hpnicfdeBridgeNumIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdeBridgeEntry.setStatus("current")


class _HpnicfdeBridgeNumIndex_Type(Integer32):
    """Custom type hpnicfdeBridgeNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfdeBridgeNumIndex_Type.__name__ = "Integer32"
_HpnicfdeBridgeNumIndex_Object = MibTableColumn
hpnicfdeBridgeNumIndex = _HpnicfdeBridgeNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 1, 1, 1),
    _HpnicfdeBridgeNumIndex_Type()
)
hpnicfdeBridgeNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfdeBridgeNumIndex.setStatus("current")
_HpnicfdeBridgeRowStatus_Type = RowStatus
_HpnicfdeBridgeRowStatus_Object = MibTableColumn
hpnicfdeBridgeRowStatus = _HpnicfdeBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 1, 1, 2),
    _HpnicfdeBridgeRowStatus_Type()
)
hpnicfdeBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeBridgeRowStatus.setStatus("current")
_HpnicfdeBridgeIfTable_Object = MibTable
hpnicfdeBridgeIfTable = _HpnicfdeBridgeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfdeBridgeIfTable.setStatus("current")
_HpnicfdeBridgeIfEntry_Object = MibTableRow
hpnicfdeBridgeIfEntry = _HpnicfdeBridgeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 2, 1)
)
hpnicfdeBridgeIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdeBridgeIfEntry.setStatus("current")


class _HpnicfdeBridgeIfBrgGrp_Type(Integer32):
    """Custom type hpnicfdeBridgeIfBrgGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfdeBridgeIfBrgGrp_Type.__name__ = "Integer32"
_HpnicfdeBridgeIfBrgGrp_Object = MibTableColumn
hpnicfdeBridgeIfBrgGrp = _HpnicfdeBridgeIfBrgGrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 2, 1, 1),
    _HpnicfdeBridgeIfBrgGrp_Type()
)
hpnicfdeBridgeIfBrgGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeBridgeIfBrgGrp.setStatus("current")
_HpnicfdeBridgeIfRowStatus_Type = RowStatus
_HpnicfdeBridgeIfRowStatus_Object = MibTableColumn
hpnicfdeBridgeIfRowStatus = _HpnicfdeBridgeIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 3, 2, 1, 2),
    _HpnicfdeBridgeIfRowStatus_Type()
)
hpnicfdeBridgeIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeBridgeIfRowStatus.setStatus("current")
_HpnicfdeQllc_ObjectIdentity = ObjectIdentity
hpnicfdeQllc = _HpnicfdeQllc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4)
)
_HpnicfdeQllcTable_Object = MibTable
hpnicfdeQllcTable = _HpnicfdeQllcTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfdeQllcTable.setStatus("current")
_HpnicfdeQllcEntry_Object = MibTableRow
hpnicfdeQllcEntry = _HpnicfdeQllcEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1)
)
hpnicfdeQllcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdeQllcEntry.setStatus("current")
_HpnicfQllcX121Address_Type = Integer32
_HpnicfQllcX121Address_Object = MibTableColumn
hpnicfQllcX121Address = _HpnicfQllcX121Address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 1),
    _HpnicfQllcX121Address_Type()
)
hpnicfQllcX121Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQllcX121Address.setStatus("current")
_HpnicfQllcLocalMac_Type = MacAddressNC
_HpnicfQllcLocalMac_Object = MibTableColumn
hpnicfQllcLocalMac = _HpnicfQllcLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 2),
    _HpnicfQllcLocalMac_Type()
)
hpnicfQllcLocalMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQllcLocalMac.setStatus("current")


class _HpnicfQllcLocalSap_Type(OctetString):
    """Custom type hpnicfQllcLocalSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HpnicfQllcLocalSap_Type.__name__ = "OctetString"
_HpnicfQllcLocalSap_Object = MibTableColumn
hpnicfQllcLocalSap = _HpnicfQllcLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 3),
    _HpnicfQllcLocalSap_Type()
)
hpnicfQllcLocalSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQllcLocalSap.setStatus("current")


class _HpnicfQllcRemoteMac_Type(MacAddressNC):
    """Custom type hpnicfQllcRemoteMac based on MacAddressNC"""
    defaultHexValue = ""


_HpnicfQllcRemoteMac_Object = MibTableColumn
hpnicfQllcRemoteMac = _HpnicfQllcRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 4),
    _HpnicfQllcRemoteMac_Type()
)
hpnicfQllcRemoteMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQllcRemoteMac.setStatus("current")


class _HpnicfQllcRemoteSap_Type(OctetString):
    """Custom type hpnicfQllcRemoteSap based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_HpnicfQllcRemoteSap_Type.__name__ = "OctetString"
_HpnicfQllcRemoteSap_Object = MibTableColumn
hpnicfQllcRemoteSap = _HpnicfQllcRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 5),
    _HpnicfQllcRemoteSap_Type()
)
hpnicfQllcRemoteSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQllcRemoteSap.setStatus("current")
_HpnicfQllcRowStatus_Type = RowStatus
_HpnicfQllcRowStatus_Object = MibTableColumn
hpnicfQllcRowStatus = _HpnicfQllcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 4, 1, 1, 6),
    _HpnicfQllcRowStatus_Type()
)
hpnicfQllcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQllcRowStatus.setStatus("current")
_HpnicfdeSdlc_ObjectIdentity = ObjectIdentity
hpnicfdeSdlc = _HpnicfdeSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5)
)
_HpnicfdeSdlcPortTable_Object = MibTable
hpnicfdeSdlcPortTable = _HpnicfdeSdlcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortTable.setStatus("current")
_HpnicfdeSdlcPortEntry_Object = MibTableRow
hpnicfdeSdlcPortEntry = _HpnicfdeSdlcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1)
)
hpnicfdeSdlcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortEntry.setStatus("current")


class _HpnicfdeSdlcPortRole_Type(Integer32):
    """Custom type hpnicfdeSdlcPortRole based on Integer32"""
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


_HpnicfdeSdlcPortRole_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortRole_Object = MibTableColumn
hpnicfdeSdlcPortRole = _HpnicfdeSdlcPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 1),
    _HpnicfdeSdlcPortRole_Type()
)
hpnicfdeSdlcPortRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortRole.setStatus("current")


class _HpnicfdeSdlcPortSendWindow_Type(Integer32):
    """Custom type hpnicfdeSdlcPortSendWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HpnicfdeSdlcPortSendWindow_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortSendWindow_Object = MibTableColumn
hpnicfdeSdlcPortSendWindow = _HpnicfdeSdlcPortSendWindow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 2),
    _HpnicfdeSdlcPortSendWindow_Type()
)
hpnicfdeSdlcPortSendWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortSendWindow.setStatus("current")


class _HpnicfdeSdlcPortModulo_Type(Integer32):
    """Custom type hpnicfdeSdlcPortModulo based on Integer32"""
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


_HpnicfdeSdlcPortModulo_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortModulo_Object = MibTableColumn
hpnicfdeSdlcPortModulo = _HpnicfdeSdlcPortModulo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 3),
    _HpnicfdeSdlcPortModulo_Type()
)
hpnicfdeSdlcPortModulo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortModulo.setStatus("current")


class _HpnicfdeSdlcPortMaxPdu_Type(Integer32):
    """Custom type hpnicfdeSdlcPortMaxPdu based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17600),
    )


_HpnicfdeSdlcPortMaxPdu_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortMaxPdu_Object = MibTableColumn
hpnicfdeSdlcPortMaxPdu = _HpnicfdeSdlcPortMaxPdu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 4),
    _HpnicfdeSdlcPortMaxPdu_Type()
)
hpnicfdeSdlcPortMaxPdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortMaxPdu.setStatus("current")


class _HpnicfdeSdlcPortMaxSendQueue_Type(Integer32):
    """Custom type hpnicfdeSdlcPortMaxSendQueue based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_HpnicfdeSdlcPortMaxSendQueue_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortMaxSendQueue_Object = MibTableColumn
hpnicfdeSdlcPortMaxSendQueue = _HpnicfdeSdlcPortMaxSendQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 5),
    _HpnicfdeSdlcPortMaxSendQueue_Type()
)
hpnicfdeSdlcPortMaxSendQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortMaxSendQueue.setStatus("current")


class _HpnicfdeSdlcPortMaxTransmission_Type(Integer32):
    """Custom type hpnicfdeSdlcPortMaxTransmission based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfdeSdlcPortMaxTransmission_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortMaxTransmission_Object = MibTableColumn
hpnicfdeSdlcPortMaxTransmission = _HpnicfdeSdlcPortMaxTransmission_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 6),
    _HpnicfdeSdlcPortMaxTransmission_Type()
)
hpnicfdeSdlcPortMaxTransmission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortMaxTransmission.setStatus("current")


class _HpnicfdeSdlcPortSimultaneousEnable_Type(Integer32):
    """Custom type hpnicfdeSdlcPortSimultaneousEnable based on Integer32"""
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


_HpnicfdeSdlcPortSimultaneousEnable_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortSimultaneousEnable_Object = MibTableColumn
hpnicfdeSdlcPortSimultaneousEnable = _HpnicfdeSdlcPortSimultaneousEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 7),
    _HpnicfdeSdlcPortSimultaneousEnable_Type()
)
hpnicfdeSdlcPortSimultaneousEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortSimultaneousEnable.setStatus("current")


class _HpnicfdeSdlcPortTimerACK_Type(Integer32):
    """Custom type hpnicfdeSdlcPortTimerACK based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_HpnicfdeSdlcPortTimerACK_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortTimerACK_Object = MibTableColumn
hpnicfdeSdlcPortTimerACK = _HpnicfdeSdlcPortTimerACK_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 8),
    _HpnicfdeSdlcPortTimerACK_Type()
)
hpnicfdeSdlcPortTimerACK.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortTimerACK.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortTimerACK.setUnits("milliseconds")


class _HpnicfdeSdlcPortTimerLifeTime_Type(Integer32):
    """Custom type hpnicfdeSdlcPortTimerLifeTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_HpnicfdeSdlcPortTimerLifeTime_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortTimerLifeTime_Object = MibTableColumn
hpnicfdeSdlcPortTimerLifeTime = _HpnicfdeSdlcPortTimerLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 9),
    _HpnicfdeSdlcPortTimerLifeTime_Type()
)
hpnicfdeSdlcPortTimerLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortTimerLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortTimerLifeTime.setUnits("milliseconds")


class _HpnicfdeSdlcPortTimerPollPause_Type(Integer32):
    """Custom type hpnicfdeSdlcPortTimerPollPause based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HpnicfdeSdlcPortTimerPollPause_Type.__name__ = "Integer32"
_HpnicfdeSdlcPortTimerPollPause_Object = MibTableColumn
hpnicfdeSdlcPortTimerPollPause = _HpnicfdeSdlcPortTimerPollPause_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 10),
    _HpnicfdeSdlcPortTimerPollPause_Type()
)
hpnicfdeSdlcPortTimerPollPause.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortTimerPollPause.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortTimerPollPause.setUnits("milliseconds")
_HpnicfdeSdlcPortRowStatus_Type = RowStatus
_HpnicfdeSdlcPortRowStatus_Object = MibTableColumn
hpnicfdeSdlcPortRowStatus = _HpnicfdeSdlcPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 5, 1, 1, 11),
    _HpnicfdeSdlcPortRowStatus_Type()
)
hpnicfdeSdlcPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeSdlcPortRowStatus.setStatus("current")
_HpnicfdeLlc2_ObjectIdentity = ObjectIdentity
hpnicfdeLlc2 = _HpnicfdeLlc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6)
)
_HpnicfdeLlc2PortTable_Object = MibTable
hpnicfdeLlc2PortTable = _HpnicfdeLlc2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTable.setStatus("current")
_HpnicfdeLlc2PortEntry_Object = MibTableRow
hpnicfdeLlc2PortEntry = _HpnicfdeLlc2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1)
)
hpnicfdeLlc2PortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortEntry.setStatus("current")


class _HpnicfdeLlc2PortMaxAck_Type(Integer32):
    """Custom type hpnicfdeLlc2PortMaxAck based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_HpnicfdeLlc2PortMaxAck_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortMaxAck_Object = MibTableColumn
hpnicfdeLlc2PortMaxAck = _HpnicfdeLlc2PortMaxAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 1),
    _HpnicfdeLlc2PortMaxAck_Type()
)
hpnicfdeLlc2PortMaxAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortMaxAck.setStatus("current")


class _HpnicfdeLlc2PortMaxPdu_Type(Integer32):
    """Custom type hpnicfdeLlc2PortMaxPdu based on Integer32"""
    defaultValue = 1493

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1700),
    )


_HpnicfdeLlc2PortMaxPdu_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortMaxPdu_Object = MibTableColumn
hpnicfdeLlc2PortMaxPdu = _HpnicfdeLlc2PortMaxPdu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 2),
    _HpnicfdeLlc2PortMaxPdu_Type()
)
hpnicfdeLlc2PortMaxPdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortMaxPdu.setStatus("current")


class _HpnicfdeLlc2PortMaxSendQueue_Type(Integer32):
    """Custom type hpnicfdeLlc2PortMaxSendQueue based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_HpnicfdeLlc2PortMaxSendQueue_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortMaxSendQueue_Object = MibTableColumn
hpnicfdeLlc2PortMaxSendQueue = _HpnicfdeLlc2PortMaxSendQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 3),
    _HpnicfdeLlc2PortMaxSendQueue_Type()
)
hpnicfdeLlc2PortMaxSendQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortMaxSendQueue.setStatus("current")


class _HpnicfdeLlc2PortMaxTransmission_Type(Integer32):
    """Custom type hpnicfdeLlc2PortMaxTransmission based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfdeLlc2PortMaxTransmission_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortMaxTransmission_Object = MibTableColumn
hpnicfdeLlc2PortMaxTransmission = _HpnicfdeLlc2PortMaxTransmission_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 4),
    _HpnicfdeLlc2PortMaxTransmission_Type()
)
hpnicfdeLlc2PortMaxTransmission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortMaxTransmission.setStatus("current")


class _HpnicfdeLlc2PortModulo_Type(Integer32):
    """Custom type hpnicfdeLlc2PortModulo based on Integer32"""
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


_HpnicfdeLlc2PortModulo_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortModulo_Object = MibTableColumn
hpnicfdeLlc2PortModulo = _HpnicfdeLlc2PortModulo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 5),
    _HpnicfdeLlc2PortModulo_Type()
)
hpnicfdeLlc2PortModulo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortModulo.setStatus("current")


class _HpnicfdeLlc2PortReceiveWindow_Type(Integer32):
    """Custom type hpnicfdeLlc2PortReceiveWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_HpnicfdeLlc2PortReceiveWindow_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortReceiveWindow_Object = MibTableColumn
hpnicfdeLlc2PortReceiveWindow = _HpnicfdeLlc2PortReceiveWindow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 6),
    _HpnicfdeLlc2PortReceiveWindow_Type()
)
hpnicfdeLlc2PortReceiveWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortReceiveWindow.setStatus("current")


class _HpnicfdeLlc2PortTimerAck_Type(Integer32):
    """Custom type hpnicfdeLlc2PortTimerAck based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_HpnicfdeLlc2PortTimerAck_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortTimerAck_Object = MibTableColumn
hpnicfdeLlc2PortTimerAck = _HpnicfdeLlc2PortTimerAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 7),
    _HpnicfdeLlc2PortTimerAck_Type()
)
hpnicfdeLlc2PortTimerAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerAck.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerAck.setUnits("milliseconds")


class _HpnicfdeLlc2PortTimerAckDelay_Type(Integer32):
    """Custom type hpnicfdeLlc2PortTimerAckDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_HpnicfdeLlc2PortTimerAckDelay_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortTimerAckDelay_Object = MibTableColumn
hpnicfdeLlc2PortTimerAckDelay = _HpnicfdeLlc2PortTimerAckDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 8),
    _HpnicfdeLlc2PortTimerAckDelay_Type()
)
hpnicfdeLlc2PortTimerAckDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerAckDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerAckDelay.setUnits("milliseconds")


class _HpnicfdeLlc2PortTimerDetect_Type(Integer32):
    """Custom type hpnicfdeLlc2PortTimerDetect based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_HpnicfdeLlc2PortTimerDetect_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortTimerDetect_Object = MibTableColumn
hpnicfdeLlc2PortTimerDetect = _HpnicfdeLlc2PortTimerDetect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 9),
    _HpnicfdeLlc2PortTimerDetect_Type()
)
hpnicfdeLlc2PortTimerDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerDetect.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerDetect.setUnits("milliseconds")


class _HpnicfdeLlc2PortTimerBusy_Type(Integer32):
    """Custom type hpnicfdeLlc2PortTimerBusy based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_HpnicfdeLlc2PortTimerBusy_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortTimerBusy_Object = MibTableColumn
hpnicfdeLlc2PortTimerBusy = _HpnicfdeLlc2PortTimerBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 10),
    _HpnicfdeLlc2PortTimerBusy_Type()
)
hpnicfdeLlc2PortTimerBusy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerBusy.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerBusy.setUnits("milliseconds")


class _HpnicfdeLlc2PortTimerPoll_Type(Integer32):
    """Custom type hpnicfdeLlc2PortTimerPoll based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_HpnicfdeLlc2PortTimerPoll_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortTimerPoll_Object = MibTableColumn
hpnicfdeLlc2PortTimerPoll = _HpnicfdeLlc2PortTimerPoll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 11),
    _HpnicfdeLlc2PortTimerPoll_Type()
)
hpnicfdeLlc2PortTimerPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerPoll.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerPoll.setUnits("milliseconds")


class _HpnicfdeLlc2PortTimerReject_Type(Integer32):
    """Custom type hpnicfdeLlc2PortTimerReject based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_HpnicfdeLlc2PortTimerReject_Type.__name__ = "Integer32"
_HpnicfdeLlc2PortTimerReject_Object = MibTableColumn
hpnicfdeLlc2PortTimerReject = _HpnicfdeLlc2PortTimerReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 12),
    _HpnicfdeLlc2PortTimerReject_Type()
)
hpnicfdeLlc2PortTimerReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerReject.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortTimerReject.setUnits("milliseconds")
_HpnicfdeLlc2PortRowStatus_Type = RowStatus
_HpnicfdeLlc2PortRowStatus_Object = MibTableColumn
hpnicfdeLlc2PortRowStatus = _HpnicfdeLlc2PortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 6, 1, 1, 13),
    _HpnicfdeLlc2PortRowStatus_Type()
)
hpnicfdeLlc2PortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeLlc2PortRowStatus.setStatus("current")
_HpnicfdeReachableCache_ObjectIdentity = ObjectIdentity
hpnicfdeReachableCache = _HpnicfdeReachableCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7)
)
_HpnicfdeRchCacheStat_ObjectIdentity = ObjectIdentity
hpnicfdeRchCacheStat = _HpnicfdeRchCacheStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 1)
)
_HpnicfdeRchCacheMaxIndex_Type = Integer32
_HpnicfdeRchCacheMaxIndex_Object = MibScalar
hpnicfdeRchCacheMaxIndex = _HpnicfdeRchCacheMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 1, 1),
    _HpnicfdeRchCacheMaxIndex_Type()
)
hpnicfdeRchCacheMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeRchCacheMaxIndex.setStatus("current")
_HpnicfdeRchCacheNextIndex_Type = Integer32
_HpnicfdeRchCacheNextIndex_Object = MibScalar
hpnicfdeRchCacheNextIndex = _HpnicfdeRchCacheNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 1, 2),
    _HpnicfdeRchCacheNextIndex_Type()
)
hpnicfdeRchCacheNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeRchCacheNextIndex.setStatus("current")
_HpnicfdeRchCacheTable_Object = MibTable
hpnicfdeRchCacheTable = _HpnicfdeRchCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3)
)
if mibBuilder.loadTexts:
    hpnicfdeRchCacheTable.setStatus("current")
_HpnicfdeRchCacheEntry_Object = MibTableRow
hpnicfdeRchCacheEntry = _HpnicfdeRchCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1)
)
hpnicfdeRchCacheEntry.setIndexNames(
    (0, "HPN-ICF-SNA-DLSW-EXT-MIB", "hpnicfdeRchCacheIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdeRchCacheEntry.setStatus("current")
_HpnicfdeRchCacheIndex_Type = Integer32
_HpnicfdeRchCacheIndex_Object = MibTableColumn
hpnicfdeRchCacheIndex = _HpnicfdeRchCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 1),
    _HpnicfdeRchCacheIndex_Type()
)
hpnicfdeRchCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfdeRchCacheIndex.setStatus("current")


class _HpnicfdeRchCacheStatus_Type(Integer32):
    """Custom type hpnicfdeRchCacheStatus based on Integer32"""
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


_HpnicfdeRchCacheStatus_Type.__name__ = "Integer32"
_HpnicfdeRchCacheStatus_Object = MibTableColumn
hpnicfdeRchCacheStatus = _HpnicfdeRchCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 2),
    _HpnicfdeRchCacheStatus_Type()
)
hpnicfdeRchCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeRchCacheStatus.setStatus("current")
_HpnicfdeRchCacheRemainTime_Type = TimeTicks
_HpnicfdeRchCacheRemainTime_Object = MibTableColumn
hpnicfdeRchCacheRemainTime = _HpnicfdeRchCacheRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 3),
    _HpnicfdeRchCacheRemainTime_Type()
)
hpnicfdeRchCacheRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeRchCacheRemainTime.setStatus("current")
_HpnicfdeRchCacheMac_Type = MacAddressNC
_HpnicfdeRchCacheMac_Object = MibTableColumn
hpnicfdeRchCacheMac = _HpnicfdeRchCacheMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 4),
    _HpnicfdeRchCacheMac_Type()
)
hpnicfdeRchCacheMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeRchCacheMac.setStatus("current")
_HpnicfdeRchCacheRemoteIpAddrType_Type = InetAddressType
_HpnicfdeRchCacheRemoteIpAddrType_Object = MibTableColumn
hpnicfdeRchCacheRemoteIpAddrType = _HpnicfdeRchCacheRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 5),
    _HpnicfdeRchCacheRemoteIpAddrType_Type()
)
hpnicfdeRchCacheRemoteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeRchCacheRemoteIpAddrType.setStatus("current")
_HpnicfdeRchCacheRemoteIp_Type = InetAddress
_HpnicfdeRchCacheRemoteIp_Object = MibTableColumn
hpnicfdeRchCacheRemoteIp = _HpnicfdeRchCacheRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 6),
    _HpnicfdeRchCacheRemoteIp_Type()
)
hpnicfdeRchCacheRemoteIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeRchCacheRemoteIp.setStatus("current")
_HpnicfdeRchCacheRowStatus_Type = RowStatus
_HpnicfdeRchCacheRowStatus_Object = MibTableColumn
hpnicfdeRchCacheRowStatus = _HpnicfdeRchCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 7, 3, 1, 7),
    _HpnicfdeRchCacheRowStatus_Type()
)
hpnicfdeRchCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeRchCacheRowStatus.setStatus("current")
_HpnicfdeEthernetBackup_ObjectIdentity = ObjectIdentity
hpnicfdeEthernetBackup = _HpnicfdeEthernetBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8)
)
_HpnicfdeEBMacMapStat_ObjectIdentity = ObjectIdentity
hpnicfdeEBMacMapStat = _HpnicfdeEBMacMapStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 1)
)
_HpnicfdeEBMacMapMaxIndex_Type = Integer32
_HpnicfdeEBMacMapMaxIndex_Object = MibScalar
hpnicfdeEBMacMapMaxIndex = _HpnicfdeEBMacMapMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 1, 1),
    _HpnicfdeEBMacMapMaxIndex_Type()
)
hpnicfdeEBMacMapMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeEBMacMapMaxIndex.setStatus("current")
_HpnicfdeEBMacMapNextIndex_Type = Integer32
_HpnicfdeEBMacMapNextIndex_Object = MibScalar
hpnicfdeEBMacMapNextIndex = _HpnicfdeEBMacMapNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 1, 2),
    _HpnicfdeEBMacMapNextIndex_Type()
)
hpnicfdeEBMacMapNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdeEBMacMapNextIndex.setStatus("current")
_HpnicfdeEBIfTable_Object = MibTable
hpnicfdeEBIfTable = _HpnicfdeEBIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3)
)
if mibBuilder.loadTexts:
    hpnicfdeEBIfTable.setStatus("current")
_HpnicfdeEBIfEntry_Object = MibTableRow
hpnicfdeEBIfEntry = _HpnicfdeEBIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1)
)
hpnicfdeEBIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdeEBIfEntry.setStatus("current")


class _HpnicfdeEBMulticastMac_Type(MacAddressNC):
    """Custom type hpnicfdeEBMulticastMac based on MacAddressNC"""
    defaultHexValue = "000000000000"


_HpnicfdeEBMulticastMac_Object = MibTableColumn
hpnicfdeEBMulticastMac = _HpnicfdeEBMulticastMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1, 1),
    _HpnicfdeEBMulticastMac_Type()
)
hpnicfdeEBMulticastMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeEBMulticastMac.setStatus("current")


class _HpnicfdeEBPriority_Type(Integer32):
    """Custom type hpnicfdeEBPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HpnicfdeEBPriority_Type.__name__ = "Integer32"
_HpnicfdeEBPriority_Object = MibTableColumn
hpnicfdeEBPriority = _HpnicfdeEBPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1, 2),
    _HpnicfdeEBPriority_Type()
)
hpnicfdeEBPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeEBPriority.setStatus("current")


class _HpnicfdeEBtimer_Type(Integer32):
    """Custom type hpnicfdeEBtimer based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_HpnicfdeEBtimer_Type.__name__ = "Integer32"
_HpnicfdeEBtimer_Object = MibTableColumn
hpnicfdeEBtimer = _HpnicfdeEBtimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1, 3),
    _HpnicfdeEBtimer_Type()
)
hpnicfdeEBtimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeEBtimer.setStatus("current")
_HpnicfdeEBRowStatus_Type = RowStatus
_HpnicfdeEBRowStatus_Object = MibTableColumn
hpnicfdeEBRowStatus = _HpnicfdeEBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 3, 1, 4),
    _HpnicfdeEBRowStatus_Type()
)
hpnicfdeEBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeEBRowStatus.setStatus("current")
_HpnicfdeEBMacMapTable_Object = MibTable
hpnicfdeEBMacMapTable = _HpnicfdeEBMacMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4)
)
if mibBuilder.loadTexts:
    hpnicfdeEBMacMapTable.setStatus("current")
_HpnicfdeEBMacMapEntry_Object = MibTableRow
hpnicfdeEBMacMapEntry = _HpnicfdeEBMacMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1)
)
hpnicfdeEBMacMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-SNA-DLSW-EXT-MIB", "hpnicfdeEBMacMapIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdeEBMacMapEntry.setStatus("current")
_HpnicfdeEBMacMapIndex_Type = Integer32
_HpnicfdeEBMacMapIndex_Object = MibTableColumn
hpnicfdeEBMacMapIndex = _HpnicfdeEBMacMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 1),
    _HpnicfdeEBMacMapIndex_Type()
)
hpnicfdeEBMacMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfdeEBMacMapIndex.setStatus("current")
_HpnicfdeEBMacMapLocalMac_Type = MacAddressNC
_HpnicfdeEBMacMapLocalMac_Object = MibTableColumn
hpnicfdeEBMacMapLocalMac = _HpnicfdeEBMacMapLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 2),
    _HpnicfdeEBMacMapLocalMac_Type()
)
hpnicfdeEBMacMapLocalMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeEBMacMapLocalMac.setStatus("current")
_HpnicfdeEBMacMapRemoteMac_Type = MacAddressNC
_HpnicfdeEBMacMapRemoteMac_Object = MibTableColumn
hpnicfdeEBMacMapRemoteMac = _HpnicfdeEBMacMapRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 3),
    _HpnicfdeEBMacMapRemoteMac_Type()
)
hpnicfdeEBMacMapRemoteMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeEBMacMapRemoteMac.setStatus("current")
_HpnicfdeEBMacMapNeighbour_Type = MacAddressNC
_HpnicfdeEBMacMapNeighbour_Object = MibTableColumn
hpnicfdeEBMacMapNeighbour = _HpnicfdeEBMacMapNeighbour_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 4),
    _HpnicfdeEBMacMapNeighbour_Type()
)
hpnicfdeEBMacMapNeighbour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeEBMacMapNeighbour.setStatus("current")
_HpnicfdeEBMacMapRowStatus_Type = RowStatus
_HpnicfdeEBMacMapRowStatus_Object = MibTableColumn
hpnicfdeEBMacMapRowStatus = _HpnicfdeEBMacMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62, 1, 8, 4, 1, 5),
    _HpnicfdeEBMacMapRowStatus_Type()
)
hpnicfdeEBMacMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdeEBMacMapRowStatus.setStatus("current")
dlswTConnConfigEntry.registerAugmentions(
    ("HPN-ICF-SNA-DLSW-EXT-MIB",
     "hpnicfdeTConnConfigEntry")
)
hpnicfdeTConnConfigEntry.setIndexNames(*dlswTConnConfigEntry.getIndexNames())
dlswTConnOperEntry.registerAugmentions(
    ("HPN-ICF-SNA-DLSW-EXT-MIB",
     "hpnicfdeTConnOperEntry")
)
hpnicfdeTConnOperEntry.setIndexNames(*dlswTConnOperEntry.getIndexNames())
dlswTConnTcpConfigEntry.registerAugmentions(
    ("HPN-ICF-SNA-DLSW-EXT-MIB",
     "hpnicfdeTConnTcpConfigEntry")
)
hpnicfdeTConnTcpConfigEntry.setIndexNames(*dlswTConnTcpConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SNA-DLSW-EXT-MIB",
    **{"hpnicfDlswExt": hpnicfDlswExt,
       "hpnicfDlswExtMIBObjects": hpnicfDlswExtMIBObjects,
       "hpnicfdeNode": hpnicfdeNode,
       "hpnicfdeNodeVendorID": hpnicfdeNodeVendorID,
       "hpnicfdeNodeIpAddrType": hpnicfdeNodeIpAddrType,
       "hpnicfdeNodeLocalAddr": hpnicfdeNodeLocalAddr,
       "hpnicfdeNodePriority": hpnicfdeNodePriority,
       "hpnicfdeNodeInitPacingWindow": hpnicfdeNodeInitPacingWindow,
       "hpnicfdeNodeMaxPacingWindow": hpnicfdeNodeMaxPacingWindow,
       "hpnicfdeNodeKeepAliveInterval": hpnicfdeNodeKeepAliveInterval,
       "hpnicfdeNodePermitDynamic": hpnicfdeNodePermitDynamic,
       "hpnicfdeNodeConnTimeout": hpnicfdeNodeConnTimeout,
       "hpnicfdeNodeLocalPendTimeout": hpnicfdeNodeLocalPendTimeout,
       "hpnicfdeNodeRemotePendTimeout": hpnicfdeNodeRemotePendTimeout,
       "hpnicfdeNodeSnaCacheTimeout": hpnicfdeNodeSnaCacheTimeout,
       "hpnicfdeNodeExplorerTimeout": hpnicfdeNodeExplorerTimeout,
       "hpnicfdeNodeExplorerWaitTimeout": hpnicfdeNodeExplorerWaitTimeout,
       "hpnicfdeNodeConfigSapList": hpnicfdeNodeConfigSapList,
       "hpnicfdeNodeMaxTransmission": hpnicfdeNodeMaxTransmission,
       "hpnicfdeNodeMulticastStatus": hpnicfdeNodeMulticastStatus,
       "hpnicfdeNodeMulticastAddress": hpnicfdeNodeMulticastAddress,
       "hpnicfdeNodeResetTcpAll": hpnicfdeNodeResetTcpAll,
       "hpnicfdeNodeStCapTcpNum": hpnicfdeNodeStCapTcpNum,
       "hpnicfdeNodeTcpQueueMax": hpnicfdeNodeTcpQueueMax,
       "hpnicfdeTConn": hpnicfdeTConn,
       "hpnicfdeTConnConfigTable": hpnicfdeTConnConfigTable,
       "hpnicfdeTConnConfigEntry": hpnicfdeTConnConfigEntry,
       "hpnicfdeTConnConfigVersion": hpnicfdeTConnConfigVersion,
       "hpnicfdeTConnConfigPriority": hpnicfdeTConnConfigPriority,
       "hpnicfdeTConnConfigLfSize": hpnicfdeTConnConfigLfSize,
       "hpnicfdeTConnConfigKeepaliveIntval": hpnicfdeTConnConfigKeepaliveIntval,
       "hpnicfdeTConnConfigBackup": hpnicfdeTConnConfigBackup,
       "hpnicfdeTConnConfigBackupTAddr": hpnicfdeTConnConfigBackupTAddr,
       "hpnicfdeTConnConfigBackupLinger": hpnicfdeTConnConfigBackupLinger,
       "hpnicfdeTConnOperTable": hpnicfdeTConnOperTable,
       "hpnicfdeTConnOperEntry": hpnicfdeTConnOperEntry,
       "hpnicfdeTConnOperPeerType": hpnicfdeTConnOperPeerType,
       "hpnicfdeTConnOperVendorID": hpnicfdeTConnOperVendorID,
       "hpnicfdeTConnOperVersionString": hpnicfdeTConnOperVersionString,
       "hpnicfdeTConnOperUpTime": hpnicfdeTConnOperUpTime,
       "hpnicfdeTConnOperMulticastAddress": hpnicfdeTConnOperMulticastAddress,
       "hpnicfdeTConnOperStCapTcpNumber": hpnicfdeTConnOperStCapTcpNumber,
       "hpnicfdeTConnOperRecvPkts": hpnicfdeTConnOperRecvPkts,
       "hpnicfdeTConnOperSendPkts": hpnicfdeTConnOperSendPkts,
       "hpnicfdeTConnOperDropPkts": hpnicfdeTConnOperDropPkts,
       "hpnicfdeTConnTcpConfigTable": hpnicfdeTConnTcpConfigTable,
       "hpnicfdeTConnTcpConfigEntry": hpnicfdeTConnTcpConfigEntry,
       "hpnicfdeTConnTcpConfigQueueMax": hpnicfdeTConnTcpConfigQueueMax,
       "hpnicfdeBridge": hpnicfdeBridge,
       "hpnicfdeBridgeTable": hpnicfdeBridgeTable,
       "hpnicfdeBridgeEntry": hpnicfdeBridgeEntry,
       "hpnicfdeBridgeNumIndex": hpnicfdeBridgeNumIndex,
       "hpnicfdeBridgeRowStatus": hpnicfdeBridgeRowStatus,
       "hpnicfdeBridgeIfTable": hpnicfdeBridgeIfTable,
       "hpnicfdeBridgeIfEntry": hpnicfdeBridgeIfEntry,
       "hpnicfdeBridgeIfBrgGrp": hpnicfdeBridgeIfBrgGrp,
       "hpnicfdeBridgeIfRowStatus": hpnicfdeBridgeIfRowStatus,
       "hpnicfdeQllc": hpnicfdeQllc,
       "hpnicfdeQllcTable": hpnicfdeQllcTable,
       "hpnicfdeQllcEntry": hpnicfdeQllcEntry,
       "hpnicfQllcX121Address": hpnicfQllcX121Address,
       "hpnicfQllcLocalMac": hpnicfQllcLocalMac,
       "hpnicfQllcLocalSap": hpnicfQllcLocalSap,
       "hpnicfQllcRemoteMac": hpnicfQllcRemoteMac,
       "hpnicfQllcRemoteSap": hpnicfQllcRemoteSap,
       "hpnicfQllcRowStatus": hpnicfQllcRowStatus,
       "hpnicfdeSdlc": hpnicfdeSdlc,
       "hpnicfdeSdlcPortTable": hpnicfdeSdlcPortTable,
       "hpnicfdeSdlcPortEntry": hpnicfdeSdlcPortEntry,
       "hpnicfdeSdlcPortRole": hpnicfdeSdlcPortRole,
       "hpnicfdeSdlcPortSendWindow": hpnicfdeSdlcPortSendWindow,
       "hpnicfdeSdlcPortModulo": hpnicfdeSdlcPortModulo,
       "hpnicfdeSdlcPortMaxPdu": hpnicfdeSdlcPortMaxPdu,
       "hpnicfdeSdlcPortMaxSendQueue": hpnicfdeSdlcPortMaxSendQueue,
       "hpnicfdeSdlcPortMaxTransmission": hpnicfdeSdlcPortMaxTransmission,
       "hpnicfdeSdlcPortSimultaneousEnable": hpnicfdeSdlcPortSimultaneousEnable,
       "hpnicfdeSdlcPortTimerACK": hpnicfdeSdlcPortTimerACK,
       "hpnicfdeSdlcPortTimerLifeTime": hpnicfdeSdlcPortTimerLifeTime,
       "hpnicfdeSdlcPortTimerPollPause": hpnicfdeSdlcPortTimerPollPause,
       "hpnicfdeSdlcPortRowStatus": hpnicfdeSdlcPortRowStatus,
       "hpnicfdeLlc2": hpnicfdeLlc2,
       "hpnicfdeLlc2PortTable": hpnicfdeLlc2PortTable,
       "hpnicfdeLlc2PortEntry": hpnicfdeLlc2PortEntry,
       "hpnicfdeLlc2PortMaxAck": hpnicfdeLlc2PortMaxAck,
       "hpnicfdeLlc2PortMaxPdu": hpnicfdeLlc2PortMaxPdu,
       "hpnicfdeLlc2PortMaxSendQueue": hpnicfdeLlc2PortMaxSendQueue,
       "hpnicfdeLlc2PortMaxTransmission": hpnicfdeLlc2PortMaxTransmission,
       "hpnicfdeLlc2PortModulo": hpnicfdeLlc2PortModulo,
       "hpnicfdeLlc2PortReceiveWindow": hpnicfdeLlc2PortReceiveWindow,
       "hpnicfdeLlc2PortTimerAck": hpnicfdeLlc2PortTimerAck,
       "hpnicfdeLlc2PortTimerAckDelay": hpnicfdeLlc2PortTimerAckDelay,
       "hpnicfdeLlc2PortTimerDetect": hpnicfdeLlc2PortTimerDetect,
       "hpnicfdeLlc2PortTimerBusy": hpnicfdeLlc2PortTimerBusy,
       "hpnicfdeLlc2PortTimerPoll": hpnicfdeLlc2PortTimerPoll,
       "hpnicfdeLlc2PortTimerReject": hpnicfdeLlc2PortTimerReject,
       "hpnicfdeLlc2PortRowStatus": hpnicfdeLlc2PortRowStatus,
       "hpnicfdeReachableCache": hpnicfdeReachableCache,
       "hpnicfdeRchCacheStat": hpnicfdeRchCacheStat,
       "hpnicfdeRchCacheMaxIndex": hpnicfdeRchCacheMaxIndex,
       "hpnicfdeRchCacheNextIndex": hpnicfdeRchCacheNextIndex,
       "hpnicfdeRchCacheTable": hpnicfdeRchCacheTable,
       "hpnicfdeRchCacheEntry": hpnicfdeRchCacheEntry,
       "hpnicfdeRchCacheIndex": hpnicfdeRchCacheIndex,
       "hpnicfdeRchCacheStatus": hpnicfdeRchCacheStatus,
       "hpnicfdeRchCacheRemainTime": hpnicfdeRchCacheRemainTime,
       "hpnicfdeRchCacheMac": hpnicfdeRchCacheMac,
       "hpnicfdeRchCacheRemoteIpAddrType": hpnicfdeRchCacheRemoteIpAddrType,
       "hpnicfdeRchCacheRemoteIp": hpnicfdeRchCacheRemoteIp,
       "hpnicfdeRchCacheRowStatus": hpnicfdeRchCacheRowStatus,
       "hpnicfdeEthernetBackup": hpnicfdeEthernetBackup,
       "hpnicfdeEBMacMapStat": hpnicfdeEBMacMapStat,
       "hpnicfdeEBMacMapMaxIndex": hpnicfdeEBMacMapMaxIndex,
       "hpnicfdeEBMacMapNextIndex": hpnicfdeEBMacMapNextIndex,
       "hpnicfdeEBIfTable": hpnicfdeEBIfTable,
       "hpnicfdeEBIfEntry": hpnicfdeEBIfEntry,
       "hpnicfdeEBMulticastMac": hpnicfdeEBMulticastMac,
       "hpnicfdeEBPriority": hpnicfdeEBPriority,
       "hpnicfdeEBtimer": hpnicfdeEBtimer,
       "hpnicfdeEBRowStatus": hpnicfdeEBRowStatus,
       "hpnicfdeEBMacMapTable": hpnicfdeEBMacMapTable,
       "hpnicfdeEBMacMapEntry": hpnicfdeEBMacMapEntry,
       "hpnicfdeEBMacMapIndex": hpnicfdeEBMacMapIndex,
       "hpnicfdeEBMacMapLocalMac": hpnicfdeEBMacMapLocalMac,
       "hpnicfdeEBMacMapRemoteMac": hpnicfdeEBMacMapRemoteMac,
       "hpnicfdeEBMacMapNeighbour": hpnicfdeEBMacMapNeighbour,
       "hpnicfdeEBMacMapRowStatus": hpnicfdeEBMacMapRowStatus}
)
