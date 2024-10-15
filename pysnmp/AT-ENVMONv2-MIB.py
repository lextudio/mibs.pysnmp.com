# SNMP MIB module (AT-ENVMONv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-ENVMONv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:05 2024
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

(DisplayStringUnsized,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized")

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SYSINFO-MIB",
    "sysinfo")

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

atEnvMonv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12)
)
atEnvMonv2.setRevisions(
        ("2012-09-21 00:00",
         "2010-09-15 00:00",
         "2010-09-07 00:00",
         "2010-06-14 04:50",
         "2010-05-24 01:19",
         "2010-01-15 00:39",
         "2008-11-26 00:00",
         "2008-09-24 00:00",
         "2008-02-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtEnvMonv2PsbSensorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fanSpeedDiscrete", 1),
          ("psbSensorTypeInvalid", 0),
          ("temperatureDiscrete", 2),
          ("voltageDiscrete", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AtEnvMonv2Notifications_ObjectIdentity = ObjectIdentity
atEnvMonv2Notifications = _AtEnvMonv2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 0)
)
_AtEnvMonv2FanTable_Object = MibTable
atEnvMonv2FanTable = _AtEnvMonv2FanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 1)
)
if mibBuilder.loadTexts:
    atEnvMonv2FanTable.setStatus("current")
_AtEnvMonv2FanEntry_Object = MibTableRow
atEnvMonv2FanEntry = _AtEnvMonv2FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 1, 1)
)
atEnvMonv2FanEntry.setIndexNames(
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2FanStackMemberId"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2FanBoardIndex"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2FanIndex"),
)
if mibBuilder.loadTexts:
    atEnvMonv2FanEntry.setStatus("current")
_AtEnvMonv2FanStackMemberId_Type = Unsigned32
_AtEnvMonv2FanStackMemberId_Object = MibTableColumn
atEnvMonv2FanStackMemberId = _AtEnvMonv2FanStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 1, 1, 1),
    _AtEnvMonv2FanStackMemberId_Type()
)
atEnvMonv2FanStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FanStackMemberId.setStatus("current")
_AtEnvMonv2FanBoardIndex_Type = Unsigned32
_AtEnvMonv2FanBoardIndex_Object = MibTableColumn
atEnvMonv2FanBoardIndex = _AtEnvMonv2FanBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 1, 1, 2),
    _AtEnvMonv2FanBoardIndex_Type()
)
atEnvMonv2FanBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FanBoardIndex.setStatus("current")
_AtEnvMonv2FanIndex_Type = Unsigned32
_AtEnvMonv2FanIndex_Object = MibTableColumn
atEnvMonv2FanIndex = _AtEnvMonv2FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 1, 1, 3),
    _AtEnvMonv2FanIndex_Type()
)
atEnvMonv2FanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FanIndex.setStatus("current")


class _AtEnvMonv2FanDescription_Type(DisplayStringUnsized):
    """Custom type atEnvMonv2FanDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtEnvMonv2FanDescription_Type.__name__ = "DisplayStringUnsized"
_AtEnvMonv2FanDescription_Object = MibTableColumn
atEnvMonv2FanDescription = _AtEnvMonv2FanDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 1, 1, 4),
    _AtEnvMonv2FanDescription_Type()
)
atEnvMonv2FanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FanDescription.setStatus("current")
_AtEnvMonv2FanCurrentSpeed_Type = Unsigned32
_AtEnvMonv2FanCurrentSpeed_Object = MibTableColumn
atEnvMonv2FanCurrentSpeed = _AtEnvMonv2FanCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 1, 1, 5),
    _AtEnvMonv2FanCurrentSpeed_Type()
)
atEnvMonv2FanCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FanCurrentSpeed.setStatus("current")
_AtEnvMonv2FanLowerThreshold_Type = Unsigned32
_AtEnvMonv2FanLowerThreshold_Object = MibTableColumn
atEnvMonv2FanLowerThreshold = _AtEnvMonv2FanLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 1, 1, 6),
    _AtEnvMonv2FanLowerThreshold_Type()
)
atEnvMonv2FanLowerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FanLowerThreshold.setStatus("current")


class _AtEnvMonv2FanStatus_Type(Integer32):
    """Custom type atEnvMonv2FanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("good", 2))
    )


_AtEnvMonv2FanStatus_Type.__name__ = "Integer32"
_AtEnvMonv2FanStatus_Object = MibTableColumn
atEnvMonv2FanStatus = _AtEnvMonv2FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 1, 1, 7),
    _AtEnvMonv2FanStatus_Type()
)
atEnvMonv2FanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FanStatus.setStatus("current")
_AtEnvMonv2VoltageTable_Object = MibTable
atEnvMonv2VoltageTable = _AtEnvMonv2VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2)
)
if mibBuilder.loadTexts:
    atEnvMonv2VoltageTable.setStatus("current")
