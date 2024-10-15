# SNMP MIB module (IEEE8021-CFM-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-CFM-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:15 2024
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

(Dot1agCfmConfigErrors,
 Dot1agCfmIdPermission,
 Dot1agCfmMDLevel,
 Dot1agCfmMDLevelOrNone,
 Dot1agCfmMepIdOrZero,
 Dot1agCfmMhfCreation,
 Dot1agCfmMpDirection,
 dot1agCfmCompliances,
 dot1agCfmConfigErrorList,
 dot1agCfmDefaultMd,
 dot1agCfmGroups,
 dot1agCfmMa,
 dot1agCfmMaIndex,
 dot1agCfmMaMepListRowStatus,
 dot1agCfmMaNetRowStatus,
 dot1agCfmMdGroup,
 dot1agCfmMdIndex,
 dot1agCfmMdRowStatus,
 dot1agCfmMepDbGroup,
 dot1agCfmMepGroup,
 dot1agCfmMepLbrBadMsdu,
 dot1agCfmMepRowStatus,
 dot1agCfmNotificationsGroup,
 dot1agCfmStack,
 dot1agCfmVlan,
 ieee8021CfmDefaultMdDefGroup,
 ieee8021CfmMaNetGroup,
 ieee8021CfmPbbTeExtensionGroup,
 ieee8021CfmPbbTeTrafficBitGroup) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmConfigErrors",
    "Dot1agCfmIdPermission",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMDLevelOrNone",
    "Dot1agCfmMepIdOrZero",
    "Dot1agCfmMhfCreation",
    "Dot1agCfmMpDirection",
    "dot1agCfmCompliances",
    "dot1agCfmConfigErrorList",
    "dot1agCfmDefaultMd",
    "dot1agCfmGroups",
    "dot1agCfmMa",
    "dot1agCfmMaIndex",
    "dot1agCfmMaMepListRowStatus",
    "dot1agCfmMaNetRowStatus",
    "dot1agCfmMdGroup",
    "dot1agCfmMdIndex",
    "dot1agCfmMdRowStatus",
    "dot1agCfmMepDbGroup",
    "dot1agCfmMepGroup",
    "dot1agCfmMepLbrBadMsdu",
    "dot1agCfmMepRowStatus",
    "dot1agCfmNotificationsGroup",
    "dot1agCfmStack",
    "dot1agCfmVlan",
    "ieee8021CfmDefaultMdDefGroup",
    "ieee8021CfmMaNetGroup",
    "ieee8021CfmPbbTeExtensionGroup",
    "ieee8021CfmPbbTeTrafficBitGroup")

(IEEE8021PbbComponentIdentifier,
 IEEE8021ServiceSelectorType,
 IEEE8021ServiceSelectorValue,
 IEEE8021ServiceSelectorValueOrNone,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021ServiceSelectorType",
    "IEEE8021ServiceSelectorValue",
    "IEEE8021ServiceSelectorValueOrNone",
    "ieee802dot1mibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021CfmV2Mib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 7)
)
ieee8021CfmV2Mib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2011-02-27 00:00",
         "2008-11-18 00:00",
         "2008-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021CfmStackTable_Object = MibTable
ieee8021CfmStackTable = _Ieee8021CfmStackTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021CfmStackTable.setStatus("current")
_Ieee8021CfmStackEntry_Object = MibTableRow
ieee8021CfmStackEntry = _Ieee8021CfmStackEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1)
)
ieee8021CfmStackEntry.setIndexNames(
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackifIndex"),
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackServiceSelectorType"),
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackServiceSelectorOrNone"),
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMdLevel"),
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmStackDirection"),
)
if mibBuilder.loadTexts:
    ieee8021CfmStackEntry.setStatus("current")
