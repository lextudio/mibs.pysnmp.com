# SNMP MIB module (IEEE8021-TSN-REMOTE-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-TSN-REMOTE-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:46 2024
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

(ieee8021BridgeBaseComponentId,
 ieee8021BridgeBasePort,
 ieee8021BridgeTrafficClass) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId",
    "ieee8021BridgeBasePort",
    "ieee8021BridgeTrafficClass")

(ieee8021QBridgeVlanIndex,) = mibBuilder.importSymbols(
    "IEEE8021-Q-BRIDGE-MIB",
    "ieee8021QBridgeVlanIndex")

(IEEE8021BridgePortNumber,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "ieee802dot1mibs")

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

ieee8021TsnRemoteMgmtMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32)
)
ieee8021TsnRemoteMgmtMib.setRevisions(
        ("2018-10-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021TsnRemoteMgmtNotifications_ObjectIdentity = ObjectIdentity
ieee8021TsnRemoteMgmtNotifications = _Ieee8021TsnRemoteMgmtNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32, 0)
)
_Ieee8021TsnRemoteMgmtObjects_ObjectIdentity = ObjectIdentity
ieee8021TsnRemoteMgmtObjects = _Ieee8021TsnRemoteMgmtObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32, 1)
)
_Ieee8021TsnRemoteMgmtBridgeDelay_ObjectIdentity = ObjectIdentity
ieee8021TsnRemoteMgmtBridgeDelay = _Ieee8021TsnRemoteMgmtBridgeDelay_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 1)
)
_Ieee8021TsnRemoteMgmtBridgeDelayTable_Object = MibTable
ieee8021TsnRemoteMgmtBridgeDelayTable = _Ieee8021TsnRemoteMgmtBridgeDelayTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtBridgeDelayTable.setStatus("current")
_Ieee8021TsnRemoteMgmtBridgeDelayEntry_Object = MibTableRow
ieee8021TsnRemoteMgmtBridgeDelayEntry = _Ieee8021TsnRemoteMgmtBridgeDelayEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1)
)
ieee8021TsnRemoteMgmtBridgeDelayEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeTrafficClass"),
    (0, "IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtBridgeIngressPort"),
    (0, "IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtBridgeEgressPort"),
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtBridgeDelayEntry.setStatus("current")
_Ieee8021TsnRemoteMgmtBridgeIngressPort_Type = IEEE8021BridgePortNumber
_Ieee8021TsnRemoteMgmtBridgeIngressPort_Object = MibTableColumn
ieee8021TsnRemoteMgmtBridgeIngressPort = _Ieee8021TsnRemoteMgmtBridgeIngressPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 1),
    _Ieee8021TsnRemoteMgmtBridgeIngressPort_Type()
)
ieee8021TsnRemoteMgmtBridgeIngressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtBridgeIngressPort.setStatus("current")
_Ieee8021TsnRemoteMgmtBridgeEgressPort_Type = IEEE8021BridgePortNumber
_Ieee8021TsnRemoteMgmtBridgeEgressPort_Object = MibTableColumn
ieee8021TsnRemoteMgmtBridgeEgressPort = _Ieee8021TsnRemoteMgmtBridgeEgressPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 2),
    _Ieee8021TsnRemoteMgmtBridgeEgressPort_Type()
)
ieee8021TsnRemoteMgmtBridgeEgressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtBridgeEgressPort.setStatus("current")
_Ieee8021TsnRemoteMgmtIndependentDelayMin_Type = Unsigned32
_Ieee8021TsnRemoteMgmtIndependentDelayMin_Object = MibTableColumn
ieee8021TsnRemoteMgmtIndependentDelayMin = _Ieee8021TsnRemoteMgmtIndependentDelayMin_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 3),
    _Ieee8021TsnRemoteMgmtIndependentDelayMin_Type()
)
ieee8021TsnRemoteMgmtIndependentDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtIndependentDelayMin.setStatus("current")
_Ieee8021TsnRemoteMgmtIndependentDelayMax_Type = Unsigned32
_Ieee8021TsnRemoteMgmtIndependentDelayMax_Object = MibTableColumn
ieee8021TsnRemoteMgmtIndependentDelayMax = _Ieee8021TsnRemoteMgmtIndependentDelayMax_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 4),
    _Ieee8021TsnRemoteMgmtIndependentDelayMax_Type()
)
ieee8021TsnRemoteMgmtIndependentDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtIndependentDelayMax.setStatus("current")
_Ieee8021TsnRemoteMgmtDependentDelayMin_Type = Unsigned32
_Ieee8021TsnRemoteMgmtDependentDelayMin_Object = MibTableColumn
ieee8021TsnRemoteMgmtDependentDelayMin = _Ieee8021TsnRemoteMgmtDependentDelayMin_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 5),
    _Ieee8021TsnRemoteMgmtDependentDelayMin_Type()
)
ieee8021TsnRemoteMgmtDependentDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtDependentDelayMin.setStatus("current")
_Ieee8021TsnRemoteMgmtDependentDelayMax_Type = Unsigned32
_Ieee8021TsnRemoteMgmtDependentDelayMax_Object = MibTableColumn
ieee8021TsnRemoteMgmtDependentDelayMax = _Ieee8021TsnRemoteMgmtDependentDelayMax_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 6),
    _Ieee8021TsnRemoteMgmtDependentDelayMax_Type()
)
ieee8021TsnRemoteMgmtDependentDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtDependentDelayMax.setStatus("current")
_Ieee8021TsnRemoteMgmtPropagationDelay_ObjectIdentity = ObjectIdentity
ieee8021TsnRemoteMgmtPropagationDelay = _Ieee8021TsnRemoteMgmtPropagationDelay_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 2)
)
_Ieee8021TsnRemoteMgmtPropagationDelayTable_Object = MibTable
ieee8021TsnRemoteMgmtPropagationDelayTable = _Ieee8021TsnRemoteMgmtPropagationDelayTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtPropagationDelayTable.setStatus("current")
_Ieee8021TsnRemoteMgmtPropagationDelayEntry_Object = MibTableRow
ieee8021TsnRemoteMgmtPropagationDelayEntry = _Ieee8021TsnRemoteMgmtPropagationDelayEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 2, 1, 1)
)
ieee8021TsnRemoteMgmtPropagationDelayEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtPropagationDelayEntry.setStatus("current")
_Ieee8021TsnRemoteMgmtTxPropagationDelay_Type = Unsigned32
_Ieee8021TsnRemoteMgmtTxPropagationDelay_Object = MibTableColumn
ieee8021TsnRemoteMgmtTxPropagationDelay = _Ieee8021TsnRemoteMgmtTxPropagationDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 2, 1, 1, 1),
    _Ieee8021TsnRemoteMgmtTxPropagationDelay_Type()
)
ieee8021TsnRemoteMgmtTxPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtTxPropagationDelay.setStatus("current")
_Ieee8021TsnRemoteMgmtStaticTrees_ObjectIdentity = ObjectIdentity
ieee8021TsnRemoteMgmtStaticTrees = _Ieee8021TsnRemoteMgmtStaticTrees_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 3)
)
_Ieee8021TsnRemoteMgmtStaticTreesSupported_Type = TruthValue
_Ieee8021TsnRemoteMgmtStaticTreesSupported_Object = MibScalar
ieee8021TsnRemoteMgmtStaticTreesSupported = _Ieee8021TsnRemoteMgmtStaticTreesSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 3, 1),
    _Ieee8021TsnRemoteMgmtStaticTreesSupported_Type()
)
ieee8021TsnRemoteMgmtStaticTreesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtStaticTreesSupported.setStatus("current")
_Ieee8021TsnRemoteMgmtMrpExternalControl_ObjectIdentity = ObjectIdentity
ieee8021TsnRemoteMgmtMrpExternalControl = _Ieee8021TsnRemoteMgmtMrpExternalControl_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4)
)
_Ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable_Object = MibTable
ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable = _Ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable.setStatus("current")
_Ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry_Object = MibTableRow
ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry = _Ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1)
)
ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanIndex"),
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry.setStatus("current")


