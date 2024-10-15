# SNMP MIB module (ADH3-NETCOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADH3-NETCOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:45 2024
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

environmentalTechnology = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32185)
)
environmentalTechnology.setRevisions(
        ("2008-11-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netcom_ObjectIdentity = ObjectIdentity
netcom = _Netcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32185, 2)
)
if mibBuilder.loadTexts:
    netcom.setStatus("current")
_StatusInfo_ObjectIdentity = ObjectIdentity
statusInfo = _StatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32185, 2, 1)
)


class _AllStatuses_Type(DisplayString):
    """Custom type allStatuses based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_AllStatuses_Type.__name__ = "DisplayString"
_AllStatuses_Object = MibScalar
allStatuses = _AllStatuses_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 1, 1),
    _AllStatuses_Type()
)
allStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allStatuses.setStatus("current")


class _PressurePSI_Type(DisplayString):
    """Custom type pressurePSI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_PressurePSI_Type.__name__ = "DisplayString"
_PressurePSI_Object = MibScalar
pressurePSI = _PressurePSI_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 1, 2),
    _PressurePSI_Type()
)
pressurePSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressurePSI.setStatus("current")


class _Dutycycle_Type(DisplayString):
    """Custom type dutycycle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Dutycycle_Type.__name__ = "DisplayString"
_Dutycycle_Object = MibScalar
dutycycle = _Dutycycle_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 1, 3),
    _Dutycycle_Type()
)
dutycycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dutycycle.setStatus("current")


class _StatusVars_Type(DisplayString):
    """Custom type statusVars based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StatusVars_Type.__name__ = "DisplayString"
_StatusVars_Object = MibScalar
statusVars = _StatusVars_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 1, 4),
    _StatusVars_Type()
)
statusVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusVars.setStatus("current")


class _Temperature_Type(DisplayString):
    """Custom type temperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Temperature_Type.__name__ = "DisplayString"
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 1, 5),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")


class _Alarms_Type(DisplayString):
    """Custom type alarms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_Alarms_Type.__name__ = "DisplayString"
_Alarms_Object = MibScalar
alarms = _Alarms_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 1, 6),
    _Alarms_Type()
)
alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarms.setStatus("current")


class _CompressorHours_Type(DisplayString):
    """Custom type compressorHours based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_CompressorHours_Type.__name__ = "DisplayString"
_CompressorHours_Object = MibScalar
compressorHours = _CompressorHours_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 1, 7),
    _CompressorHours_Type()
)
compressorHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compressorHours.setStatus("current")


class _MajorState_Type(Integer32):
    """Custom type majorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leaky", 3),
          ("online", 1),
          ("standby", 2))
    )


_MajorState_Type.__name__ = "Integer32"
_MajorState_Object = MibScalar
majorState = _MajorState_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 1, 8),
    _MajorState_Type()
)
majorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    majorState.setStatus("current")
_ParamsInfo_ObjectIdentity = ObjectIdentity
paramsInfo = _ParamsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32185, 2, 2)
)


class _LowerLimit_Type(DisplayString):
    """Custom type lowerLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_LowerLimit_Type.__name__ = "DisplayString"
_LowerLimit_Object = MibScalar
lowerLimit = _LowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 2, 1),
    _LowerLimit_Type()
)
lowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowerLimit.setStatus("current")


class _UpperLimit_Type(DisplayString):
    """Custom type upperLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpperLimit_Type.__name__ = "DisplayString"
_UpperLimit_Object = MibScalar
upperLimit = _UpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 2, 2),
    _UpperLimit_Type()
)
upperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upperLimit.setStatus("current")


class _LowerAlarmLimit_Type(DisplayString):
    """Custom type lowerAlarmLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_LowerAlarmLimit_Type.__name__ = "DisplayString"
_LowerAlarmLimit_Object = MibScalar
lowerAlarmLimit = _LowerAlarmLimit_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 2, 3),
    _LowerAlarmLimit_Type()
)
lowerAlarmLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowerAlarmLimit.setStatus("current")


class _UpperAlarmLimit_Type(DisplayString):
    """Custom type upperAlarmLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpperAlarmLimit_Type.__name__ = "DisplayString"
_UpperAlarmLimit_Object = MibScalar
upperAlarmLimit = _UpperAlarmLimit_Object(
    (1, 3, 6, 1, 4, 1, 32185, 2, 2, 4),
    _UpperAlarmLimit_Type()
)
upperAlarmLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upperAlarmLimit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADH3-NETCOM-MIB",
    **{"environmentalTechnology": environmentalTechnology,
       "netcom": netcom,
       "statusInfo": statusInfo,
       "allStatuses": allStatuses,
       "pressurePSI": pressurePSI,
       "dutycycle": dutycycle,
       "statusVars": statusVars,
       "temperature": temperature,
       "alarms": alarms,
       "compressorHours": compressorHours,
       "majorState": majorState,
       "paramsInfo": paramsInfo,
       "lowerLimit": lowerLimit,
       "upperLimit": upperLimit,
       "lowerAlarmLimit": lowerAlarmLimit,
       "upperAlarmLimit": upperAlarmLimit}
)
