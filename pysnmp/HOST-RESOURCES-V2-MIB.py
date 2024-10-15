# SNMP MIB module (HOST-RESOURCES-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HOST-RESOURCES-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:49 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hostResourcesMibModule = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 25)
)
hostResourcesMibModule.setRevisions(
        ("1998-03-07 16:00",)
)


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
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





class KBytes(Integer32):
    """Custom type KBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class ProductID(ObjectIdentifier):
    """Custom type ProductID based on ObjectIdentifier"""




class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )





class InternationalDisplayString(OctetString):
    """Custom type InternationalDisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Host_ObjectIdentity = ObjectIdentity
host = _Host_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25)
)
_HrSystem_ObjectIdentity = ObjectIdentity
hrSystem = _HrSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 1)
)
_HrSystemUptime_Type = TimeTicks
_HrSystemUptime_Object = MibScalar
hrSystemUptime = _HrSystemUptime_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 1),
    _HrSystemUptime_Type()
)
hrSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemUptime.setStatus("current")
_HrSystemDate_Type = DateAndTime
_HrSystemDate_Object = MibScalar
hrSystemDate = _HrSystemDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 2),
    _HrSystemDate_Type()
)
hrSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemDate.setStatus("current")


class _HrSystemInitialLoadDevice_Type(Integer32):
    """Custom type hrSystemInitialLoadDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrSystemInitialLoadDevice_Type.__name__ = "Integer32"
_HrSystemInitialLoadDevice_Object = MibScalar
hrSystemInitialLoadDevice = _HrSystemInitialLoadDevice_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 3),
    _HrSystemInitialLoadDevice_Type()
)
hrSystemInitialLoadDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemInitialLoadDevice.setStatus("current")


class _HrSystemInitialLoadParameters_Type(InternationalDisplayString):
    """Custom type hrSystemInitialLoadParameters based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrSystemInitialLoadParameters_Type.__name__ = "InternationalDisplayString"
_HrSystemInitialLoadParameters_Object = MibScalar
hrSystemInitialLoadParameters = _HrSystemInitialLoadParameters_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 4),
    _HrSystemInitialLoadParameters_Type()
)
hrSystemInitialLoadParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemInitialLoadParameters.setStatus("current")
_HrSystemNumUsers_Type = Gauge32
_HrSystemNumUsers_Object = MibScalar
hrSystemNumUsers = _HrSystemNumUsers_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 5),
    _HrSystemNumUsers_Type()
)
hrSystemNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemNumUsers.setStatus("current")
_HrSystemProcesses_Type = Gauge32
_HrSystemProcesses_Object = MibScalar
hrSystemProcesses = _HrSystemProcesses_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 6),
    _HrSystemProcesses_Type()
)
hrSystemProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemProcesses.setStatus("current")


class _HrSystemMaxProcesses_Type(Integer32):
    """Custom type hrSystemMaxProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrSystemMaxProcesses_Type.__name__ = "Integer32"
_HrSystemMaxProcesses_Object = MibScalar
hrSystemMaxProcesses = _HrSystemMaxProcesses_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 7),
    _HrSystemMaxProcesses_Type()
)
hrSystemMaxProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemMaxProcesses.setStatus("current")
_HrStorage_ObjectIdentity = ObjectIdentity
hrStorage = _HrStorage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2)
)
_HrStorageTypes_ObjectIdentity = ObjectIdentity
hrStorageTypes = _HrStorageTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1)
)
_HrStorageOther_ObjectIdentity = ObjectIdentity
hrStorageOther = _HrStorageOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 1)
)
_HrStorageRam_ObjectIdentity = ObjectIdentity
hrStorageRam = _HrStorageRam_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 2)
)
_HrStorageVirtualMemory_ObjectIdentity = ObjectIdentity
hrStorageVirtualMemory = _HrStorageVirtualMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 3)
)
_HrStorageFixedDisk_ObjectIdentity = ObjectIdentity
hrStorageFixedDisk = _HrStorageFixedDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 4)
)
_HrStorageRemovableDisk_ObjectIdentity = ObjectIdentity
hrStorageRemovableDisk = _HrStorageRemovableDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 5)
)
_HrStorageFloppyDisk_ObjectIdentity = ObjectIdentity
hrStorageFloppyDisk = _HrStorageFloppyDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 6)
)
_HrStorageCompactDisc_ObjectIdentity = ObjectIdentity
hrStorageCompactDisc = _HrStorageCompactDisc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 7)
)
_HrStorageRamDisk_ObjectIdentity = ObjectIdentity
hrStorageRamDisk = _HrStorageRamDisk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 2, 1, 8)
)
_HrMemorySize_Type = KBytes
_HrMemorySize_Object = MibScalar
hrMemorySize = _HrMemorySize_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 2),
    _HrMemorySize_Type()
)
hrMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrMemorySize.setStatus("current")
_HrStorageTable_Object = MibTable
hrStorageTable = _HrStorageTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3)
)
if mibBuilder.loadTexts:
    hrStorageTable.setStatus("current")
_HrStorageEntry_Object = MibTableRow
hrStorageEntry = _HrStorageEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1)
)
hrStorageEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrStorageIndex"),
)
if mibBuilder.loadTexts:
    hrStorageEntry.setStatus("current")


class _HrStorageIndex_Type(Integer32):
    """Custom type hrStorageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrStorageIndex_Type.__name__ = "Integer32"
_HrStorageIndex_Object = MibTableColumn
hrStorageIndex = _HrStorageIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 1),
    _HrStorageIndex_Type()
)
hrStorageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageIndex.setStatus("current")
_HrStorageType_Type = ObjectIdentifier
_HrStorageType_Object = MibTableColumn
hrStorageType = _HrStorageType_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 2),
    _HrStorageType_Type()
)
hrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageType.setStatus("current")
_HrStorageDescr_Type = DisplayString
_HrStorageDescr_Object = MibTableColumn
hrStorageDescr = _HrStorageDescr_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 3),
    _HrStorageDescr_Type()
)
hrStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageDescr.setStatus("current")


