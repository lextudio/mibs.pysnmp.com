# SNMP MIB module (METRO1500-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/METRO1500-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:19 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Adva_ObjectIdentity = ObjectIdentity
adva = _Adva_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544)
)
_AdvaProducts_ObjectIdentity = ObjectIdentity
advaProducts = _AdvaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1)
)
_Metro1500_ObjectIdentity = ObjectIdentity
metro1500 = _Metro1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3)
)
_Metro1500Main_ObjectIdentity = ObjectIdentity
metro1500Main = _Metro1500Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1)
)
_Metro1500Housing_ObjectIdentity = ObjectIdentity
metro1500Housing = _Metro1500Housing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1)
)
_Metro1500Manufacturer_Type = DisplayString
_Metro1500Manufacturer_Object = MibScalar
metro1500Manufacturer = _Metro1500Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 1),
    _Metro1500Manufacturer_Type()
)
metro1500Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500Manufacturer.setStatus("mandatory")
_Metro1500MainType_Type = DisplayString
_Metro1500MainType_Object = MibScalar
metro1500MainType = _Metro1500MainType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 2),
    _Metro1500MainType_Type()
)
metro1500MainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainType.setStatus("mandatory")
_Metro1500MainSerialNumber_Type = DisplayString
_Metro1500MainSerialNumber_Object = MibScalar
metro1500MainSerialNumber = _Metro1500MainSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 3),
    _Metro1500MainSerialNumber_Type()
)
metro1500MainSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainSerialNumber.setStatus("mandatory")
_Metro1500MainHardwareVersion_Type = DisplayString
_Metro1500MainHardwareVersion_Object = MibScalar
metro1500MainHardwareVersion = _Metro1500MainHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 4),
    _Metro1500MainHardwareVersion_Type()
)
metro1500MainHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainHardwareVersion.setStatus("mandatory")
_Metro1500MainSoftwareVersion_Type = DisplayString
_Metro1500MainSoftwareVersion_Object = MibScalar
metro1500MainSoftwareVersion = _Metro1500MainSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 5),
    _Metro1500MainSoftwareVersion_Type()
)
metro1500MainSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainSoftwareVersion.setStatus("mandatory")
_Metro1500MainBusMessages_Type = Integer32
_Metro1500MainBusMessages_Object = MibScalar
metro1500MainBusMessages = _Metro1500MainBusMessages_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 6),
    _Metro1500MainBusMessages_Type()
)
metro1500MainBusMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainBusMessages.setStatus("mandatory")
_Metro1500MainBusErrors_Type = Integer32
_Metro1500MainBusErrors_Object = MibScalar
metro1500MainBusErrors = _Metro1500MainBusErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 7),
    _Metro1500MainBusErrors_Type()
)
metro1500MainBusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainBusErrors.setStatus("mandatory")


class _Metro1500MainLastEvent_Type(Integer32):
    """Custom type metro1500MainLastEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Metro1500MainLastEvent_Type.__name__ = "Integer32"
_Metro1500MainLastEvent_Object = MibScalar
metro1500MainLastEvent = _Metro1500MainLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 8),
    _Metro1500MainLastEvent_Type()
)
metro1500MainLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLastEvent.setStatus("mandatory")
_Metro1500MainMotd_Type = DisplayString
_Metro1500MainMotd_Object = MibScalar
metro1500MainMotd = _Metro1500MainMotd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 9),
    _Metro1500MainMotd_Type()
)
metro1500MainMotd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainMotd.setStatus("mandatory")
_Metro1500MainTrapsinkTable_Object = MibTable
metro1500MainTrapsinkTable = _Metro1500MainTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    metro1500MainTrapsinkTable.setStatus("mandatory")
_Metro1500MainTrapsinkEntry_Object = MibTableRow
metro1500MainTrapsinkEntry = _Metro1500MainTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1)
)
metro1500MainTrapsinkEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500MainTrapsinkNumber"),
)
if mibBuilder.loadTexts:
    metro1500MainTrapsinkEntry.setStatus("mandatory")


class _Metro1500MainTrapsinkNumber_Type(Integer32):
    """Custom type metro1500MainTrapsinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Metro1500MainTrapsinkNumber_Type.__name__ = "Integer32"
_Metro1500MainTrapsinkNumber_Object = MibTableColumn
metro1500MainTrapsinkNumber = _Metro1500MainTrapsinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 1),
    _Metro1500MainTrapsinkNumber_Type()
)
metro1500MainTrapsinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainTrapsinkNumber.setStatus("mandatory")
_Metro1500MainTrapsinkAddress_Type = DisplayString
_Metro1500MainTrapsinkAddress_Object = MibTableColumn
metro1500MainTrapsinkAddress = _Metro1500MainTrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 2),
    _Metro1500MainTrapsinkAddress_Type()
)
metro1500MainTrapsinkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainTrapsinkAddress.setStatus("mandatory")
_Metro1500MainTrapsinkCommunity_Type = DisplayString
_Metro1500MainTrapsinkCommunity_Object = MibTableColumn
metro1500MainTrapsinkCommunity = _Metro1500MainTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 3),
    _Metro1500MainTrapsinkCommunity_Type()
)
metro1500MainTrapsinkCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainTrapsinkCommunity.setStatus("mandatory")


class _Metro1500MainTrapsinkPriority_Type(Integer32):
    """Custom type metro1500MainTrapsinkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Metro1500MainTrapsinkPriority_Type.__name__ = "Integer32"
_Metro1500MainTrapsinkPriority_Object = MibTableColumn
metro1500MainTrapsinkPriority = _Metro1500MainTrapsinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 10, 1, 4),
    _Metro1500MainTrapsinkPriority_Type()
)
metro1500MainTrapsinkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainTrapsinkPriority.setStatus("mandatory")
_Metro1500MainLogfileTable_Object = MibTable
metro1500MainLogfileTable = _Metro1500MainLogfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    metro1500MainLogfileTable.setStatus("mandatory")
_Metro1500MainLogfileEntry_Object = MibTableRow
metro1500MainLogfileEntry = _Metro1500MainLogfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1)
)
metro1500MainLogfileEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500MainLogfileNumber"),
)
if mibBuilder.loadTexts:
    metro1500MainLogfileEntry.setStatus("mandatory")


class _Metro1500MainLogfileNumber_Type(Integer32):
    """Custom type metro1500MainLogfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Metro1500MainLogfileNumber_Type.__name__ = "Integer32"
_Metro1500MainLogfileNumber_Object = MibTableColumn
metro1500MainLogfileNumber = _Metro1500MainLogfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 1),
    _Metro1500MainLogfileNumber_Type()
)
metro1500MainLogfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLogfileNumber.setStatus("mandatory")
_Metro1500MainLogfileName_Type = DisplayString
_Metro1500MainLogfileName_Object = MibTableColumn
metro1500MainLogfileName = _Metro1500MainLogfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 2),
    _Metro1500MainLogfileName_Type()
)
metro1500MainLogfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLogfileName.setStatus("mandatory")
_Metro1500MainLogfileSize_Type = Integer32
_Metro1500MainLogfileSize_Object = MibTableColumn
metro1500MainLogfileSize = _Metro1500MainLogfileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 3),
    _Metro1500MainLogfileSize_Type()
)
metro1500MainLogfileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLogfileSize.setStatus("mandatory")


class _Metro1500MainLogfilePriority_Type(Integer32):
    """Custom type metro1500MainLogfilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Metro1500MainLogfilePriority_Type.__name__ = "Integer32"
_Metro1500MainLogfilePriority_Object = MibTableColumn
metro1500MainLogfilePriority = _Metro1500MainLogfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 1, 11, 1, 4),
    _Metro1500MainLogfilePriority_Type()
)
metro1500MainLogfilePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500MainLogfilePriority.setStatus("mandatory")
_Metro1500SlotTable_Object = MibTable
metro1500SlotTable = _Metro1500SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    metro1500SlotTable.setStatus("mandatory")
_Metro1500SlotEntry_Object = MibTableRow
metro1500SlotEntry = _Metro1500SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1)
)
metro1500SlotEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500SlotNumber"),
)
if mibBuilder.loadTexts:
    metro1500SlotEntry.setStatus("mandatory")


class _Metro1500SlotNumber_Type(Integer32):
    """Custom type metro1500SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 79),
    )


_Metro1500SlotNumber_Type.__name__ = "Integer32"
_Metro1500SlotNumber_Object = MibTableColumn
metro1500SlotNumber = _Metro1500SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 1),
    _Metro1500SlotNumber_Type()
)
metro1500SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SlotNumber.setStatus("mandatory")
_Metro1500Type_Type = DisplayString
_Metro1500Type_Object = MibTableColumn
metro1500Type = _Metro1500Type_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 2),
    _Metro1500Type_Type()
)
metro1500Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500Type.setStatus("mandatory")


