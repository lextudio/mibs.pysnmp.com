# SNMP MIB module (EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQUIPMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:20 2024
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

(AgentNotifyLevel,
 dlink_common_mgmt) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "AgentNotifyLevel",
    "dlink-common-mgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(swTimeRangeMgmtRangeName,) = mibBuilder.importSymbols(
    "TIMERANGE-MIB",
    "swTimeRangeMgmtRangeName")


# MODULE-IDENTITY

swEquipmentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwEquipment_ObjectIdentity = ObjectIdentity
swEquipment = _SwEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1)
)


class _SwEquipmentCapacity_Type(Bits):
    """Custom type swEquipmentCapacity based on Bits"""
    namedValues = NamedValues(
        *(("chassisCapable", 4),
          ("fanCapable", 0),
          ("redundantPowerCapable", 1),
          ("stackingCapable", 3),
          ("tempteratureDetection", 2))
    )

_SwEquipmentCapacity_Type.__name__ = "Bits"
_SwEquipmentCapacity_Object = MibScalar
swEquipmentCapacity = _SwEquipmentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 1),
    _SwEquipmentCapacity_Type()
)
swEquipmentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEquipmentCapacity.setStatus("current")


class _SwFanTrapState_Type(Integer32):
    """Custom type swFanTrapState based on Integer32"""
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


_SwFanTrapState_Type.__name__ = "Integer32"
_SwFanTrapState_Object = MibScalar
swFanTrapState = _SwFanTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 4),
    _SwFanTrapState_Type()
)
swFanTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFanTrapState.setStatus("current")


class _SwPowerTrapState_Type(Integer32):
    """Custom type swPowerTrapState based on Integer32"""
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


_SwPowerTrapState_Type.__name__ = "Integer32"
_SwPowerTrapState_Object = MibScalar
swPowerTrapState = _SwPowerTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 5),
    _SwPowerTrapState_Type()
)
swPowerTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPowerTrapState.setStatus("current")
_SwPowerTable_Object = MibTable
swPowerTable = _SwPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6)
)
if mibBuilder.loadTexts:
    swPowerTable.setStatus("current")
_SwPowerEntry_Object = MibTableRow
swPowerEntry = _SwPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1)
)
swPowerEntry.setIndexNames(
    (0, "EQUIPMENT-MIB", "swPowerUnitIndex"),
    (0, "EQUIPMENT-MIB", "swPowerID"),
)
if mibBuilder.loadTexts:
    swPowerEntry.setStatus("current")


class _SwPowerUnitIndex_Type(Integer32):
    """Custom type swPowerUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPowerUnitIndex_Type.__name__ = "Integer32"
_SwPowerUnitIndex_Object = MibTableColumn
swPowerUnitIndex = _SwPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 1),
    _SwPowerUnitIndex_Type()
)
swPowerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerUnitIndex.setStatus("current")


class _SwPowerID_Type(Integer32):
    """Custom type swPowerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPowerID_Type.__name__ = "Integer32"
_SwPowerID_Object = MibTableColumn
swPowerID = _SwPowerID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 2),
    _SwPowerID_Type()
)
swPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerID.setStatus("current")


class _SwPowerStatus_Type(Integer32):
    """Custom type swPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connect", 5),
          ("disconnect", 6),
          ("fail", 4),
          ("lowVoltage", 1),
          ("other", 0),
          ("overCurrent", 2),
          ("working", 3))
    )


_SwPowerStatus_Type.__name__ = "Integer32"
_SwPowerStatus_Object = MibTableColumn
swPowerStatus = _SwPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 3),
    _SwPowerStatus_Type()
)
swPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerStatus.setStatus("current")
_SwFanTable_Object = MibTable
swFanTable = _SwFanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7)
)
if mibBuilder.loadTexts:
    swFanTable.setStatus("current")
_SwFanEntry_Object = MibTableRow
swFanEntry = _SwFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1)
)
swFanEntry.setIndexNames(
    (0, "EQUIPMENT-MIB", "swFanUnitIndex"),
    (0, "EQUIPMENT-MIB", "swFanID"),
)
if mibBuilder.loadTexts:
    swFanEntry.setStatus("current")


class _SwFanUnitIndex_Type(Integer32):
    """Custom type swFanUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwFanUnitIndex_Type.__name__ = "Integer32"
_SwFanUnitIndex_Object = MibTableColumn
swFanUnitIndex = _SwFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 1),
    _SwFanUnitIndex_Type()
)
swFanUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFanUnitIndex.setStatus("current")


class _SwFanID_Type(Integer32):
    """Custom type swFanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwFanID_Type.__name__ = "Integer32"
_SwFanID_Object = MibTableColumn
swFanID = _SwFanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 2),
    _SwFanID_Type()
)
swFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFanID.setStatus("current")


class _SwFanStatus_Type(Integer32):
    """Custom type swFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("other", 0),
          ("speed-0", 3),
          ("speed-high", 6),
          ("speed-low", 4),
          ("speed-middle", 5),
          ("working", 1))
    )


_SwFanStatus_Type.__name__ = "Integer32"
_SwFanStatus_Object = MibTableColumn
swFanStatus = _SwFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 3),
    _SwFanStatus_Type()
)
swFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFanStatus.setStatus("current")


class _SwFanPostion_Type(Integer32):
    """Custom type swFanPostion based on Integer32"""
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
        *(("back", 4),
          ("cpu", 5),
          ("left", 2),
          ("other", 1),
          ("right", 3))
    )


_SwFanPostion_Type.__name__ = "Integer32"
_SwFanPostion_Object = MibTableColumn
swFanPostion = _SwFanPostion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 4),
    _SwFanPostion_Type()
)
swFanPostion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFanPostion.setStatus("current")


class _SwFanNumber_Type(Integer32):
    """Custom type swFanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwFanNumber_Type.__name__ = "Integer32"
_SwFanNumber_Object = MibTableColumn
swFanNumber = _SwFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 5),
    _SwFanNumber_Type()
)
swFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFanNumber.setStatus("current")


class _SwFanSpeed_Type(Integer32):
    """Custom type swFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwFanSpeed_Type.__name__ = "Integer32"
_SwFanSpeed_Object = MibTableColumn
swFanSpeed = _SwFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 6),
    _SwFanSpeed_Type()
)
swFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFanSpeed.setStatus("current")
_SwTemperatureTable_Object = MibTable
swTemperatureTable = _SwTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8)
)
if mibBuilder.loadTexts:
    swTemperatureTable.setStatus("current")
_SwTemperatureEntry_Object = MibTableRow
swTemperatureEntry = _SwTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1)
)
swTemperatureEntry.setIndexNames(
    (0, "EQUIPMENT-MIB", "swTemperatureUnitIndex"),
)
if mibBuilder.loadTexts:
    swTemperatureEntry.setStatus("current")


class _SwTemperatureUnitIndex_Type(Integer32):
    """Custom type swTemperatureUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwTemperatureUnitIndex_Type.__name__ = "Integer32"
_SwTemperatureUnitIndex_Object = MibTableColumn
swTemperatureUnitIndex = _SwTemperatureUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1, 1),
    _SwTemperatureUnitIndex_Type()
)
swTemperatureUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTemperatureUnitIndex.setStatus("current")


class _SwTemperatureCurrent_Type(Integer32):
    """Custom type swTemperatureCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_SwTemperatureCurrent_Type.__name__ = "Integer32"
