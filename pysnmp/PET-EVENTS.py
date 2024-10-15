# SNMP MIB module (PET-EVENTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PET-EVENTS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:31 2024
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

_Wiredformgmt_ObjectIdentity = ObjectIdentity
wiredformgmt = _Wiredformgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183)
)
_Pet_ObjectIdentity = ObjectIdentity
pet = _Pet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1)
)
_PetEvts_ObjectIdentity = ObjectIdentity
petEvts = _PetEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1)
)

# Managed Objects groups


# Notification objects

petTrapUnderTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65792)
)
if mibBuilder.loadTexts:
    petTrapUnderTemperatureWarning.setStatus(
        ""
    )

petTrapUnderTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65794)
)
if mibBuilder.loadTexts:
    petTrapUnderTemperatureCritical.setStatus(
        ""
    )

petTrapOverTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65799)
)
if mibBuilder.loadTexts:
    petTrapOverTemperatureWarning.setStatus(
        ""
    )

petTrapOverTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65801)
)
if mibBuilder.loadTexts:
    petTrapOverTemperatureCritical.setStatus(
        ""
    )

petTrapGenericCriticalTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 67330)
)
if mibBuilder.loadTexts:
    petTrapGenericCriticalTemperature.setStatus(
        ""
    )

petTrapGenericTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 67331)
)
if mibBuilder.loadTexts:
    petTrapGenericTemperatureWarning.setStatus(
        ""
    )

petTrapUnderAnalogVoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131330)
)
if mibBuilder.loadTexts:
    petTrapUnderAnalogVoltageCritical.setStatus(
        ""
    )

petTrapOverAnalogVoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131337)
)
if mibBuilder.loadTexts:
    petTrapOverAnalogVoltageCritical.setStatus(
        ""
    )

petTrapGenericCriticalDiscreteVoltage2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 132866)
)
if mibBuilder.loadTexts:
    petTrapGenericCriticalDiscreteVoltage2.setStatus(
        ""
    )

petTrapGenericDiscreteVoltageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 132867)
)
if mibBuilder.loadTexts:
    petTrapGenericDiscreteVoltageWarning.setStatus(
        ""
    )

petTrapFanSpeedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 262400)
)
if mibBuilder.loadTexts:
    petTrapFanSpeedWarning.setStatus(
        ""
    )

petTrapFanSpeedproblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 262402)
)
if mibBuilder.loadTexts:
    petTrapFanSpeedproblem.setStatus(
        ""
    )

petTrapGenericFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 263169)
)
if mibBuilder.loadTexts:
    petTrapGenericFanWarning.setStatus(
        ""
    )

petTrapGenericCriticalFan = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 263938)
)
if mibBuilder.loadTexts:
    petTrapGenericCriticalFan.setStatus(
        ""
    )

petTrapChassisIntrusion = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 356096)
)
if mibBuilder.loadTexts:
    petTrapChassisIntrusion.setStatus(
        ""
    )

petTrapProcessorInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487168)
)
if mibBuilder.loadTexts:
    petTrapProcessorInternalError.setStatus(
        ""
    )

petTrapProcessorThermalTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487169)
)
if mibBuilder.loadTexts:
    petTrapProcessorThermalTrip.setStatus(
        ""
    )

petTrapProcessorBistError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487170)
)
if mibBuilder.loadTexts:
    petTrapProcessorBistError.setStatus(
        ""
    )

petTrapProcessorFRB2Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487171)
)
if mibBuilder.loadTexts:
    petTrapProcessorFRB2Failure.setStatus(
        ""
    )

petTrapProcessorFRB3Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487172)
)
if mibBuilder.loadTexts:
    petTrapProcessorFRB3Failure.setStatus(
        ""
    )

petTrapPowerSupplyFailureDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552705)
)
if mibBuilder.loadTexts:
    petTrapPowerSupplyFailureDetected.setStatus(
        ""
    )

petTrapPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552706)
)
if mibBuilder.loadTexts:
    petTrapPowerSupplyWarning.setStatus(
        ""
    )

petTrapMemoryUncorrectableECC = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 814849)
)
if mibBuilder.loadTexts:
    petTrapMemoryUncorrectableECC.setStatus(
        ""
    )

petTrapBIOSPOSTCodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1011456)
)
if mibBuilder.loadTexts:
    petTrapBIOSPOSTCodeError.setStatus(
        ""
    )

petTrapOEMSystemBootEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1208065)
)
if mibBuilder.loadTexts:
    petTrapOEMSystemBootEvent.setStatus(
        ""
    )

petTrapCriticalInterruptBusTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1273601)
)
if mibBuilder.loadTexts:
    petTrapCriticalInterruptBusTimeout.setStatus(
        ""
    )

