# SNMP MIB module (CISCO-FILTER-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FILTER-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:32 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoIpProtocol,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoIpProtocol")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoFilterGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 474)
)
ciscoFilterGroupMIB.setRevisions(
        ("2005-04-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfgFilterGroupName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFilterGroupMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFilterGroupMIBNotifs = _CiscoFilterGroupMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 0)
)
_CiscoFilterGroupMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFilterGroupMIBObjects = _CiscoFilterGroupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1)
)
_CfgFilterConfig_ObjectIdentity = ObjectIdentity
cfgFilterConfig = _CfgFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1)
)
_CfgFilterGroupTable_Object = MibTable
cfgFilterGroupTable = _CfgFilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfgFilterGroupTable.setStatus("current")
_CfgFilterGroupEntry_Object = MibTableRow
cfgFilterGroupEntry = _CfgFilterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1)
)
cfgFilterGroupEntry.setIndexNames(
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"),
)
if mibBuilder.loadTexts:
    cfgFilterGroupEntry.setStatus("current")
_CfgFilterGroupName_Type = CfgFilterGroupName
_CfgFilterGroupName_Object = MibTableColumn
cfgFilterGroupName = _CfgFilterGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 1),
    _CfgFilterGroupName_Type()
)
cfgFilterGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFilterGroupName.setStatus("current")


class _CfgFilterGroupType_Type(Integer32):
    """Custom type cfgFilterGroupType based on Integer32"""
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
        *(("icmp", 4),
          ("ipProtocol", 2),
          ("ipService", 3),
          ("network", 1))
    )


_CfgFilterGroupType_Type.__name__ = "Integer32"
_CfgFilterGroupType_Object = MibTableColumn
cfgFilterGroupType = _CfgFilterGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 2),
    _CfgFilterGroupType_Type()
)
cfgFilterGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterGroupType.setStatus("current")
_CfgFilterGroupDescription_Type = SnmpAdminString
_CfgFilterGroupDescription_Object = MibTableColumn
cfgFilterGroupDescription = _CfgFilterGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 3),
    _CfgFilterGroupDescription_Type()
)
cfgFilterGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterGroupDescription.setStatus("current")


class _CfgFilterGroupStorageType_Type(StorageType):
    """Custom type cfgFilterGroupStorageType based on StorageType"""


_CfgFilterGroupStorageType_Object = MibTableColumn
cfgFilterGroupStorageType = _CfgFilterGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 4),
    _CfgFilterGroupStorageType_Type()
)
cfgFilterGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterGroupStorageType.setStatus("current")
_CfgFilterGroupRowStatus_Type = RowStatus
_CfgFilterGroupRowStatus_Object = MibTableColumn
cfgFilterGroupRowStatus = _CfgFilterGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 5),
    _CfgFilterGroupRowStatus_Type()
)
cfgFilterGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterGroupRowStatus.setStatus("current")
_CfgFilterNetworkGroupTable_Object = MibTable
cfgFilterNetworkGroupTable = _CfgFilterNetworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfgFilterNetworkGroupTable.setStatus("current")
_CfgFilterNetworkGroupEntry_Object = MibTableRow
cfgFilterNetworkGroupEntry = _CfgFilterNetworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1)
)
cfgFilterNetworkGroupEntry.setIndexNames(
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"),
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkGroupIndex"),
)
if mibBuilder.loadTexts:
    cfgFilterNetworkGroupEntry.setStatus("current")
_CfgFilterNetworkGroupIndex_Type = Unsigned32
_CfgFilterNetworkGroupIndex_Object = MibTableColumn
cfgFilterNetworkGroupIndex = _CfgFilterNetworkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 1),
    _CfgFilterNetworkGroupIndex_Type()
)
cfgFilterNetworkGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFilterNetworkGroupIndex.setStatus("current")
_CfgFilterNetworkAddressType_Type = InetAddressType
_CfgFilterNetworkAddressType_Object = MibTableColumn
cfgFilterNetworkAddressType = _CfgFilterNetworkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 2),
    _CfgFilterNetworkAddressType_Type()
)
cfgFilterNetworkAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterNetworkAddressType.setStatus("current")


class _CfgFilterNetworkAddress_Type(InetAddress):
    """Custom type cfgFilterNetworkAddress based on InetAddress"""
    defaultValue = OctetString("0")


_CfgFilterNetworkAddress_Object = MibTableColumn
cfgFilterNetworkAddress = _CfgFilterNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 3),
    _CfgFilterNetworkAddress_Type()
)
cfgFilterNetworkAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterNetworkAddress.setStatus("current")


