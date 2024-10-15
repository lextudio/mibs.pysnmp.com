# SNMP MIB module (SPIDCOM-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SPIDCOM-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:20 2024
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

(neMibAlarm,) = mibBuilder.importSymbols(
    "NE-ALARM-MIB",
    "neMibAlarm")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

neAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ItuAlarmProbableCause(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("adapterError", 2),
          ("applicationSubsystemFailure", 3),
          ("authenticationFailure", 59),
          ("bandwidthReduced", 4),
          ("breachOfConfidentiality", 60),
          ("cableTamper", 61),
          ("callEstablishmentError", 5),
          ("communicationsProtocolError", 6),
          ("communicationsSubsystemFailure", 7),
          ("configurationOrCustomizationError", 8),
          ("congestion", 9),
          ("corruptData", 10),
          ("cpuCyclesLimitExceeded", 11),
          ("dataSetOrModemError", 12),
          ("degradedSignal", 13),
          ("delayedInformation", 62),
          ("denialOfService", 63),
          ("dteDceInterfaceError", 14),
          ("duplicateInformation", 64),
          ("enclosureDoorOpen", 15),
          ("equipmentMalfunction", 16),
          ("excessiveVibration", 17),
          ("fileError", 18),
          ("fireDetected", 19),
          ("floodDetected", 20),
          ("framingError", 21),
          ("heatingVentCoolingSystemProblem", 22),
          ("humidityUnacceptable", 23),
          ("informationMissing", 65),
          ("informationModificationDetected", 66),
          ("informationOutOfSequence", 67),
          ("inputDeviceError", 25),
          ("inputOutputDeviceError", 24),
          ("intrusionDetection", 68),
          ("keyExpired", 69),
          ("lanError", 26),
          ("leakDetected", 27),
          ("localNodeTransmissionError", 28),
          ("lossOfFrame", 29),
          ("lossOfSignal", 30),
          ("materialSupplyExhausted", 31),
          ("multiplexerProblem", 32),
          ("nonRepudiationFailure", 70),
          ("other", 1),
          ("ouputDeviceError", 34),
          ("outOfHoursActivity", 71),
          ("outOfMemory", 33),
          ("outOfService", 72),
          ("performanceDegraded", 35),
          ("powerProblem", 36),
          ("pressureUnacceptable", 37),
          ("proceduralError", 73),
          ("processorProblem", 38),
          ("pumpFailure", 39),
          ("queueSizeExceeded", 40),
          ("receiveFailure", 41),
          ("receiverFailure", 42),
          ("remoteNodeTransmissionError", 43),
          ("resourceAtOrNearingCapacity", 44),
          ("responseTimeExecessive", 45),
          ("retransmissionRateExcessive", 46),
          ("softwareError", 47),
          ("softwareProgramAbnormallyTerminated", 48),
          ("softwareProgramError", 49),
          ("storageCapacityProblem", 50),
          ("temperatureUnacceptable", 51),
          ("thresholdCrossed", 52),
          ("timingProblem", 53),
          ("toxicLeakDetected", 54),
          ("transmitFailure", 55),
          ("transmitterFailure", 56),
          ("unauthorizedAccessAttempt", 74),
          ("underlyingResourceUnavailable", 57),
          ("unexpectedInformation", 75),
          ("versionMismatch", 58))
    )



class ItuAlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("communicationsAlarm", 2),
          ("environmentalAlarm", 6),
          ("equipmentAlarm", 5),
          ("integrityViolation", 7),
          ("operationalViolation", 8),
          ("other", 1),
          ("physicalViolation", 9),
          ("processingErrorAlarm", 4),
          ("qualityOfServiceAlarm", 3),
          ("securityServiceOrMechanismViolation", 10),
          ("timeDomainViolation", 11))
    )



class NeAlarmPhoto(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("takePhoto", 1)
    )



class NeTrapFilter(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trapFilterOff", 0),
          ("trapFilterOn", 1))
    )



# MIB Managed Objects in the order of their OIDs

_NeAlarmTable_Object = MibTable
neAlarmTable = _NeAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1)
)
if mibBuilder.loadTexts:
    neAlarmTable.setStatus("current")
_NeAlarmEntry_Object = MibTableRow
neAlarmEntry = _NeAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1)
)
neAlarmEntry.setIndexNames(
    (0, "SPIDCOM-ALARM-MIB", "neAlarmIndex"),
)
if mibBuilder.loadTexts:
    neAlarmEntry.setStatus("current")
