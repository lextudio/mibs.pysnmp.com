# SNMP MIB module (CISCO-FCIP-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FCIP-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:23 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(DomainId,
 FcNameId,
 FcNameIdOrZero) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainId",
    "FcNameId",
    "FcNameIdOrZero")

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

ciscoFcipMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 96)
)
ciscoFcipMgmtMIB.setRevisions(
        ("2003-05-19 00:00",
         "2002-10-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfmFcEntityMode(Integer32, TextualConvention):
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
        *(("bPortMode", 2),
          ("ePortMode", 1),
          ("other", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFcipObjects_ObjectIdentity = ObjectIdentity
ciscoFcipObjects = _CiscoFcipObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1)
)
_CfmFcipConfig_ObjectIdentity = ObjectIdentity
cfmFcipConfig = _CfmFcipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1)
)


class _CfmFcipDynIpConfType_Type(Integer32):
    """Custom type cfmFcipDynIpConfType based on Integer32"""
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


_CfmFcipDynIpConfType_Type.__name__ = "Integer32"
_CfmFcipDynIpConfType_Object = MibScalar
cfmFcipDynIpConfType = _CfmFcipDynIpConfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 1),
    _CfmFcipDynIpConfType_Type()
)
cfmFcipDynIpConfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmFcipDynIpConfType.setStatus("current")
_CfmFcipFabricWWN_Type = FcNameIdOrZero
_CfmFcipFabricWWN_Object = MibScalar
cfmFcipFabricWWN = _CfmFcipFabricWWN_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 2),
    _CfmFcipFabricWWN_Type()
)
cfmFcipFabricWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipFabricWWN.setStatus("current")
_CfmFcipEntityInstanceTable_Object = MibTable
cfmFcipEntityInstanceTable = _CfmFcipEntityInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfmFcipEntityInstanceTable.setStatus("current")
_CfmFcipEntityInstanceEntry_Object = MibTableRow
cfmFcipEntityInstanceEntry = _CfmFcipEntityInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3, 1)
)
cfmFcipEntityInstanceEntry.setIndexNames(
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipEntityId"),
)
if mibBuilder.loadTexts:
    cfmFcipEntityInstanceEntry.setStatus("current")
_CfmFcipEntityId_Type = Unsigned32
_CfmFcipEntityId_Object = MibTableColumn
cfmFcipEntityId = _CfmFcipEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3, 1, 1),
    _CfmFcipEntityId_Type()
)
cfmFcipEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFcipEntityId.setStatus("current")
_CfmFcipEntityAddressType_Type = InetAddressType
_CfmFcipEntityAddressType_Object = MibTableColumn
cfmFcipEntityAddressType = _CfmFcipEntityAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3, 1, 2),
    _CfmFcipEntityAddressType_Type()
)
cfmFcipEntityAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityAddressType.setStatus("current")
_CfmFcipEntityAddress_Type = InetAddress
_CfmFcipEntityAddress_Object = MibTableColumn
cfmFcipEntityAddress = _CfmFcipEntityAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3, 1, 3),
    _CfmFcipEntityAddress_Type()
)
cfmFcipEntityAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityAddress.setStatus("current")