class _HrStorageAllocationUnits_Type(Integer32):
    """Custom type hrStorageAllocationUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrStorageAllocationUnits_Type.__name__ = "Integer32"
_HrStorageAllocationUnits_Object = MibTableColumn
hrStorageAllocationUnits = _HrStorageAllocationUnits_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 4),
    _HrStorageAllocationUnits_Type()
)
hrStorageAllocationUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageAllocationUnits.setStatus("current")


class _HrStorageSize_Type(Integer32):
    """Custom type hrStorageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrStorageSize_Type.__name__ = "Integer32"
_HrStorageSize_Object = MibTableColumn
hrStorageSize = _HrStorageSize_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 5),
    _HrStorageSize_Type()
)
hrStorageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrStorageSize.setStatus("current")


class _HrStorageUsed_Type(Integer32):
    """Custom type hrStorageUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrStorageUsed_Type.__name__ = "Integer32"
_HrStorageUsed_Object = MibTableColumn
hrStorageUsed = _HrStorageUsed_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 6),
    _HrStorageUsed_Type()
)
hrStorageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageUsed.setStatus("current")
_HrStorageAllocationFailures_Type = Counter32
_HrStorageAllocationFailures_Object = MibTableColumn
hrStorageAllocationFailures = _HrStorageAllocationFailures_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 7),
    _HrStorageAllocationFailures_Type()
)
hrStorageAllocationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageAllocationFailures.setStatus("current")
_HrDevice_ObjectIdentity = ObjectIdentity
hrDevice = _HrDevice_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3)
)
_HrDeviceTypes_ObjectIdentity = ObjectIdentity
hrDeviceTypes = _HrDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1)
)
_HrDeviceOther_ObjectIdentity = ObjectIdentity
hrDeviceOther = _HrDeviceOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 1)
)
_HrDeviceUnknown_ObjectIdentity = ObjectIdentity
hrDeviceUnknown = _HrDeviceUnknown_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 2)
)
_HrDeviceProcessor_ObjectIdentity = ObjectIdentity
hrDeviceProcessor = _HrDeviceProcessor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 3)
)
_HrDeviceNetwork_ObjectIdentity = ObjectIdentity
hrDeviceNetwork = _HrDeviceNetwork_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 4)
)
_HrDevicePrinter_ObjectIdentity = ObjectIdentity
hrDevicePrinter = _HrDevicePrinter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 5)
)
_HrDeviceDiskStorage_ObjectIdentity = ObjectIdentity
hrDeviceDiskStorage = _HrDeviceDiskStorage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 6)
)
_HrDeviceVideo_ObjectIdentity = ObjectIdentity
hrDeviceVideo = _HrDeviceVideo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 10)
)
_HrDeviceAudio_ObjectIdentity = ObjectIdentity
hrDeviceAudio = _HrDeviceAudio_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 11)
)
_HrDeviceCoprocessor_ObjectIdentity = ObjectIdentity
hrDeviceCoprocessor = _HrDeviceCoprocessor_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 12)
)
_HrDeviceKeyboard_ObjectIdentity = ObjectIdentity
hrDeviceKeyboard = _HrDeviceKeyboard_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 13)
)
_HrDeviceModem_ObjectIdentity = ObjectIdentity
hrDeviceModem = _HrDeviceModem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 14)
)
_HrDeviceParallelPort_ObjectIdentity = ObjectIdentity
hrDeviceParallelPort = _HrDeviceParallelPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 15)
)
_HrDevicePointing_ObjectIdentity = ObjectIdentity
hrDevicePointing = _HrDevicePointing_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 16)
)
_HrDeviceSerialPort_ObjectIdentity = ObjectIdentity
hrDeviceSerialPort = _HrDeviceSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 17)
)
_HrDeviceTape_ObjectIdentity = ObjectIdentity
hrDeviceTape = _HrDeviceTape_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 18)
)
_HrDeviceClock_ObjectIdentity = ObjectIdentity
hrDeviceClock = _HrDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 19)
)
_HrDeviceVolatileMemory_ObjectIdentity = ObjectIdentity
hrDeviceVolatileMemory = _HrDeviceVolatileMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 20)
)
_HrDeviceNonVolatileMemory_ObjectIdentity = ObjectIdentity
hrDeviceNonVolatileMemory = _HrDeviceNonVolatileMemory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 1, 21)
)
_HrDeviceTable_Object = MibTable
hrDeviceTable = _HrDeviceTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2)
)
if mibBuilder.loadTexts:
    hrDeviceTable.setStatus("current")
_HrDeviceEntry_Object = MibTableRow
hrDeviceEntry = _HrDeviceEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1)
)
hrDeviceEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrDeviceEntry.setStatus("current")


class _HrDeviceIndex_Type(Integer32):
    """Custom type hrDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrDeviceIndex_Type.__name__ = "Integer32"
_HrDeviceIndex_Object = MibTableColumn
hrDeviceIndex = _HrDeviceIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 1),
    _HrDeviceIndex_Type()
)
hrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceIndex.setStatus("current")
_HrDeviceType_Type = ObjectIdentifier
_HrDeviceType_Object = MibTableColumn
hrDeviceType = _HrDeviceType_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 2),
    _HrDeviceType_Type()
)
hrDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceType.setStatus("current")


class _HrDeviceDescr_Type(DisplayString):
    """Custom type hrDeviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HrDeviceDescr_Type.__name__ = "DisplayString"
_HrDeviceDescr_Object = MibTableColumn
hrDeviceDescr = _HrDeviceDescr_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 3),
    _HrDeviceDescr_Type()
)
hrDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceDescr.setStatus("current")
_HrDeviceID_Type = ProductID
_HrDeviceID_Object = MibTableColumn
hrDeviceID = _HrDeviceID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 4),
    _HrDeviceID_Type()
)
hrDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceID.setStatus("current")


class _HrDeviceStatus_Type(Integer32):
    """Custom type hrDeviceStatus based on Integer32"""
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
        *(("down", 5),
          ("running", 2),
          ("testing", 4),
          ("unknown", 1),
          ("warning", 3))
    )


_HrDeviceStatus_Type.__name__ = "Integer32"
_HrDeviceStatus_Object = MibTableColumn
hrDeviceStatus = _HrDeviceStatus_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 5),
    _HrDeviceStatus_Type()
)
hrDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceStatus.setStatus("current")
_HrDeviceErrors_Type = Counter32
_HrDeviceErrors_Object = MibTableColumn
hrDeviceErrors = _HrDeviceErrors_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 6),
    _HrDeviceErrors_Type()
)
hrDeviceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceErrors.setStatus("current")
_HrProcessorTable_Object = MibTable
hrProcessorTable = _HrProcessorTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3)
)
if mibBuilder.loadTexts:
    hrProcessorTable.setStatus("current")
_HrProcessorEntry_Object = MibTableRow
hrProcessorEntry = _HrProcessorEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3, 1)
)
hrProcessorEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrProcessorEntry.setStatus("current")
_HrProcessorFrwID_Type = ProductID
_HrProcessorFrwID_Object = MibTableColumn
hrProcessorFrwID = _HrProcessorFrwID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3, 1, 1),
    _HrProcessorFrwID_Type()
)
hrProcessorFrwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrProcessorFrwID.setStatus("current")


class _HrProcessorLoad_Type(Integer32):
    """Custom type hrProcessorLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HrProcessorLoad_Type.__name__ = "Integer32"
