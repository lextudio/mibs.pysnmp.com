# SNMP MIB module (IEEE8021-PB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-PB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:29 2024
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

(ieee8021BridgeBasePort,
 ieee8021BridgeBasePortComponentId) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBasePort",
    "ieee8021BridgeBasePortComponentId")

(IEEE8021BridgePortNumberOrZero,
 IEEE8021BridgePortType,
 IEEE8021PbbComponentIdentifierOrZero,
 IEEE8021PortAcceptableFrameTypes,
 IEEE8021PriorityValue,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumberOrZero",
    "IEEE8021BridgePortType",
    "IEEE8021PbbComponentIdentifierOrZero",
    "IEEE8021PortAcceptableFrameTypes",
    "IEEE8021PriorityValue",
    "ieee802dot1mibs")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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

ieee8021PbMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 5)
)
ieee8021PbMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2012-02-10 00:00",
         "2011-04-06 00:00",
         "2011-02-27 00:00",
         "2010-08-26 00:00",
         "2008-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021PbNotifications_ObjectIdentity = ObjectIdentity
ieee8021PbNotifications = _Ieee8021PbNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 5, 0)
)
_Ieee8021PbObjects_ObjectIdentity = ObjectIdentity
ieee8021PbObjects = _Ieee8021PbObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 5, 1)
)
_Ieee8021PbVidTranslationTable_Object = MibTable
ieee8021PbVidTranslationTable = _Ieee8021PbVidTranslationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PbVidTranslationTable.setStatus("deprecated")
_Ieee8021PbVidTranslationEntry_Object = MibTableRow
ieee8021PbVidTranslationEntry = _Ieee8021PbVidTranslationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 1, 1)
)
ieee8021PbVidTranslationEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-PB-MIB", "ieee8021PbVidTranslationLocalVid"),
)
if mibBuilder.loadTexts:
    ieee8021PbVidTranslationEntry.setStatus("deprecated")
_Ieee8021PbVidTranslationLocalVid_Type = VlanId
_Ieee8021PbVidTranslationLocalVid_Object = MibTableColumn
ieee8021PbVidTranslationLocalVid = _Ieee8021PbVidTranslationLocalVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 1, 1, 1),
    _Ieee8021PbVidTranslationLocalVid_Type()
)
ieee8021PbVidTranslationLocalVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbVidTranslationLocalVid.setStatus("deprecated")
_Ieee8021PbVidTranslationRelayVid_Type = VlanId
_Ieee8021PbVidTranslationRelayVid_Object = MibTableColumn
ieee8021PbVidTranslationRelayVid = _Ieee8021PbVidTranslationRelayVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 1, 1, 2),
    _Ieee8021PbVidTranslationRelayVid_Type()
)
ieee8021PbVidTranslationRelayVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbVidTranslationRelayVid.setStatus("deprecated")
_Ieee8021PbVidTranslationRowStatus_Type = RowStatus
_Ieee8021PbVidTranslationRowStatus_Object = MibTableColumn
ieee8021PbVidTranslationRowStatus = _Ieee8021PbVidTranslationRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 1, 1, 3),
    _Ieee8021PbVidTranslationRowStatus_Type()
)
ieee8021PbVidTranslationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbVidTranslationRowStatus.setStatus("deprecated")
_Ieee8021PbCVidRegistrationTable_Object = MibTable
ieee8021PbCVidRegistrationTable = _Ieee8021PbCVidRegistrationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021PbCVidRegistrationTable.setStatus("current")
_Ieee8021PbCVidRegistrationEntry_Object = MibTableRow
ieee8021PbCVidRegistrationEntry = _Ieee8021PbCVidRegistrationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1)
)
ieee8021PbCVidRegistrationEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationCVid"),
)
if mibBuilder.loadTexts:
    ieee8021PbCVidRegistrationEntry.setStatus("current")
