# SNMP MIB module (CCPOWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CCPOWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:52 2024
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

_Ccpower_ObjectIdentity = ObjectIdentity
ccpower = _Ccpower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642)
)
_DcSystem_ObjectIdentity = ObjectIdentity
dcSystem = _DcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1)
)
_ReadWriteObjects_ObjectIdentity = ObjectIdentity
readWriteObjects = _ReadWriteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1)
)
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1)
)
_FloatVoltage_Type = Integer32
_FloatVoltage_Object = MibScalar
floatVoltage = _FloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 1),
    _FloatVoltage_Type()
)
floatVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    floatVoltage.setStatus("mandatory")
_OverloadCurrent_Type = Integer32
_OverloadCurrent_Object = MibScalar
overloadCurrent = _OverloadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 2),
    _OverloadCurrent_Type()
)
overloadCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overloadCurrent.setStatus("mandatory")
_HighVoltageAlarm_Type = Integer32
_HighVoltageAlarm_Object = MibScalar
highVoltageAlarm = _HighVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 3),
    _HighVoltageAlarm_Type()
)
highVoltageAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highVoltageAlarm.setStatus("mandatory")
_LowVoltageAlarm_Type = Integer32
_LowVoltageAlarm_Object = MibScalar
lowVoltageAlarm = _LowVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 4),
    _LowVoltageAlarm_Type()
)
lowVoltageAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowVoltageAlarm.setStatus("mandatory")
_Disconnect1Voltage_Type = Integer32
_Disconnect1Voltage_Object = MibScalar
disconnect1Voltage = _Disconnect1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 5),
    _Disconnect1Voltage_Type()
)
disconnect1Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1Voltage.setStatus("mandatory")
_Disconnect1Temperature_Type = Integer32
_Disconnect1Temperature_Object = MibScalar
disconnect1Temperature = _Disconnect1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 6),
    _Disconnect1Temperature_Type()
)
disconnect1Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1Temperature.setStatus("mandatory")
_Disconnect1LoadShedSundayOff_Type = DisplayString
_Disconnect1LoadShedSundayOff_Object = MibScalar
disconnect1LoadShedSundayOff = _Disconnect1LoadShedSundayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 7),
    _Disconnect1LoadShedSundayOff_Type()
)
disconnect1LoadShedSundayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1LoadShedSundayOff.setStatus("mandatory")
_Disconnect1LoadShedMondayOff_Type = DisplayString
_Disconnect1LoadShedMondayOff_Object = MibScalar
disconnect1LoadShedMondayOff = _Disconnect1LoadShedMondayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 8),
    _Disconnect1LoadShedMondayOff_Type()
)
disconnect1LoadShedMondayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1LoadShedMondayOff.setStatus("mandatory")
_Disconnect1LoadShedTuesdayOff_Type = DisplayString
_Disconnect1LoadShedTuesdayOff_Object = MibScalar
disconnect1LoadShedTuesdayOff = _Disconnect1LoadShedTuesdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 9),
    _Disconnect1LoadShedTuesdayOff_Type()
)
disconnect1LoadShedTuesdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1LoadShedTuesdayOff.setStatus("mandatory")
_Disconnect1LoadShedWednesdayOff_Type = DisplayString
_Disconnect1LoadShedWednesdayOff_Object = MibScalar
disconnect1LoadShedWednesdayOff = _Disconnect1LoadShedWednesdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 10),
    _Disconnect1LoadShedWednesdayOff_Type()
)
disconnect1LoadShedWednesdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1LoadShedWednesdayOff.setStatus("mandatory")
_Disconnect1LoadShedThursdayOff_Type = DisplayString
_Disconnect1LoadShedThursdayOff_Object = MibScalar
disconnect1LoadShedThursdayOff = _Disconnect1LoadShedThursdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 11),
    _Disconnect1LoadShedThursdayOff_Type()
)
disconnect1LoadShedThursdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1LoadShedThursdayOff.setStatus("mandatory")
_Disconnect1LoadShedFridayOff_Type = DisplayString
_Disconnect1LoadShedFridayOff_Object = MibScalar
disconnect1LoadShedFridayOff = _Disconnect1LoadShedFridayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 12),
    _Disconnect1LoadShedFridayOff_Type()
)
disconnect1LoadShedFridayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1LoadShedFridayOff.setStatus("mandatory")
_Disconnect1LoadShedSaturdayOff_Type = DisplayString
_Disconnect1LoadShedSaturdayOff_Object = MibScalar
disconnect1LoadShedSaturdayOff = _Disconnect1LoadShedSaturdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 13),
    _Disconnect1LoadShedSaturdayOff_Type()
)
disconnect1LoadShedSaturdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect1LoadShedSaturdayOff.setStatus("mandatory")
_Disconnect2Voltage_Type = Integer32
_Disconnect2Voltage_Object = MibScalar
disconnect2Voltage = _Disconnect2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 14),
    _Disconnect2Voltage_Type()
)
disconnect2Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2Voltage.setStatus("mandatory")
_Disconnect2Temperature_Type = Integer32
_Disconnect2Temperature_Object = MibScalar
disconnect2Temperature = _Disconnect2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 15),
    _Disconnect2Temperature_Type()
)
disconnect2Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2Temperature.setStatus("mandatory")
_Disconnect2LoadShedSundayOff_Type = DisplayString
_Disconnect2LoadShedSundayOff_Object = MibScalar
disconnect2LoadShedSundayOff = _Disconnect2LoadShedSundayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 16),
    _Disconnect2LoadShedSundayOff_Type()
)
disconnect2LoadShedSundayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2LoadShedSundayOff.setStatus("mandatory")
_Disconnect2LoadShedMondayOff_Type = DisplayString
_Disconnect2LoadShedMondayOff_Object = MibScalar
disconnect2LoadShedMondayOff = _Disconnect2LoadShedMondayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 17),
    _Disconnect2LoadShedMondayOff_Type()
)
disconnect2LoadShedMondayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2LoadShedMondayOff.setStatus("mandatory")
_Disconnect2LoadShedTuesdayOff_Type = DisplayString
_Disconnect2LoadShedTuesdayOff_Object = MibScalar
disconnect2LoadShedTuesdayOff = _Disconnect2LoadShedTuesdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 18),
    _Disconnect2LoadShedTuesdayOff_Type()
)
disconnect2LoadShedTuesdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2LoadShedTuesdayOff.setStatus("mandatory")
_Disconnect2LoadShedWednesdayOff_Type = DisplayString
_Disconnect2LoadShedWednesdayOff_Object = MibScalar
disconnect2LoadShedWednesdayOff = _Disconnect2LoadShedWednesdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 19),
    _Disconnect2LoadShedWednesdayOff_Type()
)
disconnect2LoadShedWednesdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2LoadShedWednesdayOff.setStatus("mandatory")
_Disconnect2LoadShedThursdayOff_Type = DisplayString
_Disconnect2LoadShedThursdayOff_Object = MibScalar
disconnect2LoadShedThursdayOff = _Disconnect2LoadShedThursdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 20),
    _Disconnect2LoadShedThursdayOff_Type()
)
disconnect2LoadShedThursdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2LoadShedThursdayOff.setStatus("mandatory")
_Disconnect2LoadShedFridayOff_Type = DisplayString
_Disconnect2LoadShedFridayOff_Object = MibScalar
disconnect2LoadShedFridayOff = _Disconnect2LoadShedFridayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 21),
    _Disconnect2LoadShedFridayOff_Type()
)
disconnect2LoadShedFridayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2LoadShedFridayOff.setStatus("mandatory")
_Disconnect2LoadShedSaturdayOff_Type = DisplayString
_Disconnect2LoadShedSaturdayOff_Object = MibScalar
disconnect2LoadShedSaturdayOff = _Disconnect2LoadShedSaturdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 22),
    _Disconnect2LoadShedSaturdayOff_Type()
)
disconnect2LoadShedSaturdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect2LoadShedSaturdayOff.setStatus("mandatory")
_Disconnect3Voltage_Type = Integer32
_Disconnect3Voltage_Object = MibScalar
disconnect3Voltage = _Disconnect3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 23),
    _Disconnect3Voltage_Type()
)
disconnect3Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect3Voltage.setStatus("mandatory")
_Disconnect3Temperature_Type = Integer32
_Disconnect3Temperature_Object = MibScalar
disconnect3Temperature = _Disconnect3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 24),
    _Disconnect3Temperature_Type()
)
disconnect3Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect3Temperature.setStatus("mandatory")
_Disconnect3LoadShedSundayOff_Type = DisplayString
_Disconnect3LoadShedSundayOff_Object = MibScalar
disconnect3LoadShedSundayOff = _Disconnect3LoadShedSundayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 25),
    _Disconnect3LoadShedSundayOff_Type()
)
disconnect3LoadShedSundayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect3LoadShedSundayOff.setStatus("mandatory")
_Disconnect3LoadShedMondayOff_Type = DisplayString
_Disconnect3LoadShedMondayOff_Object = MibScalar
disconnect3LoadShedMondayOff = _Disconnect3LoadShedMondayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 26),
    _Disconnect3LoadShedMondayOff_Type()
)
disconnect3LoadShedMondayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect3LoadShedMondayOff.setStatus("mandatory")
_Disconnect3LoadShedTuesdayOff_Type = DisplayString
_Disconnect3LoadShedTuesdayOff_Object = MibScalar
disconnect3LoadShedTuesdayOff = _Disconnect3LoadShedTuesdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 27),
    _Disconnect3LoadShedTuesdayOff_Type()
)
disconnect3LoadShedTuesdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect3LoadShedTuesdayOff.setStatus("mandatory")
_Disconnect3LoadShedWednesdayOff_Type = DisplayString
_Disconnect3LoadShedWednesdayOff_Object = MibScalar
disconnect3LoadShedWednesdayOff = _Disconnect3LoadShedWednesdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 28),
    _Disconnect3LoadShedWednesdayOff_Type()
)
disconnect3LoadShedWednesdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect3LoadShedWednesdayOff.setStatus("mandatory")
_Disconnect3LoadShedThursdayOff_Type = DisplayString
_Disconnect3LoadShedThursdayOff_Object = MibScalar
disconnect3LoadShedThursdayOff = _Disconnect3LoadShedThursdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 29),
    _Disconnect3LoadShedThursdayOff_Type()
)
disconnect3LoadShedThursdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect3LoadShedThursdayOff.setStatus("mandatory")
_Disconnect3LoadShedFridayOff_Type = DisplayString
_Disconnect3LoadShedFridayOff_Object = MibScalar
disconnect3LoadShedFridayOff = _Disconnect3LoadShedFridayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 30),
    _Disconnect3LoadShedFridayOff_Type()
)
disconnect3LoadShedFridayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect3LoadShedFridayOff.setStatus("mandatory")
_Disconnect3LoadShedSaturdayOff_Type = DisplayString
_Disconnect3LoadShedSaturdayOff_Object = MibScalar
disconnect3LoadShedSaturdayOff = _Disconnect3LoadShedSaturdayOff_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 31),
    _Disconnect3LoadShedSaturdayOff_Type()
)
disconnect3LoadShedSaturdayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disconnect3LoadShedSaturdayOff.setStatus("mandatory")
_Reconnect1Voltage_Type = Integer32
_Reconnect1Voltage_Object = MibScalar
reconnect1Voltage = _Reconnect1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 32),
    _Reconnect1Voltage_Type()
)
reconnect1Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect1Voltage.setStatus("mandatory")
_Reconnect1LoadShedSundayOn_Type = DisplayString
_Reconnect1LoadShedSundayOn_Object = MibScalar
reconnect1LoadShedSundayOn = _Reconnect1LoadShedSundayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 33),
    _Reconnect1LoadShedSundayOn_Type()
)
reconnect1LoadShedSundayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect1LoadShedSundayOn.setStatus("mandatory")
_Reconnect1LoadShedMondayOn_Type = DisplayString
_Reconnect1LoadShedMondayOn_Object = MibScalar
reconnect1LoadShedMondayOn = _Reconnect1LoadShedMondayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 34),
    _Reconnect1LoadShedMondayOn_Type()
)
reconnect1LoadShedMondayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect1LoadShedMondayOn.setStatus("mandatory")
_Reconnect1LoadShedTuesdayOn_Type = DisplayString
_Reconnect1LoadShedTuesdayOn_Object = MibScalar
reconnect1LoadShedTuesdayOn = _Reconnect1LoadShedTuesdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 35),
    _Reconnect1LoadShedTuesdayOn_Type()
)
reconnect1LoadShedTuesdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect1LoadShedTuesdayOn.setStatus("mandatory")
_Reconnect1LoadShedWednesdayOn_Type = DisplayString
_Reconnect1LoadShedWednesdayOn_Object = MibScalar
reconnect1LoadShedWednesdayOn = _Reconnect1LoadShedWednesdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 36),
    _Reconnect1LoadShedWednesdayOn_Type()
)
reconnect1LoadShedWednesdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect1LoadShedWednesdayOn.setStatus("mandatory")
_Reconnect1LoadShedThursdayOn_Type = DisplayString
_Reconnect1LoadShedThursdayOn_Object = MibScalar
reconnect1LoadShedThursdayOn = _Reconnect1LoadShedThursdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 37),
    _Reconnect1LoadShedThursdayOn_Type()
)
reconnect1LoadShedThursdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect1LoadShedThursdayOn.setStatus("mandatory")
_Reconnect1LoadShedFridayOn_Type = DisplayString
_Reconnect1LoadShedFridayOn_Object = MibScalar
reconnect1LoadShedFridayOn = _Reconnect1LoadShedFridayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 38),
    _Reconnect1LoadShedFridayOn_Type()
)
reconnect1LoadShedFridayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect1LoadShedFridayOn.setStatus("mandatory")
_Reconnect1LoadShedSaturdayOn_Type = DisplayString
_Reconnect1LoadShedSaturdayOn_Object = MibScalar
reconnect1LoadShedSaturdayOn = _Reconnect1LoadShedSaturdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 39),
    _Reconnect1LoadShedSaturdayOn_Type()
)
reconnect1LoadShedSaturdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect1LoadShedSaturdayOn.setStatus("mandatory")
_Reconnect2Voltage_Type = Integer32
_Reconnect2Voltage_Object = MibScalar
reconnect2Voltage = _Reconnect2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 40),
    _Reconnect2Voltage_Type()
)
reconnect2Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect2Voltage.setStatus("mandatory")
_Reconnect2LoadShedSundayOn_Type = DisplayString
_Reconnect2LoadShedSundayOn_Object = MibScalar
reconnect2LoadShedSundayOn = _Reconnect2LoadShedSundayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 41),
    _Reconnect2LoadShedSundayOn_Type()
)
reconnect2LoadShedSundayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect2LoadShedSundayOn.setStatus("mandatory")
_Reconnect2LoadShedMondayOn_Type = DisplayString
_Reconnect2LoadShedMondayOn_Object = MibScalar
reconnect2LoadShedMondayOn = _Reconnect2LoadShedMondayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 42),
    _Reconnect2LoadShedMondayOn_Type()
)
reconnect2LoadShedMondayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect2LoadShedMondayOn.setStatus("mandatory")
_Reconnect2LoadShedTuesdayOn_Type = DisplayString
_Reconnect2LoadShedTuesdayOn_Object = MibScalar
reconnect2LoadShedTuesdayOn = _Reconnect2LoadShedTuesdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 43),
    _Reconnect2LoadShedTuesdayOn_Type()
)
reconnect2LoadShedTuesdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect2LoadShedTuesdayOn.setStatus("mandatory")
_Reconnect2LoadShedWednesdayOn_Type = DisplayString
_Reconnect2LoadShedWednesdayOn_Object = MibScalar
reconnect2LoadShedWednesdayOn = _Reconnect2LoadShedWednesdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 44),
    _Reconnect2LoadShedWednesdayOn_Type()
)
reconnect2LoadShedWednesdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect2LoadShedWednesdayOn.setStatus("mandatory")
_Reconnect2LoadShedThursdayOn_Type = DisplayString
_Reconnect2LoadShedThursdayOn_Object = MibScalar
reconnect2LoadShedThursdayOn = _Reconnect2LoadShedThursdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 45),
    _Reconnect2LoadShedThursdayOn_Type()
)
reconnect2LoadShedThursdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect2LoadShedThursdayOn.setStatus("mandatory")
_Reconnect2LoadShedFridayOn_Type = DisplayString
_Reconnect2LoadShedFridayOn_Object = MibScalar
reconnect2LoadShedFridayOn = _Reconnect2LoadShedFridayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 46),
    _Reconnect2LoadShedFridayOn_Type()
)
reconnect2LoadShedFridayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect2LoadShedFridayOn.setStatus("mandatory")
_Reconnect2LoadShedSaturdayOn_Type = DisplayString
_Reconnect2LoadShedSaturdayOn_Object = MibScalar
reconnect2LoadShedSaturdayOn = _Reconnect2LoadShedSaturdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 47),
    _Reconnect2LoadShedSaturdayOn_Type()
)
reconnect2LoadShedSaturdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect2LoadShedSaturdayOn.setStatus("mandatory")
_Reconnect3Voltage_Type = Integer32
_Reconnect3Voltage_Object = MibScalar
reconnect3Voltage = _Reconnect3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 48),
    _Reconnect3Voltage_Type()
)
reconnect3Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect3Voltage.setStatus("mandatory")
_Reconnect3LoadShedSundayOn_Type = DisplayString
_Reconnect3LoadShedSundayOn_Object = MibScalar
reconnect3LoadShedSundayOn = _Reconnect3LoadShedSundayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 49),
    _Reconnect3LoadShedSundayOn_Type()
)
reconnect3LoadShedSundayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect3LoadShedSundayOn.setStatus("mandatory")
_Reconnect3LoadShedMondayOn_Type = DisplayString
_Reconnect3LoadShedMondayOn_Object = MibScalar
reconnect3LoadShedMondayOn = _Reconnect3LoadShedMondayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 50),
    _Reconnect3LoadShedMondayOn_Type()
)
reconnect3LoadShedMondayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect3LoadShedMondayOn.setStatus("mandatory")
_Reconnect3LoadShedTuesdayOn_Type = DisplayString
_Reconnect3LoadShedTuesdayOn_Object = MibScalar
reconnect3LoadShedTuesdayOn = _Reconnect3LoadShedTuesdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 51),
    _Reconnect3LoadShedTuesdayOn_Type()
)
reconnect3LoadShedTuesdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect3LoadShedTuesdayOn.setStatus("mandatory")
_Reconnect3LoadShedWednesdayOn_Type = DisplayString
_Reconnect3LoadShedWednesdayOn_Object = MibScalar
reconnect3LoadShedWednesdayOn = _Reconnect3LoadShedWednesdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 52),
    _Reconnect3LoadShedWednesdayOn_Type()
)
reconnect3LoadShedWednesdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect3LoadShedWednesdayOn.setStatus("mandatory")
_Reconnect3LoadShedThursdayOn_Type = DisplayString
_Reconnect3LoadShedThursdayOn_Object = MibScalar
reconnect3LoadShedThursdayOn = _Reconnect3LoadShedThursdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 53),
    _Reconnect3LoadShedThursdayOn_Type()
)
reconnect3LoadShedThursdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect3LoadShedThursdayOn.setStatus("mandatory")
_Reconnect3LoadShedFridayOn_Type = DisplayString
_Reconnect3LoadShedFridayOn_Object = MibScalar
reconnect3LoadShedFridayOn = _Reconnect3LoadShedFridayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 54),
    _Reconnect3LoadShedFridayOn_Type()
)
reconnect3LoadShedFridayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect3LoadShedFridayOn.setStatus("mandatory")
_Reconnect3LoadShedSaturdayOn_Type = DisplayString
_Reconnect3LoadShedSaturdayOn_Object = MibScalar
reconnect3LoadShedSaturdayOn = _Reconnect3LoadShedSaturdayOn_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 55),
    _Reconnect3LoadShedSaturdayOn_Type()
)
reconnect3LoadShedSaturdayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reconnect3LoadShedSaturdayOn.setStatus("mandatory")
_EqualizeTime_Type = Integer32
_EqualizeTime_Object = MibScalar
equalizeTime = _EqualizeTime_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 56),
    _EqualizeTime_Type()
)
equalizeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equalizeTime.setStatus("mandatory")
_EqualizeVoltage_Type = Integer32
_EqualizeVoltage_Object = MibScalar
equalizeVoltage = _EqualizeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 57),
    _EqualizeVoltage_Type()
)
equalizeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equalizeVoltage.setStatus("mandatory")
_BatteryResistancePercentChange_Type = Integer32
_BatteryResistancePercentChange_Object = MibScalar
batteryResistancePercentChange = _BatteryResistancePercentChange_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 58),
    _BatteryResistancePercentChange_Type()
)
batteryResistancePercentChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryResistancePercentChange.setStatus("mandatory")
_BatteryResistanceTestInterval_Type = Integer32
_BatteryResistanceTestInterval_Object = MibScalar
batteryResistanceTestInterval = _BatteryResistanceTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 59),
    _BatteryResistanceTestInterval_Type()
)
batteryResistanceTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryResistanceTestInterval.setStatus("mandatory")