_HrProcessorLoad_Object = MibTableColumn
hrProcessorLoad = _HrProcessorLoad_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3, 1, 2),
    _HrProcessorLoad_Type()
)
hrProcessorLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrProcessorLoad.setStatus("current")
_HrNetworkTable_Object = MibTable
hrNetworkTable = _HrNetworkTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 4)
)
if mibBuilder.loadTexts:
    hrNetworkTable.setStatus("current")
_HrNetworkEntry_Object = MibTableRow
hrNetworkEntry = _HrNetworkEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 4, 1)
)
hrNetworkEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrNetworkEntry.setStatus("current")
_HrNetworkIfIndex_Type = Integer32
_HrNetworkIfIndex_Object = MibTableColumn
hrNetworkIfIndex = _HrNetworkIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 4, 1, 1),
    _HrNetworkIfIndex_Type()
)
hrNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrNetworkIfIndex.setStatus("current")
_HrPrinterTable_Object = MibTable
hrPrinterTable = _HrPrinterTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5)
)
if mibBuilder.loadTexts:
    hrPrinterTable.setStatus("current")
_HrPrinterEntry_Object = MibTableRow
hrPrinterEntry = _HrPrinterEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1)
)
hrPrinterEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrPrinterEntry.setStatus("current")


class _HrPrinterStatus_Type(Integer32):
    """Custom type hrPrinterStatus based on Integer32"""
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
        *(("idle", 3),
          ("other", 1),
          ("printing", 4),
          ("unknown", 2),
          ("warmup", 5))
    )


_HrPrinterStatus_Type.__name__ = "Integer32"
_HrPrinterStatus_Object = MibTableColumn
hrPrinterStatus = _HrPrinterStatus_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1, 1),
    _HrPrinterStatus_Type()
)
hrPrinterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPrinterStatus.setStatus("current")


class _HrPrinterDetectedErrorState_Type(Bits):
    """Custom type hrPrinterDetectedErrorState based on Bits"""
    namedValues = NamedValues(
        *(("doorOpen", 4),
          ("inputTrayEmpty", 13),
          ("inputTrayMissing", 8),
          ("jammed", 5),
          ("lowPaper", 0),
          ("lowToner", 2),
          ("markerSupplyMissing", 10),
          ("noPaper", 1),
          ("noToner", 3),
          ("offline", 6),
          ("outputFull", 12),
          ("outputNearFull", 11),
          ("outputTrayMissing", 9),
          ("overduePreventMaint", 14),
          ("serviceRequested", 7))
    )

_HrPrinterDetectedErrorState_Type.__name__ = "Bits"
_HrPrinterDetectedErrorState_Object = MibTableColumn
hrPrinterDetectedErrorState = _HrPrinterDetectedErrorState_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1, 2),
    _HrPrinterDetectedErrorState_Type()
)
hrPrinterDetectedErrorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPrinterDetectedErrorState.setStatus("current")
_HrDiskStorageTable_Object = MibTable
hrDiskStorageTable = _HrDiskStorageTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6)
)
if mibBuilder.loadTexts:
    hrDiskStorageTable.setStatus("current")
_HrDiskStorageEntry_Object = MibTableRow
hrDiskStorageEntry = _HrDiskStorageEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1)
)
hrDiskStorageEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrDiskStorageEntry.setStatus("current")


class _HrDiskStorageAccess_Type(Integer32):
    """Custom type hrDiskStorageAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 2),
          ("readWrite", 1))
    )


_HrDiskStorageAccess_Type.__name__ = "Integer32"
_HrDiskStorageAccess_Object = MibTableColumn
hrDiskStorageAccess = _HrDiskStorageAccess_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 1),
    _HrDiskStorageAccess_Type()
)
hrDiskStorageAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageAccess.setStatus("current")


class _HrDiskStorageMedia_Type(Integer32):
    """Custom type hrDiskStorageMedia based on Integer32"""
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
        *(("floppyDisk", 4),
          ("hardDisk", 3),
          ("opticalDiskROM", 5),
          ("opticalDiskRW", 7),
          ("opticalDiskWORM", 6),
          ("other", 1),
          ("ramDisk", 8),
          ("unknown", 2))
    )


_HrDiskStorageMedia_Type.__name__ = "Integer32"
_HrDiskStorageMedia_Object = MibTableColumn
hrDiskStorageMedia = _HrDiskStorageMedia_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 2),
    _HrDiskStorageMedia_Type()
)
hrDiskStorageMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageMedia.setStatus("current")
_HrDiskStorageRemoveble_Type = Boolean
_HrDiskStorageRemoveble_Object = MibTableColumn
hrDiskStorageRemoveble = _HrDiskStorageRemoveble_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 3),
    _HrDiskStorageRemoveble_Type()
)
hrDiskStorageRemoveble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageRemoveble.setStatus("current")
_HrDiskStorageCapacity_Type = KBytes
_HrDiskStorageCapacity_Object = MibTableColumn
hrDiskStorageCapacity = _HrDiskStorageCapacity_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 4),
    _HrDiskStorageCapacity_Type()
)
hrDiskStorageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageCapacity.setStatus("current")
_HrPartitionTable_Object = MibTable
hrPartitionTable = _HrPartitionTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7)
)
if mibBuilder.loadTexts:
    hrPartitionTable.setStatus("current")
_HrPartitionEntry_Object = MibTableRow
hrPartitionEntry = _HrPartitionEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1)
)
hrPartitionEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrDeviceIndex"),
    (0, "HOST-RESOURCES-V2-MIB", "hrPartitionIndex"),
)
if mibBuilder.loadTexts:
    hrPartitionEntry.setStatus("current")


class _HrPartitionIndex_Type(Integer32):
    """Custom type hrPartitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrPartitionIndex_Type.__name__ = "Integer32"
