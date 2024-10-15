# SNMP MIB module (ACOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:37 2024
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



class AcosDeviceTypeEnum(Integer32):
    """Custom type AcosDeviceTypeEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              17,
              18,
              24,
              65534,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("atm25", 4),
          ("copperGold-CO", 17),
          ("copperGold-RT", 18),
          ("dualDS1-Bt8370", 8),
          ("ethernet", 1),
          ("mpeg2", 11),
          ("noDevice", 65534),
          ("octalPOTS", 14),
          ("quadPotsD1", 12),
          ("quadPotsD2", 13),
          ("sdsl-CO", 9),
          ("sdsl-Remote", 10),
          ("sdsl-Rev1", 24),
          ("singleDS1-Bt8370", 7),
          ("singleUSI", 2),
          ("unknown", 65535))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtlasComEngines_ObjectIdentity = ObjectIdentity
atlasComEngines = _AtlasComEngines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221)
)
_AceProductFamily_ObjectIdentity = ObjectIdentity
aceProductFamily = _AceProductFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1)
)
_AceAcos_ObjectIdentity = ObjectIdentity
aceAcos = _AceAcos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1)
)
_AcosSystem_ObjectIdentity = ObjectIdentity
acosSystem = _AcosSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1)
)


class _AcosSystemReboot_Type(Integer32):
    """Custom type acosSystemReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("rebootSystem", 2))
    )


_AcosSystemReboot_Type.__name__ = "Integer32"
_AcosSystemReboot_Object = MibScalar
acosSystemReboot = _AcosSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 1),
    _AcosSystemReboot_Type()
)
acosSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosSystemReboot.setStatus("mandatory")


class _AcosHardwareRevision_Type(DisplayString):
    """Custom type acosHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcosHardwareRevision_Type.__name__ = "DisplayString"
_AcosHardwareRevision_Object = MibScalar
acosHardwareRevision = _AcosHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 2),
    _AcosHardwareRevision_Type()
)
acosHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosHardwareRevision.setStatus("mandatory")


class _AcosSoftwareRevision_Type(DisplayString):
    """Custom type acosSoftwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcosSoftwareRevision_Type.__name__ = "DisplayString"
_AcosSoftwareRevision_Object = MibScalar
acosSoftwareRevision = _AcosSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 3),
    _AcosSoftwareRevision_Type()
)
acosSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosSoftwareRevision.setStatus("mandatory")


class _AcosSerialNumber_Type(DisplayString):
    """Custom type acosSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcosSerialNumber_Type.__name__ = "DisplayString"
_AcosSerialNumber_Object = MibScalar
acosSerialNumber = _AcosSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 4),
    _AcosSerialNumber_Type()
)
acosSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosSerialNumber.setStatus("mandatory")


class _AcosPartNumber_Type(DisplayString):
    """Custom type acosPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcosPartNumber_Type.__name__ = "DisplayString"
_AcosPartNumber_Object = MibScalar
acosPartNumber = _AcosPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 5),
    _AcosPartNumber_Type()
)
acosPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosPartNumber.setStatus("mandatory")
_AcosTotalSlots_Type = Integer32
_AcosTotalSlots_Object = MibScalar
acosTotalSlots = _AcosTotalSlots_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 6),
    _AcosTotalSlots_Type()
)
acosTotalSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosTotalSlots.setStatus("mandatory")
_AcosMemoryCapacityTable_Object = MibTable
acosMemoryCapacityTable = _AcosMemoryCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    acosMemoryCapacityTable.setStatus("mandatory")
_AcosMemoryCapacityEntry_Object = MibTableRow
acosMemoryCapacityEntry = _AcosMemoryCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 7, 1)
)
acosMemoryCapacityEntry.setIndexNames(
    (0, "ACOS-MIB", "acosMemoryTypeIndex"),
)
if mibBuilder.loadTexts:
    acosMemoryCapacityEntry.setStatus("mandatory")


class _AcosMemoryTypeIndex_Type(Integer32):
    """Custom type acosMemoryTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootFlashRom", 2),
          ("nandFlashRom", 3),
          ("sdram", 1))
    )


_AcosMemoryTypeIndex_Type.__name__ = "Integer32"
_AcosMemoryTypeIndex_Object = MibTableColumn
acosMemoryTypeIndex = _AcosMemoryTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 7, 1, 1),
    _AcosMemoryTypeIndex_Type()
)
acosMemoryTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosMemoryTypeIndex.setStatus("mandatory")
_AcosMemoryCapacity_Type = Integer32
_AcosMemoryCapacity_Object = MibTableColumn
acosMemoryCapacity = _AcosMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 7, 1, 2),
    _AcosMemoryCapacity_Type()
)
acosMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosMemoryCapacity.setStatus("mandatory")
_AcosDSPCount_Type = Integer32
_AcosDSPCount_Object = MibScalar
acosDSPCount = _AcosDSPCount_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 1, 8),
    _AcosDSPCount_Type()
)
acosDSPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDSPCount.setStatus("mandatory")
_AcosDevices_ObjectIdentity = ObjectIdentity
acosDevices = _AcosDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 2)
)
_AcosDeviceTable_Object = MibTable
acosDeviceTable = _AcosDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acosDeviceTable.setStatus("mandatory")
_AcosDeviceEntry_Object = MibTableRow
acosDeviceEntry = _AcosDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 2, 1, 1)
)
acosDeviceEntry.setIndexNames(
    (0, "ACOS-MIB", "acosDeviceSlotIndex"),
)
if mibBuilder.loadTexts:
    acosDeviceEntry.setStatus("mandatory")
_AcosDeviceSlotIndex_Type = Integer32
_AcosDeviceSlotIndex_Object = MibTableColumn
acosDeviceSlotIndex = _AcosDeviceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 2, 1, 1, 1),
    _AcosDeviceSlotIndex_Type()
)
acosDeviceSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceSlotIndex.setStatus("mandatory")
_AcosDeviceType_Type = AcosDeviceTypeEnum
_AcosDeviceType_Object = MibTableColumn
acosDeviceType = _AcosDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 2, 1, 1, 2),
    _AcosDeviceType_Type()
)
acosDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceType.setStatus("mandatory")
_AcosDeviceTotal_Type = Integer32
_AcosDeviceTotal_Object = MibTableColumn
acosDeviceTotal = _AcosDeviceTotal_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 2, 1, 1, 3),
    _AcosDeviceTotal_Type()
)
acosDeviceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceTotal.setStatus("mandatory")


class _AcosDeviceDescription_Type(DisplayString):
    """Custom type acosDeviceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcosDeviceDescription_Type.__name__ = "DisplayString"
_AcosDeviceDescription_Object = MibTableColumn
acosDeviceDescription = _AcosDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 2, 1, 1, 4),
    _AcosDeviceDescription_Type()
)
acosDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceDescription.setStatus("mandatory")
_AcosDeviceTypesAggregate_Type = OctetString
_AcosDeviceTypesAggregate_Object = MibScalar
acosDeviceTypesAggregate = _AcosDeviceTypesAggregate_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 2, 2),
    _AcosDeviceTypesAggregate_Type()
)
acosDeviceTypesAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceTypesAggregate.setStatus("mandatory")
_AcosDeviceTotalsAggregate_Type = OctetString
_AcosDeviceTotalsAggregate_Object = MibScalar
acosDeviceTotalsAggregate = _AcosDeviceTotalsAggregate_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 2, 3),
    _AcosDeviceTotalsAggregate_Type()
)
acosDeviceTotalsAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceTotalsAggregate.setStatus("mandatory")
_AcosStatus_ObjectIdentity = ObjectIdentity
acosStatus = _AcosStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 3)
)


class _AcosCpuUtilization_Type(Integer32):
    """Custom type acosCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcosCpuUtilization_Type.__name__ = "Integer32"
_AcosCpuUtilization_Object = MibScalar
acosCpuUtilization = _AcosCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 3, 1),
    _AcosCpuUtilization_Type()
)
acosCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosCpuUtilization.setStatus("mandatory")
_AcosDS1_ObjectIdentity = ObjectIdentity
acosDS1 = _AcosDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4)
)
_AcosT1LineConfigTable_Object = MibTable
acosT1LineConfigTable = _AcosT1LineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    acosT1LineConfigTable.setStatus("mandatory")
_AcosT1LineConfigEntry_Object = MibTableRow
acosT1LineConfigEntry = _AcosT1LineConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 1, 1)
)
acosT1LineConfigEntry.setIndexNames(
    (0, "ACOS-MIB", "acosT1LineSlotIndex"),
    (0, "ACOS-MIB", "acosT1LineSlotInterfaceIndex"),
)
if mibBuilder.loadTexts:
    acosT1LineConfigEntry.setStatus("mandatory")
_AcosT1LineSlotIndex_Type = Integer32
_AcosT1LineSlotIndex_Object = MibTableColumn
acosT1LineSlotIndex = _AcosT1LineSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 1, 1, 1),
    _AcosT1LineSlotIndex_Type()
)
acosT1LineSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosT1LineSlotIndex.setStatus("mandatory")
_AcosT1LineSlotInterfaceIndex_Type = Integer32
_AcosT1LineSlotInterfaceIndex_Object = MibTableColumn
acosT1LineSlotInterfaceIndex = _AcosT1LineSlotInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 1, 1, 2),
    _AcosT1LineSlotInterfaceIndex_Type()
)
acosT1LineSlotInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosT1LineSlotInterfaceIndex.setStatus("mandatory")


class _AcosT1LineBuildOut_Type(Integer32):
    """Custom type acosT1LineBuildOut based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("lbo0db", 1),
          ("lbo133ft", 2),
          ("lbo15db", 7),
          ("lbo225db", 8),
          ("lbo266ft", 3),
          ("lbo399ft", 4),
          ("lbo533ft", 5),
          ("lbo75db", 6))
    )