class _LoadShedTimeControl_Type(Integer32):
    """Custom type loadShedTimeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_LoadShedTimeControl_Type.__name__ = "Integer32"
_LoadShedTimeControl_Object = MibScalar
loadShedTimeControl = _LoadShedTimeControl_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 60),
    _LoadShedTimeControl_Type()
)
loadShedTimeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadShedTimeControl.setStatus("mandatory")
_BatteryFloatCurrent_Type = Integer32
_BatteryFloatCurrent_Object = MibScalar
batteryFloatCurrent = _BatteryFloatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 1, 1, 61),
    _BatteryFloatCurrent_Type()
)
batteryFloatCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryFloatCurrent.setStatus("mandatory")
_ReadOnlyObjects_ObjectIdentity = ObjectIdentity
readOnlyObjects = _ReadOnlyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2)
)
_Rectifiers_ObjectIdentity = ObjectIdentity
rectifiers = _Rectifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 1)
)
_RectifierFloatVoltage_Type = Integer32
_RectifierFloatVoltage_Object = MibScalar
rectifierFloatVoltage = _RectifierFloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 1, 1),
    _RectifierFloatVoltage_Type()
)
rectifierFloatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierFloatVoltage.setStatus("mandatory")
_RectifierLoadCurrent_Type = Integer32
_RectifierLoadCurrent_Object = MibScalar
rectifierLoadCurrent = _RectifierLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 1, 2),
    _RectifierLoadCurrent_Type()
)
rectifierLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierLoadCurrent.setStatus("mandatory")
_Batteries_ObjectIdentity = ObjectIdentity
batteries = _Batteries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2)
)
_BatteryCurrent_Type = Integer32
_BatteryCurrent_Object = MibScalar
batteryCurrent = _BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 1),
    _BatteryCurrent_Type()
)
batteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrent.setStatus("mandatory")
_BatteryTemperature_Type = Integer32
_BatteryTemperature_Object = MibScalar
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 2),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("mandatory")
_BatteryResistanceReference_Type = Integer32
_BatteryResistanceReference_Object = MibScalar
batteryResistanceReference = _BatteryResistanceReference_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 3),
    _BatteryResistanceReference_Type()
)
batteryResistanceReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryResistanceReference.setStatus("mandatory")
_BatteryResistanceReading_Type = Integer32
_BatteryResistanceReading_Object = MibScalar
batteryResistanceReading = _BatteryResistanceReading_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 4),
    _BatteryResistanceReading_Type()
)
batteryResistanceReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryResistanceReading.setStatus("mandatory")
_BatteryResistanceChange_Type = Integer32
_BatteryResistanceChange_Object = MibScalar
batteryResistanceChange = _BatteryResistanceChange_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 5),
    _BatteryResistanceChange_Type()
)
batteryResistanceChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryResistanceChange.setStatus("mandatory")
_BatteryCycles1_Type = Integer32
_BatteryCycles1_Object = MibScalar
batteryCycles1 = _BatteryCycles1_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 6),
    _BatteryCycles1_Type()
)
batteryCycles1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycles1.setStatus("mandatory")
_BatteryCycles1to5_Type = Integer32
_BatteryCycles1to5_Object = MibScalar
batteryCycles1to5 = _BatteryCycles1to5_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 7),
    _BatteryCycles1to5_Type()
)
batteryCycles1to5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycles1to5.setStatus("mandatory")
_BatteryCycles5to15_Type = Integer32
_BatteryCycles5to15_Object = MibScalar
batteryCycles5to15 = _BatteryCycles5to15_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 8),
    _BatteryCycles5to15_Type()
)
batteryCycles5to15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycles5to15.setStatus("mandatory")
_BatteryCycles15_Type = Integer32
_BatteryCycles15_Object = MibScalar
batteryCycles15 = _BatteryCycles15_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 9),
    _BatteryCycles15_Type()
)
batteryCycles15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycles15.setStatus("mandatory")
_BatteryCycles15LastCycleDate_Type = DisplayString
_BatteryCycles15LastCycleDate_Object = MibScalar
batteryCycles15LastCycleDate = _BatteryCycles15LastCycleDate_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 10),
    _BatteryCycles15LastCycleDate_Type()
)
batteryCycles15LastCycleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycles15LastCycleDate.setStatus("mandatory")
_BatteryCycles15LastDuration_Type = Integer32
_BatteryCycles15LastDuration_Object = MibScalar
batteryCycles15LastDuration = _BatteryCycles15LastDuration_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 11),
    _BatteryCycles15LastDuration_Type()
)
batteryCycles15LastDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycles15LastDuration.setStatus("mandatory")


class _BatteryTestFault_Type(Integer32):
    """Custom type batteryTestFault based on Integer32"""
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
        *(("abort1", 1),
          ("abort2", 2),
          ("abort3", 3),
          ("none", 4))
    )


_BatteryTestFault_Type.__name__ = "Integer32"
_BatteryTestFault_Object = MibScalar
batteryTestFault = _BatteryTestFault_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 2, 12),
    _BatteryTestFault_Type()
)
batteryTestFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestFault.setStatus("mandatory")
_FactorySettings_ObjectIdentity = ObjectIdentity
factorySettings = _FactorySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3)
)
_FloatVoltagePresets_Type = DisplayString
_FloatVoltagePresets_Object = MibScalar
floatVoltagePresets = _FloatVoltagePresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 1),
    _FloatVoltagePresets_Type()
)
floatVoltagePresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    floatVoltagePresets.setStatus("mandatory")
_HighVoltageAlarmPresets_Type = DisplayString
_HighVoltageAlarmPresets_Object = MibScalar
highVoltageAlarmPresets = _HighVoltageAlarmPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 2),
    _HighVoltageAlarmPresets_Type()
)
highVoltageAlarmPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highVoltageAlarmPresets.setStatus("mandatory")
_LowVoltageAlarmPresets_Type = DisplayString
_LowVoltageAlarmPresets_Object = MibScalar
lowVoltageAlarmPresets = _LowVoltageAlarmPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 3),
    _LowVoltageAlarmPresets_Type()
)
lowVoltageAlarmPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowVoltageAlarmPresets.setStatus("mandatory")
_Disconnect1VoltagePresets_Type = DisplayString
_Disconnect1VoltagePresets_Object = MibScalar
disconnect1VoltagePresets = _Disconnect1VoltagePresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 4),
    _Disconnect1VoltagePresets_Type()
)
disconnect1VoltagePresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect1VoltagePresets.setStatus("mandatory")
_Disconnect1TemperaturePreset_Type = DisplayString
_Disconnect1TemperaturePreset_Object = MibScalar
disconnect1TemperaturePreset = _Disconnect1TemperaturePreset_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 5),
    _Disconnect1TemperaturePreset_Type()
)
disconnect1TemperaturePreset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect1TemperaturePreset.setStatus("mandatory")
_Disconnect1LoadShedSundayPresets_Type = DisplayString
_Disconnect1LoadShedSundayPresets_Object = MibScalar
disconnect1LoadShedSundayPresets = _Disconnect1LoadShedSundayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 6),
    _Disconnect1LoadShedSundayPresets_Type()
)
disconnect1LoadShedSundayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect1LoadShedSundayPresets.setStatus("mandatory")
_Disconnect1LoadShedMondayPresets_Type = DisplayString
_Disconnect1LoadShedMondayPresets_Object = MibScalar
disconnect1LoadShedMondayPresets = _Disconnect1LoadShedMondayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 7),
    _Disconnect1LoadShedMondayPresets_Type()
)
disconnect1LoadShedMondayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect1LoadShedMondayPresets.setStatus("mandatory")
_Disconnect1LoadShedTuesdayPresets_Type = DisplayString
_Disconnect1LoadShedTuesdayPresets_Object = MibScalar
disconnect1LoadShedTuesdayPresets = _Disconnect1LoadShedTuesdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 8),
    _Disconnect1LoadShedTuesdayPresets_Type()
)
disconnect1LoadShedTuesdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect1LoadShedTuesdayPresets.setStatus("mandatory")
_Disconnect1LoadShedWednesdayPresets_Type = DisplayString
_Disconnect1LoadShedWednesdayPresets_Object = MibScalar
disconnect1LoadShedWednesdayPresets = _Disconnect1LoadShedWednesdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 9),
    _Disconnect1LoadShedWednesdayPresets_Type()
)
disconnect1LoadShedWednesdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect1LoadShedWednesdayPresets.setStatus("mandatory")
_Disconnect1LoadShedThursdayPresets_Type = DisplayString
_Disconnect1LoadShedThursdayPresets_Object = MibScalar
disconnect1LoadShedThursdayPresets = _Disconnect1LoadShedThursdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 10),
    _Disconnect1LoadShedThursdayPresets_Type()
)
disconnect1LoadShedThursdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect1LoadShedThursdayPresets.setStatus("mandatory")
_Disconnect1LoadShedFridayPresets_Type = DisplayString
_Disconnect1LoadShedFridayPresets_Object = MibScalar
disconnect1LoadShedFridayPresets = _Disconnect1LoadShedFridayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 11),
    _Disconnect1LoadShedFridayPresets_Type()
)
disconnect1LoadShedFridayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect1LoadShedFridayPresets.setStatus("mandatory")
_Disconnect1LoadShedSaturdayPresets_Type = DisplayString
_Disconnect1LoadShedSaturdayPresets_Object = MibScalar
disconnect1LoadShedSaturdayPresets = _Disconnect1LoadShedSaturdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 12),
    _Disconnect1LoadShedSaturdayPresets_Type()
)
disconnect1LoadShedSaturdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect1LoadShedSaturdayPresets.setStatus("mandatory")
_ReconnectVoltage1Presets_Type = DisplayString
_ReconnectVoltage1Presets_Object = MibScalar
reconnectVoltage1Presets = _ReconnectVoltage1Presets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 13),
    _ReconnectVoltage1Presets_Type()
)
reconnectVoltage1Presets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reconnectVoltage1Presets.setStatus("mandatory")
_Disconnect2VoltagePresets_Type = DisplayString
_Disconnect2VoltagePresets_Object = MibScalar
disconnect2VoltagePresets = _Disconnect2VoltagePresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 14),
    _Disconnect2VoltagePresets_Type()
)
disconnect2VoltagePresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect2VoltagePresets.setStatus("mandatory")
_Disconnect2TemperaturePreset_Type = DisplayString
_Disconnect2TemperaturePreset_Object = MibScalar
disconnect2TemperaturePreset = _Disconnect2TemperaturePreset_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 15),
    _Disconnect2TemperaturePreset_Type()
)
disconnect2TemperaturePreset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect2TemperaturePreset.setStatus("mandatory")
_Disconnect2LoadShedSundayPresets_Type = DisplayString
_Disconnect2LoadShedSundayPresets_Object = MibScalar
disconnect2LoadShedSundayPresets = _Disconnect2LoadShedSundayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 16),
    _Disconnect2LoadShedSundayPresets_Type()
)
disconnect2LoadShedSundayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect2LoadShedSundayPresets.setStatus("mandatory")
_Disconnect2LoadShedMondayPresets_Type = DisplayString
_Disconnect2LoadShedMondayPresets_Object = MibScalar
disconnect2LoadShedMondayPresets = _Disconnect2LoadShedMondayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 17),
    _Disconnect2LoadShedMondayPresets_Type()
)
disconnect2LoadShedMondayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect2LoadShedMondayPresets.setStatus("mandatory")
_Disconnect2LoadShedTuesdayPresets_Type = DisplayString
_Disconnect2LoadShedTuesdayPresets_Object = MibScalar
disconnect2LoadShedTuesdayPresets = _Disconnect2LoadShedTuesdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 18),
    _Disconnect2LoadShedTuesdayPresets_Type()
)
disconnect2LoadShedTuesdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect2LoadShedTuesdayPresets.setStatus("mandatory")
_Disconnect2LoadShedWednesdayPresets_Type = DisplayString
_Disconnect2LoadShedWednesdayPresets_Object = MibScalar
disconnect2LoadShedWednesdayPresets = _Disconnect2LoadShedWednesdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 19),
    _Disconnect2LoadShedWednesdayPresets_Type()
)
disconnect2LoadShedWednesdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect2LoadShedWednesdayPresets.setStatus("mandatory")
_Disconnect2LoadShedThursdayPresets_Type = DisplayString
_Disconnect2LoadShedThursdayPresets_Object = MibScalar
disconnect2LoadShedThursdayPresets = _Disconnect2LoadShedThursdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 20),
    _Disconnect2LoadShedThursdayPresets_Type()
)
disconnect2LoadShedThursdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect2LoadShedThursdayPresets.setStatus("mandatory")
_Disconnect2LoadShedFridayPresets_Type = DisplayString
_Disconnect2LoadShedFridayPresets_Object = MibScalar
disconnect2LoadShedFridayPresets = _Disconnect2LoadShedFridayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 21),
    _Disconnect2LoadShedFridayPresets_Type()
)
disconnect2LoadShedFridayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect2LoadShedFridayPresets.setStatus("mandatory")
_Disconnect2LoadShedSaturdayPresets_Type = DisplayString
_Disconnect2LoadShedSaturdayPresets_Object = MibScalar
disconnect2LoadShedSaturdayPresets = _Disconnect2LoadShedSaturdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 22),
    _Disconnect2LoadShedSaturdayPresets_Type()
)
disconnect2LoadShedSaturdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect2LoadShedSaturdayPresets.setStatus("mandatory")
_Reconnect2VoltagePresets_Type = DisplayString
_Reconnect2VoltagePresets_Object = MibScalar
reconnect2VoltagePresets = _Reconnect2VoltagePresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 23),
    _Reconnect2VoltagePresets_Type()
)
reconnect2VoltagePresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reconnect2VoltagePresets.setStatus("mandatory")
_Disconnect3VoltagePresets_Type = DisplayString
_Disconnect3VoltagePresets_Object = MibScalar
disconnect3VoltagePresets = _Disconnect3VoltagePresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 24),
    _Disconnect3VoltagePresets_Type()
)
disconnect3VoltagePresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect3VoltagePresets.setStatus("mandatory")
_Disconnect3TemperaturePreset_Type = DisplayString
_Disconnect3TemperaturePreset_Object = MibScalar
disconnect3TemperaturePreset = _Disconnect3TemperaturePreset_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 25),
    _Disconnect3TemperaturePreset_Type()
)
disconnect3TemperaturePreset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect3TemperaturePreset.setStatus("mandatory")
_Disconnect3LoadShedSundayPresets_Type = DisplayString
_Disconnect3LoadShedSundayPresets_Object = MibScalar
disconnect3LoadShedSundayPresets = _Disconnect3LoadShedSundayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 26),
    _Disconnect3LoadShedSundayPresets_Type()
)
disconnect3LoadShedSundayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect3LoadShedSundayPresets.setStatus("mandatory")
_Disconnect3LoadShedMondayPresets_Type = DisplayString
_Disconnect3LoadShedMondayPresets_Object = MibScalar
disconnect3LoadShedMondayPresets = _Disconnect3LoadShedMondayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 27),
    _Disconnect3LoadShedMondayPresets_Type()
)
disconnect3LoadShedMondayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect3LoadShedMondayPresets.setStatus("mandatory")
_Disconnect3LoadShedTuesdayPresets_Type = DisplayString
_Disconnect3LoadShedTuesdayPresets_Object = MibScalar
disconnect3LoadShedTuesdayPresets = _Disconnect3LoadShedTuesdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 28),
    _Disconnect3LoadShedTuesdayPresets_Type()
)
disconnect3LoadShedTuesdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect3LoadShedTuesdayPresets.setStatus("mandatory")
_Disconnect3LoadShedWednesdayPresets_Type = DisplayString
_Disconnect3LoadShedWednesdayPresets_Object = MibScalar
disconnect3LoadShedWednesdayPresets = _Disconnect3LoadShedWednesdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 29),
    _Disconnect3LoadShedWednesdayPresets_Type()
)
disconnect3LoadShedWednesdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect3LoadShedWednesdayPresets.setStatus("mandatory")
_Disconnect3LoadShedThursdayPresets_Type = DisplayString
_Disconnect3LoadShedThursdayPresets_Object = MibScalar
disconnect3LoadShedThursdayPresets = _Disconnect3LoadShedThursdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 30),
    _Disconnect3LoadShedThursdayPresets_Type()
)
disconnect3LoadShedThursdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect3LoadShedThursdayPresets.setStatus("mandatory")
_Disconnect3LoadShedFridayPresets_Type = DisplayString
_Disconnect3LoadShedFridayPresets_Object = MibScalar
disconnect3LoadShedFridayPresets = _Disconnect3LoadShedFridayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 31),
    _Disconnect3LoadShedFridayPresets_Type()
)
disconnect3LoadShedFridayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect3LoadShedFridayPresets.setStatus("mandatory")
_Disconnect3LoadShedSaturdayPresets_Type = DisplayString
_Disconnect3LoadShedSaturdayPresets_Object = MibScalar
disconnect3LoadShedSaturdayPresets = _Disconnect3LoadShedSaturdayPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 32),
    _Disconnect3LoadShedSaturdayPresets_Type()
)
disconnect3LoadShedSaturdayPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disconnect3LoadShedSaturdayPresets.setStatus("mandatory")
_Reconnect3VoltagePresets_Type = DisplayString
_Reconnect3VoltagePresets_Object = MibScalar
reconnect3VoltagePresets = _Reconnect3VoltagePresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 33),
    _Reconnect3VoltagePresets_Type()
)
reconnect3VoltagePresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reconnect3VoltagePresets.setStatus("mandatory")
_OverloadCurrentPresets_Type = DisplayString
_OverloadCurrentPresets_Object = MibScalar
overloadCurrentPresets = _OverloadCurrentPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 34),
    _OverloadCurrentPresets_Type()
)
overloadCurrentPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overloadCurrentPresets.setStatus("mandatory")
_MaximumCurrentPreset_Type = DisplayString
_MaximumCurrentPreset_Object = MibScalar
maximumCurrentPreset = _MaximumCurrentPreset_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 35),
    _MaximumCurrentPreset_Type()
)
maximumCurrentPreset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumCurrentPreset.setStatus("mandatory")
_BatteryFloatCurrentPresets_Type = DisplayString
_BatteryFloatCurrentPresets_Object = MibScalar
batteryFloatCurrentPresets = _BatteryFloatCurrentPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 36),
    _BatteryFloatCurrentPresets_Type()
)
batteryFloatCurrentPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFloatCurrentPresets.setStatus("mandatory")
_EqualizeTimePresets_Type = DisplayString
_EqualizeTimePresets_Object = MibScalar
equalizeTimePresets = _EqualizeTimePresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 37),
    _EqualizeTimePresets_Type()
)
equalizeTimePresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equalizeTimePresets.setStatus("mandatory")
_EqualizeVoltagePresets_Type = DisplayString
_EqualizeVoltagePresets_Object = MibScalar
equalizeVoltagePresets = _EqualizeVoltagePresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 38),
    _EqualizeVoltagePresets_Type()
)
equalizeVoltagePresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equalizeVoltagePresets.setStatus("mandatory")
_BatteryResistancePresets_Type = DisplayString
_BatteryResistancePresets_Object = MibScalar
batteryResistancePresets = _BatteryResistancePresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 39),
    _BatteryResistancePresets_Type()
)
batteryResistancePresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryResistancePresets.setStatus("mandatory")
_BatteryTestIntervalPresets_Type = DisplayString
_BatteryTestIntervalPresets_Object = MibScalar
batteryTestIntervalPresets = _BatteryTestIntervalPresets_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 3, 40),
    _BatteryTestIntervalPresets_Type()
)
batteryTestIntervalPresets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestIntervalPresets.setStatus("mandatory")
_AlarmStatus_ObjectIdentity = ObjectIdentity
alarmStatus = _AlarmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4)
)


class _HighVoltageAlarmStatus_Type(Integer32):
    """Custom type highVoltageAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_HighVoltageAlarmStatus_Type.__name__ = "Integer32"
