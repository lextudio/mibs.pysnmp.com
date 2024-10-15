# SNMP MIB module (E7-Notifications-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/E7-Notifications-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:15 2024
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

(e7,
 e7Modules) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "e7",
    "e7Modules")

(E7AlarmType,
 E7EventType,
 E7ObjectClass,
 E7SecurityType,
 E7TcaType) = mibBuilder.importSymbols(
    "E7-TC",
    "E7AlarmType",
    "E7EventType",
    "E7ObjectClass",
    "E7SecurityType",
    "E7TcaType")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

e7NotificationModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_E7Notification_ObjectIdentity = ObjectIdentity
e7Notification = _E7Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4)
)
_E7NotificationObjects_ObjectIdentity = ObjectIdentity
e7NotificationObjects = _E7NotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1)
)
_E7TrapSequenceNo_Type = Integer32
_E7TrapSequenceNo_Object = MibScalar
e7TrapSequenceNo = _E7TrapSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 1),
    _E7TrapSequenceNo_Type()
)
e7TrapSequenceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSequenceNo.setStatus("current")
_E7TrapAlarmType_Type = E7AlarmType
_E7TrapAlarmType_Object = MibScalar
e7TrapAlarmType = _E7TrapAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 2),
    _E7TrapAlarmType_Type()
)
e7TrapAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapAlarmType.setStatus("current")


class _E7TrapAlarmStatus_Type(Integer32):
    """Custom type e7TrapAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_E7TrapAlarmStatus_Type.__name__ = "Integer32"
_E7TrapAlarmStatus_Object = MibScalar
e7TrapAlarmStatus = _E7TrapAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 3),
    _E7TrapAlarmStatus_Type()
)
e7TrapAlarmStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapAlarmStatus.setStatus("current")
_E7TrapObjectClass_Type = E7ObjectClass
_E7TrapObjectClass_Object = MibScalar
e7TrapObjectClass = _E7TrapObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 4),
    _E7TrapObjectClass_Type()
)
e7TrapObjectClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectClass.setStatus("current")
_E7TrapObjectInstance1_Type = Integer32
_E7TrapObjectInstance1_Object = MibScalar
e7TrapObjectInstance1 = _E7TrapObjectInstance1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 5),
    _E7TrapObjectInstance1_Type()
)
e7TrapObjectInstance1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectInstance1.setStatus("current")
_E7TrapObjectInstance2_Type = Integer32
_E7TrapObjectInstance2_Object = MibScalar
e7TrapObjectInstance2 = _E7TrapObjectInstance2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 6),
    _E7TrapObjectInstance2_Type()
)
e7TrapObjectInstance2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectInstance2.setStatus("current")
_E7TrapObjectInstance3_Type = Integer32
_E7TrapObjectInstance3_Object = MibScalar
e7TrapObjectInstance3 = _E7TrapObjectInstance3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 7),
    _E7TrapObjectInstance3_Type()
)
e7TrapObjectInstance3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectInstance3.setStatus("current")
_E7TrapObjectInstance4_Type = Integer32
_E7TrapObjectInstance4_Object = MibScalar
e7TrapObjectInstance4 = _E7TrapObjectInstance4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 8),
    _E7TrapObjectInstance4_Type()
)
e7TrapObjectInstance4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectInstance4.setStatus("current")
_E7TrapObjectInstance5_Type = Integer32
_E7TrapObjectInstance5_Object = MibScalar
e7TrapObjectInstance5 = _E7TrapObjectInstance5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 9),
    _E7TrapObjectInstance5_Type()
)
e7TrapObjectInstance5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectInstance5.setStatus("current")
_E7TrapObjectInstance6_Type = Integer32
_E7TrapObjectInstance6_Object = MibScalar
e7TrapObjectInstance6 = _E7TrapObjectInstance6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 10),
    _E7TrapObjectInstance6_Type()
)
e7TrapObjectInstance6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectInstance6.setStatus("current")
_E7TrapObjectInstance7_Type = Integer32
_E7TrapObjectInstance7_Object = MibScalar
e7TrapObjectInstance7 = _E7TrapObjectInstance7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 11),
    _E7TrapObjectInstance7_Type()
)
e7TrapObjectInstance7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectInstance7.setStatus("current")
_E7TrapObjectInstance8_Type = Integer32
_E7TrapObjectInstance8_Object = MibScalar
e7TrapObjectInstance8 = _E7TrapObjectInstance8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 12),
    _E7TrapObjectInstance8_Type()
)
e7TrapObjectInstance8.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectInstance8.setStatus("current")


class _E7TrapAlarmSeverityLevel_Type(Integer32):
    """Custom type e7TrapAlarmSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clear", 6),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("unknown", 5),
          ("warning", 4))
    )


