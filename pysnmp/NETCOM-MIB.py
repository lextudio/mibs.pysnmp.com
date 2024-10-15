# SNMP MIB module (NETCOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETCOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:43 2024
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

_Sinetica_ObjectIdentity = ObjectIdentity
sinetica = _Sinetica_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711)
)
_Netcom_ObjectIdentity = ObjectIdentity
netcom = _Netcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 7)
)
_Netcom1_ObjectIdentity = ObjectIdentity
netcom1 = _Netcom1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1)
)
_NetcomObjects_ObjectIdentity = ObjectIdentity
netcomObjects = _NetcomObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1)
)
_NetcomEnvironment_ObjectIdentity = ObjectIdentity
netcomEnvironment = _NetcomEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1)
)
_NetcomEnvHumidity_ObjectIdentity = ObjectIdentity
netcomEnvHumidity = _NetcomEnvHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 1)
)


class _NetcomEnvHumidityEnableMonitoring_Type(Integer32):
    """Custom type netcomEnvHumidityEnableMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomEnvHumidityEnableMonitoring_Type.__name__ = "Integer32"
_NetcomEnvHumidityEnableMonitoring_Object = MibScalar
netcomEnvHumidityEnableMonitoring = _NetcomEnvHumidityEnableMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 1, 1),
    _NetcomEnvHumidityEnableMonitoring_Type()
)
netcomEnvHumidityEnableMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomEnvHumidityEnableMonitoring.setStatus("mandatory")


class _NetcomEnvCurrentHumidity_Type(Integer32):
    """Custom type netcomEnvCurrentHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NetcomEnvCurrentHumidity_Type.__name__ = "Integer32"
_NetcomEnvCurrentHumidity_Object = MibScalar
netcomEnvCurrentHumidity = _NetcomEnvCurrentHumidity_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 1, 2),
    _NetcomEnvCurrentHumidity_Type()
)
netcomEnvCurrentHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcomEnvCurrentHumidity.setStatus("mandatory")


class _NetcomEnvHumidityLowerThreshold_Type(Integer32):
    """Custom type netcomEnvHumidityLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NetcomEnvHumidityLowerThreshold_Type.__name__ = "Integer32"
_NetcomEnvHumidityLowerThreshold_Object = MibScalar
netcomEnvHumidityLowerThreshold = _NetcomEnvHumidityLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 1, 3),
    _NetcomEnvHumidityLowerThreshold_Type()
)
netcomEnvHumidityLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomEnvHumidityLowerThreshold.setStatus("mandatory")


class _NetcomEnvHumidityUpperThreshold_Type(Integer32):
    """Custom type netcomEnvHumidityUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NetcomEnvHumidityUpperThreshold_Type.__name__ = "Integer32"
_NetcomEnvHumidityUpperThreshold_Object = MibScalar
netcomEnvHumidityUpperThreshold = _NetcomEnvHumidityUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 1, 4),
    _NetcomEnvHumidityUpperThreshold_Type()
)
netcomEnvHumidityUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomEnvHumidityUpperThreshold.setStatus("mandatory")


class _NetcomEnvHumidityCalibrationOffset_Type(Integer32):
    """Custom type netcomEnvHumidityCalibrationOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_NetcomEnvHumidityCalibrationOffset_Type.__name__ = "Integer32"
_NetcomEnvHumidityCalibrationOffset_Object = MibScalar
netcomEnvHumidityCalibrationOffset = _NetcomEnvHumidityCalibrationOffset_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 1, 5),
    _NetcomEnvHumidityCalibrationOffset_Type()
)
netcomEnvHumidityCalibrationOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomEnvHumidityCalibrationOffset.setStatus("mandatory")
_NetcomEnvTemperature_ObjectIdentity = ObjectIdentity
netcomEnvTemperature = _NetcomEnvTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 2)
)


class _NetcomEnvTemperatureEnableMonitoring_Type(Integer32):
    """Custom type netcomEnvTemperatureEnableMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomEnvTemperatureEnableMonitoring_Type.__name__ = "Integer32"
