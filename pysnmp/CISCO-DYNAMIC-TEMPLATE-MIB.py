# SNMP MIB module (CISCO-DYNAMIC-TEMPLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DYNAMIC-TEMPLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:17 2024
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

(CbpElementName,) = mibBuilder.importSymbols(
    "CISCO-CBP-TC-MIB",
    "CbpElementName")

(DynamicTemplateName,
 DynamicTemplateTargetId,
 DynamicTemplateTargetType,
 DynamicTemplateType) = mibBuilder.importSymbols(
    "CISCO-DYNAMIC-TEMPLATE-TC-MIB",
    "DynamicTemplateName",
    "DynamicTemplateTargetId",
    "DynamicTemplateTargetType",
    "DynamicTemplateType")

(UnicastRpfOptions,
 UnicastRpfType) = mibBuilder.importSymbols(
    "CISCO-IP-URPF-MIB",
    "UnicastRpfOptions",
    "UnicastRpfType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoVrfName,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoVrfName")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDynamicTemplateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784)
)
ciscoDynamicTemplateMIB.setRevisions(
        ("2007-09-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDynamicTemplateMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDynamicTemplateMIBNotifs = _CiscoDynamicTemplateMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 0)
)
_CiscoDynamicTemplateMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDynamicTemplateMIBObjects = _CiscoDynamicTemplateMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1)
)
_CdtBase_ObjectIdentity = ObjectIdentity
cdtBase = _CdtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1)
)
_CdtTemplateTable_Object = MibTable
cdtTemplateTable = _CdtTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdtTemplateTable.setStatus("current")
_CdtTemplateEntry_Object = MibTableRow
cdtTemplateEntry = _CdtTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 1, 1)
)
cdtTemplateEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateName"),
)
if mibBuilder.loadTexts:
    cdtTemplateEntry.setStatus("current")
_CdtTemplateName_Type = DynamicTemplateName
_CdtTemplateName_Object = MibTableColumn
cdtTemplateName = _CdtTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 1, 1, 1),
    _CdtTemplateName_Type()
)
cdtTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtTemplateName.setStatus("current")
_CdtTemplateStatus_Type = RowStatus
_CdtTemplateStatus_Object = MibTableColumn
cdtTemplateStatus = _CdtTemplateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 1, 1, 2),
    _CdtTemplateStatus_Type()
)
cdtTemplateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtTemplateStatus.setStatus("current")


class _CdtTemplateStorage_Type(StorageType):
    """Custom type cdtTemplateStorage based on StorageType"""


_CdtTemplateStorage_Object = MibTableColumn
cdtTemplateStorage = _CdtTemplateStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 1, 1, 3),
    _CdtTemplateStorage_Type()
)
cdtTemplateStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtTemplateStorage.setStatus("current")


class _CdtTemplateType_Type(DynamicTemplateType):
    """Custom type cdtTemplateType based on DynamicTemplateType"""


_CdtTemplateType_Object = MibTableColumn
cdtTemplateType = _CdtTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 1, 1, 4),
    _CdtTemplateType_Type()
)
cdtTemplateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtTemplateType.setStatus("current")


class _CdtTemplateSrc_Type(Integer32):
    """Custom type cdtTemplateSrc based on Integer32"""
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
        *(("aaaServiceProfile", 5),
          ("aaaUserProfile", 4),
          ("derived", 2),
          ("local", 3),
          ("other", 1))
    )


_CdtTemplateSrc_Type.__name__ = "Integer32"
_CdtTemplateSrc_Object = MibTableColumn
cdtTemplateSrc = _CdtTemplateSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 1, 1, 5),
    _CdtTemplateSrc_Type()
)
cdtTemplateSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtTemplateSrc.setStatus("current")


class _CdtTemplateUsageCount_Type(Unsigned32):
    """Custom type cdtTemplateUsageCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdtTemplateUsageCount_Type.__name__ = "Unsigned32"
_CdtTemplateUsageCount_Object = MibTableColumn
cdtTemplateUsageCount = _CdtTemplateUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 1, 1, 6),
    _CdtTemplateUsageCount_Type()
)
cdtTemplateUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtTemplateUsageCount.setStatus("current")
_CdtTemplateTargetTable_Object = MibTable
cdtTemplateTargetTable = _CdtTemplateTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdtTemplateTargetTable.setStatus("current")
_CdtTemplateTargetEntry_Object = MibTableRow
cdtTemplateTargetEntry = _CdtTemplateTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 2, 1)
)
cdtTemplateTargetEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateTargetType"),
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateTargetId"),
)
if mibBuilder.loadTexts:
    cdtTemplateTargetEntry.setStatus("current")
_CdtTemplateTargetType_Type = DynamicTemplateTargetType
_CdtTemplateTargetType_Object = MibTableColumn
cdtTemplateTargetType = _CdtTemplateTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 2, 1, 1),
    _CdtTemplateTargetType_Type()
)
cdtTemplateTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdtTemplateTargetType.setStatus("current")
_CdtTemplateTargetId_Type = DynamicTemplateTargetId
_CdtTemplateTargetId_Object = MibTableColumn
cdtTemplateTargetId = _CdtTemplateTargetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 2, 1, 2),
    _CdtTemplateTargetId_Type()
)
cdtTemplateTargetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdtTemplateTargetId.setStatus("current")
_CdtTemplateTargetStatus_Type = RowStatus
_CdtTemplateTargetStatus_Object = MibTableColumn
cdtTemplateTargetStatus = _CdtTemplateTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 2, 1, 3),
    _CdtTemplateTargetStatus_Type()
)
cdtTemplateTargetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtTemplateTargetStatus.setStatus("current")


class _CdtTemplateTargetStorage_Type(StorageType):
    """Custom type cdtTemplateTargetStorage based on StorageType"""


_CdtTemplateTargetStorage_Object = MibTableColumn
cdtTemplateTargetStorage = _CdtTemplateTargetStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 2, 1, 4),
    _CdtTemplateTargetStorage_Type()
)
cdtTemplateTargetStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtTemplateTargetStorage.setStatus("current")
_CdtTemplateAssociationTable_Object = MibTable
cdtTemplateAssociationTable = _CdtTemplateAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cdtTemplateAssociationTable.setStatus("current")
_CdtTemplateAssociationEntry_Object = MibTableRow
cdtTemplateAssociationEntry = _CdtTemplateAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 3, 1)
)
cdtTemplateAssociationEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateTargetType"),
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateTargetId"),
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateAssociationName"),
)
if mibBuilder.loadTexts:
    cdtTemplateAssociationEntry.setStatus("current")
_CdtTemplateAssociationName_Type = DynamicTemplateName
_CdtTemplateAssociationName_Object = MibTableColumn
cdtTemplateAssociationName = _CdtTemplateAssociationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 3, 1, 1),
    _CdtTemplateAssociationName_Type()
)
cdtTemplateAssociationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtTemplateAssociationName.setStatus("current")


class _CdtTemplateAssociationPrecedence_Type(Unsigned32):
    """Custom type cdtTemplateAssociationPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdtTemplateAssociationPrecedence_Type.__name__ = "Unsigned32"
_CdtTemplateAssociationPrecedence_Object = MibTableColumn
cdtTemplateAssociationPrecedence = _CdtTemplateAssociationPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 3, 1, 2),
    _CdtTemplateAssociationPrecedence_Type()
)
cdtTemplateAssociationPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtTemplateAssociationPrecedence.setStatus("current")
_CdtTemplateUsageTable_Object = MibTable
cdtTemplateUsageTable = _CdtTemplateUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cdtTemplateUsageTable.setStatus("current")
_CdtTemplateUsageEntry_Object = MibTableRow
cdtTemplateUsageEntry = _CdtTemplateUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 4, 1)
)
cdtTemplateUsageEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateName"),
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateUsageTargetType"),
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateUsageTargetId"),
)
if mibBuilder.loadTexts:
    cdtTemplateUsageEntry.setStatus("current")
_CdtTemplateUsageTargetType_Type = DynamicTemplateTargetType
_CdtTemplateUsageTargetType_Object = MibTableColumn
cdtTemplateUsageTargetType = _CdtTemplateUsageTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 4, 1, 1),
    _CdtTemplateUsageTargetType_Type()
)
cdtTemplateUsageTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtTemplateUsageTargetType.setStatus("current")
_CdtTemplateUsageTargetId_Type = DynamicTemplateTargetId
_CdtTemplateUsageTargetId_Object = MibTableColumn
cdtTemplateUsageTargetId = _CdtTemplateUsageTargetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 4, 1, 2),
    _CdtTemplateUsageTargetId_Type()
)
cdtTemplateUsageTargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdtTemplateUsageTargetId.setStatus("current")
_CdtTemplateCommonTable_Object = MibTable
cdtTemplateCommonTable = _CdtTemplateCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cdtTemplateCommonTable.setStatus("current")
_CdtTemplateCommonEntry_Object = MibTableRow
cdtTemplateCommonEntry = _CdtTemplateCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1)
)
cdtTemplateCommonEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateName"),
)
if mibBuilder.loadTexts:
    cdtTemplateCommonEntry.setStatus("current")


class _CdtCommonValid_Type(Bits):
    """Custom type cdtCommonValid based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("addrPool", 3),
          ("descr", 0),
          ("ipv4AccessGroup", 4),
          ("ipv4Unreachables", 5),
          ("ipv6AccessGroup", 6),
          ("ipv6Unreachables", 7),
          ("keepalive", 1),
          ("srvAcct", 10),
          ("srvNetflow", 12),
          ("srvQos", 11),
          ("srvRedirect", 9),
          ("srvSubControl", 8),
          ("vrf", 2))
    )

_CdtCommonValid_Type.__name__ = "Bits"
_CdtCommonValid_Object = MibTableColumn
cdtCommonValid = _CdtCommonValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 1),
    _CdtCommonValid_Type()
)
cdtCommonValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonValid.setStatus("current")


class _CdtCommonDescr_Type(SnmpAdminString):
    """Custom type cdtCommonDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtCommonDescr_Type.__name__ = "SnmpAdminString"