_AtEnvMonv2VoltageEntry_Object = MibTableRow
atEnvMonv2VoltageEntry = _AtEnvMonv2VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2, 1)
)
atEnvMonv2VoltageEntry.setIndexNames(
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2VoltageStackMemberId"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2VoltageBoardIndex"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2VoltageIndex"),
)
if mibBuilder.loadTexts:
    atEnvMonv2VoltageEntry.setStatus("current")
_AtEnvMonv2VoltageStackMemberId_Type = Unsigned32
_AtEnvMonv2VoltageStackMemberId_Object = MibTableColumn
atEnvMonv2VoltageStackMemberId = _AtEnvMonv2VoltageStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2, 1, 1),
    _AtEnvMonv2VoltageStackMemberId_Type()
)
atEnvMonv2VoltageStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2VoltageStackMemberId.setStatus("current")
_AtEnvMonv2VoltageBoardIndex_Type = Unsigned32
_AtEnvMonv2VoltageBoardIndex_Object = MibTableColumn
atEnvMonv2VoltageBoardIndex = _AtEnvMonv2VoltageBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2, 1, 2),
    _AtEnvMonv2VoltageBoardIndex_Type()
)
atEnvMonv2VoltageBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2VoltageBoardIndex.setStatus("current")
_AtEnvMonv2VoltageIndex_Type = Unsigned32
_AtEnvMonv2VoltageIndex_Object = MibTableColumn
atEnvMonv2VoltageIndex = _AtEnvMonv2VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2, 1, 3),
    _AtEnvMonv2VoltageIndex_Type()
)
atEnvMonv2VoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2VoltageIndex.setStatus("current")


class _AtEnvMonv2VoltageDescription_Type(DisplayStringUnsized):
    """Custom type atEnvMonv2VoltageDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtEnvMonv2VoltageDescription_Type.__name__ = "DisplayStringUnsized"
_AtEnvMonv2VoltageDescription_Object = MibTableColumn
atEnvMonv2VoltageDescription = _AtEnvMonv2VoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2, 1, 4),
    _AtEnvMonv2VoltageDescription_Type()
)
atEnvMonv2VoltageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2VoltageDescription.setStatus("current")
_AtEnvMonv2VoltageCurrent_Type = Integer32
_AtEnvMonv2VoltageCurrent_Object = MibTableColumn
atEnvMonv2VoltageCurrent = _AtEnvMonv2VoltageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2, 1, 5),
    _AtEnvMonv2VoltageCurrent_Type()
)
atEnvMonv2VoltageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2VoltageCurrent.setStatus("current")
_AtEnvMonv2VoltageUpperThreshold_Type = Integer32
_AtEnvMonv2VoltageUpperThreshold_Object = MibTableColumn
atEnvMonv2VoltageUpperThreshold = _AtEnvMonv2VoltageUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2, 1, 6),
    _AtEnvMonv2VoltageUpperThreshold_Type()
)
atEnvMonv2VoltageUpperThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2VoltageUpperThreshold.setStatus("current")
_AtEnvMonv2VoltageLowerThreshold_Type = Integer32
_AtEnvMonv2VoltageLowerThreshold_Object = MibTableColumn
atEnvMonv2VoltageLowerThreshold = _AtEnvMonv2VoltageLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2, 1, 7),
    _AtEnvMonv2VoltageLowerThreshold_Type()
)
atEnvMonv2VoltageLowerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2VoltageLowerThreshold.setStatus("current")


class _AtEnvMonv2VoltageStatus_Type(Integer32):
    """Custom type atEnvMonv2VoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inRange", 2),
          ("outOfRange", 1))
    )


_AtEnvMonv2VoltageStatus_Type.__name__ = "Integer32"
_AtEnvMonv2VoltageStatus_Object = MibTableColumn
atEnvMonv2VoltageStatus = _AtEnvMonv2VoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 2, 1, 8),
    _AtEnvMonv2VoltageStatus_Type()
)
atEnvMonv2VoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2VoltageStatus.setStatus("current")
_AtEnvMonv2TemperatureTable_Object = MibTable
atEnvMonv2TemperatureTable = _AtEnvMonv2TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 3)
)
if mibBuilder.loadTexts:
    atEnvMonv2TemperatureTable.setStatus("current")
_AtEnvMonv2TemperatureEntry_Object = MibTableRow
atEnvMonv2TemperatureEntry = _AtEnvMonv2TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 3, 1)
)
atEnvMonv2TemperatureEntry.setIndexNames(
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2TemperatureStackMemberId"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2TemperatureBoardIndex"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2TemperatureIndex"),
)
if mibBuilder.loadTexts:
    atEnvMonv2TemperatureEntry.setStatus("current")
