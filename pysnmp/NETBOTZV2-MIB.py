# SNMP MIB module (NETBOTZV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETBOTZV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:42 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

netBotz_V2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("error", 1),
          ("normal", 2))
    )



class ErrorStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("error", 3),
          ("failure", 5),
          ("info", 1),
          ("normal", 0),
          ("warning", 2))
    )



class BoolValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("null", 2),
          ("yes", 1))
    )



# MIB Managed Objects in the order of their OIDs

_NetBotz_ObjectIdentity = ObjectIdentity
netBotz = _NetBotz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528)
)
_NetBotzV2_ObjectIdentity = ObjectIdentity
netBotzV2 = _NetBotzV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100)
)
_NetBotzEnclosures_ObjectIdentity = ObjectIdentity
netBotzEnclosures = _NetBotzEnclosures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 2)
)
_EnclosureTable_Object = MibTable
enclosureTable = _EnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 2, 1)
)
if mibBuilder.loadTexts:
    enclosureTable.setStatus("current")
_EnclosureEntry_Object = MibTableRow
enclosureEntry = _EnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 2, 1, 1)
)
enclosureEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "enclosureId"),
)
if mibBuilder.loadTexts:
    enclosureEntry.setStatus("current")


class _EnclosureId_Type(DisplayString):
    """Custom type enclosureId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EnclosureId_Type.__name__ = "DisplayString"
_EnclosureId_Object = MibTableColumn
enclosureId = _EnclosureId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 2, 1, 1, 1),
    _EnclosureId_Type()
)
enclosureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureId.setStatus("current")
_EnclosureStatus_Type = OperStatus
_EnclosureStatus_Object = MibTableColumn
enclosureStatus = _EnclosureStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 2, 1, 1, 2),
    _EnclosureStatus_Type()
)
enclosureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureStatus.setStatus("current")
_EnclosureErrorStatus_Type = ErrorStatus
_EnclosureErrorStatus_Object = MibTableColumn
enclosureErrorStatus = _EnclosureErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 2, 1, 1, 3),
    _EnclosureErrorStatus_Type()
)
enclosureErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureErrorStatus.setStatus("current")
_EnclosureLabel_Type = DisplayString
_EnclosureLabel_Object = MibTableColumn
enclosureLabel = _EnclosureLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 2, 1, 1, 4),
    _EnclosureLabel_Type()
)
enclosureLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureLabel.setStatus("current")


class _EnclosureParentEncId_Type(DisplayString):
    """Custom type enclosureParentEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EnclosureParentEncId_Type.__name__ = "DisplayString"
_EnclosureParentEncId_Object = MibTableColumn
enclosureParentEncId = _EnclosureParentEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 2, 1, 1, 5),
    _EnclosureParentEncId_Type()
)
enclosureParentEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureParentEncId.setStatus("current")


class _EnclosureDockedToEncId_Type(DisplayString):
    """Custom type enclosureDockedToEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EnclosureDockedToEncId_Type.__name__ = "DisplayString"
_EnclosureDockedToEncId_Object = MibTableColumn
enclosureDockedToEncId = _EnclosureDockedToEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 2, 1, 1, 6),
    _EnclosureDockedToEncId_Type()
)
enclosureDockedToEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureDockedToEncId.setStatus("current")
_NetBotzPorts_ObjectIdentity = ObjectIdentity
netBotzPorts = _NetBotzPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3)
)
_DinPortTable_Object = MibTable
dinPortTable = _DinPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1)
)
if mibBuilder.loadTexts:
    dinPortTable.setStatus("current")
_DinPortEntry_Object = MibTableRow
dinPortEntry = _DinPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1, 1)
)
dinPortEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "dinPortId"),
)
if mibBuilder.loadTexts:
    dinPortEntry.setStatus("current")


class _DinPortId_Type(DisplayString):
    """Custom type dinPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DinPortId_Type.__name__ = "DisplayString"
_DinPortId_Object = MibTableColumn
dinPortId = _DinPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1, 1, 1),
    _DinPortId_Type()
)
dinPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dinPortId.setStatus("current")
_DinPortStatus_Type = OperStatus
_DinPortStatus_Object = MibTableColumn
dinPortStatus = _DinPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1, 1, 2),
    _DinPortStatus_Type()
)
dinPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dinPortStatus.setStatus("current")
_DinPortLabel_Type = DisplayString
_DinPortLabel_Object = MibTableColumn
dinPortLabel = _DinPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1, 1, 3),
    _DinPortLabel_Type()
)
dinPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dinPortLabel.setStatus("current")


class _DinPortEncId_Type(DisplayString):
    """Custom type dinPortEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DinPortEncId_Type.__name__ = "DisplayString"
_DinPortEncId_Object = MibTableColumn
dinPortEncId = _DinPortEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1, 1, 4),
    _DinPortEncId_Type()
)
dinPortEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dinPortEncId.setStatus("current")
_DinPortSensorIdSuffix_Type = DisplayString
_DinPortSensorIdSuffix_Object = MibTableColumn
dinPortSensorIdSuffix = _DinPortSensorIdSuffix_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1, 1, 5),
    _DinPortSensorIdSuffix_Type()
)
dinPortSensorIdSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dinPortSensorIdSuffix.setStatus("current")
_DinPortSupportsAverage_Type = BoolValue
_DinPortSupportsAverage_Object = MibTableColumn
dinPortSupportsAverage = _DinPortSupportsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1, 1, 6),
    _DinPortSupportsAverage_Type()
)
dinPortSupportsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dinPortSupportsAverage.setStatus("current")
_DinPortSupportsRMS_Type = BoolValue
_DinPortSupportsRMS_Object = MibTableColumn
dinPortSupportsRMS = _DinPortSupportsRMS_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1, 1, 7),
    _DinPortSupportsRMS_Type()
)
dinPortSupportsRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dinPortSupportsRMS.setStatus("current")
_DinPortSupportsDryContact_Type = BoolValue
_DinPortSupportsDryContact_Object = MibTableColumn
dinPortSupportsDryContact = _DinPortSupportsDryContact_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 1, 1, 8),
    _DinPortSupportsDryContact_Type()
)
dinPortSupportsDryContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dinPortSupportsDryContact.setStatus("current")
_OtherPortTable_Object = MibTable
otherPortTable = _OtherPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 10)
)
if mibBuilder.loadTexts:
    otherPortTable.setStatus("current")
_OtherPortEntry_Object = MibTableRow
otherPortEntry = _OtherPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 10, 1)
)
otherPortEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "otherPortId"),
)
if mibBuilder.loadTexts:
    otherPortEntry.setStatus("current")


class _OtherPortId_Type(DisplayString):
    """Custom type otherPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherPortId_Type.__name__ = "DisplayString"
_OtherPortId_Object = MibTableColumn
otherPortId = _OtherPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 10, 1, 1),
    _OtherPortId_Type()
)
otherPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherPortId.setStatus("current")
_OtherPortStatus_Type = OperStatus
_OtherPortStatus_Object = MibTableColumn
otherPortStatus = _OtherPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 10, 1, 2),
    _OtherPortStatus_Type()
)
otherPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherPortStatus.setStatus("current")
_OtherPortLabel_Type = DisplayString
_OtherPortLabel_Object = MibTableColumn
otherPortLabel = _OtherPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 10, 1, 3),
    _OtherPortLabel_Type()
)
otherPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherPortLabel.setStatus("current")


class _OtherPortEncId_Type(DisplayString):
    """Custom type otherPortEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherPortEncId_Type.__name__ = "DisplayString"
_OtherPortEncId_Object = MibTableColumn
otherPortEncId = _OtherPortEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 3, 10, 1, 4),
    _OtherPortEncId_Type()
)
otherPortEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherPortEncId.setStatus("current")
_NetBotzSensors_ObjectIdentity = ObjectIdentity
netBotzSensors = _NetBotzSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4)
)
_NetBotzNumericSensors_ObjectIdentity = ObjectIdentity
netBotzNumericSensors = _NetBotzNumericSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1)
)
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1)
)
tempSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "tempSensorId"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("current")


class _TempSensorId_Type(DisplayString):
    """Custom type tempSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TempSensorId_Type.__name__ = "DisplayString"
_TempSensorId_Object = MibTableColumn
tempSensorId = _TempSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1, 1),
    _TempSensorId_Type()
)
tempSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorId.setStatus("current")


class _TempSensorValue_Type(Integer32):
    """Custom type tempSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 1000),
    )


_TempSensorValue_Type.__name__ = "Integer32"
_TempSensorValue_Object = MibTableColumn
tempSensorValue = _TempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1, 2),
    _TempSensorValue_Type()
)
tempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValue.setStatus("current")
_TempSensorErrorStatus_Type = ErrorStatus
_TempSensorErrorStatus_Object = MibTableColumn
tempSensorErrorStatus = _TempSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1, 3),
    _TempSensorErrorStatus_Type()
)
tempSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorErrorStatus.setStatus("current")
_TempSensorLabel_Type = DisplayString
_TempSensorLabel_Object = MibTableColumn
tempSensorLabel = _TempSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1, 4),
    _TempSensorLabel_Type()
)
tempSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorLabel.setStatus("current")


class _TempSensorEncId_Type(DisplayString):
    """Custom type tempSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TempSensorEncId_Type.__name__ = "DisplayString"
_TempSensorEncId_Object = MibTableColumn
tempSensorEncId = _TempSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1, 5),
    _TempSensorEncId_Type()
)
tempSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorEncId.setStatus("current")


class _TempSensorPortId_Type(DisplayString):
    """Custom type tempSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TempSensorPortId_Type.__name__ = "DisplayString"
_TempSensorPortId_Object = MibTableColumn
tempSensorPortId = _TempSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1, 6),
    _TempSensorPortId_Type()
)
tempSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorPortId.setStatus("current")
_TempSensorValueStr_Type = DisplayString
_TempSensorValueStr_Object = MibTableColumn
tempSensorValueStr = _TempSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1, 7),
    _TempSensorValueStr_Type()
)
tempSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValueStr.setStatus("current")


class _TempSensorValueInt_Type(Integer32):
    """Custom type tempSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_TempSensorValueInt_Type.__name__ = "Integer32"
_TempSensorValueInt_Object = MibTableColumn
tempSensorValueInt = _TempSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1, 8),
    _TempSensorValueInt_Type()
)
tempSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValueInt.setStatus("current")


class _TempSensorValueIntF_Type(Integer32):
    """Custom type tempSensorValueIntF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 212),
    )


_TempSensorValueIntF_Type.__name__ = "Integer32"
_TempSensorValueIntF_Object = MibTableColumn
tempSensorValueIntF = _TempSensorValueIntF_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 1, 1, 9),
    _TempSensorValueIntF_Type()
)
tempSensorValueIntF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValueIntF.setStatus("current")
_HumiSensorTable_Object = MibTable
humiSensorTable = _HumiSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2)
)
if mibBuilder.loadTexts:
    humiSensorTable.setStatus("current")
_HumiSensorEntry_Object = MibTableRow
humiSensorEntry = _HumiSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2, 1)
)
humiSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "humiSensorId"),
)
if mibBuilder.loadTexts:
    humiSensorEntry.setStatus("current")


class _HumiSensorId_Type(DisplayString):
    """Custom type humiSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HumiSensorId_Type.__name__ = "DisplayString"
_HumiSensorId_Object = MibTableColumn
humiSensorId = _HumiSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2, 1, 1),
    _HumiSensorId_Type()
)
humiSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorId.setStatus("current")


class _HumiSensorValue_Type(Integer32):
    """Custom type humiSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HumiSensorValue_Type.__name__ = "Integer32"
_HumiSensorValue_Object = MibTableColumn
humiSensorValue = _HumiSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2, 1, 2),
    _HumiSensorValue_Type()
)
humiSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorValue.setStatus("current")
_HumiSensorErrorStatus_Type = ErrorStatus
_HumiSensorErrorStatus_Object = MibTableColumn
humiSensorErrorStatus = _HumiSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2, 1, 3),
    _HumiSensorErrorStatus_Type()
)
humiSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorErrorStatus.setStatus("current")
_HumiSensorLabel_Type = DisplayString
_HumiSensorLabel_Object = MibTableColumn
humiSensorLabel = _HumiSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2, 1, 4),
    _HumiSensorLabel_Type()
)
humiSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorLabel.setStatus("current")


class _HumiSensorEncId_Type(DisplayString):
    """Custom type humiSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HumiSensorEncId_Type.__name__ = "DisplayString"
_HumiSensorEncId_Object = MibTableColumn
humiSensorEncId = _HumiSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2, 1, 5),
    _HumiSensorEncId_Type()
)
humiSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorEncId.setStatus("current")


class _HumiSensorPortId_Type(DisplayString):
    """Custom type humiSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HumiSensorPortId_Type.__name__ = "DisplayString"
_HumiSensorPortId_Object = MibTableColumn
humiSensorPortId = _HumiSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2, 1, 6),
    _HumiSensorPortId_Type()
)
humiSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorPortId.setStatus("current")
_HumiSensorValueStr_Type = DisplayString
_HumiSensorValueStr_Object = MibTableColumn
humiSensorValueStr = _HumiSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2, 1, 7),
    _HumiSensorValueStr_Type()
)
humiSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorValueStr.setStatus("current")


class _HumiSensorValueInt_Type(Integer32):
    """Custom type humiSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HumiSensorValueInt_Type.__name__ = "Integer32"
_HumiSensorValueInt_Object = MibTableColumn
humiSensorValueInt = _HumiSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 2, 1, 8),
    _HumiSensorValueInt_Type()
)
humiSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorValueInt.setStatus("current")
_DewPointSensorTable_Object = MibTable
dewPointSensorTable = _DewPointSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3)
)
if mibBuilder.loadTexts:
    dewPointSensorTable.setStatus("current")
_DewPointSensorEntry_Object = MibTableRow
dewPointSensorEntry = _DewPointSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3, 1)
)
dewPointSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "dewPointSensorId"),
)
if mibBuilder.loadTexts:
    dewPointSensorEntry.setStatus("current")


class _DewPointSensorId_Type(DisplayString):
    """Custom type dewPointSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DewPointSensorId_Type.__name__ = "DisplayString"
_DewPointSensorId_Object = MibTableColumn
dewPointSensorId = _DewPointSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3, 1, 1),
    _DewPointSensorId_Type()
)
dewPointSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorId.setStatus("current")


class _DewPointSensorValue_Type(Integer32):
    """Custom type dewPointSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 1000),
    )


_DewPointSensorValue_Type.__name__ = "Integer32"
_DewPointSensorValue_Object = MibTableColumn
dewPointSensorValue = _DewPointSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3, 1, 2),
    _DewPointSensorValue_Type()
)
dewPointSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorValue.setStatus("current")
_DewPointSensorErrorStatus_Type = ErrorStatus
_DewPointSensorErrorStatus_Object = MibTableColumn
dewPointSensorErrorStatus = _DewPointSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3, 1, 3),
    _DewPointSensorErrorStatus_Type()
)
dewPointSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorErrorStatus.setStatus("current")
_DewPointSensorLabel_Type = DisplayString
_DewPointSensorLabel_Object = MibTableColumn
dewPointSensorLabel = _DewPointSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3, 1, 4),
    _DewPointSensorLabel_Type()
)
dewPointSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorLabel.setStatus("current")


class _DewPointSensorEncId_Type(DisplayString):
    """Custom type dewPointSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DewPointSensorEncId_Type.__name__ = "DisplayString"
_DewPointSensorEncId_Object = MibTableColumn
dewPointSensorEncId = _DewPointSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3, 1, 5),
    _DewPointSensorEncId_Type()
)
dewPointSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorEncId.setStatus("current")


class _DewPointSensorPortId_Type(DisplayString):
    """Custom type dewPointSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DewPointSensorPortId_Type.__name__ = "DisplayString"