class _Metro1500SlotTypeNumber_Type(Integer32):
    """Custom type metro1500SlotTypeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              10,
              32,
              33,
              39,
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("demi", 33),
          ("metro1000Converter", 2),
          ("metro1000EthernetConverter", 3),
          ("metro1500-2-5GbConverter", 5),
          ("metro1500-4PortTDMCard", 10),
          ("metro1500-EthernetHubCard", 39),
          ("metro1500-TRL-Converter", 7),
          ("metro1500Converter", 1),
          ("nemi", 32),
          ("other", 255),
          ("switch", 64))
    )


_Metro1500SlotTypeNumber_Type.__name__ = "Integer32"
_Metro1500SlotTypeNumber_Object = MibTableColumn
metro1500SlotTypeNumber = _Metro1500SlotTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 3),
    _Metro1500SlotTypeNumber_Type()
)
metro1500SlotTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SlotTypeNumber.setStatus("mandatory")
_Metro1500SerialNumber_Type = DisplayString
_Metro1500SerialNumber_Object = MibTableColumn
metro1500SerialNumber = _Metro1500SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 4),
    _Metro1500SerialNumber_Type()
)
metro1500SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SerialNumber.setStatus("mandatory")
_Metro1500HardwareVersion_Type = DisplayString
_Metro1500HardwareVersion_Object = MibTableColumn
metro1500HardwareVersion = _Metro1500HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 5),
    _Metro1500HardwareVersion_Type()
)
metro1500HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500HardwareVersion.setStatus("mandatory")
_Metro1500SoftwareVersion_Type = DisplayString
_Metro1500SoftwareVersion_Object = MibTableColumn
metro1500SoftwareVersion = _Metro1500SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 6),
    _Metro1500SoftwareVersion_Type()
)
metro1500SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SoftwareVersion.setStatus("mandatory")
_Metro1500Temperature_Type = Integer32
_Metro1500Temperature_Object = MibTableColumn
metro1500Temperature = _Metro1500Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 7),
    _Metro1500Temperature_Type()
)
metro1500Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500Temperature.setStatus("mandatory")
_Metro1500BoardVoltage_Type = Integer32
_Metro1500BoardVoltage_Object = MibTableColumn
metro1500BoardVoltage = _Metro1500BoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 8),
    _Metro1500BoardVoltage_Type()
)
metro1500BoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500BoardVoltage.setStatus("mandatory")
_Metro1500DetailInfo_Type = ObjectIdentifier
_Metro1500DetailInfo_Object = MibTableColumn
metro1500DetailInfo = _Metro1500DetailInfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 9),
    _Metro1500DetailInfo_Type()
)
metro1500DetailInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500DetailInfo.setStatus("mandatory")


class _Metro1500EPLDVersion_Type(Integer32):
    """Custom type metro1500EPLDVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Metro1500EPLDVersion_Type.__name__ = "Integer32"
_Metro1500EPLDVersion_Object = MibTableColumn
metro1500EPLDVersion = _Metro1500EPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 2, 1, 10),
    _Metro1500EPLDVersion_Type()
)
metro1500EPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EPLDVersion.setStatus("mandatory")
_Metro1500PSTable_Object = MibTable
metro1500PSTable = _Metro1500PSTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    metro1500PSTable.setStatus("mandatory")
_Metro1500PSEntry_Object = MibTableRow
metro1500PSEntry = _Metro1500PSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1)
)
metro1500PSEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500PSNumber"),
)
if mibBuilder.loadTexts:
    metro1500PSEntry.setStatus("mandatory")


class _Metro1500PSNumber_Type(Integer32):
    """Custom type metro1500PSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Metro1500PSNumber_Type.__name__ = "Integer32"
_Metro1500PSNumber_Object = MibTableColumn
metro1500PSNumber = _Metro1500PSNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1, 1),
    _Metro1500PSNumber_Type()
)
metro1500PSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500PSNumber.setStatus("mandatory")


class _Metro1500PSOn_Type(Integer32):
    """Custom type metro1500PSOn based on Integer32"""
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


_Metro1500PSOn_Type.__name__ = "Integer32"
_Metro1500PSOn_Object = MibTableColumn
metro1500PSOn = _Metro1500PSOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 3, 1, 2),
    _Metro1500PSOn_Type()
)
metro1500PSOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500PSOn.setStatus("mandatory")
_Metro1500FanTable_Object = MibTable
metro1500FanTable = _Metro1500FanTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    metro1500FanTable.setStatus("mandatory")
_Metro1500FanEntry_Object = MibTableRow
metro1500FanEntry = _Metro1500FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1)
)
metro1500FanEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500FanNumber"),
)
if mibBuilder.loadTexts:
    metro1500FanEntry.setStatus("mandatory")


class _Metro1500FanNumber_Type(Integer32):
    """Custom type metro1500FanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Metro1500FanNumber_Type.__name__ = "Integer32"
_Metro1500FanNumber_Object = MibTableColumn
metro1500FanNumber = _Metro1500FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1, 1),
    _Metro1500FanNumber_Type()
)
metro1500FanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500FanNumber.setStatus("mandatory")


class _Metro1500FanOn_Type(Integer32):
    """Custom type metro1500FanOn based on Integer32"""
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


_Metro1500FanOn_Type.__name__ = "Integer32"
_Metro1500FanOn_Object = MibTableColumn
metro1500FanOn = _Metro1500FanOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 1, 4, 1, 2),
    _Metro1500FanOn_Type()
)
metro1500FanOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500FanOn.setStatus("mandatory")
_Metro1500Converter_ObjectIdentity = ObjectIdentity
metro1500Converter = _Metro1500Converter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5)
)
_Metro1500ConverterTable_Object = MibTable
metro1500ConverterTable = _Metro1500ConverterTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    metro1500ConverterTable.setStatus("mandatory")
_Metro1500ConverterEntry_Object = MibTableRow
metro1500ConverterEntry = _Metro1500ConverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1)
)
metro1500ConverterEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500ConverterNumber"),
)
if mibBuilder.loadTexts:
    metro1500ConverterEntry.setStatus("mandatory")


class _Metro1500ConverterNumber_Type(Integer32):
    """Custom type metro1500ConverterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 79),
    )


_Metro1500ConverterNumber_Type.__name__ = "Integer32"
_Metro1500ConverterNumber_Object = MibTableColumn
metro1500ConverterNumber = _Metro1500ConverterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 1),
    _Metro1500ConverterNumber_Type()
)
metro1500ConverterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ConverterNumber.setStatus("mandatory")


class _Metro1500RxLoc_Type(Integer32):
    """Custom type metro1500RxLoc based on Integer32"""
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


_Metro1500RxLoc_Type.__name__ = "Integer32"
_Metro1500RxLoc_Object = MibTableColumn
metro1500RxLoc = _Metro1500RxLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 2),
    _Metro1500RxLoc_Type()
)
metro1500RxLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RxLoc.setStatus("mandatory")


class _Metro1500TxLoc_Type(Integer32):
    """Custom type metro1500TxLoc based on Integer32"""
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
        *(("alwaysOff", 4),
          ("alwaysOn", 3),
          ("off", 2),
          ("on", 1))
    )


_Metro1500TxLoc_Type.__name__ = "Integer32"
_Metro1500TxLoc_Object = MibTableColumn
metro1500TxLoc = _Metro1500TxLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 3),
    _Metro1500TxLoc_Type()
)
metro1500TxLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxLoc.setStatus("mandatory")


class _Metro1500TxLocC_Type(Integer32):
    """Custom type metro1500TxLocC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Metro1500TxLocC_Type.__name__ = "Integer32"
_Metro1500TxLocC_Object = MibTableColumn
metro1500TxLocC = _Metro1500TxLocC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 4),
    _Metro1500TxLocC_Type()
)
metro1500TxLocC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxLocC.setStatus("mandatory")


class _Metro1500TxLocTemp_Type(Integer32):
    """Custom type metro1500TxLocTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Metro1500TxLocTemp_Type.__name__ = "Integer32"
_Metro1500TxLocTemp_Object = MibTableColumn
metro1500TxLocTemp = _Metro1500TxLocTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 5),
    _Metro1500TxLocTemp_Type()
)
metro1500TxLocTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxLocTemp.setStatus("mandatory")


class _Metro1500RxRem_Type(Integer32):
    """Custom type metro1500RxRem based on Integer32"""
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


_Metro1500RxRem_Type.__name__ = "Integer32"
_Metro1500RxRem_Object = MibTableColumn
metro1500RxRem = _Metro1500RxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 6),
    _Metro1500RxRem_Type()
)
metro1500RxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RxRem.setStatus("mandatory")


class _Metro1500TxRem_Type(Integer32):
    """Custom type metro1500TxRem based on Integer32"""
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
        *(("alwaysOff", 4),
          ("alwaysOn", 3),
          ("off", 2),
          ("on", 1))
    )


_Metro1500TxRem_Type.__name__ = "Integer32"
_Metro1500TxRem_Object = MibTableColumn
metro1500TxRem = _Metro1500TxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 7),
    _Metro1500TxRem_Type()
)
metro1500TxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxRem.setStatus("mandatory")


class _Metro1500TxRemC_Type(Integer32):
    """Custom type metro1500TxRemC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Metro1500TxRemC_Type.__name__ = "Integer32"
_Metro1500TxRemC_Object = MibTableColumn
metro1500TxRemC = _Metro1500TxRemC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 8),
    _Metro1500TxRemC_Type()
)
metro1500TxRemC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxRemC.setStatus("mandatory")


class _Metro1500TxRemTemp_Type(Integer32):
    """Custom type metro1500TxRemTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Metro1500TxRemTemp_Type.__name__ = "Integer32"
_Metro1500TxRemTemp_Object = MibTableColumn
metro1500TxRemTemp = _Metro1500TxRemTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 9),
    _Metro1500TxRemTemp_Type()
)
metro1500TxRemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TxRemTemp.setStatus("mandatory")


class _Metro1500RxRem2_Type(Integer32):
    """Custom type metro1500RxRem2 based on Integer32"""
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


_Metro1500RxRem2_Type.__name__ = "Integer32"
_Metro1500RxRem2_Object = MibTableColumn
metro1500RxRem2 = _Metro1500RxRem2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 10),
    _Metro1500RxRem2_Type()
)
metro1500RxRem2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RxRem2.setStatus("mandatory")


class _Metro1500ClockState_Type(Integer32):
    """Custom type metro1500ClockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("off", 2),
          ("on", 1))
    )


