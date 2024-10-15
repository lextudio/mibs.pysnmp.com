# SNMP MIB module (E5-111-IESCOMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/E5-111-IESCOMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:10 2024
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

(e5x111,
 iesSeriesCommon) = mibBuilder.importSymbols(
    "E5-111-MIB",
    "e5x111",
    "iesSeriesCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IesChassis_ObjectIdentity = ObjectIdentity
iesChassis = _IesChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1)
)
_IesNumOfChassis_Type = Integer32
_IesNumOfChassis_Object = MibScalar
iesNumOfChassis = _IesNumOfChassis_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 1),
    _IesNumOfChassis_Type()
)
iesNumOfChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesNumOfChassis.setStatus("current")
_IesChassisTable_Object = MibTable
iesChassisTable = _IesChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2)
)
if mibBuilder.loadTexts:
    iesChassisTable.setStatus("current")
_IesChassisEntry_Object = MibTableRow
iesChassisEntry = _IesChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1)
)
iesChassisEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesChassisId"),
)
if mibBuilder.loadTexts:
    iesChassisEntry.setStatus("current")
_IesChassisId_Type = Integer32
_IesChassisId_Object = MibTableColumn
iesChassisId = _IesChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 1),
    _IesChassisId_Type()
)
iesChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisId.setStatus("current")
_IesChassisFrameNumber_Type = Integer32
_IesChassisFrameNumber_Object = MibTableColumn
iesChassisFrameNumber = _IesChassisFrameNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 2),
    _IesChassisFrameNumber_Type()
)
iesChassisFrameNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesChassisFrameNumber.setStatus("current")
_IesChassisSerialNumber_Type = DisplayString
_IesChassisSerialNumber_Object = MibTableColumn
iesChassisSerialNumber = _IesChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 3),
    _IesChassisSerialNumber_Type()
)
iesChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisSerialNumber.setStatus("current")
_IesChassisNumber_Type = Integer32
_IesChassisNumber_Object = MibTableColumn
iesChassisNumber = _IesChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 4),
    _IesChassisNumber_Type()
)
iesChassisNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesChassisNumber.setStatus("current")


class _IesChassisStatus_Type(Integer32):
    """Custom type iesChassisStatus based on Integer32"""
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
        *(("down", 3),
          ("empty", 1),
          ("testing", 4),
          ("up", 2))
    )


_IesChassisStatus_Type.__name__ = "Integer32"
_IesChassisStatus_Object = MibTableColumn
iesChassisStatus = _IesChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 5),
    _IesChassisStatus_Type()
)
iesChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisStatus.setStatus("current")
_IesChassisProductPartNumber_Type = DisplayString
_IesChassisProductPartNumber_Object = MibTableColumn
iesChassisProductPartNumber = _IesChassisProductPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 6),
    _IesChassisProductPartNumber_Type()
)
iesChassisProductPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisProductPartNumber.setStatus("current")
_IesChassisHwRevisionNumber_Type = DisplayString
_IesChassisHwRevisionNumber_Object = MibTableColumn
iesChassisHwRevisionNumber = _IesChassisHwRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 7),
    _IesChassisHwRevisionNumber_Type()
)
iesChassisHwRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisHwRevisionNumber.setStatus("current")
_IesChassisCleiCode_Type = DisplayString
_IesChassisCleiCode_Object = MibTableColumn
iesChassisCleiCode = _IesChassisCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 8),
    _IesChassisCleiCode_Type()
)
iesChassisCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisCleiCode.setStatus("current")
_IesChassisHwVersion_Type = DisplayString
_IesChassisHwVersion_Object = MibTableColumn
iesChassisHwVersion = _IesChassisHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 9),
    _IesChassisHwVersion_Type()
)
iesChassisHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisHwVersion.setStatus("current")
_IesChassisMacAddress_Type = DisplayString
_IesChassisMacAddress_Object = MibTableColumn
iesChassisMacAddress = _IesChassisMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 10),
    _IesChassisMacAddress_Type()
)
iesChassisMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisMacAddress.setStatus("current")
_IesChassisVoipDspVersion_Type = DisplayString
_IesChassisVoipDspVersion_Object = MibTableColumn
iesChassisVoipDspVersion = _IesChassisVoipDspVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 11),
    _IesChassisVoipDspVersion_Type()
)
iesChassisVoipDspVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisVoipDspVersion.setStatus("current")
_IesChassisCodecVersion_Type = DisplayString
_IesChassisCodecVersion_Object = MibTableColumn
iesChassisCodecVersion = _IesChassisCodecVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 2, 1, 12),
    _IesChassisCodecVersion_Type()
)
iesChassisCodecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesChassisCodecVersion.setStatus("current")
_IesSlotTable_Object = MibTable
iesSlotTable = _IesSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3)
)
if mibBuilder.loadTexts:
    iesSlotTable.setStatus("current")
_IesSlotEntry_Object = MibTableRow
iesSlotEntry = _IesSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3, 1)
)
iesSlotEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesChassisId"),
    (0, "E5-111-IESCOMMON-MIB", "iesSlotId"),
)
if mibBuilder.loadTexts:
    iesSlotEntry.setStatus("current")
_IesSlotId_Type = Integer32
_IesSlotId_Object = MibTableColumn
iesSlotId = _IesSlotId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3, 1, 1),
    _IesSlotId_Type()
)
iesSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSlotId.setStatus("current")


class _IesSlotModuleType_Type(Integer32):
    """Custom type iesSlotModuleType based on Integer32"""
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("alc1024-61", 4),
          ("alc1024-63", 7),
          ("alc1224-51", 13),
          ("alc1224-53", 14),
          ("alc1224-71", 10),
          ("alc1224-73", 11),
          ("msc1000-L2", 2),
          ("msc1000-ML", 3),
          ("msc1000A", 8),
          ("slc1024", 6),
          ("slc1224-22", 12),
          ("unknown", 1),
          ("vlc1012", 5),
          ("vlc1124", 9))
    )


_IesSlotModuleType_Type.__name__ = "Integer32"
_IesSlotModuleType_Object = MibTableColumn
iesSlotModuleType = _IesSlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3, 1, 2),
    _IesSlotModuleType_Type()
)
iesSlotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSlotModuleType.setStatus("current")
_IesSlotModuleDescr_Type = DisplayString
_IesSlotModuleDescr_Object = MibTableColumn
iesSlotModuleDescr = _IesSlotModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3, 1, 3),
    _IesSlotModuleDescr_Type()
)
iesSlotModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSlotModuleDescr.setStatus("current")
_IesSlotModuleFWVersion_Type = DisplayString
_IesSlotModuleFWVersion_Object = MibTableColumn
iesSlotModuleFWVersion = _IesSlotModuleFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3, 1, 4),
    _IesSlotModuleFWVersion_Type()
)
iesSlotModuleFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSlotModuleFWVersion.setStatus("current")
_IesSlotModuleDriverVersion_Type = DisplayString
_IesSlotModuleDriverVersion_Object = MibTableColumn
iesSlotModuleDriverVersion = _IesSlotModuleDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3, 1, 5),
    _IesSlotModuleDriverVersion_Type()
)
iesSlotModuleDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSlotModuleDriverVersion.setStatus("current")
_IesSlotModuleModemCodeVersion_Type = DisplayString
_IesSlotModuleModemCodeVersion_Object = MibTableColumn
iesSlotModuleModemCodeVersion = _IesSlotModuleModemCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3, 1, 6),
    _IesSlotModuleModemCodeVersion_Type()
)
iesSlotModuleModemCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSlotModuleModemCodeVersion.setStatus("current")


class _IesSlotModuleStatus_Type(Integer32):
    """Custom type iesSlotModuleStatus based on Integer32"""
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
        *(("down", 3),
          ("empty", 1),
          ("standby", 5),
          ("testing", 4),
          ("up", 2))
    )


_IesSlotModuleStatus_Type.__name__ = "Integer32"
_IesSlotModuleStatus_Object = MibTableColumn
iesSlotModuleStatus = _IesSlotModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3, 1, 7),
    _IesSlotModuleStatus_Type()
)
iesSlotModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSlotModuleStatus.setStatus("current")


class _IesSlotModuleAlarmStatus_Type(Integer32):
    """Custom type iesSlotModuleAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IesSlotModuleAlarmStatus_Type.__name__ = "Integer32"
_IesSlotModuleAlarmStatus_Object = MibTableColumn
iesSlotModuleAlarmStatus = _IesSlotModuleAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 3, 1, 8),
    _IesSlotModuleAlarmStatus_Type()
)
iesSlotModuleAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSlotModuleAlarmStatus.setStatus("current")
_IesMscPortConfTable_Object = MibTable
iesMscPortConfTable = _IesMscPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4)
)
if mibBuilder.loadTexts:
    iesMscPortConfTable.setStatus("current")
_IesMscPortConfEntry_Object = MibTableRow
iesMscPortConfEntry = _IesMscPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1)
)
iesMscPortConfEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesChassisId"),
    (0, "E5-111-IESCOMMON-MIB", "iesSlotId"),
    (0, "E5-111-IESCOMMON-MIB", "iesMscPortId"),
)
if mibBuilder.loadTexts:
    iesMscPortConfEntry.setStatus("current")
_IesMscPortId_Type = Integer32
_IesMscPortId_Object = MibTableColumn
iesMscPortId = _IesMscPortId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 1),
    _IesMscPortId_Type()
)
iesMscPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMscPortId.setStatus("current")


class _IesMscPortType_Type(Integer32):
    """Custom type iesMscPortType based on Integer32"""
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
        *(("e1000BaseGBIC", 7),
          ("e1000BaseLX", 3),
          ("e1000BaseSX", 4),
          ("e1000BaseT", 2),
          ("e100BaseFX", 5),
          ("e100BaseTX", 6),
          ("unknown", 1))
    )


_IesMscPortType_Type.__name__ = "Integer32"
_IesMscPortType_Object = MibTableColumn
iesMscPortType = _IesMscPortType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 2),
    _IesMscPortType_Type()
)
iesMscPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMscPortType.setStatus("current")
_IesMscPortIfIndex_Type = Integer32
_IesMscPortIfIndex_Object = MibTableColumn
iesMscPortIfIndex = _IesMscPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 3),
    _IesMscPortIfIndex_Type()
)
iesMscPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMscPortIfIndex.setStatus("current")


class _IesMscPortSpeed_Type(Integer32):
    """Custom type iesMscPortSpeed based on Integer32"""
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
        *(("auto", 1),
          ("e1000M", 2),
          ("e100M", 3),
          ("e10M", 4))
    )


_IesMscPortSpeed_Type.__name__ = "Integer32"
_IesMscPortSpeed_Object = MibTableColumn
iesMscPortSpeed = _IesMscPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 4),
    _IesMscPortSpeed_Type()
)
iesMscPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMscPortSpeed.setStatus("current")


class _IesMscPortDuplex_Type(Integer32):
    """Custom type iesMscPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_IesMscPortDuplex_Type.__name__ = "Integer32"
