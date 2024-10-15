# SNMP MIB module (UMSAOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UMSAOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:30 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(Boolean,
 Datetime,
 Real32,
 Real64,
 Sint16,
 Sint32,
 Sint64,
 Sint8,
 String,
 Uint16,
 Uint32,
 Uint64,
 Uint8,
 ibmpsgAlertOnLAN) = mibBuilder.importSymbols(
    "UMS-MIB",
    "Boolean",
    "Datetime",
    "Real32",
    "Real64",
    "Sint16",
    "Sint32",
    "Sint64",
    "Sint8",
    "String",
    "Uint16",
    "Uint32",
    "Uint64",
    "Uint8",
    "ibmpsgAlertOnLAN")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IBMPSGWatchdogTable_Object = MibTable
iBMPSGWatchdogTable = _IBMPSGWatchdogTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1)
)
if mibBuilder.loadTexts:
    iBMPSGWatchdogTable.setStatus("mandatory")
_IBMPSGWatchdogEntry_Object = MibTableRow
iBMPSGWatchdogEntry = _IBMPSGWatchdogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1)
)
iBMPSGWatchdogEntry.setIndexNames(
    (0, "UMSAOL-MIB", "iBMPSGWatchdogKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGWatchdogEntry.setStatus("mandatory")
_IBMPSGWatchdogKeyIndex_Type = String
_IBMPSGWatchdogKeyIndex_Object = MibTableColumn
iBMPSGWatchdogKeyIndex = _IBMPSGWatchdogKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 1),
    _IBMPSGWatchdogKeyIndex_Type()
)
iBMPSGWatchdogKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iBMPSGWatchdogKeyIndex.setStatus("mandatory")
_IBMPSGWatchdogMonitoredDeviceId_Type = String
_IBMPSGWatchdogMonitoredDeviceId_Object = MibTableColumn
iBMPSGWatchdogMonitoredDeviceId = _IBMPSGWatchdogMonitoredDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 2),
    _IBMPSGWatchdogMonitoredDeviceId_Type()
)
iBMPSGWatchdogMonitoredDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iBMPSGWatchdogMonitoredDeviceId.setStatus("mandatory")
_IBMPSGWatchdogMonitoredEntity_Type = Uint16
_IBMPSGWatchdogMonitoredEntity_Object = MibTableColumn
iBMPSGWatchdogMonitoredEntity = _IBMPSGWatchdogMonitoredEntity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 3),
    _IBMPSGWatchdogMonitoredEntity_Type()
)
iBMPSGWatchdogMonitoredEntity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogMonitoredEntity.setStatus("mandatory")
_IBMPSGWatchdogMonitoredEntityDescription_Type = String
_IBMPSGWatchdogMonitoredEntityDescription_Object = MibTableColumn
iBMPSGWatchdogMonitoredEntityDescription = _IBMPSGWatchdogMonitoredEntityDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 4),
    _IBMPSGWatchdogMonitoredEntityDescription_Type()
)
iBMPSGWatchdogMonitoredEntityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogMonitoredEntityDescription.setStatus("mandatory")
_IBMPSGWatchdogTimeoutInterval_Type = Uint32
_IBMPSGWatchdogTimeoutInterval_Object = MibTableColumn
iBMPSGWatchdogTimeoutInterval = _IBMPSGWatchdogTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 5),
    _IBMPSGWatchdogTimeoutInterval_Type()
)
iBMPSGWatchdogTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogTimeoutInterval.setStatus("mandatory")
_IBMPSGWatchdogTimerResolution_Type = Uint32
_IBMPSGWatchdogTimerResolution_Object = MibTableColumn
iBMPSGWatchdogTimerResolution = _IBMPSGWatchdogTimerResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 6),
    _IBMPSGWatchdogTimerResolution_Type()
)
iBMPSGWatchdogTimerResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogTimerResolution.setStatus("mandatory")
_IBMPSGWatchdogTimeOfLastExpiration_Type = Datetime
_IBMPSGWatchdogTimeOfLastExpiration_Object = MibTableColumn
iBMPSGWatchdogTimeOfLastExpiration = _IBMPSGWatchdogTimeOfLastExpiration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 7),
    _IBMPSGWatchdogTimeOfLastExpiration_Type()
)
iBMPSGWatchdogTimeOfLastExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogTimeOfLastExpiration.setStatus("mandatory")
_IBMPSGWatchdogMonitoredEntityOnLastExpiration_Type = Uint16
_IBMPSGWatchdogMonitoredEntityOnLastExpiration_Object = MibTableColumn
iBMPSGWatchdogMonitoredEntityOnLastExpiration = _IBMPSGWatchdogMonitoredEntityOnLastExpiration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 8),
    _IBMPSGWatchdogMonitoredEntityOnLastExpiration_Type()
)
iBMPSGWatchdogMonitoredEntityOnLastExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogMonitoredEntityOnLastExpiration.setStatus("mandatory")
_IBMPSGWatchdogActionOnExpiration_Type = Uint16
_IBMPSGWatchdogActionOnExpiration_Object = MibTableColumn
iBMPSGWatchdogActionOnExpiration = _IBMPSGWatchdogActionOnExpiration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 9),
    _IBMPSGWatchdogActionOnExpiration_Type()
)
iBMPSGWatchdogActionOnExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogActionOnExpiration.setStatus("mandatory")
_IBMPSGWatchdogMaximumTimeoutInterval_Type = Uint32
_IBMPSGWatchdogMaximumTimeoutInterval_Object = MibTableColumn
iBMPSGWatchdogMaximumTimeoutInterval = _IBMPSGWatchdogMaximumTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 10),
    _IBMPSGWatchdogMaximumTimeoutInterval_Type()
)
iBMPSGWatchdogMaximumTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogMaximumTimeoutInterval.setStatus("mandatory")
_IBMPSGWatchdogMinimumTimeoutInterval_Type = Uint32
_IBMPSGWatchdogMinimumTimeoutInterval_Object = MibTableColumn
iBMPSGWatchdogMinimumTimeoutInterval = _IBMPSGWatchdogMinimumTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 11),
    _IBMPSGWatchdogMinimumTimeoutInterval_Type()
)
iBMPSGWatchdogMinimumTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogMinimumTimeoutInterval.setStatus("mandatory")
_IBMPSGWatchdogEnabled_Type = Boolean
_IBMPSGWatchdogEnabled_Object = MibTableColumn
iBMPSGWatchdogEnabled = _IBMPSGWatchdogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 12),
    _IBMPSGWatchdogEnabled_Type()
)
iBMPSGWatchdogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogEnabled.setStatus("mandatory")
_IBMPSGWatchdogStatus_Type = String
_IBMPSGWatchdogStatus_Object = MibTableColumn
iBMPSGWatchdogStatus = _IBMPSGWatchdogStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 1, 1, 13),
    _IBMPSGWatchdogStatus_Type()
)
iBMPSGWatchdogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGWatchdogStatus.setStatus("mandatory")
_IBMPSGAlertOnLANTable_Object = MibTable
iBMPSGAlertOnLANTable = _IBMPSGAlertOnLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2)
)
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANTable.setStatus("mandatory")
_IBMPSGAlertOnLANEntry_Object = MibTableRow
iBMPSGAlertOnLANEntry = _IBMPSGAlertOnLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1)
)
iBMPSGAlertOnLANEntry.setIndexNames(
    (0, "UMSAOL-MIB", "iBMPSGAlertOnLANKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANEntry.setStatus("mandatory")
_IBMPSGAlertOnLANKeyIndex_Type = String
_IBMPSGAlertOnLANKeyIndex_Object = MibTableColumn
iBMPSGAlertOnLANKeyIndex = _IBMPSGAlertOnLANKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 1),
    _IBMPSGAlertOnLANKeyIndex_Type()
)
iBMPSGAlertOnLANKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANKeyIndex.setStatus("mandatory")
_IBMPSGAlertOnLANDestinationType_Type = Uint16
_IBMPSGAlertOnLANDestinationType_Object = MibTableColumn
iBMPSGAlertOnLANDestinationType = _IBMPSGAlertOnLANDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 2),
    _IBMPSGAlertOnLANDestinationType_Type()
)
iBMPSGAlertOnLANDestinationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANDestinationType.setStatus("mandatory")
_IBMPSGAlertOnLANOtherDestinationTypeDescription_Type = String
_IBMPSGAlertOnLANOtherDestinationTypeDescription_Object = MibTableColumn
iBMPSGAlertOnLANOtherDestinationTypeDescription = _IBMPSGAlertOnLANOtherDestinationTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 3),
    _IBMPSGAlertOnLANOtherDestinationTypeDescription_Type()
)
iBMPSGAlertOnLANOtherDestinationTypeDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANOtherDestinationTypeDescription.setStatus("mandatory")
_IBMPSGAlertOnLANAlertDestinationAddress_Type = String
_IBMPSGAlertOnLANAlertDestinationAddress_Object = MibTableColumn
iBMPSGAlertOnLANAlertDestinationAddress = _IBMPSGAlertOnLANAlertDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 4),
    _IBMPSGAlertOnLANAlertDestinationAddress_Type()
)
iBMPSGAlertOnLANAlertDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANAlertDestinationAddress.setStatus("mandatory")
_IBMPSGAlertOnLANMessageFormat_Type = Uint16
_IBMPSGAlertOnLANMessageFormat_Object = MibTableColumn
iBMPSGAlertOnLANMessageFormat = _IBMPSGAlertOnLANMessageFormat_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 5),
    _IBMPSGAlertOnLANMessageFormat_Type()
)
iBMPSGAlertOnLANMessageFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANMessageFormat.setStatus("mandatory")
_IBMPSGAlertOnLANOtherMessageFormatDescription_Type = String
_IBMPSGAlertOnLANOtherMessageFormatDescription_Object = MibTableColumn
iBMPSGAlertOnLANOtherMessageFormatDescription = _IBMPSGAlertOnLANOtherMessageFormatDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 6),
    _IBMPSGAlertOnLANOtherMessageFormatDescription_Type()
)
iBMPSGAlertOnLANOtherMessageFormatDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANOtherMessageFormatDescription.setStatus("mandatory")
_IBMPSGAlertOnLANOnlySendsFixedMessage_Type = Boolean
_IBMPSGAlertOnLANOnlySendsFixedMessage_Object = MibTableColumn
iBMPSGAlertOnLANOnlySendsFixedMessage = _IBMPSGAlertOnLANOnlySendsFixedMessage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 7),
    _IBMPSGAlertOnLANOnlySendsFixedMessage_Type()
)
iBMPSGAlertOnLANOnlySendsFixedMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANOnlySendsFixedMessage.setStatus("mandatory")
_IBMPSGAlertOnLANFixedPartOfMessage_Type = String
_IBMPSGAlertOnLANFixedPartOfMessage_Object = MibTableColumn
iBMPSGAlertOnLANFixedPartOfMessage = _IBMPSGAlertOnLANFixedPartOfMessage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 8),
    _IBMPSGAlertOnLANFixedPartOfMessage_Type()
)
iBMPSGAlertOnLANFixedPartOfMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANFixedPartOfMessage.setStatus("mandatory")
_IBMPSGAlertOnLANDestinationIsAckCapable_Type = Boolean
_IBMPSGAlertOnLANDestinationIsAckCapable_Object = MibTableColumn
iBMPSGAlertOnLANDestinationIsAckCapable = _IBMPSGAlertOnLANDestinationIsAckCapable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 9),
    _IBMPSGAlertOnLANDestinationIsAckCapable_Type()
)
iBMPSGAlertOnLANDestinationIsAckCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANDestinationIsAckCapable.setStatus("mandatory")
_IBMPSGAlertOnLANRetryCount_Type = Uint16
_IBMPSGAlertOnLANRetryCount_Object = MibTableColumn
iBMPSGAlertOnLANRetryCount = _IBMPSGAlertOnLANRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 10),
    _IBMPSGAlertOnLANRetryCount_Type()
)
iBMPSGAlertOnLANRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANRetryCount.setStatus("mandatory")
_IBMPSGAlertOnLANEnabled_Type = Boolean
_IBMPSGAlertOnLANEnabled_Object = MibTableColumn
iBMPSGAlertOnLANEnabled = _IBMPSGAlertOnLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 11),
    _IBMPSGAlertOnLANEnabled_Type()
)
iBMPSGAlertOnLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANEnabled.setStatus("mandatory")
_IBMPSGAlertOnLANVersion_Type = String
_IBMPSGAlertOnLANVersion_Object = MibTableColumn
iBMPSGAlertOnLANVersion = _IBMPSGAlertOnLANVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 12),
    _IBMPSGAlertOnLANVersion_Type()
)
iBMPSGAlertOnLANVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANVersion.setStatus("mandatory")
_IBMPSGAlertOnLANEventAutoClearEnabled_Type = Boolean
_IBMPSGAlertOnLANEventAutoClearEnabled_Object = MibTableColumn
iBMPSGAlertOnLANEventAutoClearEnabled = _IBMPSGAlertOnLANEventAutoClearEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 13),
    _IBMPSGAlertOnLANEventAutoClearEnabled_Type()
)
iBMPSGAlertOnLANEventAutoClearEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANEventAutoClearEnabled.setStatus("mandatory")
_IBMPSGAlertOnLANMaximumEventPollInterval_Type = Uint32
_IBMPSGAlertOnLANMaximumEventPollInterval_Object = MibTableColumn
iBMPSGAlertOnLANMaximumEventPollInterval = _IBMPSGAlertOnLANMaximumEventPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 14),
    _IBMPSGAlertOnLANMaximumEventPollInterval_Type()
)
iBMPSGAlertOnLANMaximumEventPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANMaximumEventPollInterval.setStatus("mandatory")
_IBMPSGAlertOnLANMinimumEventPollInterval_Type = Uint32
_IBMPSGAlertOnLANMinimumEventPollInterval_Object = MibTableColumn
iBMPSGAlertOnLANMinimumEventPollInterval = _IBMPSGAlertOnLANMinimumEventPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 15),
    _IBMPSGAlertOnLANMinimumEventPollInterval_Type()
)
iBMPSGAlertOnLANMinimumEventPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANMinimumEventPollInterval.setStatus("mandatory")
_IBMPSGAlertOnLANEventPollInterval_Type = Uint32
_IBMPSGAlertOnLANEventPollInterval_Object = MibTableColumn
iBMPSGAlertOnLANEventPollInterval = _IBMPSGAlertOnLANEventPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 16),
    _IBMPSGAlertOnLANEventPollInterval_Type()
)
iBMPSGAlertOnLANEventPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANEventPollInterval.setStatus("mandatory")
_IBMPSGAlertOnLANHeartbeatEnabled_Type = Boolean
_IBMPSGAlertOnLANHeartbeatEnabled_Object = MibTableColumn
iBMPSGAlertOnLANHeartbeatEnabled = _IBMPSGAlertOnLANHeartbeatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 17),
    _IBMPSGAlertOnLANHeartbeatEnabled_Type()
)
iBMPSGAlertOnLANHeartbeatEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANHeartbeatEnabled.setStatus("mandatory")
_IBMPSGAlertOnLANMaximumHeartbeatInterval_Type = Uint32
_IBMPSGAlertOnLANMaximumHeartbeatInterval_Object = MibTableColumn
iBMPSGAlertOnLANMaximumHeartbeatInterval = _IBMPSGAlertOnLANMaximumHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 18),
    _IBMPSGAlertOnLANMaximumHeartbeatInterval_Type()
)
iBMPSGAlertOnLANMaximumHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANMaximumHeartbeatInterval.setStatus("mandatory")
_IBMPSGAlertOnLANMinimumHeartbeatInterval_Type = Uint32
_IBMPSGAlertOnLANMinimumHeartbeatInterval_Object = MibTableColumn
iBMPSGAlertOnLANMinimumHeartbeatInterval = _IBMPSGAlertOnLANMinimumHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 19),
    _IBMPSGAlertOnLANMinimumHeartbeatInterval_Type()
)
iBMPSGAlertOnLANMinimumHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANMinimumHeartbeatInterval.setStatus("mandatory")
_IBMPSGAlertOnLANHeartbeatInterval_Type = Uint32
_IBMPSGAlertOnLANHeartbeatInterval_Object = MibTableColumn
iBMPSGAlertOnLANHeartbeatInterval = _IBMPSGAlertOnLANHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 20),
    _IBMPSGAlertOnLANHeartbeatInterval_Type()
)
iBMPSGAlertOnLANHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANHeartbeatInterval.setStatus("mandatory")
_IBMPSGAlertOnLANStatus_Type = String
_IBMPSGAlertOnLANStatus_Object = MibTableColumn
iBMPSGAlertOnLANStatus = _IBMPSGAlertOnLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 2, 1, 21),
    _IBMPSGAlertOnLANStatus_Type()
)
iBMPSGAlertOnLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAlertOnLANStatus.setStatus("mandatory")
_IBMPSGAOLEventConfigurationTable_Object = MibTable
iBMPSGAOLEventConfigurationTable = _IBMPSGAOLEventConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 3)
)
if mibBuilder.loadTexts:
    iBMPSGAOLEventConfigurationTable.setStatus("mandatory")
