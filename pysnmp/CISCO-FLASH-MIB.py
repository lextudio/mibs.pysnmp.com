# SNMP MIB module (CISCO-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FLASH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:36 2024
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

(Percent,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 InstancePointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "InstancePointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoFlashMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10)
)
ciscoFlashMIB.setRevisions(
        ("2013-08-06 00:00",
         "2011-03-16 00:00",
         "2009-06-03 00:00",
         "2008-12-08 00:00",
         "2007-03-21 00:00",
         "2006-11-08 00:00",
         "2005-06-01 00:00",
         "2005-01-28 00:00",
         "2004-03-18 00:00",
         "2003-04-23 00:00",
         "2003-01-31 12:34",
         "2002-04-01 00:00",
         "2002-01-25 00:00",
         "2002-01-22 00:00",
         "2001-02-21 12:34",
         "1998-08-27 00:00",
         "1996-04-17 00:00",
         "1995-10-18 00:00",
         "1995-08-15 00:00",
         "1995-04-29 00:00",
         "1995-01-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ChecksumString(OctetString, TextualConvention):
    status = "current"


class FlashFileType(Integer32, TextualConvention):
    status = "current"
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
        *(("config", 2),
          ("crashinfo", 5),
          ("directory", 4),
          ("image", 3),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFlashMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFlashMIBObjects = _CiscoFlashMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1)
)
_CiscoFlashDevice_ObjectIdentity = ObjectIdentity
ciscoFlashDevice = _CiscoFlashDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1)
)
_CiscoFlashDevicesSupported_Type = Unsigned32
_CiscoFlashDevicesSupported_Object = MibScalar
ciscoFlashDevicesSupported = _CiscoFlashDevicesSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 1),
    _CiscoFlashDevicesSupported_Type()
)
ciscoFlashDevicesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDevicesSupported.setStatus("current")
_CiscoFlashDeviceTable_Object = MibTable
ciscoFlashDeviceTable = _CiscoFlashDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceTable.setStatus("current")
_CiscoFlashDeviceEntry_Object = MibTableRow
ciscoFlashDeviceEntry = _CiscoFlashDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1)
)
ciscoFlashDeviceEntry.setIndexNames(
    (0, "CISCO-FLASH-MIB", "ciscoFlashDeviceIndex"),
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceEntry.setStatus("current")


class _CiscoFlashDeviceIndex_Type(Unsigned32):
    """Custom type ciscoFlashDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoFlashDeviceIndex_Type.__name__ = "Unsigned32"
_CiscoFlashDeviceIndex_Object = MibTableColumn
ciscoFlashDeviceIndex = _CiscoFlashDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 1),
    _CiscoFlashDeviceIndex_Type()
)
ciscoFlashDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoFlashDeviceIndex.setStatus("current")


class _CiscoFlashDeviceSize_Type(Unsigned32):
    """Custom type ciscoFlashDeviceSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoFlashDeviceSize_Type.__name__ = "Unsigned32"
_CiscoFlashDeviceSize_Object = MibTableColumn
ciscoFlashDeviceSize = _CiscoFlashDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 2),
    _CiscoFlashDeviceSize_Type()
)
ciscoFlashDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceSize.setStatus("current")
if mibBuilder.loadTexts:
    ciscoFlashDeviceSize.setUnits("bytes")


class _CiscoFlashDeviceMinPartitionSize_Type(Unsigned32):
    """Custom type ciscoFlashDeviceMinPartitionSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoFlashDeviceMinPartitionSize_Type.__name__ = "Unsigned32"
_CiscoFlashDeviceMinPartitionSize_Object = MibTableColumn
ciscoFlashDeviceMinPartitionSize = _CiscoFlashDeviceMinPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 3),
    _CiscoFlashDeviceMinPartitionSize_Type()
)
ciscoFlashDeviceMinPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceMinPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    ciscoFlashDeviceMinPartitionSize.setUnits("bytes")
_CiscoFlashDeviceMaxPartitions_Type = Unsigned32
_CiscoFlashDeviceMaxPartitions_Object = MibTableColumn
ciscoFlashDeviceMaxPartitions = _CiscoFlashDeviceMaxPartitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 4),
    _CiscoFlashDeviceMaxPartitions_Type()
)
ciscoFlashDeviceMaxPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceMaxPartitions.setStatus("current")


class _CiscoFlashDevicePartitions_Type(Unsigned32):
    """Custom type ciscoFlashDevicePartitions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoFlashDevicePartitions_Type.__name__ = "Unsigned32"
_CiscoFlashDevicePartitions_Object = MibTableColumn
ciscoFlashDevicePartitions = _CiscoFlashDevicePartitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 5),
    _CiscoFlashDevicePartitions_Type()
)
ciscoFlashDevicePartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDevicePartitions.setStatus("current")


class _CiscoFlashDeviceChipCount_Type(Integer32):
    """Custom type ciscoFlashDeviceChipCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CiscoFlashDeviceChipCount_Type.__name__ = "Integer32"
_CiscoFlashDeviceChipCount_Object = MibTableColumn
ciscoFlashDeviceChipCount = _CiscoFlashDeviceChipCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 6),
    _CiscoFlashDeviceChipCount_Type()
)
ciscoFlashDeviceChipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceChipCount.setStatus("current")


class _CiscoFlashDeviceName_Type(DisplayString):
    """Custom type ciscoFlashDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CiscoFlashDeviceName_Type.__name__ = "DisplayString"
_CiscoFlashDeviceName_Object = MibTableColumn
ciscoFlashDeviceName = _CiscoFlashDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 7),
    _CiscoFlashDeviceName_Type()
)
ciscoFlashDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceName.setStatus("deprecated")


class _CiscoFlashDeviceDescr_Type(DisplayString):
    """Custom type ciscoFlashDeviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CiscoFlashDeviceDescr_Type.__name__ = "DisplayString"
_CiscoFlashDeviceDescr_Object = MibTableColumn
ciscoFlashDeviceDescr = _CiscoFlashDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 8),
    _CiscoFlashDeviceDescr_Type()
)
ciscoFlashDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceDescr.setStatus("current")


class _CiscoFlashDeviceController_Type(DisplayString):
    """Custom type ciscoFlashDeviceController based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CiscoFlashDeviceController_Type.__name__ = "DisplayString"
_CiscoFlashDeviceController_Object = MibTableColumn
ciscoFlashDeviceController = _CiscoFlashDeviceController_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 9),
    _CiscoFlashDeviceController_Type()
)
ciscoFlashDeviceController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceController.setStatus("current")
_CiscoFlashDeviceCard_Type = InstancePointer
_CiscoFlashDeviceCard_Object = MibTableColumn
ciscoFlashDeviceCard = _CiscoFlashDeviceCard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 10),
    _CiscoFlashDeviceCard_Type()
)
ciscoFlashDeviceCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceCard.setStatus("deprecated")


class _CiscoFlashDeviceProgrammingJumper_Type(Integer32):
    """Custom type ciscoFlashDeviceProgrammingJumper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2),
          ("unknown", 3))
    )


_CiscoFlashDeviceProgrammingJumper_Type.__name__ = "Integer32"
_CiscoFlashDeviceProgrammingJumper_Object = MibTableColumn
ciscoFlashDeviceProgrammingJumper = _CiscoFlashDeviceProgrammingJumper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 11),
    _CiscoFlashDeviceProgrammingJumper_Type()
)
ciscoFlashDeviceProgrammingJumper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceProgrammingJumper.setStatus("current")
_CiscoFlashDeviceInitTime_Type = TimeStamp
_CiscoFlashDeviceInitTime_Object = MibTableColumn
ciscoFlashDeviceInitTime = _CiscoFlashDeviceInitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 12),
    _CiscoFlashDeviceInitTime_Type()
)
ciscoFlashDeviceInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceInitTime.setStatus("current")
_CiscoFlashDeviceRemovable_Type = TruthValue
_CiscoFlashDeviceRemovable_Object = MibTableColumn
ciscoFlashDeviceRemovable = _CiscoFlashDeviceRemovable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 13),
    _CiscoFlashDeviceRemovable_Type()
)
ciscoFlashDeviceRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceRemovable.setStatus("current")
_CiscoFlashPhyEntIndex_Type = PhysicalIndex
_CiscoFlashPhyEntIndex_Object = MibTableColumn
ciscoFlashPhyEntIndex = _CiscoFlashPhyEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 14),
    _CiscoFlashPhyEntIndex_Type()
)
ciscoFlashPhyEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPhyEntIndex.setStatus("current")


class _CiscoFlashDeviceNameExtended_Type(DisplayString):
    """Custom type ciscoFlashDeviceNameExtended based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoFlashDeviceNameExtended_Type.__name__ = "DisplayString"
_CiscoFlashDeviceNameExtended_Object = MibTableColumn
ciscoFlashDeviceNameExtended = _CiscoFlashDeviceNameExtended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 15),
    _CiscoFlashDeviceNameExtended_Type()
)
ciscoFlashDeviceNameExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceNameExtended.setStatus("current")
_CiscoFlashDeviceSizeExtended_Type = CounterBasedGauge64
_CiscoFlashDeviceSizeExtended_Object = MibTableColumn
ciscoFlashDeviceSizeExtended = _CiscoFlashDeviceSizeExtended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 16),
    _CiscoFlashDeviceSizeExtended_Type()
)
ciscoFlashDeviceSizeExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceSizeExtended.setStatus("current")
if mibBuilder.loadTexts:
    ciscoFlashDeviceSizeExtended.setUnits("bytes")