_AcosT1LineBuildOut_Type.__name__ = "Integer32"
_AcosT1LineBuildOut_Object = MibTableColumn
acosT1LineBuildOut = _AcosT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 1, 1, 3),
    _AcosT1LineBuildOut_Type()
)
acosT1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosT1LineBuildOut.setStatus("mandatory")
_AcosDS1ChannelConfigTable_Object = MibTable
acosDS1ChannelConfigTable = _AcosDS1ChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    acosDS1ChannelConfigTable.setStatus("mandatory")
_AcosDS1ChannelConfigEntry_Object = MibTableRow
acosDS1ChannelConfigEntry = _AcosDS1ChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 2, 1)
)
acosDS1ChannelConfigEntry.setIndexNames(
    (0, "ACOS-MIB", "acosDS1ChannelSlotIndex"),
    (0, "ACOS-MIB", "acosDS1ChannelSlotDeviceIndex"),
    (0, "ACOS-MIB", "acosDS1ChannelIndex"),
)
if mibBuilder.loadTexts:
    acosDS1ChannelConfigEntry.setStatus("mandatory")
_AcosDS1ChannelSlotIndex_Type = Integer32
_AcosDS1ChannelSlotIndex_Object = MibTableColumn
acosDS1ChannelSlotIndex = _AcosDS1ChannelSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 2, 1, 1),
    _AcosDS1ChannelSlotIndex_Type()
)
acosDS1ChannelSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDS1ChannelSlotIndex.setStatus("mandatory")
_AcosDS1ChannelSlotDeviceIndex_Type = Integer32
_AcosDS1ChannelSlotDeviceIndex_Object = MibTableColumn
acosDS1ChannelSlotDeviceIndex = _AcosDS1ChannelSlotDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 2, 1, 2),
    _AcosDS1ChannelSlotDeviceIndex_Type()
)
acosDS1ChannelSlotDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDS1ChannelSlotDeviceIndex.setStatus("mandatory")


class _AcosDS1ChannelIndex_Type(Integer32):
    """Custom type acosDS1ChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AcosDS1ChannelIndex_Type.__name__ = "Integer32"
_AcosDS1ChannelIndex_Object = MibTableColumn
acosDS1ChannelIndex = _AcosDS1ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 2, 1, 3),
    _AcosDS1ChannelIndex_Type()
)
acosDS1ChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDS1ChannelIndex.setStatus("mandatory")


class _AcosDS1TxChannelControl_Type(Integer32):
    """Custom type acosDS1TxChannelControl based on Integer32"""
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


_AcosDS1TxChannelControl_Type.__name__ = "Integer32"
_AcosDS1TxChannelControl_Object = MibTableColumn
acosDS1TxChannelControl = _AcosDS1TxChannelControl_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 2, 1, 4),
    _AcosDS1TxChannelControl_Type()
)
acosDS1TxChannelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDS1TxChannelControl.setStatus("mandatory")


class _AcosDS1RxChannelControl_Type(Integer32):
    """Custom type acosDS1RxChannelControl based on Integer32"""
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


_AcosDS1RxChannelControl_Type.__name__ = "Integer32"
_AcosDS1RxChannelControl_Object = MibTableColumn
acosDS1RxChannelControl = _AcosDS1RxChannelControl_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 2, 1, 5),
    _AcosDS1RxChannelControl_Type()
)
acosDS1RxChannelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDS1RxChannelControl.setStatus("mandatory")
_AcosDS1AggChanConfigTable_Object = MibTable
acosDS1AggChanConfigTable = _AcosDS1AggChanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    acosDS1AggChanConfigTable.setStatus("mandatory")
_AcosDS1AggChanConfigEntry_Object = MibTableRow
acosDS1AggChanConfigEntry = _AcosDS1AggChanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 3, 1)
)
acosDS1AggChanConfigEntry.setIndexNames(
    (0, "ACOS-MIB", "acosDS1AggChanSlotIndex"),
    (0, "ACOS-MIB", "acosDS1AggChanSlotDeviceIndex"),
)
if mibBuilder.loadTexts:
    acosDS1AggChanConfigEntry.setStatus("mandatory")
_AcosDS1AggChanSlotIndex_Type = Integer32
_AcosDS1AggChanSlotIndex_Object = MibTableColumn
acosDS1AggChanSlotIndex = _AcosDS1AggChanSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 3, 1, 1),
    _AcosDS1AggChanSlotIndex_Type()
)
acosDS1AggChanSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDS1AggChanSlotIndex.setStatus("mandatory")
_AcosDS1AggChanSlotDeviceIndex_Type = Integer32
_AcosDS1AggChanSlotDeviceIndex_Object = MibTableColumn
acosDS1AggChanSlotDeviceIndex = _AcosDS1AggChanSlotDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 3, 1, 2),
    _AcosDS1AggChanSlotDeviceIndex_Type()
)
acosDS1AggChanSlotDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDS1AggChanSlotDeviceIndex.setStatus("mandatory")
_AcosDS1TxChannelsAggregate_Type = OctetString
_AcosDS1TxChannelsAggregate_Object = MibTableColumn
acosDS1TxChannelsAggregate = _AcosDS1TxChannelsAggregate_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 3, 1, 3),
    _AcosDS1TxChannelsAggregate_Type()
)
acosDS1TxChannelsAggregate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDS1TxChannelsAggregate.setStatus("mandatory")
_AcosDS1RxChannelsAggregate_Type = OctetString
_AcosDS1RxChannelsAggregate_Object = MibTableColumn
acosDS1RxChannelsAggregate = _AcosDS1RxChannelsAggregate_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 4, 3, 1, 4),
    _AcosDS1RxChannelsAggregate_Type()
)
acosDS1RxChannelsAggregate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDS1RxChannelsAggregate.setStatus("mandatory")
_AcosUSI_ObjectIdentity = ObjectIdentity
acosUSI = _AcosUSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 5)
)
_AcosUSIConfigTable_Object = MibTable
acosUSIConfigTable = _AcosUSIConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    acosUSIConfigTable.setStatus("mandatory")
_AcosUSIConfigEntry_Object = MibTableRow
acosUSIConfigEntry = _AcosUSIConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 5, 1, 1)
)
acosUSIConfigEntry.setIndexNames(
    (0, "ACOS-MIB", "acosUSISlotIndex"),
    (0, "ACOS-MIB", "acosUSISlotInterfaceIndex"),
)
if mibBuilder.loadTexts:
    acosUSIConfigEntry.setStatus("mandatory")
_AcosUSISlotIndex_Type = Integer32
_AcosUSISlotIndex_Object = MibTableColumn
acosUSISlotIndex = _AcosUSISlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 5, 1, 1, 1),
    _AcosUSISlotIndex_Type()
)
acosUSISlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosUSISlotIndex.setStatus("mandatory")
_AcosUSISlotInterfaceIndex_Type = Integer32
_AcosUSISlotInterfaceIndex_Object = MibTableColumn
acosUSISlotInterfaceIndex = _AcosUSISlotInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 5, 1, 1, 2),
    _AcosUSISlotInterfaceIndex_Type()
)
acosUSISlotInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosUSISlotInterfaceIndex.setStatus("mandatory")


class _AcosUSIInterfaceType_Type(Integer32):
    """Custom type acosUSIInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 2),
          ("rs530", 7),
          ("rs530a", 8),
          ("v10", 4),
          ("v35", 5),
          ("x21", 6))
    )


_AcosUSIInterfaceType_Type.__name__ = "Integer32"
_AcosUSIInterfaceType_Object = MibTableColumn
acosUSIInterfaceType = _AcosUSIInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 5, 1, 1, 3),
    _AcosUSIInterfaceType_Type()
)
acosUSIInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosUSIInterfaceType.setStatus("mandatory")
_AcosSDSL_ObjectIdentity = ObjectIdentity
acosSDSL = _AcosSDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 6)
)
_AcosSDSLConfigTable_Object = MibTable
acosSDSLConfigTable = _AcosSDSLConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    acosSDSLConfigTable.setStatus("mandatory")
_AcosSDSLConfigEntry_Object = MibTableRow
acosSDSLConfigEntry = _AcosSDSLConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 6, 1, 1)
)
acosSDSLConfigEntry.setIndexNames(
    (0, "ACOS-MIB", "acosSDSLSlotIndex"),
    (0, "ACOS-MIB", "acosSDSLSlotInterfaceIndex"),
)
if mibBuilder.loadTexts:
    acosSDSLConfigEntry.setStatus("mandatory")
_AcosSDSLSlotIndex_Type = Integer32
_AcosSDSLSlotIndex_Object = MibTableColumn
acosSDSLSlotIndex = _AcosSDSLSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 6, 1, 1, 1),
    _AcosSDSLSlotIndex_Type()
)
acosSDSLSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosSDSLSlotIndex.setStatus("mandatory")
_AcosSDSLSlotInterfaceIndex_Type = Integer32
_AcosSDSLSlotInterfaceIndex_Object = MibTableColumn
acosSDSLSlotInterfaceIndex = _AcosSDSLSlotInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 6, 1, 1, 2),
    _AcosSDSLSlotInterfaceIndex_Type()
)
acosSDSLSlotInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosSDSLSlotInterfaceIndex.setStatus("mandatory")


class _AcosSDSLInterfaceType_Type(Integer32):
    """Custom type acosSDSLInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("co", 2),
          ("cpe", 1))
    )


_AcosSDSLInterfaceType_Type.__name__ = "Integer32"
_AcosSDSLInterfaceType_Object = MibTableColumn
acosSDSLInterfaceType = _AcosSDSLInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 6, 1, 1, 3),
    _AcosSDSLInterfaceType_Type()
)
acosSDSLInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosSDSLInterfaceType.setStatus("mandatory")


class _AcosSDSLClockType_Type(Integer32):
    """Custom type acosSDSLClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_AcosSDSLClockType_Type.__name__ = "Integer32"