_HighVoltageAlarmStatus_Object = MibScalar
highVoltageAlarmStatus = _HighVoltageAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 1),
    _HighVoltageAlarmStatus_Type()
)
highVoltageAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highVoltageAlarmStatus.setStatus("mandatory")


class _LowVoltageAlarmStatus_Type(Integer32):
    """Custom type lowVoltageAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_LowVoltageAlarmStatus_Type.__name__ = "Integer32"
_LowVoltageAlarmStatus_Object = MibScalar
lowVoltageAlarmStatus = _LowVoltageAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 2),
    _LowVoltageAlarmStatus_Type()
)
lowVoltageAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowVoltageAlarmStatus.setStatus("mandatory")


class _OverloadAlarmStatus_Type(Integer32):
    """Custom type overloadAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_OverloadAlarmStatus_Type.__name__ = "Integer32"
_OverloadAlarmStatus_Object = MibScalar
overloadAlarmStatus = _OverloadAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 3),
    _OverloadAlarmStatus_Type()
)
overloadAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overloadAlarmStatus.setStatus("mandatory")


class _BreakerAlarmStatus_Type(Integer32):
    """Custom type breakerAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BreakerAlarmStatus_Type.__name__ = "Integer32"
_BreakerAlarmStatus_Object = MibScalar
breakerAlarmStatus = _BreakerAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 4),
    _BreakerAlarmStatus_Type()
)
breakerAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerAlarmStatus.setStatus("mandatory")


class _AcFailureAlarmStatus_Type(Integer32):
    """Custom type acFailureAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_AcFailureAlarmStatus_Type.__name__ = "Integer32"
