# SNMP MIB module (VERTICAL-STATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICAL-STATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:24 2024
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

_Vertical_ObjectIdentity = ObjectIdentity
vertical = _Vertical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338)
)
_VStationModule_ObjectIdentity = ObjectIdentity
vStationModule = _VStationModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 7)
)
_VStationCommonGroup_ObjectIdentity = ObjectIdentity
vStationCommonGroup = _VStationCommonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 7, 1)
)
_VStationFirstDigitTimeout_Type = Integer32
_VStationFirstDigitTimeout_Object = MibScalar
vStationFirstDigitTimeout = _VStationFirstDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 1, 1),
    _VStationFirstDigitTimeout_Type()
)
vStationFirstDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationFirstDigitTimeout.setStatus("mandatory")
_VStationDigitTimeout_Type = Integer32
_VStationDigitTimeout_Object = MibTableColumn
vStationDigitTimeout = _VStationDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 1, 2),
    _VStationDigitTimeout_Type()
)
vStationDigitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationDigitTimeout.setStatus("mandatory")
_VStationOffHookTimeout_Type = Integer32
_VStationOffHookTimeout_Object = MibScalar
vStationOffHookTimeout = _VStationOffHookTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 1, 3),
    _VStationOffHookTimeout_Type()
)
vStationOffHookTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationOffHookTimeout.setStatus("mandatory")
_VStationNumStationCards_Type = Integer32
_VStationNumStationCards_Object = MibScalar
vStationNumStationCards = _VStationNumStationCards_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 1, 4),
    _VStationNumStationCards_Type()
)
vStationNumStationCards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationNumStationCards.setStatus("mandatory")


class _VStationExternalDialDigit_Type(DisplayString):
    """Custom type vStationExternalDialDigit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_VStationExternalDialDigit_Type.__name__ = "DisplayString"
_VStationExternalDialDigit_Object = MibScalar
vStationExternalDialDigit = _VStationExternalDialDigit_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 1, 5),
    _VStationExternalDialDigit_Type()
)
vStationExternalDialDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationExternalDialDigit.setStatus("mandatory")
_VStationCardGroup_ObjectIdentity = ObjectIdentity
vStationCardGroup = _VStationCardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2)
)
_VStationCardTable_Object = MibTable
vStationCardTable = _VStationCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vStationCardTable.setStatus("current")
_VStationCardEntry_Object = MibTableRow
vStationCardEntry = _VStationCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1)
)
vStationCardEntry.setIndexNames(
    (0, "VERTICAL-STATION-MIB", "vStationCardSlotNumber"),
)
if mibBuilder.loadTexts:
    vStationCardEntry.setStatus("mandatory")


class _VStationCardSlotNumber_Type(Integer32):
    """Custom type vStationCardSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_VStationCardSlotNumber_Type.__name__ = "Integer32"
_VStationCardSlotNumber_Object = MibTableColumn
vStationCardSlotNumber = _VStationCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 1),
    _VStationCardSlotNumber_Type()
)
vStationCardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationCardSlotNumber.setStatus("mandatory")


class _VStationCardType_Type(Integer32):
    """Custom type vStationCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("card-type-24-CHANNEL-STATION", 2),
          ("card-type-BRIDGE1", 4),
          ("card-type-NOT-CONFIGURED", 0))
    )


_VStationCardType_Type.__name__ = "Integer32"
_VStationCardType_Object = MibTableColumn
vStationCardType = _VStationCardType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 2),
    _VStationCardType_Type()
)
vStationCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationCardType.setStatus("mandatory")


class _VStationCardIOPortAddress_Type(Integer32):
    """Custom type vStationCardIOPortAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VStationCardIOPortAddress_Type.__name__ = "Integer32"
_VStationCardIOPortAddress_Object = MibTableColumn
vStationCardIOPortAddress = _VStationCardIOPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 3),
    _VStationCardIOPortAddress_Type()
)
vStationCardIOPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationCardIOPortAddress.setStatus("mandatory")