_IBMPSGAOLEventConfigurationEntry_Object = MibTableRow
iBMPSGAOLEventConfigurationEntry = _IBMPSGAOLEventConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 3, 1)
)
iBMPSGAOLEventConfigurationEntry.setIndexNames(
    (0, "UMSAOL-MIB", "iBMPSGAOLEventConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGAOLEventConfigurationEntry.setStatus("mandatory")
_IBMPSGAOLEventConfigurationKeyIndex_Type = String
_IBMPSGAOLEventConfigurationKeyIndex_Object = MibTableColumn
iBMPSGAOLEventConfigurationKeyIndex = _IBMPSGAOLEventConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 3, 1, 1),
    _IBMPSGAOLEventConfigurationKeyIndex_Type()
)
iBMPSGAOLEventConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAOLEventConfigurationKeyIndex.setStatus("mandatory")
_IBMPSGAOLEventConfigurationName_Type = String
_IBMPSGAOLEventConfigurationName_Object = MibTableColumn
iBMPSGAOLEventConfigurationName = _IBMPSGAOLEventConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 3, 1, 2),
    _IBMPSGAOLEventConfigurationName_Type()
)
iBMPSGAOLEventConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAOLEventConfigurationName.setStatus("mandatory")
_IBMPSGAOLEventConfigurationIdentifier_Type = Uint32
_IBMPSGAOLEventConfigurationIdentifier_Object = MibTableColumn
iBMPSGAOLEventConfigurationIdentifier = _IBMPSGAOLEventConfigurationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 3, 1, 3),
    _IBMPSGAOLEventConfigurationIdentifier_Type()
)
iBMPSGAOLEventConfigurationIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAOLEventConfigurationIdentifier.setStatus("mandatory")
_IBMPSGAOLEventConfigurationEnabled_Type = Boolean
_IBMPSGAOLEventConfigurationEnabled_Object = MibTableColumn
iBMPSGAOLEventConfigurationEnabled = _IBMPSGAOLEventConfigurationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 3, 1, 4),
    _IBMPSGAOLEventConfigurationEnabled_Type()
)
iBMPSGAOLEventConfigurationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAOLEventConfigurationEnabled.setStatus("mandatory")
_IBMPSGAOLEventConfigurationActivated_Type = Boolean
_IBMPSGAOLEventConfigurationActivated_Object = MibTableColumn
iBMPSGAOLEventConfigurationActivated = _IBMPSGAOLEventConfigurationActivated_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 3, 1, 5),
    _IBMPSGAOLEventConfigurationActivated_Type()
)
iBMPSGAOLEventConfigurationActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAOLEventConfigurationActivated.setStatus("mandatory")
_IBMPSGAOLControlFunctionConfigurationTable_Object = MibTable
iBMPSGAOLControlFunctionConfigurationTable = _IBMPSGAOLControlFunctionConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 4)
)
if mibBuilder.loadTexts:
    iBMPSGAOLControlFunctionConfigurationTable.setStatus("mandatory")