_IesMscPortDuplex_Object = MibTableColumn
iesMscPortDuplex = _IesMscPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 5),
    _IesMscPortDuplex_Type()
)
iesMscPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMscPortDuplex.setStatus("current")


class _IesMscPortFlowControl_Type(Integer32):
    """Custom type iesMscPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IesMscPortFlowControl_Type.__name__ = "Integer32"
_IesMscPortFlowControl_Object = MibTableColumn
iesMscPortFlowControl = _IesMscPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 6),
    _IesMscPortFlowControl_Type()
)
iesMscPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMscPortFlowControl.setStatus("current")


class _IesMscPortDefaultVLANTagging_Type(Integer32):
    """Custom type iesMscPortDefaultVLANTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IesMscPortDefaultVLANTagging_Type.__name__ = "Integer32"
_IesMscPortDefaultVLANTagging_Object = MibTableColumn
iesMscPortDefaultVLANTagging = _IesMscPortDefaultVLANTagging_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 7),
    _IesMscPortDefaultVLANTagging_Type()
)
iesMscPortDefaultVLANTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMscPortDefaultVLANTagging.setStatus("current")
_IesMscPortTrunkGroupId_Type = Integer32
_IesMscPortTrunkGroupId_Object = MibTableColumn
iesMscPortTrunkGroupId = _IesMscPortTrunkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 8),
    _IesMscPortTrunkGroupId_Type()
)
iesMscPortTrunkGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMscPortTrunkGroupId.setStatus("current")


class _IesMscPortMode_Type(Integer32):
    """Custom type iesMscPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("subtending", 2),
          ("uplink", 1))
    )


_IesMscPortMode_Type.__name__ = "Integer32"
_IesMscPortMode_Object = MibTableColumn
iesMscPortMode = _IesMscPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 9),
    _IesMscPortMode_Type()
)
iesMscPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMscPortMode.setStatus("current")


class _IesMscPortVLANTrunking_Type(Integer32):
    """Custom type iesMscPortVLANTrunking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IesMscPortVLANTrunking_Type.__name__ = "Integer32"
_IesMscPortVLANTrunking_Object = MibTableColumn
iesMscPortVLANTrunking = _IesMscPortVLANTrunking_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 1, 4, 1, 10),
    _IesMscPortVLANTrunking_Type()
)
iesMscPortVLANTrunking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMscPortVLANTrunking.setStatus("current")
_IesHWMonitor_ObjectIdentity = ObjectIdentity
iesHWMonitor = _IesHWMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2)
)
_IesFanRpmTable_Object = MibTable
iesFanRpmTable = _IesFanRpmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 1)
)
if mibBuilder.loadTexts:
    iesFanRpmTable.setStatus("current")
_IesFanRpmEntry_Object = MibTableRow
iesFanRpmEntry = _IesFanRpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 1, 1)
)
iesFanRpmEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesChassisId"),
    (0, "E5-111-IESCOMMON-MIB", "iesFanRpmIndex"),
)
if mibBuilder.loadTexts:
    iesFanRpmEntry.setStatus("current")
_IesFanRpmIndex_Type = Integer32
_IesFanRpmIndex_Object = MibTableColumn
iesFanRpmIndex = _IesFanRpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 1, 1, 1),
    _IesFanRpmIndex_Type()
)
iesFanRpmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesFanRpmIndex.setStatus("current")
_IesFanRpmCurValue_Type = Integer32
_IesFanRpmCurValue_Object = MibTableColumn
iesFanRpmCurValue = _IesFanRpmCurValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 1, 1, 2),
    _IesFanRpmCurValue_Type()
)
iesFanRpmCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesFanRpmCurValue.setStatus("current")
_IesFanRpmMaxValue_Type = Integer32
_IesFanRpmMaxValue_Object = MibTableColumn
iesFanRpmMaxValue = _IesFanRpmMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 1, 1, 3),
    _IesFanRpmMaxValue_Type()
)
iesFanRpmMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesFanRpmMaxValue.setStatus("current")
_IesFanRpmMinValue_Type = Integer32
_IesFanRpmMinValue_Object = MibTableColumn
iesFanRpmMinValue = _IesFanRpmMinValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 1, 1, 4),
    _IesFanRpmMinValue_Type()
)
iesFanRpmMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesFanRpmMinValue.setStatus("current")
_IesFanRpmLowThresh_Type = Integer32
_IesFanRpmLowThresh_Object = MibTableColumn
iesFanRpmLowThresh = _IesFanRpmLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 1, 1, 5),
    _IesFanRpmLowThresh_Type()
)
iesFanRpmLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesFanRpmLowThresh.setStatus("current")
_IesFanRpmDescr_Type = DisplayString
_IesFanRpmDescr_Object = MibTableColumn
iesFanRpmDescr = _IesFanRpmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 1, 1, 6),
    _IesFanRpmDescr_Type()
)
iesFanRpmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesFanRpmDescr.setStatus("current")
_IesVoltageTable_Object = MibTable
iesVoltageTable = _IesVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 2)
)
if mibBuilder.loadTexts:
    iesVoltageTable.setStatus("current")
_IesVoltageEntry_Object = MibTableRow
iesVoltageEntry = _IesVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 2, 1)
)
iesVoltageEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesChassisId"),
    (0, "E5-111-IESCOMMON-MIB", "iesSlotId"),
    (0, "E5-111-IESCOMMON-MIB", "iesVoltageIndex"),
)
if mibBuilder.loadTexts:
    iesVoltageEntry.setStatus("current")
_IesVoltageIndex_Type = Integer32
_IesVoltageIndex_Object = MibTableColumn
iesVoltageIndex = _IesVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 2, 1, 1),
    _IesVoltageIndex_Type()
)
iesVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesVoltageIndex.setStatus("current")
_IesVoltageCurValue_Type = Integer32
_IesVoltageCurValue_Object = MibTableColumn
iesVoltageCurValue = _IesVoltageCurValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 2, 1, 2),
    _IesVoltageCurValue_Type()
)
iesVoltageCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesVoltageCurValue.setStatus("current")
_IesVoltageMaxValue_Type = Integer32
_IesVoltageMaxValue_Object = MibTableColumn
iesVoltageMaxValue = _IesVoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 2, 1, 3),
    _IesVoltageMaxValue_Type()
)
iesVoltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesVoltageMaxValue.setStatus("current")
_IesVoltageMinValue_Type = Integer32
_IesVoltageMinValue_Object = MibTableColumn
iesVoltageMinValue = _IesVoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 2, 1, 4),
    _IesVoltageMinValue_Type()
)
iesVoltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesVoltageMinValue.setStatus("current")
_IesVoltageNominalValue_Type = Integer32
_IesVoltageNominalValue_Object = MibTableColumn
iesVoltageNominalValue = _IesVoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 2, 1, 5),
    _IesVoltageNominalValue_Type()
)
iesVoltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesVoltageNominalValue.setStatus("current")
_IesVoltageLowThresh_Type = Integer32
_IesVoltageLowThresh_Object = MibTableColumn
iesVoltageLowThresh = _IesVoltageLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 2, 1, 6),
    _IesVoltageLowThresh_Type()
)
iesVoltageLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesVoltageLowThresh.setStatus("current")
_IesVoltageDescr_Type = DisplayString
_IesVoltageDescr_Object = MibTableColumn
iesVoltageDescr = _IesVoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 2, 1, 7),
    _IesVoltageDescr_Type()
)
iesVoltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesVoltageDescr.setStatus("current")
_IesSysTempTable_Object = MibTable
iesSysTempTable = _IesSysTempTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 3)
)
if mibBuilder.loadTexts:
    iesSysTempTable.setStatus("current")
_IesSysTempEntry_Object = MibTableRow
iesSysTempEntry = _IesSysTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 3, 1)
)
iesSysTempEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesChassisId"),
    (0, "E5-111-IESCOMMON-MIB", "iesSlotId"),
    (0, "E5-111-IESCOMMON-MIB", "iesSysTempIndex"),
)
if mibBuilder.loadTexts:
    iesSysTempEntry.setStatus("current")
_IesSysTempIndex_Type = Integer32
_IesSysTempIndex_Object = MibTableColumn
iesSysTempIndex = _IesSysTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 3, 1, 1),
    _IesSysTempIndex_Type()
)
iesSysTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSysTempIndex.setStatus("current")
_IesSysTempCurValue_Type = Integer32
_IesSysTempCurValue_Object = MibTableColumn
iesSysTempCurValue = _IesSysTempCurValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 3, 1, 2),
    _IesSysTempCurValue_Type()
)
iesSysTempCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSysTempCurValue.setStatus("current")
_IesSysTempMaxValue_Type = Integer32
_IesSysTempMaxValue_Object = MibTableColumn
iesSysTempMaxValue = _IesSysTempMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 3, 1, 3),
    _IesSysTempMaxValue_Type()
)
iesSysTempMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSysTempMaxValue.setStatus("current")
_IesSysTempMinValue_Type = Integer32
_IesSysTempMinValue_Object = MibTableColumn
iesSysTempMinValue = _IesSysTempMinValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 3, 1, 4),
    _IesSysTempMinValue_Type()
)
iesSysTempMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSysTempMinValue.setStatus("current")
_IesSysTempHighThresh_Type = Integer32
_IesSysTempHighThresh_Object = MibTableColumn
iesSysTempHighThresh = _IesSysTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 3, 1, 5),
    _IesSysTempHighThresh_Type()
)
iesSysTempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSysTempHighThresh.setStatus("current")
_IesSysTempDescr_Type = DisplayString
_IesSysTempDescr_Object = MibTableColumn
iesSysTempDescr = _IesSysTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 2, 3, 1, 6),
    _IesSysTempDescr_Type()
)
iesSysTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSysTempDescr.setStatus("current")
_IesSysMgnt_ObjectIdentity = ObjectIdentity
iesSysMgnt = _IesSysMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3)
)
_IesSysState_ObjectIdentity = ObjectIdentity
iesSysState = _IesSysState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 1)
)


class _IesSystemCurrentStatus_Type(Integer32):
    """Custom type iesSystemCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IesSystemCurrentStatus_Type.__name__ = "Integer32"
_IesSystemCurrentStatus_Object = MibScalar
iesSystemCurrentStatus = _IesSystemCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 1, 1),
    _IesSystemCurrentStatus_Type()
)
iesSystemCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSystemCurrentStatus.setStatus("current")
_IesProblemCause_Type = DisplayString
_IesProblemCause_Object = MibScalar
iesProblemCause = _IesProblemCause_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 1, 2),
    _IesProblemCause_Type()
)
iesProblemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesProblemCause.setStatus("current")
_IesSysMaintenance_ObjectIdentity = ObjectIdentity
iesSysMaintenance = _IesSysMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2)
)
_IesMaintenanceOps_Type = Integer32
_IesMaintenanceOps_Object = MibScalar
iesMaintenanceOps = _IesMaintenanceOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 1),
    _IesMaintenanceOps_Type()
)
iesMaintenanceOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceOps.setStatus("current")


class _IesMaintenanceTarget_Type(Integer32):
    """Custom type iesMaintenanceTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IesMaintenanceTarget_Type.__name__ = "Integer32"