_HrPartitionIndex_Object = MibTableColumn
hrPartitionIndex = _HrPartitionIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 1),
    _HrPartitionIndex_Type()
)
hrPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionIndex.setStatus("current")


class _HrPartitionLabel_Type(InternationalDisplayString):
    """Custom type hrPartitionLabel based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrPartitionLabel_Type.__name__ = "InternationalDisplayString"
_HrPartitionLabel_Object = MibTableColumn
hrPartitionLabel = _HrPartitionLabel_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 2),
    _HrPartitionLabel_Type()
)
hrPartitionLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionLabel.setStatus("current")
_HrPartitionID_Type = OctetString
_HrPartitionID_Object = MibTableColumn
hrPartitionID = _HrPartitionID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 3),
    _HrPartitionID_Type()
)
hrPartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionID.setStatus("current")
_HrPartitionSize_Type = KBytes
_HrPartitionSize_Object = MibTableColumn
hrPartitionSize = _HrPartitionSize_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 4),
    _HrPartitionSize_Type()
)
hrPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionSize.setStatus("current")


class _HrPartitionFSIndex_Type(Integer32):
    """Custom type hrPartitionFSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrPartitionFSIndex_Type.__name__ = "Integer32"
_HrPartitionFSIndex_Object = MibTableColumn
hrPartitionFSIndex = _HrPartitionFSIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 5),
    _HrPartitionFSIndex_Type()
)
hrPartitionFSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionFSIndex.setStatus("current")
_HrFSTable_Object = MibTable
hrFSTable = _HrFSTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8)
)
if mibBuilder.loadTexts:
    hrFSTable.setStatus("current")
_HrFSEntry_Object = MibTableRow
hrFSEntry = _HrFSEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1)
)
hrFSEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrFSIndex"),
)
if mibBuilder.loadTexts:
    hrFSEntry.setStatus("current")


class _HrFSIndex_Type(Integer32):
    """Custom type hrFSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrFSIndex_Type.__name__ = "Integer32"
_HrFSIndex_Object = MibTableColumn
hrFSIndex = _HrFSIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 1),
    _HrFSIndex_Type()
)
hrFSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSIndex.setStatus("current")


class _HrFSMountPoint_Type(InternationalDisplayString):
    """Custom type hrFSMountPoint based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrFSMountPoint_Type.__name__ = "InternationalDisplayString"
_HrFSMountPoint_Object = MibTableColumn
hrFSMountPoint = _HrFSMountPoint_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 2),
    _HrFSMountPoint_Type()
)
hrFSMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSMountPoint.setStatus("current")


class _HrFSRemoteMountPoint_Type(InternationalDisplayString):
    """Custom type hrFSRemoteMountPoint based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrFSRemoteMountPoint_Type.__name__ = "InternationalDisplayString"
_HrFSRemoteMountPoint_Object = MibTableColumn
hrFSRemoteMountPoint = _HrFSRemoteMountPoint_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 3),
    _HrFSRemoteMountPoint_Type()
)
hrFSRemoteMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSRemoteMountPoint.setStatus("current")
_HrFSType_Type = ObjectIdentifier
_HrFSType_Object = MibTableColumn
hrFSType = _HrFSType_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 4),
    _HrFSType_Type()
)
hrFSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSType.setStatus("current")


class _HrFSAccess_Type(Integer32):
    """Custom type hrFSAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 2),
          ("readWrite", 1))
    )


_HrFSAccess_Type.__name__ = "Integer32"
_HrFSAccess_Object = MibTableColumn
hrFSAccess = _HrFSAccess_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 5),
    _HrFSAccess_Type()
)
hrFSAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSAccess.setStatus("current")
_HrFSBootable_Type = Boolean
_HrFSBootable_Object = MibTableColumn
hrFSBootable = _HrFSBootable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 6),
    _HrFSBootable_Type()
)
hrFSBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSBootable.setStatus("current")