_AtEnvMonv2TemperatureStackMemberId_Type = Unsigned32
_AtEnvMonv2TemperatureStackMemberId_Object = MibTableColumn
atEnvMonv2TemperatureStackMemberId = _AtEnvMonv2TemperatureStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 3, 1, 1),
    _AtEnvMonv2TemperatureStackMemberId_Type()
)
atEnvMonv2TemperatureStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2TemperatureStackMemberId.setStatus("current")
_AtEnvMonv2TemperatureBoardIndex_Type = Unsigned32
_AtEnvMonv2TemperatureBoardIndex_Object = MibTableColumn
atEnvMonv2TemperatureBoardIndex = _AtEnvMonv2TemperatureBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 3, 1, 2),
    _AtEnvMonv2TemperatureBoardIndex_Type()
)
atEnvMonv2TemperatureBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2TemperatureBoardIndex.setStatus("current")
_AtEnvMonv2TemperatureIndex_Type = Unsigned32
_AtEnvMonv2TemperatureIndex_Object = MibTableColumn
atEnvMonv2TemperatureIndex = _AtEnvMonv2TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 3, 1, 3),
    _AtEnvMonv2TemperatureIndex_Type()
)
atEnvMonv2TemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2TemperatureIndex.setStatus("current")


class _AtEnvMonv2TemperatureDescription_Type(DisplayStringUnsized):
    """Custom type atEnvMonv2TemperatureDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtEnvMonv2TemperatureDescription_Type.__name__ = "DisplayStringUnsized"
_AtEnvMonv2TemperatureDescription_Object = MibTableColumn
atEnvMonv2TemperatureDescription = _AtEnvMonv2TemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 3, 1, 4),
    _AtEnvMonv2TemperatureDescription_Type()
)
atEnvMonv2TemperatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2TemperatureDescription.setStatus("current")
_AtEnvMonv2TemperatureCurrent_Type = Integer32
_AtEnvMonv2TemperatureCurrent_Object = MibTableColumn
atEnvMonv2TemperatureCurrent = _AtEnvMonv2TemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 3, 1, 5),
    _AtEnvMonv2TemperatureCurrent_Type()
)
atEnvMonv2TemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2TemperatureCurrent.setStatus("current")
_AtEnvMonv2TemperatureUpperThreshold_Type = Integer32
_AtEnvMonv2TemperatureUpperThreshold_Object = MibTableColumn
atEnvMonv2TemperatureUpperThreshold = _AtEnvMonv2TemperatureUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 3, 1, 6),
    _AtEnvMonv2TemperatureUpperThreshold_Type()
)
atEnvMonv2TemperatureUpperThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2TemperatureUpperThreshold.setStatus("current")


class _AtEnvMonv2TemperatureStatus_Type(Integer32):
    """Custom type atEnvMonv2TemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inRange", 2),
          ("outOfRange", 1))
    )


_AtEnvMonv2TemperatureStatus_Type.__name__ = "Integer32"
_AtEnvMonv2TemperatureStatus_Object = MibTableColumn
atEnvMonv2TemperatureStatus = _AtEnvMonv2TemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 3, 1, 7),
    _AtEnvMonv2TemperatureStatus_Type()
)
atEnvMonv2TemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2TemperatureStatus.setStatus("current")
_AtEnvMonv2PsbObjects_ObjectIdentity = ObjectIdentity
atEnvMonv2PsbObjects = _AtEnvMonv2PsbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4)
)
_AtEnvMonv2PsbTable_Object = MibTable
atEnvMonv2PsbTable = _AtEnvMonv2PsbTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 1)
)
if mibBuilder.loadTexts:
    atEnvMonv2PsbTable.setStatus("current")
_AtEnvMonv2PsbEntry_Object = MibTableRow
atEnvMonv2PsbEntry = _AtEnvMonv2PsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 1, 1)
)
atEnvMonv2PsbEntry.setIndexNames(
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2PsbHostStackMemberId"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2PsbHostBoardIndex"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2PsbHostSlotIndex"),
)
if mibBuilder.loadTexts:
    atEnvMonv2PsbEntry.setStatus("current")