_CdtCommonDescr_Object = MibTableColumn
cdtCommonDescr = _CdtCommonDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 2),
    _CdtCommonDescr_Type()
)
cdtCommonDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonDescr.setStatus("current")


class _CdtCommonKeepaliveInt_Type(Unsigned32):
    """Custom type cdtCommonKeepaliveInt based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdtCommonKeepaliveInt_Type.__name__ = "Unsigned32"
_CdtCommonKeepaliveInt_Object = MibTableColumn
cdtCommonKeepaliveInt = _CdtCommonKeepaliveInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 3),
    _CdtCommonKeepaliveInt_Type()
)
cdtCommonKeepaliveInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonKeepaliveInt.setStatus("current")
if mibBuilder.loadTexts:
    cdtCommonKeepaliveInt.setUnits("seconds")


class _CdtCommonKeepaliveRetries_Type(Unsigned32):
    """Custom type cdtCommonKeepaliveRetries based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CdtCommonKeepaliveRetries_Type.__name__ = "Unsigned32"
_CdtCommonKeepaliveRetries_Object = MibTableColumn
cdtCommonKeepaliveRetries = _CdtCommonKeepaliveRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 4),
    _CdtCommonKeepaliveRetries_Type()
)
cdtCommonKeepaliveRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonKeepaliveRetries.setStatus("current")
if mibBuilder.loadTexts:
    cdtCommonKeepaliveRetries.setUnits("retries")
_CdtCommonVrf_Type = CiscoVrfName
_CdtCommonVrf_Object = MibTableColumn
cdtCommonVrf = _CdtCommonVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 5),
    _CdtCommonVrf_Type()
)
cdtCommonVrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonVrf.setStatus("current")


class _CdtCommonAddrPool_Type(SnmpAdminString):
    """Custom type cdtCommonAddrPool based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtCommonAddrPool_Type.__name__ = "SnmpAdminString"
_CdtCommonAddrPool_Object = MibTableColumn
cdtCommonAddrPool = _CdtCommonAddrPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 6),
    _CdtCommonAddrPool_Type()
)
cdtCommonAddrPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonAddrPool.setStatus("current")


class _CdtCommonIpv4AccessGroup_Type(SnmpAdminString):
    """Custom type cdtCommonIpv4AccessGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtCommonIpv4AccessGroup_Type.__name__ = "SnmpAdminString"
_CdtCommonIpv4AccessGroup_Object = MibTableColumn
cdtCommonIpv4AccessGroup = _CdtCommonIpv4AccessGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 7),
    _CdtCommonIpv4AccessGroup_Type()
)
cdtCommonIpv4AccessGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonIpv4AccessGroup.setStatus("current")


class _CdtCommonIpv4Unreachables_Type(TruthValue):
    """Custom type cdtCommonIpv4Unreachables based on TruthValue"""


_CdtCommonIpv4Unreachables_Object = MibTableColumn
cdtCommonIpv4Unreachables = _CdtCommonIpv4Unreachables_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 8),
    _CdtCommonIpv4Unreachables_Type()
)
cdtCommonIpv4Unreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonIpv4Unreachables.setStatus("current")


class _CdtCommonIpv6AccessGroup_Type(SnmpAdminString):
    """Custom type cdtCommonIpv6AccessGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtCommonIpv6AccessGroup_Type.__name__ = "SnmpAdminString"
_CdtCommonIpv6AccessGroup_Object = MibTableColumn
cdtCommonIpv6AccessGroup = _CdtCommonIpv6AccessGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 9),
    _CdtCommonIpv6AccessGroup_Type()
)
cdtCommonIpv6AccessGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonIpv6AccessGroup.setStatus("current")


class _CdtCommonIpv6Unreachables_Type(TruthValue):
    """Custom type cdtCommonIpv6Unreachables based on TruthValue"""


_CdtCommonIpv6Unreachables_Object = MibTableColumn
cdtCommonIpv6Unreachables = _CdtCommonIpv6Unreachables_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 10),
    _CdtCommonIpv6Unreachables_Type()
)
cdtCommonIpv6Unreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonIpv6Unreachables.setStatus("current")
_CdtCommonSrvSubControl_Type = CbpElementName
_CdtCommonSrvSubControl_Object = MibTableColumn
cdtCommonSrvSubControl = _CdtCommonSrvSubControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 11),
    _CdtCommonSrvSubControl_Type()
)
cdtCommonSrvSubControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonSrvSubControl.setStatus("current")
_CdtCommonSrvRedirect_Type = CbpElementName
_CdtCommonSrvRedirect_Object = MibTableColumn
cdtCommonSrvRedirect = _CdtCommonSrvRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 12),
    _CdtCommonSrvRedirect_Type()
)
cdtCommonSrvRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonSrvRedirect.setStatus("current")
_CdtCommonSrvAcct_Type = CbpElementName
_CdtCommonSrvAcct_Object = MibTableColumn
cdtCommonSrvAcct = _CdtCommonSrvAcct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 13),
    _CdtCommonSrvAcct_Type()
)
cdtCommonSrvAcct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonSrvAcct.setStatus("current")
_CdtCommonSrvQos_Type = CbpElementName
_CdtCommonSrvQos_Object = MibTableColumn
cdtCommonSrvQos = _CdtCommonSrvQos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 14),
    _CdtCommonSrvQos_Type()
)
cdtCommonSrvQos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonSrvQos.setStatus("current")
_CdtCommonSrvNetflow_Type = CbpElementName
_CdtCommonSrvNetflow_Object = MibTableColumn
cdtCommonSrvNetflow = _CdtCommonSrvNetflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 1, 5, 1, 15),
    _CdtCommonSrvNetflow_Type()
)
cdtCommonSrvNetflow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtCommonSrvNetflow.setStatus("current")
_CdtCommonIf_ObjectIdentity = ObjectIdentity
cdtCommonIf = _CdtCommonIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2)
)
_CdtIfTemplateTable_Object = MibTable
cdtIfTemplateTable = _CdtIfTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdtIfTemplateTable.setStatus("current")
_CdtIfTemplateEntry_Object = MibTableRow
cdtIfTemplateEntry = _CdtIfTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1)
)
cdtIfTemplateEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateName"),
)
if mibBuilder.loadTexts:
    cdtIfTemplateEntry.setStatus("current")


class _CdtIfValid_Type(Bits):
    """Custom type cdtIfValid based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("cdpEnable", 1),
          ("flowMonitor", 2),
          ("ipv4Mtu", 5),
          ("ipv4SubEnable", 4),
          ("ipv4TcpMssAdjust", 6),
          ("ipv4Unnumbered", 3),
          ("ipv4VerifyUniRpf", 7),
          ("ipv4VerifyUniRpfAcl", 8),
          ("ipv4VerifyUniRpfOpts", 9),
          ("ipv6Enable", 10),
          ("ipv6NdDadAttempts", 20),
          ("ipv6NdNsInterval", 21),
          ("ipv6NdOpts", 19),
          ("ipv6NdPreferredLife", 18),
          ("ipv6NdPrefix", 16),
          ("ipv6NdRaIntervalMax", 23),
          ("ipv6NdRaIntervalMin", 24),
          ("ipv6NdRaLife", 25),
          ("ipv6NdRaRouterPreference", 26),
          ("ipv6NdReachableTime", 22),
          ("ipv6NdValidLife", 17),
          ("ipv6SubEnable", 11),
          ("ipv6TcpMssAdjust", 12),
          ("ipv6VerifyUniRpf", 13),
          ("ipv6VerifyUniRpfAcl", 14),
          ("ipv6VerifyUniRpfOpts", 15),
          ("mtu", 0))
    )

_CdtIfValid_Type.__name__ = "Bits"
_CdtIfValid_Object = MibTableColumn
cdtIfValid = _CdtIfValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 1),
    _CdtIfValid_Type()
)
cdtIfValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfValid.setStatus("current")


class _CdtIfMtu_Type(Unsigned32):
    """Custom type cdtIfMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 65535),
    )


_CdtIfMtu_Type.__name__ = "Unsigned32"
_CdtIfMtu_Object = MibTableColumn
cdtIfMtu = _CdtIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 2),
    _CdtIfMtu_Type()
)
cdtIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfMtu.setStatus("current")
if mibBuilder.loadTexts:
    cdtIfMtu.setUnits("octets")


class _CdtIfCdpEnable_Type(TruthValue):
    """Custom type cdtIfCdpEnable based on TruthValue"""


_CdtIfCdpEnable_Object = MibTableColumn
cdtIfCdpEnable = _CdtIfCdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 3),
    _CdtIfCdpEnable_Type()
)
cdtIfCdpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfCdpEnable.setStatus("current")


class _CdtIfFlowMonitor_Type(SnmpAdminString):
    """Custom type cdtIfFlowMonitor based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtIfFlowMonitor_Type.__name__ = "SnmpAdminString"
_CdtIfFlowMonitor_Object = MibTableColumn
cdtIfFlowMonitor = _CdtIfFlowMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 4),
    _CdtIfFlowMonitor_Type()
)
cdtIfFlowMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfFlowMonitor.setStatus("current")


class _CdtIfIpv4Unnumbered_Type(InterfaceIndexOrZero):
    """Custom type cdtIfIpv4Unnumbered based on InterfaceIndexOrZero"""
    defaultValue = 0


_CdtIfIpv4Unnumbered_Object = MibTableColumn
cdtIfIpv4Unnumbered = _CdtIfIpv4Unnumbered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 5),
    _CdtIfIpv4Unnumbered_Type()
)
cdtIfIpv4Unnumbered.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv4Unnumbered.setStatus("current")


class _CdtIfIpv4SubEnable_Type(TruthValue):
    """Custom type cdtIfIpv4SubEnable based on TruthValue"""


_CdtIfIpv4SubEnable_Object = MibTableColumn
cdtIfIpv4SubEnable = _CdtIfIpv4SubEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 6),
    _CdtIfIpv4SubEnable_Type()
)
cdtIfIpv4SubEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv4SubEnable.setStatus("current")