class _HrFSStorageIndex_Type(Integer32):
    """Custom type hrFSStorageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HrFSStorageIndex_Type.__name__ = "Integer32"
_HrFSStorageIndex_Object = MibTableColumn
hrFSStorageIndex = _HrFSStorageIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 7),
    _HrFSStorageIndex_Type()
)
hrFSStorageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSStorageIndex.setStatus("current")
_HrFSLastFullBackupDate_Type = DateAndTime
_HrFSLastFullBackupDate_Object = MibTableColumn
hrFSLastFullBackupDate = _HrFSLastFullBackupDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 8),
    _HrFSLastFullBackupDate_Type()
)
hrFSLastFullBackupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrFSLastFullBackupDate.setStatus("current")
_HrFSLastPartialBackupDate_Type = DateAndTime
_HrFSLastPartialBackupDate_Object = MibTableColumn
hrFSLastPartialBackupDate = _HrFSLastPartialBackupDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 9),
    _HrFSLastPartialBackupDate_Type()
)
hrFSLastPartialBackupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrFSLastPartialBackupDate.setStatus("current")
_HrFSTypes_ObjectIdentity = ObjectIdentity
hrFSTypes = _HrFSTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9)
)
_HrFSOther_ObjectIdentity = ObjectIdentity
hrFSOther = _HrFSOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 1)
)
_HrFSUnknown_ObjectIdentity = ObjectIdentity
hrFSUnknown = _HrFSUnknown_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 2)
)
_HrFSBerkeleyFFS_ObjectIdentity = ObjectIdentity
hrFSBerkeleyFFS = _HrFSBerkeleyFFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 3)
)
_HrFSSys5FS_ObjectIdentity = ObjectIdentity
hrFSSys5FS = _HrFSSys5FS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 4)
)
_HrFSFat_ObjectIdentity = ObjectIdentity
hrFSFat = _HrFSFat_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 5)
)
_HrFSHPFS_ObjectIdentity = ObjectIdentity
hrFSHPFS = _HrFSHPFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 6)
)
_HrFSHFS_ObjectIdentity = ObjectIdentity
hrFSHFS = _HrFSHFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 7)
)
_HrFSMFS_ObjectIdentity = ObjectIdentity
hrFSMFS = _HrFSMFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 8)
)
_HrFSNTFS_ObjectIdentity = ObjectIdentity
hrFSNTFS = _HrFSNTFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 9)
)
_HrFSVNode_ObjectIdentity = ObjectIdentity
hrFSVNode = _HrFSVNode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 10)
)
_HrFSJournaled_ObjectIdentity = ObjectIdentity
hrFSJournaled = _HrFSJournaled_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 11)
)
_HrFSiso9660_ObjectIdentity = ObjectIdentity
hrFSiso9660 = _HrFSiso9660_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 12)
)
_HrFSRockRidge_ObjectIdentity = ObjectIdentity
hrFSRockRidge = _HrFSRockRidge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 13)
)
_HrFSNFS_ObjectIdentity = ObjectIdentity
hrFSNFS = _HrFSNFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 14)
)
_HrFSNetware_ObjectIdentity = ObjectIdentity
hrFSNetware = _HrFSNetware_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 15)
)
_HrFSAFS_ObjectIdentity = ObjectIdentity
hrFSAFS = _HrFSAFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 16)
)
_HrFSDFS_ObjectIdentity = ObjectIdentity
hrFSDFS = _HrFSDFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 17)
)
_HrFSAppleshare_ObjectIdentity = ObjectIdentity
hrFSAppleshare = _HrFSAppleshare_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 18)
)
_HrFSRFS_ObjectIdentity = ObjectIdentity
hrFSRFS = _HrFSRFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 19)
)
_HrFSDGCFS_ObjectIdentity = ObjectIdentity
hrFSDGCFS = _HrFSDGCFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 20)
)
_HrFSBFS_ObjectIdentity = ObjectIdentity
hrFSBFS = _HrFSBFS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 3, 9, 21)
)
_HrSWRun_ObjectIdentity = ObjectIdentity
hrSWRun = _HrSWRun_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 4)
)


class _HrSWOSIndex_Type(Integer32):
    """Custom type hrSWOSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrSWOSIndex_Type.__name__ = "Integer32"
_HrSWOSIndex_Object = MibScalar
hrSWOSIndex = _HrSWOSIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 1),
    _HrSWOSIndex_Type()
)
hrSWOSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWOSIndex.setStatus("current")
_HrSWRunTable_Object = MibTable
hrSWRunTable = _HrSWRunTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2)
)
if mibBuilder.loadTexts:
    hrSWRunTable.setStatus("current")
_HrSWRunEntry_Object = MibTableRow
hrSWRunEntry = _HrSWRunEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1)
)
hrSWRunEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrSWRunIndex"),
)
if mibBuilder.loadTexts:
    hrSWRunEntry.setStatus("current")


class _HrSWRunIndex_Type(Integer32):
    """Custom type hrSWRunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrSWRunIndex_Type.__name__ = "Integer32"
_HrSWRunIndex_Object = MibTableColumn
hrSWRunIndex = _HrSWRunIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 1),
    _HrSWRunIndex_Type()
)
hrSWRunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunIndex.setStatus("current")


class _HrSWRunName_Type(InternationalDisplayString):
    """Custom type hrSWRunName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HrSWRunName_Type.__name__ = "InternationalDisplayString"
_HrSWRunName_Object = MibTableColumn
hrSWRunName = _HrSWRunName_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 2),
    _HrSWRunName_Type()
)
hrSWRunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunName.setStatus("current")
_HrSWRunID_Type = ProductID
_HrSWRunID_Object = MibTableColumn
hrSWRunID = _HrSWRunID_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 3),
    _HrSWRunID_Type()
)
hrSWRunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunID.setStatus("current")


class _HrSWRunPath_Type(InternationalDisplayString):
    """Custom type hrSWRunPath based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrSWRunPath_Type.__name__ = "InternationalDisplayString"
_HrSWRunPath_Object = MibTableColumn
hrSWRunPath = _HrSWRunPath_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 4),
    _HrSWRunPath_Type()
)
hrSWRunPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunPath.setStatus("current")


class _HrSWRunParameters_Type(InternationalDisplayString):
    """Custom type hrSWRunParameters based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HrSWRunParameters_Type.__name__ = "InternationalDisplayString"
_HrSWRunParameters_Object = MibTableColumn
hrSWRunParameters = _HrSWRunParameters_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 5),
    _HrSWRunParameters_Type()
)
hrSWRunParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunParameters.setStatus("current")


class _HrSWRunType_Type(Integer32):
    """Custom type hrSWRunType based on Integer32"""
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
        *(("application", 4),
          ("deviceDriver", 3),
          ("operatingSystem", 2),
          ("unknown", 1))
    )


_HrSWRunType_Type.__name__ = "Integer32"
_HrSWRunType_Object = MibTableColumn
hrSWRunType = _HrSWRunType_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 6),
    _HrSWRunType_Type()
)
hrSWRunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunType.setStatus("current")


class _HrSWRunStatus_Type(Integer32):
    """Custom type hrSWRunStatus based on Integer32"""
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
        *(("invalid", 4),
          ("notRunnable", 3),
          ("runnable", 2),
          ("running", 1))
    )


_HrSWRunStatus_Type.__name__ = "Integer32"
_HrSWRunStatus_Object = MibTableColumn
hrSWRunStatus = _HrSWRunStatus_Object(
    (1, 3, 6, 1, 2, 1, 25, 4, 2, 1, 7),
    _HrSWRunStatus_Type()
)
hrSWRunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSWRunStatus.setStatus("current")
_HrSWRunPerf_ObjectIdentity = ObjectIdentity
hrSWRunPerf = _HrSWRunPerf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 5)
)
_HrSWRunPerfTable_Object = MibTable
hrSWRunPerfTable = _HrSWRunPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 5, 1)
)
if mibBuilder.loadTexts:
    hrSWRunPerfTable.setStatus("current")
_HrSWRunPerfEntry_Object = MibTableRow
hrSWRunPerfEntry = _HrSWRunPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 5, 1, 1)
)
hrSWRunPerfEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrSWRunIndex"),
)
if mibBuilder.loadTexts:
    hrSWRunPerfEntry.setStatus("current")