_DewPointSensorPortId_Object = MibTableColumn
dewPointSensorPortId = _DewPointSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3, 1, 6),
    _DewPointSensorPortId_Type()
)
dewPointSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorPortId.setStatus("current")
_DewPointSensorValueStr_Type = DisplayString
_DewPointSensorValueStr_Object = MibTableColumn
dewPointSensorValueStr = _DewPointSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3, 1, 7),
    _DewPointSensorValueStr_Type()
)
dewPointSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorValueStr.setStatus("current")


class _DewPointSensorValueInt_Type(Integer32):
    """Custom type dewPointSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_DewPointSensorValueInt_Type.__name__ = "Integer32"
_DewPointSensorValueInt_Object = MibTableColumn
dewPointSensorValueInt = _DewPointSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 3, 1, 8),
    _DewPointSensorValueInt_Type()
)
dewPointSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorValueInt.setStatus("current")
_AudioSensorTable_Object = MibTable
audioSensorTable = _AudioSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4)
)
if mibBuilder.loadTexts:
    audioSensorTable.setStatus("current")
_AudioSensorEntry_Object = MibTableRow
audioSensorEntry = _AudioSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4, 1)
)
audioSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "audioSensorId"),
)
if mibBuilder.loadTexts:
    audioSensorEntry.setStatus("current")


class _AudioSensorId_Type(DisplayString):
    """Custom type audioSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AudioSensorId_Type.__name__ = "DisplayString"
_AudioSensorId_Object = MibTableColumn
audioSensorId = _AudioSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4, 1, 1),
    _AudioSensorId_Type()
)
audioSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSensorId.setStatus("current")
_AudioSensorValue_Type = Integer32
_AudioSensorValue_Object = MibTableColumn
audioSensorValue = _AudioSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4, 1, 2),
    _AudioSensorValue_Type()
)
audioSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSensorValue.setStatus("current")
_AudioSensorErrorStatus_Type = ErrorStatus
_AudioSensorErrorStatus_Object = MibTableColumn
audioSensorErrorStatus = _AudioSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4, 1, 3),
    _AudioSensorErrorStatus_Type()
)
audioSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSensorErrorStatus.setStatus("current")
_AudioSensorLabel_Type = DisplayString
_AudioSensorLabel_Object = MibTableColumn
audioSensorLabel = _AudioSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4, 1, 4),
    _AudioSensorLabel_Type()
)
audioSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSensorLabel.setStatus("current")


class _AudioSensorEncId_Type(DisplayString):
    """Custom type audioSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AudioSensorEncId_Type.__name__ = "DisplayString"
_AudioSensorEncId_Object = MibTableColumn
audioSensorEncId = _AudioSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4, 1, 5),
    _AudioSensorEncId_Type()
)
audioSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSensorEncId.setStatus("current")


class _AudioSensorPortId_Type(DisplayString):
    """Custom type audioSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AudioSensorPortId_Type.__name__ = "DisplayString"
_AudioSensorPortId_Object = MibTableColumn
audioSensorPortId = _AudioSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4, 1, 6),
    _AudioSensorPortId_Type()
)
audioSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSensorPortId.setStatus("current")
_AudioSensorValueStr_Type = DisplayString
_AudioSensorValueStr_Object = MibTableColumn
audioSensorValueStr = _AudioSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4, 1, 7),
    _AudioSensorValueStr_Type()
)
audioSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSensorValueStr.setStatus("current")
_AudioSensorValueInt_Type = Integer32
_AudioSensorValueInt_Object = MibTableColumn
audioSensorValueInt = _AudioSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 4, 1, 8),
    _AudioSensorValueInt_Type()
)
audioSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSensorValueInt.setStatus("current")
_AirFlowSensorTable_Object = MibTable
airFlowSensorTable = _AirFlowSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5)
)
if mibBuilder.loadTexts:
    airFlowSensorTable.setStatus("current")
_AirFlowSensorEntry_Object = MibTableRow
airFlowSensorEntry = _AirFlowSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5, 1)
)
airFlowSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "airFlowSensorId"),
)
if mibBuilder.loadTexts:
    airFlowSensorEntry.setStatus("current")


class _AirFlowSensorId_Type(DisplayString):
    """Custom type airFlowSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AirFlowSensorId_Type.__name__ = "DisplayString"
_AirFlowSensorId_Object = MibTableColumn
airFlowSensorId = _AirFlowSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5, 1, 1),
    _AirFlowSensorId_Type()
)
airFlowSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorId.setStatus("current")


class _AirFlowSensorValue_Type(Integer32):
    """Custom type airFlowSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AirFlowSensorValue_Type.__name__ = "Integer32"
_AirFlowSensorValue_Object = MibTableColumn
airFlowSensorValue = _AirFlowSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5, 1, 2),
    _AirFlowSensorValue_Type()
)
airFlowSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorValue.setStatus("current")
_AirFlowSensorErrorStatus_Type = ErrorStatus
_AirFlowSensorErrorStatus_Object = MibTableColumn
airFlowSensorErrorStatus = _AirFlowSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5, 1, 3),
    _AirFlowSensorErrorStatus_Type()
)
airFlowSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorErrorStatus.setStatus("current")
_AirFlowSensorLabel_Type = DisplayString
_AirFlowSensorLabel_Object = MibTableColumn
airFlowSensorLabel = _AirFlowSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5, 1, 4),
    _AirFlowSensorLabel_Type()
)
airFlowSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorLabel.setStatus("current")


class _AirFlowSensorEncId_Type(DisplayString):
    """Custom type airFlowSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AirFlowSensorEncId_Type.__name__ = "DisplayString"
_AirFlowSensorEncId_Object = MibTableColumn
airFlowSensorEncId = _AirFlowSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5, 1, 5),
    _AirFlowSensorEncId_Type()
)
airFlowSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorEncId.setStatus("current")


class _AirFlowSensorPortId_Type(DisplayString):
    """Custom type airFlowSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AirFlowSensorPortId_Type.__name__ = "DisplayString"
_AirFlowSensorPortId_Object = MibTableColumn
airFlowSensorPortId = _AirFlowSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5, 1, 6),
    _AirFlowSensorPortId_Type()
)
airFlowSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorPortId.setStatus("current")
_AirFlowSensorValueStr_Type = DisplayString
_AirFlowSensorValueStr_Object = MibTableColumn
airFlowSensorValueStr = _AirFlowSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5, 1, 7),
    _AirFlowSensorValueStr_Type()
)
airFlowSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorValueStr.setStatus("current")


class _AirFlowSensorValueInt_Type(Integer32):
    """Custom type airFlowSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AirFlowSensorValueInt_Type.__name__ = "Integer32"
_AirFlowSensorValueInt_Object = MibTableColumn
airFlowSensorValueInt = _AirFlowSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 5, 1, 8),
    _AirFlowSensorValueInt_Type()
)
airFlowSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorValueInt.setStatus("current")
_AmpDetectSensorTable_Object = MibTable
ampDetectSensorTable = _AmpDetectSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6)
)
if mibBuilder.loadTexts:
    ampDetectSensorTable.setStatus("current")
_AmpDetectSensorEntry_Object = MibTableRow
ampDetectSensorEntry = _AmpDetectSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6, 1)
)
ampDetectSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "ampDetectSensorId"),
)
if mibBuilder.loadTexts:
    ampDetectSensorEntry.setStatus("current")


class _AmpDetectSensorId_Type(DisplayString):
    """Custom type ampDetectSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AmpDetectSensorId_Type.__name__ = "DisplayString"
_AmpDetectSensorId_Object = MibTableColumn
ampDetectSensorId = _AmpDetectSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6, 1, 1),
    _AmpDetectSensorId_Type()
)
ampDetectSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorId.setStatus("current")


class _AmpDetectSensorValue_Type(Integer32):
    """Custom type ampDetectSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AmpDetectSensorValue_Type.__name__ = "Integer32"
_AmpDetectSensorValue_Object = MibTableColumn
ampDetectSensorValue = _AmpDetectSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6, 1, 2),
    _AmpDetectSensorValue_Type()
)
ampDetectSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorValue.setStatus("current")
_AmpDetectSensorErrorStatus_Type = ErrorStatus
_AmpDetectSensorErrorStatus_Object = MibTableColumn
ampDetectSensorErrorStatus = _AmpDetectSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6, 1, 3),
    _AmpDetectSensorErrorStatus_Type()
)
ampDetectSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorErrorStatus.setStatus("current")
_AmpDetectSensorLabel_Type = DisplayString
_AmpDetectSensorLabel_Object = MibTableColumn
ampDetectSensorLabel = _AmpDetectSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6, 1, 4),
    _AmpDetectSensorLabel_Type()
)
ampDetectSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorLabel.setStatus("current")


class _AmpDetectSensorEncId_Type(DisplayString):
    """Custom type ampDetectSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AmpDetectSensorEncId_Type.__name__ = "DisplayString"
_AmpDetectSensorEncId_Object = MibTableColumn
ampDetectSensorEncId = _AmpDetectSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6, 1, 5),
    _AmpDetectSensorEncId_Type()
)
ampDetectSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorEncId.setStatus("current")


class _AmpDetectSensorPortId_Type(DisplayString):
    """Custom type ampDetectSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AmpDetectSensorPortId_Type.__name__ = "DisplayString"
_AmpDetectSensorPortId_Object = MibTableColumn
ampDetectSensorPortId = _AmpDetectSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6, 1, 6),
    _AmpDetectSensorPortId_Type()
)
ampDetectSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorPortId.setStatus("current")
_AmpDetectSensorValueStr_Type = DisplayString
_AmpDetectSensorValueStr_Object = MibTableColumn
ampDetectSensorValueStr = _AmpDetectSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6, 1, 7),
    _AmpDetectSensorValueStr_Type()
)
ampDetectSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorValueStr.setStatus("current")


class _AmpDetectSensorValueInt_Type(Integer32):
    """Custom type ampDetectSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_AmpDetectSensorValueInt_Type.__name__ = "Integer32"
_AmpDetectSensorValueInt_Object = MibTableColumn
ampDetectSensorValueInt = _AmpDetectSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 6, 1, 8),
    _AmpDetectSensorValueInt_Type()
)
ampDetectSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorValueInt.setStatus("current")
_OtherNumericSensorTable_Object = MibTable
otherNumericSensorTable = _OtherNumericSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10)
)
if mibBuilder.loadTexts:
    otherNumericSensorTable.setStatus("current")
_OtherNumericSensorEntry_Object = MibTableRow
otherNumericSensorEntry = _OtherNumericSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1)
)
otherNumericSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "otherNumericSensorId"),
)
if mibBuilder.loadTexts:
    otherNumericSensorEntry.setStatus("current")


class _OtherNumericSensorId_Type(DisplayString):
    """Custom type otherNumericSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherNumericSensorId_Type.__name__ = "DisplayString"
_OtherNumericSensorId_Object = MibTableColumn
otherNumericSensorId = _OtherNumericSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 1),
    _OtherNumericSensorId_Type()
)
otherNumericSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorId.setStatus("current")
_OtherNumericSensorValue_Type = Integer32
_OtherNumericSensorValue_Object = MibTableColumn
otherNumericSensorValue = _OtherNumericSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 2),
    _OtherNumericSensorValue_Type()
)
otherNumericSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValue.setStatus("current")
_OtherNumericSensorErrorStatus_Type = ErrorStatus
_OtherNumericSensorErrorStatus_Object = MibTableColumn
otherNumericSensorErrorStatus = _OtherNumericSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 3),
    _OtherNumericSensorErrorStatus_Type()
)
otherNumericSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorErrorStatus.setStatus("current")
_OtherNumericSensorLabel_Type = DisplayString
_OtherNumericSensorLabel_Object = MibTableColumn
otherNumericSensorLabel = _OtherNumericSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 4),
    _OtherNumericSensorLabel_Type()
)
otherNumericSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorLabel.setStatus("current")


class _OtherNumericSensorEncId_Type(DisplayString):
    """Custom type otherNumericSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherNumericSensorEncId_Type.__name__ = "DisplayString"
_OtherNumericSensorEncId_Object = MibTableColumn
otherNumericSensorEncId = _OtherNumericSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 5),
    _OtherNumericSensorEncId_Type()
)
otherNumericSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorEncId.setStatus("current")


class _OtherNumericSensorPortId_Type(DisplayString):
    """Custom type otherNumericSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherNumericSensorPortId_Type.__name__ = "DisplayString"
_OtherNumericSensorPortId_Object = MibTableColumn
otherNumericSensorPortId = _OtherNumericSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 6),
    _OtherNumericSensorPortId_Type()
)
otherNumericSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorPortId.setStatus("current")
_OtherNumericSensorValueStr_Type = DisplayString
_OtherNumericSensorValueStr_Object = MibTableColumn
otherNumericSensorValueStr = _OtherNumericSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 7),
    _OtherNumericSensorValueStr_Type()
)
otherNumericSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValueStr.setStatus("current")
_OtherNumericSensorValueInt_Type = Integer32
_OtherNumericSensorValueInt_Object = MibTableColumn
otherNumericSensorValueInt = _OtherNumericSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 8),
    _OtherNumericSensorValueInt_Type()
)
otherNumericSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValueInt.setStatus("current")
_OtherNumericSensorUnits_Type = DisplayString
_OtherNumericSensorUnits_Object = MibTableColumn
otherNumericSensorUnits = _OtherNumericSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 9),
    _OtherNumericSensorUnits_Type()
)
otherNumericSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorUnits.setStatus("current")
_OtherNumericSensorValueIntX1000_Type = Integer32
_OtherNumericSensorValueIntX1000_Object = MibTableColumn
otherNumericSensorValueIntX1000 = _OtherNumericSensorValueIntX1000_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 10),
    _OtherNumericSensorValueIntX1000_Type()
)
otherNumericSensorValueIntX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValueIntX1000.setStatus("current")
_OtherNumericSensorValueIntX1000000_Type = Integer32
_OtherNumericSensorValueIntX1000000_Object = MibTableColumn
otherNumericSensorValueIntX1000000 = _OtherNumericSensorValueIntX1000000_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 1, 10, 1, 11),
    _OtherNumericSensorValueIntX1000000_Type()
)
otherNumericSensorValueIntX1000000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValueIntX1000000.setStatus("current")
_NetBotzStateSensors_ObjectIdentity = ObjectIdentity
netBotzStateSensors = _NetBotzStateSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2)
)
_DryContactSensorTable_Object = MibTable
dryContactSensorTable = _DryContactSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dryContactSensorTable.setStatus("current")
_DryContactSensorEntry_Object = MibTableRow
dryContactSensorEntry = _DryContactSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 1, 1)
)
dryContactSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "dryContactSensorId"),
)
if mibBuilder.loadTexts:
    dryContactSensorEntry.setStatus("current")


class _DryContactSensorId_Type(DisplayString):
    """Custom type dryContactSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DryContactSensorId_Type.__name__ = "DisplayString"
_DryContactSensorId_Object = MibTableColumn
dryContactSensorId = _DryContactSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 1, 1, 1),
    _DryContactSensorId_Type()
)
dryContactSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorId.setStatus("current")


class _DryContactSensorValue_Type(Integer32):
    """Custom type dryContactSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("null", -1),
          ("open", 0))
    )


_DryContactSensorValue_Type.__name__ = "Integer32"
_DryContactSensorValue_Object = MibTableColumn
dryContactSensorValue = _DryContactSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 1, 1, 2),
    _DryContactSensorValue_Type()
)
dryContactSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorValue.setStatus("current")
_DryContactSensorErrorStatus_Type = ErrorStatus
_DryContactSensorErrorStatus_Object = MibTableColumn
dryContactSensorErrorStatus = _DryContactSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 1, 1, 3),
    _DryContactSensorErrorStatus_Type()
)
dryContactSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorErrorStatus.setStatus("current")
_DryContactSensorLabel_Type = DisplayString
_DryContactSensorLabel_Object = MibTableColumn
dryContactSensorLabel = _DryContactSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 1, 1, 4),
    _DryContactSensorLabel_Type()
)
dryContactSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorLabel.setStatus("current")


class _DryContactSensorEncId_Type(DisplayString):
    """Custom type dryContactSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DryContactSensorEncId_Type.__name__ = "DisplayString"
