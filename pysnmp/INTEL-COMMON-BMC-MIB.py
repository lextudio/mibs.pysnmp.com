# SNMP MIB module (INTEL-COMMON-BMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-COMMON-BMC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:32 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wired_for_management_ObjectIdentity = ObjectIdentity
wired_for_management = _Wired_for_management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183)
)
_Pet_ObjectIdentity = ObjectIdentity
pet = _Pet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1)
)
_Pet_events_ObjectIdentity = ObjectIdentity
pet_events = _Pet_events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1)
)

# Managed Objects groups


# Notification objects

tempUpperNonCriticalGoingHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65799)
)
if mibBuilder.loadTexts:
    tempUpperNonCriticalGoingHigh.setStatus(
        ""
    )

tempUpperCriticalGoingHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65801)
)
if mibBuilder.loadTexts:
    tempUpperCriticalGoingHigh.setStatus(
        ""
    )

voltageLowerNonCriticalGoingLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131328)
)
if mibBuilder.loadTexts:
    voltageLowerNonCriticalGoingLow.setStatus(
        ""
    )

voltageLowerCriticalGoingLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131330)
)
if mibBuilder.loadTexts:
    voltageLowerCriticalGoingLow.setStatus(
        ""
    )

voltageUpperNonCriticalGoingHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131335)
)
if mibBuilder.loadTexts:
    voltageUpperNonCriticalGoingHigh.setStatus(
        ""
    )

voltageUpperCriticalGoingHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131337)
)
if mibBuilder.loadTexts:
    voltageUpperCriticalGoingHigh.setStatus(
        ""
    )

smiTimeoutError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 258817)
)
if mibBuilder.loadTexts:
    smiTimeoutError.setStatus(
        ""
    )

fanFailureLowerNonCriticalGoingLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 262400)
)
if mibBuilder.loadTexts:
    fanFailureLowerNonCriticalGoingLow.setStatus(
        ""
    )

fanFailureLowerCriticalGoingLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 262402)
)
if mibBuilder.loadTexts:
    fanFailureLowerCriticalGoingLow.setStatus(
        ""
    )

chassisIntrusionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 356096)
)
if mibBuilder.loadTexts:
    chassisIntrusionEvent.setStatus(
        ""
    )

chassisIntrusionEventLANLeashLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 356100)
)
if mibBuilder.loadTexts:
    chassisIntrusionEventLANLeashLost.setStatus(
        ""
    )

procDisabledError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 459521)
)
if mibBuilder.loadTexts:
    procDisabledError.setStatus(
        ""
    )

thermalTripError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487169)
)
if mibBuilder.loadTexts:
    thermalTripError.setStatus(
        ""
    )

cpuPresence = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487175)
)
if mibBuilder.loadTexts:
    cpuPresence.setStatus(
        ""
    )

powerSupplyPresence = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552704)
)
if mibBuilder.loadTexts:
    powerSupplyPresence.setStatus(
        ""
    )

powerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552705)
)
if mibBuilder.loadTexts:
    powerSupplyFailure.setStatus(
        ""
    )

powerSupplyPredictiveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552706)
)
if mibBuilder.loadTexts:
    powerSupplyPredictiveFailure.setStatus(
        ""
    )

powerSupplyACLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552707)
)
if mibBuilder.loadTexts:
    powerSupplyACLost.setStatus(
        ""
    )

powerSupplyConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552710)
)
if mibBuilder.loadTexts:
    powerSupplyConfigurationError.setStatus(
        ""
    )

powerOffPowerUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 618240)
)
if mibBuilder.loadTexts:
    powerOffPowerUnit.setStatus(
        ""
    )

acLostPowerUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 618244)
)
if mibBuilder.loadTexts:
    acLostPowerUnit.setStatus(
        ""
    )

softPowerControlPowerUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 618245)
)
if mibBuilder.loadTexts:
    softPowerControlPowerUnit.setStatus(
        ""
    )

powerUnitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 618246)
)
if mibBuilder.loadTexts:
    powerUnitFailure.setStatus(
        ""
    )