_Metro1500ClockState_Type.__name__ = "Integer32"
_Metro1500ClockState_Object = MibTableColumn
metro1500ClockState = _Metro1500ClockState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 11),
    _Metro1500ClockState_Type()
)
metro1500ClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ClockState.setStatus("mandatory")
_Metro1500ClockFreq_Type = Integer32
_Metro1500ClockFreq_Object = MibTableColumn
metro1500ClockFreq = _Metro1500ClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 12),
    _Metro1500ClockFreq_Type()
)
metro1500ClockFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ClockFreq.setStatus("mandatory")


class _Metro1500LocLoop_Type(Integer32):
    """Custom type metro1500LocLoop based on Integer32"""
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


_Metro1500LocLoop_Type.__name__ = "Integer32"
_Metro1500LocLoop_Object = MibTableColumn
metro1500LocLoop = _Metro1500LocLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 13),
    _Metro1500LocLoop_Type()
)
metro1500LocLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500LocLoop.setStatus("mandatory")


class _Metro1500RemLoop_Type(Integer32):
    """Custom type metro1500RemLoop based on Integer32"""
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


_Metro1500RemLoop_Type.__name__ = "Integer32"
_Metro1500RemLoop_Object = MibTableColumn
metro1500RemLoop = _Metro1500RemLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 14),
    _Metro1500RemLoop_Type()
)
metro1500RemLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500RemLoop.setStatus("mandatory")


class _Metro1500ClockType_Type(Integer32):
    """Custom type metro1500ClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              9,
              11,
              21,
              22,
              31,
              32,
              41,
              42,
              51,
              52,
              61,
              62,
              71,
              72,
              75,
              76,
              81,
              82,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fixedClock1062Mbps", 72),
          ("fixedClock1062MbpsModule", 71),
          ("fixedClock1250Mbps", 76),
          ("fixedClock1250MbpsModule", 75),
          ("fixedClock125Mbps", 22),
          ("fixedClock125MbpsModule", 21),
          ("fixedClock155Mbps", 32),
          ("fixedClock155MbpsModule", 31),
          ("fixedClock200Mbps", 42),
          ("fixedClock200MbpsModule", 41),
          ("fixedClock2500Mbps", 82),
          ("fixedClock2500MbpsModule", 81),
          ("fixedClock266Mbps", 52),
          ("fixedClock266MbpsModule", 51),
          ("fixedClock622Mbps", 62),
          ("fixedClock622MbpsModule", 61),
          ("multiClockFCGbE", 3),
          ("multiClockFCGbEOnBoard", 11),
          ("multiClockLS", 2),
          ("multiClockLSModule", 1),
          ("multiClockOCxFC", 7),
          ("multiClockOCxGbE", 5),
          ("multiClockOCxGbEFC", 9),
          ("other", 255))
    )


_Metro1500ClockType_Type.__name__ = "Integer32"
_Metro1500ClockType_Object = MibTableColumn
metro1500ClockType = _Metro1500ClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 5, 1, 1, 15),
    _Metro1500ClockType_Type()
)
metro1500ClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500ClockType.setStatus("mandatory")
_Metro1500Switch_ObjectIdentity = ObjectIdentity
metro1500Switch = _Metro1500Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10)
)
_Metro1500SwitchTable_Object = MibTable
metro1500SwitchTable = _Metro1500SwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    metro1500SwitchTable.setStatus("mandatory")
_Metro1500SwitchEntry_Object = MibTableRow
metro1500SwitchEntry = _Metro1500SwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1)
)
metro1500SwitchEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500SwitchNumber"),
)
if mibBuilder.loadTexts:
    metro1500SwitchEntry.setStatus("mandatory")


class _Metro1500SwitchNumber_Type(Integer32):
    """Custom type metro1500SwitchNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 79),
    )


_Metro1500SwitchNumber_Type.__name__ = "Integer32"
_Metro1500SwitchNumber_Object = MibTableColumn
metro1500SwitchNumber = _Metro1500SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 1),
    _Metro1500SwitchNumber_Type()
)
metro1500SwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchNumber.setStatus("mandatory")


class _Metro1500SwitchLine_Type(Integer32):
    """Custom type metro1500SwitchLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineA", 1),
          ("lineB", 2))
    )


_Metro1500SwitchLine_Type.__name__ = "Integer32"
_Metro1500SwitchLine_Object = MibTableColumn
metro1500SwitchLine = _Metro1500SwitchLine_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 2),
    _Metro1500SwitchLine_Type()
)
metro1500SwitchLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchLine.setStatus("mandatory")


class _Metro1500SwitchMode_Type(Integer32):
    """Custom type metro1500SwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("locked", 2))
    )


_Metro1500SwitchMode_Type.__name__ = "Integer32"
_Metro1500SwitchMode_Object = MibTableColumn
metro1500SwitchMode = _Metro1500SwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 3),
    _Metro1500SwitchMode_Type()
)
metro1500SwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchMode.setStatus("mandatory")


class _Metro1500SwitchLaserOn_Type(Integer32):
    """Custom type metro1500SwitchLaserOn based on Integer32"""
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


_Metro1500SwitchLaserOn_Type.__name__ = "Integer32"
_Metro1500SwitchLaserOn_Object = MibTableColumn
metro1500SwitchLaserOn = _Metro1500SwitchLaserOn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 4),
    _Metro1500SwitchLaserOn_Type()
)
metro1500SwitchLaserOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchLaserOn.setStatus("mandatory")


class _Metro1500SwitchLineAavail_Type(Integer32):
    """Custom type metro1500SwitchLineAavail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_Metro1500SwitchLineAavail_Type.__name__ = "Integer32"
_Metro1500SwitchLineAavail_Object = MibTableColumn
metro1500SwitchLineAavail = _Metro1500SwitchLineAavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 5),
    _Metro1500SwitchLineAavail_Type()
)
metro1500SwitchLineAavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchLineAavail.setStatus("mandatory")


class _Metro1500SwitchLineBavail_Type(Integer32):
    """Custom type metro1500SwitchLineBavail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_Metro1500SwitchLineBavail_Type.__name__ = "Integer32"
_Metro1500SwitchLineBavail_Object = MibTableColumn
metro1500SwitchLineBavail = _Metro1500SwitchLineBavail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 10, 1, 1, 6),
    _Metro1500SwitchLineBavail_Type()
)
metro1500SwitchLineBavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500SwitchLineBavail.setStatus("mandatory")
_Metro1500EthernetHub_ObjectIdentity = ObjectIdentity
metro1500EthernetHub = _Metro1500EthernetHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14)
)
_Metro1500EthernetHubTable_Object = MibTable
metro1500EthernetHubTable = _Metro1500EthernetHubTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1)
)
if mibBuilder.loadTexts:
    metro1500EthernetHubTable.setStatus("mandatory")
_Metro1500EthernetHubEntry_Object = MibTableRow
metro1500EthernetHubEntry = _Metro1500EthernetHubEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1)
)
metro1500EthernetHubEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500EthernetHubNumber"),
)
if mibBuilder.loadTexts:
    metro1500EthernetHubEntry.setStatus("mandatory")


class _Metro1500EthernetHubNumber_Type(Integer32):
    """Custom type metro1500EthernetHubNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 79),
    )


_Metro1500EthernetHubNumber_Type.__name__ = "Integer32"
_Metro1500EthernetHubNumber_Object = MibTableColumn
metro1500EthernetHubNumber = _Metro1500EthernetHubNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 1),
    _Metro1500EthernetHubNumber_Type()
)
metro1500EthernetHubNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubNumber.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable1_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable1 based on Integer32"""
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


_Metro1500EthernetHubPortEnable1_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable1_Object = MibTableColumn
metro1500EthernetHubPortEnable1 = _Metro1500EthernetHubPortEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 10),
    _Metro1500EthernetHubPortEnable1_Type()
)
metro1500EthernetHubPortEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable1.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus1_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPartitioned", 2),
          ("partitioned", 1))
    )


_Metro1500EthernetHubPortPartitionStatus1_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus1_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus1 = _Metro1500EthernetHubPortPartitionStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 11),
    _Metro1500EthernetHubPortPartitionStatus1_Type()
)
metro1500EthernetHubPortPartitionStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus1.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus1_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus1_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus1_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus1 = _Metro1500EthernetHubPortLinkStatus1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 12),
    _Metro1500EthernetHubPortLinkStatus1_Type()
)
metro1500EthernetHubPortLinkStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus1.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity1_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1))
    )