_AcosSDSLClockType_Object = MibTableColumn
acosSDSLClockType = _AcosSDSLClockType_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 6, 1, 1, 4),
    _AcosSDSLClockType_Type()
)
acosSDSLClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosSDSLClockType.setStatus("mandatory")
_AcosEthernet_ObjectIdentity = ObjectIdentity
acosEthernet = _AcosEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 7)
)
_AcosEthernetConfigTable_Object = MibTable
acosEthernetConfigTable = _AcosEthernetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    acosEthernetConfigTable.setStatus("mandatory")
_AcosEthernetConfigEntry_Object = MibTableRow
acosEthernetConfigEntry = _AcosEthernetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 7, 1, 1)
)
acosEthernetConfigEntry.setIndexNames(
    (0, "ACOS-MIB", "acosEthernetSlotIndex"),
)
if mibBuilder.loadTexts:
    acosEthernetConfigEntry.setStatus("mandatory")
_AcosEthernetSlotIndex_Type = Integer32
_AcosEthernetSlotIndex_Object = MibTableColumn
acosEthernetSlotIndex = _AcosEthernetSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 7, 1, 1, 1),
    _AcosEthernetSlotIndex_Type()
)
acosEthernetSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosEthernetSlotIndex.setStatus("mandatory")


class _AcosEthernetFullDuplex_Type(Integer32):
    """Custom type acosEthernetFullDuplex based on Integer32"""
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


_AcosEthernetFullDuplex_Type.__name__ = "Integer32"
_AcosEthernetFullDuplex_Object = MibTableColumn
acosEthernetFullDuplex = _AcosEthernetFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 7, 1, 1, 2),
    _AcosEthernetFullDuplex_Type()
)
acosEthernetFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosEthernetFullDuplex.setStatus("mandatory")
_AcosWAN_ObjectIdentity = ObjectIdentity
acosWAN = _AcosWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8)
)
_AcosWANConfigTable_Object = MibTable
acosWANConfigTable = _AcosWANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    acosWANConfigTable.setStatus("mandatory")
_AcosWANConfigEntry_Object = MibTableRow
acosWANConfigEntry = _AcosWANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 1, 1)
)
acosWANConfigEntry.setIndexNames(
    (0, "ACOS-MIB", "acosWANSlotIndex"),
    (0, "ACOS-MIB", "acosWANSlotDeviceIndex"),
)
if mibBuilder.loadTexts:
    acosWANConfigEntry.setStatus("mandatory")
_AcosWANSlotIndex_Type = Integer32
_AcosWANSlotIndex_Object = MibTableColumn
acosWANSlotIndex = _AcosWANSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 1, 1, 1),
    _AcosWANSlotIndex_Type()
)
acosWANSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANSlotIndex.setStatus("mandatory")
_AcosWANSlotDeviceIndex_Type = Integer32
_AcosWANSlotDeviceIndex_Object = MibTableColumn
acosWANSlotDeviceIndex = _AcosWANSlotDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 1, 1, 2),
    _AcosWANSlotDeviceIndex_Type()
)
acosWANSlotDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANSlotDeviceIndex.setStatus("mandatory")


