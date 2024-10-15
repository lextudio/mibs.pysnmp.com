# SNMP MIB module (Fore-TCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-TCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:19 2024
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

(EntryStatus,
 atmSwitch,
 hardware) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "EntryStatus",
    "atmSwitch",
    "hardware")

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ecpStationModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7)
)


# Types definitions



class EsiReferenceSource(Integer32):
    """Custom type EsiReferenceSource based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("bits1", 9),
          ("bits2", 10),
          ("fab1Pri", 1),
          ("fab1Sec", 2),
          ("fab2Pri", 3),
          ("fab2Sec", 4),
          ("fab3Pri", 5),
          ("fab3Sec", 6),
          ("fab4Pri", 7),
          ("fab4Sec", 8))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EcpHardware_ObjectIdentity = ObjectIdentity
ecpHardware = _EcpHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1)
)
_EcpBoardTable_Object = MibTable
ecpBoardTable = _EcpBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ecpBoardTable.setStatus("current")
_EcpBoardEntry_Object = MibTableRow
ecpBoardEntry = _EcpBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 1, 1)
)
ecpBoardEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
)
if mibBuilder.loadTexts:
    ecpBoardEntry.setStatus("current")


class _EcpBoardIndex_Type(Integer32):
    """Custom type ecpBoardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slotX", 1),
          ("slotY", 2))
    )


_EcpBoardIndex_Type.__name__ = "Integer32"
_EcpBoardIndex_Object = MibTableColumn
ecpBoardIndex = _EcpBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 1, 1, 1),
    _EcpBoardIndex_Type()
)
ecpBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpBoardIndex.setStatus("current")
_EcpBoardVersion_Type = Integer32
_EcpBoardVersion_Object = MibTableColumn
ecpBoardVersion = _EcpBoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 1, 1, 2),
    _EcpBoardVersion_Type()
)
ecpBoardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpBoardVersion.setStatus("current")
_EcpBoardSerialNumber_Type = Integer32
_EcpBoardSerialNumber_Object = MibTableColumn
ecpBoardSerialNumber = _EcpBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 1, 1, 3),
    _EcpBoardSerialNumber_Type()
)
ecpBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpBoardSerialNumber.setStatus("current")


class _EcpBoardOtherEcpPresent_Type(Integer32):
    """Custom type ecpBoardOtherEcpPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecpAbsent", 2),
          ("ecpPresent", 1))
    )


_EcpBoardOtherEcpPresent_Type.__name__ = "Integer32"
_EcpBoardOtherEcpPresent_Object = MibTableColumn
ecpBoardOtherEcpPresent = _EcpBoardOtherEcpPresent_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 1, 1, 4),
    _EcpBoardOtherEcpPresent_Type()
)
ecpBoardOtherEcpPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpBoardOtherEcpPresent.setStatus("current")


class _EcpBoardEsiPresent_Type(Integer32):
    """Custom type ecpBoardEsiPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("esiAbsent", 2),
          ("esiPresent", 1))
    )


_EcpBoardEsiPresent_Type.__name__ = "Integer32"
_EcpBoardEsiPresent_Object = MibTableColumn
ecpBoardEsiPresent = _EcpBoardEsiPresent_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 1, 1, 5),
    _EcpBoardEsiPresent_Type()
)
ecpBoardEsiPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpBoardEsiPresent.setStatus("current")
_EcpSerialIfTable_Object = MibTable
ecpSerialIfTable = _EcpSerialIfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    ecpSerialIfTable.setStatus("current")
_EcpSerialIfEntry_Object = MibTableRow
ecpSerialIfEntry = _EcpSerialIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 2, 1)
)
ecpSerialIfEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
    (0, "Fore-TCM-MIB", "ecpSerialIfPortIndex"),
)
if mibBuilder.loadTexts:
    ecpSerialIfEntry.setStatus("current")
_EcpSerialIfPortIndex_Type = Integer32
_EcpSerialIfPortIndex_Object = MibTableColumn
ecpSerialIfPortIndex = _EcpSerialIfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 2, 1, 1),
    _EcpSerialIfPortIndex_Type()
)
ecpSerialIfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSerialIfPortIndex.setStatus("current")


class _EcpSerialIfPortType_Type(Integer32):
    """Custom type ecpSerialIfPortType based on Integer32"""
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
        *(("other", 1),
          ("rs232", 2),
          ("rs422", 3),
          ("rs423", 4),
          ("v35", 5),
          ("x21", 6))
    )


_EcpSerialIfPortType_Type.__name__ = "Integer32"
_EcpSerialIfPortType_Object = MibTableColumn
ecpSerialIfPortType = _EcpSerialIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 2, 1, 2),
    _EcpSerialIfPortType_Type()
)
ecpSerialIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSerialIfPortType.setStatus("current")
_EcpSerialIfPortSpeed_Type = Integer32
_EcpSerialIfPortSpeed_Object = MibTableColumn
ecpSerialIfPortSpeed = _EcpSerialIfPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 2, 1, 3),
    _EcpSerialIfPortSpeed_Type()
)
ecpSerialIfPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSerialIfPortSpeed.setStatus("current")


class _EcpSerialIfFlowType_Type(Integer32):
    """Custom type ecpSerialIfFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctsRts", 2),
          ("dsrDtr", 3),
          ("none", 1))
    )


_EcpSerialIfFlowType_Type.__name__ = "Integer32"
_EcpSerialIfFlowType_Object = MibTableColumn
ecpSerialIfFlowType = _EcpSerialIfFlowType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 2, 1, 4),
    _EcpSerialIfFlowType_Type()
)
ecpSerialIfFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSerialIfFlowType.setStatus("current")
_EcpSerialIfPortBits_Type = Integer32
_EcpSerialIfPortBits_Object = MibTableColumn
ecpSerialIfPortBits = _EcpSerialIfPortBits_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 2, 1, 5),
    _EcpSerialIfPortBits_Type()
)
ecpSerialIfPortBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSerialIfPortBits.setStatus("current")


class _EcpSerialIfPortStopBits_Type(Integer32):
    """Custom type ecpSerialIfPortStopBits based on Integer32"""
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
        *(("dynamic", 4),
          ("one", 1),
          ("oneAndHalf", 3),
          ("two", 2))
    )


_EcpSerialIfPortStopBits_Type.__name__ = "Integer32"
_EcpSerialIfPortStopBits_Object = MibTableColumn
ecpSerialIfPortStopBits = _EcpSerialIfPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 2, 1, 6),
    _EcpSerialIfPortStopBits_Type()
)
ecpSerialIfPortStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSerialIfPortStopBits.setStatus("current")


class _EcpSerialIfPortParity_Type(Integer32):
    """Custom type ecpSerialIfPortParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_EcpSerialIfPortParity_Type.__name__ = "Integer32"
_EcpSerialIfPortParity_Object = MibTableColumn
ecpSerialIfPortParity = _EcpSerialIfPortParity_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 2, 1, 7),
    _EcpSerialIfPortParity_Type()
)
ecpSerialIfPortParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSerialIfPortParity.setStatus("current")
_EcpEnvironment_ObjectIdentity = ObjectIdentity
ecpEnvironment = _EcpEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3)
)
_EcpAlarmGroup_ObjectIdentity = ObjectIdentity
ecpAlarmGroup = _EcpAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1)
)
_EcpAlarmTable_Object = MibTable
ecpAlarmTable = _EcpAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ecpAlarmTable.setStatus("current")
_EcpAlarmEntry_Object = MibTableRow
ecpAlarmEntry = _EcpAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 1, 1)
)
ecpAlarmEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
    (0, "Fore-TCM-MIB", "ecpAlarmType"),
)
if mibBuilder.loadTexts:
    ecpAlarmEntry.setStatus("current")


class _EcpAlarmType_Type(Integer32):
    """Custom type ecpAlarmType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("esiLossOfSyncSrc", 10),
          ("fanBankFailed", 3),
          ("faultyOrMissingStandbyTcm", 9),
          ("linkFailed", 5),
          ("powerSupply5VoltFailed", 8),
          ("powerSupplyInputFailed", 1),
          ("powerSupplyOutputFailed", 2),
          ("powerSupplyOverCurrent", 7),
          ("spansFailed", 6),
          ("tempSensorOverTemp", 4))
    )


_EcpAlarmType_Type.__name__ = "Integer32"
_EcpAlarmType_Object = MibTableColumn
ecpAlarmType = _EcpAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 1, 1, 1),
    _EcpAlarmType_Type()
)
ecpAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpAlarmType.setStatus("current")


class _EcpAlarmStatus_Type(Integer32):
    """Custom type ecpAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_EcpAlarmStatus_Type.__name__ = "Integer32"
_EcpAlarmStatus_Object = MibTableColumn
ecpAlarmStatus = _EcpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 1, 1, 2),
    _EcpAlarmStatus_Type()
)
ecpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpAlarmStatus.setStatus("current")


class _EcpAlarmMinorCategory_Type(Integer32):
    """Custom type ecpAlarmMinorCategory based on Integer32"""
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


_EcpAlarmMinorCategory_Type.__name__ = "Integer32"
_EcpAlarmMinorCategory_Object = MibTableColumn
ecpAlarmMinorCategory = _EcpAlarmMinorCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 1, 1, 3),
    _EcpAlarmMinorCategory_Type()
)
ecpAlarmMinorCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpAlarmMinorCategory.setStatus("current")


