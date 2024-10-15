# SNMP MIB module (VMWARE-SRM-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-SRM-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:55 2024
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

(vmwSRM,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwSRM")


# MODULE-IDENTITY

vmwSRMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 51, 10)
)
vmwSRMMIB.setRevisions(
        ("2012-02-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwSRMevents_ObjectIdentity = ObjectIdentity
vmwSRMevents = _VmwSRMevents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0)
)
_VmwSrmNotification_ObjectIdentity = ObjectIdentity
vmwSrmNotification = _VmwSrmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1)
)
_VmwSrmVmName_Type = DisplayString
_VmwSrmVmName_Object = MibScalar
vmwSrmVmName = _VmwSrmVmName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1, 1),
    _VmwSrmVmName_Type()
)
vmwSrmVmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwSrmVmName.setStatus("current")
_VmwSrmRecoveryName_Type = DisplayString
_VmwSrmRecoveryName_Object = MibScalar
vmwSrmRecoveryName = _VmwSrmRecoveryName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1, 2),
    _VmwSrmRecoveryName_Type()
)
vmwSrmRecoveryName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwSrmRecoveryName.setStatus("current")
_VmwSrmPromptString_Type = DisplayString
_VmwSrmPromptString_Object = MibScalar
vmwSrmPromptString = _VmwSrmPromptString_Object(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1, 3),
    _VmwSrmPromptString_Type()
)
vmwSrmPromptString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwSrmPromptString.setStatus("current")


class _VmwSrmRecoveryType_Type(Integer32):
    """Custom type vmwSrmRecoveryType based on Integer32"""
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
        *(("cleanup", 4),
          ("recovery", 2),
          ("reprotect", 3),
          ("test", 1))
    )


_VmwSrmRecoveryType_Type.__name__ = "Integer32"
_VmwSrmRecoveryType_Object = MibScalar
vmwSrmRecoveryType = _VmwSrmRecoveryType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1, 4),
    _VmwSrmRecoveryType_Type()
)
vmwSrmRecoveryType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwSrmRecoveryType.setStatus("current")


class _VmwSrmRecoveryState_Type(Integer32):
    """Custom type vmwSrmRecoveryState based on Integer32"""
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
        *(("cancelled", 4),
          ("completed", 5),
          ("paused", 3),
          ("running", 2),
          ("uninitialized", 1))
    )


_VmwSrmRecoveryState_Type.__name__ = "Integer32"
_VmwSrmRecoveryState_Object = MibScalar
vmwSrmRecoveryState = _VmwSrmRecoveryState_Object(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1, 5),
    _VmwSrmRecoveryState_Type()
)
vmwSrmRecoveryState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwSrmRecoveryState.setStatus("current")
_VmwSrmSiteString_Type = DisplayString
_VmwSrmSiteString_Object = MibScalar
vmwSrmSiteString = _VmwSrmSiteString_Object(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1, 6),
    _VmwSrmSiteString_Type()
)
vmwSrmSiteString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwSrmSiteString.setStatus("current")
_VmwSrmVmUuid_Type = DisplayString
_VmwSrmVmUuid_Object = MibScalar
vmwSrmVmUuid = _VmwSrmVmUuid_Object(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1, 7),
    _VmwSrmVmUuid_Type()
)
vmwSrmVmUuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwSrmVmUuid.setStatus("current")


class _VmwSrmResult_Type(Integer32):
    """Custom type vmwSrmResult based on Integer32"""
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
        *(("cancelled", 4),
          ("failure", 2),
          ("success", 1),
          ("warning", 3))
    )


_VmwSrmResult_Type.__name__ = "Integer32"
_VmwSrmResult_Object = MibScalar
vmwSrmResult = _VmwSrmResult_Object(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1, 8),
    _VmwSrmResult_Type()
)
vmwSrmResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwSrmResult.setStatus("current")
_VmwSrmCommandName_Type = DisplayString
_VmwSrmCommandName_Object = MibScalar
vmwSrmCommandName = _VmwSrmCommandName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 51, 1, 9),
    _VmwSrmCommandName_Type()
)
vmwSrmCommandName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwSrmCommandName.setStatus("current")
_VmwSRMMIBConformance_ObjectIdentity = ObjectIdentity
vmwSRMMIBConformance = _VmwSRMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 51, 10, 2)
)
_VmwSRMMIBCompliances_ObjectIdentity = ObjectIdentity
vmwSRMMIBCompliances = _VmwSRMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 1)
)
_VmwSRMMIBGroups_ObjectIdentity = ObjectIdentity
vmwSRMMIBGroups = _VmwSRMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 2)
)

