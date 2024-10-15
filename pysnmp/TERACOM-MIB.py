# SNMP MIB module (TERACOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERACOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:09 2024
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
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 1)
)
snmpMIB.setRevisions(
        ("2015-05-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CONTROLLED(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("analog1", 17),
          ("analog2", 18),
          ("analog3", 19),
          ("analog4", 20),
          ("digital1", 21),
          ("digital2", 22),
          ("digital3", 23),
          ("digital4", 24),
          ("manual", 0),
          ("scheduler1", 25),
          ("scheduler2", 26),
          ("scheduler3", 27),
          ("scheduler4", 28),
          ("sensor11", 1),
          ("sensor12", 9),
          ("sensor21", 2),
          ("sensor22", 10),
          ("sensor31", 3),
          ("sensor32", 11),
          ("sensor41", 4),
          ("sensor42", 12),
          ("sensor51", 5),
          ("sensor52", 13),
          ("sensor61", 6),
          ("sensor62", 14),
          ("sensor71", 7),
          ("sensor72", 15),
          ("sensor81", 8),
          ("sensor82", 16))
    )



# MIB Managed Objects in the order of their OIDs

_Teracom_ObjectIdentity = ObjectIdentity
teracom = _Teracom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783)
)
_Tcw240b_ObjectIdentity = ObjectIdentity
tcw240b = _Tcw240b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1)
)
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 0)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_DateTime_Type = DateAndTime
_DateTime_Object = MibScalar
dateTime = _DateTime_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 1, 3),
    _DateTime_Type()
)
dateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateTime.setStatus("current")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 1)
)
_DeviceID_Type = MacAddress
_DeviceID_Object = MibScalar
deviceID = _DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 1, 1),
    _DeviceID_Type()
)
deviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceID.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_DeviceIP_Type = IpAddress
_DeviceIP_Object = MibScalar
deviceIP = _DeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 1, 3),
    _DeviceIP_Type()
)
deviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIP.setStatus("current")
_Io_ObjectIdentity = ObjectIdentity
io = _Io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2)
)
_SensorsSetup_ObjectIdentity = ObjectIdentity
sensorsSetup = _SensorsSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1)
)
_Sensor1setup_ObjectIdentity = ObjectIdentity
sensor1setup = _Sensor1setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1)
)


class _S1description_Type(DisplayString):
    """Custom type s1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S1description_Type.__name__ = "DisplayString"
_S1description_Object = MibScalar
s1description = _S1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1, 1),
    _S1description_Type()
)
s1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s1description.setStatus("current")
_Sensor11setup_ObjectIdentity = ObjectIdentity
sensor11setup = _Sensor11setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1, 2)
)
_S11MAXx10Int_Type = Integer32
_S11MAXx10Int_Object = MibScalar
s11MAXx10Int = _S11MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1, 2, 1),
    _S11MAXx10Int_Type()
)
s11MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11MAXx10Int.setStatus("current")
_S11MINx10Int_Type = Integer32
_S11MINx10Int_Object = MibScalar
s11MINx10Int = _S11MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1, 2, 2),
    _S11MINx10Int_Type()
)
s11MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11MINx10Int.setStatus("current")
_S11HYSTx10Int_Type = Integer32
_S11HYSTx10Int_Object = MibScalar
s11HYSTx10Int = _S11HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1, 2, 3),
    _S11HYSTx10Int_Type()
)
s11HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11HYSTx10Int.setStatus("current")
_Sensor12setup_ObjectIdentity = ObjectIdentity
sensor12setup = _Sensor12setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1, 3)
)
_S12MAXx10Int_Type = Integer32
_S12MAXx10Int_Object = MibScalar
s12MAXx10Int = _S12MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1, 3, 1),
    _S12MAXx10Int_Type()
)
s12MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12MAXx10Int.setStatus("current")
_S12MINx10Int_Type = Integer32
_S12MINx10Int_Object = MibScalar
s12MINx10Int = _S12MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1, 3, 2),
    _S12MINx10Int_Type()
)
s12MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12MINx10Int.setStatus("current")
_S12HYSTx10Int_Type = Integer32
_S12HYSTx10Int_Object = MibScalar
s12HYSTx10Int = _S12HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 1, 3, 3),
    _S12HYSTx10Int_Type()
)
s12HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12HYSTx10Int.setStatus("current")
_Sensor2setup_ObjectIdentity = ObjectIdentity
sensor2setup = _Sensor2setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2)
)


class _S2description_Type(DisplayString):
    """Custom type s2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S2description_Type.__name__ = "DisplayString"
_S2description_Object = MibScalar
s2description = _S2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2, 1),
    _S2description_Type()
)
s2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s2description.setStatus("current")
_Sensor21setup_ObjectIdentity = ObjectIdentity
sensor21setup = _Sensor21setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2, 2)
)
_S21MAXx10Int_Type = Integer32
_S21MAXx10Int_Object = MibScalar
s21MAXx10Int = _S21MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2, 2, 1),
    _S21MAXx10Int_Type()
)
s21MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21MAXx10Int.setStatus("current")
_S21MINx10Int_Type = Integer32
_S21MINx10Int_Object = MibScalar
s21MINx10Int = _S21MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2, 2, 2),
    _S21MINx10Int_Type()
)
s21MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21MINx10Int.setStatus("current")
_S21HYSTx10Int_Type = Integer32
_S21HYSTx10Int_Object = MibScalar
s21HYSTx10Int = _S21HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2, 2, 3),
    _S21HYSTx10Int_Type()
)
s21HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21HYSTx10Int.setStatus("current")
_Sensor22setup_ObjectIdentity = ObjectIdentity
sensor22setup = _Sensor22setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2, 3)
)
_S22MAXx10Int_Type = Integer32
_S22MAXx10Int_Object = MibScalar
s22MAXx10Int = _S22MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2, 3, 1),
    _S22MAXx10Int_Type()
)
s22MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22MAXx10Int.setStatus("current")
_S22MINx10Int_Type = Integer32
_S22MINx10Int_Object = MibScalar
s22MINx10Int = _S22MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2, 3, 2),
    _S22MINx10Int_Type()
)
s22MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22MINx10Int.setStatus("current")
_S22HYSTx10Int_Type = Integer32
_S22HYSTx10Int_Object = MibScalar
s22HYSTx10Int = _S22HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 2, 3, 3),
    _S22HYSTx10Int_Type()
)
s22HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22HYSTx10Int.setStatus("current")
_Sensor3setup_ObjectIdentity = ObjectIdentity
sensor3setup = _Sensor3setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3)
)


class _S3description_Type(DisplayString):
    """Custom type s3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S3description_Type.__name__ = "DisplayString"
_S3description_Object = MibScalar
s3description = _S3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3, 1),
    _S3description_Type()
)
s3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3description.setStatus("current")
_Sensor31setup_ObjectIdentity = ObjectIdentity
sensor31setup = _Sensor31setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3, 2)
)
_S31MAXx10Int_Type = Integer32
_S31MAXx10Int_Object = MibScalar
s31MAXx10Int = _S31MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3, 2, 1),
    _S31MAXx10Int_Type()
)
s31MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31MAXx10Int.setStatus("current")
_S31MINx10Int_Type = Integer32
_S31MINx10Int_Object = MibScalar
s31MINx10Int = _S31MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3, 2, 2),
    _S31MINx10Int_Type()
)
s31MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31MINx10Int.setStatus("current")
_S31HYSTx10Int_Type = Integer32
_S31HYSTx10Int_Object = MibScalar
s31HYSTx10Int = _S31HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3, 2, 3),
    _S31HYSTx10Int_Type()
)
s31HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31HYSTx10Int.setStatus("current")
_Sensor32setup_ObjectIdentity = ObjectIdentity
sensor32setup = _Sensor32setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3, 3)
)
_S32MAXx10Int_Type = Integer32
_S32MAXx10Int_Object = MibScalar
s32MAXx10Int = _S32MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3, 3, 1),
    _S32MAXx10Int_Type()
)
s32MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32MAXx10Int.setStatus("current")
_S32MINx10Int_Type = Integer32
_S32MINx10Int_Object = MibScalar
s32MINx10Int = _S32MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3, 3, 2),
    _S32MINx10Int_Type()
)
s32MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32MINx10Int.setStatus("current")
_S32HYSTx10Int_Type = Integer32
_S32HYSTx10Int_Object = MibScalar
s32HYSTx10Int = _S32HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 3, 3, 3),
    _S32HYSTx10Int_Type()
)
s32HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32HYSTx10Int.setStatus("current")
_Sensor4setup_ObjectIdentity = ObjectIdentity
sensor4setup = _Sensor4setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4)
)


class _S4description_Type(DisplayString):
    """Custom type s4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S4description_Type.__name__ = "DisplayString"