_Ieee8021PbCVidRegistrationCVid_Type = VlanId
_Ieee8021PbCVidRegistrationCVid_Object = MibTableColumn
ieee8021PbCVidRegistrationCVid = _Ieee8021PbCVidRegistrationCVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 1),
    _Ieee8021PbCVidRegistrationCVid_Type()
)
ieee8021PbCVidRegistrationCVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbCVidRegistrationCVid.setStatus("current")
_Ieee8021PbCVidRegistrationSVid_Type = VlanId
_Ieee8021PbCVidRegistrationSVid_Object = MibTableColumn
ieee8021PbCVidRegistrationSVid = _Ieee8021PbCVidRegistrationSVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 2),
    _Ieee8021PbCVidRegistrationSVid_Type()
)
ieee8021PbCVidRegistrationSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbCVidRegistrationSVid.setStatus("current")


class _Ieee8021PbCVidRegistrationUntaggedPep_Type(TruthValue):
    """Custom type ieee8021PbCVidRegistrationUntaggedPep based on TruthValue"""


_Ieee8021PbCVidRegistrationUntaggedPep_Object = MibTableColumn
ieee8021PbCVidRegistrationUntaggedPep = _Ieee8021PbCVidRegistrationUntaggedPep_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 3),
    _Ieee8021PbCVidRegistrationUntaggedPep_Type()
)
ieee8021PbCVidRegistrationUntaggedPep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbCVidRegistrationUntaggedPep.setStatus("current")


class _Ieee8021PbCVidRegistrationUntaggedCep_Type(TruthValue):
    """Custom type ieee8021PbCVidRegistrationUntaggedCep based on TruthValue"""


_Ieee8021PbCVidRegistrationUntaggedCep_Object = MibTableColumn
ieee8021PbCVidRegistrationUntaggedCep = _Ieee8021PbCVidRegistrationUntaggedCep_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 4),
    _Ieee8021PbCVidRegistrationUntaggedCep_Type()
)
ieee8021PbCVidRegistrationUntaggedCep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbCVidRegistrationUntaggedCep.setStatus("current")
_Ieee8021PbCVidRegistrationRowStatus_Type = RowStatus
_Ieee8021PbCVidRegistrationRowStatus_Object = MibTableColumn
ieee8021PbCVidRegistrationRowStatus = _Ieee8021PbCVidRegistrationRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 2, 1, 5),
    _Ieee8021PbCVidRegistrationRowStatus_Type()
)
ieee8021PbCVidRegistrationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbCVidRegistrationRowStatus.setStatus("current")
_Ieee8021PbEdgePortTable_Object = MibTable
ieee8021PbEdgePortTable = _Ieee8021PbEdgePortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021PbEdgePortTable.setStatus("current")
_Ieee8021PbEdgePortEntry_Object = MibTableRow
ieee8021PbEdgePortEntry = _Ieee8021PbEdgePortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1)
)
ieee8021PbEdgePortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-PB-MIB", "ieee8021PbEdgePortSVid"),
)
if mibBuilder.loadTexts:
    ieee8021PbEdgePortEntry.setStatus("current")
_Ieee8021PbEdgePortSVid_Type = VlanId
_Ieee8021PbEdgePortSVid_Object = MibTableColumn
ieee8021PbEdgePortSVid = _Ieee8021PbEdgePortSVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 1),
    _Ieee8021PbEdgePortSVid_Type()
)
ieee8021PbEdgePortSVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbEdgePortSVid.setStatus("current")
_Ieee8021PbEdgePortPVID_Type = VlanId
_Ieee8021PbEdgePortPVID_Object = MibTableColumn
ieee8021PbEdgePortPVID = _Ieee8021PbEdgePortPVID_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 2),
    _Ieee8021PbEdgePortPVID_Type()
)
ieee8021PbEdgePortPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbEdgePortPVID.setStatus("current")
_Ieee8021PbEdgePortDefaultUserPriority_Type = IEEE8021PriorityValue
_Ieee8021PbEdgePortDefaultUserPriority_Object = MibTableColumn
ieee8021PbEdgePortDefaultUserPriority = _Ieee8021PbEdgePortDefaultUserPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 3),
    _Ieee8021PbEdgePortDefaultUserPriority_Type()
)
ieee8021PbEdgePortDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbEdgePortDefaultUserPriority.setStatus("current")


