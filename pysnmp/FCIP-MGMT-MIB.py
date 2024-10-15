# SNMP MIB module (FCIP-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FCIP-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:25 2024
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

(FcNameIdOrZero,) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcNameIdOrZero")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fcipMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 224)
)
fcipMIB.setRevisions(
        ("2006-02-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FcipDomainIdInOctetForm(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class FcipEntityMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bPortMode", 2),
          ("ePortMode", 1))
    )



class FcipEntityId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_FcipObjects_ObjectIdentity = ObjectIdentity
fcipObjects = _FcipObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 224, 1)
)
_FcipConfig_ObjectIdentity = ObjectIdentity
fcipConfig = _FcipConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 224, 1, 1)
)


class _FcipDynIpConfType_Type(Integer32):
    """Custom type fcipDynIpConfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("slpv2", 1))
    )


_FcipDynIpConfType_Type.__name__ = "Integer32"
_FcipDynIpConfType_Object = MibScalar
fcipDynIpConfType = _FcipDynIpConfType_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 1),
    _FcipDynIpConfType_Type()
)
fcipDynIpConfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcipDynIpConfType.setStatus("current")
_FcipDeviceWWN_Type = FcNameIdOrZero
_FcipDeviceWWN_Object = MibScalar
fcipDeviceWWN = _FcipDeviceWWN_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 2),
    _FcipDeviceWWN_Type()
)
fcipDeviceWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipDeviceWWN.setStatus("current")


class _FcipEntitySACKOption_Type(Integer32):
    """Custom type fcipEntitySACKOption based on Integer32"""
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


_FcipEntitySACKOption_Type.__name__ = "Integer32"
_FcipEntitySACKOption_Object = MibScalar
fcipEntitySACKOption = _FcipEntitySACKOption_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 3),
    _FcipEntitySACKOption_Type()
)
fcipEntitySACKOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipEntitySACKOption.setStatus("current")
_FcipEntityInstanceTable_Object = MibTable
fcipEntityInstanceTable = _FcipEntityInstanceTable_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fcipEntityInstanceTable.setStatus("current")
_FcipEntityInstanceEntry_Object = MibTableRow
fcipEntityInstanceEntry = _FcipEntityInstanceEntry_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1)
)
fcipEntityInstanceEntry.setIndexNames(
    (0, "FCIP-MGMT-MIB", "fcipEntityId"),
)
if mibBuilder.loadTexts:
    fcipEntityInstanceEntry.setStatus("current")
_FcipEntityId_Type = FcipEntityId
_FcipEntityId_Object = MibTableColumn
fcipEntityId = _FcipEntityId_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 1),
    _FcipEntityId_Type()
)
fcipEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcipEntityId.setStatus("current")


class _FcipEntityName_Type(SnmpAdminString):
    """Custom type fcipEntityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FcipEntityName_Type.__name__ = "SnmpAdminString"
_FcipEntityName_Object = MibTableColumn
fcipEntityName = _FcipEntityName_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 2),
    _FcipEntityName_Type()
)
fcipEntityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipEntityName.setStatus("current")
_FcipEntityAddressType_Type = InetAddressType
_FcipEntityAddressType_Object = MibTableColumn
fcipEntityAddressType = _FcipEntityAddressType_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 3),
    _FcipEntityAddressType_Type()
)
fcipEntityAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipEntityAddressType.setStatus("current")
_FcipEntityAddress_Type = InetAddress
_FcipEntityAddress_Object = MibTableColumn
fcipEntityAddress = _FcipEntityAddress_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 4),
    _FcipEntityAddress_Type()
)
fcipEntityAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipEntityAddress.setStatus("current")


class _FcipEntityTcpConnPort_Type(InetPortNumber):
    """Custom type fcipEntityTcpConnPort based on InetPortNumber"""
    defaultValue = 0


