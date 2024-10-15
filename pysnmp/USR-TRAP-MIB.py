# SNMP MIB module (USR-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/USR-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:04 2024
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

(uchasEntityIndex,
 uchasEntityObjectID,
 uchasPowerSupplyIndex,
 uchasPowerSupplyOutNominalVolt,
 uchasPowerSupplyOutOfferedVolt,
 uchasSlotIndex,
 uchasSlotModuleType) = mibBuilder.importSymbols(
    "CHS-MIB",
    "uchasEntityIndex",
    "uchasEntityObjectID",
    "uchasPowerSupplyIndex",
    "uchasPowerSupplyOutNominalVolt",
    "uchasPowerSupplyOutOfferedVolt",
    "uchasSlotIndex",
    "uchasSlotModuleType")

(mdmCsCallDuration,
 mdmCsCallRefNum,
 mdmCsSecurityUserName) = mibBuilder.importSymbols(
    "MDM-MIB",
    "mdmCsCallDuration",
    "mdmCsCallRefNum",
    "mdmCsSecurityUserName")

(nmcArTrapId,
 nmcCfgLogSrvrSelect,
 nmcGmtime,
 nmcStatEventId,
 nmcStatTemperature,
 nmcTrapSequenceNumber) = mibBuilder.importSymbols(
    "NMC-MIB",
    "nmcArTrapId",
    "nmcCfgLogSrvrSelect",
    "nmcGmtime",
    "nmcStatEventId",
    "nmcStatTemperature",
    "nmcTrapSequenceNumber")

(pbSessionErrorStatus,
 pbSessionIndex) = mibBuilder.importSymbols(
    "PB-MIB",
    "pbSessionErrorStatus",
    "pbSessionIndex")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(uds1StatE1PhysicalState,) = mibBuilder.importSymbols(
    "UDS1-MIB",
    "uds1StatE1PhysicalState")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)

# Managed Objects groups


# Notification objects

moduleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 1)
)
moduleInserted.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasSlotModuleType"))
)
if mibBuilder.loadTexts:
    moduleInserted.setStatus(
        ""
    )

moduleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 2)
)
moduleRemoved.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasSlotModuleType"))
)
if mibBuilder.loadTexts:
    moduleRemoved.setStatus(
        ""
    )

psuWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 3)
)
psuWarning.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasPowerSupplyOutNominalVolt"),
        ("CHS-MIB", "uchasPowerSupplyOutOfferedVolt"))
)
if mibBuilder.loadTexts:
    psuWarning.setStatus(
        ""
    )

psuFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 4)
)
psuFailure.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasPowerSupplyIndex"))
)
if mibBuilder.loadTexts:
    psuFailure.setStatus(
        ""
    )

tempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 5)
)
tempWarning.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("NMC-MIB", "nmcStatTemperature"))
)
if mibBuilder.loadTexts:
    tempWarning.setStatus(
        ""
    )

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 6)
)
fanFailure.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"))
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        ""
    )

entityWatchdogTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 7)
)
entityWatchdogTimeout.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    entityWatchdogTimeout.setStatus(
        ""
    )

entityMgtBusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 8)
)
entityMgtBusFailure.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    entityMgtBusFailure.setStatus(
        ""
    )

incomingConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 9)
)
incomingConnectionEstablished.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    incomingConnectionEstablished.setStatus(
        ""
    )

outgoingConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 10)
)
outgoingConnectionEstablished.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    outgoingConnectionEstablished.setStatus(
        ""
    )

incomingConnectionTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 11)
)
incomingConnectionTerminated.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    incomingConnectionTerminated.setStatus(
        ""
    )

outgoingConnectionTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 12)
)
outgoingConnectionTerminated.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    outgoingConnectionTerminated.setStatus(
        ""
    )

connectAttemptFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 13)
)
connectAttemptFailure.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    connectAttemptFailure.setStatus(
        ""
    )

connectTimerExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 14)
)
connectTimerExpired.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    connectTimerExpired.setStatus(
        ""
    )

dteTransmitDataIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 15)
)
dteTransmitDataIdle.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    dteTransmitDataIdle.setStatus(
        ""
    )