class _Ieee8021PbEdgePortAcceptableFrameTypes_Type(IEEE8021PortAcceptableFrameTypes):
    """Custom type ieee8021PbEdgePortAcceptableFrameTypes based on IEEE8021PortAcceptableFrameTypes"""


_Ieee8021PbEdgePortAcceptableFrameTypes_Object = MibTableColumn
ieee8021PbEdgePortAcceptableFrameTypes = _Ieee8021PbEdgePortAcceptableFrameTypes_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 4),
    _Ieee8021PbEdgePortAcceptableFrameTypes_Type()
)
ieee8021PbEdgePortAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbEdgePortAcceptableFrameTypes.setStatus("current")


class _Ieee8021PbEdgePortEnableIngressFiltering_Type(TruthValue):
    """Custom type ieee8021PbEdgePortEnableIngressFiltering based on TruthValue"""


_Ieee8021PbEdgePortEnableIngressFiltering_Object = MibTableColumn
ieee8021PbEdgePortEnableIngressFiltering = _Ieee8021PbEdgePortEnableIngressFiltering_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 3, 1, 5),
    _Ieee8021PbEdgePortEnableIngressFiltering_Type()
)
ieee8021PbEdgePortEnableIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbEdgePortEnableIngressFiltering.setStatus("current")
_Ieee8021PbServicePriorityRegenerationTable_Object = MibTable
ieee8021PbServicePriorityRegenerationTable = _Ieee8021PbServicePriorityRegenerationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021PbServicePriorityRegenerationTable.setStatus("current")
_Ieee8021PbServicePriorityRegenerationEntry_Object = MibTableRow
ieee8021PbServicePriorityRegenerationEntry = _Ieee8021PbServicePriorityRegenerationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 4, 1)
)
ieee8021PbServicePriorityRegenerationEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-PB-MIB", "ieee8021PbServicePriorityRegenerationSVid"),
    (0, "IEEE8021-PB-MIB", "ieee8021PbServicePriorityRegenerationReceivedPriority"),
)
if mibBuilder.loadTexts:
    ieee8021PbServicePriorityRegenerationEntry.setStatus("current")