class _VStationCardState_Type(Integer32):
    """Custom type vStationCardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("removed", 255))
    )


_VStationCardState_Type.__name__ = "Integer32"
_VStationCardState_Object = MibTableColumn
vStationCardState = _VStationCardState_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 4),
    _VStationCardState_Type()
)
vStationCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationCardState.setStatus("mandatory")


class _VStationCardErrorLED_Type(Integer32):
    """Custom type vStationCardErrorLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VStationCardErrorLED_Type.__name__ = "Integer32"
_VStationCardErrorLED_Object = MibTableColumn
vStationCardErrorLED = _VStationCardErrorLED_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 5),
    _VStationCardErrorLED_Type()
)
vStationCardErrorLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationCardErrorLED.setStatus("mandatory")


class _VStationCardReadyLED_Type(Integer32):
    """Custom type vStationCardReadyLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VStationCardReadyLED_Type.__name__ = "Integer32"
_VStationCardReadyLED_Object = MibTableColumn
vStationCardReadyLED = _VStationCardReadyLED_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 6),
    _VStationCardReadyLED_Type()
)
vStationCardReadyLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationCardReadyLED.setStatus("mandatory")
_VStationDeviceTable_Object = MibTable
vStationDeviceTable = _VStationDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2)
)
if mibBuilder.loadTexts:
    vStationDeviceTable.setStatus("current")
_VStationDeviceEntry_Object = MibTableRow
vStationDeviceEntry = _VStationDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1)
)
vStationDeviceEntry.setIndexNames(
    (0, "VERTICAL-STATION-MIB", "vStationDeviceSlotNumber"),
)
if mibBuilder.loadTexts:
    vStationDeviceEntry.setStatus("mandatory")


class _VStationDeviceSlotNumber_Type(Integer32):
    """Custom type vStationDeviceSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VStationDeviceSlotNumber_Type.__name__ = "Integer32"
_VStationDeviceSlotNumber_Object = MibTableColumn
vStationDeviceSlotNumber = _VStationDeviceSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 1),
    _VStationDeviceSlotNumber_Type()
)
vStationDeviceSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDeviceSlotNumber.setStatus("mandatory")


class _VStationDeviceDeviceNumber_Type(Integer32):
    """Custom type vStationDeviceDeviceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VStationDeviceDeviceNumber_Type.__name__ = "Integer32"
_VStationDeviceDeviceNumber_Object = MibTableColumn
vStationDeviceDeviceNumber = _VStationDeviceDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 2),
    _VStationDeviceDeviceNumber_Type()
)
vStationDeviceDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDeviceDeviceNumber.setStatus("mandatory")


class _VStationDeviceIfIndex_Type(Integer32):
    """Custom type vStationDeviceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VStationDeviceIfIndex_Type.__name__ = "Integer32"
_VStationDeviceIfIndex_Object = MibTableColumn
vStationDeviceIfIndex = _VStationDeviceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 3),
    _VStationDeviceIfIndex_Type()
)
vStationDeviceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDeviceIfIndex.setStatus("mandatory")


class _VStationDeviceBaseIOAddress_Type(Integer32):
    """Custom type vStationDeviceBaseIOAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VStationDeviceBaseIOAddress_Type.__name__ = "Integer32"
_VStationDeviceBaseIOAddress_Object = MibTableColumn
vStationDeviceBaseIOAddress = _VStationDeviceBaseIOAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 4),
    _VStationDeviceBaseIOAddress_Type()
)
vStationDeviceBaseIOAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDeviceBaseIOAddress.setStatus("mandatory")


class _VStationDeviceEnabled_Type(Integer32):
    """Custom type vStationDeviceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VStationDeviceEnabled_Type.__name__ = "Integer32"
_VStationDeviceEnabled_Object = MibTableColumn
vStationDeviceEnabled = _VStationDeviceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 5),
    _VStationDeviceEnabled_Type()
)
vStationDeviceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationDeviceEnabled.setStatus("mandatory")