_AcFailureAlarmStatus_Object = MibScalar
acFailureAlarmStatus = _AcFailureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 5),
    _AcFailureAlarmStatus_Type()
)
acFailureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFailureAlarmStatus.setStatus("mandatory")


class _FanFailureAlarmStatus_Type(Integer32):
    """Custom type fanFailureAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_FanFailureAlarmStatus_Type.__name__ = "Integer32"
_FanFailureAlarmStatus_Object = MibScalar
fanFailureAlarmStatus = _FanFailureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 6),
    _FanFailureAlarmStatus_Type()
)
fanFailureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailureAlarmStatus.setStatus("mandatory")


class _RectifierFailureAlarmStatus_Type(Integer32):
    """Custom type rectifierFailureAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_RectifierFailureAlarmStatus_Type.__name__ = "Integer32"
_RectifierFailureAlarmStatus_Object = MibScalar
rectifierFailureAlarmStatus = _RectifierFailureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 7),
    _RectifierFailureAlarmStatus_Type()
)
rectifierFailureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierFailureAlarmStatus.setStatus("mandatory")


class _MajorAlarmStatus_Type(Integer32):
    """Custom type majorAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_MajorAlarmStatus_Type.__name__ = "Integer32"
_MajorAlarmStatus_Object = MibScalar
majorAlarmStatus = _MajorAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 8),
    _MajorAlarmStatus_Type()
)
majorAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorAlarmStatus.setStatus("mandatory")


class _LowVoltageDisconnect1TemperatureAlarmStatus_Type(Integer32):
    """Custom type lowVoltageDisconnect1TemperatureAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_LowVoltageDisconnect1TemperatureAlarmStatus_Type.__name__ = "Integer32"