_Ieee8021PbServicePriorityRegenerationSVid_Type = VlanId
_Ieee8021PbServicePriorityRegenerationSVid_Object = MibTableColumn
ieee8021PbServicePriorityRegenerationSVid = _Ieee8021PbServicePriorityRegenerationSVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 4, 1, 1),
    _Ieee8021PbServicePriorityRegenerationSVid_Type()
)
ieee8021PbServicePriorityRegenerationSVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbServicePriorityRegenerationSVid.setStatus("current")
_Ieee8021PbServicePriorityRegenerationReceivedPriority_Type = IEEE8021PriorityValue
_Ieee8021PbServicePriorityRegenerationReceivedPriority_Object = MibTableColumn
ieee8021PbServicePriorityRegenerationReceivedPriority = _Ieee8021PbServicePriorityRegenerationReceivedPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 4, 1, 2),
    _Ieee8021PbServicePriorityRegenerationReceivedPriority_Type()
)
ieee8021PbServicePriorityRegenerationReceivedPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbServicePriorityRegenerationReceivedPriority.setStatus("current")
_Ieee8021PbServicePriorityRegenerationRegeneratedPriority_Type = IEEE8021PriorityValue
_Ieee8021PbServicePriorityRegenerationRegeneratedPriority_Object = MibTableColumn
ieee8021PbServicePriorityRegenerationRegeneratedPriority = _Ieee8021PbServicePriorityRegenerationRegeneratedPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 4, 1, 3),
    _Ieee8021PbServicePriorityRegenerationRegeneratedPriority_Type()
)
ieee8021PbServicePriorityRegenerationRegeneratedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbServicePriorityRegenerationRegeneratedPriority.setStatus("current")
_Ieee8021PbCnpTable_Object = MibTable
ieee8021PbCnpTable = _Ieee8021PbCnpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021PbCnpTable.setStatus("current")
_Ieee8021PbCnpEntry_Object = MibTableRow
ieee8021PbCnpEntry = _Ieee8021PbCnpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 5, 1)
)
ieee8021PbCnpEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021PbCnpEntry.setStatus("current")
_Ieee8021PbCnpCComponentId_Type = IEEE8021PbbComponentIdentifierOrZero
_Ieee8021PbCnpCComponentId_Object = MibTableColumn
ieee8021PbCnpCComponentId = _Ieee8021PbCnpCComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 5, 1, 1),
    _Ieee8021PbCnpCComponentId_Type()
)
ieee8021PbCnpCComponentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbCnpCComponentId.setStatus("current")
_Ieee8021PbCnpSVid_Type = VlanIdOrNone
_Ieee8021PbCnpSVid_Object = MibTableColumn
ieee8021PbCnpSVid = _Ieee8021PbCnpSVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 5, 1, 2),
    _Ieee8021PbCnpSVid_Type()
)
ieee8021PbCnpSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbCnpSVid.setStatus("current")
_Ieee8021PbCnpRowStatus_Type = RowStatus
_Ieee8021PbCnpRowStatus_Object = MibTableColumn
ieee8021PbCnpRowStatus = _Ieee8021PbCnpRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 5, 1, 3),
    _Ieee8021PbCnpRowStatus_Type()
)
ieee8021PbCnpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbCnpRowStatus.setStatus("current")
_Ieee8021PbPnpTable_Object = MibTable
ieee8021PbPnpTable = _Ieee8021PbPnpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021PbPnpTable.setStatus("current")
_Ieee8021PbPnpEntry_Object = MibTableRow
ieee8021PbPnpEntry = _Ieee8021PbPnpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 6, 1)
)
ieee8021PbPnpEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021PbPnpEntry.setStatus("current")
_Ieee8021PbPnpRowStatus_Type = RowStatus
_Ieee8021PbPnpRowStatus_Object = MibTableColumn
ieee8021PbPnpRowStatus = _Ieee8021PbPnpRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 6, 1, 1),
    _Ieee8021PbPnpRowStatus_Type()
)
ieee8021PbPnpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbPnpRowStatus.setStatus("current")
_Ieee8021PbCepTable_Object = MibTable
ieee8021PbCepTable = _Ieee8021PbCepTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    ieee8021PbCepTable.setStatus("current")
_Ieee8021PbCepEntry_Object = MibTableRow
ieee8021PbCepEntry = _Ieee8021PbCepEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 7, 1)
)
ieee8021PbCepEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021PbCepEntry.setStatus("current")
_Ieee8021PbCepCComponentId_Type = IEEE8021PbbComponentIdentifierOrZero
_Ieee8021PbCepCComponentId_Object = MibTableColumn
ieee8021PbCepCComponentId = _Ieee8021PbCepCComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 7, 1, 1),
    _Ieee8021PbCepCComponentId_Type()
)
ieee8021PbCepCComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbCepCComponentId.setStatus("current")
_Ieee8021PbCepCepPortNumber_Type = IEEE8021BridgePortNumberOrZero
_Ieee8021PbCepCepPortNumber_Object = MibTableColumn
ieee8021PbCepCepPortNumber = _Ieee8021PbCepCepPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 7, 1, 2),
    _Ieee8021PbCepCepPortNumber_Type()
)
ieee8021PbCepCepPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbCepCepPortNumber.setStatus("current")
_Ieee8021PbCepRowStatus_Type = RowStatus
_Ieee8021PbCepRowStatus_Object = MibTableColumn
ieee8021PbCepRowStatus = _Ieee8021PbCepRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 7, 1, 3),
    _Ieee8021PbCepRowStatus_Type()
)
ieee8021PbCepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbCepRowStatus.setStatus("current")
_Ieee8021PbRcapTable_Object = MibTable
ieee8021PbRcapTable = _Ieee8021PbRcapTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 8)
)
if mibBuilder.loadTexts:
    ieee8021PbRcapTable.setStatus("current")
