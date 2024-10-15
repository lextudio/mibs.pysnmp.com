# SNMP MIB module (IEEE8021-PBBTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-PBBTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:32 2024
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

(ieee8021BridgeBaseComponentId,) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId")

(ieee8021QBridgeVlanCurrentComponentId,) = mibBuilder.importSymbols(
    "IEEE8021-Q-BRIDGE-MIB",
    "ieee8021QBridgeVlanCurrentComponentId")

(IEEE8021BridgePortNumber,
 IEEE8021PbbComponentIdentifier,
 IEEE8021PbbServiceIdentifier,
 IEEE8021PbbTeEsp,
 IEEE8021PbbTeProtectionGroupActiveRequests,
 IEEE8021PbbTeProtectionGroupConfigAdmin,
 IEEE8021PbbTeProtectionGroupId,
 IEEE8021PbbTeTSidId,
 IEEE8021VlanIndexOrWildcard,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021PbbServiceIdentifier",
    "IEEE8021PbbTeEsp",
    "IEEE8021PbbTeProtectionGroupActiveRequests",
    "IEEE8021PbbTeProtectionGroupConfigAdmin",
    "IEEE8021PbbTeProtectionGroupId",
    "IEEE8021PbbTeTSidId",
    "IEEE8021VlanIndexOrWildcard",
    "ieee802dot1mibs")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021PbbTeMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 10)
)
ieee8021PbbTeMib.setRevisions(
        ("2014-12-15 00:00",
         "2011-02-27 00:00",
         "2008-11-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021PbbTeNotifications_ObjectIdentity = ObjectIdentity
ieee8021PbbTeNotifications = _Ieee8021PbbTeNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 10, 0)
)
_Ieee8021PbbTeObjects_ObjectIdentity = ObjectIdentity
ieee8021PbbTeObjects = _Ieee8021PbbTeObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 10, 1)
)
_Ieee8021PbbTeProtectionGroupListTable_Object = MibTable
ieee8021PbbTeProtectionGroupListTable = _Ieee8021PbbTeProtectionGroupListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupListTable.setStatus("current")
_Ieee8021PbbTeProtectionGroupListEntry_Object = MibTableRow
ieee8021PbbTeProtectionGroupListEntry = _Ieee8021PbbTeProtectionGroupListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1)
)
ieee8021PbbTeProtectionGroupListEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListGroupId"),
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupListEntry.setStatus("current")
_Ieee8021PbbTeProtectionGroupListGroupId_Type = IEEE8021PbbTeProtectionGroupId
_Ieee8021PbbTeProtectionGroupListGroupId_Object = MibTableColumn
ieee8021PbbTeProtectionGroupListGroupId = _Ieee8021PbbTeProtectionGroupListGroupId_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 1),
    _Ieee8021PbbTeProtectionGroupListGroupId_Type()
)
ieee8021PbbTeProtectionGroupListGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupListGroupId.setStatus("current")
_Ieee8021PbbTeProtectionGroupListMD_Type = Unsigned32
_Ieee8021PbbTeProtectionGroupListMD_Object = MibTableColumn
ieee8021PbbTeProtectionGroupListMD = _Ieee8021PbbTeProtectionGroupListMD_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 2),
    _Ieee8021PbbTeProtectionGroupListMD_Type()
)
ieee8021PbbTeProtectionGroupListMD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupListMD.setStatus("current")
_Ieee8021PbbTeProtectionGroupListWorkingMA_Type = Unsigned32
_Ieee8021PbbTeProtectionGroupListWorkingMA_Object = MibTableColumn
ieee8021PbbTeProtectionGroupListWorkingMA = _Ieee8021PbbTeProtectionGroupListWorkingMA_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 3),
    _Ieee8021PbbTeProtectionGroupListWorkingMA_Type()
)
ieee8021PbbTeProtectionGroupListWorkingMA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupListWorkingMA.setStatus("current")
_Ieee8021PbbTeProtectionGroupListProtectionMA_Type = Unsigned32
_Ieee8021PbbTeProtectionGroupListProtectionMA_Object = MibTableColumn
ieee8021PbbTeProtectionGroupListProtectionMA = _Ieee8021PbbTeProtectionGroupListProtectionMA_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 4),
    _Ieee8021PbbTeProtectionGroupListProtectionMA_Type()
)
ieee8021PbbTeProtectionGroupListProtectionMA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupListProtectionMA.setStatus("current")