_Metro1500EthernetHubPortPolarity1_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity1_Object = MibTableColumn
metro1500EthernetHubPortPolarity1 = _Metro1500EthernetHubPortPolarity1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 13),
    _Metro1500EthernetHubPortPolarity1_Type()
)
metro1500EthernetHubPortPolarity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity1.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable2_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable2 based on Integer32"""
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


_Metro1500EthernetHubPortEnable2_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable2_Object = MibTableColumn
metro1500EthernetHubPortEnable2 = _Metro1500EthernetHubPortEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 20),
    _Metro1500EthernetHubPortEnable2_Type()
)
metro1500EthernetHubPortEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable2.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus2_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPartitioned", 2),
          ("partitioned", 1))
    )


_Metro1500EthernetHubPortPartitionStatus2_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus2_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus2 = _Metro1500EthernetHubPortPartitionStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 21),
    _Metro1500EthernetHubPortPartitionStatus2_Type()
)
metro1500EthernetHubPortPartitionStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus2.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus2_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus2_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus2_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus2 = _Metro1500EthernetHubPortLinkStatus2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 22),
    _Metro1500EthernetHubPortLinkStatus2_Type()
)
metro1500EthernetHubPortLinkStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus2.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity2_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1))
    )


_Metro1500EthernetHubPortPolarity2_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity2_Object = MibTableColumn
metro1500EthernetHubPortPolarity2 = _Metro1500EthernetHubPortPolarity2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 23),
    _Metro1500EthernetHubPortPolarity2_Type()
)
metro1500EthernetHubPortPolarity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity2.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable3_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable3 based on Integer32"""
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


_Metro1500EthernetHubPortEnable3_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable3_Object = MibTableColumn
metro1500EthernetHubPortEnable3 = _Metro1500EthernetHubPortEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 30),
    _Metro1500EthernetHubPortEnable3_Type()
)
metro1500EthernetHubPortEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable3.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus3_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPartitioned", 2),
          ("partitioned", 1))
    )


_Metro1500EthernetHubPortPartitionStatus3_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus3_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus3 = _Metro1500EthernetHubPortPartitionStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 31),
    _Metro1500EthernetHubPortPartitionStatus3_Type()
)
metro1500EthernetHubPortPartitionStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus3.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus3_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus3_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus3_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus3 = _Metro1500EthernetHubPortLinkStatus3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 32),
    _Metro1500EthernetHubPortLinkStatus3_Type()
)
metro1500EthernetHubPortLinkStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus3.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity3_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1))
    )


_Metro1500EthernetHubPortPolarity3_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity3_Object = MibTableColumn
metro1500EthernetHubPortPolarity3 = _Metro1500EthernetHubPortPolarity3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 33),
    _Metro1500EthernetHubPortPolarity3_Type()
)
metro1500EthernetHubPortPolarity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity3.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable4_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable4 based on Integer32"""
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


_Metro1500EthernetHubPortEnable4_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable4_Object = MibTableColumn
metro1500EthernetHubPortEnable4 = _Metro1500EthernetHubPortEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 40),
    _Metro1500EthernetHubPortEnable4_Type()
)
metro1500EthernetHubPortEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable4.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus4_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPartitioned", 2),
          ("partitioned", 1))
    )


_Metro1500EthernetHubPortPartitionStatus4_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus4_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus4 = _Metro1500EthernetHubPortPartitionStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 41),
    _Metro1500EthernetHubPortPartitionStatus4_Type()
)
metro1500EthernetHubPortPartitionStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus4.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus4_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus4_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus4_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus4 = _Metro1500EthernetHubPortLinkStatus4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 42),
    _Metro1500EthernetHubPortLinkStatus4_Type()
)
metro1500EthernetHubPortLinkStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus4.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity4_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1))
    )


_Metro1500EthernetHubPortPolarity4_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity4_Object = MibTableColumn
metro1500EthernetHubPortPolarity4 = _Metro1500EthernetHubPortPolarity4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 43),
    _Metro1500EthernetHubPortPolarity4_Type()
)
metro1500EthernetHubPortPolarity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity4.setStatus("mandatory")


class _Metro1500EthernetHubPortEnable5_Type(Integer32):
    """Custom type metro1500EthernetHubPortEnable5 based on Integer32"""
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


_Metro1500EthernetHubPortEnable5_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortEnable5_Object = MibTableColumn
metro1500EthernetHubPortEnable5 = _Metro1500EthernetHubPortEnable5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 50),
    _Metro1500EthernetHubPortEnable5_Type()
)
metro1500EthernetHubPortEnable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable5.setStatus("mandatory")


class _Metro1500EthernetHubPortPartitionStatus5_Type(Integer32):
    """Custom type metro1500EthernetHubPortPartitionStatus5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPartitioned", 2),
          ("partitioned", 1))
    )


_Metro1500EthernetHubPortPartitionStatus5_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPartitionStatus5_Object = MibTableColumn
metro1500EthernetHubPortPartitionStatus5 = _Metro1500EthernetHubPortPartitionStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 51),
    _Metro1500EthernetHubPortPartitionStatus5_Type()
)
metro1500EthernetHubPortPartitionStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitionStatus5.setStatus("mandatory")


class _Metro1500EthernetHubPortLinkStatus5_Type(Integer32):
    """Custom type metro1500EthernetHubPortLinkStatus5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linked", 1),
          ("notLinked", 2))
    )


_Metro1500EthernetHubPortLinkStatus5_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortLinkStatus5_Object = MibTableColumn
metro1500EthernetHubPortLinkStatus5 = _Metro1500EthernetHubPortLinkStatus5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 52),
    _Metro1500EthernetHubPortLinkStatus5_Type()
)
metro1500EthernetHubPortLinkStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkStatus5.setStatus("mandatory")


class _Metro1500EthernetHubPortPolarity5_Type(Integer32):
    """Custom type metro1500EthernetHubPortPolarity5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1))
    )


_Metro1500EthernetHubPortPolarity5_Type.__name__ = "Integer32"
_Metro1500EthernetHubPortPolarity5_Object = MibTableColumn
metro1500EthernetHubPortPolarity5 = _Metro1500EthernetHubPortPolarity5_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 14, 1, 1, 53),
    _Metro1500EthernetHubPortPolarity5_Type()
)
metro1500EthernetHubPortPolarity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPolarity5.setStatus("mandatory")
_Metro1500TDM_ObjectIdentity = ObjectIdentity
metro1500TDM = _Metro1500TDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15)
)
_Metro1500TDMTable_Object = MibTable
metro1500TDMTable = _Metro1500TDMTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1)
)
if mibBuilder.loadTexts:
    metro1500TDMTable.setStatus("mandatory")
_Metro1500TDMEntry_Object = MibTableRow
metro1500TDMEntry = _Metro1500TDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1)
)
metro1500TDMEntry.setIndexNames(
    (0, "METRO1500-MIB", "metro1500TDMNumber"),
)
if mibBuilder.loadTexts:
    metro1500TDMEntry.setStatus("mandatory")


class _Metro1500TDMNumber_Type(Integer32):
    """Custom type metro1500TDMNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 79),
    )


_Metro1500TDMNumber_Type.__name__ = "Integer32"
_Metro1500TDMNumber_Object = MibTableColumn
metro1500TDMNumber = _Metro1500TDMNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 1),
    _Metro1500TDMNumber_Type()
)
metro1500TDMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMNumber.setStatus("mandatory")


class _Metro1500TDMRxRem_Type(Integer32):
    """Custom type metro1500TDMRxRem based on Integer32"""
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


_Metro1500TDMRxRem_Type.__name__ = "Integer32"
_Metro1500TDMRxRem_Object = MibTableColumn
metro1500TDMRxRem = _Metro1500TDMRxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 4),
    _Metro1500TDMRxRem_Type()
)
metro1500TDMRxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMRxRem.setStatus("mandatory")


class _Metro1500TDMRxSync_Type(Integer32):
    """Custom type metro1500TDMRxSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSync", 2),
          ("sync", 1))
    )


_Metro1500TDMRxSync_Type.__name__ = "Integer32"
_Metro1500TDMRxSync_Object = MibTableColumn
metro1500TDMRxSync = _Metro1500TDMRxSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 5),
    _Metro1500TDMRxSync_Type()
)
metro1500TDMRxSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMRxSync.setStatus("mandatory")


class _Metro1500TDMTxRem_Type(Integer32):
    """Custom type metro1500TDMTxRem based on Integer32"""
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
        *(("alwaysOff", 4),
          ("alwaysOn", 3),
          ("off", 2),
          ("on", 1))
    )


_Metro1500TDMTxRem_Type.__name__ = "Integer32"
_Metro1500TDMTxRem_Object = MibTableColumn
metro1500TDMTxRem = _Metro1500TDMTxRem_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 6),
    _Metro1500TDMTxRem_Type()
)
metro1500TDMTxRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMTxRem.setStatus("mandatory")


class _Metro1500TDMTxRemC_Type(Integer32):
    """Custom type metro1500TDMTxRemC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Metro1500TDMTxRemC_Type.__name__ = "Integer32"
_Metro1500TDMTxRemC_Object = MibTableColumn
metro1500TDMTxRemC = _Metro1500TDMTxRemC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 7),
    _Metro1500TDMTxRemC_Type()
)
metro1500TDMTxRemC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMTxRemC.setStatus("mandatory")


class _Metro1500TDMTxRemTemp_Type(Integer32):
    """Custom type metro1500TDMTxRemTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_Metro1500TDMTxRemTemp_Type.__name__ = "Integer32"
_Metro1500TDMTxRemTemp_Object = MibTableColumn
metro1500TDMTxRemTemp = _Metro1500TDMTxRemTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 8),
    _Metro1500TDMTxRemTemp_Type()
)
metro1500TDMTxRemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMTxRemTemp.setStatus("mandatory")


class _Metro1500TDMLocLoop_Type(Integer32):
    """Custom type metro1500TDMLocLoop based on Integer32"""
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


