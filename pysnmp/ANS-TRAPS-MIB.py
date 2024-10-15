# SNMP MIB module (ANS-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANS-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:00 2024
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

(AlarmSeverity,
 AlarmType,
 InstancePointer) = mibBuilder.importSymbols(
    "ANS-ALARM-MIB",
    "AlarmSeverity",
    "AlarmType",
    "InstancePointer")

(DateAndTime,
 RowPointer,
 RowStatus,
 common,
 mlpmpR115) = mibBuilder.importSymbols(
    "ANS-COMMON-MIB",
    "DateAndTime",
    "RowPointer",
    "RowStatus",
    "common",
    "mlpmpR115")

(board,
 slot,
 subrack,
 systemNode) = mibBuilder.importSymbols(
    "ANS-EQUIPMENT-MIB",
    "board",
    "slot",
    "subrack",
    "systemNode")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysDescr,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysDescr",
    "sysLocation",
    "sysName")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 7)
)
_AnsIdentifier_Type = RowPointer
_AnsIdentifier_Object = MibScalar
ansIdentifier = _AnsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 7, 1),
    _AnsIdentifier_Type()
)
ansIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ansIdentifier.setStatus("mandatory")
_AlarmingObject_Type = InstancePointer
_AlarmingObject_Object = MibScalar
alarmingObject = _AlarmingObject_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 7, 11),
    _AlarmingObject_Type()
)
alarmingObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmingObject.setStatus("mandatory")
_AlarmType_Type = AlarmType
_AlarmType_Object = MibScalar
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 7, 12),
    _AlarmType_Type()
)
alarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmType.setStatus("mandatory")
_AlarmSeverity_Type = AlarmSeverity
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 7, 13),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("mandatory")
_AlarmTime_Type = DateAndTime
_AlarmTime_Object = MibScalar
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 7, 14),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmTime.setStatus("mandatory")
_AlarmInformation_Type = DisplayString
_AlarmInformation_Object = MibScalar
alarmInformation = _AlarmInformation_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 7, 15),
    _AlarmInformation_Type()
)
alarmInformation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmInformation.setStatus("mandatory")
_EventTime_Type = DateAndTime
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 7, 17),
    _EventTime_Type()
)
eventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTime.setStatus("mandatory")