class _CfmFcipEntityTcpConnPort_Type(Unsigned32):
    """Custom type cfmFcipEntityTcpConnPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfmFcipEntityTcpConnPort_Type.__name__ = "Unsigned32"
_CfmFcipEntityTcpConnPort_Object = MibTableColumn
cfmFcipEntityTcpConnPort = _CfmFcipEntityTcpConnPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3, 1, 4),
    _CfmFcipEntityTcpConnPort_Type()
)
cfmFcipEntityTcpConnPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityTcpConnPort.setStatus("current")


class _CfmFcipEntitySACKOption_Type(Integer32):
    """Custom type cfmFcipEntitySACKOption based on Integer32"""
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


_CfmFcipEntitySACKOption_Type.__name__ = "Integer32"
_CfmFcipEntitySACKOption_Object = MibTableColumn
cfmFcipEntitySACKOption = _CfmFcipEntitySACKOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3, 1, 5),
    _CfmFcipEntitySACKOption_Type()
)
cfmFcipEntitySACKOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntitySACKOption.setStatus("current")
_CfmFcipEntitySeqNumWrap_Type = TruthValue
_CfmFcipEntitySeqNumWrap_Object = MibTableColumn
cfmFcipEntitySeqNumWrap = _CfmFcipEntitySeqNumWrap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3, 1, 6),
    _CfmFcipEntitySeqNumWrap_Type()
)
cfmFcipEntitySeqNumWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipEntitySeqNumWrap.setStatus("current")
_CfmFcipEntityPHBSupport_Type = TruthValue
_CfmFcipEntityPHBSupport_Object = MibTableColumn
cfmFcipEntityPHBSupport = _CfmFcipEntityPHBSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3, 1, 7),
    _CfmFcipEntityPHBSupport_Type()
)
cfmFcipEntityPHBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipEntityPHBSupport.setStatus("current")
_CfmFcipEntityStatus_Type = RowStatus
_CfmFcipEntityStatus_Object = MibTableColumn
cfmFcipEntityStatus = _CfmFcipEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 3, 1, 8),
    _CfmFcipEntityStatus_Type()
)
cfmFcipEntityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityStatus.setStatus("current")
_CfmFcipLinkTable_Object = MibTable
cfmFcipLinkTable = _CfmFcipLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cfmFcipLinkTable.setStatus("current")
_CfmFcipLinkEntry_Object = MibTableRow
cfmFcipLinkEntry = _CfmFcipLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1)
)
cfmFcipLinkEntry.setIndexNames(
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipEntityId"),
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipLinkIndex"),
)
if mibBuilder.loadTexts:
    cfmFcipLinkEntry.setStatus("current")
_CfmFcipLinkIndex_Type = Unsigned32
_CfmFcipLinkIndex_Object = MibTableColumn
cfmFcipLinkIndex = _CfmFcipLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 1),
    _CfmFcipLinkIndex_Type()
)
cfmFcipLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFcipLinkIndex.setStatus("current")


class _CfmFcipLinkIfIndex_Type(Integer32):
    """Custom type cfmFcipLinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CfmFcipLinkIfIndex_Type.__name__ = "Integer32"
_CfmFcipLinkIfIndex_Object = MibTableColumn
cfmFcipLinkIfIndex = _CfmFcipLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 2),
    _CfmFcipLinkIfIndex_Type()
)
cfmFcipLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkIfIndex.setStatus("current")


class _CfmFcipLinkCost_Type(Unsigned32):
    """Custom type cfmFcipLinkCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfmFcipLinkCost_Type.__name__ = "Unsigned32"
_CfmFcipLinkCost_Object = MibTableColumn
cfmFcipLinkCost = _CfmFcipLinkCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 3),
    _CfmFcipLinkCost_Type()
)
cfmFcipLinkCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkCost.setStatus("current")
_CfmFcipLinkLocalFcipEntityMode_Type = CfmFcEntityMode
_CfmFcipLinkLocalFcipEntityMode_Object = MibTableColumn
cfmFcipLinkLocalFcipEntityMode = _CfmFcipLinkLocalFcipEntityMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 4),
    _CfmFcipLinkLocalFcipEntityMode_Type()
)
cfmFcipLinkLocalFcipEntityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkLocalFcipEntityMode.setStatus("current")
_CfmFcipLinkRemFcipEntityWWN_Type = FcNameIdOrZero
_CfmFcipLinkRemFcipEntityWWN_Object = MibTableColumn
cfmFcipLinkRemFcipEntityWWN = _CfmFcipLinkRemFcipEntityWWN_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 5),
    _CfmFcipLinkRemFcipEntityWWN_Type()
)
cfmFcipLinkRemFcipEntityWWN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkRemFcipEntityWWN.setStatus("current")


class _CfmFcipLinkRemFcipEntityId_Type(Unsigned32):
    """Custom type cfmFcipLinkRemFcipEntityId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CfmFcipLinkRemFcipEntityId_Type.__name__ = "Unsigned32"