_SwTemperatureCurrent_Object = MibTableColumn
swTemperatureCurrent = _SwTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1, 2),
    _SwTemperatureCurrent_Type()
)
swTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTemperatureCurrent.setStatus("current")


class _SwTemperatureHighThresh_Type(Integer32):
    """Custom type swTemperatureHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_SwTemperatureHighThresh_Type.__name__ = "Integer32"
_SwTemperatureHighThresh_Object = MibTableColumn
swTemperatureHighThresh = _SwTemperatureHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1, 3),
    _SwTemperatureHighThresh_Type()
)
swTemperatureHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTemperatureHighThresh.setStatus("current")


class _SwTemperatureLowThresh_Type(Integer32):
    """Custom type swTemperatureLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_SwTemperatureLowThresh_Type.__name__ = "Integer32"
_SwTemperatureLowThresh_Object = MibTableColumn
swTemperatureLowThresh = _SwTemperatureLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1, 4),
    _SwTemperatureLowThresh_Type()
)
swTemperatureLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTemperatureLowThresh.setStatus("current")
_SwUnitMgmt_ObjectIdentity = ObjectIdentity
swUnitMgmt = _SwUnitMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9)
)


class _SwUnitStackingVersion_Type(Integer32):
    """Custom type swUnitStackingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwUnitStackingVersion_Type.__name__ = "Integer32"
_SwUnitStackingVersion_Object = MibScalar
swUnitStackingVersion = _SwUnitStackingVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 1),
    _SwUnitStackingVersion_Type()
)
swUnitStackingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitStackingVersion.setStatus("current")


class _SwUnitMaxSupportedUnits_Type(Integer32):
    """Custom type swUnitMaxSupportedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwUnitMaxSupportedUnits_Type.__name__ = "Integer32"
_SwUnitMaxSupportedUnits_Object = MibScalar
swUnitMaxSupportedUnits = _SwUnitMaxSupportedUnits_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 2),
    _SwUnitMaxSupportedUnits_Type()
)
swUnitMaxSupportedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMaxSupportedUnits.setStatus("current")


class _SwUnitNumOfUnit_Type(Integer32):
    """Custom type swUnitNumOfUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwUnitNumOfUnit_Type.__name__ = "Integer32"
_SwUnitNumOfUnit_Object = MibScalar
swUnitNumOfUnit = _SwUnitNumOfUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 3),
    _SwUnitNumOfUnit_Type()
)
swUnitNumOfUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitNumOfUnit.setStatus("current")
_SwUnitMgmtTable_Object = MibTable
swUnitMgmtTable = _SwUnitMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4)
)
if mibBuilder.loadTexts:
    swUnitMgmtTable.setStatus("current")
_SwUnitMgmtEntry_Object = MibTableRow
swUnitMgmtEntry = _SwUnitMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1)
)
swUnitMgmtEntry.setIndexNames(
    (0, "EQUIPMENT-MIB", "swUnitMgmtId"),
)
if mibBuilder.loadTexts:
    swUnitMgmtEntry.setStatus("current")


class _SwUnitMgmtId_Type(Integer32):
    """Custom type swUnitMgmtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_SwUnitMgmtId_Type.__name__ = "Integer32"
_SwUnitMgmtId_Object = MibTableColumn
swUnitMgmtId = _SwUnitMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 1),
    _SwUnitMgmtId_Type()
)
swUnitMgmtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtId.setStatus("current")
_SwUnitMgmtMacAddr_Type = MacAddress
_SwUnitMgmtMacAddr_Object = MibTableColumn
swUnitMgmtMacAddr = _SwUnitMgmtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 2),
    _SwUnitMgmtMacAddr_Type()
)
swUnitMgmtMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtMacAddr.setStatus("current")


class _SwUnitMgmtStartPort_Type(Integer32):
    """Custom type swUnitMgmtStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwUnitMgmtStartPort_Type.__name__ = "Integer32"
_SwUnitMgmtStartPort_Object = MibTableColumn
swUnitMgmtStartPort = _SwUnitMgmtStartPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 3),
    _SwUnitMgmtStartPort_Type()
)
swUnitMgmtStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtStartPort.setStatus("current")


class _SwUnitMgmtPortRange_Type(Integer32):
    """Custom type swUnitMgmtPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwUnitMgmtPortRange_Type.__name__ = "Integer32"
_SwUnitMgmtPortRange_Object = MibTableColumn
swUnitMgmtPortRange = _SwUnitMgmtPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 4),
    _SwUnitMgmtPortRange_Type()
)
swUnitMgmtPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtPortRange.setStatus("current")


class _SwUnitMgmtFrontPanelLedStatus_Type(OctetString):
    """Custom type swUnitMgmtFrontPanelLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwUnitMgmtFrontPanelLedStatus_Type.__name__ = "OctetString"
_SwUnitMgmtFrontPanelLedStatus_Object = MibTableColumn
swUnitMgmtFrontPanelLedStatus = _SwUnitMgmtFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 5),
    _SwUnitMgmtFrontPanelLedStatus_Type()
)
swUnitMgmtFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtFrontPanelLedStatus.setStatus("current")


class _SwUnitMgmtCtrlMode_Type(Integer32):
    """Custom type swUnitMgmtCtrlMode based on Integer32"""
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
        *(("auto", 2),
          ("master", 4),
          ("other", 1),
          ("slave", 5),
          ("stand-alone", 3))
    )


_SwUnitMgmtCtrlMode_Type.__name__ = "Integer32"
_SwUnitMgmtCtrlMode_Object = MibTableColumn
swUnitMgmtCtrlMode = _SwUnitMgmtCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 6),
    _SwUnitMgmtCtrlMode_Type()
)
swUnitMgmtCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitMgmtCtrlMode.setStatus("current")


class _SwUnitMgmtCurrentMode_Type(Integer32):
    """Custom type swUnitMgmtCurrentMode based on Integer32"""
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
        *(("auto", 2),
          ("backup-master", 6),
          ("master", 4),
          ("other", 1),
          ("slave", 5),
          ("stand-alone", 3))
    )


_SwUnitMgmtCurrentMode_Type.__name__ = "Integer32"
_SwUnitMgmtCurrentMode_Object = MibTableColumn
swUnitMgmtCurrentMode = _SwUnitMgmtCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 7),
    _SwUnitMgmtCurrentMode_Type()
)
swUnitMgmtCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtCurrentMode.setStatus("current")


class _SwUnitMgmtVersion_Type(DisplayString):
    """Custom type swUnitMgmtVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwUnitMgmtVersion_Type.__name__ = "DisplayString"
_SwUnitMgmtVersion_Object = MibTableColumn
swUnitMgmtVersion = _SwUnitMgmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 8),
    _SwUnitMgmtVersion_Type()
)
swUnitMgmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtVersion.setStatus("current")