_LowVoltageDisconnect1TemperatureAlarmStatus_Object = MibScalar
lowVoltageDisconnect1TemperatureAlarmStatus = _LowVoltageDisconnect1TemperatureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 9),
    _LowVoltageDisconnect1TemperatureAlarmStatus_Type()
)
lowVoltageDisconnect1TemperatureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowVoltageDisconnect1TemperatureAlarmStatus.setStatus("mandatory")


class _LowVoltageDisconnect2TemperatureAlarmStatus_Type(Integer32):
    """Custom type lowVoltageDisconnect2TemperatureAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_LowVoltageDisconnect2TemperatureAlarmStatus_Type.__name__ = "Integer32"
_LowVoltageDisconnect2TemperatureAlarmStatus_Object = MibScalar
lowVoltageDisconnect2TemperatureAlarmStatus = _LowVoltageDisconnect2TemperatureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 10),
    _LowVoltageDisconnect2TemperatureAlarmStatus_Type()
)
lowVoltageDisconnect2TemperatureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowVoltageDisconnect2TemperatureAlarmStatus.setStatus("mandatory")


class _LowVoltageDisconnect3TemperatureAlarmStatus_Type(Integer32):
    """Custom type lowVoltageDisconnect3TemperatureAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_LowVoltageDisconnect3TemperatureAlarmStatus_Type.__name__ = "Integer32"