_Ieee8021PbRcapEntry_Object = MibTableRow
ieee8021PbRcapEntry = _Ieee8021PbRcapEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 8, 1)
)
ieee8021PbRcapEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021PbRcapEntry.setStatus("current")
_Ieee8021PbRcapSComponentId_Type = IEEE8021PbbComponentIdentifierOrZero
_Ieee8021PbRcapSComponentId_Object = MibTableColumn
ieee8021PbRcapSComponentId = _Ieee8021PbRcapSComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 8, 1, 1),
    _Ieee8021PbRcapSComponentId_Type()
)
ieee8021PbRcapSComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbRcapSComponentId.setStatus("current")
_Ieee8021PbRcapRcapPortNumber_Type = IEEE8021BridgePortNumberOrZero
_Ieee8021PbRcapRcapPortNumber_Object = MibTableColumn
ieee8021PbRcapRcapPortNumber = _Ieee8021PbRcapRcapPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 8, 1, 2),
    _Ieee8021PbRcapRcapPortNumber_Type()
)
ieee8021PbRcapRcapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbRcapRcapPortNumber.setStatus("current")
_Ieee8021PbRcapRowStatus_Type = RowStatus
_Ieee8021PbRcapRowStatus_Object = MibTableColumn
ieee8021PbRcapRowStatus = _Ieee8021PbRcapRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 8, 1, 3),
    _Ieee8021PbRcapRowStatus_Type()
)
ieee8021PbRcapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbRcapRowStatus.setStatus("current")
_Ieee8021PbInternalInterfaceTable_Object = MibTable
ieee8021PbInternalInterfaceTable = _Ieee8021PbInternalInterfaceTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 9)
)
if mibBuilder.loadTexts:
    ieee8021PbInternalInterfaceTable.setStatus("current")
_Ieee8021PbIiEntry_Object = MibTableRow
ieee8021PbIiEntry = _Ieee8021PbIiEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1)
)
ieee8021PbIiEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-PB-MIB", "ieee8021PbIiExternalSVid"),
)
if mibBuilder.loadTexts:
    ieee8021PbIiEntry.setStatus("current")
_Ieee8021PbIiExternalSVid_Type = VlanId
_Ieee8021PbIiExternalSVid_Object = MibTableColumn
ieee8021PbIiExternalSVid = _Ieee8021PbIiExternalSVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 1),
    _Ieee8021PbIiExternalSVid_Type()
)
ieee8021PbIiExternalSVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbIiExternalSVid.setStatus("current")
_Ieee8021PbIiInternalPortNumber_Type = IEEE8021BridgePortNumberOrZero
_Ieee8021PbIiInternalPortNumber_Object = MibTableColumn
ieee8021PbIiInternalPortNumber = _Ieee8021PbIiInternalPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 2),
    _Ieee8021PbIiInternalPortNumber_Type()
)
ieee8021PbIiInternalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbIiInternalPortNumber.setStatus("current")
_Ieee8021PbIiInternalPortType_Type = IEEE8021BridgePortType
_Ieee8021PbIiInternalPortType_Object = MibTableColumn
ieee8021PbIiInternalPortType = _Ieee8021PbIiInternalPortType_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 3),
    _Ieee8021PbIiInternalPortType_Type()
)
ieee8021PbIiInternalPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbIiInternalPortType.setStatus("current")
_Ieee8021PbIiInternalSVid_Type = VlanIdOrNone
_Ieee8021PbIiInternalSVid_Object = MibTableColumn
ieee8021PbIiInternalSVid = _Ieee8021PbIiInternalSVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 4),
    _Ieee8021PbIiInternalSVid_Type()
)
ieee8021PbIiInternalSVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbIiInternalSVid.setStatus("current")
_Ieee8021PbIiRowStatus_Type = RowStatus
_Ieee8021PbIiRowStatus_Object = MibTableColumn
ieee8021PbIiRowStatus = _Ieee8021PbIiRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 5, 1, 9, 1, 5),
    _Ieee8021PbIiRowStatus_Type()
)
ieee8021PbIiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbIiRowStatus.setStatus("current")
_Ieee8021PbConformance_ObjectIdentity = ObjectIdentity
ieee8021PbConformance = _Ieee8021PbConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 5, 2)
)
_Ieee8021PbGroups_ObjectIdentity = ObjectIdentity
ieee8021PbGroups = _Ieee8021PbGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1)
)
_Ieee8021PbCompliances_ObjectIdentity = ObjectIdentity
ieee8021PbCompliances = _Ieee8021PbCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 2)
)

