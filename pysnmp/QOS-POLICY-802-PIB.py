# SNMP MIB module (QOS-POLICY-802-PIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QOS-POLICY-802-PIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:39 2024
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

(PolicyInstanceId,) = mibBuilder.importSymbols(
    "POLICY-FRAMEWORK-PIB",
    "PolicyInstanceId")

(Dscp,) = mibBuilder.importSymbols(
    "QOS-POLICY-IP-PIB",
    "Dscp")

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
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(policy,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "policy")


# MODULE-IDENTITY

qosPolicy802Pib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QosIeee802Cos(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_QosPolicy802PibClasses_ObjectIdentity = ObjectIdentity
qosPolicy802PibClasses = _QosPolicy802PibClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1)
)
_Qos802DomainConfig_ObjectIdentity = ObjectIdentity
qos802DomainConfig = _Qos802DomainConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1)
)
_Qos802DscpMappingTable_Object = MibTable
qos802DscpMappingTable = _Qos802DscpMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qos802DscpMappingTable.setStatus("current")
_Qos802DscpMappingEntry_Object = MibTableRow
qos802DscpMappingEntry = _Qos802DscpMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1)
)
qos802DscpMappingEntry.setIndexNames(
    (0, "QOS-POLICY-802-PIB", "qos802DscpMappingId"),
)
if mibBuilder.loadTexts:
    qos802DscpMappingEntry.setStatus("current")
_Qos802DscpMappingId_Type = PolicyInstanceId
_Qos802DscpMappingId_Object = MibTableColumn
qos802DscpMappingId = _Qos802DscpMappingId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 1),
    _Qos802DscpMappingId_Type()
)
qos802DscpMappingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qos802DscpMappingId.setStatus("current")
_Qos802DscpMappingDscp_Type = Dscp
_Qos802DscpMappingDscp_Object = MibTableColumn
qos802DscpMappingDscp = _Qos802DscpMappingDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 2),
    _Qos802DscpMappingDscp_Type()
)
qos802DscpMappingDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802DscpMappingDscp.setStatus("current")
_Qos802DscpMapping802Cos_Type = QosIeee802Cos
_Qos802DscpMapping802Cos_Object = MibTableColumn
qos802DscpMapping802Cos = _Qos802DscpMapping802Cos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 3),
    _Qos802DscpMapping802Cos_Type()
)
qos802DscpMapping802Cos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802DscpMapping802Cos.setStatus("current")


class _Qos802DscpMappingStorageType_Type(StorageType):
    """Custom type qos802DscpMappingStorageType based on StorageType"""


_Qos802DscpMappingStorageType_Object = MibTableColumn
qos802DscpMappingStorageType = _Qos802DscpMappingStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 4),
    _Qos802DscpMappingStorageType_Type()
)
qos802DscpMappingStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802DscpMappingStorageType.setStatus("current")
_Qos802DscpMappingStatus_Type = RowStatus
_Qos802DscpMappingStatus_Object = MibTableColumn
qos802DscpMappingStatus = _Qos802DscpMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 1, 1, 5),
    _Qos802DscpMappingStatus_Type()
)
qos802DscpMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802DscpMappingStatus.setStatus("current")
_Qos802CosToDscpTable_Object = MibTable
qos802CosToDscpTable = _Qos802CosToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qos802CosToDscpTable.setStatus("current")
_Qos802CosToDscpEntry_Object = MibTableRow
qos802CosToDscpEntry = _Qos802CosToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1)
)
qos802CosToDscpEntry.setIndexNames(
    (0, "QOS-POLICY-802-PIB", "qos802CosToDscpId"),
)
if mibBuilder.loadTexts:
    qos802CosToDscpEntry.setStatus("current")
