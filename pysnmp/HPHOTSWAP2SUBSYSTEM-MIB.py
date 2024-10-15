# SNMP MIB module (HPHOTSWAP2SUBSYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPHOTSWAP2SUBSYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:15 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaHotswap2_ObjectIdentity = ObjectIdentity
hpnsaHotswap2 = _HpnsaHotswap2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27)
)
_HpnsaHS2MibRev_ObjectIdentity = ObjectIdentity
hpnsaHS2MibRev = _HpnsaHS2MibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 1)
)
_HpnsaHS2MibRevMajor_Type = Integer32
_HpnsaHS2MibRevMajor_Object = MibScalar
hpnsaHS2MibRevMajor = _HpnsaHS2MibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 1, 1),
    _HpnsaHS2MibRevMajor_Type()
)
hpnsaHS2MibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2MibRevMajor.setStatus("mandatory")
_HpnsaHS2MibRevMinor_Type = Integer32
_HpnsaHS2MibRevMinor_Object = MibScalar
hpnsaHS2MibRevMinor = _HpnsaHS2MibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 1, 2),
    _HpnsaHS2MibRevMinor_Type()
)
hpnsaHS2MibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2MibRevMinor.setStatus("mandatory")
_HpnsaHS2Cage_ObjectIdentity = ObjectIdentity
hpnsaHS2Cage = _HpnsaHS2Cage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2)
)
_HpnsaHS2CageTable_Object = MibTable
hpnsaHS2CageTable = _HpnsaHS2CageTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaHS2CageTable.setStatus("mandatory")
_HpnsaHS2CageEntry_Object = MibTableRow
hpnsaHS2CageEntry = _HpnsaHS2CageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1)
)
hpnsaHS2CageEntry.setIndexNames(
    (0, "HPHOTSWAP2SUBSYSTEM-MIB", "hpnsaHS2CageIndex"),
)
if mibBuilder.loadTexts:
    hpnsaHS2CageEntry.setStatus("mandatory")
_HpnsaHS2CageIndex_Type = Integer32
_HpnsaHS2CageIndex_Object = MibTableColumn
hpnsaHS2CageIndex = _HpnsaHS2CageIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 1),
    _HpnsaHS2CageIndex_Type()
)
hpnsaHS2CageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageIndex.setStatus("mandatory")


class _HpnsaHS2Cage12VPower_Type(Integer32):
    """Custom type hpnsaHS2Cage12VPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )


_HpnsaHS2Cage12VPower_Type.__name__ = "Integer32"
_HpnsaHS2Cage12VPower_Object = MibTableColumn
hpnsaHS2Cage12VPower = _HpnsaHS2Cage12VPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 2),
    _HpnsaHS2Cage12VPower_Type()
)
hpnsaHS2Cage12VPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2Cage12VPower.setStatus("mandatory")


class _HpnsaHS2CageTerminator1_Type(Integer32):
    """Custom type hpnsaHS2CageTerminator1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 2),
          ("not-attached", 1))
    )


_HpnsaHS2CageTerminator1_Type.__name__ = "Integer32"
_HpnsaHS2CageTerminator1_Object = MibTableColumn
hpnsaHS2CageTerminator1 = _HpnsaHS2CageTerminator1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 3),
    _HpnsaHS2CageTerminator1_Type()
)
hpnsaHS2CageTerminator1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageTerminator1.setStatus("mandatory")


class _HpnsaHS2CageTerminator2_Type(Integer32):
    """Custom type hpnsaHS2CageTerminator2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 2),
          ("not-attached", 1))
    )


_HpnsaHS2CageTerminator2_Type.__name__ = "Integer32"
_HpnsaHS2CageTerminator2_Object = MibTableColumn
hpnsaHS2CageTerminator2 = _HpnsaHS2CageTerminator2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 4),
    _HpnsaHS2CageTerminator2_Type()
)
hpnsaHS2CageTerminator2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageTerminator2.setStatus("mandatory")


class _HpnsaHS2CageSCSICable1_Type(Integer32):
    """Custom type hpnsaHS2CageSCSICable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 2),
          ("not-attached", 1))
    )


_HpnsaHS2CageSCSICable1_Type.__name__ = "Integer32"
_HpnsaHS2CageSCSICable1_Object = MibTableColumn
hpnsaHS2CageSCSICable1 = _HpnsaHS2CageSCSICable1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 5),
    _HpnsaHS2CageSCSICable1_Type()
)
hpnsaHS2CageSCSICable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageSCSICable1.setStatus("mandatory")