_Ieee8021CfmStackifIndex_Type = InterfaceIndex
_Ieee8021CfmStackifIndex_Object = MibTableColumn
ieee8021CfmStackifIndex = _Ieee8021CfmStackifIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 1),
    _Ieee8021CfmStackifIndex_Type()
)
ieee8021CfmStackifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmStackifIndex.setStatus("current")
_Ieee8021CfmStackServiceSelectorType_Type = IEEE8021ServiceSelectorType
_Ieee8021CfmStackServiceSelectorType_Object = MibTableColumn
ieee8021CfmStackServiceSelectorType = _Ieee8021CfmStackServiceSelectorType_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 2),
    _Ieee8021CfmStackServiceSelectorType_Type()
)
ieee8021CfmStackServiceSelectorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmStackServiceSelectorType.setStatus("current")
_Ieee8021CfmStackServiceSelectorOrNone_Type = IEEE8021ServiceSelectorValueOrNone
_Ieee8021CfmStackServiceSelectorOrNone_Object = MibTableColumn
ieee8021CfmStackServiceSelectorOrNone = _Ieee8021CfmStackServiceSelectorOrNone_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 3),
    _Ieee8021CfmStackServiceSelectorOrNone_Type()
)
ieee8021CfmStackServiceSelectorOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmStackServiceSelectorOrNone.setStatus("current")
_Ieee8021CfmStackMdLevel_Type = Dot1agCfmMDLevel
_Ieee8021CfmStackMdLevel_Object = MibTableColumn
ieee8021CfmStackMdLevel = _Ieee8021CfmStackMdLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 4),
    _Ieee8021CfmStackMdLevel_Type()
)
ieee8021CfmStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmStackMdLevel.setStatus("current")
_Ieee8021CfmStackDirection_Type = Dot1agCfmMpDirection
_Ieee8021CfmStackDirection_Object = MibTableColumn
ieee8021CfmStackDirection = _Ieee8021CfmStackDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 5),
    _Ieee8021CfmStackDirection_Type()
)
ieee8021CfmStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmStackDirection.setStatus("current")
_Ieee8021CfmStackMdIndex_Type = Unsigned32
_Ieee8021CfmStackMdIndex_Object = MibTableColumn
ieee8021CfmStackMdIndex = _Ieee8021CfmStackMdIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 6),
    _Ieee8021CfmStackMdIndex_Type()
)
ieee8021CfmStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CfmStackMdIndex.setStatus("current")
_Ieee8021CfmStackMaIndex_Type = Unsigned32
_Ieee8021CfmStackMaIndex_Object = MibTableColumn
ieee8021CfmStackMaIndex = _Ieee8021CfmStackMaIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 7),
    _Ieee8021CfmStackMaIndex_Type()
)
ieee8021CfmStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CfmStackMaIndex.setStatus("current")
_Ieee8021CfmStackMepId_Type = Dot1agCfmMepIdOrZero
_Ieee8021CfmStackMepId_Object = MibTableColumn
ieee8021CfmStackMepId = _Ieee8021CfmStackMepId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 8),
    _Ieee8021CfmStackMepId_Type()
)
ieee8021CfmStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CfmStackMepId.setStatus("current")
_Ieee8021CfmStackMacAddress_Type = MacAddress
_Ieee8021CfmStackMacAddress_Object = MibTableColumn
ieee8021CfmStackMacAddress = _Ieee8021CfmStackMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 2, 1, 9),
    _Ieee8021CfmStackMacAddress_Type()
)
ieee8021CfmStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CfmStackMacAddress.setStatus("current")
_Ieee8021CfmDefaultMdTable_Object = MibTable
ieee8021CfmDefaultMdTable = _Ieee8021CfmDefaultMdTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdTable.setStatus("current")
_Ieee8021CfmDefaultMdEntry_Object = MibTableRow
ieee8021CfmDefaultMdEntry = _Ieee8021CfmDefaultMdEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1)
)
ieee8021CfmDefaultMdEntry.setIndexNames(
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdComponentId"),
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdPrimarySelectorType"),
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdPrimarySelector"),
)
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdEntry.setStatus("current")
_Ieee8021CfmDefaultMdComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CfmDefaultMdComponentId_Object = MibTableColumn
ieee8021CfmDefaultMdComponentId = _Ieee8021CfmDefaultMdComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 1),
    _Ieee8021CfmDefaultMdComponentId_Type()
)
ieee8021CfmDefaultMdComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdComponentId.setStatus("current")
_Ieee8021CfmDefaultMdPrimarySelectorType_Type = IEEE8021ServiceSelectorType
_Ieee8021CfmDefaultMdPrimarySelectorType_Object = MibTableColumn
ieee8021CfmDefaultMdPrimarySelectorType = _Ieee8021CfmDefaultMdPrimarySelectorType_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 2),
    _Ieee8021CfmDefaultMdPrimarySelectorType_Type()
)
ieee8021CfmDefaultMdPrimarySelectorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdPrimarySelectorType.setStatus("current")
_Ieee8021CfmDefaultMdPrimarySelector_Type = IEEE8021ServiceSelectorValue
_Ieee8021CfmDefaultMdPrimarySelector_Object = MibTableColumn
ieee8021CfmDefaultMdPrimarySelector = _Ieee8021CfmDefaultMdPrimarySelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 3),
    _Ieee8021CfmDefaultMdPrimarySelector_Type()
)
ieee8021CfmDefaultMdPrimarySelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdPrimarySelector.setStatus("current")
_Ieee8021CfmDefaultMdStatus_Type = TruthValue
_Ieee8021CfmDefaultMdStatus_Object = MibTableColumn
ieee8021CfmDefaultMdStatus = _Ieee8021CfmDefaultMdStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 4),
    _Ieee8021CfmDefaultMdStatus_Type()
)
ieee8021CfmDefaultMdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdStatus.setStatus("current")