_DryContactSensorEncId_Object = MibTableColumn
dryContactSensorEncId = _DryContactSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 1, 1, 5),
    _DryContactSensorEncId_Type()
)
dryContactSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorEncId.setStatus("current")


class _DryContactSensorPortId_Type(DisplayString):
    """Custom type dryContactSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DryContactSensorPortId_Type.__name__ = "DisplayString"
_DryContactSensorPortId_Object = MibTableColumn
dryContactSensorPortId = _DryContactSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 1, 1, 6),
    _DryContactSensorPortId_Type()
)
dryContactSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorPortId.setStatus("current")
_DryContactSensorValueStr_Type = DisplayString
_DryContactSensorValueStr_Object = MibTableColumn
dryContactSensorValueStr = _DryContactSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 1, 1, 7),
    _DryContactSensorValueStr_Type()
)
dryContactSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorValueStr.setStatus("current")
_DoorSwitchSensorTable_Object = MibTable
doorSwitchSensorTable = _DoorSwitchSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 2)
)
if mibBuilder.loadTexts:
    doorSwitchSensorTable.setStatus("current")
_DoorSwitchSensorEntry_Object = MibTableRow
doorSwitchSensorEntry = _DoorSwitchSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 2, 1)
)
doorSwitchSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "doorSwitchSensorId"),
)
if mibBuilder.loadTexts:
    doorSwitchSensorEntry.setStatus("current")


class _DoorSwitchSensorId_Type(DisplayString):
    """Custom type doorSwitchSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DoorSwitchSensorId_Type.__name__ = "DisplayString"
_DoorSwitchSensorId_Object = MibTableColumn
doorSwitchSensorId = _DoorSwitchSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 2, 1, 1),
    _DoorSwitchSensorId_Type()
)
doorSwitchSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorId.setStatus("current")


class _DoorSwitchSensorValue_Type(Integer32):
    """Custom type doorSwitchSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("null", -1),
          ("open", 0))
    )


_DoorSwitchSensorValue_Type.__name__ = "Integer32"
_DoorSwitchSensorValue_Object = MibTableColumn
doorSwitchSensorValue = _DoorSwitchSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 2, 1, 2),
    _DoorSwitchSensorValue_Type()
)
doorSwitchSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorValue.setStatus("current")
_DoorSwitchSensorErrorStatus_Type = ErrorStatus
_DoorSwitchSensorErrorStatus_Object = MibTableColumn
doorSwitchSensorErrorStatus = _DoorSwitchSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 2, 1, 3),
    _DoorSwitchSensorErrorStatus_Type()
)
doorSwitchSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorErrorStatus.setStatus("current")
_DoorSwitchSensorLabel_Type = DisplayString
_DoorSwitchSensorLabel_Object = MibTableColumn
doorSwitchSensorLabel = _DoorSwitchSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 2, 1, 4),
    _DoorSwitchSensorLabel_Type()
)
doorSwitchSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorLabel.setStatus("current")


class _DoorSwitchSensorEncId_Type(DisplayString):
    """Custom type doorSwitchSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DoorSwitchSensorEncId_Type.__name__ = "DisplayString"
_DoorSwitchSensorEncId_Object = MibTableColumn
doorSwitchSensorEncId = _DoorSwitchSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 2, 1, 5),
    _DoorSwitchSensorEncId_Type()
)
doorSwitchSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorEncId.setStatus("current")


class _DoorSwitchSensorPortId_Type(DisplayString):
    """Custom type doorSwitchSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DoorSwitchSensorPortId_Type.__name__ = "DisplayString"
_DoorSwitchSensorPortId_Object = MibTableColumn
doorSwitchSensorPortId = _DoorSwitchSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 2, 1, 6),
    _DoorSwitchSensorPortId_Type()
)
doorSwitchSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorPortId.setStatus("current")
_DoorSwitchSensorValueStr_Type = DisplayString
_DoorSwitchSensorValueStr_Object = MibTableColumn
doorSwitchSensorValueStr = _DoorSwitchSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 2, 1, 7),
    _DoorSwitchSensorValueStr_Type()
)
doorSwitchSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorValueStr.setStatus("current")
_CameraMotionSensorTable_Object = MibTable
cameraMotionSensorTable = _CameraMotionSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 3)
)
if mibBuilder.loadTexts:
    cameraMotionSensorTable.setStatus("current")
_CameraMotionSensorEntry_Object = MibTableRow
cameraMotionSensorEntry = _CameraMotionSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 3, 1)
)
cameraMotionSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "cameraMotionSensorId"),
)
if mibBuilder.loadTexts:
    cameraMotionSensorEntry.setStatus("current")


class _CameraMotionSensorId_Type(DisplayString):
    """Custom type cameraMotionSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraMotionSensorId_Type.__name__ = "DisplayString"
_CameraMotionSensorId_Object = MibTableColumn
cameraMotionSensorId = _CameraMotionSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 3, 1, 1),
    _CameraMotionSensorId_Type()
)
cameraMotionSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorId.setStatus("current")


class _CameraMotionSensorValue_Type(Integer32):
    """Custom type cameraMotionSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("motionDetected", 1),
          ("noMotion", 0),
          ("null", -1))
    )


_CameraMotionSensorValue_Type.__name__ = "Integer32"
_CameraMotionSensorValue_Object = MibTableColumn
cameraMotionSensorValue = _CameraMotionSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 3, 1, 2),
    _CameraMotionSensorValue_Type()
)
cameraMotionSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorValue.setStatus("current")
_CameraMotionSensorErrorStatus_Type = ErrorStatus
_CameraMotionSensorErrorStatus_Object = MibTableColumn
cameraMotionSensorErrorStatus = _CameraMotionSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 3, 1, 3),
    _CameraMotionSensorErrorStatus_Type()
)
cameraMotionSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorErrorStatus.setStatus("current")
_CameraMotionSensorLabel_Type = DisplayString
_CameraMotionSensorLabel_Object = MibTableColumn
cameraMotionSensorLabel = _CameraMotionSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 3, 1, 4),
    _CameraMotionSensorLabel_Type()
)
cameraMotionSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorLabel.setStatus("current")


class _CameraMotionSensorEncId_Type(DisplayString):
    """Custom type cameraMotionSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraMotionSensorEncId_Type.__name__ = "DisplayString"
_CameraMotionSensorEncId_Object = MibTableColumn
cameraMotionSensorEncId = _CameraMotionSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 3, 1, 5),
    _CameraMotionSensorEncId_Type()
)
cameraMotionSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorEncId.setStatus("current")


class _CameraMotionSensorPortId_Type(DisplayString):
    """Custom type cameraMotionSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraMotionSensorPortId_Type.__name__ = "DisplayString"
_CameraMotionSensorPortId_Object = MibTableColumn
cameraMotionSensorPortId = _CameraMotionSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 3, 1, 6),
    _CameraMotionSensorPortId_Type()
)
cameraMotionSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorPortId.setStatus("current")
_CameraMotionSensorValueStr_Type = DisplayString
_CameraMotionSensorValueStr_Object = MibTableColumn
cameraMotionSensorValueStr = _CameraMotionSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 3, 1, 7),
    _CameraMotionSensorValueStr_Type()
)
cameraMotionSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorValueStr.setStatus("current")
_OtherStateSensorTable_Object = MibTable
otherStateSensorTable = _OtherStateSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 10)
)
if mibBuilder.loadTexts:
    otherStateSensorTable.setStatus("current")
_OtherStateSensorEntry_Object = MibTableRow
otherStateSensorEntry = _OtherStateSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 10, 1)
)
otherStateSensorEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "otherStateSensorId"),
)
if mibBuilder.loadTexts:
    otherStateSensorEntry.setStatus("current")


class _OtherStateSensorId_Type(DisplayString):
    """Custom type otherStateSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherStateSensorId_Type.__name__ = "DisplayString"
_OtherStateSensorId_Object = MibTableColumn
otherStateSensorId = _OtherStateSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 10, 1, 1),
    _OtherStateSensorId_Type()
)
otherStateSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorId.setStatus("current")
_OtherStateSensorValue_Type = Integer32
_OtherStateSensorValue_Object = MibTableColumn
otherStateSensorValue = _OtherStateSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 10, 1, 2),
    _OtherStateSensorValue_Type()
)
otherStateSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorValue.setStatus("current")
_OtherStateSensorErrorStatus_Type = ErrorStatus
_OtherStateSensorErrorStatus_Object = MibTableColumn
otherStateSensorErrorStatus = _OtherStateSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 10, 1, 3),
    _OtherStateSensorErrorStatus_Type()
)
otherStateSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorErrorStatus.setStatus("current")
_OtherStateSensorLabel_Type = DisplayString
_OtherStateSensorLabel_Object = MibTableColumn
otherStateSensorLabel = _OtherStateSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 10, 1, 4),
    _OtherStateSensorLabel_Type()
)
otherStateSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorLabel.setStatus("current")


class _OtherStateSensorEncId_Type(DisplayString):
    """Custom type otherStateSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherStateSensorEncId_Type.__name__ = "DisplayString"
_OtherStateSensorEncId_Object = MibTableColumn
otherStateSensorEncId = _OtherStateSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 10, 1, 5),
    _OtherStateSensorEncId_Type()
)
otherStateSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorEncId.setStatus("current")


class _OtherStateSensorPortId_Type(DisplayString):
    """Custom type otherStateSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherStateSensorPortId_Type.__name__ = "DisplayString"
_OtherStateSensorPortId_Object = MibTableColumn
otherStateSensorPortId = _OtherStateSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 10, 1, 6),
    _OtherStateSensorPortId_Type()
)
otherStateSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorPortId.setStatus("current")
_OtherStateSensorValueStr_Type = DisplayString
_OtherStateSensorValueStr_Object = MibTableColumn
otherStateSensorValueStr = _OtherStateSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 4, 2, 10, 1, 7),
    _OtherStateSensorValueStr_Type()
)
otherStateSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorValueStr.setStatus("current")
_NetBotzErrors_ObjectIdentity = ObjectIdentity
netBotzErrors = _NetBotzErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5)
)
_ErrorCondTable_Object = MibTable
errorCondTable = _ErrorCondTable_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1)
)
if mibBuilder.loadTexts:
    errorCondTable.setStatus("current")
_ErrorCondEntry_Object = MibTableRow
errorCondEntry = _ErrorCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1)
)
errorCondEntry.setIndexNames(
    (0, "NETBOTZV2-MIB", "errorCondId"),
)
if mibBuilder.loadTexts:
    errorCondEntry.setStatus("current")


class _ErrorCondId_Type(DisplayString):
    """Custom type errorCondId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondId_Type.__name__ = "DisplayString"
_ErrorCondId_Object = MibTableColumn
errorCondId = _ErrorCondId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 1),
    _ErrorCondId_Type()
)
errorCondId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondId.setStatus("current")
_ErrorCondSeverity_Type = ErrorStatus
_ErrorCondSeverity_Object = MibTableColumn
errorCondSeverity = _ErrorCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 2),
    _ErrorCondSeverity_Type()
)
errorCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondSeverity.setStatus("current")


class _ErrorCondTypeId_Type(DisplayString):
    """Custom type errorCondTypeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondTypeId_Type.__name__ = "DisplayString"
_ErrorCondTypeId_Object = MibTableColumn
errorCondTypeId = _ErrorCondTypeId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 3),
    _ErrorCondTypeId_Type()
)
errorCondTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondTypeId.setStatus("current")
_ErrorCondStartTime_Type = DateAndTime
_ErrorCondStartTime_Object = MibTableColumn
errorCondStartTime = _ErrorCondStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 4),
    _ErrorCondStartTime_Type()
)
errorCondStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondStartTime.setStatus("current")
_ErrorCondStartTimeStr_Type = DisplayString
_ErrorCondStartTimeStr_Object = MibTableColumn
errorCondStartTimeStr = _ErrorCondStartTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 5),
    _ErrorCondStartTimeStr_Type()
)
errorCondStartTimeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondStartTimeStr.setStatus("current")
_ErrorCondResolved_Type = BoolValue
_ErrorCondResolved_Object = MibTableColumn
errorCondResolved = _ErrorCondResolved_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 6),
    _ErrorCondResolved_Type()
)
errorCondResolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondResolved.setStatus("current")
_ErrorCondResolvedTime_Type = DateAndTime
_ErrorCondResolvedTime_Object = MibTableColumn
errorCondResolvedTime = _ErrorCondResolvedTime_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 7),
    _ErrorCondResolvedTime_Type()
)
errorCondResolvedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondResolvedTime.setStatus("current")
_ErrorCondResolvedTimeStr_Type = DisplayString
_ErrorCondResolvedTimeStr_Object = MibTableColumn
errorCondResolvedTimeStr = _ErrorCondResolvedTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 8),
    _ErrorCondResolvedTimeStr_Type()
)
errorCondResolvedTimeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondResolvedTimeStr.setStatus("current")


class _ErrorCondEncId_Type(DisplayString):
    """Custom type errorCondEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondEncId_Type.__name__ = "DisplayString"
_ErrorCondEncId_Object = MibTableColumn
errorCondEncId = _ErrorCondEncId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 9),
    _ErrorCondEncId_Type()
)
errorCondEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondEncId.setStatus("current")


class _ErrorCondPortId_Type(DisplayString):
    """Custom type errorCondPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondPortId_Type.__name__ = "DisplayString"
_ErrorCondPortId_Object = MibTableColumn
errorCondPortId = _ErrorCondPortId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 10),
    _ErrorCondPortId_Type()
)
errorCondPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondPortId.setStatus("current")


