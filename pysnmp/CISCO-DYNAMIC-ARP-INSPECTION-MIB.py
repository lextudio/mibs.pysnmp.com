# SNMP MIB module (CISCO-DYNAMIC-ARP-INSPECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DYNAMIC-ARP-INSPECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:14 2024
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

(VlanIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-PRIVATE-VLAN-MIB",
    "VlanIndexOrZero")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDynamicArpInspectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374)
)
ciscoDynamicArpInspectionMIB.setRevisions(
        ("2011-03-21 00:00",
         "2003-10-29 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CdaiMIBNotifs_ObjectIdentity = ObjectIdentity
cdaiMIBNotifs = _CdaiMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 0)
)
_CdaiMIBObjects_ObjectIdentity = ObjectIdentity
cdaiMIBObjects = _CdaiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1)
)
_CdaiGlobal_ObjectIdentity = ObjectIdentity
cdaiGlobal = _CdaiGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1)
)
_CdaiLoggingEnable_Type = TruthValue
_CdaiLoggingEnable_Object = MibScalar
cdaiLoggingEnable = _CdaiLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 1),
    _CdaiLoggingEnable_Type()
)
cdaiLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdaiLoggingEnable.setStatus("current")


class _CdaiAddressValidate_Type(Bits):
    """Custom type cdaiAddressValidate based on Bits"""
    namedValues = NamedValues(
        *(("dstMacAddress", 1),
          ("ip", 2),
          ("ipAllowZeros", 3),
          ("srcMacAddress", 0))
    )

_CdaiAddressValidate_Type.__name__ = "Bits"
_CdaiAddressValidate_Object = MibScalar
cdaiAddressValidate = _CdaiAddressValidate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 2),
    _CdaiAddressValidate_Type()
)
cdaiAddressValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdaiAddressValidate.setStatus("current")
_CdaiLogBufferSize_Type = Unsigned32
_CdaiLogBufferSize_Object = MibScalar
cdaiLogBufferSize = _CdaiLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 3),
    _CdaiLogBufferSize_Type()
)
cdaiLogBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdaiLogBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    cdaiLogBufferSize.setUnits("entries")
_CdaiLoggingRate_Type = Unsigned32
_CdaiLoggingRate_Object = MibScalar
cdaiLoggingRate = _CdaiLoggingRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 4),
    _CdaiLoggingRate_Type()
)
cdaiLoggingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdaiLoggingRate.setStatus("current")
if mibBuilder.loadTexts:
    cdaiLoggingRate.setUnits("entries")
_CdaiLoggingInterval_Type = Unsigned32
_CdaiLoggingInterval_Object = MibScalar
cdaiLoggingInterval = _CdaiLoggingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 5),
    _CdaiLoggingInterval_Type()
)
cdaiLoggingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdaiLoggingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdaiLoggingInterval.setUnits("seconds")


class _CdaiLogBufferAction_Type(Integer32):
    """Custom type cdaiLogBufferAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("none", 1))
    )


_CdaiLogBufferAction_Type.__name__ = "Integer32"
_CdaiLogBufferAction_Object = MibScalar
cdaiLogBufferAction = _CdaiLogBufferAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 6),
    _CdaiLogBufferAction_Type()
)
cdaiLogBufferAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdaiLogBufferAction.setStatus("current")
_CdaiLogBufferTable_Object = MibTable
cdaiLogBufferTable = _CdaiLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cdaiLogBufferTable.setStatus("current")
_CdaiLogBufferEntry_Object = MibTableRow
cdaiLogBufferEntry = _CdaiLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1)
)
cdaiLogBufferEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferIndex"),
)
if mibBuilder.loadTexts:
    cdaiLogBufferEntry.setStatus("current")


class _CdaiLogBufferIndex_Type(Unsigned32):
    """Custom type cdaiLogBufferIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdaiLogBufferIndex_Type.__name__ = "Unsigned32"