_CiscoFlashDeviceMinPartitionSizeExtended_Type = CounterBasedGauge64
_CiscoFlashDeviceMinPartitionSizeExtended_Object = MibTableColumn
ciscoFlashDeviceMinPartitionSizeExtended = _CiscoFlashDeviceMinPartitionSizeExtended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 2, 1, 17),
    _CiscoFlashDeviceMinPartitionSizeExtended_Type()
)
ciscoFlashDeviceMinPartitionSizeExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashDeviceMinPartitionSizeExtended.setStatus("current")
_CiscoFlashChips_ObjectIdentity = ObjectIdentity
ciscoFlashChips = _CiscoFlashChips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3)
)
_CiscoFlashChipTable_Object = MibTable
ciscoFlashChipTable = _CiscoFlashChipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoFlashChipTable.setStatus("current")
_CiscoFlashChipEntry_Object = MibTableRow
ciscoFlashChipEntry = _CiscoFlashChipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3, 1, 1)
)
ciscoFlashChipEntry.setIndexNames(
    (0, "CISCO-FLASH-MIB", "ciscoFlashDeviceIndex"),
    (0, "CISCO-FLASH-MIB", "ciscoFlashChipIndex"),
)
if mibBuilder.loadTexts:
    ciscoFlashChipEntry.setStatus("current")


class _CiscoFlashChipIndex_Type(Integer32):
    """Custom type ciscoFlashChipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CiscoFlashChipIndex_Type.__name__ = "Integer32"
_CiscoFlashChipIndex_Object = MibTableColumn
ciscoFlashChipIndex = _CiscoFlashChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3, 1, 1, 1),
    _CiscoFlashChipIndex_Type()
)
ciscoFlashChipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoFlashChipIndex.setStatus("current")


class _CiscoFlashChipCode_Type(DisplayString):
    """Custom type ciscoFlashChipCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CiscoFlashChipCode_Type.__name__ = "DisplayString"
_CiscoFlashChipCode_Object = MibTableColumn
ciscoFlashChipCode = _CiscoFlashChipCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3, 1, 1, 2),
    _CiscoFlashChipCode_Type()
)
ciscoFlashChipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashChipCode.setStatus("current")


class _CiscoFlashChipDescr_Type(DisplayString):
    """Custom type ciscoFlashChipDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiscoFlashChipDescr_Type.__name__ = "DisplayString"
_CiscoFlashChipDescr_Object = MibTableColumn
ciscoFlashChipDescr = _CiscoFlashChipDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3, 1, 1, 3),
    _CiscoFlashChipDescr_Type()
)
ciscoFlashChipDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashChipDescr.setStatus("current")
_CiscoFlashChipWriteRetries_Type = Counter32
_CiscoFlashChipWriteRetries_Object = MibTableColumn
ciscoFlashChipWriteRetries = _CiscoFlashChipWriteRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3, 1, 1, 4),
    _CiscoFlashChipWriteRetries_Type()
)
ciscoFlashChipWriteRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashChipWriteRetries.setStatus("current")
_CiscoFlashChipEraseRetries_Type = Counter32
_CiscoFlashChipEraseRetries_Object = MibTableColumn
ciscoFlashChipEraseRetries = _CiscoFlashChipEraseRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3, 1, 1, 5),
    _CiscoFlashChipEraseRetries_Type()
)
ciscoFlashChipEraseRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashChipEraseRetries.setStatus("current")
_CiscoFlashChipMaxWriteRetries_Type = Unsigned32
_CiscoFlashChipMaxWriteRetries_Object = MibTableColumn
ciscoFlashChipMaxWriteRetries = _CiscoFlashChipMaxWriteRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3, 1, 1, 6),
    _CiscoFlashChipMaxWriteRetries_Type()
)
ciscoFlashChipMaxWriteRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashChipMaxWriteRetries.setStatus("current")
_CiscoFlashChipMaxEraseRetries_Type = Unsigned32
_CiscoFlashChipMaxEraseRetries_Object = MibTableColumn
ciscoFlashChipMaxEraseRetries = _CiscoFlashChipMaxEraseRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 3, 1, 1, 7),
    _CiscoFlashChipMaxEraseRetries_Type()
)
ciscoFlashChipMaxEraseRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashChipMaxEraseRetries.setStatus("current")
_CiscoFlashPartitions_ObjectIdentity = ObjectIdentity
ciscoFlashPartitions = _CiscoFlashPartitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4)
)
_CiscoFlashPartitionTable_Object = MibTable
ciscoFlashPartitionTable = _CiscoFlashPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoFlashPartitionTable.setStatus("current")
_CiscoFlashPartitionEntry_Object = MibTableRow
ciscoFlashPartitionEntry = _CiscoFlashPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1)
)
ciscoFlashPartitionEntry.setIndexNames(
    (0, "CISCO-FLASH-MIB", "ciscoFlashDeviceIndex"),
    (0, "CISCO-FLASH-MIB", "ciscoFlashPartitionIndex"),
)
if mibBuilder.loadTexts:
    ciscoFlashPartitionEntry.setStatus("current")


class _CiscoFlashPartitionIndex_Type(Unsigned32):
    """Custom type ciscoFlashPartitionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoFlashPartitionIndex_Type.__name__ = "Unsigned32"
_CiscoFlashPartitionIndex_Object = MibTableColumn
ciscoFlashPartitionIndex = _CiscoFlashPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 1),
    _CiscoFlashPartitionIndex_Type()
)
ciscoFlashPartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoFlashPartitionIndex.setStatus("current")


class _CiscoFlashPartitionStartChip_Type(Integer32):
    """Custom type ciscoFlashPartitionStartChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CiscoFlashPartitionStartChip_Type.__name__ = "Integer32"
_CiscoFlashPartitionStartChip_Object = MibTableColumn
ciscoFlashPartitionStartChip = _CiscoFlashPartitionStartChip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 2),
    _CiscoFlashPartitionStartChip_Type()
)
ciscoFlashPartitionStartChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionStartChip.setStatus("current")


class _CiscoFlashPartitionEndChip_Type(Integer32):
    """Custom type ciscoFlashPartitionEndChip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CiscoFlashPartitionEndChip_Type.__name__ = "Integer32"
_CiscoFlashPartitionEndChip_Object = MibTableColumn
ciscoFlashPartitionEndChip = _CiscoFlashPartitionEndChip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 3),
    _CiscoFlashPartitionEndChip_Type()
)
ciscoFlashPartitionEndChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionEndChip.setStatus("current")


class _CiscoFlashPartitionSize_Type(Unsigned32):
    """Custom type ciscoFlashPartitionSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoFlashPartitionSize_Type.__name__ = "Unsigned32"
_CiscoFlashPartitionSize_Object = MibTableColumn
ciscoFlashPartitionSize = _CiscoFlashPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 4),
    _CiscoFlashPartitionSize_Type()
)
ciscoFlashPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionSize.setStatus("current")
if mibBuilder.loadTexts:
    ciscoFlashPartitionSize.setUnits("bytes")
_CiscoFlashPartitionFreeSpace_Type = Gauge32
_CiscoFlashPartitionFreeSpace_Object = MibTableColumn
ciscoFlashPartitionFreeSpace = _CiscoFlashPartitionFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 5),
    _CiscoFlashPartitionFreeSpace_Type()
)
ciscoFlashPartitionFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    ciscoFlashPartitionFreeSpace.setUnits("bytes")
_CiscoFlashPartitionFileCount_Type = Gauge32
_CiscoFlashPartitionFileCount_Object = MibTableColumn
ciscoFlashPartitionFileCount = _CiscoFlashPartitionFileCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 6),
    _CiscoFlashPartitionFileCount_Type()
)
ciscoFlashPartitionFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionFileCount.setStatus("current")


class _CiscoFlashPartitionChecksumAlgorithm_Type(Integer32):
    """Custom type ciscoFlashPartitionChecksumAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("simpleCRC", 3),
          ("simpleChecksum", 1),
          ("undefined", 2))
    )


_CiscoFlashPartitionChecksumAlgorithm_Type.__name__ = "Integer32"
_CiscoFlashPartitionChecksumAlgorithm_Object = MibTableColumn
ciscoFlashPartitionChecksumAlgorithm = _CiscoFlashPartitionChecksumAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 7),
    _CiscoFlashPartitionChecksumAlgorithm_Type()
)
ciscoFlashPartitionChecksumAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionChecksumAlgorithm.setStatus("current")


class _CiscoFlashPartitionStatus_Type(Integer32):
    """Custom type ciscoFlashPartitionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 3),
          ("runFromFlash", 2))
    )


_CiscoFlashPartitionStatus_Type.__name__ = "Integer32"
_CiscoFlashPartitionStatus_Object = MibTableColumn
ciscoFlashPartitionStatus = _CiscoFlashPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 8),
    _CiscoFlashPartitionStatus_Type()
)
ciscoFlashPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionStatus.setStatus("current")


class _CiscoFlashPartitionUpgradeMethod_Type(Integer32):
    """Custom type ciscoFlashPartitionUpgradeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 3),
          ("rxbootFLH", 2),
          ("unknown", 1))
    )


_CiscoFlashPartitionUpgradeMethod_Type.__name__ = "Integer32"
_CiscoFlashPartitionUpgradeMethod_Object = MibTableColumn
ciscoFlashPartitionUpgradeMethod = _CiscoFlashPartitionUpgradeMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 9),
    _CiscoFlashPartitionUpgradeMethod_Type()
)
ciscoFlashPartitionUpgradeMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionUpgradeMethod.setStatus("current")