_NetcomEnvTemperatureEnableMonitoring_Object = MibScalar
netcomEnvTemperatureEnableMonitoring = _NetcomEnvTemperatureEnableMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 2, 1),
    _NetcomEnvTemperatureEnableMonitoring_Type()
)
netcomEnvTemperatureEnableMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomEnvTemperatureEnableMonitoring.setStatus("mandatory")


class _NetcomEnvCurrentTemperature_Type(Integer32):
    """Custom type netcomEnvCurrentTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 1000),
    )


_NetcomEnvCurrentTemperature_Type.__name__ = "Integer32"
_NetcomEnvCurrentTemperature_Object = MibScalar
netcomEnvCurrentTemperature = _NetcomEnvCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 2, 2),
    _NetcomEnvCurrentTemperature_Type()
)
netcomEnvCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcomEnvCurrentTemperature.setStatus("mandatory")


class _NetcomEnvTemperatureLowerThreshold_Type(Integer32):
    """Custom type netcomEnvTemperatureLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 1000),
    )


_NetcomEnvTemperatureLowerThreshold_Type.__name__ = "Integer32"
_NetcomEnvTemperatureLowerThreshold_Object = MibScalar
netcomEnvTemperatureLowerThreshold = _NetcomEnvTemperatureLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 2, 3),
    _NetcomEnvTemperatureLowerThreshold_Type()
)
netcomEnvTemperatureLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomEnvTemperatureLowerThreshold.setStatus("mandatory")


class _NetcomEnvTemperatureUpperThreshold_Type(Integer32):
    """Custom type netcomEnvTemperatureUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 1000),
    )


_NetcomEnvTemperatureUpperThreshold_Type.__name__ = "Integer32"
_NetcomEnvTemperatureUpperThreshold_Object = MibScalar
netcomEnvTemperatureUpperThreshold = _NetcomEnvTemperatureUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 2, 4),
    _NetcomEnvTemperatureUpperThreshold_Type()
)
netcomEnvTemperatureUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomEnvTemperatureUpperThreshold.setStatus("mandatory")


class _NetcomEnvTemperatureCalibrationOffset_Type(Integer32):
    """Custom type netcomEnvTemperatureCalibrationOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_NetcomEnvTemperatureCalibrationOffset_Type.__name__ = "Integer32"
_NetcomEnvTemperatureCalibrationOffset_Object = MibScalar
netcomEnvTemperatureCalibrationOffset = _NetcomEnvTemperatureCalibrationOffset_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 2, 5),
    _NetcomEnvTemperatureCalibrationOffset_Type()
)
netcomEnvTemperatureCalibrationOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomEnvTemperatureCalibrationOffset.setStatus("mandatory")
_NetcomContact_ObjectIdentity = ObjectIdentity
netcomContact = _NetcomContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2)
)


class _NetcomContactEnable_Type(Integer32):
    """Custom type netcomContactEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContactEnable_Type.__name__ = "Integer32"
_NetcomContactEnable_Object = MibScalar
netcomContactEnable = _NetcomContactEnable_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 1),
    _NetcomContactEnable_Type()
)
netcomContactEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomContactEnable.setStatus("mandatory")
_NetcomContactNormalStates_ObjectIdentity = ObjectIdentity
netcomContactNormalStates = _NetcomContactNormalStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 2)
)


class _NetcomContact1NormalState_Type(Integer32):
    """Custom type netcomContact1NormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact1NormalState_Type.__name__ = "Integer32"
_NetcomContact1NormalState_Object = MibScalar
netcomContact1NormalState = _NetcomContact1NormalState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 2, 1),
    _NetcomContact1NormalState_Type()
)
netcomContact1NormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomContact1NormalState.setStatus("mandatory")


class _NetcomContact2NormalState_Type(Integer32):
    """Custom type netcomContact2NormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact2NormalState_Type.__name__ = "Integer32"
_NetcomContact2NormalState_Object = MibScalar
netcomContact2NormalState = _NetcomContact2NormalState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 2, 2),
    _NetcomContact2NormalState_Type()
)
netcomContact2NormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomContact2NormalState.setStatus("mandatory")


class _NetcomContact3NormalState_Type(Integer32):
    """Custom type netcomContact3NormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact3NormalState_Type.__name__ = "Integer32"