class _Ieee8021CfmDefaultMdLevel_Type(Dot1agCfmMDLevelOrNone):
    """Custom type ieee8021CfmDefaultMdLevel based on Dot1agCfmMDLevelOrNone"""
    defaultValue = -1


_Ieee8021CfmDefaultMdLevel_Object = MibTableColumn
ieee8021CfmDefaultMdLevel = _Ieee8021CfmDefaultMdLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 5),
    _Ieee8021CfmDefaultMdLevel_Type()
)
ieee8021CfmDefaultMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdLevel.setStatus("current")


class _Ieee8021CfmDefaultMdMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type ieee8021CfmDefaultMdMhfCreation based on Dot1agCfmMhfCreation"""


_Ieee8021CfmDefaultMdMhfCreation_Object = MibTableColumn
ieee8021CfmDefaultMdMhfCreation = _Ieee8021CfmDefaultMdMhfCreation_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 6),
    _Ieee8021CfmDefaultMdMhfCreation_Type()
)
ieee8021CfmDefaultMdMhfCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdMhfCreation.setStatus("current")


class _Ieee8021CfmDefaultMdIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type ieee8021CfmDefaultMdIdPermission based on Dot1agCfmIdPermission"""


_Ieee8021CfmDefaultMdIdPermission_Object = MibTableColumn
ieee8021CfmDefaultMdIdPermission = _Ieee8021CfmDefaultMdIdPermission_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 5, 1, 7),
    _Ieee8021CfmDefaultMdIdPermission_Type()
)
ieee8021CfmDefaultMdIdPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdIdPermission.setStatus("current")
_Ieee8021CfmVlanTable_Object = MibTable
ieee8021CfmVlanTable = _Ieee8021CfmVlanTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ieee8021CfmVlanTable.setStatus("current")
_Ieee8021CfmVlanEntry_Object = MibTableRow
ieee8021CfmVlanEntry = _Ieee8021CfmVlanEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1)
)
ieee8021CfmVlanEntry.setIndexNames(
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanComponentId"),
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanSelector"),
)
if mibBuilder.loadTexts:
    ieee8021CfmVlanEntry.setStatus("current")