_AtEnvMonv2PsbHostStackMemberId_Type = Unsigned32
_AtEnvMonv2PsbHostStackMemberId_Object = MibTableColumn
atEnvMonv2PsbHostStackMemberId = _AtEnvMonv2PsbHostStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 1, 1, 1),
    _AtEnvMonv2PsbHostStackMemberId_Type()
)
atEnvMonv2PsbHostStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbHostStackMemberId.setStatus("current")
_AtEnvMonv2PsbHostBoardIndex_Type = Unsigned32
_AtEnvMonv2PsbHostBoardIndex_Object = MibTableColumn
atEnvMonv2PsbHostBoardIndex = _AtEnvMonv2PsbHostBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 1, 1, 2),
    _AtEnvMonv2PsbHostBoardIndex_Type()
)
atEnvMonv2PsbHostBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbHostBoardIndex.setStatus("current")
_AtEnvMonv2PsbHostSlotIndex_Type = Unsigned32
_AtEnvMonv2PsbHostSlotIndex_Object = MibTableColumn
atEnvMonv2PsbHostSlotIndex = _AtEnvMonv2PsbHostSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 1, 1, 3),
    _AtEnvMonv2PsbHostSlotIndex_Type()
)
atEnvMonv2PsbHostSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbHostSlotIndex.setStatus("current")
_AtEnvMonv2PsbHeldBoardIndex_Type = Unsigned32
_AtEnvMonv2PsbHeldBoardIndex_Object = MibTableColumn
atEnvMonv2PsbHeldBoardIndex = _AtEnvMonv2PsbHeldBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 1, 1, 4),
    _AtEnvMonv2PsbHeldBoardIndex_Type()
)
atEnvMonv2PsbHeldBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbHeldBoardIndex.setStatus("current")
_AtEnvMonv2PsbHeldBoardId_Type = ObjectIdentifier
_AtEnvMonv2PsbHeldBoardId_Object = MibTableColumn
atEnvMonv2PsbHeldBoardId = _AtEnvMonv2PsbHeldBoardId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 1, 1, 5),
    _AtEnvMonv2PsbHeldBoardId_Type()
)
atEnvMonv2PsbHeldBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbHeldBoardId.setStatus("current")


class _AtEnvMonv2PsbDescription_Type(DisplayStringUnsized):
    """Custom type atEnvMonv2PsbDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtEnvMonv2PsbDescription_Type.__name__ = "DisplayStringUnsized"
_AtEnvMonv2PsbDescription_Object = MibTableColumn
atEnvMonv2PsbDescription = _AtEnvMonv2PsbDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 1, 1, 6),
    _AtEnvMonv2PsbDescription_Type()
)
atEnvMonv2PsbDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbDescription.setStatus("current")
_AtEnvMonv2PsbSensorTable_Object = MibTable
atEnvMonv2PsbSensorTable = _AtEnvMonv2PsbSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 2)
)
if mibBuilder.loadTexts:
    atEnvMonv2PsbSensorTable.setStatus("current")
_AtEnvMonv2PsbSensorEntry_Object = MibTableRow
atEnvMonv2PsbSensorEntry = _AtEnvMonv2PsbSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 2, 1)
)
atEnvMonv2PsbSensorEntry.setIndexNames(
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorStackMemberId"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorBoardIndex"),
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorIndex"),
)
if mibBuilder.loadTexts:
    atEnvMonv2PsbSensorEntry.setStatus("current")
_AtEnvMonv2PsbSensorStackMemberId_Type = Unsigned32
_AtEnvMonv2PsbSensorStackMemberId_Object = MibTableColumn
atEnvMonv2PsbSensorStackMemberId = _AtEnvMonv2PsbSensorStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 2, 1, 1),
    _AtEnvMonv2PsbSensorStackMemberId_Type()
)
atEnvMonv2PsbSensorStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbSensorStackMemberId.setStatus("current")
_AtEnvMonv2PsbSensorBoardIndex_Type = Unsigned32
_AtEnvMonv2PsbSensorBoardIndex_Object = MibTableColumn
atEnvMonv2PsbSensorBoardIndex = _AtEnvMonv2PsbSensorBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 2, 1, 2),
    _AtEnvMonv2PsbSensorBoardIndex_Type()
)
atEnvMonv2PsbSensorBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbSensorBoardIndex.setStatus("current")
_AtEnvMonv2PsbSensorIndex_Type = Unsigned32
_AtEnvMonv2PsbSensorIndex_Object = MibTableColumn
atEnvMonv2PsbSensorIndex = _AtEnvMonv2PsbSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 2, 1, 3),
    _AtEnvMonv2PsbSensorIndex_Type()
)
atEnvMonv2PsbSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbSensorIndex.setStatus("current")
_AtEnvMonv2PsbSensorType_Type = AtEnvMonv2PsbSensorType
_AtEnvMonv2PsbSensorType_Object = MibTableColumn
atEnvMonv2PsbSensorType = _AtEnvMonv2PsbSensorType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 2, 1, 4),
    _AtEnvMonv2PsbSensorType_Type()
)
atEnvMonv2PsbSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbSensorType.setStatus("current")


class _AtEnvMonv2PsbSensorDescription_Type(DisplayStringUnsized):
    """Custom type atEnvMonv2PsbSensorDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AtEnvMonv2PsbSensorDescription_Type.__name__ = "DisplayStringUnsized"