class _VStationDeviceInterrupt_Type(Integer32):
    """Custom type vStationDeviceInterrupt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VStationDeviceInterrupt_Type.__name__ = "Integer32"
_VStationDeviceInterrupt_Object = MibTableColumn
vStationDeviceInterrupt = _VStationDeviceInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 6),
    _VStationDeviceInterrupt_Type()
)
vStationDeviceInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDeviceInterrupt.setStatus("mandatory")


class _VStationDeviceNumChannels_Type(Integer32):
    """Custom type vStationDeviceNumChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VStationDeviceNumChannels_Type.__name__ = "Integer32"
_VStationDeviceNumChannels_Object = MibTableColumn
vStationDeviceNumChannels = _VStationDeviceNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 7),
    _VStationDeviceNumChannels_Type()
)
vStationDeviceNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDeviceNumChannels.setStatus("mandatory")


class _VStationDeviceMVIPStartingChannel_Type(Integer32):
    """Custom type vStationDeviceMVIPStartingChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VStationDeviceMVIPStartingChannel_Type.__name__ = "Integer32"
_VStationDeviceMVIPStartingChannel_Object = MibTableColumn
vStationDeviceMVIPStartingChannel = _VStationDeviceMVIPStartingChannel_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 8),
    _VStationDeviceMVIPStartingChannel_Type()
)
vStationDeviceMVIPStartingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDeviceMVIPStartingChannel.setStatus("mandatory")


class _VStationDeviceMVIPStream_Type(Integer32):
    """Custom type vStationDeviceMVIPStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VStationDeviceMVIPStream_Type.__name__ = "Integer32"
_VStationDeviceMVIPStream_Object = MibTableColumn
vStationDeviceMVIPStream = _VStationDeviceMVIPStream_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 9),
    _VStationDeviceMVIPStream_Type()
)
vStationDeviceMVIPStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDeviceMVIPStream.setStatus("mandatory")


class _VStationDeviceType_Type(Integer32):
    """Custom type vStationDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dev-station", 8),
          ("dev-undef", 0))
    )


_VStationDeviceType_Type.__name__ = "Integer32"
_VStationDeviceType_Object = MibTableColumn
vStationDeviceType = _VStationDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 10),
    _VStationDeviceType_Type()
)
vStationDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDeviceType.setStatus("mandatory")


class _VStationDeviceChangePending_Type(Integer32):
    """Custom type vStationDeviceChangePending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VStationDeviceChangePending_Type.__name__ = "Integer32"
_VStationDeviceChangePending_Object = MibTableColumn
vStationDeviceChangePending = _VStationDeviceChangePending_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 11),
    _VStationDeviceChangePending_Type()
)
vStationDeviceChangePending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationDeviceChangePending.setStatus("mandatory")
_VStationChannelTable_Object = MibTable
vStationChannelTable = _VStationChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3)
)
if mibBuilder.loadTexts:
    vStationChannelTable.setStatus("current")
_VStationChannelEntry_Object = MibTableRow
vStationChannelEntry = _VStationChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1)
)
vStationChannelEntry.setIndexNames(
    (0, "VERTICAL-STATION-MIB", "vStationChannelSlotNumber"),
    (0, "VERTICAL-STATION-MIB", "vStationChannelIndex"),
)
if mibBuilder.loadTexts:
    vStationChannelEntry.setStatus("mandatory")


class _VStationChannelIndex_Type(Integer32):
    """Custom type vStationChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_VStationChannelIndex_Type.__name__ = "Integer32"
_VStationChannelIndex_Object = MibTableColumn
vStationChannelIndex = _VStationChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 1),
    _VStationChannelIndex_Type()
)
vStationChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationChannelIndex.setStatus("mandatory")


class _VStationChannelSlotNumber_Type(Integer32):
    """Custom type vStationChannelSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VStationChannelSlotNumber_Type.__name__ = "Integer32"
_VStationChannelSlotNumber_Object = MibTableColumn
vStationChannelSlotNumber = _VStationChannelSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 2),
    _VStationChannelSlotNumber_Type()
)
vStationChannelSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationChannelSlotNumber.setStatus("mandatory")