class _Ieee8021PbbTeProtectionGroupListStorageType_Type(StorageType):
    """Custom type ieee8021PbbTeProtectionGroupListStorageType based on StorageType"""


_Ieee8021PbbTeProtectionGroupListStorageType_Object = MibTableColumn
ieee8021PbbTeProtectionGroupListStorageType = _Ieee8021PbbTeProtectionGroupListStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 5),
    _Ieee8021PbbTeProtectionGroupListStorageType_Type()
)
ieee8021PbbTeProtectionGroupListStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupListStorageType.setStatus("current")
_Ieee8021PbbTeProtectionGroupListRowStatus_Type = RowStatus
_Ieee8021PbbTeProtectionGroupListRowStatus_Object = MibTableColumn
ieee8021PbbTeProtectionGroupListRowStatus = _Ieee8021PbbTeProtectionGroupListRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 1, 1, 6),
    _Ieee8021PbbTeProtectionGroupListRowStatus_Type()
)
ieee8021PbbTeProtectionGroupListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupListRowStatus.setStatus("current")
_Ieee8021PbbTeMASharedGroupTable_Object = MibTable
ieee8021PbbTeMASharedGroupTable = _Ieee8021PbbTeMASharedGroupTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021PbbTeMASharedGroupTable.setStatus("current")
_Ieee8021PbbTeMASharedGroupEntry_Object = MibTableRow
ieee8021PbbTeMASharedGroupEntry = _Ieee8021PbbTeMASharedGroupEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 2, 1)
)
ieee8021PbbTeMASharedGroupEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListGroupId"),
    (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeMASharedGroupSubIndex"),
)
if mibBuilder.loadTexts:
    ieee8021PbbTeMASharedGroupEntry.setStatus("current")


class _Ieee8021PbbTeMASharedGroupSubIndex_Type(Unsigned32):
    """Custom type ieee8021PbbTeMASharedGroupSubIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ieee8021PbbTeMASharedGroupSubIndex_Type.__name__ = "Unsigned32"
_Ieee8021PbbTeMASharedGroupSubIndex_Object = MibTableColumn
ieee8021PbbTeMASharedGroupSubIndex = _Ieee8021PbbTeMASharedGroupSubIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 2, 1, 1),
    _Ieee8021PbbTeMASharedGroupSubIndex_Type()
)
ieee8021PbbTeMASharedGroupSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbTeMASharedGroupSubIndex.setStatus("current")
_Ieee8021PbbTeMASharedGroupId_Type = IEEE8021PbbTeProtectionGroupId
_Ieee8021PbbTeMASharedGroupId_Object = MibTableColumn
ieee8021PbbTeMASharedGroupId = _Ieee8021PbbTeMASharedGroupId_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 2, 1, 2),
    _Ieee8021PbbTeMASharedGroupId_Type()
)
ieee8021PbbTeMASharedGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbTeMASharedGroupId.setStatus("current")
_Ieee8021PbbTeTesiTable_Object = MibTable
ieee8021PbbTeTesiTable = _Ieee8021PbbTeTesiTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021PbbTeTesiTable.setStatus("current")
_Ieee8021PbbTeTesiEntry_Object = MibTableRow
ieee8021PbbTeTesiEntry = _Ieee8021PbbTeTesiEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1)
)
ieee8021PbbTeTesiEntry.setIndexNames(
    (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiId"),
)
if mibBuilder.loadTexts:
    ieee8021PbbTeTesiEntry.setStatus("current")
_Ieee8021PbbTeTesiId_Type = IEEE8021PbbTeTSidId
_Ieee8021PbbTeTesiId_Object = MibTableColumn
ieee8021PbbTeTesiId = _Ieee8021PbbTeTesiId_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 1),
    _Ieee8021PbbTeTesiId_Type()
)
ieee8021PbbTeTesiId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbTeTesiId.setStatus("current")
_Ieee8021PbbTeTesiComponent_Type = IEEE8021PbbComponentIdentifier
_Ieee8021PbbTeTesiComponent_Object = MibTableColumn
ieee8021PbbTeTesiComponent = _Ieee8021PbbTeTesiComponent_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 2),
    _Ieee8021PbbTeTesiComponent_Type()
)
ieee8021PbbTeTesiComponent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeTesiComponent.setStatus("current")
_Ieee8021PbbTeTesiBridgePort_Type = IEEE8021BridgePortNumber
_Ieee8021PbbTeTesiBridgePort_Object = MibTableColumn
ieee8021PbbTeTesiBridgePort = _Ieee8021PbbTeTesiBridgePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 3),
    _Ieee8021PbbTeTesiBridgePort_Type()
)
ieee8021PbbTeTesiBridgePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeTesiBridgePort.setStatus("current")


class _Ieee8021PbbTeTesiStorageType_Type(StorageType):
    """Custom type ieee8021PbbTeTesiStorageType based on StorageType"""


_Ieee8021PbbTeTesiStorageType_Object = MibTableColumn
ieee8021PbbTeTesiStorageType = _Ieee8021PbbTeTesiStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 4),
    _Ieee8021PbbTeTesiStorageType_Type()
)
ieee8021PbbTeTesiStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeTesiStorageType.setStatus("current")
_Ieee8021PbbTeTesiRowStatus_Type = RowStatus
_Ieee8021PbbTeTesiRowStatus_Object = MibTableColumn
ieee8021PbbTeTesiRowStatus = _Ieee8021PbbTeTesiRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 3, 1, 5),
    _Ieee8021PbbTeTesiRowStatus_Type()
)
ieee8021PbbTeTesiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeTesiRowStatus.setStatus("current")
_Ieee8021PbbTeTeSiEspTable_Object = MibTable
ieee8021PbbTeTeSiEspTable = _Ieee8021PbbTeTeSiEspTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021PbbTeTeSiEspTable.setStatus("current")
_Ieee8021PbbTeTeSiEspEntry_Object = MibTableRow
ieee8021PbbTeTeSiEspEntry = _Ieee8021PbbTeTeSiEspEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1)
)
ieee8021PbbTeTeSiEspEntry.setIndexNames(
    (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiId"),
    (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeTeSiEspEspIndex"),
)
if mibBuilder.loadTexts:
    ieee8021PbbTeTeSiEspEntry.setStatus("current")


class _Ieee8021PbbTeTeSiEspEspIndex_Type(Unsigned32):
    """Custom type ieee8021PbbTeTeSiEspEspIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ieee8021PbbTeTeSiEspEspIndex_Type.__name__ = "Unsigned32"