class _Ieee8021TsnRemoteMgmtMsrpMrpExternalControl_Type(TruthValue):
    """Custom type ieee8021TsnRemoteMgmtMsrpMrpExternalControl based on TruthValue"""


_Ieee8021TsnRemoteMgmtMsrpMrpExternalControl_Object = MibTableColumn
ieee8021TsnRemoteMgmtMsrpMrpExternalControl = _Ieee8021TsnRemoteMgmtMsrpMrpExternalControl_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 1),
    _Ieee8021TsnRemoteMgmtMsrpMrpExternalControl_Type()
)
ieee8021TsnRemoteMgmtMsrpMrpExternalControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMsrpMrpExternalControl.setStatus("current")
_Ieee8021TsnRemoteMgmtMrpIndicationList_Type = OctetString
_Ieee8021TsnRemoteMgmtMrpIndicationList_Object = MibTableColumn
ieee8021TsnRemoteMgmtMrpIndicationList = _Ieee8021TsnRemoteMgmtMrpIndicationList_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 2),
    _Ieee8021TsnRemoteMgmtMrpIndicationList_Type()
)
ieee8021TsnRemoteMgmtMrpIndicationList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMrpIndicationList.setStatus("current")
_Ieee8021TsnRemoteMgmtMrpIndicationListLength_Type = Unsigned32
_Ieee8021TsnRemoteMgmtMrpIndicationListLength_Object = MibTableColumn
ieee8021TsnRemoteMgmtMrpIndicationListLength = _Ieee8021TsnRemoteMgmtMrpIndicationListLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 3),
    _Ieee8021TsnRemoteMgmtMrpIndicationListLength_Type()
)
ieee8021TsnRemoteMgmtMrpIndicationListLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMrpIndicationListLength.setStatus("current")
_Ieee8021TsnRemoteMgmtMrpIndicationChangeCounter_Type = Counter64
_Ieee8021TsnRemoteMgmtMrpIndicationChangeCounter_Object = MibTableColumn
ieee8021TsnRemoteMgmtMrpIndicationChangeCounter = _Ieee8021TsnRemoteMgmtMrpIndicationChangeCounter_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 4),
    _Ieee8021TsnRemoteMgmtMrpIndicationChangeCounter_Type()
)
ieee8021TsnRemoteMgmtMrpIndicationChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMrpIndicationChangeCounter.setStatus("current")
_Ieee8021TsnRemoteMgmtMrpAdminRequestList_Type = OctetString
_Ieee8021TsnRemoteMgmtMrpAdminRequestList_Object = MibTableColumn
ieee8021TsnRemoteMgmtMrpAdminRequestList = _Ieee8021TsnRemoteMgmtMrpAdminRequestList_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 5),
    _Ieee8021TsnRemoteMgmtMrpAdminRequestList_Type()
)
ieee8021TsnRemoteMgmtMrpAdminRequestList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMrpAdminRequestList.setStatus("current")