_Ieee8021CfmVlanComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CfmVlanComponentId_Object = MibTableColumn
ieee8021CfmVlanComponentId = _Ieee8021CfmVlanComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1, 1),
    _Ieee8021CfmVlanComponentId_Type()
)
ieee8021CfmVlanComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmVlanComponentId.setStatus("current")
_Ieee8021CfmVlanSelector_Type = IEEE8021ServiceSelectorValue
_Ieee8021CfmVlanSelector_Object = MibTableColumn
ieee8021CfmVlanSelector = _Ieee8021CfmVlanSelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1, 3),
    _Ieee8021CfmVlanSelector_Type()
)
ieee8021CfmVlanSelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmVlanSelector.setStatus("current")
_Ieee8021CfmVlanPrimarySelector_Type = IEEE8021ServiceSelectorValue
_Ieee8021CfmVlanPrimarySelector_Object = MibTableColumn
ieee8021CfmVlanPrimarySelector = _Ieee8021CfmVlanPrimarySelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1, 5),
    _Ieee8021CfmVlanPrimarySelector_Type()
)
ieee8021CfmVlanPrimarySelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CfmVlanPrimarySelector.setStatus("current")
_Ieee8021CfmVlanRowStatus_Type = RowStatus
_Ieee8021CfmVlanRowStatus_Object = MibTableColumn
ieee8021CfmVlanRowStatus = _Ieee8021CfmVlanRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 2, 1, 6),
    _Ieee8021CfmVlanRowStatus_Type()
)
ieee8021CfmVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CfmVlanRowStatus.setStatus("current")
_Ieee8021CfmConfigErrorListTable_Object = MibTable
ieee8021CfmConfigErrorListTable = _Ieee8021CfmConfigErrorListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ieee8021CfmConfigErrorListTable.setStatus("current")
_Ieee8021CfmConfigErrorListEntry_Object = MibTableRow
ieee8021CfmConfigErrorListEntry = _Ieee8021CfmConfigErrorListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1)
)
ieee8021CfmConfigErrorListEntry.setIndexNames(
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListSelectorType"),
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListSelector"),
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021CfmConfigErrorListEntry.setStatus("current")
_Ieee8021CfmConfigErrorListSelectorType_Type = IEEE8021ServiceSelectorType
_Ieee8021CfmConfigErrorListSelectorType_Object = MibTableColumn
ieee8021CfmConfigErrorListSelectorType = _Ieee8021CfmConfigErrorListSelectorType_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1, 1),
    _Ieee8021CfmConfigErrorListSelectorType_Type()
)
ieee8021CfmConfigErrorListSelectorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmConfigErrorListSelectorType.setStatus("current")
_Ieee8021CfmConfigErrorListSelector_Type = IEEE8021ServiceSelectorValue
_Ieee8021CfmConfigErrorListSelector_Object = MibTableColumn
ieee8021CfmConfigErrorListSelector = _Ieee8021CfmConfigErrorListSelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1, 2),
    _Ieee8021CfmConfigErrorListSelector_Type()
)
ieee8021CfmConfigErrorListSelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmConfigErrorListSelector.setStatus("current")
_Ieee8021CfmConfigErrorListIfIndex_Type = InterfaceIndex
_Ieee8021CfmConfigErrorListIfIndex_Object = MibTableColumn
ieee8021CfmConfigErrorListIfIndex = _Ieee8021CfmConfigErrorListIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1, 3),
    _Ieee8021CfmConfigErrorListIfIndex_Type()
)
ieee8021CfmConfigErrorListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmConfigErrorListIfIndex.setStatus("current")
_Ieee8021CfmConfigErrorListErrorType_Type = Dot1agCfmConfigErrors
_Ieee8021CfmConfigErrorListErrorType_Object = MibTableColumn
ieee8021CfmConfigErrorListErrorType = _Ieee8021CfmConfigErrorListErrorType_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 2, 1, 4),
    _Ieee8021CfmConfigErrorListErrorType_Type()
)
ieee8021CfmConfigErrorListErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CfmConfigErrorListErrorType.setStatus("current")
_Ieee8021CfmMaCompTable_Object = MibTable
ieee8021CfmMaCompTable = _Ieee8021CfmMaCompTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4)
)
if mibBuilder.loadTexts:
    ieee8021CfmMaCompTable.setStatus("current")
_Ieee8021CfmMaCompEntry_Object = MibTableRow
ieee8021CfmMaCompEntry = _Ieee8021CfmMaCompEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1)
)
ieee8021CfmMaCompEntry.setIndexNames(
    (0, "IEEE8021-CFM-V2-MIB", "ieee8021CfmMaComponentId"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    ieee8021CfmMaCompEntry.setStatus("current")
_Ieee8021CfmMaComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CfmMaComponentId_Object = MibTableColumn
ieee8021CfmMaComponentId = _Ieee8021CfmMaComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 1),
    _Ieee8021CfmMaComponentId_Type()
)
ieee8021CfmMaComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CfmMaComponentId.setStatus("current")
_Ieee8021CfmMaCompPrimarySelectorType_Type = IEEE8021ServiceSelectorType
_Ieee8021CfmMaCompPrimarySelectorType_Object = MibTableColumn
ieee8021CfmMaCompPrimarySelectorType = _Ieee8021CfmMaCompPrimarySelectorType_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 2),
    _Ieee8021CfmMaCompPrimarySelectorType_Type()
)
ieee8021CfmMaCompPrimarySelectorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CfmMaCompPrimarySelectorType.setStatus("current")
_Ieee8021CfmMaCompPrimarySelectorOrNone_Type = IEEE8021ServiceSelectorValueOrNone
_Ieee8021CfmMaCompPrimarySelectorOrNone_Object = MibTableColumn
ieee8021CfmMaCompPrimarySelectorOrNone = _Ieee8021CfmMaCompPrimarySelectorOrNone_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 3),
    _Ieee8021CfmMaCompPrimarySelectorOrNone_Type()
)
ieee8021CfmMaCompPrimarySelectorOrNone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CfmMaCompPrimarySelectorOrNone.setStatus("current")