class _HpnsaHS2CageSCSICable2_Type(Integer32):
    """Custom type hpnsaHS2CageSCSICable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 2),
          ("not-attached", 1))
    )


_HpnsaHS2CageSCSICable2_Type.__name__ = "Integer32"
_HpnsaHS2CageSCSICable2_Object = MibTableColumn
hpnsaHS2CageSCSICable2 = _HpnsaHS2CageSCSICable2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 6),
    _HpnsaHS2CageSCSICable2_Type()
)
hpnsaHS2CageSCSICable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageSCSICable2.setStatus("mandatory")
_HpnsaHS2CageBaseSCSIAddress_Type = Integer32
_HpnsaHS2CageBaseSCSIAddress_Object = MibTableColumn
hpnsaHS2CageBaseSCSIAddress = _HpnsaHS2CageBaseSCSIAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 7),
    _HpnsaHS2CageBaseSCSIAddress_Type()
)
hpnsaHS2CageBaseSCSIAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaHS2CageBaseSCSIAddress.setStatus("mandatory")
_HpnsaHS2CageTemperature_Type = Integer32
_HpnsaHS2CageTemperature_Object = MibTableColumn
hpnsaHS2CageTemperature = _HpnsaHS2CageTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 8),
    _HpnsaHS2CageTemperature_Type()
)
hpnsaHS2CageTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageTemperature.setStatus("mandatory")
_HpnsaHS2CageTemperatureWarningThreshold_Type = Integer32
_HpnsaHS2CageTemperatureWarningThreshold_Object = MibTableColumn
hpnsaHS2CageTemperatureWarningThreshold = _HpnsaHS2CageTemperatureWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 9),
    _HpnsaHS2CageTemperatureWarningThreshold_Type()
)
hpnsaHS2CageTemperatureWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaHS2CageTemperatureWarningThreshold.setStatus("mandatory")
_HpnsaHS2CageTemperatureAlertThreshold_Type = Integer32
_HpnsaHS2CageTemperatureAlertThreshold_Object = MibTableColumn
hpnsaHS2CageTemperatureAlertThreshold = _HpnsaHS2CageTemperatureAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 10),
    _HpnsaHS2CageTemperatureAlertThreshold_Type()
)
hpnsaHS2CageTemperatureAlertThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaHS2CageTemperatureAlertThreshold.setStatus("mandatory")


class _HpnsaHS2CageManagementBoardFRU_Type(OctetString):
    """Custom type hpnsaHS2CageManagementBoardFRU based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaHS2CageManagementBoardFRU_Type.__name__ = "OctetString"
_HpnsaHS2CageManagementBoardFRU_Object = MibTableColumn
hpnsaHS2CageManagementBoardFRU = _HpnsaHS2CageManagementBoardFRU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 11),
    _HpnsaHS2CageManagementBoardFRU_Type()
)
hpnsaHS2CageManagementBoardFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageManagementBoardFRU.setStatus("mandatory")


class _HpnsaHS2CageInterconnectFRU_Type(OctetString):
    """Custom type hpnsaHS2CageInterconnectFRU based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaHS2CageInterconnectFRU_Type.__name__ = "OctetString"
_HpnsaHS2CageInterconnectFRU_Object = MibTableColumn
hpnsaHS2CageInterconnectFRU = _HpnsaHS2CageInterconnectFRU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 12),
    _HpnsaHS2CageInterconnectFRU_Type()
)
hpnsaHS2CageInterconnectFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageInterconnectFRU.setStatus("mandatory")
_HpnsaHS2CageFirmwareMajorRev_Type = Integer32
_HpnsaHS2CageFirmwareMajorRev_Object = MibTableColumn
hpnsaHS2CageFirmwareMajorRev = _HpnsaHS2CageFirmwareMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 13),
    _HpnsaHS2CageFirmwareMajorRev_Type()
)
hpnsaHS2CageFirmwareMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageFirmwareMajorRev.setStatus("mandatory")
_HpnsaHS2CageFirmwareMinorRev_Type = Integer32
_HpnsaHS2CageFirmwareMinorRev_Object = MibTableColumn
hpnsaHS2CageFirmwareMinorRev = _HpnsaHS2CageFirmwareMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 2, 1, 1, 14),
    _HpnsaHS2CageFirmwareMinorRev_Type()
)
hpnsaHS2CageFirmwareMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2CageFirmwareMinorRev.setStatus("mandatory")
_HpnsaHS2Slot_ObjectIdentity = ObjectIdentity
hpnsaHS2Slot = _HpnsaHS2Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3)
)
_HpnsaHS2SlotTable_Object = MibTable
hpnsaHS2SlotTable = _HpnsaHS2SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1)
)
if mibBuilder.loadTexts:
    hpnsaHS2SlotTable.setStatus("mandatory")
_HpnsaHS2SlotEntry_Object = MibTableRow
hpnsaHS2SlotEntry = _HpnsaHS2SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1)
)
hpnsaHS2SlotEntry.setIndexNames(
    (0, "HPHOTSWAP2SUBSYSTEM-MIB", "hpnsaHS2SlotCageIndex"),
    (0, "HPHOTSWAP2SUBSYSTEM-MIB", "hpnsaHS2SlotIndex"),
)
if mibBuilder.loadTexts:
    hpnsaHS2SlotEntry.setStatus("mandatory")
_HpnsaHS2SlotCageIndex_Type = Integer32
_HpnsaHS2SlotCageIndex_Object = MibTableColumn
hpnsaHS2SlotCageIndex = _HpnsaHS2SlotCageIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 1),
    _HpnsaHS2SlotCageIndex_Type()
)
hpnsaHS2SlotCageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2SlotCageIndex.setStatus("mandatory")
_HpnsaHS2SlotIndex_Type = Integer32
_HpnsaHS2SlotIndex_Object = MibTableColumn
hpnsaHS2SlotIndex = _HpnsaHS2SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 2),
    _HpnsaHS2SlotIndex_Type()
)
hpnsaHS2SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2SlotIndex.setStatus("mandatory")


class _HpnsaHS2DrivePresent_Type(Integer32):
    """Custom type hpnsaHS2DrivePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 1),
          ("present", 2))
    )