_IesMaintenanceTarget_Object = MibScalar
iesMaintenanceTarget = _IesMaintenanceTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 2),
    _IesMaintenanceTarget_Type()
)
iesMaintenanceTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceTarget.setStatus("current")
_IesMaintenanceDSLConfOps_Type = Integer32
_IesMaintenanceDSLConfOps_Object = MibScalar
iesMaintenanceDSLConfOps = _IesMaintenanceDSLConfOps_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 3),
    _IesMaintenanceDSLConfOps_Type()
)
iesMaintenanceDSLConfOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfOps.setStatus("current")
_IesMaintenanceDSLConfTarget_Type = OctetString
_IesMaintenanceDSLConfTarget_Object = MibScalar
iesMaintenanceDSLConfTarget = _IesMaintenanceDSLConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 4),
    _IesMaintenanceDSLConfTarget_Type()
)
iesMaintenanceDSLConfTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfTarget.setStatus("current")


class _IesMaintenanceDSLConfProfileName_Type(DisplayString):
    """Custom type iesMaintenanceDSLConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IesMaintenanceDSLConfProfileName_Type.__name__ = "DisplayString"
_IesMaintenanceDSLConfProfileName_Object = MibScalar
iesMaintenanceDSLConfProfileName = _IesMaintenanceDSLConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 5),
    _IesMaintenanceDSLConfProfileName_Type()
)
iesMaintenanceDSLConfProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfProfileName.setStatus("current")
_IesMaintenanceDSLConfMode_Type = Integer32
_IesMaintenanceDSLConfMode_Object = MibScalar
iesMaintenanceDSLConfMode = _IesMaintenanceDSLConfMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 6),
    _IesMaintenanceDSLConfMode_Type()
)
iesMaintenanceDSLConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfMode.setStatus("current")
_IesMaintenanceDSLConfPktFilter_Type = Integer32
_IesMaintenanceDSLConfPktFilter_Object = MibScalar
iesMaintenanceDSLConfPktFilter = _IesMaintenanceDSLConfPktFilter_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 7),
    _IesMaintenanceDSLConfPktFilter_Type()
)
iesMaintenanceDSLConfPktFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfPktFilter.setStatus("current")


class _IesMaintenanceDSLConfDot1xControl_Type(Integer32):
    """Custom type iesMaintenanceDSLConfDot1xControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnAuth", 3))
    )


_IesMaintenanceDSLConfDot1xControl_Type.__name__ = "Integer32"
_IesMaintenanceDSLConfDot1xControl_Object = MibScalar
iesMaintenanceDSLConfDot1xControl = _IesMaintenanceDSLConfDot1xControl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 8),
    _IesMaintenanceDSLConfDot1xControl_Type()
)
iesMaintenanceDSLConfDot1xControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfDot1xControl.setStatus("current")
_IesMaintenanceDSLConfDot1xReauthPeriod_Type = Integer32
_IesMaintenanceDSLConfDot1xReauthPeriod_Object = MibScalar
iesMaintenanceDSLConfDot1xReauthPeriod = _IesMaintenanceDSLConfDot1xReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 9),
    _IesMaintenanceDSLConfDot1xReauthPeriod_Type()
)
iesMaintenanceDSLConfDot1xReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfDot1xReauthPeriod.setStatus("current")
_IesMaintenanceDSLConfMacCount_Type = Integer32
_IesMaintenanceDSLConfMacCount_Object = MibScalar
iesMaintenanceDSLConfMacCount = _IesMaintenanceDSLConfMacCount_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 10),
    _IesMaintenanceDSLConfMacCount_Type()
)
iesMaintenanceDSLConfMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfMacCount.setStatus("current")


class _IesMaintenanceVpi_Type(Integer32):
    """Custom type iesMaintenanceVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IesMaintenanceVpi_Type.__name__ = "Integer32"
_IesMaintenanceVpi_Object = MibScalar
iesMaintenanceVpi = _IesMaintenanceVpi_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 11),
    _IesMaintenanceVpi_Type()
)
iesMaintenanceVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceVpi.setStatus("current")


class _IesMaintenanceVci_Type(Integer32):
    """Custom type iesMaintenanceVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IesMaintenanceVci_Type.__name__ = "Integer32"
_IesMaintenanceVci_Object = MibScalar
iesMaintenanceVci = _IesMaintenanceVci_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 12),
    _IesMaintenanceVci_Type()
)
iesMaintenanceVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceVci.setStatus("current")


class _IesMaintenanceDSLConfAlarmProfileName_Type(OctetString):
    """Custom type iesMaintenanceDSLConfAlarmProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IesMaintenanceDSLConfAlarmProfileName_Type.__name__ = "OctetString"
_IesMaintenanceDSLConfAlarmProfileName_Object = MibScalar
iesMaintenanceDSLConfAlarmProfileName = _IesMaintenanceDSLConfAlarmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 13),
    _IesMaintenanceDSLConfAlarmProfileName_Type()
)
iesMaintenanceDSLConfAlarmProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfAlarmProfileName.setStatus("current")


class _IesMaintenanceDSLConfAnnexL_Type(Integer32):
    """Custom type iesMaintenanceDSLConfAnnexL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enableNarrowMode", 1),
          ("enableWideMode", 2))
    )


_IesMaintenanceDSLConfAnnexL_Type.__name__ = "Integer32"
_IesMaintenanceDSLConfAnnexL_Object = MibScalar
iesMaintenanceDSLConfAnnexL = _IesMaintenanceDSLConfAnnexL_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 14),
    _IesMaintenanceDSLConfAnnexL_Type()
)
iesMaintenanceDSLConfAnnexL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfAnnexL.setStatus("current")


class _IesMaintenanceDSLConfPmMode_Type(Integer32):
    """Custom type iesMaintenanceDSLConfPmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enableL2Mode", 1),
          ("enableL3Mode", 2))
    )


_IesMaintenanceDSLConfPmMode_Type.__name__ = "Integer32"
_IesMaintenanceDSLConfPmMode_Object = MibScalar
iesMaintenanceDSLConfPmMode = _IesMaintenanceDSLConfPmMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 15),
    _IesMaintenanceDSLConfPmMode_Type()
)
iesMaintenanceDSLConfPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfPmMode.setStatus("current")


class _IesMaintenanceDSLConfRateMode_Type(Integer32):
    """Custom type iesMaintenanceDSLConfRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptAtRuntime", 3),
          ("adaptAtStartup", 2),
          ("fixed", 1))
    )


_IesMaintenanceDSLConfRateMode_Type.__name__ = "Integer32"
_IesMaintenanceDSLConfRateMode_Object = MibScalar
iesMaintenanceDSLConfRateMode = _IesMaintenanceDSLConfRateMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 16),
    _IesMaintenanceDSLConfRateMode_Type()
)
iesMaintenanceDSLConfRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfRateMode.setStatus("current")


class _IesMaintenanceDSLConfIgmpFilter_Type(OctetString):
    """Custom type iesMaintenanceDSLConfIgmpFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IesMaintenanceDSLConfIgmpFilter_Type.__name__ = "OctetString"
_IesMaintenanceDSLConfIgmpFilter_Object = MibScalar
iesMaintenanceDSLConfIgmpFilter = _IesMaintenanceDSLConfIgmpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 2, 17),
    _IesMaintenanceDSLConfIgmpFilter_Type()
)
iesMaintenanceDSLConfIgmpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMaintenanceDSLConfIgmpFilter.setStatus("current")
_IesSysTimeSetup_ObjectIdentity = ObjectIdentity
iesSysTimeSetup = _IesSysTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 3)
)


class _IesTimeServerMode_Type(Integer32):
    """Custom type iesTimeServerMode based on Integer32"""
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
        *(("daytime", 2),
          ("none", 1),
          ("ntp", 4),
          ("time", 3))
    )


_IesTimeServerMode_Type.__name__ = "Integer32"
_IesTimeServerMode_Object = MibScalar
iesTimeServerMode = _IesTimeServerMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 3, 1),
    _IesTimeServerMode_Type()
)
iesTimeServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesTimeServerMode.setStatus("current")
_IesTimeServerIP_Type = IpAddress
_IesTimeServerIP_Object = MibScalar
iesTimeServerIP = _IesTimeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 3, 2),
    _IesTimeServerIP_Type()
)
iesTimeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesTimeServerIP.setStatus("current")
_IesSystemTime_Type = DisplayString
_IesSystemTime_Object = MibScalar
iesSystemTime = _IesSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 3, 3),
    _IesSystemTime_Type()
)
iesSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSystemTime.setStatus("current")
_IesSystemDate_Type = DisplayString
_IesSystemDate_Object = MibScalar
iesSystemDate = _IesSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 3, 4),
    _IesSystemDate_Type()
)
iesSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSystemDate.setStatus("current")


class _IesSystemTimeZone_Type(Integer32):
    """Custom type iesSystemTimeZone based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("utc", 13),
          ("utc-0100", 12),
          ("utc-0200", 11),
          ("utc-0300", 10),
          ("utc-0400", 9),
          ("utc-0500", 8),
          ("utc-0600", 7),
          ("utc-0700", 6),
          ("utc-0800", 5),
          ("utc-0900", 4),
          ("utc-1000", 3),
          ("utc-1100", 2),
          ("utc-1200", 1),
          ("utc0100", 14),
          ("utc0200", 15),
          ("utc0300", 16),
          ("utc0400", 17),
          ("utc0500", 18),
          ("utc0600", 19),
          ("utc0700", 20),
          ("utc0800", 21),
          ("utc0900", 22),
          ("utc1000", 23),
          ("utc1100", 24),
          ("utc1200", 25))
    )


_IesSystemTimeZone_Type.__name__ = "Integer32"
_IesSystemTimeZone_Object = MibScalar
iesSystemTimeZone = _IesSystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 3, 5),
    _IesSystemTimeZone_Type()
)
iesSystemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSystemTimeZone.setStatus("current")
_IesSysAccessControl_ObjectIdentity = ObjectIdentity
iesSysAccessControl = _IesSysAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4)
)
_IesAccessCtrlTable_Object = MibTable
iesAccessCtrlTable = _IesAccessCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 1)
)
if mibBuilder.loadTexts:
    iesAccessCtrlTable.setStatus("current")
_IesAccessCtrlEntry_Object = MibTableRow
iesAccessCtrlEntry = _IesAccessCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 1, 1)
)
iesAccessCtrlEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesAccessCtrlService"),
)
if mibBuilder.loadTexts:
    iesAccessCtrlEntry.setStatus("current")


class _IesAccessCtrlService_Type(Integer32):
    """Custom type iesAccessCtrlService based on Integer32"""
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
        *(("ftp", 2),
          ("icmp", 4),
          ("telnet", 1),
          ("web", 3))
    )


_IesAccessCtrlService_Type.__name__ = "Integer32"
_IesAccessCtrlService_Object = MibTableColumn
iesAccessCtrlService = _IesAccessCtrlService_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 1, 1, 1),
    _IesAccessCtrlService_Type()
)
iesAccessCtrlService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesAccessCtrlService.setStatus("current")