class _CiscoFlashPartitionName_Type(DisplayString):
    """Custom type ciscoFlashPartitionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CiscoFlashPartitionName_Type.__name__ = "DisplayString"
_CiscoFlashPartitionName_Object = MibTableColumn
ciscoFlashPartitionName = _CiscoFlashPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 10),
    _CiscoFlashPartitionName_Type()
)
ciscoFlashPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionName.setStatus("current")
_CiscoFlashPartitionNeedErasure_Type = TruthValue
_CiscoFlashPartitionNeedErasure_Object = MibTableColumn
ciscoFlashPartitionNeedErasure = _CiscoFlashPartitionNeedErasure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 11),
    _CiscoFlashPartitionNeedErasure_Type()
)
ciscoFlashPartitionNeedErasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionNeedErasure.setStatus("current")


class _CiscoFlashPartitionFileNameLength_Type(Integer32):
    """Custom type ciscoFlashPartitionFileNameLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CiscoFlashPartitionFileNameLength_Type.__name__ = "Integer32"
_CiscoFlashPartitionFileNameLength_Object = MibTableColumn
ciscoFlashPartitionFileNameLength = _CiscoFlashPartitionFileNameLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 12),
    _CiscoFlashPartitionFileNameLength_Type()
)
ciscoFlashPartitionFileNameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionFileNameLength.setStatus("current")
_CiscoFlashPartitionSizeExtended_Type = CounterBasedGauge64
_CiscoFlashPartitionSizeExtended_Object = MibTableColumn
ciscoFlashPartitionSizeExtended = _CiscoFlashPartitionSizeExtended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 13),
    _CiscoFlashPartitionSizeExtended_Type()
)
ciscoFlashPartitionSizeExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionSizeExtended.setStatus("current")
if mibBuilder.loadTexts:
    ciscoFlashPartitionSizeExtended.setUnits("bytes")
_CiscoFlashPartitionFreeSpaceExtended_Type = CounterBasedGauge64
_CiscoFlashPartitionFreeSpaceExtended_Object = MibTableColumn
ciscoFlashPartitionFreeSpaceExtended = _CiscoFlashPartitionFreeSpaceExtended_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 14),
    _CiscoFlashPartitionFreeSpaceExtended_Type()
)
ciscoFlashPartitionFreeSpaceExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitionFreeSpaceExtended.setStatus("current")
if mibBuilder.loadTexts:
    ciscoFlashPartitionFreeSpaceExtended.setUnits("bytes")
_CiscoFlashPartitionLowSpaceNotifThreshold_Type = Percent
_CiscoFlashPartitionLowSpaceNotifThreshold_Object = MibTableColumn
ciscoFlashPartitionLowSpaceNotifThreshold = _CiscoFlashPartitionLowSpaceNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 1, 1, 15),
    _CiscoFlashPartitionLowSpaceNotifThreshold_Type()
)
ciscoFlashPartitionLowSpaceNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoFlashPartitionLowSpaceNotifThreshold.setStatus("current")
_CiscoFlashFiles_ObjectIdentity = ObjectIdentity
ciscoFlashFiles = _CiscoFlashFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2)
)
_CiscoFlashFileTable_Object = MibTable
ciscoFlashFileTable = _CiscoFlashFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoFlashFileTable.setStatus("current")
_CiscoFlashFileEntry_Object = MibTableRow
ciscoFlashFileEntry = _CiscoFlashFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 1, 1)
)
ciscoFlashFileEntry.setIndexNames(
    (0, "CISCO-FLASH-MIB", "ciscoFlashDeviceIndex"),
    (0, "CISCO-FLASH-MIB", "ciscoFlashPartitionIndex"),
    (0, "CISCO-FLASH-MIB", "ciscoFlashFileIndex"),
)
if mibBuilder.loadTexts:
    ciscoFlashFileEntry.setStatus("current")


class _CiscoFlashFileIndex_Type(Unsigned32):
    """Custom type ciscoFlashFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoFlashFileIndex_Type.__name__ = "Unsigned32"
_CiscoFlashFileIndex_Object = MibTableColumn
ciscoFlashFileIndex = _CiscoFlashFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 1, 1, 1),
    _CiscoFlashFileIndex_Type()
)
ciscoFlashFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoFlashFileIndex.setStatus("current")
_CiscoFlashFileSize_Type = Unsigned32
_CiscoFlashFileSize_Object = MibTableColumn
ciscoFlashFileSize = _CiscoFlashFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 1, 1, 2),
    _CiscoFlashFileSize_Type()
)
ciscoFlashFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileSize.setStatus("current")
if mibBuilder.loadTexts:
    ciscoFlashFileSize.setUnits("bytes")
_CiscoFlashFileChecksum_Type = ChecksumString
_CiscoFlashFileChecksum_Object = MibTableColumn
ciscoFlashFileChecksum = _CiscoFlashFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 1, 1, 3),
    _CiscoFlashFileChecksum_Type()
)
ciscoFlashFileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileChecksum.setStatus("current")


class _CiscoFlashFileStatus_Type(Integer32):
    """Custom type ciscoFlashFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("invalidChecksum", 2),
          ("valid", 3))
    )


_CiscoFlashFileStatus_Type.__name__ = "Integer32"
_CiscoFlashFileStatus_Object = MibTableColumn
ciscoFlashFileStatus = _CiscoFlashFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 1, 1, 4),
    _CiscoFlashFileStatus_Type()
)
ciscoFlashFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileStatus.setStatus("current")


class _CiscoFlashFileName_Type(DisplayString):
    """Custom type ciscoFlashFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiscoFlashFileName_Type.__name__ = "DisplayString"
_CiscoFlashFileName_Object = MibTableColumn
ciscoFlashFileName = _CiscoFlashFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 1, 1, 5),
    _CiscoFlashFileName_Type()
)
ciscoFlashFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileName.setStatus("current")
_CiscoFlashFileType_Type = FlashFileType
_CiscoFlashFileType_Object = MibTableColumn
ciscoFlashFileType = _CiscoFlashFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 1, 1, 6),
    _CiscoFlashFileType_Type()
)
ciscoFlashFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileType.setStatus("current")
_CiscoFlashFileDate_Type = DateAndTime
_CiscoFlashFileDate_Object = MibTableColumn
ciscoFlashFileDate = _CiscoFlashFileDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 1, 1, 7),
    _CiscoFlashFileDate_Type()
)
ciscoFlashFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileDate.setStatus("current")
_CiscoFlashFileByTypeTable_Object = MibTable
ciscoFlashFileByTypeTable = _CiscoFlashFileByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoFlashFileByTypeTable.setStatus("current")
_CiscoFlashFileByTypeEntry_Object = MibTableRow
ciscoFlashFileByTypeEntry = _CiscoFlashFileByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 2, 1)
)
ciscoFlashFileByTypeEntry.setIndexNames(
    (0, "CISCO-FLASH-MIB", "ciscoFlashFileType"),
    (0, "CISCO-FLASH-MIB", "ciscoFlashDeviceIndex"),
    (0, "CISCO-FLASH-MIB", "ciscoFlashPartitionIndex"),
    (0, "CISCO-FLASH-MIB", "ciscoFlashFileIndex"),
)
if mibBuilder.loadTexts:
    ciscoFlashFileByTypeEntry.setStatus("current")
_CiscoFlashFileByTypeSize_Type = Unsigned32
_CiscoFlashFileByTypeSize_Object = MibTableColumn
ciscoFlashFileByTypeSize = _CiscoFlashFileByTypeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 2, 1, 1),
    _CiscoFlashFileByTypeSize_Type()
)
ciscoFlashFileByTypeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileByTypeSize.setStatus("current")
if mibBuilder.loadTexts:
    ciscoFlashFileByTypeSize.setUnits("bytes")
_CiscoFlashFileByTypeChecksum_Type = ChecksumString
_CiscoFlashFileByTypeChecksum_Object = MibTableColumn
ciscoFlashFileByTypeChecksum = _CiscoFlashFileByTypeChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 2, 1, 2),
    _CiscoFlashFileByTypeChecksum_Type()
)
ciscoFlashFileByTypeChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileByTypeChecksum.setStatus("current")


class _CiscoFlashFileByTypeStatus_Type(Integer32):
    """Custom type ciscoFlashFileByTypeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("invalidChecksum", 2),
          ("valid", 3))
    )


_CiscoFlashFileByTypeStatus_Type.__name__ = "Integer32"
_CiscoFlashFileByTypeStatus_Object = MibTableColumn
ciscoFlashFileByTypeStatus = _CiscoFlashFileByTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 2, 1, 3),
    _CiscoFlashFileByTypeStatus_Type()
)
ciscoFlashFileByTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileByTypeStatus.setStatus("current")


class _CiscoFlashFileByTypeName_Type(DisplayString):
    """Custom type ciscoFlashFileByTypeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiscoFlashFileByTypeName_Type.__name__ = "DisplayString"
_CiscoFlashFileByTypeName_Object = MibTableColumn
ciscoFlashFileByTypeName = _CiscoFlashFileByTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 2, 1, 4),
    _CiscoFlashFileByTypeName_Type()
)
ciscoFlashFileByTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileByTypeName.setStatus("current")
_CiscoFlashFileByTypeDate_Type = DateAndTime
_CiscoFlashFileByTypeDate_Object = MibTableColumn
ciscoFlashFileByTypeDate = _CiscoFlashFileByTypeDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 1, 4, 2, 2, 1, 5),
    _CiscoFlashFileByTypeDate_Type()
)
ciscoFlashFileByTypeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashFileByTypeDate.setStatus("current")
_CiscoFlashOps_ObjectIdentity = ObjectIdentity
ciscoFlashOps = _CiscoFlashOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2)
)
_CiscoFlashCopyTable_Object = MibTable
ciscoFlashCopyTable = _CiscoFlashCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoFlashCopyTable.setStatus("current")
_CiscoFlashCopyEntry_Object = MibTableRow
ciscoFlashCopyEntry = _CiscoFlashCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1)
)
ciscoFlashCopyEntry.setIndexNames(
    (0, "CISCO-FLASH-MIB", "ciscoFlashCopySerialNumber"),
)
if mibBuilder.loadTexts:
    ciscoFlashCopyEntry.setStatus("current")


class _CiscoFlashCopySerialNumber_Type(Integer32):
    """Custom type ciscoFlashCopySerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoFlashCopySerialNumber_Type.__name__ = "Integer32"