_Ieee8021PbbTeTeSiEspEspIndex_Object = MibTableColumn
ieee8021PbbTeTeSiEspEspIndex = _Ieee8021PbbTeTeSiEspEspIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1, 1),
    _Ieee8021PbbTeTeSiEspEspIndex_Type()
)
ieee8021PbbTeTeSiEspEspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbTeTeSiEspEspIndex.setStatus("current")
_Ieee8021PbbTeTeSiEspEsp_Type = IEEE8021PbbTeEsp
_Ieee8021PbbTeTeSiEspEsp_Object = MibTableColumn
ieee8021PbbTeTeSiEspEsp = _Ieee8021PbbTeTeSiEspEsp_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1, 2),
    _Ieee8021PbbTeTeSiEspEsp_Type()
)
ieee8021PbbTeTeSiEspEsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeTeSiEspEsp.setStatus("current")


class _Ieee8021PbbTeTeSiEspStorageType_Type(StorageType):
    """Custom type ieee8021PbbTeTeSiEspStorageType based on StorageType"""


_Ieee8021PbbTeTeSiEspStorageType_Object = MibTableColumn
ieee8021PbbTeTeSiEspStorageType = _Ieee8021PbbTeTeSiEspStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1, 3),
    _Ieee8021PbbTeTeSiEspStorageType_Type()
)
ieee8021PbbTeTeSiEspStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeTeSiEspStorageType.setStatus("current")
_Ieee8021PbbTeTeSiEspRowStatus_Type = RowStatus
_Ieee8021PbbTeTeSiEspRowStatus_Object = MibTableColumn
ieee8021PbbTeTeSiEspRowStatus = _Ieee8021PbbTeTeSiEspRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 4, 1, 4),
    _Ieee8021PbbTeTeSiEspRowStatus_Type()
)
ieee8021PbbTeTeSiEspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeTeSiEspRowStatus.setStatus("current")
_Ieee8021PbbTeProtectionGroupConfigTable_Object = MibTable
ieee8021PbbTeProtectionGroupConfigTable = _Ieee8021PbbTeProtectionGroupConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigTable.setStatus("current")
_Ieee8021PbbTeProtectionGroupConfigEntry_Object = MibTableRow
ieee8021PbbTeProtectionGroupConfigEntry = _Ieee8021PbbTeProtectionGroupConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1)
)
ieee8021PbbTeProtectionGroupConfigEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListGroupId"),
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigEntry.setStatus("current")