class _IesAccessCtrlEnable_Type(Integer32):
    """Custom type iesAccessCtrlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IesAccessCtrlEnable_Type.__name__ = "Integer32"
_IesAccessCtrlEnable_Object = MibTableColumn
iesAccessCtrlEnable = _IesAccessCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 1, 1, 2),
    _IesAccessCtrlEnable_Type()
)
iesAccessCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesAccessCtrlEnable.setStatus("current")
_IesAccessCtrlPort_Type = Integer32
_IesAccessCtrlPort_Object = MibTableColumn
iesAccessCtrlPort = _IesAccessCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 1, 1, 3),
    _IesAccessCtrlPort_Type()
)
iesAccessCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesAccessCtrlPort.setStatus("current")
_IesMaxNumOfSecuredClients_Type = Integer32
_IesMaxNumOfSecuredClients_Object = MibScalar
iesMaxNumOfSecuredClients = _IesMaxNumOfSecuredClients_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 2),
    _IesMaxNumOfSecuredClients_Type()
)
iesMaxNumOfSecuredClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumOfSecuredClients.setStatus("current")
_IesSecuredClientTable_Object = MibTable
iesSecuredClientTable = _IesSecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 3)
)
if mibBuilder.loadTexts:
    iesSecuredClientTable.setStatus("current")
_IesSecuredClientEntry_Object = MibTableRow
iesSecuredClientEntry = _IesSecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 3, 1)
)
iesSecuredClientEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesSecuredClientStartIp"),
    (0, "E5-111-IESCOMMON-MIB", "iesSecuredClientEndIp"),
)
if mibBuilder.loadTexts:
    iesSecuredClientEntry.setStatus("current")
_IesSecuredClientStartIp_Type = IpAddress
_IesSecuredClientStartIp_Object = MibTableColumn
iesSecuredClientStartIp = _IesSecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 3, 1, 1),
    _IesSecuredClientStartIp_Type()
)
iesSecuredClientStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSecuredClientStartIp.setStatus("current")
_IesSecuredClientEndIp_Type = IpAddress
_IesSecuredClientEndIp_Object = MibTableColumn
iesSecuredClientEndIp = _IesSecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 3, 1, 2),
    _IesSecuredClientEndIp_Type()
)
iesSecuredClientEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesSecuredClientEndIp.setStatus("current")
_IesSecuredClientService_Type = Integer32
_IesSecuredClientService_Object = MibTableColumn
iesSecuredClientService = _IesSecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 3, 1, 3),
    _IesSecuredClientService_Type()
)
iesSecuredClientService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesSecuredClientService.setStatus("current")
_IesSecuredClientRowStatus_Type = RowStatus
_IesSecuredClientRowStatus_Object = MibTableColumn
iesSecuredClientRowStatus = _IesSecuredClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 4, 3, 1, 4),
    _IesSecuredClientRowStatus_Type()
)
iesSecuredClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesSecuredClientRowStatus.setStatus("current")
_IesSysStaticRoute_ObjectIdentity = ObjectIdentity
iesSysStaticRoute = _IesSysStaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5)
)
_IesMaxNumOfStaticRoutes_Type = Integer32
_IesMaxNumOfStaticRoutes_Object = MibScalar
iesMaxNumOfStaticRoutes = _IesMaxNumOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5, 1),
    _IesMaxNumOfStaticRoutes_Type()
)
iesMaxNumOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumOfStaticRoutes.setStatus("current")
_IesStaticRouteTable_Object = MibTable
iesStaticRouteTable = _IesStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5, 2)
)
if mibBuilder.loadTexts:
    iesStaticRouteTable.setStatus("current")
_IesStaticRouteEntry_Object = MibTableRow
iesStaticRouteEntry = _IesStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5, 2, 1)
)
iesStaticRouteEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesStaticRouteName"),
)
if mibBuilder.loadTexts:
    iesStaticRouteEntry.setStatus("current")
_IesStaticRouteName_Type = DisplayString
_IesStaticRouteName_Object = MibTableColumn
iesStaticRouteName = _IesStaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5, 2, 1, 1),
    _IesStaticRouteName_Type()
)
iesStaticRouteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesStaticRouteName.setStatus("current")
_IesStaticRouteDest_Type = IpAddress
_IesStaticRouteDest_Object = MibTableColumn
iesStaticRouteDest = _IesStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5, 2, 1, 2),
    _IesStaticRouteDest_Type()
)
iesStaticRouteDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesStaticRouteDest.setStatus("current")
_IesStaticRouteMask_Type = IpAddress
_IesStaticRouteMask_Object = MibTableColumn
iesStaticRouteMask = _IesStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5, 2, 1, 3),
    _IesStaticRouteMask_Type()
)
iesStaticRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesStaticRouteMask.setStatus("current")
_IesStaticRouteGateway_Type = IpAddress
_IesStaticRouteGateway_Object = MibTableColumn
iesStaticRouteGateway = _IesStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5, 2, 1, 4),
    _IesStaticRouteGateway_Type()
)
iesStaticRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesStaticRouteGateway.setStatus("current")
_IesStaticRouteMetric_Type = Integer32
_IesStaticRouteMetric_Object = MibTableColumn
iesStaticRouteMetric = _IesStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5, 2, 1, 5),
    _IesStaticRouteMetric_Type()
)
iesStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesStaticRouteMetric.setStatus("current")
_IesStaticRouteRowStatus_Type = RowStatus
_IesStaticRouteRowStatus_Object = MibTableColumn
iesStaticRouteRowStatus = _IesStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 5, 2, 1, 6),
    _IesStaticRouteRowStatus_Type()
)
iesStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesStaticRouteRowStatus.setStatus("current")
_IesSyslogSetup_ObjectIdentity = ObjectIdentity
iesSyslogSetup = _IesSyslogSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 6)
)
_IesSysLogEnable_Type = Integer32
_IesSysLogEnable_Object = MibScalar
iesSysLogEnable = _IesSysLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 6, 1),
    _IesSysLogEnable_Type()
)
iesSysLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSysLogEnable.setStatus("current")
_IesSysLogServer_Type = IpAddress
_IesSysLogServer_Object = MibScalar
iesSysLogServer = _IesSysLogServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 6, 2),
    _IesSysLogServer_Type()
)
iesSysLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSysLogServer.setStatus("current")


class _IesSysLogFacility_Type(Integer32):
    """Custom type iesSysLogFacility based on Integer32"""
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
        *(("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_IesSysLogFacility_Type.__name__ = "Integer32"
_IesSysLogFacility_Object = MibScalar
iesSysLogFacility = _IesSysLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 6, 3),
    _IesSysLogFacility_Type()
)
iesSysLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSysLogFacility.setStatus("current")
_IesSysDhcpSetup_ObjectIdentity = ObjectIdentity
iesSysDhcpSetup = _IesSysDhcpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 7)
)


class _IesDhcpRelayEnable_Type(Integer32):
    """Custom type iesDhcpRelayEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IesDhcpRelayEnable_Type.__name__ = "Integer32"
_IesDhcpRelayEnable_Object = MibScalar
iesDhcpRelayEnable = _IesDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 7, 1),
    _IesDhcpRelayEnable_Type()
)
iesDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesDhcpRelayEnable.setStatus("current")