_E7TrapAlarmSeverityLevel_Type.__name__ = "Integer32"
_E7TrapAlarmSeverityLevel_Object = MibScalar
e7TrapAlarmSeverityLevel = _E7TrapAlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 13),
    _E7TrapAlarmSeverityLevel_Type()
)
e7TrapAlarmSeverityLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapAlarmSeverityLevel.setStatus("current")


class _E7TrapTimeStamp_Type(OctetString):
    """Custom type e7TrapTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_E7TrapTimeStamp_Type.__name__ = "OctetString"
_E7TrapTimeStamp_Object = MibScalar
e7TrapTimeStamp = _E7TrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 14),
    _E7TrapTimeStamp_Type()
)
e7TrapTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapTimeStamp.setStatus("current")


class _E7TrapServiceAffecting_Type(Integer32):
    """Custom type e7TrapServiceAffecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_E7TrapServiceAffecting_Type.__name__ = "Integer32"
_E7TrapServiceAffecting_Object = MibScalar
e7TrapServiceAffecting = _E7TrapServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 15),
    _E7TrapServiceAffecting_Type()
)
e7TrapServiceAffecting.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapServiceAffecting.setStatus("current")


class _E7TrapAlarmLocationInfo_Type(Integer32):
    """Custom type e7TrapAlarmLocationInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("nearEnd", 1)
    )


_E7TrapAlarmLocationInfo_Type.__name__ = "Integer32"
_E7TrapAlarmLocationInfo_Object = MibScalar
e7TrapAlarmLocationInfo = _E7TrapAlarmLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 16),
    _E7TrapAlarmLocationInfo_Type()
)
e7TrapAlarmLocationInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapAlarmLocationInfo.setStatus("current")
_E7TrapText_Type = OctetString
_E7TrapText_Object = MibScalar
e7TrapText = _E7TrapText_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 17),
    _E7TrapText_Type()
)
e7TrapText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapText.setStatus("current")
_E7TrapEventType_Type = E7EventType
_E7TrapEventType_Object = MibScalar
e7TrapEventType = _E7TrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 18),
    _E7TrapEventType_Type()
)
e7TrapEventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapEventType.setStatus("current")


class _E7TrapDbChangeType_Type(Integer32):
    """Custom type e7TrapDbChangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 4),
          ("modify", 3))
    )


_E7TrapDbChangeType_Type.__name__ = "Integer32"
_E7TrapDbChangeType_Object = MibScalar
e7TrapDbChangeType = _E7TrapDbChangeType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 19),
    _E7TrapDbChangeType_Type()
)
e7TrapDbChangeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapDbChangeType.setStatus("current")
_E7TrapSessionNumber_Type = Integer32
_E7TrapSessionNumber_Object = MibScalar
e7TrapSessionNumber = _E7TrapSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 20),
    _E7TrapSessionNumber_Type()
)
e7TrapSessionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSessionNumber.setStatus("current")
_E7TrapUserName_Type = OctetString
_E7TrapUserName_Object = MibScalar
e7TrapUserName = _E7TrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 21),
    _E7TrapUserName_Type()
)
e7TrapUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapUserName.setStatus("current")
_E7TrapIpAddr_Type = IpAddress
_E7TrapIpAddr_Object = MibScalar
e7TrapIpAddr = _E7TrapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 22),
    _E7TrapIpAddr_Type()
)
e7TrapIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapIpAddr.setStatus("current")
_E7TrapSecurityType_Type = E7SecurityType
_E7TrapSecurityType_Object = MibScalar
e7TrapSecurityType = _E7TrapSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 23),
    _E7TrapSecurityType_Type()
)
e7TrapSecurityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecurityType.setStatus("current")