_S4description_Object = MibScalar
s4description = _S4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4, 1),
    _S4description_Type()
)
s4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s4description.setStatus("current")
_Sensor41setup_ObjectIdentity = ObjectIdentity
sensor41setup = _Sensor41setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4, 2)
)
_S41MAXx10Int_Type = Integer32
_S41MAXx10Int_Object = MibScalar
s41MAXx10Int = _S41MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4, 2, 1),
    _S41MAXx10Int_Type()
)
s41MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41MAXx10Int.setStatus("current")
_S41MINx10Int_Type = Integer32
_S41MINx10Int_Object = MibScalar
s41MINx10Int = _S41MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4, 2, 2),
    _S41MINx10Int_Type()
)
s41MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41MINx10Int.setStatus("current")
_S41HYSTx10Int_Type = Integer32
_S41HYSTx10Int_Object = MibScalar
s41HYSTx10Int = _S41HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4, 2, 3),
    _S41HYSTx10Int_Type()
)
s41HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41HYSTx10Int.setStatus("current")
_Sensor42setup_ObjectIdentity = ObjectIdentity
sensor42setup = _Sensor42setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4, 3)
)
_S42MAXx10Int_Type = Integer32
_S42MAXx10Int_Object = MibScalar
s42MAXx10Int = _S42MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4, 3, 1),
    _S42MAXx10Int_Type()
)
s42MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42MAXx10Int.setStatus("current")
_S42MINx10Int_Type = Integer32
_S42MINx10Int_Object = MibScalar
s42MINx10Int = _S42MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4, 3, 2),
    _S42MINx10Int_Type()
)
s42MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42MINx10Int.setStatus("current")
_S42HYSTx10Int_Type = Integer32
_S42HYSTx10Int_Object = MibScalar
s42HYSTx10Int = _S42HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 4, 3, 3),
    _S42HYSTx10Int_Type()
)
s42HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42HYSTx10Int.setStatus("current")
_Sensor5setup_ObjectIdentity = ObjectIdentity
sensor5setup = _Sensor5setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5)
)


class _S5description_Type(DisplayString):
    """Custom type s5description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S5description_Type.__name__ = "DisplayString"
_S5description_Object = MibScalar
s5description = _S5description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5, 1),
    _S5description_Type()
)
s5description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5description.setStatus("current")
_Sensor51setup_ObjectIdentity = ObjectIdentity
sensor51setup = _Sensor51setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5, 2)
)
_S51MAXx10Int_Type = Integer32
_S51MAXx10Int_Object = MibScalar
s51MAXx10Int = _S51MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5, 2, 1),
    _S51MAXx10Int_Type()
)
s51MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51MAXx10Int.setStatus("current")
_S51MINx10Int_Type = Integer32
_S51MINx10Int_Object = MibScalar
s51MINx10Int = _S51MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5, 2, 2),
    _S51MINx10Int_Type()
)
s51MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51MINx10Int.setStatus("current")
_S51HYSTx10Int_Type = Integer32
_S51HYSTx10Int_Object = MibScalar
s51HYSTx10Int = _S51HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5, 2, 3),
    _S51HYSTx10Int_Type()
)
s51HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51HYSTx10Int.setStatus("current")
_Sensor52setup_ObjectIdentity = ObjectIdentity
sensor52setup = _Sensor52setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5, 3)
)
_S52MAXx10Int_Type = Integer32
_S52MAXx10Int_Object = MibScalar
s52MAXx10Int = _S52MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5, 3, 1),
    _S52MAXx10Int_Type()
)
s52MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52MAXx10Int.setStatus("current")
_S52MINx10Int_Type = Integer32
_S52MINx10Int_Object = MibScalar
s52MINx10Int = _S52MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5, 3, 2),
    _S52MINx10Int_Type()
)
s52MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52MINx10Int.setStatus("current")
_S52HYSTx10Int_Type = Integer32
_S52HYSTx10Int_Object = MibScalar
s52HYSTx10Int = _S52HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 5, 3, 3),
    _S52HYSTx10Int_Type()
)
s52HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52HYSTx10Int.setStatus("current")
_Sensor6setup_ObjectIdentity = ObjectIdentity
sensor6setup = _Sensor6setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6)
)


class _S6description_Type(DisplayString):
    """Custom type s6description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S6description_Type.__name__ = "DisplayString"
_S6description_Object = MibScalar
s6description = _S6description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6, 1),
    _S6description_Type()
)
s6description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s6description.setStatus("current")
_Sensor61setup_ObjectIdentity = ObjectIdentity
sensor61setup = _Sensor61setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6, 2)
)
_S61MAXx10Int_Type = Integer32
_S61MAXx10Int_Object = MibScalar
s61MAXx10Int = _S61MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6, 2, 1),
    _S61MAXx10Int_Type()
)
s61MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61MAXx10Int.setStatus("current")
_S61MINx10Int_Type = Integer32
_S61MINx10Int_Object = MibScalar
s61MINx10Int = _S61MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6, 2, 2),
    _S61MINx10Int_Type()
)
s61MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61MINx10Int.setStatus("current")
_S61HYSTx10Int_Type = Integer32
_S61HYSTx10Int_Object = MibScalar
s61HYSTx10Int = _S61HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6, 2, 3),
    _S61HYSTx10Int_Type()
)
s61HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61HYSTx10Int.setStatus("current")
_Sensor62setup_ObjectIdentity = ObjectIdentity
sensor62setup = _Sensor62setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6, 3)
)
_S62MAXx10Int_Type = Integer32
_S62MAXx10Int_Object = MibScalar
s62MAXx10Int = _S62MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6, 3, 1),
    _S62MAXx10Int_Type()
)
s62MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62MAXx10Int.setStatus("current")
_S62MINx10Int_Type = Integer32
_S62MINx10Int_Object = MibScalar
s62MINx10Int = _S62MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6, 3, 2),
    _S62MINx10Int_Type()
)
s62MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62MINx10Int.setStatus("current")
_S62HYSTx10Int_Type = Integer32
_S62HYSTx10Int_Object = MibScalar
s62HYSTx10Int = _S62HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 6, 3, 3),
    _S62HYSTx10Int_Type()
)
s62HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62HYSTx10Int.setStatus("current")
_Sensor7setup_ObjectIdentity = ObjectIdentity
sensor7setup = _Sensor7setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7)
)