class _VStationChannelDeviceNumber_Type(Integer32):
    """Custom type vStationChannelDeviceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VStationChannelDeviceNumber_Type.__name__ = "Integer32"
_VStationChannelDeviceNumber_Object = MibTableColumn
vStationChannelDeviceNumber = _VStationChannelDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 3),
    _VStationChannelDeviceNumber_Type()
)
vStationChannelDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationChannelDeviceNumber.setStatus("mandatory")


class _VStationChannelChannelType_Type(Integer32):
    """Custom type vStationChannelChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loopStart", 1)
    )


_VStationChannelChannelType_Type.__name__ = "Integer32"
_VStationChannelChannelType_Object = MibTableColumn
vStationChannelChannelType = _VStationChannelChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 4),
    _VStationChannelChannelType_Type()
)
vStationChannelChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationChannelChannelType.setStatus("mandatory")


class _VStationChannelMWIType_Type(Integer32):
    """Custom type vStationChannelMWIType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lamp", 2),
          ("stutter", 1))
    )


_VStationChannelMWIType_Type.__name__ = "Integer32"
_VStationChannelMWIType_Object = MibTableColumn
vStationChannelMWIType = _VStationChannelMWIType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 5),
    _VStationChannelMWIType_Type()
)
vStationChannelMWIType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationChannelMWIType.setStatus("mandatory")


class _VStationChannelOperationMode_Type(Integer32):
    """Custom type vStationChannelOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pBX", 3),
          ("station", 1),
          ("voiceMail", 2))
    )


_VStationChannelOperationMode_Type.__name__ = "Integer32"
_VStationChannelOperationMode_Object = MibTableColumn
vStationChannelOperationMode = _VStationChannelOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 6),
    _VStationChannelOperationMode_Type()
)
vStationChannelOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationChannelOperationMode.setStatus("mandatory")


class _VStationChannelState_Type(Integer32):
    """Custom type vStationChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notConfigured", 2))
    )


_VStationChannelState_Type.__name__ = "Integer32"
_VStationChannelState_Object = MibTableColumn
vStationChannelState = _VStationChannelState_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 7),
    _VStationChannelState_Type()
)
vStationChannelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationChannelState.setStatus("mandatory")


class _VStationChannelType_Type(Integer32):
    """Custom type vStationChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("callerID", 2),
          ("callerID-callWaiting", 3))
    )


_VStationChannelType_Type.__name__ = "Integer32"
_VStationChannelType_Object = MibTableColumn
vStationChannelType = _VStationChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 8),
    _VStationChannelType_Type()
)
vStationChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationChannelType.setStatus("mandatory")


class _VStationChannelCallState_Type(Integer32):
    """Custom type vStationChannelCallState based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("call-state-ALERTING", 8),
          ("call-state-CALL-OFFERED", 5),
          ("call-state-COLLECT-DIGITS", 4),
          ("call-state-COLLECT-FIRST-DIGIT", 3),
          ("call-state-CONNECTED", 9),
          ("call-state-DIAL-REQUEST", 16),
          ("call-state-DIALING", 2),
          ("call-state-DISCONNECTING", 10),
          ("call-state-FAILED", 11),
          ("call-state-FEATURE-INVOKED", 18),
          ("call-state-HELD", 17),
          ("call-state-IDLE", 1),
          ("call-state-INITIALIZE", 14),
          ("call-state-INITIALIZING", 15),
          ("call-state-OFFHOOK", 13),
          ("call-state-OFFHOOK-ACTIVE", 20),
          ("call-state-OFFHOOK-IDLE", 19),
          ("call-state-OUT-OF-SERVICE", 21),
          ("call-state-OUTPULSING", 22),
          ("call-state-PROCEEDING", 6),
          ("call-state-RINGING", 7),
          ("call-state-UNAVAILABLE", 12),
          ("call-state-VOID", 0))
    )


_VStationChannelCallState_Type.__name__ = "Integer32"
_VStationChannelCallState_Object = MibTableColumn
vStationChannelCallState = _VStationChannelCallState_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 9),
    _VStationChannelCallState_Type()
)
vStationChannelCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationChannelCallState.setStatus("mandatory")


class _VStationChannelCalledPartyNumber_Type(DisplayString):
    """Custom type vStationChannelCalledPartyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VStationChannelCalledPartyNumber_Type.__name__ = "DisplayString"