class _EcpAlarmMajorCategory_Type(Integer32):
    """Custom type ecpAlarmMajorCategory based on Integer32"""
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


_EcpAlarmMajorCategory_Type.__name__ = "Integer32"
_EcpAlarmMajorCategory_Object = MibTableColumn
ecpAlarmMajorCategory = _EcpAlarmMajorCategory_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 1, 1, 4),
    _EcpAlarmMajorCategory_Type()
)
ecpAlarmMajorCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpAlarmMajorCategory.setStatus("current")
_EcpAlarmReset_Type = Integer32
_EcpAlarmReset_Object = MibTableColumn
ecpAlarmReset = _EcpAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 1, 1, 5),
    _EcpAlarmReset_Type()
)
ecpAlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpAlarmReset.setStatus("current")


class _EcpAlarmMajorRelayState_Type(Integer32):
    """Custom type ecpAlarmMajorRelayState based on Integer32"""
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


_EcpAlarmMajorRelayState_Type.__name__ = "Integer32"
_EcpAlarmMajorRelayState_Object = MibScalar
ecpAlarmMajorRelayState = _EcpAlarmMajorRelayState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 2),
    _EcpAlarmMajorRelayState_Type()
)
ecpAlarmMajorRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpAlarmMajorRelayState.setStatus("current")


class _EcpAlarmMinorRelayState_Type(Integer32):
    """Custom type ecpAlarmMinorRelayState based on Integer32"""
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


_EcpAlarmMinorRelayState_Type.__name__ = "Integer32"
_EcpAlarmMinorRelayState_Object = MibScalar
ecpAlarmMinorRelayState = _EcpAlarmMinorRelayState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 3),
    _EcpAlarmMinorRelayState_Type()
)
ecpAlarmMinorRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpAlarmMinorRelayState.setStatus("current")
_EcpAlarmRelayTable_Object = MibTable
ecpAlarmRelayTable = _EcpAlarmRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ecpAlarmRelayTable.setStatus("current")
_EcpAlarmRelayEntry_Object = MibTableRow
ecpAlarmRelayEntry = _EcpAlarmRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 4, 1)
)
ecpAlarmRelayEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
    (0, "Fore-TCM-MIB", "ecpAlarmRelayIndex"),
)
if mibBuilder.loadTexts:
    ecpAlarmRelayEntry.setStatus("current")
_EcpAlarmRelayIndex_Type = Integer32
_EcpAlarmRelayIndex_Object = MibTableColumn
ecpAlarmRelayIndex = _EcpAlarmRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 4, 1, 1),
    _EcpAlarmRelayIndex_Type()
)
ecpAlarmRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpAlarmRelayIndex.setStatus("current")


class _EcpAlarmRelayFunction_Type(Integer32):
    """Custom type ecpAlarmRelayFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ecpMajorAlarmRelay", 2),
          ("ecpMinorAlarmRelay", 3),
          ("ecpUnusedRelay", 1))
    )


_EcpAlarmRelayFunction_Type.__name__ = "Integer32"
_EcpAlarmRelayFunction_Object = MibTableColumn
ecpAlarmRelayFunction = _EcpAlarmRelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 4, 1, 2),
    _EcpAlarmRelayFunction_Type()
)
ecpAlarmRelayFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpAlarmRelayFunction.setStatus("current")


class _EcpAlarmRelayState_Type(Integer32):
    """Custom type ecpAlarmRelayState based on Integer32"""
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


_EcpAlarmRelayState_Type.__name__ = "Integer32"
_EcpAlarmRelayState_Object = MibTableColumn
ecpAlarmRelayState = _EcpAlarmRelayState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 1, 3, 1, 4, 1, 3),
    _EcpAlarmRelayState_Type()
)
ecpAlarmRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpAlarmRelayState.setStatus("current")
_EcpSoftware_ObjectIdentity = ObjectIdentity
ecpSoftware = _EcpSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2)
)
_EcpSwMainGroup_ObjectIdentity = ObjectIdentity
ecpSwMainGroup = _EcpSwMainGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1)
)
_EcpSwMainTable_Object = MibTable
ecpSwMainTable = _EcpSwMainTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ecpSwMainTable.setStatus("current")
_EcpSwMainEntry_Object = MibTableRow
ecpSwMainEntry = _EcpSwMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1)
)
ecpSwMainEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
)
if mibBuilder.loadTexts:
    ecpSwMainEntry.setStatus("current")
_EcpName_Type = DisplayString
_EcpName_Object = MibTableColumn
ecpName = _EcpName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 1),
    _EcpName_Type()
)
ecpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpName.setStatus("current")
_EcpHardwareVersion_Type = Integer32
_EcpHardwareVersion_Object = MibTableColumn
ecpHardwareVersion = _EcpHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 2),
    _EcpHardwareVersion_Type()
)
ecpHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpHardwareVersion.setStatus("current")
_EcpSoftwareVersion_Type = Integer32
_EcpSoftwareVersion_Object = MibTableColumn
ecpSoftwareVersion = _EcpSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 3),
    _EcpSoftwareVersion_Type()
)
ecpSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSoftwareVersion.setStatus("current")
_EcpSoftwareVersionText_Type = DisplayString
_EcpSoftwareVersionText_Object = MibTableColumn
ecpSoftwareVersionText = _EcpSoftwareVersionText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 4),
    _EcpSoftwareVersionText_Type()
)
ecpSoftwareVersionText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpSoftwareVersionText.setStatus("current")


class _EcpType_Type(Integer32):
    """Custom type ecpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cec-plus", 2),
          ("cec-plus-t", 3),
          ("unrecognized", 1))
    )


_EcpType_Type.__name__ = "Integer32"
_EcpType_Object = MibTableColumn
ecpType = _EcpType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 5),
    _EcpType_Type()
)
ecpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpType.setStatus("current")


class _EcpOperatingStatus_Type(Integer32):
    """Custom type ecpOperatingStatus based on Integer32"""
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
        *(("ecpActive", 3),
          ("ecpOffline", 4),
          ("ecpStandby", 2),
          ("ecpUnknown", 1))
    )


_EcpOperatingStatus_Type.__name__ = "Integer32"
_EcpOperatingStatus_Object = MibTableColumn
ecpOperatingStatus = _EcpOperatingStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 6),
    _EcpOperatingStatus_Type()
)
ecpOperatingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpOperatingStatus.setStatus("current")


class _EcpProtocolType_Type(Integer32):
    """Custom type ecpProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("tftp", 1))
    )


_EcpProtocolType_Type.__name__ = "Integer32"
_EcpProtocolType_Object = MibTableColumn
ecpProtocolType = _EcpProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 7),
    _EcpProtocolType_Type()
)
ecpProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpProtocolType.setStatus("current")


class _EcpTimeZone_Type(DisplayString):
    """Custom type ecpTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EcpTimeZone_Type.__name__ = "DisplayString"
_EcpTimeZone_Object = MibTableColumn
ecpTimeZone = _EcpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 8),
    _EcpTimeZone_Type()
)
ecpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpTimeZone.setStatus("current")
_EcpGMTime_Type = DateAndTime
_EcpGMTime_Object = MibTableColumn
ecpGMTime = _EcpGMTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 9),
    _EcpGMTime_Type()
)
ecpGMTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpGMTime.setStatus("current")
_EcpUptime_Type = TimeTicks
_EcpUptime_Object = MibTableColumn
ecpUptime = _EcpUptime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 10),
    _EcpUptime_Type()
)
ecpUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpUptime.setStatus("current")
_EcpModeChangeTime_Type = DateAndTime
_EcpModeChangeTime_Object = MibTableColumn
ecpModeChangeTime = _EcpModeChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 11),
    _EcpModeChangeTime_Type()
)
ecpModeChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpModeChangeTime.setStatus("current")


class _EcpOtherEcpStatus_Type(Integer32):
    """Custom type ecpOtherEcpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecpNormal", 1),
          ("ecpUnknown", 2))
    )


_EcpOtherEcpStatus_Type.__name__ = "Integer32"
_EcpOtherEcpStatus_Object = MibTableColumn
ecpOtherEcpStatus = _EcpOtherEcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 12),
    _EcpOtherEcpStatus_Type()
)
ecpOtherEcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpOtherEcpStatus.setStatus("current")


class _EcpExternalInput1_Type(Integer32):
    """Custom type ecpExternalInput1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecpInputOff", 2),
          ("ecpInputOn", 1))
    )


_EcpExternalInput1_Type.__name__ = "Integer32"
_EcpExternalInput1_Object = MibTableColumn
ecpExternalInput1 = _EcpExternalInput1_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 13),
    _EcpExternalInput1_Type()
)
ecpExternalInput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpExternalInput1.setStatus("current")


class _EcpExternalInput2_Type(Integer32):
    """Custom type ecpExternalInput2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecpInputOff", 2),
          ("ecpInputOn", 1))
    )


_EcpExternalInput2_Type.__name__ = "Integer32"
_EcpExternalInput2_Object = MibTableColumn
ecpExternalInput2 = _EcpExternalInput2_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 14),
    _EcpExternalInput2_Type()
)
ecpExternalInput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpExternalInput2.setStatus("current")


class _EcpExternalInput3_Type(Integer32):
    """Custom type ecpExternalInput3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecpInputOff", 2),
          ("ecpInputOn", 1))
    )