_CfmFcipLinkRemFcipEntityId_Object = MibTableColumn
cfmFcipLinkRemFcipEntityId = _CfmFcipLinkRemFcipEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 6),
    _CfmFcipLinkRemFcipEntityId_Type()
)
cfmFcipLinkRemFcipEntityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkRemFcipEntityId.setStatus("current")
_CfmFcipLinkRemFcipEntityAddrType_Type = InetAddressType
_CfmFcipLinkRemFcipEntityAddrType_Object = MibTableColumn
cfmFcipLinkRemFcipEntityAddrType = _CfmFcipLinkRemFcipEntityAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 7),
    _CfmFcipLinkRemFcipEntityAddrType_Type()
)
cfmFcipLinkRemFcipEntityAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkRemFcipEntityAddrType.setStatus("current")
_CfmFcipLinkRemFcipEntityAddress_Type = InetAddress
_CfmFcipLinkRemFcipEntityAddress_Object = MibTableColumn
cfmFcipLinkRemFcipEntityAddress = _CfmFcipLinkRemFcipEntityAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 8),
    _CfmFcipLinkRemFcipEntityAddress_Type()
)
cfmFcipLinkRemFcipEntityAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkRemFcipEntityAddress.setStatus("current")
_CfmFcipLinkRemFcipEntityMode_Type = CfmFcEntityMode
_CfmFcipLinkRemFcipEntityMode_Object = MibTableColumn
cfmFcipLinkRemFcipEntityMode = _CfmFcipLinkRemFcipEntityMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 9),
    _CfmFcipLinkRemFcipEntityMode_Type()
)
cfmFcipLinkRemFcipEntityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkRemFcipEntityMode.setStatus("current")
_CfmFcipLinkStatus_Type = RowStatus
_CfmFcipLinkStatus_Object = MibTableColumn
cfmFcipLinkStatus = _CfmFcipLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 4, 1, 10),
    _CfmFcipLinkStatus_Type()
)
cfmFcipLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkStatus.setStatus("current")
_CfmFcipTcpConnTable_Object = MibTable
cfmFcipTcpConnTable = _CfmFcipTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cfmFcipTcpConnTable.setStatus("current")
_CfmFcipTcpConnEntry_Object = MibTableRow
cfmFcipTcpConnEntry = _CfmFcipTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 5, 1)
)
cfmFcipTcpConnEntry.setIndexNames(
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipEntityId"),
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipLinkIndex"),
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipTcpConnLocalPort"),
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipTcpConnRemPort"),
)
if mibBuilder.loadTexts:
    cfmFcipTcpConnEntry.setStatus("current")


class _CfmFcipTcpConnLocalPort_Type(Integer32):
    """Custom type cfmFcipTcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfmFcipTcpConnLocalPort_Type.__name__ = "Integer32"
_CfmFcipTcpConnLocalPort_Object = MibTableColumn
cfmFcipTcpConnLocalPort = _CfmFcipTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 5, 1, 1),
    _CfmFcipTcpConnLocalPort_Type()
)
cfmFcipTcpConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFcipTcpConnLocalPort.setStatus("current")


class _CfmFcipTcpConnRemPort_Type(Integer32):
    """Custom type cfmFcipTcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfmFcipTcpConnRemPort_Type.__name__ = "Integer32"
_CfmFcipTcpConnRemPort_Object = MibTableColumn
cfmFcipTcpConnRemPort = _CfmFcipTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 5, 1, 2),
    _CfmFcipTcpConnRemPort_Type()
)
cfmFcipTcpConnRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFcipTcpConnRemPort.setStatus("current")


class _CfmFcipTcpConnPurpose_Type(Integer32):
    """Custom type cfmFcipTcpConnPurpose based on Integer32"""
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
          ("control", 1),
          ("data", 2))
    )


_CfmFcipTcpConnPurpose_Type.__name__ = "Integer32"
_CfmFcipTcpConnPurpose_Object = MibTableColumn
cfmFcipTcpConnPurpose = _CfmFcipTcpConnPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 5, 1, 3),
    _CfmFcipTcpConnPurpose_Type()
)
cfmFcipTcpConnPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipTcpConnPurpose.setStatus("current")
_CfmFcipTcpConnRWSize_Type = Unsigned32
_CfmFcipTcpConnRWSize_Object = MibTableColumn
cfmFcipTcpConnRWSize = _CfmFcipTcpConnRWSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 5, 1, 4),
    _CfmFcipTcpConnRWSize_Type()
)
cfmFcipTcpConnRWSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipTcpConnRWSize.setStatus("current")
_CfmFcipTcpConnMSS_Type = Unsigned32
_CfmFcipTcpConnMSS_Object = MibTableColumn
cfmFcipTcpConnMSS = _CfmFcipTcpConnMSS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 5, 1, 5),
    _CfmFcipTcpConnMSS_Type()
)
cfmFcipTcpConnMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipTcpConnMSS.setStatus("current")
_CfmFcipTcpConnTimeOut_Type = Unsigned32
_CfmFcipTcpConnTimeOut_Object = MibTableColumn
cfmFcipTcpConnTimeOut = _CfmFcipTcpConnTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 5, 1, 6),
    _CfmFcipTcpConnTimeOut_Type()
)
cfmFcipTcpConnTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipTcpConnTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipTcpConnTimeOut.setUnits("seconds")
_CfmFcipDynamicRouteTable_Object = MibTable
cfmFcipDynamicRouteTable = _CfmFcipDynamicRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cfmFcipDynamicRouteTable.setStatus("current")
_CfmFcipDynamicRouteEntry_Object = MibTableRow
cfmFcipDynamicRouteEntry = _CfmFcipDynamicRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 6, 1)
)
cfmFcipDynamicRouteEntry.setIndexNames(
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipEntityId"),
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipDynamicRouteDID"),
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipDynamicRouteIndex"),
)
if mibBuilder.loadTexts:
    cfmFcipDynamicRouteEntry.setStatus("current")