_CiscoFlashCopySerialNumber_Object = MibTableColumn
ciscoFlashCopySerialNumber = _CiscoFlashCopySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 1),
    _CiscoFlashCopySerialNumber_Type()
)
ciscoFlashCopySerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoFlashCopySerialNumber.setStatus("current")


class _CiscoFlashCopyCommand_Type(Integer32):
    """Custom type ciscoFlashCopyCommand based on Integer32"""
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
        *(("copyFromFlash", 3),
          ("copyFromFlhLog", 4),
          ("copyToFlashWithErase", 1),
          ("copyToFlashWithoutErase", 2))
    )


_CiscoFlashCopyCommand_Type.__name__ = "Integer32"
_CiscoFlashCopyCommand_Object = MibTableColumn
ciscoFlashCopyCommand = _CiscoFlashCopyCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 2),
    _CiscoFlashCopyCommand_Type()
)
ciscoFlashCopyCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyCommand.setStatus("current")


class _CiscoFlashCopyProtocol_Type(Integer32):
    """Custom type ciscoFlashCopyProtocol based on Integer32"""
    defaultValue = 1

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
        *(("ftp", 4),
          ("lex", 3),
          ("rcp", 2),
          ("scp", 5),
          ("sftp", 6),
          ("tftp", 1))
    )


_CiscoFlashCopyProtocol_Type.__name__ = "Integer32"
_CiscoFlashCopyProtocol_Object = MibTableColumn
ciscoFlashCopyProtocol = _CiscoFlashCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 3),
    _CiscoFlashCopyProtocol_Type()
)
ciscoFlashCopyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyProtocol.setStatus("current")


class _CiscoFlashCopyServerAddress_Type(IpAddress):
    """Custom type ciscoFlashCopyServerAddress based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_CiscoFlashCopyServerAddress_Object = MibTableColumn
ciscoFlashCopyServerAddress = _CiscoFlashCopyServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 4),
    _CiscoFlashCopyServerAddress_Type()
)
ciscoFlashCopyServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyServerAddress.setStatus("deprecated")


class _CiscoFlashCopySourceName_Type(DisplayString):
    """Custom type ciscoFlashCopySourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiscoFlashCopySourceName_Type.__name__ = "DisplayString"
_CiscoFlashCopySourceName_Object = MibTableColumn
ciscoFlashCopySourceName = _CiscoFlashCopySourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 5),
    _CiscoFlashCopySourceName_Type()
)
ciscoFlashCopySourceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopySourceName.setStatus("current")


class _CiscoFlashCopyDestinationName_Type(DisplayString):
    """Custom type ciscoFlashCopyDestinationName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoFlashCopyDestinationName_Type.__name__ = "DisplayString"
_CiscoFlashCopyDestinationName_Object = MibTableColumn
ciscoFlashCopyDestinationName = _CiscoFlashCopyDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 6),
    _CiscoFlashCopyDestinationName_Type()
)
ciscoFlashCopyDestinationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyDestinationName.setStatus("current")


class _CiscoFlashCopyRemoteUserName_Type(DisplayString):
    """Custom type ciscoFlashCopyRemoteUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiscoFlashCopyRemoteUserName_Type.__name__ = "DisplayString"
_CiscoFlashCopyRemoteUserName_Object = MibTableColumn
ciscoFlashCopyRemoteUserName = _CiscoFlashCopyRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 7),
    _CiscoFlashCopyRemoteUserName_Type()
)
ciscoFlashCopyRemoteUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyRemoteUserName.setStatus("current")


class _CiscoFlashCopyStatus_Type(Integer32):
    """Custom type ciscoFlashCopyStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("copyDeviceBusy", 8),
          ("copyDeviceError", 10),
          ("copyDeviceFull", 12),
          ("copyDeviceNotProgrammable", 11),
          ("copyDeviceOpenError", 9),
          ("copyFileChecksumError", 15),
          ("copyFileOpenError", 13),
          ("copyFileTransferError", 14),
          ("copyInProgress", 1),
          ("copyInvalidDestName", 6),
          ("copyInvalidOperation", 3),
          ("copyInvalidProtocol", 4),
          ("copyInvalidServerAddress", 7),
          ("copyInvalidSignature", 18),
          ("copyInvalidSourceName", 5),
          ("copyNoMemory", 16),
          ("copyOperationPending", 0),
          ("copyOperationSuccess", 2),
          ("copyProhibited", 19),
          ("copyUnknownFailure", 17))
    )


_CiscoFlashCopyStatus_Type.__name__ = "Integer32"
_CiscoFlashCopyStatus_Object = MibTableColumn
ciscoFlashCopyStatus = _CiscoFlashCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 8),
    _CiscoFlashCopyStatus_Type()
)
ciscoFlashCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashCopyStatus.setStatus("current")


class _CiscoFlashCopyNotifyOnCompletion_Type(TruthValue):
    """Custom type ciscoFlashCopyNotifyOnCompletion based on TruthValue"""


_CiscoFlashCopyNotifyOnCompletion_Object = MibTableColumn
ciscoFlashCopyNotifyOnCompletion = _CiscoFlashCopyNotifyOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 9),
    _CiscoFlashCopyNotifyOnCompletion_Type()
)
ciscoFlashCopyNotifyOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyNotifyOnCompletion.setStatus("current")
_CiscoFlashCopyTime_Type = TimeTicks
_CiscoFlashCopyTime_Object = MibTableColumn
ciscoFlashCopyTime = _CiscoFlashCopyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 10),
    _CiscoFlashCopyTime_Type()
)
ciscoFlashCopyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashCopyTime.setStatus("current")
_CiscoFlashCopyEntryStatus_Type = RowStatus
_CiscoFlashCopyEntryStatus_Object = MibTableColumn
ciscoFlashCopyEntryStatus = _CiscoFlashCopyEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 11),
    _CiscoFlashCopyEntryStatus_Type()
)
ciscoFlashCopyEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyEntryStatus.setStatus("current")


class _CiscoFlashCopyVerify_Type(TruthValue):
    """Custom type ciscoFlashCopyVerify based on TruthValue"""


_CiscoFlashCopyVerify_Object = MibTableColumn
ciscoFlashCopyVerify = _CiscoFlashCopyVerify_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 12),
    _CiscoFlashCopyVerify_Type()
)
ciscoFlashCopyVerify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyVerify.setStatus("current")


class _CiscoFlashCopyServerAddrType_Type(InetAddressType):
    """Custom type ciscoFlashCopyServerAddrType based on InetAddressType"""


_CiscoFlashCopyServerAddrType_Object = MibTableColumn
ciscoFlashCopyServerAddrType = _CiscoFlashCopyServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 13),
    _CiscoFlashCopyServerAddrType_Type()
)
ciscoFlashCopyServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyServerAddrType.setStatus("current")


class _CiscoFlashCopyServerAddrRev1_Type(InetAddress):
    """Custom type ciscoFlashCopyServerAddrRev1 based on InetAddress"""
    defaultHexValue = "FFFFFFFF"


_CiscoFlashCopyServerAddrRev1_Object = MibTableColumn
ciscoFlashCopyServerAddrRev1 = _CiscoFlashCopyServerAddrRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 14),
    _CiscoFlashCopyServerAddrRev1_Type()
)
ciscoFlashCopyServerAddrRev1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyServerAddrRev1.setStatus("current")


class _CiscoFlashCopyRemotePassword_Type(DisplayString):
    """Custom type ciscoFlashCopyRemotePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CiscoFlashCopyRemotePassword_Type.__name__ = "DisplayString"
_CiscoFlashCopyRemotePassword_Object = MibTableColumn
ciscoFlashCopyRemotePassword = _CiscoFlashCopyRemotePassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 1, 1, 15),
    _CiscoFlashCopyRemotePassword_Type()
)
ciscoFlashCopyRemotePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashCopyRemotePassword.setStatus("current")
_CiscoFlashPartitioningTable_Object = MibTable
ciscoFlashPartitioningTable = _CiscoFlashPartitioningTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoFlashPartitioningTable.setStatus("current")
_CiscoFlashPartitioningEntry_Object = MibTableRow
ciscoFlashPartitioningEntry = _CiscoFlashPartitioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1)
)
ciscoFlashPartitioningEntry.setIndexNames(
    (0, "CISCO-FLASH-MIB", "ciscoFlashPartitioningSerialNumber"),
)
if mibBuilder.loadTexts:
    ciscoFlashPartitioningEntry.setStatus("current")


class _CiscoFlashPartitioningSerialNumber_Type(Integer32):
    """Custom type ciscoFlashPartitioningSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoFlashPartitioningSerialNumber_Type.__name__ = "Integer32"
_CiscoFlashPartitioningSerialNumber_Object = MibTableColumn
ciscoFlashPartitioningSerialNumber = _CiscoFlashPartitioningSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1, 1),
    _CiscoFlashPartitioningSerialNumber_Type()
)
ciscoFlashPartitioningSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoFlashPartitioningSerialNumber.setStatus("current")


class _CiscoFlashPartitioningCommand_Type(Integer32):
    """Custom type ciscoFlashPartitioningCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("partition", 1)
    )


_CiscoFlashPartitioningCommand_Type.__name__ = "Integer32"
_CiscoFlashPartitioningCommand_Object = MibTableColumn
ciscoFlashPartitioningCommand = _CiscoFlashPartitioningCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1, 2),
    _CiscoFlashPartitioningCommand_Type()
)
ciscoFlashPartitioningCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashPartitioningCommand.setStatus("current")