_VStationChannelCalledPartyNumber_Object = MibTableColumn
vStationChannelCalledPartyNumber = _VStationChannelCalledPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 10),
    _VStationChannelCalledPartyNumber_Type()
)
vStationChannelCalledPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationChannelCalledPartyNumber.setStatus("mandatory")


class _VStationChannelCallingPartyNumber_Type(DisplayString):
    """Custom type vStationChannelCallingPartyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VStationChannelCallingPartyNumber_Type.__name__ = "DisplayString"
_VStationChannelCallingPartyNumber_Object = MibTableColumn
vStationChannelCallingPartyNumber = _VStationChannelCallingPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 11),
    _VStationChannelCallingPartyNumber_Type()
)
vStationChannelCallingPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationChannelCallingPartyNumber.setStatus("mandatory")


class _VStationChannelChangePending_Type(Integer32):
    """Custom type vStationChannelChangePending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VStationChannelChangePending_Type.__name__ = "Integer32"
_VStationChannelChangePending_Object = MibTableColumn
vStationChannelChangePending = _VStationChannelChangePending_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 12),
    _VStationChannelChangePending_Type()
)
vStationChannelChangePending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationChannelChangePending.setStatus("mandatory")
_VStationDigitTableGroup_ObjectIdentity = ObjectIdentity
vStationDigitTableGroup = _VStationDigitTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 7, 3)
)
_VStationFirstDigitTable_Object = MibTable
vStationFirstDigitTable = _VStationFirstDigitTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 3, 1)
)
if mibBuilder.loadTexts:
    vStationFirstDigitTable.setStatus("current")
_VStationFirstDigitEntry_Object = MibTableRow
vStationFirstDigitEntry = _VStationFirstDigitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1)
)
vStationFirstDigitEntry.setIndexNames(
    (0, "VERTICAL-STATION-MIB", "vStationDigitIndex"),
)
if mibBuilder.loadTexts:
    vStationFirstDigitEntry.setStatus("mandatory")


class _VStationDigitIndex_Type(Integer32):
    """Custom type vStationDigitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VStationDigitIndex_Type.__name__ = "Integer32"
_VStationDigitIndex_Object = MibTableColumn
vStationDigitIndex = _VStationDigitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 1),
    _VStationDigitIndex_Type()
)
vStationDigitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDigitIndex.setStatus("mandatory")


class _VStationDigitString_Type(DisplayString):
    """Custom type vStationDigitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_VStationDigitString_Type.__name__ = "DisplayString"
_VStationDigitString_Object = MibTableColumn
vStationDigitString = _VStationDigitString_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 2),
    _VStationDigitString_Type()
)
vStationDigitString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationDigitString.setStatus("mandatory")


class _VStationDigitCallType_Type(Integer32):
    """Custom type vStationDigitCallType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("fc-CAMP-ON-CALL", 9),
          ("fc-HOLD-CALL", 1),
          ("fc-INTERNATIONAL-CALL", 5),
          ("fc-LOCAL-CALL", 6),
          ("fc-LONG-DISTANCE-CALL", 4),
          ("fc-OPERATOR-CALL", 7),
          ("fc-PARK-CALL", 2),
          ("fc-RECEPTIONIST-CALL", 8),
          ("fc-STATION-CALL", 3),
          ("fc-VOID", 0))
    )


_VStationDigitCallType_Type.__name__ = "Integer32"
_VStationDigitCallType_Object = MibTableColumn
vStationDigitCallType = _VStationDigitCallType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 3),
    _VStationDigitCallType_Type()
)
vStationDigitCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationDigitCallType.setStatus("mandatory")


class _VStationDigitMoreDigits_Type(Integer32):
    """Custom type vStationDigitMoreDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VStationDigitMoreDigits_Type.__name__ = "Integer32"