class _AcosWANDataLinkProtocol_Type(Integer32):
    """Custom type acosWANDataLinkProtocol based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("atm-RFC1483", 6),
          ("cisco-HDLC", 3),
          ("frameRelay", 8),
          ("ip-Plus-HDLC", 4),
          ("ppp", 5),
          ("pppOverAtm-RFC2364", 7),
          ("raw-HDLC", 2),
          ("transparent", 1))
    )


_AcosWANDataLinkProtocol_Type.__name__ = "Integer32"
_AcosWANDataLinkProtocol_Object = MibTableColumn
acosWANDataLinkProtocol = _AcosWANDataLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 1, 1, 3),
    _AcosWANDataLinkProtocol_Type()
)
acosWANDataLinkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosWANDataLinkProtocol.setStatus("mandatory")
_AcosWANSpeed_Type = Integer32
_AcosWANSpeed_Object = MibTableColumn
acosWANSpeed = _AcosWANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 1, 1, 4),
    _AcosWANSpeed_Type()
)
acosWANSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosWANSpeed.setStatus("mandatory")
_AcosWANSerialStatsTable_Object = MibTable
acosWANSerialStatsTable = _AcosWANSerialStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    acosWANSerialStatsTable.setStatus("mandatory")
_AcosWANSerialStatsEntry_Object = MibTableRow
acosWANSerialStatsEntry = _AcosWANSerialStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1)
)
acosWANSerialStatsEntry.setIndexNames(
    (0, "ACOS-MIB", "acosWANSerialStatsSlotIndex"),
    (0, "ACOS-MIB", "acosWANSerialStatsSlotDeviceIndex"),
)
if mibBuilder.loadTexts:
    acosWANSerialStatsEntry.setStatus("mandatory")
_AcosWANSerialStatsSlotIndex_Type = Integer32
_AcosWANSerialStatsSlotIndex_Object = MibTableColumn
acosWANSerialStatsSlotIndex = _AcosWANSerialStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 1),
    _AcosWANSerialStatsSlotIndex_Type()
)
acosWANSerialStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANSerialStatsSlotIndex.setStatus("mandatory")
_AcosWANSerialStatsSlotDeviceIndex_Type = Integer32
_AcosWANSerialStatsSlotDeviceIndex_Object = MibTableColumn
acosWANSerialStatsSlotDeviceIndex = _AcosWANSerialStatsSlotDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 2),
    _AcosWANSerialStatsSlotDeviceIndex_Type()
)
acosWANSerialStatsSlotDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANSerialStatsSlotDeviceIndex.setStatus("mandatory")
_AcosWANTotalRxFrames_Type = Integer32
_AcosWANTotalRxFrames_Object = MibTableColumn
acosWANTotalRxFrames = _AcosWANTotalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 3),
    _AcosWANTotalRxFrames_Type()
)
acosWANTotalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTotalRxFrames.setStatus("mandatory")
_AcosWANTotalRxOctets_Type = Integer32
_AcosWANTotalRxOctets_Object = MibTableColumn
acosWANTotalRxOctets = _AcosWANTotalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 4),
    _AcosWANTotalRxOctets_Type()
)
acosWANTotalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTotalRxOctets.setStatus("mandatory")
_AcosWANRxMissedFrames_Type = Integer32
_AcosWANRxMissedFrames_Object = MibTableColumn
acosWANRxMissedFrames = _AcosWANRxMissedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 5),
    _AcosWANRxMissedFrames_Type()
)
acosWANRxMissedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxMissedFrames.setStatus("mandatory")
_AcosWANRxErrorFrames_Type = Integer32
_AcosWANRxErrorFrames_Object = MibTableColumn
acosWANRxErrorFrames = _AcosWANRxErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 6),
    _AcosWANRxErrorFrames_Type()
)
acosWANRxErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxErrorFrames.setStatus("mandatory")
_AcosWANRxGlitchErrors_Type = Integer32
_AcosWANRxGlitchErrors_Object = MibTableColumn
acosWANRxGlitchErrors = _AcosWANRxGlitchErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 7),
    _AcosWANRxGlitchErrors_Type()
)
acosWANRxGlitchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxGlitchErrors.setStatus("mandatory")
_AcosWANRxPllErrors_Type = Integer32
_AcosWANRxPllErrors_Object = MibTableColumn
acosWANRxPllErrors = _AcosWANRxPllErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 8),
    _AcosWANRxPllErrors_Type()
)
acosWANRxPllErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxPllErrors.setStatus("mandatory")
_AcosWANRxLongErrors_Type = Integer32
_AcosWANRxLongErrors_Object = MibTableColumn
acosWANRxLongErrors = _AcosWANRxLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 9),
    _AcosWANRxLongErrors_Type()
)
acosWANRxLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxLongErrors.setStatus("mandatory")
_AcosWANRxNonOctetErrors_Type = Integer32
_AcosWANRxNonOctetErrors_Object = MibTableColumn
acosWANRxNonOctetErrors = _AcosWANRxNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 10),
    _AcosWANRxNonOctetErrors_Type()
)
acosWANRxNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxNonOctetErrors.setStatus("mandatory")
_AcosWANRxAbortErrors_Type = Integer32
_AcosWANRxAbortErrors_Object = MibTableColumn
acosWANRxAbortErrors = _AcosWANRxAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 11),
    _AcosWANRxAbortErrors_Type()
)
acosWANRxAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxAbortErrors.setStatus("mandatory")
_AcosWANRxCrcErrors_Type = Integer32
_AcosWANRxCrcErrors_Object = MibTableColumn
acosWANRxCrcErrors = _AcosWANRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 12),
    _AcosWANRxCrcErrors_Type()
)
acosWANRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxCrcErrors.setStatus("mandatory")
_AcosWANRxOverrunErrors_Type = Integer32
_AcosWANRxOverrunErrors_Object = MibTableColumn
acosWANRxOverrunErrors = _AcosWANRxOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 13),
    _AcosWANRxOverrunErrors_Type()
)
acosWANRxOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxOverrunErrors.setStatus("mandatory")
_AcosWANRxCdLostErrors_Type = Integer32
_AcosWANRxCdLostErrors_Object = MibTableColumn
acosWANRxCdLostErrors = _AcosWANRxCdLostErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 14),
    _AcosWANRxCdLostErrors_Type()
)
acosWANRxCdLostErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANRxCdLostErrors.setStatus("mandatory")
_AcosWANTotalTxFrames_Type = Integer32
_AcosWANTotalTxFrames_Object = MibTableColumn
acosWANTotalTxFrames = _AcosWANTotalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 15),
    _AcosWANTotalTxFrames_Type()
)
acosWANTotalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTotalTxFrames.setStatus("mandatory")
_AcosWANTotalTxOctets_Type = Integer32
_AcosWANTotalTxOctets_Object = MibTableColumn
acosWANTotalTxOctets = _AcosWANTotalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 16),
    _AcosWANTotalTxOctets_Type()
)
acosWANTotalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTotalTxOctets.setStatus("mandatory")
_AcosWANTxMissedFrames_Type = Integer32
_AcosWANTxMissedFrames_Object = MibTableColumn
acosWANTxMissedFrames = _AcosWANTxMissedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 17),
    _AcosWANTxMissedFrames_Type()
)
acosWANTxMissedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTxMissedFrames.setStatus("mandatory")
_AcosWANTxDiscardedFrames_Type = Integer32
_AcosWANTxDiscardedFrames_Object = MibTableColumn
acosWANTxDiscardedFrames = _AcosWANTxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 18),
    _AcosWANTxDiscardedFrames_Type()
)
acosWANTxDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTxDiscardedFrames.setStatus("mandatory")
_AcosWANTxErrorFrames_Type = Integer32
_AcosWANTxErrorFrames_Object = MibTableColumn
acosWANTxErrorFrames = _AcosWANTxErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 19),
    _AcosWANTxErrorFrames_Type()
)
acosWANTxErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTxErrorFrames.setStatus("mandatory")
_AcosWANTxGlitchErrors_Type = Integer32
_AcosWANTxGlitchErrors_Object = MibTableColumn
acosWANTxGlitchErrors = _AcosWANTxGlitchErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 20),
    _AcosWANTxGlitchErrors_Type()
)
acosWANTxGlitchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTxGlitchErrors.setStatus("mandatory")
_AcosWANTxUnderrunErrors_Type = Integer32
_AcosWANTxUnderrunErrors_Object = MibTableColumn
acosWANTxUnderrunErrors = _AcosWANTxUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 22),
    _AcosWANTxUnderrunErrors_Type()
)
acosWANTxUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTxUnderrunErrors.setStatus("mandatory")
_AcosWANTxCtsLostErrors_Type = Integer32
_AcosWANTxCtsLostErrors_Object = MibTableColumn
acosWANTxCtsLostErrors = _AcosWANTxCtsLostErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 2, 1, 23),
    _AcosWANTxCtsLostErrors_Type()
)
acosWANTxCtsLostErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANTxCtsLostErrors.setStatus("mandatory")
_AcosWANAtmStatsTable_Object = MibTable
acosWANAtmStatsTable = _AcosWANAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    acosWANAtmStatsTable.setStatus("mandatory")
_AcosWANAtmStatsEntry_Object = MibTableRow
acosWANAtmStatsEntry = _AcosWANAtmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1)
)
acosWANAtmStatsEntry.setIndexNames(
    (0, "ACOS-MIB", "acosWANAtmStatsSlotIndex"),
    (0, "ACOS-MIB", "acosWANAtmStatsSlotDeviceIndex"),
)
if mibBuilder.loadTexts:
    acosWANAtmStatsEntry.setStatus("mandatory")
_AcosWANAtmStatsSlotIndex_Type = Integer32
_AcosWANAtmStatsSlotIndex_Object = MibTableColumn
acosWANAtmStatsSlotIndex = _AcosWANAtmStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 1),
    _AcosWANAtmStatsSlotIndex_Type()
)
acosWANAtmStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmStatsSlotIndex.setStatus("mandatory")
_AcosWANAtmStatsSlotDeviceIndex_Type = Integer32
_AcosWANAtmStatsSlotDeviceIndex_Object = MibTableColumn
acosWANAtmStatsSlotDeviceIndex = _AcosWANAtmStatsSlotDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 2),
    _AcosWANAtmStatsSlotDeviceIndex_Type()
)
acosWANAtmStatsSlotDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmStatsSlotDeviceIndex.setStatus("mandatory")
_AcosWANAtmTotalRxCells_Type = Integer32
_AcosWANAtmTotalRxCells_Object = MibTableColumn
acosWANAtmTotalRxCells = _AcosWANAtmTotalRxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 3),
    _AcosWANAtmTotalRxCells_Type()
)
acosWANAtmTotalRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmTotalRxCells.setStatus("mandatory")
_AcosWANAtmClpiRxCells_Type = Integer32
_AcosWANAtmClpiRxCells_Object = MibTableColumn
acosWANAtmClpiRxCells = _AcosWANAtmClpiRxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 4),
    _AcosWANAtmClpiRxCells_Type()
)
acosWANAtmClpiRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmClpiRxCells.setStatus("mandatory")
_AcosWANAtmOamRxCells_Type = Integer32
_AcosWANAtmOamRxCells_Object = MibTableColumn
acosWANAtmOamRxCells = _AcosWANAtmOamRxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 5),
    _AcosWANAtmOamRxCells_Type()
)
acosWANAtmOamRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmOamRxCells.setStatus("mandatory")
_AcosWANAtmEfciRxCells_Type = Integer32
_AcosWANAtmEfciRxCells_Object = MibTableColumn
acosWANAtmEfciRxCells = _AcosWANAtmEfciRxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 6),
    _AcosWANAtmEfciRxCells_Type()
)
acosWANAtmEfciRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmEfciRxCells.setStatus("mandatory")
_AcosWANAtmRmRxCells_Type = Integer32
_AcosWANAtmRmRxCells_Object = MibTableColumn
acosWANAtmRmRxCells = _AcosWANAtmRmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 7),
    _AcosWANAtmRmRxCells_Type()
)
acosWANAtmRmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmRmRxCells.setStatus("mandatory")
_AcosWANAtmRxCellsDiscarded_Type = Integer32
_AcosWANAtmRxCellsDiscarded_Object = MibTableColumn
acosWANAtmRxCellsDiscarded = _AcosWANAtmRxCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 8),
    _AcosWANAtmRxCellsDiscarded_Type()
)
acosWANAtmRxCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmRxCellsDiscarded.setStatus("mandatory")
_AcosWANAtmTotalTxCells_Type = Integer32
_AcosWANAtmTotalTxCells_Object = MibTableColumn
acosWANAtmTotalTxCells = _AcosWANAtmTotalTxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 9),
    _AcosWANAtmTotalTxCells_Type()
)
acosWANAtmTotalTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmTotalTxCells.setStatus("mandatory")
_AcosWANAtmOamTxCells_Type = Integer32
_AcosWANAtmOamTxCells_Object = MibTableColumn
acosWANAtmOamTxCells = _AcosWANAtmOamTxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 10),
    _AcosWANAtmOamTxCells_Type()
)
acosWANAtmOamTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmOamTxCells.setStatus("mandatory")
_AcosWANAtmClpiTxCells_Type = Integer32
_AcosWANAtmClpiTxCells_Object = MibTableColumn
acosWANAtmClpiTxCells = _AcosWANAtmClpiTxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 11),
    _AcosWANAtmClpiTxCells_Type()
)
acosWANAtmClpiTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmClpiTxCells.setStatus("mandatory")
_AcosWANAtmEfciTxCells_Type = Integer32
_AcosWANAtmEfciTxCells_Object = MibTableColumn
acosWANAtmEfciTxCells = _AcosWANAtmEfciTxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 12),
    _AcosWANAtmEfciTxCells_Type()
)
acosWANAtmEfciTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmEfciTxCells.setStatus("mandatory")
_AcosWANAtmRmTxCells_Type = Integer32
_AcosWANAtmRmTxCells_Object = MibTableColumn
acosWANAtmRmTxCells = _AcosWANAtmRmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 13),
    _AcosWANAtmRmTxCells_Type()
)
acosWANAtmRmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmRmTxCells.setStatus("mandatory")
_AcosWANAtmRxHecErrors_Type = Integer32
_AcosWANAtmRxHecErrors_Object = MibTableColumn
acosWANAtmRxHecErrors = _AcosWANAtmRxHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 14),
    _AcosWANAtmRxHecErrors_Type()
)
acosWANAtmRxHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmRxHecErrors.setStatus("mandatory")


class _AcosWANAtmPortStatus_Type(Integer32):
    """Custom type acosWANAtmPortStatus based on Integer32"""
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


_AcosWANAtmPortStatus_Type.__name__ = "Integer32"
_AcosWANAtmPortStatus_Object = MibTableColumn
acosWANAtmPortStatus = _AcosWANAtmPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 8, 3, 1, 15),
    _AcosWANAtmPortStatus_Type()
)
acosWANAtmPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosWANAtmPortStatus.setStatus("mandatory")
_AcosRouting_ObjectIdentity = ObjectIdentity
acosRouting = _AcosRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9)
)
_AcosDeviceIpAddressTable_Object = MibTable
acosDeviceIpAddressTable = _AcosDeviceIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    acosDeviceIpAddressTable.setStatus("mandatory")
_AcosDeviceIpAddressEntry_Object = MibTableRow
acosDeviceIpAddressEntry = _AcosDeviceIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 1, 1)
)
acosDeviceIpAddressEntry.setIndexNames(
    (0, "ACOS-MIB", "acosDeviceIpSlotIndex"),
    (0, "ACOS-MIB", "acosDeviceIpInterfaceIndex"),
    (0, "ACOS-MIB", "acosDeviceIpPortIndex"),
    (0, "ACOS-MIB", "acosDeviceIpConnectionIndex"),
)
if mibBuilder.loadTexts:
    acosDeviceIpAddressEntry.setStatus("mandatory")
_AcosDeviceIpSlotIndex_Type = Integer32
_AcosDeviceIpSlotIndex_Object = MibTableColumn
acosDeviceIpSlotIndex = _AcosDeviceIpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 1, 1, 1),
    _AcosDeviceIpSlotIndex_Type()
)
acosDeviceIpSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceIpSlotIndex.setStatus("mandatory")
_AcosDeviceIpInterfaceIndex_Type = Integer32
_AcosDeviceIpInterfaceIndex_Object = MibTableColumn
acosDeviceIpInterfaceIndex = _AcosDeviceIpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 1, 1, 2),
    _AcosDeviceIpInterfaceIndex_Type()
)
acosDeviceIpInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceIpInterfaceIndex.setStatus("mandatory")
_AcosDeviceIpPortIndex_Type = Integer32
_AcosDeviceIpPortIndex_Object = MibTableColumn
acosDeviceIpPortIndex = _AcosDeviceIpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 1, 1, 3),
    _AcosDeviceIpPortIndex_Type()
)
acosDeviceIpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceIpPortIndex.setStatus("mandatory")
_AcosDeviceIpConnectionIndex_Type = Integer32
_AcosDeviceIpConnectionIndex_Object = MibTableColumn
acosDeviceIpConnectionIndex = _AcosDeviceIpConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 1, 1, 4),
    _AcosDeviceIpConnectionIndex_Type()
)
acosDeviceIpConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceIpConnectionIndex.setStatus("mandatory")
_AcosDeviceIpAddress_Type = IpAddress
_AcosDeviceIpAddress_Object = MibTableColumn
acosDeviceIpAddress = _AcosDeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 1, 1, 5),
    _AcosDeviceIpAddress_Type()
)
acosDeviceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDeviceIpAddress.setStatus("mandatory")
_AcosDeviceIpAddressSubnetMask_Type = IpAddress
_AcosDeviceIpAddressSubnetMask_Object = MibTableColumn
acosDeviceIpAddressSubnetMask = _AcosDeviceIpAddressSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 1, 1, 6),
    _AcosDeviceIpAddressSubnetMask_Type()
)
acosDeviceIpAddressSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDeviceIpAddressSubnetMask.setStatus("mandatory")
_AcosDeviceIpPeerAddress_Type = IpAddress
_AcosDeviceIpPeerAddress_Object = MibTableColumn
acosDeviceIpPeerAddress = _AcosDeviceIpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 1, 1, 7),
    _AcosDeviceIpPeerAddress_Type()
)
acosDeviceIpPeerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDeviceIpPeerAddress.setStatus("mandatory")


class _AcosRIPControl_Type(Integer32):
    """Custom type acosRIPControl based on Integer32"""
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


_AcosRIPControl_Type.__name__ = "Integer32"
_AcosRIPControl_Object = MibScalar
acosRIPControl = _AcosRIPControl_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 2),
    _AcosRIPControl_Type()
)
acosRIPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosRIPControl.setStatus("mandatory")
_AcosDeviceRipParameterTable_Object = MibTable
acosDeviceRipParameterTable = _AcosDeviceRipParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 3)
)
if mibBuilder.loadTexts:
    acosDeviceRipParameterTable.setStatus("mandatory")
_AcosDeviceRipParameterEntry_Object = MibTableRow
acosDeviceRipParameterEntry = _AcosDeviceRipParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 3, 1)
)
acosDeviceRipParameterEntry.setIndexNames(
    (0, "ACOS-MIB", "acosDeviceRipSlotIndex"),
    (0, "ACOS-MIB", "acosDeviceRipInterfaceIndex"),
    (0, "ACOS-MIB", "acosDeviceRipPortIndex"),
)
if mibBuilder.loadTexts:
    acosDeviceRipParameterEntry.setStatus("mandatory")
_AcosDeviceRipSlotIndex_Type = Integer32
_AcosDeviceRipSlotIndex_Object = MibTableColumn
acosDeviceRipSlotIndex = _AcosDeviceRipSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 3, 1, 1),
    _AcosDeviceRipSlotIndex_Type()
)
acosDeviceRipSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceRipSlotIndex.setStatus("mandatory")
_AcosDeviceRipInterfaceIndex_Type = Integer32
_AcosDeviceRipInterfaceIndex_Object = MibTableColumn
acosDeviceRipInterfaceIndex = _AcosDeviceRipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 3, 1, 2),
    _AcosDeviceRipInterfaceIndex_Type()
)
acosDeviceRipInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceRipInterfaceIndex.setStatus("mandatory")
_AcosDeviceRipPortIndex_Type = Integer32
_AcosDeviceRipPortIndex_Object = MibTableColumn
acosDeviceRipPortIndex = _AcosDeviceRipPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 3, 1, 3),
    _AcosDeviceRipPortIndex_Type()
)
acosDeviceRipPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDeviceRipPortIndex.setStatus("mandatory")


class _AcosDeviceRipVersion_Type(Integer32):
    """Custom type acosDeviceRipVersion based on Integer32"""
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
        *(("disabled", 1),
          ("version1Broadcast", 2),
          ("version2Broadcast", 3),
          ("version2Multicast", 4))
    )


_AcosDeviceRipVersion_Type.__name__ = "Integer32"
_AcosDeviceRipVersion_Object = MibTableColumn
acosDeviceRipVersion = _AcosDeviceRipVersion_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 3, 1, 4),
    _AcosDeviceRipVersion_Type()
)
acosDeviceRipVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDeviceRipVersion.setStatus("mandatory")


class _AcosDeviceRipPoisonedReverse_Type(Integer32):
    """Custom type acosDeviceRipPoisonedReverse based on Integer32"""
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


_AcosDeviceRipPoisonedReverse_Type.__name__ = "Integer32"
_AcosDeviceRipPoisonedReverse_Object = MibTableColumn
acosDeviceRipPoisonedReverse = _AcosDeviceRipPoisonedReverse_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 3, 1, 5),
    _AcosDeviceRipPoisonedReverse_Type()
)
acosDeviceRipPoisonedReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDeviceRipPoisonedReverse.setStatus("mandatory")
_AcosDNSServerAddress_Type = IpAddress
_AcosDNSServerAddress_Object = MibScalar
acosDNSServerAddress = _AcosDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 4),
    _AcosDNSServerAddress_Type()
)
acosDNSServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDNSServerAddress.setStatus("mandatory")
_AcosDNSTimeout_Type = TimeTicks
_AcosDNSTimeout_Object = MibScalar
acosDNSTimeout = _AcosDNSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 9, 5),
    _AcosDNSTimeout_Type()
)
acosDNSTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDNSTimeout.setStatus("mandatory")
_AcosBridge_ObjectIdentity = ObjectIdentity
acosBridge = _AcosBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 10)
)


class _AcosBridging_Type(Integer32):
    """Custom type acosBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globallyDisabled", 2),
          ("globallyEnabled", 1))
    )