_NetcomContact3NormalState_Object = MibScalar
netcomContact3NormalState = _NetcomContact3NormalState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 2, 3),
    _NetcomContact3NormalState_Type()
)
netcomContact3NormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomContact3NormalState.setStatus("mandatory")


class _NetcomContact4NormalState_Type(Integer32):
    """Custom type netcomContact4NormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact4NormalState_Type.__name__ = "Integer32"
_NetcomContact4NormalState_Object = MibScalar
netcomContact4NormalState = _NetcomContact4NormalState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 2, 4),
    _NetcomContact4NormalState_Type()
)
netcomContact4NormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomContact4NormalState.setStatus("mandatory")


class _NetcomContact5NormalState_Type(Integer32):
    """Custom type netcomContact5NormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact5NormalState_Type.__name__ = "Integer32"
_NetcomContact5NormalState_Object = MibScalar
netcomContact5NormalState = _NetcomContact5NormalState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 2, 5),
    _NetcomContact5NormalState_Type()
)
netcomContact5NormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomContact5NormalState.setStatus("mandatory")


class _NetcomContact6NormalState_Type(Integer32):
    """Custom type netcomContact6NormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact6NormalState_Type.__name__ = "Integer32"
_NetcomContact6NormalState_Object = MibScalar
netcomContact6NormalState = _NetcomContact6NormalState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 2, 6),
    _NetcomContact6NormalState_Type()
)
netcomContact6NormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomContact6NormalState.setStatus("mandatory")


class _NetcomContact7NormalState_Type(Integer32):
    """Custom type netcomContact7NormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact7NormalState_Type.__name__ = "Integer32"
_NetcomContact7NormalState_Object = MibScalar
netcomContact7NormalState = _NetcomContact7NormalState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 2, 7),
    _NetcomContact7NormalState_Type()
)
netcomContact7NormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcomContact7NormalState.setStatus("mandatory")
_NetcomContactCurrentStates_ObjectIdentity = ObjectIdentity
netcomContactCurrentStates = _NetcomContactCurrentStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 3)
)


class _NetcomContact1CurrentState_Type(Integer32):
    """Custom type netcomContact1CurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact1CurrentState_Type.__name__ = "Integer32"
_NetcomContact1CurrentState_Object = MibScalar
netcomContact1CurrentState = _NetcomContact1CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 3, 1),
    _NetcomContact1CurrentState_Type()
)
netcomContact1CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcomContact1CurrentState.setStatus("mandatory")


class _NetcomContact2CurrentState_Type(Integer32):
    """Custom type netcomContact2CurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact2CurrentState_Type.__name__ = "Integer32"
_NetcomContact2CurrentState_Object = MibScalar
netcomContact2CurrentState = _NetcomContact2CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 3, 2),
    _NetcomContact2CurrentState_Type()
)
netcomContact2CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcomContact2CurrentState.setStatus("mandatory")


class _NetcomContact3CurrentState_Type(Integer32):
    """Custom type netcomContact3CurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact3CurrentState_Type.__name__ = "Integer32"
_NetcomContact3CurrentState_Object = MibScalar
netcomContact3CurrentState = _NetcomContact3CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 3, 3),
    _NetcomContact3CurrentState_Type()
)
netcomContact3CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcomContact3CurrentState.setStatus("mandatory")


class _NetcomContact4CurrentState_Type(Integer32):
    """Custom type netcomContact4CurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact4CurrentState_Type.__name__ = "Integer32"
_NetcomContact4CurrentState_Object = MibScalar
netcomContact4CurrentState = _NetcomContact4CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 3, 4),
    _NetcomContact4CurrentState_Type()
)
netcomContact4CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcomContact4CurrentState.setStatus("mandatory")


class _NetcomContact5CurrentState_Type(Integer32):
    """Custom type netcomContact5CurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact5CurrentState_Type.__name__ = "Integer32"
_NetcomContact5CurrentState_Object = MibScalar
netcomContact5CurrentState = _NetcomContact5CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 3, 5),
    _NetcomContact5CurrentState_Type()
)
netcomContact5CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcomContact5CurrentState.setStatus("mandatory")


class _NetcomContact6CurrentState_Type(Integer32):
    """Custom type netcomContact6CurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact6CurrentState_Type.__name__ = "Integer32"