class _S7description_Type(DisplayString):
    """Custom type s7description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S7description_Type.__name__ = "DisplayString"
_S7description_Object = MibScalar
s7description = _S7description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7, 1),
    _S7description_Type()
)
s7description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s7description.setStatus("current")
_Sensor71setup_ObjectIdentity = ObjectIdentity
sensor71setup = _Sensor71setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7, 2)
)
_S71MAXx10Int_Type = Integer32
_S71MAXx10Int_Object = MibScalar
s71MAXx10Int = _S71MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7, 2, 1),
    _S71MAXx10Int_Type()
)
s71MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71MAXx10Int.setStatus("current")
_S71MINx10Int_Type = Integer32
_S71MINx10Int_Object = MibScalar
s71MINx10Int = _S71MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7, 2, 2),
    _S71MINx10Int_Type()
)
s71MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71MINx10Int.setStatus("current")
_S71HYSTx10Int_Type = Integer32
_S71HYSTx10Int_Object = MibScalar
s71HYSTx10Int = _S71HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7, 2, 3),
    _S71HYSTx10Int_Type()
)
s71HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71HYSTx10Int.setStatus("current")
_Sensor72setup_ObjectIdentity = ObjectIdentity
sensor72setup = _Sensor72setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7, 3)
)
_S72MAXx10Int_Type = Integer32
_S72MAXx10Int_Object = MibScalar
s72MAXx10Int = _S72MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7, 3, 1),
    _S72MAXx10Int_Type()
)
s72MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72MAXx10Int.setStatus("current")
_S72MINx10Int_Type = Integer32
_S72MINx10Int_Object = MibScalar
s72MINx10Int = _S72MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7, 3, 2),
    _S72MINx10Int_Type()
)
s72MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72MINx10Int.setStatus("current")
_S72HYSTx10Int_Type = Integer32
_S72HYSTx10Int_Object = MibScalar
s72HYSTx10Int = _S72HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 7, 3, 3),
    _S72HYSTx10Int_Type()
)
s72HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72HYSTx10Int.setStatus("current")
_Sensor8setup_ObjectIdentity = ObjectIdentity
sensor8setup = _Sensor8setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8)
)


class _S8description_Type(DisplayString):
    """Custom type s8description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S8description_Type.__name__ = "DisplayString"
_S8description_Object = MibScalar
s8description = _S8description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8, 1),
    _S8description_Type()
)
s8description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s8description.setStatus("current")
_Sensor81setup_ObjectIdentity = ObjectIdentity
sensor81setup = _Sensor81setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8, 2)
)
_S81MAXx10Int_Type = Integer32
_S81MAXx10Int_Object = MibScalar
s81MAXx10Int = _S81MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8, 2, 1),
    _S81MAXx10Int_Type()
)
s81MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81MAXx10Int.setStatus("current")
_S81MINx10Int_Type = Integer32
_S81MINx10Int_Object = MibScalar
s81MINx10Int = _S81MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8, 2, 2),
    _S81MINx10Int_Type()
)
s81MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81MINx10Int.setStatus("current")
_S81HYSTx10Int_Type = Integer32
_S81HYSTx10Int_Object = MibScalar
s81HYSTx10Int = _S81HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8, 2, 3),
    _S81HYSTx10Int_Type()
)
s81HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81HYSTx10Int.setStatus("current")
_Sensor82setup_ObjectIdentity = ObjectIdentity
sensor82setup = _Sensor82setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8, 3)
)
_S82MAXx10Int_Type = Integer32
_S82MAXx10Int_Object = MibScalar
s82MAXx10Int = _S82MAXx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8, 3, 1),
    _S82MAXx10Int_Type()
)
s82MAXx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82MAXx10Int.setStatus("current")
_S82MINx10Int_Type = Integer32
_S82MINx10Int_Object = MibScalar
s82MINx10Int = _S82MINx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8, 3, 2),
    _S82MINx10Int_Type()
)
s82MINx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82MINx10Int.setStatus("current")
_S82HYSTx10Int_Type = Integer32
_S82HYSTx10Int_Object = MibScalar
s82HYSTx10Int = _S82HYSTx10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 1, 8, 3, 3),
    _S82HYSTx10Int_Type()
)
s82HYSTx10Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82HYSTx10Int.setStatus("current")
_AnalogSetup_ObjectIdentity = ObjectIdentity
analogSetup = _AnalogSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2)
)
_Analog1setup_ObjectIdentity = ObjectIdentity
analog1setup = _Analog1setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 1)
)


class _Voltage1description_Type(DisplayString):
    """Custom type voltage1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Voltage1description_Type.__name__ = "DisplayString"
_Voltage1description_Object = MibScalar
voltage1description = _Voltage1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 1, 1),
    _Voltage1description_Type()
)
voltage1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage1description.setStatus("current")
_Voltage1max_Type = Integer32
_Voltage1max_Object = MibScalar
voltage1max = _Voltage1max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 1, 2),
    _Voltage1max_Type()
)
voltage1max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage1max.setStatus("current")
_Voltage1min_Type = Integer32
_Voltage1min_Object = MibScalar
voltage1min = _Voltage1min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 1, 3),
    _Voltage1min_Type()
)
voltage1min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage1min.setStatus("current")
_Voltage1hyst_Type = Integer32
_Voltage1hyst_Object = MibScalar
voltage1hyst = _Voltage1hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 1, 4),
    _Voltage1hyst_Type()
)
voltage1hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage1hyst.setStatus("current")
_Analog2setup_ObjectIdentity = ObjectIdentity
analog2setup = _Analog2setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 2)
)


class _Voltage2description_Type(DisplayString):
    """Custom type voltage2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Voltage2description_Type.__name__ = "DisplayString"
_Voltage2description_Object = MibScalar
voltage2description = _Voltage2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 2, 1),
    _Voltage2description_Type()
)
voltage2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage2description.setStatus("current")
_Voltage2max_Type = Integer32
_Voltage2max_Object = MibScalar
voltage2max = _Voltage2max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 2, 2),
    _Voltage2max_Type()
)
voltage2max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage2max.setStatus("current")
_Voltage2min_Type = Integer32
_Voltage2min_Object = MibScalar
voltage2min = _Voltage2min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 2, 3),
    _Voltage2min_Type()
)
voltage2min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage2min.setStatus("current")
_Voltage2hyst_Type = Integer32
_Voltage2hyst_Object = MibScalar
voltage2hyst = _Voltage2hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 2, 4),
    _Voltage2hyst_Type()
)
voltage2hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage2hyst.setStatus("current")
_Analog3setup_ObjectIdentity = ObjectIdentity
analog3setup = _Analog3setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 3)
)


class _Voltage3description_Type(DisplayString):
    """Custom type voltage3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Voltage3description_Type.__name__ = "DisplayString"
_Voltage3description_Object = MibScalar
voltage3description = _Voltage3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 3, 1),
    _Voltage3description_Type()
)
voltage3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage3description.setStatus("current")
_Voltage3max_Type = Integer32
_Voltage3max_Object = MibScalar
voltage3max = _Voltage3max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 3, 2),
    _Voltage3max_Type()
)
voltage3max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage3max.setStatus("current")
_Voltage3min_Type = Integer32
_Voltage3min_Object = MibScalar
voltage3min = _Voltage3min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 3, 3),
    _Voltage3min_Type()
)
voltage3min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage3min.setStatus("current")
_Voltage3hyst_Type = Integer32
_Voltage3hyst_Object = MibScalar
voltage3hyst = _Voltage3hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 3, 4),
    _Voltage3hyst_Type()
)
voltage3hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage3hyst.setStatus("current")
_Analog4setup_ObjectIdentity = ObjectIdentity
analog4setup = _Analog4setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 4)
)


class _Voltage4description_Type(DisplayString):
    """Custom type voltage4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Voltage4description_Type.__name__ = "DisplayString"
_Voltage4description_Object = MibScalar
voltage4description = _Voltage4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 4, 1),
    _Voltage4description_Type()
)
voltage4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage4description.setStatus("current")
_Voltage4max_Type = Integer32
_Voltage4max_Object = MibScalar
voltage4max = _Voltage4max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 4, 2),
    _Voltage4max_Type()
)
voltage4max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage4max.setStatus("current")
_Voltage4min_Type = Integer32
_Voltage4min_Object = MibScalar
voltage4min = _Voltage4min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 4, 3),
    _Voltage4min_Type()
)
voltage4min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage4min.setStatus("current")
_Voltage4hyst_Type = Integer32
_Voltage4hyst_Object = MibScalar
voltage4hyst = _Voltage4hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 2, 4, 4),
    _Voltage4hyst_Type()
)
voltage4hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage4hyst.setStatus("current")
_DigitalSetup_ObjectIdentity = ObjectIdentity
digitalSetup = _DigitalSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 3)
)


class _DigitalInput1description_Type(DisplayString):
    """Custom type digitalInput1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DigitalInput1description_Type.__name__ = "DisplayString"
_DigitalInput1description_Object = MibScalar
digitalInput1description = _DigitalInput1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 3, 1),
    _DigitalInput1description_Type()
)
digitalInput1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput1description.setStatus("current")


class _DigitalInput2description_Type(DisplayString):
    """Custom type digitalInput2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DigitalInput2description_Type.__name__ = "DisplayString"