_HpnsaHS2DrivePresent_Type.__name__ = "Integer32"
_HpnsaHS2DrivePresent_Object = MibTableColumn
hpnsaHS2DrivePresent = _HpnsaHS2DrivePresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 3),
    _HpnsaHS2DrivePresent_Type()
)
hpnsaHS2DrivePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2DrivePresent.setStatus("mandatory")


class _HpnsaHS2DriveSCSIBusType_Type(Integer32):
    """Custom type hpnsaHS2DriveSCSIBusType based on Integer32"""
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
        *(("hvd", 3),
          ("lvd", 2),
          ("none", 4),
          ("se", 1))
    )


_HpnsaHS2DriveSCSIBusType_Type.__name__ = "Integer32"
_HpnsaHS2DriveSCSIBusType_Object = MibTableColumn
hpnsaHS2DriveSCSIBusType = _HpnsaHS2DriveSCSIBusType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 4),
    _HpnsaHS2DriveSCSIBusType_Type()
)
hpnsaHS2DriveSCSIBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHS2DriveSCSIBusType.setStatus("mandatory")
_HpnsaHS2DriveIdentify_Type = Integer32
_HpnsaHS2DriveIdentify_Object = MibTableColumn
hpnsaHS2DriveIdentify = _HpnsaHS2DriveIdentify_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 27, 3, 1, 1, 5),
    _HpnsaHS2DriveIdentify_Type()
)
hpnsaHS2DriveIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaHS2DriveIdentify.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPHOTSWAP2SUBSYSTEM-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaHotswap2": hpnsaHotswap2,
       "hpnsaHS2MibRev": hpnsaHS2MibRev,
       "hpnsaHS2MibRevMajor": hpnsaHS2MibRevMajor,
       "hpnsaHS2MibRevMinor": hpnsaHS2MibRevMinor,
       "hpnsaHS2Cage": hpnsaHS2Cage,
       "hpnsaHS2CageTable": hpnsaHS2CageTable,
       "hpnsaHS2CageEntry": hpnsaHS2CageEntry,
       "hpnsaHS2CageIndex": hpnsaHS2CageIndex,
       "hpnsaHS2Cage12VPower": hpnsaHS2Cage12VPower,
       "hpnsaHS2CageTerminator1": hpnsaHS2CageTerminator1,
       "hpnsaHS2CageTerminator2": hpnsaHS2CageTerminator2,
       "hpnsaHS2CageSCSICable1": hpnsaHS2CageSCSICable1,
       "hpnsaHS2CageSCSICable2": hpnsaHS2CageSCSICable2,
       "hpnsaHS2CageBaseSCSIAddress": hpnsaHS2CageBaseSCSIAddress,
       "hpnsaHS2CageTemperature": hpnsaHS2CageTemperature,
       "hpnsaHS2CageTemperatureWarningThreshold": hpnsaHS2CageTemperatureWarningThreshold,
       "hpnsaHS2CageTemperatureAlertThreshold": hpnsaHS2CageTemperatureAlertThreshold,
       "hpnsaHS2CageManagementBoardFRU": hpnsaHS2CageManagementBoardFRU,
       "hpnsaHS2CageInterconnectFRU": hpnsaHS2CageInterconnectFRU,
       "hpnsaHS2CageFirmwareMajorRev": hpnsaHS2CageFirmwareMajorRev,
       "hpnsaHS2CageFirmwareMinorRev": hpnsaHS2CageFirmwareMinorRev,
       "hpnsaHS2Slot": hpnsaHS2Slot,
       "hpnsaHS2SlotTable": hpnsaHS2SlotTable,
       "hpnsaHS2SlotEntry": hpnsaHS2SlotEntry,
       "hpnsaHS2SlotCageIndex": hpnsaHS2SlotCageIndex,
       "hpnsaHS2SlotIndex": hpnsaHS2SlotIndex,
       "hpnsaHS2DrivePresent": hpnsaHS2DrivePresent,
       "hpnsaHS2DriveSCSIBusType": hpnsaHS2DriveSCSIBusType,
       "hpnsaHS2DriveIdentify": hpnsaHS2DriveIdentify}
)