_CfmFcipDynamicRouteIndex_Type = Unsigned32
_CfmFcipDynamicRouteIndex_Object = MibTableColumn
cfmFcipDynamicRouteIndex = _CfmFcipDynamicRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 6, 1, 1),
    _CfmFcipDynamicRouteIndex_Type()
)
cfmFcipDynamicRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFcipDynamicRouteIndex.setStatus("current")
_CfmFcipDynamicRouteDID_Type = DomainId
_CfmFcipDynamicRouteDID_Object = MibTableColumn
cfmFcipDynamicRouteDID = _CfmFcipDynamicRouteDID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 6, 1, 2),
    _CfmFcipDynamicRouteDID_Type()
)
cfmFcipDynamicRouteDID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFcipDynamicRouteDID.setStatus("current")
_CfmFcipDynamicRouteLinkIndex_Type = Unsigned32
_CfmFcipDynamicRouteLinkIndex_Object = MibTableColumn
cfmFcipDynamicRouteLinkIndex = _CfmFcipDynamicRouteLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 6, 1, 3),
    _CfmFcipDynamicRouteLinkIndex_Type()
)
cfmFcipDynamicRouteLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipDynamicRouteLinkIndex.setStatus("current")
_CfmFcipStaticRouteTable_Object = MibTable
cfmFcipStaticRouteTable = _CfmFcipStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cfmFcipStaticRouteTable.setStatus("current")
_CfmFcipStaticRouteEntry_Object = MibTableRow
cfmFcipStaticRouteEntry = _CfmFcipStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 7, 1)
)
cfmFcipStaticRouteEntry.setIndexNames(
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipEntityId"),
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipStaRtDID"),
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipStaRtIndex"),
)
if mibBuilder.loadTexts:
    cfmFcipStaticRouteEntry.setStatus("current")
_CfmFcipStaRtIndex_Type = Unsigned32
_CfmFcipStaRtIndex_Object = MibTableColumn
cfmFcipStaRtIndex = _CfmFcipStaRtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 7, 1, 1),
    _CfmFcipStaRtIndex_Type()
)
cfmFcipStaRtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFcipStaRtIndex.setStatus("current")
_CfmFcipStaRtDID_Type = DomainId
_CfmFcipStaRtDID_Object = MibTableColumn
cfmFcipStaRtDID = _CfmFcipStaRtDID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 7, 1, 2),
    _CfmFcipStaRtDID_Type()
)
cfmFcipStaRtDID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFcipStaRtDID.setStatus("current")
_CfmFcipStaRtRemFcipEntWWN_Type = FcNameId
_CfmFcipStaRtRemFcipEntWWN_Object = MibTableColumn
cfmFcipStaRtRemFcipEntWWN = _CfmFcipStaRtRemFcipEntWWN_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 7, 1, 3),
    _CfmFcipStaRtRemFcipEntWWN_Type()
)
cfmFcipStaRtRemFcipEntWWN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipStaRtRemFcipEntWWN.setStatus("current")
_CfmFcipStaRtRemFcipEntId_Type = Unsigned32
_CfmFcipStaRtRemFcipEntId_Object = MibTableColumn
cfmFcipStaRtRemFcipEntId = _CfmFcipStaRtRemFcipEntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 7, 1, 4),
    _CfmFcipStaRtRemFcipEntId_Type()
)
cfmFcipStaRtRemFcipEntId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipStaRtRemFcipEntId.setStatus("current")
_CfmFcipStaRtRemFcipEntAddrType_Type = InetAddressType
_CfmFcipStaRtRemFcipEntAddrType_Object = MibTableColumn
cfmFcipStaRtRemFcipEntAddrType = _CfmFcipStaRtRemFcipEntAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 7, 1, 5),
    _CfmFcipStaRtRemFcipEntAddrType_Type()
)
cfmFcipStaRtRemFcipEntAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipStaRtRemFcipEntAddrType.setStatus("current")
_CfmFcipStaRtRemFcipEntAddr_Type = InetAddress
_CfmFcipStaRtRemFcipEntAddr_Object = MibTableColumn
cfmFcipStaRtRemFcipEntAddr = _CfmFcipStaRtRemFcipEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 7, 1, 6),
    _CfmFcipStaRtRemFcipEntAddr_Type()
)
cfmFcipStaRtRemFcipEntAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipStaRtRemFcipEntAddr.setStatus("current")
_CfmFcipStaRtStatus_Type = RowStatus
_CfmFcipStaRtStatus_Object = MibTableColumn
cfmFcipStaRtStatus = _CfmFcipStaRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 7, 1, 7),
    _CfmFcipStaRtStatus_Type()
)
cfmFcipStaRtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipStaRtStatus.setStatus("current")
_CfmFcipLinkErrorsTable_Object = MibTable
cfmFcipLinkErrorsTable = _CfmFcipLinkErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cfmFcipLinkErrorsTable.setStatus("current")
_CfmFcipLinkErrorsEntry_Object = MibTableRow
cfmFcipLinkErrorsEntry = _CfmFcipLinkErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1)
)
cfmFcipLinkErrorsEntry.setIndexNames(
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipEntityId"),
    (0, "CISCO-FCIP-MGMT-MIB", "cfmFcipLinkIndex"),
)
if mibBuilder.loadTexts:
    cfmFcipLinkErrorsEntry.setStatus("current")