_DigitalInput2description_Object = MibScalar
digitalInput2description = _DigitalInput2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 3, 2),
    _DigitalInput2description_Type()
)
digitalInput2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput2description.setStatus("current")


class _DigitalInput3description_Type(DisplayString):
    """Custom type digitalInput3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DigitalInput3description_Type.__name__ = "DisplayString"
_DigitalInput3description_Object = MibScalar
digitalInput3description = _DigitalInput3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 3, 3),
    _DigitalInput3description_Type()
)
digitalInput3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput3description.setStatus("current")


class _DigitalInput4description_Type(DisplayString):
    """Custom type digitalInput4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DigitalInput4description_Type.__name__ = "DisplayString"
_DigitalInput4description_Object = MibScalar
digitalInput4description = _DigitalInput4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 3, 4),
    _DigitalInput4description_Type()
)
digitalInput4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput4description.setStatus("current")
_RelaysSetup_ObjectIdentity = ObjectIdentity
relaysSetup = _RelaysSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4)
)
_Relay1setup_ObjectIdentity = ObjectIdentity
relay1setup = _Relay1setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 1)
)


class _Relay1description_Type(DisplayString):
    """Custom type relay1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Relay1description_Type.__name__ = "DisplayString"
_Relay1description_Object = MibScalar
relay1description = _Relay1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 1, 1),
    _Relay1description_Type()
)
relay1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1description.setStatus("current")


class _Relay1pulseWidth_Type(Integer32):
    """Custom type relay1pulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Relay1pulseWidth_Type.__name__ = "Integer32"
_Relay1pulseWidth_Object = MibScalar
relay1pulseWidth = _Relay1pulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 1, 2),
    _Relay1pulseWidth_Type()
)
relay1pulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1pulseWidth.setStatus("current")
_Relay1controlledBy_Type = CONTROLLED
_Relay1controlledBy_Object = MibScalar
relay1controlledBy = _Relay1controlledBy_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 1, 3),
    _Relay1controlledBy_Type()
)
relay1controlledBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1controlledBy.setStatus("current")
_Relay2setup_ObjectIdentity = ObjectIdentity
relay2setup = _Relay2setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 2)
)


class _Relay2description_Type(DisplayString):
    """Custom type relay2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Relay2description_Type.__name__ = "DisplayString"
_Relay2description_Object = MibScalar
relay2description = _Relay2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 2, 1),
    _Relay2description_Type()
)
relay2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2description.setStatus("current")


class _Relay2pulseWidth_Type(Integer32):
    """Custom type relay2pulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Relay2pulseWidth_Type.__name__ = "Integer32"
_Relay2pulseWidth_Object = MibScalar
relay2pulseWidth = _Relay2pulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 2, 2),
    _Relay2pulseWidth_Type()
)
relay2pulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2pulseWidth.setStatus("current")
_Relay2controlledBy_Type = CONTROLLED
_Relay2controlledBy_Object = MibScalar
relay2controlledBy = _Relay2controlledBy_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 2, 3),
    _Relay2controlledBy_Type()
)
relay2controlledBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2controlledBy.setStatus("current")
_Relay3setup_ObjectIdentity = ObjectIdentity
relay3setup = _Relay3setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 3)
)


class _Relay3description_Type(DisplayString):
    """Custom type relay3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Relay3description_Type.__name__ = "DisplayString"
_Relay3description_Object = MibScalar
relay3description = _Relay3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 3, 1),
    _Relay3description_Type()
)
relay3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3description.setStatus("current")


class _Relay3pulseWidth_Type(Integer32):
    """Custom type relay3pulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Relay3pulseWidth_Type.__name__ = "Integer32"
_Relay3pulseWidth_Object = MibScalar
relay3pulseWidth = _Relay3pulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 3, 2),
    _Relay3pulseWidth_Type()
)
relay3pulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3pulseWidth.setStatus("current")
_Relay3controlledBy_Type = CONTROLLED
_Relay3controlledBy_Object = MibScalar
relay3controlledBy = _Relay3controlledBy_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 3, 3),
    _Relay3controlledBy_Type()
)
relay3controlledBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3controlledBy.setStatus("current")
_Relay4setup_ObjectIdentity = ObjectIdentity
relay4setup = _Relay4setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 4)
)


class _Relay4description_Type(DisplayString):
    """Custom type relay4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Relay4description_Type.__name__ = "DisplayString"
_Relay4description_Object = MibScalar
relay4description = _Relay4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 4, 1),
    _Relay4description_Type()
)
relay4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4description.setStatus("current")


class _Relay4pulseWidth_Type(Integer32):
    """Custom type relay4pulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Relay4pulseWidth_Type.__name__ = "Integer32"