class _CfgFilterNetworkMask_Type(InetAddress):
    """Custom type cfgFilterNetworkMask based on InetAddress"""
    defaultHexValue = "ffffffff"


_CfgFilterNetworkMask_Object = MibTableColumn
cfgFilterNetworkMask = _CfgFilterNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 4),
    _CfgFilterNetworkMask_Type()
)
cfgFilterNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterNetworkMask.setStatus("current")


class _CfgFilterNetworkStorageType_Type(StorageType):
    """Custom type cfgFilterNetworkStorageType based on StorageType"""


_CfgFilterNetworkStorageType_Object = MibTableColumn
cfgFilterNetworkStorageType = _CfgFilterNetworkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 5),
    _CfgFilterNetworkStorageType_Type()
)
cfgFilterNetworkStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterNetworkStorageType.setStatus("current")
_CfgFilterNetworkRowStatus_Type = RowStatus
_CfgFilterNetworkRowStatus_Object = MibTableColumn
cfgFilterNetworkRowStatus = _CfgFilterNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 6),
    _CfgFilterNetworkRowStatus_Type()
)
cfgFilterNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterNetworkRowStatus.setStatus("current")
_CfgFilterIpProtocolGroupTable_Object = MibTable
cfgFilterIpProtocolGroupTable = _CfgFilterIpProtocolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfgFilterIpProtocolGroupTable.setStatus("current")
_CfgFilterIpProtocolGroupEntry_Object = MibTableRow
cfgFilterIpProtocolGroupEntry = _CfgFilterIpProtocolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1)
)
cfgFilterIpProtocolGroupEntry.setIndexNames(
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"),
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterIpProtocolGroupIndex"),
)
if mibBuilder.loadTexts:
    cfgFilterIpProtocolGroupEntry.setStatus("current")
_CfgFilterIpProtocolGroupIndex_Type = Unsigned32
_CfgFilterIpProtocolGroupIndex_Object = MibTableColumn
cfgFilterIpProtocolGroupIndex = _CfgFilterIpProtocolGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1, 1),
    _CfgFilterIpProtocolGroupIndex_Type()
)
cfgFilterIpProtocolGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFilterIpProtocolGroupIndex.setStatus("current")


class _CfgFilterIpProtocolNumber_Type(CiscoIpProtocol):
    """Custom type cfgFilterIpProtocolNumber based on CiscoIpProtocol"""
    defaultValue = 0


_CfgFilterIpProtocolNumber_Object = MibTableColumn
cfgFilterIpProtocolNumber = _CfgFilterIpProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1, 2),
    _CfgFilterIpProtocolNumber_Type()
)
cfgFilterIpProtocolNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterIpProtocolNumber.setStatus("current")


class _CfgFilterIpProtocolStorageType_Type(StorageType):
    """Custom type cfgFilterIpProtocolStorageType based on StorageType"""


_CfgFilterIpProtocolStorageType_Object = MibTableColumn
cfgFilterIpProtocolStorageType = _CfgFilterIpProtocolStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1, 3),
    _CfgFilterIpProtocolStorageType_Type()
)
cfgFilterIpProtocolStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterIpProtocolStorageType.setStatus("current")
_CfgFilterIpProtocolGroupRowStatus_Type = RowStatus
_CfgFilterIpProtocolGroupRowStatus_Object = MibTableColumn
cfgFilterIpProtocolGroupRowStatus = _CfgFilterIpProtocolGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1, 4),
    _CfgFilterIpProtocolGroupRowStatus_Type()
)
cfgFilterIpProtocolGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterIpProtocolGroupRowStatus.setStatus("current")
_CfgFilterIpServiceGroupTable_Object = MibTable
cfgFilterIpServiceGroupTable = _CfgFilterIpServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cfgFilterIpServiceGroupTable.setStatus("current")
_CfgFilterIpServiceGroupEntry_Object = MibTableRow
cfgFilterIpServiceGroupEntry = _CfgFilterIpServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1)
)
cfgFilterIpServiceGroupEntry.setIndexNames(
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"),
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterIpServiceGroupIndex"),
)
if mibBuilder.loadTexts:
    cfgFilterIpServiceGroupEntry.setStatus("current")
_CfgFilterIpServiceGroupIndex_Type = Unsigned32
_CfgFilterIpServiceGroupIndex_Object = MibTableColumn
cfgFilterIpServiceGroupIndex = _CfgFilterIpServiceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 1),
    _CfgFilterIpServiceGroupIndex_Type()
)
cfgFilterIpServiceGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFilterIpServiceGroupIndex.setStatus("current")