# Managed Objects groups

ieee8021PbVidTranslationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 1)
)
ieee8021PbVidTranslationGroup.setObjects(
      *(("IEEE8021-PB-MIB", "ieee8021PbVidTranslationRelayVid"),
        ("IEEE8021-PB-MIB", "ieee8021PbVidTranslationRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbVidTranslationGroup.setStatus("deprecated")

ieee8021PbCVidRegistrationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 2)
)
ieee8021PbCVidRegistrationGroup.setObjects(
      *(("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationSVid"),
        ("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationUntaggedPep"),
        ("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationUntaggedCep"),
        ("IEEE8021-PB-MIB", "ieee8021PbCVidRegistrationRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbCVidRegistrationGroup.setStatus("current")

ieee8021PbEdgePortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 3)
)
ieee8021PbEdgePortGroup.setObjects(
      *(("IEEE8021-PB-MIB", "ieee8021PbEdgePortPVID"),
        ("IEEE8021-PB-MIB", "ieee8021PbEdgePortDefaultUserPriority"),
        ("IEEE8021-PB-MIB", "ieee8021PbEdgePortAcceptableFrameTypes"),
        ("IEEE8021-PB-MIB", "ieee8021PbEdgePortEnableIngressFiltering"))
)
if mibBuilder.loadTexts:
    ieee8021PbEdgePortGroup.setStatus("current")

ieee8021PbServicePriorityRegenerationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 4)
)
ieee8021PbServicePriorityRegenerationGroup.setObjects(
    ("IEEE8021-PB-MIB", "ieee8021PbServicePriorityRegenerationRegeneratedPriority")
)
if mibBuilder.loadTexts:
    ieee8021PbServicePriorityRegenerationGroup.setStatus("current")