_FcipEntityTcpConnPort_Object = MibTableColumn
fcipEntityTcpConnPort = _FcipEntityTcpConnPort_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 5),
    _FcipEntityTcpConnPort_Type()
)
fcipEntityTcpConnPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipEntityTcpConnPort.setStatus("current")
_FcipEntitySeqNumWrap_Type = TruthValue
_FcipEntitySeqNumWrap_Object = MibTableColumn
fcipEntitySeqNumWrap = _FcipEntitySeqNumWrap_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 6),
    _FcipEntitySeqNumWrap_Type()
)
fcipEntitySeqNumWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipEntitySeqNumWrap.setStatus("current")
_FcipEntityPHBSupport_Type = TruthValue
_FcipEntityPHBSupport_Object = MibTableColumn
fcipEntityPHBSupport = _FcipEntityPHBSupport_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 7),
    _FcipEntityPHBSupport_Type()
)
fcipEntityPHBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipEntityPHBSupport.setStatus("current")
_FcipEntityStatus_Type = RowStatus
_FcipEntityStatus_Object = MibTableColumn
fcipEntityStatus = _FcipEntityStatus_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 4, 1, 8),
    _FcipEntityStatus_Type()
)
fcipEntityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipEntityStatus.setStatus("current")
_FcipLinkTable_Object = MibTable
fcipLinkTable = _FcipLinkTable_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fcipLinkTable.setStatus("current")
_FcipLinkEntry_Object = MibTableRow
fcipLinkEntry = _FcipLinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1)
)
fcipLinkEntry.setIndexNames(
    (0, "FCIP-MGMT-MIB", "fcipEntityId"),
    (0, "FCIP-MGMT-MIB", "fcipLinkIndex"),
)
if mibBuilder.loadTexts:
    fcipLinkEntry.setStatus("current")