_CdaiLogBufferIndex_Object = MibTableColumn
cdaiLogBufferIndex = _CdaiLogBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1, 1),
    _CdaiLogBufferIndex_Type()
)
cdaiLogBufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdaiLogBufferIndex.setStatus("current")
_CdaiLogBufferInterface_Type = InterfaceIndexOrZero
_CdaiLogBufferInterface_Object = MibTableColumn
cdaiLogBufferInterface = _CdaiLogBufferInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1, 2),
    _CdaiLogBufferInterface_Type()
)
cdaiLogBufferInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiLogBufferInterface.setStatus("current")
_CdaiLogBufferVlan_Type = VlanIndexOrZero
_CdaiLogBufferVlan_Object = MibTableColumn
cdaiLogBufferVlan = _CdaiLogBufferVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1, 3),
    _CdaiLogBufferVlan_Type()
)
cdaiLogBufferVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiLogBufferVlan.setStatus("current")
_CdaiLogBufferSenderMacAddress_Type = MacAddress
_CdaiLogBufferSenderMacAddress_Object = MibTableColumn
cdaiLogBufferSenderMacAddress = _CdaiLogBufferSenderMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1, 4),
    _CdaiLogBufferSenderMacAddress_Type()
)
cdaiLogBufferSenderMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiLogBufferSenderMacAddress.setStatus("current")
_CdaiLogBufferSenderAddressType_Type = InetAddressType
_CdaiLogBufferSenderAddressType_Object = MibTableColumn
cdaiLogBufferSenderAddressType = _CdaiLogBufferSenderAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1, 5),
    _CdaiLogBufferSenderAddressType_Type()
)
cdaiLogBufferSenderAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiLogBufferSenderAddressType.setStatus("current")
_CdaiLogBufferSenderIpAddress_Type = InetAddress
_CdaiLogBufferSenderIpAddress_Object = MibTableColumn
cdaiLogBufferSenderIpAddress = _CdaiLogBufferSenderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1, 6),
    _CdaiLogBufferSenderIpAddress_Type()
)
cdaiLogBufferSenderIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiLogBufferSenderIpAddress.setStatus("current")


class _CdaiLogBufferReason_Type(Integer32):
    """Custom type cdaiLogBufferReason based on Integer32"""
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
        *(("aclDeny", 3),
          ("aclPermit", 4),
          ("deny", 2),
          ("dhcpDeny", 5),
          ("dhcpPermit", 6),
          ("probePermit", 7),
          ("unknown", 1))
    )


_CdaiLogBufferReason_Type.__name__ = "Integer32"
_CdaiLogBufferReason_Object = MibTableColumn
cdaiLogBufferReason = _CdaiLogBufferReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1, 7),
    _CdaiLogBufferReason_Type()
)
cdaiLogBufferReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiLogBufferReason.setStatus("current")
_CdaiLogBufferLastUpdate_Type = DateAndTime
_CdaiLogBufferLastUpdate_Object = MibTableColumn
cdaiLogBufferLastUpdate = _CdaiLogBufferLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1, 8),
    _CdaiLogBufferLastUpdate_Type()
)
cdaiLogBufferLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiLogBufferLastUpdate.setStatus("current")
_CdaiLogBufferPacketsCount_Type = Gauge32
_CdaiLogBufferPacketsCount_Object = MibTableColumn
cdaiLogBufferPacketsCount = _CdaiLogBufferPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 1, 7, 1, 9),
    _CdaiLogBufferPacketsCount_Type()
)
cdaiLogBufferPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiLogBufferPacketsCount.setStatus("current")
_CdaiVlan_ObjectIdentity = ObjectIdentity
cdaiVlan = _CdaiVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2)
)
_CdaiVlanConfigTable_Object = MibTable
cdaiVlanConfigTable = _CdaiVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdaiVlanConfigTable.setStatus("current")
_CdaiVlanConfigEntry_Object = MibTableRow
cdaiVlanConfigEntry = _CdaiVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 1, 1)
)
cdaiVlanConfigEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanIndex"),
)
if mibBuilder.loadTexts:
    cdaiVlanConfigEntry.setStatus("current")
_CdaiVlanIndex_Type = VlanIndex
_CdaiVlanIndex_Object = MibTableColumn
cdaiVlanIndex = _CdaiVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 1, 1, 1),
    _CdaiVlanIndex_Type()
)
cdaiVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdaiVlanIndex.setStatus("current")
_CdaiVlanDynArpInspEnable_Type = TruthValue
_CdaiVlanDynArpInspEnable_Object = MibTableColumn
cdaiVlanDynArpInspEnable = _CdaiVlanDynArpInspEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 1, 1, 2),
    _CdaiVlanDynArpInspEnable_Type()
)
cdaiVlanDynArpInspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdaiVlanDynArpInspEnable.setStatus("current")
_CdaiVlanCfgTable_Object = MibTable
cdaiVlanCfgTable = _CdaiVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cdaiVlanCfgTable.setStatus("current")
_CdaiVlanCfgEntry_Object = MibTableRow
cdaiVlanCfgEntry = _CdaiVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1)
)
cdaiVlanCfgEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanId"),
)
if mibBuilder.loadTexts:
    cdaiVlanCfgEntry.setStatus("current")