_Metro1500TDMLocLoop_Type.__name__ = "Integer32"
_Metro1500TDMLocLoop_Object = MibTableColumn
metro1500TDMLocLoop = _Metro1500TDMLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 9),
    _Metro1500TDMLocLoop_Type()
)
metro1500TDMLocLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocLoop.setStatus("mandatory")


class _Metro1500TDMLocModuleInst1_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst1_Object = MibTableColumn
metro1500TDMLocModuleInst1 = _Metro1500TDMLocModuleInst1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 20),
    _Metro1500TDMLocModuleInst1_Type()
)
metro1500TDMLocModuleInst1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst1.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable1_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable1_Object = MibTableColumn
metro1500TDMLocModuleEnable1 = _Metro1500TDMLocModuleEnable1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 21),
    _Metro1500TDMLocModuleEnable1_Type()
)
metro1500TDMLocModuleEnable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable1.setStatus("mandatory")


class _Metro1500TDMLocModuleRx1_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx1 based on Integer32"""
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


_Metro1500TDMLocModuleRx1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx1_Object = MibTableColumn
metro1500TDMLocModuleRx1 = _Metro1500TDMLocModuleRx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 22),
    _Metro1500TDMLocModuleRx1_Type()
)
metro1500TDMLocModuleRx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx1.setStatus("mandatory")


class _Metro1500TDMLocModuleTx1_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx1 based on Integer32"""
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
        *(("alwaysOff", 4),
          ("alwaysOn", 3),
          ("off", 2),
          ("on", 1))
    )


_Metro1500TDMLocModuleTx1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx1_Object = MibTableColumn
metro1500TDMLocModuleTx1 = _Metro1500TDMLocModuleTx1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 23),
    _Metro1500TDMLocModuleTx1_Type()
)
metro1500TDMLocModuleTx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx1.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData1_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData1_Object = MibTableColumn
metro1500TDMLocModuleRemoteData1 = _Metro1500TDMLocModuleRemoteData1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 24),
    _Metro1500TDMLocModuleRemoteData1_Type()
)
metro1500TDMLocModuleRemoteData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData1.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency1_Type = Integer32
_Metro1500TDMLocModuleClockFrequency1_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency1 = _Metro1500TDMLocModuleClockFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 25),
    _Metro1500TDMLocModuleClockFrequency1_Type()
)
metro1500TDMLocModuleClockFrequency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency1.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError1_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError1_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError1_Object = MibTableColumn
metro1500TDMLocModuleClockError1 = _Metro1500TDMLocModuleClockError1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 26),
    _Metro1500TDMLocModuleClockError1_Type()
)
metro1500TDMLocModuleClockError1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError1.setStatus("mandatory")


class _Metro1500TDMLocModuleInst2_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst2_Object = MibTableColumn
metro1500TDMLocModuleInst2 = _Metro1500TDMLocModuleInst2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 30),
    _Metro1500TDMLocModuleInst2_Type()
)
metro1500TDMLocModuleInst2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst2.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable2_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable2_Object = MibTableColumn
metro1500TDMLocModuleEnable2 = _Metro1500TDMLocModuleEnable2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 31),
    _Metro1500TDMLocModuleEnable2_Type()
)
metro1500TDMLocModuleEnable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable2.setStatus("mandatory")


class _Metro1500TDMLocModuleRx2_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx2 based on Integer32"""
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


_Metro1500TDMLocModuleRx2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx2_Object = MibTableColumn
metro1500TDMLocModuleRx2 = _Metro1500TDMLocModuleRx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 32),
    _Metro1500TDMLocModuleRx2_Type()
)
metro1500TDMLocModuleRx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx2.setStatus("mandatory")


class _Metro1500TDMLocModuleTx2_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx2 based on Integer32"""
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
        *(("alwaysOff", 4),
          ("alwaysOn", 3),
          ("off", 2),
          ("on", 1))
    )


_Metro1500TDMLocModuleTx2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx2_Object = MibTableColumn
metro1500TDMLocModuleTx2 = _Metro1500TDMLocModuleTx2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 33),
    _Metro1500TDMLocModuleTx2_Type()
)
metro1500TDMLocModuleTx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx2.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData2_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData2_Object = MibTableColumn
metro1500TDMLocModuleRemoteData2 = _Metro1500TDMLocModuleRemoteData2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 34),
    _Metro1500TDMLocModuleRemoteData2_Type()
)
metro1500TDMLocModuleRemoteData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData2.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency2_Type = Integer32
_Metro1500TDMLocModuleClockFrequency2_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency2 = _Metro1500TDMLocModuleClockFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 35),
    _Metro1500TDMLocModuleClockFrequency2_Type()
)
metro1500TDMLocModuleClockFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency2.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError2_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError2_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError2_Object = MibTableColumn
metro1500TDMLocModuleClockError2 = _Metro1500TDMLocModuleClockError2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 36),
    _Metro1500TDMLocModuleClockError2_Type()
)
metro1500TDMLocModuleClockError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError2.setStatus("mandatory")


class _Metro1500TDMLocModuleInst3_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst3_Object = MibTableColumn
metro1500TDMLocModuleInst3 = _Metro1500TDMLocModuleInst3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 40),
    _Metro1500TDMLocModuleInst3_Type()
)
metro1500TDMLocModuleInst3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst3.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable3_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable3_Object = MibTableColumn
metro1500TDMLocModuleEnable3 = _Metro1500TDMLocModuleEnable3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 41),
    _Metro1500TDMLocModuleEnable3_Type()
)
metro1500TDMLocModuleEnable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable3.setStatus("mandatory")


class _Metro1500TDMLocModuleRx3_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx3 based on Integer32"""
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


_Metro1500TDMLocModuleRx3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx3_Object = MibTableColumn
metro1500TDMLocModuleRx3 = _Metro1500TDMLocModuleRx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 42),
    _Metro1500TDMLocModuleRx3_Type()
)
metro1500TDMLocModuleRx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx3.setStatus("mandatory")


class _Metro1500TDMLocModuleTx3_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx3 based on Integer32"""
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
        *(("alwaysOff", 4),
          ("alwaysOn", 3),
          ("off", 2),
          ("on", 1))
    )


_Metro1500TDMLocModuleTx3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx3_Object = MibTableColumn
metro1500TDMLocModuleTx3 = _Metro1500TDMLocModuleTx3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 43),
    _Metro1500TDMLocModuleTx3_Type()
)
metro1500TDMLocModuleTx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx3.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData3_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData3_Object = MibTableColumn
metro1500TDMLocModuleRemoteData3 = _Metro1500TDMLocModuleRemoteData3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 44),
    _Metro1500TDMLocModuleRemoteData3_Type()
)
metro1500TDMLocModuleRemoteData3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData3.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency3_Type = Integer32
_Metro1500TDMLocModuleClockFrequency3_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency3 = _Metro1500TDMLocModuleClockFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 45),
    _Metro1500TDMLocModuleClockFrequency3_Type()
)
metro1500TDMLocModuleClockFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency3.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError3_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError3_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError3_Object = MibTableColumn
metro1500TDMLocModuleClockError3 = _Metro1500TDMLocModuleClockError3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 46),
    _Metro1500TDMLocModuleClockError3_Type()
)
metro1500TDMLocModuleClockError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError3.setStatus("mandatory")


class _Metro1500TDMLocModuleInst4_Type(Integer32):
    """Custom type metro1500TDMLocModuleInst4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2))
    )


_Metro1500TDMLocModuleInst4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleInst4_Object = MibTableColumn
metro1500TDMLocModuleInst4 = _Metro1500TDMLocModuleInst4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 50),
    _Metro1500TDMLocModuleInst4_Type()
)
metro1500TDMLocModuleInst4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleInst4.setStatus("mandatory")


class _Metro1500TDMLocModuleEnable4_Type(Integer32):
    """Custom type metro1500TDMLocModuleEnable4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("notEnabled", 2))
    )


_Metro1500TDMLocModuleEnable4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleEnable4_Object = MibTableColumn
metro1500TDMLocModuleEnable4 = _Metro1500TDMLocModuleEnable4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 51),
    _Metro1500TDMLocModuleEnable4_Type()
)
metro1500TDMLocModuleEnable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnable4.setStatus("mandatory")


class _Metro1500TDMLocModuleRx4_Type(Integer32):
    """Custom type metro1500TDMLocModuleRx4 based on Integer32"""
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


_Metro1500TDMLocModuleRx4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRx4_Object = MibTableColumn
metro1500TDMLocModuleRx4 = _Metro1500TDMLocModuleRx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 52),
    _Metro1500TDMLocModuleRx4_Type()
)
metro1500TDMLocModuleRx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRx4.setStatus("mandatory")


class _Metro1500TDMLocModuleTx4_Type(Integer32):
    """Custom type metro1500TDMLocModuleTx4 based on Integer32"""
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
        *(("alwaysOff", 4),
          ("alwaysOn", 3),
          ("off", 2),
          ("on", 1))
    )


_Metro1500TDMLocModuleTx4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleTx4_Object = MibTableColumn
metro1500TDMLocModuleTx4 = _Metro1500TDMLocModuleTx4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 53),
    _Metro1500TDMLocModuleTx4_Type()
)
metro1500TDMLocModuleTx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleTx4.setStatus("mandatory")