class _Ieee8021TsnRemoteMgmtMrpAdminRequestListLength_Type(Unsigned32):
    """Custom type ieee8021TsnRemoteMgmtMrpAdminRequestListLength based on Unsigned32"""
    defaultValue = 0


_Ieee8021TsnRemoteMgmtMrpAdminRequestListLength_Object = MibTableColumn
ieee8021TsnRemoteMgmtMrpAdminRequestListLength = _Ieee8021TsnRemoteMgmtMrpAdminRequestListLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 6),
    _Ieee8021TsnRemoteMgmtMrpAdminRequestListLength_Type()
)
ieee8021TsnRemoteMgmtMrpAdminRequestListLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMrpAdminRequestListLength.setStatus("current")
_Ieee8021TsnRemoteMgmtMrpOperRequestList_Type = OctetString
_Ieee8021TsnRemoteMgmtMrpOperRequestList_Object = MibTableColumn
ieee8021TsnRemoteMgmtMrpOperRequestList = _Ieee8021TsnRemoteMgmtMrpOperRequestList_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 7),
    _Ieee8021TsnRemoteMgmtMrpOperRequestList_Type()
)
ieee8021TsnRemoteMgmtMrpOperRequestList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMrpOperRequestList.setStatus("current")
_Ieee8021TsnRemoteMgmtMrpOperRequestListLength_Type = Unsigned32
_Ieee8021TsnRemoteMgmtMrpOperRequestListLength_Object = MibTableColumn
ieee8021TsnRemoteMgmtMrpOperRequestListLength = _Ieee8021TsnRemoteMgmtMrpOperRequestListLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 8),
    _Ieee8021TsnRemoteMgmtMrpOperRequestListLength_Type()
)
ieee8021TsnRemoteMgmtMrpOperRequestListLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMrpOperRequestListLength.setStatus("current")
_Ieee8021TsnRemoteMgmtConformance_ObjectIdentity = ObjectIdentity
ieee8021TsnRemoteMgmtConformance = _Ieee8021TsnRemoteMgmtConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32, 2)
)
_Ieee8021TsnRemoteMgmtCompliances_ObjectIdentity = ObjectIdentity
ieee8021TsnRemoteMgmtCompliances = _Ieee8021TsnRemoteMgmtCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32, 2, 1)
)
_Ieee8021TsnRemoteMgmtGroups_ObjectIdentity = ObjectIdentity
ieee8021TsnRemoteMgmtGroups = _Ieee8021TsnRemoteMgmtGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 32, 2, 2)
)