_AcosBridging_Type.__name__ = "Integer32"
_AcosBridging_Object = MibScalar
acosBridging = _AcosBridging_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 10, 1),
    _AcosBridging_Type()
)
acosBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosBridging.setStatus("mandatory")
_AcosBridgeTable_Object = MibTable
acosBridgeTable = _AcosBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    acosBridgeTable.setStatus("mandatory")
_AcosBridgeEntry_Object = MibTableRow
acosBridgeEntry = _AcosBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 10, 2, 1)
)
acosBridgeEntry.setIndexNames(
    (0, "ACOS-MIB", "acosBridgeSlotIndex"),
    (0, "ACOS-MIB", "acosBridgeInterfaceIndex"),
    (0, "ACOS-MIB", "acosBridgePortIndex"),
)
if mibBuilder.loadTexts:
    acosBridgeEntry.setStatus("mandatory")
_AcosBridgeSlotIndex_Type = Integer32
_AcosBridgeSlotIndex_Object = MibTableColumn
acosBridgeSlotIndex = _AcosBridgeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 10, 2, 1, 1),
    _AcosBridgeSlotIndex_Type()
)
acosBridgeSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosBridgeSlotIndex.setStatus("mandatory")
_AcosBridgeInterfaceIndex_Type = Integer32
_AcosBridgeInterfaceIndex_Object = MibTableColumn
acosBridgeInterfaceIndex = _AcosBridgeInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 10, 2, 1, 2),
    _AcosBridgeInterfaceIndex_Type()
)
acosBridgeInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosBridgeInterfaceIndex.setStatus("mandatory")
_AcosBridgePortIndex_Type = Integer32
_AcosBridgePortIndex_Object = MibTableColumn
acosBridgePortIndex = _AcosBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 10, 2, 1, 3),
    _AcosBridgePortIndex_Type()
)
acosBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosBridgePortIndex.setStatus("mandatory")


class _AcosBridgeControl_Type(Integer32):
    """Custom type acosBridgeControl based on Integer32"""
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


_AcosBridgeControl_Type.__name__ = "Integer32"
_AcosBridgeControl_Object = MibTableColumn
acosBridgeControl = _AcosBridgeControl_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 10, 2, 1, 4),
    _AcosBridgeControl_Type()
)
acosBridgeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosBridgeControl.setStatus("mandatory")
_AcosTftpClient_ObjectIdentity = ObjectIdentity
acosTftpClient = _AcosTftpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 11)
)
_AcosTftpServerAddress_Type = IpAddress
_AcosTftpServerAddress_Object = MibScalar
acosTftpServerAddress = _AcosTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 11, 1),
    _AcosTftpServerAddress_Type()
)
acosTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosTftpServerAddress.setStatus("mandatory")


class _AcosTftpAcosName_Type(DisplayString):
    """Custom type acosTftpAcosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcosTftpAcosName_Type.__name__ = "DisplayString"
_AcosTftpAcosName_Object = MibScalar
acosTftpAcosName = _AcosTftpAcosName_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 11, 2),
    _AcosTftpAcosName_Type()
)
acosTftpAcosName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosTftpAcosName.setStatus("mandatory")


class _AcosTftpUpgradeACOS_Type(Integer32):
    """Custom type acosTftpUpgradeACOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("upgradeACOS", 2))
    )


_AcosTftpUpgradeACOS_Type.__name__ = "Integer32"
_AcosTftpUpgradeACOS_Object = MibScalar
acosTftpUpgradeACOS = _AcosTftpUpgradeACOS_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 11, 3),
    _AcosTftpUpgradeACOS_Type()
)
acosTftpUpgradeACOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosTftpUpgradeACOS.setStatus("mandatory")


class _AcosTftpApplicationName_Type(DisplayString):
    """Custom type acosTftpApplicationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcosTftpApplicationName_Type.__name__ = "DisplayString"
_AcosTftpApplicationName_Object = MibScalar
acosTftpApplicationName = _AcosTftpApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 11, 4),
    _AcosTftpApplicationName_Type()
)
acosTftpApplicationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosTftpApplicationName.setStatus("mandatory")


class _AcosTftpUpgradeApplication_Type(Integer32):
    """Custom type acosTftpUpgradeApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("upgradeApp", 2))
    )


_AcosTftpUpgradeApplication_Type.__name__ = "Integer32"
_AcosTftpUpgradeApplication_Object = MibScalar
acosTftpUpgradeApplication = _AcosTftpUpgradeApplication_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 11, 5),
    _AcosTftpUpgradeApplication_Type()
)
acosTftpUpgradeApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosTftpUpgradeApplication.setStatus("mandatory")