class _Metro1500TDMLocModuleRemoteData4_Type(Integer32):
    """Custom type metro1500TDMLocModuleRemoteData4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("noData", 2))
    )


_Metro1500TDMLocModuleRemoteData4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleRemoteData4_Object = MibTableColumn
metro1500TDMLocModuleRemoteData4 = _Metro1500TDMLocModuleRemoteData4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 54),
    _Metro1500TDMLocModuleRemoteData4_Type()
)
metro1500TDMLocModuleRemoteData4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRemoteData4.setStatus("mandatory")
_Metro1500TDMLocModuleClockFrequency4_Type = Integer32
_Metro1500TDMLocModuleClockFrequency4_Object = MibTableColumn
metro1500TDMLocModuleClockFrequency4 = _Metro1500TDMLocModuleClockFrequency4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 55),
    _Metro1500TDMLocModuleClockFrequency4_Type()
)
metro1500TDMLocModuleClockFrequency4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFrequency4.setStatus("mandatory")


class _Metro1500TDMLocModuleClockError4_Type(Integer32):
    """Custom type metro1500TDMLocModuleClockError4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 2))
    )


_Metro1500TDMLocModuleClockError4_Type.__name__ = "Integer32"
_Metro1500TDMLocModuleClockError4_Object = MibTableColumn
metro1500TDMLocModuleClockError4 = _Metro1500TDMLocModuleClockError4_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 15, 1, 1, 56),
    _Metro1500TDMLocModuleClockError4_Type()
)
metro1500TDMLocModuleClockError4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockError4.setStatus("mandatory")
_Metro1500Trap_ObjectIdentity = ObjectIdentity
metro1500Trap = _Metro1500Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100)
)

# Managed Objects groups


# Notification objects

metro1500HardwareAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 1)
)
metro1500HardwareAdded.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500HardwareAdded.setStatus(
        ""
    )

metro1500HardwareDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 2)
)
metro1500HardwareDeleted.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500HardwareDeleted.setStatus(
        ""
    )

metro1500PSNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 3)
)
metro1500PSNotFail.setObjects(
    ("METRO1500-MIB", "metro1500PSNumber")
)
if mibBuilder.loadTexts:
    metro1500PSNotFail.setStatus(
        ""
    )

metro1500PSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 4)
)
metro1500PSFail.setObjects(
    ("METRO1500-MIB", "metro1500PSNumber")
)
if mibBuilder.loadTexts:
    metro1500PSFail.setStatus(
        ""
    )

metro1500FanNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 5)
)
metro1500FanNotFail.setObjects(
    ("METRO1500-MIB", "metro1500FanNumber")
)
if mibBuilder.loadTexts:
    metro1500FanNotFail.setStatus(
        ""
    )

metro1500FanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 6)
)
metro1500FanFail.setObjects(
    ("METRO1500-MIB", "metro1500FanNumber")
)
if mibBuilder.loadTexts:
    metro1500FanFail.setStatus(
        ""
    )

metro1500BusNotFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 7)
)
if mibBuilder.loadTexts:
    metro1500BusNotFail.setStatus(
        ""
    )

metro1500BusFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 8)
)
if mibBuilder.loadTexts:
    metro1500BusFail.setStatus(
        ""
    )

metro1500RxLocOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 20)
)
metro1500RxLocOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxLocOn.setStatus(
        ""
    )

metro1500RxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 21)
)
metro1500RxLocOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxLocOff.setStatus(
        ""
    )

metro1500TxLocOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 22)
)
metro1500TxLocOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxLocOn.setStatus(
        ""
    )

metro1500TxLocOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 23)
)
metro1500TxLocOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxLocOff.setStatus(
        ""
    )

metro1500RxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 24)
)
metro1500RxRemOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxRemOn.setStatus(
        ""
    )

metro1500RxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 25)
)
metro1500RxRemOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxRemOff.setStatus(
        ""
    )

metro1500TxRemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 26)
)
metro1500TxRemOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxRemOn.setStatus(
        ""
    )

metro1500TxRemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 27)
)
metro1500TxRemOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxRemOff.setStatus(
        ""
    )

metro1500RxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 28)
)
metro1500RxRem2On.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxRem2On.setStatus(
        ""
    )

metro1500RxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 29)
)
metro1500RxRem2Off.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RxRem2Off.setStatus(
        ""
    )

metro1500TxRem2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 30)
)
metro1500TxRem2On.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxRem2On.setStatus(
        ""
    )

metro1500TxRem2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 31)
)
metro1500TxRem2Off.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TxRem2Off.setStatus(
        ""
    )

metro1500ClockNoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 32)
)
metro1500ClockNoFail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500ClockNoFail.setStatus(
        ""
    )

metro1500ClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 33)
)
metro1500ClockFail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500ClockFail.setStatus(
        ""
    )

metro1500ClockChangeFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 34)
)
metro1500ClockChangeFrequency.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500ClockChangeFrequency.setStatus(
        ""
    )

metro1500LocLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 35)
)
metro1500LocLoopOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500LocLoopOn.setStatus(
        ""
    )

metro1500LocLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 36)
)
metro1500LocLoopOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500LocLoopOff.setStatus(
        ""
    )

metro1500RemLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 37)
)
metro1500RemLoopOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RemLoopOn.setStatus(
        ""
    )

metro1500RemLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 38)
)
metro1500RemLoopOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500RemLoopOff.setStatus(
        ""
    )

metro1500switchReferenceLaserOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 40)
)
metro1500switchReferenceLaserOn.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchReferenceLaserOn.setStatus(
        ""
    )

metro1500switchReferenceLaserOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 41)
)
metro1500switchReferenceLaserOff.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchReferenceLaserOff.setStatus(
        ""
    )

metro1500switchToA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 42)
)
metro1500switchToA.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchToA.setStatus(
        ""
    )

metro1500switchToB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 43)
)
metro1500switchToB.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchToB.setStatus(
        ""
    )

metro1500switchAutomatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 44)
)
metro1500switchAutomatic.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchAutomatic.setStatus(
        ""
    )

metro1500switchLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 45)
)
metro1500switchLocked.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLocked.setStatus(
        ""
    )

metro1500switchLineAavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 46)
)
metro1500switchLineAavail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLineAavail.setStatus(
        ""
    )

metro1500switchLineANotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 47)
)
metro1500switchLineANotAvail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLineANotAvail.setStatus(
        ""
    )

metro1500switchLineBavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 48)
)
metro1500switchLineBavail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLineBavail.setStatus(
        ""
    )

metro1500switchLineBNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 49)
)
metro1500switchLineBNotAvail.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500switchLineBNotAvail.setStatus(
        ""
    )

metro1500repeatedMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 50)
)
metro1500repeatedMessage.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500repeatedMessage.setStatus(
        ""
    )

metro1500INNCDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 51)
)
if mibBuilder.loadTexts:
    metro1500INNCDown.setStatus(
        ""
    )

metro1500INNCUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 52)
)
if mibBuilder.loadTexts:
    metro1500INNCUp.setStatus(
        ""
    )

metro1500EthernetHubPortEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 60)
)
metro1500EthernetHubPortEnable.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetHubPortEnable.setStatus(
        ""
    )

metro1500EthernetHubPortDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 61)
)
metro1500EthernetHubPortDisable.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetHubPortDisable.setStatus(
        ""
    )

metro1500EthernetHubPortPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 62)
)
metro1500EthernetHubPortPartitioned.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetHubPortPartitioned.setStatus(
        ""
    )

metro1500EthernetHubPortNotPartitioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 63)
)
metro1500EthernetHubPortNotPartitioned.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetHubPortNotPartitioned.setStatus(
        ""
    )

metro1500EthernetHubPortLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 64)
)
metro1500EthernetHubPortLinkPulses.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetHubPortLinkPulses.setStatus(
        ""
    )

metro1500EthernetHubPortNoLinkPulses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 65)
)
metro1500EthernetHubPortNoLinkPulses.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500EthernetHubPortNoLinkPulses.setStatus(
        ""
    )

metro1500TDMRemoteSyncLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 70)
)
metro1500TDMRemoteSyncLoss.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMRemoteSyncLoss.setStatus(
        ""
    )

metro1500TDMRemoteSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 71)
)
metro1500TDMRemoteSync.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMRemoteSync.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 72)
)
metro1500TDMLocModuleEnabled1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled1.setStatus(
        ""
    )

metro1500TDMLocModuleDisable1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 73)
)
metro1500TDMLocModuleDisable1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable1.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 74)
)
metro1500TDMLocModuleEnabled2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled2.setStatus(
        ""
    )

metro1500TDMLocModuleDisable2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 75)
)
metro1500TDMLocModuleDisable2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable2.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 76)
)
metro1500TDMLocModuleEnabled3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled3.setStatus(
        ""
    )

metro1500TDMLocModuleDisable3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 77)
)
metro1500TDMLocModuleDisable3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable3.setStatus(
        ""
    )

metro1500TDMLocModuleEnabled4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 78)
)
metro1500TDMLocModuleEnabled4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleEnabled4.setStatus(
        ""
    )

metro1500TDMLocModuleDisable4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 79)
)
metro1500TDMLocModuleDisable4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleDisable4.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 88)
)
metro1500TDMLocModuleRxOn1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn1.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 89)
)
metro1500TDMLocModuleRxOff1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff1.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 90)
)
metro1500TDMLocModuleRxOn2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn2.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 91)
)
metro1500TDMLocModuleRxOff2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff2.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 92)
)
metro1500TDMLocModuleRxOn3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn3.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 93)
)
metro1500TDMLocModuleRxOff3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff3.setStatus(
        ""
    )