class _CiscoFlashPartitioningDestinationName_Type(DisplayString):
    """Custom type ciscoFlashPartitioningDestinationName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoFlashPartitioningDestinationName_Type.__name__ = "DisplayString"
_CiscoFlashPartitioningDestinationName_Object = MibTableColumn
ciscoFlashPartitioningDestinationName = _CiscoFlashPartitioningDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1, 3),
    _CiscoFlashPartitioningDestinationName_Type()
)
ciscoFlashPartitioningDestinationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashPartitioningDestinationName.setStatus("current")


class _CiscoFlashPartitioningPartitionCount_Type(Unsigned32):
    """Custom type ciscoFlashPartitioningPartitionCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoFlashPartitioningPartitionCount_Type.__name__ = "Unsigned32"
_CiscoFlashPartitioningPartitionCount_Object = MibTableColumn
ciscoFlashPartitioningPartitionCount = _CiscoFlashPartitioningPartitionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1, 4),
    _CiscoFlashPartitioningPartitionCount_Type()
)
ciscoFlashPartitioningPartitionCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashPartitioningPartitionCount.setStatus("current")


class _CiscoFlashPartitioningPartitionSizes_Type(DisplayString):
    """Custom type ciscoFlashPartitioningPartitionSizes based on DisplayString"""
    defaultHexValue = ""


_CiscoFlashPartitioningPartitionSizes_Object = MibTableColumn
ciscoFlashPartitioningPartitionSizes = _CiscoFlashPartitioningPartitionSizes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1, 5),
    _CiscoFlashPartitioningPartitionSizes_Type()
)
ciscoFlashPartitioningPartitionSizes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashPartitioningPartitionSizes.setStatus("current")


class _CiscoFlashPartitioningStatus_Type(Integer32):
    """Custom type ciscoFlashPartitioningStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("partitioningDeviceBusy", 7),
          ("partitioningDeviceError", 9),
          ("partitioningDeviceOpenError", 8),
          ("partitioningInProgress", 1),
          ("partitioningInvalidDestName", 4),
          ("partitioningInvalidOperation", 3),
          ("partitioningInvalidPartitionCount", 5),
          ("partitioningInvalidPartitionSizes", 6),
          ("partitioningNoMemory", 10),
          ("partitioningOperationSuccess", 2),
          ("partitioningUnknownFailure", 11))
    )


_CiscoFlashPartitioningStatus_Type.__name__ = "Integer32"
_CiscoFlashPartitioningStatus_Object = MibTableColumn
ciscoFlashPartitioningStatus = _CiscoFlashPartitioningStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1, 6),
    _CiscoFlashPartitioningStatus_Type()
)
ciscoFlashPartitioningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitioningStatus.setStatus("current")


class _CiscoFlashPartitioningNotifyOnCompletion_Type(TruthValue):
    """Custom type ciscoFlashPartitioningNotifyOnCompletion based on TruthValue"""


_CiscoFlashPartitioningNotifyOnCompletion_Object = MibTableColumn
ciscoFlashPartitioningNotifyOnCompletion = _CiscoFlashPartitioningNotifyOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1, 7),
    _CiscoFlashPartitioningNotifyOnCompletion_Type()
)
ciscoFlashPartitioningNotifyOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashPartitioningNotifyOnCompletion.setStatus("current")
_CiscoFlashPartitioningTime_Type = TimeTicks
_CiscoFlashPartitioningTime_Object = MibTableColumn
ciscoFlashPartitioningTime = _CiscoFlashPartitioningTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1, 8),
    _CiscoFlashPartitioningTime_Type()
)
ciscoFlashPartitioningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashPartitioningTime.setStatus("current")
_CiscoFlashPartitioningEntryStatus_Type = RowStatus
_CiscoFlashPartitioningEntryStatus_Object = MibTableColumn
ciscoFlashPartitioningEntryStatus = _CiscoFlashPartitioningEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 2, 1, 9),
    _CiscoFlashPartitioningEntryStatus_Type()
)
ciscoFlashPartitioningEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashPartitioningEntryStatus.setStatus("current")
_CiscoFlashMiscOpTable_Object = MibTable
ciscoFlashMiscOpTable = _CiscoFlashMiscOpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ciscoFlashMiscOpTable.setStatus("current")
_CiscoFlashMiscOpEntry_Object = MibTableRow
ciscoFlashMiscOpEntry = _CiscoFlashMiscOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 3, 1)
)
ciscoFlashMiscOpEntry.setIndexNames(
    (0, "CISCO-FLASH-MIB", "ciscoFlashMiscOpSerialNumber"),
)
if mibBuilder.loadTexts:
    ciscoFlashMiscOpEntry.setStatus("current")


class _CiscoFlashMiscOpSerialNumber_Type(Integer32):
    """Custom type ciscoFlashMiscOpSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoFlashMiscOpSerialNumber_Type.__name__ = "Integer32"
_CiscoFlashMiscOpSerialNumber_Object = MibTableColumn
ciscoFlashMiscOpSerialNumber = _CiscoFlashMiscOpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 3, 1, 1),
    _CiscoFlashMiscOpSerialNumber_Type()
)
ciscoFlashMiscOpSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoFlashMiscOpSerialNumber.setStatus("current")


class _CiscoFlashMiscOpCommand_Type(Integer32):
    """Custom type ciscoFlashMiscOpCommand based on Integer32"""
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
        *(("delete", 3),
          ("erase", 1),
          ("format", 6),
          ("squeeze", 5),
          ("undelete", 4),
          ("verify", 2))
    )


_CiscoFlashMiscOpCommand_Type.__name__ = "Integer32"
_CiscoFlashMiscOpCommand_Object = MibTableColumn
ciscoFlashMiscOpCommand = _CiscoFlashMiscOpCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 3, 1, 2),
    _CiscoFlashMiscOpCommand_Type()
)
ciscoFlashMiscOpCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashMiscOpCommand.setStatus("current")