_LowVoltageDisconnect3TemperatureAlarmStatus_Object = MibScalar
lowVoltageDisconnect3TemperatureAlarmStatus = _LowVoltageDisconnect3TemperatureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 11),
    _LowVoltageDisconnect3TemperatureAlarmStatus_Type()
)
lowVoltageDisconnect3TemperatureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowVoltageDisconnect3TemperatureAlarmStatus.setStatus("mandatory")


class _LowVoltageDisconnect1VoltageAlarmStatus_Type(Integer32):
    """Custom type lowVoltageDisconnect1VoltageAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_LowVoltageDisconnect1VoltageAlarmStatus_Type.__name__ = "Integer32"
_LowVoltageDisconnect1VoltageAlarmStatus_Object = MibScalar
lowVoltageDisconnect1VoltageAlarmStatus = _LowVoltageDisconnect1VoltageAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 12),
    _LowVoltageDisconnect1VoltageAlarmStatus_Type()
)
lowVoltageDisconnect1VoltageAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowVoltageDisconnect1VoltageAlarmStatus.setStatus("mandatory")


class _LowVoltageDisconnect2VoltageAlarmStatus_Type(Integer32):
    """Custom type lowVoltageDisconnect2VoltageAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_LowVoltageDisconnect2VoltageAlarmStatus_Type.__name__ = "Integer32"
_LowVoltageDisconnect2VoltageAlarmStatus_Object = MibScalar
lowVoltageDisconnect2VoltageAlarmStatus = _LowVoltageDisconnect2VoltageAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 13),
    _LowVoltageDisconnect2VoltageAlarmStatus_Type()
)
lowVoltageDisconnect2VoltageAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowVoltageDisconnect2VoltageAlarmStatus.setStatus("mandatory")


class _LowVoltageDisconnect3VoltageAlarmStatus_Type(Integer32):
    """Custom type lowVoltageDisconnect3VoltageAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_LowVoltageDisconnect3VoltageAlarmStatus_Type.__name__ = "Integer32"
_LowVoltageDisconnect3VoltageAlarmStatus_Object = MibScalar
lowVoltageDisconnect3VoltageAlarmStatus = _LowVoltageDisconnect3VoltageAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 14),
    _LowVoltageDisconnect3VoltageAlarmStatus_Type()
)
lowVoltageDisconnect3VoltageAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowVoltageDisconnect3VoltageAlarmStatus.setStatus("mandatory")


class _BatteryResistanceAlarmStatus_Type(Integer32):
    """Custom type batteryResistanceAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BatteryResistanceAlarmStatus_Type.__name__ = "Integer32"
_BatteryResistanceAlarmStatus_Object = MibScalar
batteryResistanceAlarmStatus = _BatteryResistanceAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 15),
    _BatteryResistanceAlarmStatus_Type()
)
batteryResistanceAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryResistanceAlarmStatus.setStatus("mandatory")


class _BatteryCurrentAlarmStatus_Type(Integer32):
    """Custom type batteryCurrentAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BatteryCurrentAlarmStatus_Type.__name__ = "Integer32"
_BatteryCurrentAlarmStatus_Object = MibScalar
batteryCurrentAlarmStatus = _BatteryCurrentAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 16),
    _BatteryCurrentAlarmStatus_Type()
)
batteryCurrentAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentAlarmStatus.setStatus("mandatory")


class _BatteryTestAbortCondition1AlarmStatus_Type(Integer32):
    """Custom type batteryTestAbortCondition1AlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BatteryTestAbortCondition1AlarmStatus_Type.__name__ = "Integer32"
_BatteryTestAbortCondition1AlarmStatus_Object = MibScalar
batteryTestAbortCondition1AlarmStatus = _BatteryTestAbortCondition1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 17),
    _BatteryTestAbortCondition1AlarmStatus_Type()
)
batteryTestAbortCondition1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestAbortCondition1AlarmStatus.setStatus("mandatory")


class _BatteryTestAbortCondition2AlarmStatus_Type(Integer32):
    """Custom type batteryTestAbortCondition2AlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BatteryTestAbortCondition2AlarmStatus_Type.__name__ = "Integer32"
_BatteryTestAbortCondition2AlarmStatus_Object = MibScalar
batteryTestAbortCondition2AlarmStatus = _BatteryTestAbortCondition2AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 18),
    _BatteryTestAbortCondition2AlarmStatus_Type()
)
batteryTestAbortCondition2AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestAbortCondition2AlarmStatus.setStatus("mandatory")


class _BatteryTestAbortCondition3AlarmStatus_Type(Integer32):
    """Custom type batteryTestAbortCondition3AlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BatteryTestAbortCondition3AlarmStatus_Type.__name__ = "Integer32"
_BatteryTestAbortCondition3AlarmStatus_Object = MibScalar
batteryTestAbortCondition3AlarmStatus = _BatteryTestAbortCondition3AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 19),
    _BatteryTestAbortCondition3AlarmStatus_Type()
)
batteryTestAbortCondition3AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestAbortCondition3AlarmStatus.setStatus("mandatory")


class _BatteryDisconnectAlarmStatus_Type(Integer32):
    """Custom type batteryDisconnectAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BatteryDisconnectAlarmStatus_Type.__name__ = "Integer32"
_BatteryDisconnectAlarmStatus_Object = MibScalar
batteryDisconnectAlarmStatus = _BatteryDisconnectAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 20),
    _BatteryDisconnectAlarmStatus_Type()
)
batteryDisconnectAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryDisconnectAlarmStatus.setStatus("mandatory")


class _FuseAlarmStatus_Type(Integer32):
    """Custom type fuseAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_FuseAlarmStatus_Type.__name__ = "Integer32"
_FuseAlarmStatus_Object = MibScalar
fuseAlarmStatus = _FuseAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 4, 21),
    _FuseAlarmStatus_Type()
)
fuseAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuseAlarmStatus.setStatus("mandatory")
_DigitalSensorAlarms_ObjectIdentity = ObjectIdentity
digitalSensorAlarms = _DigitalSensorAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 5)
)
_SystemAlarms_ObjectIdentity = ObjectIdentity
systemAlarms = _SystemAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 6)
)
_DigitalSensorAlarmClears_ObjectIdentity = ObjectIdentity
digitalSensorAlarmClears = _DigitalSensorAlarmClears_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 7)
)
_SystemAlarmClears_ObjectIdentity = ObjectIdentity
systemAlarmClears = _SystemAlarmClears_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18642, 1, 2, 8)
)

# Managed Objects groups


# Notification objects

breakerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 0)
)
if mibBuilder.loadTexts:
    breakerTrap.setStatus(
        ""
    )

fuseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 1)
)
if mibBuilder.loadTexts:
    fuseTrap.setStatus(
        ""
    )

batteryDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 2)
)
if mibBuilder.loadTexts:
    batteryDisconnectTrap.setStatus(
        ""
    )

programmableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 3)
)
if mibBuilder.loadTexts:
    programmableTrap.setStatus(
        ""
    )

highVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 4)
)
if mibBuilder.loadTexts:
    highVoltageTrap.setStatus(
        ""
    )

lowVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 5)
)
if mibBuilder.loadTexts:
    lowVoltageTrap.setStatus(
        ""
    )

loadOverCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 6)
)
if mibBuilder.loadTexts:
    loadOverCurrentTrap.setStatus(
        ""
    )

batteryFloatCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 7)
)
if mibBuilder.loadTexts:
    batteryFloatCurrentTrap.setStatus(
        ""
    )

loadDisconnect1VoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 8)
)
if mibBuilder.loadTexts:
    loadDisconnect1VoltageTrap.setStatus(
        ""
    )

loadDisconnect2VoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 9)
)
if mibBuilder.loadTexts:
    loadDisconnect2VoltageTrap.setStatus(
        ""
    )

loadDisconnect3VoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 10)
)
if mibBuilder.loadTexts:
    loadDisconnect3VoltageTrap.setStatus(
        ""
    )

loadDisconnect1TemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 11)
)
if mibBuilder.loadTexts:
    loadDisconnect1TemperatureTrap.setStatus(
        ""
    )

loadDisconnect2TemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 12)
)
if mibBuilder.loadTexts:
    loadDisconnect2TemperatureTrap.setStatus(
        ""
    )

loadDisconnect3TemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 13)
)
if mibBuilder.loadTexts:
    loadDisconnect3TemperatureTrap.setStatus(
        ""
    )

rectifierFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 14)
)
if mibBuilder.loadTexts:
    rectifierFailureTrap.setStatus(
        ""
    )

fanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 15)
)
if mibBuilder.loadTexts:
    fanFailureTrap.setStatus(
        ""
    )

acFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 16)
)
if mibBuilder.loadTexts:
    acFailureTrap.setStatus(
        ""
    )

majorFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 17)
)
if mibBuilder.loadTexts:
    majorFailureTrap.setStatus(
        ""
    )

batteryResistanceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 18)
)
if mibBuilder.loadTexts:
    batteryResistanceTrap.setStatus(
        ""
    )