class _FcipLinkIndex_Type(Unsigned32):
    """Custom type fcipLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcipLinkIndex_Type.__name__ = "Unsigned32"
_FcipLinkIndex_Object = MibTableColumn
fcipLinkIndex = _FcipLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 1),
    _FcipLinkIndex_Type()
)
fcipLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcipLinkIndex.setStatus("current")
_FcipLinkIfIndex_Type = InterfaceIndex
_FcipLinkIfIndex_Object = MibTableColumn
fcipLinkIfIndex = _FcipLinkIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 2),
    _FcipLinkIfIndex_Type()
)
fcipLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkIfIndex.setStatus("current")


class _FcipLinkCost_Type(Unsigned32):
    """Custom type fcipLinkCost based on Unsigned32"""
    defaultValue = 0


_FcipLinkCost_Object = MibTableColumn
fcipLinkCost = _FcipLinkCost_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 3),
    _FcipLinkCost_Type()
)
fcipLinkCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipLinkCost.setStatus("current")
_FcipLinkLocalFcipEntityMode_Type = FcipEntityMode
_FcipLinkLocalFcipEntityMode_Object = MibTableColumn
fcipLinkLocalFcipEntityMode = _FcipLinkLocalFcipEntityMode_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 4),
    _FcipLinkLocalFcipEntityMode_Type()
)
fcipLinkLocalFcipEntityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkLocalFcipEntityMode.setStatus("current")
_FcipLinkLocalFcipEntityAddressType_Type = InetAddressType
_FcipLinkLocalFcipEntityAddressType_Object = MibTableColumn
fcipLinkLocalFcipEntityAddressType = _FcipLinkLocalFcipEntityAddressType_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 5),
    _FcipLinkLocalFcipEntityAddressType_Type()
)
fcipLinkLocalFcipEntityAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipLinkLocalFcipEntityAddressType.setStatus("current")
_FcipLinkLocalFcipEntityAddress_Type = InetAddress
_FcipLinkLocalFcipEntityAddress_Object = MibTableColumn
fcipLinkLocalFcipEntityAddress = _FcipLinkLocalFcipEntityAddress_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 6),
    _FcipLinkLocalFcipEntityAddress_Type()
)
fcipLinkLocalFcipEntityAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipLinkLocalFcipEntityAddress.setStatus("current")
_FcipLinkRemFcipEntityWWN_Type = FcNameIdOrZero
_FcipLinkRemFcipEntityWWN_Object = MibTableColumn
fcipLinkRemFcipEntityWWN = _FcipLinkRemFcipEntityWWN_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 7),
    _FcipLinkRemFcipEntityWWN_Type()
)
fcipLinkRemFcipEntityWWN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipLinkRemFcipEntityWWN.setStatus("current")
_FcipLinkRemFcipEntityId_Type = FcipEntityId
_FcipLinkRemFcipEntityId_Object = MibTableColumn
fcipLinkRemFcipEntityId = _FcipLinkRemFcipEntityId_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 8),
    _FcipLinkRemFcipEntityId_Type()
)
fcipLinkRemFcipEntityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipLinkRemFcipEntityId.setStatus("current")
_FcipLinkRemFcipEntityAddressType_Type = InetAddressType
_FcipLinkRemFcipEntityAddressType_Object = MibTableColumn
fcipLinkRemFcipEntityAddressType = _FcipLinkRemFcipEntityAddressType_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 9),
    _FcipLinkRemFcipEntityAddressType_Type()
)
fcipLinkRemFcipEntityAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipLinkRemFcipEntityAddressType.setStatus("current")
_FcipLinkRemFcipEntityAddress_Type = InetAddress
_FcipLinkRemFcipEntityAddress_Object = MibTableColumn
fcipLinkRemFcipEntityAddress = _FcipLinkRemFcipEntityAddress_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 10),
    _FcipLinkRemFcipEntityAddress_Type()
)
fcipLinkRemFcipEntityAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipLinkRemFcipEntityAddress.setStatus("current")
_FcipLinkStatus_Type = RowStatus
_FcipLinkStatus_Object = MibTableColumn
fcipLinkStatus = _FcipLinkStatus_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 11),
    _FcipLinkStatus_Type()
)
fcipLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipLinkStatus.setStatus("current")
_FcipLinkCreateTime_Type = TimeStamp
_FcipLinkCreateTime_Object = MibTableColumn
fcipLinkCreateTime = _FcipLinkCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 5, 1, 12),
    _FcipLinkCreateTime_Type()
)
fcipLinkCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkCreateTime.setStatus("current")
_FcipTcpConnTable_Object = MibTable
fcipTcpConnTable = _FcipTcpConnTable_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fcipTcpConnTable.setStatus("current")
_FcipTcpConnEntry_Object = MibTableRow
fcipTcpConnEntry = _FcipTcpConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1)
)
fcipTcpConnEntry.setIndexNames(
    (0, "FCIP-MGMT-MIB", "fcipEntityId"),
    (0, "FCIP-MGMT-MIB", "fcipLinkIndex"),
    (0, "FCIP-MGMT-MIB", "fcipTcpConnLocalPort"),
    (0, "FCIP-MGMT-MIB", "fcipTcpConnRemPort"),
)
if mibBuilder.loadTexts:
    fcipTcpConnEntry.setStatus("current")
_FcipTcpConnLocalPort_Type = InetPortNumber
_FcipTcpConnLocalPort_Object = MibTableColumn
fcipTcpConnLocalPort = _FcipTcpConnLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1, 1),
    _FcipTcpConnLocalPort_Type()
)
fcipTcpConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcipTcpConnLocalPort.setStatus("current")
_FcipTcpConnRemPort_Type = InetPortNumber
_FcipTcpConnRemPort_Object = MibTableColumn
fcipTcpConnRemPort = _FcipTcpConnRemPort_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1, 2),
    _FcipTcpConnRemPort_Type()
)
fcipTcpConnRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcipTcpConnRemPort.setStatus("current")
_FcipTcpConnRWSize_Type = Unsigned32
_FcipTcpConnRWSize_Object = MibTableColumn
fcipTcpConnRWSize = _FcipTcpConnRWSize_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1, 3),
    _FcipTcpConnRWSize_Type()
)
fcipTcpConnRWSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipTcpConnRWSize.setStatus("current")
_FcipTcpConnMSS_Type = Unsigned32
_FcipTcpConnMSS_Object = MibTableColumn
fcipTcpConnMSS = _FcipTcpConnMSS_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 6, 1, 4),
    _FcipTcpConnMSS_Type()
)
fcipTcpConnMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipTcpConnMSS.setStatus("current")
_FcipDynamicRouteTable_Object = MibTable
fcipDynamicRouteTable = _FcipDynamicRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 7)
)
if mibBuilder.loadTexts:
    fcipDynamicRouteTable.setStatus("current")
_FcipDynamicRouteEntry_Object = MibTableRow
fcipDynamicRouteEntry = _FcipDynamicRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 7, 1)
)
fcipDynamicRouteEntry.setIndexNames(
    (0, "FCIP-MGMT-MIB", "fcipEntityId"),
    (0, "FCIP-MGMT-MIB", "fcipDynamicRouteDID"),
)
if mibBuilder.loadTexts:
    fcipDynamicRouteEntry.setStatus("current")
_FcipDynamicRouteDID_Type = FcipDomainIdInOctetForm
_FcipDynamicRouteDID_Object = MibTableColumn
fcipDynamicRouteDID = _FcipDynamicRouteDID_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 7, 1, 1),
    _FcipDynamicRouteDID_Type()
)
fcipDynamicRouteDID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcipDynamicRouteDID.setStatus("current")


class _FcipDynamicRouteLinkIndex_Type(Unsigned32):
    """Custom type fcipDynamicRouteLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcipDynamicRouteLinkIndex_Type.__name__ = "Unsigned32"
