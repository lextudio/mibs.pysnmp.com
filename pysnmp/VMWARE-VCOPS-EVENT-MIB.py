# SNMP MIB module (VMWARE-VCOPS-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-VCOPS-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:59 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(vmwVCOps,) = mibBuilder.importSymbols(
    "VMWARE-PRODUCTS-MIB",
    "vmwVCOps")


# MODULE-IDENTITY

vmwVcopsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1)
)
vmwVcopsMIB.setRevisions(
        ("2013-02-01 00:00",
         "2011-10-19 00:00",
         "2009-01-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwareAlertTrap_ObjectIdentity = ObjectIdentity
vmwareAlertTrap = _VmwareAlertTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0)
)
if mibBuilder.loadTexts:
    vmwareAlertTrap.setStatus("current")
_VmwareGenericAlertData_ObjectIdentity = ObjectIdentity
vmwareGenericAlertData = _VmwareGenericAlertData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2)
)
if mibBuilder.loadTexts:
    vmwareGenericAlertData.setStatus("current")
_VmwareAlertAliveServerName_Type = OctetString
_VmwareAlertAliveServerName_Object = MibScalar
vmwareAlertAliveServerName = _VmwareAlertAliveServerName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 1),
    _VmwareAlertAliveServerName_Type()
)
vmwareAlertAliveServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertAliveServerName.setStatus("current")
_VmwareAlertEntityName_Type = OctetString
_VmwareAlertEntityName_Object = MibScalar
vmwareAlertEntityName = _VmwareAlertEntityName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 2),
    _VmwareAlertEntityName_Type()
)
vmwareAlertEntityName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertEntityName.setStatus("current")
_VmwareAlertEntityType_Type = OctetString
_VmwareAlertEntityType_Object = MibScalar
vmwareAlertEntityType = _VmwareAlertEntityType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 3),
    _VmwareAlertEntityType_Type()
)
vmwareAlertEntityType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertEntityType.setStatus("current")
_VmwareAlertTimestamp_Type = OctetString
_VmwareAlertTimestamp_Object = MibScalar
vmwareAlertTimestamp = _VmwareAlertTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 4),
    _VmwareAlertTimestamp_Type()
)
vmwareAlertTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertTimestamp.setStatus("current")
_VmwareAlertCriticality_Type = OctetString
_VmwareAlertCriticality_Object = MibScalar
vmwareAlertCriticality = _VmwareAlertCriticality_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 5),
    _VmwareAlertCriticality_Type()
)
vmwareAlertCriticality.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertCriticality.setStatus("current")
_VmwareAlertRootCause_Type = OctetString
_VmwareAlertRootCause_Object = MibScalar
vmwareAlertRootCause = _VmwareAlertRootCause_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 6),
    _VmwareAlertRootCause_Type()
)
vmwareAlertRootCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertRootCause.setStatus("current")
_VmwareAlertURL_Type = OctetString
_VmwareAlertURL_Object = MibScalar
vmwareAlertURL = _VmwareAlertURL_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 7),
    _VmwareAlertURL_Type()
)
vmwareAlertURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertURL.setStatus("current")
_VmwareAlertID_Type = OctetString
_VmwareAlertID_Object = MibScalar
vmwareAlertID = _VmwareAlertID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 8),
    _VmwareAlertID_Type()
)
vmwareAlertID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertID.setStatus("current")
_VmwareAlertMessage_Type = OctetString
_VmwareAlertMessage_Object = MibScalar
vmwareAlertMessage = _VmwareAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 9),
    _VmwareAlertMessage_Type()
)
vmwareAlertMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertMessage.setStatus("current")
_VmwareAlertType_Type = OctetString
_VmwareAlertType_Object = MibScalar
vmwareAlertType = _VmwareAlertType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 10),
    _VmwareAlertType_Type()
)
vmwareAlertType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertType.setStatus("current")
_VmwareAlertSubtype_Type = OctetString
_VmwareAlertSubtype_Object = MibScalar
vmwareAlertSubtype = _VmwareAlertSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 2, 11),
    _VmwareAlertSubtype_Type()
)
vmwareAlertSubtype.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwareAlertSubtype.setStatus("current")
_VmwVCOPSMIBConformance_ObjectIdentity = ObjectIdentity
vmwVCOPSMIBConformance = _VmwVCOPSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 99)
)
_VmwVCOPSMIBCompliances_ObjectIdentity = ObjectIdentity
vmwVCOPSMIBCompliances = _VmwVCOPSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 99, 1)
)
_VmwVCOPSMIBGroups_ObjectIdentity = ObjectIdentity
vmwVCOPSMIBGroups = _VmwVCOPSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 99, 2)
)