_Relay4pulseWidth_Object = MibScalar
relay4pulseWidth = _Relay4pulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 4, 2),
    _Relay4pulseWidth_Type()
)
relay4pulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4pulseWidth.setStatus("current")
_Relay4controlledBy_Type = CONTROLLED
_Relay4controlledBy_Object = MibScalar
relay4controlledBy = _Relay4controlledBy_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2, 2, 4, 4, 3),
    _Relay4controlledBy_Type()
)
relay4controlledBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4controlledBy.setStatus("current")
_MonitorNcontrol_ObjectIdentity = ObjectIdentity
monitorNcontrol = _MonitorNcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1)
)
_Sensor1_ObjectIdentity = ObjectIdentity
sensor1 = _Sensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 1)
)
_S11x10Int_Type = Integer32
_S11x10Int_Object = MibScalar
s11x10Int = _S11x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 1, 1),
    _S11x10Int_Type()
)
s11x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s11x10Int.setStatus("current")
_S12x10Int_Type = Integer32
_S12x10Int_Object = MibScalar
s12x10Int = _S12x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 1, 2),
    _S12x10Int_Type()
)
s12x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s12x10Int.setStatus("current")
_S1ID_Type = MacAddress
_S1ID_Object = MibScalar
s1ID = _S1ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 1, 3),
    _S1ID_Type()
)
s1ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s1ID.setStatus("current")
_Sensor2_ObjectIdentity = ObjectIdentity
sensor2 = _Sensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 2)
)
_S21x10Int_Type = Integer32
_S21x10Int_Object = MibScalar
s21x10Int = _S21x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 2, 1),
    _S21x10Int_Type()
)
s21x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s21x10Int.setStatus("current")
_S22x10Int_Type = Integer32
_S22x10Int_Object = MibScalar
s22x10Int = _S22x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 2, 2),
    _S22x10Int_Type()
)
s22x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s22x10Int.setStatus("current")
_S2ID_Type = MacAddress
_S2ID_Object = MibScalar
s2ID = _S2ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 2, 3),
    _S2ID_Type()
)
s2ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2ID.setStatus("current")
_Sensor3_ObjectIdentity = ObjectIdentity
sensor3 = _Sensor3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 3)
)
_S31x10Int_Type = Integer32
_S31x10Int_Object = MibScalar
s31x10Int = _S31x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 3, 1),
    _S31x10Int_Type()
)
s31x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s31x10Int.setStatus("current")
_S32x10Int_Type = Integer32
_S32x10Int_Object = MibScalar
s32x10Int = _S32x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 3, 2),
    _S32x10Int_Type()
)
s32x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s32x10Int.setStatus("current")
_S3ID_Type = MacAddress
_S3ID_Object = MibScalar
s3ID = _S3ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 3, 3),
    _S3ID_Type()
)
s3ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3ID.setStatus("current")
_Sensor4_ObjectIdentity = ObjectIdentity
sensor4 = _Sensor4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 4)
)
_S41x10Int_Type = Integer32
_S41x10Int_Object = MibScalar
s41x10Int = _S41x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 4, 1),
    _S41x10Int_Type()
)
s41x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s41x10Int.setStatus("current")
_S42x10Int_Type = Integer32
_S42x10Int_Object = MibScalar
s42x10Int = _S42x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 4, 2),
    _S42x10Int_Type()
)
s42x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s42x10Int.setStatus("current")
_S4ID_Type = MacAddress
_S4ID_Object = MibScalar
s4ID = _S4ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 4, 3),
    _S4ID_Type()
)
s4ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s4ID.setStatus("current")
_Sensor5_ObjectIdentity = ObjectIdentity
sensor5 = _Sensor5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 5)
)
_S51x10Int_Type = Integer32
_S51x10Int_Object = MibScalar
s51x10Int = _S51x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 5, 1),
    _S51x10Int_Type()
)
s51x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s51x10Int.setStatus("current")
_S52x10Int_Type = Integer32
_S52x10Int_Object = MibScalar
s52x10Int = _S52x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 5, 2),
    _S52x10Int_Type()
)
s52x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s52x10Int.setStatus("current")
_S5ID_Type = MacAddress
_S5ID_Object = MibScalar
s5ID = _S5ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 5, 3),
    _S5ID_Type()
)
s5ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ID.setStatus("current")
_Sensor6_ObjectIdentity = ObjectIdentity
sensor6 = _Sensor6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 6)
)
_S61x10Int_Type = Integer32
_S61x10Int_Object = MibScalar
s61x10Int = _S61x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 6, 1),
    _S61x10Int_Type()
)
s61x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s61x10Int.setStatus("current")
_S62x10Int_Type = Integer32
_S62x10Int_Object = MibScalar
s62x10Int = _S62x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 6, 2),
    _S62x10Int_Type()
)
s62x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s62x10Int.setStatus("current")
_S6ID_Type = MacAddress
_S6ID_Object = MibScalar
s6ID = _S6ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 6, 3),
    _S6ID_Type()
)
s6ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6ID.setStatus("current")
_Sensor7_ObjectIdentity = ObjectIdentity
sensor7 = _Sensor7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 7)
)
_S71x10Int_Type = Integer32
_S71x10Int_Object = MibScalar
s71x10Int = _S71x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 7, 1),
    _S71x10Int_Type()
)
s71x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s71x10Int.setStatus("current")
_S72x10Int_Type = Integer32
_S72x10Int_Object = MibScalar
s72x10Int = _S72x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 7, 2),
    _S72x10Int_Type()
)
s72x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s72x10Int.setStatus("current")
_S7ID_Type = MacAddress
_S7ID_Object = MibScalar
s7ID = _S7ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 7, 3),
    _S7ID_Type()
)
s7ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s7ID.setStatus("current")
_Sensor8_ObjectIdentity = ObjectIdentity
sensor8 = _Sensor8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 8)
)
_S81x10Int_Type = Integer32
_S81x10Int_Object = MibScalar
s81x10Int = _S81x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 8, 1),
    _S81x10Int_Type()
)
s81x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s81x10Int.setStatus("current")
_S82x10Int_Type = Integer32
_S82x10Int_Object = MibScalar
s82x10Int = _S82x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 8, 2),
    _S82x10Int_Type()
)
s82x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s82x10Int.setStatus("current")
_S8ID_Type = MacAddress
_S8ID_Object = MibScalar
s8ID = _S8ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 1, 8, 3),
    _S8ID_Type()
)
s8ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s8ID.setStatus("current")
_Analog_ObjectIdentity = ObjectIdentity
analog = _Analog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 2)
)
_Voltage1x10Int_Type = Integer32
_Voltage1x10Int_Object = MibScalar
voltage1x10Int = _Voltage1x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 2, 1),
    _Voltage1x10Int_Type()
)
voltage1x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage1x10Int.setStatus("current")
_Voltage2x10Int_Type = Integer32
_Voltage2x10Int_Object = MibScalar
voltage2x10Int = _Voltage2x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 2, 2),
    _Voltage2x10Int_Type()
)
voltage2x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage2x10Int.setStatus("current")
_Voltage3x10Int_Type = Integer32
_Voltage3x10Int_Object = MibScalar
voltage3x10Int = _Voltage3x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 2, 3),
    _Voltage3x10Int_Type()
)
voltage3x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage3x10Int.setStatus("current")
_Voltage4x10Int_Type = Integer32
_Voltage4x10Int_Object = MibScalar
voltage4x10Int = _Voltage4x10Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 2, 4),
    _Voltage4x10Int_Type()
)
voltage4x10Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage4x10Int.setStatus("current")
_Voltage1x100Int_Type = Integer32
_Voltage1x100Int_Object = MibScalar
voltage1x100Int = _Voltage1x100Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 2, 5),
    _Voltage1x100Int_Type()
)
voltage1x100Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage1x100Int.setStatus("current")
_Voltage2x100Int_Type = Integer32
_Voltage2x100Int_Object = MibScalar
voltage2x100Int = _Voltage2x100Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 2, 6),
    _Voltage2x100Int_Type()
)
voltage2x100Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage2x100Int.setStatus("current")
_Voltage3x100Int_Type = Integer32
_Voltage3x100Int_Object = MibScalar
voltage3x100Int = _Voltage3x100Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 2, 7),
    _Voltage3x100Int_Type()
)
voltage3x100Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage3x100Int.setStatus("current")
_Voltage4x100Int_Type = Integer32
_Voltage4x100Int_Object = MibScalar
voltage4x100Int = _Voltage4x100Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 2, 8),
    _Voltage4x100Int_Type()
)
voltage4x100Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage4x100Int.setStatus("current")
_Digital_ObjectIdentity = ObjectIdentity
digital = _Digital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 3)
)


class _DigitalInput1State_Type(Integer32):
    """Custom type digitalInput1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigitalInput1State_Type.__name__ = "Integer32"
_DigitalInput1State_Object = MibScalar
digitalInput1State = _DigitalInput1State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 3, 1),
    _DigitalInput1State_Type()
)
digitalInput1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput1State.setStatus("current")


class _DigitalInput2State_Type(Integer32):
    """Custom type digitalInput2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigitalInput2State_Type.__name__ = "Integer32"
_DigitalInput2State_Object = MibScalar
digitalInput2State = _DigitalInput2State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 3, 2),
    _DigitalInput2State_Type()
)
digitalInput2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput2State.setStatus("current")


class _DigitalInput3State_Type(Integer32):
    """Custom type digitalInput3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigitalInput3State_Type.__name__ = "Integer32"
_DigitalInput3State_Object = MibScalar
digitalInput3State = _DigitalInput3State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 3, 3),
    _DigitalInput3State_Type()
)
digitalInput3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput3State.setStatus("current")


class _DigitalInput4State_Type(Integer32):
    """Custom type digitalInput4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigitalInput4State_Type.__name__ = "Integer32"
_DigitalInput4State_Object = MibScalar
digitalInput4State = _DigitalInput4State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 3, 4),
    _DigitalInput4State_Type()
)
digitalInput4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput4State.setStatus("current")
_Relays_ObjectIdentity = ObjectIdentity
relays = _Relays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4)
)
_Relay1_ObjectIdentity = ObjectIdentity
relay1 = _Relay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 1)
)


class _Relay1State_Type(Integer32):
    """Custom type relay1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay1State_Type.__name__ = "Integer32"
_Relay1State_Object = MibScalar
relay1State = _Relay1State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 1, 1),
    _Relay1State_Type()
)
relay1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1State.setStatus("current")


class _Relay1Pulse_Type(Integer32):
    """Custom type relay1Pulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay1Pulse_Type.__name__ = "Integer32"
_Relay1Pulse_Object = MibScalar
relay1Pulse = _Relay1Pulse_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 1, 2),
    _Relay1Pulse_Type()
)
relay1Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1Pulse.setStatus("current")
_Relay2_ObjectIdentity = ObjectIdentity
relay2 = _Relay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 2)
)


class _Relay2State_Type(Integer32):
    """Custom type relay2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay2State_Type.__name__ = "Integer32"
_Relay2State_Object = MibScalar
relay2State = _Relay2State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 2, 1),
    _Relay2State_Type()
)
relay2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2State.setStatus("current")


class _Relay2Pulse_Type(Integer32):
    """Custom type relay2Pulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay2Pulse_Type.__name__ = "Integer32"