uncorrectableECCError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 814849)
)
if mibBuilder.loadTexts:
    uncorrectableECCError.setStatus(
        ""
    )

drivePresence = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 880384)
)
if mibBuilder.loadTexts:
    drivePresence.setStatus(
        ""
    )

driveFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 880385)
)
if mibBuilder.loadTexts:
    driveFault.setStatus(
        ""
    )

drivePredictiveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 880386)
)
if mibBuilder.loadTexts:
    drivePredictiveFailure.setStatus(
        ""
    )

driveRebuild = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 880391)
)
if mibBuilder.loadTexts:
    driveRebuild.setStatus(
        ""
    )

postError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1011456)
)
if mibBuilder.loadTexts:
    postError.setStatus(
        ""
    )

selLogAreaReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1076994)
)
if mibBuilder.loadTexts:
    selLogAreaReset.setStatus(
        ""
    )

oemSystemBootEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1208065)
)
if mibBuilder.loadTexts:
    oemSystemBootEvent.setStatus(
        ""
    )

fatalNMIError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1273600)
)
if mibBuilder.loadTexts:
    fatalNMIError.setStatus(
        ""
    )

timerExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322176)
)
if mibBuilder.loadTexts:
    timerExpired.setStatus(
        ""
    )

hardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322177)
)
if mibBuilder.loadTexts:
    hardReset.setStatus(
        ""
    )

powerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322178)
)
if mibBuilder.loadTexts:
    powerDown.setStatus(
        ""
    )

powerReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322179)
)
if mibBuilder.loadTexts:
    powerReset.setStatus(
        ""
    )

timerInterrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322184)
)
if mibBuilder.loadTexts:
    timerInterrupt.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-COMMON-BMC-MIB",
    **{"wired-for-management": wired_for_management,
       "pet": pet,
       "pet-events": pet_events,
       "tempUpperNonCriticalGoingHigh": tempUpperNonCriticalGoingHigh,
       "tempUpperCriticalGoingHigh": tempUpperCriticalGoingHigh,
       "voltageLowerNonCriticalGoingLow": voltageLowerNonCriticalGoingLow,
       "voltageLowerCriticalGoingLow": voltageLowerCriticalGoingLow,
       "voltageUpperNonCriticalGoingHigh": voltageUpperNonCriticalGoingHigh,
       "voltageUpperCriticalGoingHigh": voltageUpperCriticalGoingHigh,
       "smiTimeoutError": smiTimeoutError,
       "fanFailureLowerNonCriticalGoingLow": fanFailureLowerNonCriticalGoingLow,
       "fanFailureLowerCriticalGoingLow": fanFailureLowerCriticalGoingLow,
       "chassisIntrusionEvent": chassisIntrusionEvent,
       "chassisIntrusionEventLANLeashLost": chassisIntrusionEventLANLeashLost,
       "procDisabledError": procDisabledError,
       "thermalTripError": thermalTripError,
       "cpuPresence": cpuPresence,
       "powerSupplyPresence": powerSupplyPresence,
       "powerSupplyFailure": powerSupplyFailure,
       "powerSupplyPredictiveFailure": powerSupplyPredictiveFailure,
       "powerSupplyACLost": powerSupplyACLost,
       "powerSupplyConfigurationError": powerSupplyConfigurationError,
       "powerOffPowerUnit": powerOffPowerUnit,
       "acLostPowerUnit": acLostPowerUnit,
       "softPowerControlPowerUnit": softPowerControlPowerUnit,
       "powerUnitFailure": powerUnitFailure,
       "uncorrectableECCError": uncorrectableECCError,
       "drivePresence": drivePresence,
       "driveFault": driveFault,
       "drivePredictiveFailure": drivePredictiveFailure,
       "driveRebuild": driveRebuild,
       "postError": postError,
       "selLogAreaReset": selLogAreaReset,
       "oemSystemBootEvent": oemSystemBootEvent,
       "fatalNMIError": fatalNMIError,
       "timerExpired": timerExpired,
       "hardReset": hardReset,
       "powerDown": powerDown,
       "powerReset": powerReset,
       "timerInterrupt": timerInterrupt}
)
