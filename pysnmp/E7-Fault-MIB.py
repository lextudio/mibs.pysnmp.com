# SNMP MIB module (E7-Fault-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/E7-Fault-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:14 2024
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
 E7ObjectClass) = mibBuilder.importSymbols(
    "E7-TC",
    "E7AlarmType",
    "E7ObjectClass")

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

e7FaultModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_E7Fault_ObjectIdentity = ObjectIdentity
e7Fault = _E7Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3)
)
_E7Alarms_ObjectIdentity = ObjectIdentity
e7Alarms = _E7Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1)
)
_E7AlarmTable_Object = MibTable
e7AlarmTable = _E7AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    e7AlarmTable.setStatus("current")
_E7AlarmEntry_Object = MibTableRow
e7AlarmEntry = _E7AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1)
)
e7AlarmEntry.setIndexNames(
    (0, "E7-Fault-MIB", "e7AlarmObjectClass"),
    (0, "E7-Fault-MIB", "e7AlarmObjectInstance1"),
    (0, "E7-Fault-MIB", "e7AlarmObjectInstance2"),
    (0, "E7-Fault-MIB", "e7AlarmObjectInstance3"),
    (0, "E7-Fault-MIB", "e7AlarmObjectInstance4"),
    (0, "E7-Fault-MIB", "e7AlarmObjectInstance5"),
    (0, "E7-Fault-MIB", "e7AlarmObjectInstance6"),
    (0, "E7-Fault-MIB", "e7AlarmObjectInstance7"),
    (0, "E7-Fault-MIB", "e7AlarmObjectInstance8"),
    (0, "E7-Fault-MIB", "e7AlarmType"),
)
if mibBuilder.loadTexts:
    e7AlarmEntry.setStatus("current")
_E7AlarmObjectClass_Type = E7ObjectClass
_E7AlarmObjectClass_Object = MibTableColumn
e7AlarmObjectClass = _E7AlarmObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 1),
    _E7AlarmObjectClass_Type()
)
e7AlarmObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmObjectClass.setStatus("current")
_E7AlarmObjectInstance1_Type = Integer32
_E7AlarmObjectInstance1_Object = MibTableColumn
e7AlarmObjectInstance1 = _E7AlarmObjectInstance1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 2),
    _E7AlarmObjectInstance1_Type()
)
e7AlarmObjectInstance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmObjectInstance1.setStatus("current")
_E7AlarmObjectInstance2_Type = Integer32
_E7AlarmObjectInstance2_Object = MibTableColumn
e7AlarmObjectInstance2 = _E7AlarmObjectInstance2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 3),
    _E7AlarmObjectInstance2_Type()
)
e7AlarmObjectInstance2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmObjectInstance2.setStatus("current")
_E7AlarmObjectInstance3_Type = Integer32
_E7AlarmObjectInstance3_Object = MibTableColumn
e7AlarmObjectInstance3 = _E7AlarmObjectInstance3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 4),
    _E7AlarmObjectInstance3_Type()
)
e7AlarmObjectInstance3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmObjectInstance3.setStatus("current")
_E7AlarmObjectInstance4_Type = Integer32
_E7AlarmObjectInstance4_Object = MibTableColumn
e7AlarmObjectInstance4 = _E7AlarmObjectInstance4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 5),
    _E7AlarmObjectInstance4_Type()
)
e7AlarmObjectInstance4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmObjectInstance4.setStatus("current")
_E7AlarmObjectInstance5_Type = Integer32
_E7AlarmObjectInstance5_Object = MibTableColumn
e7AlarmObjectInstance5 = _E7AlarmObjectInstance5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 6),
    _E7AlarmObjectInstance5_Type()
)
e7AlarmObjectInstance5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmObjectInstance5.setStatus("current")
_E7AlarmObjectInstance6_Type = Integer32
_E7AlarmObjectInstance6_Object = MibTableColumn
e7AlarmObjectInstance6 = _E7AlarmObjectInstance6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 7),
    _E7AlarmObjectInstance6_Type()
)
e7AlarmObjectInstance6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmObjectInstance6.setStatus("current")
_E7AlarmObjectInstance7_Type = Integer32
_E7AlarmObjectInstance7_Object = MibTableColumn
e7AlarmObjectInstance7 = _E7AlarmObjectInstance7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 8),
    _E7AlarmObjectInstance7_Type()
)
e7AlarmObjectInstance7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmObjectInstance7.setStatus("current")
_E7AlarmObjectInstance8_Type = Integer32
_E7AlarmObjectInstance8_Object = MibTableColumn
e7AlarmObjectInstance8 = _E7AlarmObjectInstance8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 9),
    _E7AlarmObjectInstance8_Type()
)
e7AlarmObjectInstance8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmObjectInstance8.setStatus("current")
_E7AlarmType_Type = E7AlarmType
_E7AlarmType_Object = MibTableColumn
e7AlarmType = _E7AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 10),
    _E7AlarmType_Type()
)
e7AlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmType.setStatus("current")