class _NtId_Type(DisplayString):
    """Custom type ntId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtId_Type.__name__ = "DisplayString"
_NtId_Object = MibScalar
ntId = _NtId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 7, 18),
    _NtId_Type()
)
ntId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntId.setStatus("mandatory")

# Managed Objects groups


# Notification objects

systemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 0)
)
systemUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"),
        ("ANS-TRAPS-MIB", "eventTime"))
)
if mibBuilder.loadTexts:
    systemUp.setStatus(
        ""
    )

los = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 1)
)
los.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    los.setStatus(
        ""
    )

lof = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 2)
)
lof.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    lof.setStatus(
        ""
    )

lop = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 3)
)
lop.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    lop.setStatus(
        ""
    )

ais = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 4)
)
ais.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    ais.setStatus(
        ""
    )

rai = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 6)
)
rai.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    rai.setStatus(
        ""
    )

lossOfCellDelineation = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 8)
)
lossOfCellDelineation.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    lossOfCellDelineation.setStatus(
        ""
    )

protectionSchemeNotRespected = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 10)
)
protectionSchemeNotRespected.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"),
        ("ANS-TRAPS-MIB", "eventTime"))
)
if mibBuilder.loadTexts:
    protectionSchemeNotRespected.setStatus(
        ""
    )

rnSwitched = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 11)
)
rnSwitched.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"),
        ("ANS-TRAPS-MIB", "eventTime"))
)
if mibBuilder.loadTexts:
    rnSwitched.setStatus(
        ""
    )

subrackMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 31)
)
subrackMismatch.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    subrackMismatch.setStatus(
        ""
    )

subrackCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 32)
)
subrackCreated.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    subrackCreated.setStatus(
        ""
    )

systemNodeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 33)
)
systemNodeCreated.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    systemNodeCreated.setStatus(
        ""
    )

systemNodeDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 34)
)
systemNodeDeleted.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    systemNodeDeleted.setStatus(
        ""
    )

subrackDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 35)
)
subrackDeleted.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    subrackDeleted.setStatus(
        ""
    )

cbrQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 36)
)
cbrQueueFull.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    cbrQueueFull.setStatus(
        ""
    )

signOnComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 37)
)
signOnComplete.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    signOnComplete.setStatus(
        ""
    )

alarmDisturbance = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 38)
)
alarmDisturbance.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    alarmDisturbance.setStatus(
        ""
    )

selfTestOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 39)
)
selfTestOk.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    selfTestOk.setStatus(
        ""
    )

selfTestFailedOnRadio = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 40)
)
selfTestFailedOnRadio.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    selfTestFailedOnRadio.setStatus(
        ""
    )

radioTxOffFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 52)
)
radioTxOffFail.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioTxOffFail.setStatus(
        ""
    )

radioRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 53)
)
radioRestart.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioRestart.setStatus(
        ""
    )

swDownloadFailureRadio = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 54)
)
swDownloadFailureRadio.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    swDownloadFailureRadio.setStatus(
        ""
    )

swDownloadFailureModem = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 55)
)
swDownloadFailureModem.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    swDownloadFailureModem.setStatus(
        ""
    )

incorrectSwVersModem = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 56)
)
incorrectSwVersModem.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    incorrectSwVersModem.setStatus(
        ""
    )

systemAudit = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 57)
)
systemAudit.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"),
        ("ANS-TRAPS-MIB", "eventTime"))
)
if mibBuilder.loadTexts:
    systemAudit.setStatus(
        ""
    )

incorrectSwVersRadio = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 58)
)
incorrectSwVersRadio.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    incorrectSwVersRadio.setStatus(
        ""
    )

swdlFromActiveToModemInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 59)
)
swdlFromActiveToModemInProgress.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    swdlFromActiveToModemInProgress.setStatus(
        ""
    )

mcnWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 60)
)
mcnWarning.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    mcnWarning.setStatus(
        ""
    )

lossOfNetSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 61)
)
lossOfNetSync.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    lossOfNetSync.setStatus(
        ""
    )

externalAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 62)
)
externalAlarm1.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    externalAlarm1.setStatus(
        ""
    )

atControlChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 63)
)
atControlChannel.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    atControlChannel.setStatus(
        ""
    )

externalAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 64)
)
externalAlarm2.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    externalAlarm2.setStatus(
        ""
    )

suMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 65)
)
suMismatch.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    suMismatch.setStatus(
        ""
    )

suPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 66)
)
suPowerFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    suPowerFailure.setStatus(
        ""
    )

suInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 67)
)
suInitFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    suInitFailure.setStatus(
        ""
    )

suUnsupportedType = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 68)
)
suUnsupportedType.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    suUnsupportedType.setStatus(
        ""
    )

suHwFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 69)
)
suHwFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    suHwFailure.setStatus(
        ""
    )

radioTxLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 70)
)
radioTxLos.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioTxLos.setStatus(
        ""
    )

radioRfOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 71)
)
radioRfOut.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioRfOut.setStatus(
        ""
    )

radioTxFreq = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 72)
)
radioTxFreq.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioTxFreq.setStatus(
        ""
    )

radioRxIfc = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 73)
)
radioRxIfc.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioRxIfc.setStatus(
        ""
    )

radioRxFreq = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 74)
)
radioRxFreq.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioRxFreq.setStatus(
        ""
    )

swdlFromActiveToRadioInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 75)
)
swdlFromActiveToRadioInProgress.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    swdlFromActiveToRadioInProgress.setStatus(
        ""
    )

radioHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 76)
)
radioHighTemperature.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioHighTemperature.setStatus(
        ""
    )

radioTxOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 77)
)
radioTxOn.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioTxOn.setStatus(
        ""
    )

radioVco = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 78)
)
radioVco.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioVco.setStatus(
        ""
    )

radioTxLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 79)
)
radioTxLevel.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioTxLevel.setStatus(
        ""
    )

swdlFromPassiveToModemInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 80)
)
swdlFromPassiveToModemInProgress.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    swdlFromPassiveToModemInProgress.setStatus(
        ""
    )

swdlFromPassiveToRadioInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 81)
)
swdlFromPassiveToRadioInProgress.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    swdlFromPassiveToRadioInProgress.setStatus(
        ""
    )

modemRauPow = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 82)
)
modemRauPow.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemRauPow.setStatus(
        ""
    )

modemLofTdm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 83)
)
modemLofTdm.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemLofTdm.setStatus(
        ""
    )

radioMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 84)
)
radioMismatch.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioMismatch.setStatus(
        ""
    )

modemModInd = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 85)
)
modemModInd.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemModInd.setStatus(
        ""
    )

modemSwException = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 86)
)
modemSwException.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemSwException.setStatus(
        ""
    )

modemHwException = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 87)
)
modemHwException.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemHwException.setStatus(
        ""
    )

modemControlChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 88)
)
modemControlChannel.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemControlChannel.setStatus(
        ""
    )

modemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 89)
)
modemRestart.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemRestart.setStatus(
        ""
    )

ethernetLossOfCarrier = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 90)
)
ethernetLossOfCarrier.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    ethernetLossOfCarrier.setStatus(
        ""
    )

aal1Starvation = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 91)
)
aal1Starvation.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    aal1Starvation.setStatus(
        ""
    )

lossOfRefClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 92)
)
lossOfRefClock.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    lossOfRefClock.setStatus(
        ""
    )

radioIrsLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 94)
)
radioIrsLoss.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioIrsLoss.setStatus(
        ""
    )

lofMf = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 95)
)
lofMf.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    lofMf.setStatus(
        ""
    )

selfTestFailedOnModem = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 96)
)
selfTestFailedOnModem.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    selfTestFailedOnModem.setStatus(
        ""
    )

diskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 97)
)
diskFull.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    diskFull.setStatus(
        ""
    )

hwFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 98)
)
hwFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    hwFailure.setStatus(
        ""
    )

suRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 99)
)
suRemoved.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    suRemoved.setStatus(
        ""
    )

modemEberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 100)
)
modemEberUp.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemEberUp.setStatus(
        ""
    )

modemEberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 101)
)
modemEberDown.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemEberDown.setStatus(
        ""
    )

modemRxlFinUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 102)
)
modemRxlFinUp.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemRxlFinUp.setStatus(
        ""
    )

modemRxlFinDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 103)
)
modemRxlFinDown.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    modemRxlFinDown.setStatus(
        ""
    )

radioTxVco = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 104)
)
radioTxVco.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioTxVco.setStatus(
        ""
    )

aal1SarFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 106)
)
aal1SarFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    aal1SarFailure.setStatus(
        ""
    )

masterLinkSwitched = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 107)
)
masterLinkSwitched.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"),
        ("ANS-TRAPS-MIB", "eventTime"))
)
if mibBuilder.loadTexts:
    masterLinkSwitched.setStatus(
        ""
    )

licenseCapacityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 108)
)
licenseCapacityEvent.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"),
        ("ANS-TRAPS-MIB", "eventTime"))
)
if mibBuilder.loadTexts:
    licenseCapacityEvent.setStatus(
        ""
    )

licenseExpirationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 109)
)
licenseExpirationEvent.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"),
        ("ANS-TRAPS-MIB", "eventTime"))
)
if mibBuilder.loadTexts:
    licenseExpirationEvent.setStatus(
        ""
    )

hostidMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 110)
)
hostidMismatch.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"),
        ("ANS-TRAPS-MIB", "eventTime"))
)
if mibBuilder.loadTexts:
    hostidMismatch.setStatus(
        ""
    )

radioFrequencyMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 0, 111)
)
radioFrequencyMismatch.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    radioFrequencyMismatch.setStatus(
        ""
    )

cellbusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 0, 5)
)
cellbusFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    cellbusFailure.setStatus(
        ""
    )

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 0, 6)
)
fanFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        ""
    )

powerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 0, 7)
)
powerFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    powerFailure.setStatus(
        ""
    )

communicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 0, 1)
)
communicationLost.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    communicationLost.setStatus(
        ""
    )

boardReplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 0, 2)
)
boardReplaced.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    boardReplaced.setStatus(
        ""
    )

boardRemovedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 0, 4)
)
boardRemovedAlarm.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    boardRemovedAlarm.setStatus(
        ""
    )

boardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 0, 6)
)
boardMismatch.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    boardMismatch.setStatus(
        ""
    )

boardUnrecognized = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 0, 7)
)
boardUnrecognized.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    boardUnrecognized.setStatus(
        ""
    )

powerLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 0, 8)
)
powerLoss.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    powerLoss.setStatus(
        ""
    )

interfaceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 0, 9)
)
interfaceFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    interfaceFailure.setStatus(
        ""
    )

macSignonFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 0, 12)
)
macSignonFailed.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macSignonFailed.setStatus(
        ""
    )

communicationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 9)
)
communicationError.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    communicationError.setStatus(
        ""
    )

startError = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 12)
)
startError.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    startError.setStatus(
        ""
    )

laserPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 13)
)
laserPower.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    laserPower.setStatus(
        ""
    )

dpSoftwareFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 15)
)
dpSoftwareFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    dpSoftwareFailure.setStatus(
        ""
    )

bufferOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 16)
)
bufferOverflow.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    bufferOverflow.setStatus(
        ""
    )

bufferUnderflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 17)
)
bufferUnderflow.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    bufferUnderflow.setStatus(
        ""
    )

macModemSwDownloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 18)
)
macModemSwDownloadFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macModemSwDownloadFailure.setStatus(
        ""
    )

downLoadLmFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 19)
)
downLoadLmFailed.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    downLoadLmFailed.setStatus(
        ""
    )

macRadioSwDownloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 20)
)
macRadioSwDownloadFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macRadioSwDownloadFailure.setStatus(
        ""
    )

incorrectSwVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 21)
)
incorrectSwVersion.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    incorrectSwVersion.setStatus(
        ""
    )

loopBackFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 22)
)
loopBackFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    loopBackFailure.setStatus(
        ""
    )

vpAis = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 23)
)
vpAis.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    vpAis.setStatus(
        ""
    )

vpRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 24)
)
vpRdi.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    vpRdi.setStatus(
        ""
    )

softwareDownloadInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 25)
)
softwareDownloadInProgress.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    softwareDownloadInProgress.setStatus(
        ""
    )

softwareDownloadDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 26)
)
softwareDownloadDone.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    softwareDownloadDone.setStatus(
        ""
    )

msAis = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 27)
)
msAis.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    msAis.setStatus(
        ""
    )

msRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 28)
)
msRdi.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    msRdi.setStatus(
        ""
    )

pathRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 29)
)
pathRdi.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    pathRdi.setStatus(
        ""
    )

pathAis = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 30)
)
pathAis.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    pathAis.setStatus(
        ""
    )

macControlChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 37)
)
macControlChannel.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macControlChannel.setStatus(
        ""
    )

macRclFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 38)
)
macRclFailure.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macRclFailure.setStatus(
        ""
    )

macCbrOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 39)
)
macCbrOverflow.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macCbrOverflow.setStatus(
        ""
    )

macSwException = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 40)
)
macSwException.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macSwException.setStatus(
        ""
    )

macHwException = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 41)
)
macHwException.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macHwException.setStatus(
        ""
    )

macIncorrSwVersModem = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 42)
)
macIncorrSwVersModem.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macIncorrSwVersModem.setStatus(
        ""
    )

macIncorrSwVersRadio = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 43)
)
macIncorrSwVersRadio.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macIncorrSwVersRadio.setStatus(
        ""
    )

macSwdlFromActiveToModemInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 44)
)
macSwdlFromActiveToModemInProgress.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macSwdlFromActiveToModemInProgress.setStatus(
        ""
    )

macSwdlFromActiveToRadioInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 45)
)
macSwdlFromActiveToRadioInProgress.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macSwdlFromActiveToRadioInProgress.setStatus(
        ""
    )

atRollbacked = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 46)
)
atRollbacked.setObjects(
      *(("ANS-TRAPS-MIB", "ansIdentifier"),
        ("ANS-TRAPS-MIB", "eventTime"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    atRollbacked.setStatus(
        ""
    )

macSwdlFromPassiveToModemInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 47)
)
macSwdlFromPassiveToModemInProgress.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macSwdlFromPassiveToModemInProgress.setStatus(
        ""
    )

macSwdlFromPassiveToRadioInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 48)
)
macSwdlFromPassiveToRadioInProgress.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macSwdlFromPassiveToRadioInProgress.setStatus(
        ""
    )

macKeepAliveFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 49)
)
macKeepAliveFail.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macKeepAliveFail.setStatus(
        ""
    )

macRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 50)
)
macRestart.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macRestart.setStatus(
        ""
    )

macModemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 0, 51)
)
macModemRestart.setObjects(
      *(("ANS-TRAPS-MIB", "alarmingObject"),
        ("ANS-TRAPS-MIB", "alarmType"),
        ("ANS-TRAPS-MIB", "alarmSeverity"),
        ("ANS-TRAPS-MIB", "alarmTime"),
        ("ANS-TRAPS-MIB", "alarmInformation"),
        ("ANS-TRAPS-MIB", "ntId"))
)
if mibBuilder.loadTexts:
    macModemRestart.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANS-TRAPS-MIB",
    **{"systemUp": systemUp,
       "los": los,
       "lof": lof,
       "lop": lop,
       "ais": ais,
       "rai": rai,
       "lossOfCellDelineation": lossOfCellDelineation,
       "protectionSchemeNotRespected": protectionSchemeNotRespected,
       "rnSwitched": rnSwitched,
       "subrackMismatch": subrackMismatch,
       "subrackCreated": subrackCreated,
       "systemNodeCreated": systemNodeCreated,
       "systemNodeDeleted": systemNodeDeleted,
       "subrackDeleted": subrackDeleted,
       "cbrQueueFull": cbrQueueFull,
       "signOnComplete": signOnComplete,
       "alarmDisturbance": alarmDisturbance,
       "selfTestOk": selfTestOk,
       "selfTestFailedOnRadio": selfTestFailedOnRadio,
       "radioTxOffFail": radioTxOffFail,
       "radioRestart": radioRestart,
       "swDownloadFailureRadio": swDownloadFailureRadio,
       "swDownloadFailureModem": swDownloadFailureModem,
       "incorrectSwVersModem": incorrectSwVersModem,
       "systemAudit": systemAudit,
       "incorrectSwVersRadio": incorrectSwVersRadio,
       "swdlFromActiveToModemInProgress": swdlFromActiveToModemInProgress,
       "mcnWarning": mcnWarning,
       "lossOfNetSync": lossOfNetSync,
       "externalAlarm1": externalAlarm1,
       "atControlChannel": atControlChannel,
       "externalAlarm2": externalAlarm2,
       "suMismatch": suMismatch,
       "suPowerFailure": suPowerFailure,
       "suInitFailure": suInitFailure,
       "suUnsupportedType": suUnsupportedType,
       "suHwFailure": suHwFailure,
       "radioTxLos": radioTxLos,
       "radioRfOut": radioRfOut,
       "radioTxFreq": radioTxFreq,
       "radioRxIfc": radioRxIfc,
       "radioRxFreq": radioRxFreq,
       "swdlFromActiveToRadioInProgress": swdlFromActiveToRadioInProgress,
       "radioHighTemperature": radioHighTemperature,
       "radioTxOn": radioTxOn,
       "radioVco": radioVco,
       "radioTxLevel": radioTxLevel,
       "swdlFromPassiveToModemInProgress": swdlFromPassiveToModemInProgress,
       "swdlFromPassiveToRadioInProgress": swdlFromPassiveToRadioInProgress,
       "modemRauPow": modemRauPow,
       "modemLofTdm": modemLofTdm,
       "radioMismatch": radioMismatch,
       "modemModInd": modemModInd,
       "modemSwException": modemSwException,
       "modemHwException": modemHwException,
       "modemControlChannel": modemControlChannel,
       "modemRestart": modemRestart,
       "ethernetLossOfCarrier": ethernetLossOfCarrier,
       "aal1Starvation": aal1Starvation,
       "lossOfRefClock": lossOfRefClock,
       "radioIrsLoss": radioIrsLoss,
       "lofMf": lofMf,
       "selfTestFailedOnModem": selfTestFailedOnModem,
       "diskFull": diskFull,
       "hwFailure": hwFailure,
       "suRemoved": suRemoved,
       "modemEberUp": modemEberUp,
       "modemEberDown": modemEberDown,
       "modemRxlFinUp": modemRxlFinUp,
       "modemRxlFinDown": modemRxlFinDown,
       "radioTxVco": radioTxVco,
       "aal1SarFailure": aal1SarFailure,
       "masterLinkSwitched": masterLinkSwitched,
       "licenseCapacityEvent": licenseCapacityEvent,
       "licenseExpirationEvent": licenseExpirationEvent,
       "hostidMismatch": hostidMismatch,
       "radioFrequencyMismatch": radioFrequencyMismatch,
       "cellbusFailure": cellbusFailure,
       "fanFailure": fanFailure,
       "powerFailure": powerFailure,
       "communicationLost": communicationLost,
       "boardReplaced": boardReplaced,
       "boardRemovedAlarm": boardRemovedAlarm,
       "boardMismatch": boardMismatch,
       "boardUnrecognized": boardUnrecognized,
       "powerLoss": powerLoss,
       "interfaceFailure": interfaceFailure,
       "macSignonFailed": macSignonFailed,
       "communicationError": communicationError,
       "startError": startError,
       "laserPower": laserPower,
       "dpSoftwareFailure": dpSoftwareFailure,
       "bufferOverflow": bufferOverflow,
       "bufferUnderflow": bufferUnderflow,
       "macModemSwDownloadFailure": macModemSwDownloadFailure,
       "downLoadLmFailed": downLoadLmFailed,
       "macRadioSwDownloadFailure": macRadioSwDownloadFailure,
       "incorrectSwVersion": incorrectSwVersion,
       "loopBackFailure": loopBackFailure,
       "vpAis": vpAis,
       "vpRdi": vpRdi,
       "softwareDownloadInProgress": softwareDownloadInProgress,
       "softwareDownloadDone": softwareDownloadDone,
       "msAis": msAis,
       "msRdi": msRdi,
       "pathRdi": pathRdi,
       "pathAis": pathAis,
       "macControlChannel": macControlChannel,
       "macRclFailure": macRclFailure,
       "macCbrOverflow": macCbrOverflow,
       "macSwException": macSwException,
       "macHwException": macHwException,
       "macIncorrSwVersModem": macIncorrSwVersModem,
       "macIncorrSwVersRadio": macIncorrSwVersRadio,
       "macSwdlFromActiveToModemInProgress": macSwdlFromActiveToModemInProgress,
       "macSwdlFromActiveToRadioInProgress": macSwdlFromActiveToRadioInProgress,
       "atRollbacked": atRollbacked,
       "macSwdlFromPassiveToModemInProgress": macSwdlFromPassiveToModemInProgress,
       "macSwdlFromPassiveToRadioInProgress": macSwdlFromPassiveToRadioInProgress,
       "macKeepAliveFail": macKeepAliveFail,
       "macRestart": macRestart,
       "macModemRestart": macModemRestart,
       "traps": traps,
       "ansIdentifier": ansIdentifier,
       "alarmingObject": alarmingObject,
       "alarmType": alarmType,
       "alarmSeverity": alarmSeverity,
       "alarmTime": alarmTime,
       "alarmInformation": alarmInformation,
       "eventTime": eventTime,
       "ntId": ntId}
)