_FcipDynamicRouteLinkIndex_Object = MibTableColumn
fcipDynamicRouteLinkIndex = _FcipDynamicRouteLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 7, 1, 2),
    _FcipDynamicRouteLinkIndex_Type()
)
fcipDynamicRouteLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipDynamicRouteLinkIndex.setStatus("current")
_FcipStaticRouteTable_Object = MibTable
fcipStaticRouteTable = _FcipStaticRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 8)
)
if mibBuilder.loadTexts:
    fcipStaticRouteTable.setStatus("current")
_FcipStaticRouteEntry_Object = MibTableRow
fcipStaticRouteEntry = _FcipStaticRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 8, 1)
)
fcipStaticRouteEntry.setIndexNames(
    (0, "FCIP-MGMT-MIB", "fcipEntityId"),
    (0, "FCIP-MGMT-MIB", "fcipStaticRouteDID"),
)
if mibBuilder.loadTexts:
    fcipStaticRouteEntry.setStatus("current")
_FcipStaticRouteDID_Type = FcipDomainIdInOctetForm
_FcipStaticRouteDID_Object = MibTableColumn
fcipStaticRouteDID = _FcipStaticRouteDID_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 8, 1, 1),
    _FcipStaticRouteDID_Type()
)
fcipStaticRouteDID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcipStaticRouteDID.setStatus("current")


class _FcipStaticRouteLinkIndex_Type(Unsigned32):
    """Custom type fcipStaticRouteLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcipStaticRouteLinkIndex_Type.__name__ = "Unsigned32"
_FcipStaticRouteLinkIndex_Object = MibTableColumn
fcipStaticRouteLinkIndex = _FcipStaticRouteLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 8, 1, 2),
    _FcipStaticRouteLinkIndex_Type()
)
fcipStaticRouteLinkIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipStaticRouteLinkIndex.setStatus("current")
_FcipStaticRouteStatus_Type = RowStatus
_FcipStaticRouteStatus_Object = MibTableColumn
fcipStaticRouteStatus = _FcipStaticRouteStatus_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 8, 1, 3),
    _FcipStaticRouteStatus_Type()
)
fcipStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcipStaticRouteStatus.setStatus("current")
_FcipDiscoveryDomainTable_Object = MibTable
fcipDiscoveryDomainTable = _FcipDiscoveryDomainTable_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 9)
)
if mibBuilder.loadTexts:
    fcipDiscoveryDomainTable.setStatus("current")
_FcipDiscoveryDomainEntry_Object = MibTableRow
fcipDiscoveryDomainEntry = _FcipDiscoveryDomainEntry_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 9, 1)
)
fcipDiscoveryDomainEntry.setIndexNames(
    (0, "FCIP-MGMT-MIB", "fcipEntityId"),
    (0, "FCIP-MGMT-MIB", "fcipDiscoveryDomainIndex"),
)
if mibBuilder.loadTexts:
    fcipDiscoveryDomainEntry.setStatus("current")


class _FcipDiscoveryDomainIndex_Type(Unsigned32):
    """Custom type fcipDiscoveryDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FcipDiscoveryDomainIndex_Type.__name__ = "Unsigned32"
_FcipDiscoveryDomainIndex_Object = MibTableColumn
fcipDiscoveryDomainIndex = _FcipDiscoveryDomainIndex_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 9, 1, 1),
    _FcipDiscoveryDomainIndex_Type()
)
fcipDiscoveryDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcipDiscoveryDomainIndex.setStatus("current")