_NeAlarmIndex_Type = Unsigned32
_NeAlarmIndex_Object = MibTableColumn
neAlarmIndex = _NeAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 1),
    _NeAlarmIndex_Type()
)
neAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmIndex.setStatus("current")
_NeAlarmAdditionalText_Type = DisplayString
_NeAlarmAdditionalText_Object = MibTableColumn
neAlarmAdditionalText = _NeAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 2),
    _NeAlarmAdditionalText_Type()
)
neAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmAdditionalText.setStatus("current")
_NeAlarmProbableCause_Type = ItuAlarmProbableCause
_NeAlarmProbableCause_Object = MibTableColumn
neAlarmProbableCause = _NeAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 3),
    _NeAlarmProbableCause_Type()
)
neAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmProbableCause.setStatus("current")
_NeAlarmDescription_Type = DisplayString
_NeAlarmDescription_Object = MibTableColumn
neAlarmDescription = _NeAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 4),
    _NeAlarmDescription_Type()
)
neAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmDescription.setStatus("current")
_NeAlarmType_Type = ItuAlarmType
_NeAlarmType_Object = MibTableColumn
neAlarmType = _NeAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 5),
    _NeAlarmType_Type()
)
neAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmType.setStatus("current")
_NeAlarmManagedObject_Type = DisplayString
_NeAlarmManagedObject_Object = MibTableColumn
neAlarmManagedObject = _NeAlarmManagedObject_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 6),
    _NeAlarmManagedObject_Type()
)
neAlarmManagedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmManagedObject.setStatus("current")


class _NeAlarmStatus_Type(Integer32):
    """Custom type neAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("terminate", 3))
    )


_NeAlarmStatus_Type.__name__ = "Integer32"
_NeAlarmStatus_Object = MibTableColumn
neAlarmStatus = _NeAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 7),
    _NeAlarmStatus_Type()
)
neAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAlarmStatus.setStatus("current")


class _NeAlarmAlreadyPresent_Type(Integer32):
    """Custom type neAlarmAlreadyPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_NeAlarmAlreadyPresent_Type.__name__ = "Integer32"
_NeAlarmAlreadyPresent_Object = MibTableColumn
neAlarmAlreadyPresent = _NeAlarmAlreadyPresent_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 8),
    _NeAlarmAlreadyPresent_Type()
)
neAlarmAlreadyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmAlreadyPresent.setStatus("current")
_NeAlarmTimeStamp_Type = TimeTicks
_NeAlarmTimeStamp_Object = MibTableColumn
neAlarmTimeStamp = _NeAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 1, 1, 9),
    _NeAlarmTimeStamp_Type()
)
neAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmTimeStamp.setStatus("current")
_NeAlarmActiveLastTrapIndex_Type = Unsigned32
_NeAlarmActiveLastTrapIndex_Object = MibScalar
neAlarmActiveLastTrapIndex = _NeAlarmActiveLastTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 2),
    _NeAlarmActiveLastTrapIndex_Type()
)
neAlarmActiveLastTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmActiveLastTrapIndex.setStatus("current")


class _NeClearTerminatedAlarms_Type(Integer32):
    """Custom type neClearTerminatedAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NeClearTerminatedAlarms_Type.__name__ = "Integer32"
_NeClearTerminatedAlarms_Object = MibScalar
neClearTerminatedAlarms = _NeClearTerminatedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 3),
    _NeClearTerminatedAlarms_Type()
)
neClearTerminatedAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neClearTerminatedAlarms.setStatus("current")


class _NeAlarmActivePhoto_Type(Integer32):
    """Custom type neAlarmActivePhoto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NeAlarmActivePhoto_Type.__name__ = "Integer32"