class _SwUnitMgmtModuleName_Type(DisplayString):
    """Custom type swUnitMgmtModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwUnitMgmtModuleName_Type.__name__ = "DisplayString"
_SwUnitMgmtModuleName_Object = MibTableColumn
swUnitMgmtModuleName = _SwUnitMgmtModuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 9),
    _SwUnitMgmtModuleName_Type()
)
swUnitMgmtModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtModuleName.setStatus("current")


class _SwUnitMgmtPromVersion_Type(DisplayString):
    """Custom type swUnitMgmtPromVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwUnitMgmtPromVersion_Type.__name__ = "DisplayString"
_SwUnitMgmtPromVersion_Object = MibTableColumn
swUnitMgmtPromVersion = _SwUnitMgmtPromVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 10),
    _SwUnitMgmtPromVersion_Type()
)
swUnitMgmtPromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtPromVersion.setStatus("current")


class _SwUnitMgmtFirmwareVersion_Type(DisplayString):
    """Custom type swUnitMgmtFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwUnitMgmtFirmwareVersion_Type.__name__ = "DisplayString"
_SwUnitMgmtFirmwareVersion_Object = MibTableColumn
swUnitMgmtFirmwareVersion = _SwUnitMgmtFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 11),
    _SwUnitMgmtFirmwareVersion_Type()
)
swUnitMgmtFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtFirmwareVersion.setStatus("current")


class _SwUnitMgmtHardwareVersion_Type(DisplayString):
    """Custom type swUnitMgmtHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwUnitMgmtHardwareVersion_Type.__name__ = "DisplayString"
_SwUnitMgmtHardwareVersion_Object = MibTableColumn
swUnitMgmtHardwareVersion = _SwUnitMgmtHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 12),
    _SwUnitMgmtHardwareVersion_Type()
)
swUnitMgmtHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtHardwareVersion.setStatus("current")


class _SwUnitMgmtPriority_Type(Integer32):
    """Custom type swUnitMgmtPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SwUnitMgmtPriority_Type.__name__ = "Integer32"
_SwUnitMgmtPriority_Object = MibTableColumn
swUnitMgmtPriority = _SwUnitMgmtPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 13),
    _SwUnitMgmtPriority_Type()
)
swUnitMgmtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitMgmtPriority.setStatus("current")


class _SwUnitMgmtUserSetState_Type(Integer32):
    """Custom type swUnitMgmtUserSetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("other", 1),
          ("user", 3))
    )


_SwUnitMgmtUserSetState_Type.__name__ = "Integer32"
_SwUnitMgmtUserSetState_Object = MibTableColumn
swUnitMgmtUserSetState = _SwUnitMgmtUserSetState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 14),
    _SwUnitMgmtUserSetState_Type()
)
swUnitMgmtUserSetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtUserSetState.setStatus("current")


class _SwUnitMgmtExistState_Type(Integer32):
    """Custom type swUnitMgmtExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("no-exist", 2))
    )


_SwUnitMgmtExistState_Type.__name__ = "Integer32"
_SwUnitMgmtExistState_Object = MibTableColumn
swUnitMgmtExistState = _SwUnitMgmtExistState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 15),
    _SwUnitMgmtExistState_Type()
)
swUnitMgmtExistState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtExistState.setStatus("current")


class _SwUnitMgmtBoxId_Type(Integer32):
    """Custom type swUnitMgmtBoxId based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("auto", 13),
          ("box-1", 1),
          ("box-10", 10),
          ("box-11", 11),
          ("box-12", 12),
          ("box-2", 2),
          ("box-3", 3),
          ("box-4", 4),
          ("box-5", 5),
          ("box-6", 6),
          ("box-7", 7),
          ("box-8", 8),
          ("box-9", 9))
    )


_SwUnitMgmtBoxId_Type.__name__ = "Integer32"
_SwUnitMgmtBoxId_Object = MibTableColumn
swUnitMgmtBoxId = _SwUnitMgmtBoxId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 16),
    _SwUnitMgmtBoxId_Type()
)
swUnitMgmtBoxId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitMgmtBoxId.setStatus("current")
_SwUnitMgmtSerialNumber_Type = DisplayString
_SwUnitMgmtSerialNumber_Object = MibTableColumn
swUnitMgmtSerialNumber = _SwUnitMgmtSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 17),
    _SwUnitMgmtSerialNumber_Type()
)
swUnitMgmtSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtSerialNumber.setStatus("current")


class _SwUnitTopology_Type(Integer32):
    """Custom type swUnitTopology based on Integer32"""
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
        *(("duplex-chain", 2),
          ("duplex-ring", 3),
          ("stand-alone", 1),
          ("star", 4),
          ("unstable", 5))
    )


_SwUnitTopology_Type.__name__ = "Integer32"
_SwUnitTopology_Object = MibScalar
swUnitTopology = _SwUnitTopology_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 5),
    _SwUnitTopology_Type()
)
swUnitTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitTopology.setStatus("current")


class _SwUnitStackMode_Type(Integer32):
    """Custom type swUnitStackMode based on Integer32"""
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


_SwUnitStackMode_Type.__name__ = "Integer32"
_SwUnitStackMode_Object = MibScalar
swUnitStackMode = _SwUnitStackMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 6),
    _SwUnitStackMode_Type()
)
swUnitStackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitStackMode.setStatus("current")


class _SwUnitStackForceMasterRole_Type(Integer32):
    """Custom type swUnitStackForceMasterRole based on Integer32"""
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


_SwUnitStackForceMasterRole_Type.__name__ = "Integer32"
_SwUnitStackForceMasterRole_Object = MibScalar
swUnitStackForceMasterRole = _SwUnitStackForceMasterRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 7),
    _SwUnitStackForceMasterRole_Type()
)
swUnitStackForceMasterRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitStackForceMasterRole.setStatus("current")


class _SwUnitStackTrapState_Type(Integer32):
    """Custom type swUnitStackTrapState based on Integer32"""
    defaultValue = 1

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


_SwUnitStackTrapState_Type.__name__ = "Integer32"
_SwUnitStackTrapState_Object = MibScalar
swUnitStackTrapState = _SwUnitStackTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 8),
    _SwUnitStackTrapState_Type()
)
swUnitStackTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitStackTrapState.setStatus("current")


class _SwUnitStackLogState_Type(Integer32):
    """Custom type swUnitStackLogState based on Integer32"""
    defaultValue = 1

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


_SwUnitStackLogState_Type.__name__ = "Integer32"
_SwUnitStackLogState_Object = MibScalar
swUnitStackLogState = _SwUnitStackLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 9),
    _SwUnitStackLogState_Type()
)
swUnitStackLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitStackLogState.setStatus("current")
_SwExternalAlarmTable_Object = MibTable
swExternalAlarmTable = _SwExternalAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10)
)
if mibBuilder.loadTexts:
    swExternalAlarmTable.setStatus("current")
_SwExternalAlarmEntry_Object = MibTableRow
swExternalAlarmEntry = _SwExternalAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10, 1)
)
swExternalAlarmEntry.setIndexNames(
    (0, "EQUIPMENT-MIB", "swExternalAlarmChannel"),
)
if mibBuilder.loadTexts:
    swExternalAlarmEntry.setStatus("current")