ieee8021PbDynamicCnpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 5)
)
ieee8021PbDynamicCnpGroup.setObjects(
      *(("IEEE8021-PB-MIB", "ieee8021PbCnpCComponentId"),
        ("IEEE8021-PB-MIB", "ieee8021PbCnpSVid"),
        ("IEEE8021-PB-MIB", "ieee8021PbCnpRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbDynamicCnpGroup.setStatus("current")

ieee8021PbDynamicPnpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 6)
)
ieee8021PbDynamicPnpGroup.setObjects(
    ("IEEE8021-PB-MIB", "ieee8021PbPnpRowStatus")
)
if mibBuilder.loadTexts:
    ieee8021PbDynamicPnpGroup.setStatus("current")

ieee8021PbDynamicCepGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 7)
)
ieee8021PbDynamicCepGroup.setObjects(
      *(("IEEE8021-PB-MIB", "ieee8021PbCepCComponentId"),
        ("IEEE8021-PB-MIB", "ieee8021PbCepCepPortNumber"),
        ("IEEE8021-PB-MIB", "ieee8021PbCepRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbDynamicCepGroup.setStatus("current")

ieee8021PbDynamicRcapGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 8)
)
ieee8021PbDynamicRcapGroup.setObjects(
      *(("IEEE8021-PB-MIB", "ieee8021PbRcapSComponentId"),
        ("IEEE8021-PB-MIB", "ieee8021PbRcapRcapPortNumber"),
        ("IEEE8021-PB-MIB", "ieee8021PbCepRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbDynamicRcapGroup.setStatus("deprecated")

ieee8021PbInternalInterfaceGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 9)
)
ieee8021PbInternalInterfaceGroup.setObjects(
      *(("IEEE8021-PB-MIB", "ieee8021PbIiInternalPortNumber"),
        ("IEEE8021-PB-MIB", "ieee8021PbIiInternalPortType"),
        ("IEEE8021-PB-MIB", "ieee8021PbIiInternalSVid"),
        ("IEEE8021-PB-MIB", "ieee8021PbIiRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbInternalInterfaceGroup.setStatus("current")

ieee8021PbDynamicRcapV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 1, 10)
)
ieee8021PbDynamicRcapV2Group.setObjects(
      *(("IEEE8021-PB-MIB", "ieee8021PbRcapSComponentId"),
        ("IEEE8021-PB-MIB", "ieee8021PbRcapRcapPortNumber"),
        ("IEEE8021-PB-MIB", "ieee8021PbRcapRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbDynamicRcapV2Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021PbCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021PbCompliance.setStatus(
        "deprecated"
    )

ieee8021PbComplianceV2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 5, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021PbComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-PB-MIB",
    **{"ieee8021PbMib": ieee8021PbMib,
       "ieee8021PbNotifications": ieee8021PbNotifications,
       "ieee8021PbObjects": ieee8021PbObjects,
       "ieee8021PbVidTranslationTable": ieee8021PbVidTranslationTable,
       "ieee8021PbVidTranslationEntry": ieee8021PbVidTranslationEntry,
       "ieee8021PbVidTranslationLocalVid": ieee8021PbVidTranslationLocalVid,
       "ieee8021PbVidTranslationRelayVid": ieee8021PbVidTranslationRelayVid,
       "ieee8021PbVidTranslationRowStatus": ieee8021PbVidTranslationRowStatus,
       "ieee8021PbCVidRegistrationTable": ieee8021PbCVidRegistrationTable,
       "ieee8021PbCVidRegistrationEntry": ieee8021PbCVidRegistrationEntry,
       "ieee8021PbCVidRegistrationCVid": ieee8021PbCVidRegistrationCVid,
       "ieee8021PbCVidRegistrationSVid": ieee8021PbCVidRegistrationSVid,
       "ieee8021PbCVidRegistrationUntaggedPep": ieee8021PbCVidRegistrationUntaggedPep,
       "ieee8021PbCVidRegistrationUntaggedCep": ieee8021PbCVidRegistrationUntaggedCep,
       "ieee8021PbCVidRegistrationRowStatus": ieee8021PbCVidRegistrationRowStatus,
       "ieee8021PbEdgePortTable": ieee8021PbEdgePortTable,
       "ieee8021PbEdgePortEntry": ieee8021PbEdgePortEntry,
       "ieee8021PbEdgePortSVid": ieee8021PbEdgePortSVid,
       "ieee8021PbEdgePortPVID": ieee8021PbEdgePortPVID,
       "ieee8021PbEdgePortDefaultUserPriority": ieee8021PbEdgePortDefaultUserPriority,
       "ieee8021PbEdgePortAcceptableFrameTypes": ieee8021PbEdgePortAcceptableFrameTypes,
       "ieee8021PbEdgePortEnableIngressFiltering": ieee8021PbEdgePortEnableIngressFiltering,
       "ieee8021PbServicePriorityRegenerationTable": ieee8021PbServicePriorityRegenerationTable,
       "ieee8021PbServicePriorityRegenerationEntry": ieee8021PbServicePriorityRegenerationEntry,
       "ieee8021PbServicePriorityRegenerationSVid": ieee8021PbServicePriorityRegenerationSVid,
       "ieee8021PbServicePriorityRegenerationReceivedPriority": ieee8021PbServicePriorityRegenerationReceivedPriority,
       "ieee8021PbServicePriorityRegenerationRegeneratedPriority": ieee8021PbServicePriorityRegenerationRegeneratedPriority,
       "ieee8021PbCnpTable": ieee8021PbCnpTable,
       "ieee8021PbCnpEntry": ieee8021PbCnpEntry,
       "ieee8021PbCnpCComponentId": ieee8021PbCnpCComponentId,
       "ieee8021PbCnpSVid": ieee8021PbCnpSVid,
       "ieee8021PbCnpRowStatus": ieee8021PbCnpRowStatus,
       "ieee8021PbPnpTable": ieee8021PbPnpTable,
       "ieee8021PbPnpEntry": ieee8021PbPnpEntry,
       "ieee8021PbPnpRowStatus": ieee8021PbPnpRowStatus,
       "ieee8021PbCepTable": ieee8021PbCepTable,
       "ieee8021PbCepEntry": ieee8021PbCepEntry,
       "ieee8021PbCepCComponentId": ieee8021PbCepCComponentId,
       "ieee8021PbCepCepPortNumber": ieee8021PbCepCepPortNumber,
       "ieee8021PbCepRowStatus": ieee8021PbCepRowStatus,
       "ieee8021PbRcapTable": ieee8021PbRcapTable,
       "ieee8021PbRcapEntry": ieee8021PbRcapEntry,
       "ieee8021PbRcapSComponentId": ieee8021PbRcapSComponentId,
       "ieee8021PbRcapRcapPortNumber": ieee8021PbRcapRcapPortNumber,
       "ieee8021PbRcapRowStatus": ieee8021PbRcapRowStatus,
       "ieee8021PbInternalInterfaceTable": ieee8021PbInternalInterfaceTable,
       "ieee8021PbIiEntry": ieee8021PbIiEntry,
       "ieee8021PbIiExternalSVid": ieee8021PbIiExternalSVid,
       "ieee8021PbIiInternalPortNumber": ieee8021PbIiInternalPortNumber,
       "ieee8021PbIiInternalPortType": ieee8021PbIiInternalPortType,
       "ieee8021PbIiInternalSVid": ieee8021PbIiInternalSVid,
       "ieee8021PbIiRowStatus": ieee8021PbIiRowStatus,
       "ieee8021PbConformance": ieee8021PbConformance,
       "ieee8021PbGroups": ieee8021PbGroups,
       "ieee8021PbVidTranslationGroup": ieee8021PbVidTranslationGroup,
       "ieee8021PbCVidRegistrationGroup": ieee8021PbCVidRegistrationGroup,
       "ieee8021PbEdgePortGroup": ieee8021PbEdgePortGroup,
       "ieee8021PbServicePriorityRegenerationGroup": ieee8021PbServicePriorityRegenerationGroup,
       "ieee8021PbDynamicCnpGroup": ieee8021PbDynamicCnpGroup,
       "ieee8021PbDynamicPnpGroup": ieee8021PbDynamicPnpGroup,
       "ieee8021PbDynamicCepGroup": ieee8021PbDynamicCepGroup,
       "ieee8021PbDynamicRcapGroup": ieee8021PbDynamicRcapGroup,
       "ieee8021PbInternalInterfaceGroup": ieee8021PbInternalInterfaceGroup,
       "ieee8021PbDynamicRcapV2Group": ieee8021PbDynamicRcapV2Group,
       "ieee8021PbCompliances": ieee8021PbCompliances,
       "ieee8021PbCompliance": ieee8021PbCompliance,
       "ieee8021PbComplianceV2": ieee8021PbComplianceV2}
)