class _Ieee8021CfmMaCompMhfCreation_Type(Dot1agCfmMhfCreation):
    """Custom type ieee8021CfmMaCompMhfCreation based on Dot1agCfmMhfCreation"""


_Ieee8021CfmMaCompMhfCreation_Object = MibTableColumn
ieee8021CfmMaCompMhfCreation = _Ieee8021CfmMaCompMhfCreation_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 4),
    _Ieee8021CfmMaCompMhfCreation_Type()
)
ieee8021CfmMaCompMhfCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CfmMaCompMhfCreation.setStatus("current")


class _Ieee8021CfmMaCompIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type ieee8021CfmMaCompIdPermission based on Dot1agCfmIdPermission"""


_Ieee8021CfmMaCompIdPermission_Object = MibTableColumn
ieee8021CfmMaCompIdPermission = _Ieee8021CfmMaCompIdPermission_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 5),
    _Ieee8021CfmMaCompIdPermission_Type()
)
ieee8021CfmMaCompIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CfmMaCompIdPermission.setStatus("current")
_Ieee8021CfmMaCompNumberOfVids_Type = Unsigned32
_Ieee8021CfmMaCompNumberOfVids_Object = MibTableColumn
ieee8021CfmMaCompNumberOfVids = _Ieee8021CfmMaCompNumberOfVids_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 6),
    _Ieee8021CfmMaCompNumberOfVids_Type()
)
ieee8021CfmMaCompNumberOfVids.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CfmMaCompNumberOfVids.setStatus("current")
_Ieee8021CfmMaCompRowStatus_Type = RowStatus
_Ieee8021CfmMaCompRowStatus_Object = MibTableColumn
ieee8021CfmMaCompRowStatus = _Ieee8021CfmMaCompRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 4, 1, 7),
    _Ieee8021CfmMaCompRowStatus_Type()
)
ieee8021CfmMaCompRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CfmMaCompRowStatus.setStatus("current")

# Managed Objects groups

ieee8021CfmStackGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 12)
)
ieee8021CfmStackGroup.setObjects(
      *(("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMdIndex"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMaIndex"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMepId"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmStackMacAddress"))
)
if mibBuilder.loadTexts:
    ieee8021CfmStackGroup.setStatus("current")

ieee8021CfmMaGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 13)
)
ieee8021CfmMaGroup.setObjects(
      *(("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompPrimarySelectorType"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompPrimarySelectorOrNone"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompMhfCreation"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompIdPermission"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompRowStatus"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmMaCompNumberOfVids"))
)
if mibBuilder.loadTexts:
    ieee8021CfmMaGroup.setStatus("current")

ieee8021CfmDefaultMdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 14)
)
ieee8021CfmDefaultMdGroup.setObjects(
      *(("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdStatus"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdLevel"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdMhfCreation"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmDefaultMdIdPermission"))
)
if mibBuilder.loadTexts:
    ieee8021CfmDefaultMdGroup.setStatus("current")

ieee8021CfmVlanIdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 15)
)
ieee8021CfmVlanIdGroup.setObjects(
      *(("IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanPrimarySelector"),
        ("IEEE8021-CFM-V2-MIB", "ieee8021CfmVlanRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021CfmVlanIdGroup.setStatus("current")

ieee8021CfmConfigErrorListGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 16)
)
ieee8021CfmConfigErrorListGroup.setObjects(
    ("IEEE8021-CFM-V2-MIB", "ieee8021CfmConfigErrorListErrorType")
)
if mibBuilder.loadTexts:
    ieee8021CfmConfigErrorListGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021CfmComplianceV2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021CfmComplianceV2.setStatus(
        "current"
    )

dot1agCfmWithPbbTeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 8, 2, 1, 3)
)
if mibBuilder.loadTexts:
    dot1agCfmWithPbbTeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-CFM-V2-MIB",
    **{"ieee8021CfmV2Mib": ieee8021CfmV2Mib,
       "ieee8021CfmStackTable": ieee8021CfmStackTable,
       "ieee8021CfmStackEntry": ieee8021CfmStackEntry,
       "ieee8021CfmStackifIndex": ieee8021CfmStackifIndex,
       "ieee8021CfmStackServiceSelectorType": ieee8021CfmStackServiceSelectorType,
       "ieee8021CfmStackServiceSelectorOrNone": ieee8021CfmStackServiceSelectorOrNone,
       "ieee8021CfmStackMdLevel": ieee8021CfmStackMdLevel,
       "ieee8021CfmStackDirection": ieee8021CfmStackDirection,
       "ieee8021CfmStackMdIndex": ieee8021CfmStackMdIndex,
       "ieee8021CfmStackMaIndex": ieee8021CfmStackMaIndex,
       "ieee8021CfmStackMepId": ieee8021CfmStackMepId,
       "ieee8021CfmStackMacAddress": ieee8021CfmStackMacAddress,
       "ieee8021CfmDefaultMdTable": ieee8021CfmDefaultMdTable,
       "ieee8021CfmDefaultMdEntry": ieee8021CfmDefaultMdEntry,
       "ieee8021CfmDefaultMdComponentId": ieee8021CfmDefaultMdComponentId,
       "ieee8021CfmDefaultMdPrimarySelectorType": ieee8021CfmDefaultMdPrimarySelectorType,
       "ieee8021CfmDefaultMdPrimarySelector": ieee8021CfmDefaultMdPrimarySelector,
       "ieee8021CfmDefaultMdStatus": ieee8021CfmDefaultMdStatus,
       "ieee8021CfmDefaultMdLevel": ieee8021CfmDefaultMdLevel,
       "ieee8021CfmDefaultMdMhfCreation": ieee8021CfmDefaultMdMhfCreation,
       "ieee8021CfmDefaultMdIdPermission": ieee8021CfmDefaultMdIdPermission,
       "ieee8021CfmVlanTable": ieee8021CfmVlanTable,
       "ieee8021CfmVlanEntry": ieee8021CfmVlanEntry,
       "ieee8021CfmVlanComponentId": ieee8021CfmVlanComponentId,
       "ieee8021CfmVlanSelector": ieee8021CfmVlanSelector,
       "ieee8021CfmVlanPrimarySelector": ieee8021CfmVlanPrimarySelector,
       "ieee8021CfmVlanRowStatus": ieee8021CfmVlanRowStatus,
       "ieee8021CfmConfigErrorListTable": ieee8021CfmConfigErrorListTable,
       "ieee8021CfmConfigErrorListEntry": ieee8021CfmConfigErrorListEntry,
       "ieee8021CfmConfigErrorListSelectorType": ieee8021CfmConfigErrorListSelectorType,
       "ieee8021CfmConfigErrorListSelector": ieee8021CfmConfigErrorListSelector,
       "ieee8021CfmConfigErrorListIfIndex": ieee8021CfmConfigErrorListIfIndex,
       "ieee8021CfmConfigErrorListErrorType": ieee8021CfmConfigErrorListErrorType,
       "ieee8021CfmMaCompTable": ieee8021CfmMaCompTable,
       "ieee8021CfmMaCompEntry": ieee8021CfmMaCompEntry,
       "ieee8021CfmMaComponentId": ieee8021CfmMaComponentId,
       "ieee8021CfmMaCompPrimarySelectorType": ieee8021CfmMaCompPrimarySelectorType,
       "ieee8021CfmMaCompPrimarySelectorOrNone": ieee8021CfmMaCompPrimarySelectorOrNone,
       "ieee8021CfmMaCompMhfCreation": ieee8021CfmMaCompMhfCreation,
       "ieee8021CfmMaCompIdPermission": ieee8021CfmMaCompIdPermission,
       "ieee8021CfmMaCompNumberOfVids": ieee8021CfmMaCompNumberOfVids,
       "ieee8021CfmMaCompRowStatus": ieee8021CfmMaCompRowStatus,
       "ieee8021CfmComplianceV2": ieee8021CfmComplianceV2,
       "dot1agCfmWithPbbTeCompliance": dot1agCfmWithPbbTeCompliance,
       "ieee8021CfmStackGroup": ieee8021CfmStackGroup,
       "ieee8021CfmMaGroup": ieee8021CfmMaGroup,
       "ieee8021CfmDefaultMdGroup": ieee8021CfmDefaultMdGroup,
       "ieee8021CfmVlanIdGroup": ieee8021CfmVlanIdGroup,
       "ieee8021CfmConfigErrorListGroup": ieee8021CfmConfigErrorListGroup}
)