_CdaiVlanId_Type = VlanIndex
_CdaiVlanId_Object = MibTableColumn
cdaiVlanId = _CdaiVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 1),
    _CdaiVlanId_Type()
)
cdaiVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdaiVlanId.setStatus("current")


class _CdaiVlanDynArpInspAdmin_Type(Integer32):
    """Custom type cdaiVlanDynArpInspAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CdaiVlanDynArpInspAdmin_Type.__name__ = "Integer32"
_CdaiVlanDynArpInspAdmin_Object = MibTableColumn
cdaiVlanDynArpInspAdmin = _CdaiVlanDynArpInspAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 2),
    _CdaiVlanDynArpInspAdmin_Type()
)
cdaiVlanDynArpInspAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdaiVlanDynArpInspAdmin.setStatus("current")


class _CdaiVlanDynArpInspOper_Type(Integer32):
    """Custom type cdaiVlanDynArpInspOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CdaiVlanDynArpInspOper_Type.__name__ = "Integer32"
_CdaiVlanDynArpInspOper_Object = MibTableColumn
cdaiVlanDynArpInspOper = _CdaiVlanDynArpInspOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 3),
    _CdaiVlanDynArpInspOper_Type()
)
cdaiVlanDynArpInspOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanDynArpInspOper.setStatus("current")
_CdaiVlanFilterArpAclName_Type = SnmpAdminString
_CdaiVlanFilterArpAclName_Object = MibTableColumn
cdaiVlanFilterArpAclName = _CdaiVlanFilterArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 4),
    _CdaiVlanFilterArpAclName_Type()
)
cdaiVlanFilterArpAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdaiVlanFilterArpAclName.setStatus("current")


class _CdaiVlanFilterArpAclStatic_Type(TruthValue):
    """Custom type cdaiVlanFilterArpAclStatic based on TruthValue"""


_CdaiVlanFilterArpAclStatic_Object = MibTableColumn
cdaiVlanFilterArpAclStatic = _CdaiVlanFilterArpAclStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 5),
    _CdaiVlanFilterArpAclStatic_Type()
)
cdaiVlanFilterArpAclStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdaiVlanFilterArpAclStatic.setStatus("current")


class _CdaiVlanAclLogging_Type(Integer32):
    """Custom type cdaiVlanAclLogging based on Integer32"""
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
        *(("aclMatch", 2),
          ("deny", 3),
          ("none", 1))
    )


_CdaiVlanAclLogging_Type.__name__ = "Integer32"
_CdaiVlanAclLogging_Object = MibTableColumn
cdaiVlanAclLogging = _CdaiVlanAclLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 6),
    _CdaiVlanAclLogging_Type()
)
cdaiVlanAclLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdaiVlanAclLogging.setStatus("current")


class _CdaiVlanDhcpBindingLogging_Type(Integer32):
    """Custom type cdaiVlanDhcpBindingLogging based on Integer32"""
    defaultValue = 3

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
        *(("all", 4),
          ("deny", 3),
          ("none", 1),
          ("permit", 2))
    )


_CdaiVlanDhcpBindingLogging_Type.__name__ = "Integer32"
_CdaiVlanDhcpBindingLogging_Object = MibTableColumn
cdaiVlanDhcpBindingLogging = _CdaiVlanDhcpBindingLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 7),
    _CdaiVlanDhcpBindingLogging_Type()
)
cdaiVlanDhcpBindingLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdaiVlanDhcpBindingLogging.setStatus("current")


class _CdaiVlanArpProbeLogging_Type(TruthValue):
    """Custom type cdaiVlanArpProbeLogging based on TruthValue"""


_CdaiVlanArpProbeLogging_Object = MibTableColumn
cdaiVlanArpProbeLogging = _CdaiVlanArpProbeLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 8),
    _CdaiVlanArpProbeLogging_Type()
)
cdaiVlanArpProbeLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdaiVlanArpProbeLogging.setStatus("current")


class _CdaiVlanCfgStorageType_Type(StorageType):
    """Custom type cdaiVlanCfgStorageType based on StorageType"""


