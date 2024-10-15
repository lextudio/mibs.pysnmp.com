# SNMP MIB module (HHMSSMALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HHMSSMALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:26 2024
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Akcp_ObjectIdentity = ObjectIdentity
akcp = _Akcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854)
)
_Hhmsagent_ObjectIdentity = ObjectIdentity
hhmsagent = _Hhmsagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1)
)
_HhmsSensor_ObjectIdentity = ObjectIdentity
hhmsSensor = _HhmsSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2)
)
_HhmsSensorArray_ObjectIdentity = ObjectIdentity
hhmsSensorArray = _HhmsSensorArray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2)
)
_HhmsSensorArrayEntry_ObjectIdentity = ObjectIdentity
hhmsSensorArrayEntry = _HhmsSensorArrayEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1)
)
_HhmsSensorArrayTemp_ObjectIdentity = ObjectIdentity
hhmsSensorArrayTemp = _HhmsSensorArrayTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16)
)
_HhmsSensorArrayTempEntry_ObjectIdentity = ObjectIdentity
hhmsSensorArrayTempEntry = _HhmsSensorArrayTempEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1)
)
_HhmsSensorArrayTempDegree_Type = Integer32
_HhmsSensorArrayTempDegree_Object = MibScalar
hhmsSensorArrayTempDegree = _HhmsSensorArrayTempDegree_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 3),
    _HhmsSensorArrayTempDegree_Type()
)
hhmsSensorArrayTempDegree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempDegree.setStatus("mandatory")


class _HhmsSensorArrayTempStatus_Type(Integer32):
    """Custom type hhmsSensorArrayTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 6),
          ("lowWarning", 5),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArrayTempStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayTempStatus_Object = MibScalar
hhmsSensorArrayTempStatus = _HhmsSensorArrayTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 4),
    _HhmsSensorArrayTempStatus_Type()
)
hhmsSensorArrayTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempStatus.setStatus("mandatory")
_HhmsSensorArrayHumidity_ObjectIdentity = ObjectIdentity
hhmsSensorArrayHumidity = _HhmsSensorArrayHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17)
)
_HhmsSensorArrayHumidityEntry_ObjectIdentity = ObjectIdentity
hhmsSensorArrayHumidityEntry = _HhmsSensorArrayHumidityEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1)
)
_HhmsSensorArrayHumidityPercent_Type = Integer32
_HhmsSensorArrayHumidityPercent_Object = MibScalar
hhmsSensorArrayHumidityPercent = _HhmsSensorArrayHumidityPercent_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 3),
    _HhmsSensorArrayHumidityPercent_Type()
)
hhmsSensorArrayHumidityPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityPercent.setStatus("mandatory")


class _HhmsSensorArrayHumidityStatus_Type(Integer32):
    """Custom type hhmsSensorArrayHumidityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 6),
          ("lowWarning", 5),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArrayHumidityStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayHumidityStatus_Object = MibScalar
hhmsSensorArrayHumidityStatus = _HhmsSensorArrayHumidityStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 4),
    _HhmsSensorArrayHumidityStatus_Type()
)
hhmsSensorArrayHumidityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityStatus.setStatus("mandatory")
_HhmsSensorArraySwitch_ObjectIdentity = ObjectIdentity
hhmsSensorArraySwitch = _HhmsSensorArraySwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18)
)
_HhmsSensorArraySwitchEntry_ObjectIdentity = ObjectIdentity
hhmsSensorArraySwitchEntry = _HhmsSensorArraySwitchEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1)
)


class _HhmsSensorArraySwitchStatus_Type(Integer32):
    """Custom type hhmsSensorArraySwitchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArraySwitchStatus_Type.__name__ = "Integer32"
_HhmsSensorArraySwitchStatus_Object = MibScalar
hhmsSensorArraySwitchStatus = _HhmsSensorArraySwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 3),
    _HhmsSensorArraySwitchStatus_Type()
)
hhmsSensorArraySwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchStatus.setStatus("mandatory")
_HhmsAgentTraps_ObjectIdentity = ObjectIdentity
hhmsAgentTraps = _HhmsAgentTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7)
)


class _HhmsSensorStatus_Type(Integer32):
    """Custom type hhmsSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 6),
          ("lowWarning", 5),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorStatus_Type.__name__ = "Integer32"
_HhmsSensorStatus_Object = MibScalar
hhmsSensorStatus = _HhmsSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 1),
    _HhmsSensorStatus_Type()
)
hhmsSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorStatus.setStatus("mandatory")
_HhmsSensorValue_Type = Integer32
_HhmsSensorValue_Object = MibScalar
hhmsSensorValue = _HhmsSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 2),
    _HhmsSensorValue_Type()
)
hhmsSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorValue.setStatus("mandatory")
_HhmsSensorLevelExceeded_Type = Integer32
_HhmsSensorLevelExceeded_Object = MibScalar
hhmsSensorLevelExceeded = _HhmsSensorLevelExceeded_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 3),
    _HhmsSensorLevelExceeded_Type()
)
hhmsSensorLevelExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorLevelExceeded.setStatus("mandatory")
_HhmsSensorIndex_Type = Integer32
_HhmsSensorIndex_Object = MibScalar
hhmsSensorIndex = _HhmsSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 4),
    _HhmsSensorIndex_Type()
)
hhmsSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorIndex.setStatus("mandatory")
_HhmsSensorName_Type = DisplayString
_HhmsSensorName_Object = MibScalar
hhmsSensorName = _HhmsSensorName_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 5),
    _HhmsSensorName_Type()
)
hhmsSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorName.setStatus("mandatory")
_HhmsSensorDescription_Type = DisplayString
_HhmsSensorDescription_Object = MibScalar
hhmsSensorDescription = _HhmsSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 6),
    _HhmsSensorDescription_Type()
)
hhmsSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hhmsUnknownStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 0)
)
if mibBuilder.loadTexts:
    hhmsUnknownStatus.setStatus(
        ""
    )

hhmsNormalStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 1)
)
if mibBuilder.loadTexts:
    hhmsNormalStatus.setStatus(
        ""
    )

hhmsWarningStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 2)
)
if mibBuilder.loadTexts:
    hhmsWarningStatus.setStatus(
        ""
    )

hhmsCriticalStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 3)
)
if mibBuilder.loadTexts:
    hhmsCriticalStatus.setStatus(
        ""
    )

hhmsDownStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 4)
)
if mibBuilder.loadTexts:
    hhmsDownStatus.setStatus(
        ""
    )

hhmsTemperatureStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 10)
)
hhmsTemperatureStatus.setObjects(
      *(("HHMSSMALL-MIB", "hhmsSensorStatus"),
        ("HHMSSMALL-MIB", "hhmsSensorValue"),
        ("HHMSSMALL-MIB", "hhmsSensorLevelExceeded"),
        ("HHMSSMALL-MIB", "hhmsSensorIndex"),
        ("HHMSSMALL-MIB", "hhmsSensorName"),
        ("HHMSSMALL-MIB", "hhmsSensorDescription"))
)
if mibBuilder.loadTexts:
    hhmsTemperatureStatus.setStatus(
        ""
    )

hhmsHumidityStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 20)
)
hhmsHumidityStatus.setObjects(
      *(("HHMSSMALL-MIB", "hhmsSensorStatus"),
        ("HHMSSMALL-MIB", "hhmsSensorValue"),
        ("HHMSSMALL-MIB", "hhmsSensorLevelExceeded"),
        ("HHMSSMALL-MIB", "hhmsSensorIndex"),
        ("HHMSSMALL-MIB", "hhmsSensorName"),
        ("HHMSSMALL-MIB", "hhmsSensorDescription"))
)
if mibBuilder.loadTexts:
    hhmsHumidityStatus.setStatus(
        ""
    )

hhmsSwitchStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 30)
)
hhmsSwitchStatus.setObjects(
      *(("HHMSSMALL-MIB", "hhmsSensorStatus"),
        ("HHMSSMALL-MIB", "hhmsSensorValue"),
        ("HHMSSMALL-MIB", "hhmsSensorLevelExceeded"),
        ("HHMSSMALL-MIB", "hhmsSensorIndex"),
        ("HHMSSMALL-MIB", "hhmsSensorName"),
        ("HHMSSMALL-MIB", "hhmsSensorDescription"))
)
if mibBuilder.loadTexts:
    hhmsSwitchStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HHMSSMALL-MIB",
    **{"DisplayString": DisplayString,
       "internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "akcp": akcp,
       "hhmsagent": hhmsagent,
       "hhmsUnknownStatus": hhmsUnknownStatus,
       "hhmsNormalStatus": hhmsNormalStatus,
       "hhmsWarningStatus": hhmsWarningStatus,
       "hhmsCriticalStatus": hhmsCriticalStatus,
       "hhmsDownStatus": hhmsDownStatus,
       "hhmsTemperatureStatus": hhmsTemperatureStatus,
       "hhmsHumidityStatus": hhmsHumidityStatus,
       "hhmsSwitchStatus": hhmsSwitchStatus,
       "hhmsSensor": hhmsSensor,
       "hhmsSensorArray": hhmsSensorArray,
       "hhmsSensorArrayEntry": hhmsSensorArrayEntry,
       "hhmsSensorArrayTemp": hhmsSensorArrayTemp,
       "hhmsSensorArrayTempEntry": hhmsSensorArrayTempEntry,
       "hhmsSensorArrayTempDegree": hhmsSensorArrayTempDegree,
       "hhmsSensorArrayTempStatus": hhmsSensorArrayTempStatus,
       "hhmsSensorArrayHumidity": hhmsSensorArrayHumidity,
       "hhmsSensorArrayHumidityEntry": hhmsSensorArrayHumidityEntry,
       "hhmsSensorArrayHumidityPercent": hhmsSensorArrayHumidityPercent,
       "hhmsSensorArrayHumidityStatus": hhmsSensorArrayHumidityStatus,
       "hhmsSensorArraySwitch": hhmsSensorArraySwitch,
       "hhmsSensorArraySwitchEntry": hhmsSensorArraySwitchEntry,
       "hhmsSensorArraySwitchStatus": hhmsSensorArraySwitchStatus,
       "hhmsAgentTraps": hhmsAgentTraps,
       "hhmsSensorStatus": hhmsSensorStatus,
       "hhmsSensorValue": hhmsSensorValue,
       "hhmsSensorLevelExceeded": hhmsSensorLevelExceeded,
       "hhmsSensorIndex": hhmsSensorIndex,
       "hhmsSensorName": hhmsSensorName,
       "hhmsSensorDescription": hhmsSensorDescription}
)