_VStationDigitMoreDigits_Object = MibTableColumn
vStationDigitMoreDigits = _VStationDigitMoreDigits_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 4),
    _VStationDigitMoreDigits_Type()
)
vStationDigitMoreDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationDigitMoreDigits.setStatus("mandatory")


class _VStationDigitTimeout2_Type(Integer32):
    """Custom type vStationDigitTimeout2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dontTerminate", 0),
          ("terminate", 1))
    )


_VStationDigitTimeout2_Type.__name__ = "Integer32"
_VStationDigitTimeout2_Object = MibScalar
vStationDigitTimeout2 = _VStationDigitTimeout2_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 5),
    _VStationDigitTimeout2_Type()
)
vStationDigitTimeout2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationDigitTimeout2.setStatus("mandatory")


class _VStationDigitStripDigits_Type(Integer32):
    """Custom type vStationDigitStripDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VStationDigitStripDigits_Type.__name__ = "Integer32"
_VStationDigitStripDigits_Object = MibTableColumn
vStationDigitStripDigits = _VStationDigitStripDigits_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 6),
    _VStationDigitStripDigits_Type()
)
vStationDigitStripDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationDigitStripDigits.setStatus("mandatory")
_VStationExtVoiceMailGroup_ObjectIdentity = ObjectIdentity
vStationExtVoiceMailGroup = _VStationExtVoiceMailGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4)
)
_VStationATTSystem25Group_ObjectIdentity = ObjectIdentity
vStationATTSystem25Group = _VStationATTSystem25Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1)
)


class _VStationMWILampON_Type(DisplayString):
    """Custom type vStationMWILampON based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VStationMWILampON_Type.__name__ = "DisplayString"
_VStationMWILampON_Object = MibScalar
vStationMWILampON = _VStationMWILampON_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 1),
    _VStationMWILampON_Type()
)
vStationMWILampON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationMWILampON.setStatus("mandatory")


class _VStationMWILampOFF_Type(DisplayString):
    """Custom type vStationMWILampOFF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VStationMWILampOFF_Type.__name__ = "DisplayString"
_VStationMWILampOFF_Object = MibScalar
vStationMWILampOFF = _VStationMWILampOFF_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 2),
    _VStationMWILampOFF_Type()
)
vStationMWILampOFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationMWILampOFF.setStatus("mandatory")
_VStationVMCallHandleTable_Object = MibTable
vStationVMCallHandleTable = _VStationVMCallHandleTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3)
)
if mibBuilder.loadTexts:
    vStationVMCallHandleTable.setStatus("current")
_VStationVMCallHandleEntry_Object = MibTableRow
vStationVMCallHandleEntry = _VStationVMCallHandleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1)
)
vStationVMCallHandleEntry.setIndexNames(
    (0, "VERTICAL-STATION-MIB", "vStationVMCallHandleIndex"),
)
if mibBuilder.loadTexts:
    vStationVMCallHandleEntry.setStatus("mandatory")


class _VStationVMCallHandleIndex_Type(Integer32):
    """Custom type vStationVMCallHandleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VStationVMCallHandleIndex_Type.__name__ = "Integer32"
_VStationVMCallHandleIndex_Object = MibTableColumn
vStationVMCallHandleIndex = _VStationVMCallHandleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 1),
    _VStationVMCallHandleIndex_Type()
)
vStationVMCallHandleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationVMCallHandleIndex.setStatus("mandatory")


class _VStationVMCallHandleType_Type(Integer32):
    """Custom type vStationVMCallHandleType based on Integer32"""
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
        *(("directExternal", 1),
          ("directInternal", 3),
          ("forwardExternal", 2),
          ("forwardInternal", 4))
    )


_VStationVMCallHandleType_Type.__name__ = "Integer32"
_VStationVMCallHandleType_Object = MibTableColumn
vStationVMCallHandleType = _VStationVMCallHandleType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 2),
    _VStationVMCallHandleType_Type()
)
vStationVMCallHandleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStationVMCallHandleType.setStatus("mandatory")


class _VStationVMCallHandleOpcode_Type(OctetString):
    """Custom type vStationVMCallHandleOpcode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VStationVMCallHandleOpcode_Type.__name__ = "OctetString"