_IBMPSGAOLControlFunctionConfigurationEntry_Object = MibTableRow
iBMPSGAOLControlFunctionConfigurationEntry = _IBMPSGAOLControlFunctionConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 4, 1)
)
iBMPSGAOLControlFunctionConfigurationEntry.setIndexNames(
    (0, "UMSAOL-MIB", "iBMPSGAOLControlFunctionConfigurationKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGAOLControlFunctionConfigurationEntry.setStatus("mandatory")
_IBMPSGAOLControlFunctionConfigurationKeyIndex_Type = String
_IBMPSGAOLControlFunctionConfigurationKeyIndex_Object = MibTableColumn
iBMPSGAOLControlFunctionConfigurationKeyIndex = _IBMPSGAOLControlFunctionConfigurationKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 4, 1, 1),
    _IBMPSGAOLControlFunctionConfigurationKeyIndex_Type()
)
iBMPSGAOLControlFunctionConfigurationKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAOLControlFunctionConfigurationKeyIndex.setStatus("mandatory")
_IBMPSGAOLControlFunctionConfigurationName_Type = String
_IBMPSGAOLControlFunctionConfigurationName_Object = MibTableColumn
iBMPSGAOLControlFunctionConfigurationName = _IBMPSGAOLControlFunctionConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 4, 1, 2),
    _IBMPSGAOLControlFunctionConfigurationName_Type()
)
iBMPSGAOLControlFunctionConfigurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAOLControlFunctionConfigurationName.setStatus("mandatory")
_IBMPSGAOLControlFunctionConfigurationIdentifier_Type = Uint32
_IBMPSGAOLControlFunctionConfigurationIdentifier_Object = MibTableColumn
iBMPSGAOLControlFunctionConfigurationIdentifier = _IBMPSGAOLControlFunctionConfigurationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 4, 1, 3),
    _IBMPSGAOLControlFunctionConfigurationIdentifier_Type()
)
iBMPSGAOLControlFunctionConfigurationIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAOLControlFunctionConfigurationIdentifier.setStatus("mandatory")
_IBMPSGAOLControlFunctionConfigurationEnabled_Type = Boolean
_IBMPSGAOLControlFunctionConfigurationEnabled_Object = MibTableColumn
iBMPSGAOLControlFunctionConfigurationEnabled = _IBMPSGAOLControlFunctionConfigurationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 70, 4, 1, 4),
    _IBMPSGAOLControlFunctionConfigurationEnabled_Type()
)
iBMPSGAOLControlFunctionConfigurationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGAOLControlFunctionConfigurationEnabled.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UMSAOL-MIB",
    **{"iBMPSGWatchdogTable": iBMPSGWatchdogTable,
       "iBMPSGWatchdogEntry": iBMPSGWatchdogEntry,
       "iBMPSGWatchdogKeyIndex": iBMPSGWatchdogKeyIndex,
       "iBMPSGWatchdogMonitoredDeviceId": iBMPSGWatchdogMonitoredDeviceId,
       "iBMPSGWatchdogMonitoredEntity": iBMPSGWatchdogMonitoredEntity,
       "iBMPSGWatchdogMonitoredEntityDescription": iBMPSGWatchdogMonitoredEntityDescription,
       "iBMPSGWatchdogTimeoutInterval": iBMPSGWatchdogTimeoutInterval,
       "iBMPSGWatchdogTimerResolution": iBMPSGWatchdogTimerResolution,
       "iBMPSGWatchdogTimeOfLastExpiration": iBMPSGWatchdogTimeOfLastExpiration,
       "iBMPSGWatchdogMonitoredEntityOnLastExpiration": iBMPSGWatchdogMonitoredEntityOnLastExpiration,
       "iBMPSGWatchdogActionOnExpiration": iBMPSGWatchdogActionOnExpiration,
       "iBMPSGWatchdogMaximumTimeoutInterval": iBMPSGWatchdogMaximumTimeoutInterval,
       "iBMPSGWatchdogMinimumTimeoutInterval": iBMPSGWatchdogMinimumTimeoutInterval,
       "iBMPSGWatchdogEnabled": iBMPSGWatchdogEnabled,
       "iBMPSGWatchdogStatus": iBMPSGWatchdogStatus,
       "iBMPSGAlertOnLANTable": iBMPSGAlertOnLANTable,
       "iBMPSGAlertOnLANEntry": iBMPSGAlertOnLANEntry,
       "iBMPSGAlertOnLANKeyIndex": iBMPSGAlertOnLANKeyIndex,
       "iBMPSGAlertOnLANDestinationType": iBMPSGAlertOnLANDestinationType,
       "iBMPSGAlertOnLANOtherDestinationTypeDescription": iBMPSGAlertOnLANOtherDestinationTypeDescription,
       "iBMPSGAlertOnLANAlertDestinationAddress": iBMPSGAlertOnLANAlertDestinationAddress,
       "iBMPSGAlertOnLANMessageFormat": iBMPSGAlertOnLANMessageFormat,
       "iBMPSGAlertOnLANOtherMessageFormatDescription": iBMPSGAlertOnLANOtherMessageFormatDescription,
       "iBMPSGAlertOnLANOnlySendsFixedMessage": iBMPSGAlertOnLANOnlySendsFixedMessage,
       "iBMPSGAlertOnLANFixedPartOfMessage": iBMPSGAlertOnLANFixedPartOfMessage,
       "iBMPSGAlertOnLANDestinationIsAckCapable": iBMPSGAlertOnLANDestinationIsAckCapable,
       "iBMPSGAlertOnLANRetryCount": iBMPSGAlertOnLANRetryCount,
       "iBMPSGAlertOnLANEnabled": iBMPSGAlertOnLANEnabled,
       "iBMPSGAlertOnLANVersion": iBMPSGAlertOnLANVersion,
       "iBMPSGAlertOnLANEventAutoClearEnabled": iBMPSGAlertOnLANEventAutoClearEnabled,
       "iBMPSGAlertOnLANMaximumEventPollInterval": iBMPSGAlertOnLANMaximumEventPollInterval,
       "iBMPSGAlertOnLANMinimumEventPollInterval": iBMPSGAlertOnLANMinimumEventPollInterval,
       "iBMPSGAlertOnLANEventPollInterval": iBMPSGAlertOnLANEventPollInterval,
       "iBMPSGAlertOnLANHeartbeatEnabled": iBMPSGAlertOnLANHeartbeatEnabled,
       "iBMPSGAlertOnLANMaximumHeartbeatInterval": iBMPSGAlertOnLANMaximumHeartbeatInterval,
       "iBMPSGAlertOnLANMinimumHeartbeatInterval": iBMPSGAlertOnLANMinimumHeartbeatInterval,
       "iBMPSGAlertOnLANHeartbeatInterval": iBMPSGAlertOnLANHeartbeatInterval,
       "iBMPSGAlertOnLANStatus": iBMPSGAlertOnLANStatus,
       "iBMPSGAOLEventConfigurationTable": iBMPSGAOLEventConfigurationTable,
       "iBMPSGAOLEventConfigurationEntry": iBMPSGAOLEventConfigurationEntry,
       "iBMPSGAOLEventConfigurationKeyIndex": iBMPSGAOLEventConfigurationKeyIndex,
       "iBMPSGAOLEventConfigurationName": iBMPSGAOLEventConfigurationName,
       "iBMPSGAOLEventConfigurationIdentifier": iBMPSGAOLEventConfigurationIdentifier,
       "iBMPSGAOLEventConfigurationEnabled": iBMPSGAOLEventConfigurationEnabled,
       "iBMPSGAOLEventConfigurationActivated": iBMPSGAOLEventConfigurationActivated,
       "iBMPSGAOLControlFunctionConfigurationTable": iBMPSGAOLControlFunctionConfigurationTable,
       "iBMPSGAOLControlFunctionConfigurationEntry": iBMPSGAOLControlFunctionConfigurationEntry,
       "iBMPSGAOLControlFunctionConfigurationKeyIndex": iBMPSGAOLControlFunctionConfigurationKeyIndex,
       "iBMPSGAOLControlFunctionConfigurationName": iBMPSGAOLControlFunctionConfigurationName,
       "iBMPSGAOLControlFunctionConfigurationIdentifier": iBMPSGAOLControlFunctionConfigurationIdentifier,
       "iBMPSGAOLControlFunctionConfigurationEnabled": iBMPSGAOLControlFunctionConfigurationEnabled}
)