class _CfgFilterIpServiceType_Type(Integer32):
    """Custom type cfgFilterIpServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("tcpUdp", 3),
          ("udp", 2))
    )


_CfgFilterIpServiceType_Type.__name__ = "Integer32"
_CfgFilterIpServiceType_Object = MibTableColumn
cfgFilterIpServiceType = _CfgFilterIpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 2),
    _CfgFilterIpServiceType_Type()
)
cfgFilterIpServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterIpServiceType.setStatus("current")


class _CfgFilterIpServicePortLow_Type(InetPortNumber):
    """Custom type cfgFilterIpServicePortLow based on InetPortNumber"""
    defaultValue = 0


_CfgFilterIpServicePortLow_Object = MibTableColumn
cfgFilterIpServicePortLow = _CfgFilterIpServicePortLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 3),
    _CfgFilterIpServicePortLow_Type()
)
cfgFilterIpServicePortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterIpServicePortLow.setStatus("current")


class _CfgFilterIpServicePortHigh_Type(InetPortNumber):
    """Custom type cfgFilterIpServicePortHigh based on InetPortNumber"""
    defaultValue = 65535


_CfgFilterIpServicePortHigh_Object = MibTableColumn
cfgFilterIpServicePortHigh = _CfgFilterIpServicePortHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 4),
    _CfgFilterIpServicePortHigh_Type()
)
cfgFilterIpServicePortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterIpServicePortHigh.setStatus("current")


class _CfgFilterIpServiceStorageType_Type(StorageType):
    """Custom type cfgFilterIpServiceStorageType based on StorageType"""


_CfgFilterIpServiceStorageType_Object = MibTableColumn
cfgFilterIpServiceStorageType = _CfgFilterIpServiceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 5),
    _CfgFilterIpServiceStorageType_Type()
)
cfgFilterIpServiceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterIpServiceStorageType.setStatus("current")
_CfgFilterIpServiceGroupRowStatus_Type = RowStatus
_CfgFilterIpServiceGroupRowStatus_Object = MibTableColumn
cfgFilterIpServiceGroupRowStatus = _CfgFilterIpServiceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 6),
    _CfgFilterIpServiceGroupRowStatus_Type()
)
cfgFilterIpServiceGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterIpServiceGroupRowStatus.setStatus("current")
_CfgFilterICMPGroupTable_Object = MibTable
cfgFilterICMPGroupTable = _CfgFilterICMPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cfgFilterICMPGroupTable.setStatus("current")
_CfgFilterICMPGroupEntry_Object = MibTableRow
cfgFilterICMPGroupEntry = _CfgFilterICMPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1)
)
cfgFilterICMPGroupEntry.setIndexNames(
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"),
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterICMPGroupIndex"),
)
if mibBuilder.loadTexts:
    cfgFilterICMPGroupEntry.setStatus("current")
_CfgFilterICMPGroupIndex_Type = Unsigned32
_CfgFilterICMPGroupIndex_Object = MibTableColumn
cfgFilterICMPGroupIndex = _CfgFilterICMPGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 1),
    _CfgFilterICMPGroupIndex_Type()
)
cfgFilterICMPGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFilterICMPGroupIndex.setStatus("current")


class _CfgFilterICMPType_Type(Integer32):
    """Custom type cfgFilterICMPType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CfgFilterICMPType_Type.__name__ = "Integer32"
_CfgFilterICMPType_Object = MibTableColumn
cfgFilterICMPType = _CfgFilterICMPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 2),
    _CfgFilterICMPType_Type()
)
cfgFilterICMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterICMPType.setStatus("current")