class _E7TrapMgmtIfType_Type(Integer32):
    """Custom type e7TrapMgmtIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cli", 3),
          ("debug", 1),
          ("netconf", 5),
          ("snmp", 4),
          ("system", 2))
    )


_E7TrapMgmtIfType_Type.__name__ = "Integer32"
_E7TrapMgmtIfType_Object = MibScalar
e7TrapMgmtIfType = _E7TrapMgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 24),
    _E7TrapMgmtIfType_Type()
)
e7TrapMgmtIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapMgmtIfType.setStatus("current")
_E7TrapTcaType_Type = E7TcaType
_E7TrapTcaType_Object = MibScalar
e7TrapTcaType = _E7TrapTcaType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 25),
    _E7TrapTcaType_Type()
)
e7TrapTcaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapTcaType.setStatus("current")


class _E7TrapTcaBinType_Type(Integer32):
    """Custom type e7TrapTcaBinType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("day1", 2),
          ("min15", 1),
          ("total", 3))
    )


_E7TrapTcaBinType_Type.__name__ = "Integer32"
_E7TrapTcaBinType_Object = MibScalar
e7TrapTcaBinType = _E7TrapTcaBinType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 26),
    _E7TrapTcaBinType_Type()
)
e7TrapTcaBinType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapTcaBinType.setStatus("current")
_E7TrapTime_Type = Integer32
_E7TrapTime_Object = MibScalar
e7TrapTime = _E7TrapTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 27),
    _E7TrapTime_Type()
)
e7TrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapTime.setStatus("current")