batteryTestAbort1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 19)
)
if mibBuilder.loadTexts:
    batteryTestAbort1Trap.setStatus(
        ""
    )

batteryTestAbort2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 20)
)
if mibBuilder.loadTexts:
    batteryTestAbort2Trap.setStatus(
        ""
    )

batteryTestAbort3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 21)
)
if mibBuilder.loadTexts:
    batteryTestAbort3Trap.setStatus(
        ""
    )

breakerTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 100)
)
if mibBuilder.loadTexts:
    breakerTrapClear.setStatus(
        ""
    )

fuseTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 101)
)
if mibBuilder.loadTexts:
    fuseTrapClear.setStatus(
        ""
    )

batteryDisconnectTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 102)
)
if mibBuilder.loadTexts:
    batteryDisconnectTrapClear.setStatus(
        ""
    )

programmableTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 103)
)
if mibBuilder.loadTexts:
    programmableTrapClear.setStatus(
        ""
    )

highVoltageTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 104)
)
if mibBuilder.loadTexts:
    highVoltageTrapClear.setStatus(
        ""
    )

lowVoltageTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 105)
)
if mibBuilder.loadTexts:
    lowVoltageTrapClear.setStatus(
        ""
    )

loadOverCurrentTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 106)
)
if mibBuilder.loadTexts:
    loadOverCurrentTrapClear.setStatus(
        ""
    )

batteryFloatCurrentTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 107)
)
if mibBuilder.loadTexts:
    batteryFloatCurrentTrapClear.setStatus(
        ""
    )

loadDisconnect1VoltageTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 108)
)
if mibBuilder.loadTexts:
    loadDisconnect1VoltageTrapClear.setStatus(
        ""
    )

loadDisconnect2VoltageTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 109)
)
if mibBuilder.loadTexts:
    loadDisconnect2VoltageTrapClear.setStatus(
        ""
    )

loadDisconnect3VoltageTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 110)
)
if mibBuilder.loadTexts:
    loadDisconnect3VoltageTrapClear.setStatus(
        ""
    )

loadDisconnect1TemperatureTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 111)
)
if mibBuilder.loadTexts:
    loadDisconnect1TemperatureTrapClear.setStatus(
        ""
    )

loadDisconnect2TemperatureTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 112)
)
if mibBuilder.loadTexts:
    loadDisconnect2TemperatureTrapClear.setStatus(
        ""
    )

loadDisconnect3TemperatureTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 113)
)
if mibBuilder.loadTexts:
    loadDisconnect3TemperatureTrapClear.setStatus(
        ""
    )

rectifierFailureTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 114)
)
if mibBuilder.loadTexts:
    rectifierFailureTrapClear.setStatus(
        ""
    )

fanFailureTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 115)
)
if mibBuilder.loadTexts:
    fanFailureTrapClear.setStatus(
        ""
    )

acFailureTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 116)
)
if mibBuilder.loadTexts:
    acFailureTrapClear.setStatus(
        ""
    )

majorFailureTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 117)
)
if mibBuilder.loadTexts:
    majorFailureTrapClear.setStatus(
        ""
    )

batteryResistanceTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 118)
)
if mibBuilder.loadTexts:
    batteryResistanceTrapClear.setStatus(
        ""
    )

batteryTestAbort1TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 119)
)
if mibBuilder.loadTexts:
    batteryTestAbort1TrapClear.setStatus(
        ""
    )

batteryTestAbort2TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 120)
)
if mibBuilder.loadTexts:
    batteryTestAbort2TrapClear.setStatus(
        ""
    )