_CfmFcipLinkFcipLossofFcSynchs_Type = Counter64
_CfmFcipLinkFcipLossofFcSynchs_Object = MibTableColumn
cfmFcipLinkFcipLossofFcSynchs = _CfmFcipLinkFcipLossofFcSynchs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 1),
    _CfmFcipLinkFcipLossofFcSynchs_Type()
)
cfmFcipLinkFcipLossofFcSynchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkFcipLossofFcSynchs.setStatus("current")
_CfmFcipLinkFcipSfNotRcv_Type = Counter64
_CfmFcipLinkFcipSfNotRcv_Object = MibTableColumn
cfmFcipLinkFcipSfNotRcv = _CfmFcipLinkFcipSfNotRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 2),
    _CfmFcipLinkFcipSfNotRcv_Type()
)
cfmFcipLinkFcipSfNotRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkFcipSfNotRcv.setStatus("current")
_CfmFcipLinkFcipSfRespNotRcv_Type = Counter64
_CfmFcipLinkFcipSfRespNotRcv_Object = MibTableColumn
cfmFcipLinkFcipSfRespNotRcv = _CfmFcipLinkFcipSfRespNotRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 3),
    _CfmFcipLinkFcipSfRespNotRcv_Type()
)
cfmFcipLinkFcipSfRespNotRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkFcipSfRespNotRcv.setStatus("current")
_CfmFcipLinkFcipSfRespMismatch_Type = Counter64
_CfmFcipLinkFcipSfRespMismatch_Object = MibTableColumn
cfmFcipLinkFcipSfRespMismatch = _CfmFcipLinkFcipSfRespMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 4),
    _CfmFcipLinkFcipSfRespMismatch_Type()
)
cfmFcipLinkFcipSfRespMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkFcipSfRespMismatch.setStatus("current")
_CfmFcipLinkFcipSfInvalidNonce_Type = Counter64
_CfmFcipLinkFcipSfInvalidNonce_Object = MibTableColumn
cfmFcipLinkFcipSfInvalidNonce = _CfmFcipLinkFcipSfInvalidNonce_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 5),
    _CfmFcipLinkFcipSfInvalidNonce_Type()
)
cfmFcipLinkFcipSfInvalidNonce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkFcipSfInvalidNonce.setStatus("current")
_CfmFcipLinkFcipDuplicateSfRcv_Type = Counter64
_CfmFcipLinkFcipDuplicateSfRcv_Object = MibTableColumn
cfmFcipLinkFcipDuplicateSfRcv = _CfmFcipLinkFcipDuplicateSfRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 6),
    _CfmFcipLinkFcipDuplicateSfRcv_Type()
)
cfmFcipLinkFcipDuplicateSfRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkFcipDuplicateSfRcv.setStatus("current")
_CfmFcipLinkFcipSfInvalidWWN_Type = Counter64
_CfmFcipLinkFcipSfInvalidWWN_Object = MibTableColumn
cfmFcipLinkFcipSfInvalidWWN = _CfmFcipLinkFcipSfInvalidWWN_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 7),
    _CfmFcipLinkFcipSfInvalidWWN_Type()
)
cfmFcipLinkFcipSfInvalidWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkFcipSfInvalidWWN.setStatus("current")
_CfmFcipLinkFcipBB2LkaTimeOut_Type = Counter64
_CfmFcipLinkFcipBB2LkaTimeOut_Object = MibTableColumn
cfmFcipLinkFcipBB2LkaTimeOut = _CfmFcipLinkFcipBB2LkaTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 8),
    _CfmFcipLinkFcipBB2LkaTimeOut_Type()
)
cfmFcipLinkFcipBB2LkaTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkFcipBB2LkaTimeOut.setStatus("current")
_CfmFcipLinkFcipSntpTimeStampExp_Type = Counter64
_CfmFcipLinkFcipSntpTimeStampExp_Object = MibTableColumn
cfmFcipLinkFcipSntpTimeStampExp = _CfmFcipLinkFcipSntpTimeStampExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 9),
    _CfmFcipLinkFcipSntpTimeStampExp_Type()
)
cfmFcipLinkFcipSntpTimeStampExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkFcipSntpTimeStampExp.setStatus("current")
_CfmFcipLinkTcpTooManyErrors_Type = Counter64
_CfmFcipLinkTcpTooManyErrors_Object = MibTableColumn
cfmFcipLinkTcpTooManyErrors = _CfmFcipLinkTcpTooManyErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 10),
    _CfmFcipLinkTcpTooManyErrors_Type()
)
cfmFcipLinkTcpTooManyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkTcpTooManyErrors.setStatus("current")
_CfmFcipLinkTcpKeepAliveTimeOut_Type = Counter64
_CfmFcipLinkTcpKeepAliveTimeOut_Object = MibTableColumn
cfmFcipLinkTcpKeepAliveTimeOut = _CfmFcipLinkTcpKeepAliveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 11),
    _CfmFcipLinkTcpKeepAliveTimeOut_Type()
)
cfmFcipLinkTcpKeepAliveTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkTcpKeepAliveTimeOut.setStatus("current")
_CfmFcipLinkTcpExDatagramsDropped_Type = Counter64
_CfmFcipLinkTcpExDatagramsDropped_Object = MibTableColumn
cfmFcipLinkTcpExDatagramsDropped = _CfmFcipLinkTcpExDatagramsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 12),
    _CfmFcipLinkTcpExDatagramsDropped_Type()
)
cfmFcipLinkTcpExDatagramsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkTcpExDatagramsDropped.setStatus("current")
_CfmFcipLinkTcpSaParamMismatch_Type = Counter64
_CfmFcipLinkTcpSaParamMismatch_Object = MibTableColumn
cfmFcipLinkTcpSaParamMismatch = _CfmFcipLinkTcpSaParamMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 1, 8, 1, 13),
    _CfmFcipLinkTcpSaParamMismatch_Type()
)
cfmFcipLinkTcpSaParamMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkTcpSaParamMismatch.setStatus("current")
_CfmFcipNotification_ObjectIdentity = ObjectIdentity
cfmFcipNotification = _CfmFcipNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 2)
)
_CfmFcipNotifications_ObjectIdentity = ObjectIdentity
cfmFcipNotifications = _CfmFcipNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 1, 2, 0)
)
_CfmFcipConformance_ObjectIdentity = ObjectIdentity
cfmFcipConformance = _CfmFcipConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2)
)
_CfmFcipCompliances_ObjectIdentity = ObjectIdentity
cfmFcipCompliances = _CfmFcipCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 1)
)
_CfmFcipGroups_ObjectIdentity = ObjectIdentity
cfmFcipGroups = _CfmFcipGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 2)
)