_EcpExternalInput3_Type.__name__ = "Integer32"
_EcpExternalInput3_Object = MibTableColumn
ecpExternalInput3 = _EcpExternalInput3_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 15),
    _EcpExternalInput3_Type()
)
ecpExternalInput3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpExternalInput3.setStatus("current")


class _EcpExternalInput4_Type(Integer32):
    """Custom type ecpExternalInput4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecpInputOff", 2),
          ("ecpInputOn", 1))
    )


_EcpExternalInput4_Type.__name__ = "Integer32"
_EcpExternalInput4_Object = MibTableColumn
ecpExternalInput4 = _EcpExternalInput4_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 16),
    _EcpExternalInput4_Type()
)
ecpExternalInput4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpExternalInput4.setStatus("current")


class _EcpExternalInput5_Type(Integer32):
    """Custom type ecpExternalInput5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecpInputOff", 2),
          ("ecpInputOn", 1))
    )


_EcpExternalInput5_Type.__name__ = "Integer32"
_EcpExternalInput5_Object = MibTableColumn
ecpExternalInput5 = _EcpExternalInput5_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 1, 1, 1, 17),
    _EcpExternalInput5_Type()
)
ecpExternalInput5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpExternalInput5.setStatus("current")
_EcpIpGroup_ObjectIdentity = ObjectIdentity
ecpIpGroup = _EcpIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2)
)
_EcpNetIfTable_Object = MibTable
ecpNetIfTable = _EcpNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ecpNetIfTable.setStatus("current")
_EcpNetIfEntry_Object = MibTableRow
ecpNetIfEntry = _EcpNetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1)
)
ecpNetIfEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
    (0, "Fore-TCM-MIB", "ecpNetIfIndex"),
)
if mibBuilder.loadTexts:
    ecpNetIfEntry.setStatus("current")
_EcpNetIfIndex_Type = Integer32
_EcpNetIfIndex_Object = MibTableColumn
ecpNetIfIndex = _EcpNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1, 1),
    _EcpNetIfIndex_Type()
)
ecpNetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfIndex.setStatus("current")
_EcpNetIfDescr_Type = DisplayString
_EcpNetIfDescr_Object = MibTableColumn
ecpNetIfDescr = _EcpNetIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1, 2),
    _EcpNetIfDescr_Type()
)
ecpNetIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfDescr.setStatus("current")
_EcpNetIfPhysAddress_Type = PhysAddress
_EcpNetIfPhysAddress_Object = MibTableColumn
ecpNetIfPhysAddress = _EcpNetIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1, 3),
    _EcpNetIfPhysAddress_Type()
)
ecpNetIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfPhysAddress.setStatus("current")


class _EcpNetIfAdminStatus_Type(Integer32):
    """Custom type ecpNetIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EcpNetIfAdminStatus_Type.__name__ = "Integer32"
_EcpNetIfAdminStatus_Object = MibTableColumn
ecpNetIfAdminStatus = _EcpNetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1, 4),
    _EcpNetIfAdminStatus_Type()
)
ecpNetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpNetIfAdminStatus.setStatus("current")


class _EcpNetIfOperStatus_Type(Integer32):
    """Custom type ecpNetIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EcpNetIfOperStatus_Type.__name__ = "Integer32"
_EcpNetIfOperStatus_Object = MibTableColumn
ecpNetIfOperStatus = _EcpNetIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1, 5),
    _EcpNetIfOperStatus_Type()
)
ecpNetIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfOperStatus.setStatus("current")
_EcpNetIfLastChange_Type = TimeTicks
_EcpNetIfLastChange_Object = MibTableColumn
ecpNetIfLastChange = _EcpNetIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1, 6),
    _EcpNetIfLastChange_Type()
)
ecpNetIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfLastChange.setStatus("current")
_EcpNetIfIpAddr_Type = IpAddress
_EcpNetIfIpAddr_Object = MibTableColumn
ecpNetIfIpAddr = _EcpNetIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1, 7),
    _EcpNetIfIpAddr_Type()
)
ecpNetIfIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpNetIfIpAddr.setStatus("current")
_EcpNetIfIpMask_Type = IpAddress
_EcpNetIfIpMask_Object = MibTableColumn
ecpNetIfIpMask = _EcpNetIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1, 8),
    _EcpNetIfIpMask_Type()
)
ecpNetIfIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpNetIfIpMask.setStatus("current")
_EcpNetIfIpBcastAddr_Type = Integer32
_EcpNetIfIpBcastAddr_Object = MibTableColumn
ecpNetIfIpBcastAddr = _EcpNetIfIpBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 1, 1, 9),
    _EcpNetIfIpBcastAddr_Type()
)
ecpNetIfIpBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpNetIfIpBcastAddr.setStatus("current")
_EcpNetIfStatsTable_Object = MibTable
ecpNetIfStatsTable = _EcpNetIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ecpNetIfStatsTable.setStatus("current")
_EcpNetIfStatsEntry_Object = MibTableRow
ecpNetIfStatsEntry = _EcpNetIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1)
)
ecpNetIfStatsEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
    (0, "Fore-TCM-MIB", "ecpNetIfIndex"),
)
if mibBuilder.loadTexts:
    ecpNetIfStatsEntry.setStatus("current")
_EcpNetIfInOctets_Type = Counter32
_EcpNetIfInOctets_Object = MibTableColumn
ecpNetIfInOctets = _EcpNetIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 1),
    _EcpNetIfInOctets_Type()
)
ecpNetIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfInOctets.setStatus("current")
_EcpNetIfInUcastPkts_Type = Counter32
_EcpNetIfInUcastPkts_Object = MibTableColumn
ecpNetIfInUcastPkts = _EcpNetIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 2),
    _EcpNetIfInUcastPkts_Type()
)
ecpNetIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfInUcastPkts.setStatus("current")
_EcpNetIfInNUcastPkts_Type = Counter32
_EcpNetIfInNUcastPkts_Object = MibTableColumn
ecpNetIfInNUcastPkts = _EcpNetIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 3),
    _EcpNetIfInNUcastPkts_Type()
)
ecpNetIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfInNUcastPkts.setStatus("current")
_EcpNetIfInDiscards_Type = Counter32
_EcpNetIfInDiscards_Object = MibTableColumn
ecpNetIfInDiscards = _EcpNetIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 4),
    _EcpNetIfInDiscards_Type()
)
ecpNetIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfInDiscards.setStatus("current")
_EcpNetIfInErrors_Type = Counter32
_EcpNetIfInErrors_Object = MibTableColumn
ecpNetIfInErrors = _EcpNetIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 5),
    _EcpNetIfInErrors_Type()
)
ecpNetIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfInErrors.setStatus("current")
_EcpNetIfInUnknownProtos_Type = Counter32
_EcpNetIfInUnknownProtos_Object = MibTableColumn
ecpNetIfInUnknownProtos = _EcpNetIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 6),
    _EcpNetIfInUnknownProtos_Type()
)
ecpNetIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfInUnknownProtos.setStatus("current")
_EcpNetIfOutOctets_Type = Counter32
_EcpNetIfOutOctets_Object = MibTableColumn
ecpNetIfOutOctets = _EcpNetIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 7),
    _EcpNetIfOutOctets_Type()
)
ecpNetIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfOutOctets.setStatus("current")
_EcpNetIfOutUcastPkts_Type = Counter32
_EcpNetIfOutUcastPkts_Object = MibTableColumn
ecpNetIfOutUcastPkts = _EcpNetIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 8),
    _EcpNetIfOutUcastPkts_Type()
)
ecpNetIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfOutUcastPkts.setStatus("current")
_EcpNetIfOutNUcastPkts_Type = Counter32
_EcpNetIfOutNUcastPkts_Object = MibTableColumn
ecpNetIfOutNUcastPkts = _EcpNetIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 9),
    _EcpNetIfOutNUcastPkts_Type()
)
ecpNetIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfOutNUcastPkts.setStatus("current")
_EcpNetIfOutDiscards_Type = Counter32
_EcpNetIfOutDiscards_Object = MibTableColumn
ecpNetIfOutDiscards = _EcpNetIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 10),
    _EcpNetIfOutDiscards_Type()
)
ecpNetIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfOutDiscards.setStatus("current")
_EcpNetIfOutErrors_Type = Counter32
_EcpNetIfOutErrors_Object = MibTableColumn
ecpNetIfOutErrors = _EcpNetIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 11),
    _EcpNetIfOutErrors_Type()
)
ecpNetIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfOutErrors.setStatus("current")
_EcpNetIfOutQLen_Type = Gauge32
_EcpNetIfOutQLen_Object = MibTableColumn
ecpNetIfOutQLen = _EcpNetIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 2, 1, 12),
    _EcpNetIfOutQLen_Type()
)
ecpNetIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpNetIfOutQLen.setStatus("current")
_EcpIpStatsTable_Object = MibTable
ecpIpStatsTable = _EcpIpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3)
)
if mibBuilder.loadTexts:
    ecpIpStatsTable.setStatus("current")
_EcpIpStatsEntry_Object = MibTableRow
ecpIpStatsEntry = _EcpIpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1)
)
ecpIpStatsEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
)
if mibBuilder.loadTexts:
    ecpIpStatsEntry.setStatus("current")