# Managed Objects groups

vmwVCOPSNotificationInfoGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 99, 2, 2)
)
vmwVCOPSNotificationInfoGroup1.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwVCOPSNotificationInfoGroup1.setStatus("current")


# Notification objects

vmwareTrapKPIBreachActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 1)
)
vmwareTrapKPIBreachActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapKPIBreachActive.setStatus(
        "current"
    )

vmwareTrapKPIBreachClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 2)
)
vmwareTrapKPIBreachClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapKPIBreachClear.setStatus(
        "current"
    )

vmwareTrapKPIBreachChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 3)
)
vmwareTrapKPIBreachChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapKPIBreachChange.setStatus(
        "current"
    )

vmwareTrapKPIPredictionActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 4)
)
vmwareTrapKPIPredictionActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapKPIPredictionActive.setStatus(
        "current"
    )

vmwareTrapKPIPredictionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 5)
)
vmwareTrapKPIPredictionClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapKPIPredictionClear.setStatus(
        "current"
    )

vmwareTrapKPIPredictionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 6)
)
vmwareTrapKPIPredictionChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapKPIPredictionChange.setStatus(
        "current"
    )

vmwareTrapAggregateAnomalyActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 7)
)
vmwareTrapAggregateAnomalyActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAggregateAnomalyActive.setStatus(
        "current"
    )

vmwareTrapAggregateAnomalyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 8)
)
vmwareTrapAggregateAnomalyClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAggregateAnomalyClear.setStatus(
        "current"
    )

vmwareTrapKPIHTBreachActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 10)
)
vmwareTrapKPIHTBreachActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapKPIHTBreachActive.setStatus(
        "current"
    )

vmwareTrapKPIHTBreachClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 11)
)
vmwareTrapKPIHTBreachClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapKPIHTBreachClear.setStatus(
        "current"
    )

vmwareTrapKPIHTBreachChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 12)
)
vmwareTrapKPIHTBreachChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapKPIHTBreachChange.setStatus(
        "current"
    )

vmwareTrapNotificationActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 13)
)
vmwareTrapNotificationActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapNotificationActive.setStatus(
        "current"
    )

vmwareTrapNotificationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 14)
)
vmwareTrapNotificationClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapNotificationClear.setStatus(
        "current"
    )

vmwareTrapNotificationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 15)
)
vmwareTrapNotificationChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapNotificationChange.setStatus(
        "current"
    )

vmwareTrapAbnormalityActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 16)
)
vmwareTrapAbnormalityActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAbnormalityActive.setStatus(
        "current"
    )

vmwareTrapAbnormalityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 17)
)
vmwareTrapAbnormalityClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAbnormalityClear.setStatus(
        "current"
    )

vmwareTrapAbnormalityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 18)
)
vmwareTrapAbnormalityChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAbnormalityChange.setStatus(
        "current"
    )

vmwareTrapWorkloadActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 19)
)
vmwareTrapWorkloadActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapWorkloadActive.setStatus(
        "current"
    )

vmwareTrapWorkloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 20)
)
vmwareTrapWorkloadClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapWorkloadClear.setStatus(
        "current"
    )

vmwareTrapWorkloadChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 21)
)
vmwareTrapWorkloadChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapWorkloadChange.setStatus(
        "current"
    )

vmwareTrapAnomalyActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 22)
)
vmwareTrapAnomalyActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAnomalyActive.setStatus(
        "current"
    )

vmwareTrapAnomalyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 23)
)
vmwareTrapAnomalyClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAnomalyClear.setStatus(
        "current"
    )

vmwareTrapAnomalyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 24)
)
vmwareTrapAnomalyChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAnomalyChange.setStatus(
        "current"
    )

vmwareTrapFaultActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 25)
)
vmwareTrapFaultActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapFaultActive.setStatus(
        "current"
    )

vmwareTrapFaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 26)
)
vmwareTrapFaultClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapFaultClear.setStatus(
        "current"
    )

vmwareTrapFaultChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 27)
)
vmwareTrapFaultChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapFaultChange.setStatus(
        "current"
    )

vmwareTrapTimeRemainingActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 28)
)
vmwareTrapTimeRemainingActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapTimeRemainingActive.setStatus(
        "current"
    )

vmwareTrapTimeRemainingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 29)
)
vmwareTrapTimeRemainingClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapTimeRemainingClear.setStatus(
        "current"
    )

vmwareTrapTimeRemainingChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 30)
)
vmwareTrapTimeRemainingChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapTimeRemainingChange.setStatus(
        "current"
    )

vmwareTrapCapacityRemainingActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 31)
)
vmwareTrapCapacityRemainingActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapCapacityRemainingActive.setStatus(
        "current"
    )

vmwareTrapCapacityRemainingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 32)
)
vmwareTrapCapacityRemainingClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapCapacityRemainingClear.setStatus(
        "current"
    )

vmwareTrapCapacityRemainingChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 33)
)
vmwareTrapCapacityRemainingChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapCapacityRemainingChange.setStatus(
        "current"
    )

vmwareTrapStressActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 34)
)
vmwareTrapStressActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapStressActive.setStatus(
        "current"
    )

vmwareTrapStressClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 35)
)
vmwareTrapStressClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapStressClear.setStatus(
        "current"
    )

vmwareTrapStressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 36)
)
vmwareTrapStressChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapStressChange.setStatus(
        "current"
    )

vmwareTrapWasteActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 37)
)
vmwareTrapWasteActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapWasteActive.setStatus(
        "current"
    )

vmwareTrapWasteClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 38)
)
vmwareTrapWasteClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapWasteClear.setStatus(
        "current"
    )

vmwareTrapWasteChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 39)
)
vmwareTrapWasteChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapWasteChange.setStatus(
        "current"
    )

vmwareTrapDensityActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 40)
)
vmwareTrapDensityActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapDensityActive.setStatus(
        "current"
    )

vmwareTrapDensityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 41)
)
vmwareTrapDensityClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapDensityClear.setStatus(
        "current"
    )

vmwareTrapDensityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 42)
)
vmwareTrapDensityChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapDensityChange.setStatus(
        "current"
    )

vmwareTrapComplianceActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 43)
)
vmwareTrapComplianceActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapComplianceActive.setStatus(
        "current"
    )

vmwareTrapComplianceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 44)
)
vmwareTrapComplianceClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapComplianceClear.setStatus(
        "current"
    )

vmwareTrapComplianceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 45)
)
vmwareTrapComplianceChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapComplianceChange.setStatus(
        "current"
    )

vmwareTrapConsolidatedAlertActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 60)
)
vmwareTrapConsolidatedAlertActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapConsolidatedAlertActive.setStatus(
        "current"
    )

vmwareTrapConsolidatedAlertClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 61)
)
vmwareTrapConsolidatedAlertClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapConsolidatedAlertClear.setStatus(
        "current"
    )

vmwareTrapConsolidatedAlertChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 62)
)
vmwareTrapConsolidatedAlertChange.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapConsolidatedAlertChange.setStatus(
        "current"
    )

vmwareTrapAliveComponentFailureActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 101)
)
vmwareTrapAliveComponentFailureActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAliveComponentFailureActive.setStatus(
        "current"
    )

vmwareTrapAliveComponentFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 102)
)
vmwareTrapAliveComponentFailureClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapAliveComponentFailureClear.setStatus(
        "current"
    )

vmwareTrapResourceDisconnectedActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 103)
)
vmwareTrapResourceDisconnectedActive.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapResourceDisconnectedActive.setStatus(
        "current"
    )

vmwareTrapResourceDisconnectedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 104)
)
vmwareTrapResourceDisconnectedClear.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapResourceDisconnectedClear.setStatus(
        "current"
    )

vmwareTrapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 0, 200)
)
vmwareTrapTest.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertAliveServerName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityName"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertEntityType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertTimestamp"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertCriticality"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertRootCause"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertURL"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertID"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertMessage"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertType"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareAlertSubtype"))
)
if mibBuilder.loadTexts:
    vmwareTrapTest.setStatus(
        "current"
    )


# Notifications groups

vmwVCOPSNotificationGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 99, 2, 3)
)
vmwVCOPSNotificationGroup1.setObjects(
      *(("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapComplianceActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapComplianceClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapComplianceChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapConsolidatedAlertActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapConsolidatedAlertClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapConsolidatedAlertChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapTest"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapKPIBreachActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapKPIBreachClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapKPIBreachChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapKPIPredictionActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapKPIPredictionClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapKPIPredictionChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAggregateAnomalyActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAggregateAnomalyClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapKPIHTBreachActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapKPIHTBreachClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapKPIHTBreachChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapNotificationActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapNotificationClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapNotificationChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAbnormalityActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAbnormalityClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAbnormalityChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapWorkloadActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapWorkloadClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapWorkloadChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAnomalyActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAnomalyClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAnomalyChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapFaultActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapFaultClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapFaultChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapTimeRemainingActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapTimeRemainingClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapTimeRemainingChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapCapacityRemainingActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapCapacityRemainingClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapCapacityRemainingChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapStressActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapStressClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapStressChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapWasteActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapWasteClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapWasteChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapDensityActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapDensityClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapDensityChange"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAliveComponentFailureActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapAliveComponentFailureClear"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapResourceDisconnectedActive"),
        ("VMWARE-VCOPS-EVENT-MIB", "vmwareTrapResourceDisconnectedClear"))
)
if mibBuilder.loadTexts:
    vmwVCOPSNotificationGroup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwVCOPSMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5, 1, 99, 1, 3)
)
if mibBuilder.loadTexts:
    vmwVCOPSMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VCOPS-EVENT-MIB",
    **{"vmwVcopsMIB": vmwVcopsMIB,
       "vmwareAlertTrap": vmwareAlertTrap,
       "vmwareTrapKPIBreachActive": vmwareTrapKPIBreachActive,
       "vmwareTrapKPIBreachClear": vmwareTrapKPIBreachClear,
       "vmwareTrapKPIBreachChange": vmwareTrapKPIBreachChange,
       "vmwareTrapKPIPredictionActive": vmwareTrapKPIPredictionActive,
       "vmwareTrapKPIPredictionClear": vmwareTrapKPIPredictionClear,
       "vmwareTrapKPIPredictionChange": vmwareTrapKPIPredictionChange,
       "vmwareTrapAggregateAnomalyActive": vmwareTrapAggregateAnomalyActive,
       "vmwareTrapAggregateAnomalyClear": vmwareTrapAggregateAnomalyClear,
       "vmwareTrapKPIHTBreachActive": vmwareTrapKPIHTBreachActive,
       "vmwareTrapKPIHTBreachClear": vmwareTrapKPIHTBreachClear,
       "vmwareTrapKPIHTBreachChange": vmwareTrapKPIHTBreachChange,
       "vmwareTrapNotificationActive": vmwareTrapNotificationActive,
       "vmwareTrapNotificationClear": vmwareTrapNotificationClear,
       "vmwareTrapNotificationChange": vmwareTrapNotificationChange,
       "vmwareTrapAbnormalityActive": vmwareTrapAbnormalityActive,
       "vmwareTrapAbnormalityClear": vmwareTrapAbnormalityClear,
       "vmwareTrapAbnormalityChange": vmwareTrapAbnormalityChange,
       "vmwareTrapWorkloadActive": vmwareTrapWorkloadActive,
       "vmwareTrapWorkloadClear": vmwareTrapWorkloadClear,
       "vmwareTrapWorkloadChange": vmwareTrapWorkloadChange,
       "vmwareTrapAnomalyActive": vmwareTrapAnomalyActive,
       "vmwareTrapAnomalyClear": vmwareTrapAnomalyClear,
       "vmwareTrapAnomalyChange": vmwareTrapAnomalyChange,
       "vmwareTrapFaultActive": vmwareTrapFaultActive,
       "vmwareTrapFaultClear": vmwareTrapFaultClear,
       "vmwareTrapFaultChange": vmwareTrapFaultChange,
       "vmwareTrapTimeRemainingActive": vmwareTrapTimeRemainingActive,
       "vmwareTrapTimeRemainingClear": vmwareTrapTimeRemainingClear,
       "vmwareTrapTimeRemainingChange": vmwareTrapTimeRemainingChange,
       "vmwareTrapCapacityRemainingActive": vmwareTrapCapacityRemainingActive,
       "vmwareTrapCapacityRemainingClear": vmwareTrapCapacityRemainingClear,
       "vmwareTrapCapacityRemainingChange": vmwareTrapCapacityRemainingChange,
       "vmwareTrapStressActive": vmwareTrapStressActive,
       "vmwareTrapStressClear": vmwareTrapStressClear,
       "vmwareTrapStressChange": vmwareTrapStressChange,
       "vmwareTrapWasteActive": vmwareTrapWasteActive,
       "vmwareTrapWasteClear": vmwareTrapWasteClear,
       "vmwareTrapWasteChange": vmwareTrapWasteChange,
       "vmwareTrapDensityActive": vmwareTrapDensityActive,
       "vmwareTrapDensityClear": vmwareTrapDensityClear,
       "vmwareTrapDensityChange": vmwareTrapDensityChange,
       "vmwareTrapComplianceActive": vmwareTrapComplianceActive,
       "vmwareTrapComplianceClear": vmwareTrapComplianceClear,
       "vmwareTrapComplianceChange": vmwareTrapComplianceChange,
       "vmwareTrapConsolidatedAlertActive": vmwareTrapConsolidatedAlertActive,
       "vmwareTrapConsolidatedAlertClear": vmwareTrapConsolidatedAlertClear,
       "vmwareTrapConsolidatedAlertChange": vmwareTrapConsolidatedAlertChange,
       "vmwareTrapAliveComponentFailureActive": vmwareTrapAliveComponentFailureActive,
       "vmwareTrapAliveComponentFailureClear": vmwareTrapAliveComponentFailureClear,
       "vmwareTrapResourceDisconnectedActive": vmwareTrapResourceDisconnectedActive,
       "vmwareTrapResourceDisconnectedClear": vmwareTrapResourceDisconnectedClear,
       "vmwareTrapTest": vmwareTrapTest,
       "vmwareGenericAlertData": vmwareGenericAlertData,
       "vmwareAlertAliveServerName": vmwareAlertAliveServerName,
       "vmwareAlertEntityName": vmwareAlertEntityName,
       "vmwareAlertEntityType": vmwareAlertEntityType,
       "vmwareAlertTimestamp": vmwareAlertTimestamp,
       "vmwareAlertCriticality": vmwareAlertCriticality,
       "vmwareAlertRootCause": vmwareAlertRootCause,
       "vmwareAlertURL": vmwareAlertURL,
       "vmwareAlertID": vmwareAlertID,
       "vmwareAlertMessage": vmwareAlertMessage,
       "vmwareAlertType": vmwareAlertType,
       "vmwareAlertSubtype": vmwareAlertSubtype,
       "vmwVCOPSMIBConformance": vmwVCOPSMIBConformance,
       "vmwVCOPSMIBCompliances": vmwVCOPSMIBCompliances,
       "vmwVCOPSMIBBasicCompliance": vmwVCOPSMIBBasicCompliance,
       "vmwVCOPSMIBGroups": vmwVCOPSMIBGroups,
       "vmwVCOPSNotificationInfoGroup1": vmwVCOPSNotificationInfoGroup1,
       "vmwVCOPSNotificationGroup1": vmwVCOPSNotificationGroup1}
)