class _IesDhcpRelayOption82Enable_Type(Integer32):
    """Custom type iesDhcpRelayOption82Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IesDhcpRelayOption82Enable_Type.__name__ = "Integer32"
_IesDhcpRelayOption82Enable_Object = MibScalar
iesDhcpRelayOption82Enable = _IesDhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 7, 2),
    _IesDhcpRelayOption82Enable_Type()
)
iesDhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesDhcpRelayOption82Enable.setStatus("current")
_IesDhcpRelayOption82Info_Type = DisplayString
_IesDhcpRelayOption82Info_Object = MibScalar
iesDhcpRelayOption82Info = _IesDhcpRelayOption82Info_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 7, 3),
    _IesDhcpRelayOption82Info_Type()
)
iesDhcpRelayOption82Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesDhcpRelayOption82Info.setStatus("current")
_IesMaxNumOfDhcpServers_Type = Integer32
_IesMaxNumOfDhcpServers_Object = MibScalar
iesMaxNumOfDhcpServers = _IesMaxNumOfDhcpServers_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 7, 4),
    _IesMaxNumOfDhcpServers_Type()
)
iesMaxNumOfDhcpServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumOfDhcpServers.setStatus("current")
_IesDhcpServerTable_Object = MibTable
iesDhcpServerTable = _IesDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 7, 5)
)
if mibBuilder.loadTexts:
    iesDhcpServerTable.setStatus("current")
_IesDhcpServerEntry_Object = MibTableRow
iesDhcpServerEntry = _IesDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 7, 5, 1)
)
iesDhcpServerEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesDhcpServerIp"),
)
if mibBuilder.loadTexts:
    iesDhcpServerEntry.setStatus("current")
_IesDhcpServerIp_Type = IpAddress
_IesDhcpServerIp_Object = MibTableColumn
iesDhcpServerIp = _IesDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 7, 5, 1, 1),
    _IesDhcpServerIp_Type()
)
iesDhcpServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesDhcpServerIp.setStatus("current")
_IesDhcpServerRowStatus_Type = RowStatus
_IesDhcpServerRowStatus_Object = MibTableColumn
iesDhcpServerRowStatus = _IesDhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 7, 5, 1, 2),
    _IesDhcpServerRowStatus_Type()
)
iesDhcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesDhcpServerRowStatus.setStatus("current")
_IesSysSNMPSetup_ObjectIdentity = ObjectIdentity
iesSysSNMPSetup = _IesSysSNMPSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8)
)
_IesMaxNumberOfTrapDestinations_Type = Integer32
_IesMaxNumberOfTrapDestinations_Object = MibScalar
iesMaxNumberOfTrapDestinations = _IesMaxNumberOfTrapDestinations_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8, 1),
    _IesMaxNumberOfTrapDestinations_Type()
)
iesMaxNumberOfTrapDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumberOfTrapDestinations.setStatus("current")
_IesSNMPTrapDestTable_Object = MibTable
iesSNMPTrapDestTable = _IesSNMPTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8, 2)
)
if mibBuilder.loadTexts:
    iesSNMPTrapDestTable.setStatus("current")
_IesSNMPTrapDestEntry_Object = MibTableRow
iesSNMPTrapDestEntry = _IesSNMPTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8, 2, 1)
)
iesSNMPTrapDestEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesTrapDestIp"),
    (0, "E5-111-IESCOMMON-MIB", "iesTrapDestPort"),
)
if mibBuilder.loadTexts:
    iesSNMPTrapDestEntry.setStatus("current")
_IesTrapDestIp_Type = IpAddress
_IesTrapDestIp_Object = MibTableColumn
iesTrapDestIp = _IesTrapDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8, 2, 1, 1),
    _IesTrapDestIp_Type()
)
iesTrapDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesTrapDestIp.setStatus("current")
_IesTrapDestPort_Type = Integer32
_IesTrapDestPort_Object = MibTableColumn
iesTrapDestPort = _IesTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8, 2, 1, 2),
    _IesTrapDestPort_Type()
)
iesTrapDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesTrapDestPort.setStatus("current")
_IesTrapDestRowStatus_Type = RowStatus
_IesTrapDestRowStatus_Object = MibTableColumn
iesTrapDestRowStatus = _IesTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8, 2, 1, 3),
    _IesTrapDestRowStatus_Type()
)
iesTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesTrapDestRowStatus.setStatus("current")
_IesSnmpGetCommunity_Type = DisplayString
_IesSnmpGetCommunity_Object = MibScalar
iesSnmpGetCommunity = _IesSnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8, 3),
    _IesSnmpGetCommunity_Type()
)
iesSnmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSnmpGetCommunity.setStatus("current")
_IesSnmpSetCommunity_Type = DisplayString
_IesSnmpSetCommunity_Object = MibScalar
iesSnmpSetCommunity = _IesSnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8, 4),
    _IesSnmpSetCommunity_Type()
)
iesSnmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSnmpSetCommunity.setStatus("current")
_IesSnmpTrapCommunity_Type = DisplayString
_IesSnmpTrapCommunity_Object = MibScalar
iesSnmpTrapCommunity = _IesSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 8, 5),
    _IesSnmpTrapCommunity_Type()
)
iesSnmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSnmpTrapCommunity.setStatus("current")
_IesSysDot1xSetup_ObjectIdentity = ObjectIdentity
iesSysDot1xSetup = _IesSysDot1xSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9)
)
_IesMaxNumberOfRadiusServers_Type = Integer32
_IesMaxNumberOfRadiusServers_Object = MibScalar
iesMaxNumberOfRadiusServers = _IesMaxNumberOfRadiusServers_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 1),
    _IesMaxNumberOfRadiusServers_Type()
)
iesMaxNumberOfRadiusServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumberOfRadiusServers.setStatus("current")
_IesRadiusServerTable_Object = MibTable
iesRadiusServerTable = _IesRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 2)
)
if mibBuilder.loadTexts:
    iesRadiusServerTable.setStatus("current")
_IesRadiusServerEntry_Object = MibTableRow
iesRadiusServerEntry = _IesRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 2, 1)
)
iesRadiusServerEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    iesRadiusServerEntry.setStatus("current")
_IesRadiusServerIndex_Type = Integer32
_IesRadiusServerIndex_Object = MibTableColumn
iesRadiusServerIndex = _IesRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 2, 1, 1),
    _IesRadiusServerIndex_Type()
)
iesRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesRadiusServerIndex.setStatus("current")
_IesRadiusServerIp_Type = IpAddress
_IesRadiusServerIp_Object = MibTableColumn
iesRadiusServerIp = _IesRadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 2, 1, 2),
    _IesRadiusServerIp_Type()
)
iesRadiusServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesRadiusServerIp.setStatus("current")
_IesRadiusServerPort_Type = Integer32
_IesRadiusServerPort_Object = MibTableColumn
iesRadiusServerPort = _IesRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 2, 1, 3),
    _IesRadiusServerPort_Type()
)
iesRadiusServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesRadiusServerPort.setStatus("current")
_IesRadiusSharedSecret_Type = DisplayString
_IesRadiusSharedSecret_Object = MibTableColumn
iesRadiusSharedSecret = _IesRadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 2, 1, 4),
    _IesRadiusSharedSecret_Type()
)
iesRadiusSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesRadiusSharedSecret.setStatus("current")
_IesRadiusServerRowStatus_Type = RowStatus
_IesRadiusServerRowStatus_Object = MibTableColumn
iesRadiusServerRowStatus = _IesRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 2, 1, 5),
    _IesRadiusServerRowStatus_Type()
)
iesRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesRadiusServerRowStatus.setStatus("current")


class _IesDot1xEnable_Type(Integer32):
    """Custom type iesDot1xEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IesDot1xEnable_Type.__name__ = "Integer32"
_IesDot1xEnable_Object = MibScalar
iesDot1xEnable = _IesDot1xEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 3),
    _IesDot1xEnable_Type()
)
iesDot1xEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesDot1xEnable.setStatus("current")
_IesDot1xPortTable_Object = MibTable
iesDot1xPortTable = _IesDot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 4)
)
if mibBuilder.loadTexts:
    iesDot1xPortTable.setStatus("current")
_IesDot1xPortEntry_Object = MibTableRow
iesDot1xPortEntry = _IesDot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 4, 1)
)
iesDot1xPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    iesDot1xPortEntry.setStatus("current")


class _IesDot1xPortEnable_Type(Integer32):
    """Custom type iesDot1xPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IesDot1xPortEnable_Type.__name__ = "Integer32"
_IesDot1xPortEnable_Object = MibTableColumn
iesDot1xPortEnable = _IesDot1xPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 4, 1, 1),
    _IesDot1xPortEnable_Type()
)
iesDot1xPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesDot1xPortEnable.setStatus("current")


class _IesDot1xPortControl_Type(Integer32):
    """Custom type iesDot1xPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnAuth", 3))
    )


_IesDot1xPortControl_Type.__name__ = "Integer32"
_IesDot1xPortControl_Object = MibTableColumn
iesDot1xPortControl = _IesDot1xPortControl_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 4, 1, 2),
    _IesDot1xPortControl_Type()
)
iesDot1xPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesDot1xPortControl.setStatus("current")


class _IesDot1xPortReAuthEnable_Type(Integer32):
    """Custom type iesDot1xPortReAuthEnable based on Integer32"""
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


_IesDot1xPortReAuthEnable_Type.__name__ = "Integer32"
_IesDot1xPortReAuthEnable_Object = MibTableColumn
iesDot1xPortReAuthEnable = _IesDot1xPortReAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 4, 1, 3),
    _IesDot1xPortReAuthEnable_Type()
)
iesDot1xPortReAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesDot1xPortReAuthEnable.setStatus("current")
_IesDot1xPortReAuthPeriod_Type = Integer32
_IesDot1xPortReAuthPeriod_Object = MibTableColumn
iesDot1xPortReAuthPeriod = _IesDot1xPortReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 9, 4, 1, 4),
    _IesDot1xPortReAuthPeriod_Type()
)
iesDot1xPortReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesDot1xPortReAuthPeriod.setStatus("current")
_IesSysMacFilter_ObjectIdentity = ObjectIdentity
iesSysMacFilter = _IesSysMacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10)
)
_IesMacFilterStatusTable_Object = MibTable
iesMacFilterStatusTable = _IesMacFilterStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 1)
)
if mibBuilder.loadTexts:
    iesMacFilterStatusTable.setStatus("current")
_IesMacFilterStatusEntry_Object = MibTableRow
iesMacFilterStatusEntry = _IesMacFilterStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 1, 1)
)
iesMacFilterStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    iesMacFilterStatusEntry.setStatus("current")


class _IesMacFilterStatusEnable_Type(Integer32):
    """Custom type iesMacFilterStatusEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enableAccept", 1),
          ("enableDeny", 3))
    )


_IesMacFilterStatusEnable_Type.__name__ = "Integer32"
_IesMacFilterStatusEnable_Object = MibTableColumn
iesMacFilterStatusEnable = _IesMacFilterStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 1, 1, 1),
    _IesMacFilterStatusEnable_Type()
)
iesMacFilterStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMacFilterStatusEnable.setStatus("current")
_IesMaxNumberOfMacFilters_Type = Integer32
_IesMaxNumberOfMacFilters_Object = MibScalar
iesMaxNumberOfMacFilters = _IesMaxNumberOfMacFilters_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 2),
    _IesMaxNumberOfMacFilters_Type()
)
iesMaxNumberOfMacFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumberOfMacFilters.setStatus("current")
_IesMaxNumberOfMacFiltersPerPort_Type = Integer32
_IesMaxNumberOfMacFiltersPerPort_Object = MibScalar
iesMaxNumberOfMacFiltersPerPort = _IesMaxNumberOfMacFiltersPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 3),
    _IesMaxNumberOfMacFiltersPerPort_Type()
)
iesMaxNumberOfMacFiltersPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumberOfMacFiltersPerPort.setStatus("current")
_IesCurrNumberOfMacFilters_Type = Integer32
_IesCurrNumberOfMacFilters_Object = MibScalar
iesCurrNumberOfMacFilters = _IesCurrNumberOfMacFilters_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 4),
    _IesCurrNumberOfMacFilters_Type()
)
iesCurrNumberOfMacFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesCurrNumberOfMacFilters.setStatus("current")
_IesMacFilterTable_Object = MibTable
iesMacFilterTable = _IesMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 5)
)
if mibBuilder.loadTexts:
    iesMacFilterTable.setStatus("current")
_IesMacFilterEntry_Object = MibTableRow
iesMacFilterEntry = _IesMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 5, 1)
)
iesMacFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E5-111-IESCOMMON-MIB", "iesMacFilterMacAddr"),
)
if mibBuilder.loadTexts:
    iesMacFilterEntry.setStatus("current")
_IesMacFilterMacAddr_Type = PhysAddress
_IesMacFilterMacAddr_Object = MibTableColumn
iesMacFilterMacAddr = _IesMacFilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 5, 1, 1),
    _IesMacFilterMacAddr_Type()
)
iesMacFilterMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMacFilterMacAddr.setStatus("current")
_IesMacFilterRowStatus_Type = RowStatus
_IesMacFilterRowStatus_Object = MibTableColumn
iesMacFilterRowStatus = _IesMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 10, 5, 1, 2),
    _IesMacFilterRowStatus_Type()
)
iesMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesMacFilterRowStatus.setStatus("current")
_IesSysPacketFilter_ObjectIdentity = ObjectIdentity
iesSysPacketFilter = _IesSysPacketFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 11)
)
_IesPacketFilterTable_Object = MibTable
iesPacketFilterTable = _IesPacketFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 11, 1)
)
if mibBuilder.loadTexts:
    iesPacketFilterTable.setStatus("current")
_IesPacketFilterEntry_Object = MibTableRow
iesPacketFilterEntry = _IesPacketFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 11, 1, 1)
)
iesPacketFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    iesPacketFilterEntry.setStatus("current")
_IesPacketFilter_Type = Integer32
_IesPacketFilter_Object = MibTableColumn
iesPacketFilter = _IesPacketFilter_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 11, 1, 1, 1),
    _IesPacketFilter_Type()
)
iesPacketFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesPacketFilter.setStatus("current")
_IesSysMacCountFilter_ObjectIdentity = ObjectIdentity
iesSysMacCountFilter = _IesSysMacCountFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 12)
)
_IesMacCountFilterTable_Object = MibTable
iesMacCountFilterTable = _IesMacCountFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 12, 1)
)
if mibBuilder.loadTexts:
    iesMacCountFilterTable.setStatus("current")
_IesMacCountFilterEntry_Object = MibTableRow
iesMacCountFilterEntry = _IesMacCountFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 12, 1, 1)
)
iesMacCountFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    iesMacCountFilterEntry.setStatus("current")


class _IesMacCountFilterStatus_Type(Integer32):
    """Custom type iesMacCountFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IesMacCountFilterStatus_Type.__name__ = "Integer32"