_VStationVMCallHandleOpcode_Object = MibTableColumn
vStationVMCallHandleOpcode = _VStationVMCallHandleOpcode_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 3),
    _VStationVMCallHandleOpcode_Type()
)
vStationVMCallHandleOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationVMCallHandleOpcode.setStatus("mandatory")


class _VStationVMCallHandleSRCNumber_Type(OctetString):
    """Custom type vStationVMCallHandleSRCNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VStationVMCallHandleSRCNumber_Type.__name__ = "OctetString"
_VStationVMCallHandleSRCNumber_Object = MibTableColumn
vStationVMCallHandleSRCNumber = _VStationVMCallHandleSRCNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 4),
    _VStationVMCallHandleSRCNumber_Type()
)
vStationVMCallHandleSRCNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationVMCallHandleSRCNumber.setStatus("mandatory")


class _VStationVMCallHandleDSTNumber_Type(OctetString):
    """Custom type vStationVMCallHandleDSTNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VStationVMCallHandleDSTNumber_Type.__name__ = "OctetString"
_VStationVMCallHandleDSTNumber_Object = MibTableColumn
vStationVMCallHandleDSTNumber = _VStationVMCallHandleDSTNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 5),
    _VStationVMCallHandleDSTNumber_Type()
)
vStationVMCallHandleDSTNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStationVMCallHandleDSTNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects

vStationCannotPlayTone = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 12)
)
vStationCannotPlayTone.setObjects(
      *(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
)
if mibBuilder.loadTexts:
    vStationCannotPlayTone.setStatus(
        ""
    )

vStationCannotCancelTone = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 13)
)
vStationCannotCancelTone.setObjects(
      *(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
)
if mibBuilder.loadTexts:
    vStationCannotCancelTone.setStatus(
        ""
    )

vStationCannotAttachDigitCollector = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 14)
)
vStationCannotAttachDigitCollector.setObjects(
      *(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
)
if mibBuilder.loadTexts:
    vStationCannotAttachDigitCollector.setStatus(
        ""
    )

vStationCannotReleaseDigitCollector = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 15)
)
vStationCannotReleaseDigitCollector.setObjects(
      *(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
)
if mibBuilder.loadTexts:
    vStationCannotReleaseDigitCollector.setStatus(
        ""
    )

vStationRECONFIG_COMPLETE = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 16)
)
vStationRECONFIG_COMPLETE.setObjects(
      *(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"))
)
if mibBuilder.loadTexts:
    vStationRECONFIG_COMPLETE.setStatus(
        ""
    )

vStationRECONFIG_ERROR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 17)
)
vStationRECONFIG_ERROR.setObjects(
      *(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"),
        ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"))
)
if mibBuilder.loadTexts:
    vStationRECONFIG_ERROR.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICAL-STATION-MIB",
    **{"vertical": vertical,
       "vStationCannotPlayTone": vStationCannotPlayTone,
       "vStationCannotCancelTone": vStationCannotCancelTone,
       "vStationCannotAttachDigitCollector": vStationCannotAttachDigitCollector,
       "vStationCannotReleaseDigitCollector": vStationCannotReleaseDigitCollector,
       "vStationRECONFIG-COMPLETE": vStationRECONFIG_COMPLETE,
       "vStationRECONFIG-ERROR": vStationRECONFIG_ERROR,
       "vStationModule": vStationModule,
       "vStationCommonGroup": vStationCommonGroup,
       "vStationFirstDigitTimeout": vStationFirstDigitTimeout,
       "vStationDigitTimeout": vStationDigitTimeout,
       "vStationOffHookTimeout": vStationOffHookTimeout,
       "vStationNumStationCards": vStationNumStationCards,
       "vStationExternalDialDigit": vStationExternalDialDigit,
       "vStationCardGroup": vStationCardGroup,
       "vStationCardTable": vStationCardTable,
       "vStationCardEntry": vStationCardEntry,
       "vStationCardSlotNumber": vStationCardSlotNumber,
       "vStationCardType": vStationCardType,
       "vStationCardIOPortAddress": vStationCardIOPortAddress,
       "vStationCardState": vStationCardState,
       "vStationCardErrorLED": vStationCardErrorLED,
       "vStationCardReadyLED": vStationCardReadyLED,
       "vStationDeviceTable": vStationDeviceTable,
       "vStationDeviceEntry": vStationDeviceEntry,
       "vStationDeviceSlotNumber": vStationDeviceSlotNumber,
       "vStationDeviceDeviceNumber": vStationDeviceDeviceNumber,
       "vStationDeviceIfIndex": vStationDeviceIfIndex,
       "vStationDeviceBaseIOAddress": vStationDeviceBaseIOAddress,
       "vStationDeviceEnabled": vStationDeviceEnabled,
       "vStationDeviceInterrupt": vStationDeviceInterrupt,
       "vStationDeviceNumChannels": vStationDeviceNumChannels,
       "vStationDeviceMVIPStartingChannel": vStationDeviceMVIPStartingChannel,
       "vStationDeviceMVIPStream": vStationDeviceMVIPStream,
       "vStationDeviceType": vStationDeviceType,
       "vStationDeviceChangePending": vStationDeviceChangePending,
       "vStationChannelTable": vStationChannelTable,
       "vStationChannelEntry": vStationChannelEntry,
       "vStationChannelIndex": vStationChannelIndex,
       "vStationChannelSlotNumber": vStationChannelSlotNumber,
       "vStationChannelDeviceNumber": vStationChannelDeviceNumber,
       "vStationChannelChannelType": vStationChannelChannelType,
       "vStationChannelMWIType": vStationChannelMWIType,
       "vStationChannelOperationMode": vStationChannelOperationMode,
       "vStationChannelState": vStationChannelState,
       "vStationChannelType": vStationChannelType,
       "vStationChannelCallState": vStationChannelCallState,
       "vStationChannelCalledPartyNumber": vStationChannelCalledPartyNumber,
       "vStationChannelCallingPartyNumber": vStationChannelCallingPartyNumber,
       "vStationChannelChangePending": vStationChannelChangePending,
       "vStationDigitTableGroup": vStationDigitTableGroup,
       "vStationFirstDigitTable": vStationFirstDigitTable,
       "vStationFirstDigitEntry": vStationFirstDigitEntry,
       "vStationDigitIndex": vStationDigitIndex,
       "vStationDigitString": vStationDigitString,
       "vStationDigitCallType": vStationDigitCallType,
       "vStationDigitMoreDigits": vStationDigitMoreDigits,
       "vStationDigitTimeout2": vStationDigitTimeout2,
       "vStationDigitStripDigits": vStationDigitStripDigits,
       "vStationExtVoiceMailGroup": vStationExtVoiceMailGroup,
       "vStationATTSystem25Group": vStationATTSystem25Group,
       "vStationMWILampON": vStationMWILampON,
       "vStationMWILampOFF": vStationMWILampOFF,
       "vStationVMCallHandleTable": vStationVMCallHandleTable,
       "vStationVMCallHandleEntry": vStationVMCallHandleEntry,
       "vStationVMCallHandleIndex": vStationVMCallHandleIndex,
       "vStationVMCallHandleType": vStationVMCallHandleType,
       "vStationVMCallHandleOpcode": vStationVMCallHandleOpcode,
       "vStationVMCallHandleSRCNumber": vStationVMCallHandleSRCNumber,
       "vStationVMCallHandleDSTNumber": vStationVMCallHandleDSTNumber}
)