_SwExternalAlarmChannel_Type = Integer32
_SwExternalAlarmChannel_Object = MibTableColumn
swExternalAlarmChannel = _SwExternalAlarmChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10, 1, 1),
    _SwExternalAlarmChannel_Type()
)
swExternalAlarmChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExternalAlarmChannel.setStatus("current")


class _SwExternalAlarmMessage_Type(DisplayString):
    """Custom type swExternalAlarmMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwExternalAlarmMessage_Type.__name__ = "DisplayString"
_SwExternalAlarmMessage_Object = MibTableColumn
swExternalAlarmMessage = _SwExternalAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10, 1, 2),
    _SwExternalAlarmMessage_Type()
)
swExternalAlarmMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swExternalAlarmMessage.setStatus("current")


class _SwExternalAlarmStatus_Type(Integer32):
    """Custom type swExternalAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarming", 1),
          ("normal", 2))
    )


_SwExternalAlarmStatus_Type.__name__ = "Integer32"
_SwExternalAlarmStatus_Object = MibTableColumn
swExternalAlarmStatus = _SwExternalAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10, 1, 3),
    _SwExternalAlarmStatus_Type()
)
swExternalAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExternalAlarmStatus.setStatus("current")
_SwEquipmentPowerSaving_ObjectIdentity = ObjectIdentity
swEquipmentPowerSaving = _SwEquipmentPowerSaving_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11)
)


class _SwEquipPowerSavingLinkDetectState_Type(Integer32):
    """Custom type swEquipPowerSavingLinkDetectState based on Integer32"""
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


_SwEquipPowerSavingLinkDetectState_Type.__name__ = "Integer32"
_SwEquipPowerSavingLinkDetectState_Object = MibScalar
swEquipPowerSavingLinkDetectState = _SwEquipPowerSavingLinkDetectState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 1),
    _SwEquipPowerSavingLinkDetectState_Type()
)
swEquipPowerSavingLinkDetectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEquipPowerSavingLinkDetectState.setStatus("current")


class _SwEquipPowerSavingLenDetect_Type(Integer32):
    """Custom type swEquipPowerSavingLenDetect based on Integer32"""
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


_SwEquipPowerSavingLenDetect_Type.__name__ = "Integer32"
_SwEquipPowerSavingLenDetect_Object = MibScalar
swEquipPowerSavingLenDetect = _SwEquipPowerSavingLenDetect_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 2),
    _SwEquipPowerSavingLenDetect_Type()
)
swEquipPowerSavingLenDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEquipPowerSavingLenDetect.setStatus("current")


class _SwEquipPowerSavingHiberState_Type(Integer32):
    """Custom type swEquipPowerSavingHiberState based on Integer32"""
    defaultValue = 2

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


_SwEquipPowerSavingHiberState_Type.__name__ = "Integer32"
_SwEquipPowerSavingHiberState_Object = MibScalar
swEquipPowerSavingHiberState = _SwEquipPowerSavingHiberState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 3),
    _SwEquipPowerSavingHiberState_Type()
)
swEquipPowerSavingHiberState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEquipPowerSavingHiberState.setStatus("current")


class _SwEquipPowerSavingPortLEDState_Type(Integer32):
    """Custom type swEquipPowerSavingPortLEDState based on Integer32"""
    defaultValue = 2

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


_SwEquipPowerSavingPortLEDState_Type.__name__ = "Integer32"
_SwEquipPowerSavingPortLEDState_Object = MibScalar
swEquipPowerSavingPortLEDState = _SwEquipPowerSavingPortLEDState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 4),
    _SwEquipPowerSavingPortLEDState_Type()
)
swEquipPowerSavingPortLEDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEquipPowerSavingPortLEDState.setStatus("current")


class _SwEquipPowerSavingPortState_Type(Integer32):
    """Custom type swEquipPowerSavingPortState based on Integer32"""
    defaultValue = 2

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


_SwEquipPowerSavingPortState_Type.__name__ = "Integer32"
_SwEquipPowerSavingPortState_Object = MibScalar
swEquipPowerSavingPortState = _SwEquipPowerSavingPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 5),
    _SwEquipPowerSavingPortState_Type()
)
swEquipPowerSavingPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEquipPowerSavingPortState.setStatus("current")
_SwEquipPowerSavingScheduleCtrl_ObjectIdentity = ObjectIdentity
swEquipPowerSavingScheduleCtrl = _SwEquipPowerSavingScheduleCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6)
)
_SwEquipPowerSavingHibernationTable_Object = MibTable
swEquipPowerSavingHibernationTable = _SwEquipPowerSavingHibernationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 1)
)
if mibBuilder.loadTexts:
    swEquipPowerSavingHibernationTable.setStatus("current")
_SwEquipPowerSavingHibernationEntry_Object = MibTableRow
swEquipPowerSavingHibernationEntry = _SwEquipPowerSavingHibernationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 1, 1)
)
swEquipPowerSavingHibernationEntry.setIndexNames(
    (0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"),
)
if mibBuilder.loadTexts:
    swEquipPowerSavingHibernationEntry.setStatus("current")
_SwEquipPowerSavingHiberRowStatus_Type = RowStatus
_SwEquipPowerSavingHiberRowStatus_Object = MibTableColumn
swEquipPowerSavingHiberRowStatus = _SwEquipPowerSavingHiberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 1, 1, 100),
    _SwEquipPowerSavingHiberRowStatus_Type()
)
swEquipPowerSavingHiberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEquipPowerSavingHiberRowStatus.setStatus("current")
_SwEquipPowerSavingPortLedTable_Object = MibTable
swEquipPowerSavingPortLedTable = _SwEquipPowerSavingPortLedTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 2)
)
if mibBuilder.loadTexts:
    swEquipPowerSavingPortLedTable.setStatus("current")
_SwEquipPowerSavingPortLedEntry_Object = MibTableRow
swEquipPowerSavingPortLedEntry = _SwEquipPowerSavingPortLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 2, 1)
)
swEquipPowerSavingPortLedEntry.setIndexNames(
    (0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"),
)
if mibBuilder.loadTexts:
    swEquipPowerSavingPortLedEntry.setStatus("current")
_SwEquipPowerSavingPortLedRowStatus_Type = RowStatus
_SwEquipPowerSavingPortLedRowStatus_Object = MibTableColumn
swEquipPowerSavingPortLedRowStatus = _SwEquipPowerSavingPortLedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 2, 1, 100),
    _SwEquipPowerSavingPortLedRowStatus_Type()
)
swEquipPowerSavingPortLedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEquipPowerSavingPortLedRowStatus.setStatus("current")
_SwEquipPowerSavingPortTable_Object = MibTable
swEquipPowerSavingPortTable = _SwEquipPowerSavingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 3)
)
if mibBuilder.loadTexts:
    swEquipPowerSavingPortTable.setStatus("current")