_IesMacCountFilterStatus_Object = MibTableColumn
iesMacCountFilterStatus = _IesMacCountFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 12, 1, 1, 1),
    _IesMacCountFilterStatus_Type()
)
iesMacCountFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMacCountFilterStatus.setStatus("current")
_IesMacCountFilterCount_Type = Integer32
_IesMacCountFilterCount_Object = MibTableColumn
iesMacCountFilterCount = _IesMacCountFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 12, 1, 1, 2),
    _IesMacCountFilterCount_Type()
)
iesMacCountFilterCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesMacCountFilterCount.setStatus("current")
_IesSysMulticastGroup_ObjectIdentity = ObjectIdentity
iesSysMulticastGroup = _IesSysMulticastGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 13)
)
_IesMaxNumberOfMulticastGroups_Type = Integer32
_IesMaxNumberOfMulticastGroups_Object = MibScalar
iesMaxNumberOfMulticastGroups = _IesMaxNumberOfMulticastGroups_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 13, 1),
    _IesMaxNumberOfMulticastGroups_Type()
)
iesMaxNumberOfMulticastGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumberOfMulticastGroups.setStatus("current")
_IesMulticastGroupTable_Object = MibTable
iesMulticastGroupTable = _IesMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 13, 2)
)
if mibBuilder.loadTexts:
    iesMulticastGroupTable.setStatus("current")
_IesMulticastGroupEntry_Object = MibTableRow
iesMulticastGroupEntry = _IesMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 13, 2, 1)
)
iesMulticastGroupEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesMulticastGroupMacAddr"),
)
if mibBuilder.loadTexts:
    iesMulticastGroupEntry.setStatus("current")
_IesMulticastGroupMacAddr_Type = PhysAddress
_IesMulticastGroupMacAddr_Object = MibTableColumn
iesMulticastGroupMacAddr = _IesMulticastGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 13, 2, 1, 1),
    _IesMulticastGroupMacAddr_Type()
)
iesMulticastGroupMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMulticastGroupMacAddr.setStatus("current")
_IesMulticastGroupPorts_Type = PortList
_IesMulticastGroupPorts_Object = MibTableColumn
iesMulticastGroupPorts = _IesMulticastGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 13, 2, 1, 2),
    _IesMulticastGroupPorts_Type()
)
iesMulticastGroupPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesMulticastGroupPorts.setStatus("current")
_IesMulticastGroupRowStatus_Type = RowStatus
_IesMulticastGroupRowStatus_Object = MibTableColumn
iesMulticastGroupRowStatus = _IesMulticastGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 13, 2, 1, 3),
    _IesMulticastGroupRowStatus_Type()
)
iesMulticastGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesMulticastGroupRowStatus.setStatus("current")
_IesSysIgmpFilter_ObjectIdentity = ObjectIdentity
iesSysIgmpFilter = _IesSysIgmpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14)
)
_IesMaxNumberOfIgmpFilters_Type = Integer32
_IesMaxNumberOfIgmpFilters_Object = MibScalar
iesMaxNumberOfIgmpFilters = _IesMaxNumberOfIgmpFilters_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 1),
    _IesMaxNumberOfIgmpFilters_Type()
)
iesMaxNumberOfIgmpFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumberOfIgmpFilters.setStatus("current")
_IesIgmpFilterTable_Object = MibTable
iesIgmpFilterTable = _IesIgmpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 2)
)
if mibBuilder.loadTexts:
    iesIgmpFilterTable.setStatus("current")
_IesIgmpFilterEntry_Object = MibTableRow
iesIgmpFilterEntry = _IesIgmpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 2, 1)
)
iesIgmpFilterEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesIgmpFilterName"),
    (0, "E5-111-IESCOMMON-MIB", "iesIgmpFilterIndex"),
)
if mibBuilder.loadTexts:
    iesIgmpFilterEntry.setStatus("current")


class _IesIgmpFilterName_Type(OctetString):
    """Custom type iesIgmpFilterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IesIgmpFilterName_Type.__name__ = "OctetString"
_IesIgmpFilterName_Object = MibTableColumn
iesIgmpFilterName = _IesIgmpFilterName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 2, 1, 1),
    _IesIgmpFilterName_Type()
)
iesIgmpFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIgmpFilterName.setStatus("current")
_IesIgmpFilterIndex_Type = Integer32
_IesIgmpFilterIndex_Object = MibTableColumn
iesIgmpFilterIndex = _IesIgmpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 2, 1, 2),
    _IesIgmpFilterIndex_Type()
)
iesIgmpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesIgmpFilterIndex.setStatus("current")
_IesIgmpFilterStartIp_Type = IpAddress
_IesIgmpFilterStartIp_Object = MibTableColumn
iesIgmpFilterStartIp = _IesIgmpFilterStartIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 2, 1, 3),
    _IesIgmpFilterStartIp_Type()
)
iesIgmpFilterStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIgmpFilterStartIp.setStatus("current")
_IesIgmpFilterEndIp_Type = IpAddress
_IesIgmpFilterEndIp_Object = MibTableColumn
iesIgmpFilterEndIp = _IesIgmpFilterEndIp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 2, 1, 4),
    _IesIgmpFilterEndIp_Type()
)
iesIgmpFilterEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIgmpFilterEndIp.setStatus("current")
_IesIgmpFilterRowStatus_Type = RowStatus
_IesIgmpFilterRowStatus_Object = MibTableColumn
iesIgmpFilterRowStatus = _IesIgmpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 2, 1, 5),
    _IesIgmpFilterRowStatus_Type()
)
iesIgmpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesIgmpFilterRowStatus.setStatus("current")
_IesIgmpFilterPortTable_Object = MibTable
iesIgmpFilterPortTable = _IesIgmpFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 3)
)
if mibBuilder.loadTexts:
    iesIgmpFilterPortTable.setStatus("current")
_IesIgmpFilterPortEntry_Object = MibTableRow
iesIgmpFilterPortEntry = _IesIgmpFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 3, 1)
)
iesIgmpFilterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    iesIgmpFilterPortEntry.setStatus("current")


class _IesIgmpFilterPortFilter_Type(OctetString):
    """Custom type iesIgmpFilterPortFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_IesIgmpFilterPortFilter_Type.__name__ = "OctetString"
_IesIgmpFilterPortFilter_Object = MibTableColumn
iesIgmpFilterPortFilter = _IesIgmpFilterPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 3, 14, 3, 1, 1),
    _IesIgmpFilterPortFilter_Type()
)
iesIgmpFilterPortFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesIgmpFilterPortFilter.setStatus("current")
_IesL2SW_ObjectIdentity = ObjectIdentity
iesL2SW = _IesL2SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4)
)


class _IesIGMPSnoopingEnabled_Type(Integer32):
    """Custom type iesIGMPSnoopingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IesIGMPSnoopingEnabled_Type.__name__ = "Integer32"
_IesIGMPSnoopingEnabled_Object = MibScalar
iesIGMPSnoopingEnabled = _IesIGMPSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 1),
    _IesIGMPSnoopingEnabled_Type()
)
iesIGMPSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesIGMPSnoopingEnabled.setStatus("current")
_IesManagementVLANId_Type = Integer32
_IesManagementVLANId_Object = MibScalar
iesManagementVLANId = _IesManagementVLANId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 2),
    _IesManagementVLANId_Type()
)
iesManagementVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesManagementVLANId.setStatus("current")
_IesMaxNumOfStaticVlans_Type = Integer32
_IesMaxNumOfStaticVlans_Object = MibScalar
iesMaxNumOfStaticVlans = _IesMaxNumOfStaticVlans_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 3),
    _IesMaxNumOfStaticVlans_Type()
)
iesMaxNumOfStaticVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumOfStaticVlans.setStatus("current")
_IesMaxNumOfTrunkGroups_Type = Integer32
_IesMaxNumOfTrunkGroups_Object = MibScalar
iesMaxNumOfTrunkGroups = _IesMaxNumOfTrunkGroups_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 4),
    _IesMaxNumOfTrunkGroups_Type()
)
iesMaxNumOfTrunkGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesMaxNumOfTrunkGroups.setStatus("current")
_IesTrunkGroupTable_Object = MibTable
iesTrunkGroupTable = _IesTrunkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 5)
)
if mibBuilder.loadTexts:
    iesTrunkGroupTable.setStatus("current")
_IesTrunkGroupEntry_Object = MibTableRow
iesTrunkGroupEntry = _IesTrunkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 5, 1)
)
iesTrunkGroupEntry.setIndexNames(
    (0, "E5-111-IESCOMMON-MIB", "iesTrunkGroupId"),
)
if mibBuilder.loadTexts:
    iesTrunkGroupEntry.setStatus("current")
_IesTrunkGroupId_Type = Integer32
_IesTrunkGroupId_Object = MibTableColumn
iesTrunkGroupId = _IesTrunkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 5, 1, 1),
    _IesTrunkGroupId_Type()
)
iesTrunkGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iesTrunkGroupId.setStatus("current")
_IesTrunkGroupName_Type = DisplayString
_IesTrunkGroupName_Object = MibTableColumn
iesTrunkGroupName = _IesTrunkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 5, 1, 2),
    _IesTrunkGroupName_Type()
)
iesTrunkGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesTrunkGroupName.setStatus("current")
_IesTrunkGroupPorts_Type = PortList
_IesTrunkGroupPorts_Object = MibTableColumn
iesTrunkGroupPorts = _IesTrunkGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 5, 1, 3),
    _IesTrunkGroupPorts_Type()
)
iesTrunkGroupPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesTrunkGroupPorts.setStatus("current")
_IesTrunkGroupRowStatus_Type = RowStatus
_IesTrunkGroupRowStatus_Object = MibTableColumn
iesTrunkGroupRowStatus = _IesTrunkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 5, 1, 4),
    _IesTrunkGroupRowStatus_Type()
)
iesTrunkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iesTrunkGroupRowStatus.setStatus("current")


class _IesPortIsolationEnable_Type(Integer32):
    """Custom type iesPortIsolationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IesPortIsolationEnable_Type.__name__ = "Integer32"
_IesPortIsolationEnable_Object = MibScalar
iesPortIsolationEnable = _IesPortIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 6),
    _IesPortIsolationEnable_Type()
)
iesPortIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesPortIsolationEnable.setStatus("current")


class _IesRSTPEnable_Type(Integer32):
    """Custom type iesRSTPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IesRSTPEnable_Type.__name__ = "Integer32"
_IesRSTPEnable_Object = MibScalar
iesRSTPEnable = _IesRSTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 7),
    _IesRSTPEnable_Type()
)
iesRSTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesRSTPEnable.setStatus("current")


class _IesSwitchMode_Type(Integer32):
    """Custom type iesSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daisyChain", 1),
          ("standalone", 2))
    )