_Relay2Pulse_Object = MibScalar
relay2Pulse = _Relay2Pulse_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 2, 2),
    _Relay2Pulse_Type()
)
relay2Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2Pulse.setStatus("current")
_Relay3_ObjectIdentity = ObjectIdentity
relay3 = _Relay3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 3)
)


class _Relay3State_Type(Integer32):
    """Custom type relay3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay3State_Type.__name__ = "Integer32"
_Relay3State_Object = MibScalar
relay3State = _Relay3State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 3, 1),
    _Relay3State_Type()
)
relay3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3State.setStatus("current")


class _Relay3Pulse_Type(Integer32):
    """Custom type relay3Pulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay3Pulse_Type.__name__ = "Integer32"
_Relay3Pulse_Object = MibScalar
relay3Pulse = _Relay3Pulse_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 3, 2),
    _Relay3Pulse_Type()
)
relay3Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3Pulse.setStatus("current")
_Relay4_ObjectIdentity = ObjectIdentity
relay4 = _Relay4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 4)
)


class _Relay4State_Type(Integer32):
    """Custom type relay4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay4State_Type.__name__ = "Integer32"
_Relay4State_Object = MibScalar
relay4State = _Relay4State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 4, 1),
    _Relay4State_Type()
)
relay4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4State.setStatus("current")


class _Relay4Pulse_Type(Integer32):
    """Custom type relay4Pulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay4Pulse_Type.__name__ = "Integer32"
_Relay4Pulse_Object = MibScalar
relay4Pulse = _Relay4Pulse_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 4, 4, 2),
    _Relay4Pulse_Type()
)
relay4Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4Pulse.setStatus("current")


class _ConfigurationSaved_Type(Integer32):
    """Custom type configurationSaved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("saved", 1),
          ("unsaved", 0))
    )


_ConfigurationSaved_Type.__name__ = "Integer32"
_ConfigurationSaved_Object = MibScalar
configurationSaved = _ConfigurationSaved_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 5),
    _ConfigurationSaved_Type()
)
configurationSaved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationSaved.setStatus("current")


class _RestartDevice_Type(Integer32):
    """Custom type restartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 0),
          ("restart", 1))
    )


_RestartDevice_Type.__name__ = "Integer32"
_RestartDevice_Object = MibScalar
restartDevice = _RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 6),
    _RestartDevice_Type()
)
restartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartDevice.setStatus("current")


class _TemperatureUnit_Type(Integer32):
    """Custom type temperatureUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("celcius", 0),
          ("fahrenheit", 1))
    )


_TemperatureUnit_Type.__name__ = "Integer32"
_TemperatureUnit_Object = MibScalar
temperatureUnit = _TemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 7),
    _TemperatureUnit_Type()
)
temperatureUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureUnit.setStatus("current")


class _HardwareErr_Type(Integer32):
    """Custom type hardwareErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hwErr", 2),
          ("noErr", 0),
          ("owErr", 1))
    )


_HardwareErr_Type.__name__ = "Integer32"
_HardwareErr_Object = MibScalar
hardwareErr = _HardwareErr_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3, 8),
    _HardwareErr_Type()
)
hardwareErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareErr.setStatus("current")
_Tcw240bMIBConformance_ObjectIdentity = ObjectIdentity
tcw240bMIBConformance = _Tcw240bMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 4)
)
_Tcw240bMIBCompliances_ObjectIdentity = ObjectIdentity
tcw240bMIBCompliances = _Tcw240bMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 4, 1)
)
_Tcw240bMIBGroups_ObjectIdentity = ObjectIdentity
tcw240bMIBGroups = _Tcw240bMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1, 4, 2)
)

# Managed Objects groups

tcw240bProductGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 1, 4, 2, 1)
)
tcw240bProductGroup.setObjects(
      *(("TERACOM-MIB", "name"),
        ("TERACOM-MIB", "version"),
        ("TERACOM-MIB", "dateTime"))
)
if mibBuilder.loadTexts:
    tcw240bProductGroup.setStatus("current")

tcw240bSetupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 1, 4, 2, 2)
)
tcw240bSetupGroup.setObjects(
      *(("TERACOM-MIB", "deviceID"),
        ("TERACOM-MIB", "hostName"),
        ("TERACOM-MIB", "deviceIP"),
        ("TERACOM-MIB", "s1description"),
        ("TERACOM-MIB", "s11MAXx10Int"),
        ("TERACOM-MIB", "s11MINx10Int"),
        ("TERACOM-MIB", "s11HYSTx10Int"),
        ("TERACOM-MIB", "s12MAXx10Int"),
        ("TERACOM-MIB", "s12MINx10Int"),
        ("TERACOM-MIB", "s12HYSTx10Int"),
        ("TERACOM-MIB", "s2description"),
        ("TERACOM-MIB", "s21MAXx10Int"),
        ("TERACOM-MIB", "s21MINx10Int"),
        ("TERACOM-MIB", "s21HYSTx10Int"),
        ("TERACOM-MIB", "s22MAXx10Int"),
        ("TERACOM-MIB", "s22MINx10Int"),
        ("TERACOM-MIB", "s22HYSTx10Int"),
        ("TERACOM-MIB", "s3description"),
        ("TERACOM-MIB", "s31MAXx10Int"),
        ("TERACOM-MIB", "s31MINx10Int"),
        ("TERACOM-MIB", "s31HYSTx10Int"),
        ("TERACOM-MIB", "s32MAXx10Int"),
        ("TERACOM-MIB", "s32MINx10Int"),
        ("TERACOM-MIB", "s32HYSTx10Int"),
        ("TERACOM-MIB", "s4description"),
        ("TERACOM-MIB", "s41MAXx10Int"),
        ("TERACOM-MIB", "s41MINx10Int"),
        ("TERACOM-MIB", "s41HYSTx10Int"),
        ("TERACOM-MIB", "s42MAXx10Int"),
        ("TERACOM-MIB", "s42MINx10Int"),
        ("TERACOM-MIB", "s42HYSTx10Int"),
        ("TERACOM-MIB", "s5description"),
        ("TERACOM-MIB", "s51MAXx10Int"),
        ("TERACOM-MIB", "s51MINx10Int"),
        ("TERACOM-MIB", "s51HYSTx10Int"),
        ("TERACOM-MIB", "s52MAXx10Int"),
        ("TERACOM-MIB", "s52MINx10Int"),
        ("TERACOM-MIB", "s52HYSTx10Int"),
        ("TERACOM-MIB", "s6description"),
        ("TERACOM-MIB", "s61MAXx10Int"),
        ("TERACOM-MIB", "s61MINx10Int"),
        ("TERACOM-MIB", "s61HYSTx10Int"),
        ("TERACOM-MIB", "s62MAXx10Int"),
        ("TERACOM-MIB", "s62MINx10Int"),
        ("TERACOM-MIB", "s62HYSTx10Int"),
        ("TERACOM-MIB", "s7description"),
        ("TERACOM-MIB", "s71MAXx10Int"),
        ("TERACOM-MIB", "s71MINx10Int"),
        ("TERACOM-MIB", "s71HYSTx10Int"),
        ("TERACOM-MIB", "s72MAXx10Int"),
        ("TERACOM-MIB", "s72MINx10Int"),
        ("TERACOM-MIB", "s72HYSTx10Int"),
        ("TERACOM-MIB", "s8description"),
        ("TERACOM-MIB", "s81MAXx10Int"),
        ("TERACOM-MIB", "s81MINx10Int"),
        ("TERACOM-MIB", "s81HYSTx10Int"),
        ("TERACOM-MIB", "s82MAXx10Int"),
        ("TERACOM-MIB", "s82MINx10Int"),
        ("TERACOM-MIB", "s82HYSTx10Int"),
        ("TERACOM-MIB", "voltage1description"),
        ("TERACOM-MIB", "voltage1max"),
        ("TERACOM-MIB", "voltage1min"),
        ("TERACOM-MIB", "voltage1hyst"),
        ("TERACOM-MIB", "voltage2description"),
        ("TERACOM-MIB", "voltage2max"),
        ("TERACOM-MIB", "voltage2min"),
        ("TERACOM-MIB", "voltage2hyst"),
        ("TERACOM-MIB", "voltage3description"),
        ("TERACOM-MIB", "voltage3max"),
        ("TERACOM-MIB", "voltage3min"),
        ("TERACOM-MIB", "voltage3hyst"),
        ("TERACOM-MIB", "voltage4description"),
        ("TERACOM-MIB", "voltage4max"),
        ("TERACOM-MIB", "voltage4min"),
        ("TERACOM-MIB", "voltage4hyst"),
        ("TERACOM-MIB", "digitalInput1description"),
        ("TERACOM-MIB", "digitalInput2description"),
        ("TERACOM-MIB", "digitalInput3description"),
        ("TERACOM-MIB", "digitalInput4description"),
        ("TERACOM-MIB", "relay1description"),
        ("TERACOM-MIB", "relay1pulseWidth"),
        ("TERACOM-MIB", "relay1controlledBy"),
        ("TERACOM-MIB", "relay2description"),
        ("TERACOM-MIB", "relay2pulseWidth"),
        ("TERACOM-MIB", "relay2controlledBy"),
        ("TERACOM-MIB", "relay3description"),
        ("TERACOM-MIB", "relay3pulseWidth"),
        ("TERACOM-MIB", "relay3controlledBy"),
        ("TERACOM-MIB", "relay4description"),
        ("TERACOM-MIB", "relay4pulseWidth"),
        ("TERACOM-MIB", "relay4controlledBy"))
)
if mibBuilder.loadTexts:
    tcw240bSetupGroup.setStatus("current")