metro1500TDMLocModuleRxOn4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 94)
)
metro1500TDMLocModuleRxOn4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOn4.setStatus(
        ""
    )

metro1500TDMLocModuleRxOff4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 95)
)
metro1500TDMLocModuleRxOff4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleRxOff4.setStatus(
        ""
    )

metro1500TDMLocModuleData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 104)
)
metro1500TDMLocModuleData1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData1.setStatus(
        ""
    )

metro1500TDMLocModuleNoData1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 105)
)
metro1500TDMLocModuleNoData1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData1.setStatus(
        ""
    )

metro1500TDMLocModuleData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 106)
)
metro1500TDMLocModuleData2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData2.setStatus(
        ""
    )

metro1500TDMLocModuleNoData2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 107)
)
metro1500TDMLocModuleNoData2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData2.setStatus(
        ""
    )

metro1500TDMLocModuleData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 108)
)
metro1500TDMLocModuleData3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData3.setStatus(
        ""
    )

metro1500TDMLocModuleNoData3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 109)
)
metro1500TDMLocModuleNoData3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData3.setStatus(
        ""
    )

metro1500TDMLocModuleData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 110)
)
metro1500TDMLocModuleData4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleData4.setStatus(
        ""
    )

metro1500TDMLocModuleNoData4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 111)
)
metro1500TDMLocModuleNoData4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleNoData4.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 120)
)
metro1500TDMLocModuleClockFail1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail1.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 121)
)
metro1500TDMLocModuleClockNoFail1.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail1.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 122)
)
metro1500TDMLocModuleClockFail2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail2.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 123)
)
metro1500TDMLocModuleClockNoFail2.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail2.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 124)
)
metro1500TDMLocModuleClockFail3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail3.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 125)
)
metro1500TDMLocModuleClockNoFail3.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail3.setStatus(
        ""
    )

metro1500TDMLocModuleClockFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 126)
)
metro1500TDMLocModuleClockFail4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockFail4.setStatus(
        ""
    )