class _CdtIfIpv4Mtu_Type(Unsigned32):
    """Custom type cdtIfIpv4Mtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 65535),
    )


_CdtIfIpv4Mtu_Type.__name__ = "Unsigned32"
_CdtIfIpv4Mtu_Object = MibTableColumn
cdtIfIpv4Mtu = _CdtIfIpv4Mtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 7),
    _CdtIfIpv4Mtu_Type()
)
cdtIfIpv4Mtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv4Mtu.setStatus("current")
if mibBuilder.loadTexts:
    cdtIfIpv4Mtu.setUnits("octets")


class _CdtIfIpv4TcpMssAdjust_Type(Unsigned32):
    """Custom type cdtIfIpv4TcpMssAdjust based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 1460),
    )


_CdtIfIpv4TcpMssAdjust_Type.__name__ = "Unsigned32"
_CdtIfIpv4TcpMssAdjust_Object = MibTableColumn
cdtIfIpv4TcpMssAdjust = _CdtIfIpv4TcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 8),
    _CdtIfIpv4TcpMssAdjust_Type()
)
cdtIfIpv4TcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv4TcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    cdtIfIpv4TcpMssAdjust.setUnits("octets")


class _CdtIfIpv4VerifyUniRpf_Type(UnicastRpfType):
    """Custom type cdtIfIpv4VerifyUniRpf based on UnicastRpfType"""


_CdtIfIpv4VerifyUniRpf_Object = MibTableColumn
cdtIfIpv4VerifyUniRpf = _CdtIfIpv4VerifyUniRpf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 9),
    _CdtIfIpv4VerifyUniRpf_Type()
)
cdtIfIpv4VerifyUniRpf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv4VerifyUniRpf.setStatus("current")


class _CdtIfIpv4VerifyUniRpfAcl_Type(SnmpAdminString):
    """Custom type cdtIfIpv4VerifyUniRpfAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtIfIpv4VerifyUniRpfAcl_Type.__name__ = "SnmpAdminString"
_CdtIfIpv4VerifyUniRpfAcl_Object = MibTableColumn
cdtIfIpv4VerifyUniRpfAcl = _CdtIfIpv4VerifyUniRpfAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 10),
    _CdtIfIpv4VerifyUniRpfAcl_Type()
)
cdtIfIpv4VerifyUniRpfAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv4VerifyUniRpfAcl.setStatus("current")


class _CdtIfIpv4VerifyUniRpfOpts_Type(UnicastRpfOptions):
    """Custom type cdtIfIpv4VerifyUniRpfOpts based on UnicastRpfOptions"""
    defaultBinValue = "0"


_CdtIfIpv4VerifyUniRpfOpts_Object = MibTableColumn
cdtIfIpv4VerifyUniRpfOpts = _CdtIfIpv4VerifyUniRpfOpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 11),
    _CdtIfIpv4VerifyUniRpfOpts_Type()
)
cdtIfIpv4VerifyUniRpfOpts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv4VerifyUniRpfOpts.setStatus("current")


class _CdtIfIpv6Enable_Type(TruthValue):
    """Custom type cdtIfIpv6Enable based on TruthValue"""


_CdtIfIpv6Enable_Object = MibTableColumn
cdtIfIpv6Enable = _CdtIfIpv6Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 12),
    _CdtIfIpv6Enable_Type()
)
cdtIfIpv6Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6Enable.setStatus("current")


class _CdtIfIpv6SubEnable_Type(TruthValue):
    """Custom type cdtIfIpv6SubEnable based on TruthValue"""


_CdtIfIpv6SubEnable_Object = MibTableColumn
cdtIfIpv6SubEnable = _CdtIfIpv6SubEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 13),
    _CdtIfIpv6SubEnable_Type()
)
cdtIfIpv6SubEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6SubEnable.setStatus("current")


class _CdtIfIpv6TcpMssAdjust_Type(Unsigned32):
    """Custom type cdtIfIpv6TcpMssAdjust based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 1460),
    )


_CdtIfIpv6TcpMssAdjust_Type.__name__ = "Unsigned32"
_CdtIfIpv6TcpMssAdjust_Object = MibTableColumn
cdtIfIpv6TcpMssAdjust = _CdtIfIpv6TcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 14),
    _CdtIfIpv6TcpMssAdjust_Type()
)
cdtIfIpv6TcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6TcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    cdtIfIpv6TcpMssAdjust.setUnits("octets")


class _CdtIfIpv6VerifyUniRpf_Type(UnicastRpfType):
    """Custom type cdtIfIpv6VerifyUniRpf based on UnicastRpfType"""


_CdtIfIpv6VerifyUniRpf_Object = MibTableColumn
cdtIfIpv6VerifyUniRpf = _CdtIfIpv6VerifyUniRpf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 15),
    _CdtIfIpv6VerifyUniRpf_Type()
)
cdtIfIpv6VerifyUniRpf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6VerifyUniRpf.setStatus("current")


class _CdtIfIpv6VerifyUniRpfAcl_Type(SnmpAdminString):
    """Custom type cdtIfIpv6VerifyUniRpfAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtIfIpv6VerifyUniRpfAcl_Type.__name__ = "SnmpAdminString"
_CdtIfIpv6VerifyUniRpfAcl_Object = MibTableColumn
cdtIfIpv6VerifyUniRpfAcl = _CdtIfIpv6VerifyUniRpfAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 16),
    _CdtIfIpv6VerifyUniRpfAcl_Type()
)
cdtIfIpv6VerifyUniRpfAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6VerifyUniRpfAcl.setStatus("current")


class _CdtIfIpv6VerifyUniRpfOpts_Type(UnicastRpfOptions):
    """Custom type cdtIfIpv6VerifyUniRpfOpts based on UnicastRpfOptions"""
    defaultBinValue = "0"


_CdtIfIpv6VerifyUniRpfOpts_Object = MibTableColumn
cdtIfIpv6VerifyUniRpfOpts = _CdtIfIpv6VerifyUniRpfOpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 17),
    _CdtIfIpv6VerifyUniRpfOpts_Type()
)
cdtIfIpv6VerifyUniRpfOpts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6VerifyUniRpfOpts.setStatus("current")


class _CdtIfIpv6NdPrefix_Type(InetAddressIPv6):
    """Custom type cdtIfIpv6NdPrefix based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_CdtIfIpv6NdPrefix_Object = MibTableColumn
cdtIfIpv6NdPrefix = _CdtIfIpv6NdPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 18),
    _CdtIfIpv6NdPrefix_Type()
)
cdtIfIpv6NdPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdPrefix.setStatus("current")


class _CdtIfIpv6NdPrefixLength_Type(InetAddressPrefixLength):
    """Custom type cdtIfIpv6NdPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_CdtIfIpv6NdPrefixLength_Object = MibTableColumn
cdtIfIpv6NdPrefixLength = _CdtIfIpv6NdPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 19),
    _CdtIfIpv6NdPrefixLength_Type()
)
cdtIfIpv6NdPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdPrefixLength.setStatus("current")


class _CdtIfIpv6NdValidLife_Type(Unsigned32):
    """Custom type cdtIfIpv6NdValidLife based on Unsigned32"""
    defaultValue = 2592000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdtIfIpv6NdValidLife_Type.__name__ = "Unsigned32"
_CdtIfIpv6NdValidLife_Object = MibTableColumn
cdtIfIpv6NdValidLife = _CdtIfIpv6NdValidLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 20),
    _CdtIfIpv6NdValidLife_Type()
)
cdtIfIpv6NdValidLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdValidLife.setStatus("current")
if mibBuilder.loadTexts:
    cdtIfIpv6NdValidLife.setUnits("seconds")


class _CdtIfIpv6NdPreferredLife_Type(Unsigned32):
    """Custom type cdtIfIpv6NdPreferredLife based on Unsigned32"""
    defaultValue = 604800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdtIfIpv6NdPreferredLife_Type.__name__ = "Unsigned32"
_CdtIfIpv6NdPreferredLife_Object = MibTableColumn
cdtIfIpv6NdPreferredLife = _CdtIfIpv6NdPreferredLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 21),
    _CdtIfIpv6NdPreferredLife_Type()
)
cdtIfIpv6NdPreferredLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdPreferredLife.setStatus("current")
if mibBuilder.loadTexts:
    cdtIfIpv6NdPreferredLife.setUnits("seconds")


class _CdtIfIpv6NdOpts_Type(Bits):
    """Custom type cdtIfIpv6NdOpts based on Bits"""
    defaultBinValue = "1111"

    namedValues = NamedValues(
        *(("advertise", 0),
          ("advertisementInterval", 4),
          ("autoConfig", 3),
          ("framedIpv6Prefix", 7),
          ("managedConfigFlag", 5),
          ("onlink", 1),
          ("otherConfigFlag", 6),
          ("raSuppress", 8),
          ("router", 2))
    )

_CdtIfIpv6NdOpts_Type.__name__ = "Bits"
_CdtIfIpv6NdOpts_Object = MibTableColumn
cdtIfIpv6NdOpts = _CdtIfIpv6NdOpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 22),
    _CdtIfIpv6NdOpts_Type()
)
cdtIfIpv6NdOpts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdOpts.setStatus("current")


class _CdtIfIpv6NdDadAttempts_Type(Unsigned32):
    """Custom type cdtIfIpv6NdDadAttempts based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CdtIfIpv6NdDadAttempts_Type.__name__ = "Unsigned32"
_CdtIfIpv6NdDadAttempts_Object = MibTableColumn
cdtIfIpv6NdDadAttempts = _CdtIfIpv6NdDadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 23),
    _CdtIfIpv6NdDadAttempts_Type()
)
cdtIfIpv6NdDadAttempts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdDadAttempts.setStatus("current")


class _CdtIfIpv6NdNsInterval_Type(Unsigned32):
    """Custom type cdtIfIpv6NdNsInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_CdtIfIpv6NdNsInterval_Type.__name__ = "Unsigned32"
_CdtIfIpv6NdNsInterval_Object = MibTableColumn
cdtIfIpv6NdNsInterval = _CdtIfIpv6NdNsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 24),
    _CdtIfIpv6NdNsInterval_Type()
)
cdtIfIpv6NdNsInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdNsInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdtIfIpv6NdNsInterval.setUnits("milliseconds")


class _CdtIfIpv6NdReachableTime_Type(Unsigned32):
    """Custom type cdtIfIpv6NdReachableTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdtIfIpv6NdReachableTime_Type.__name__ = "Unsigned32"