class _AcosTftpSessionStatus_Type(Integer32):
    """Custom type acosTftpSessionStatus based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("ready", 1),
          ("succeeded", 3))
    )


_AcosTftpSessionStatus_Type.__name__ = "Integer32"
_AcosTftpSessionStatus_Object = MibScalar
acosTftpSessionStatus = _AcosTftpSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 11, 6),
    _AcosTftpSessionStatus_Type()
)
acosTftpSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosTftpSessionStatus.setStatus("mandatory")


class _AcosTftpFailReason_Type(DisplayString):
    """Custom type acosTftpFailReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcosTftpFailReason_Type.__name__ = "DisplayString"
_AcosTftpFailReason_Object = MibScalar
acosTftpFailReason = _AcosTftpFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 11, 7),
    _AcosTftpFailReason_Type()
)
acosTftpFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosTftpFailReason.setStatus("mandatory")
_AcosTftpOctetsRead_Type = Integer32
_AcosTftpOctetsRead_Object = MibScalar
acosTftpOctetsRead = _AcosTftpOctetsRead_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 11, 8),
    _AcosTftpOctetsRead_Type()
)
acosTftpOctetsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosTftpOctetsRead.setStatus("mandatory")
_AcosManagement_ObjectIdentity = ObjectIdentity
acosManagement = _AcosManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 12)
)
_AcosManagerIpAddress_Type = IpAddress
_AcosManagerIpAddress_Object = MibScalar
acosManagerIpAddress = _AcosManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 12, 1),
    _AcosManagerIpAddress_Type()
)
acosManagerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosManagerIpAddress.setStatus("mandatory")


class _AcosManagerWriteCommunity_Type(DisplayString):
    """Custom type acosManagerWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_AcosManagerWriteCommunity_Type.__name__ = "DisplayString"
_AcosManagerWriteCommunity_Object = MibScalar
acosManagerWriteCommunity = _AcosManagerWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 12, 2),
    _AcosManagerWriteCommunity_Type()
)
acosManagerWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosManagerWriteCommunity.setStatus("mandatory")
_AcosTrapObjects_ObjectIdentity = ObjectIdentity
acosTrapObjects = _AcosTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 13)
)


class _AcosTftpFileName_Type(DisplayString):
    """Custom type acosTftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcosTftpFileName_Type.__name__ = "DisplayString"
_AcosTftpFileName_Object = MibScalar
acosTftpFileName = _AcosTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 13, 1),
    _AcosTftpFileName_Type()
)
acosTftpFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acosTftpFileName.setStatus("mandatory")
_AcosDhcp_ObjectIdentity = ObjectIdentity
acosDhcp = _AcosDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14)
)


class _AcosDhcpEnable_Type(Integer32):
    """Custom type acosDhcpEnable based on Integer32"""
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


_AcosDhcpEnable_Type.__name__ = "Integer32"
_AcosDhcpEnable_Object = MibScalar
acosDhcpEnable = _AcosDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 1),
    _AcosDhcpEnable_Type()
)
acosDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpEnable.setStatus("mandatory")
_AcosDhcpGateway_Type = IpAddress
_AcosDhcpGateway_Object = MibScalar
acosDhcpGateway = _AcosDhcpGateway_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 2),
    _AcosDhcpGateway_Type()
)
acosDhcpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpGateway.setStatus("mandatory")
_AcosDhcpDnsServer_Type = IpAddress
_AcosDhcpDnsServer_Object = MibScalar
acosDhcpDnsServer = _AcosDhcpDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 3),
    _AcosDhcpDnsServer_Type()
)
acosDhcpDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpDnsServer.setStatus("mandatory")
_AcosDhcpSubnet_Type = IpAddress
_AcosDhcpSubnet_Object = MibScalar
acosDhcpSubnet = _AcosDhcpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 4),
    _AcosDhcpSubnet_Type()
)
acosDhcpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpSubnet.setStatus("mandatory")
_AcosDhcpLowAddress_Type = IpAddress
_AcosDhcpLowAddress_Object = MibScalar
acosDhcpLowAddress = _AcosDhcpLowAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 5),
    _AcosDhcpLowAddress_Type()
)
acosDhcpLowAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpLowAddress.setStatus("mandatory")
_AcosDhcpHighAddress_Type = IpAddress
_AcosDhcpHighAddress_Object = MibScalar
acosDhcpHighAddress = _AcosDhcpHighAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 6),
    _AcosDhcpHighAddress_Type()
)
acosDhcpHighAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpHighAddress.setStatus("mandatory")
_AcosDhcpLeaseTime_Type = Integer32
_AcosDhcpLeaseTime_Object = MibScalar
acosDhcpLeaseTime = _AcosDhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 7),
    _AcosDhcpLeaseTime_Type()
)
acosDhcpLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpLeaseTime.setStatus("mandatory")


class _AcosDhcpDomainName_Type(DisplayString):
    """Custom type acosDhcpDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AcosDhcpDomainName_Type.__name__ = "DisplayString"
_AcosDhcpDomainName_Object = MibScalar
acosDhcpDomainName = _AcosDhcpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 8),
    _AcosDhcpDomainName_Type()
)
acosDhcpDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpDomainName.setStatus("mandatory")
_AcosDhcpInterface_Type = Integer32
_AcosDhcpInterface_Object = MibScalar
acosDhcpInterface = _AcosDhcpInterface_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 9),
    _AcosDhcpInterface_Type()
)
acosDhcpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpInterface.setStatus("mandatory")
_AcosDhcpClientTable_Object = MibTable
acosDhcpClientTable = _AcosDhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10)
)
if mibBuilder.loadTexts:
    acosDhcpClientTable.setStatus("mandatory")
_AcosDhcpClientEntry_Object = MibTableRow
acosDhcpClientEntry = _AcosDhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10, 1)
)
acosDhcpClientEntry.setIndexNames(
    (0, "ACOS-MIB", "acosDhcpClientIndex"),
)
if mibBuilder.loadTexts:
    acosDhcpClientEntry.setStatus("mandatory")
_AcosDhcpClientIndex_Type = Integer32
_AcosDhcpClientIndex_Object = MibTableColumn
acosDhcpClientIndex = _AcosDhcpClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10, 1, 1),
    _AcosDhcpClientIndex_Type()
)
acosDhcpClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosDhcpClientIndex.setStatus("mandatory")
_AcosDhcpClientIpAddress_Type = IpAddress
_AcosDhcpClientIpAddress_Object = MibTableColumn
acosDhcpClientIpAddress = _AcosDhcpClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10, 1, 2),
    _AcosDhcpClientIpAddress_Type()
)
acosDhcpClientIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpClientIpAddress.setStatus("mandatory")


class _AcosDhcpClientMacAddress_Type(OctetString):
    """Custom type acosDhcpClientMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AcosDhcpClientMacAddress_Type.__name__ = "OctetString"
_AcosDhcpClientMacAddress_Object = MibTableColumn
acosDhcpClientMacAddress = _AcosDhcpClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10, 1, 3),
    _AcosDhcpClientMacAddress_Type()
)
acosDhcpClientMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpClientMacAddress.setStatus("mandatory")


class _AcosDhcpClientName_Type(DisplayString):
    """Custom type acosDhcpClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AcosDhcpClientName_Type.__name__ = "DisplayString"
_AcosDhcpClientName_Object = MibTableColumn
acosDhcpClientName = _AcosDhcpClientName_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10, 1, 4),
    _AcosDhcpClientName_Type()
)
acosDhcpClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpClientName.setStatus("mandatory")
_AcosDhcpClientLeaseTime_Type = Integer32
_AcosDhcpClientLeaseTime_Object = MibTableColumn
acosDhcpClientLeaseTime = _AcosDhcpClientLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10, 1, 5),
    _AcosDhcpClientLeaseTime_Type()
)
acosDhcpClientLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpClientLeaseTime.setStatus("mandatory")
_AcosDhcpClientSubnetMask_Type = IpAddress
_AcosDhcpClientSubnetMask_Object = MibTableColumn
acosDhcpClientSubnetMask = _AcosDhcpClientSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10, 1, 6),
    _AcosDhcpClientSubnetMask_Type()
)
acosDhcpClientSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpClientSubnetMask.setStatus("mandatory")
_AcosDhcpClientGateway_Type = IpAddress
_AcosDhcpClientGateway_Object = MibTableColumn
acosDhcpClientGateway = _AcosDhcpClientGateway_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10, 1, 7),
    _AcosDhcpClientGateway_Type()
)
acosDhcpClientGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpClientGateway.setStatus("mandatory")
_AcosDhcpClientDnsServer_Type = IpAddress
_AcosDhcpClientDnsServer_Object = MibTableColumn
acosDhcpClientDnsServer = _AcosDhcpClientDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 14, 10, 1, 8),
    _AcosDhcpClientDnsServer_Type()
)
acosDhcpClientDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosDhcpClientDnsServer.setStatus("mandatory")
_AcosNat_ObjectIdentity = ObjectIdentity
acosNat = _AcosNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15)
)
_AcosNatServerTable_Object = MibTable
acosNatServerTable = _AcosNatServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    acosNatServerTable.setStatus("mandatory")
_AcosNatServerEntry_Object = MibTableRow
acosNatServerEntry = _AcosNatServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 1, 1)
)
acosNatServerEntry.setIndexNames(
    (0, "ACOS-MIB", "acosNatServerIndex"),
)
if mibBuilder.loadTexts:
    acosNatServerEntry.setStatus("mandatory")
_AcosNatServerIndex_Type = Integer32
_AcosNatServerIndex_Object = MibTableColumn
acosNatServerIndex = _AcosNatServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 1, 1, 1),
    _AcosNatServerIndex_Type()
)
acosNatServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosNatServerIndex.setStatus("mandatory")
_AcosNatServerTranslatedIpAddress_Type = IpAddress
_AcosNatServerTranslatedIpAddress_Object = MibTableColumn
acosNatServerTranslatedIpAddress = _AcosNatServerTranslatedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 1, 1, 2),
    _AcosNatServerTranslatedIpAddress_Type()
)
acosNatServerTranslatedIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosNatServerTranslatedIpAddress.setStatus("mandatory")
_AcosNatServerTranslatedPort_Type = Integer32
_AcosNatServerTranslatedPort_Object = MibTableColumn
acosNatServerTranslatedPort = _AcosNatServerTranslatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 1, 1, 3),
    _AcosNatServerTranslatedPort_Type()
)
acosNatServerTranslatedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosNatServerTranslatedPort.setStatus("mandatory")
_AcosNatServerStandardPort_Type = Integer32
_AcosNatServerStandardPort_Object = MibTableColumn
acosNatServerStandardPort = _AcosNatServerStandardPort_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 1, 1, 4),
    _AcosNatServerStandardPort_Type()
)
acosNatServerStandardPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosNatServerStandardPort.setStatus("mandatory")


class _AcosNatServerProtocol_Type(Integer32):
    """Custom type acosNatServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_AcosNatServerProtocol_Type.__name__ = "Integer32"