_Qos802CosToDscpId_Type = PolicyInstanceId
_Qos802CosToDscpId_Object = MibTableColumn
qos802CosToDscpId = _Qos802CosToDscpId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 1),
    _Qos802CosToDscpId_Type()
)
qos802CosToDscpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qos802CosToDscpId.setStatus("current")
_Qos802CosToDscpCos_Type = QosIeee802Cos
_Qos802CosToDscpCos_Object = MibTableColumn
qos802CosToDscpCos = _Qos802CosToDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 2),
    _Qos802CosToDscpCos_Type()
)
qos802CosToDscpCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802CosToDscpCos.setStatus("current")
_Qos802CosToDscpDscp_Type = Dscp
_Qos802CosToDscpDscp_Object = MibTableColumn
qos802CosToDscpDscp = _Qos802CosToDscpDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 3),
    _Qos802CosToDscpDscp_Type()
)
qos802CosToDscpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802CosToDscpDscp.setStatus("current")


class _Qos802CosToDscpStorageType_Type(StorageType):
    """Custom type qos802CosToDscpStorageType based on StorageType"""


_Qos802CosToDscpStorageType_Object = MibTableColumn
qos802CosToDscpStorageType = _Qos802CosToDscpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 4),
    _Qos802CosToDscpStorageType_Type()
)
qos802CosToDscpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802CosToDscpStorageType.setStatus("current")
_Qos802CosToDscpStatus_Type = RowStatus
_Qos802CosToDscpStatus_Object = MibTableColumn
qos802CosToDscpStatus = _Qos802CosToDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 1, 2, 1, 5),
    _Qos802CosToDscpStatus_Type()
)
qos802CosToDscpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802CosToDscpStatus.setStatus("current")
_Qos802Qos_ObjectIdentity = ObjectIdentity
qos802Qos = _Qos802Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2)
)
_Qos802AceTable_Object = MibTable
qos802AceTable = _Qos802AceTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qos802AceTable.setStatus("current")
_Qos802AceEntry_Object = MibTableRow
qos802AceEntry = _Qos802AceEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1)
)
qos802AceEntry.setIndexNames(
    (0, "QOS-POLICY-802-PIB", "qos802AceId"),
)
if mibBuilder.loadTexts:
    qos802AceEntry.setStatus("current")
_Qos802AceId_Type = PolicyInstanceId
_Qos802AceId_Object = MibTableColumn
qos802AceId = _Qos802AceId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 1),
    _Qos802AceId_Type()
)
qos802AceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qos802AceId.setStatus("current")
_Qos802AceDstAddr_Type = PhysAddress
_Qos802AceDstAddr_Object = MibTableColumn
qos802AceDstAddr = _Qos802AceDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 2),
    _Qos802AceDstAddr_Type()
)
qos802AceDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceDstAddr.setStatus("current")
_Qos802AceDstAddrMask_Type = PhysAddress
_Qos802AceDstAddrMask_Object = MibTableColumn
qos802AceDstAddrMask = _Qos802AceDstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 3),
    _Qos802AceDstAddrMask_Type()
)
qos802AceDstAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceDstAddrMask.setStatus("current")
_Qos802AceSrcAddr_Type = PhysAddress
_Qos802AceSrcAddr_Object = MibTableColumn
qos802AceSrcAddr = _Qos802AceSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 4),
    _Qos802AceSrcAddr_Type()
)
qos802AceSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceSrcAddr.setStatus("current")
_Qos802AceSrcAddrMask_Type = PhysAddress
_Qos802AceSrcAddrMask_Object = MibTableColumn
qos802AceSrcAddrMask = _Qos802AceSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 5),
    _Qos802AceSrcAddrMask_Type()
)
qos802AceSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceSrcAddrMask.setStatus("current")


class _Qos802AceVlanId_Type(Integer32):
    """Custom type qos802AceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4094),
    )


_Qos802AceVlanId_Type.__name__ = "Integer32"
_Qos802AceVlanId_Object = MibTableColumn
qos802AceVlanId = _Qos802AceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 6),
    _Qos802AceVlanId_Type()
)
qos802AceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceVlanId.setStatus("current")


class _Qos802AceVlanTagRequired_Type(Integer32):
    """Custom type qos802AceVlanTagRequired based on Integer32"""
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
        *(("ignoreTag", 4),
          ("priorityTagged", 2),
          ("taggedOnly", 1),
          ("untaggedOnly", 3))
    )


_Qos802AceVlanTagRequired_Type.__name__ = "Integer32"
_Qos802AceVlanTagRequired_Object = MibTableColumn
qos802AceVlanTagRequired = _Qos802AceVlanTagRequired_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 7),
    _Qos802AceVlanTagRequired_Type()
)
qos802AceVlanTagRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceVlanTagRequired.setStatus("current")


class _Qos802AceEtherType_Type(Integer32):
    """Custom type qos802AceEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_Qos802AceEtherType_Type.__name__ = "Integer32"