_HrSWRunPerfCPU_Type = Integer32
_HrSWRunPerfCPU_Object = MibTableColumn
hrSWRunPerfCPU = _HrSWRunPerfCPU_Object(
    (1, 3, 6, 1, 2, 1, 25, 5, 1, 1, 1),
    _HrSWRunPerfCPU_Type()
)
hrSWRunPerfCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunPerfCPU.setStatus("current")
_HrSWRunPerfMem_Type = KBytes
_HrSWRunPerfMem_Object = MibTableColumn
hrSWRunPerfMem = _HrSWRunPerfMem_Object(
    (1, 3, 6, 1, 2, 1, 25, 5, 1, 1, 2),
    _HrSWRunPerfMem_Type()
)
hrSWRunPerfMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWRunPerfMem.setStatus("current")
_HrSWInstalled_ObjectIdentity = ObjectIdentity
hrSWInstalled = _HrSWInstalled_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 6)
)
_HrSWInstalledLastChange_Type = TimeTicks
_HrSWInstalledLastChange_Object = MibScalar
hrSWInstalledLastChange = _HrSWInstalledLastChange_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 1),
    _HrSWInstalledLastChange_Type()
)
hrSWInstalledLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledLastChange.setStatus("current")
_HrSWInstalledLastUpdateTime_Type = TimeTicks
_HrSWInstalledLastUpdateTime_Object = MibScalar
hrSWInstalledLastUpdateTime = _HrSWInstalledLastUpdateTime_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 2),
    _HrSWInstalledLastUpdateTime_Type()
)
hrSWInstalledLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledLastUpdateTime.setStatus("current")
_HrSWInstalledTable_Object = MibTable
hrSWInstalledTable = _HrSWInstalledTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3)
)
if mibBuilder.loadTexts:
    hrSWInstalledTable.setStatus("current")
_HrSWInstalledEntry_Object = MibTableRow
hrSWInstalledEntry = _HrSWInstalledEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1)
)
hrSWInstalledEntry.setIndexNames(
    (0, "HOST-RESOURCES-V2-MIB", "hrSWInstalledIndex"),
)
if mibBuilder.loadTexts:
    hrSWInstalledEntry.setStatus("current")


class _HrSWInstalledIndex_Type(Integer32):
    """Custom type hrSWInstalledIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HrSWInstalledIndex_Type.__name__ = "Integer32"
_HrSWInstalledIndex_Object = MibTableColumn
hrSWInstalledIndex = _HrSWInstalledIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 1),
    _HrSWInstalledIndex_Type()
)
hrSWInstalledIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledIndex.setStatus("current")


class _HrSWInstalledName_Type(InternationalDisplayString):
    """Custom type hrSWInstalledName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HrSWInstalledName_Type.__name__ = "InternationalDisplayString"
_HrSWInstalledName_Object = MibTableColumn
hrSWInstalledName = _HrSWInstalledName_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 2),
    _HrSWInstalledName_Type()
)
hrSWInstalledName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledName.setStatus("current")
_HrSWInstalledID_Type = ProductID
_HrSWInstalledID_Object = MibTableColumn
hrSWInstalledID = _HrSWInstalledID_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 3),
    _HrSWInstalledID_Type()
)
hrSWInstalledID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledID.setStatus("current")


class _HrSWInstalledType_Type(Integer32):
    """Custom type hrSWInstalledType based on Integer32"""
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
        *(("application", 4),
          ("deviceDriver", 3),
          ("operatingSystem", 2),
          ("unknown", 1))
    )


_HrSWInstalledType_Type.__name__ = "Integer32"
_HrSWInstalledType_Object = MibTableColumn
hrSWInstalledType = _HrSWInstalledType_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 4),
    _HrSWInstalledType_Type()
)
hrSWInstalledType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledType.setStatus("current")
_HrSWInstalledDate_Type = DateAndTime
_HrSWInstalledDate_Object = MibTableColumn
hrSWInstalledDate = _HrSWInstalledDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 6, 3, 1, 5),
    _HrSWInstalledDate_Type()
)
hrSWInstalledDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSWInstalledDate.setStatus("current")
_HrConformance_ObjectIdentity = ObjectIdentity
hrConformance = _HrConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 7)
)
_HrMIBCompliances_ObjectIdentity = ObjectIdentity
hrMIBCompliances = _HrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 7, 1)
)
_HrMIBGroups_ObjectIdentity = ObjectIdentity
hrMIBGroups = _HrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 25, 7, 2)
)

# Managed Objects groups

hrSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 2, 1)
)
hrSystemGroup.setObjects(
      *(("HOST-RESOURCES-V2-MIB", "hrSystemUptime"),
        ("HOST-RESOURCES-V2-MIB", "hrSystemDate"),
        ("HOST-RESOURCES-V2-MIB", "hrSystemInitialLoadDevice"),
        ("HOST-RESOURCES-V2-MIB", "hrSystemInitialLoadParameters"),
        ("HOST-RESOURCES-V2-MIB", "hrSystemNumUsers"),
        ("HOST-RESOURCES-V2-MIB", "hrSystemProcesses"),
        ("HOST-RESOURCES-V2-MIB", "hrSystemMaxProcesses"))
)
if mibBuilder.loadTexts:
    hrSystemGroup.setStatus("current")

hrStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 2, 2)
)
hrStorageGroup.setObjects(
      *(("HOST-RESOURCES-V2-MIB", "hrMemorySize"),
        ("HOST-RESOURCES-V2-MIB", "hrStorageIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrStorageType"),
        ("HOST-RESOURCES-V2-MIB", "hrStorageDescr"),
        ("HOST-RESOURCES-V2-MIB", "hrStorageAllocationUnits"),
        ("HOST-RESOURCES-V2-MIB", "hrStorageSize"),
        ("HOST-RESOURCES-V2-MIB", "hrStorageUsed"),
        ("HOST-RESOURCES-V2-MIB", "hrStorageAllocationFailures"))
)
if mibBuilder.loadTexts:
    hrStorageGroup.setStatus("current")

hrDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 2, 3)
)
hrDeviceGroup.setObjects(
      *(("HOST-RESOURCES-V2-MIB", "hrDeviceIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrDeviceType"),
        ("HOST-RESOURCES-V2-MIB", "hrDeviceDescr"),
        ("HOST-RESOURCES-V2-MIB", "hrDeviceID"),
        ("HOST-RESOURCES-V2-MIB", "hrDeviceStatus"),
        ("HOST-RESOURCES-V2-MIB", "hrDeviceErrors"),
        ("HOST-RESOURCES-V2-MIB", "hrProcessorFrwID"),
        ("HOST-RESOURCES-V2-MIB", "hrProcessorLoad"),
        ("HOST-RESOURCES-V2-MIB", "hrNetworkIfIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrPrinterStatus"),
        ("HOST-RESOURCES-V2-MIB", "hrPrinterDetectedErrorState"),
        ("HOST-RESOURCES-V2-MIB", "hrDiskStorageAccess"),
        ("HOST-RESOURCES-V2-MIB", "hrDiskStorageMedia"),
        ("HOST-RESOURCES-V2-MIB", "hrDiskStorageRemoveble"),
        ("HOST-RESOURCES-V2-MIB", "hrDiskStorageCapacity"),
        ("HOST-RESOURCES-V2-MIB", "hrPartitionIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrPartitionLabel"),
        ("HOST-RESOURCES-V2-MIB", "hrPartitionID"),
        ("HOST-RESOURCES-V2-MIB", "hrPartitionSize"),
        ("HOST-RESOURCES-V2-MIB", "hrPartitionFSIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrFSIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrFSMountPoint"),
        ("HOST-RESOURCES-V2-MIB", "hrFSRemoteMountPoint"),
        ("HOST-RESOURCES-V2-MIB", "hrFSType"),
        ("HOST-RESOURCES-V2-MIB", "hrFSAccess"),
        ("HOST-RESOURCES-V2-MIB", "hrFSBootable"),
        ("HOST-RESOURCES-V2-MIB", "hrFSStorageIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrFSLastFullBackupDate"),
        ("HOST-RESOURCES-V2-MIB", "hrFSLastPartialBackupDate"))
)
if mibBuilder.loadTexts:
    hrDeviceGroup.setStatus("current")

hrSWRunGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 2, 4)
)
hrSWRunGroup.setObjects(
      *(("HOST-RESOURCES-V2-MIB", "hrSWOSIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrSWRunIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrSWRunName"),
        ("HOST-RESOURCES-V2-MIB", "hrSWRunID"),
        ("HOST-RESOURCES-V2-MIB", "hrSWRunPath"),
        ("HOST-RESOURCES-V2-MIB", "hrSWRunParameters"),
        ("HOST-RESOURCES-V2-MIB", "hrSWRunType"),
        ("HOST-RESOURCES-V2-MIB", "hrSWRunStatus"),
        ("HOST-RESOURCES-V2-MIB", "hrSWRunPerfCPU"),
        ("HOST-RESOURCES-V2-MIB", "hrSWRunPerfMem"))
)
if mibBuilder.loadTexts:
    hrSWRunGroup.setStatus("current")

hrSWInstalledGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 25, 7, 2, 5)
)
hrSWInstalledGroup.setObjects(
      *(("HOST-RESOURCES-V2-MIB", "hrSWInstalledLastChange"),
        ("HOST-RESOURCES-V2-MIB", "hrSWInstalledLastUpdateTime"),
        ("HOST-RESOURCES-V2-MIB", "hrSWInstalledIndex"),
        ("HOST-RESOURCES-V2-MIB", "hrSWInstalledName"),
        ("HOST-RESOURCES-V2-MIB", "hrSWInstalledID"),
        ("HOST-RESOURCES-V2-MIB", "hrSWInstalledType"),
        ("HOST-RESOURCES-V2-MIB", "hrSWInstalledDate"))
)
if mibBuilder.loadTexts:
    hrSWInstalledGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 25, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HOST-RESOURCES-V2-MIB",
    **{"Boolean": Boolean,
       "KBytes": KBytes,
       "ProductID": ProductID,
       "DateAndTime": DateAndTime,
       "InternationalDisplayString": InternationalDisplayString,
       "hostResourcesMibModule": hostResourcesMibModule,
       "host": host,
       "hrSystem": hrSystem,
       "hrSystemUptime": hrSystemUptime,
       "hrSystemDate": hrSystemDate,
       "hrSystemInitialLoadDevice": hrSystemInitialLoadDevice,
       "hrSystemInitialLoadParameters": hrSystemInitialLoadParameters,
       "hrSystemNumUsers": hrSystemNumUsers,
       "hrSystemProcesses": hrSystemProcesses,
       "hrSystemMaxProcesses": hrSystemMaxProcesses,
       "hrStorage": hrStorage,
       "hrStorageTypes": hrStorageTypes,
       "hrStorageOther": hrStorageOther,
       "hrStorageRam": hrStorageRam,
       "hrStorageVirtualMemory": hrStorageVirtualMemory,
       "hrStorageFixedDisk": hrStorageFixedDisk,
       "hrStorageRemovableDisk": hrStorageRemovableDisk,
       "hrStorageFloppyDisk": hrStorageFloppyDisk,
       "hrStorageCompactDisc": hrStorageCompactDisc,
       "hrStorageRamDisk": hrStorageRamDisk,
       "hrMemorySize": hrMemorySize,
       "hrStorageTable": hrStorageTable,
       "hrStorageEntry": hrStorageEntry,
       "hrStorageIndex": hrStorageIndex,
       "hrStorageType": hrStorageType,
       "hrStorageDescr": hrStorageDescr,
       "hrStorageAllocationUnits": hrStorageAllocationUnits,
       "hrStorageSize": hrStorageSize,
       "hrStorageUsed": hrStorageUsed,
       "hrStorageAllocationFailures": hrStorageAllocationFailures,
       "hrDevice": hrDevice,
       "hrDeviceTypes": hrDeviceTypes,
       "hrDeviceOther": hrDeviceOther,
       "hrDeviceUnknown": hrDeviceUnknown,
       "hrDeviceProcessor": hrDeviceProcessor,
       "hrDeviceNetwork": hrDeviceNetwork,
       "hrDevicePrinter": hrDevicePrinter,
       "hrDeviceDiskStorage": hrDeviceDiskStorage,
       "hrDeviceVideo": hrDeviceVideo,
       "hrDeviceAudio": hrDeviceAudio,
       "hrDeviceCoprocessor": hrDeviceCoprocessor,
       "hrDeviceKeyboard": hrDeviceKeyboard,
       "hrDeviceModem": hrDeviceModem,
       "hrDeviceParallelPort": hrDeviceParallelPort,
       "hrDevicePointing": hrDevicePointing,
       "hrDeviceSerialPort": hrDeviceSerialPort,
       "hrDeviceTape": hrDeviceTape,
       "hrDeviceClock": hrDeviceClock,
       "hrDeviceVolatileMemory": hrDeviceVolatileMemory,
       "hrDeviceNonVolatileMemory": hrDeviceNonVolatileMemory,
       "hrDeviceTable": hrDeviceTable,
       "hrDeviceEntry": hrDeviceEntry,
       "hrDeviceIndex": hrDeviceIndex,
       "hrDeviceType": hrDeviceType,
       "hrDeviceDescr": hrDeviceDescr,
       "hrDeviceID": hrDeviceID,
       "hrDeviceStatus": hrDeviceStatus,
       "hrDeviceErrors": hrDeviceErrors,
       "hrProcessorTable": hrProcessorTable,
       "hrProcessorEntry": hrProcessorEntry,
       "hrProcessorFrwID": hrProcessorFrwID,
       "hrProcessorLoad": hrProcessorLoad,
       "hrNetworkTable": hrNetworkTable,
       "hrNetworkEntry": hrNetworkEntry,
       "hrNetworkIfIndex": hrNetworkIfIndex,
       "hrPrinterTable": hrPrinterTable,
       "hrPrinterEntry": hrPrinterEntry,
       "hrPrinterStatus": hrPrinterStatus,
       "hrPrinterDetectedErrorState": hrPrinterDetectedErrorState,
       "hrDiskStorageTable": hrDiskStorageTable,
       "hrDiskStorageEntry": hrDiskStorageEntry,
       "hrDiskStorageAccess": hrDiskStorageAccess,
       "hrDiskStorageMedia": hrDiskStorageMedia,
       "hrDiskStorageRemoveble": hrDiskStorageRemoveble,
       "hrDiskStorageCapacity": hrDiskStorageCapacity,
       "hrPartitionTable": hrPartitionTable,
       "hrPartitionEntry": hrPartitionEntry,
       "hrPartitionIndex": hrPartitionIndex,
       "hrPartitionLabel": hrPartitionLabel,
       "hrPartitionID": hrPartitionID,
       "hrPartitionSize": hrPartitionSize,
       "hrPartitionFSIndex": hrPartitionFSIndex,
       "hrFSTable": hrFSTable,
       "hrFSEntry": hrFSEntry,
       "hrFSIndex": hrFSIndex,
       "hrFSMountPoint": hrFSMountPoint,
       "hrFSRemoteMountPoint": hrFSRemoteMountPoint,
       "hrFSType": hrFSType,
       "hrFSAccess": hrFSAccess,
       "hrFSBootable": hrFSBootable,
       "hrFSStorageIndex": hrFSStorageIndex,
       "hrFSLastFullBackupDate": hrFSLastFullBackupDate,
       "hrFSLastPartialBackupDate": hrFSLastPartialBackupDate,
       "hrFSTypes": hrFSTypes,
       "hrFSOther": hrFSOther,
       "hrFSUnknown": hrFSUnknown,
       "hrFSBerkeleyFFS": hrFSBerkeleyFFS,
       "hrFSSys5FS": hrFSSys5FS,
       "hrFSFat": hrFSFat,
       "hrFSHPFS": hrFSHPFS,
       "hrFSHFS": hrFSHFS,
       "hrFSMFS": hrFSMFS,
       "hrFSNTFS": hrFSNTFS,
       "hrFSVNode": hrFSVNode,
       "hrFSJournaled": hrFSJournaled,
       "hrFSiso9660": hrFSiso9660,
       "hrFSRockRidge": hrFSRockRidge,
       "hrFSNFS": hrFSNFS,
       "hrFSNetware": hrFSNetware,
       "hrFSAFS": hrFSAFS,
       "hrFSDFS": hrFSDFS,
       "hrFSAppleshare": hrFSAppleshare,
       "hrFSRFS": hrFSRFS,
       "hrFSDGCFS": hrFSDGCFS,
       "hrFSBFS": hrFSBFS,
       "hrSWRun": hrSWRun,
       "hrSWOSIndex": hrSWOSIndex,
       "hrSWRunTable": hrSWRunTable,
       "hrSWRunEntry": hrSWRunEntry,
       "hrSWRunIndex": hrSWRunIndex,
       "hrSWRunName": hrSWRunName,
       "hrSWRunID": hrSWRunID,
       "hrSWRunPath": hrSWRunPath,
       "hrSWRunParameters": hrSWRunParameters,
       "hrSWRunType": hrSWRunType,
       "hrSWRunStatus": hrSWRunStatus,
       "hrSWRunPerf": hrSWRunPerf,
       "hrSWRunPerfTable": hrSWRunPerfTable,
       "hrSWRunPerfEntry": hrSWRunPerfEntry,
       "hrSWRunPerfCPU": hrSWRunPerfCPU,
       "hrSWRunPerfMem": hrSWRunPerfMem,
       "hrSWInstalled": hrSWInstalled,
       "hrSWInstalledLastChange": hrSWInstalledLastChange,
       "hrSWInstalledLastUpdateTime": hrSWInstalledLastUpdateTime,
       "hrSWInstalledTable": hrSWInstalledTable,
       "hrSWInstalledEntry": hrSWInstalledEntry,
       "hrSWInstalledIndex": hrSWInstalledIndex,
       "hrSWInstalledName": hrSWInstalledName,
       "hrSWInstalledID": hrSWInstalledID,
       "hrSWInstalledType": hrSWInstalledType,
       "hrSWInstalledDate": hrSWInstalledDate,
       "hrConformance": hrConformance,
       "hrMIBCompliances": hrMIBCompliances,
       "hrMIBCompliance": hrMIBCompliance,
       "hrMIBGroups": hrMIBGroups,
       "hrSystemGroup": hrSystemGroup,
       "hrStorageGroup": hrStorageGroup,
       "hrDeviceGroup": hrDeviceGroup,
       "hrSWRunGroup": hrSWRunGroup,
       "hrSWInstalledGroup": hrSWInstalledGroup}
)