_AtEnvMonv2PsbSensorDescription_Object = MibTableColumn
atEnvMonv2PsbSensorDescription = _AtEnvMonv2PsbSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 2, 1, 5),
    _AtEnvMonv2PsbSensorDescription_Type()
)
atEnvMonv2PsbSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbSensorDescription.setStatus("current")


class _AtEnvMonv2PsbSensorStatus_Type(Integer32):
    """Custom type atEnvMonv2PsbSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("good", 2),
          ("notPowered", 3))
    )


_AtEnvMonv2PsbSensorStatus_Type.__name__ = "Integer32"
_AtEnvMonv2PsbSensorStatus_Object = MibTableColumn
atEnvMonv2PsbSensorStatus = _AtEnvMonv2PsbSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 2, 1, 6),
    _AtEnvMonv2PsbSensorStatus_Type()
)
atEnvMonv2PsbSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbSensorStatus.setStatus("current")


class _AtEnvMonv2PsbSensorReading_Type(Integer32):
    """Custom type atEnvMonv2PsbSensorReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtEnvMonv2PsbSensorReading_Type.__name__ = "Integer32"
_AtEnvMonv2PsbSensorReading_Object = MibTableColumn
atEnvMonv2PsbSensorReading = _AtEnvMonv2PsbSensorReading_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 4, 2, 1, 7),
    _AtEnvMonv2PsbSensorReading_Type()
)
atEnvMonv2PsbSensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2PsbSensorReading.setStatus("current")
_AtEnvMonv2Traps_ObjectIdentity = ObjectIdentity
atEnvMonv2Traps = _AtEnvMonv2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 5)
)
_AtEnvMonv2FaultLedTable_Object = MibTable
atEnvMonv2FaultLedTable = _AtEnvMonv2FaultLedTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 6)
)
if mibBuilder.loadTexts:
    atEnvMonv2FaultLedTable.setStatus("current")
_AtEnvMonv2FaultLedEntry_Object = MibTableRow
atEnvMonv2FaultLedEntry = _AtEnvMonv2FaultLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 6, 1)
)
atEnvMonv2FaultLedEntry.setIndexNames(
    (0, "AT-ENVMONv2-MIB", "atEnvMonv2FaultLedStackMemberId"),
)
if mibBuilder.loadTexts:
    atEnvMonv2FaultLedEntry.setStatus("current")
_AtEnvMonv2FaultLedStackMemberId_Type = Unsigned32
_AtEnvMonv2FaultLedStackMemberId_Object = MibTableColumn
atEnvMonv2FaultLedStackMemberId = _AtEnvMonv2FaultLedStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 6, 1, 1),
    _AtEnvMonv2FaultLedStackMemberId_Type()
)
atEnvMonv2FaultLedStackMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FaultLedStackMemberId.setStatus("current")


class _AtEnvMonv2FaultLed1Flash_Type(Integer32):
    """Custom type atEnvMonv2FaultLed1Flash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("heatsinkFanFailure", 1),
          ("noFault", 2))
    )


_AtEnvMonv2FaultLed1Flash_Type.__name__ = "Integer32"
_AtEnvMonv2FaultLed1Flash_Object = MibTableColumn
atEnvMonv2FaultLed1Flash = _AtEnvMonv2FaultLed1Flash_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 6, 1, 2),
    _AtEnvMonv2FaultLed1Flash_Type()
)
atEnvMonv2FaultLed1Flash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FaultLed1Flash.setStatus("current")


class _AtEnvMonv2FaultLed2Flashes_Type(Integer32):
    """Custom type atEnvMonv2FaultLed2Flashes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chassisFanFailure", 1),
          ("noFault", 2))
    )


_AtEnvMonv2FaultLed2Flashes_Type.__name__ = "Integer32"
_AtEnvMonv2FaultLed2Flashes_Object = MibTableColumn
atEnvMonv2FaultLed2Flashes = _AtEnvMonv2FaultLed2Flashes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 6, 1, 3),
    _AtEnvMonv2FaultLed2Flashes_Type()
)
atEnvMonv2FaultLed2Flashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FaultLed2Flashes.setStatus("current")


class _AtEnvMonv2FaultLed3Flashes_Type(Integer32):
    """Custom type atEnvMonv2FaultLed3Flashes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noFault", 2),
          ("sensorFailure", 1))
    )


_AtEnvMonv2FaultLed3Flashes_Type.__name__ = "Integer32"
_AtEnvMonv2FaultLed3Flashes_Object = MibTableColumn
atEnvMonv2FaultLed3Flashes = _AtEnvMonv2FaultLed3Flashes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 6, 1, 4),
    _AtEnvMonv2FaultLed3Flashes_Type()
)
atEnvMonv2FaultLed3Flashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FaultLed3Flashes.setStatus("current")


class _AtEnvMonv2FaultLed4Flashes_Type(Integer32):
    """Custom type atEnvMonv2FaultLed4Flashes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noFault", 2),
          ("xemInitialisationFailure", 1))
    )