class _CiscoFlashMiscOpDestinationName_Type(DisplayString):
    """Custom type ciscoFlashMiscOpDestinationName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoFlashMiscOpDestinationName_Type.__name__ = "DisplayString"
_CiscoFlashMiscOpDestinationName_Object = MibTableColumn
ciscoFlashMiscOpDestinationName = _CiscoFlashMiscOpDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 3, 1, 3),
    _CiscoFlashMiscOpDestinationName_Type()
)
ciscoFlashMiscOpDestinationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashMiscOpDestinationName.setStatus("current")


class _CiscoFlashMiscOpStatus_Type(Integer32):
    """Custom type ciscoFlashMiscOpStatus based on Integer32"""
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
              14,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("miscOpDeviceBusy", 5),
          ("miscOpDeviceError", 7),
          ("miscOpDeviceNotProgrammable", 8),
          ("miscOpDeviceOpenError", 6),
          ("miscOpFileChecksumError", 12),
          ("miscOpFileDeleteFailure", 10),
          ("miscOpFileOpenError", 9),
          ("miscOpFileUndeleteFailure", 11),
          ("miscOpFormatFailure", 20),
          ("miscOpInProgress", 1),
          ("miscOpInvalidDestName", 4),
          ("miscOpInvalidOperation", 3),
          ("miscOpNoMemory", 13),
          ("miscOpNoSuchFile", 19),
          ("miscOpOperationSuccess", 2),
          ("miscOpSqueezeFailure", 18),
          ("miscOpUnknownFailure", 14))
    )


_CiscoFlashMiscOpStatus_Type.__name__ = "Integer32"
_CiscoFlashMiscOpStatus_Object = MibTableColumn
ciscoFlashMiscOpStatus = _CiscoFlashMiscOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 3, 1, 4),
    _CiscoFlashMiscOpStatus_Type()
)
ciscoFlashMiscOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashMiscOpStatus.setStatus("current")


class _CiscoFlashMiscOpNotifyOnCompletion_Type(TruthValue):
    """Custom type ciscoFlashMiscOpNotifyOnCompletion based on TruthValue"""


_CiscoFlashMiscOpNotifyOnCompletion_Object = MibTableColumn
ciscoFlashMiscOpNotifyOnCompletion = _CiscoFlashMiscOpNotifyOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 3, 1, 5),
    _CiscoFlashMiscOpNotifyOnCompletion_Type()
)
ciscoFlashMiscOpNotifyOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashMiscOpNotifyOnCompletion.setStatus("current")
_CiscoFlashMiscOpTime_Type = TimeTicks
_CiscoFlashMiscOpTime_Object = MibTableColumn
ciscoFlashMiscOpTime = _CiscoFlashMiscOpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 3, 1, 6),
    _CiscoFlashMiscOpTime_Type()
)
ciscoFlashMiscOpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoFlashMiscOpTime.setStatus("current")
_CiscoFlashMiscOpEntryStatus_Type = RowStatus
_CiscoFlashMiscOpEntryStatus_Object = MibTableColumn
ciscoFlashMiscOpEntryStatus = _CiscoFlashMiscOpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 2, 3, 1, 7),
    _CiscoFlashMiscOpEntryStatus_Type()
)
ciscoFlashMiscOpEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoFlashMiscOpEntryStatus.setStatus("current")
_CiscoFlashMIBTrapPrefix_ObjectIdentity = ObjectIdentity
ciscoFlashMIBTrapPrefix = _CiscoFlashMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3)
)
_CiscoFlashMIBTraps_ObjectIdentity = ObjectIdentity
ciscoFlashMIBTraps = _CiscoFlashMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0)
)
_CiscoFlashCfg_ObjectIdentity = ObjectIdentity
ciscoFlashCfg = _CiscoFlashCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 4)
)


class _CiscoFlashCfgDevInsNotifEnable_Type(TruthValue):
    """Custom type ciscoFlashCfgDevInsNotifEnable based on TruthValue"""


_CiscoFlashCfgDevInsNotifEnable_Object = MibScalar
ciscoFlashCfgDevInsNotifEnable = _CiscoFlashCfgDevInsNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 4, 1),
    _CiscoFlashCfgDevInsNotifEnable_Type()
)
ciscoFlashCfgDevInsNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoFlashCfgDevInsNotifEnable.setStatus("current")


class _CiscoFlashCfgDevRemNotifEnable_Type(TruthValue):
    """Custom type ciscoFlashCfgDevRemNotifEnable based on TruthValue"""


_CiscoFlashCfgDevRemNotifEnable_Object = MibScalar
ciscoFlashCfgDevRemNotifEnable = _CiscoFlashCfgDevRemNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 4, 2),
    _CiscoFlashCfgDevRemNotifEnable_Type()
)
ciscoFlashCfgDevRemNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoFlashCfgDevRemNotifEnable.setStatus("current")
_CiscoFlashPartitionLowSpaceNotifEnable_Type = TruthValue
_CiscoFlashPartitionLowSpaceNotifEnable_Object = MibScalar
ciscoFlashPartitionLowSpaceNotifEnable = _CiscoFlashPartitionLowSpaceNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 4, 3),
    _CiscoFlashPartitionLowSpaceNotifEnable_Type()
)
ciscoFlashPartitionLowSpaceNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoFlashPartitionLowSpaceNotifEnable.setStatus("current")
_CiscoFlashMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFlashMIBConformance = _CiscoFlashMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2)
)
_CiscoFlashMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFlashMIBCompliances = _CiscoFlashMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1)
)
_CiscoFlashMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFlashMIBGroups = _CiscoFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2)
)

# Managed Objects groups

ciscoFlashDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 1)
)
ciscoFlashDeviceInfoGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashDevicesSupported"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceName"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceDescr"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceProgrammingJumper"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceInitTime"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceChipCount"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceRemovable"))
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceInfoGroup.setStatus("deprecated")

ciscoFlashDeviceOptionalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 2)
)
ciscoFlashDeviceOptionalInfoGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashDeviceMinPartitionSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceMaxPartitions"),
        ("CISCO-FLASH-MIB", "ciscoFlashDevicePartitions"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceController"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceCard"))
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceOptionalInfoGroup.setStatus("deprecated")

ciscoFlashChipInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 3)
)
ciscoFlashChipInfoGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashChipCode"),
        ("CISCO-FLASH-MIB", "ciscoFlashChipDescr"),
        ("CISCO-FLASH-MIB", "ciscoFlashChipWriteRetries"),
        ("CISCO-FLASH-MIB", "ciscoFlashChipEraseRetries"),
        ("CISCO-FLASH-MIB", "ciscoFlashChipMaxWriteRetries"),
        ("CISCO-FLASH-MIB", "ciscoFlashChipMaxEraseRetries"))
)
if mibBuilder.loadTexts:
    ciscoFlashChipInfoGroup.setStatus("current")

ciscoFlashPartitionInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 4)
)
ciscoFlashPartitionInfoGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashPartitionStartChip"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionEndChip"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionFreeSpace"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionFileCount"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionChecksumAlgorithm"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionUpgradeMethod"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionName"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionNeedErasure"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionFileNameLength"))
)
if mibBuilder.loadTexts:
    ciscoFlashPartitionInfoGroup.setStatus("deprecated")

ciscoFlashFileInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 5)
)
ciscoFlashFileInfoGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashFileSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileChecksum"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileName"))
)
if mibBuilder.loadTexts:
    ciscoFlashFileInfoGroup.setStatus("deprecated")

ciscoFlashCopyOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 6)
)
ciscoFlashCopyOpGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashCopyCommand"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyProtocol"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyServerAddress"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopySourceName"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyDestinationName"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyRemoteUserName"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyNotifyOnCompletion"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyTime"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoFlashCopyOpGroup.setStatus("deprecated")

ciscoFlashPartitioningOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 7)
)
ciscoFlashPartitioningOpGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashPartitioningCommand"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningDestinationName"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningPartitionCount"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningPartitionSizes"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningNotifyOnCompletion"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningTime"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoFlashPartitioningOpGroup.setStatus("current")

ciscoFlashMiscOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 8)
)
ciscoFlashMiscOpGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashMiscOpCommand"),
        ("CISCO-FLASH-MIB", "ciscoFlashMiscOpDestinationName"),
        ("CISCO-FLASH-MIB", "ciscoFlashMiscOpStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashMiscOpNotifyOnCompletion"),
        ("CISCO-FLASH-MIB", "ciscoFlashMiscOpTime"),
        ("CISCO-FLASH-MIB", "ciscoFlashMiscOpEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoFlashMiscOpGroup.setStatus("current")

ciscoFlashFileInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 10)
)
ciscoFlashFileInfoGroupRev1.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashFileSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileChecksum"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileName"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileType"))
)
if mibBuilder.loadTexts:
    ciscoFlashFileInfoGroupRev1.setStatus("current")

ciscoFlashDeviceInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 12)
)
ciscoFlashDeviceInfoGroupRev1.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashDevicesSupported"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceName"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceDescr"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceProgrammingJumper"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceInitTime"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceChipCount"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceRemovable"),
        ("CISCO-FLASH-MIB", "ciscoFlashCfgDevInsNotifEnable"),
        ("CISCO-FLASH-MIB", "ciscoFlashCfgDevRemNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceInfoGroupRev1.setStatus("deprecated")

ciscoFlashDeviceOptionalInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 13)
)
ciscoFlashDeviceOptionalInfoGroupRev1.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashDeviceMinPartitionSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceMaxPartitions"),
        ("CISCO-FLASH-MIB", "ciscoFlashDevicePartitions"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceController"),
        ("CISCO-FLASH-MIB", "ciscoFlashPhyEntIndex"))
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceOptionalInfoGroupRev1.setStatus("current")

ciscoFlashCopyOpGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 14)
)
ciscoFlashCopyOpGroupRev1.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashCopyCommand"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyProtocol"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyServerAddress"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopySourceName"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyDestinationName"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyRemoteUserName"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyNotifyOnCompletion"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyTime"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyEntryStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyVerify"))
)
if mibBuilder.loadTexts:
    ciscoFlashCopyOpGroupRev1.setStatus("deprecated")

ciscoFlashDeviceInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 15)
)
ciscoFlashDeviceInfoGroupRev2.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashDevicesSupported"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceNameExtended"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceDescr"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceProgrammingJumper"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceInitTime"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceChipCount"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceRemovable"),
        ("CISCO-FLASH-MIB", "ciscoFlashCfgDevInsNotifEnable"),
        ("CISCO-FLASH-MIB", "ciscoFlashCfgDevRemNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceInfoGroupRev2.setStatus("current")

ciscoFlashCopyOpGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 16)
)
ciscoFlashCopyOpGroupRev2.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashCopyCommand"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyProtocol"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopySourceName"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyDestinationName"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyRemoteUserName"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyNotifyOnCompletion"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyTime"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyEntryStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyVerify"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyServerAddrType"),
        ("CISCO-FLASH-MIB", "ciscoFlashCopyServerAddrRev1"))
)
if mibBuilder.loadTexts:
    ciscoFlashCopyOpGroupRev2.setStatus("current")

ciscoFlashCopyOpGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 18)
)
ciscoFlashCopyOpGroupRev3.setObjects(
    ("CISCO-FLASH-MIB", "ciscoFlashCopyRemotePassword")
)
if mibBuilder.loadTexts:
    ciscoFlashCopyOpGroupRev3.setStatus("current")

ciscoFlashFileInfoGroupSupp1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 19)
)
ciscoFlashFileInfoGroupSupp1.setObjects(
    ("CISCO-FLASH-MIB", "ciscoFlashFileDate")
)
if mibBuilder.loadTexts:
    ciscoFlashFileInfoGroupSupp1.setStatus("current")

ciscoFlashFileTypeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 20)
)
ciscoFlashFileTypeInfoGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashFileByTypeSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileByTypeChecksum"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileByTypeStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileByTypeName"),
        ("CISCO-FLASH-MIB", "ciscoFlashFileByTypeDate"))
)
if mibBuilder.loadTexts:
    ciscoFlashFileTypeInfoGroup.setStatus("current")

ciscoFlashDeviceInfoExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 21)
)
ciscoFlashDeviceInfoExtGroup.setObjects(
    ("CISCO-FLASH-MIB", "ciscoFlashDeviceSizeExtended")
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceInfoExtGroup.setStatus("current")

ciscoFlashPartitionInfoExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 22)
)
ciscoFlashPartitionInfoExtGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashPartitionSizeExtended"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionFreeSpaceExtended"))
)
if mibBuilder.loadTexts:
    ciscoFlashPartitionInfoExtGroup.setStatus("current")

ciscoFlashDeviceInfoExtGroupSupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 23)
)
ciscoFlashDeviceInfoExtGroupSupRev1.setObjects(
    ("CISCO-FLASH-MIB", "ciscoFlashDeviceMinPartitionSizeExtended")
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceInfoExtGroupSupRev1.setStatus("current")

ciscoFlashPartitionInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 24)
)
ciscoFlashPartitionInfoGroupRev1.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashPartitionStartChip"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionEndChip"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionFreeSpace"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionFileCount"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionChecksumAlgorithm"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionStatus"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionUpgradeMethod"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionName"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionNeedErasure"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionFileNameLength"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionLowSpaceNotifThreshold"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionLowSpaceNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoFlashPartitionInfoGroupRev1.setStatus("current")


# Notification objects

ciscoFlashCopyCompletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 1)
)
ciscoFlashCopyCompletionTrap.setObjects(
    ("CISCO-FLASH-MIB", "ciscoFlashCopyStatus")
)
if mibBuilder.loadTexts:
    ciscoFlashCopyCompletionTrap.setStatus(
        "current"
    )

ciscoFlashPartitioningCompletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 2)
)
ciscoFlashPartitioningCompletionTrap.setObjects(
    ("CISCO-FLASH-MIB", "ciscoFlashPartitioningStatus")
)
if mibBuilder.loadTexts:
    ciscoFlashPartitioningCompletionTrap.setStatus(
        "current"
    )

ciscoFlashMiscOpCompletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 3)
)
ciscoFlashMiscOpCompletionTrap.setObjects(
    ("CISCO-FLASH-MIB", "ciscoFlashMiscOpStatus")
)
if mibBuilder.loadTexts:
    ciscoFlashMiscOpCompletionTrap.setStatus(
        "current"
    )

ciscoFlashDeviceChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 4)
)
ciscoFlashDeviceChangeTrap.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashDeviceMinPartitionSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceName"))
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceChangeTrap.setStatus(
        "deprecated"
    )

ciscoFlashDeviceInsertedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 5)
)
ciscoFlashDeviceInsertedNotif.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashDeviceMinPartitionSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceName"))
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceInsertedNotif.setStatus(
        "deprecated"
    )

ciscoFlashDeviceRemovedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 6)
)
ciscoFlashDeviceRemovedNotif.setObjects(
    ("CISCO-FLASH-MIB", "ciscoFlashDeviceName")
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceRemovedNotif.setStatus(
        "deprecated"
    )

ciscoFlashDeviceInsertedNotifRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 7)
)
ciscoFlashDeviceInsertedNotifRev1.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashDeviceMinPartitionSize"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceNameExtended"))
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceInsertedNotifRev1.setStatus(
        "current"
    )

ciscoFlashDeviceRemovedNotifRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 8)
)
ciscoFlashDeviceRemovedNotifRev1.setObjects(
    ("CISCO-FLASH-MIB", "ciscoFlashDeviceNameExtended")
)
if mibBuilder.loadTexts:
    ciscoFlashDeviceRemovedNotifRev1.setStatus(
        "current"
    )

ciscoFlashPartitionLowSpaceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 9)
)
ciscoFlashPartitionLowSpaceNotif.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashPartitionName"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionFreeSpaceExtended"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionLowSpaceNotifThreshold"))
)
if mibBuilder.loadTexts:
    ciscoFlashPartitionLowSpaceNotif.setStatus(
        "current"
    )

ciscoFlashPartitionLowSpaceRecoveryNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 1, 3, 0, 10)
)
ciscoFlashPartitionLowSpaceRecoveryNotif.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashPartitionName"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionFreeSpaceExtended"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionLowSpaceNotifThreshold"))
)
if mibBuilder.loadTexts:
    ciscoFlashPartitionLowSpaceRecoveryNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoFlashNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 9)
)
ciscoFlashNotifGroup.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashCopyCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashMiscOpCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceChangeTrap"))
)
if mibBuilder.loadTexts:
    ciscoFlashNotifGroup.setStatus(
        "deprecated"
    )

ciscoFlashNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 11)
)
ciscoFlashNotifGroupRev1.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashCopyCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashMiscOpCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceInsertedNotif"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceRemovedNotif"))
)
if mibBuilder.loadTexts:
    ciscoFlashNotifGroupRev1.setStatus(
        "deprecated"
    )

ciscoFlashNotifGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 17)
)
ciscoFlashNotifGroupRev2.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashCopyCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashMiscOpCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceInsertedNotifRev1"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceRemovedNotifRev1"))
)
if mibBuilder.loadTexts:
    ciscoFlashNotifGroupRev2.setStatus(
        "deprecated"
    )

ciscoFlashNotifGroupRev3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 2, 25)
)
ciscoFlashNotifGroupRev3.setObjects(
      *(("CISCO-FLASH-MIB", "ciscoFlashCopyCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitioningCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashMiscOpCompletionTrap"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceInsertedNotifRev1"),
        ("CISCO-FLASH-MIB", "ciscoFlashDeviceRemovedNotifRev1"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionLowSpaceNotif"),
        ("CISCO-FLASH-MIB", "ciscoFlashPartitionLowSpaceRecoveryNotif"))
)
if mibBuilder.loadTexts:
    ciscoFlashNotifGroupRev3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFlashMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBCompliance.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev7.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev8.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev9.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev10.setStatus(
        "deprecated"
    )

ciscoFlashMIBComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 10, 2, 1, 12)
)
if mibBuilder.loadTexts:
    ciscoFlashMIBComplianceRev11.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FLASH-MIB",
    **{"ChecksumString": ChecksumString,
       "FlashFileType": FlashFileType,
       "ciscoFlashMIB": ciscoFlashMIB,
       "ciscoFlashMIBObjects": ciscoFlashMIBObjects,
       "ciscoFlashDevice": ciscoFlashDevice,
       "ciscoFlashDevicesSupported": ciscoFlashDevicesSupported,
       "ciscoFlashDeviceTable": ciscoFlashDeviceTable,
       "ciscoFlashDeviceEntry": ciscoFlashDeviceEntry,
       "ciscoFlashDeviceIndex": ciscoFlashDeviceIndex,
       "ciscoFlashDeviceSize": ciscoFlashDeviceSize,
       "ciscoFlashDeviceMinPartitionSize": ciscoFlashDeviceMinPartitionSize,
       "ciscoFlashDeviceMaxPartitions": ciscoFlashDeviceMaxPartitions,
       "ciscoFlashDevicePartitions": ciscoFlashDevicePartitions,
       "ciscoFlashDeviceChipCount": ciscoFlashDeviceChipCount,
       "ciscoFlashDeviceName": ciscoFlashDeviceName,
       "ciscoFlashDeviceDescr": ciscoFlashDeviceDescr,
       "ciscoFlashDeviceController": ciscoFlashDeviceController,
       "ciscoFlashDeviceCard": ciscoFlashDeviceCard,
       "ciscoFlashDeviceProgrammingJumper": ciscoFlashDeviceProgrammingJumper,
       "ciscoFlashDeviceInitTime": ciscoFlashDeviceInitTime,
       "ciscoFlashDeviceRemovable": ciscoFlashDeviceRemovable,
       "ciscoFlashPhyEntIndex": ciscoFlashPhyEntIndex,
       "ciscoFlashDeviceNameExtended": ciscoFlashDeviceNameExtended,
       "ciscoFlashDeviceSizeExtended": ciscoFlashDeviceSizeExtended,
       "ciscoFlashDeviceMinPartitionSizeExtended": ciscoFlashDeviceMinPartitionSizeExtended,
       "ciscoFlashChips": ciscoFlashChips,
       "ciscoFlashChipTable": ciscoFlashChipTable,
       "ciscoFlashChipEntry": ciscoFlashChipEntry,
       "ciscoFlashChipIndex": ciscoFlashChipIndex,
       "ciscoFlashChipCode": ciscoFlashChipCode,
       "ciscoFlashChipDescr": ciscoFlashChipDescr,
       "ciscoFlashChipWriteRetries": ciscoFlashChipWriteRetries,
       "ciscoFlashChipEraseRetries": ciscoFlashChipEraseRetries,
       "ciscoFlashChipMaxWriteRetries": ciscoFlashChipMaxWriteRetries,
       "ciscoFlashChipMaxEraseRetries": ciscoFlashChipMaxEraseRetries,
       "ciscoFlashPartitions": ciscoFlashPartitions,
       "ciscoFlashPartitionTable": ciscoFlashPartitionTable,
       "ciscoFlashPartitionEntry": ciscoFlashPartitionEntry,
       "ciscoFlashPartitionIndex": ciscoFlashPartitionIndex,
       "ciscoFlashPartitionStartChip": ciscoFlashPartitionStartChip,
       "ciscoFlashPartitionEndChip": ciscoFlashPartitionEndChip,
       "ciscoFlashPartitionSize": ciscoFlashPartitionSize,
       "ciscoFlashPartitionFreeSpace": ciscoFlashPartitionFreeSpace,
       "ciscoFlashPartitionFileCount": ciscoFlashPartitionFileCount,
       "ciscoFlashPartitionChecksumAlgorithm": ciscoFlashPartitionChecksumAlgorithm,
       "ciscoFlashPartitionStatus": ciscoFlashPartitionStatus,
       "ciscoFlashPartitionUpgradeMethod": ciscoFlashPartitionUpgradeMethod,
       "ciscoFlashPartitionName": ciscoFlashPartitionName,
       "ciscoFlashPartitionNeedErasure": ciscoFlashPartitionNeedErasure,
       "ciscoFlashPartitionFileNameLength": ciscoFlashPartitionFileNameLength,
       "ciscoFlashPartitionSizeExtended": ciscoFlashPartitionSizeExtended,
       "ciscoFlashPartitionFreeSpaceExtended": ciscoFlashPartitionFreeSpaceExtended,
       "ciscoFlashPartitionLowSpaceNotifThreshold": ciscoFlashPartitionLowSpaceNotifThreshold,
       "ciscoFlashFiles": ciscoFlashFiles,
       "ciscoFlashFileTable": ciscoFlashFileTable,
       "ciscoFlashFileEntry": ciscoFlashFileEntry,
       "ciscoFlashFileIndex": ciscoFlashFileIndex,
       "ciscoFlashFileSize": ciscoFlashFileSize,
       "ciscoFlashFileChecksum": ciscoFlashFileChecksum,
       "ciscoFlashFileStatus": ciscoFlashFileStatus,
       "ciscoFlashFileName": ciscoFlashFileName,
       "ciscoFlashFileType": ciscoFlashFileType,
       "ciscoFlashFileDate": ciscoFlashFileDate,
       "ciscoFlashFileByTypeTable": ciscoFlashFileByTypeTable,
       "ciscoFlashFileByTypeEntry": ciscoFlashFileByTypeEntry,
       "ciscoFlashFileByTypeSize": ciscoFlashFileByTypeSize,
       "ciscoFlashFileByTypeChecksum": ciscoFlashFileByTypeChecksum,
       "ciscoFlashFileByTypeStatus": ciscoFlashFileByTypeStatus,
       "ciscoFlashFileByTypeName": ciscoFlashFileByTypeName,
       "ciscoFlashFileByTypeDate": ciscoFlashFileByTypeDate,
       "ciscoFlashOps": ciscoFlashOps,
       "ciscoFlashCopyTable": ciscoFlashCopyTable,
       "ciscoFlashCopyEntry": ciscoFlashCopyEntry,
       "ciscoFlashCopySerialNumber": ciscoFlashCopySerialNumber,
       "ciscoFlashCopyCommand": ciscoFlashCopyCommand,
       "ciscoFlashCopyProtocol": ciscoFlashCopyProtocol,
       "ciscoFlashCopyServerAddress": ciscoFlashCopyServerAddress,
       "ciscoFlashCopySourceName": ciscoFlashCopySourceName,
       "ciscoFlashCopyDestinationName": ciscoFlashCopyDestinationName,
       "ciscoFlashCopyRemoteUserName": ciscoFlashCopyRemoteUserName,
       "ciscoFlashCopyStatus": ciscoFlashCopyStatus,
       "ciscoFlashCopyNotifyOnCompletion": ciscoFlashCopyNotifyOnCompletion,
       "ciscoFlashCopyTime": ciscoFlashCopyTime,
       "ciscoFlashCopyEntryStatus": ciscoFlashCopyEntryStatus,
       "ciscoFlashCopyVerify": ciscoFlashCopyVerify,
       "ciscoFlashCopyServerAddrType": ciscoFlashCopyServerAddrType,
       "ciscoFlashCopyServerAddrRev1": ciscoFlashCopyServerAddrRev1,
       "ciscoFlashCopyRemotePassword": ciscoFlashCopyRemotePassword,
       "ciscoFlashPartitioningTable": ciscoFlashPartitioningTable,
       "ciscoFlashPartitioningEntry": ciscoFlashPartitioningEntry,
       "ciscoFlashPartitioningSerialNumber": ciscoFlashPartitioningSerialNumber,
       "ciscoFlashPartitioningCommand": ciscoFlashPartitioningCommand,
       "ciscoFlashPartitioningDestinationName": ciscoFlashPartitioningDestinationName,
       "ciscoFlashPartitioningPartitionCount": ciscoFlashPartitioningPartitionCount,
       "ciscoFlashPartitioningPartitionSizes": ciscoFlashPartitioningPartitionSizes,
       "ciscoFlashPartitioningStatus": ciscoFlashPartitioningStatus,
       "ciscoFlashPartitioningNotifyOnCompletion": ciscoFlashPartitioningNotifyOnCompletion,
       "ciscoFlashPartitioningTime": ciscoFlashPartitioningTime,
       "ciscoFlashPartitioningEntryStatus": ciscoFlashPartitioningEntryStatus,
       "ciscoFlashMiscOpTable": ciscoFlashMiscOpTable,
       "ciscoFlashMiscOpEntry": ciscoFlashMiscOpEntry,
       "ciscoFlashMiscOpSerialNumber": ciscoFlashMiscOpSerialNumber,
       "ciscoFlashMiscOpCommand": ciscoFlashMiscOpCommand,
       "ciscoFlashMiscOpDestinationName": ciscoFlashMiscOpDestinationName,
       "ciscoFlashMiscOpStatus": ciscoFlashMiscOpStatus,
       "ciscoFlashMiscOpNotifyOnCompletion": ciscoFlashMiscOpNotifyOnCompletion,
       "ciscoFlashMiscOpTime": ciscoFlashMiscOpTime,
       "ciscoFlashMiscOpEntryStatus": ciscoFlashMiscOpEntryStatus,
       "ciscoFlashMIBTrapPrefix": ciscoFlashMIBTrapPrefix,
       "ciscoFlashMIBTraps": ciscoFlashMIBTraps,
       "ciscoFlashCopyCompletionTrap": ciscoFlashCopyCompletionTrap,
       "ciscoFlashPartitioningCompletionTrap": ciscoFlashPartitioningCompletionTrap,
       "ciscoFlashMiscOpCompletionTrap": ciscoFlashMiscOpCompletionTrap,
       "ciscoFlashDeviceChangeTrap": ciscoFlashDeviceChangeTrap,
       "ciscoFlashDeviceInsertedNotif": ciscoFlashDeviceInsertedNotif,
       "ciscoFlashDeviceRemovedNotif": ciscoFlashDeviceRemovedNotif,
       "ciscoFlashDeviceInsertedNotifRev1": ciscoFlashDeviceInsertedNotifRev1,
       "ciscoFlashDeviceRemovedNotifRev1": ciscoFlashDeviceRemovedNotifRev1,
       "ciscoFlashPartitionLowSpaceNotif": ciscoFlashPartitionLowSpaceNotif,
       "ciscoFlashPartitionLowSpaceRecoveryNotif": ciscoFlashPartitionLowSpaceRecoveryNotif,
       "ciscoFlashCfg": ciscoFlashCfg,
       "ciscoFlashCfgDevInsNotifEnable": ciscoFlashCfgDevInsNotifEnable,
       "ciscoFlashCfgDevRemNotifEnable": ciscoFlashCfgDevRemNotifEnable,
       "ciscoFlashPartitionLowSpaceNotifEnable": ciscoFlashPartitionLowSpaceNotifEnable,
       "ciscoFlashMIBConformance": ciscoFlashMIBConformance,
       "ciscoFlashMIBCompliances": ciscoFlashMIBCompliances,
       "ciscoFlashMIBCompliance": ciscoFlashMIBCompliance,
       "ciscoFlashMIBComplianceRev1": ciscoFlashMIBComplianceRev1,
       "ciscoFlashMIBComplianceRev2": ciscoFlashMIBComplianceRev2,
       "ciscoFlashMIBComplianceRev3": ciscoFlashMIBComplianceRev3,
       "ciscoFlashMIBComplianceRev4": ciscoFlashMIBComplianceRev4,
       "ciscoFlashMIBComplianceRev5": ciscoFlashMIBComplianceRev5,
       "ciscoFlashMIBComplianceRev6": ciscoFlashMIBComplianceRev6,
       "ciscoFlashMIBComplianceRev7": ciscoFlashMIBComplianceRev7,
       "ciscoFlashMIBComplianceRev8": ciscoFlashMIBComplianceRev8,
       "ciscoFlashMIBComplianceRev9": ciscoFlashMIBComplianceRev9,
       "ciscoFlashMIBComplianceRev10": ciscoFlashMIBComplianceRev10,
       "ciscoFlashMIBComplianceRev11": ciscoFlashMIBComplianceRev11,
       "ciscoFlashMIBGroups": ciscoFlashMIBGroups,
       "ciscoFlashDeviceInfoGroup": ciscoFlashDeviceInfoGroup,
       "ciscoFlashDeviceOptionalInfoGroup": ciscoFlashDeviceOptionalInfoGroup,
       "ciscoFlashChipInfoGroup": ciscoFlashChipInfoGroup,
       "ciscoFlashPartitionInfoGroup": ciscoFlashPartitionInfoGroup,
       "ciscoFlashFileInfoGroup": ciscoFlashFileInfoGroup,
       "ciscoFlashCopyOpGroup": ciscoFlashCopyOpGroup,
       "ciscoFlashPartitioningOpGroup": ciscoFlashPartitioningOpGroup,
       "ciscoFlashMiscOpGroup": ciscoFlashMiscOpGroup,
       "ciscoFlashNotifGroup": ciscoFlashNotifGroup,
       "ciscoFlashFileInfoGroupRev1": ciscoFlashFileInfoGroupRev1,
       "ciscoFlashNotifGroupRev1": ciscoFlashNotifGroupRev1,
       "ciscoFlashDeviceInfoGroupRev1": ciscoFlashDeviceInfoGroupRev1,
       "ciscoFlashDeviceOptionalInfoGroupRev1": ciscoFlashDeviceOptionalInfoGroupRev1,
       "ciscoFlashCopyOpGroupRev1": ciscoFlashCopyOpGroupRev1,
       "ciscoFlashDeviceInfoGroupRev2": ciscoFlashDeviceInfoGroupRev2,
       "ciscoFlashCopyOpGroupRev2": ciscoFlashCopyOpGroupRev2,
       "ciscoFlashNotifGroupRev2": ciscoFlashNotifGroupRev2,
       "ciscoFlashCopyOpGroupRev3": ciscoFlashCopyOpGroupRev3,
       "ciscoFlashFileInfoGroupSupp1": ciscoFlashFileInfoGroupSupp1,
       "ciscoFlashFileTypeInfoGroup": ciscoFlashFileTypeInfoGroup,
       "ciscoFlashDeviceInfoExtGroup": ciscoFlashDeviceInfoExtGroup,
       "ciscoFlashPartitionInfoExtGroup": ciscoFlashPartitionInfoExtGroup,
       "ciscoFlashDeviceInfoExtGroupSupRev1": ciscoFlashDeviceInfoExtGroupSupRev1,
       "ciscoFlashPartitionInfoGroupRev1": ciscoFlashPartitionInfoGroupRev1,
       "ciscoFlashNotifGroupRev3": ciscoFlashNotifGroupRev3}
)