batteryTestAbort3TrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18642, 0, 121)
)
if mibBuilder.loadTexts:
    batteryTestAbort3TrapClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CCPOWER-MIB",
    **{"ccpower": ccpower,
       "breakerTrap": breakerTrap,
       "fuseTrap": fuseTrap,
       "batteryDisconnectTrap": batteryDisconnectTrap,
       "programmableTrap": programmableTrap,
       "highVoltageTrap": highVoltageTrap,
       "lowVoltageTrap": lowVoltageTrap,
       "loadOverCurrentTrap": loadOverCurrentTrap,
       "batteryFloatCurrentTrap": batteryFloatCurrentTrap,
       "loadDisconnect1VoltageTrap": loadDisconnect1VoltageTrap,
       "loadDisconnect2VoltageTrap": loadDisconnect2VoltageTrap,
       "loadDisconnect3VoltageTrap": loadDisconnect3VoltageTrap,
       "loadDisconnect1TemperatureTrap": loadDisconnect1TemperatureTrap,
       "loadDisconnect2TemperatureTrap": loadDisconnect2TemperatureTrap,
       "loadDisconnect3TemperatureTrap": loadDisconnect3TemperatureTrap,
       "rectifierFailureTrap": rectifierFailureTrap,
       "fanFailureTrap": fanFailureTrap,
       "acFailureTrap": acFailureTrap,
       "majorFailureTrap": majorFailureTrap,
       "batteryResistanceTrap": batteryResistanceTrap,
       "batteryTestAbort1Trap": batteryTestAbort1Trap,
       "batteryTestAbort2Trap": batteryTestAbort2Trap,
       "batteryTestAbort3Trap": batteryTestAbort3Trap,
       "breakerTrapClear": breakerTrapClear,
       "fuseTrapClear": fuseTrapClear,
       "batteryDisconnectTrapClear": batteryDisconnectTrapClear,
       "programmableTrapClear": programmableTrapClear,
       "highVoltageTrapClear": highVoltageTrapClear,
       "lowVoltageTrapClear": lowVoltageTrapClear,
       "loadOverCurrentTrapClear": loadOverCurrentTrapClear,
       "batteryFloatCurrentTrapClear": batteryFloatCurrentTrapClear,
       "loadDisconnect1VoltageTrapClear": loadDisconnect1VoltageTrapClear,
       "loadDisconnect2VoltageTrapClear": loadDisconnect2VoltageTrapClear,
       "loadDisconnect3VoltageTrapClear": loadDisconnect3VoltageTrapClear,
       "loadDisconnect1TemperatureTrapClear": loadDisconnect1TemperatureTrapClear,
       "loadDisconnect2TemperatureTrapClear": loadDisconnect2TemperatureTrapClear,
       "loadDisconnect3TemperatureTrapClear": loadDisconnect3TemperatureTrapClear,
       "rectifierFailureTrapClear": rectifierFailureTrapClear,
       "fanFailureTrapClear": fanFailureTrapClear,
       "acFailureTrapClear": acFailureTrapClear,
       "majorFailureTrapClear": majorFailureTrapClear,
       "batteryResistanceTrapClear": batteryResistanceTrapClear,
       "batteryTestAbort1TrapClear": batteryTestAbort1TrapClear,
       "batteryTestAbort2TrapClear": batteryTestAbort2TrapClear,
       "batteryTestAbort3TrapClear": batteryTestAbort3TrapClear,
       "dcSystem": dcSystem,
       "readWriteObjects": readWriteObjects,
       "settings": settings,
       "floatVoltage": floatVoltage,
       "overloadCurrent": overloadCurrent,
       "highVoltageAlarm": highVoltageAlarm,
       "lowVoltageAlarm": lowVoltageAlarm,
       "disconnect1Voltage": disconnect1Voltage,
       "disconnect1Temperature": disconnect1Temperature,
       "disconnect1LoadShedSundayOff": disconnect1LoadShedSundayOff,
       "disconnect1LoadShedMondayOff": disconnect1LoadShedMondayOff,
       "disconnect1LoadShedTuesdayOff": disconnect1LoadShedTuesdayOff,
       "disconnect1LoadShedWednesdayOff": disconnect1LoadShedWednesdayOff,
       "disconnect1LoadShedThursdayOff": disconnect1LoadShedThursdayOff,
       "disconnect1LoadShedFridayOff": disconnect1LoadShedFridayOff,
       "disconnect1LoadShedSaturdayOff": disconnect1LoadShedSaturdayOff,
       "disconnect2Voltage": disconnect2Voltage,
       "disconnect2Temperature": disconnect2Temperature,
       "disconnect2LoadShedSundayOff": disconnect2LoadShedSundayOff,
       "disconnect2LoadShedMondayOff": disconnect2LoadShedMondayOff,
       "disconnect2LoadShedTuesdayOff": disconnect2LoadShedTuesdayOff,
       "disconnect2LoadShedWednesdayOff": disconnect2LoadShedWednesdayOff,
       "disconnect2LoadShedThursdayOff": disconnect2LoadShedThursdayOff,
       "disconnect2LoadShedFridayOff": disconnect2LoadShedFridayOff,
       "disconnect2LoadShedSaturdayOff": disconnect2LoadShedSaturdayOff,
       "disconnect3Voltage": disconnect3Voltage,
       "disconnect3Temperature": disconnect3Temperature,
       "disconnect3LoadShedSundayOff": disconnect3LoadShedSundayOff,
       "disconnect3LoadShedMondayOff": disconnect3LoadShedMondayOff,
       "disconnect3LoadShedTuesdayOff": disconnect3LoadShedTuesdayOff,
       "disconnect3LoadShedWednesdayOff": disconnect3LoadShedWednesdayOff,
       "disconnect3LoadShedThursdayOff": disconnect3LoadShedThursdayOff,
       "disconnect3LoadShedFridayOff": disconnect3LoadShedFridayOff,
       "disconnect3LoadShedSaturdayOff": disconnect3LoadShedSaturdayOff,
       "reconnect1Voltage": reconnect1Voltage,
       "reconnect1LoadShedSundayOn": reconnect1LoadShedSundayOn,
       "reconnect1LoadShedMondayOn": reconnect1LoadShedMondayOn,
       "reconnect1LoadShedTuesdayOn": reconnect1LoadShedTuesdayOn,
       "reconnect1LoadShedWednesdayOn": reconnect1LoadShedWednesdayOn,
       "reconnect1LoadShedThursdayOn": reconnect1LoadShedThursdayOn,
       "reconnect1LoadShedFridayOn": reconnect1LoadShedFridayOn,
       "reconnect1LoadShedSaturdayOn": reconnect1LoadShedSaturdayOn,
       "reconnect2Voltage": reconnect2Voltage,
       "reconnect2LoadShedSundayOn": reconnect2LoadShedSundayOn,
       "reconnect2LoadShedMondayOn": reconnect2LoadShedMondayOn,
       "reconnect2LoadShedTuesdayOn": reconnect2LoadShedTuesdayOn,
       "reconnect2LoadShedWednesdayOn": reconnect2LoadShedWednesdayOn,
       "reconnect2LoadShedThursdayOn": reconnect2LoadShedThursdayOn,
       "reconnect2LoadShedFridayOn": reconnect2LoadShedFridayOn,
       "reconnect2LoadShedSaturdayOn": reconnect2LoadShedSaturdayOn,
       "reconnect3Voltage": reconnect3Voltage,
       "reconnect3LoadShedSundayOn": reconnect3LoadShedSundayOn,
       "reconnect3LoadShedMondayOn": reconnect3LoadShedMondayOn,
       "reconnect3LoadShedTuesdayOn": reconnect3LoadShedTuesdayOn,
       "reconnect3LoadShedWednesdayOn": reconnect3LoadShedWednesdayOn,
       "reconnect3LoadShedThursdayOn": reconnect3LoadShedThursdayOn,
       "reconnect3LoadShedFridayOn": reconnect3LoadShedFridayOn,
       "reconnect3LoadShedSaturdayOn": reconnect3LoadShedSaturdayOn,
       "equalizeTime": equalizeTime,
       "equalizeVoltage": equalizeVoltage,
       "batteryResistancePercentChange": batteryResistancePercentChange,
       "batteryResistanceTestInterval": batteryResistanceTestInterval,
       "loadShedTimeControl": loadShedTimeControl,
       "batteryFloatCurrent": batteryFloatCurrent,
       "readOnlyObjects": readOnlyObjects,
       "rectifiers": rectifiers,
       "rectifierFloatVoltage": rectifierFloatVoltage,
       "rectifierLoadCurrent": rectifierLoadCurrent,
       "batteries": batteries,
       "batteryCurrent": batteryCurrent,
       "batteryTemperature": batteryTemperature,
       "batteryResistanceReference": batteryResistanceReference,
       "batteryResistanceReading": batteryResistanceReading,
       "batteryResistanceChange": batteryResistanceChange,
       "batteryCycles1": batteryCycles1,
       "batteryCycles1to5": batteryCycles1to5,
       "batteryCycles5to15": batteryCycles5to15,
       "batteryCycles15": batteryCycles15,
       "batteryCycles15LastCycleDate": batteryCycles15LastCycleDate,
       "batteryCycles15LastDuration": batteryCycles15LastDuration,
       "batteryTestFault": batteryTestFault,
       "factorySettings": factorySettings,
       "floatVoltagePresets": floatVoltagePresets,
       "highVoltageAlarmPresets": highVoltageAlarmPresets,
       "lowVoltageAlarmPresets": lowVoltageAlarmPresets,
       "disconnect1VoltagePresets": disconnect1VoltagePresets,
       "disconnect1TemperaturePreset": disconnect1TemperaturePreset,
       "disconnect1LoadShedSundayPresets": disconnect1LoadShedSundayPresets,
       "disconnect1LoadShedMondayPresets": disconnect1LoadShedMondayPresets,
       "disconnect1LoadShedTuesdayPresets": disconnect1LoadShedTuesdayPresets,
       "disconnect1LoadShedWednesdayPresets": disconnect1LoadShedWednesdayPresets,
       "disconnect1LoadShedThursdayPresets": disconnect1LoadShedThursdayPresets,
       "disconnect1LoadShedFridayPresets": disconnect1LoadShedFridayPresets,
       "disconnect1LoadShedSaturdayPresets": disconnect1LoadShedSaturdayPresets,
       "reconnectVoltage1Presets": reconnectVoltage1Presets,
       "disconnect2VoltagePresets": disconnect2VoltagePresets,
       "disconnect2TemperaturePreset": disconnect2TemperaturePreset,
       "disconnect2LoadShedSundayPresets": disconnect2LoadShedSundayPresets,
       "disconnect2LoadShedMondayPresets": disconnect2LoadShedMondayPresets,
       "disconnect2LoadShedTuesdayPresets": disconnect2LoadShedTuesdayPresets,
       "disconnect2LoadShedWednesdayPresets": disconnect2LoadShedWednesdayPresets,
       "disconnect2LoadShedThursdayPresets": disconnect2LoadShedThursdayPresets,
       "disconnect2LoadShedFridayPresets": disconnect2LoadShedFridayPresets,
       "disconnect2LoadShedSaturdayPresets": disconnect2LoadShedSaturdayPresets,
       "reconnect2VoltagePresets": reconnect2VoltagePresets,
       "disconnect3VoltagePresets": disconnect3VoltagePresets,
       "disconnect3TemperaturePreset": disconnect3TemperaturePreset,
       "disconnect3LoadShedSundayPresets": disconnect3LoadShedSundayPresets,
       "disconnect3LoadShedMondayPresets": disconnect3LoadShedMondayPresets,
       "disconnect3LoadShedTuesdayPresets": disconnect3LoadShedTuesdayPresets,
       "disconnect3LoadShedWednesdayPresets": disconnect3LoadShedWednesdayPresets,
       "disconnect3LoadShedThursdayPresets": disconnect3LoadShedThursdayPresets,
       "disconnect3LoadShedFridayPresets": disconnect3LoadShedFridayPresets,
       "disconnect3LoadShedSaturdayPresets": disconnect3LoadShedSaturdayPresets,
       "reconnect3VoltagePresets": reconnect3VoltagePresets,
       "overloadCurrentPresets": overloadCurrentPresets,
       "maximumCurrentPreset": maximumCurrentPreset,
       "batteryFloatCurrentPresets": batteryFloatCurrentPresets,
       "equalizeTimePresets": equalizeTimePresets,
       "equalizeVoltagePresets": equalizeVoltagePresets,
       "batteryResistancePresets": batteryResistancePresets,
       "batteryTestIntervalPresets": batteryTestIntervalPresets,
       "alarmStatus": alarmStatus,
       "highVoltageAlarmStatus": highVoltageAlarmStatus,
       "lowVoltageAlarmStatus": lowVoltageAlarmStatus,
       "overloadAlarmStatus": overloadAlarmStatus,
       "breakerAlarmStatus": breakerAlarmStatus,
       "acFailureAlarmStatus": acFailureAlarmStatus,
       "fanFailureAlarmStatus": fanFailureAlarmStatus,
       "rectifierFailureAlarmStatus": rectifierFailureAlarmStatus,
       "majorAlarmStatus": majorAlarmStatus,
       "lowVoltageDisconnect1TemperatureAlarmStatus": lowVoltageDisconnect1TemperatureAlarmStatus,
       "lowVoltageDisconnect2TemperatureAlarmStatus": lowVoltageDisconnect2TemperatureAlarmStatus,
       "lowVoltageDisconnect3TemperatureAlarmStatus": lowVoltageDisconnect3TemperatureAlarmStatus,
       "lowVoltageDisconnect1VoltageAlarmStatus": lowVoltageDisconnect1VoltageAlarmStatus,
       "lowVoltageDisconnect2VoltageAlarmStatus": lowVoltageDisconnect2VoltageAlarmStatus,
       "lowVoltageDisconnect3VoltageAlarmStatus": lowVoltageDisconnect3VoltageAlarmStatus,
       "batteryResistanceAlarmStatus": batteryResistanceAlarmStatus,
       "batteryCurrentAlarmStatus": batteryCurrentAlarmStatus,
       "batteryTestAbortCondition1AlarmStatus": batteryTestAbortCondition1AlarmStatus,
       "batteryTestAbortCondition2AlarmStatus": batteryTestAbortCondition2AlarmStatus,
       "batteryTestAbortCondition3AlarmStatus": batteryTestAbortCondition3AlarmStatus,
       "batteryDisconnectAlarmStatus": batteryDisconnectAlarmStatus,
       "fuseAlarmStatus": fuseAlarmStatus,
       "digitalSensorAlarms": digitalSensorAlarms,
       "systemAlarms": systemAlarms,
       "digitalSensorAlarmClears": digitalSensorAlarmClears,
       "systemAlarmClears": systemAlarmClears}
)