_Qos802AceEtherType_Object = MibTableColumn
qos802AceEtherType = _Qos802AceEtherType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 8),
    _Qos802AceEtherType_Type()
)
qos802AceEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceEtherType.setStatus("current")


class _Qos802AceUserPriority_Type(Bits):
    """Custom type qos802AceUserPriority based on Bits"""
    namedValues = NamedValues(
        *(("matchPriority0", 0),
          ("matchPriority1", 1),
          ("matchPriority2", 2),
          ("matchPriority3", 3),
          ("matchPriority4", 4),
          ("matchPriority5", 5),
          ("matchPriority6", 6),
          ("matchPriority7", 7))
    )

_Qos802AceUserPriority_Type.__name__ = "Bits"
_Qos802AceUserPriority_Object = MibTableColumn
qos802AceUserPriority = _Qos802AceUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 9),
    _Qos802AceUserPriority_Type()
)
qos802AceUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceUserPriority.setStatus("current")
_Qos802AcePermit_Type = TruthValue
_Qos802AcePermit_Object = MibTableColumn
qos802AcePermit = _Qos802AcePermit_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 10),
    _Qos802AcePermit_Type()
)
qos802AcePermit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AcePermit.setStatus("current")


class _Qos802AceStorageType_Type(StorageType):
    """Custom type qos802AceStorageType based on StorageType"""


_Qos802AceStorageType_Object = MibTableColumn
qos802AceStorageType = _Qos802AceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 11),
    _Qos802AceStorageType_Type()
)
qos802AceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceStorageType.setStatus("current")
_Qos802AceStatus_Type = RowStatus
_Qos802AceStatus_Object = MibTableColumn
qos802AceStatus = _Qos802AceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 1, 1, 12),
    _Qos802AceStatus_Type()
)
qos802AceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AceStatus.setStatus("current")
_Qos802AclDefinitionTable_Object = MibTable
qos802AclDefinitionTable = _Qos802AclDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qos802AclDefinitionTable.setStatus("current")
_Qos802AclDefinitionEntry_Object = MibTableRow
qos802AclDefinitionEntry = _Qos802AclDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1)
)
qos802AclDefinitionEntry.setIndexNames(
    (0, "QOS-POLICY-802-PIB", "qos802AclDefinitionId"),
)
if mibBuilder.loadTexts:
    qos802AclDefinitionEntry.setStatus("current")
_Qos802AclDefinitionId_Type = PolicyInstanceId
_Qos802AclDefinitionId_Object = MibTableColumn
qos802AclDefinitionId = _Qos802AclDefinitionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 1),
    _Qos802AclDefinitionId_Type()
)
qos802AclDefinitionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qos802AclDefinitionId.setStatus("current")
_Qos802AclDefinitionAclId_Type = PolicyInstanceId
_Qos802AclDefinitionAclId_Object = MibTableColumn
qos802AclDefinitionAclId = _Qos802AclDefinitionAclId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 2),
    _Qos802AclDefinitionAclId_Type()
)
qos802AclDefinitionAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AclDefinitionAclId.setStatus("current")
_Qos802AclDefinitionAceId_Type = PolicyInstanceId
_Qos802AclDefinitionAceId_Object = MibTableColumn
qos802AclDefinitionAceId = _Qos802AclDefinitionAceId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 3),
    _Qos802AclDefinitionAceId_Type()
)
qos802AclDefinitionAceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AclDefinitionAceId.setStatus("current")
_Qos802AclDefinitionAceOrder_Type = Unsigned32
_Qos802AclDefinitionAceOrder_Object = MibTableColumn
qos802AclDefinitionAceOrder = _Qos802AclDefinitionAceOrder_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 4),
    _Qos802AclDefinitionAceOrder_Type()
)
qos802AclDefinitionAceOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AclDefinitionAceOrder.setStatus("current")