_NeAlarmActivePhoto_Object = MibScalar
neAlarmActivePhoto = _NeAlarmActivePhoto_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 4),
    _NeAlarmActivePhoto_Type()
)
neAlarmActivePhoto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAlarmActivePhoto.setStatus("current")
_NeAlarmTrap_ObjectIdentity = ObjectIdentity
neAlarmTrap = _NeAlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 10)
)
_NeAlarmTrapCounter_Type = Counter32
_NeAlarmTrapCounter_Object = MibScalar
neAlarmTrapCounter = _NeAlarmTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 2),
    _NeAlarmTrapCounter_Type()
)
neAlarmTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neAlarmTrapCounter.setStatus("current")
_NeAlarmTrapFilter_Type = NeTrapFilter
_NeAlarmTrapFilter_Object = MibScalar
neAlarmTrapFilter = _NeAlarmTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 3),
    _NeAlarmTrapFilter_Type()
)
neAlarmTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAlarmTrapFilter.setStatus("current")
_NeAlarmTrapDestiIp_Type = IpAddress
_NeAlarmTrapDestiIp_Object = MibScalar
neAlarmTrapDestiIp = _NeAlarmTrapDestiIp_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 4),
    _NeAlarmTrapDestiIp_Type()
)
neAlarmTrapDestiIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAlarmTrapDestiIp.setStatus("current")
_NeAlarmTrapDestiPort_Type = Unsigned32
_NeAlarmTrapDestiPort_Object = MibScalar
neAlarmTrapDestiPort = _NeAlarmTrapDestiPort_Object(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 10, 5),
    _NeAlarmTrapDestiPort_Type()
)
neAlarmTrapDestiPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neAlarmTrapDestiPort.setStatus("current")

# Managed Objects groups

neAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 11)
)
neAlarmGroup.setObjects(
      *(("SPIDCOM-ALARM-MIB", "neAlarmIndex"),
        ("SPIDCOM-ALARM-MIB", "neAlarmAdditionalText"),
        ("SPIDCOM-ALARM-MIB", "neAlarmProbableCause"),
        ("SPIDCOM-ALARM-MIB", "neAlarmDescription"),
        ("SPIDCOM-ALARM-MIB", "neAlarmType"),
        ("SPIDCOM-ALARM-MIB", "neAlarmManagedObject"),
        ("SPIDCOM-ALARM-MIB", "neAlarmAlreadyPresent"),
        ("SPIDCOM-ALARM-MIB", "neAlarmTimeStamp"),
        ("SPIDCOM-ALARM-MIB", "neAlarmStatus"))
)
if mibBuilder.loadTexts:
    neAlarmGroup.setStatus("current")

neAlarmActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 2, 1, 13)
)
neAlarmActiveGroup.setObjects(
      *(("SPIDCOM-ALARM-MIB", "neAlarmActiveLastTrapIndex"),
        ("SPIDCOM-ALARM-MIB", "neAlarmActivePhoto"),
        ("SPIDCOM-ALARM-MIB", "neAlarmTrapFilter"),
        ("SPIDCOM-ALARM-MIB", "neAlarmTrapDestiIp"),
        ("SPIDCOM-ALARM-MIB", "neAlarmTrapDestiPort"),
        ("SPIDCOM-ALARM-MIB", "neAlarmTrapCounter"),
        ("SPIDCOM-ALARM-MIB", "neClearTerminatedAlarms"))
)
if mibBuilder.loadTexts:
    neAlarmActiveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPIDCOM-ALARM-MIB",
    **{"ItuAlarmProbableCause": ItuAlarmProbableCause,
       "ItuAlarmType": ItuAlarmType,
       "NeAlarmPhoto": NeAlarmPhoto,
       "NeTrapFilter": NeTrapFilter,
       "neAlarm": neAlarm,
       "neAlarmTable": neAlarmTable,
       "neAlarmEntry": neAlarmEntry,
       "neAlarmIndex": neAlarmIndex,
       "neAlarmAdditionalText": neAlarmAdditionalText,
       "neAlarmProbableCause": neAlarmProbableCause,
       "neAlarmDescription": neAlarmDescription,
       "neAlarmType": neAlarmType,
       "neAlarmManagedObject": neAlarmManagedObject,
       "neAlarmStatus": neAlarmStatus,
       "neAlarmAlreadyPresent": neAlarmAlreadyPresent,
       "neAlarmTimeStamp": neAlarmTimeStamp,
       "neAlarmActiveLastTrapIndex": neAlarmActiveLastTrapIndex,
       "neClearTerminatedAlarms": neClearTerminatedAlarms,
       "neAlarmActivePhoto": neAlarmActivePhoto,
       "neAlarmTrap": neAlarmTrap,
       "neAlarmTrapCounter": neAlarmTrapCounter,
       "neAlarmTrapFilter": neAlarmTrapFilter,
       "neAlarmTrapDestiIp": neAlarmTrapDestiIp,
       "neAlarmTrapDestiPort": neAlarmTrapDestiPort,
       "neAlarmGroup": neAlarmGroup,
       "neAlarmActiveGroup": neAlarmActiveGroup}
)