# Managed Objects groups

cfmFcipEntityScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 2, 1)
)
cfmFcipEntityScalarGroup.setObjects(
      *(("CISCO-FCIP-MGMT-MIB", "cfmFcipDynIpConfType"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipFabricWWN"))
)
if mibBuilder.loadTexts:
    cfmFcipEntityScalarGroup.setStatus("current")

cfmFcipEntityInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 2, 2)
)
cfmFcipEntityInstanceGroup.setObjects(
      *(("CISCO-FCIP-MGMT-MIB", "cfmFcipEntityAddressType"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipEntityAddress"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipEntityTcpConnPort"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipEntitySACKOption"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipEntitySeqNumWrap"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipEntityPHBSupport"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipEntityStatus"))
)
if mibBuilder.loadTexts:
    cfmFcipEntityInstanceGroup.setStatus("current")

cfmFcipLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 2, 3)
)
cfmFcipLinkGroup.setObjects(
      *(("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkIfIndex"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkCost"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkLocalFcipEntityMode"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkRemFcipEntityWWN"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkRemFcipEntityId"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkRemFcipEntityAddrType"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkRemFcipEntityAddress"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkRemFcipEntityMode"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkStatus"))
)
if mibBuilder.loadTexts:
    cfmFcipLinkGroup.setStatus("current")

cfmFcipTcpConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 2, 4)
)
cfmFcipTcpConnGroup.setObjects(
      *(("CISCO-FCIP-MGMT-MIB", "cfmFcipTcpConnPurpose"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipTcpConnRWSize"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipTcpConnMSS"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipTcpConnTimeOut"))
)
if mibBuilder.loadTexts:
    cfmFcipTcpConnGroup.setStatus("current")

cfmFcipDynamicRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 2, 5)
)
cfmFcipDynamicRouteGroup.setObjects(
    ("CISCO-FCIP-MGMT-MIB", "cfmFcipDynamicRouteLinkIndex")
)
if mibBuilder.loadTexts:
    cfmFcipDynamicRouteGroup.setStatus("current")

cfmFcipStaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 2, 6)
)
cfmFcipStaticRouteGroup.setObjects(
      *(("CISCO-FCIP-MGMT-MIB", "cfmFcipStaRtRemFcipEntWWN"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipStaRtRemFcipEntId"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipStaRtRemFcipEntAddrType"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipStaRtRemFcipEntAddr"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipStaRtStatus"))
)
if mibBuilder.loadTexts:
    cfmFcipStaticRouteGroup.setStatus("current")

cfmFcipLinkErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 2, 7)
)
cfmFcipLinkErrorsGroup.setObjects(
      *(("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkFcipLossofFcSynchs"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkFcipSfNotRcv"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkFcipSfRespNotRcv"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkFcipSfRespMismatch"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkFcipSfInvalidNonce"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkFcipDuplicateSfRcv"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkFcipSfInvalidWWN"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkFcipBB2LkaTimeOut"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkFcipSntpTimeStampExp"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkTcpTooManyErrors"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkTcpKeepAliveTimeOut"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkTcpExDatagramsDropped"),
        ("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkTcpSaParamMismatch"))
)
if mibBuilder.loadTexts:
    cfmFcipLinkErrorsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cfmFcipCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 96, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfmFcipCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FCIP-MGMT-MIB",
    **{"CfmFcEntityMode": CfmFcEntityMode,
       "ciscoFcipMgmtMIB": ciscoFcipMgmtMIB,
       "ciscoFcipObjects": ciscoFcipObjects,
       "cfmFcipConfig": cfmFcipConfig,
       "cfmFcipDynIpConfType": cfmFcipDynIpConfType,
       "cfmFcipFabricWWN": cfmFcipFabricWWN,
       "cfmFcipEntityInstanceTable": cfmFcipEntityInstanceTable,
       "cfmFcipEntityInstanceEntry": cfmFcipEntityInstanceEntry,
       "cfmFcipEntityId": cfmFcipEntityId,
       "cfmFcipEntityAddressType": cfmFcipEntityAddressType,
       "cfmFcipEntityAddress": cfmFcipEntityAddress,
       "cfmFcipEntityTcpConnPort": cfmFcipEntityTcpConnPort,
       "cfmFcipEntitySACKOption": cfmFcipEntitySACKOption,
       "cfmFcipEntitySeqNumWrap": cfmFcipEntitySeqNumWrap,
       "cfmFcipEntityPHBSupport": cfmFcipEntityPHBSupport,
       "cfmFcipEntityStatus": cfmFcipEntityStatus,
       "cfmFcipLinkTable": cfmFcipLinkTable,
       "cfmFcipLinkEntry": cfmFcipLinkEntry,
       "cfmFcipLinkIndex": cfmFcipLinkIndex,
       "cfmFcipLinkIfIndex": cfmFcipLinkIfIndex,
       "cfmFcipLinkCost": cfmFcipLinkCost,
       "cfmFcipLinkLocalFcipEntityMode": cfmFcipLinkLocalFcipEntityMode,
       "cfmFcipLinkRemFcipEntityWWN": cfmFcipLinkRemFcipEntityWWN,
       "cfmFcipLinkRemFcipEntityId": cfmFcipLinkRemFcipEntityId,
       "cfmFcipLinkRemFcipEntityAddrType": cfmFcipLinkRemFcipEntityAddrType,
       "cfmFcipLinkRemFcipEntityAddress": cfmFcipLinkRemFcipEntityAddress,
       "cfmFcipLinkRemFcipEntityMode": cfmFcipLinkRemFcipEntityMode,
       "cfmFcipLinkStatus": cfmFcipLinkStatus,
       "cfmFcipTcpConnTable": cfmFcipTcpConnTable,
       "cfmFcipTcpConnEntry": cfmFcipTcpConnEntry,
       "cfmFcipTcpConnLocalPort": cfmFcipTcpConnLocalPort,
       "cfmFcipTcpConnRemPort": cfmFcipTcpConnRemPort,
       "cfmFcipTcpConnPurpose": cfmFcipTcpConnPurpose,
       "cfmFcipTcpConnRWSize": cfmFcipTcpConnRWSize,
       "cfmFcipTcpConnMSS": cfmFcipTcpConnMSS,
       "cfmFcipTcpConnTimeOut": cfmFcipTcpConnTimeOut,
       "cfmFcipDynamicRouteTable": cfmFcipDynamicRouteTable,
       "cfmFcipDynamicRouteEntry": cfmFcipDynamicRouteEntry,
       "cfmFcipDynamicRouteIndex": cfmFcipDynamicRouteIndex,
       "cfmFcipDynamicRouteDID": cfmFcipDynamicRouteDID,
       "cfmFcipDynamicRouteLinkIndex": cfmFcipDynamicRouteLinkIndex,
       "cfmFcipStaticRouteTable": cfmFcipStaticRouteTable,
       "cfmFcipStaticRouteEntry": cfmFcipStaticRouteEntry,
       "cfmFcipStaRtIndex": cfmFcipStaRtIndex,
       "cfmFcipStaRtDID": cfmFcipStaRtDID,
       "cfmFcipStaRtRemFcipEntWWN": cfmFcipStaRtRemFcipEntWWN,
       "cfmFcipStaRtRemFcipEntId": cfmFcipStaRtRemFcipEntId,
       "cfmFcipStaRtRemFcipEntAddrType": cfmFcipStaRtRemFcipEntAddrType,
       "cfmFcipStaRtRemFcipEntAddr": cfmFcipStaRtRemFcipEntAddr,
       "cfmFcipStaRtStatus": cfmFcipStaRtStatus,
       "cfmFcipLinkErrorsTable": cfmFcipLinkErrorsTable,
       "cfmFcipLinkErrorsEntry": cfmFcipLinkErrorsEntry,
       "cfmFcipLinkFcipLossofFcSynchs": cfmFcipLinkFcipLossofFcSynchs,
       "cfmFcipLinkFcipSfNotRcv": cfmFcipLinkFcipSfNotRcv,
       "cfmFcipLinkFcipSfRespNotRcv": cfmFcipLinkFcipSfRespNotRcv,
       "cfmFcipLinkFcipSfRespMismatch": cfmFcipLinkFcipSfRespMismatch,
       "cfmFcipLinkFcipSfInvalidNonce": cfmFcipLinkFcipSfInvalidNonce,
       "cfmFcipLinkFcipDuplicateSfRcv": cfmFcipLinkFcipDuplicateSfRcv,
       "cfmFcipLinkFcipSfInvalidWWN": cfmFcipLinkFcipSfInvalidWWN,
       "cfmFcipLinkFcipBB2LkaTimeOut": cfmFcipLinkFcipBB2LkaTimeOut,
       "cfmFcipLinkFcipSntpTimeStampExp": cfmFcipLinkFcipSntpTimeStampExp,
       "cfmFcipLinkTcpTooManyErrors": cfmFcipLinkTcpTooManyErrors,
       "cfmFcipLinkTcpKeepAliveTimeOut": cfmFcipLinkTcpKeepAliveTimeOut,
       "cfmFcipLinkTcpExDatagramsDropped": cfmFcipLinkTcpExDatagramsDropped,
       "cfmFcipLinkTcpSaParamMismatch": cfmFcipLinkTcpSaParamMismatch,
       "cfmFcipNotification": cfmFcipNotification,
       "cfmFcipNotifications": cfmFcipNotifications,
       "cfmFcipConformance": cfmFcipConformance,
       "cfmFcipCompliances": cfmFcipCompliances,
       "cfmFcipCompliance": cfmFcipCompliance,
       "cfmFcipGroups": cfmFcipGroups,
       "cfmFcipEntityScalarGroup": cfmFcipEntityScalarGroup,
       "cfmFcipEntityInstanceGroup": cfmFcipEntityInstanceGroup,
       "cfmFcipLinkGroup": cfmFcipLinkGroup,
       "cfmFcipTcpConnGroup": cfmFcipTcpConnGroup,
       "cfmFcipDynamicRouteGroup": cfmFcipDynamicRouteGroup,
       "cfmFcipStaticRouteGroup": cfmFcipStaticRouteGroup,
       "cfmFcipLinkErrorsGroup": cfmFcipLinkErrorsGroup}
)