_CdtIfIpv6NdReachableTime_Object = MibTableColumn
cdtIfIpv6NdReachableTime = _CdtIfIpv6NdReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 25),
    _CdtIfIpv6NdReachableTime_Type()
)
cdtIfIpv6NdReachableTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    cdtIfIpv6NdReachableTime.setUnits("milliseconds")


class _CdtIfIpv6NdRaIntervalUnits_Type(Integer32):
    """Custom type cdtIfIpv6NdRaIntervalUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("milliseconds", 2),
          ("seconds", 1))
    )


_CdtIfIpv6NdRaIntervalUnits_Type.__name__ = "Integer32"
_CdtIfIpv6NdRaIntervalUnits_Object = MibTableColumn
cdtIfIpv6NdRaIntervalUnits = _CdtIfIpv6NdRaIntervalUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 26),
    _CdtIfIpv6NdRaIntervalUnits_Type()
)
cdtIfIpv6NdRaIntervalUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdRaIntervalUnits.setStatus("current")


class _CdtIfIpv6NdRaIntervalMax_Type(Unsigned32):
    """Custom type cdtIfIpv6NdRaIntervalMax based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdtIfIpv6NdRaIntervalMax_Type.__name__ = "Unsigned32"
_CdtIfIpv6NdRaIntervalMax_Object = MibTableColumn
cdtIfIpv6NdRaIntervalMax = _CdtIfIpv6NdRaIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 27),
    _CdtIfIpv6NdRaIntervalMax_Type()
)
cdtIfIpv6NdRaIntervalMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdRaIntervalMax.setStatus("current")


class _CdtIfIpv6NdRaIntervalMin_Type(Unsigned32):
    """Custom type cdtIfIpv6NdRaIntervalMin based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdtIfIpv6NdRaIntervalMin_Type.__name__ = "Unsigned32"
_CdtIfIpv6NdRaIntervalMin_Object = MibTableColumn
cdtIfIpv6NdRaIntervalMin = _CdtIfIpv6NdRaIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 28),
    _CdtIfIpv6NdRaIntervalMin_Type()
)
cdtIfIpv6NdRaIntervalMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdRaIntervalMin.setStatus("current")


class _CdtIfIpv6NdRaLife_Type(Unsigned32):
    """Custom type cdtIfIpv6NdRaLife based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdtIfIpv6NdRaLife_Type.__name__ = "Unsigned32"
_CdtIfIpv6NdRaLife_Object = MibTableColumn
cdtIfIpv6NdRaLife = _CdtIfIpv6NdRaLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 29),
    _CdtIfIpv6NdRaLife_Type()
)
cdtIfIpv6NdRaLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdRaLife.setStatus("current")
if mibBuilder.loadTexts:
    cdtIfIpv6NdRaLife.setUnits("seconds")


class _CdtIfIpv6NdRouterPreference_Type(Integer32):
    """Custom type cdtIfIpv6NdRouterPreference based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_CdtIfIpv6NdRouterPreference_Type.__name__ = "Integer32"
_CdtIfIpv6NdRouterPreference_Object = MibTableColumn
cdtIfIpv6NdRouterPreference = _CdtIfIpv6NdRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 2, 1, 1, 30),
    _CdtIfIpv6NdRouterPreference_Type()
)
cdtIfIpv6NdRouterPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtIfIpv6NdRouterPreference.setStatus("current")
_CdtPpp_ObjectIdentity = ObjectIdentity
cdtPpp = _CdtPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3)
)
_CdtPppTemplateTable_Object = MibTable
cdtPppTemplateTable = _CdtPppTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdtPppTemplateTable.setStatus("current")
_CdtPppTemplateEntry_Object = MibTableRow
cdtPppTemplateEntry = _CdtPppTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1)
)
cdtPppTemplateEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateName"),
)
if mibBuilder.loadTexts:
    cdtPppTemplateEntry.setStatus("current")


class _CdtPppValid_Type(Bits):
    """Custom type cdtPppValid based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("accounting", 1),
          ("authentication", 2),
          ("authorization", 4),
          ("autthenticationMethods", 3),
          ("chapHostname", 13),
          ("chapOpts", 12),
          ("chapPassword", 14),
          ("eapIdentity", 25),
          ("eapOpts", 24),
          ("eapPassword", 26),
          ("ipcpAddrOption", 27),
          ("ipcpDnsOption", 28),
          ("ipcpDnsPrimary", 29),
          ("ipcpDnsSecondary", 30),
          ("ipcpMask", 35),
          ("ipcpMaskOption", 34),
          ("ipcpWinsOption", 31),
          ("ipcpWinsPrimary", 32),
          ("ipcpWinsSecondary", 33),
          ("loopbackIgnore", 5),
          ("maxBadAuth", 6),
          ("maxConfigure", 7),
          ("maxFailure", 8),
          ("maxTerminate", 9),
          ("msChapV1Hostname", 16),
          ("msChapV1Opts", 15),
          ("msChapV1Password", 17),
          ("msChapV2Hostname", 19),
          ("msChapV2Opts", 18),
          ("msChapV2Password", 20),
          ("papOpts", 21),
          ("papPassword", 23),
          ("papUsername", 22),
          ("peerDefIpAddr", 38),
          ("peerDefIpAddrOpts", 36),
          ("peerDefIpAddrSrc", 37),
          ("timeoutAuthentication", 10),
          ("timeoutRetry", 11),
          ("valid", 0))
    )

_CdtPppValid_Type.__name__ = "Bits"
_CdtPppValid_Object = MibTableColumn
cdtPppValid = _CdtPppValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 1),
    _CdtPppValid_Type()
)
cdtPppValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppValid.setStatus("current")


class _CdtPppAccounting_Type(TruthValue):
    """Custom type cdtPppAccounting based on TruthValue"""


_CdtPppAccounting_Object = MibTableColumn
cdtPppAccounting = _CdtPppAccounting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 2),
    _CdtPppAccounting_Type()
)
cdtPppAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppAccounting.setStatus("current")


class _CdtPppAuthentication_Type(Bits):
    """Custom type cdtPppAuthentication based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("callin", 6),
          ("chap", 0),
          ("eap", 4),
          ("msChap", 1),
          ("msChapV2", 2),
          ("oneTime", 7),
          ("optional", 5),
          ("pap", 3))
    )

_CdtPppAuthentication_Type.__name__ = "Bits"
_CdtPppAuthentication_Object = MibTableColumn
cdtPppAuthentication = _CdtPppAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 3),
    _CdtPppAuthentication_Type()
)
cdtPppAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppAuthentication.setStatus("current")


class _CdtPppAuthenticationMethods_Type(SnmpAdminString):
    """Custom type cdtPppAuthenticationMethods based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppAuthenticationMethods_Type.__name__ = "SnmpAdminString"
_CdtPppAuthenticationMethods_Object = MibTableColumn
cdtPppAuthenticationMethods = _CdtPppAuthenticationMethods_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 4),
    _CdtPppAuthenticationMethods_Type()
)
cdtPppAuthenticationMethods.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppAuthenticationMethods.setStatus("current")


class _CdtPppAuthorization_Type(TruthValue):
    """Custom type cdtPppAuthorization based on TruthValue"""


_CdtPppAuthorization_Object = MibTableColumn
cdtPppAuthorization = _CdtPppAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 5),
    _CdtPppAuthorization_Type()
)
cdtPppAuthorization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppAuthorization.setStatus("current")


class _CdtPppLoopbackIgnore_Type(TruthValue):
    """Custom type cdtPppLoopbackIgnore based on TruthValue"""


_CdtPppLoopbackIgnore_Object = MibTableColumn
cdtPppLoopbackIgnore = _CdtPppLoopbackIgnore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 6),
    _CdtPppLoopbackIgnore_Type()
)
cdtPppLoopbackIgnore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppLoopbackIgnore.setStatus("current")


class _CdtPppMaxBadAuth_Type(Unsigned32):
    """Custom type cdtPppMaxBadAuth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdtPppMaxBadAuth_Type.__name__ = "Unsigned32"
_CdtPppMaxBadAuth_Object = MibTableColumn
cdtPppMaxBadAuth = _CdtPppMaxBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 7),
    _CdtPppMaxBadAuth_Type()
)
cdtPppMaxBadAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMaxBadAuth.setStatus("current")


class _CdtPppMaxConfigure_Type(Unsigned32):
    """Custom type cdtPppMaxConfigure based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdtPppMaxConfigure_Type.__name__ = "Unsigned32"
_CdtPppMaxConfigure_Object = MibTableColumn
cdtPppMaxConfigure = _CdtPppMaxConfigure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 8),
    _CdtPppMaxConfigure_Type()
)
cdtPppMaxConfigure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMaxConfigure.setStatus("current")


class _CdtPppMaxFailure_Type(Unsigned32):
    """Custom type cdtPppMaxFailure based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdtPppMaxFailure_Type.__name__ = "Unsigned32"
_CdtPppMaxFailure_Object = MibTableColumn
cdtPppMaxFailure = _CdtPppMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 9),
    _CdtPppMaxFailure_Type()
)
cdtPppMaxFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMaxFailure.setStatus("current")


class _CdtPppMaxTerminate_Type(Unsigned32):
    """Custom type cdtPppMaxTerminate based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdtPppMaxTerminate_Type.__name__ = "Unsigned32"
_CdtPppMaxTerminate_Object = MibTableColumn
cdtPppMaxTerminate = _CdtPppMaxTerminate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 10),
    _CdtPppMaxTerminate_Type()
)
cdtPppMaxTerminate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMaxTerminate.setStatus("current")