class _ErrorCondSensorId_Type(DisplayString):
    """Custom type errorCondSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondSensorId_Type.__name__ = "DisplayString"
_ErrorCondSensorId_Object = MibTableColumn
errorCondSensorId = _ErrorCondSensorId_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 5, 1, 1, 11),
    _ErrorCondSensorId_Type()
)
errorCondSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondSensorId.setStatus("current")
_NetBotzV2Traps_ObjectIdentity = ObjectIdentity
netBotzV2Traps = _NetBotzV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10)
)
_NetBotzV2GenericTraps_ObjectIdentity = ObjectIdentity
netBotzV2GenericTraps = _NetBotzV2GenericTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 1)
)
_NetBotzV2SensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2SensorTraps = _NetBotzV2SensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2)
)
_NetBotzV2TempSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2TempSensorTraps = _NetBotzV2TempSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1)
)
_NetBotzV2HumiditySensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2HumiditySensorTraps = _NetBotzV2HumiditySensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2)
)
_NetBotzV2DewPointSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2DewPointSensorTraps = _NetBotzV2DewPointSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3)
)
_NetBotzV2AirFlowSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2AirFlowSensorTraps = _NetBotzV2AirFlowSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4)
)
_NetBotzV2AudioSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2AudioSensorTraps = _NetBotzV2AudioSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5)
)
_NetBotzV2AmpDetectSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2AmpDetectSensorTraps = _NetBotzV2AmpDetectSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6)
)
_NetBotzV2DryContactSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2DryContactSensorTraps = _NetBotzV2DryContactSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 7)
)
_NetBotzV2CameraMotionSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2CameraMotionSensorTraps = _NetBotzV2CameraMotionSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 8)
)
_NetBotzV2DoorSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2DoorSensorTraps = _NetBotzV2DoorSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 9)
)
_NetBotzV2MicPlugSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2MicPlugSensorTraps = _NetBotzV2MicPlugSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 10)
)
_NetBotzV2SpeakerPlugSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2SpeakerPlugSensorTraps = _NetBotzV2SpeakerPlugSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 11)
)
_NetBotzV2TVSignalSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2TVSignalSensorTraps = _NetBotzV2TVSignalSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 12)
)
_NetBotzV2GPSPositionSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2GPSPositionSensorTraps = _NetBotzV2GPSPositionSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13)
)
_NetBotzV2GPSMovementSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2GPSMovementSensorTraps = _NetBotzV2GPSMovementSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14)
)
_NetBotzV2GPSStatusSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2GPSStatusSensorTraps = _NetBotzV2GPSStatusSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 15)
)
_NetBotzV2WirelessStatusSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2WirelessStatusSensorTraps = _NetBotzV2WirelessStatusSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 22)
)
_NetBotzV2PacketDropSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2PacketDropSensorTraps = _NetBotzV2PacketDropSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23)
)
_NetBotzV2SNMPCrawlerSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2SNMPCrawlerSensorTraps = _NetBotzV2SNMPCrawlerSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24)
)
_NetBotzV2PlugModuleStatusSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2PlugModuleStatusSensorTraps = _NetBotzV2PlugModuleStatusSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 25)
)
_NetBotzV2OutputControlSensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2OutputControlSensorTraps = _NetBotzV2OutputControlSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 26)
)
_NetBotzV2MultiRAESensorTraps_ObjectIdentity = ObjectIdentity
netBotzV2MultiRAESensorTraps = _NetBotzV2MultiRAESensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27)
)
_NetBotzV2MultiRAESensorStatusTraps_ObjectIdentity = ObjectIdentity
netBotzV2MultiRAESensorStatusTraps = _NetBotzV2MultiRAESensorStatusTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 28)
)
_NetBotzV2MultiRAEDeviceStatusTraps_ObjectIdentity = ObjectIdentity
netBotzV2MultiRAEDeviceStatusTraps = _NetBotzV2MultiRAEDeviceStatusTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 29)
)
_NetBotzV2PodTraps_ObjectIdentity = ObjectIdentity
netBotzV2PodTraps = _NetBotzV2PodTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3)
)
_NetBotzV2BasePodTraps_ObjectIdentity = ObjectIdentity
netBotzV2BasePodTraps = _NetBotzV2BasePodTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 1)
)
_NetBotzV2SensorPodTraps_ObjectIdentity = ObjectIdentity
netBotzV2SensorPodTraps = _NetBotzV2SensorPodTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 2)
)
_NetBotzV2CameraPodTraps_ObjectIdentity = ObjectIdentity
netBotzV2CameraPodTraps = _NetBotzV2CameraPodTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 3)
)
_NetBotzV2PortTraps_ObjectIdentity = ObjectIdentity
netBotzV2PortTraps = _NetBotzV2PortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 4)
)
_NetBotzV2TrapParms_ObjectIdentity = ObjectIdentity
netBotzV2TrapParms = _NetBotzV2TrapParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11)
)


class _NetBotzV2TrapErrorID_Type(DisplayString):
    """Custom type netBotzV2TrapErrorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzV2TrapErrorID_Type.__name__ = "DisplayString"
_NetBotzV2TrapErrorID_Object = MibScalar
netBotzV2TrapErrorID = _NetBotzV2TrapErrorID_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 1),
    _NetBotzV2TrapErrorID_Type()
)
netBotzV2TrapErrorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapErrorID.setStatus("current")


class _NetBotzV2TrapErrorType_Type(DisplayString):
    """Custom type netBotzV2TrapErrorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzV2TrapErrorType_Type.__name__ = "DisplayString"
_NetBotzV2TrapErrorType_Object = MibScalar
netBotzV2TrapErrorType = _NetBotzV2TrapErrorType_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 2),
    _NetBotzV2TrapErrorType_Type()
)
netBotzV2TrapErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapErrorType.setStatus("current")
_NetBotzV2TrapErrorTypeLabel_Type = DisplayString
_NetBotzV2TrapErrorTypeLabel_Object = MibScalar
netBotzV2TrapErrorTypeLabel = _NetBotzV2TrapErrorTypeLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 3),
    _NetBotzV2TrapErrorTypeLabel_Type()
)
netBotzV2TrapErrorTypeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapErrorTypeLabel.setStatus("current")


class _NetBotzV2TrapSensorID_Type(DisplayString):
    """Custom type netBotzV2TrapSensorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzV2TrapSensorID_Type.__name__ = "DisplayString"
_NetBotzV2TrapSensorID_Object = MibScalar
netBotzV2TrapSensorID = _NetBotzV2TrapSensorID_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 4),
    _NetBotzV2TrapSensorID_Type()
)
netBotzV2TrapSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapSensorID.setStatus("current")
_NetBotzV2TrapSensorLabel_Type = DisplayString
_NetBotzV2TrapSensorLabel_Object = MibScalar
netBotzV2TrapSensorLabel = _NetBotzV2TrapSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 5),
    _NetBotzV2TrapSensorLabel_Type()
)
netBotzV2TrapSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapSensorLabel.setStatus("current")


class _NetBotzV2TrapPodID_Type(DisplayString):
    """Custom type netBotzV2TrapPodID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzV2TrapPodID_Type.__name__ = "DisplayString"
_NetBotzV2TrapPodID_Object = MibScalar
netBotzV2TrapPodID = _NetBotzV2TrapPodID_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 6),
    _NetBotzV2TrapPodID_Type()
)
netBotzV2TrapPodID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapPodID.setStatus("current")
_NetBotzV2TrapPodLabel_Type = DisplayString
_NetBotzV2TrapPodLabel_Object = MibScalar
netBotzV2TrapPodLabel = _NetBotzV2TrapPodLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 7),
    _NetBotzV2TrapPodLabel_Type()
)
netBotzV2TrapPodLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapPodLabel.setStatus("current")


class _NetBotzV2TrapPortID_Type(DisplayString):
    """Custom type netBotzV2TrapPortID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzV2TrapPortID_Type.__name__ = "DisplayString"
_NetBotzV2TrapPortID_Object = MibScalar
netBotzV2TrapPortID = _NetBotzV2TrapPortID_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 8),
    _NetBotzV2TrapPortID_Type()
)
netBotzV2TrapPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapPortID.setStatus("current")
_NetBotzV2TrapPortLabel_Type = DisplayString
_NetBotzV2TrapPortLabel_Object = MibScalar
netBotzV2TrapPortLabel = _NetBotzV2TrapPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 9),
    _NetBotzV2TrapPortLabel_Type()
)
netBotzV2TrapPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapPortLabel.setStatus("current")
_NetBotzV2TrapStartTime_Type = Integer32
_NetBotzV2TrapStartTime_Object = MibScalar
netBotzV2TrapStartTime = _NetBotzV2TrapStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 10),
    _NetBotzV2TrapStartTime_Type()
)
netBotzV2TrapStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapStartTime.setStatus("current")
_NetBotzV2TrapNotifyTime_Type = Integer32
_NetBotzV2TrapNotifyTime_Object = MibScalar
netBotzV2TrapNotifyTime = _NetBotzV2TrapNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 11),
    _NetBotzV2TrapNotifyTime_Type()
)
netBotzV2TrapNotifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapNotifyTime.setStatus("current")
_NetBotzV2TrapResolveTime_Type = Integer32
_NetBotzV2TrapResolveTime_Object = MibScalar
netBotzV2TrapResolveTime = _NetBotzV2TrapResolveTime_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 12),
    _NetBotzV2TrapResolveTime_Type()
)
netBotzV2TrapResolveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapResolveTime.setStatus("current")