_CdaiVlanCfgStorageType_Object = MibTableColumn
cdaiVlanCfgStorageType = _CdaiVlanCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 9),
    _CdaiVlanCfgStorageType_Type()
)
cdaiVlanCfgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdaiVlanCfgStorageType.setStatus("current")
_CdaiVlanCfgRowStatus_Type = RowStatus
_CdaiVlanCfgRowStatus_Object = MibTableColumn
cdaiVlanCfgRowStatus = _CdaiVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 2, 2, 1, 10),
    _CdaiVlanCfgRowStatus_Type()
)
cdaiVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdaiVlanCfgRowStatus.setStatus("current")
_CdaiInterface_ObjectIdentity = ObjectIdentity
cdaiInterface = _CdaiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 3)
)
_CdaiIfConfigTable_Object = MibTable
cdaiIfConfigTable = _CdaiIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdaiIfConfigTable.setStatus("current")
_CdaiIfConfigEntry_Object = MibTableRow
cdaiIfConfigEntry = _CdaiIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 3, 1, 1)
)
cdaiIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdaiIfConfigEntry.setStatus("current")
_CdaiIfTrustEnable_Type = TruthValue
_CdaiIfTrustEnable_Object = MibTableColumn
cdaiIfTrustEnable = _CdaiIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 3, 1, 1, 1),
    _CdaiIfTrustEnable_Type()
)
cdaiIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdaiIfTrustEnable.setStatus("current")
_CdaiIfRateLimitTable_Object = MibTable
cdaiIfRateLimitTable = _CdaiIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdaiIfRateLimitTable.setStatus("current")
_CdaiIfRateLimitEntry_Object = MibTableRow
cdaiIfRateLimitEntry = _CdaiIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 3, 2, 1)
)
cdaiIfRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdaiIfRateLimitEntry.setStatus("current")
_CdaiIfRateLimit_Type = Unsigned32
_CdaiIfRateLimit_Object = MibTableColumn
cdaiIfRateLimit = _CdaiIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 3, 2, 1, 1),
    _CdaiIfRateLimit_Type()
)
cdaiIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdaiIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cdaiIfRateLimit.setUnits("packet per second")
_CdaiStatistics_ObjectIdentity = ObjectIdentity
cdaiStatistics = _CdaiStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4)
)
_CdaiVlanStatsTable_Object = MibTable
cdaiVlanStatsTable = _CdaiVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdaiVlanStatsTable.setStatus("current")
_CdaiVlanStatsEntry_Object = MibTableRow
cdaiVlanStatsEntry = _CdaiVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1)
)
cdaiVlanStatsEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanStatsIndex"),
)
if mibBuilder.loadTexts:
    cdaiVlanStatsEntry.setStatus("current")