class _CdtPppTimeoutAuthentication_Type(Unsigned32):
    """Custom type cdtPppTimeoutAuthentication based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CdtPppTimeoutAuthentication_Type.__name__ = "Unsigned32"
_CdtPppTimeoutAuthentication_Object = MibTableColumn
cdtPppTimeoutAuthentication = _CdtPppTimeoutAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 11),
    _CdtPppTimeoutAuthentication_Type()
)
cdtPppTimeoutAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppTimeoutAuthentication.setStatus("current")
if mibBuilder.loadTexts:
    cdtPppTimeoutAuthentication.setUnits("seconds")


class _CdtPppTimeoutRetry_Type(Unsigned32):
    """Custom type cdtPppTimeoutRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CdtPppTimeoutRetry_Type.__name__ = "Unsigned32"
_CdtPppTimeoutRetry_Object = MibTableColumn
cdtPppTimeoutRetry = _CdtPppTimeoutRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 12),
    _CdtPppTimeoutRetry_Type()
)
cdtPppTimeoutRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppTimeoutRetry.setStatus("current")
if mibBuilder.loadTexts:
    cdtPppTimeoutRetry.setUnits("seconds")


class _CdtPppChapOpts_Type(Bits):
    """Custom type cdtPppChapOpts based on Bits"""
    defaultBinValue = "001"

    namedValues = NamedValues(
        *(("callin", 1),
          ("encrypted", 3),
          ("refuse", 0),
          ("wait", 2))
    )

_CdtPppChapOpts_Type.__name__ = "Bits"
_CdtPppChapOpts_Object = MibTableColumn
cdtPppChapOpts = _CdtPppChapOpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 13),
    _CdtPppChapOpts_Type()
)
cdtPppChapOpts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppChapOpts.setStatus("current")


class _CdtPppChapHostname_Type(SnmpAdminString):
    """Custom type cdtPppChapHostname based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppChapHostname_Type.__name__ = "SnmpAdminString"
_CdtPppChapHostname_Object = MibTableColumn
cdtPppChapHostname = _CdtPppChapHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 14),
    _CdtPppChapHostname_Type()
)
cdtPppChapHostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppChapHostname.setStatus("current")


class _CdtPppChapPassword_Type(SnmpAdminString):
    """Custom type cdtPppChapPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppChapPassword_Type.__name__ = "SnmpAdminString"
_CdtPppChapPassword_Object = MibTableColumn
cdtPppChapPassword = _CdtPppChapPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 15),
    _CdtPppChapPassword_Type()
)
cdtPppChapPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppChapPassword.setStatus("current")


class _CdtPppMsChapV1Opts_Type(Bits):
    """Custom type cdtPppMsChapV1Opts based on Bits"""
    defaultBinValue = "001"

    namedValues = NamedValues(
        *(("callin", 1),
          ("encrypted", 3),
          ("refuse", 0),
          ("wait", 2))
    )

_CdtPppMsChapV1Opts_Type.__name__ = "Bits"
_CdtPppMsChapV1Opts_Object = MibTableColumn
cdtPppMsChapV1Opts = _CdtPppMsChapV1Opts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 16),
    _CdtPppMsChapV1Opts_Type()
)
cdtPppMsChapV1Opts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMsChapV1Opts.setStatus("current")


class _CdtPppMsChapV1Hostname_Type(SnmpAdminString):
    """Custom type cdtPppMsChapV1Hostname based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppMsChapV1Hostname_Type.__name__ = "SnmpAdminString"
_CdtPppMsChapV1Hostname_Object = MibTableColumn
cdtPppMsChapV1Hostname = _CdtPppMsChapV1Hostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 17),
    _CdtPppMsChapV1Hostname_Type()
)
cdtPppMsChapV1Hostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMsChapV1Hostname.setStatus("current")


class _CdtPppMsChapV1Password_Type(SnmpAdminString):
    """Custom type cdtPppMsChapV1Password based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppMsChapV1Password_Type.__name__ = "SnmpAdminString"
_CdtPppMsChapV1Password_Object = MibTableColumn
cdtPppMsChapV1Password = _CdtPppMsChapV1Password_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 18),
    _CdtPppMsChapV1Password_Type()
)
cdtPppMsChapV1Password.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMsChapV1Password.setStatus("current")


class _CdtPppMsChapV2Opts_Type(Bits):
    """Custom type cdtPppMsChapV2Opts based on Bits"""
    defaultBinValue = "001"

    namedValues = NamedValues(
        *(("callin", 1),
          ("encrypted", 3),
          ("refuse", 0),
          ("wait", 2))
    )

_CdtPppMsChapV2Opts_Type.__name__ = "Bits"
_CdtPppMsChapV2Opts_Object = MibTableColumn
cdtPppMsChapV2Opts = _CdtPppMsChapV2Opts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 19),
    _CdtPppMsChapV2Opts_Type()
)
cdtPppMsChapV2Opts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMsChapV2Opts.setStatus("current")


class _CdtPppMsChapV2Hostname_Type(SnmpAdminString):
    """Custom type cdtPppMsChapV2Hostname based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppMsChapV2Hostname_Type.__name__ = "SnmpAdminString"
_CdtPppMsChapV2Hostname_Object = MibTableColumn
cdtPppMsChapV2Hostname = _CdtPppMsChapV2Hostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 20),
    _CdtPppMsChapV2Hostname_Type()
)
cdtPppMsChapV2Hostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMsChapV2Hostname.setStatus("current")


class _CdtPppMsChapV2Password_Type(SnmpAdminString):
    """Custom type cdtPppMsChapV2Password based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppMsChapV2Password_Type.__name__ = "SnmpAdminString"
_CdtPppMsChapV2Password_Object = MibTableColumn
cdtPppMsChapV2Password = _CdtPppMsChapV2Password_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 21),
    _CdtPppMsChapV2Password_Type()
)
cdtPppMsChapV2Password.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppMsChapV2Password.setStatus("current")


class _CdtPppPapOpts_Type(Bits):
    """Custom type cdtPppPapOpts based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("encrypted", 1),
          ("refuse", 0))
    )

_CdtPppPapOpts_Type.__name__ = "Bits"
_CdtPppPapOpts_Object = MibTableColumn
cdtPppPapOpts = _CdtPppPapOpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 22),
    _CdtPppPapOpts_Type()
)
cdtPppPapOpts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppPapOpts.setStatus("current")


class _CdtPppPapUsername_Type(SnmpAdminString):
    """Custom type cdtPppPapUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppPapUsername_Type.__name__ = "SnmpAdminString"
_CdtPppPapUsername_Object = MibTableColumn
cdtPppPapUsername = _CdtPppPapUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 23),
    _CdtPppPapUsername_Type()
)
cdtPppPapUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppPapUsername.setStatus("current")


class _CdtPppPapPassword_Type(SnmpAdminString):
    """Custom type cdtPppPapPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppPapPassword_Type.__name__ = "SnmpAdminString"
_CdtPppPapPassword_Object = MibTableColumn
cdtPppPapPassword = _CdtPppPapPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 24),
    _CdtPppPapPassword_Type()
)
cdtPppPapPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppPapPassword.setStatus("current")


class _CdtPppEapOpts_Type(Bits):
    """Custom type cdtPppEapOpts based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("callin", 1),
          ("local", 3),
          ("refuse", 0),
          ("wait", 2))
    )

_CdtPppEapOpts_Type.__name__ = "Bits"
_CdtPppEapOpts_Object = MibTableColumn
cdtPppEapOpts = _CdtPppEapOpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 25),
    _CdtPppEapOpts_Type()
)
cdtPppEapOpts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppEapOpts.setStatus("current")


class _CdtPppEapIdentity_Type(SnmpAdminString):
    """Custom type cdtPppEapIdentity based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppEapIdentity_Type.__name__ = "SnmpAdminString"
_CdtPppEapIdentity_Object = MibTableColumn
cdtPppEapIdentity = _CdtPppEapIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 26),
    _CdtPppEapIdentity_Type()
)
cdtPppEapIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppEapIdentity.setStatus("current")


class _CdtPppEapPassword_Type(SnmpAdminString):
    """Custom type cdtPppEapPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppEapPassword_Type.__name__ = "SnmpAdminString"
_CdtPppEapPassword_Object = MibTableColumn
cdtPppEapPassword = _CdtPppEapPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 27),
    _CdtPppEapPassword_Type()
)
cdtPppEapPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppEapPassword.setStatus("current")


class _CdtPppIpcpAddrOption_Type(Integer32):
    """Custom type cdtPppIpcpAddrOption based on Integer32"""
    defaultValue = 1

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
        *(("accept", 2),
          ("other", 1),
          ("required", 3),
          ("unique", 4))
    )


_CdtPppIpcpAddrOption_Type.__name__ = "Integer32"
_CdtPppIpcpAddrOption_Object = MibTableColumn
cdtPppIpcpAddrOption = _CdtPppIpcpAddrOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 28),
    _CdtPppIpcpAddrOption_Type()
)
cdtPppIpcpAddrOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppIpcpAddrOption.setStatus("current")


class _CdtPppIpcpDnsOption_Type(Integer32):
    """Custom type cdtPppIpcpDnsOption based on Integer32"""
    defaultValue = 1

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
        *(("accept", 2),
          ("other", 1),
          ("reject", 4),
          ("request", 3))
    )


_CdtPppIpcpDnsOption_Type.__name__ = "Integer32"
_CdtPppIpcpDnsOption_Object = MibTableColumn
cdtPppIpcpDnsOption = _CdtPppIpcpDnsOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 29),
    _CdtPppIpcpDnsOption_Type()
)
cdtPppIpcpDnsOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppIpcpDnsOption.setStatus("current")


class _CdtPppIpcpDnsPrimary_Type(InetAddressIPv4):
    """Custom type cdtPppIpcpDnsPrimary based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_CdtPppIpcpDnsPrimary_Object = MibTableColumn
cdtPppIpcpDnsPrimary = _CdtPppIpcpDnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 30),
    _CdtPppIpcpDnsPrimary_Type()
)
cdtPppIpcpDnsPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppIpcpDnsPrimary.setStatus("current")


class _CdtPppIpcpDnsSecondary_Type(InetAddressIPv4):
    """Custom type cdtPppIpcpDnsSecondary based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_CdtPppIpcpDnsSecondary_Object = MibTableColumn
cdtPppIpcpDnsSecondary = _CdtPppIpcpDnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 31),
    _CdtPppIpcpDnsSecondary_Type()
)
cdtPppIpcpDnsSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppIpcpDnsSecondary.setStatus("current")