# Managed Objects groups

ieee8021TsnRemoteMgmtBridgeDelayGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 32, 2, 2, 1)
)
ieee8021TsnRemoteMgmtBridgeDelayGroup.setObjects(
      *(("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtIndependentDelayMin"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtIndependentDelayMax"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtDependentDelayMin"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtDependentDelayMax"))
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtBridgeDelayGroup.setStatus("current")

ieee8021TsnRemoteMgmtPropagationDelayGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 32, 2, 2, 2)
)
ieee8021TsnRemoteMgmtPropagationDelayGroup.setObjects(
    ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtTxPropagationDelay")
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtPropagationDelayGroup.setStatus("current")

ieee8021TsnRemoteMgmtStaticTreesGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 32, 2, 2, 3)
)
ieee8021TsnRemoteMgmtStaticTreesGroup.setObjects(
    ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtStaticTreesSupported")
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtStaticTreesGroup.setStatus("current")

ieee8021TsnRemoteMgmtMrpExternalControlGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 32, 2, 2, 4)
)
ieee8021TsnRemoteMgmtMrpExternalControlGroup.setObjects(
      *(("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMsrpMrpExternalControl"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpIndicationList"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpIndicationListLength"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpIndicationChangeCounter"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpAdminRequestList"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpAdminRequestListLength"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpOperRequestList"),
        ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpOperRequestListLength"))
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtMrpExternalControlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021TsnRemoteMgmtCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021TsnRemoteMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-TSN-REMOTE-MANAGEMENT-MIB",
    **{"ieee8021TsnRemoteMgmtMib": ieee8021TsnRemoteMgmtMib,
       "ieee8021TsnRemoteMgmtNotifications": ieee8021TsnRemoteMgmtNotifications,
       "ieee8021TsnRemoteMgmtObjects": ieee8021TsnRemoteMgmtObjects,
       "ieee8021TsnRemoteMgmtBridgeDelay": ieee8021TsnRemoteMgmtBridgeDelay,
       "ieee8021TsnRemoteMgmtBridgeDelayTable": ieee8021TsnRemoteMgmtBridgeDelayTable,
       "ieee8021TsnRemoteMgmtBridgeDelayEntry": ieee8021TsnRemoteMgmtBridgeDelayEntry,
       "ieee8021TsnRemoteMgmtBridgeIngressPort": ieee8021TsnRemoteMgmtBridgeIngressPort,
       "ieee8021TsnRemoteMgmtBridgeEgressPort": ieee8021TsnRemoteMgmtBridgeEgressPort,
       "ieee8021TsnRemoteMgmtIndependentDelayMin": ieee8021TsnRemoteMgmtIndependentDelayMin,
       "ieee8021TsnRemoteMgmtIndependentDelayMax": ieee8021TsnRemoteMgmtIndependentDelayMax,
       "ieee8021TsnRemoteMgmtDependentDelayMin": ieee8021TsnRemoteMgmtDependentDelayMin,
       "ieee8021TsnRemoteMgmtDependentDelayMax": ieee8021TsnRemoteMgmtDependentDelayMax,
       "ieee8021TsnRemoteMgmtPropagationDelay": ieee8021TsnRemoteMgmtPropagationDelay,
       "ieee8021TsnRemoteMgmtPropagationDelayTable": ieee8021TsnRemoteMgmtPropagationDelayTable,
       "ieee8021TsnRemoteMgmtPropagationDelayEntry": ieee8021TsnRemoteMgmtPropagationDelayEntry,
       "ieee8021TsnRemoteMgmtTxPropagationDelay": ieee8021TsnRemoteMgmtTxPropagationDelay,
       "ieee8021TsnRemoteMgmtStaticTrees": ieee8021TsnRemoteMgmtStaticTrees,
       "ieee8021TsnRemoteMgmtStaticTreesSupported": ieee8021TsnRemoteMgmtStaticTreesSupported,
       "ieee8021TsnRemoteMgmtMrpExternalControl": ieee8021TsnRemoteMgmtMrpExternalControl,
       "ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable": ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable,
       "ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry": ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry,
       "ieee8021TsnRemoteMgmtMsrpMrpExternalControl": ieee8021TsnRemoteMgmtMsrpMrpExternalControl,
       "ieee8021TsnRemoteMgmtMrpIndicationList": ieee8021TsnRemoteMgmtMrpIndicationList,
       "ieee8021TsnRemoteMgmtMrpIndicationListLength": ieee8021TsnRemoteMgmtMrpIndicationListLength,
       "ieee8021TsnRemoteMgmtMrpIndicationChangeCounter": ieee8021TsnRemoteMgmtMrpIndicationChangeCounter,
       "ieee8021TsnRemoteMgmtMrpAdminRequestList": ieee8021TsnRemoteMgmtMrpAdminRequestList,
       "ieee8021TsnRemoteMgmtMrpAdminRequestListLength": ieee8021TsnRemoteMgmtMrpAdminRequestListLength,
       "ieee8021TsnRemoteMgmtMrpOperRequestList": ieee8021TsnRemoteMgmtMrpOperRequestList,
       "ieee8021TsnRemoteMgmtMrpOperRequestListLength": ieee8021TsnRemoteMgmtMrpOperRequestListLength,
       "ieee8021TsnRemoteMgmtConformance": ieee8021TsnRemoteMgmtConformance,
       "ieee8021TsnRemoteMgmtCompliances": ieee8021TsnRemoteMgmtCompliances,
       "ieee8021TsnRemoteMgmtCompliance": ieee8021TsnRemoteMgmtCompliance,
       "ieee8021TsnRemoteMgmtGroups": ieee8021TsnRemoteMgmtGroups,
       "ieee8021TsnRemoteMgmtBridgeDelayGroup": ieee8021TsnRemoteMgmtBridgeDelayGroup,
       "ieee8021TsnRemoteMgmtPropagationDelayGroup": ieee8021TsnRemoteMgmtPropagationDelayGroup,
       "ieee8021TsnRemoteMgmtStaticTreesGroup": ieee8021TsnRemoteMgmtStaticTreesGroup,
       "ieee8021TsnRemoteMgmtMrpExternalControlGroup": ieee8021TsnRemoteMgmtMrpExternalControlGroup}
)