dtrTrue = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 16)
)
dtrTrue.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    dtrTrue.setStatus(
        ""
    )

dtrFalse = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 17)
)
dtrFalse.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    dtrFalse.setStatus(
        ""
    )

blerCountAtThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 18)
)
blerCountAtThreshold.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    blerCountAtThreshold.setStatus(
        ""
    )

fallbackCountAtThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 19)
)
fallbackCountAtThreshold.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    fallbackCountAtThreshold.setStatus(
        ""
    )

noDialtone = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 20)
)
if mibBuilder.loadTexts:
    noDialtone.setStatus(
        ""
    )

noLoopCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 21)
)
noLoopCurrent.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    noLoopCurrent.setStatus(
        ""
    )

yellowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 22)
)
yellowAlarm.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    yellowAlarm.setStatus(
        ""
    )

redAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 23)
)
redAlarm.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    redAlarm.setStatus(
        ""
    )

lossOfSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 24)
)
lossOfSignal.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    lossOfSignal.setStatus(
        ""
    )

alarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 25)
)
alarmIndicationSignal.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    alarmIndicationSignal.setStatus(
        ""
    )

transmitTimingSourceSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 26)
)
transmitTimingSourceSwitch.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasSlotModuleType"))
)
if mibBuilder.loadTexts:
    transmitTimingSourceSwitch.setStatus(
        ""
    )

modemResetByDte = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 27)
)
modemResetByDte.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    modemResetByDte.setStatus(
        ""
    )

modemRingNoAnswer = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 28)
)
modemRingNoAnswer.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    modemRingNoAnswer.setStatus(
        ""
    )

dteRingNoAnswer = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 29)
)
dteRingNoAnswer.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    dteRingNoAnswer.setStatus(
        ""
    )

pktBusSessActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 30)
)
pktBusSessActive.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("PB-MIB", "pbSessionIndex"))
)
if mibBuilder.loadTexts:
    pktBusSessActive.setStatus(
        ""
    )

pktBusSessCongestion = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 31)
)
pktBusSessCongestion.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("PB-MIB", "pbSessionIndex"))
)
if mibBuilder.loadTexts:
    pktBusSessCongestion.setStatus(
        ""
    )

pktBusSessLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 32)
)
pktBusSessLost.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("PB-MIB", "pbSessionIndex"))
)
if mibBuilder.loadTexts:
    pktBusSessLost.setStatus(
        ""
    )

pktBusSessInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 33)
)
pktBusSessInactive.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("PB-MIB", "pbSessionIndex"))
)
if mibBuilder.loadTexts:
    pktBusSessInactive.setStatus(
        ""
    )

nacUserInterfaceReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 34)
)
nacUserInterfaceReset.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"))
)
if mibBuilder.loadTexts:
    nacUserInterfaceReset.setStatus(
        ""
    )

gwWanPortOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 35)
)
gwWanPortOutOfService.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"))
)
if mibBuilder.loadTexts:
    gwWanPortOutOfService.setStatus(
        ""
    )

gwWanPortLinkActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 36)
)
gwWanPortLinkActive.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"))
)
if mibBuilder.loadTexts:
    gwWanPortLinkActive.setStatus(
        ""
    )

dialOutLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 37)
)
dialOutLoginFail.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"))
)
if mibBuilder.loadTexts:
    dialOutLoginFail.setStatus(
        ""
    )

dialInLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 38)
)
dialInLoginFail.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"))
)
if mibBuilder.loadTexts:
    dialInLoginFail.setStatus(
        ""
    )

dialOutRestrictedNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 39)
)
dialOutRestrictedNum.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"))
)
if mibBuilder.loadTexts:
    dialOutRestrictedNum.setStatus(
        ""
    )

dialBackRestrictedNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 40)
)
dialBackRestrictedNum.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"))
)
if mibBuilder.loadTexts:
    dialBackRestrictedNum.setStatus(
        ""
    )

userBlacklisted = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 41)
)
userBlacklisted.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"))
)
if mibBuilder.loadTexts:
    userBlacklisted.setStatus(
        ""
    )

loginAttemptByBlacklistedUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 42)
)
loginAttemptByBlacklistedUser.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"))
)
if mibBuilder.loadTexts:
    loginAttemptByBlacklistedUser.setStatus(
        ""
    )

responseAttemptLimExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 43)
)
responseAttemptLimExceeded.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"))
)
if mibBuilder.loadTexts:
    responseAttemptLimExceeded.setStatus(
        ""
    )

mdmLoginAttemptLimExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 44)
)
mdmLoginAttemptLimExceeded.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"))
)
if mibBuilder.loadTexts:
    mdmLoginAttemptLimExceeded.setStatus(
        ""
    )

dialOutCallDuration = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 45)
)
dialOutCallDuration.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"),
        ("MDM-MIB", "mdmCsCallDuration"))
)
if mibBuilder.loadTexts:
    dialOutCallDuration.setStatus(
        ""
    )

dialInCallDuration = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 46)
)
dialInCallDuration.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("MDM-MIB", "mdmCsSecurityUserName"),
        ("MDM-MIB", "mdmCsCallDuration"))
)
if mibBuilder.loadTexts:
    dialInCallDuration.setStatus(
        ""
    )

pktBusSessError = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 47)
)
pktBusSessError.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("PB-MIB", "pbSessionIndex"),
        ("PB-MIB", "pbSessionErrorStatus"))
)
if mibBuilder.loadTexts:
    pktBusSessError.setStatus(
        ""
    )

nmcArCustomTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 48)
)
nmcArCustomTrap.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("NMC-MIB", "nmcArTrapId"))
)
if mibBuilder.loadTexts:
    nmcArCustomTrap.setStatus(
        ""
    )

acctSrvrLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 49)
)
acctSrvrLoss.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("NMC-MIB", "nmcCfgLogSrvrSelect"))
)
if mibBuilder.loadTexts:
    acctSrvrLoss.setStatus(
        ""
    )

yellowAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 50)
)
yellowAlarmClear.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    yellowAlarmClear.setStatus(
        ""
    )

redAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 51)
)
redAlarmClear.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    redAlarmClear.setStatus(
        ""
    )

lossOfSignalClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 52)
)
lossOfSignalClear.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    lossOfSignalClear.setStatus(
        ""
    )

alarmIndicationSignalClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 53)
)
alarmIndicationSignalClear.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    alarmIndicationSignalClear.setStatus(
        ""
    )

ctIncomingConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 54)
)
ctIncomingConnectionEstablished.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"),
        ("MDM-MIB", "mdmCsCallRefNum"))
)
if mibBuilder.loadTexts:
    ctIncomingConnectionEstablished.setStatus(
        ""
    )

ctOutgoingConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 55)
)
ctOutgoingConnectionEstablished.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"),
        ("MDM-MIB", "mdmCsCallRefNum"))
)
if mibBuilder.loadTexts:
    ctOutgoingConnectionEstablished.setStatus(
        ""
    )

ctIncomingConnectionTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 56)
)
ctIncomingConnectionTerminated.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"),
        ("MDM-MIB", "mdmCsCallRefNum"))
)
if mibBuilder.loadTexts:
    ctIncomingConnectionTerminated.setStatus(
        ""
    )

ctOutgoingConnectionTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 57)
)
ctOutgoingConnectionTerminated.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"),
        ("MDM-MIB", "mdmCsCallRefNum"))
)
if mibBuilder.loadTexts:
    ctOutgoingConnectionTerminated.setStatus(
        ""
    )

ctConnectAttemptFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 58)
)
ctConnectAttemptFailure.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"),
        ("MDM-MIB", "mdmCsCallRefNum"))
)
if mibBuilder.loadTexts:
    ctConnectAttemptFailure.setStatus(
        ""
    )

contCrcAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 59)
)
contCrcAlarm.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    contCrcAlarm.setStatus(
        ""
    )

contCrcAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 60)
)
contCrcAlarmClear.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"))
)
if mibBuilder.loadTexts:
    contCrcAlarmClear.setStatus(
        ""
    )

phyStateChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 429, 0, 61)
)
phyStateChng.setObjects(
      *(("NMC-MIB", "nmcTrapSequenceNumber"),
        ("NMC-MIB", "nmcStatEventId"),
        ("NMC-MIB", "nmcGmtime"),
        ("CHS-MIB", "uchasSlotIndex"),
        ("CHS-MIB", "uchasEntityIndex"),
        ("CHS-MIB", "uchasEntityObjectID"),
        ("UDS1-MIB", "uds1StatE1PhysicalState"))
)
if mibBuilder.loadTexts:
    phyStateChng.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "USR-TRAP-MIB",
    **{"usr": usr,
       "moduleInserted": moduleInserted,
       "moduleRemoved": moduleRemoved,
       "psuWarning": psuWarning,
       "psuFailure": psuFailure,
       "tempWarning": tempWarning,
       "fanFailure": fanFailure,
       "entityWatchdogTimeout": entityWatchdogTimeout,
       "entityMgtBusFailure": entityMgtBusFailure,
       "incomingConnectionEstablished": incomingConnectionEstablished,
       "outgoingConnectionEstablished": outgoingConnectionEstablished,
       "incomingConnectionTerminated": incomingConnectionTerminated,
       "outgoingConnectionTerminated": outgoingConnectionTerminated,
       "connectAttemptFailure": connectAttemptFailure,
       "connectTimerExpired": connectTimerExpired,
       "dteTransmitDataIdle": dteTransmitDataIdle,
       "dtrTrue": dtrTrue,
       "dtrFalse": dtrFalse,
       "blerCountAtThreshold": blerCountAtThreshold,
       "fallbackCountAtThreshold": fallbackCountAtThreshold,
       "noDialtone": noDialtone,
       "noLoopCurrent": noLoopCurrent,
       "yellowAlarm": yellowAlarm,
       "redAlarm": redAlarm,
       "lossOfSignal": lossOfSignal,
       "alarmIndicationSignal": alarmIndicationSignal,
       "transmitTimingSourceSwitch": transmitTimingSourceSwitch,
       "modemResetByDte": modemResetByDte,
       "modemRingNoAnswer": modemRingNoAnswer,
       "dteRingNoAnswer": dteRingNoAnswer,
       "pktBusSessActive": pktBusSessActive,
       "pktBusSessCongestion": pktBusSessCongestion,
       "pktBusSessLost": pktBusSessLost,
       "pktBusSessInactive": pktBusSessInactive,
       "nacUserInterfaceReset": nacUserInterfaceReset,
       "gwWanPortOutOfService": gwWanPortOutOfService,
       "gwWanPortLinkActive": gwWanPortLinkActive,
       "dialOutLoginFail": dialOutLoginFail,
       "dialInLoginFail": dialInLoginFail,
       "dialOutRestrictedNum": dialOutRestrictedNum,
       "dialBackRestrictedNum": dialBackRestrictedNum,
       "userBlacklisted": userBlacklisted,
       "loginAttemptByBlacklistedUser": loginAttemptByBlacklistedUser,
       "responseAttemptLimExceeded": responseAttemptLimExceeded,
       "mdmLoginAttemptLimExceeded": mdmLoginAttemptLimExceeded,
       "dialOutCallDuration": dialOutCallDuration,
       "dialInCallDuration": dialInCallDuration,
       "pktBusSessError": pktBusSessError,
       "nmcArCustomTrap": nmcArCustomTrap,
       "acctSrvrLoss": acctSrvrLoss,
       "yellowAlarmClear": yellowAlarmClear,
       "redAlarmClear": redAlarmClear,
       "lossOfSignalClear": lossOfSignalClear,
       "alarmIndicationSignalClear": alarmIndicationSignalClear,
       "ctIncomingConnectionEstablished": ctIncomingConnectionEstablished,
       "ctOutgoingConnectionEstablished": ctOutgoingConnectionEstablished,
       "ctIncomingConnectionTerminated": ctIncomingConnectionTerminated,
       "ctOutgoingConnectionTerminated": ctOutgoingConnectionTerminated,
       "ctConnectAttemptFailure": ctConnectAttemptFailure,
       "contCrcAlarm": contCrcAlarm,
       "contCrcAlarmClear": contCrcAlarmClear,
       "phyStateChng": phyStateChng}
)