class _CdtPppIpcpWinsOption_Type(Integer32):
    """Custom type cdtPppIpcpWinsOption based on Integer32"""
    defaultValue = 1

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
        *(("accept", 2),
          ("other", 1),
          ("reject", 4),
          ("request", 3))
    )


_CdtPppIpcpWinsOption_Type.__name__ = "Integer32"
_CdtPppIpcpWinsOption_Object = MibTableColumn
cdtPppIpcpWinsOption = _CdtPppIpcpWinsOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 32),
    _CdtPppIpcpWinsOption_Type()
)
cdtPppIpcpWinsOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppIpcpWinsOption.setStatus("current")


class _CdtPppIpcpWinsPrimary_Type(InetAddressIPv4):
    """Custom type cdtPppIpcpWinsPrimary based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_CdtPppIpcpWinsPrimary_Object = MibTableColumn
cdtPppIpcpWinsPrimary = _CdtPppIpcpWinsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 33),
    _CdtPppIpcpWinsPrimary_Type()
)
cdtPppIpcpWinsPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppIpcpWinsPrimary.setStatus("current")


class _CdtPppIpcpWinsSecondary_Type(InetAddressIPv4):
    """Custom type cdtPppIpcpWinsSecondary based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_CdtPppIpcpWinsSecondary_Object = MibTableColumn
cdtPppIpcpWinsSecondary = _CdtPppIpcpWinsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 34),
    _CdtPppIpcpWinsSecondary_Type()
)
cdtPppIpcpWinsSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppIpcpWinsSecondary.setStatus("current")


class _CdtPppIpcpMaskOption_Type(Integer32):
    """Custom type cdtPppIpcpMaskOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reject", 3),
          ("request", 2))
    )


_CdtPppIpcpMaskOption_Type.__name__ = "Integer32"
_CdtPppIpcpMaskOption_Object = MibTableColumn
cdtPppIpcpMaskOption = _CdtPppIpcpMaskOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 35),
    _CdtPppIpcpMaskOption_Type()
)
cdtPppIpcpMaskOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppIpcpMaskOption.setStatus("current")


class _CdtPppIpcpMask_Type(InetAddressIPv4):
    """Custom type cdtPppIpcpMask based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_CdtPppIpcpMask_Object = MibTableColumn
cdtPppIpcpMask = _CdtPppIpcpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 36),
    _CdtPppIpcpMask_Type()
)
cdtPppIpcpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppIpcpMask.setStatus("current")


class _CdtPppPeerDefIpAddrOpts_Type(Bits):
    """Custom type cdtPppPeerDefIpAddrOpts based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("ipAddrForced", 0),
          ("matchAaaPools", 1),
          ("staticPool", 2))
    )

_CdtPppPeerDefIpAddrOpts_Type.__name__ = "Bits"
_CdtPppPeerDefIpAddrOpts_Object = MibTableColumn
cdtPppPeerDefIpAddrOpts = _CdtPppPeerDefIpAddrOpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 37),
    _CdtPppPeerDefIpAddrOpts_Type()
)
cdtPppPeerDefIpAddrOpts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppPeerDefIpAddrOpts.setStatus("current")


class _CdtPppPeerDefIpAddrSrc_Type(Integer32):
    """Custom type cdtPppPeerDefIpAddrSrc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 3),
          ("pool", 2),
          ("static", 1))
    )


_CdtPppPeerDefIpAddrSrc_Type.__name__ = "Integer32"
_CdtPppPeerDefIpAddrSrc_Object = MibTableColumn
cdtPppPeerDefIpAddrSrc = _CdtPppPeerDefIpAddrSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 38),
    _CdtPppPeerDefIpAddrSrc_Type()
)
cdtPppPeerDefIpAddrSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppPeerDefIpAddrSrc.setStatus("current")


class _CdtPppPeerDefIpAddr_Type(InetAddressIPv4):
    """Custom type cdtPppPeerDefIpAddr based on InetAddressIPv4"""
    defaultHexValue = "00000000"


_CdtPppPeerDefIpAddr_Object = MibTableColumn
cdtPppPeerDefIpAddr = _CdtPppPeerDefIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 1, 1, 39),
    _CdtPppPeerDefIpAddr_Type()
)
cdtPppPeerDefIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppPeerDefIpAddr.setStatus("current")
_CdtPppPeerIpAddrPoolTable_Object = MibTable
cdtPppPeerIpAddrPoolTable = _CdtPppPeerIpAddrPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdtPppPeerIpAddrPoolTable.setStatus("current")
_CdtPppPeerIpAddrPoolEntry_Object = MibTableRow
cdtPppPeerIpAddrPoolEntry = _CdtPppPeerIpAddrPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 2, 1)
)
cdtPppPeerIpAddrPoolEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateName"),
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPeerIpAddrPoolPriority"),
)
if mibBuilder.loadTexts:
    cdtPppPeerIpAddrPoolEntry.setStatus("current")


class _CdtPppPeerIpAddrPoolPriority_Type(Unsigned32):
    """Custom type cdtPppPeerIpAddrPoolPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdtPppPeerIpAddrPoolPriority_Type.__name__ = "Unsigned32"
_CdtPppPeerIpAddrPoolPriority_Object = MibTableColumn
cdtPppPeerIpAddrPoolPriority = _CdtPppPeerIpAddrPoolPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 2, 1, 1),
    _CdtPppPeerIpAddrPoolPriority_Type()
)
cdtPppPeerIpAddrPoolPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdtPppPeerIpAddrPoolPriority.setStatus("current")
_CdtPppPeerIpAddrPoolStatus_Type = RowStatus
_CdtPppPeerIpAddrPoolStatus_Object = MibTableColumn
cdtPppPeerIpAddrPoolStatus = _CdtPppPeerIpAddrPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 2, 1, 2),
    _CdtPppPeerIpAddrPoolStatus_Type()
)
cdtPppPeerIpAddrPoolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppPeerIpAddrPoolStatus.setStatus("current")


class _CdtPppPeerIpAddrPoolStorage_Type(StorageType):
    """Custom type cdtPppPeerIpAddrPoolStorage based on StorageType"""


_CdtPppPeerIpAddrPoolStorage_Object = MibTableColumn
cdtPppPeerIpAddrPoolStorage = _CdtPppPeerIpAddrPoolStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 2, 1, 3),
    _CdtPppPeerIpAddrPoolStorage_Type()
)
cdtPppPeerIpAddrPoolStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppPeerIpAddrPoolStorage.setStatus("current")


class _CdtPppPeerIpAddrPoolName_Type(SnmpAdminString):
    """Custom type cdtPppPeerIpAddrPoolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtPppPeerIpAddrPoolName_Type.__name__ = "SnmpAdminString"
_CdtPppPeerIpAddrPoolName_Object = MibTableColumn
cdtPppPeerIpAddrPoolName = _CdtPppPeerIpAddrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 3, 2, 1, 4),
    _CdtPppPeerIpAddrPoolName_Type()
)
cdtPppPeerIpAddrPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtPppPeerIpAddrPoolName.setStatus("current")
_CdtEthernet_ObjectIdentity = ObjectIdentity
cdtEthernet = _CdtEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 4)
)
_CdtEthernetTemplateTable_Object = MibTable
cdtEthernetTemplateTable = _CdtEthernetTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdtEthernetTemplateTable.setStatus("current")
_CdtEthernetTemplateEntry_Object = MibTableRow
cdtEthernetTemplateEntry = _CdtEthernetTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 4, 1, 1)
)
cdtEthernetTemplateEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateName"),
)
if mibBuilder.loadTexts:
    cdtEthernetTemplateEntry.setStatus("current")


class _CdtEthernetValid_Type(Bits):
    """Custom type cdtEthernetValid based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bridgeDomain", 0),
          ("ipv4PointToPoint", 2),
          ("macAddr", 3),
          ("pppoeEnable", 1))
    )

_CdtEthernetValid_Type.__name__ = "Bits"
_CdtEthernetValid_Object = MibTableColumn
cdtEthernetValid = _CdtEthernetValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 4, 1, 1, 1),
    _CdtEthernetValid_Type()
)
cdtEthernetValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtEthernetValid.setStatus("current")


class _CdtEthernetBridgeDomain_Type(SnmpAdminString):
    """Custom type cdtEthernetBridgeDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtEthernetBridgeDomain_Type.__name__ = "SnmpAdminString"
_CdtEthernetBridgeDomain_Object = MibTableColumn
cdtEthernetBridgeDomain = _CdtEthernetBridgeDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 4, 1, 1, 2),
    _CdtEthernetBridgeDomain_Type()
)
cdtEthernetBridgeDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtEthernetBridgeDomain.setStatus("current")


class _CdtEthernetPppoeEnable_Type(TruthValue):
    """Custom type cdtEthernetPppoeEnable based on TruthValue"""


_CdtEthernetPppoeEnable_Object = MibTableColumn
cdtEthernetPppoeEnable = _CdtEthernetPppoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 4, 1, 1, 3),
    _CdtEthernetPppoeEnable_Type()
)
cdtEthernetPppoeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtEthernetPppoeEnable.setStatus("current")


class _CdtEthernetIpv4PointToPoint_Type(TruthValue):
    """Custom type cdtEthernetIpv4PointToPoint based on TruthValue"""


_CdtEthernetIpv4PointToPoint_Object = MibTableColumn
cdtEthernetIpv4PointToPoint = _CdtEthernetIpv4PointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 4, 1, 1, 4),
    _CdtEthernetIpv4PointToPoint_Type()
)
cdtEthernetIpv4PointToPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtEthernetIpv4PointToPoint.setStatus("current")