class _Qos802AclDefinitionStorageType_Type(StorageType):
    """Custom type qos802AclDefinitionStorageType based on StorageType"""


_Qos802AclDefinitionStorageType_Object = MibTableColumn
qos802AclDefinitionStorageType = _Qos802AclDefinitionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 5),
    _Qos802AclDefinitionStorageType_Type()
)
qos802AclDefinitionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AclDefinitionStorageType.setStatus("current")
_Qos802AclDefinitionStatus_Type = RowStatus
_Qos802AclDefinitionStatus_Object = MibTableColumn
qos802AclDefinitionStatus = _Qos802AclDefinitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 6),
    _Qos802AclDefinitionStatus_Type()
)
qos802AclDefinitionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AclDefinitionStatus.setStatus("current")


class _Qos802AclDefinitionLabel_Type(SnmpAdminString):
    """Custom type qos802AclDefinitionLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Qos802AclDefinitionLabel_Type.__name__ = "SnmpAdminString"
_Qos802AclDefinitionLabel_Object = MibTableColumn
qos802AclDefinitionLabel = _Qos802AclDefinitionLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 1, 2, 2, 1, 7),
    _Qos802AclDefinitionLabel_Type()
)
qos802AclDefinitionLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qos802AclDefinitionLabel.setStatus("current")
_QosPolicy802PibConformance_ObjectIdentity = ObjectIdentity
qosPolicy802PibConformance = _QosPolicy802PibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 2)
)
_QosPolicy802PibCompliances_ObjectIdentity = ObjectIdentity
qosPolicy802PibCompliances = _QosPolicy802PibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 1)
)
_QosPolicy802PibGroups_ObjectIdentity = ObjectIdentity
qosPolicy802PibGroups = _QosPolicy802PibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2)
)

# Managed Objects groups

qos802DscpMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2, 1)
)
qos802DscpMappingGroup.setObjects(
      *(("QOS-POLICY-802-PIB", "qos802DscpMappingDscp"),
        ("QOS-POLICY-802-PIB", "qos802DscpMapping802Cos"),
        ("QOS-POLICY-802-PIB", "qos802DscpMappingStorageType"),
        ("QOS-POLICY-802-PIB", "qos802DscpMappingStatus"))
)
if mibBuilder.loadTexts:
    qos802DscpMappingGroup.setStatus("current")

qos802CosToDscpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2, 2)
)
qos802CosToDscpGroup.setObjects(
      *(("QOS-POLICY-802-PIB", "qos802CosToDscpCos"),
        ("QOS-POLICY-802-PIB", "qos802CosToDscpDscp"),
        ("QOS-POLICY-802-PIB", "qos802CosToDscpStorageType"),
        ("QOS-POLICY-802-PIB", "qos802CosToDscpStatus"))
)
if mibBuilder.loadTexts:
    qos802CosToDscpGroup.setStatus("current")

qos802AceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2, 3)
)
qos802AceGroup.setObjects(
      *(("QOS-POLICY-802-PIB", "qos802AceDstAddr"),
        ("QOS-POLICY-802-PIB", "qos802AceDstAddrMask"),
        ("QOS-POLICY-802-PIB", "qos802AceSrcAddr"),
        ("QOS-POLICY-802-PIB", "qos802AceSrcAddrMask"),
        ("QOS-POLICY-802-PIB", "qos802AceVlanId"),
        ("QOS-POLICY-802-PIB", "qos802AceVlanTagRequired"),
        ("QOS-POLICY-802-PIB", "qos802AceEtherType"),
        ("QOS-POLICY-802-PIB", "qos802AceUserPriority"),
        ("QOS-POLICY-802-PIB", "qos802AcePermit"),
        ("QOS-POLICY-802-PIB", "qos802AceStorageType"),
        ("QOS-POLICY-802-PIB", "qos802AceStatus"))
)
if mibBuilder.loadTexts:
    qos802AceGroup.setStatus("current")

qos802AclDefinitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 2, 4)
)
qos802AclDefinitionGroup.setObjects(
      *(("QOS-POLICY-802-PIB", "qos802AclDefinitionAclId"),
        ("QOS-POLICY-802-PIB", "qos802AclDefinitionAceId"),
        ("QOS-POLICY-802-PIB", "qos802AclDefinitionAceOrder"),
        ("QOS-POLICY-802-PIB", "qos802AclDefinitionStorageType"),
        ("QOS-POLICY-802-PIB", "qos802AclDefinitionStatus"),
        ("QOS-POLICY-802-PIB", "qos802AclDefinitionLabel"))
)
if mibBuilder.loadTexts:
    qos802AclDefinitionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qosPolicy802PibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 4, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qosPolicy802PibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QOS-POLICY-802-PIB",
    **{"QosIeee802Cos": QosIeee802Cos,
       "qosPolicy802Pib": qosPolicy802Pib,
       "qosPolicy802PibClasses": qosPolicy802PibClasses,
       "qos802DomainConfig": qos802DomainConfig,
       "qos802DscpMappingTable": qos802DscpMappingTable,
       "qos802DscpMappingEntry": qos802DscpMappingEntry,
       "qos802DscpMappingId": qos802DscpMappingId,
       "qos802DscpMappingDscp": qos802DscpMappingDscp,
       "qos802DscpMapping802Cos": qos802DscpMapping802Cos,
       "qos802DscpMappingStorageType": qos802DscpMappingStorageType,
       "qos802DscpMappingStatus": qos802DscpMappingStatus,
       "qos802CosToDscpTable": qos802CosToDscpTable,
       "qos802CosToDscpEntry": qos802CosToDscpEntry,
       "qos802CosToDscpId": qos802CosToDscpId,
       "qos802CosToDscpCos": qos802CosToDscpCos,
       "qos802CosToDscpDscp": qos802CosToDscpDscp,
       "qos802CosToDscpStorageType": qos802CosToDscpStorageType,
       "qos802CosToDscpStatus": qos802CosToDscpStatus,
       "qos802Qos": qos802Qos,
       "qos802AceTable": qos802AceTable,
       "qos802AceEntry": qos802AceEntry,
       "qos802AceId": qos802AceId,
       "qos802AceDstAddr": qos802AceDstAddr,
       "qos802AceDstAddrMask": qos802AceDstAddrMask,
       "qos802AceSrcAddr": qos802AceSrcAddr,
       "qos802AceSrcAddrMask": qos802AceSrcAddrMask,
       "qos802AceVlanId": qos802AceVlanId,
       "qos802AceVlanTagRequired": qos802AceVlanTagRequired,
       "qos802AceEtherType": qos802AceEtherType,
       "qos802AceUserPriority": qos802AceUserPriority,
       "qos802AcePermit": qos802AcePermit,
       "qos802AceStorageType": qos802AceStorageType,
       "qos802AceStatus": qos802AceStatus,
       "qos802AclDefinitionTable": qos802AclDefinitionTable,
       "qos802AclDefinitionEntry": qos802AclDefinitionEntry,
       "qos802AclDefinitionId": qos802AclDefinitionId,
       "qos802AclDefinitionAclId": qos802AclDefinitionAclId,
       "qos802AclDefinitionAceId": qos802AclDefinitionAceId,
       "qos802AclDefinitionAceOrder": qos802AclDefinitionAceOrder,
       "qos802AclDefinitionStorageType": qos802AclDefinitionStorageType,
       "qos802AclDefinitionStatus": qos802AclDefinitionStatus,
       "qos802AclDefinitionLabel": qos802AclDefinitionLabel,
       "qosPolicy802PibConformance": qosPolicy802PibConformance,
       "qosPolicy802PibCompliances": qosPolicy802PibCompliances,
       "qosPolicy802PibCompliance": qosPolicy802PibCompliance,
       "qosPolicy802PibGroups": qosPolicy802PibGroups,
       "qos802DscpMappingGroup": qos802DscpMappingGroup,
       "qos802CosToDscpGroup": qos802CosToDscpGroup,
       "qos802AceGroup": qos802AceGroup,
       "qos802AclDefinitionGroup": qos802AclDefinitionGroup}
)