class _FcipDiscoveryDomainName_Type(SnmpAdminString):
    """Custom type fcipDiscoveryDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FcipDiscoveryDomainName_Type.__name__ = "SnmpAdminString"
_FcipDiscoveryDomainName_Object = MibTableColumn
fcipDiscoveryDomainName = _FcipDiscoveryDomainName_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 9, 1, 2),
    _FcipDiscoveryDomainName_Type()
)
fcipDiscoveryDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcipDiscoveryDomainName.setStatus("current")
_FcipLinkErrorsTable_Object = MibTable
fcipLinkErrorsTable = _FcipLinkErrorsTable_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10)
)
if mibBuilder.loadTexts:
    fcipLinkErrorsTable.setStatus("current")
_FcipLinkErrorsEntry_Object = MibTableRow
fcipLinkErrorsEntry = _FcipLinkErrorsEntry_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1)
)
fcipLinkErrorsEntry.setIndexNames(
    (0, "FCIP-MGMT-MIB", "fcipEntityId"),
    (0, "FCIP-MGMT-MIB", "fcipLinkIndex"),
)
if mibBuilder.loadTexts:
    fcipLinkErrorsEntry.setStatus("current")
_FcipLinkFcipLossofFcSynchs_Type = Counter32
_FcipLinkFcipLossofFcSynchs_Object = MibTableColumn
fcipLinkFcipLossofFcSynchs = _FcipLinkFcipLossofFcSynchs_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 1),
    _FcipLinkFcipLossofFcSynchs_Type()
)
fcipLinkFcipLossofFcSynchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkFcipLossofFcSynchs.setStatus("current")
_FcipLinkFcipEncapErrors_Type = Counter32
_FcipLinkFcipEncapErrors_Object = MibTableColumn
fcipLinkFcipEncapErrors = _FcipLinkFcipEncapErrors_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 2),
    _FcipLinkFcipEncapErrors_Type()
)
fcipLinkFcipEncapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkFcipEncapErrors.setStatus("current")
_FcipLinkFcipNotReceivedSfResps_Type = Counter32
_FcipLinkFcipNotReceivedSfResps_Object = MibTableColumn
fcipLinkFcipNotReceivedSfResps = _FcipLinkFcipNotReceivedSfResps_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 3),
    _FcipLinkFcipNotReceivedSfResps_Type()
)
fcipLinkFcipNotReceivedSfResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkFcipNotReceivedSfResps.setStatus("current")
_FcipLinkFcipSfRespMismatches_Type = Counter32
_FcipLinkFcipSfRespMismatches_Object = MibTableColumn
fcipLinkFcipSfRespMismatches = _FcipLinkFcipSfRespMismatches_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 4),
    _FcipLinkFcipSfRespMismatches_Type()
)
fcipLinkFcipSfRespMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkFcipSfRespMismatches.setStatus("current")
_FcipLinkFcipSfInvalidNonces_Type = Counter32
_FcipLinkFcipSfInvalidNonces_Object = MibTableColumn
fcipLinkFcipSfInvalidNonces = _FcipLinkFcipSfInvalidNonces_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 5),
    _FcipLinkFcipSfInvalidNonces_Type()
)
fcipLinkFcipSfInvalidNonces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkFcipSfInvalidNonces.setStatus("current")
_FcipLinkFcipReceivedSfDuplicates_Type = Counter32
_FcipLinkFcipReceivedSfDuplicates_Object = MibTableColumn
fcipLinkFcipReceivedSfDuplicates = _FcipLinkFcipReceivedSfDuplicates_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 6),
    _FcipLinkFcipReceivedSfDuplicates_Type()
)
fcipLinkFcipReceivedSfDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkFcipReceivedSfDuplicates.setStatus("current")
_FcipLinkFcipSfInvalidWWNs_Type = Counter32
_FcipLinkFcipSfInvalidWWNs_Object = MibTableColumn
fcipLinkFcipSfInvalidWWNs = _FcipLinkFcipSfInvalidWWNs_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 7),
    _FcipLinkFcipSfInvalidWWNs_Type()
)
fcipLinkFcipSfInvalidWWNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkFcipSfInvalidWWNs.setStatus("current")
_FcipLinkFcipBB2LkaTimeOuts_Type = Counter32
_FcipLinkFcipBB2LkaTimeOuts_Object = MibTableColumn
fcipLinkFcipBB2LkaTimeOuts = _FcipLinkFcipBB2LkaTimeOuts_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 8),
    _FcipLinkFcipBB2LkaTimeOuts_Type()
)
fcipLinkFcipBB2LkaTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkFcipBB2LkaTimeOuts.setStatus("current")
_FcipLinkFcipSntpExpiredTimeStamps_Type = Counter32
_FcipLinkFcipSntpExpiredTimeStamps_Object = MibTableColumn
fcipLinkFcipSntpExpiredTimeStamps = _FcipLinkFcipSntpExpiredTimeStamps_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 9),
    _FcipLinkFcipSntpExpiredTimeStamps_Type()
)
fcipLinkFcipSntpExpiredTimeStamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkFcipSntpExpiredTimeStamps.setStatus("current")
_FcipLinkTcpTooManyErrors_Type = Counter32
_FcipLinkTcpTooManyErrors_Object = MibTableColumn
fcipLinkTcpTooManyErrors = _FcipLinkTcpTooManyErrors_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 10),
    _FcipLinkTcpTooManyErrors_Type()
)
fcipLinkTcpTooManyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkTcpTooManyErrors.setStatus("current")
_FcipLinkTcpExcessiveDroppedDatagrams_Type = Counter32
_FcipLinkTcpExcessiveDroppedDatagrams_Object = MibTableColumn
fcipLinkTcpExcessiveDroppedDatagrams = _FcipLinkTcpExcessiveDroppedDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 11),
    _FcipLinkTcpExcessiveDroppedDatagrams_Type()
)
fcipLinkTcpExcessiveDroppedDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkTcpExcessiveDroppedDatagrams.setStatus("current")
_FcipLinkTcpSaParamMismatches_Type = Counter32
_FcipLinkTcpSaParamMismatches_Object = MibTableColumn
fcipLinkTcpSaParamMismatches = _FcipLinkTcpSaParamMismatches_Object(
    (1, 3, 6, 1, 2, 1, 224, 1, 1, 10, 1, 12),
    _FcipLinkTcpSaParamMismatches_Type()
)
fcipLinkTcpSaParamMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipLinkTcpSaParamMismatches.setStatus("current")
_FcipConformance_ObjectIdentity = ObjectIdentity
fcipConformance = _FcipConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 224, 2)
)
_FcipCompliances_ObjectIdentity = ObjectIdentity
fcipCompliances = _FcipCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 224, 2, 1)
)
_FcipGroups_ObjectIdentity = ObjectIdentity
fcipGroups = _FcipGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 224, 2, 2)
)

# Managed Objects groups

fcipEntityScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 224, 2, 2, 1)
)
fcipEntityScalarGroup.setObjects(
      *(("FCIP-MGMT-MIB", "fcipDynIpConfType"),
        ("FCIP-MGMT-MIB", "fcipDeviceWWN"),
        ("FCIP-MGMT-MIB", "fcipEntitySACKOption"))
)
if mibBuilder.loadTexts:
    fcipEntityScalarGroup.setStatus("current")

fcipEntityInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 224, 2, 2, 2)
)
fcipEntityInstanceGroup.setObjects(
      *(("FCIP-MGMT-MIB", "fcipEntityName"),
        ("FCIP-MGMT-MIB", "fcipEntityAddressType"),
        ("FCIP-MGMT-MIB", "fcipEntityAddress"),
        ("FCIP-MGMT-MIB", "fcipEntityTcpConnPort"),
        ("FCIP-MGMT-MIB", "fcipEntitySeqNumWrap"),
        ("FCIP-MGMT-MIB", "fcipEntityPHBSupport"),
        ("FCIP-MGMT-MIB", "fcipEntityStatus"))
)
if mibBuilder.loadTexts:
    fcipEntityInstanceGroup.setStatus("current")

fcipLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 224, 2, 2, 3)
)
fcipLinkGroup.setObjects(
      *(("FCIP-MGMT-MIB", "fcipLinkIfIndex"),
        ("FCIP-MGMT-MIB", "fcipLinkCost"),
        ("FCIP-MGMT-MIB", "fcipLinkLocalFcipEntityMode"),
        ("FCIP-MGMT-MIB", "fcipLinkLocalFcipEntityAddressType"),
        ("FCIP-MGMT-MIB", "fcipLinkLocalFcipEntityAddress"),
        ("FCIP-MGMT-MIB", "fcipLinkRemFcipEntityWWN"),
        ("FCIP-MGMT-MIB", "fcipLinkRemFcipEntityId"),
        ("FCIP-MGMT-MIB", "fcipLinkRemFcipEntityAddressType"),
        ("FCIP-MGMT-MIB", "fcipLinkRemFcipEntityAddress"),
        ("FCIP-MGMT-MIB", "fcipLinkStatus"),
        ("FCIP-MGMT-MIB", "fcipLinkCreateTime"))
)
if mibBuilder.loadTexts:
    fcipLinkGroup.setStatus("current")

fcipTcpConnGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 224, 2, 2, 4)
)
fcipTcpConnGroup.setObjects(
      *(("FCIP-MGMT-MIB", "fcipTcpConnRWSize"),
        ("FCIP-MGMT-MIB", "fcipTcpConnMSS"))
)
if mibBuilder.loadTexts:
    fcipTcpConnGroup.setStatus("current")

fcipDiscoveryDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 224, 2, 2, 5)
)
fcipDiscoveryDomainGroup.setObjects(
    ("FCIP-MGMT-MIB", "fcipDiscoveryDomainName")
)
if mibBuilder.loadTexts:
    fcipDiscoveryDomainGroup.setStatus("current")

fcipLinkErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 224, 2, 2, 6)
)
fcipLinkErrorsGroup.setObjects(
      *(("FCIP-MGMT-MIB", "fcipLinkFcipLossofFcSynchs"),
        ("FCIP-MGMT-MIB", "fcipLinkFcipEncapErrors"),
        ("FCIP-MGMT-MIB", "fcipLinkFcipNotReceivedSfResps"),
        ("FCIP-MGMT-MIB", "fcipLinkFcipSfRespMismatches"),
        ("FCIP-MGMT-MIB", "fcipLinkFcipSfInvalidNonces"),
        ("FCIP-MGMT-MIB", "fcipLinkFcipReceivedSfDuplicates"),
        ("FCIP-MGMT-MIB", "fcipLinkFcipSfInvalidWWNs"),
        ("FCIP-MGMT-MIB", "fcipLinkFcipBB2LkaTimeOuts"),
        ("FCIP-MGMT-MIB", "fcipLinkFcipSntpExpiredTimeStamps"),
        ("FCIP-MGMT-MIB", "fcipLinkTcpTooManyErrors"),
        ("FCIP-MGMT-MIB", "fcipLinkTcpExcessiveDroppedDatagrams"),
        ("FCIP-MGMT-MIB", "fcipLinkTcpSaParamMismatches"))
)
if mibBuilder.loadTexts:
    fcipLinkErrorsGroup.setStatus("current")

fcipDynamicRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 224, 2, 2, 7)
)
fcipDynamicRouteGroup.setObjects(
    ("FCIP-MGMT-MIB", "fcipDynamicRouteLinkIndex")
)
if mibBuilder.loadTexts:
    fcipDynamicRouteGroup.setStatus("current")

fcipStaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 224, 2, 2, 8)
)
fcipStaticRouteGroup.setObjects(
      *(("FCIP-MGMT-MIB", "fcipStaticRouteLinkIndex"),
        ("FCIP-MGMT-MIB", "fcipStaticRouteStatus"))
)
if mibBuilder.loadTexts:
    fcipStaticRouteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fcipCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 224, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcipCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FCIP-MGMT-MIB",
    **{"FcipDomainIdInOctetForm": FcipDomainIdInOctetForm,
       "FcipEntityMode": FcipEntityMode,
       "FcipEntityId": FcipEntityId,
       "fcipMIB": fcipMIB,
       "fcipObjects": fcipObjects,
       "fcipConfig": fcipConfig,
       "fcipDynIpConfType": fcipDynIpConfType,
       "fcipDeviceWWN": fcipDeviceWWN,
       "fcipEntitySACKOption": fcipEntitySACKOption,
       "fcipEntityInstanceTable": fcipEntityInstanceTable,
       "fcipEntityInstanceEntry": fcipEntityInstanceEntry,
       "fcipEntityId": fcipEntityId,
       "fcipEntityName": fcipEntityName,
       "fcipEntityAddressType": fcipEntityAddressType,
       "fcipEntityAddress": fcipEntityAddress,
       "fcipEntityTcpConnPort": fcipEntityTcpConnPort,
       "fcipEntitySeqNumWrap": fcipEntitySeqNumWrap,
       "fcipEntityPHBSupport": fcipEntityPHBSupport,
       "fcipEntityStatus": fcipEntityStatus,
       "fcipLinkTable": fcipLinkTable,
       "fcipLinkEntry": fcipLinkEntry,
       "fcipLinkIndex": fcipLinkIndex,
       "fcipLinkIfIndex": fcipLinkIfIndex,
       "fcipLinkCost": fcipLinkCost,
       "fcipLinkLocalFcipEntityMode": fcipLinkLocalFcipEntityMode,
       "fcipLinkLocalFcipEntityAddressType": fcipLinkLocalFcipEntityAddressType,
       "fcipLinkLocalFcipEntityAddress": fcipLinkLocalFcipEntityAddress,
       "fcipLinkRemFcipEntityWWN": fcipLinkRemFcipEntityWWN,
       "fcipLinkRemFcipEntityId": fcipLinkRemFcipEntityId,
       "fcipLinkRemFcipEntityAddressType": fcipLinkRemFcipEntityAddressType,
       "fcipLinkRemFcipEntityAddress": fcipLinkRemFcipEntityAddress,
       "fcipLinkStatus": fcipLinkStatus,
       "fcipLinkCreateTime": fcipLinkCreateTime,
       "fcipTcpConnTable": fcipTcpConnTable,
       "fcipTcpConnEntry": fcipTcpConnEntry,
       "fcipTcpConnLocalPort": fcipTcpConnLocalPort,
       "fcipTcpConnRemPort": fcipTcpConnRemPort,
       "fcipTcpConnRWSize": fcipTcpConnRWSize,
       "fcipTcpConnMSS": fcipTcpConnMSS,
       "fcipDynamicRouteTable": fcipDynamicRouteTable,
       "fcipDynamicRouteEntry": fcipDynamicRouteEntry,
       "fcipDynamicRouteDID": fcipDynamicRouteDID,
       "fcipDynamicRouteLinkIndex": fcipDynamicRouteLinkIndex,
       "fcipStaticRouteTable": fcipStaticRouteTable,
       "fcipStaticRouteEntry": fcipStaticRouteEntry,
       "fcipStaticRouteDID": fcipStaticRouteDID,
       "fcipStaticRouteLinkIndex": fcipStaticRouteLinkIndex,
       "fcipStaticRouteStatus": fcipStaticRouteStatus,
       "fcipDiscoveryDomainTable": fcipDiscoveryDomainTable,
       "fcipDiscoveryDomainEntry": fcipDiscoveryDomainEntry,
       "fcipDiscoveryDomainIndex": fcipDiscoveryDomainIndex,
       "fcipDiscoveryDomainName": fcipDiscoveryDomainName,
       "fcipLinkErrorsTable": fcipLinkErrorsTable,
       "fcipLinkErrorsEntry": fcipLinkErrorsEntry,
       "fcipLinkFcipLossofFcSynchs": fcipLinkFcipLossofFcSynchs,
       "fcipLinkFcipEncapErrors": fcipLinkFcipEncapErrors,
       "fcipLinkFcipNotReceivedSfResps": fcipLinkFcipNotReceivedSfResps,
       "fcipLinkFcipSfRespMismatches": fcipLinkFcipSfRespMismatches,
       "fcipLinkFcipSfInvalidNonces": fcipLinkFcipSfInvalidNonces,
       "fcipLinkFcipReceivedSfDuplicates": fcipLinkFcipReceivedSfDuplicates,
       "fcipLinkFcipSfInvalidWWNs": fcipLinkFcipSfInvalidWWNs,
       "fcipLinkFcipBB2LkaTimeOuts": fcipLinkFcipBB2LkaTimeOuts,
       "fcipLinkFcipSntpExpiredTimeStamps": fcipLinkFcipSntpExpiredTimeStamps,
       "fcipLinkTcpTooManyErrors": fcipLinkTcpTooManyErrors,
       "fcipLinkTcpExcessiveDroppedDatagrams": fcipLinkTcpExcessiveDroppedDatagrams,
       "fcipLinkTcpSaParamMismatches": fcipLinkTcpSaParamMismatches,
       "fcipConformance": fcipConformance,
       "fcipCompliances": fcipCompliances,
       "fcipCompliance": fcipCompliance,
       "fcipGroups": fcipGroups,
       "fcipEntityScalarGroup": fcipEntityScalarGroup,
       "fcipEntityInstanceGroup": fcipEntityInstanceGroup,
       "fcipLinkGroup": fcipLinkGroup,
       "fcipTcpConnGroup": fcipTcpConnGroup,
       "fcipDiscoveryDomainGroup": fcipDiscoveryDomainGroup,
       "fcipLinkErrorsGroup": fcipLinkErrorsGroup,
       "fcipDynamicRouteGroup": fcipDynamicRouteGroup,
       "fcipStaticRouteGroup": fcipStaticRouteGroup}
)