class _CdtEthernetMacAddr_Type(MacAddress):
    """Custom type cdtEthernetMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_CdtEthernetMacAddr_Object = MibTableColumn
cdtEthernetMacAddr = _CdtEthernetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 4, 1, 1, 5),
    _CdtEthernetMacAddr_Type()
)
cdtEthernetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtEthernetMacAddr.setStatus("current")
_CdtIpSubscriber_ObjectIdentity = ObjectIdentity
cdtIpSubscriber = _CdtIpSubscriber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 5)
)
_CdtService_ObjectIdentity = ObjectIdentity
cdtService = _CdtService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 6)
)
_CdtSrvTemplateTable_Object = MibTable
cdtSrvTemplateTable = _CdtSrvTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cdtSrvTemplateTable.setStatus("current")
_CdtSrvTemplateEntry_Object = MibTableRow
cdtSrvTemplateEntry = _CdtSrvTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 6, 1, 1)
)
cdtSrvTemplateEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateName"),
)
if mibBuilder.loadTexts:
    cdtSrvTemplateEntry.setStatus("current")


class _CdtSrvValid_Type(Bits):
    """Custom type cdtSrvValid based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("multicast", 4),
          ("networkSrv", 0),
          ("sgSrvGroup", 2),
          ("sgSrvType", 3),
          ("vpdnGroup", 1))
    )

_CdtSrvValid_Type.__name__ = "Bits"
_CdtSrvValid_Object = MibTableColumn
cdtSrvValid = _CdtSrvValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 6, 1, 1, 1),
    _CdtSrvValid_Type()
)
cdtSrvValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtSrvValid.setStatus("current")


class _CdtSrvNetworkSrv_Type(Integer32):
    """Custom type cdtSrvNetworkSrv based on Integer32"""
    defaultValue = 2

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
        *(("local", 3),
          ("none", 2),
          ("other", 1),
          ("vpdn", 4))
    )


_CdtSrvNetworkSrv_Type.__name__ = "Integer32"
_CdtSrvNetworkSrv_Object = MibTableColumn
cdtSrvNetworkSrv = _CdtSrvNetworkSrv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 6, 1, 1, 2),
    _CdtSrvNetworkSrv_Type()
)
cdtSrvNetworkSrv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtSrvNetworkSrv.setStatus("current")


class _CdtSrvVpdnGroup_Type(SnmpAdminString):
    """Custom type cdtSrvVpdnGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtSrvVpdnGroup_Type.__name__ = "SnmpAdminString"
_CdtSrvVpdnGroup_Object = MibTableColumn
cdtSrvVpdnGroup = _CdtSrvVpdnGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 6, 1, 1, 3),
    _CdtSrvVpdnGroup_Type()
)
cdtSrvVpdnGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtSrvVpdnGroup.setStatus("current")


class _CdtSrvSgSrvGroup_Type(SnmpAdminString):
    """Custom type cdtSrvSgSrvGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdtSrvSgSrvGroup_Type.__name__ = "SnmpAdminString"
_CdtSrvSgSrvGroup_Object = MibTableColumn
cdtSrvSgSrvGroup = _CdtSrvSgSrvGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 6, 1, 1, 4),
    _CdtSrvSgSrvGroup_Type()
)
cdtSrvSgSrvGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtSrvSgSrvGroup.setStatus("current")