metro1500TDMLocModuleClockNoFail4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 3, 100, 0, 127)
)
metro1500TDMLocModuleClockNoFail4.setObjects(
    ("METRO1500-MIB", "metro1500SlotNumber")
)
if mibBuilder.loadTexts:
    metro1500TDMLocModuleClockNoFail4.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "METRO1500-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "adva": adva,
       "advaProducts": advaProducts,
       "metro1500": metro1500,
       "metro1500Main": metro1500Main,
       "metro1500Housing": metro1500Housing,
       "metro1500Manufacturer": metro1500Manufacturer,
       "metro1500MainType": metro1500MainType,
       "metro1500MainSerialNumber": metro1500MainSerialNumber,
       "metro1500MainHardwareVersion": metro1500MainHardwareVersion,
       "metro1500MainSoftwareVersion": metro1500MainSoftwareVersion,
       "metro1500MainBusMessages": metro1500MainBusMessages,
       "metro1500MainBusErrors": metro1500MainBusErrors,
       "metro1500MainLastEvent": metro1500MainLastEvent,
       "metro1500MainMotd": metro1500MainMotd,
       "metro1500MainTrapsinkTable": metro1500MainTrapsinkTable,
       "metro1500MainTrapsinkEntry": metro1500MainTrapsinkEntry,
       "metro1500MainTrapsinkNumber": metro1500MainTrapsinkNumber,
       "metro1500MainTrapsinkAddress": metro1500MainTrapsinkAddress,
       "metro1500MainTrapsinkCommunity": metro1500MainTrapsinkCommunity,
       "metro1500MainTrapsinkPriority": metro1500MainTrapsinkPriority,
       "metro1500MainLogfileTable": metro1500MainLogfileTable,
       "metro1500MainLogfileEntry": metro1500MainLogfileEntry,
       "metro1500MainLogfileNumber": metro1500MainLogfileNumber,
       "metro1500MainLogfileName": metro1500MainLogfileName,
       "metro1500MainLogfileSize": metro1500MainLogfileSize,
       "metro1500MainLogfilePriority": metro1500MainLogfilePriority,
       "metro1500SlotTable": metro1500SlotTable,
       "metro1500SlotEntry": metro1500SlotEntry,
       "metro1500SlotNumber": metro1500SlotNumber,
       "metro1500Type": metro1500Type,
       "metro1500SlotTypeNumber": metro1500SlotTypeNumber,
       "metro1500SerialNumber": metro1500SerialNumber,
       "metro1500HardwareVersion": metro1500HardwareVersion,
       "metro1500SoftwareVersion": metro1500SoftwareVersion,
       "metro1500Temperature": metro1500Temperature,
       "metro1500BoardVoltage": metro1500BoardVoltage,
       "metro1500DetailInfo": metro1500DetailInfo,
       "metro1500EPLDVersion": metro1500EPLDVersion,
       "metro1500PSTable": metro1500PSTable,
       "metro1500PSEntry": metro1500PSEntry,
       "metro1500PSNumber": metro1500PSNumber,
       "metro1500PSOn": metro1500PSOn,
       "metro1500FanTable": metro1500FanTable,
       "metro1500FanEntry": metro1500FanEntry,
       "metro1500FanNumber": metro1500FanNumber,
       "metro1500FanOn": metro1500FanOn,
       "metro1500Converter": metro1500Converter,
       "metro1500ConverterTable": metro1500ConverterTable,
       "metro1500ConverterEntry": metro1500ConverterEntry,
       "metro1500ConverterNumber": metro1500ConverterNumber,
       "metro1500RxLoc": metro1500RxLoc,
       "metro1500TxLoc": metro1500TxLoc,
       "metro1500TxLocC": metro1500TxLocC,
       "metro1500TxLocTemp": metro1500TxLocTemp,
       "metro1500RxRem": metro1500RxRem,
       "metro1500TxRem": metro1500TxRem,
       "metro1500TxRemC": metro1500TxRemC,
       "metro1500TxRemTemp": metro1500TxRemTemp,
       "metro1500RxRem2": metro1500RxRem2,
       "metro1500ClockState": metro1500ClockState,
       "metro1500ClockFreq": metro1500ClockFreq,
       "metro1500LocLoop": metro1500LocLoop,
       "metro1500RemLoop": metro1500RemLoop,
       "metro1500ClockType": metro1500ClockType,
       "metro1500Switch": metro1500Switch,
       "metro1500SwitchTable": metro1500SwitchTable,
       "metro1500SwitchEntry": metro1500SwitchEntry,
       "metro1500SwitchNumber": metro1500SwitchNumber,
       "metro1500SwitchLine": metro1500SwitchLine,
       "metro1500SwitchMode": metro1500SwitchMode,
       "metro1500SwitchLaserOn": metro1500SwitchLaserOn,
       "metro1500SwitchLineAavail": metro1500SwitchLineAavail,
       "metro1500SwitchLineBavail": metro1500SwitchLineBavail,
       "metro1500EthernetHub": metro1500EthernetHub,
       "metro1500EthernetHubTable": metro1500EthernetHubTable,
       "metro1500EthernetHubEntry": metro1500EthernetHubEntry,
       "metro1500EthernetHubNumber": metro1500EthernetHubNumber,
       "metro1500EthernetHubPortEnable1": metro1500EthernetHubPortEnable1,
       "metro1500EthernetHubPortPartitionStatus1": metro1500EthernetHubPortPartitionStatus1,
       "metro1500EthernetHubPortLinkStatus1": metro1500EthernetHubPortLinkStatus1,
       "metro1500EthernetHubPortPolarity1": metro1500EthernetHubPortPolarity1,
       "metro1500EthernetHubPortEnable2": metro1500EthernetHubPortEnable2,
       "metro1500EthernetHubPortPartitionStatus2": metro1500EthernetHubPortPartitionStatus2,
       "metro1500EthernetHubPortLinkStatus2": metro1500EthernetHubPortLinkStatus2,
       "metro1500EthernetHubPortPolarity2": metro1500EthernetHubPortPolarity2,
       "metro1500EthernetHubPortEnable3": metro1500EthernetHubPortEnable3,
       "metro1500EthernetHubPortPartitionStatus3": metro1500EthernetHubPortPartitionStatus3,
       "metro1500EthernetHubPortLinkStatus3": metro1500EthernetHubPortLinkStatus3,
       "metro1500EthernetHubPortPolarity3": metro1500EthernetHubPortPolarity3,
       "metro1500EthernetHubPortEnable4": metro1500EthernetHubPortEnable4,
       "metro1500EthernetHubPortPartitionStatus4": metro1500EthernetHubPortPartitionStatus4,
       "metro1500EthernetHubPortLinkStatus4": metro1500EthernetHubPortLinkStatus4,
       "metro1500EthernetHubPortPolarity4": metro1500EthernetHubPortPolarity4,
       "metro1500EthernetHubPortEnable5": metro1500EthernetHubPortEnable5,
       "metro1500EthernetHubPortPartitionStatus5": metro1500EthernetHubPortPartitionStatus5,
       "metro1500EthernetHubPortLinkStatus5": metro1500EthernetHubPortLinkStatus5,
       "metro1500EthernetHubPortPolarity5": metro1500EthernetHubPortPolarity5,
       "metro1500TDM": metro1500TDM,
       "metro1500TDMTable": metro1500TDMTable,
       "metro1500TDMEntry": metro1500TDMEntry,
       "metro1500TDMNumber": metro1500TDMNumber,
       "metro1500TDMRxRem": metro1500TDMRxRem,
       "metro1500TDMRxSync": metro1500TDMRxSync,
       "metro1500TDMTxRem": metro1500TDMTxRem,
       "metro1500TDMTxRemC": metro1500TDMTxRemC,
       "metro1500TDMTxRemTemp": metro1500TDMTxRemTemp,
       "metro1500TDMLocLoop": metro1500TDMLocLoop,
       "metro1500TDMLocModuleInst1": metro1500TDMLocModuleInst1,
       "metro1500TDMLocModuleEnable1": metro1500TDMLocModuleEnable1,
       "metro1500TDMLocModuleRx1": metro1500TDMLocModuleRx1,
       "metro1500TDMLocModuleTx1": metro1500TDMLocModuleTx1,
       "metro1500TDMLocModuleRemoteData1": metro1500TDMLocModuleRemoteData1,
       "metro1500TDMLocModuleClockFrequency1": metro1500TDMLocModuleClockFrequency1,
       "metro1500TDMLocModuleClockError1": metro1500TDMLocModuleClockError1,
       "metro1500TDMLocModuleInst2": metro1500TDMLocModuleInst2,
       "metro1500TDMLocModuleEnable2": metro1500TDMLocModuleEnable2,
       "metro1500TDMLocModuleRx2": metro1500TDMLocModuleRx2,
       "metro1500TDMLocModuleTx2": metro1500TDMLocModuleTx2,
       "metro1500TDMLocModuleRemoteData2": metro1500TDMLocModuleRemoteData2,
       "metro1500TDMLocModuleClockFrequency2": metro1500TDMLocModuleClockFrequency2,
       "metro1500TDMLocModuleClockError2": metro1500TDMLocModuleClockError2,
       "metro1500TDMLocModuleInst3": metro1500TDMLocModuleInst3,
       "metro1500TDMLocModuleEnable3": metro1500TDMLocModuleEnable3,
       "metro1500TDMLocModuleRx3": metro1500TDMLocModuleRx3,
       "metro1500TDMLocModuleTx3": metro1500TDMLocModuleTx3,
       "metro1500TDMLocModuleRemoteData3": metro1500TDMLocModuleRemoteData3,
       "metro1500TDMLocModuleClockFrequency3": metro1500TDMLocModuleClockFrequency3,
       "metro1500TDMLocModuleClockError3": metro1500TDMLocModuleClockError3,
       "metro1500TDMLocModuleInst4": metro1500TDMLocModuleInst4,
       "metro1500TDMLocModuleEnable4": metro1500TDMLocModuleEnable4,
       "metro1500TDMLocModuleRx4": metro1500TDMLocModuleRx4,
       "metro1500TDMLocModuleTx4": metro1500TDMLocModuleTx4,
       "metro1500TDMLocModuleRemoteData4": metro1500TDMLocModuleRemoteData4,
       "metro1500TDMLocModuleClockFrequency4": metro1500TDMLocModuleClockFrequency4,
       "metro1500TDMLocModuleClockError4": metro1500TDMLocModuleClockError4,
       "metro1500Trap": metro1500Trap,
       "metro1500HardwareAdded": metro1500HardwareAdded,
       "metro1500HardwareDeleted": metro1500HardwareDeleted,
       "metro1500PSNotFail": metro1500PSNotFail,
       "metro1500PSFail": metro1500PSFail,
       "metro1500FanNotFail": metro1500FanNotFail,
       "metro1500FanFail": metro1500FanFail,
       "metro1500BusNotFail": metro1500BusNotFail,
       "metro1500BusFail": metro1500BusFail,
       "metro1500RxLocOn": metro1500RxLocOn,
       "metro1500RxLocOff": metro1500RxLocOff,
       "metro1500TxLocOn": metro1500TxLocOn,
       "metro1500TxLocOff": metro1500TxLocOff,
       "metro1500RxRemOn": metro1500RxRemOn,
       "metro1500RxRemOff": metro1500RxRemOff,
       "metro1500TxRemOn": metro1500TxRemOn,
       "metro1500TxRemOff": metro1500TxRemOff,
       "metro1500RxRem2On": metro1500RxRem2On,
       "metro1500RxRem2Off": metro1500RxRem2Off,
       "metro1500TxRem2On": metro1500TxRem2On,
       "metro1500TxRem2Off": metro1500TxRem2Off,
       "metro1500ClockNoFail": metro1500ClockNoFail,
       "metro1500ClockFail": metro1500ClockFail,
       "metro1500ClockChangeFrequency": metro1500ClockChangeFrequency,
       "metro1500LocLoopOn": metro1500LocLoopOn,
       "metro1500LocLoopOff": metro1500LocLoopOff,
       "metro1500RemLoopOn": metro1500RemLoopOn,
       "metro1500RemLoopOff": metro1500RemLoopOff,
       "metro1500switchReferenceLaserOn": metro1500switchReferenceLaserOn,
       "metro1500switchReferenceLaserOff": metro1500switchReferenceLaserOff,
       "metro1500switchToA": metro1500switchToA,
       "metro1500switchToB": metro1500switchToB,
       "metro1500switchAutomatic": metro1500switchAutomatic,
       "metro1500switchLocked": metro1500switchLocked,
       "metro1500switchLineAavail": metro1500switchLineAavail,
       "metro1500switchLineANotAvail": metro1500switchLineANotAvail,
       "metro1500switchLineBavail": metro1500switchLineBavail,
       "metro1500switchLineBNotAvail": metro1500switchLineBNotAvail,
       "metro1500repeatedMessage": metro1500repeatedMessage,
       "metro1500INNCDown": metro1500INNCDown,
       "metro1500INNCUp": metro1500INNCUp,
       "metro1500EthernetHubPortEnable": metro1500EthernetHubPortEnable,
       "metro1500EthernetHubPortDisable": metro1500EthernetHubPortDisable,
       "metro1500EthernetHubPortPartitioned": metro1500EthernetHubPortPartitioned,
       "metro1500EthernetHubPortNotPartitioned": metro1500EthernetHubPortNotPartitioned,
       "metro1500EthernetHubPortLinkPulses": metro1500EthernetHubPortLinkPulses,
       "metro1500EthernetHubPortNoLinkPulses": metro1500EthernetHubPortNoLinkPulses,
       "metro1500TDMRemoteSyncLoss": metro1500TDMRemoteSyncLoss,
       "metro1500TDMRemoteSync": metro1500TDMRemoteSync,
       "metro1500TDMLocModuleEnabled1": metro1500TDMLocModuleEnabled1,
       "metro1500TDMLocModuleDisable1": metro1500TDMLocModuleDisable1,
       "metro1500TDMLocModuleEnabled2": metro1500TDMLocModuleEnabled2,
       "metro1500TDMLocModuleDisable2": metro1500TDMLocModuleDisable2,
       "metro1500TDMLocModuleEnabled3": metro1500TDMLocModuleEnabled3,
       "metro1500TDMLocModuleDisable3": metro1500TDMLocModuleDisable3,
       "metro1500TDMLocModuleEnabled4": metro1500TDMLocModuleEnabled4,
       "metro1500TDMLocModuleDisable4": metro1500TDMLocModuleDisable4,
       "metro1500TDMLocModuleRxOn1": metro1500TDMLocModuleRxOn1,
       "metro1500TDMLocModuleRxOff1": metro1500TDMLocModuleRxOff1,
       "metro1500TDMLocModuleRxOn2": metro1500TDMLocModuleRxOn2,
       "metro1500TDMLocModuleRxOff2": metro1500TDMLocModuleRxOff2,
       "metro1500TDMLocModuleRxOn3": metro1500TDMLocModuleRxOn3,
       "metro1500TDMLocModuleRxOff3": metro1500TDMLocModuleRxOff3,
       "metro1500TDMLocModuleRxOn4": metro1500TDMLocModuleRxOn4,
       "metro1500TDMLocModuleRxOff4": metro1500TDMLocModuleRxOff4,
       "metro1500TDMLocModuleData1": metro1500TDMLocModuleData1,
       "metro1500TDMLocModuleNoData1": metro1500TDMLocModuleNoData1,
       "metro1500TDMLocModuleData2": metro1500TDMLocModuleData2,
       "metro1500TDMLocModuleNoData2": metro1500TDMLocModuleNoData2,
       "metro1500TDMLocModuleData3": metro1500TDMLocModuleData3,
       "metro1500TDMLocModuleNoData3": metro1500TDMLocModuleNoData3,
       "metro1500TDMLocModuleData4": metro1500TDMLocModuleData4,
       "metro1500TDMLocModuleNoData4": metro1500TDMLocModuleNoData4,
       "metro1500TDMLocModuleClockFail1": metro1500TDMLocModuleClockFail1,
       "metro1500TDMLocModuleClockNoFail1": metro1500TDMLocModuleClockNoFail1,
       "metro1500TDMLocModuleClockFail2": metro1500TDMLocModuleClockFail2,
       "metro1500TDMLocModuleClockNoFail2": metro1500TDMLocModuleClockNoFail2,
       "metro1500TDMLocModuleClockFail3": metro1500TDMLocModuleClockFail3,
       "metro1500TDMLocModuleClockNoFail3": metro1500TDMLocModuleClockNoFail3,
       "metro1500TDMLocModuleClockFail4": metro1500TDMLocModuleClockFail4,
       "metro1500TDMLocModuleClockNoFail4": metro1500TDMLocModuleClockNoFail4}
)