_EcpIpInReceives_Type = Counter32
_EcpIpInReceives_Object = MibTableColumn
ecpIpInReceives = _EcpIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 1),
    _EcpIpInReceives_Type()
)
ecpIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpInReceives.setStatus("current")
_EcpIpInHdrErrors_Type = Counter32
_EcpIpInHdrErrors_Object = MibTableColumn
ecpIpInHdrErrors = _EcpIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 2),
    _EcpIpInHdrErrors_Type()
)
ecpIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpInHdrErrors.setStatus("current")
_EcpIpInAddrErrors_Type = Counter32
_EcpIpInAddrErrors_Object = MibTableColumn
ecpIpInAddrErrors = _EcpIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 3),
    _EcpIpInAddrErrors_Type()
)
ecpIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpInAddrErrors.setStatus("current")
_EcpIpForwDatagrams_Type = Counter32
_EcpIpForwDatagrams_Object = MibTableColumn
ecpIpForwDatagrams = _EcpIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 4),
    _EcpIpForwDatagrams_Type()
)
ecpIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpForwDatagrams.setStatus("current")
_EcpIpInUnknownProtos_Type = Counter32
_EcpIpInUnknownProtos_Object = MibTableColumn
ecpIpInUnknownProtos = _EcpIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 5),
    _EcpIpInUnknownProtos_Type()
)
ecpIpInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpInUnknownProtos.setStatus("current")
_EcpIpInDiscards_Type = Counter32
_EcpIpInDiscards_Object = MibTableColumn
ecpIpInDiscards = _EcpIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 6),
    _EcpIpInDiscards_Type()
)
ecpIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpInDiscards.setStatus("current")
_EcpIpInDelivers_Type = Counter32
_EcpIpInDelivers_Object = MibTableColumn
ecpIpInDelivers = _EcpIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 7),
    _EcpIpInDelivers_Type()
)
ecpIpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpInDelivers.setStatus("current")
_EcpIpOutRequests_Type = Counter32
_EcpIpOutRequests_Object = MibTableColumn
ecpIpOutRequests = _EcpIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 8),
    _EcpIpOutRequests_Type()
)
ecpIpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpOutRequests.setStatus("current")
_EcpIpOutDiscards_Type = Counter32
_EcpIpOutDiscards_Object = MibTableColumn
ecpIpOutDiscards = _EcpIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 9),
    _EcpIpOutDiscards_Type()
)
ecpIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpOutDiscards.setStatus("current")
_EcpIpOutNoRoutes_Type = Counter32
_EcpIpOutNoRoutes_Object = MibTableColumn
ecpIpOutNoRoutes = _EcpIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 10),
    _EcpIpOutNoRoutes_Type()
)
ecpIpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpOutNoRoutes.setStatus("current")
_EcpIpReasmReqds_Type = Counter32
_EcpIpReasmReqds_Object = MibTableColumn
ecpIpReasmReqds = _EcpIpReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 11),
    _EcpIpReasmReqds_Type()
)
ecpIpReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpReasmReqds.setStatus("current")
_EcpIpReasmOKs_Type = Counter32
_EcpIpReasmOKs_Object = MibTableColumn
ecpIpReasmOKs = _EcpIpReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 12),
    _EcpIpReasmOKs_Type()
)
ecpIpReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpReasmOKs.setStatus("current")
_EcpIpReasmFails_Type = Counter32
_EcpIpReasmFails_Object = MibTableColumn
ecpIpReasmFails = _EcpIpReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 13),
    _EcpIpReasmFails_Type()
)
ecpIpReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpReasmFails.setStatus("current")
_EcpIpFragOKs_Type = Counter32
_EcpIpFragOKs_Object = MibTableColumn
ecpIpFragOKs = _EcpIpFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 14),
    _EcpIpFragOKs_Type()
)
ecpIpFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpFragOKs.setStatus("current")
_EcpIpFragFails_Type = Counter32
_EcpIpFragFails_Object = MibTableColumn
ecpIpFragFails = _EcpIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 15),
    _EcpIpFragFails_Type()
)
ecpIpFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpFragFails.setStatus("current")
_EcpIpFragCreates_Type = Counter32
_EcpIpFragCreates_Object = MibTableColumn
ecpIpFragCreates = _EcpIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 3, 1, 16),
    _EcpIpFragCreates_Type()
)
ecpIpFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpFragCreates.setStatus("current")
_EcpIpRouteTable_Object = MibTable
ecpIpRouteTable = _EcpIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ecpIpRouteTable.setStatus("current")
_EcpIpRouteEntry_Object = MibTableRow
ecpIpRouteEntry = _EcpIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 4, 1)
)
ecpIpRouteEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
    (0, "Fore-TCM-MIB", "ecpIpRouteDest"),
)
if mibBuilder.loadTexts:
    ecpIpRouteEntry.setStatus("current")
_EcpIpRouteDest_Type = IpAddress
_EcpIpRouteDest_Object = MibTableColumn
ecpIpRouteDest = _EcpIpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 4, 1, 1),
    _EcpIpRouteDest_Type()
)
ecpIpRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIpRouteDest.setStatus("current")
_EcpIpRouteIfIndex_Type = Integer32
_EcpIpRouteIfIndex_Object = MibTableColumn
ecpIpRouteIfIndex = _EcpIpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 4, 1, 2),
    _EcpIpRouteIfIndex_Type()
)
ecpIpRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpIpRouteIfIndex.setStatus("current")
_EcpIpRouteNextHop_Type = IpAddress
_EcpIpRouteNextHop_Object = MibTableColumn
ecpIpRouteNextHop = _EcpIpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 4, 1, 3),
    _EcpIpRouteNextHop_Type()
)
ecpIpRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpIpRouteNextHop.setStatus("current")
_EcpIpRouteMetric1_Type = Integer32
_EcpIpRouteMetric1_Object = MibTableColumn
ecpIpRouteMetric1 = _EcpIpRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 4, 1, 4),
    _EcpIpRouteMetric1_Type()
)
ecpIpRouteMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpIpRouteMetric1.setStatus("current")