_IesSwitchMode_Type.__name__ = "Integer32"
_IesSwitchMode_Object = MibScalar
iesSwitchMode = _IesSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 98, 4, 8),
    _IesSwitchMode_Type()
)
iesSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iesSwitchMode.setStatus("current")

# Managed Objects groups


# Notification objects

reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 1)
)
reboot.setObjects(
    ("E5-111-IESCOMMON-MIB", "iesProblemCause")
)
if mibBuilder.loadTexts:
    reboot.setStatus(
        ""
    )

systemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 2)
)
systemShutdown.setObjects(
    ("E5-111-IESCOMMON-MIB", "iesProblemCause")
)
if mibBuilder.loadTexts:
    systemShutdown.setStatus(
        ""
    )

overheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 3)
)
overheat.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"),
        ("E5-111-IESCOMMON-MIB", "iesSysTempIndex"),
        ("E5-111-IESCOMMON-MIB", "iesSysTempCurValue"))
)
if mibBuilder.loadTexts:
    overheat.setStatus(
        ""
    )

overheatOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 4)
)
overheatOver.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"),
        ("E5-111-IESCOMMON-MIB", "iesSysTempIndex"),
        ("E5-111-IESCOMMON-MIB", "iesSysTempCurValue"))
)
if mibBuilder.loadTexts:
    overheatOver.setStatus(
        ""
    )

errLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 5)
)
errLog.setObjects(
    ("E5-111-IESCOMMON-MIB", "iesProblemCause")
)
if mibBuilder.loadTexts:
    errLog.setStatus(
        ""
    )

fanRpmLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 6)
)
fanRpmLow.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesFanRpmIndex"),
        ("E5-111-IESCOMMON-MIB", "iesFanRpmCurValue"))
)
if mibBuilder.loadTexts:
    fanRpmLow.setStatus(
        ""
    )

fanRpmNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 7)
)
fanRpmNormal.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesFanRpmIndex"),
        ("E5-111-IESCOMMON-MIB", "iesFanRpmCurValue"))
)
if mibBuilder.loadTexts:
    fanRpmNormal.setStatus(
        ""
    )

voltageOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 8)
)
voltageOutOfRange.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"),
        ("E5-111-IESCOMMON-MIB", "iesVoltageIndex"),
        ("E5-111-IESCOMMON-MIB", "iesVoltageCurValue"))
)
if mibBuilder.loadTexts:
    voltageOutOfRange.setStatus(
        ""
    )

voltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 9)
)
voltageNormal.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"),
        ("E5-111-IESCOMMON-MIB", "iesVoltageIndex"),
        ("E5-111-IESCOMMON-MIB", "iesVoltageCurValue"))
)
if mibBuilder.loadTexts:
    voltageNormal.setStatus(
        ""
    )

systemMaintenanceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 10)
)
systemMaintenanceFailure.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"),
        ("E5-111-IESCOMMON-MIB", "iesProblemCause"))
)
if mibBuilder.loadTexts:
    systemMaintenanceFailure.setStatus(
        ""
    )

configChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 11)
)
configChange.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"),
        ("E5-111-IESCOMMON-MIB", "iesProblemCause"))
)
if mibBuilder.loadTexts:
    configChange.setStatus(
        ""
    )

moduleUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 12)
)
moduleUp.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"))
)
if mibBuilder.loadTexts:
    moduleUp.setStatus(
        ""
    )

moduleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 13)
)
moduleDown.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"))
)
if mibBuilder.loadTexts:
    moduleDown.setStatus(
        ""
    )

modulePlugIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 14)
)
modulePlugIn.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"))
)
if mibBuilder.loadTexts:
    modulePlugIn.setStatus(
        ""
    )

modulePullOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 15)
)
modulePullOut.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"))
)
if mibBuilder.loadTexts:
    modulePullOut.setStatus(
        ""
    )

powerDC48VAFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 16)
)
if mibBuilder.loadTexts:
    powerDC48VAFailure.setStatus(
        ""
    )

powerDC48VANormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 17)
)
if mibBuilder.loadTexts:
    powerDC48VANormal.setStatus(
        ""
    )

powerDC48VBFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 18)
)
if mibBuilder.loadTexts:
    powerDC48VBFailure.setStatus(
        ""
    )

powerDC48VBNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 19)
)
if mibBuilder.loadTexts:
    powerDC48VBNormal.setStatus(
        ""
    )

extAlarmInputTrigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 20)
)
if mibBuilder.loadTexts:
    extAlarmInputTrigger.setStatus(
        ""
    )

extAlarmInputRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 21)
)
if mibBuilder.loadTexts:
    extAlarmInputRelease.setStatus(
        ""
    )

thermalSensorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 22)
)
thermalSensorFailure.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"))
)
if mibBuilder.loadTexts:
    thermalSensorFailure.setStatus(
        ""
    )

mscSwitchOverOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 23)
)
mscSwitchOverOK.setObjects(
      *(("E5-111-IESCOMMON-MIB", "iesChassisId"),
        ("E5-111-IESCOMMON-MIB", "iesSlotId"))
)
if mibBuilder.loadTexts:
    mscSwitchOverOK.setStatus(
        ""
    )

networkTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 24)
)
if mibBuilder.loadTexts:
    networkTopologyChange.setStatus(
        ""
    )

adslAtucLof = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 25)
)
adslAtucLof.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAtucLof.setStatus(
        ""
    )

adslAturLof = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 26)
)
adslAturLof.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAturLof.setStatus(
        ""
    )

adslAtucLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 27)
)
adslAtucLos.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAtucLos.setStatus(
        ""
    )

adslAturLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 28)
)
adslAturLos.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAturLos.setStatus(
        ""
    )

adslAturLpr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 29)
)
adslAturLpr.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAturLpr.setStatus(
        ""
    )

adslAtucLofClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 30)
)
adslAtucLofClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAtucLofClear.setStatus(
        ""
    )

adslAturLofClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 31)
)
adslAturLofClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAturLofClear.setStatus(
        ""
    )

adslAtucLosClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 32)
)
adslAtucLosClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAtucLosClear.setStatus(
        ""
    )

adslAturLosClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 33)
)
adslAturLosClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAturLosClear.setStatus(
        ""
    )

adslAturLprClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 2, 0, 34)
)
adslAturLprClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adslAturLprClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E5-111-IESCOMMON-MIB",
    **{"reboot": reboot,
       "systemShutdown": systemShutdown,
       "overheat": overheat,
       "overheatOver": overheatOver,
       "errLog": errLog,
       "fanRpmLow": fanRpmLow,
       "fanRpmNormal": fanRpmNormal,
       "voltageOutOfRange": voltageOutOfRange,
       "voltageNormal": voltageNormal,
       "systemMaintenanceFailure": systemMaintenanceFailure,
       "configChange": configChange,
       "moduleUp": moduleUp,
       "moduleDown": moduleDown,
       "modulePlugIn": modulePlugIn,
       "modulePullOut": modulePullOut,
       "powerDC48VAFailure": powerDC48VAFailure,
       "powerDC48VANormal": powerDC48VANormal,
       "powerDC48VBFailure": powerDC48VBFailure,
       "powerDC48VBNormal": powerDC48VBNormal,
       "extAlarmInputTrigger": extAlarmInputTrigger,
       "extAlarmInputRelease": extAlarmInputRelease,
       "thermalSensorFailure": thermalSensorFailure,
       "mscSwitchOverOK": mscSwitchOverOK,
       "networkTopologyChange": networkTopologyChange,
       "adslAtucLof": adslAtucLof,
       "adslAturLof": adslAturLof,
       "adslAtucLos": adslAtucLos,
       "adslAturLos": adslAturLos,
       "adslAturLpr": adslAturLpr,
       "adslAtucLofClear": adslAtucLofClear,
       "adslAturLofClear": adslAturLofClear,
       "adslAtucLosClear": adslAtucLosClear,
       "adslAturLosClear": adslAturLosClear,
       "adslAturLprClear": adslAturLprClear,
       "iesChassis": iesChassis,
       "iesNumOfChassis": iesNumOfChassis,
       "iesChassisTable": iesChassisTable,
       "iesChassisEntry": iesChassisEntry,
       "iesChassisId": iesChassisId,
       "iesChassisFrameNumber": iesChassisFrameNumber,
       "iesChassisSerialNumber": iesChassisSerialNumber,
       "iesChassisNumber": iesChassisNumber,
       "iesChassisStatus": iesChassisStatus,
       "iesChassisProductPartNumber": iesChassisProductPartNumber,
       "iesChassisHwRevisionNumber": iesChassisHwRevisionNumber,
       "iesChassisCleiCode": iesChassisCleiCode,
       "iesChassisHwVersion": iesChassisHwVersion,
       "iesChassisMacAddress": iesChassisMacAddress,
       "iesChassisVoipDspVersion": iesChassisVoipDspVersion,
       "iesChassisCodecVersion": iesChassisCodecVersion,
       "iesSlotTable": iesSlotTable,
       "iesSlotEntry": iesSlotEntry,
       "iesSlotId": iesSlotId,
       "iesSlotModuleType": iesSlotModuleType,
       "iesSlotModuleDescr": iesSlotModuleDescr,
       "iesSlotModuleFWVersion": iesSlotModuleFWVersion,
       "iesSlotModuleDriverVersion": iesSlotModuleDriverVersion,
       "iesSlotModuleModemCodeVersion": iesSlotModuleModemCodeVersion,
       "iesSlotModuleStatus": iesSlotModuleStatus,
       "iesSlotModuleAlarmStatus": iesSlotModuleAlarmStatus,
       "iesMscPortConfTable": iesMscPortConfTable,
       "iesMscPortConfEntry": iesMscPortConfEntry,
       "iesMscPortId": iesMscPortId,
       "iesMscPortType": iesMscPortType,
       "iesMscPortIfIndex": iesMscPortIfIndex,
       "iesMscPortSpeed": iesMscPortSpeed,
       "iesMscPortDuplex": iesMscPortDuplex,
       "iesMscPortFlowControl": iesMscPortFlowControl,
       "iesMscPortDefaultVLANTagging": iesMscPortDefaultVLANTagging,
       "iesMscPortTrunkGroupId": iesMscPortTrunkGroupId,
       "iesMscPortMode": iesMscPortMode,
       "iesMscPortVLANTrunking": iesMscPortVLANTrunking,
       "iesHWMonitor": iesHWMonitor,
       "iesFanRpmTable": iesFanRpmTable,
       "iesFanRpmEntry": iesFanRpmEntry,
       "iesFanRpmIndex": iesFanRpmIndex,
       "iesFanRpmCurValue": iesFanRpmCurValue,
       "iesFanRpmMaxValue": iesFanRpmMaxValue,
       "iesFanRpmMinValue": iesFanRpmMinValue,
       "iesFanRpmLowThresh": iesFanRpmLowThresh,
       "iesFanRpmDescr": iesFanRpmDescr,
       "iesVoltageTable": iesVoltageTable,
       "iesVoltageEntry": iesVoltageEntry,
       "iesVoltageIndex": iesVoltageIndex,
       "iesVoltageCurValue": iesVoltageCurValue,
       "iesVoltageMaxValue": iesVoltageMaxValue,
       "iesVoltageMinValue": iesVoltageMinValue,
       "iesVoltageNominalValue": iesVoltageNominalValue,
       "iesVoltageLowThresh": iesVoltageLowThresh,
       "iesVoltageDescr": iesVoltageDescr,
       "iesSysTempTable": iesSysTempTable,
       "iesSysTempEntry": iesSysTempEntry,
       "iesSysTempIndex": iesSysTempIndex,
       "iesSysTempCurValue": iesSysTempCurValue,
       "iesSysTempMaxValue": iesSysTempMaxValue,
       "iesSysTempMinValue": iesSysTempMinValue,
       "iesSysTempHighThresh": iesSysTempHighThresh,
       "iesSysTempDescr": iesSysTempDescr,
       "iesSysMgnt": iesSysMgnt,
       "iesSysState": iesSysState,
       "iesSystemCurrentStatus": iesSystemCurrentStatus,
       "iesProblemCause": iesProblemCause,
       "iesSysMaintenance": iesSysMaintenance,
       "iesMaintenanceOps": iesMaintenanceOps,
       "iesMaintenanceTarget": iesMaintenanceTarget,
       "iesMaintenanceDSLConfOps": iesMaintenanceDSLConfOps,
       "iesMaintenanceDSLConfTarget": iesMaintenanceDSLConfTarget,
       "iesMaintenanceDSLConfProfileName": iesMaintenanceDSLConfProfileName,
       "iesMaintenanceDSLConfMode": iesMaintenanceDSLConfMode,
       "iesMaintenanceDSLConfPktFilter": iesMaintenanceDSLConfPktFilter,
       "iesMaintenanceDSLConfDot1xControl": iesMaintenanceDSLConfDot1xControl,
       "iesMaintenanceDSLConfDot1xReauthPeriod": iesMaintenanceDSLConfDot1xReauthPeriod,
       "iesMaintenanceDSLConfMacCount": iesMaintenanceDSLConfMacCount,
       "iesMaintenanceVpi": iesMaintenanceVpi,
       "iesMaintenanceVci": iesMaintenanceVci,
       "iesMaintenanceDSLConfAlarmProfileName": iesMaintenanceDSLConfAlarmProfileName,
       "iesMaintenanceDSLConfAnnexL": iesMaintenanceDSLConfAnnexL,
       "iesMaintenanceDSLConfPmMode": iesMaintenanceDSLConfPmMode,
       "iesMaintenanceDSLConfRateMode": iesMaintenanceDSLConfRateMode,
       "iesMaintenanceDSLConfIgmpFilter": iesMaintenanceDSLConfIgmpFilter,
       "iesSysTimeSetup": iesSysTimeSetup,
       "iesTimeServerMode": iesTimeServerMode,
       "iesTimeServerIP": iesTimeServerIP,
       "iesSystemTime": iesSystemTime,
       "iesSystemDate": iesSystemDate,
       "iesSystemTimeZone": iesSystemTimeZone,
       "iesSysAccessControl": iesSysAccessControl,
       "iesAccessCtrlTable": iesAccessCtrlTable,
       "iesAccessCtrlEntry": iesAccessCtrlEntry,
       "iesAccessCtrlService": iesAccessCtrlService,
       "iesAccessCtrlEnable": iesAccessCtrlEnable,
       "iesAccessCtrlPort": iesAccessCtrlPort,
       "iesMaxNumOfSecuredClients": iesMaxNumOfSecuredClients,
       "iesSecuredClientTable": iesSecuredClientTable,
       "iesSecuredClientEntry": iesSecuredClientEntry,
       "iesSecuredClientStartIp": iesSecuredClientStartIp,
       "iesSecuredClientEndIp": iesSecuredClientEndIp,
       "iesSecuredClientService": iesSecuredClientService,
       "iesSecuredClientRowStatus": iesSecuredClientRowStatus,
       "iesSysStaticRoute": iesSysStaticRoute,
       "iesMaxNumOfStaticRoutes": iesMaxNumOfStaticRoutes,
       "iesStaticRouteTable": iesStaticRouteTable,
       "iesStaticRouteEntry": iesStaticRouteEntry,
       "iesStaticRouteName": iesStaticRouteName,
       "iesStaticRouteDest": iesStaticRouteDest,
       "iesStaticRouteMask": iesStaticRouteMask,
       "iesStaticRouteGateway": iesStaticRouteGateway,
       "iesStaticRouteMetric": iesStaticRouteMetric,
       "iesStaticRouteRowStatus": iesStaticRouteRowStatus,
       "iesSyslogSetup": iesSyslogSetup,
       "iesSysLogEnable": iesSysLogEnable,
       "iesSysLogServer": iesSysLogServer,
       "iesSysLogFacility": iesSysLogFacility,
       "iesSysDhcpSetup": iesSysDhcpSetup,
       "iesDhcpRelayEnable": iesDhcpRelayEnable,
       "iesDhcpRelayOption82Enable": iesDhcpRelayOption82Enable,
       "iesDhcpRelayOption82Info": iesDhcpRelayOption82Info,
       "iesMaxNumOfDhcpServers": iesMaxNumOfDhcpServers,
       "iesDhcpServerTable": iesDhcpServerTable,
       "iesDhcpServerEntry": iesDhcpServerEntry,
       "iesDhcpServerIp": iesDhcpServerIp,
       "iesDhcpServerRowStatus": iesDhcpServerRowStatus,
       "iesSysSNMPSetup": iesSysSNMPSetup,
       "iesMaxNumberOfTrapDestinations": iesMaxNumberOfTrapDestinations,
       "iesSNMPTrapDestTable": iesSNMPTrapDestTable,
       "iesSNMPTrapDestEntry": iesSNMPTrapDestEntry,
       "iesTrapDestIp": iesTrapDestIp,
       "iesTrapDestPort": iesTrapDestPort,
       "iesTrapDestRowStatus": iesTrapDestRowStatus,
       "iesSnmpGetCommunity": iesSnmpGetCommunity,
       "iesSnmpSetCommunity": iesSnmpSetCommunity,
       "iesSnmpTrapCommunity": iesSnmpTrapCommunity,
       "iesSysDot1xSetup": iesSysDot1xSetup,
       "iesMaxNumberOfRadiusServers": iesMaxNumberOfRadiusServers,
       "iesRadiusServerTable": iesRadiusServerTable,
       "iesRadiusServerEntry": iesRadiusServerEntry,
       "iesRadiusServerIndex": iesRadiusServerIndex,
       "iesRadiusServerIp": iesRadiusServerIp,
       "iesRadiusServerPort": iesRadiusServerPort,
       "iesRadiusSharedSecret": iesRadiusSharedSecret,
       "iesRadiusServerRowStatus": iesRadiusServerRowStatus,
       "iesDot1xEnable": iesDot1xEnable,
       "iesDot1xPortTable": iesDot1xPortTable,
       "iesDot1xPortEntry": iesDot1xPortEntry,
       "iesDot1xPortEnable": iesDot1xPortEnable,
       "iesDot1xPortControl": iesDot1xPortControl,
       "iesDot1xPortReAuthEnable": iesDot1xPortReAuthEnable,
       "iesDot1xPortReAuthPeriod": iesDot1xPortReAuthPeriod,
       "iesSysMacFilter": iesSysMacFilter,
       "iesMacFilterStatusTable": iesMacFilterStatusTable,
       "iesMacFilterStatusEntry": iesMacFilterStatusEntry,
       "iesMacFilterStatusEnable": iesMacFilterStatusEnable,
       "iesMaxNumberOfMacFilters": iesMaxNumberOfMacFilters,
       "iesMaxNumberOfMacFiltersPerPort": iesMaxNumberOfMacFiltersPerPort,
       "iesCurrNumberOfMacFilters": iesCurrNumberOfMacFilters,
       "iesMacFilterTable": iesMacFilterTable,
       "iesMacFilterEntry": iesMacFilterEntry,
       "iesMacFilterMacAddr": iesMacFilterMacAddr,
       "iesMacFilterRowStatus": iesMacFilterRowStatus,
       "iesSysPacketFilter": iesSysPacketFilter,
       "iesPacketFilterTable": iesPacketFilterTable,
       "iesPacketFilterEntry": iesPacketFilterEntry,
       "iesPacketFilter": iesPacketFilter,
       "iesSysMacCountFilter": iesSysMacCountFilter,
       "iesMacCountFilterTable": iesMacCountFilterTable,
       "iesMacCountFilterEntry": iesMacCountFilterEntry,
       "iesMacCountFilterStatus": iesMacCountFilterStatus,
       "iesMacCountFilterCount": iesMacCountFilterCount,
       "iesSysMulticastGroup": iesSysMulticastGroup,
       "iesMaxNumberOfMulticastGroups": iesMaxNumberOfMulticastGroups,
       "iesMulticastGroupTable": iesMulticastGroupTable,
       "iesMulticastGroupEntry": iesMulticastGroupEntry,
       "iesMulticastGroupMacAddr": iesMulticastGroupMacAddr,
       "iesMulticastGroupPorts": iesMulticastGroupPorts,
       "iesMulticastGroupRowStatus": iesMulticastGroupRowStatus,
       "iesSysIgmpFilter": iesSysIgmpFilter,
       "iesMaxNumberOfIgmpFilters": iesMaxNumberOfIgmpFilters,
       "iesIgmpFilterTable": iesIgmpFilterTable,
       "iesIgmpFilterEntry": iesIgmpFilterEntry,
       "iesIgmpFilterName": iesIgmpFilterName,
       "iesIgmpFilterIndex": iesIgmpFilterIndex,
       "iesIgmpFilterStartIp": iesIgmpFilterStartIp,
       "iesIgmpFilterEndIp": iesIgmpFilterEndIp,
       "iesIgmpFilterRowStatus": iesIgmpFilterRowStatus,
       "iesIgmpFilterPortTable": iesIgmpFilterPortTable,
       "iesIgmpFilterPortEntry": iesIgmpFilterPortEntry,
       "iesIgmpFilterPortFilter": iesIgmpFilterPortFilter,
       "iesL2SW": iesL2SW,
       "iesIGMPSnoopingEnabled": iesIGMPSnoopingEnabled,
       "iesManagementVLANId": iesManagementVLANId,
       "iesMaxNumOfStaticVlans": iesMaxNumOfStaticVlans,
       "iesMaxNumOfTrunkGroups": iesMaxNumOfTrunkGroups,
       "iesTrunkGroupTable": iesTrunkGroupTable,
       "iesTrunkGroupEntry": iesTrunkGroupEntry,
       "iesTrunkGroupId": iesTrunkGroupId,
       "iesTrunkGroupName": iesTrunkGroupName,
       "iesTrunkGroupPorts": iesTrunkGroupPorts,
       "iesTrunkGroupRowStatus": iesTrunkGroupRowStatus,
       "iesPortIsolationEnable": iesPortIsolationEnable,
       "iesRSTPEnable": iesRSTPEnable,
       "iesSwitchMode": iesSwitchMode}
)