class _CdtSrvSgSrvType_Type(Integer32):
    """Custom type cdtSrvSgSrvType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_CdtSrvSgSrvType_Type.__name__ = "Integer32"
_CdtSrvSgSrvType_Object = MibTableColumn
cdtSrvSgSrvType = _CdtSrvSgSrvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 6, 1, 1, 5),
    _CdtSrvSgSrvType_Type()
)
cdtSrvSgSrvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtSrvSgSrvType.setStatus("current")


class _CdtSrvMulticast_Type(TruthValue):
    """Custom type cdtSrvMulticast based on TruthValue"""


_CdtSrvMulticast_Object = MibTableColumn
cdtSrvMulticast = _CdtSrvMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 6, 1, 1, 6),
    _CdtSrvMulticast_Type()
)
cdtSrvMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdtSrvMulticast.setStatus("current")
_CdtSubscriberGroup_ObjectIdentity = ObjectIdentity
cdtSubscriberGroup = _CdtSubscriberGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 1, 7)
)
_CiscoDynamicTemplateMIBConform_ObjectIdentity = ObjectIdentity
ciscoDynamicTemplateMIBConform = _CiscoDynamicTemplateMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2)
)
_CiscoDynamicTemplateMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDynamicTemplateMIBCompliances = _CiscoDynamicTemplateMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2, 1)
)
_CiscoDynamicTemplateMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDynamicTemplateMIBGroups = _CiscoDynamicTemplateMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2, 2)
)

# Managed Objects groups

cdtBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2, 2, 1)
)
cdtBaseGroup.setObjects(
      *(("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateStatus"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateStorage"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateType"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateSrc"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateUsageCount"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateTargetStatus"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateTargetStorage"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateAssociationPrecedence"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateUsageTargetType"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtTemplateUsageTargetId"))
)
if mibBuilder.loadTexts:
    cdtBaseGroup.setStatus("current")

cdtCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2, 2, 2)
)
cdtCommonGroup.setObjects(
      *(("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonValid"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonDescr"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonKeepaliveInt"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonKeepaliveRetries"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonVrf"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonAddrPool"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonIpv4AccessGroup"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonIpv4Unreachables"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonIpv6AccessGroup"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonIpv6Unreachables"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonSrvSubControl"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonSrvRedirect"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonSrvAcct"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonSrvQos"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtCommonSrvNetflow"))
)
if mibBuilder.loadTexts:
    cdtCommonGroup.setStatus("current")

cdtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2, 2, 3)
)
cdtIfGroup.setObjects(
      *(("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfValid"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfMtu"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfCdpEnable"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfFlowMonitor"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv4Unnumbered"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv4SubEnable"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv4Mtu"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv4TcpMssAdjust"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv4VerifyUniRpf"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv4VerifyUniRpfAcl"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv4VerifyUniRpfOpts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6Enable"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6SubEnable"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6TcpMssAdjust"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6VerifyUniRpf"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6VerifyUniRpfAcl"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6VerifyUniRpfOpts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdPrefix"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdPrefixLength"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdValidLife"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdPreferredLife"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdOpts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdDadAttempts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdNsInterval"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdReachableTime"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdRaIntervalUnits"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdRaIntervalMax"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdRaIntervalMin"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdRaLife"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtIfIpv6NdRouterPreference"))
)
if mibBuilder.loadTexts:
    cdtIfGroup.setStatus("current")

cdtPppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2, 2, 4)
)
cdtPppGroup.setObjects(
      *(("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppValid"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppAccounting"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppAuthentication"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppAuthenticationMethods"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppAuthorization"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppLoopbackIgnore"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMaxBadAuth"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMaxConfigure"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMaxFailure"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMaxTerminate"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppTimeoutAuthentication"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppTimeoutRetry"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppChapOpts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppChapHostname"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppChapPassword"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMsChapV1Opts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMsChapV1Hostname"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMsChapV1Password"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMsChapV2Opts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMsChapV2Hostname"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppMsChapV2Password"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPapOpts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPapUsername"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPapPassword"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppEapOpts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppEapIdentity"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppEapPassword"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppIpcpAddrOption"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppIpcpDnsOption"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppIpcpDnsPrimary"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppIpcpDnsSecondary"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppIpcpWinsOption"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppIpcpWinsPrimary"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppIpcpWinsSecondary"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppIpcpMaskOption"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppIpcpMask"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPeerDefIpAddrOpts"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPeerDefIpAddrSrc"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPeerDefIpAddr"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPeerIpAddrPoolStatus"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPeerIpAddrPoolStorage"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtPppPeerIpAddrPoolName"))
)
if mibBuilder.loadTexts:
    cdtPppGroup.setStatus("current")

cdtEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2, 2, 5)
)
cdtEthernetGroup.setObjects(
      *(("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtEthernetValid"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtEthernetBridgeDomain"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtEthernetPppoeEnable"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtEthernetIpv4PointToPoint"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtEthernetMacAddr"))
)
if mibBuilder.loadTexts:
    cdtEthernetGroup.setStatus("current")

cdtSrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2, 2, 6)
)
cdtSrvGroup.setObjects(
      *(("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtSrvValid"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtSrvNetworkSrv"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtSrvVpdnGroup"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtSrvSgSrvGroup"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtSrvSgSrvType"),
        ("CISCO-DYNAMIC-TEMPLATE-MIB", "cdtSrvMulticast"))
)
if mibBuilder.loadTexts:
    cdtSrvGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDynamicTemplateR1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 784, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDynamicTemplateR1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DYNAMIC-TEMPLATE-MIB",
    **{"ciscoDynamicTemplateMIB": ciscoDynamicTemplateMIB,
       "ciscoDynamicTemplateMIBNotifs": ciscoDynamicTemplateMIBNotifs,
       "ciscoDynamicTemplateMIBObjects": ciscoDynamicTemplateMIBObjects,
       "cdtBase": cdtBase,
       "cdtTemplateTable": cdtTemplateTable,
       "cdtTemplateEntry": cdtTemplateEntry,
       "cdtTemplateName": cdtTemplateName,
       "cdtTemplateStatus": cdtTemplateStatus,
       "cdtTemplateStorage": cdtTemplateStorage,
       "cdtTemplateType": cdtTemplateType,
       "cdtTemplateSrc": cdtTemplateSrc,
       "cdtTemplateUsageCount": cdtTemplateUsageCount,
       "cdtTemplateTargetTable": cdtTemplateTargetTable,
       "cdtTemplateTargetEntry": cdtTemplateTargetEntry,
       "cdtTemplateTargetType": cdtTemplateTargetType,
       "cdtTemplateTargetId": cdtTemplateTargetId,
       "cdtTemplateTargetStatus": cdtTemplateTargetStatus,
       "cdtTemplateTargetStorage": cdtTemplateTargetStorage,
       "cdtTemplateAssociationTable": cdtTemplateAssociationTable,
       "cdtTemplateAssociationEntry": cdtTemplateAssociationEntry,
       "cdtTemplateAssociationName": cdtTemplateAssociationName,
       "cdtTemplateAssociationPrecedence": cdtTemplateAssociationPrecedence,
       "cdtTemplateUsageTable": cdtTemplateUsageTable,
       "cdtTemplateUsageEntry": cdtTemplateUsageEntry,
       "cdtTemplateUsageTargetType": cdtTemplateUsageTargetType,
       "cdtTemplateUsageTargetId": cdtTemplateUsageTargetId,
       "cdtTemplateCommonTable": cdtTemplateCommonTable,
       "cdtTemplateCommonEntry": cdtTemplateCommonEntry,
       "cdtCommonValid": cdtCommonValid,
       "cdtCommonDescr": cdtCommonDescr,
       "cdtCommonKeepaliveInt": cdtCommonKeepaliveInt,
       "cdtCommonKeepaliveRetries": cdtCommonKeepaliveRetries,
       "cdtCommonVrf": cdtCommonVrf,
       "cdtCommonAddrPool": cdtCommonAddrPool,
       "cdtCommonIpv4AccessGroup": cdtCommonIpv4AccessGroup,
       "cdtCommonIpv4Unreachables": cdtCommonIpv4Unreachables,
       "cdtCommonIpv6AccessGroup": cdtCommonIpv6AccessGroup,
       "cdtCommonIpv6Unreachables": cdtCommonIpv6Unreachables,
       "cdtCommonSrvSubControl": cdtCommonSrvSubControl,
       "cdtCommonSrvRedirect": cdtCommonSrvRedirect,
       "cdtCommonSrvAcct": cdtCommonSrvAcct,
       "cdtCommonSrvQos": cdtCommonSrvQos,
       "cdtCommonSrvNetflow": cdtCommonSrvNetflow,
       "cdtCommonIf": cdtCommonIf,
       "cdtIfTemplateTable": cdtIfTemplateTable,
       "cdtIfTemplateEntry": cdtIfTemplateEntry,
       "cdtIfValid": cdtIfValid,
       "cdtIfMtu": cdtIfMtu,
       "cdtIfCdpEnable": cdtIfCdpEnable,
       "cdtIfFlowMonitor": cdtIfFlowMonitor,
       "cdtIfIpv4Unnumbered": cdtIfIpv4Unnumbered,
       "cdtIfIpv4SubEnable": cdtIfIpv4SubEnable,
       "cdtIfIpv4Mtu": cdtIfIpv4Mtu,
       "cdtIfIpv4TcpMssAdjust": cdtIfIpv4TcpMssAdjust,
       "cdtIfIpv4VerifyUniRpf": cdtIfIpv4VerifyUniRpf,
       "cdtIfIpv4VerifyUniRpfAcl": cdtIfIpv4VerifyUniRpfAcl,
       "cdtIfIpv4VerifyUniRpfOpts": cdtIfIpv4VerifyUniRpfOpts,
       "cdtIfIpv6Enable": cdtIfIpv6Enable,
       "cdtIfIpv6SubEnable": cdtIfIpv6SubEnable,
       "cdtIfIpv6TcpMssAdjust": cdtIfIpv6TcpMssAdjust,
       "cdtIfIpv6VerifyUniRpf": cdtIfIpv6VerifyUniRpf,
       "cdtIfIpv6VerifyUniRpfAcl": cdtIfIpv6VerifyUniRpfAcl,
       "cdtIfIpv6VerifyUniRpfOpts": cdtIfIpv6VerifyUniRpfOpts,
       "cdtIfIpv6NdPrefix": cdtIfIpv6NdPrefix,
       "cdtIfIpv6NdPrefixLength": cdtIfIpv6NdPrefixLength,
       "cdtIfIpv6NdValidLife": cdtIfIpv6NdValidLife,
       "cdtIfIpv6NdPreferredLife": cdtIfIpv6NdPreferredLife,
       "cdtIfIpv6NdOpts": cdtIfIpv6NdOpts,
       "cdtIfIpv6NdDadAttempts": cdtIfIpv6NdDadAttempts,
       "cdtIfIpv6NdNsInterval": cdtIfIpv6NdNsInterval,
       "cdtIfIpv6NdReachableTime": cdtIfIpv6NdReachableTime,
       "cdtIfIpv6NdRaIntervalUnits": cdtIfIpv6NdRaIntervalUnits,
       "cdtIfIpv6NdRaIntervalMax": cdtIfIpv6NdRaIntervalMax,
       "cdtIfIpv6NdRaIntervalMin": cdtIfIpv6NdRaIntervalMin,
       "cdtIfIpv6NdRaLife": cdtIfIpv6NdRaLife,
       "cdtIfIpv6NdRouterPreference": cdtIfIpv6NdRouterPreference,
       "cdtPpp": cdtPpp,
       "cdtPppTemplateTable": cdtPppTemplateTable,
       "cdtPppTemplateEntry": cdtPppTemplateEntry,
       "cdtPppValid": cdtPppValid,
       "cdtPppAccounting": cdtPppAccounting,
       "cdtPppAuthentication": cdtPppAuthentication,
       "cdtPppAuthenticationMethods": cdtPppAuthenticationMethods,
       "cdtPppAuthorization": cdtPppAuthorization,
       "cdtPppLoopbackIgnore": cdtPppLoopbackIgnore,
       "cdtPppMaxBadAuth": cdtPppMaxBadAuth,
       "cdtPppMaxConfigure": cdtPppMaxConfigure,
       "cdtPppMaxFailure": cdtPppMaxFailure,
       "cdtPppMaxTerminate": cdtPppMaxTerminate,
       "cdtPppTimeoutAuthentication": cdtPppTimeoutAuthentication,
       "cdtPppTimeoutRetry": cdtPppTimeoutRetry,
       "cdtPppChapOpts": cdtPppChapOpts,
       "cdtPppChapHostname": cdtPppChapHostname,
       "cdtPppChapPassword": cdtPppChapPassword,
       "cdtPppMsChapV1Opts": cdtPppMsChapV1Opts,
       "cdtPppMsChapV1Hostname": cdtPppMsChapV1Hostname,
       "cdtPppMsChapV1Password": cdtPppMsChapV1Password,
       "cdtPppMsChapV2Opts": cdtPppMsChapV2Opts,
       "cdtPppMsChapV2Hostname": cdtPppMsChapV2Hostname,
       "cdtPppMsChapV2Password": cdtPppMsChapV2Password,
       "cdtPppPapOpts": cdtPppPapOpts,
       "cdtPppPapUsername": cdtPppPapUsername,
       "cdtPppPapPassword": cdtPppPapPassword,
       "cdtPppEapOpts": cdtPppEapOpts,
       "cdtPppEapIdentity": cdtPppEapIdentity,
       "cdtPppEapPassword": cdtPppEapPassword,
       "cdtPppIpcpAddrOption": cdtPppIpcpAddrOption,
       "cdtPppIpcpDnsOption": cdtPppIpcpDnsOption,
       "cdtPppIpcpDnsPrimary": cdtPppIpcpDnsPrimary,
       "cdtPppIpcpDnsSecondary": cdtPppIpcpDnsSecondary,
       "cdtPppIpcpWinsOption": cdtPppIpcpWinsOption,
       "cdtPppIpcpWinsPrimary": cdtPppIpcpWinsPrimary,
       "cdtPppIpcpWinsSecondary": cdtPppIpcpWinsSecondary,
       "cdtPppIpcpMaskOption": cdtPppIpcpMaskOption,
       "cdtPppIpcpMask": cdtPppIpcpMask,
       "cdtPppPeerDefIpAddrOpts": cdtPppPeerDefIpAddrOpts,
       "cdtPppPeerDefIpAddrSrc": cdtPppPeerDefIpAddrSrc,
       "cdtPppPeerDefIpAddr": cdtPppPeerDefIpAddr,
       "cdtPppPeerIpAddrPoolTable": cdtPppPeerIpAddrPoolTable,
       "cdtPppPeerIpAddrPoolEntry": cdtPppPeerIpAddrPoolEntry,
       "cdtPppPeerIpAddrPoolPriority": cdtPppPeerIpAddrPoolPriority,
       "cdtPppPeerIpAddrPoolStatus": cdtPppPeerIpAddrPoolStatus,
       "cdtPppPeerIpAddrPoolStorage": cdtPppPeerIpAddrPoolStorage,
       "cdtPppPeerIpAddrPoolName": cdtPppPeerIpAddrPoolName,
       "cdtEthernet": cdtEthernet,
       "cdtEthernetTemplateTable": cdtEthernetTemplateTable,
       "cdtEthernetTemplateEntry": cdtEthernetTemplateEntry,
       "cdtEthernetValid": cdtEthernetValid,
       "cdtEthernetBridgeDomain": cdtEthernetBridgeDomain,
       "cdtEthernetPppoeEnable": cdtEthernetPppoeEnable,
       "cdtEthernetIpv4PointToPoint": cdtEthernetIpv4PointToPoint,
       "cdtEthernetMacAddr": cdtEthernetMacAddr,
       "cdtIpSubscriber": cdtIpSubscriber,
       "cdtService": cdtService,
       "cdtSrvTemplateTable": cdtSrvTemplateTable,
       "cdtSrvTemplateEntry": cdtSrvTemplateEntry,
       "cdtSrvValid": cdtSrvValid,
       "cdtSrvNetworkSrv": cdtSrvNetworkSrv,
       "cdtSrvVpdnGroup": cdtSrvVpdnGroup,
       "cdtSrvSgSrvGroup": cdtSrvSgSrvGroup,
       "cdtSrvSgSrvType": cdtSrvSgSrvType,
       "cdtSrvMulticast": cdtSrvMulticast,
       "cdtSubscriberGroup": cdtSubscriberGroup,
       "ciscoDynamicTemplateMIBConform": ciscoDynamicTemplateMIBConform,
       "ciscoDynamicTemplateMIBCompliances": ciscoDynamicTemplateMIBCompliances,
       "ciscoDynamicTemplateR1Compliance": ciscoDynamicTemplateR1Compliance,
       "ciscoDynamicTemplateMIBGroups": ciscoDynamicTemplateMIBGroups,
       "cdtBaseGroup": cdtBaseGroup,
       "cdtCommonGroup": cdtCommonGroup,
       "cdtIfGroup": cdtIfGroup,
       "cdtPppGroup": cdtPppGroup,
       "cdtEthernetGroup": cdtEthernetGroup,
       "cdtSrvGroup": cdtSrvGroup}
)