class _Ieee8021PbbTeProtectionGroupConfigState_Type(Integer32):
    """Custom type ieee8021PbbTeProtectionGroupConfigState based on Integer32"""
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
        *(("protAdmin", 4),
          ("protectionPat", 2),
          ("waitToRestore", 3),
          ("workingPath", 1))
    )


_Ieee8021PbbTeProtectionGroupConfigState_Type.__name__ = "Integer32"
_Ieee8021PbbTeProtectionGroupConfigState_Object = MibTableColumn
ieee8021PbbTeProtectionGroupConfigState = _Ieee8021PbbTeProtectionGroupConfigState_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 1),
    _Ieee8021PbbTeProtectionGroupConfigState_Type()
)
ieee8021PbbTeProtectionGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigState.setStatus("current")
_Ieee8021PbbTeProtectionGroupConfigCommandStatus_Type = IEEE8021PbbTeProtectionGroupConfigAdmin
_Ieee8021PbbTeProtectionGroupConfigCommandStatus_Object = MibTableColumn
ieee8021PbbTeProtectionGroupConfigCommandStatus = _Ieee8021PbbTeProtectionGroupConfigCommandStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 2),
    _Ieee8021PbbTeProtectionGroupConfigCommandStatus_Type()
)
ieee8021PbbTeProtectionGroupConfigCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigCommandStatus.setStatus("current")
_Ieee8021PbbTeProtectionGroupConfigCommandLast_Type = IEEE8021PbbTeProtectionGroupConfigAdmin
_Ieee8021PbbTeProtectionGroupConfigCommandLast_Object = MibTableColumn
ieee8021PbbTeProtectionGroupConfigCommandLast = _Ieee8021PbbTeProtectionGroupConfigCommandLast_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 3),
    _Ieee8021PbbTeProtectionGroupConfigCommandLast_Type()
)
ieee8021PbbTeProtectionGroupConfigCommandLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigCommandLast.setStatus("current")


class _Ieee8021PbbTeProtectionGroupConfigCommandAdmin_Type(IEEE8021PbbTeProtectionGroupConfigAdmin):
    """Custom type ieee8021PbbTeProtectionGroupConfigCommandAdmin based on IEEE8021PbbTeProtectionGroupConfigAdmin"""


_Ieee8021PbbTeProtectionGroupConfigCommandAdmin_Object = MibTableColumn
ieee8021PbbTeProtectionGroupConfigCommandAdmin = _Ieee8021PbbTeProtectionGroupConfigCommandAdmin_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 4),
    _Ieee8021PbbTeProtectionGroupConfigCommandAdmin_Type()
)
ieee8021PbbTeProtectionGroupConfigCommandAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigCommandAdmin.setStatus("current")
_Ieee8021PbbTeProtectionGroupConfigActiveRequests_Type = IEEE8021PbbTeProtectionGroupActiveRequests
_Ieee8021PbbTeProtectionGroupConfigActiveRequests_Object = MibTableColumn
ieee8021PbbTeProtectionGroupConfigActiveRequests = _Ieee8021PbbTeProtectionGroupConfigActiveRequests_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 5),
    _Ieee8021PbbTeProtectionGroupConfigActiveRequests_Type()
)
ieee8021PbbTeProtectionGroupConfigActiveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigActiveRequests.setStatus("current")


class _Ieee8021PbbTeProtectionGroupConfigWTR_Type(Unsigned32):
    """Custom type ieee8021PbbTeProtectionGroupConfigWTR based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 12),
    )


_Ieee8021PbbTeProtectionGroupConfigWTR_Type.__name__ = "Unsigned32"
_Ieee8021PbbTeProtectionGroupConfigWTR_Object = MibTableColumn
ieee8021PbbTeProtectionGroupConfigWTR = _Ieee8021PbbTeProtectionGroupConfigWTR_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 6),
    _Ieee8021PbbTeProtectionGroupConfigWTR_Type()
)
ieee8021PbbTeProtectionGroupConfigWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigWTR.setStatus("current")


class _Ieee8021PbbTeProtectionGroupConfigHoldOff_Type(Unsigned32):
    """Custom type ieee8021PbbTeProtectionGroupConfigHoldOff based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ieee8021PbbTeProtectionGroupConfigHoldOff_Type.__name__ = "Unsigned32"