class _E7TrapTcaValueType_Type(Integer32):
    """Custom type e7TrapTcaValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ceiling", 3),
          ("count", 1),
          ("floor", 2))
    )


_E7TrapTcaValueType_Type.__name__ = "Integer32"
_E7TrapTcaValueType_Object = MibScalar
e7TrapTcaValueType = _E7TrapTcaValueType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 28),
    _E7TrapTcaValueType_Type()
)
e7TrapTcaValueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapTcaValueType.setStatus("current")
_E7TrapCliObject_Type = OctetString
_E7TrapCliObject_Object = MibScalar
e7TrapCliObject = _E7TrapCliObject_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 29),
    _E7TrapCliObject_Type()
)
e7TrapCliObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapCliObject.setStatus("current")
_E7TrapRepeatCount_Type = Integer32
_E7TrapRepeatCount_Object = MibScalar
e7TrapRepeatCount = _E7TrapRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 30),
    _E7TrapRepeatCount_Type()
)
e7TrapRepeatCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapRepeatCount.setStatus("current")
_E7TrapSecObjectClass_Type = E7ObjectClass
_E7TrapSecObjectClass_Object = MibScalar
e7TrapSecObjectClass = _E7TrapSecObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 31),
    _E7TrapSecObjectClass_Type()
)
e7TrapSecObjectClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectClass.setStatus("current")
_E7TrapSecObjectInstance1_Type = Integer32
_E7TrapSecObjectInstance1_Object = MibScalar
e7TrapSecObjectInstance1 = _E7TrapSecObjectInstance1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 32),
    _E7TrapSecObjectInstance1_Type()
)
e7TrapSecObjectInstance1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectInstance1.setStatus("current")
_E7TrapSecObjectInstance2_Type = Integer32
_E7TrapSecObjectInstance2_Object = MibScalar
e7TrapSecObjectInstance2 = _E7TrapSecObjectInstance2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 33),
    _E7TrapSecObjectInstance2_Type()
)
e7TrapSecObjectInstance2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectInstance2.setStatus("current")
_E7TrapSecObjectInstance3_Type = Integer32
_E7TrapSecObjectInstance3_Object = MibScalar
e7TrapSecObjectInstance3 = _E7TrapSecObjectInstance3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 34),
    _E7TrapSecObjectInstance3_Type()
)
e7TrapSecObjectInstance3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectInstance3.setStatus("current")
_E7TrapSecObjectInstance4_Type = Integer32
_E7TrapSecObjectInstance4_Object = MibScalar
e7TrapSecObjectInstance4 = _E7TrapSecObjectInstance4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 35),
    _E7TrapSecObjectInstance4_Type()
)
e7TrapSecObjectInstance4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectInstance4.setStatus("current")
_E7TrapSecObjectInstance5_Type = Integer32
_E7TrapSecObjectInstance5_Object = MibScalar
e7TrapSecObjectInstance5 = _E7TrapSecObjectInstance5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 36),
    _E7TrapSecObjectInstance5_Type()
)
e7TrapSecObjectInstance5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectInstance5.setStatus("current")
_E7TrapSecObjectInstance6_Type = Integer32
_E7TrapSecObjectInstance6_Object = MibScalar
e7TrapSecObjectInstance6 = _E7TrapSecObjectInstance6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 37),
    _E7TrapSecObjectInstance6_Type()
)
e7TrapSecObjectInstance6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectInstance6.setStatus("current")
_E7TrapSecObjectInstance7_Type = Integer32
_E7TrapSecObjectInstance7_Object = MibScalar
e7TrapSecObjectInstance7 = _E7TrapSecObjectInstance7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 38),
    _E7TrapSecObjectInstance7_Type()
)
e7TrapSecObjectInstance7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectInstance7.setStatus("current")
_E7TrapSecObjectInstance8_Type = Integer32
_E7TrapSecObjectInstance8_Object = MibScalar
e7TrapSecObjectInstance8 = _E7TrapSecObjectInstance8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 39),
    _E7TrapSecObjectInstance8_Type()
)
e7TrapSecObjectInstance8.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectInstance8.setStatus("current")
_E7TrapObjectLabel1_Type = OctetString
_E7TrapObjectLabel1_Object = MibScalar
e7TrapObjectLabel1 = _E7TrapObjectLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 40),
    _E7TrapObjectLabel1_Type()
)
e7TrapObjectLabel1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectLabel1.setStatus("current")
_E7TrapObjectLabel2_Type = OctetString
_E7TrapObjectLabel2_Object = MibScalar
e7TrapObjectLabel2 = _E7TrapObjectLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 41),
    _E7TrapObjectLabel2_Type()
)
e7TrapObjectLabel2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapObjectLabel2.setStatus("current")
_E7TrapSecObjectLabel1_Type = OctetString
_E7TrapSecObjectLabel1_Object = MibScalar
e7TrapSecObjectLabel1 = _E7TrapSecObjectLabel1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 42),
    _E7TrapSecObjectLabel1_Type()
)
e7TrapSecObjectLabel1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectLabel1.setStatus("current")
_E7TrapSecObjectLabel2_Type = OctetString
_E7TrapSecObjectLabel2_Object = MibScalar
e7TrapSecObjectLabel2 = _E7TrapSecObjectLabel2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 1, 43),
    _E7TrapSecObjectLabel2_Type()
)
e7TrapSecObjectLabel2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7TrapSecObjectLabel2.setStatus("current")
_E7Notifications_ObjectIdentity = ObjectIdentity
e7Notifications = _E7Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 2)
)

# Managed Objects groups


# Notification objects

e7TrapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 2, 1)
)
e7TrapAlarm.setObjects(
      *(("E7-Notifications-MIB", "e7TrapSequenceNo"),
        ("E7-Notifications-MIB", "e7TrapAlarmType"),
        ("E7-Notifications-MIB", "e7TrapAlarmStatus"),
        ("E7-Notifications-MIB", "e7TrapObjectClass"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance1"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance2"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance3"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance4"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance5"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance6"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance7"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance8"),
        ("E7-Notifications-MIB", "e7TrapCliObject"),
        ("E7-Notifications-MIB", "e7TrapAlarmSeverityLevel"),
        ("E7-Notifications-MIB", "e7TrapTimeStamp"),
        ("E7-Notifications-MIB", "e7TrapTime"),
        ("E7-Notifications-MIB", "e7TrapServiceAffecting"),
        ("E7-Notifications-MIB", "e7TrapAlarmLocationInfo"),
        ("E7-Notifications-MIB", "e7TrapText"),
        ("E7-Notifications-MIB", "e7TrapSecObjectClass"),
        ("E7-Notifications-MIB", "e7TrapSecObjectInstance1"),
        ("E7-Notifications-MIB", "e7TrapSecObjectInstance2"),
        ("E7-Notifications-MIB", "e7TrapSecObjectInstance3"),
        ("E7-Notifications-MIB", "e7TrapSecObjectInstance4"),
        ("E7-Notifications-MIB", "e7TrapSecObjectInstance5"),
        ("E7-Notifications-MIB", "e7TrapSecObjectInstance6"),
        ("E7-Notifications-MIB", "e7TrapSecObjectInstance7"),
        ("E7-Notifications-MIB", "e7TrapSecObjectInstance8"),
        ("E7-Notifications-MIB", "e7TrapObjectLabel1"),
        ("E7-Notifications-MIB", "e7TrapObjectLabel2"),
        ("E7-Notifications-MIB", "e7TrapSecObjectLabel1"),
        ("E7-Notifications-MIB", "e7TrapSecObjectLabel2"))
)
if mibBuilder.loadTexts:
    e7TrapAlarm.setStatus(
        "current"
    )

e7TrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 2, 2)
)
e7TrapEvent.setObjects(
      *(("E7-Notifications-MIB", "e7TrapSequenceNo"),
        ("E7-Notifications-MIB", "e7TrapEventType"),
        ("E7-Notifications-MIB", "e7TrapObjectClass"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance1"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance2"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance3"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance4"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance5"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance6"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance7"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance8"),
        ("E7-Notifications-MIB", "e7TrapCliObject"),
        ("E7-Notifications-MIB", "e7TrapTimeStamp"),
        ("E7-Notifications-MIB", "e7TrapTime"),
        ("E7-Notifications-MIB", "e7TrapText"),
        ("E7-Notifications-MIB", "e7TrapRepeatCount"),
        ("E7-Notifications-MIB", "e7TrapObjectLabel1"),
        ("E7-Notifications-MIB", "e7TrapObjectLabel2"))
)
if mibBuilder.loadTexts:
    e7TrapEvent.setStatus(
        "current"
    )

e7TrapDbChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 2, 3)
)
e7TrapDbChange.setObjects(
      *(("E7-Notifications-MIB", "e7TrapSequenceNo"),
        ("E7-Notifications-MIB", "e7TrapDbChangeType"),
        ("E7-Notifications-MIB", "e7TrapObjectClass"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance1"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance2"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance3"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance4"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance5"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance6"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance7"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance8"),
        ("E7-Notifications-MIB", "e7TrapCliObject"),
        ("E7-Notifications-MIB", "e7TrapMgmtIfType"),
        ("E7-Notifications-MIB", "e7TrapSessionNumber"),
        ("E7-Notifications-MIB", "e7TrapUserName"),
        ("E7-Notifications-MIB", "e7TrapIpAddr"),
        ("E7-Notifications-MIB", "e7TrapTimeStamp"),
        ("E7-Notifications-MIB", "e7TrapTime"),
        ("E7-Notifications-MIB", "e7TrapText"),
        ("E7-Notifications-MIB", "e7TrapObjectLabel1"),
        ("E7-Notifications-MIB", "e7TrapObjectLabel2"))
)
if mibBuilder.loadTexts:
    e7TrapDbChange.setStatus(
        "current"
    )

e7TrapSecurity = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 2, 4)
)
e7TrapSecurity.setObjects(
      *(("E7-Notifications-MIB", "e7TrapSequenceNo"),
        ("E7-Notifications-MIB", "e7TrapSecurityType"),
        ("E7-Notifications-MIB", "e7TrapMgmtIfType"),
        ("E7-Notifications-MIB", "e7TrapSessionNumber"),
        ("E7-Notifications-MIB", "e7TrapUserName"),
        ("E7-Notifications-MIB", "e7TrapIpAddr"),
        ("E7-Notifications-MIB", "e7TrapTimeStamp"),
        ("E7-Notifications-MIB", "e7TrapTime"),
        ("E7-Notifications-MIB", "e7TrapText"))
)
if mibBuilder.loadTexts:
    e7TrapSecurity.setStatus(
        "current"
    )

e7TrapTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 4, 2, 5)
)
e7TrapTca.setObjects(
      *(("E7-Notifications-MIB", "e7TrapSequenceNo"),
        ("E7-Notifications-MIB", "e7TrapTcaType"),
        ("E7-Notifications-MIB", "e7TrapTcaBinType"),
        ("E7-Notifications-MIB", "e7TrapTcaValueType"),
        ("E7-Notifications-MIB", "e7TrapObjectClass"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance1"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance2"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance3"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance4"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance5"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance6"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance7"),
        ("E7-Notifications-MIB", "e7TrapObjectInstance8"),
        ("E7-Notifications-MIB", "e7TrapCliObject"),
        ("E7-Notifications-MIB", "e7TrapTimeStamp"),
        ("E7-Notifications-MIB", "e7TrapTime"),
        ("E7-Notifications-MIB", "e7TrapText"),
        ("E7-Notifications-MIB", "e7TrapObjectLabel1"),
        ("E7-Notifications-MIB", "e7TrapObjectLabel2"))
)
if mibBuilder.loadTexts:
    e7TrapTca.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E7-Notifications-MIB",
    **{"e7NotificationModule": e7NotificationModule,
       "e7Notification": e7Notification,
       "e7NotificationObjects": e7NotificationObjects,
       "e7TrapSequenceNo": e7TrapSequenceNo,
       "e7TrapAlarmType": e7TrapAlarmType,
       "e7TrapAlarmStatus": e7TrapAlarmStatus,
       "e7TrapObjectClass": e7TrapObjectClass,
       "e7TrapObjectInstance1": e7TrapObjectInstance1,
       "e7TrapObjectInstance2": e7TrapObjectInstance2,
       "e7TrapObjectInstance3": e7TrapObjectInstance3,
       "e7TrapObjectInstance4": e7TrapObjectInstance4,
       "e7TrapObjectInstance5": e7TrapObjectInstance5,
       "e7TrapObjectInstance6": e7TrapObjectInstance6,
       "e7TrapObjectInstance7": e7TrapObjectInstance7,
       "e7TrapObjectInstance8": e7TrapObjectInstance8,
       "e7TrapAlarmSeverityLevel": e7TrapAlarmSeverityLevel,
       "e7TrapTimeStamp": e7TrapTimeStamp,
       "e7TrapServiceAffecting": e7TrapServiceAffecting,
       "e7TrapAlarmLocationInfo": e7TrapAlarmLocationInfo,
       "e7TrapText": e7TrapText,
       "e7TrapEventType": e7TrapEventType,
       "e7TrapDbChangeType": e7TrapDbChangeType,
       "e7TrapSessionNumber": e7TrapSessionNumber,
       "e7TrapUserName": e7TrapUserName,
       "e7TrapIpAddr": e7TrapIpAddr,
       "e7TrapSecurityType": e7TrapSecurityType,
       "e7TrapMgmtIfType": e7TrapMgmtIfType,
       "e7TrapTcaType": e7TrapTcaType,
       "e7TrapTcaBinType": e7TrapTcaBinType,
       "e7TrapTime": e7TrapTime,
       "e7TrapTcaValueType": e7TrapTcaValueType,
       "e7TrapCliObject": e7TrapCliObject,
       "e7TrapRepeatCount": e7TrapRepeatCount,
       "e7TrapSecObjectClass": e7TrapSecObjectClass,
       "e7TrapSecObjectInstance1": e7TrapSecObjectInstance1,
       "e7TrapSecObjectInstance2": e7TrapSecObjectInstance2,
       "e7TrapSecObjectInstance3": e7TrapSecObjectInstance3,
       "e7TrapSecObjectInstance4": e7TrapSecObjectInstance4,
       "e7TrapSecObjectInstance5": e7TrapSecObjectInstance5,
       "e7TrapSecObjectInstance6": e7TrapSecObjectInstance6,
       "e7TrapSecObjectInstance7": e7TrapSecObjectInstance7,
       "e7TrapSecObjectInstance8": e7TrapSecObjectInstance8,
       "e7TrapObjectLabel1": e7TrapObjectLabel1,
       "e7TrapObjectLabel2": e7TrapObjectLabel2,
       "e7TrapSecObjectLabel1": e7TrapSecObjectLabel1,
       "e7TrapSecObjectLabel2": e7TrapSecObjectLabel2,
       "e7Notifications": e7Notifications,
       "e7TrapAlarm": e7TrapAlarm,
       "e7TrapEvent": e7TrapEvent,
       "e7TrapDbChange": e7TrapDbChange,
       "e7TrapSecurity": e7TrapSecurity,
       "e7TrapTca": e7TrapTca}
)