tcw240bMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 1, 4, 2, 3)
)
tcw240bMonitorGroup.setObjects(
      *(("TERACOM-MIB", "s11x10Int"),
        ("TERACOM-MIB", "s12x10Int"),
        ("TERACOM-MIB", "s1ID"),
        ("TERACOM-MIB", "s21x10Int"),
        ("TERACOM-MIB", "s22x10Int"),
        ("TERACOM-MIB", "s2ID"),
        ("TERACOM-MIB", "s31x10Int"),
        ("TERACOM-MIB", "s32x10Int"),
        ("TERACOM-MIB", "s3ID"),
        ("TERACOM-MIB", "s41x10Int"),
        ("TERACOM-MIB", "s42x10Int"),
        ("TERACOM-MIB", "s4ID"),
        ("TERACOM-MIB", "s51x10Int"),
        ("TERACOM-MIB", "s52x10Int"),
        ("TERACOM-MIB", "s5ID"),
        ("TERACOM-MIB", "s61x10Int"),
        ("TERACOM-MIB", "s62x10Int"),
        ("TERACOM-MIB", "s6ID"),
        ("TERACOM-MIB", "s71x10Int"),
        ("TERACOM-MIB", "s72x10Int"),
        ("TERACOM-MIB", "s7ID"),
        ("TERACOM-MIB", "s81x10Int"),
        ("TERACOM-MIB", "s82x10Int"),
        ("TERACOM-MIB", "s8ID"),
        ("TERACOM-MIB", "voltage1x10Int"),
        ("TERACOM-MIB", "voltage2x10Int"),
        ("TERACOM-MIB", "voltage3x10Int"),
        ("TERACOM-MIB", "voltage4x10Int"),
        ("TERACOM-MIB", "voltage1x100Int"),
        ("TERACOM-MIB", "voltage2x100Int"),
        ("TERACOM-MIB", "voltage3x100Int"),
        ("TERACOM-MIB", "voltage4x100Int"),
        ("TERACOM-MIB", "digitalInput1State"),
        ("TERACOM-MIB", "digitalInput2State"),
        ("TERACOM-MIB", "digitalInput3State"),
        ("TERACOM-MIB", "digitalInput4State"),
        ("TERACOM-MIB", "relay1State"),
        ("TERACOM-MIB", "relay1Pulse"),
        ("TERACOM-MIB", "relay2State"),
        ("TERACOM-MIB", "relay2Pulse"),
        ("TERACOM-MIB", "relay3State"),
        ("TERACOM-MIB", "relay3Pulse"),
        ("TERACOM-MIB", "relay4State"),
        ("TERACOM-MIB", "relay4Pulse"),
        ("TERACOM-MIB", "configurationSaved"),
        ("TERACOM-MIB", "restartDevice"),
        ("TERACOM-MIB", "temperatureUnit"),
        ("TERACOM-MIB", "hardwareErr"))
)
if mibBuilder.loadTexts:
    tcw240bMonitorGroup.setStatus("current")


# Notification objects

snmp_trap_notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 38783, 1, 0, 1)
)
snmp_trap_notification.setObjects(
      *(("TERACOM-MIB", "digitalInput1State"),
        ("TERACOM-MIB", "digitalInput2State"),
        ("TERACOM-MIB", "digitalInput3State"),
        ("TERACOM-MIB", "digitalInput4State"),
        ("TERACOM-MIB", "voltage1x10Int"),
        ("TERACOM-MIB", "voltage2x10Int"),
        ("TERACOM-MIB", "voltage3x10Int"),
        ("TERACOM-MIB", "voltage4x10Int"),
        ("TERACOM-MIB", "s11x10Int"),
        ("TERACOM-MIB", "s12x10Int"),
        ("TERACOM-MIB", "s21x10Int"),
        ("TERACOM-MIB", "s22x10Int"),
        ("TERACOM-MIB", "s31x10Int"),
        ("TERACOM-MIB", "s32x10Int"),
        ("TERACOM-MIB", "s41x10Int"),
        ("TERACOM-MIB", "s42x10Int"),
        ("TERACOM-MIB", "s51x10Int"),
        ("TERACOM-MIB", "s52x10Int"),
        ("TERACOM-MIB", "s61x10Int"),
        ("TERACOM-MIB", "s62x10Int"),
        ("TERACOM-MIB", "s71x10Int"),
        ("TERACOM-MIB", "s72x10Int"),
        ("TERACOM-MIB", "s81x10Int"),
        ("TERACOM-MIB", "s82x10Int"),
        ("TERACOM-MIB", "restartDevice"))
)
if mibBuilder.loadTexts:
    snmp_trap_notification.setStatus(
        "current"
    )


# Notifications groups