_Ieee8021PbbTeProtectionGroupConfigHoldOff_Object = MibTableColumn
ieee8021PbbTeProtectionGroupConfigHoldOff = _Ieee8021PbbTeProtectionGroupConfigHoldOff_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 7),
    _Ieee8021PbbTeProtectionGroupConfigHoldOff_Type()
)
ieee8021PbbTeProtectionGroupConfigHoldOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigHoldOff.setStatus("current")


class _Ieee8021PbbTeProtectionGroupConfigNotifyEnable_Type(TruthValue):
    """Custom type ieee8021PbbTeProtectionGroupConfigNotifyEnable based on TruthValue"""


_Ieee8021PbbTeProtectionGroupConfigNotifyEnable_Object = MibTableColumn
ieee8021PbbTeProtectionGroupConfigNotifyEnable = _Ieee8021PbbTeProtectionGroupConfigNotifyEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 8),
    _Ieee8021PbbTeProtectionGroupConfigNotifyEnable_Type()
)
ieee8021PbbTeProtectionGroupConfigNotifyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigNotifyEnable.setStatus("current")


class _Ieee8021PbbTeProtectionGroupConfigStorageType_Type(StorageType):
    """Custom type ieee8021PbbTeProtectionGroupConfigStorageType based on StorageType"""


_Ieee8021PbbTeProtectionGroupConfigStorageType_Object = MibTableColumn
ieee8021PbbTeProtectionGroupConfigStorageType = _Ieee8021PbbTeProtectionGroupConfigStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 5, 1, 9),
    _Ieee8021PbbTeProtectionGroupConfigStorageType_Type()
)
ieee8021PbbTeProtectionGroupConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupConfigStorageType.setStatus("current")
_Ieee8021PbbTeProtectionGroupISidTable_Object = MibTable
ieee8021PbbTeProtectionGroupISidTable = _Ieee8021PbbTeProtectionGroupISidTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupISidTable.setStatus("current")
_Ieee8021PbbTeProtectionGroupISidEntry_Object = MibTableRow
ieee8021PbbTeProtectionGroupISidEntry = _Ieee8021PbbTeProtectionGroupISidEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1)
)
ieee8021PbbTeProtectionGroupISidEntry.setIndexNames(
    (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidIndex"),
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupISidEntry.setStatus("current")
_Ieee8021PbbTeProtectionGroupISidIndex_Type = IEEE8021PbbServiceIdentifier
_Ieee8021PbbTeProtectionGroupISidIndex_Object = MibTableColumn
ieee8021PbbTeProtectionGroupISidIndex = _Ieee8021PbbTeProtectionGroupISidIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 1),
    _Ieee8021PbbTeProtectionGroupISidIndex_Type()
)
ieee8021PbbTeProtectionGroupISidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupISidIndex.setStatus("current")
_Ieee8021PbbTeProtectionGroupISidComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021PbbTeProtectionGroupISidComponentId_Object = MibTableColumn
ieee8021PbbTeProtectionGroupISidComponentId = _Ieee8021PbbTeProtectionGroupISidComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 2),
    _Ieee8021PbbTeProtectionGroupISidComponentId_Type()
)
ieee8021PbbTeProtectionGroupISidComponentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupISidComponentId.setStatus("current")
_Ieee8021PbbTeProtectionGroupISidGroupId_Type = IEEE8021PbbTeProtectionGroupId
_Ieee8021PbbTeProtectionGroupISidGroupId_Object = MibTableColumn
ieee8021PbbTeProtectionGroupISidGroupId = _Ieee8021PbbTeProtectionGroupISidGroupId_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 3),
    _Ieee8021PbbTeProtectionGroupISidGroupId_Type()
)
ieee8021PbbTeProtectionGroupISidGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupISidGroupId.setStatus("current")


class _Ieee8021PbbTeProtectionGroupISidStorageType_Type(StorageType):
    """Custom type ieee8021PbbTeProtectionGroupISidStorageType based on StorageType"""