_SwEquipPowerSavingPortEntry_Object = MibTableRow
swEquipPowerSavingPortEntry = _SwEquipPowerSavingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 3, 1)
)
swEquipPowerSavingPortEntry.setIndexNames(
    (0, "EQUIPMENT-MIB", "swEquipPowerSavingPortIndex"),
    (0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"),
)
if mibBuilder.loadTexts:
    swEquipPowerSavingPortEntry.setStatus("current")
_SwEquipPowerSavingPortIndex_Type = Integer32
_SwEquipPowerSavingPortIndex_Object = MibTableColumn
swEquipPowerSavingPortIndex = _SwEquipPowerSavingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 3, 1, 1),
    _SwEquipPowerSavingPortIndex_Type()
)
swEquipPowerSavingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEquipPowerSavingPortIndex.setStatus("current")
_SwEquipPowerSavingPortRowStatus_Type = RowStatus
_SwEquipPowerSavingPortRowStatus_Object = MibTableColumn
swEquipPowerSavingPortRowStatus = _SwEquipPowerSavingPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 3, 1, 100),
    _SwEquipPowerSavingPortRowStatus_Type()
)
swEquipPowerSavingPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swEquipPowerSavingPortRowStatus.setStatus("current")
_SwEquipmentTemperatureCtrl_ObjectIdentity = ObjectIdentity
swEquipmentTemperatureCtrl = _SwEquipmentTemperatureCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 12)
)


class _SwTemperatureTrapState_Type(Integer32):
    """Custom type swTemperatureTrapState based on Integer32"""
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


_SwTemperatureTrapState_Type.__name__ = "Integer32"
_SwTemperatureTrapState_Object = MibScalar
swTemperatureTrapState = _SwTemperatureTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 12, 1),
    _SwTemperatureTrapState_Type()
)
swTemperatureTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTemperatureTrapState.setStatus("current")


class _SwTemperatureLogState_Type(Integer32):
    """Custom type swTemperatureLogState based on Integer32"""
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


_SwTemperatureLogState_Type.__name__ = "Integer32"
_SwTemperatureLogState_Object = MibScalar
swTemperatureLogState = _SwTemperatureLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 12, 2),
    _SwTemperatureLogState_Type()
)
swTemperatureLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTemperatureLogState.setStatus("current")
_SwEquipmentLEDCtrl_ObjectIdentity = ObjectIdentity
swEquipmentLEDCtrl = _SwEquipmentLEDCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 13)
)


class _SwEquipmentPortLEDState_Type(Integer32):
    """Custom type swEquipmentPortLEDState based on Integer32"""
    defaultValue = 1

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


_SwEquipmentPortLEDState_Type.__name__ = "Integer32"
_SwEquipmentPortLEDState_Object = MibScalar
swEquipmentPortLEDState = _SwEquipmentPortLEDState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 13, 1),
    _SwEquipmentPortLEDState_Type()
)
swEquipmentPortLEDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEquipmentPortLEDState.setStatus("current")
_SwExternalAlarmStackingTable_Object = MibTable
swExternalAlarmStackingTable = _SwExternalAlarmStackingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15)
)
if mibBuilder.loadTexts:
    swExternalAlarmStackingTable.setStatus("current")
_SwExternalAlarmStackingEntry_Object = MibTableRow
swExternalAlarmStackingEntry = _SwExternalAlarmStackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1)
)
swExternalAlarmStackingEntry.setIndexNames(
    (0, "EQUIPMENT-MIB", "swExternalAlarmStackingUnitIndex"),
    (0, "EQUIPMENT-MIB", "swExternalAlarmStackingChannel"),
)
if mibBuilder.loadTexts:
    swExternalAlarmStackingEntry.setStatus("current")
_SwExternalAlarmStackingUnitIndex_Type = Integer32
_SwExternalAlarmStackingUnitIndex_Object = MibTableColumn
swExternalAlarmStackingUnitIndex = _SwExternalAlarmStackingUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1, 1),
    _SwExternalAlarmStackingUnitIndex_Type()
)
swExternalAlarmStackingUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swExternalAlarmStackingUnitIndex.setStatus("current")
_SwExternalAlarmStackingChannel_Type = Integer32
_SwExternalAlarmStackingChannel_Object = MibTableColumn
swExternalAlarmStackingChannel = _SwExternalAlarmStackingChannel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1, 2),
    _SwExternalAlarmStackingChannel_Type()
)
swExternalAlarmStackingChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swExternalAlarmStackingChannel.setStatus("current")


class _SwExternalAlarmStackingMessage_Type(DisplayString):
    """Custom type swExternalAlarmStackingMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwExternalAlarmStackingMessage_Type.__name__ = "DisplayString"
_SwExternalAlarmStackingMessage_Object = MibTableColumn
swExternalAlarmStackingMessage = _SwExternalAlarmStackingMessage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1, 3),
    _SwExternalAlarmStackingMessage_Type()
)
swExternalAlarmStackingMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swExternalAlarmStackingMessage.setStatus("current")


class _SwExternalAlarmStackingStatus_Type(Integer32):
    """Custom type swExternalAlarmStackingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarming", 1),
          ("normal", 2))
    )