class _EcpIpRouteType_Type(Integer32):
    """Custom type ecpIpRouteType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_EcpIpRouteType_Type.__name__ = "Integer32"
_EcpIpRouteType_Object = MibTableColumn
ecpIpRouteType = _EcpIpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 4, 1, 5),
    _EcpIpRouteType_Type()
)
ecpIpRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpIpRouteType.setStatus("current")
_EcpIpRouteMask_Type = IpAddress
_EcpIpRouteMask_Object = MibTableColumn
ecpIpRouteMask = _EcpIpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 4, 1, 6),
    _EcpIpRouteMask_Type()
)
ecpIpRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpIpRouteMask.setStatus("current")
_EcpIcmpStatsTable_Object = MibTable
ecpIcmpStatsTable = _EcpIcmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5)
)
if mibBuilder.loadTexts:
    ecpIcmpStatsTable.setStatus("current")
_EcpIcmpStatsEntry_Object = MibTableRow
ecpIcmpStatsEntry = _EcpIcmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1)
)
ecpIcmpStatsEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
)
if mibBuilder.loadTexts:
    ecpIcmpStatsEntry.setStatus("current")
_EcpIcmpInMsgs_Type = Counter32
_EcpIcmpInMsgs_Object = MibTableColumn
ecpIcmpInMsgs = _EcpIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 1),
    _EcpIcmpInMsgs_Type()
)
ecpIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInMsgs.setStatus("current")
_EcpIcmpInErrors_Type = Counter32
_EcpIcmpInErrors_Object = MibTableColumn
ecpIcmpInErrors = _EcpIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 2),
    _EcpIcmpInErrors_Type()
)
ecpIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInErrors.setStatus("current")
_EcpIcmpInDestUnreach_Type = Counter32
_EcpIcmpInDestUnreach_Object = MibTableColumn
ecpIcmpInDestUnreach = _EcpIcmpInDestUnreach_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 3),
    _EcpIcmpInDestUnreach_Type()
)
ecpIcmpInDestUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInDestUnreach.setStatus("current")
_EcpIcmpInTimeExcds_Type = Counter32
_EcpIcmpInTimeExcds_Object = MibTableColumn
ecpIcmpInTimeExcds = _EcpIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 4),
    _EcpIcmpInTimeExcds_Type()
)
ecpIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInTimeExcds.setStatus("current")
_EcpIcmpInParmProbs_Type = Counter32
_EcpIcmpInParmProbs_Object = MibTableColumn
ecpIcmpInParmProbs = _EcpIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 5),
    _EcpIcmpInParmProbs_Type()
)
ecpIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInParmProbs.setStatus("current")
_EcpIcmpInSrcQuenchs_Type = Counter32
_EcpIcmpInSrcQuenchs_Object = MibTableColumn
ecpIcmpInSrcQuenchs = _EcpIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 6),
    _EcpIcmpInSrcQuenchs_Type()
)
ecpIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInSrcQuenchs.setStatus("current")
_EcpIcmpInRedirects_Type = Counter32
_EcpIcmpInRedirects_Object = MibTableColumn
ecpIcmpInRedirects = _EcpIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 7),
    _EcpIcmpInRedirects_Type()
)
ecpIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInRedirects.setStatus("current")
_EcpIcmpInEchos_Type = Counter32
_EcpIcmpInEchos_Object = MibTableColumn
ecpIcmpInEchos = _EcpIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 8),
    _EcpIcmpInEchos_Type()
)
ecpIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInEchos.setStatus("current")
_EcpIcmpInEchoReps_Type = Counter32
_EcpIcmpInEchoReps_Object = MibTableColumn
ecpIcmpInEchoReps = _EcpIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 9),
    _EcpIcmpInEchoReps_Type()
)
ecpIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInEchoReps.setStatus("current")
_EcpIcmpInTimestamps_Type = Counter32
_EcpIcmpInTimestamps_Object = MibTableColumn
ecpIcmpInTimestamps = _EcpIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 10),
    _EcpIcmpInTimestamps_Type()
)
ecpIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInTimestamps.setStatus("current")
_EcpIcmpInTimestampReps_Type = Counter32
_EcpIcmpInTimestampReps_Object = MibTableColumn
ecpIcmpInTimestampReps = _EcpIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 11),
    _EcpIcmpInTimestampReps_Type()
)
ecpIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInTimestampReps.setStatus("current")
_EcpIcmpInaddrMasks_Type = Counter32
_EcpIcmpInaddrMasks_Object = MibTableColumn
ecpIcmpInaddrMasks = _EcpIcmpInaddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 12),
    _EcpIcmpInaddrMasks_Type()
)
ecpIcmpInaddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInaddrMasks.setStatus("current")
_EcpIcmpInAddrMaskReps_Type = Counter32
_EcpIcmpInAddrMaskReps_Object = MibTableColumn
ecpIcmpInAddrMaskReps = _EcpIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 13),
    _EcpIcmpInAddrMaskReps_Type()
)
ecpIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpInAddrMaskReps.setStatus("current")
_EcpIcmpOutMsgs_Type = Counter32
_EcpIcmpOutMsgs_Object = MibTableColumn
ecpIcmpOutMsgs = _EcpIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 14),
    _EcpIcmpOutMsgs_Type()
)
ecpIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutMsgs.setStatus("current")
_EcpIcmpOutErrors_Type = Counter32
_EcpIcmpOutErrors_Object = MibTableColumn
ecpIcmpOutErrors = _EcpIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 15),
    _EcpIcmpOutErrors_Type()
)
ecpIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutErrors.setStatus("current")
_EcpIcmpOutDestUnreachs_Type = Counter32
_EcpIcmpOutDestUnreachs_Object = MibTableColumn
ecpIcmpOutDestUnreachs = _EcpIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 16),
    _EcpIcmpOutDestUnreachs_Type()
)
ecpIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutDestUnreachs.setStatus("current")
_EcpIcmpOutTimeExcds_Type = Counter32
_EcpIcmpOutTimeExcds_Object = MibTableColumn
ecpIcmpOutTimeExcds = _EcpIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 17),
    _EcpIcmpOutTimeExcds_Type()
)
ecpIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutTimeExcds.setStatus("current")
_EcpIcmpOutParmProbs_Type = Counter32
_EcpIcmpOutParmProbs_Object = MibTableColumn
ecpIcmpOutParmProbs = _EcpIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 18),
    _EcpIcmpOutParmProbs_Type()
)
ecpIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutParmProbs.setStatus("current")
_EcpIcmpOutSrcQuenchs_Type = Counter32
_EcpIcmpOutSrcQuenchs_Object = MibTableColumn
ecpIcmpOutSrcQuenchs = _EcpIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 19),
    _EcpIcmpOutSrcQuenchs_Type()
)
ecpIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutSrcQuenchs.setStatus("current")
_EcpIcmpOutRedirects_Type = Counter32
_EcpIcmpOutRedirects_Object = MibTableColumn
ecpIcmpOutRedirects = _EcpIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 20),
    _EcpIcmpOutRedirects_Type()
)
ecpIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutRedirects.setStatus("current")
_EcpIcmpOutEchos_Type = Counter32
_EcpIcmpOutEchos_Object = MibTableColumn
ecpIcmpOutEchos = _EcpIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 21),
    _EcpIcmpOutEchos_Type()
)
ecpIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutEchos.setStatus("current")
_EcpIcmpOutEchoReps_Type = Counter32
_EcpIcmpOutEchoReps_Object = MibTableColumn
ecpIcmpOutEchoReps = _EcpIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 22),
    _EcpIcmpOutEchoReps_Type()
)
ecpIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutEchoReps.setStatus("current")
_EcpIcmpOutTimestamps_Type = Counter32
_EcpIcmpOutTimestamps_Object = MibTableColumn
ecpIcmpOutTimestamps = _EcpIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 23),
    _EcpIcmpOutTimestamps_Type()
)
ecpIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutTimestamps.setStatus("current")
_EcpIcmpOutTimestampReps_Type = Counter32
_EcpIcmpOutTimestampReps_Object = MibTableColumn
ecpIcmpOutTimestampReps = _EcpIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 24),
    _EcpIcmpOutTimestampReps_Type()
)
ecpIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutTimestampReps.setStatus("current")
_EcpIcmpOutAddrMasks_Type = Counter32
_EcpIcmpOutAddrMasks_Object = MibTableColumn
ecpIcmpOutAddrMasks = _EcpIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 25),
    _EcpIcmpOutAddrMasks_Type()
)
ecpIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutAddrMasks.setStatus("current")
_EcpIcmpOutAddrMaskReps_Type = Counter32
_EcpIcmpOutAddrMaskReps_Object = MibTableColumn
ecpIcmpOutAddrMaskReps = _EcpIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 5, 1, 26),
    _EcpIcmpOutAddrMaskReps_Type()
)
ecpIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpIcmpOutAddrMaskReps.setStatus("current")
_EcpTcpStatsTable_Object = MibTable
ecpTcpStatsTable = _EcpTcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6)
)
if mibBuilder.loadTexts:
    ecpTcpStatsTable.setStatus("current")
_EcpTcpStatsEntry_Object = MibTableRow
ecpTcpStatsEntry = _EcpTcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6, 1)
)
ecpTcpStatsEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
)
if mibBuilder.loadTexts:
    ecpTcpStatsEntry.setStatus("current")
_EcpTcpActiveOpens_Type = Counter32
_EcpTcpActiveOpens_Object = MibTableColumn
ecpTcpActiveOpens = _EcpTcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6, 1, 1),
    _EcpTcpActiveOpens_Type()
)
ecpTcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTcpActiveOpens.setStatus("current")
_EcpTcpPassiveOpens_Type = Counter32
_EcpTcpPassiveOpens_Object = MibTableColumn
ecpTcpPassiveOpens = _EcpTcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6, 1, 2),
    _EcpTcpPassiveOpens_Type()
)
ecpTcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTcpPassiveOpens.setStatus("current")
_EcpTcpAttemptFails_Type = Counter32
_EcpTcpAttemptFails_Object = MibTableColumn
ecpTcpAttemptFails = _EcpTcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6, 1, 3),
    _EcpTcpAttemptFails_Type()
)
ecpTcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTcpAttemptFails.setStatus("current")
_EcpTcpEstabResets_Type = Counter32
_EcpTcpEstabResets_Object = MibTableColumn
ecpTcpEstabResets = _EcpTcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6, 1, 4),
    _EcpTcpEstabResets_Type()
)
ecpTcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTcpEstabResets.setStatus("current")
_EcpTcpCurrEstab_Type = Counter32
_EcpTcpCurrEstab_Object = MibTableColumn
ecpTcpCurrEstab = _EcpTcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6, 1, 5),
    _EcpTcpCurrEstab_Type()
)
ecpTcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTcpCurrEstab.setStatus("current")
_EcpTcpInSegs_Type = Counter32
_EcpTcpInSegs_Object = MibTableColumn
ecpTcpInSegs = _EcpTcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6, 1, 6),
    _EcpTcpInSegs_Type()
)
ecpTcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTcpInSegs.setStatus("current")
_EcpTcpOutSegs_Type = Counter32
_EcpTcpOutSegs_Object = MibTableColumn
ecpTcpOutSegs = _EcpTcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6, 1, 7),
    _EcpTcpOutSegs_Type()
)
ecpTcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTcpOutSegs.setStatus("current")
_EcpTcpRetransSegs_Type = Counter32
_EcpTcpRetransSegs_Object = MibTableColumn
ecpTcpRetransSegs = _EcpTcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 6, 1, 8),
    _EcpTcpRetransSegs_Type()
)
ecpTcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTcpRetransSegs.setStatus("current")
_EcpUdpStatsTable_Object = MibTable
ecpUdpStatsTable = _EcpUdpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 7)
)
if mibBuilder.loadTexts:
    ecpUdpStatsTable.setStatus("current")
_EcpUdpStatsEntry_Object = MibTableRow
ecpUdpStatsEntry = _EcpUdpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 7, 1)
)
ecpUdpStatsEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
)
if mibBuilder.loadTexts:
    ecpUdpStatsEntry.setStatus("current")
_EcpUdpInDatagrams_Type = Counter32
_EcpUdpInDatagrams_Object = MibTableColumn
ecpUdpInDatagrams = _EcpUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 7, 1, 1),
    _EcpUdpInDatagrams_Type()
)
ecpUdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpUdpInDatagrams.setStatus("current")
_EcpUdpNoPorts_Type = Counter32
_EcpUdpNoPorts_Object = MibTableColumn
ecpUdpNoPorts = _EcpUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 7, 1, 2),
    _EcpUdpNoPorts_Type()
)
ecpUdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpUdpNoPorts.setStatus("current")
_EcpUdpInErrors_Type = Counter32
_EcpUdpInErrors_Object = MibTableColumn
ecpUdpInErrors = _EcpUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 7, 1, 3),
    _EcpUdpInErrors_Type()
)
ecpUdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpUdpInErrors.setStatus("current")
_EcpUdpOutDatagrams_Type = Counter32
_EcpUdpOutDatagrams_Object = MibTableColumn
ecpUdpOutDatagrams = _EcpUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 7, 1, 4),
    _EcpUdpOutDatagrams_Type()
)
ecpUdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpUdpOutDatagrams.setStatus("current")
_EcpIpConfigTable_Object = MibTable
ecpIpConfigTable = _EcpIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 8)
)
if mibBuilder.loadTexts:
    ecpIpConfigTable.setStatus("current")
_EcpIpConfigEntry_Object = MibTableRow
ecpIpConfigEntry = _EcpIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 8, 1)
)
ecpIpConfigEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
)
if mibBuilder.loadTexts:
    ecpIpConfigEntry.setStatus("current")


class _EcpIpForwarding_Type(Integer32):
    """Custom type ecpIpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("not-forwarding", 2))
    )