_AtEnvMonv2FaultLed4Flashes_Type.__name__ = "Integer32"
_AtEnvMonv2FaultLed4Flashes_Object = MibTableColumn
atEnvMonv2FaultLed4Flashes = _AtEnvMonv2FaultLed4Flashes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 6, 1, 5),
    _AtEnvMonv2FaultLed4Flashes_Type()
)
atEnvMonv2FaultLed4Flashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FaultLed4Flashes.setStatus("current")


class _AtEnvMonv2FaultLed5Flashes_Type(Integer32):
    """Custom type atEnvMonv2FaultLed5Flashes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("noFault", 2)
    )


_AtEnvMonv2FaultLed5Flashes_Type.__name__ = "Integer32"
_AtEnvMonv2FaultLed5Flashes_Object = MibTableColumn
atEnvMonv2FaultLed5Flashes = _AtEnvMonv2FaultLed5Flashes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 6, 1, 6),
    _AtEnvMonv2FaultLed5Flashes_Type()
)
atEnvMonv2FaultLed5Flashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FaultLed5Flashes.setStatus("current")


class _AtEnvMonv2FaultLed6Flashes_Type(Integer32):
    """Custom type atEnvMonv2FaultLed6Flashes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noFault", 2),
          ("temperatureFailure", 1))
    )


_AtEnvMonv2FaultLed6Flashes_Type.__name__ = "Integer32"
_AtEnvMonv2FaultLed6Flashes_Object = MibTableColumn
atEnvMonv2FaultLed6Flashes = _AtEnvMonv2FaultLed6Flashes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 6, 1, 7),
    _AtEnvMonv2FaultLed6Flashes_Type()
)
atEnvMonv2FaultLed6Flashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEnvMonv2FaultLed6Flashes.setStatus("current")

# Managed Objects groups


# Notification objects

atEnvMonv2FanAlarmSetNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 0, 1)
)
atEnvMonv2FanAlarmSetNotify.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2FanStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanLowerThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanCurrentSpeed"))
)
if mibBuilder.loadTexts:
    atEnvMonv2FanAlarmSetNotify.setStatus(
        "current"
    )

atEnvMonv2FanAlarmClearedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 0, 2)
)
atEnvMonv2FanAlarmClearedNotify.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2FanStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanLowerThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanCurrentSpeed"))
)
if mibBuilder.loadTexts:
    atEnvMonv2FanAlarmClearedNotify.setStatus(
        "current"
    )

atEnvMonv2VoltAlarmSetNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 0, 3)
)
atEnvMonv2VoltAlarmSetNotify.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2VoltageStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageUpperThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageLowerThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageCurrent"))
)
if mibBuilder.loadTexts:
    atEnvMonv2VoltAlarmSetNotify.setStatus(
        "current"
    )

atEnvMonv2VoltAlarmClearedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 0, 4)
)
atEnvMonv2VoltAlarmClearedNotify.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2VoltageStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageUpperThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageLowerThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageCurrent"))
)
if mibBuilder.loadTexts:
    atEnvMonv2VoltAlarmClearedNotify.setStatus(
        "current"
    )

atEnvMonv2TempAlarmSetNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 0, 5)
)
atEnvMonv2TempAlarmSetNotify.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureUpperThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureCurrent"))
)
if mibBuilder.loadTexts:
    atEnvMonv2TempAlarmSetNotify.setStatus(
        "current"
    )

atEnvMonv2TempAlarmClearedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 0, 6)
)
atEnvMonv2TempAlarmClearedNotify.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureUpperThreshold"))
)
if mibBuilder.loadTexts:
    atEnvMonv2TempAlarmClearedNotify.setStatus(
        "current"
    )

atEnvMonv2PsbAlarmSetNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 0, 7)
)
atEnvMonv2PsbAlarmSetNotify.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorType"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorDescription"))
)
if mibBuilder.loadTexts:
    atEnvMonv2PsbAlarmSetNotify.setStatus(
        "current"
    )

atEnvMonv2PsbAlarmClearedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 0, 8)
)
atEnvMonv2PsbAlarmClearedNotify.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorType"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorDescription"))
)
if mibBuilder.loadTexts:
    atEnvMonv2PsbAlarmClearedNotify.setStatus(
        "current"
    )

atEnvMonv2FanAlarmSetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 5, 1)
)
atEnvMonv2FanAlarmSetEvent.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2FanStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanLowerThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanCurrentSpeed"))
)
if mibBuilder.loadTexts:
    atEnvMonv2FanAlarmSetEvent.setStatus(
        "deprecated"
    )