class _E7AlarmSeverity_Type(Integer32):
    """Custom type e7AlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("unknown", 5),
          ("warning", 4))
    )


_E7AlarmSeverity_Type.__name__ = "Integer32"
_E7AlarmSeverity_Object = MibTableColumn
e7AlarmSeverity = _E7AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 11),
    _E7AlarmSeverity_Type()
)
e7AlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSeverity.setStatus("current")


class _E7AlarmTimeStamp_Type(OctetString):
    """Custom type e7AlarmTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_E7AlarmTimeStamp_Type.__name__ = "OctetString"
_E7AlarmTimeStamp_Object = MibTableColumn
e7AlarmTimeStamp = _E7AlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 12),
    _E7AlarmTimeStamp_Type()
)
e7AlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmTimeStamp.setStatus("current")


class _E7AlarmServiceAffecting_Type(Integer32):
    """Custom type e7AlarmServiceAffecting based on Integer32"""
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


_E7AlarmServiceAffecting_Type.__name__ = "Integer32"
_E7AlarmServiceAffecting_Object = MibTableColumn
e7AlarmServiceAffecting = _E7AlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 13),
    _E7AlarmServiceAffecting_Type()
)
e7AlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmServiceAffecting.setStatus("current")


class _E7AlarmLocationInfo_Type(Integer32):
    """Custom type e7AlarmLocationInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("nearEnd", 1)
    )


_E7AlarmLocationInfo_Type.__name__ = "Integer32"
_E7AlarmLocationInfo_Object = MibTableColumn
e7AlarmLocationInfo = _E7AlarmLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 14),
    _E7AlarmLocationInfo_Type()
)
e7AlarmLocationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmLocationInfo.setStatus("current")
_E7AlarmText_Type = OctetString
_E7AlarmText_Object = MibTableColumn
e7AlarmText = _E7AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 15),
    _E7AlarmText_Type()
)
e7AlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmText.setStatus("current")
_E7AlarmTime_Type = Integer32
_E7AlarmTime_Object = MibTableColumn
e7AlarmTime = _E7AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 16),
    _E7AlarmTime_Type()
)
e7AlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmTime.setStatus("current")
_E7AlarmCliObject_Type = OctetString
_E7AlarmCliObject_Object = MibTableColumn
e7AlarmCliObject = _E7AlarmCliObject_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 17),
    _E7AlarmCliObject_Type()
)
e7AlarmCliObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmCliObject.setStatus("current")
_E7AlarmSecObjectClass_Type = E7ObjectClass
_E7AlarmSecObjectClass_Object = MibTableColumn
e7AlarmSecObjectClass = _E7AlarmSecObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 18),
    _E7AlarmSecObjectClass_Type()
)
e7AlarmSecObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSecObjectClass.setStatus("current")
_E7AlarmSecObjectInstance1_Type = Integer32
_E7AlarmSecObjectInstance1_Object = MibTableColumn
e7AlarmSecObjectInstance1 = _E7AlarmSecObjectInstance1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 19),
    _E7AlarmSecObjectInstance1_Type()
)
e7AlarmSecObjectInstance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSecObjectInstance1.setStatus("current")
_E7AlarmSecObjectInstance2_Type = Integer32
_E7AlarmSecObjectInstance2_Object = MibTableColumn
e7AlarmSecObjectInstance2 = _E7AlarmSecObjectInstance2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 20),
    _E7AlarmSecObjectInstance2_Type()
)
e7AlarmSecObjectInstance2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSecObjectInstance2.setStatus("current")
_E7AlarmSecObjectInstance3_Type = Integer32
_E7AlarmSecObjectInstance3_Object = MibTableColumn
e7AlarmSecObjectInstance3 = _E7AlarmSecObjectInstance3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 21),
    _E7AlarmSecObjectInstance3_Type()
)
e7AlarmSecObjectInstance3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSecObjectInstance3.setStatus("current")
_E7AlarmSecObjectInstance4_Type = Integer32
_E7AlarmSecObjectInstance4_Object = MibTableColumn
e7AlarmSecObjectInstance4 = _E7AlarmSecObjectInstance4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 22),
    _E7AlarmSecObjectInstance4_Type()
)
e7AlarmSecObjectInstance4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSecObjectInstance4.setStatus("current")
_E7AlarmSecObjectInstance5_Type = Integer32
_E7AlarmSecObjectInstance5_Object = MibTableColumn
e7AlarmSecObjectInstance5 = _E7AlarmSecObjectInstance5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 23),
    _E7AlarmSecObjectInstance5_Type()
)
e7AlarmSecObjectInstance5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSecObjectInstance5.setStatus("current")
_E7AlarmSecObjectInstance6_Type = Integer32
_E7AlarmSecObjectInstance6_Object = MibTableColumn
e7AlarmSecObjectInstance6 = _E7AlarmSecObjectInstance6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 24),
    _E7AlarmSecObjectInstance6_Type()
)
e7AlarmSecObjectInstance6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSecObjectInstance6.setStatus("current")
_E7AlarmSecObjectInstance7_Type = Integer32
_E7AlarmSecObjectInstance7_Object = MibTableColumn
e7AlarmSecObjectInstance7 = _E7AlarmSecObjectInstance7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 25),
    _E7AlarmSecObjectInstance7_Type()
)
e7AlarmSecObjectInstance7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSecObjectInstance7.setStatus("current")
_E7AlarmSecObjectInstance8_Type = Integer32
_E7AlarmSecObjectInstance8_Object = MibTableColumn
e7AlarmSecObjectInstance8 = _E7AlarmSecObjectInstance8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 1, 1, 26),
    _E7AlarmSecObjectInstance8_Type()
)
e7AlarmSecObjectInstance8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmSecObjectInstance8.setStatus("current")
_E7AlarmTableEnd_Type = Integer32
_E7AlarmTableEnd_Object = MibScalar
e7AlarmTableEnd = _E7AlarmTableEnd_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 1, 2),
    _E7AlarmTableEnd_Type()
)
e7AlarmTableEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmTableEnd.setStatus("current")
_E7AlarmCount_ObjectIdentity = ObjectIdentity
e7AlarmCount = _E7AlarmCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 2)
)
_E7AlarmCountCritical_Type = Integer32
_E7AlarmCountCritical_Object = MibScalar
e7AlarmCountCritical = _E7AlarmCountCritical_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 2, 1),
    _E7AlarmCountCritical_Type()
)
e7AlarmCountCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmCountCritical.setStatus("current")
_E7AlarmCountMajor_Type = Integer32
_E7AlarmCountMajor_Object = MibScalar
e7AlarmCountMajor = _E7AlarmCountMajor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 2, 2),
    _E7AlarmCountMajor_Type()
)
e7AlarmCountMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmCountMajor.setStatus("current")
_E7AlarmCountMinor_Type = Integer32
_E7AlarmCountMinor_Object = MibScalar
e7AlarmCountMinor = _E7AlarmCountMinor_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 2, 3),
    _E7AlarmCountMinor_Type()
)
e7AlarmCountMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmCountMinor.setStatus("current")
_E7AlarmCountWarning_Type = Integer32
_E7AlarmCountWarning_Object = MibScalar
e7AlarmCountWarning = _E7AlarmCountWarning_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 2, 4),
    _E7AlarmCountWarning_Type()
)
e7AlarmCountWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmCountWarning.setStatus("current")
_E7AlarmCountInfo_Type = Integer32
_E7AlarmCountInfo_Object = MibScalar
e7AlarmCountInfo = _E7AlarmCountInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 3, 2, 5),
    _E7AlarmCountInfo_Type()
)
e7AlarmCountInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7AlarmCountInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E7-Fault-MIB",
    **{"e7FaultModule": e7FaultModule,
       "e7Fault": e7Fault,
       "e7Alarms": e7Alarms,
       "e7AlarmTable": e7AlarmTable,
       "e7AlarmEntry": e7AlarmEntry,
       "e7AlarmObjectClass": e7AlarmObjectClass,
       "e7AlarmObjectInstance1": e7AlarmObjectInstance1,
       "e7AlarmObjectInstance2": e7AlarmObjectInstance2,
       "e7AlarmObjectInstance3": e7AlarmObjectInstance3,
       "e7AlarmObjectInstance4": e7AlarmObjectInstance4,
       "e7AlarmObjectInstance5": e7AlarmObjectInstance5,
       "e7AlarmObjectInstance6": e7AlarmObjectInstance6,
       "e7AlarmObjectInstance7": e7AlarmObjectInstance7,
       "e7AlarmObjectInstance8": e7AlarmObjectInstance8,
       "e7AlarmType": e7AlarmType,
       "e7AlarmSeverity": e7AlarmSeverity,
       "e7AlarmTimeStamp": e7AlarmTimeStamp,
       "e7AlarmServiceAffecting": e7AlarmServiceAffecting,
       "e7AlarmLocationInfo": e7AlarmLocationInfo,
       "e7AlarmText": e7AlarmText,
       "e7AlarmTime": e7AlarmTime,
       "e7AlarmCliObject": e7AlarmCliObject,
       "e7AlarmSecObjectClass": e7AlarmSecObjectClass,
       "e7AlarmSecObjectInstance1": e7AlarmSecObjectInstance1,
       "e7AlarmSecObjectInstance2": e7AlarmSecObjectInstance2,
       "e7AlarmSecObjectInstance3": e7AlarmSecObjectInstance3,
       "e7AlarmSecObjectInstance4": e7AlarmSecObjectInstance4,
       "e7AlarmSecObjectInstance5": e7AlarmSecObjectInstance5,
       "e7AlarmSecObjectInstance6": e7AlarmSecObjectInstance6,
       "e7AlarmSecObjectInstance7": e7AlarmSecObjectInstance7,
       "e7AlarmSecObjectInstance8": e7AlarmSecObjectInstance8,
       "e7AlarmTableEnd": e7AlarmTableEnd,
       "e7AlarmCount": e7AlarmCount,
       "e7AlarmCountCritical": e7AlarmCountCritical,
       "e7AlarmCountMajor": e7AlarmCountMajor,
       "e7AlarmCountMinor": e7AlarmCountMinor,
       "e7AlarmCountWarning": e7AlarmCountWarning,
       "e7AlarmCountInfo": e7AlarmCountInfo}
)
