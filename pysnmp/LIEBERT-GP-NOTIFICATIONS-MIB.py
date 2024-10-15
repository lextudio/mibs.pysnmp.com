# SNMP MIB module (LIEBERT-GP-NOTIFICATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-NOTIFICATIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:57 2024
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

(lgpConditionDescr,
 lgpConditionId,
 lgpConditionTableRef,
 lgpConditionTableRowRef,
 lgpConditionTime) = mibBuilder.importSymbols(
    "LIEBERT-GP-CONDITIONS-MIB",
    "lgpConditionDescr",
    "lgpConditionId",
    "lgpConditionTableRef",
    "lgpConditionTableRowRef",
    "lgpConditionTime")

(lgpNotifications,
 liebertNotificationsModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpNotifications",
    "liebertNotificationsModuleReg")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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


# MODULE-IDENTITY

liebertGlobalProductsNotificationsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 4, 1)
)
liebertGlobalProductsNotificationsModule.setRevisions(
        ("2008-07-02 00:00",
         "2008-05-15 00:00",
         "2008-01-10 00:00",
         "2006-08-15 00:00",
         "2006-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpEventNotifications_ObjectIdentity = ObjectIdentity
lgpEventNotifications = _LgpEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0)
)
if mibBuilder.loadTexts:
    lgpEventNotifications.setStatus("current")
_LgpEventParameters_ObjectIdentity = ObjectIdentity
lgpEventParameters = _LgpEventParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10)
)
if mibBuilder.loadTexts:
    lgpEventParameters.setStatus("current")
_LgpEventParmTableRef_Type = ObjectIdentifier
_LgpEventParmTableRef_Object = MibScalar
lgpEventParmTableRef = _LgpEventParmTableRef_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 5),
    _LgpEventParmTableRef_Type()
)
lgpEventParmTableRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEventParmTableRef.setStatus("current")
_LgpEventParmTableRowRef_Type = ObjectIdentifier
_LgpEventParmTableRowRef_Object = MibScalar
lgpEventParmTableRowRef = _LgpEventParmTableRowRef_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 6),
    _LgpEventParmTableRowRef_Type()
)
lgpEventParmTableRowRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEventParmTableRowRef.setStatus("current")

# Managed Objects groups


# Notification objects

lgpEventConditionEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 1)
)
lgpEventConditionEntryAdded.setObjects(
      *(("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionId"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionDescr"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTime"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRef"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventConditionEntryAdded.setStatus(
        "current"
    )

lgpEventConditionEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 2)
)
lgpEventConditionEntryRemoved.setObjects(
      *(("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionId"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionDescr"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTime"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRef"),
        ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventConditionEntryRemoved.setStatus(
        "current"
    )

lgpEventLowBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 3)
)
lgpEventLowBatteryWarning.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventLowBatteryWarning.setStatus(
        "current"
    )

lgpEventLoadTransferedToBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 4)
)
lgpEventLoadTransferedToBypass.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventLoadTransferedToBypass.setStatus(
        "current"
    )

lgpEventInternalFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 5)
)
lgpEventInternalFault.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventInternalFault.setStatus(
        "current"
    )

lgpEventBatteryTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 6)
)
lgpEventBatteryTestFailed.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventBatteryTestFailed.setStatus(
        "current"
    )

lgpEventOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 7)
)
lgpEventOutputOverload.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventOutputOverload.setStatus(
        "current"
    )

lgpEventEstablishedPowerRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 8)
)
lgpEventEstablishedPowerRedundancy.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventEstablishedPowerRedundancy.setStatus(
        "current"
    )

lgpEventLostPowerRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 9)
)
lgpEventLostPowerRedundancy.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventLostPowerRedundancy.setStatus(
        "current"
    )

lgpEventPowerModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 10)
)
lgpEventPowerModuleFailure.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventPowerModuleFailure.setStatus(
        "current"
    )

lgpEventBatteryModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 11)
)
lgpEventBatteryModuleFailure.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventBatteryModuleFailure.setStatus(
        "current"
    )

lgpEventControlModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 12)
)
lgpEventControlModuleFailure.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventControlModuleFailure.setStatus(
        "current"
    )

lgpEventPowerModuleWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 13)
)
lgpEventPowerModuleWarning.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventPowerModuleWarning.setStatus(
        "current"
    )

lgpEventBatteryModuleWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 14)
)
lgpEventBatteryModuleWarning.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventBatteryModuleWarning.setStatus(
        "current"
    )

lgpEventControlModuleWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 15)
)
lgpEventControlModuleWarning.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventControlModuleWarning.setStatus(
        "current"
    )

lgpEventAgentFirmwareUpdateSuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 16)
)
lgpEventAgentFirmwareUpdateSuccessful.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventAgentFirmwareUpdateSuccessful.setStatus(
        "deprecated"
    )

lgpEventAgentFirmwareCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 17)
)
lgpEventAgentFirmwareCorrupt.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventAgentFirmwareCorrupt.setStatus(
        "deprecated"
    )

lgpEventConfigModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 18)
)
lgpEventConfigModified.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventConfigModified.setStatus(
        "current"
    )

lgpEventModuleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 19)
)
lgpEventModuleAdded.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventModuleAdded.setStatus(
        "current"
    )

lgpEventModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 20)
)
lgpEventModuleRemoved.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventModuleRemoved.setStatus(
        "current"
    )

lgpEventRcpPowerStateChangeOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 21)
)
lgpEventRcpPowerStateChangeOn.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventRcpPowerStateChangeOn.setStatus(
        "current"
    )

lgpEventRcpPowerStateChangeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 22)
)
lgpEventRcpPowerStateChangeOff.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventRcpPowerStateChangeOff.setStatus(
        "current"
    )

lgpEventRcpLoadAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 23)
)
lgpEventRcpLoadAdded.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventRcpLoadAdded.setStatus(
        "current"
    )

lgpEventRcpLoadRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 24)
)
lgpEventRcpLoadRemoved.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventRcpLoadRemoved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-NOTIFICATIONS-MIB",
    **{"liebertGlobalProductsNotificationsModule": liebertGlobalProductsNotificationsModule,
       "lgpEventNotifications": lgpEventNotifications,
       "lgpEventConditionEntryAdded": lgpEventConditionEntryAdded,
       "lgpEventConditionEntryRemoved": lgpEventConditionEntryRemoved,
       "lgpEventLowBatteryWarning": lgpEventLowBatteryWarning,
       "lgpEventLoadTransferedToBypass": lgpEventLoadTransferedToBypass,
       "lgpEventInternalFault": lgpEventInternalFault,
       "lgpEventBatteryTestFailed": lgpEventBatteryTestFailed,
       "lgpEventOutputOverload": lgpEventOutputOverload,
       "lgpEventEstablishedPowerRedundancy": lgpEventEstablishedPowerRedundancy,
       "lgpEventLostPowerRedundancy": lgpEventLostPowerRedundancy,
       "lgpEventPowerModuleFailure": lgpEventPowerModuleFailure,
       "lgpEventBatteryModuleFailure": lgpEventBatteryModuleFailure,
       "lgpEventControlModuleFailure": lgpEventControlModuleFailure,
       "lgpEventPowerModuleWarning": lgpEventPowerModuleWarning,
       "lgpEventBatteryModuleWarning": lgpEventBatteryModuleWarning,
       "lgpEventControlModuleWarning": lgpEventControlModuleWarning,
       "lgpEventAgentFirmwareUpdateSuccessful": lgpEventAgentFirmwareUpdateSuccessful,
       "lgpEventAgentFirmwareCorrupt": lgpEventAgentFirmwareCorrupt,
       "lgpEventConfigModified": lgpEventConfigModified,
       "lgpEventModuleAdded": lgpEventModuleAdded,
       "lgpEventModuleRemoved": lgpEventModuleRemoved,
       "lgpEventRcpPowerStateChangeOn": lgpEventRcpPowerStateChangeOn,
       "lgpEventRcpPowerStateChangeOff": lgpEventRcpPowerStateChangeOff,
       "lgpEventRcpLoadAdded": lgpEventRcpLoadAdded,
       "lgpEventRcpLoadRemoved": lgpEventRcpLoadRemoved,
       "lgpEventParameters": lgpEventParameters,
       "lgpEventParmTableRef": lgpEventParmTableRef,
       "lgpEventParmTableRowRef": lgpEventParmTableRowRef}
)