_Ieee8021PbbTeProtectionGroupISidStorageType_Object = MibTableColumn
ieee8021PbbTeProtectionGroupISidStorageType = _Ieee8021PbbTeProtectionGroupISidStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 4),
    _Ieee8021PbbTeProtectionGroupISidStorageType_Type()
)
ieee8021PbbTeProtectionGroupISidStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupISidStorageType.setStatus("current")
_Ieee8021PbbTeProtectionGroupISidRowStatus_Type = RowStatus
_Ieee8021PbbTeProtectionGroupISidRowStatus_Object = MibTableColumn
ieee8021PbbTeProtectionGroupISidRowStatus = _Ieee8021PbbTeProtectionGroupISidRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 6, 1, 5),
    _Ieee8021PbbTeProtectionGroupISidRowStatus_Type()
)
ieee8021PbbTeProtectionGroupISidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupISidRowStatus.setStatus("current")
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastTable_Object = MibTable
ieee8021PbbTeBridgeStaticForwardAnyUnicastTable = _Ieee8021PbbTeBridgeStaticForwardAnyUnicastTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 7)
)
if mibBuilder.loadTexts:
    ieee8021PbbTeBridgeStaticForwardAnyUnicastTable.setStatus("current")
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry_Object = MibTableRow
ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry = _Ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1)
)
ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry.setIndexNames(
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanCurrentComponentId"),
    (0, "IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex"),
)
if mibBuilder.loadTexts:
    ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry.setStatus("current")
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex_Type = IEEE8021VlanIndexOrWildcard
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex_Object = MibTableColumn
ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex = _Ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 1),
    _Ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex_Type()
)
ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex.setStatus("current")
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts_Type = PortList
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts_Object = MibTableColumn
ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts = _Ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 2),
    _Ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts_Type()
)
ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts.setStatus("current")
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts_Type = PortList
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts_Object = MibTableColumn
ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts = _Ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 3),
    _Ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts_Type()
)
ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts.setStatus("current")


class _Ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType_Type(StorageType):
    """Custom type ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType based on StorageType"""


_Ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType_Object = MibTableColumn
ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType = _Ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 4),
    _Ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType_Type()
)
ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType.setStatus("current")
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus_Type = RowStatus
_Ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus_Object = MibTableColumn
ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus = _Ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 10, 1, 7, 1, 5),
    _Ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus_Type()
)
ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus.setStatus("current")
_Ieee8021PbbTeConformance_ObjectIdentity = ObjectIdentity
ieee8021PbbTeConformance = _Ieee8021PbbTeConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 10, 2)
)
_Ieee8021PbbTeCompliances_ObjectIdentity = ObjectIdentity
ieee8021PbbTeCompliances = _Ieee8021PbbTeCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 1)
)
_Ieee8021PbbTeGroups_ObjectIdentity = ObjectIdentity
ieee8021PbbTeGroups = _Ieee8021PbbTeGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2)
)

# Managed Objects groups

ieee8021PbbTeGroupListGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 1)
)
ieee8021PbbTeGroupListGroup.setObjects(
      *(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListMD"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListWorkingMA"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListProtectionMA"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListStorageType"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupListRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbbTeGroupListGroup.setStatus("current")

ieee8021PbbTeMASharedGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 2)
)
ieee8021PbbTeMASharedGroup.setObjects(
    ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeMASharedGroupId")
)
if mibBuilder.loadTexts:
    ieee8021PbbTeMASharedGroup.setStatus("current")

ieee8021PbbTeTesiGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 3)
)
ieee8021PbbTeTesiGroup.setObjects(
      *(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiComponent"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiBridgePort"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiStorageType"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTesiRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbbTeTesiGroup.setStatus("current")

ieee8021PbbTeSiEspGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 4)
)
ieee8021PbbTeSiEspGroup.setObjects(
      *(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTeSiEspEsp"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTeSiEspStorageType"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeTeSiEspRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbbTeSiEspGroup.setStatus("current")

ieee8021PbbTeProtectionConfigManGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 5)
)
ieee8021PbbTeProtectionConfigManGroup.setObjects(
      *(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigState"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandStatus"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandLast"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandAdmin"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigActiveRequests"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigNotifyEnable"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigStorageType"))
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionConfigManGroup.setStatus("current")

ieee8021PbbTeProtectionConfigOptGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 6)
)
ieee8021PbbTeProtectionConfigOptGroup.setObjects(
      *(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigWTR"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigHoldOff"))
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionConfigOptGroup.setStatus("current")

ieee8021PbbTeProtectionGroupISidGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 7)
)
ieee8021PbbTeProtectionGroupISidGroup.setObjects(
      *(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidComponentId"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidGroupId"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidStorageType"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupISidRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupISidGroup.setStatus("current")

ieee8021PbbTeFdbGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 8)
)
ieee8021PbbTeFdbGroup.setObjects(
      *(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbbTeFdbGroup.setStatus("current")


# Notification objects

ieee8021PbbTeProtectionGroupAdminFailure = NotificationType(
    (1, 3, 111, 2, 802, 1, 1, 10, 0, 1)
)
ieee8021PbbTeProtectionGroupAdminFailure.setObjects(
      *(("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigState"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandStatus"),
        ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupConfigCommandLast"))
)
if mibBuilder.loadTexts:
    ieee8021PbbTeProtectionGroupAdminFailure.setStatus(
        "current"
    )


# Notifications groups

ieee8021PbbTeNotificationsGroup = NotificationGroup(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 2, 9)
)
ieee8021PbbTeNotificationsGroup.setObjects(
    ("IEEE8021-PBBTE-MIB", "ieee8021PbbTeProtectionGroupAdminFailure")
)
if mibBuilder.loadTexts:
    ieee8021PbbTeNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ieee8021PbbTeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PbbTeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-PBBTE-MIB",
    **{"ieee8021PbbTeMib": ieee8021PbbTeMib,
       "ieee8021PbbTeNotifications": ieee8021PbbTeNotifications,
       "ieee8021PbbTeProtectionGroupAdminFailure": ieee8021PbbTeProtectionGroupAdminFailure,
       "ieee8021PbbTeObjects": ieee8021PbbTeObjects,
       "ieee8021PbbTeProtectionGroupListTable": ieee8021PbbTeProtectionGroupListTable,
       "ieee8021PbbTeProtectionGroupListEntry": ieee8021PbbTeProtectionGroupListEntry,
       "ieee8021PbbTeProtectionGroupListGroupId": ieee8021PbbTeProtectionGroupListGroupId,
       "ieee8021PbbTeProtectionGroupListMD": ieee8021PbbTeProtectionGroupListMD,
       "ieee8021PbbTeProtectionGroupListWorkingMA": ieee8021PbbTeProtectionGroupListWorkingMA,
       "ieee8021PbbTeProtectionGroupListProtectionMA": ieee8021PbbTeProtectionGroupListProtectionMA,
       "ieee8021PbbTeProtectionGroupListStorageType": ieee8021PbbTeProtectionGroupListStorageType,
       "ieee8021PbbTeProtectionGroupListRowStatus": ieee8021PbbTeProtectionGroupListRowStatus,
       "ieee8021PbbTeMASharedGroupTable": ieee8021PbbTeMASharedGroupTable,
       "ieee8021PbbTeMASharedGroupEntry": ieee8021PbbTeMASharedGroupEntry,
       "ieee8021PbbTeMASharedGroupSubIndex": ieee8021PbbTeMASharedGroupSubIndex,
       "ieee8021PbbTeMASharedGroupId": ieee8021PbbTeMASharedGroupId,
       "ieee8021PbbTeTesiTable": ieee8021PbbTeTesiTable,
       "ieee8021PbbTeTesiEntry": ieee8021PbbTeTesiEntry,
       "ieee8021PbbTeTesiId": ieee8021PbbTeTesiId,
       "ieee8021PbbTeTesiComponent": ieee8021PbbTeTesiComponent,
       "ieee8021PbbTeTesiBridgePort": ieee8021PbbTeTesiBridgePort,
       "ieee8021PbbTeTesiStorageType": ieee8021PbbTeTesiStorageType,
       "ieee8021PbbTeTesiRowStatus": ieee8021PbbTeTesiRowStatus,
       "ieee8021PbbTeTeSiEspTable": ieee8021PbbTeTeSiEspTable,
       "ieee8021PbbTeTeSiEspEntry": ieee8021PbbTeTeSiEspEntry,
       "ieee8021PbbTeTeSiEspEspIndex": ieee8021PbbTeTeSiEspEspIndex,
       "ieee8021PbbTeTeSiEspEsp": ieee8021PbbTeTeSiEspEsp,
       "ieee8021PbbTeTeSiEspStorageType": ieee8021PbbTeTeSiEspStorageType,
       "ieee8021PbbTeTeSiEspRowStatus": ieee8021PbbTeTeSiEspRowStatus,
       "ieee8021PbbTeProtectionGroupConfigTable": ieee8021PbbTeProtectionGroupConfigTable,
       "ieee8021PbbTeProtectionGroupConfigEntry": ieee8021PbbTeProtectionGroupConfigEntry,
       "ieee8021PbbTeProtectionGroupConfigState": ieee8021PbbTeProtectionGroupConfigState,
       "ieee8021PbbTeProtectionGroupConfigCommandStatus": ieee8021PbbTeProtectionGroupConfigCommandStatus,
       "ieee8021PbbTeProtectionGroupConfigCommandLast": ieee8021PbbTeProtectionGroupConfigCommandLast,
       "ieee8021PbbTeProtectionGroupConfigCommandAdmin": ieee8021PbbTeProtectionGroupConfigCommandAdmin,
       "ieee8021PbbTeProtectionGroupConfigActiveRequests": ieee8021PbbTeProtectionGroupConfigActiveRequests,
       "ieee8021PbbTeProtectionGroupConfigWTR": ieee8021PbbTeProtectionGroupConfigWTR,
       "ieee8021PbbTeProtectionGroupConfigHoldOff": ieee8021PbbTeProtectionGroupConfigHoldOff,
       "ieee8021PbbTeProtectionGroupConfigNotifyEnable": ieee8021PbbTeProtectionGroupConfigNotifyEnable,
       "ieee8021PbbTeProtectionGroupConfigStorageType": ieee8021PbbTeProtectionGroupConfigStorageType,
       "ieee8021PbbTeProtectionGroupISidTable": ieee8021PbbTeProtectionGroupISidTable,
       "ieee8021PbbTeProtectionGroupISidEntry": ieee8021PbbTeProtectionGroupISidEntry,
       "ieee8021PbbTeProtectionGroupISidIndex": ieee8021PbbTeProtectionGroupISidIndex,
       "ieee8021PbbTeProtectionGroupISidComponentId": ieee8021PbbTeProtectionGroupISidComponentId,
       "ieee8021PbbTeProtectionGroupISidGroupId": ieee8021PbbTeProtectionGroupISidGroupId,
       "ieee8021PbbTeProtectionGroupISidStorageType": ieee8021PbbTeProtectionGroupISidStorageType,
       "ieee8021PbbTeProtectionGroupISidRowStatus": ieee8021PbbTeProtectionGroupISidRowStatus,
       "ieee8021PbbTeBridgeStaticForwardAnyUnicastTable": ieee8021PbbTeBridgeStaticForwardAnyUnicastTable,
       "ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry": ieee8021PbbTeBridgeStaticForwardAnyUnicastEntry,
       "ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex": ieee8021PbbTeBridgeStaticForwardAnyUnicastVlanIndex,
       "ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts": ieee8021PbbTeBridgeStaticForwardAnyUnicastEgressPorts,
       "ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts": ieee8021PbbTeBridgeStaticForwardAnyUnicastForbiddenPorts,
       "ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType": ieee8021PbbTeBridgeStaticForwardAnyUnicastStorageType,
       "ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus": ieee8021PbbTeBridgeStaticForwardAnyUnicastRowStatus,
       "ieee8021PbbTeConformance": ieee8021PbbTeConformance,
       "ieee8021PbbTeCompliances": ieee8021PbbTeCompliances,
       "ieee8021PbbTeCompliance": ieee8021PbbTeCompliance,
       "ieee8021PbbTeGroups": ieee8021PbbTeGroups,
       "ieee8021PbbTeGroupListGroup": ieee8021PbbTeGroupListGroup,
       "ieee8021PbbTeMASharedGroup": ieee8021PbbTeMASharedGroup,
       "ieee8021PbbTeTesiGroup": ieee8021PbbTeTesiGroup,
       "ieee8021PbbTeSiEspGroup": ieee8021PbbTeSiEspGroup,
       "ieee8021PbbTeProtectionConfigManGroup": ieee8021PbbTeProtectionConfigManGroup,
       "ieee8021PbbTeProtectionConfigOptGroup": ieee8021PbbTeProtectionConfigOptGroup,
       "ieee8021PbbTeProtectionGroupISidGroup": ieee8021PbbTeProtectionGroupISidGroup,
       "ieee8021PbbTeFdbGroup": ieee8021PbbTeFdbGroup,
       "ieee8021PbbTeNotificationsGroup": ieee8021PbbTeNotificationsGroup}
)