# Managed Objects groups

vmwSRMNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 2, 1)
)
vmwSRMNotificationInfoGroup.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmPromptString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"))
)
if mibBuilder.loadTexts:
    vmwSRMNotificationInfoGroup.setStatus("current")


# Notification objects

vmwareSrmRecoveryPlanExecuteTestBeginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 1)
)
vmwareSrmRecoveryPlanExecuteTestBeginTrap.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanExecuteTestBeginTrap.setStatus(
        "current"
    )

vmwareSrmRecoveryPlanExecuteTestEndEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 2)
)
vmwareSrmRecoveryPlanExecuteTestEndEvent.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanExecuteTestEndEvent.setStatus(
        "current"
    )

vmwareSrmRecoveryPlanExecuteBeginEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 3)
)
vmwareSrmRecoveryPlanExecuteBeginEvent.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanExecuteBeginEvent.setStatus(
        "current"
    )

vmwareVmwSrmRecoveryPlanExecuteEndEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 4)
)
vmwareVmwSrmRecoveryPlanExecuteEndEvent.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
)
if mibBuilder.loadTexts:
    vmwareVmwSrmRecoveryPlanExecuteEndEvent.setStatus(
        "current"
    )

vmwareVmwSrmRecoveryVmBeginEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 5)
)
vmwareVmwSrmRecoveryVmBeginEvent.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"))
)
if mibBuilder.loadTexts:
    vmwareVmwSrmRecoveryVmBeginEvent.setStatus(
        "current"
    )

vmwareSrmRecoveryVmEndEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 6)
)
vmwareSrmRecoveryVmEndEvent.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryVmEndEvent.setStatus(
        "current"
    )

vmwareSrmRecoveryPlanPromptDisplay = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 7)
)
vmwareSrmRecoveryPlanPromptDisplay.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmPromptString"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanPromptDisplay.setStatus(
        "current"
    )

vmwareSrmRecoveryPlanPromptResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 8)
)
vmwareSrmRecoveryPlanPromptResponse.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanPromptResponse.setStatus(
        "current"
    )

vmwareVmwSrmRecoveryPlanServerCommandBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 9)
)
vmwareVmwSrmRecoveryPlanServerCommandBegin.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"))
)
if mibBuilder.loadTexts:
    vmwareVmwSrmRecoveryPlanServerCommandBegin.setStatus(
        "current"
    )

vmwareSrmRecoveryPlanServerCommandEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 10)
)
vmwareSrmRecoveryPlanServerCommandEnd.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanServerCommandEnd.setStatus(
        "current"
    )

vmwareSrmRecoveryPlanVmCommandBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 11)
)
vmwareSrmRecoveryPlanVmCommandBegin.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanVmCommandBegin.setStatus(
        "current"
    )

vmwareSrmRecoveryPlanVmCommandEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 12)
)
vmwareSrmRecoveryPlanVmCommandEnd.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmCommandName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmVmUuid"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanVmCommandEnd.setStatus(
        "current"
    )

vmwareSrmRecoveryPlanExecuteReprotectBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 13)
)
vmwareSrmRecoveryPlanExecuteReprotectBegin.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanExecuteReprotectBegin.setStatus(
        "current"
    )

vmwareSrmRecoveryPlanExecuteReprotectEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 14)
)
vmwareSrmRecoveryPlanExecuteReprotectEnd.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
)
if mibBuilder.loadTexts:
    vmwareSrmRecoveryPlanExecuteReprotectEnd.setStatus(
        "current"
    )

vmwareVmwSrmRecoveryPlanExecuteCleanupBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 15)
)
vmwareVmwSrmRecoveryPlanExecuteCleanupBegin.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"))
)
if mibBuilder.loadTexts:
    vmwareVmwSrmRecoveryPlanExecuteCleanupBegin.setStatus(
        "current"
    )

vmwSrmRecoveryPlanExecuteCleanupEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 51, 0, 16)
)
vmwSrmRecoveryPlanExecuteCleanupEnd.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwSrmSiteString"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryName"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryType"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryState"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmResult"))
)
if mibBuilder.loadTexts:
    vmwSrmRecoveryPlanExecuteCleanupEnd.setStatus(
        "current"
    )


# Notifications groups

vmwSRMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 2, 2)
)
vmwSRMNotificationGroup.setObjects(
      *(("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteTestBeginTrap"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteTestEndEvent"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteBeginEvent"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareVmwSrmRecoveryPlanExecuteEndEvent"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareVmwSrmRecoveryVmBeginEvent"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryVmEndEvent"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanPromptDisplay"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanPromptResponse"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareVmwSrmRecoveryPlanServerCommandBegin"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanServerCommandEnd"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanVmCommandBegin"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanVmCommandEnd"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteReprotectBegin"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareSrmRecoveryPlanExecuteReprotectEnd"),
        ("VMWARE-SRM-EVENT-MIB", "vmwareVmwSrmRecoveryPlanExecuteCleanupBegin"),
        ("VMWARE-SRM-EVENT-MIB", "vmwSrmRecoveryPlanExecuteCleanupEnd"))
)
if mibBuilder.loadTexts:
    vmwSRMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwSRMMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 51, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    vmwSRMMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-SRM-EVENT-MIB",
    **{"vmwSRMevents": vmwSRMevents,
       "vmwareSrmRecoveryPlanExecuteTestBeginTrap": vmwareSrmRecoveryPlanExecuteTestBeginTrap,
       "vmwareSrmRecoveryPlanExecuteTestEndEvent": vmwareSrmRecoveryPlanExecuteTestEndEvent,
       "vmwareSrmRecoveryPlanExecuteBeginEvent": vmwareSrmRecoveryPlanExecuteBeginEvent,
       "vmwareVmwSrmRecoveryPlanExecuteEndEvent": vmwareVmwSrmRecoveryPlanExecuteEndEvent,
       "vmwareVmwSrmRecoveryVmBeginEvent": vmwareVmwSrmRecoveryVmBeginEvent,
       "vmwareSrmRecoveryVmEndEvent": vmwareSrmRecoveryVmEndEvent,
       "vmwareSrmRecoveryPlanPromptDisplay": vmwareSrmRecoveryPlanPromptDisplay,
       "vmwareSrmRecoveryPlanPromptResponse": vmwareSrmRecoveryPlanPromptResponse,
       "vmwareVmwSrmRecoveryPlanServerCommandBegin": vmwareVmwSrmRecoveryPlanServerCommandBegin,
       "vmwareSrmRecoveryPlanServerCommandEnd": vmwareSrmRecoveryPlanServerCommandEnd,
       "vmwareSrmRecoveryPlanVmCommandBegin": vmwareSrmRecoveryPlanVmCommandBegin,
       "vmwareSrmRecoveryPlanVmCommandEnd": vmwareSrmRecoveryPlanVmCommandEnd,
       "vmwareSrmRecoveryPlanExecuteReprotectBegin": vmwareSrmRecoveryPlanExecuteReprotectBegin,
       "vmwareSrmRecoveryPlanExecuteReprotectEnd": vmwareSrmRecoveryPlanExecuteReprotectEnd,
       "vmwareVmwSrmRecoveryPlanExecuteCleanupBegin": vmwareVmwSrmRecoveryPlanExecuteCleanupBegin,
       "vmwSrmRecoveryPlanExecuteCleanupEnd": vmwSrmRecoveryPlanExecuteCleanupEnd,
       "vmwSrmNotification": vmwSrmNotification,
       "vmwSrmVmName": vmwSrmVmName,
       "vmwSrmRecoveryName": vmwSrmRecoveryName,
       "vmwSrmPromptString": vmwSrmPromptString,
       "vmwSrmRecoveryType": vmwSrmRecoveryType,
       "vmwSrmRecoveryState": vmwSrmRecoveryState,
       "vmwSrmSiteString": vmwSrmSiteString,
       "vmwSrmVmUuid": vmwSrmVmUuid,
       "vmwSrmResult": vmwSrmResult,
       "vmwSrmCommandName": vmwSrmCommandName,
       "vmwSRMMIB": vmwSRMMIB,
       "vmwSRMMIBConformance": vmwSRMMIBConformance,
       "vmwSRMMIBCompliances": vmwSRMMIBCompliances,
       "vmwSRMMIBBasicCompliance": vmwSRMMIBBasicCompliance,
       "vmwSRMMIBGroups": vmwSRMMIBGroups,
       "vmwSRMNotificationInfoGroup": vmwSRMNotificationInfoGroup,
       "vmwSRMNotificationGroup": vmwSRMNotificationGroup}
)