class _NetBotzV2TrapSeverity_Type(Integer32):
    """Custom type netBotzV2TrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("error", 2),
          ("failure", 4),
          ("information", 0),
          ("warning", 1))
    )


_NetBotzV2TrapSeverity_Type.__name__ = "Integer32"
_NetBotzV2TrapSeverity_Object = MibScalar
netBotzV2TrapSeverity = _NetBotzV2TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 13),
    _NetBotzV2TrapSeverity_Type()
)
netBotzV2TrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapSeverity.setStatus("current")
_NetBotzV2TrapSensorValue_Type = DisplayString
_NetBotzV2TrapSensorValue_Object = MibScalar
netBotzV2TrapSensorValue = _NetBotzV2TrapSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 14),
    _NetBotzV2TrapSensorValue_Type()
)
netBotzV2TrapSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapSensorValue.setStatus("current")
_NetBotzV2TrapSensorValueInt_Type = Integer32
_NetBotzV2TrapSensorValueInt_Object = MibScalar
netBotzV2TrapSensorValueInt = _NetBotzV2TrapSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 15),
    _NetBotzV2TrapSensorValueInt_Type()
)
netBotzV2TrapSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapSensorValueInt.setStatus("current")
_NetBotzV2TrapSensorValueFraction_Type = Integer32
_NetBotzV2TrapSensorValueFraction_Object = MibScalar
netBotzV2TrapSensorValueFraction = _NetBotzV2TrapSensorValueFraction_Object(
    (1, 3, 6, 1, 4, 1, 5528, 100, 11, 16),
    _NetBotzV2TrapSensorValueFraction_Type()
)
netBotzV2TrapSensorValueFraction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzV2TrapSensorValueFraction.setStatus("current")
_NetBotzV2Products_ObjectIdentity = ObjectIdentity
netBotzV2Products = _NetBotzV2Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20)
)
_NetBotzV2Botz_ObjectIdentity = ObjectIdentity
netBotzV2Botz = _NetBotzV2Botz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20, 10)
)
_NetBotzWallBotz500_ObjectIdentity = ObjectIdentity
netBotzWallBotz500 = _NetBotzWallBotz500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20, 10, 2000)
)
_NetBotz420Wall_ObjectIdentity = ObjectIdentity
netBotz420Wall = _NetBotz420Wall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20, 10, 2001)
)
_RaeSystemsAreaConnect500_ObjectIdentity = ObjectIdentity
raeSystemsAreaConnect500 = _RaeSystemsAreaConnect500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20, 10, 2002)
)
_NetBotz420Rack_ObjectIdentity = ObjectIdentity
netBotz420Rack = _NetBotz420Rack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20, 10, 2003)
)
_NetBotz320Wall_ObjectIdentity = ObjectIdentity
netBotz320Wall = _NetBotz320Wall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20, 10, 2004)
)
_NetBotz320Rack_ObjectIdentity = ObjectIdentity
netBotz320Rack = _NetBotz320Rack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20, 10, 2005)
)
_NetBotz420ERack_ObjectIdentity = ObjectIdentity
netBotz420ERack = _NetBotz420ERack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20, 10, 2006)
)
_NetBotz320ERack_ObjectIdentity = ObjectIdentity
netBotz320ERack = _NetBotz320ERack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 100, 20, 10, 2007)
)

# Managed Objects groups


# Notification objects

netBotzTempError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 1)
)
netBotzTempError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempError.setStatus(
        "current"
    )

netBotzTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 2)
)
netBotzTempTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooHigh.setStatus(
        "current"
    )

netBotzTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 3)
)
netBotzTempTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooLow.setStatus(
        "current"
    )

netBotzTempTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 4)
)
netBotzTempTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooHighTooLong.setStatus(
        "current"
    )

netBotzTempTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 5)
)
netBotzTempTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooLowTooLong.setStatus(
        "current"
    )

netBotzTempUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 6)
)
netBotzTempUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempUnplugged.setStatus(
        "current"
    )

netBotzTempIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 8)
)
netBotzTempIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzTempDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 9)
)
netBotzTempDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzTempErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 101)
)
netBotzTempErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempErrorRTN.setStatus(
        "current"
    )

netBotzTempTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 102)
)
netBotzTempTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooHighRTN.setStatus(
        "current"
    )

netBotzTempTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 103)
)
netBotzTempTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooLowRTN.setStatus(
        "current"
    )

netBotzTempTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 104)
)
netBotzTempTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzTempTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 105)
)
netBotzTempTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzTempReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 106)
)
netBotzTempReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempReplugged.setStatus(
        "current"
    )

netBotzTempNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 108)
)
netBotzTempNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzTempNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 1, 0, 109)
)
netBotzTempNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzHumidityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 1)
)
netBotzHumidityError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityError.setStatus(
        "current"
    )

netBotzHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 2)
)
netBotzHumidityTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooHigh.setStatus(
        "current"
    )

netBotzHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 3)
)
netBotzHumidityTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooLow.setStatus(
        "current"
    )

netBotzHumidityTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 4)
)
netBotzHumidityTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooHighTooLong.setStatus(
        "current"
    )

netBotzHumidityTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 5)
)
netBotzHumidityTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooLowTooLong.setStatus(
        "current"
    )

netBotzHumidityUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 6)
)
netBotzHumidityUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityUnplugged.setStatus(
        "current"
    )

netBotzHumidityIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 8)
)
netBotzHumidityIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzHumidityDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 9)
)
netBotzHumidityDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzHumidityErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 101)
)
netBotzHumidityErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityErrorRTN.setStatus(
        "current"
    )

netBotzHumidityTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 102)
)
netBotzHumidityTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooHighRTN.setStatus(
        "current"
    )

netBotzHumidityTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 103)
)
netBotzHumidityTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooLowRTN.setStatus(
        "current"
    )

netBotzHumidityTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 104)
)
netBotzHumidityTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzHumidityTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 105)
)
netBotzHumidityTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzHumidityReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 106)
)
netBotzHumidityReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityReplugged.setStatus(
        "current"
    )

netBotzHumidityNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 108)
)
netBotzHumidityNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzHumidityNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 2, 0, 109)
)
netBotzHumidityNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzDewPointError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 1)
)
netBotzDewPointError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointError.setStatus(
        "current"
    )

netBotzDewPointTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 2)
)
netBotzDewPointTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooHigh.setStatus(
        "current"
    )

netBotzDewPointTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 3)
)
netBotzDewPointTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooLow.setStatus(
        "current"
    )

netBotzDewPointTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 4)
)
netBotzDewPointTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooHighTooLong.setStatus(
        "current"
    )

netBotzDewPointTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 5)
)
netBotzDewPointTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooLowTooLong.setStatus(
        "current"
    )

netBotzDewPointUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 6)
)
netBotzDewPointUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointUnplugged.setStatus(
        "current"
    )

netBotzDewPointIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 8)
)
netBotzDewPointIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzDewPointDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 9)
)
netBotzDewPointDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzDewPointErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 101)
)
netBotzDewPointErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointErrorRTN.setStatus(
        "current"
    )

netBotzDewPointTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 102)
)
netBotzDewPointTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooHighRTN.setStatus(
        "current"
    )

netBotzDewPointTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 103)
)
netBotzDewPointTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooLowRTN.setStatus(
        "current"
    )

netBotzDewPointTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 104)
)
netBotzDewPointTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzDewPointTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 105)
)
netBotzDewPointTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzDewPointReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 106)
)
netBotzDewPointReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointReplugged.setStatus(
        "current"
    )

netBotzDewPointNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 108)
)
netBotzDewPointNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzDewPointNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 3, 0, 109)
)
netBotzDewPointNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzAirFlowError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 1)
)
netBotzAirFlowError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowError.setStatus(
        "current"
    )

netBotzAirFlowTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 2)
)
netBotzAirFlowTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooHigh.setStatus(
        "current"
    )

netBotzAirFlowTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 3)
)
netBotzAirFlowTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooLow.setStatus(
        "current"
    )

netBotzAirFlowTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 4)
)
netBotzAirFlowTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooHighTooLong.setStatus(
        "current"
    )

netBotzAirFlowTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 5)
)
netBotzAirFlowTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooLowTooLong.setStatus(
        "current"
    )

netBotzAirFlowUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 6)
)
netBotzAirFlowUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowUnplugged.setStatus(
        "current"
    )

netBotzAirFlowIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 8)
)
netBotzAirFlowIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzAirFlowDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 9)
)
netBotzAirFlowDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzAirFlowErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 101)
)
netBotzAirFlowErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowErrorRTN.setStatus(
        "current"
    )

netBotzAirFlowTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 102)
)
netBotzAirFlowTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooHighRTN.setStatus(
        "current"
    )

netBotzAirFlowTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 103)
)
netBotzAirFlowTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooLowRTN.setStatus(
        "current"
    )

netBotzAirFlowTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 104)
)
netBotzAirFlowTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzAirFlowTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 105)
)
netBotzAirFlowTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzAirFlowReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 106)
)
netBotzAirFlowReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowReplugged.setStatus(
        "current"
    )

netBotzAirFlowNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 108)
)
netBotzAirFlowNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzAirFlowNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 4, 0, 109)
)
netBotzAirFlowNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzAudioError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 1)
)
netBotzAudioError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioError.setStatus(
        "current"
    )

netBotzAudioTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 2)
)
netBotzAudioTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioTooHigh.setStatus(
        "current"
    )

netBotzAudioTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 3)
)
netBotzAudioTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioTooLow.setStatus(
        "current"
    )

netBotzAudioTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 4)
)
netBotzAudioTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioTooHighTooLong.setStatus(
        "current"
    )

netBotzAudioTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 5)
)
netBotzAudioTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioTooLowTooLong.setStatus(
        "current"
    )

netBotzAudioUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 6)
)
netBotzAudioUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioUnplugged.setStatus(
        "current"
    )

netBotzAudioIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 8)
)
netBotzAudioIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzAudioDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 9)
)
netBotzAudioDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzAudioErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 101)
)
netBotzAudioErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioErrorRTN.setStatus(
        "current"
    )

netBotzAudioTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 102)
)
netBotzAudioTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioTooHighRTN.setStatus(
        "current"
    )

netBotzAudioTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 103)
)
netBotzAudioTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioTooLowRTN.setStatus(
        "current"
    )

netBotzAudioTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 104)
)
netBotzAudioTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzAudioTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 105)
)
netBotzAudioTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzAudioReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 106)
)
netBotzAudioReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioReplugged.setStatus(
        "current"
    )

netBotzAudioNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 108)
)
netBotzAudioNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzAudioNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 5, 0, 109)
)
netBotzAudioNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAudioNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzAmpDetectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 1)
)
netBotzAmpDetectError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectError.setStatus(
        "current"
    )

netBotzAmpDetectTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 2)
)
netBotzAmpDetectTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooHigh.setStatus(
        "current"
    )

netBotzAmpDetectTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 3)
)
netBotzAmpDetectTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooLow.setStatus(
        "current"
    )

netBotzAmpDetectTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 4)
)
netBotzAmpDetectTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooHighTooLong.setStatus(
        "current"
    )

netBotzAmpDetectTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 5)
)
netBotzAmpDetectTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooLowTooLong.setStatus(
        "current"
    )

netBotzAmpDetectUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 6)
)
netBotzAmpDetectUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectUnplugged.setStatus(
        "current"
    )

netBotzAmpDetectIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 8)
)
netBotzAmpDetectIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzAmpDetectDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 9)
)
netBotzAmpDetectDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzAmpDetectErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 101)
)
netBotzAmpDetectErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectErrorRTN.setStatus(
        "current"
    )

netBotzAmpDetectTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 102)
)
netBotzAmpDetectTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooHighRTN.setStatus(
        "current"
    )

netBotzAmpDetectTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 103)
)
netBotzAmpDetectTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooLowRTN.setStatus(
        "current"
    )

netBotzAmpDetectTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 104)
)
netBotzAmpDetectTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzAmpDetectTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 105)
)
netBotzAmpDetectTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzAmpDetectReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 106)
)
netBotzAmpDetectReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectReplugged.setStatus(
        "current"
    )

netBotzAmpDetectNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 108)
)
netBotzAmpDetectNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzAmpDetectNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 6, 0, 109)
)
netBotzAmpDetectNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzDryContactError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 7, 0, 1)
)
netBotzDryContactError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactError.setStatus(
        "current"
    )

netBotzDryContactUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 7, 0, 6)
)
netBotzDryContactUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactUnplugged.setStatus(
        "current"
    )

netBotzDryContactValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 7, 0, 10)
)
netBotzDryContactValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactValueError.setStatus(
        "current"
    )

netBotzDryContactErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 7, 0, 101)
)
netBotzDryContactErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactErrorRTN.setStatus(
        "current"
    )

netBotzDryContactReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 7, 0, 106)
)
netBotzDryContactReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactReplugged.setStatus(
        "current"
    )

netBotzDryContactValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 7, 0, 110)
)
netBotzDryContactValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactValueErrorRTN.setStatus(
        "current"
    )

netBotzCameraMotionSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 8, 0, 1)
)
netBotzCameraMotionSensorError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorError.setStatus(
        "current"
    )

netBotzCameraMotionSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 8, 0, 6)
)
netBotzCameraMotionSensorUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorUnplugged.setStatus(
        "current"
    )

netBotzCameraMotionSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 8, 0, 10)
)
netBotzCameraMotionSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorValueError.setStatus(
        "current"
    )

netBotzCameraMotionSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 8, 0, 101)
)
netBotzCameraMotionSensorErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorErrorRTN.setStatus(
        "current"
    )

netBotzCameraMotionSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 8, 0, 106)
)
netBotzCameraMotionSensorReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorReplugged.setStatus(
        "current"
    )

netBotzCameraMotionSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 8, 0, 110)
)
netBotzCameraMotionSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzDoorSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 9, 0, 1)
)
netBotzDoorSensorError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorError.setStatus(
        "current"
    )

netBotzDoorSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 9, 0, 6)
)
netBotzDoorSensorUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorUnplugged.setStatus(
        "current"
    )

netBotzDoorSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 9, 0, 10)
)
netBotzDoorSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorValueError.setStatus(
        "current"
    )

netBotzDoorSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 9, 0, 101)
)
netBotzDoorSensorErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorErrorRTN.setStatus(
        "current"
    )

netBotzDoorSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 9, 0, 106)
)
netBotzDoorSensorReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorReplugged.setStatus(
        "current"
    )

netBotzDoorSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 9, 0, 110)
)
netBotzDoorSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzMicPlugSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 10, 0, 1)
)
netBotzMicPlugSensorError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMicPlugSensorError.setStatus(
        "current"
    )

netBotzMicPlugSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 10, 0, 6)
)
netBotzMicPlugSensorUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMicPlugSensorUnplugged.setStatus(
        "current"
    )

netBotzMicPlugSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 10, 0, 10)
)
netBotzMicPlugSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMicPlugSensorValueError.setStatus(
        "current"
    )

netBotzMicPlugSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 10, 0, 101)
)
netBotzMicPlugSensorErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMicPlugSensorErrorRTN.setStatus(
        "current"
    )

netBotzMicPlugSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 10, 0, 106)
)
netBotzMicPlugSensorReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMicPlugSensorReplugged.setStatus(
        "current"
    )

netBotzMicPlugSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 10, 0, 110)
)
netBotzMicPlugSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMicPlugSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzSpeakerPlugSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 11, 0, 1)
)
netBotzSpeakerPlugSensorError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpeakerPlugSensorError.setStatus(
        "current"
    )

netBotzSpeakerPlugSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 11, 0, 6)
)
netBotzSpeakerPlugSensorUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpeakerPlugSensorUnplugged.setStatus(
        "current"
    )

netBotzSpeakerPlugSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 11, 0, 10)
)
netBotzSpeakerPlugSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpeakerPlugSensorValueError.setStatus(
        "current"
    )

netBotzSpeakerPlugSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 11, 0, 101)
)
netBotzSpeakerPlugSensorErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpeakerPlugSensorErrorRTN.setStatus(
        "current"
    )

netBotzSpeakerPlugSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 11, 0, 106)
)
netBotzSpeakerPlugSensorReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpeakerPlugSensorReplugged.setStatus(
        "current"
    )

netBotzSpeakerPlugSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 11, 0, 110)
)
netBotzSpeakerPlugSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpeakerPlugSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzTVSignalSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 12, 0, 1)
)
netBotzTVSignalSensorError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTVSignalSensorError.setStatus(
        "current"
    )

netBotzTVSignalSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 12, 0, 6)
)
netBotzTVSignalSensorUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTVSignalSensorUnplugged.setStatus(
        "current"
    )

netBotzTVSignalSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 12, 0, 10)
)
netBotzTVSignalSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTVSignalSensorValueError.setStatus(
        "current"
    )

netBotzTVSignalSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 12, 0, 101)
)
netBotzTVSignalSensorErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTVSignalSensorErrorRTN.setStatus(
        "current"
    )

netBotzTVSignalSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 12, 0, 106)
)
netBotzTVSignalSensorReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTVSignalSensorReplugged.setStatus(
        "current"
    )

netBotzTVSignalSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 12, 0, 110)
)
netBotzTVSignalSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTVSignalSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzGPSPositionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 1)
)
netBotzGPSPositionError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionError.setStatus(
        "current"
    )

netBotzGPSPositionTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 2)
)
netBotzGPSPositionTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionTooHigh.setStatus(
        "current"
    )

netBotzGPSPositionTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 3)
)
netBotzGPSPositionTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionTooLow.setStatus(
        "current"
    )

netBotzGPSPositionTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 4)
)
netBotzGPSPositionTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionTooHighTooLong.setStatus(
        "current"
    )

netBotzGPSPositionTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 5)
)
netBotzGPSPositionTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionTooLowTooLong.setStatus(
        "current"
    )

netBotzGPSPositionUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 6)
)
netBotzGPSPositionUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionUnplugged.setStatus(
        "current"
    )

netBotzGPSPositionIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 8)
)
netBotzGPSPositionIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzGPSPositionDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 9)
)
netBotzGPSPositionDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzGPSPositionErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 101)
)
netBotzGPSPositionErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionErrorRTN.setStatus(
        "current"
    )

netBotzGPSPositionTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 102)
)
netBotzGPSPositionTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionTooHighRTN.setStatus(
        "current"
    )

netBotzGPSPositionTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 103)
)
netBotzGPSPositionTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionTooLowRTN.setStatus(
        "current"
    )

netBotzGPSPositionTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 104)
)
netBotzGPSPositionTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzGPSPositionTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 105)
)
netBotzGPSPositionTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzGPSPositionReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 106)
)
netBotzGPSPositionReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionReplugged.setStatus(
        "current"
    )

netBotzGPSPositionNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 108)
)
netBotzGPSPositionNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzGPSPositionNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 13, 0, 109)
)
netBotzGPSPositionNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSPositionNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzGPSMovementError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 1)
)
netBotzGPSMovementError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementError.setStatus(
        "current"
    )

netBotzGPSMovementTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 2)
)
netBotzGPSMovementTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementTooHigh.setStatus(
        "current"
    )

netBotzGPSMovementTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 3)
)
netBotzGPSMovementTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementTooLow.setStatus(
        "current"
    )

netBotzGPSMovementTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 4)
)
netBotzGPSMovementTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementTooHighTooLong.setStatus(
        "current"
    )

netBotzGPSMovementTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 5)
)
netBotzGPSMovementTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementTooLowTooLong.setStatus(
        "current"
    )

netBotzGPSMovementUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 6)
)
netBotzGPSMovementUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementUnplugged.setStatus(
        "current"
    )

netBotzGPSMovementIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 8)
)
netBotzGPSMovementIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzGPSMovementDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 9)
)
netBotzGPSMovementDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzGPSMovementErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 101)
)
netBotzGPSMovementErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementErrorRTN.setStatus(
        "current"
    )

netBotzGPSMovementTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 102)
)
netBotzGPSMovementTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementTooHighRTN.setStatus(
        "current"
    )

netBotzGPSMovementTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 103)
)
netBotzGPSMovementTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementTooLowRTN.setStatus(
        "current"
    )

netBotzGPSMovementTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 104)
)
netBotzGPSMovementTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzGPSMovementTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 105)
)
netBotzGPSMovementTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzGPSMovementReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 106)
)
netBotzGPSMovementReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementReplugged.setStatus(
        "current"
    )

netBotzGPSMovementNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 108)
)
netBotzGPSMovementNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzGPSMovementNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 14, 0, 109)
)
netBotzGPSMovementNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSMovementNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzGPSStatusSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 15, 0, 1)
)
netBotzGPSStatusSensorError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSStatusSensorError.setStatus(
        "current"
    )

netBotzGPSStatusSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 15, 0, 6)
)
netBotzGPSStatusSensorUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSStatusSensorUnplugged.setStatus(
        "current"
    )

netBotzGPSStatusSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 15, 0, 10)
)
netBotzGPSStatusSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSStatusSensorValueError.setStatus(
        "current"
    )

netBotzGPSStatusSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 15, 0, 101)
)
netBotzGPSStatusSensorErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSStatusSensorErrorRTN.setStatus(
        "current"
    )

netBotzGPSStatusSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 15, 0, 106)
)
netBotzGPSStatusSensorReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSStatusSensorReplugged.setStatus(
        "current"
    )

netBotzGPSStatusSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 15, 0, 110)
)
netBotzGPSStatusSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzGPSStatusSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzWirelessStatusSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 22, 0, 1)
)
netBotzWirelessStatusSensorError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorError.setStatus(
        "current"
    )

netBotzWirelessStatusSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 22, 0, 6)
)
netBotzWirelessStatusSensorUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorUnplugged.setStatus(
        "current"
    )

netBotzWirelessStatusSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 22, 0, 10)
)
netBotzWirelessStatusSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorValueError.setStatus(
        "current"
    )

netBotzWirelessStatusSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 22, 0, 101)
)
netBotzWirelessStatusSensorErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorErrorRTN.setStatus(
        "current"
    )

netBotzWirelessStatusSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 22, 0, 106)
)
netBotzWirelessStatusSensorReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorReplugged.setStatus(
        "current"
    )

netBotzWirelessStatusSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 22, 0, 110)
)
netBotzWirelessStatusSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzPacketDropError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 1)
)
netBotzPacketDropError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropError.setStatus(
        "current"
    )

netBotzPacketDropTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 2)
)
netBotzPacketDropTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropTooHigh.setStatus(
        "current"
    )

netBotzPacketDropTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 3)
)
netBotzPacketDropTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropTooLow.setStatus(
        "current"
    )

netBotzPacketDropTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 4)
)
netBotzPacketDropTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropTooHighTooLong.setStatus(
        "current"
    )

netBotzPacketDropTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 5)
)
netBotzPacketDropTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropTooLowTooLong.setStatus(
        "current"
    )

netBotzPacketDropUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 6)
)
netBotzPacketDropUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropUnplugged.setStatus(
        "current"
    )

netBotzPacketDropIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 8)
)
netBotzPacketDropIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzPacketDropDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 9)
)
netBotzPacketDropDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzPacketDropErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 101)
)
netBotzPacketDropErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropErrorRTN.setStatus(
        "current"
    )

netBotzPacketDropTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 102)
)
netBotzPacketDropTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropTooHighRTN.setStatus(
        "current"
    )

netBotzPacketDropTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 103)
)
netBotzPacketDropTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropTooLowRTN.setStatus(
        "current"
    )

netBotzPacketDropTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 104)
)
netBotzPacketDropTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzPacketDropTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 105)
)
netBotzPacketDropTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzPacketDropReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 106)
)
netBotzPacketDropReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropReplugged.setStatus(
        "current"
    )

netBotzPacketDropNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 108)
)
netBotzPacketDropNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzPacketDropNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 23, 0, 109)
)
netBotzPacketDropNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPacketDropNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzSNMPCrawlerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 1)
)
netBotzSNMPCrawlerError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerError.setStatus(
        "current"
    )

netBotzSNMPCrawlerTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 2)
)
netBotzSNMPCrawlerTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerTooHigh.setStatus(
        "current"
    )

netBotzSNMPCrawlerTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 3)
)
netBotzSNMPCrawlerTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerTooLow.setStatus(
        "current"
    )

netBotzSNMPCrawlerTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 4)
)
netBotzSNMPCrawlerTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerTooHighTooLong.setStatus(
        "current"
    )

netBotzSNMPCrawlerTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 5)
)
netBotzSNMPCrawlerTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerTooLowTooLong.setStatus(
        "current"
    )

netBotzSNMPCrawlerUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 6)
)
netBotzSNMPCrawlerUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerUnplugged.setStatus(
        "current"
    )

netBotzSNMPCrawlerIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 8)
)
netBotzSNMPCrawlerIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzSNMPCrawlerDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 9)
)
netBotzSNMPCrawlerDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzSNMPCrawlerSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 10)
)
netBotzSNMPCrawlerSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerSensorValueError.setStatus(
        "current"
    )

netBotzSNMPCrawlerErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 101)
)
netBotzSNMPCrawlerErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerErrorRTN.setStatus(
        "current"
    )

netBotzSNMPCrawlerTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 102)
)
netBotzSNMPCrawlerTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerTooHighRTN.setStatus(
        "current"
    )

netBotzSNMPCrawlerTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 103)
)
netBotzSNMPCrawlerTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerTooLowRTN.setStatus(
        "current"
    )

netBotzSNMPCrawlerTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 104)
)
netBotzSNMPCrawlerTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzSNMPCrawlerTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 105)
)
netBotzSNMPCrawlerTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzSNMPCrawlerReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 106)
)
netBotzSNMPCrawlerReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerReplugged.setStatus(
        "current"
    )

netBotzSNMPCrawlerNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 108)
)
netBotzSNMPCrawlerNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzSNMPCrawlerNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 109)
)
netBotzSNMPCrawlerNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzSNMPCrawlerSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 24, 0, 110)
)
netBotzSNMPCrawlerSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSNMPCrawlerSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzOutputControlSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 26, 0, 1)
)
netBotzOutputControlSensorError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorError.setStatus(
        "current"
    )

netBotzOutputControlSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 26, 0, 6)
)
netBotzOutputControlSensorUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorUnplugged.setStatus(
        "current"
    )

netBotzOutputControlSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 26, 0, 10)
)
netBotzOutputControlSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorValueError.setStatus(
        "current"
    )

netBotzOutputControlSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 26, 0, 101)
)
netBotzOutputControlSensorErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorErrorRTN.setStatus(
        "current"
    )

netBotzOutputControlSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 26, 0, 106)
)
netBotzOutputControlSensorReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorReplugged.setStatus(
        "current"
    )

netBotzOutputControlSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 26, 0, 110)
)
netBotzOutputControlSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzMultiRAESensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 1)
)
netBotzMultiRAESensorError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorError.setStatus(
        "current"
    )

netBotzMultiRAESensorTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 2)
)
netBotzMultiRAESensorTooHigh.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorTooHigh.setStatus(
        "current"
    )

netBotzMultiRAESensorTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 3)
)
netBotzMultiRAESensorTooLow.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorTooLow.setStatus(
        "current"
    )

netBotzMultiRAESensorTooHighTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 4)
)
netBotzMultiRAESensorTooHighTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorTooHighTooLong.setStatus(
        "current"
    )

netBotzMultiRAESensorTooLowTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 5)
)
netBotzMultiRAESensorTooLowTooLong.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorTooLowTooLong.setStatus(
        "current"
    )

netBotzMultiRAESensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 6)
)
netBotzMultiRAESensorUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorUnplugged.setStatus(
        "current"
    )

netBotzMultiRAESensorIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 8)
)
netBotzMultiRAESensorIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzMultiRAESensorDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 9)
)
netBotzMultiRAESensorDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzMultiRAESensorSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 10)
)
netBotzMultiRAESensorSensorValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorSensorValueError.setStatus(
        "current"
    )

netBotzMultiRAESensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 101)
)
netBotzMultiRAESensorErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorErrorRTN.setStatus(
        "current"
    )

netBotzMultiRAESensorTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 102)
)
netBotzMultiRAESensorTooHighRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorTooHighRTN.setStatus(
        "current"
    )

netBotzMultiRAESensorTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 103)
)
netBotzMultiRAESensorTooLowRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorTooLowRTN.setStatus(
        "current"
    )

netBotzMultiRAESensorTooHighTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 104)
)
netBotzMultiRAESensorTooHighTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorTooHighTooLongRTN.setStatus(
        "current"
    )

netBotzMultiRAESensorTooLowForTooLongRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 105)
)
netBotzMultiRAESensorTooLowForTooLongRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorTooLowForTooLongRTN.setStatus(
        "current"
    )

netBotzMultiRAESensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 106)
)
netBotzMultiRAESensorReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorReplugged.setStatus(
        "current"
    )

netBotzMultiRAESensorNotIncreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 108)
)
netBotzMultiRAESensorNotIncreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorNotIncreasingTooQuickly.setStatus(
        "current"
    )

netBotzMultiRAESensorNotDecreasingTooQuickly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 109)
)
netBotzMultiRAESensorNotDecreasingTooQuickly.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorNotDecreasingTooQuickly.setStatus(
        "current"
    )

netBotzMultiRAESensorSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 27, 0, 110)
)
netBotzMultiRAESensorSensorValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzMultiRAESensorStatusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 28, 0, 1)
)
netBotzMultiRAESensorStatusError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorStatusError.setStatus(
        "current"
    )

netBotzMultiRAESensorStatusUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 28, 0, 6)
)
netBotzMultiRAESensorStatusUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorStatusUnplugged.setStatus(
        "current"
    )

netBotzMultiRAESensorStatusValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 28, 0, 10)
)
netBotzMultiRAESensorStatusValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorStatusValueError.setStatus(
        "current"
    )

netBotzMultiRAESensorStatusErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 28, 0, 101)
)
netBotzMultiRAESensorStatusErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorStatusErrorRTN.setStatus(
        "current"
    )

netBotzMultiRAESensorStatusReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 28, 0, 106)
)
netBotzMultiRAESensorStatusReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorStatusReplugged.setStatus(
        "current"
    )

netBotzMultiRAESensorStatusValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 28, 0, 110)
)
netBotzMultiRAESensorStatusValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAESensorStatusValueErrorRTN.setStatus(
        "current"
    )

netBotzMultiRAEDeviceStatusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 29, 0, 1)
)
netBotzMultiRAEDeviceStatusError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAEDeviceStatusError.setStatus(
        "current"
    )

netBotzMultiRAEDeviceStatusUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 29, 0, 6)
)
netBotzMultiRAEDeviceStatusUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAEDeviceStatusUnplugged.setStatus(
        "current"
    )

netBotzMultiRAEDeviceStatusValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 29, 0, 10)
)
netBotzMultiRAEDeviceStatusValueError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAEDeviceStatusValueError.setStatus(
        "current"
    )

netBotzMultiRAEDeviceStatusErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 29, 0, 101)
)
netBotzMultiRAEDeviceStatusErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAEDeviceStatusErrorRTN.setStatus(
        "current"
    )

netBotzMultiRAEDeviceStatusReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 29, 0, 106)
)
netBotzMultiRAEDeviceStatusReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAEDeviceStatusReplugged.setStatus(
        "current"
    )

netBotzMultiRAEDeviceStatusValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 2, 29, 0, 110)
)
netBotzMultiRAEDeviceStatusValueErrorRTN.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzMultiRAEDeviceStatusValueErrorRTN.setStatus(
        "current"
    )

netBotzPodUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 0, 7)
)
netBotzPodUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPodUnplugged.setStatus(
        "current"
    )

netBotzLogonError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 0, 11)
)
netBotzLogonError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLogonError.setStatus(
        "current"
    )

netBotzDriveNotFoundError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 0, 12)
)
netBotzDriveNotFoundError.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDriveNotFoundError.setStatus(
        "current"
    )

netBotzPodReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 0, 107)
)
netBotzPodReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzPodReplugged.setStatus(
        "current"
    )

netBotzLogonErrorResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 0, 111)
)
netBotzLogonErrorResolved.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLogonErrorResolved.setStatus(
        "current"
    )

netBotzDriveNotFoundErrorResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 0, 112)
)
netBotzDriveNotFoundErrorResolved.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDriveNotFoundErrorResolved.setStatus(
        "current"
    )

netBotzSensorPodUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 2, 0, 7)
)
netBotzSensorPodUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSensorPodUnplugged.setStatus(
        "current"
    )

netBotzSensorPodReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 2, 0, 107)
)
netBotzSensorPodReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSensorPodReplugged.setStatus(
        "current"
    )

netBotzCameraPodUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 3, 0, 7)
)
netBotzCameraPodUnplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraPodUnplugged.setStatus(
        "current"
    )

netBotzCameraPodReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 100, 10, 3, 3, 0, 107)
)
netBotzCameraPodReplugged.setObjects(
      *(("NETBOTZV2-MIB", "netBotzV2TrapErrorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorType"),
        ("NETBOTZV2-MIB", "netBotzV2TrapErrorTypeLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPodLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortID"),
        ("NETBOTZV2-MIB", "netBotzV2TrapPortLabel"),
        ("NETBOTZV2-MIB", "netBotzV2TrapStartTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapNotifyTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapResolveTime"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSeverity"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValue"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueInt"),
        ("NETBOTZV2-MIB", "netBotzV2TrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraPodReplugged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETBOTZV2-MIB",
    **{"OperStatus": OperStatus,
       "ErrorStatus": ErrorStatus,
       "BoolValue": BoolValue,
       "netBotz": netBotz,
       "netBotzV2": netBotzV2,
       "netBotz-V2": netBotz_V2,
       "netBotzEnclosures": netBotzEnclosures,
       "enclosureTable": enclosureTable,
       "enclosureEntry": enclosureEntry,
       "enclosureId": enclosureId,
       "enclosureStatus": enclosureStatus,
       "enclosureErrorStatus": enclosureErrorStatus,
       "enclosureLabel": enclosureLabel,
       "enclosureParentEncId": enclosureParentEncId,
       "enclosureDockedToEncId": enclosureDockedToEncId,
       "netBotzPorts": netBotzPorts,
       "dinPortTable": dinPortTable,
       "dinPortEntry": dinPortEntry,
       "dinPortId": dinPortId,
       "dinPortStatus": dinPortStatus,
       "dinPortLabel": dinPortLabel,
       "dinPortEncId": dinPortEncId,
       "dinPortSensorIdSuffix": dinPortSensorIdSuffix,
       "dinPortSupportsAverage": dinPortSupportsAverage,
       "dinPortSupportsRMS": dinPortSupportsRMS,
       "dinPortSupportsDryContact": dinPortSupportsDryContact,
       "otherPortTable": otherPortTable,
       "otherPortEntry": otherPortEntry,
       "otherPortId": otherPortId,
       "otherPortStatus": otherPortStatus,
       "otherPortLabel": otherPortLabel,
       "otherPortEncId": otherPortEncId,
       "netBotzSensors": netBotzSensors,
       "netBotzNumericSensors": netBotzNumericSensors,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorId": tempSensorId,
       "tempSensorValue": tempSensorValue,
       "tempSensorErrorStatus": tempSensorErrorStatus,
       "tempSensorLabel": tempSensorLabel,
       "tempSensorEncId": tempSensorEncId,
       "tempSensorPortId": tempSensorPortId,
       "tempSensorValueStr": tempSensorValueStr,
       "tempSensorValueInt": tempSensorValueInt,
       "tempSensorValueIntF": tempSensorValueIntF,
       "humiSensorTable": humiSensorTable,
       "humiSensorEntry": humiSensorEntry,
       "humiSensorId": humiSensorId,
       "humiSensorValue": humiSensorValue,
       "humiSensorErrorStatus": humiSensorErrorStatus,
       "humiSensorLabel": humiSensorLabel,
       "humiSensorEncId": humiSensorEncId,
       "humiSensorPortId": humiSensorPortId,
       "humiSensorValueStr": humiSensorValueStr,
       "humiSensorValueInt": humiSensorValueInt,
       "dewPointSensorTable": dewPointSensorTable,
       "dewPointSensorEntry": dewPointSensorEntry,
       "dewPointSensorId": dewPointSensorId,
       "dewPointSensorValue": dewPointSensorValue,
       "dewPointSensorErrorStatus": dewPointSensorErrorStatus,
       "dewPointSensorLabel": dewPointSensorLabel,
       "dewPointSensorEncId": dewPointSensorEncId,
       "dewPointSensorPortId": dewPointSensorPortId,
       "dewPointSensorValueStr": dewPointSensorValueStr,
       "dewPointSensorValueInt": dewPointSensorValueInt,
       "audioSensorTable": audioSensorTable,
       "audioSensorEntry": audioSensorEntry,
       "audioSensorId": audioSensorId,
       "audioSensorValue": audioSensorValue,
       "audioSensorErrorStatus": audioSensorErrorStatus,
       "audioSensorLabel": audioSensorLabel,
       "audioSensorEncId": audioSensorEncId,
       "audioSensorPortId": audioSensorPortId,
       "audioSensorValueStr": audioSensorValueStr,
       "audioSensorValueInt": audioSensorValueInt,
       "airFlowSensorTable": airFlowSensorTable,
       "airFlowSensorEntry": airFlowSensorEntry,
       "airFlowSensorId": airFlowSensorId,
       "airFlowSensorValue": airFlowSensorValue,
       "airFlowSensorErrorStatus": airFlowSensorErrorStatus,
       "airFlowSensorLabel": airFlowSensorLabel,
       "airFlowSensorEncId": airFlowSensorEncId,
       "airFlowSensorPortId": airFlowSensorPortId,
       "airFlowSensorValueStr": airFlowSensorValueStr,
       "airFlowSensorValueInt": airFlowSensorValueInt,
       "ampDetectSensorTable": ampDetectSensorTable,
       "ampDetectSensorEntry": ampDetectSensorEntry,
       "ampDetectSensorId": ampDetectSensorId,
       "ampDetectSensorValue": ampDetectSensorValue,
       "ampDetectSensorErrorStatus": ampDetectSensorErrorStatus,
       "ampDetectSensorLabel": ampDetectSensorLabel,
       "ampDetectSensorEncId": ampDetectSensorEncId,
       "ampDetectSensorPortId": ampDetectSensorPortId,
       "ampDetectSensorValueStr": ampDetectSensorValueStr,
       "ampDetectSensorValueInt": ampDetectSensorValueInt,
       "otherNumericSensorTable": otherNumericSensorTable,
       "otherNumericSensorEntry": otherNumericSensorEntry,
       "otherNumericSensorId": otherNumericSensorId,
       "otherNumericSensorValue": otherNumericSensorValue,
       "otherNumericSensorErrorStatus": otherNumericSensorErrorStatus,
       "otherNumericSensorLabel": otherNumericSensorLabel,
       "otherNumericSensorEncId": otherNumericSensorEncId,
       "otherNumericSensorPortId": otherNumericSensorPortId,
       "otherNumericSensorValueStr": otherNumericSensorValueStr,
       "otherNumericSensorValueInt": otherNumericSensorValueInt,
       "otherNumericSensorUnits": otherNumericSensorUnits,
       "otherNumericSensorValueIntX1000": otherNumericSensorValueIntX1000,
       "otherNumericSensorValueIntX1000000": otherNumericSensorValueIntX1000000,
       "netBotzStateSensors": netBotzStateSensors,
       "dryContactSensorTable": dryContactSensorTable,
       "dryContactSensorEntry": dryContactSensorEntry,
       "dryContactSensorId": dryContactSensorId,
       "dryContactSensorValue": dryContactSensorValue,
       "dryContactSensorErrorStatus": dryContactSensorErrorStatus,
       "dryContactSensorLabel": dryContactSensorLabel,
       "dryContactSensorEncId": dryContactSensorEncId,
       "dryContactSensorPortId": dryContactSensorPortId,
       "dryContactSensorValueStr": dryContactSensorValueStr,
       "doorSwitchSensorTable": doorSwitchSensorTable,
       "doorSwitchSensorEntry": doorSwitchSensorEntry,
       "doorSwitchSensorId": doorSwitchSensorId,
       "doorSwitchSensorValue": doorSwitchSensorValue,
       "doorSwitchSensorErrorStatus": doorSwitchSensorErrorStatus,
       "doorSwitchSensorLabel": doorSwitchSensorLabel,
       "doorSwitchSensorEncId": doorSwitchSensorEncId,
       "doorSwitchSensorPortId": doorSwitchSensorPortId,
       "doorSwitchSensorValueStr": doorSwitchSensorValueStr,
       "cameraMotionSensorTable": cameraMotionSensorTable,
       "cameraMotionSensorEntry": cameraMotionSensorEntry,
       "cameraMotionSensorId": cameraMotionSensorId,
       "cameraMotionSensorValue": cameraMotionSensorValue,
       "cameraMotionSensorErrorStatus": cameraMotionSensorErrorStatus,
       "cameraMotionSensorLabel": cameraMotionSensorLabel,
       "cameraMotionSensorEncId": cameraMotionSensorEncId,
       "cameraMotionSensorPortId": cameraMotionSensorPortId,
       "cameraMotionSensorValueStr": cameraMotionSensorValueStr,
       "otherStateSensorTable": otherStateSensorTable,
       "otherStateSensorEntry": otherStateSensorEntry,
       "otherStateSensorId": otherStateSensorId,
       "otherStateSensorValue": otherStateSensorValue,
       "otherStateSensorErrorStatus": otherStateSensorErrorStatus,
       "otherStateSensorLabel": otherStateSensorLabel,
       "otherStateSensorEncId": otherStateSensorEncId,
       "otherStateSensorPortId": otherStateSensorPortId,
       "otherStateSensorValueStr": otherStateSensorValueStr,
       "netBotzErrors": netBotzErrors,
       "errorCondTable": errorCondTable,
       "errorCondEntry": errorCondEntry,
       "errorCondId": errorCondId,
       "errorCondSeverity": errorCondSeverity,
       "errorCondTypeId": errorCondTypeId,
       "errorCondStartTime": errorCondStartTime,
       "errorCondStartTimeStr": errorCondStartTimeStr,
       "errorCondResolved": errorCondResolved,
       "errorCondResolvedTime": errorCondResolvedTime,
       "errorCondResolvedTimeStr": errorCondResolvedTimeStr,
       "errorCondEncId": errorCondEncId,
       "errorCondPortId": errorCondPortId,
       "errorCondSensorId": errorCondSensorId,
       "netBotzV2Traps": netBotzV2Traps,
       "netBotzV2GenericTraps": netBotzV2GenericTraps,
       "netBotzV2SensorTraps": netBotzV2SensorTraps,
       "netBotzV2TempSensorTraps": netBotzV2TempSensorTraps,
       "netBotzTempError": netBotzTempError,
       "netBotzTempTooHigh": netBotzTempTooHigh,
       "netBotzTempTooLow": netBotzTempTooLow,
       "netBotzTempTooHighTooLong": netBotzTempTooHighTooLong,
       "netBotzTempTooLowTooLong": netBotzTempTooLowTooLong,
       "netBotzTempUnplugged": netBotzTempUnplugged,
       "netBotzTempIncreasingTooQuickly": netBotzTempIncreasingTooQuickly,
       "netBotzTempDecreasingTooQuickly": netBotzTempDecreasingTooQuickly,
       "netBotzTempErrorRTN": netBotzTempErrorRTN,
       "netBotzTempTooHighRTN": netBotzTempTooHighRTN,
       "netBotzTempTooLowRTN": netBotzTempTooLowRTN,
       "netBotzTempTooHighTooLongRTN": netBotzTempTooHighTooLongRTN,
       "netBotzTempTooLowForTooLongRTN": netBotzTempTooLowForTooLongRTN,
       "netBotzTempReplugged": netBotzTempReplugged,
       "netBotzTempNotIncreasingTooQuickly": netBotzTempNotIncreasingTooQuickly,
       "netBotzTempNotDecreasingTooQuickly": netBotzTempNotDecreasingTooQuickly,
       "netBotzV2HumiditySensorTraps": netBotzV2HumiditySensorTraps,
       "netBotzHumidityError": netBotzHumidityError,
       "netBotzHumidityTooHigh": netBotzHumidityTooHigh,
       "netBotzHumidityTooLow": netBotzHumidityTooLow,
       "netBotzHumidityTooHighTooLong": netBotzHumidityTooHighTooLong,
       "netBotzHumidityTooLowTooLong": netBotzHumidityTooLowTooLong,
       "netBotzHumidityUnplugged": netBotzHumidityUnplugged,
       "netBotzHumidityIncreasingTooQuickly": netBotzHumidityIncreasingTooQuickly,
       "netBotzHumidityDecreasingTooQuickly": netBotzHumidityDecreasingTooQuickly,
       "netBotzHumidityErrorRTN": netBotzHumidityErrorRTN,
       "netBotzHumidityTooHighRTN": netBotzHumidityTooHighRTN,
       "netBotzHumidityTooLowRTN": netBotzHumidityTooLowRTN,
       "netBotzHumidityTooHighTooLongRTN": netBotzHumidityTooHighTooLongRTN,
       "netBotzHumidityTooLowForTooLongRTN": netBotzHumidityTooLowForTooLongRTN,
       "netBotzHumidityReplugged": netBotzHumidityReplugged,
       "netBotzHumidityNotIncreasingTooQuickly": netBotzHumidityNotIncreasingTooQuickly,
       "netBotzHumidityNotDecreasingTooQuickly": netBotzHumidityNotDecreasingTooQuickly,
       "netBotzV2DewPointSensorTraps": netBotzV2DewPointSensorTraps,
       "netBotzDewPointError": netBotzDewPointError,
       "netBotzDewPointTooHigh": netBotzDewPointTooHigh,
       "netBotzDewPointTooLow": netBotzDewPointTooLow,
       "netBotzDewPointTooHighTooLong": netBotzDewPointTooHighTooLong,
       "netBotzDewPointTooLowTooLong": netBotzDewPointTooLowTooLong,
       "netBotzDewPointUnplugged": netBotzDewPointUnplugged,
       "netBotzDewPointIncreasingTooQuickly": netBotzDewPointIncreasingTooQuickly,
       "netBotzDewPointDecreasingTooQuickly": netBotzDewPointDecreasingTooQuickly,
       "netBotzDewPointErrorRTN": netBotzDewPointErrorRTN,
       "netBotzDewPointTooHighRTN": netBotzDewPointTooHighRTN,
       "netBotzDewPointTooLowRTN": netBotzDewPointTooLowRTN,
       "netBotzDewPointTooHighTooLongRTN": netBotzDewPointTooHighTooLongRTN,
       "netBotzDewPointTooLowForTooLongRTN": netBotzDewPointTooLowForTooLongRTN,
       "netBotzDewPointReplugged": netBotzDewPointReplugged,
       "netBotzDewPointNotIncreasingTooQuickly": netBotzDewPointNotIncreasingTooQuickly,
       "netBotzDewPointNotDecreasingTooQuickly": netBotzDewPointNotDecreasingTooQuickly,
       "netBotzV2AirFlowSensorTraps": netBotzV2AirFlowSensorTraps,
       "netBotzAirFlowError": netBotzAirFlowError,
       "netBotzAirFlowTooHigh": netBotzAirFlowTooHigh,
       "netBotzAirFlowTooLow": netBotzAirFlowTooLow,
       "netBotzAirFlowTooHighTooLong": netBotzAirFlowTooHighTooLong,
       "netBotzAirFlowTooLowTooLong": netBotzAirFlowTooLowTooLong,
       "netBotzAirFlowUnplugged": netBotzAirFlowUnplugged,
       "netBotzAirFlowIncreasingTooQuickly": netBotzAirFlowIncreasingTooQuickly,
       "netBotzAirFlowDecreasingTooQuickly": netBotzAirFlowDecreasingTooQuickly,
       "netBotzAirFlowErrorRTN": netBotzAirFlowErrorRTN,
       "netBotzAirFlowTooHighRTN": netBotzAirFlowTooHighRTN,
       "netBotzAirFlowTooLowRTN": netBotzAirFlowTooLowRTN,
       "netBotzAirFlowTooHighTooLongRTN": netBotzAirFlowTooHighTooLongRTN,
       "netBotzAirFlowTooLowForTooLongRTN": netBotzAirFlowTooLowForTooLongRTN,
       "netBotzAirFlowReplugged": netBotzAirFlowReplugged,
       "netBotzAirFlowNotIncreasingTooQuickly": netBotzAirFlowNotIncreasingTooQuickly,
       "netBotzAirFlowNotDecreasingTooQuickly": netBotzAirFlowNotDecreasingTooQuickly,
       "netBotzV2AudioSensorTraps": netBotzV2AudioSensorTraps,
       "netBotzAudioError": netBotzAudioError,
       "netBotzAudioTooHigh": netBotzAudioTooHigh,
       "netBotzAudioTooLow": netBotzAudioTooLow,
       "netBotzAudioTooHighTooLong": netBotzAudioTooHighTooLong,
       "netBotzAudioTooLowTooLong": netBotzAudioTooLowTooLong,
       "netBotzAudioUnplugged": netBotzAudioUnplugged,
       "netBotzAudioIncreasingTooQuickly": netBotzAudioIncreasingTooQuickly,
       "netBotzAudioDecreasingTooQuickly": netBotzAudioDecreasingTooQuickly,
       "netBotzAudioErrorRTN": netBotzAudioErrorRTN,
       "netBotzAudioTooHighRTN": netBotzAudioTooHighRTN,
       "netBotzAudioTooLowRTN": netBotzAudioTooLowRTN,
       "netBotzAudioTooHighTooLongRTN": netBotzAudioTooHighTooLongRTN,
       "netBotzAudioTooLowForTooLongRTN": netBotzAudioTooLowForTooLongRTN,
       "netBotzAudioReplugged": netBotzAudioReplugged,
       "netBotzAudioNotIncreasingTooQuickly": netBotzAudioNotIncreasingTooQuickly,
       "netBotzAudioNotDecreasingTooQuickly": netBotzAudioNotDecreasingTooQuickly,
       "netBotzV2AmpDetectSensorTraps": netBotzV2AmpDetectSensorTraps,
       "netBotzAmpDetectError": netBotzAmpDetectError,
       "netBotzAmpDetectTooHigh": netBotzAmpDetectTooHigh,
       "netBotzAmpDetectTooLow": netBotzAmpDetectTooLow,
       "netBotzAmpDetectTooHighTooLong": netBotzAmpDetectTooHighTooLong,
       "netBotzAmpDetectTooLowTooLong": netBotzAmpDetectTooLowTooLong,
       "netBotzAmpDetectUnplugged": netBotzAmpDetectUnplugged,
       "netBotzAmpDetectIncreasingTooQuickly": netBotzAmpDetectIncreasingTooQuickly,
       "netBotzAmpDetectDecreasingTooQuickly": netBotzAmpDetectDecreasingTooQuickly,
       "netBotzAmpDetectErrorRTN": netBotzAmpDetectErrorRTN,
       "netBotzAmpDetectTooHighRTN": netBotzAmpDetectTooHighRTN,
       "netBotzAmpDetectTooLowRTN": netBotzAmpDetectTooLowRTN,
       "netBotzAmpDetectTooHighTooLongRTN": netBotzAmpDetectTooHighTooLongRTN,
       "netBotzAmpDetectTooLowForTooLongRTN": netBotzAmpDetectTooLowForTooLongRTN,
       "netBotzAmpDetectReplugged": netBotzAmpDetectReplugged,
       "netBotzAmpDetectNotIncreasingTooQuickly": netBotzAmpDetectNotIncreasingTooQuickly,
       "netBotzAmpDetectNotDecreasingTooQuickly": netBotzAmpDetectNotDecreasingTooQuickly,
       "netBotzV2DryContactSensorTraps": netBotzV2DryContactSensorTraps,
       "netBotzDryContactError": netBotzDryContactError,
       "netBotzDryContactUnplugged": netBotzDryContactUnplugged,
       "netBotzDryContactValueError": netBotzDryContactValueError,
       "netBotzDryContactErrorRTN": netBotzDryContactErrorRTN,
       "netBotzDryContactReplugged": netBotzDryContactReplugged,
       "netBotzDryContactValueErrorRTN": netBotzDryContactValueErrorRTN,
       "netBotzV2CameraMotionSensorTraps": netBotzV2CameraMotionSensorTraps,
       "netBotzCameraMotionSensorError": netBotzCameraMotionSensorError,
       "netBotzCameraMotionSensorUnplugged": netBotzCameraMotionSensorUnplugged,
       "netBotzCameraMotionSensorValueError": netBotzCameraMotionSensorValueError,
       "netBotzCameraMotionSensorErrorRTN": netBotzCameraMotionSensorErrorRTN,
       "netBotzCameraMotionSensorReplugged": netBotzCameraMotionSensorReplugged,
       "netBotzCameraMotionSensorValueErrorRTN": netBotzCameraMotionSensorValueErrorRTN,
       "netBotzV2DoorSensorTraps": netBotzV2DoorSensorTraps,
       "netBotzDoorSensorError": netBotzDoorSensorError,
       "netBotzDoorSensorUnplugged": netBotzDoorSensorUnplugged,
       "netBotzDoorSensorValueError": netBotzDoorSensorValueError,
       "netBotzDoorSensorErrorRTN": netBotzDoorSensorErrorRTN,
       "netBotzDoorSensorReplugged": netBotzDoorSensorReplugged,
       "netBotzDoorSensorValueErrorRTN": netBotzDoorSensorValueErrorRTN,
       "netBotzV2MicPlugSensorTraps": netBotzV2MicPlugSensorTraps,
       "netBotzMicPlugSensorError": netBotzMicPlugSensorError,
       "netBotzMicPlugSensorUnplugged": netBotzMicPlugSensorUnplugged,
       "netBotzMicPlugSensorValueError": netBotzMicPlugSensorValueError,
       "netBotzMicPlugSensorErrorRTN": netBotzMicPlugSensorErrorRTN,
       "netBotzMicPlugSensorReplugged": netBotzMicPlugSensorReplugged,
       "netBotzMicPlugSensorValueErrorRTN": netBotzMicPlugSensorValueErrorRTN,
       "netBotzV2SpeakerPlugSensorTraps": netBotzV2SpeakerPlugSensorTraps,
       "netBotzSpeakerPlugSensorError": netBotzSpeakerPlugSensorError,
       "netBotzSpeakerPlugSensorUnplugged": netBotzSpeakerPlugSensorUnplugged,
       "netBotzSpeakerPlugSensorValueError": netBotzSpeakerPlugSensorValueError,
       "netBotzSpeakerPlugSensorErrorRTN": netBotzSpeakerPlugSensorErrorRTN,
       "netBotzSpeakerPlugSensorReplugged": netBotzSpeakerPlugSensorReplugged,
       "netBotzSpeakerPlugSensorValueErrorRTN": netBotzSpeakerPlugSensorValueErrorRTN,
       "netBotzV2TVSignalSensorTraps": netBotzV2TVSignalSensorTraps,
       "netBotzTVSignalSensorError": netBotzTVSignalSensorError,
       "netBotzTVSignalSensorUnplugged": netBotzTVSignalSensorUnplugged,
       "netBotzTVSignalSensorValueError": netBotzTVSignalSensorValueError,
       "netBotzTVSignalSensorErrorRTN": netBotzTVSignalSensorErrorRTN,
       "netBotzTVSignalSensorReplugged": netBotzTVSignalSensorReplugged,
       "netBotzTVSignalSensorValueErrorRTN": netBotzTVSignalSensorValueErrorRTN,
       "netBotzV2GPSPositionSensorTraps": netBotzV2GPSPositionSensorTraps,
       "netBotzGPSPositionError": netBotzGPSPositionError,
       "netBotzGPSPositionTooHigh": netBotzGPSPositionTooHigh,
       "netBotzGPSPositionTooLow": netBotzGPSPositionTooLow,
       "netBotzGPSPositionTooHighTooLong": netBotzGPSPositionTooHighTooLong,
       "netBotzGPSPositionTooLowTooLong": netBotzGPSPositionTooLowTooLong,
       "netBotzGPSPositionUnplugged": netBotzGPSPositionUnplugged,
       "netBotzGPSPositionIncreasingTooQuickly": netBotzGPSPositionIncreasingTooQuickly,
       "netBotzGPSPositionDecreasingTooQuickly": netBotzGPSPositionDecreasingTooQuickly,
       "netBotzGPSPositionErrorRTN": netBotzGPSPositionErrorRTN,
       "netBotzGPSPositionTooHighRTN": netBotzGPSPositionTooHighRTN,
       "netBotzGPSPositionTooLowRTN": netBotzGPSPositionTooLowRTN,
       "netBotzGPSPositionTooHighTooLongRTN": netBotzGPSPositionTooHighTooLongRTN,
       "netBotzGPSPositionTooLowForTooLongRTN": netBotzGPSPositionTooLowForTooLongRTN,
       "netBotzGPSPositionReplugged": netBotzGPSPositionReplugged,
       "netBotzGPSPositionNotIncreasingTooQuickly": netBotzGPSPositionNotIncreasingTooQuickly,
       "netBotzGPSPositionNotDecreasingTooQuickly": netBotzGPSPositionNotDecreasingTooQuickly,
       "netBotzV2GPSMovementSensorTraps": netBotzV2GPSMovementSensorTraps,
       "netBotzGPSMovementError": netBotzGPSMovementError,
       "netBotzGPSMovementTooHigh": netBotzGPSMovementTooHigh,
       "netBotzGPSMovementTooLow": netBotzGPSMovementTooLow,
       "netBotzGPSMovementTooHighTooLong": netBotzGPSMovementTooHighTooLong,
       "netBotzGPSMovementTooLowTooLong": netBotzGPSMovementTooLowTooLong,
       "netBotzGPSMovementUnplugged": netBotzGPSMovementUnplugged,
       "netBotzGPSMovementIncreasingTooQuickly": netBotzGPSMovementIncreasingTooQuickly,
       "netBotzGPSMovementDecreasingTooQuickly": netBotzGPSMovementDecreasingTooQuickly,
       "netBotzGPSMovementErrorRTN": netBotzGPSMovementErrorRTN,
       "netBotzGPSMovementTooHighRTN": netBotzGPSMovementTooHighRTN,
       "netBotzGPSMovementTooLowRTN": netBotzGPSMovementTooLowRTN,
       "netBotzGPSMovementTooHighTooLongRTN": netBotzGPSMovementTooHighTooLongRTN,
       "netBotzGPSMovementTooLowForTooLongRTN": netBotzGPSMovementTooLowForTooLongRTN,
       "netBotzGPSMovementReplugged": netBotzGPSMovementReplugged,
       "netBotzGPSMovementNotIncreasingTooQuickly": netBotzGPSMovementNotIncreasingTooQuickly,
       "netBotzGPSMovementNotDecreasingTooQuickly": netBotzGPSMovementNotDecreasingTooQuickly,
       "netBotzV2GPSStatusSensorTraps": netBotzV2GPSStatusSensorTraps,
       "netBotzGPSStatusSensorError": netBotzGPSStatusSensorError,
       "netBotzGPSStatusSensorUnplugged": netBotzGPSStatusSensorUnplugged,
       "netBotzGPSStatusSensorValueError": netBotzGPSStatusSensorValueError,
       "netBotzGPSStatusSensorErrorRTN": netBotzGPSStatusSensorErrorRTN,
       "netBotzGPSStatusSensorReplugged": netBotzGPSStatusSensorReplugged,
       "netBotzGPSStatusSensorValueErrorRTN": netBotzGPSStatusSensorValueErrorRTN,
       "netBotzV2WirelessStatusSensorTraps": netBotzV2WirelessStatusSensorTraps,
       "netBotzWirelessStatusSensorError": netBotzWirelessStatusSensorError,
       "netBotzWirelessStatusSensorUnplugged": netBotzWirelessStatusSensorUnplugged,
       "netBotzWirelessStatusSensorValueError": netBotzWirelessStatusSensorValueError,
       "netBotzWirelessStatusSensorErrorRTN": netBotzWirelessStatusSensorErrorRTN,
       "netBotzWirelessStatusSensorReplugged": netBotzWirelessStatusSensorReplugged,
       "netBotzWirelessStatusSensorValueErrorRTN": netBotzWirelessStatusSensorValueErrorRTN,
       "netBotzV2PacketDropSensorTraps": netBotzV2PacketDropSensorTraps,
       "netBotzPacketDropError": netBotzPacketDropError,
       "netBotzPacketDropTooHigh": netBotzPacketDropTooHigh,
       "netBotzPacketDropTooLow": netBotzPacketDropTooLow,
       "netBotzPacketDropTooHighTooLong": netBotzPacketDropTooHighTooLong,
       "netBotzPacketDropTooLowTooLong": netBotzPacketDropTooLowTooLong,
       "netBotzPacketDropUnplugged": netBotzPacketDropUnplugged,
       "netBotzPacketDropIncreasingTooQuickly": netBotzPacketDropIncreasingTooQuickly,
       "netBotzPacketDropDecreasingTooQuickly": netBotzPacketDropDecreasingTooQuickly,
       "netBotzPacketDropErrorRTN": netBotzPacketDropErrorRTN,
       "netBotzPacketDropTooHighRTN": netBotzPacketDropTooHighRTN,
       "netBotzPacketDropTooLowRTN": netBotzPacketDropTooLowRTN,
       "netBotzPacketDropTooHighTooLongRTN": netBotzPacketDropTooHighTooLongRTN,
       "netBotzPacketDropTooLowForTooLongRTN": netBotzPacketDropTooLowForTooLongRTN,
       "netBotzPacketDropReplugged": netBotzPacketDropReplugged,
       "netBotzPacketDropNotIncreasingTooQuickly": netBotzPacketDropNotIncreasingTooQuickly,
       "netBotzPacketDropNotDecreasingTooQuickly": netBotzPacketDropNotDecreasingTooQuickly,
       "netBotzV2SNMPCrawlerSensorTraps": netBotzV2SNMPCrawlerSensorTraps,
       "netBotzSNMPCrawlerError": netBotzSNMPCrawlerError,
       "netBotzSNMPCrawlerTooHigh": netBotzSNMPCrawlerTooHigh,
       "netBotzSNMPCrawlerTooLow": netBotzSNMPCrawlerTooLow,
       "netBotzSNMPCrawlerTooHighTooLong": netBotzSNMPCrawlerTooHighTooLong,
       "netBotzSNMPCrawlerTooLowTooLong": netBotzSNMPCrawlerTooLowTooLong,
       "netBotzSNMPCrawlerUnplugged": netBotzSNMPCrawlerUnplugged,
       "netBotzSNMPCrawlerIncreasingTooQuickly": netBotzSNMPCrawlerIncreasingTooQuickly,
       "netBotzSNMPCrawlerDecreasingTooQuickly": netBotzSNMPCrawlerDecreasingTooQuickly,
       "netBotzSNMPCrawlerSensorValueError": netBotzSNMPCrawlerSensorValueError,
       "netBotzSNMPCrawlerErrorRTN": netBotzSNMPCrawlerErrorRTN,
       "netBotzSNMPCrawlerTooHighRTN": netBotzSNMPCrawlerTooHighRTN,
       "netBotzSNMPCrawlerTooLowRTN": netBotzSNMPCrawlerTooLowRTN,
       "netBotzSNMPCrawlerTooHighTooLongRTN": netBotzSNMPCrawlerTooHighTooLongRTN,
       "netBotzSNMPCrawlerTooLowForTooLongRTN": netBotzSNMPCrawlerTooLowForTooLongRTN,
       "netBotzSNMPCrawlerReplugged": netBotzSNMPCrawlerReplugged,
       "netBotzSNMPCrawlerNotIncreasingTooQuickly": netBotzSNMPCrawlerNotIncreasingTooQuickly,
       "netBotzSNMPCrawlerNotDecreasingTooQuickly": netBotzSNMPCrawlerNotDecreasingTooQuickly,
       "netBotzSNMPCrawlerSensorValueErrorRTN": netBotzSNMPCrawlerSensorValueErrorRTN,
       "netBotzV2PlugModuleStatusSensorTraps": netBotzV2PlugModuleStatusSensorTraps,
       "netBotzV2OutputControlSensorTraps": netBotzV2OutputControlSensorTraps,
       "netBotzOutputControlSensorError": netBotzOutputControlSensorError,
       "netBotzOutputControlSensorUnplugged": netBotzOutputControlSensorUnplugged,
       "netBotzOutputControlSensorValueError": netBotzOutputControlSensorValueError,
       "netBotzOutputControlSensorErrorRTN": netBotzOutputControlSensorErrorRTN,
       "netBotzOutputControlSensorReplugged": netBotzOutputControlSensorReplugged,
       "netBotzOutputControlSensorValueErrorRTN": netBotzOutputControlSensorValueErrorRTN,
       "netBotzV2MultiRAESensorTraps": netBotzV2MultiRAESensorTraps,
       "netBotzMultiRAESensorError": netBotzMultiRAESensorError,
       "netBotzMultiRAESensorTooHigh": netBotzMultiRAESensorTooHigh,
       "netBotzMultiRAESensorTooLow": netBotzMultiRAESensorTooLow,
       "netBotzMultiRAESensorTooHighTooLong": netBotzMultiRAESensorTooHighTooLong,
       "netBotzMultiRAESensorTooLowTooLong": netBotzMultiRAESensorTooLowTooLong,
       "netBotzMultiRAESensorUnplugged": netBotzMultiRAESensorUnplugged,
       "netBotzMultiRAESensorIncreasingTooQuickly": netBotzMultiRAESensorIncreasingTooQuickly,
       "netBotzMultiRAESensorDecreasingTooQuickly": netBotzMultiRAESensorDecreasingTooQuickly,
       "netBotzMultiRAESensorSensorValueError": netBotzMultiRAESensorSensorValueError,
       "netBotzMultiRAESensorErrorRTN": netBotzMultiRAESensorErrorRTN,
       "netBotzMultiRAESensorTooHighRTN": netBotzMultiRAESensorTooHighRTN,
       "netBotzMultiRAESensorTooLowRTN": netBotzMultiRAESensorTooLowRTN,
       "netBotzMultiRAESensorTooHighTooLongRTN": netBotzMultiRAESensorTooHighTooLongRTN,
       "netBotzMultiRAESensorTooLowForTooLongRTN": netBotzMultiRAESensorTooLowForTooLongRTN,
       "netBotzMultiRAESensorReplugged": netBotzMultiRAESensorReplugged,
       "netBotzMultiRAESensorNotIncreasingTooQuickly": netBotzMultiRAESensorNotIncreasingTooQuickly,
       "netBotzMultiRAESensorNotDecreasingTooQuickly": netBotzMultiRAESensorNotDecreasingTooQuickly,
       "netBotzMultiRAESensorSensorValueErrorRTN": netBotzMultiRAESensorSensorValueErrorRTN,
       "netBotzV2MultiRAESensorStatusTraps": netBotzV2MultiRAESensorStatusTraps,
       "netBotzMultiRAESensorStatusError": netBotzMultiRAESensorStatusError,
       "netBotzMultiRAESensorStatusUnplugged": netBotzMultiRAESensorStatusUnplugged,
       "netBotzMultiRAESensorStatusValueError": netBotzMultiRAESensorStatusValueError,
       "netBotzMultiRAESensorStatusErrorRTN": netBotzMultiRAESensorStatusErrorRTN,
       "netBotzMultiRAESensorStatusReplugged": netBotzMultiRAESensorStatusReplugged,
       "netBotzMultiRAESensorStatusValueErrorRTN": netBotzMultiRAESensorStatusValueErrorRTN,
       "netBotzV2MultiRAEDeviceStatusTraps": netBotzV2MultiRAEDeviceStatusTraps,
       "netBotzMultiRAEDeviceStatusError": netBotzMultiRAEDeviceStatusError,
       "netBotzMultiRAEDeviceStatusUnplugged": netBotzMultiRAEDeviceStatusUnplugged,
       "netBotzMultiRAEDeviceStatusValueError": netBotzMultiRAEDeviceStatusValueError,
       "netBotzMultiRAEDeviceStatusErrorRTN": netBotzMultiRAEDeviceStatusErrorRTN,
       "netBotzMultiRAEDeviceStatusReplugged": netBotzMultiRAEDeviceStatusReplugged,
       "netBotzMultiRAEDeviceStatusValueErrorRTN": netBotzMultiRAEDeviceStatusValueErrorRTN,
       "netBotzV2PodTraps": netBotzV2PodTraps,
       "netBotzPodUnplugged": netBotzPodUnplugged,
       "netBotzLogonError": netBotzLogonError,
       "netBotzDriveNotFoundError": netBotzDriveNotFoundError,
       "netBotzPodReplugged": netBotzPodReplugged,
       "netBotzLogonErrorResolved": netBotzLogonErrorResolved,
       "netBotzDriveNotFoundErrorResolved": netBotzDriveNotFoundErrorResolved,
       "netBotzV2BasePodTraps": netBotzV2BasePodTraps,
       "netBotzV2SensorPodTraps": netBotzV2SensorPodTraps,
       "netBotzSensorPodUnplugged": netBotzSensorPodUnplugged,
       "netBotzSensorPodReplugged": netBotzSensorPodReplugged,
       "netBotzV2CameraPodTraps": netBotzV2CameraPodTraps,
       "netBotzCameraPodUnplugged": netBotzCameraPodUnplugged,
       "netBotzCameraPodReplugged": netBotzCameraPodReplugged,
       "netBotzV2PortTraps": netBotzV2PortTraps,
       "netBotzV2TrapParms": netBotzV2TrapParms,
       "netBotzV2TrapErrorID": netBotzV2TrapErrorID,
       "netBotzV2TrapErrorType": netBotzV2TrapErrorType,
       "netBotzV2TrapErrorTypeLabel": netBotzV2TrapErrorTypeLabel,
       "netBotzV2TrapSensorID": netBotzV2TrapSensorID,
       "netBotzV2TrapSensorLabel": netBotzV2TrapSensorLabel,
       "netBotzV2TrapPodID": netBotzV2TrapPodID,
       "netBotzV2TrapPodLabel": netBotzV2TrapPodLabel,
       "netBotzV2TrapPortID": netBotzV2TrapPortID,
       "netBotzV2TrapPortLabel": netBotzV2TrapPortLabel,
       "netBotzV2TrapStartTime": netBotzV2TrapStartTime,
       "netBotzV2TrapNotifyTime": netBotzV2TrapNotifyTime,
       "netBotzV2TrapResolveTime": netBotzV2TrapResolveTime,
       "netBotzV2TrapSeverity": netBotzV2TrapSeverity,
       "netBotzV2TrapSensorValue": netBotzV2TrapSensorValue,
       "netBotzV2TrapSensorValueInt": netBotzV2TrapSensorValueInt,
       "netBotzV2TrapSensorValueFraction": netBotzV2TrapSensorValueFraction,
       "netBotzV2Products": netBotzV2Products,
       "netBotzV2Botz": netBotzV2Botz,
       "netBotzWallBotz500": netBotzWallBotz500,
       "netBotz420Wall": netBotz420Wall,
       "raeSystemsAreaConnect500": raeSystemsAreaConnect500,
       "netBotz420Rack": netBotz420Rack,
       "netBotz320Wall": netBotz320Wall,
       "netBotz320Rack": netBotz320Rack,
       "netBotz420ERack": netBotz420ERack,
       "netBotz320ERack": netBotz320ERack}
)