_SwExternalAlarmStackingStatus_Type.__name__ = "Integer32"
_SwExternalAlarmStackingStatus_Object = MibTableColumn
swExternalAlarmStackingStatus = _SwExternalAlarmStackingStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1, 4),
    _SwExternalAlarmStackingStatus_Type()
)
swExternalAlarmStackingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExternalAlarmStackingStatus.setStatus("current")
_SwEquipmentNotify_ObjectIdentity = ObjectIdentity
swEquipmentNotify = _SwEquipmentNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2)
)
_SwEquipmentNotifyMgmt_ObjectIdentity = ObjectIdentity
swEquipmentNotifyMgmt = _SwEquipmentNotifyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1)
)
_SwEquipUnitNotifyMgmt_ObjectIdentity = ObjectIdentity
swEquipUnitNotifyMgmt = _SwEquipUnitNotifyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 1)
)
_SwUnitInsertSeverity_Type = AgentNotifyLevel
_SwUnitInsertSeverity_Object = MibScalar
swUnitInsertSeverity = _SwUnitInsertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 1, 1),
    _SwUnitInsertSeverity_Type()
)
swUnitInsertSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitInsertSeverity.setStatus("current")
_SwUnitRemoveSeverity_Type = AgentNotifyLevel
_SwUnitRemoveSeverity_Object = MibScalar
swUnitRemoveSeverity = _SwUnitRemoveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 1, 2),
    _SwUnitRemoveSeverity_Type()
)
swUnitRemoveSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitRemoveSeverity.setStatus("current")
_SwUnitFailureSeverity_Type = AgentNotifyLevel
_SwUnitFailureSeverity_Object = MibScalar
swUnitFailureSeverity = _SwUnitFailureSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 1, 3),
    _SwUnitFailureSeverity_Type()
)
swUnitFailureSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitFailureSeverity.setStatus("current")
_SwEquipPowerNotifyMgmt_ObjectIdentity = ObjectIdentity
swEquipPowerNotifyMgmt = _SwEquipPowerNotifyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 2)
)
_SwPowerStatusChgSeverity_Type = AgentNotifyLevel
_SwPowerStatusChgSeverity_Object = MibScalar
swPowerStatusChgSeverity = _SwPowerStatusChgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 2, 1),
    _SwPowerStatusChgSeverity_Type()
)
swPowerStatusChgSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPowerStatusChgSeverity.setStatus("current")
_SwPowerFailureSeverity_Type = AgentNotifyLevel
_SwPowerFailureSeverity_Object = MibScalar
swPowerFailureSeverity = _SwPowerFailureSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 2, 2),
    _SwPowerFailureSeverity_Type()
)
swPowerFailureSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPowerFailureSeverity.setStatus("current")
_SwPowerRecoverSeverity_Type = AgentNotifyLevel
_SwPowerRecoverSeverity_Object = MibScalar
swPowerRecoverSeverity = _SwPowerRecoverSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 2, 3),
    _SwPowerRecoverSeverity_Type()
)
swPowerRecoverSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPowerRecoverSeverity.setStatus("current")
_SwEquipFanNotifyMgmt_ObjectIdentity = ObjectIdentity
swEquipFanNotifyMgmt = _SwEquipFanNotifyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 3)
)
_SwFanFailureSeverity_Type = AgentNotifyLevel
_SwFanFailureSeverity_Object = MibScalar
swFanFailureSeverity = _SwFanFailureSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 3, 1),
    _SwFanFailureSeverity_Type()
)
swFanFailureSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFanFailureSeverity.setStatus("current")
_SwFanRecoverSeverity_Type = AgentNotifyLevel
_SwFanRecoverSeverity_Object = MibScalar
swFanRecoverSeverity = _SwFanRecoverSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 3, 2),
    _SwFanRecoverSeverity_Type()
)
swFanRecoverSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFanRecoverSeverity.setStatus("current")
_SwEquipTemperatureNotifyMgmt_ObjectIdentity = ObjectIdentity
swEquipTemperatureNotifyMgmt = _SwEquipTemperatureNotifyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4)
)
_SwHighTemperatureSeverity_Type = AgentNotifyLevel
_SwHighTemperatureSeverity_Object = MibScalar
swHighTemperatureSeverity = _SwHighTemperatureSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4, 1),
    _SwHighTemperatureSeverity_Type()
)
swHighTemperatureSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swHighTemperatureSeverity.setStatus("current")
_SwHighTemperatureRecoverSeverity_Type = AgentNotifyLevel
_SwHighTemperatureRecoverSeverity_Object = MibScalar
swHighTemperatureRecoverSeverity = _SwHighTemperatureRecoverSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4, 2),
    _SwHighTemperatureRecoverSeverity_Type()
)
swHighTemperatureRecoverSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swHighTemperatureRecoverSeverity.setStatus("current")
_SwLowTemperatureSeverity_Type = AgentNotifyLevel
_SwLowTemperatureSeverity_Object = MibScalar
swLowTemperatureSeverity = _SwLowTemperatureSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4, 3),
    _SwLowTemperatureSeverity_Type()
)
swLowTemperatureSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLowTemperatureSeverity.setStatus("current")
_SwLowTemperatureRecoverSeverity_Type = AgentNotifyLevel
_SwLowTemperatureRecoverSeverity_Object = MibScalar
swLowTemperatureRecoverSeverity = _SwLowTemperatureRecoverSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4, 4),
    _SwLowTemperatureRecoverSeverity_Type()
)
swLowTemperatureRecoverSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLowTemperatureRecoverSeverity.setStatus("current")
_SwEquipmentNotification_ObjectIdentity = ObjectIdentity
swEquipmentNotification = _SwEquipmentNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2)
)
_SwEquipUnitNotification_ObjectIdentity = ObjectIdentity
swEquipUnitNotification = _SwEquipUnitNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1)
)
_SwEquipUnitNotifyPrefix_ObjectIdentity = ObjectIdentity
swEquipUnitNotifyPrefix = _SwEquipUnitNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0)
)
_SwEquipPowerNotification_ObjectIdentity = ObjectIdentity
swEquipPowerNotification = _SwEquipPowerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2)
)
_SwEquipPowerNotifyPerfix_ObjectIdentity = ObjectIdentity
swEquipPowerNotifyPerfix = _SwEquipPowerNotifyPerfix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0)
)
_SwEquipFanNotification_ObjectIdentity = ObjectIdentity
swEquipFanNotification = _SwEquipFanNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 3)
)
_SwEquipFanNotifyPrefix_ObjectIdentity = ObjectIdentity
swEquipFanNotifyPrefix = _SwEquipFanNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 3, 0)
)
_SwEquipTemperatureNotification_ObjectIdentity = ObjectIdentity
swEquipTemperatureNotification = _SwEquipTemperatureNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4)
)
_SwEquipTemperatureNotifyPrefix_ObjectIdentity = ObjectIdentity
swEquipTemperatureNotifyPrefix = _SwEquipTemperatureNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0)
)
_SwEquipExternalAlarmNotification_ObjectIdentity = ObjectIdentity
swEquipExternalAlarmNotification = _SwEquipExternalAlarmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 5)
)
_SwEquipExternalAlarmNotifyPrefix_ObjectIdentity = ObjectIdentity
swEquipExternalAlarmNotifyPrefix = _SwEquipExternalAlarmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 5, 0)
)
_SwNotificationBindings_ObjectIdentity = ObjectIdentity
swNotificationBindings = _SwNotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3)
)
_SwEquipTemperNotifyBindings_ObjectIdentity = ObjectIdentity
swEquipTemperNotifyBindings = _SwEquipTemperNotifyBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 1)
)
_SwTemperSensorID_Type = Integer32
_SwTemperSensorID_Object = MibScalar
swTemperSensorID = _SwTemperSensorID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 1, 1),
    _SwTemperSensorID_Type()
)
swTemperSensorID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swTemperSensorID.setStatus("current")
_SwEquipUnitNotifyBindings_ObjectIdentity = ObjectIdentity
swEquipUnitNotifyBindings = _SwEquipUnitNotifyBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 2)
)


class _SwStackTopologyType_Type(Integer32):
    """Custom type swStackTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chain", 1),
          ("ring", 2))
    )


_SwStackTopologyType_Type.__name__ = "Integer32"
_SwStackTopologyType_Object = MibScalar
swStackTopologyType = _SwStackTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 2, 1),
    _SwStackTopologyType_Type()
)
swStackTopologyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swStackTopologyType.setStatus("current")


class _SwStackRoleChangeType_Type(Integer32):
    """Custom type swStackRoleChangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup-to-master", 1),
          ("slave-to-master", 2))
    )


_SwStackRoleChangeType_Type.__name__ = "Integer32"
_SwStackRoleChangeType_Object = MibScalar
swStackRoleChangeType = _SwStackRoleChangeType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 2, 2),
    _SwStackRoleChangeType_Type()
)
swStackRoleChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swStackRoleChangeType.setStatus("current")

# Managed Objects groups


# Notification objects

swUnitInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 1)
)
swUnitInsert.setObjects(
      *(("EQUIPMENT-MIB", "swUnitMgmtId"),
        ("EQUIPMENT-MIB", "swUnitMgmtMacAddr"))
)
if mibBuilder.loadTexts:
    swUnitInsert.setStatus(
        "current"
    )

swUnitRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 2)
)
swUnitRemove.setObjects(
      *(("EQUIPMENT-MIB", "swUnitMgmtId"),
        ("EQUIPMENT-MIB", "swUnitMgmtMacAddr"))
)
if mibBuilder.loadTexts:
    swUnitRemove.setStatus(
        "current"
    )

swUnitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 3)
)
swUnitFailure.setObjects(
    ("EQUIPMENT-MIB", "swUnitMgmtId")
)
if mibBuilder.loadTexts:
    swUnitFailure.setStatus(
        "current"
    )

swUnitTPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 4)
)
swUnitTPChange.setObjects(
      *(("EQUIPMENT-MIB", "swStackTopologyType"),
        ("EQUIPMENT-MIB", "swUnitMgmtId"),
        ("EQUIPMENT-MIB", "swUnitMgmtMacAddr"))
)
if mibBuilder.loadTexts:
    swUnitTPChange.setStatus(
        "current"
    )

swUnitRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 5)
)
swUnitRoleChange.setObjects(
      *(("EQUIPMENT-MIB", "swStackRoleChangeType"),
        ("EQUIPMENT-MIB", "swUnitMgmtId"))
)
if mibBuilder.loadTexts:
    swUnitRoleChange.setStatus(
        "current"
    )

swPowerStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 1)
)
swPowerStatusChg.setObjects(
      *(("EQUIPMENT-MIB", "swPowerUnitIndex"),
        ("EQUIPMENT-MIB", "swPowerID"),
        ("EQUIPMENT-MIB", "swPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChg.setStatus(
        "current"
    )

swPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 2)
)
swPowerFailure.setObjects(
      *(("EQUIPMENT-MIB", "swPowerUnitIndex"),
        ("EQUIPMENT-MIB", "swPowerID"),
        ("EQUIPMENT-MIB", "swPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerFailure.setStatus(
        "current"
    )

swPowerRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 3)
)
swPowerRecover.setObjects(
      *(("EQUIPMENT-MIB", "swPowerUnitIndex"),
        ("EQUIPMENT-MIB", "swPowerID"),
        ("EQUIPMENT-MIB", "swPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerRecover.setStatus(
        "current"
    )

swFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 3, 0, 1)
)
swFanFailure.setObjects(
      *(("EQUIPMENT-MIB", "swFanUnitIndex"),
        ("EQUIPMENT-MIB", "swFanID"))
)
if mibBuilder.loadTexts:
    swFanFailure.setStatus(
        "current"
    )

swFanRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 3, 0, 2)
)
swFanRecover.setObjects(
      *(("EQUIPMENT-MIB", "swFanUnitIndex"),
        ("EQUIPMENT-MIB", "swFanID"))
)
if mibBuilder.loadTexts:
    swFanRecover.setStatus(
        "current"
    )

swHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0, 1)
)
swHighTemperature.setObjects(
      *(("EQUIPMENT-MIB", "swTemperatureUnitIndex"),
        ("EQUIPMENT-MIB", "swTemperSensorID"),
        ("EQUIPMENT-MIB", "swTemperatureCurrent"))
)
if mibBuilder.loadTexts:
    swHighTemperature.setStatus(
        "current"
    )

swHighTemperatureRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0, 2)
)
swHighTemperatureRecover.setObjects(
      *(("EQUIPMENT-MIB", "swTemperatureUnitIndex"),
        ("EQUIPMENT-MIB", "swTemperSensorID"),
        ("EQUIPMENT-MIB", "swTemperatureCurrent"))
)
if mibBuilder.loadTexts:
    swHighTemperatureRecover.setStatus(
        "current"
    )

swLowTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0, 3)
)
swLowTemperature.setObjects(
      *(("EQUIPMENT-MIB", "swTemperatureUnitIndex"),
        ("EQUIPMENT-MIB", "swTemperSensorID"),
        ("EQUIPMENT-MIB", "swTemperatureCurrent"))
)
if mibBuilder.loadTexts:
    swLowTemperature.setStatus(
        "current"
    )

swLowTemperatureRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0, 4)
)
swLowTemperatureRecover.setObjects(
      *(("EQUIPMENT-MIB", "swTemperatureUnitIndex"),
        ("EQUIPMENT-MIB", "swTemperSensorID"),
        ("EQUIPMENT-MIB", "swTemperatureCurrent"))
)
if mibBuilder.loadTexts:
    swLowTemperatureRecover.setStatus(
        "current"
    )

swExternalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 5, 0, 1)
)
swExternalAlarm.setObjects(
      *(("EQUIPMENT-MIB", "swExternalAlarmChannel"),
        ("EQUIPMENT-MIB", "swExternalAlarmMessage"))
)
if mibBuilder.loadTexts:
    swExternalAlarm.setStatus(
        "current"
    )