petTrapCriticalInterruptIOChannelNMI = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1273602)
)
if mibBuilder.loadTexts:
    petTrapCriticalInterruptIOChannelNMI.setStatus(
        ""
    )

petTrapCriticalInterruptSoftwareNMI = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1273603)
)
if mibBuilder.loadTexts:
    petTrapCriticalInterruptSoftwareNMI.setStatus(
        ""
    )

petTrapCriticalInterruptPCIPERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1273604)
)
if mibBuilder.loadTexts:
    petTrapCriticalInterruptPCIPERR.setStatus(
        ""
    )

petTrapCriticalInterruptPCISERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1273605)
)
if mibBuilder.loadTexts:
    petTrapCriticalInterruptPCISERR.setStatus(
        ""
    )

petTrapCriticalInterruptBusUncorrect = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1273608)
)
if mibBuilder.loadTexts:
    petTrapCriticalInterruptBusUncorrect.setStatus(
        ""
    )

petTrapCriticalInterruptFatalNMI = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1273609)
)
if mibBuilder.loadTexts:
    petTrapCriticalInterruptFatalNMI.setStatus(
        ""
    )

petTrapWatchdogReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322177)
)
if mibBuilder.loadTexts:
    petTrapWatchdogReset.setStatus(
        ""
    )

petTrapWatchdogPowerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322178)
)
if mibBuilder.loadTexts:
    petTrapWatchdogPowerDown.setStatus(
        ""
    )

petTrapWatchdogPowerCycle = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322179)
)
if mibBuilder.loadTexts:
    petTrapWatchdogPowerCycle.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PET-EVENTS",
    **{"wiredformgmt": wiredformgmt,
       "pet": pet,
       "petEvts": petEvts,
       "petTrapUnderTemperatureWarning": petTrapUnderTemperatureWarning,
       "petTrapUnderTemperatureCritical": petTrapUnderTemperatureCritical,
       "petTrapOverTemperatureWarning": petTrapOverTemperatureWarning,
       "petTrapOverTemperatureCritical": petTrapOverTemperatureCritical,
       "petTrapGenericCriticalTemperature": petTrapGenericCriticalTemperature,
       "petTrapGenericTemperatureWarning": petTrapGenericTemperatureWarning,
       "petTrapUnderAnalogVoltageCritical": petTrapUnderAnalogVoltageCritical,
       "petTrapOverAnalogVoltageCritical": petTrapOverAnalogVoltageCritical,
       "petTrapGenericCriticalDiscreteVoltage2": petTrapGenericCriticalDiscreteVoltage2,
       "petTrapGenericDiscreteVoltageWarning": petTrapGenericDiscreteVoltageWarning,
       "petTrapFanSpeedWarning": petTrapFanSpeedWarning,
       "petTrapFanSpeedproblem": petTrapFanSpeedproblem,
       "petTrapGenericFanWarning": petTrapGenericFanWarning,
       "petTrapGenericCriticalFan": petTrapGenericCriticalFan,
       "petTrapChassisIntrusion": petTrapChassisIntrusion,
       "petTrapProcessorInternalError": petTrapProcessorInternalError,
       "petTrapProcessorThermalTrip": petTrapProcessorThermalTrip,
       "petTrapProcessorBistError": petTrapProcessorBistError,
       "petTrapProcessorFRB2Failure": petTrapProcessorFRB2Failure,
       "petTrapProcessorFRB3Failure": petTrapProcessorFRB3Failure,
       "petTrapPowerSupplyFailureDetected": petTrapPowerSupplyFailureDetected,
       "petTrapPowerSupplyWarning": petTrapPowerSupplyWarning,
       "petTrapMemoryUncorrectableECC": petTrapMemoryUncorrectableECC,
       "petTrapBIOSPOSTCodeError": petTrapBIOSPOSTCodeError,
       "petTrapOEMSystemBootEvent": petTrapOEMSystemBootEvent,
       "petTrapCriticalInterruptBusTimeout": petTrapCriticalInterruptBusTimeout,
       "petTrapCriticalInterruptIOChannelNMI": petTrapCriticalInterruptIOChannelNMI,
       "petTrapCriticalInterruptSoftwareNMI": petTrapCriticalInterruptSoftwareNMI,
       "petTrapCriticalInterruptPCIPERR": petTrapCriticalInterruptPCIPERR,
       "petTrapCriticalInterruptPCISERR": petTrapCriticalInterruptPCISERR,
       "petTrapCriticalInterruptBusUncorrect": petTrapCriticalInterruptBusUncorrect,
       "petTrapCriticalInterruptFatalNMI": petTrapCriticalInterruptFatalNMI,
       "petTrapWatchdogReset": petTrapWatchdogReset,
       "petTrapWatchdogPowerDown": petTrapWatchdogPowerDown,
       "petTrapWatchdogPowerCycle": petTrapWatchdogPowerCycle}
)