_NetcomContact6CurrentState_Object = MibScalar
netcomContact6CurrentState = _NetcomContact6CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 3, 6),
    _NetcomContact6CurrentState_Type()
)
netcomContact6CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcomContact6CurrentState.setStatus("mandatory")


class _NetcomContact7CurrentState_Type(Integer32):
    """Custom type netcomContact7CurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetcomContact7CurrentState_Type.__name__ = "Integer32"
_NetcomContact7CurrentState_Object = MibScalar
netcomContact7CurrentState = _NetcomContact7CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 3, 7),
    _NetcomContact7CurrentState_Type()
)
netcomContact7CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcomContact7CurrentState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

netcomLowHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 1, 0, 21)
)
netcomLowHumidity.setObjects(
    ("NETCOM-MIB", "netcomEnvCurrentHumidity")
)
if mibBuilder.loadTexts:
    netcomLowHumidity.setStatus(
        ""
    )

netcomHighHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 1, 0, 22)
)
netcomHighHumidity.setObjects(
    ("NETCOM-MIB", "netcomEnvCurrentHumidity")
)
if mibBuilder.loadTexts:
    netcomHighHumidity.setStatus(
        ""
    )

netcomHumidityReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 1, 0, 23)
)
netcomHumidityReturnToNormal.setObjects(
    ("NETCOM-MIB", "netcomEnvCurrentHumidity")
)
if mibBuilder.loadTexts:
    netcomHumidityReturnToNormal.setStatus(
        ""
    )

netcomLowTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 2, 0, 31)
)
netcomLowTemperature.setObjects(
    ("NETCOM-MIB", "netcomEnvCurrentTemperature")
)
if mibBuilder.loadTexts:
    netcomLowTemperature.setStatus(
        ""
    )

netcomHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 2, 0, 32)
)
netcomHighTemperature.setObjects(
    ("NETCOM-MIB", "netcomEnvCurrentTemperature")
)
if mibBuilder.loadTexts:
    netcomHighTemperature.setStatus(
        ""
    )

netcomTemperatureReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 1, 2, 0, 33)
)
netcomTemperatureReturnToNormal.setObjects(
    ("NETCOM-MIB", "netcomEnvCurrentTemperature")
)
if mibBuilder.loadTexts:
    netcomTemperatureReturnToNormal.setStatus(
        ""
    )

netcomContact1NonNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    netcomContact1NonNormal.setStatus(
        ""
    )

netcomContact2NonNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    netcomContact2NonNormal.setStatus(
        ""
    )

netcomContact3NonNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    netcomContact3NonNormal.setStatus(
        ""
    )

netcomContact4NonNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    netcomContact4NonNormal.setStatus(
        ""
    )

netcomContact5NonNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    netcomContact5NonNormal.setStatus(
        ""
    )

netcomContact6NonNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    netcomContact6NonNormal.setStatus(
        ""
    )

netcomContact7NonNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 7)
)
if mibBuilder.loadTexts:
    netcomContact7NonNormal.setStatus(
        ""
    )

netcomContact1ReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 11)
)
if mibBuilder.loadTexts:
    netcomContact1ReturnToNormal.setStatus(
        ""
    )

netcomContact2ReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 12)
)
if mibBuilder.loadTexts:
    netcomContact2ReturnToNormal.setStatus(
        ""
    )

netcomContact3ReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 13)
)
if mibBuilder.loadTexts:
    netcomContact3ReturnToNormal.setStatus(
        ""
    )

netcomContact4ReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 14)
)
if mibBuilder.loadTexts:
    netcomContact4ReturnToNormal.setStatus(
        ""
    )

netcomContact5ReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 15)
)
if mibBuilder.loadTexts:
    netcomContact5ReturnToNormal.setStatus(
        ""
    )

netcomContact6ReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 16)
)
if mibBuilder.loadTexts:
    netcomContact6ReturnToNormal.setStatus(
        ""
    )

netcomContact7ReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3711, 7, 1, 1, 2, 0, 17)
)
if mibBuilder.loadTexts:
    netcomContact7ReturnToNormal.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETCOM-MIB",
    **{"sinetica": sinetica,
       "netcom": netcom,
       "netcom1": netcom1,
       "netcomObjects": netcomObjects,
       "netcomEnvironment": netcomEnvironment,
       "netcomEnvHumidity": netcomEnvHumidity,
       "netcomLowHumidity": netcomLowHumidity,
       "netcomHighHumidity": netcomHighHumidity,
       "netcomHumidityReturnToNormal": netcomHumidityReturnToNormal,
       "netcomEnvHumidityEnableMonitoring": netcomEnvHumidityEnableMonitoring,
       "netcomEnvCurrentHumidity": netcomEnvCurrentHumidity,
       "netcomEnvHumidityLowerThreshold": netcomEnvHumidityLowerThreshold,
       "netcomEnvHumidityUpperThreshold": netcomEnvHumidityUpperThreshold,
       "netcomEnvHumidityCalibrationOffset": netcomEnvHumidityCalibrationOffset,
       "netcomEnvTemperature": netcomEnvTemperature,
       "netcomLowTemperature": netcomLowTemperature,
       "netcomHighTemperature": netcomHighTemperature,
       "netcomTemperatureReturnToNormal": netcomTemperatureReturnToNormal,
       "netcomEnvTemperatureEnableMonitoring": netcomEnvTemperatureEnableMonitoring,
       "netcomEnvCurrentTemperature": netcomEnvCurrentTemperature,
       "netcomEnvTemperatureLowerThreshold": netcomEnvTemperatureLowerThreshold,
       "netcomEnvTemperatureUpperThreshold": netcomEnvTemperatureUpperThreshold,
       "netcomEnvTemperatureCalibrationOffset": netcomEnvTemperatureCalibrationOffset,
       "netcomContact": netcomContact,
       "netcomContact1NonNormal": netcomContact1NonNormal,
       "netcomContact2NonNormal": netcomContact2NonNormal,
       "netcomContact3NonNormal": netcomContact3NonNormal,
       "netcomContact4NonNormal": netcomContact4NonNormal,
       "netcomContact5NonNormal": netcomContact5NonNormal,
       "netcomContact6NonNormal": netcomContact6NonNormal,
       "netcomContact7NonNormal": netcomContact7NonNormal,
       "netcomContact1ReturnToNormal": netcomContact1ReturnToNormal,
       "netcomContact2ReturnToNormal": netcomContact2ReturnToNormal,
       "netcomContact3ReturnToNormal": netcomContact3ReturnToNormal,
       "netcomContact4ReturnToNormal": netcomContact4ReturnToNormal,
       "netcomContact5ReturnToNormal": netcomContact5ReturnToNormal,
       "netcomContact6ReturnToNormal": netcomContact6ReturnToNormal,
       "netcomContact7ReturnToNormal": netcomContact7ReturnToNormal,
       "netcomContactEnable": netcomContactEnable,
       "netcomContactNormalStates": netcomContactNormalStates,
       "netcomContact1NormalState": netcomContact1NormalState,
       "netcomContact2NormalState": netcomContact2NormalState,
       "netcomContact3NormalState": netcomContact3NormalState,
       "netcomContact4NormalState": netcomContact4NormalState,
       "netcomContact5NormalState": netcomContact5NormalState,
       "netcomContact6NormalState": netcomContact6NormalState,
       "netcomContact7NormalState": netcomContact7NormalState,
       "netcomContactCurrentStates": netcomContactCurrentStates,
       "netcomContact1CurrentState": netcomContact1CurrentState,
       "netcomContact2CurrentState": netcomContact2CurrentState,
       "netcomContact3CurrentState": netcomContact3CurrentState,
       "netcomContact4CurrentState": netcomContact4CurrentState,
       "netcomContact5CurrentState": netcomContact5CurrentState,
       "netcomContact6CurrentState": netcomContact6CurrentState,
       "netcomContact7CurrentState": netcomContact7CurrentState}
)