class _CfgFilterICMPCode_Type(Integer32):
    """Custom type cfgFilterICMPCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CfgFilterICMPCode_Type.__name__ = "Integer32"
_CfgFilterICMPCode_Object = MibTableColumn
cfgFilterICMPCode = _CfgFilterICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 3),
    _CfgFilterICMPCode_Type()
)
cfgFilterICMPCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterICMPCode.setStatus("current")


class _CfgFilterICMPStorageType_Type(StorageType):
    """Custom type cfgFilterICMPStorageType based on StorageType"""


_CfgFilterICMPStorageType_Object = MibTableColumn
cfgFilterICMPStorageType = _CfgFilterICMPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 4),
    _CfgFilterICMPStorageType_Type()
)
cfgFilterICMPStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterICMPStorageType.setStatus("current")
_CfgFilterICMPGroupRowStatus_Type = RowStatus
_CfgFilterICMPGroupRowStatus_Object = MibTableColumn
cfgFilterICMPGroupRowStatus = _CfgFilterICMPGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 5),
    _CfgFilterICMPGroupRowStatus_Type()
)
cfgFilterICMPGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterICMPGroupRowStatus.setStatus("current")
_CfgFilterNestedGroupTable_Object = MibTable
cfgFilterNestedGroupTable = _CfgFilterNestedGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cfgFilterNestedGroupTable.setStatus("current")
_CfgFilterNestedGroupEntry_Object = MibTableRow
cfgFilterNestedGroupEntry = _CfgFilterNestedGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1)
)
cfgFilterNestedGroupEntry.setIndexNames(
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterParentGroupName"),
    (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterNestedGroupName"),
)
if mibBuilder.loadTexts:
    cfgFilterNestedGroupEntry.setStatus("current")
_CfgFilterParentGroupName_Type = CfgFilterGroupName
_CfgFilterParentGroupName_Object = MibTableColumn
cfgFilterParentGroupName = _CfgFilterParentGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1, 1),
    _CfgFilterParentGroupName_Type()
)
cfgFilterParentGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFilterParentGroupName.setStatus("current")
_CfgFilterNestedGroupName_Type = CfgFilterGroupName
_CfgFilterNestedGroupName_Object = MibTableColumn
cfgFilterNestedGroupName = _CfgFilterNestedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1, 2),
    _CfgFilterNestedGroupName_Type()
)
cfgFilterNestedGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFilterNestedGroupName.setStatus("current")


class _CfgFilterNestedStorageType_Type(StorageType):
    """Custom type cfgFilterNestedStorageType based on StorageType"""


_CfgFilterNestedStorageType_Object = MibTableColumn
cfgFilterNestedStorageType = _CfgFilterNestedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1, 3),
    _CfgFilterNestedStorageType_Type()
)
cfgFilterNestedStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterNestedStorageType.setStatus("current")
_CfgFilterNestedGroupRowStatus_Type = RowStatus
_CfgFilterNestedGroupRowStatus_Object = MibTableColumn
cfgFilterNestedGroupRowStatus = _CfgFilterNestedGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1, 4),
    _CfgFilterNestedGroupRowStatus_Type()
)
cfgFilterNestedGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgFilterNestedGroupRowStatus.setStatus("current")
_CiscoFilterGroupMIBConform_ObjectIdentity = ObjectIdentity
ciscoFilterGroupMIBConform = _CiscoFilterGroupMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 2)
)
_CiscoFilterGroupMIBCompl_ObjectIdentity = ObjectIdentity
ciscoFilterGroupMIBCompl = _CiscoFilterGroupMIBCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 2, 1)
)
_CiscoFilterGroupMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFilterGroupMIBGroups = _CiscoFilterGroupMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 2, 2)
)

# Managed Objects groups

ciscoFilterObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 2)
)
ciscoFilterObjectGroup.setObjects(
      *(("CISCO-FILTER-GROUP-MIB", "cfgFilterGroupType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterGroupDescription"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterGroupStorageType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoFilterObjectGroup.setStatus("current")

ciscoFilterNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 3)
)
ciscoFilterNetworkGroup.setObjects(
      *(("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkAddressType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkAddress"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkMask"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkStorageType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoFilterNetworkGroup.setStatus("current")

ciscoFilterIpProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 4)
)
ciscoFilterIpProtocolGroup.setObjects(
      *(("CISCO-FILTER-GROUP-MIB", "cfgFilterIpProtocolNumber"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpProtocolStorageType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpProtocolGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoFilterIpProtocolGroup.setStatus("current")

ciscoFilterIpServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 5)
)
ciscoFilterIpServiceGroup.setObjects(
      *(("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServiceType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServicePortLow"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServicePortHigh"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServiceStorageType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServiceGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoFilterIpServiceGroup.setStatus("current")

ciscoFilterICMPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 6)
)
ciscoFilterICMPGroup.setObjects(
      *(("CISCO-FILTER-GROUP-MIB", "cfgFilterICMPType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterICMPCode"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterICMPStorageType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterICMPGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoFilterICMPGroup.setStatus("current")

ciscoFilterNestedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 7)
)
ciscoFilterNestedGroup.setObjects(
      *(("CISCO-FILTER-GROUP-MIB", "cfgFilterNestedStorageType"),
        ("CISCO-FILTER-GROUP-MIB", "cfgFilterNestedGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoFilterNestedGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoFilterGroupConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 474, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFilterGroupConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FILTER-GROUP-MIB",
    **{"CfgFilterGroupName": CfgFilterGroupName,
       "ciscoFilterGroupMIB": ciscoFilterGroupMIB,
       "ciscoFilterGroupMIBNotifs": ciscoFilterGroupMIBNotifs,
       "ciscoFilterGroupMIBObjects": ciscoFilterGroupMIBObjects,
       "cfgFilterConfig": cfgFilterConfig,
       "cfgFilterGroupTable": cfgFilterGroupTable,
       "cfgFilterGroupEntry": cfgFilterGroupEntry,
       "cfgFilterGroupName": cfgFilterGroupName,
       "cfgFilterGroupType": cfgFilterGroupType,
       "cfgFilterGroupDescription": cfgFilterGroupDescription,
       "cfgFilterGroupStorageType": cfgFilterGroupStorageType,
       "cfgFilterGroupRowStatus": cfgFilterGroupRowStatus,
       "cfgFilterNetworkGroupTable": cfgFilterNetworkGroupTable,
       "cfgFilterNetworkGroupEntry": cfgFilterNetworkGroupEntry,
       "cfgFilterNetworkGroupIndex": cfgFilterNetworkGroupIndex,
       "cfgFilterNetworkAddressType": cfgFilterNetworkAddressType,
       "cfgFilterNetworkAddress": cfgFilterNetworkAddress,
       "cfgFilterNetworkMask": cfgFilterNetworkMask,
       "cfgFilterNetworkStorageType": cfgFilterNetworkStorageType,
       "cfgFilterNetworkRowStatus": cfgFilterNetworkRowStatus,
       "cfgFilterIpProtocolGroupTable": cfgFilterIpProtocolGroupTable,
       "cfgFilterIpProtocolGroupEntry": cfgFilterIpProtocolGroupEntry,
       "cfgFilterIpProtocolGroupIndex": cfgFilterIpProtocolGroupIndex,
       "cfgFilterIpProtocolNumber": cfgFilterIpProtocolNumber,
       "cfgFilterIpProtocolStorageType": cfgFilterIpProtocolStorageType,
       "cfgFilterIpProtocolGroupRowStatus": cfgFilterIpProtocolGroupRowStatus,
       "cfgFilterIpServiceGroupTable": cfgFilterIpServiceGroupTable,
       "cfgFilterIpServiceGroupEntry": cfgFilterIpServiceGroupEntry,
       "cfgFilterIpServiceGroupIndex": cfgFilterIpServiceGroupIndex,
       "cfgFilterIpServiceType": cfgFilterIpServiceType,
       "cfgFilterIpServicePortLow": cfgFilterIpServicePortLow,
       "cfgFilterIpServicePortHigh": cfgFilterIpServicePortHigh,
       "cfgFilterIpServiceStorageType": cfgFilterIpServiceStorageType,
       "cfgFilterIpServiceGroupRowStatus": cfgFilterIpServiceGroupRowStatus,
       "cfgFilterICMPGroupTable": cfgFilterICMPGroupTable,
       "cfgFilterICMPGroupEntry": cfgFilterICMPGroupEntry,
       "cfgFilterICMPGroupIndex": cfgFilterICMPGroupIndex,
       "cfgFilterICMPType": cfgFilterICMPType,
       "cfgFilterICMPCode": cfgFilterICMPCode,
       "cfgFilterICMPStorageType": cfgFilterICMPStorageType,
       "cfgFilterICMPGroupRowStatus": cfgFilterICMPGroupRowStatus,
       "cfgFilterNestedGroupTable": cfgFilterNestedGroupTable,
       "cfgFilterNestedGroupEntry": cfgFilterNestedGroupEntry,
       "cfgFilterParentGroupName": cfgFilterParentGroupName,
       "cfgFilterNestedGroupName": cfgFilterNestedGroupName,
       "cfgFilterNestedStorageType": cfgFilterNestedStorageType,
       "cfgFilterNestedGroupRowStatus": cfgFilterNestedGroupRowStatus,
       "ciscoFilterObjectGroup": ciscoFilterObjectGroup,
       "ciscoFilterNetworkGroup": ciscoFilterNetworkGroup,
       "ciscoFilterIpProtocolGroup": ciscoFilterIpProtocolGroup,
       "ciscoFilterIpServiceGroup": ciscoFilterIpServiceGroup,
       "ciscoFilterICMPGroup": ciscoFilterICMPGroup,
       "ciscoFilterNestedGroup": ciscoFilterNestedGroup,
       "ciscoFilterGroupMIBConform": ciscoFilterGroupMIBConform,
       "ciscoFilterGroupMIBCompl": ciscoFilterGroupMIBCompl,
       "ciscoFilterGroupConfigMIBCompliance": ciscoFilterGroupConfigMIBCompliance,
       "ciscoFilterGroupMIBGroups": ciscoFilterGroupMIBGroups}
)