_AcosNatServerProtocol_Object = MibTableColumn
acosNatServerProtocol = _AcosNatServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 1, 1, 5),
    _AcosNatServerProtocol_Type()
)
acosNatServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosNatServerProtocol.setStatus("mandatory")
_AcosNatDeviceParameterTable_Object = MibTable
acosNatDeviceParameterTable = _AcosNatDeviceParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 2)
)
if mibBuilder.loadTexts:
    acosNatDeviceParameterTable.setStatus("mandatory")
_AcosNatDeviceParameterEntry_Object = MibTableRow
acosNatDeviceParameterEntry = _AcosNatDeviceParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 2, 1)
)
acosNatDeviceParameterEntry.setIndexNames(
    (0, "ACOS-MIB", "acosNatDeviceSlotIndex"),
    (0, "ACOS-MIB", "acosNatDeviceInterfaceIndex"),
    (0, "ACOS-MIB", "acosNatDevicePortIndex"),
)
if mibBuilder.loadTexts:
    acosNatDeviceParameterEntry.setStatus("mandatory")
_AcosNatDeviceSlotIndex_Type = Integer32
_AcosNatDeviceSlotIndex_Object = MibTableColumn
acosNatDeviceSlotIndex = _AcosNatDeviceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 2, 1, 1),
    _AcosNatDeviceSlotIndex_Type()
)
acosNatDeviceSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosNatDeviceSlotIndex.setStatus("mandatory")
_AcosNatDeviceInterfaceIndex_Type = Integer32
_AcosNatDeviceInterfaceIndex_Object = MibTableColumn
acosNatDeviceInterfaceIndex = _AcosNatDeviceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 2, 1, 2),
    _AcosNatDeviceInterfaceIndex_Type()
)
acosNatDeviceInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosNatDeviceInterfaceIndex.setStatus("mandatory")
_AcosNatDevicePortIndex_Type = Integer32
_AcosNatDevicePortIndex_Object = MibTableColumn
acosNatDevicePortIndex = _AcosNatDevicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 2, 1, 3),
    _AcosNatDevicePortIndex_Type()
)
acosNatDevicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acosNatDevicePortIndex.setStatus("mandatory")


class _AcosNatDeviceTranslationEnabled_Type(Integer32):
    """Custom type acosNatDeviceTranslationEnabled based on Integer32"""
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


_AcosNatDeviceTranslationEnabled_Type.__name__ = "Integer32"
_AcosNatDeviceTranslationEnabled_Object = MibTableColumn
acosNatDeviceTranslationEnabled = _AcosNatDeviceTranslationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 2, 1, 4),
    _AcosNatDeviceTranslationEnabled_Type()
)
acosNatDeviceTranslationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosNatDeviceTranslationEnabled.setStatus("mandatory")
_AcosNatTcpTimeout_Type = TimeTicks
_AcosNatTcpTimeout_Object = MibScalar
acosNatTcpTimeout = _AcosNatTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 3),
    _AcosNatTcpTimeout_Type()
)
acosNatTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosNatTcpTimeout.setStatus("mandatory")
_AcosNatUdpTimeout_Type = TimeTicks
_AcosNatUdpTimeout_Object = MibScalar
acosNatUdpTimeout = _AcosNatUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 4),
    _AcosNatUdpTimeout_Type()
)
acosNatUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosNatUdpTimeout.setStatus("mandatory")
_AcosNatPortLow_Type = Integer32
_AcosNatPortLow_Object = MibScalar
acosNatPortLow = _AcosNatPortLow_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 5),
    _AcosNatPortLow_Type()
)
acosNatPortLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosNatPortLow.setStatus("mandatory")
_AcosNatPortHigh_Type = Integer32
_AcosNatPortHigh_Object = MibScalar
acosNatPortHigh = _AcosNatPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 15, 6),
    _AcosNatPortHigh_Type()
)
acosNatPortHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acosNatPortHigh.setStatus("mandatory")

# Managed Objects groups


# Notification objects

acosCardInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 0, 1)
)
acosCardInsertedTrap.setObjects(
      *(("ACOS-MIB", "acosDeviceSlotIndex"),
        ("ACOS-MIB", "acosDeviceType"))
)
if mibBuilder.loadTexts:
    acosCardInsertedTrap.setStatus(
        ""
    )

acosCardRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 0, 2)
)
acosCardRemovedTrap.setObjects(
      *(("ACOS-MIB", "acosDeviceSlotIndex"),
        ("ACOS-MIB", "acosDeviceType"))
)
if mibBuilder.loadTexts:
    acosCardRemovedTrap.setStatus(
        ""
    )

acosTftpInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 0, 3)
)
acosTftpInitiatedTrap.setObjects(
      *(("ACOS-MIB", "acosTftpFileName"),
        ("ACOS-MIB", "acosTftpServerAddress"))
)
if mibBuilder.loadTexts:
    acosTftpInitiatedTrap.setStatus(
        ""
    )

acosTftpFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 0, 4)
)
acosTftpFailedTrap.setObjects(
      *(("ACOS-MIB", "acosTftpFileName"),
        ("ACOS-MIB", "acosTftpServerAddress"),
        ("ACOS-MIB", "acosTftpFailReason"))
)
if mibBuilder.loadTexts:
    acosTftpFailedTrap.setStatus(
        ""
    )

acosTftpSucceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2221, 1, 1, 0, 5)
)
acosTftpSucceededTrap.setObjects(
      *(("ACOS-MIB", "acosTftpFileName"),
        ("ACOS-MIB", "acosTftpServerAddress"))
)
if mibBuilder.loadTexts:
    acosTftpSucceededTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACOS-MIB",
    **{"AcosDeviceTypeEnum": AcosDeviceTypeEnum,
       "atlasComEngines": atlasComEngines,
       "aceProductFamily": aceProductFamily,
       "aceAcos": aceAcos,
       "acosCardInsertedTrap": acosCardInsertedTrap,
       "acosCardRemovedTrap": acosCardRemovedTrap,
       "acosTftpInitiatedTrap": acosTftpInitiatedTrap,
       "acosTftpFailedTrap": acosTftpFailedTrap,
       "acosTftpSucceededTrap": acosTftpSucceededTrap,
       "acosSystem": acosSystem,
       "acosSystemReboot": acosSystemReboot,
       "acosHardwareRevision": acosHardwareRevision,
       "acosSoftwareRevision": acosSoftwareRevision,
       "acosSerialNumber": acosSerialNumber,
       "acosPartNumber": acosPartNumber,
       "acosTotalSlots": acosTotalSlots,
       "acosMemoryCapacityTable": acosMemoryCapacityTable,
       "acosMemoryCapacityEntry": acosMemoryCapacityEntry,
       "acosMemoryTypeIndex": acosMemoryTypeIndex,
       "acosMemoryCapacity": acosMemoryCapacity,
       "acosDSPCount": acosDSPCount,
       "acosDevices": acosDevices,
       "acosDeviceTable": acosDeviceTable,
       "acosDeviceEntry": acosDeviceEntry,
       "acosDeviceSlotIndex": acosDeviceSlotIndex,
       "acosDeviceType": acosDeviceType,
       "acosDeviceTotal": acosDeviceTotal,
       "acosDeviceDescription": acosDeviceDescription,
       "acosDeviceTypesAggregate": acosDeviceTypesAggregate,
       "acosDeviceTotalsAggregate": acosDeviceTotalsAggregate,
       "acosStatus": acosStatus,
       "acosCpuUtilization": acosCpuUtilization,
       "acosDS1": acosDS1,
       "acosT1LineConfigTable": acosT1LineConfigTable,
       "acosT1LineConfigEntry": acosT1LineConfigEntry,
       "acosT1LineSlotIndex": acosT1LineSlotIndex,
       "acosT1LineSlotInterfaceIndex": acosT1LineSlotInterfaceIndex,
       "acosT1LineBuildOut": acosT1LineBuildOut,
       "acosDS1ChannelConfigTable": acosDS1ChannelConfigTable,
       "acosDS1ChannelConfigEntry": acosDS1ChannelConfigEntry,
       "acosDS1ChannelSlotIndex": acosDS1ChannelSlotIndex,
       "acosDS1ChannelSlotDeviceIndex": acosDS1ChannelSlotDeviceIndex,
       "acosDS1ChannelIndex": acosDS1ChannelIndex,
       "acosDS1TxChannelControl": acosDS1TxChannelControl,
       "acosDS1RxChannelControl": acosDS1RxChannelControl,
       "acosDS1AggChanConfigTable": acosDS1AggChanConfigTable,
       "acosDS1AggChanConfigEntry": acosDS1AggChanConfigEntry,
       "acosDS1AggChanSlotIndex": acosDS1AggChanSlotIndex,
       "acosDS1AggChanSlotDeviceIndex": acosDS1AggChanSlotDeviceIndex,
       "acosDS1TxChannelsAggregate": acosDS1TxChannelsAggregate,
       "acosDS1RxChannelsAggregate": acosDS1RxChannelsAggregate,
       "acosUSI": acosUSI,
       "acosUSIConfigTable": acosUSIConfigTable,
       "acosUSIConfigEntry": acosUSIConfigEntry,
       "acosUSISlotIndex": acosUSISlotIndex,
       "acosUSISlotInterfaceIndex": acosUSISlotInterfaceIndex,
       "acosUSIInterfaceType": acosUSIInterfaceType,
       "acosSDSL": acosSDSL,
       "acosSDSLConfigTable": acosSDSLConfigTable,
       "acosSDSLConfigEntry": acosSDSLConfigEntry,
       "acosSDSLSlotIndex": acosSDSLSlotIndex,
       "acosSDSLSlotInterfaceIndex": acosSDSLSlotInterfaceIndex,
       "acosSDSLInterfaceType": acosSDSLInterfaceType,
       "acosSDSLClockType": acosSDSLClockType,
       "acosEthernet": acosEthernet,
       "acosEthernetConfigTable": acosEthernetConfigTable,
       "acosEthernetConfigEntry": acosEthernetConfigEntry,
       "acosEthernetSlotIndex": acosEthernetSlotIndex,
       "acosEthernetFullDuplex": acosEthernetFullDuplex,
       "acosWAN": acosWAN,
       "acosWANConfigTable": acosWANConfigTable,
       "acosWANConfigEntry": acosWANConfigEntry,
       "acosWANSlotIndex": acosWANSlotIndex,
       "acosWANSlotDeviceIndex": acosWANSlotDeviceIndex,
       "acosWANDataLinkProtocol": acosWANDataLinkProtocol,
       "acosWANSpeed": acosWANSpeed,
       "acosWANSerialStatsTable": acosWANSerialStatsTable,
       "acosWANSerialStatsEntry": acosWANSerialStatsEntry,
       "acosWANSerialStatsSlotIndex": acosWANSerialStatsSlotIndex,
       "acosWANSerialStatsSlotDeviceIndex": acosWANSerialStatsSlotDeviceIndex,
       "acosWANTotalRxFrames": acosWANTotalRxFrames,
       "acosWANTotalRxOctets": acosWANTotalRxOctets,
       "acosWANRxMissedFrames": acosWANRxMissedFrames,
       "acosWANRxErrorFrames": acosWANRxErrorFrames,
       "acosWANRxGlitchErrors": acosWANRxGlitchErrors,
       "acosWANRxPllErrors": acosWANRxPllErrors,
       "acosWANRxLongErrors": acosWANRxLongErrors,
       "acosWANRxNonOctetErrors": acosWANRxNonOctetErrors,
       "acosWANRxAbortErrors": acosWANRxAbortErrors,
       "acosWANRxCrcErrors": acosWANRxCrcErrors,
       "acosWANRxOverrunErrors": acosWANRxOverrunErrors,
       "acosWANRxCdLostErrors": acosWANRxCdLostErrors,
       "acosWANTotalTxFrames": acosWANTotalTxFrames,
       "acosWANTotalTxOctets": acosWANTotalTxOctets,
       "acosWANTxMissedFrames": acosWANTxMissedFrames,
       "acosWANTxDiscardedFrames": acosWANTxDiscardedFrames,
       "acosWANTxErrorFrames": acosWANTxErrorFrames,
       "acosWANTxGlitchErrors": acosWANTxGlitchErrors,
       "acosWANTxUnderrunErrors": acosWANTxUnderrunErrors,
       "acosWANTxCtsLostErrors": acosWANTxCtsLostErrors,
       "acosWANAtmStatsTable": acosWANAtmStatsTable,
       "acosWANAtmStatsEntry": acosWANAtmStatsEntry,
       "acosWANAtmStatsSlotIndex": acosWANAtmStatsSlotIndex,
       "acosWANAtmStatsSlotDeviceIndex": acosWANAtmStatsSlotDeviceIndex,
       "acosWANAtmTotalRxCells": acosWANAtmTotalRxCells,
       "acosWANAtmClpiRxCells": acosWANAtmClpiRxCells,
       "acosWANAtmOamRxCells": acosWANAtmOamRxCells,
       "acosWANAtmEfciRxCells": acosWANAtmEfciRxCells,
       "acosWANAtmRmRxCells": acosWANAtmRmRxCells,
       "acosWANAtmRxCellsDiscarded": acosWANAtmRxCellsDiscarded,
       "acosWANAtmTotalTxCells": acosWANAtmTotalTxCells,
       "acosWANAtmOamTxCells": acosWANAtmOamTxCells,
       "acosWANAtmClpiTxCells": acosWANAtmClpiTxCells,
       "acosWANAtmEfciTxCells": acosWANAtmEfciTxCells,
       "acosWANAtmRmTxCells": acosWANAtmRmTxCells,
       "acosWANAtmRxHecErrors": acosWANAtmRxHecErrors,
       "acosWANAtmPortStatus": acosWANAtmPortStatus,
       "acosRouting": acosRouting,
       "acosDeviceIpAddressTable": acosDeviceIpAddressTable,
       "acosDeviceIpAddressEntry": acosDeviceIpAddressEntry,
       "acosDeviceIpSlotIndex": acosDeviceIpSlotIndex,
       "acosDeviceIpInterfaceIndex": acosDeviceIpInterfaceIndex,
       "acosDeviceIpPortIndex": acosDeviceIpPortIndex,
       "acosDeviceIpConnectionIndex": acosDeviceIpConnectionIndex,
       "acosDeviceIpAddress": acosDeviceIpAddress,
       "acosDeviceIpAddressSubnetMask": acosDeviceIpAddressSubnetMask,
       "acosDeviceIpPeerAddress": acosDeviceIpPeerAddress,
       "acosRIPControl": acosRIPControl,
       "acosDeviceRipParameterTable": acosDeviceRipParameterTable,
       "acosDeviceRipParameterEntry": acosDeviceRipParameterEntry,
       "acosDeviceRipSlotIndex": acosDeviceRipSlotIndex,
       "acosDeviceRipInterfaceIndex": acosDeviceRipInterfaceIndex,
       "acosDeviceRipPortIndex": acosDeviceRipPortIndex,
       "acosDeviceRipVersion": acosDeviceRipVersion,
       "acosDeviceRipPoisonedReverse": acosDeviceRipPoisonedReverse,
       "acosDNSServerAddress": acosDNSServerAddress,
       "acosDNSTimeout": acosDNSTimeout,
       "acosBridge": acosBridge,
       "acosBridging": acosBridging,
       "acosBridgeTable": acosBridgeTable,
       "acosBridgeEntry": acosBridgeEntry,
       "acosBridgeSlotIndex": acosBridgeSlotIndex,
       "acosBridgeInterfaceIndex": acosBridgeInterfaceIndex,
       "acosBridgePortIndex": acosBridgePortIndex,
       "acosBridgeControl": acosBridgeControl,
       "acosTftpClient": acosTftpClient,
       "acosTftpServerAddress": acosTftpServerAddress,
       "acosTftpAcosName": acosTftpAcosName,
       "acosTftpUpgradeACOS": acosTftpUpgradeACOS,
       "acosTftpApplicationName": acosTftpApplicationName,
       "acosTftpUpgradeApplication": acosTftpUpgradeApplication,
       "acosTftpSessionStatus": acosTftpSessionStatus,
       "acosTftpFailReason": acosTftpFailReason,
       "acosTftpOctetsRead": acosTftpOctetsRead,
       "acosManagement": acosManagement,
       "acosManagerIpAddress": acosManagerIpAddress,
       "acosManagerWriteCommunity": acosManagerWriteCommunity,
       "acosTrapObjects": acosTrapObjects,
       "acosTftpFileName": acosTftpFileName,
       "acosDhcp": acosDhcp,
       "acosDhcpEnable": acosDhcpEnable,
       "acosDhcpGateway": acosDhcpGateway,
       "acosDhcpDnsServer": acosDhcpDnsServer,
       "acosDhcpSubnet": acosDhcpSubnet,
       "acosDhcpLowAddress": acosDhcpLowAddress,
       "acosDhcpHighAddress": acosDhcpHighAddress,
       "acosDhcpLeaseTime": acosDhcpLeaseTime,
       "acosDhcpDomainName": acosDhcpDomainName,
       "acosDhcpInterface": acosDhcpInterface,
       "acosDhcpClientTable": acosDhcpClientTable,
       "acosDhcpClientEntry": acosDhcpClientEntry,
       "acosDhcpClientIndex": acosDhcpClientIndex,
       "acosDhcpClientIpAddress": acosDhcpClientIpAddress,
       "acosDhcpClientMacAddress": acosDhcpClientMacAddress,
       "acosDhcpClientName": acosDhcpClientName,
       "acosDhcpClientLeaseTime": acosDhcpClientLeaseTime,
       "acosDhcpClientSubnetMask": acosDhcpClientSubnetMask,
       "acosDhcpClientGateway": acosDhcpClientGateway,
       "acosDhcpClientDnsServer": acosDhcpClientDnsServer,
       "acosNat": acosNat,
       "acosNatServerTable": acosNatServerTable,
       "acosNatServerEntry": acosNatServerEntry,
       "acosNatServerIndex": acosNatServerIndex,
       "acosNatServerTranslatedIpAddress": acosNatServerTranslatedIpAddress,
       "acosNatServerTranslatedPort": acosNatServerTranslatedPort,
       "acosNatServerStandardPort": acosNatServerStandardPort,
       "acosNatServerProtocol": acosNatServerProtocol,
       "acosNatDeviceParameterTable": acosNatDeviceParameterTable,
       "acosNatDeviceParameterEntry": acosNatDeviceParameterEntry,
       "acosNatDeviceSlotIndex": acosNatDeviceSlotIndex,
       "acosNatDeviceInterfaceIndex": acosNatDeviceInterfaceIndex,
       "acosNatDevicePortIndex": acosNatDevicePortIndex,
       "acosNatDeviceTranslationEnabled": acosNatDeviceTranslationEnabled,
       "acosNatTcpTimeout": acosNatTcpTimeout,
       "acosNatUdpTimeout": acosNatUdpTimeout,
       "acosNatPortLow": acosNatPortLow,
       "acosNatPortHigh": acosNatPortHigh}
)