atEnvMonv2FanAlarmClearedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 5, 2)
)
atEnvMonv2FanAlarmClearedEvent.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2FanStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanLowerThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2FanCurrentSpeed"))
)
if mibBuilder.loadTexts:
    atEnvMonv2FanAlarmClearedEvent.setStatus(
        "deprecated"
    )

atEnvMonv2VoltAlarmSetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 5, 3)
)
atEnvMonv2VoltAlarmSetEvent.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2VoltageStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageUpperThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageLowerThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageCurrent"))
)
if mibBuilder.loadTexts:
    atEnvMonv2VoltAlarmSetEvent.setStatus(
        "deprecated"
    )

atEnvMonv2VoltAlarmClearedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 5, 4)
)
atEnvMonv2VoltAlarmClearedEvent.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2VoltageStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageUpperThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageLowerThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2VoltageCurrent"))
)
if mibBuilder.loadTexts:
    atEnvMonv2VoltAlarmClearedEvent.setStatus(
        "deprecated"
    )

atEnvMonv2TempAlarmSetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 5, 5)
)
atEnvMonv2TempAlarmSetEvent.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureUpperThreshold"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureCurrent"))
)
if mibBuilder.loadTexts:
    atEnvMonv2TempAlarmSetEvent.setStatus(
        "deprecated"
    )

atEnvMonv2TempAlarmClearedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 5, 6)
)
atEnvMonv2TempAlarmClearedEvent.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureDescription"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2TemperatureUpperThreshold"))
)
if mibBuilder.loadTexts:
    atEnvMonv2TempAlarmClearedEvent.setStatus(
        "deprecated"
    )

atEnvMonv2PsbAlarmSetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 5, 7)
)
atEnvMonv2PsbAlarmSetEvent.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorType"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorDescription"))
)
if mibBuilder.loadTexts:
    atEnvMonv2PsbAlarmSetEvent.setStatus(
        "deprecated"
    )