_CdaiVlanStatsIndex_Type = VlanIndex
_CdaiVlanStatsIndex_Object = MibTableColumn
cdaiVlanStatsIndex = _CdaiVlanStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 1),
    _CdaiVlanStatsIndex_Type()
)
cdaiVlanStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdaiVlanStatsIndex.setStatus("current")
_CdaiVlanForwarded_Type = Counter32
_CdaiVlanForwarded_Object = MibTableColumn
cdaiVlanForwarded = _CdaiVlanForwarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 2),
    _CdaiVlanForwarded_Type()
)
cdaiVlanForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanForwarded.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanForwarded.setUnits("packets")
_CdaiVlanDropped_Type = Counter32
_CdaiVlanDropped_Object = MibTableColumn
cdaiVlanDropped = _CdaiVlanDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 3),
    _CdaiVlanDropped_Type()
)
cdaiVlanDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanDropped.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanDropped.setUnits("packets")
_CdaiVlanAclPermitted_Type = Counter32
_CdaiVlanAclPermitted_Object = MibTableColumn
cdaiVlanAclPermitted = _CdaiVlanAclPermitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 4),
    _CdaiVlanAclPermitted_Type()
)
cdaiVlanAclPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanAclPermitted.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanAclPermitted.setUnits("packets")
_CdaiVlanDhcpBindingsPermitted_Type = Counter32
_CdaiVlanDhcpBindingsPermitted_Object = MibTableColumn
cdaiVlanDhcpBindingsPermitted = _CdaiVlanDhcpBindingsPermitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 5),
    _CdaiVlanDhcpBindingsPermitted_Type()
)
cdaiVlanDhcpBindingsPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanDhcpBindingsPermitted.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanDhcpBindingsPermitted.setUnits("packets")
_CdaiVlanAclDenied_Type = Counter32
_CdaiVlanAclDenied_Object = MibTableColumn
cdaiVlanAclDenied = _CdaiVlanAclDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 6),
    _CdaiVlanAclDenied_Type()
)
cdaiVlanAclDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanAclDenied.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanAclDenied.setUnits("packets")
_CdaiVlanDhcpBindingDenied_Type = Counter32
_CdaiVlanDhcpBindingDenied_Object = MibTableColumn
cdaiVlanDhcpBindingDenied = _CdaiVlanDhcpBindingDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 7),
    _CdaiVlanDhcpBindingDenied_Type()
)
cdaiVlanDhcpBindingDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanDhcpBindingDenied.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanDhcpBindingDenied.setUnits("packets")
_CdaiVlanSrcMacValidationFailures_Type = Counter32
_CdaiVlanSrcMacValidationFailures_Object = MibTableColumn
cdaiVlanSrcMacValidationFailures = _CdaiVlanSrcMacValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 8),
    _CdaiVlanSrcMacValidationFailures_Type()
)
cdaiVlanSrcMacValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanSrcMacValidationFailures.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanSrcMacValidationFailures.setUnits("packets")
_CdaiVlanDestMacValidationFailures_Type = Counter32
_CdaiVlanDestMacValidationFailures_Object = MibTableColumn
cdaiVlanDestMacValidationFailures = _CdaiVlanDestMacValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 9),
    _CdaiVlanDestMacValidationFailures_Type()
)
cdaiVlanDestMacValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanDestMacValidationFailures.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanDestMacValidationFailures.setUnits("packets")
_CdaiVlanIpValidationFailures_Type = Counter32
_CdaiVlanIpValidationFailures_Object = MibTableColumn
cdaiVlanIpValidationFailures = _CdaiVlanIpValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 10),
    _CdaiVlanIpValidationFailures_Type()
)
cdaiVlanIpValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanIpValidationFailures.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanIpValidationFailures.setUnits("packets")
_CdaiVlanArpProbePermitted_Type = Counter32
_CdaiVlanArpProbePermitted_Object = MibTableColumn
cdaiVlanArpProbePermitted = _CdaiVlanArpProbePermitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 11),
    _CdaiVlanArpProbePermitted_Type()
)
cdaiVlanArpProbePermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanArpProbePermitted.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanArpProbePermitted.setUnits("packets")
_CdaiVlanInvalidProtocolData_Type = Counter32
_CdaiVlanInvalidProtocolData_Object = MibTableColumn
cdaiVlanInvalidProtocolData = _CdaiVlanInvalidProtocolData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 1, 4, 1, 1, 12),
    _CdaiVlanInvalidProtocolData_Type()
)
cdaiVlanInvalidProtocolData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdaiVlanInvalidProtocolData.setStatus("current")
if mibBuilder.loadTexts:
    cdaiVlanInvalidProtocolData.setUnits("packets")
_CdaiMIBConformance_ObjectIdentity = ObjectIdentity
cdaiMIBConformance = _CdaiMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2)
)
_CdaiMIBCompliances_ObjectIdentity = ObjectIdentity
cdaiMIBCompliances = _CdaiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 1)
)
_CdaiMIBGroups_ObjectIdentity = ObjectIdentity
cdaiMIBGroups = _CdaiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2)
)

# Managed Objects groups

cdaiGlobalLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 1)
)
cdaiGlobalLoggingGroup.setObjects(
    ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLoggingEnable")
)
if mibBuilder.loadTexts:
    cdaiGlobalLoggingGroup.setStatus("current")

cdaiVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 2)
)
cdaiVlanConfigGroup.setObjects(
    ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanDynArpInspEnable")
)
if mibBuilder.loadTexts:
    cdaiVlanConfigGroup.setStatus("current")

cdaiIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 3)
)
cdaiIfConfigGroup.setObjects(
    ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiIfTrustEnable")
)
if mibBuilder.loadTexts:
    cdaiIfConfigGroup.setStatus("current")

cdaiIfRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 4)
)
cdaiIfRateLimitGroup.setObjects(
    ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiIfRateLimit")
)
if mibBuilder.loadTexts:
    cdaiIfRateLimitGroup.setStatus("current")

cdaiLoggingConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 5)
)
cdaiLoggingConfigGroup.setObjects(
      *(("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferSize"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLoggingRate"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLoggingInterval"))
)
if mibBuilder.loadTexts:
    cdaiLoggingConfigGroup.setStatus("current")

cdaiAddressValidationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 6)
)
cdaiAddressValidationGroup.setObjects(
    ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiAddressValidate")
)
if mibBuilder.loadTexts:
    cdaiAddressValidationGroup.setStatus("current")

cdaiVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 7)
)
cdaiVlanCfgGroup.setObjects(
      *(("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanDynArpInspAdmin"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanDynArpInspOper"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanFilterArpAclName"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanFilterArpAclStatic"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanAclLogging"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanDhcpBindingLogging"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanCfgStorageType"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanCfgRowStatus"))
)
if mibBuilder.loadTexts:
    cdaiVlanCfgGroup.setStatus("current")

cdaiVlanStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 8)
)
cdaiVlanStatisticsGroup.setObjects(
      *(("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanForwarded"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanDropped"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanAclPermitted"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanDhcpBindingsPermitted"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanAclDenied"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanDhcpBindingDenied"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanSrcMacValidationFailures"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanDestMacValidationFailures"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanIpValidationFailures"))
)
if mibBuilder.loadTexts:
    cdaiVlanStatisticsGroup.setStatus("current")

cdaiLogBufferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 9)
)
cdaiLogBufferGroup.setObjects(
      *(("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferInterface"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferVlan"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferSenderMacAddress"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferSenderAddressType"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferSenderIpAddress"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferReason"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferLastUpdate"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferPacketsCount"))
)
if mibBuilder.loadTexts:
    cdaiLogBufferGroup.setStatus("current")

cdaiVlanExtStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 10)
)
cdaiVlanExtStatisticsGroup.setObjects(
      *(("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanArpProbePermitted"),
        ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanInvalidProtocolData"))
)
if mibBuilder.loadTexts:
    cdaiVlanExtStatisticsGroup.setStatus("current")

cdaiVlanArpProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 11)
)
cdaiVlanArpProbeGroup.setObjects(
    ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiVlanArpProbeLogging")
)
if mibBuilder.loadTexts:
    cdaiVlanArpProbeGroup.setStatus("current")

cdaiLogBufferActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 2, 12)
)
cdaiLogBufferActionGroup.setObjects(
    ("CISCO-DYNAMIC-ARP-INSPECTION-MIB", "cdaiLogBufferAction")
)
if mibBuilder.loadTexts:
    cdaiLogBufferActionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cdaiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cdaiMIBCompliance.setStatus(
        "deprecated"
    )

cdaiMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 374, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cdaiMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DYNAMIC-ARP-INSPECTION-MIB",
    **{"ciscoDynamicArpInspectionMIB": ciscoDynamicArpInspectionMIB,
       "cdaiMIBNotifs": cdaiMIBNotifs,
       "cdaiMIBObjects": cdaiMIBObjects,
       "cdaiGlobal": cdaiGlobal,
       "cdaiLoggingEnable": cdaiLoggingEnable,
       "cdaiAddressValidate": cdaiAddressValidate,
       "cdaiLogBufferSize": cdaiLogBufferSize,
       "cdaiLoggingRate": cdaiLoggingRate,
       "cdaiLoggingInterval": cdaiLoggingInterval,
       "cdaiLogBufferAction": cdaiLogBufferAction,
       "cdaiLogBufferTable": cdaiLogBufferTable,
       "cdaiLogBufferEntry": cdaiLogBufferEntry,
       "cdaiLogBufferIndex": cdaiLogBufferIndex,
       "cdaiLogBufferInterface": cdaiLogBufferInterface,
       "cdaiLogBufferVlan": cdaiLogBufferVlan,
       "cdaiLogBufferSenderMacAddress": cdaiLogBufferSenderMacAddress,
       "cdaiLogBufferSenderAddressType": cdaiLogBufferSenderAddressType,
       "cdaiLogBufferSenderIpAddress": cdaiLogBufferSenderIpAddress,
       "cdaiLogBufferReason": cdaiLogBufferReason,
       "cdaiLogBufferLastUpdate": cdaiLogBufferLastUpdate,
       "cdaiLogBufferPacketsCount": cdaiLogBufferPacketsCount,
       "cdaiVlan": cdaiVlan,
       "cdaiVlanConfigTable": cdaiVlanConfigTable,
       "cdaiVlanConfigEntry": cdaiVlanConfigEntry,
       "cdaiVlanIndex": cdaiVlanIndex,
       "cdaiVlanDynArpInspEnable": cdaiVlanDynArpInspEnable,
       "cdaiVlanCfgTable": cdaiVlanCfgTable,
       "cdaiVlanCfgEntry": cdaiVlanCfgEntry,
       "cdaiVlanId": cdaiVlanId,
       "cdaiVlanDynArpInspAdmin": cdaiVlanDynArpInspAdmin,
       "cdaiVlanDynArpInspOper": cdaiVlanDynArpInspOper,
       "cdaiVlanFilterArpAclName": cdaiVlanFilterArpAclName,
       "cdaiVlanFilterArpAclStatic": cdaiVlanFilterArpAclStatic,
       "cdaiVlanAclLogging": cdaiVlanAclLogging,
       "cdaiVlanDhcpBindingLogging": cdaiVlanDhcpBindingLogging,
       "cdaiVlanArpProbeLogging": cdaiVlanArpProbeLogging,
       "cdaiVlanCfgStorageType": cdaiVlanCfgStorageType,
       "cdaiVlanCfgRowStatus": cdaiVlanCfgRowStatus,
       "cdaiInterface": cdaiInterface,
       "cdaiIfConfigTable": cdaiIfConfigTable,
       "cdaiIfConfigEntry": cdaiIfConfigEntry,
       "cdaiIfTrustEnable": cdaiIfTrustEnable,
       "cdaiIfRateLimitTable": cdaiIfRateLimitTable,
       "cdaiIfRateLimitEntry": cdaiIfRateLimitEntry,
       "cdaiIfRateLimit": cdaiIfRateLimit,
       "cdaiStatistics": cdaiStatistics,
       "cdaiVlanStatsTable": cdaiVlanStatsTable,
       "cdaiVlanStatsEntry": cdaiVlanStatsEntry,
       "cdaiVlanStatsIndex": cdaiVlanStatsIndex,
       "cdaiVlanForwarded": cdaiVlanForwarded,
       "cdaiVlanDropped": cdaiVlanDropped,
       "cdaiVlanAclPermitted": cdaiVlanAclPermitted,
       "cdaiVlanDhcpBindingsPermitted": cdaiVlanDhcpBindingsPermitted,
       "cdaiVlanAclDenied": cdaiVlanAclDenied,
       "cdaiVlanDhcpBindingDenied": cdaiVlanDhcpBindingDenied,
       "cdaiVlanSrcMacValidationFailures": cdaiVlanSrcMacValidationFailures,
       "cdaiVlanDestMacValidationFailures": cdaiVlanDestMacValidationFailures,
       "cdaiVlanIpValidationFailures": cdaiVlanIpValidationFailures,
       "cdaiVlanArpProbePermitted": cdaiVlanArpProbePermitted,
       "cdaiVlanInvalidProtocolData": cdaiVlanInvalidProtocolData,
       "cdaiMIBConformance": cdaiMIBConformance,
       "cdaiMIBCompliances": cdaiMIBCompliances,
       "cdaiMIBCompliance": cdaiMIBCompliance,
       "cdaiMIBCompliance1": cdaiMIBCompliance1,
       "cdaiMIBGroups": cdaiMIBGroups,
       "cdaiGlobalLoggingGroup": cdaiGlobalLoggingGroup,
       "cdaiVlanConfigGroup": cdaiVlanConfigGroup,
       "cdaiIfConfigGroup": cdaiIfConfigGroup,
       "cdaiIfRateLimitGroup": cdaiIfRateLimitGroup,
       "cdaiLoggingConfigGroup": cdaiLoggingConfigGroup,
       "cdaiAddressValidationGroup": cdaiAddressValidationGroup,
       "cdaiVlanCfgGroup": cdaiVlanCfgGroup,
       "cdaiVlanStatisticsGroup": cdaiVlanStatisticsGroup,
       "cdaiLogBufferGroup": cdaiLogBufferGroup,
       "cdaiVlanExtStatisticsGroup": cdaiVlanExtStatisticsGroup,
       "cdaiVlanArpProbeGroup": cdaiVlanArpProbeGroup,
       "cdaiLogBufferActionGroup": cdaiLogBufferActionGroup}
)