swExternalAlarmStacking = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 5, 0, 2)
)
swExternalAlarmStacking.setObjects(
      *(("EQUIPMENT-MIB", "swExternalAlarmStackingUnitIndex"),
        ("EQUIPMENT-MIB", "swExternalAlarmStackingChannel"),
        ("EQUIPMENT-MIB", "swExternalAlarmStackingMessage"))
)
if mibBuilder.loadTexts:
    swExternalAlarmStacking.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQUIPMENT-MIB",
    **{"MacAddress": MacAddress,
       "swEquipmentMIB": swEquipmentMIB,
       "swEquipment": swEquipment,
       "swEquipmentCapacity": swEquipmentCapacity,
       "swFanTrapState": swFanTrapState,
       "swPowerTrapState": swPowerTrapState,
       "swPowerTable": swPowerTable,
       "swPowerEntry": swPowerEntry,
       "swPowerUnitIndex": swPowerUnitIndex,
       "swPowerID": swPowerID,
       "swPowerStatus": swPowerStatus,
       "swFanTable": swFanTable,
       "swFanEntry": swFanEntry,
       "swFanUnitIndex": swFanUnitIndex,
       "swFanID": swFanID,
       "swFanStatus": swFanStatus,
       "swFanPostion": swFanPostion,
       "swFanNumber": swFanNumber,
       "swFanSpeed": swFanSpeed,
       "swTemperatureTable": swTemperatureTable,
       "swTemperatureEntry": swTemperatureEntry,
       "swTemperatureUnitIndex": swTemperatureUnitIndex,
       "swTemperatureCurrent": swTemperatureCurrent,
       "swTemperatureHighThresh": swTemperatureHighThresh,
       "swTemperatureLowThresh": swTemperatureLowThresh,
       "swUnitMgmt": swUnitMgmt,
       "swUnitStackingVersion": swUnitStackingVersion,
       "swUnitMaxSupportedUnits": swUnitMaxSupportedUnits,
       "swUnitNumOfUnit": swUnitNumOfUnit,
       "swUnitMgmtTable": swUnitMgmtTable,
       "swUnitMgmtEntry": swUnitMgmtEntry,
       "swUnitMgmtId": swUnitMgmtId,
       "swUnitMgmtMacAddr": swUnitMgmtMacAddr,
       "swUnitMgmtStartPort": swUnitMgmtStartPort,
       "swUnitMgmtPortRange": swUnitMgmtPortRange,
       "swUnitMgmtFrontPanelLedStatus": swUnitMgmtFrontPanelLedStatus,
       "swUnitMgmtCtrlMode": swUnitMgmtCtrlMode,
       "swUnitMgmtCurrentMode": swUnitMgmtCurrentMode,
       "swUnitMgmtVersion": swUnitMgmtVersion,
       "swUnitMgmtModuleName": swUnitMgmtModuleName,
       "swUnitMgmtPromVersion": swUnitMgmtPromVersion,
       "swUnitMgmtFirmwareVersion": swUnitMgmtFirmwareVersion,
       "swUnitMgmtHardwareVersion": swUnitMgmtHardwareVersion,
       "swUnitMgmtPriority": swUnitMgmtPriority,
       "swUnitMgmtUserSetState": swUnitMgmtUserSetState,
       "swUnitMgmtExistState": swUnitMgmtExistState,
       "swUnitMgmtBoxId": swUnitMgmtBoxId,
       "swUnitMgmtSerialNumber": swUnitMgmtSerialNumber,
       "swUnitTopology": swUnitTopology,
       "swUnitStackMode": swUnitStackMode,
       "swUnitStackForceMasterRole": swUnitStackForceMasterRole,
       "swUnitStackTrapState": swUnitStackTrapState,
       "swUnitStackLogState": swUnitStackLogState,
       "swExternalAlarmTable": swExternalAlarmTable,
       "swExternalAlarmEntry": swExternalAlarmEntry,
       "swExternalAlarmChannel": swExternalAlarmChannel,
       "swExternalAlarmMessage": swExternalAlarmMessage,
       "swExternalAlarmStatus": swExternalAlarmStatus,
       "swEquipmentPowerSaving": swEquipmentPowerSaving,
       "swEquipPowerSavingLinkDetectState": swEquipPowerSavingLinkDetectState,
       "swEquipPowerSavingLenDetect": swEquipPowerSavingLenDetect,
       "swEquipPowerSavingHiberState": swEquipPowerSavingHiberState,
       "swEquipPowerSavingPortLEDState": swEquipPowerSavingPortLEDState,
       "swEquipPowerSavingPortState": swEquipPowerSavingPortState,
       "swEquipPowerSavingScheduleCtrl": swEquipPowerSavingScheduleCtrl,
       "swEquipPowerSavingHibernationTable": swEquipPowerSavingHibernationTable,
       "swEquipPowerSavingHibernationEntry": swEquipPowerSavingHibernationEntry,
       "swEquipPowerSavingHiberRowStatus": swEquipPowerSavingHiberRowStatus,
       "swEquipPowerSavingPortLedTable": swEquipPowerSavingPortLedTable,
       "swEquipPowerSavingPortLedEntry": swEquipPowerSavingPortLedEntry,
       "swEquipPowerSavingPortLedRowStatus": swEquipPowerSavingPortLedRowStatus,
       "swEquipPowerSavingPortTable": swEquipPowerSavingPortTable,
       "swEquipPowerSavingPortEntry": swEquipPowerSavingPortEntry,
       "swEquipPowerSavingPortIndex": swEquipPowerSavingPortIndex,
       "swEquipPowerSavingPortRowStatus": swEquipPowerSavingPortRowStatus,
       "swEquipmentTemperatureCtrl": swEquipmentTemperatureCtrl,
       "swTemperatureTrapState": swTemperatureTrapState,
       "swTemperatureLogState": swTemperatureLogState,
       "swEquipmentLEDCtrl": swEquipmentLEDCtrl,
       "swEquipmentPortLEDState": swEquipmentPortLEDState,
       "swExternalAlarmStackingTable": swExternalAlarmStackingTable,
       "swExternalAlarmStackingEntry": swExternalAlarmStackingEntry,
       "swExternalAlarmStackingUnitIndex": swExternalAlarmStackingUnitIndex,
       "swExternalAlarmStackingChannel": swExternalAlarmStackingChannel,
       "swExternalAlarmStackingMessage": swExternalAlarmStackingMessage,
       "swExternalAlarmStackingStatus": swExternalAlarmStackingStatus,
       "swEquipmentNotify": swEquipmentNotify,
       "swEquipmentNotifyMgmt": swEquipmentNotifyMgmt,
       "swEquipUnitNotifyMgmt": swEquipUnitNotifyMgmt,
       "swUnitInsertSeverity": swUnitInsertSeverity,
       "swUnitRemoveSeverity": swUnitRemoveSeverity,
       "swUnitFailureSeverity": swUnitFailureSeverity,
       "swEquipPowerNotifyMgmt": swEquipPowerNotifyMgmt,
       "swPowerStatusChgSeverity": swPowerStatusChgSeverity,
       "swPowerFailureSeverity": swPowerFailureSeverity,
       "swPowerRecoverSeverity": swPowerRecoverSeverity,
       "swEquipFanNotifyMgmt": swEquipFanNotifyMgmt,
       "swFanFailureSeverity": swFanFailureSeverity,
       "swFanRecoverSeverity": swFanRecoverSeverity,
       "swEquipTemperatureNotifyMgmt": swEquipTemperatureNotifyMgmt,
       "swHighTemperatureSeverity": swHighTemperatureSeverity,
       "swHighTemperatureRecoverSeverity": swHighTemperatureRecoverSeverity,
       "swLowTemperatureSeverity": swLowTemperatureSeverity,
       "swLowTemperatureRecoverSeverity": swLowTemperatureRecoverSeverity,
       "swEquipmentNotification": swEquipmentNotification,
       "swEquipUnitNotification": swEquipUnitNotification,
       "swEquipUnitNotifyPrefix": swEquipUnitNotifyPrefix,
       "swUnitInsert": swUnitInsert,
       "swUnitRemove": swUnitRemove,
       "swUnitFailure": swUnitFailure,
       "swUnitTPChange": swUnitTPChange,
       "swUnitRoleChange": swUnitRoleChange,
       "swEquipPowerNotification": swEquipPowerNotification,
       "swEquipPowerNotifyPerfix": swEquipPowerNotifyPerfix,
       "swPowerStatusChg": swPowerStatusChg,
       "swPowerFailure": swPowerFailure,
       "swPowerRecover": swPowerRecover,
       "swEquipFanNotification": swEquipFanNotification,
       "swEquipFanNotifyPrefix": swEquipFanNotifyPrefix,
       "swFanFailure": swFanFailure,
       "swFanRecover": swFanRecover,
       "swEquipTemperatureNotification": swEquipTemperatureNotification,
       "swEquipTemperatureNotifyPrefix": swEquipTemperatureNotifyPrefix,
       "swHighTemperature": swHighTemperature,
       "swHighTemperatureRecover": swHighTemperatureRecover,
       "swLowTemperature": swLowTemperature,
       "swLowTemperatureRecover": swLowTemperatureRecover,
       "swEquipExternalAlarmNotification": swEquipExternalAlarmNotification,
       "swEquipExternalAlarmNotifyPrefix": swEquipExternalAlarmNotifyPrefix,
       "swExternalAlarm": swExternalAlarm,
       "swExternalAlarmStacking": swExternalAlarmStacking,
       "swNotificationBindings": swNotificationBindings,
       "swEquipTemperNotifyBindings": swEquipTemperNotifyBindings,
       "swTemperSensorID": swTemperSensorID,
       "swEquipUnitNotifyBindings": swEquipUnitNotifyBindings,
       "swStackTopologyType": swStackTopologyType,
       "swStackRoleChangeType": swStackRoleChangeType}
)