_EcpIpForwarding_Type.__name__ = "Integer32"
_EcpIpForwarding_Object = MibTableColumn
ecpIpForwarding = _EcpIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 2, 8, 1, 1),
    _EcpIpForwarding_Type()
)
ecpIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpIpForwarding.setStatus("current")
_EcpSnmp_ObjectIdentity = ObjectIdentity
ecpSnmp = _EcpSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 3)
)
_EcpTrapConfGroup_ObjectIdentity = ObjectIdentity
ecpTrapConfGroup = _EcpTrapConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 3, 1)
)
_EcpTrapNumberOfDest_Type = Integer32
_EcpTrapNumberOfDest_Object = MibScalar
ecpTrapNumberOfDest = _EcpTrapNumberOfDest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 3, 1, 1),
    _EcpTrapNumberOfDest_Type()
)
ecpTrapNumberOfDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTrapNumberOfDest.setStatus("current")
_EcpTrapDestTable_Object = MibTable
ecpTrapDestTable = _EcpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ecpTrapDestTable.setStatus("current")
_EcpTrapDestEntry_Object = MibTableRow
ecpTrapDestEntry = _EcpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 3, 1, 2, 1)
)
ecpTrapDestEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "ecpBoardIndex"),
    (0, "Fore-TCM-MIB", "ecpTrapDest"),
)
if mibBuilder.loadTexts:
    ecpTrapDestEntry.setStatus("current")
_EcpTrapDest_Type = IpAddress
_EcpTrapDest_Object = MibTableColumn
ecpTrapDest = _EcpTrapDest_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 3, 1, 2, 1, 1),
    _EcpTrapDest_Type()
)
ecpTrapDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecpTrapDest.setStatus("current")
_EcpTrapDestStatus_Type = EntryStatus
_EcpTrapDestStatus_Object = MibTableColumn
ecpTrapDestStatus = _EcpTrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 7, 2, 3, 1, 2, 1, 2),
    _EcpTrapDestStatus_Type()
)
ecpTrapDestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecpTrapDestStatus.setStatus("current")
_EsiCard_ObjectIdentity = ObjectIdentity
esiCard = _EsiCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8)
)
_EsiHardware_ObjectIdentity = ObjectIdentity
esiHardware = _EsiHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 1)
)
_EsiCardHwTable_Object = MibTable
esiCardHwTable = _EsiCardHwTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    esiCardHwTable.setStatus("current")
_EsiCardHwEntry_Object = MibTableRow
esiCardHwEntry = _EsiCardHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 1, 1, 1)
)
esiCardHwEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "esiCardIndex"),
)
if mibBuilder.loadTexts:
    esiCardHwEntry.setStatus("current")


class _EsiCardIndex_Type(Integer32):
    """Custom type esiCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slotX", 1),
          ("slotY", 2))
    )


_EsiCardIndex_Type.__name__ = "Integer32"
_EsiCardIndex_Object = MibTableColumn
esiCardIndex = _EsiCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 1, 1, 1, 1),
    _EsiCardIndex_Type()
)
esiCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiCardIndex.setStatus("current")


class _EsiHwCardType_Type(Integer32):
    """Custom type esiHwCardType based on Integer32"""
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
        *(("esiDs1TypeA", 1),
          ("esiDs1TypeB", 2),
          ("esiE1TypeA", 3),
          ("esiE1TypeB", 4))
    )


_EsiHwCardType_Type.__name__ = "Integer32"
_EsiHwCardType_Object = MibTableColumn
esiHwCardType = _EsiHwCardType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 1, 1, 1, 2),
    _EsiHwCardType_Type()
)
esiHwCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiHwCardType.setStatus("current")
_EsiHwCardVersion_Type = Integer32
_EsiHwCardVersion_Object = MibTableColumn
esiHwCardVersion = _EsiHwCardVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 1, 1, 1, 3),
    _EsiHwCardVersion_Type()
)
esiHwCardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiHwCardVersion.setStatus("current")


class _EsiHwPllStatus_Type(Integer32):
    """Custom type esiHwPllStatus based on Integer32"""
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
        *(("pllAcquire", 3),
          ("pllFreeRun", 1),
          ("pllHoldover", 4),
          ("pllLocked", 2),
          ("pllRefQualFail", 5))
    )


_EsiHwPllStatus_Type.__name__ = "Integer32"
_EsiHwPllStatus_Object = MibTableColumn
esiHwPllStatus = _EsiHwPllStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 1, 1, 1, 4),
    _EsiHwPllStatus_Type()
)
esiHwPllStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiHwPllStatus.setStatus("current")
_EsiSoftware_ObjectIdentity = ObjectIdentity
esiSoftware = _EsiSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2)
)
_EsiCardSwTable_Object = MibTable
esiCardSwTable = _EsiCardSwTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    esiCardSwTable.setStatus("current")
_EsiCardSwEntry_Object = MibTableRow
esiCardSwEntry = _EsiCardSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1)
)
esiCardSwEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "esiCardIndex"),
)
if mibBuilder.loadTexts:
    esiCardSwEntry.setStatus("current")


class _EsiOperationStatus_Type(Integer32):
    """Custom type esiOperationStatus based on Integer32"""
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


_EsiOperationStatus_Type.__name__ = "Integer32"
_EsiOperationStatus_Object = MibTableColumn
esiOperationStatus = _EsiOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 1),
    _EsiOperationStatus_Type()
)
esiOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiOperationStatus.setStatus("current")


class _EsiCurrentTimingRef_Type(Integer32):
    """Custom type esiCurrentTimingRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("refFreeRun", 1),
          ("refIsBits1", 5),
          ("refIsBits2", 6),
          ("refIsPrimary", 2),
          ("refIsSecondary", 3))
    )


_EsiCurrentTimingRef_Type.__name__ = "Integer32"
_EsiCurrentTimingRef_Object = MibTableColumn
esiCurrentTimingRef = _EsiCurrentTimingRef_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 2),
    _EsiCurrentTimingRef_Type()
)
esiCurrentTimingRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiCurrentTimingRef.setStatus("current")


class _EsiRequestedTimingRef_Type(Integer32):
    """Custom type esiRequestedTimingRef based on Integer32"""
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
        *(("requestAutomatic", 4),
          ("requestBits", 5),
          ("requestFreeRun", 1),
          ("requestPrimary", 2),
          ("requestSecondary", 3))
    )


_EsiRequestedTimingRef_Type.__name__ = "Integer32"
_EsiRequestedTimingRef_Object = MibTableColumn
esiRequestedTimingRef = _EsiRequestedTimingRef_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 3),
    _EsiRequestedTimingRef_Type()
)
esiRequestedTimingRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiRequestedTimingRef.setStatus("current")
_EsiPrimaryRefSource_Type = EsiReferenceSource
_EsiPrimaryRefSource_Object = MibTableColumn
esiPrimaryRefSource = _EsiPrimaryRefSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 4),
    _EsiPrimaryRefSource_Type()
)
esiPrimaryRefSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiPrimaryRefSource.setStatus("current")
_EsiSecondaryRefSource_Type = EsiReferenceSource
_EsiSecondaryRefSource_Object = MibTableColumn
esiSecondaryRefSource = _EsiSecondaryRefSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 5),
    _EsiSecondaryRefSource_Type()
)
esiSecondaryRefSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiSecondaryRefSource.setStatus("current")
_EsiCurrentFaultBits_Type = Integer32
_EsiCurrentFaultBits_Object = MibTableColumn
esiCurrentFaultBits = _EsiCurrentFaultBits_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 6),
    _EsiCurrentFaultBits_Type()
)
esiCurrentFaultBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiCurrentFaultBits.setStatus("current")


class _EsiBitsFramingFormat_Type(Integer32):
    """Custom type esiBitsFramingFormat based on Integer32"""
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
        *(("d4", 1),
          ("esf", 2),
          ("fas", 5),
          ("fascrc4", 6),
          ("mfas", 3),
          ("mfascrc4", 4))
    )


_EsiBitsFramingFormat_Type.__name__ = "Integer32"
_EsiBitsFramingFormat_Object = MibTableColumn
esiBitsFramingFormat = _EsiBitsFramingFormat_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 7),
    _EsiBitsFramingFormat_Type()
)
esiBitsFramingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiBitsFramingFormat.setStatus("current")