atEnvMonv2PsbAlarmClearedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 12, 5, 8)
)
atEnvMonv2PsbAlarmClearedEvent.setObjects(
      *(("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorStackMemberId"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorBoardIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorIndex"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorType"),
        ("AT-ENVMONv2-MIB", "atEnvMonv2PsbSensorDescription"))
)
if mibBuilder.loadTexts:
    atEnvMonv2PsbAlarmClearedEvent.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-ENVMONv2-MIB",
    **{"AtEnvMonv2PsbSensorType": AtEnvMonv2PsbSensorType,
       "atEnvMonv2": atEnvMonv2,
       "atEnvMonv2Notifications": atEnvMonv2Notifications,
       "atEnvMonv2FanAlarmSetNotify": atEnvMonv2FanAlarmSetNotify,
       "atEnvMonv2FanAlarmClearedNotify": atEnvMonv2FanAlarmClearedNotify,
       "atEnvMonv2VoltAlarmSetNotify": atEnvMonv2VoltAlarmSetNotify,
       "atEnvMonv2VoltAlarmClearedNotify": atEnvMonv2VoltAlarmClearedNotify,
       "atEnvMonv2TempAlarmSetNotify": atEnvMonv2TempAlarmSetNotify,
       "atEnvMonv2TempAlarmClearedNotify": atEnvMonv2TempAlarmClearedNotify,
       "atEnvMonv2PsbAlarmSetNotify": atEnvMonv2PsbAlarmSetNotify,
       "atEnvMonv2PsbAlarmClearedNotify": atEnvMonv2PsbAlarmClearedNotify,
       "atEnvMonv2FanTable": atEnvMonv2FanTable,
       "atEnvMonv2FanEntry": atEnvMonv2FanEntry,
       "atEnvMonv2FanStackMemberId": atEnvMonv2FanStackMemberId,
       "atEnvMonv2FanBoardIndex": atEnvMonv2FanBoardIndex,
       "atEnvMonv2FanIndex": atEnvMonv2FanIndex,
       "atEnvMonv2FanDescription": atEnvMonv2FanDescription,
       "atEnvMonv2FanCurrentSpeed": atEnvMonv2FanCurrentSpeed,
       "atEnvMonv2FanLowerThreshold": atEnvMonv2FanLowerThreshold,
       "atEnvMonv2FanStatus": atEnvMonv2FanStatus,
       "atEnvMonv2VoltageTable": atEnvMonv2VoltageTable,
       "atEnvMonv2VoltageEntry": atEnvMonv2VoltageEntry,
       "atEnvMonv2VoltageStackMemberId": atEnvMonv2VoltageStackMemberId,
       "atEnvMonv2VoltageBoardIndex": atEnvMonv2VoltageBoardIndex,
       "atEnvMonv2VoltageIndex": atEnvMonv2VoltageIndex,
       "atEnvMonv2VoltageDescription": atEnvMonv2VoltageDescription,
       "atEnvMonv2VoltageCurrent": atEnvMonv2VoltageCurrent,
       "atEnvMonv2VoltageUpperThreshold": atEnvMonv2VoltageUpperThreshold,
       "atEnvMonv2VoltageLowerThreshold": atEnvMonv2VoltageLowerThreshold,
       "atEnvMonv2VoltageStatus": atEnvMonv2VoltageStatus,
       "atEnvMonv2TemperatureTable": atEnvMonv2TemperatureTable,
       "atEnvMonv2TemperatureEntry": atEnvMonv2TemperatureEntry,
       "atEnvMonv2TemperatureStackMemberId": atEnvMonv2TemperatureStackMemberId,
       "atEnvMonv2TemperatureBoardIndex": atEnvMonv2TemperatureBoardIndex,
       "atEnvMonv2TemperatureIndex": atEnvMonv2TemperatureIndex,
       "atEnvMonv2TemperatureDescription": atEnvMonv2TemperatureDescription,
       "atEnvMonv2TemperatureCurrent": atEnvMonv2TemperatureCurrent,
       "atEnvMonv2TemperatureUpperThreshold": atEnvMonv2TemperatureUpperThreshold,
       "atEnvMonv2TemperatureStatus": atEnvMonv2TemperatureStatus,
       "atEnvMonv2PsbObjects": atEnvMonv2PsbObjects,
       "atEnvMonv2PsbTable": atEnvMonv2PsbTable,
       "atEnvMonv2PsbEntry": atEnvMonv2PsbEntry,
       "atEnvMonv2PsbHostStackMemberId": atEnvMonv2PsbHostStackMemberId,
       "atEnvMonv2PsbHostBoardIndex": atEnvMonv2PsbHostBoardIndex,
       "atEnvMonv2PsbHostSlotIndex": atEnvMonv2PsbHostSlotIndex,
       "atEnvMonv2PsbHeldBoardIndex": atEnvMonv2PsbHeldBoardIndex,
       "atEnvMonv2PsbHeldBoardId": atEnvMonv2PsbHeldBoardId,
       "atEnvMonv2PsbDescription": atEnvMonv2PsbDescription,
       "atEnvMonv2PsbSensorTable": atEnvMonv2PsbSensorTable,
       "atEnvMonv2PsbSensorEntry": atEnvMonv2PsbSensorEntry,
       "atEnvMonv2PsbSensorStackMemberId": atEnvMonv2PsbSensorStackMemberId,
       "atEnvMonv2PsbSensorBoardIndex": atEnvMonv2PsbSensorBoardIndex,
       "atEnvMonv2PsbSensorIndex": atEnvMonv2PsbSensorIndex,
       "atEnvMonv2PsbSensorType": atEnvMonv2PsbSensorType,
       "atEnvMonv2PsbSensorDescription": atEnvMonv2PsbSensorDescription,
       "atEnvMonv2PsbSensorStatus": atEnvMonv2PsbSensorStatus,
       "atEnvMonv2PsbSensorReading": atEnvMonv2PsbSensorReading,
       "atEnvMonv2Traps": atEnvMonv2Traps,
       "atEnvMonv2FanAlarmSetEvent": atEnvMonv2FanAlarmSetEvent,
       "atEnvMonv2FanAlarmClearedEvent": atEnvMonv2FanAlarmClearedEvent,
       "atEnvMonv2VoltAlarmSetEvent": atEnvMonv2VoltAlarmSetEvent,
       "atEnvMonv2VoltAlarmClearedEvent": atEnvMonv2VoltAlarmClearedEvent,
       "atEnvMonv2TempAlarmSetEvent": atEnvMonv2TempAlarmSetEvent,
       "atEnvMonv2TempAlarmClearedEvent": atEnvMonv2TempAlarmClearedEvent,
       "atEnvMonv2PsbAlarmSetEvent": atEnvMonv2PsbAlarmSetEvent,
       "atEnvMonv2PsbAlarmClearedEvent": atEnvMonv2PsbAlarmClearedEvent,
       "atEnvMonv2FaultLedTable": atEnvMonv2FaultLedTable,
       "atEnvMonv2FaultLedEntry": atEnvMonv2FaultLedEntry,
       "atEnvMonv2FaultLedStackMemberId": atEnvMonv2FaultLedStackMemberId,
       "atEnvMonv2FaultLed1Flash": atEnvMonv2FaultLed1Flash,
       "atEnvMonv2FaultLed2Flashes": atEnvMonv2FaultLed2Flashes,
       "atEnvMonv2FaultLed3Flashes": atEnvMonv2FaultLed3Flashes,
       "atEnvMonv2FaultLed4Flashes": atEnvMonv2FaultLed4Flashes,
       "atEnvMonv2FaultLed5Flashes": atEnvMonv2FaultLed5Flashes,
       "atEnvMonv2FaultLed6Flashes": atEnvMonv2FaultLed6Flashes}
)