tcw240bTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 38783, 1, 4, 2, 4)
)
tcw240bTrapGroup.setObjects(
    ("TERACOM-MIB", "snmp_trap_notification")
)
if mibBuilder.loadTexts:
    tcw240bTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tcw240bMIBCompliances1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 38783, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tcw240bMIBCompliances1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERACOM-MIB",
    **{"CONTROLLED": CONTROLLED,
       "teracom": teracom,
       "tcw240b": tcw240b,
       "trapNotifications": trapNotifications,
       "snmp-trap-notification": snmp_trap_notification,
       "product": product,
       "name": name,
       "version": version,
       "dateTime": dateTime,
       "setup": setup,
       "network": network,
       "deviceID": deviceID,
       "hostName": hostName,
       "deviceIP": deviceIP,
       "io": io,
       "sensorsSetup": sensorsSetup,
       "sensor1setup": sensor1setup,
       "s1description": s1description,
       "sensor11setup": sensor11setup,
       "s11MAXx10Int": s11MAXx10Int,
       "s11MINx10Int": s11MINx10Int,
       "s11HYSTx10Int": s11HYSTx10Int,
       "sensor12setup": sensor12setup,
       "s12MAXx10Int": s12MAXx10Int,
       "s12MINx10Int": s12MINx10Int,
       "s12HYSTx10Int": s12HYSTx10Int,
       "sensor2setup": sensor2setup,
       "s2description": s2description,
       "sensor21setup": sensor21setup,
       "s21MAXx10Int": s21MAXx10Int,
       "s21MINx10Int": s21MINx10Int,
       "s21HYSTx10Int": s21HYSTx10Int,
       "sensor22setup": sensor22setup,
       "s22MAXx10Int": s22MAXx10Int,
       "s22MINx10Int": s22MINx10Int,
       "s22HYSTx10Int": s22HYSTx10Int,
       "sensor3setup": sensor3setup,
       "s3description": s3description,
       "sensor31setup": sensor31setup,
       "s31MAXx10Int": s31MAXx10Int,
       "s31MINx10Int": s31MINx10Int,
       "s31HYSTx10Int": s31HYSTx10Int,
       "sensor32setup": sensor32setup,
       "s32MAXx10Int": s32MAXx10Int,
       "s32MINx10Int": s32MINx10Int,
       "s32HYSTx10Int": s32HYSTx10Int,
       "sensor4setup": sensor4setup,
       "s4description": s4description,
       "sensor41setup": sensor41setup,
       "s41MAXx10Int": s41MAXx10Int,
       "s41MINx10Int": s41MINx10Int,
       "s41HYSTx10Int": s41HYSTx10Int,
       "sensor42setup": sensor42setup,
       "s42MAXx10Int": s42MAXx10Int,
       "s42MINx10Int": s42MINx10Int,
       "s42HYSTx10Int": s42HYSTx10Int,
       "sensor5setup": sensor5setup,
       "s5description": s5description,
       "sensor51setup": sensor51setup,
       "s51MAXx10Int": s51MAXx10Int,
       "s51MINx10Int": s51MINx10Int,
       "s51HYSTx10Int": s51HYSTx10Int,
       "sensor52setup": sensor52setup,
       "s52MAXx10Int": s52MAXx10Int,
       "s52MINx10Int": s52MINx10Int,
       "s52HYSTx10Int": s52HYSTx10Int,
       "sensor6setup": sensor6setup,
       "s6description": s6description,
       "sensor61setup": sensor61setup,
       "s61MAXx10Int": s61MAXx10Int,
       "s61MINx10Int": s61MINx10Int,
       "s61HYSTx10Int": s61HYSTx10Int,
       "sensor62setup": sensor62setup,
       "s62MAXx10Int": s62MAXx10Int,
       "s62MINx10Int": s62MINx10Int,
       "s62HYSTx10Int": s62HYSTx10Int,
       "sensor7setup": sensor7setup,
       "s7description": s7description,
       "sensor71setup": sensor71setup,
       "s71MAXx10Int": s71MAXx10Int,
       "s71MINx10Int": s71MINx10Int,
       "s71HYSTx10Int": s71HYSTx10Int,
       "sensor72setup": sensor72setup,
       "s72MAXx10Int": s72MAXx10Int,
       "s72MINx10Int": s72MINx10Int,
       "s72HYSTx10Int": s72HYSTx10Int,
       "sensor8setup": sensor8setup,
       "s8description": s8description,
       "sensor81setup": sensor81setup,
       "s81MAXx10Int": s81MAXx10Int,
       "s81MINx10Int": s81MINx10Int,
       "s81HYSTx10Int": s81HYSTx10Int,
       "sensor82setup": sensor82setup,
       "s82MAXx10Int": s82MAXx10Int,
       "s82MINx10Int": s82MINx10Int,
       "s82HYSTx10Int": s82HYSTx10Int,
       "analogSetup": analogSetup,
       "analog1setup": analog1setup,
       "voltage1description": voltage1description,
       "voltage1max": voltage1max,
       "voltage1min": voltage1min,
       "voltage1hyst": voltage1hyst,
       "analog2setup": analog2setup,
       "voltage2description": voltage2description,
       "voltage2max": voltage2max,
       "voltage2min": voltage2min,
       "voltage2hyst": voltage2hyst,
       "analog3setup": analog3setup,
       "voltage3description": voltage3description,
       "voltage3max": voltage3max,
       "voltage3min": voltage3min,
       "voltage3hyst": voltage3hyst,
       "analog4setup": analog4setup,
       "voltage4description": voltage4description,
       "voltage4max": voltage4max,
       "voltage4min": voltage4min,
       "voltage4hyst": voltage4hyst,
       "digitalSetup": digitalSetup,
       "digitalInput1description": digitalInput1description,
       "digitalInput2description": digitalInput2description,
       "digitalInput3description": digitalInput3description,
       "digitalInput4description": digitalInput4description,
       "relaysSetup": relaysSetup,
       "relay1setup": relay1setup,
       "relay1description": relay1description,
       "relay1pulseWidth": relay1pulseWidth,
       "relay1controlledBy": relay1controlledBy,
       "relay2setup": relay2setup,
       "relay2description": relay2description,
       "relay2pulseWidth": relay2pulseWidth,
       "relay2controlledBy": relay2controlledBy,
       "relay3setup": relay3setup,
       "relay3description": relay3description,
       "relay3pulseWidth": relay3pulseWidth,
       "relay3controlledBy": relay3controlledBy,
       "relay4setup": relay4setup,
       "relay4description": relay4description,
       "relay4pulseWidth": relay4pulseWidth,
       "relay4controlledBy": relay4controlledBy,
       "monitorNcontrol": monitorNcontrol,
       "sensors": sensors,
       "sensor1": sensor1,
       "s11x10Int": s11x10Int,
       "s12x10Int": s12x10Int,
       "s1ID": s1ID,
       "sensor2": sensor2,
       "s21x10Int": s21x10Int,
       "s22x10Int": s22x10Int,
       "s2ID": s2ID,
       "sensor3": sensor3,
       "s31x10Int": s31x10Int,
       "s32x10Int": s32x10Int,
       "s3ID": s3ID,
       "sensor4": sensor4,
       "s41x10Int": s41x10Int,
       "s42x10Int": s42x10Int,
       "s4ID": s4ID,
       "sensor5": sensor5,
       "s51x10Int": s51x10Int,
       "s52x10Int": s52x10Int,
       "s5ID": s5ID,
       "sensor6": sensor6,
       "s61x10Int": s61x10Int,
       "s62x10Int": s62x10Int,
       "s6ID": s6ID,
       "sensor7": sensor7,
       "s71x10Int": s71x10Int,
       "s72x10Int": s72x10Int,
       "s7ID": s7ID,
       "sensor8": sensor8,
       "s81x10Int": s81x10Int,
       "s82x10Int": s82x10Int,
       "s8ID": s8ID,
       "analog": analog,
       "voltage1x10Int": voltage1x10Int,
       "voltage2x10Int": voltage2x10Int,
       "voltage3x10Int": voltage3x10Int,
       "voltage4x10Int": voltage4x10Int,
       "voltage1x100Int": voltage1x100Int,
       "voltage2x100Int": voltage2x100Int,
       "voltage3x100Int": voltage3x100Int,
       "voltage4x100Int": voltage4x100Int,
       "digital": digital,
       "digitalInput1State": digitalInput1State,
       "digitalInput2State": digitalInput2State,
       "digitalInput3State": digitalInput3State,
       "digitalInput4State": digitalInput4State,
       "relays": relays,
       "relay1": relay1,
       "relay1State": relay1State,
       "relay1Pulse": relay1Pulse,
       "relay2": relay2,
       "relay2State": relay2State,
       "relay2Pulse": relay2Pulse,
       "relay3": relay3,
       "relay3State": relay3State,
       "relay3Pulse": relay3Pulse,
       "relay4": relay4,
       "relay4State": relay4State,
       "relay4Pulse": relay4Pulse,
       "configurationSaved": configurationSaved,
       "restartDevice": restartDevice,
       "temperatureUnit": temperatureUnit,
       "hardwareErr": hardwareErr,
       "tcw240bMIBConformance": tcw240bMIBConformance,
       "tcw240bMIBCompliances": tcw240bMIBCompliances,
       "tcw240bMIBCompliances1": tcw240bMIBCompliances1,
       "tcw240bMIBGroups": tcw240bMIBGroups,
       "tcw240bProductGroup": tcw240bProductGroup,
       "tcw240bSetupGroup": tcw240bSetupGroup,
       "tcw240bMonitorGroup": tcw240bMonitorGroup,
       "tcw240bTrapGroup": tcw240bTrapGroup,
       "snmpMIB": snmpMIB}
)