class _EsiBitsCodingFormat_Type(Integer32):
    """Custom type esiBitsCodingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_EsiBitsCodingFormat_Type.__name__ = "Integer32"
_EsiBitsCodingFormat_Object = MibTableColumn
esiBitsCodingFormat = _EsiBitsCodingFormat_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 8),
    _EsiBitsCodingFormat_Type()
)
esiBitsCodingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiBitsCodingFormat.setStatus("current")


class _EsiBitsOutputLevel_Type(Integer32):
    """Custom type esiBitsOutputLevel based on Integer32"""
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
        *(("esiDs1Level0-6", 1),
          ("esiDs1Level1-2", 2),
          ("esiDs1Level1-8", 3),
          ("esiDs1Level2-4", 4),
          ("esiDs1Level3-0", 5))
    )


_EsiBitsOutputLevel_Type.__name__ = "Integer32"
_EsiBitsOutputLevel_Object = MibTableColumn
esiBitsOutputLevel = _EsiBitsOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 9),
    _EsiBitsOutputLevel_Type()
)
esiBitsOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiBitsOutputLevel.setStatus("current")


class _EsiRevertiveSwitching_Type(Integer32):
    """Custom type esiRevertiveSwitching based on Integer32"""
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


_EsiRevertiveSwitching_Type.__name__ = "Integer32"
_EsiRevertiveSwitching_Object = MibTableColumn
esiRevertiveSwitching = _EsiRevertiveSwitching_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 10),
    _EsiRevertiveSwitching_Type()
)
esiRevertiveSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiRevertiveSwitching.setStatus("current")
_EsiRevertiveDelay_Type = TimeInterval
_EsiRevertiveDelay_Object = MibTableColumn
esiRevertiveDelay = _EsiRevertiveDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 11),
    _EsiRevertiveDelay_Type()
)
esiRevertiveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiRevertiveDelay.setStatus("current")
_EsiSwitchingDelay_Type = TimeInterval
_EsiSwitchingDelay_Object = MibTableColumn
esiSwitchingDelay = _EsiSwitchingDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 1, 1, 12),
    _EsiSwitchingDelay_Type()
)
esiSwitchingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiSwitchingDelay.setStatus("current")
_EsiReferenceTable_Object = MibTable
esiReferenceTable = _EsiReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    esiReferenceTable.setStatus("current")
_EsiReferenceEntry_Object = MibTableRow
esiReferenceEntry = _EsiReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 2, 1)
)
esiReferenceEntry.setIndexNames(
    (0, "Fore-TCM-MIB", "esiCardIndex"),
    (0, "Fore-TCM-MIB", "esiRefSource"),
)
if mibBuilder.loadTexts:
    esiReferenceEntry.setStatus("current")
_EsiRefSource_Type = EsiReferenceSource
_EsiRefSource_Object = MibTableColumn
esiRefSource = _EsiRefSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 2, 1, 1),
    _EsiRefSource_Type()
)
esiRefSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiRefSource.setStatus("current")
_EsiRefSourceText_Type = DisplayString
_EsiRefSourceText_Object = MibTableColumn
esiRefSourceText = _EsiRefSourceText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 2, 1, 2),
    _EsiRefSourceText_Type()
)
esiRefSourceText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiRefSourceText.setStatus("current")


class _EsiRefSourceStatus_Type(Integer32):
    """Custom type esiRefSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_EsiRefSourceStatus_Type.__name__ = "Integer32"
_EsiRefSourceStatus_Object = MibTableColumn
esiRefSourceStatus = _EsiRefSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 2, 1, 3),
    _EsiRefSourceStatus_Type()
)
esiRefSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esiRefSourceStatus.setStatus("current")


class _EsiRefSourceAdminStatus_Type(Integer32):
    """Custom type esiRefSourceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EsiRefSourceAdminStatus_Type.__name__ = "Integer32"
_EsiRefSourceAdminStatus_Object = MibTableColumn
esiRefSourceAdminStatus = _EsiRefSourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 2, 1, 4),
    _EsiRefSourceAdminStatus_Type()
)
esiRefSourceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiRefSourceAdminStatus.setStatus("current")


class _EsiRefSourceQualStatus_Type(Integer32):
    """Custom type esiRefSourceQualStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_EsiRefSourceQualStatus_Type.__name__ = "Integer32"
_EsiRefSourceQualStatus_Object = MibTableColumn
esiRefSourceQualStatus = _EsiRefSourceQualStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 8, 2, 2, 1, 5),
    _EsiRefSourceQualStatus_Type()
)
esiRefSourceQualStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esiRefSourceQualStatus.setStatus("current")

# Managed Objects groups


# Notification objects

ecpOperatingModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1050)
)
ecpOperatingModeChange.setObjects(
      *(("Fore-TCM-MIB", "ecpBoardIndex"),
        ("Fore-TCM-MIB", "ecpOperatingStatus"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    ecpOperatingModeChange.setStatus(
        "current"
    )

esiTimingSourceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1051)
)
esiTimingSourceChange.setObjects(
      *(("Fore-TCM-MIB", "esiCardIndex"),
        ("Fore-TCM-MIB", "esiCurrentTimingRef"),
        ("Fore-TCM-MIB", "esiRefSource"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    esiTimingSourceChange.setStatus(
        "current"
    )

esiTimingSourceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1052)
)
esiTimingSourceFailed.setObjects(
      *(("Fore-TCM-MIB", "esiCardIndex"),
        ("Fore-TCM-MIB", "esiCurrentTimingRef"),
        ("Fore-TCM-MIB", "esiRefSource"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    esiTimingSourceFailed.setStatus(
        "current"
    )

ecpStandbyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 1076)
)
ecpStandbyFailed.setObjects(
      *(("Fore-TCM-MIB", "ecpBoardIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    ecpStandbyFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-TCM-MIB",
    **{"EsiReferenceSource": EsiReferenceSource,
       "ecpOperatingModeChange": ecpOperatingModeChange,
       "esiTimingSourceChange": esiTimingSourceChange,
       "esiTimingSourceFailed": esiTimingSourceFailed,
       "ecpStandbyFailed": ecpStandbyFailed,
       "ecpStationModule": ecpStationModule,
       "ecpHardware": ecpHardware,
       "ecpBoardTable": ecpBoardTable,
       "ecpBoardEntry": ecpBoardEntry,
       "ecpBoardIndex": ecpBoardIndex,
       "ecpBoardVersion": ecpBoardVersion,
       "ecpBoardSerialNumber": ecpBoardSerialNumber,
       "ecpBoardOtherEcpPresent": ecpBoardOtherEcpPresent,
       "ecpBoardEsiPresent": ecpBoardEsiPresent,
       "ecpSerialIfTable": ecpSerialIfTable,
       "ecpSerialIfEntry": ecpSerialIfEntry,
       "ecpSerialIfPortIndex": ecpSerialIfPortIndex,
       "ecpSerialIfPortType": ecpSerialIfPortType,
       "ecpSerialIfPortSpeed": ecpSerialIfPortSpeed,
       "ecpSerialIfFlowType": ecpSerialIfFlowType,
       "ecpSerialIfPortBits": ecpSerialIfPortBits,
       "ecpSerialIfPortStopBits": ecpSerialIfPortStopBits,
       "ecpSerialIfPortParity": ecpSerialIfPortParity,
       "ecpEnvironment": ecpEnvironment,
       "ecpAlarmGroup": ecpAlarmGroup,
       "ecpAlarmTable": ecpAlarmTable,
       "ecpAlarmEntry": ecpAlarmEntry,
       "ecpAlarmType": ecpAlarmType,
       "ecpAlarmStatus": ecpAlarmStatus,
       "ecpAlarmMinorCategory": ecpAlarmMinorCategory,
       "ecpAlarmMajorCategory": ecpAlarmMajorCategory,
       "ecpAlarmReset": ecpAlarmReset,
       "ecpAlarmMajorRelayState": ecpAlarmMajorRelayState,
       "ecpAlarmMinorRelayState": ecpAlarmMinorRelayState,
       "ecpAlarmRelayTable": ecpAlarmRelayTable,
       "ecpAlarmRelayEntry": ecpAlarmRelayEntry,
       "ecpAlarmRelayIndex": ecpAlarmRelayIndex,
       "ecpAlarmRelayFunction": ecpAlarmRelayFunction,
       "ecpAlarmRelayState": ecpAlarmRelayState,
       "ecpSoftware": ecpSoftware,
       "ecpSwMainGroup": ecpSwMainGroup,
       "ecpSwMainTable": ecpSwMainTable,
       "ecpSwMainEntry": ecpSwMainEntry,
       "ecpName": ecpName,
       "ecpHardwareVersion": ecpHardwareVersion,
       "ecpSoftwareVersion": ecpSoftwareVersion,
       "ecpSoftwareVersionText": ecpSoftwareVersionText,
       "ecpType": ecpType,
       "ecpOperatingStatus": ecpOperatingStatus,
       "ecpProtocolType": ecpProtocolType,
       "ecpTimeZone": ecpTimeZone,
       "ecpGMTime": ecpGMTime,
       "ecpUptime": ecpUptime,
       "ecpModeChangeTime": ecpModeChangeTime,
       "ecpOtherEcpStatus": ecpOtherEcpStatus,
       "ecpExternalInput1": ecpExternalInput1,
       "ecpExternalInput2": ecpExternalInput2,
       "ecpExternalInput3": ecpExternalInput3,
       "ecpExternalInput4": ecpExternalInput4,
       "ecpExternalInput5": ecpExternalInput5,
       "ecpIpGroup": ecpIpGroup,
       "ecpNetIfTable": ecpNetIfTable,
       "ecpNetIfEntry": ecpNetIfEntry,
       "ecpNetIfIndex": ecpNetIfIndex,
       "ecpNetIfDescr": ecpNetIfDescr,
       "ecpNetIfPhysAddress": ecpNetIfPhysAddress,
       "ecpNetIfAdminStatus": ecpNetIfAdminStatus,
       "ecpNetIfOperStatus": ecpNetIfOperStatus,
       "ecpNetIfLastChange": ecpNetIfLastChange,
       "ecpNetIfIpAddr": ecpNetIfIpAddr,
       "ecpNetIfIpMask": ecpNetIfIpMask,
       "ecpNetIfIpBcastAddr": ecpNetIfIpBcastAddr,
       "ecpNetIfStatsTable": ecpNetIfStatsTable,
       "ecpNetIfStatsEntry": ecpNetIfStatsEntry,
       "ecpNetIfInOctets": ecpNetIfInOctets,
       "ecpNetIfInUcastPkts": ecpNetIfInUcastPkts,
       "ecpNetIfInNUcastPkts": ecpNetIfInNUcastPkts,
       "ecpNetIfInDiscards": ecpNetIfInDiscards,
       "ecpNetIfInErrors": ecpNetIfInErrors,
       "ecpNetIfInUnknownProtos": ecpNetIfInUnknownProtos,
       "ecpNetIfOutOctets": ecpNetIfOutOctets,
       "ecpNetIfOutUcastPkts": ecpNetIfOutUcastPkts,
       "ecpNetIfOutNUcastPkts": ecpNetIfOutNUcastPkts,
       "ecpNetIfOutDiscards": ecpNetIfOutDiscards,
       "ecpNetIfOutErrors": ecpNetIfOutErrors,
       "ecpNetIfOutQLen": ecpNetIfOutQLen,
       "ecpIpStatsTable": ecpIpStatsTable,
       "ecpIpStatsEntry": ecpIpStatsEntry,
       "ecpIpInReceives": ecpIpInReceives,
       "ecpIpInHdrErrors": ecpIpInHdrErrors,
       "ecpIpInAddrErrors": ecpIpInAddrErrors,
       "ecpIpForwDatagrams": ecpIpForwDatagrams,
       "ecpIpInUnknownProtos": ecpIpInUnknownProtos,
       "ecpIpInDiscards": ecpIpInDiscards,
       "ecpIpInDelivers": ecpIpInDelivers,
       "ecpIpOutRequests": ecpIpOutRequests,
       "ecpIpOutDiscards": ecpIpOutDiscards,
       "ecpIpOutNoRoutes": ecpIpOutNoRoutes,
       "ecpIpReasmReqds": ecpIpReasmReqds,
       "ecpIpReasmOKs": ecpIpReasmOKs,
       "ecpIpReasmFails": ecpIpReasmFails,
       "ecpIpFragOKs": ecpIpFragOKs,
       "ecpIpFragFails": ecpIpFragFails,
       "ecpIpFragCreates": ecpIpFragCreates,
       "ecpIpRouteTable": ecpIpRouteTable,
       "ecpIpRouteEntry": ecpIpRouteEntry,
       "ecpIpRouteDest": ecpIpRouteDest,
       "ecpIpRouteIfIndex": ecpIpRouteIfIndex,
       "ecpIpRouteNextHop": ecpIpRouteNextHop,
       "ecpIpRouteMetric1": ecpIpRouteMetric1,
       "ecpIpRouteType": ecpIpRouteType,
       "ecpIpRouteMask": ecpIpRouteMask,
       "ecpIcmpStatsTable": ecpIcmpStatsTable,
       "ecpIcmpStatsEntry": ecpIcmpStatsEntry,
       "ecpIcmpInMsgs": ecpIcmpInMsgs,
       "ecpIcmpInErrors": ecpIcmpInErrors,
       "ecpIcmpInDestUnreach": ecpIcmpInDestUnreach,
       "ecpIcmpInTimeExcds": ecpIcmpInTimeExcds,
       "ecpIcmpInParmProbs": ecpIcmpInParmProbs,
       "ecpIcmpInSrcQuenchs": ecpIcmpInSrcQuenchs,
       "ecpIcmpInRedirects": ecpIcmpInRedirects,
       "ecpIcmpInEchos": ecpIcmpInEchos,
       "ecpIcmpInEchoReps": ecpIcmpInEchoReps,
       "ecpIcmpInTimestamps": ecpIcmpInTimestamps,
       "ecpIcmpInTimestampReps": ecpIcmpInTimestampReps,
       "ecpIcmpInaddrMasks": ecpIcmpInaddrMasks,
       "ecpIcmpInAddrMaskReps": ecpIcmpInAddrMaskReps,
       "ecpIcmpOutMsgs": ecpIcmpOutMsgs,
       "ecpIcmpOutErrors": ecpIcmpOutErrors,
       "ecpIcmpOutDestUnreachs": ecpIcmpOutDestUnreachs,
       "ecpIcmpOutTimeExcds": ecpIcmpOutTimeExcds,
       "ecpIcmpOutParmProbs": ecpIcmpOutParmProbs,
       "ecpIcmpOutSrcQuenchs": ecpIcmpOutSrcQuenchs,
       "ecpIcmpOutRedirects": ecpIcmpOutRedirects,
       "ecpIcmpOutEchos": ecpIcmpOutEchos,
       "ecpIcmpOutEchoReps": ecpIcmpOutEchoReps,
       "ecpIcmpOutTimestamps": ecpIcmpOutTimestamps,
       "ecpIcmpOutTimestampReps": ecpIcmpOutTimestampReps,
       "ecpIcmpOutAddrMasks": ecpIcmpOutAddrMasks,
       "ecpIcmpOutAddrMaskReps": ecpIcmpOutAddrMaskReps,
       "ecpTcpStatsTable": ecpTcpStatsTable,
       "ecpTcpStatsEntry": ecpTcpStatsEntry,
       "ecpTcpActiveOpens": ecpTcpActiveOpens,
       "ecpTcpPassiveOpens": ecpTcpPassiveOpens,
       "ecpTcpAttemptFails": ecpTcpAttemptFails,
       "ecpTcpEstabResets": ecpTcpEstabResets,
       "ecpTcpCurrEstab": ecpTcpCurrEstab,
       "ecpTcpInSegs": ecpTcpInSegs,
       "ecpTcpOutSegs": ecpTcpOutSegs,
       "ecpTcpRetransSegs": ecpTcpRetransSegs,
       "ecpUdpStatsTable": ecpUdpStatsTable,
       "ecpUdpStatsEntry": ecpUdpStatsEntry,
       "ecpUdpInDatagrams": ecpUdpInDatagrams,
       "ecpUdpNoPorts": ecpUdpNoPorts,
       "ecpUdpInErrors": ecpUdpInErrors,
       "ecpUdpOutDatagrams": ecpUdpOutDatagrams,
       "ecpIpConfigTable": ecpIpConfigTable,
       "ecpIpConfigEntry": ecpIpConfigEntry,
       "ecpIpForwarding": ecpIpForwarding,
       "ecpSnmp": ecpSnmp,
       "ecpTrapConfGroup": ecpTrapConfGroup,
       "ecpTrapNumberOfDest": ecpTrapNumberOfDest,
       "ecpTrapDestTable": ecpTrapDestTable,
       "ecpTrapDestEntry": ecpTrapDestEntry,
       "ecpTrapDest": ecpTrapDest,
       "ecpTrapDestStatus": ecpTrapDestStatus,
       "esiCard": esiCard,
       "esiHardware": esiHardware,
       "esiCardHwTable": esiCardHwTable,
       "esiCardHwEntry": esiCardHwEntry,
       "esiCardIndex": esiCardIndex,
       "esiHwCardType": esiHwCardType,
       "esiHwCardVersion": esiHwCardVersion,
       "esiHwPllStatus": esiHwPllStatus,
       "esiSoftware": esiSoftware,
       "esiCardSwTable": esiCardSwTable,
       "esiCardSwEntry": esiCardSwEntry,
       "esiOperationStatus": esiOperationStatus,
       "esiCurrentTimingRef": esiCurrentTimingRef,
       "esiRequestedTimingRef": esiRequestedTimingRef,
       "esiPrimaryRefSource": esiPrimaryRefSource,
       "esiSecondaryRefSource": esiSecondaryRefSource,
       "esiCurrentFaultBits": esiCurrentFaultBits,
       "esiBitsFramingFormat": esiBitsFramingFormat,
       "esiBitsCodingFormat": esiBitsCodingFormat,
       "esiBitsOutputLevel": esiBitsOutputLevel,
       "esiRevertiveSwitching": esiRevertiveSwitching,
       "esiRevertiveDelay": esiRevertiveDelay,
       "esiSwitchingDelay": esiSwitchingDelay,
       "esiReferenceTable": esiReferenceTable,
       "esiReferenceEntry": esiReferenceEntry,
       "esiRefSource": esiRefSource,
       "esiRefSourceText": esiRefSourceText,
       "esiRefSourceStatus": esiRefSourceStatus,
       "esiRefSourceAdminStatus": esiRefSourceAdminStatus,
       "esiRefSourceQualStatus": esiRefSourceQualStatus}
)
