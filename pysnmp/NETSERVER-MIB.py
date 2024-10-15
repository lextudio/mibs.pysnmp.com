# SNMP MIB module (NETSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:12 2024
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


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



class RaidLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("raid0", 0),
          ("raid1", 1),
          ("raid3", 3),
          ("raid5", 5),
          ("raid6", 6),
          ("raid7", 7))
    )



class RebuildFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              240,
              241,
              242,
              243,
              244,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autorebuild", 1),
          ("autorebuildfailed", 255),
          ("canceled", 243),
          ("check", 3),
          ("expandcapacity", 4),
          ("expandcapacityfailed", 244),
          ("justfailed", 242),
          ("logdevfailed", 241),
          ("manualrebuild", 2),
          ("none", 0),
          ("phydevfailed", 240))
    )



class BusType(Integer32, TextualConvention):
    status = "current"
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
        *(("eisa", 1),
          ("isa", 5),
          ("mca", 2),
          ("pci", 3),
          ("scsi", 6),
          ("vesa", 4))
    )



class ControllerType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              80,
              96,
              97,
              98,
              99,
              100,
              129,
              130,
              131,
              132,
              133,
              134,
              136,
              137,
              138,
              139,
              140,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              192,
              193,
              194,
              195)
        )
    )
    namedValues = NamedValues(
        *(("dac1164P", 26),
          ("dac960E", 1),
          ("dac960FL", 100),
          ("dac960M", 8),
          ("dac960PD", 16),
          ("dac960PDU", 18),
          ("dac960PE", 19),
          ("dac960PG", 20),
          ("dac960PJ", 21),
          ("dac960PL", 17),
          ("dac960PR", 23),
          ("dac960PRL", 24),
          ("dac960PT", 25),
          ("dac960PTL", 22),
          ("dac960S", 96),
          ("dac960SF", 99),
          ("dac960SU", 97),
          ("dac960SX", 98),
          ("dacI20", 80),
          ("hba440", 129),
          ("hba440C", 130),
          ("hba440xC", 133),
          ("hba445", 131),
          ("hba445C", 132),
          ("hba445S", 134),
          ("hba446", 138),
          ("hba446D", 139),
          ("hba446S", 140),
          ("hba540", 160),
          ("hba540C", 161),
          ("hba542", 162),
          ("hba542B", 163),
          ("hba542C", 164),
          ("hba542D", 165),
          ("hba545", 166),
          ("hba545C", 167),
          ("hba545S", 168),
          ("hba54xC", 169),
          ("hba640", 136),
          ("hba640A", 137),
          ("hba742", 144),
          ("hba742A", 145),
          ("hba747", 146),
          ("hba747C", 155),
          ("hba747D", 147),
          ("hba747S", 148),
          ("hba74xC", 149),
          ("hba757", 150),
          ("hba757C", 156),
          ("hba757CD", 153),
          ("hba757D", 151),
          ("hba757S", 152),
          ("hba75xC", 154),
          ("hba930", 192),
          ("hba932", 193),
          ("hba946", 176),
          ("hba946C", 177),
          ("hba948", 178),
          ("hba948C", 179),
          ("hba950", 194),
          ("hba952", 195),
          ("hba956", 180),
          ("hba956C", 181),
          ("hba956CD", 185),
          ("hba958", 182),
          ("hba958C", 183),
          ("hba958CD", 186),
          ("hba958D", 184))
    )



class VendorName(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("att", 4),
          ("dec", 3),
          ("dell", 5),
          ("hp", 2),
          ("ibm", 1),
          ("mylex", 0),
          ("ncr", 8),
          ("nec", 6),
          ("sni", 7))
    )



class U08Bits(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class U16Bits(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



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
    hrSystemUptime.setStatus("mandatory")
_HrSystemDate_Type = DateAndTime
_HrSystemDate_Object = MibScalar
hrSystemDate = _HrSystemDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 2),
    _HrSystemDate_Type()
)
hrSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrSystemDate.setStatus("mandatory")


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
    hrSystemInitialLoadDevice.setStatus("mandatory")


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
    hrSystemInitialLoadParameters.setStatus("mandatory")
_HrSystemNumUsers_Type = Gauge32
_HrSystemNumUsers_Object = MibScalar
hrSystemNumUsers = _HrSystemNumUsers_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 5),
    _HrSystemNumUsers_Type()
)
hrSystemNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemNumUsers.setStatus("mandatory")
_HrSystemProcesses_Type = Gauge32
_HrSystemProcesses_Object = MibScalar
hrSystemProcesses = _HrSystemProcesses_Object(
    (1, 3, 6, 1, 2, 1, 25, 1, 6),
    _HrSystemProcesses_Type()
)
hrSystemProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrSystemProcesses.setStatus("mandatory")


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
    hrSystemMaxProcesses.setStatus("mandatory")
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
    hrMemorySize.setStatus("mandatory")
_HrStorageTable_Object = MibTable
hrStorageTable = _HrStorageTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3)
)
if mibBuilder.loadTexts:
    hrStorageTable.setStatus("mandatory")
_HrStorageEntry_Object = MibTableRow
hrStorageEntry = _HrStorageEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1)
)
hrStorageEntry.setIndexNames(
    (0, "NETSERVER-MIB", "hrStorageIndex"),
)
if mibBuilder.loadTexts:
    hrStorageEntry.setStatus("mandatory")


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
    hrStorageIndex.setStatus("mandatory")
_HrStorageType_Type = ObjectIdentifier
_HrStorageType_Object = MibTableColumn
hrStorageType = _HrStorageType_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 2),
    _HrStorageType_Type()
)
hrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageType.setStatus("mandatory")
_HrStorageDescr_Type = DisplayString
_HrStorageDescr_Object = MibTableColumn
hrStorageDescr = _HrStorageDescr_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 3),
    _HrStorageDescr_Type()
)
hrStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageDescr.setStatus("mandatory")


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
    hrStorageAllocationUnits.setStatus("mandatory")


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
    hrStorageSize.setStatus("mandatory")


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
    hrStorageUsed.setStatus("mandatory")
_HrStorageAllocationFailures_Type = Counter32
_HrStorageAllocationFailures_Object = MibTableColumn
hrStorageAllocationFailures = _HrStorageAllocationFailures_Object(
    (1, 3, 6, 1, 2, 1, 25, 2, 3, 1, 7),
    _HrStorageAllocationFailures_Type()
)
hrStorageAllocationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrStorageAllocationFailures.setStatus("mandatory")
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
    hrDeviceTable.setStatus("mandatory")
_HrDeviceEntry_Object = MibTableRow
hrDeviceEntry = _HrDeviceEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1)
)
hrDeviceEntry.setIndexNames(
    (0, "NETSERVER-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrDeviceEntry.setStatus("mandatory")


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
    hrDeviceIndex.setStatus("mandatory")
_HrDeviceType_Type = ObjectIdentifier
_HrDeviceType_Object = MibTableColumn
hrDeviceType = _HrDeviceType_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 2),
    _HrDeviceType_Type()
)
hrDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceType.setStatus("mandatory")


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
    hrDeviceDescr.setStatus("mandatory")
_HrDeviceID_Type = ProductID
_HrDeviceID_Object = MibTableColumn
hrDeviceID = _HrDeviceID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 4),
    _HrDeviceID_Type()
)
hrDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceID.setStatus("mandatory")


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
    hrDeviceStatus.setStatus("mandatory")
_HrDeviceErrors_Type = Counter32
_HrDeviceErrors_Object = MibTableColumn
hrDeviceErrors = _HrDeviceErrors_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 2, 1, 6),
    _HrDeviceErrors_Type()
)
hrDeviceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDeviceErrors.setStatus("mandatory")
_HrProcessorTable_Object = MibTable
hrProcessorTable = _HrProcessorTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3)
)
if mibBuilder.loadTexts:
    hrProcessorTable.setStatus("mandatory")
_HrProcessorEntry_Object = MibTableRow
hrProcessorEntry = _HrProcessorEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3, 1)
)
hrProcessorEntry.setIndexNames(
    (0, "NETSERVER-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrProcessorEntry.setStatus("mandatory")
_HrProcessorFrwID_Type = ProductID
_HrProcessorFrwID_Object = MibTableColumn
hrProcessorFrwID = _HrProcessorFrwID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 3, 1, 1),
    _HrProcessorFrwID_Type()
)
hrProcessorFrwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrProcessorFrwID.setStatus("mandatory")


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
    hrProcessorLoad.setStatus("mandatory")
_HrNetworkTable_Object = MibTable
hrNetworkTable = _HrNetworkTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 4)
)
if mibBuilder.loadTexts:
    hrNetworkTable.setStatus("mandatory")
_HrNetworkEntry_Object = MibTableRow
hrNetworkEntry = _HrNetworkEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 4, 1)
)
hrNetworkEntry.setIndexNames(
    (0, "NETSERVER-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrNetworkEntry.setStatus("mandatory")
_HrNetworkIfIndex_Type = Integer32
_HrNetworkIfIndex_Object = MibTableColumn
hrNetworkIfIndex = _HrNetworkIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 4, 1, 1),
    _HrNetworkIfIndex_Type()
)
hrNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrNetworkIfIndex.setStatus("mandatory")
_HrPrinterTable_Object = MibTable
hrPrinterTable = _HrPrinterTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5)
)
if mibBuilder.loadTexts:
    hrPrinterTable.setStatus("mandatory")
_HrPrinterEntry_Object = MibTableRow
hrPrinterEntry = _HrPrinterEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1)
)
hrPrinterEntry.setIndexNames(
    (0, "NETSERVER-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrPrinterEntry.setStatus("mandatory")


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
    hrPrinterStatus.setStatus("mandatory")
_HrPrinterDetectedErrorState_Type = OctetString
_HrPrinterDetectedErrorState_Object = MibTableColumn
hrPrinterDetectedErrorState = _HrPrinterDetectedErrorState_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 5, 1, 2),
    _HrPrinterDetectedErrorState_Type()
)
hrPrinterDetectedErrorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPrinterDetectedErrorState.setStatus("mandatory")
_HrDiskStorageTable_Object = MibTable
hrDiskStorageTable = _HrDiskStorageTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6)
)
if mibBuilder.loadTexts:
    hrDiskStorageTable.setStatus("mandatory")
_HrDiskStorageEntry_Object = MibTableRow
hrDiskStorageEntry = _HrDiskStorageEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1)
)
hrDiskStorageEntry.setIndexNames(
    (0, "NETSERVER-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    hrDiskStorageEntry.setStatus("mandatory")


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
    hrDiskStorageAccess.setStatus("mandatory")


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
    hrDiskStorageMedia.setStatus("mandatory")
_HrDiskStorageRemoveble_Type = Boolean
_HrDiskStorageRemoveble_Object = MibTableColumn
hrDiskStorageRemoveble = _HrDiskStorageRemoveble_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 3),
    _HrDiskStorageRemoveble_Type()
)
hrDiskStorageRemoveble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageRemoveble.setStatus("mandatory")
_HrDiskStorageCapacity_Type = KBytes
_HrDiskStorageCapacity_Object = MibTableColumn
hrDiskStorageCapacity = _HrDiskStorageCapacity_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 6, 1, 4),
    _HrDiskStorageCapacity_Type()
)
hrDiskStorageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrDiskStorageCapacity.setStatus("mandatory")
_HrPartitionTable_Object = MibTable
hrPartitionTable = _HrPartitionTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7)
)
if mibBuilder.loadTexts:
    hrPartitionTable.setStatus("mandatory")
_HrPartitionEntry_Object = MibTableRow
hrPartitionEntry = _HrPartitionEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1)
)
hrPartitionEntry.setIndexNames(
    (0, "NETSERVER-MIB", "hrDeviceIndex"),
    (0, "NETSERVER-MIB", "hrPartitionIndex"),
)
if mibBuilder.loadTexts:
    hrPartitionEntry.setStatus("mandatory")


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
    hrPartitionIndex.setStatus("mandatory")


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
    hrPartitionLabel.setStatus("mandatory")
_HrPartitionID_Type = OctetString
_HrPartitionID_Object = MibTableColumn
hrPartitionID = _HrPartitionID_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 3),
    _HrPartitionID_Type()
)
hrPartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionID.setStatus("mandatory")
_HrPartitionSize_Type = KBytes
_HrPartitionSize_Object = MibTableColumn
hrPartitionSize = _HrPartitionSize_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 7, 1, 4),
    _HrPartitionSize_Type()
)
hrPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrPartitionSize.setStatus("mandatory")


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
    hrPartitionFSIndex.setStatus("mandatory")
_HrFSTable_Object = MibTable
hrFSTable = _HrFSTable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8)
)
if mibBuilder.loadTexts:
    hrFSTable.setStatus("mandatory")
_HrFSEntry_Object = MibTableRow
hrFSEntry = _HrFSEntry_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1)
)
hrFSEntry.setIndexNames(
    (0, "NETSERVER-MIB", "hrFSIndex"),
)
if mibBuilder.loadTexts:
    hrFSEntry.setStatus("mandatory")


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
    hrFSIndex.setStatus("mandatory")


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
    hrFSMountPoint.setStatus("mandatory")


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
    hrFSRemoteMountPoint.setStatus("mandatory")
_HrFSType_Type = ObjectIdentifier
_HrFSType_Object = MibTableColumn
hrFSType = _HrFSType_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 4),
    _HrFSType_Type()
)
hrFSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSType.setStatus("mandatory")


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
    hrFSAccess.setStatus("mandatory")
_HrFSBootable_Type = Boolean
_HrFSBootable_Object = MibTableColumn
hrFSBootable = _HrFSBootable_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 6),
    _HrFSBootable_Type()
)
hrFSBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrFSBootable.setStatus("mandatory")


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
    hrFSStorageIndex.setStatus("mandatory")
_HrFSLastFullBackupDate_Type = DateAndTime
_HrFSLastFullBackupDate_Object = MibTableColumn
hrFSLastFullBackupDate = _HrFSLastFullBackupDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 8),
    _HrFSLastFullBackupDate_Type()
)
hrFSLastFullBackupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrFSLastFullBackupDate.setStatus("mandatory")
_HrFSLastPartialBackupDate_Type = DateAndTime
_HrFSLastPartialBackupDate_Object = MibTableColumn
hrFSLastPartialBackupDate = _HrFSLastPartialBackupDate_Object(
    (1, 3, 6, 1, 2, 1, 25, 3, 8, 1, 9),
    _HrFSLastPartialBackupDate_Type()
)
hrFSLastPartialBackupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrFSLastPartialBackupDate.setStatus("mandatory")
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
_Auspex_ObjectIdentity = ObjectIdentity
auspex = _Auspex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80)
)
_NetServer_ObjectIdentity = ObjectIdentity
netServer = _NetServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3)
)
_AxProductInfo_ObjectIdentity = ObjectIdentity
axProductInfo = _AxProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 1)
)
_AxProductName_Type = OctetString
_AxProductName_Object = MibScalar
axProductName = _AxProductName_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 1, 1),
    _AxProductName_Type()
)
axProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axProductName.setStatus("mandatory")
_AxSWVersion_Type = OctetString
_AxSWVersion_Object = MibScalar
axSWVersion = _AxSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 1, 2),
    _AxSWVersion_Type()
)
axSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSWVersion.setStatus("mandatory")
_AxNumNPFSP_Type = Integer32
_AxNumNPFSP_Object = MibScalar
axNumNPFSP = _AxNumNPFSP_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 1, 3),
    _AxNumNPFSP_Type()
)
axNumNPFSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNumNPFSP.setStatus("mandatory")
_AxNP_ObjectIdentity = ObjectIdentity
axNP = _AxNP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 2)
)
_NpTable_Object = MibTable
npTable = _NpTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 1)
)
if mibBuilder.loadTexts:
    npTable.setStatus("mandatory")
_NpEntry_Object = MibTableRow
npEntry = _NpEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 1, 1)
)
npEntry.setIndexNames(
    (0, "NETSERVER-MIB", "npIndex"),
)
if mibBuilder.loadTexts:
    npEntry.setStatus("mandatory")
_NpIndex_Type = Integer32
_NpIndex_Object = MibTableColumn
npIndex = _NpIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 1, 1, 1),
    _NpIndex_Type()
)
npIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIndex.setStatus("mandatory")
_NpBusyCount_Type = Counter32
_NpBusyCount_Object = MibTableColumn
npBusyCount = _NpBusyCount_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 1, 1, 2),
    _NpBusyCount_Type()
)
npBusyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npBusyCount.setStatus("mandatory")
_NpIdleCount_Type = Counter32
_NpIdleCount_Object = MibTableColumn
npIdleCount = _NpIdleCount_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 1, 1, 3),
    _NpIdleCount_Type()
)
npIdleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIdleCount.setStatus("mandatory")
_NpIfTable_Object = MibTable
npIfTable = _NpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2)
)
if mibBuilder.loadTexts:
    npIfTable.setStatus("mandatory")
_NpIfEntry_Object = MibTableRow
npIfEntry = _NpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1)
)
npIfEntry.setIndexNames(
    (0, "NETSERVER-MIB", "npIndex"),
    (0, "NETSERVER-MIB", "npIfIndex"),
)
if mibBuilder.loadTexts:
    npIfEntry.setStatus("mandatory")
_NpIfIndex_Type = Integer32
_NpIfIndex_Object = MibTableColumn
npIfIndex = _NpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 1),
    _NpIfIndex_Type()
)
npIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfIndex.setStatus("mandatory")
_NpIfifIndex_Type = Integer32
_NpIfifIndex_Object = MibTableColumn
npIfifIndex = _NpIfifIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 2),
    _NpIfifIndex_Type()
)
npIfifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfifIndex.setStatus("mandatory")
_NpIfType_Type = DisplayString
_NpIfType_Object = MibTableColumn
npIfType = _NpIfType_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 3),
    _NpIfType_Type()
)
npIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfType.setStatus("mandatory")
_NpIfSpeed_Type = Integer32
_NpIfSpeed_Object = MibTableColumn
npIfSpeed = _NpIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 4),
    _NpIfSpeed_Type()
)
npIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfSpeed.setStatus("mandatory")
_NpIfInOctets_Type = Counter32
_NpIfInOctets_Object = MibTableColumn
npIfInOctets = _NpIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 5),
    _NpIfInOctets_Type()
)
npIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfInOctets.setStatus("mandatory")
_NpIfInUcastPkts_Type = Counter32
_NpIfInUcastPkts_Object = MibTableColumn
npIfInUcastPkts = _NpIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 6),
    _NpIfInUcastPkts_Type()
)
npIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfInUcastPkts.setStatus("mandatory")
_NpIfInNUcastPkts_Type = Counter32
_NpIfInNUcastPkts_Object = MibTableColumn
npIfInNUcastPkts = _NpIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 7),
    _NpIfInNUcastPkts_Type()
)
npIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfInNUcastPkts.setStatus("mandatory")
_NpIfInDiscards_Type = Counter32
_NpIfInDiscards_Object = MibTableColumn
npIfInDiscards = _NpIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 8),
    _NpIfInDiscards_Type()
)
npIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfInDiscards.setStatus("mandatory")
_NpIfInErrors_Type = Counter32
_NpIfInErrors_Object = MibTableColumn
npIfInErrors = _NpIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 9),
    _NpIfInErrors_Type()
)
npIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfInErrors.setStatus("mandatory")
_NpIfInUnknownProto_Type = Counter32
_NpIfInUnknownProto_Object = MibTableColumn
npIfInUnknownProto = _NpIfInUnknownProto_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 10),
    _NpIfInUnknownProto_Type()
)
npIfInUnknownProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfInUnknownProto.setStatus("mandatory")
_NpIfOutOctets_Type = Counter32
_NpIfOutOctets_Object = MibTableColumn
npIfOutOctets = _NpIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 11),
    _NpIfOutOctets_Type()
)
npIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfOutOctets.setStatus("mandatory")
_NpIfOutUcastPkts_Type = Counter32
_NpIfOutUcastPkts_Object = MibTableColumn
npIfOutUcastPkts = _NpIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 12),
    _NpIfOutUcastPkts_Type()
)
npIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfOutUcastPkts.setStatus("mandatory")
_NpIfOutNUcastPkts_Type = Counter32
_NpIfOutNUcastPkts_Object = MibTableColumn
npIfOutNUcastPkts = _NpIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 13),
    _NpIfOutNUcastPkts_Type()
)
npIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfOutNUcastPkts.setStatus("mandatory")
_NpIfOutDiscards_Type = Counter32
_NpIfOutDiscards_Object = MibTableColumn
npIfOutDiscards = _NpIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 14),
    _NpIfOutDiscards_Type()
)
npIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfOutDiscards.setStatus("mandatory")
_NpIfOutErrors_Type = Counter32
_NpIfOutErrors_Object = MibTableColumn
npIfOutErrors = _NpIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 15),
    _NpIfOutErrors_Type()
)
npIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfOutErrors.setStatus("mandatory")
_NpIfOutCollisions_Type = Counter32
_NpIfOutCollisions_Object = MibTableColumn
npIfOutCollisions = _NpIfOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 16),
    _NpIfOutCollisions_Type()
)
npIfOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfOutCollisions.setStatus("mandatory")
_NpIfOutQLen_Type = Gauge32
_NpIfOutQLen_Object = MibTableColumn
npIfOutQLen = _NpIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 17),
    _NpIfOutQLen_Type()
)
npIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfOutQLen.setStatus("mandatory")


class _NpIfAdminStatus_Type(Integer32):
    """Custom type npIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_NpIfAdminStatus_Type.__name__ = "Integer32"
_NpIfAdminStatus_Object = MibTableColumn
npIfAdminStatus = _NpIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 18),
    _NpIfAdminStatus_Type()
)
npIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIfAdminStatus.setStatus("mandatory")


class _NpIfOperStatus_Type(Integer32):
    """Custom type npIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_NpIfOperStatus_Type.__name__ = "Integer32"
_NpIfOperStatus_Object = MibTableColumn
npIfOperStatus = _NpIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 2, 1, 19),
    _NpIfOperStatus_Type()
)
npIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIfOperStatus.setStatus("mandatory")
_NpProtocols_ObjectIdentity = ObjectIdentity
npProtocols = _NpProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3)
)
_NpIPTable_Object = MibTable
npIPTable = _NpIPTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    npIPTable.setStatus("mandatory")
_NpIPEntry_Object = MibTableRow
npIPEntry = _NpIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1)
)
npIPEntry.setIndexNames(
    (0, "NETSERVER-MIB", "npIndex"),
)
if mibBuilder.loadTexts:
    npIPEntry.setStatus("mandatory")


class _NpIPForwarding_Type(Integer32):
    """Custom type npIPForwarding based on Integer32"""
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


_NpIPForwarding_Type.__name__ = "Integer32"
_NpIPForwarding_Object = MibTableColumn
npIPForwarding = _NpIPForwarding_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 1),
    _NpIPForwarding_Type()
)
npIPForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPForwarding.setStatus("mandatory")
_NpIPDefaultTTL_Type = Integer32
_NpIPDefaultTTL_Object = MibTableColumn
npIPDefaultTTL = _NpIPDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 2),
    _NpIPDefaultTTL_Type()
)
npIPDefaultTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPDefaultTTL.setStatus("mandatory")
_NpIPInReceives_Type = Counter32
_NpIPInReceives_Object = MibTableColumn
npIPInReceives = _NpIPInReceives_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 3),
    _NpIPInReceives_Type()
)
npIPInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPInReceives.setStatus("mandatory")
_NpIPInHdrErrors_Type = Counter32
_NpIPInHdrErrors_Object = MibTableColumn
npIPInHdrErrors = _NpIPInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 4),
    _NpIPInHdrErrors_Type()
)
npIPInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPInHdrErrors.setStatus("mandatory")
_NpIPInAddrErrors_Type = Counter32
_NpIPInAddrErrors_Object = MibTableColumn
npIPInAddrErrors = _NpIPInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 5),
    _NpIPInAddrErrors_Type()
)
npIPInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPInAddrErrors.setStatus("mandatory")
_NpIPForwDatagrams_Type = Counter32
_NpIPForwDatagrams_Object = MibTableColumn
npIPForwDatagrams = _NpIPForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 6),
    _NpIPForwDatagrams_Type()
)
npIPForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPForwDatagrams.setStatus("mandatory")
_NpIPInUnknownProtos_Type = Counter32
_NpIPInUnknownProtos_Object = MibTableColumn
npIPInUnknownProtos = _NpIPInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 7),
    _NpIPInUnknownProtos_Type()
)
npIPInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPInUnknownProtos.setStatus("mandatory")
_NpIPInDiscards_Type = Counter32
_NpIPInDiscards_Object = MibTableColumn
npIPInDiscards = _NpIPInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 8),
    _NpIPInDiscards_Type()
)
npIPInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPInDiscards.setStatus("mandatory")
_NpIPInDelivers_Type = Counter32
_NpIPInDelivers_Object = MibTableColumn
npIPInDelivers = _NpIPInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 9),
    _NpIPInDelivers_Type()
)
npIPInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPInDelivers.setStatus("mandatory")
_NpIPOutRequests_Type = Counter32
_NpIPOutRequests_Object = MibTableColumn
npIPOutRequests = _NpIPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 10),
    _NpIPOutRequests_Type()
)
npIPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPOutRequests.setStatus("mandatory")
_NpIPOutDiscards_Type = Counter32
_NpIPOutDiscards_Object = MibTableColumn
npIPOutDiscards = _NpIPOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 11),
    _NpIPOutDiscards_Type()
)
npIPOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPOutDiscards.setStatus("mandatory")
_NpIPOutNoRoutes_Type = Counter32
_NpIPOutNoRoutes_Object = MibTableColumn
npIPOutNoRoutes = _NpIPOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 12),
    _NpIPOutNoRoutes_Type()
)
npIPOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPOutNoRoutes.setStatus("mandatory")
_NpIPReasmTimeout_Type = Counter32
_NpIPReasmTimeout_Object = MibTableColumn
npIPReasmTimeout = _NpIPReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 13),
    _NpIPReasmTimeout_Type()
)
npIPReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPReasmTimeout.setStatus("mandatory")
_NpIPReasmReqds_Type = Counter32
_NpIPReasmReqds_Object = MibTableColumn
npIPReasmReqds = _NpIPReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 14),
    _NpIPReasmReqds_Type()
)
npIPReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPReasmReqds.setStatus("mandatory")
_NpIPReasmOKs_Type = Counter32
_NpIPReasmOKs_Object = MibTableColumn
npIPReasmOKs = _NpIPReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 15),
    _NpIPReasmOKs_Type()
)
npIPReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPReasmOKs.setStatus("mandatory")
_NpIPReasmFails_Type = Counter32
_NpIPReasmFails_Object = MibTableColumn
npIPReasmFails = _NpIPReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 16),
    _NpIPReasmFails_Type()
)
npIPReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPReasmFails.setStatus("mandatory")
_NpIPFragOKs_Type = Counter32
_NpIPFragOKs_Object = MibTableColumn
npIPFragOKs = _NpIPFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 17),
    _NpIPFragOKs_Type()
)
npIPFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPFragOKs.setStatus("mandatory")
_NpIPFragFails_Type = Counter32
_NpIPFragFails_Object = MibTableColumn
npIPFragFails = _NpIPFragFails_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 18),
    _NpIPFragFails_Type()
)
npIPFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPFragFails.setStatus("mandatory")
_NpIPFragCreates_Type = Counter32
_NpIPFragCreates_Object = MibTableColumn
npIPFragCreates = _NpIPFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 19),
    _NpIPFragCreates_Type()
)
npIPFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPFragCreates.setStatus("mandatory")
_NpIPRoutingDiscards_Type = Counter32
_NpIPRoutingDiscards_Object = MibTableColumn
npIPRoutingDiscards = _NpIPRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 1, 1, 20),
    _NpIPRoutingDiscards_Type()
)
npIPRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIPRoutingDiscards.setStatus("mandatory")
_NpICMPTable_Object = MibTable
npICMPTable = _NpICMPTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    npICMPTable.setStatus("mandatory")
_NpICMPEntry_Object = MibTableRow
npICMPEntry = _NpICMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1)
)
npICMPEntry.setIndexNames(
    (0, "NETSERVER-MIB", "npIndex"),
)
if mibBuilder.loadTexts:
    npICMPEntry.setStatus("mandatory")
_NpICMPInMsgs_Type = Counter32
_NpICMPInMsgs_Object = MibTableColumn
npICMPInMsgs = _NpICMPInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 1),
    _NpICMPInMsgs_Type()
)
npICMPInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInMsgs.setStatus("mandatory")
_NpICMPInErrors_Type = Counter32
_NpICMPInErrors_Object = MibTableColumn
npICMPInErrors = _NpICMPInErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 2),
    _NpICMPInErrors_Type()
)
npICMPInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInErrors.setStatus("mandatory")
_NpICMPInDestUnreachs_Type = Counter32
_NpICMPInDestUnreachs_Object = MibTableColumn
npICMPInDestUnreachs = _NpICMPInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 3),
    _NpICMPInDestUnreachs_Type()
)
npICMPInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInDestUnreachs.setStatus("mandatory")
_NpICMPInTimeExcds_Type = Counter32
_NpICMPInTimeExcds_Object = MibTableColumn
npICMPInTimeExcds = _NpICMPInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 4),
    _NpICMPInTimeExcds_Type()
)
npICMPInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInTimeExcds.setStatus("mandatory")
_NpICMPInParmProbs_Type = Counter32
_NpICMPInParmProbs_Object = MibTableColumn
npICMPInParmProbs = _NpICMPInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 5),
    _NpICMPInParmProbs_Type()
)
npICMPInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInParmProbs.setStatus("mandatory")
_NpICMPInSrcQuenchs_Type = Counter32
_NpICMPInSrcQuenchs_Object = MibTableColumn
npICMPInSrcQuenchs = _NpICMPInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 6),
    _NpICMPInSrcQuenchs_Type()
)
npICMPInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInSrcQuenchs.setStatus("mandatory")
_NpICMPInRedirects_Type = Counter32
_NpICMPInRedirects_Object = MibTableColumn
npICMPInRedirects = _NpICMPInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 7),
    _NpICMPInRedirects_Type()
)
npICMPInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInRedirects.setStatus("mandatory")
_NpICMPInEchos_Type = Counter32
_NpICMPInEchos_Object = MibTableColumn
npICMPInEchos = _NpICMPInEchos_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 8),
    _NpICMPInEchos_Type()
)
npICMPInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInEchos.setStatus("mandatory")
_NpICMPInEchoReps_Type = Counter32
_NpICMPInEchoReps_Object = MibTableColumn
npICMPInEchoReps = _NpICMPInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 9),
    _NpICMPInEchoReps_Type()
)
npICMPInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInEchoReps.setStatus("mandatory")
_NpICMPInTimestamps_Type = Counter32
_NpICMPInTimestamps_Object = MibTableColumn
npICMPInTimestamps = _NpICMPInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 10),
    _NpICMPInTimestamps_Type()
)
npICMPInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInTimestamps.setStatus("mandatory")
_NpICMPInTimestampReps_Type = Counter32
_NpICMPInTimestampReps_Object = MibTableColumn
npICMPInTimestampReps = _NpICMPInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 11),
    _NpICMPInTimestampReps_Type()
)
npICMPInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInTimestampReps.setStatus("mandatory")
_NpICMPInAddrMasks_Type = Counter32
_NpICMPInAddrMasks_Object = MibTableColumn
npICMPInAddrMasks = _NpICMPInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 12),
    _NpICMPInAddrMasks_Type()
)
npICMPInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInAddrMasks.setStatus("mandatory")
_NpICMPInAddrMaskReps_Type = Counter32
_NpICMPInAddrMaskReps_Object = MibTableColumn
npICMPInAddrMaskReps = _NpICMPInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 13),
    _NpICMPInAddrMaskReps_Type()
)
npICMPInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPInAddrMaskReps.setStatus("mandatory")
_NpICMPOutMsgs_Type = Counter32
_NpICMPOutMsgs_Object = MibTableColumn
npICMPOutMsgs = _NpICMPOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 14),
    _NpICMPOutMsgs_Type()
)
npICMPOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutMsgs.setStatus("mandatory")
_NpICMPOutErrors_Type = Counter32
_NpICMPOutErrors_Object = MibTableColumn
npICMPOutErrors = _NpICMPOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 15),
    _NpICMPOutErrors_Type()
)
npICMPOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutErrors.setStatus("mandatory")
_NpICMPOutDestUnreachs_Type = Counter32
_NpICMPOutDestUnreachs_Object = MibTableColumn
npICMPOutDestUnreachs = _NpICMPOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 16),
    _NpICMPOutDestUnreachs_Type()
)
npICMPOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutDestUnreachs.setStatus("mandatory")
_NpICMPOutTimeExcds_Type = Counter32
_NpICMPOutTimeExcds_Object = MibTableColumn
npICMPOutTimeExcds = _NpICMPOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 17),
    _NpICMPOutTimeExcds_Type()
)
npICMPOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutTimeExcds.setStatus("mandatory")
_NpICMPOutParmProbs_Type = Counter32
_NpICMPOutParmProbs_Object = MibTableColumn
npICMPOutParmProbs = _NpICMPOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 18),
    _NpICMPOutParmProbs_Type()
)
npICMPOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutParmProbs.setStatus("mandatory")
_NpICMPOutSrcQuenchs_Type = Counter32
_NpICMPOutSrcQuenchs_Object = MibTableColumn
npICMPOutSrcQuenchs = _NpICMPOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 19),
    _NpICMPOutSrcQuenchs_Type()
)
npICMPOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutSrcQuenchs.setStatus("mandatory")
_NpICMPOutRedirects_Type = Counter32
_NpICMPOutRedirects_Object = MibTableColumn
npICMPOutRedirects = _NpICMPOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 20),
    _NpICMPOutRedirects_Type()
)
npICMPOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutRedirects.setStatus("mandatory")
_NpICMPOutEchos_Type = Counter32
_NpICMPOutEchos_Object = MibTableColumn
npICMPOutEchos = _NpICMPOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 21),
    _NpICMPOutEchos_Type()
)
npICMPOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutEchos.setStatus("mandatory")
_NpICMPOutEchoReps_Type = Counter32
_NpICMPOutEchoReps_Object = MibTableColumn
npICMPOutEchoReps = _NpICMPOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 22),
    _NpICMPOutEchoReps_Type()
)
npICMPOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutEchoReps.setStatus("mandatory")
_NpICMPOutTimestamps_Type = Counter32
_NpICMPOutTimestamps_Object = MibTableColumn
npICMPOutTimestamps = _NpICMPOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 23),
    _NpICMPOutTimestamps_Type()
)
npICMPOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutTimestamps.setStatus("mandatory")
_NpICMPOutTimestampReps_Type = Counter32
_NpICMPOutTimestampReps_Object = MibTableColumn
npICMPOutTimestampReps = _NpICMPOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 24),
    _NpICMPOutTimestampReps_Type()
)
npICMPOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutTimestampReps.setStatus("mandatory")
_NpICMPOutAddrMasks_Type = Counter32
_NpICMPOutAddrMasks_Object = MibTableColumn
npICMPOutAddrMasks = _NpICMPOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 25),
    _NpICMPOutAddrMasks_Type()
)
npICMPOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutAddrMasks.setStatus("mandatory")
_NpICMPOutAddrMaskReps_Type = Counter32
_NpICMPOutAddrMaskReps_Object = MibTableColumn
npICMPOutAddrMaskReps = _NpICMPOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 2, 1, 26),
    _NpICMPOutAddrMaskReps_Type()
)
npICMPOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npICMPOutAddrMaskReps.setStatus("mandatory")
_NpTCPTable_Object = MibTable
npTCPTable = _NpTCPTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    npTCPTable.setStatus("mandatory")
_NpTCPEntry_Object = MibTableRow
npTCPEntry = _NpTCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1)
)
npTCPEntry.setIndexNames(
    (0, "NETSERVER-MIB", "npIndex"),
)
if mibBuilder.loadTexts:
    npTCPEntry.setStatus("mandatory")


class _NpTCPRtoAlgorithm_Type(Integer32):
    """Custom type npTCPRtoAlgorithm based on Integer32"""
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
        *(("constant", 2),
          ("other", 1),
          ("rsre", 3),
          ("vanj", 4))
    )


_NpTCPRtoAlgorithm_Type.__name__ = "Integer32"
_NpTCPRtoAlgorithm_Object = MibTableColumn
npTCPRtoAlgorithm = _NpTCPRtoAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 1),
    _NpTCPRtoAlgorithm_Type()
)
npTCPRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPRtoAlgorithm.setStatus("mandatory")
_NpTCPRtoMin_Type = Integer32
_NpTCPRtoMin_Object = MibTableColumn
npTCPRtoMin = _NpTCPRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 2),
    _NpTCPRtoMin_Type()
)
npTCPRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPRtoMin.setStatus("mandatory")
_NpTCPRtoMax_Type = Integer32
_NpTCPRtoMax_Object = MibTableColumn
npTCPRtoMax = _NpTCPRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 3),
    _NpTCPRtoMax_Type()
)
npTCPRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPRtoMax.setStatus("mandatory")
_NpTCPMaxConn_Type = Integer32
_NpTCPMaxConn_Object = MibTableColumn
npTCPMaxConn = _NpTCPMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 4),
    _NpTCPMaxConn_Type()
)
npTCPMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPMaxConn.setStatus("mandatory")
_NpTCPActiveOpens_Type = Counter32
_NpTCPActiveOpens_Object = MibTableColumn
npTCPActiveOpens = _NpTCPActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 5),
    _NpTCPActiveOpens_Type()
)
npTCPActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPActiveOpens.setStatus("mandatory")
_NpTCPPassiveOpens_Type = Counter32
_NpTCPPassiveOpens_Object = MibTableColumn
npTCPPassiveOpens = _NpTCPPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 6),
    _NpTCPPassiveOpens_Type()
)
npTCPPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPPassiveOpens.setStatus("mandatory")
_NpTCPAttemptFails_Type = Counter32
_NpTCPAttemptFails_Object = MibTableColumn
npTCPAttemptFails = _NpTCPAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 7),
    _NpTCPAttemptFails_Type()
)
npTCPAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPAttemptFails.setStatus("mandatory")
_NpTCPEstabResets_Type = Counter32
_NpTCPEstabResets_Object = MibTableColumn
npTCPEstabResets = _NpTCPEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 8),
    _NpTCPEstabResets_Type()
)
npTCPEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPEstabResets.setStatus("mandatory")
_NpTCPCurrEstab_Type = Integer32
_NpTCPCurrEstab_Object = MibTableColumn
npTCPCurrEstab = _NpTCPCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 9),
    _NpTCPCurrEstab_Type()
)
npTCPCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPCurrEstab.setStatus("mandatory")
_NpTCPInSegs_Type = Counter32
_NpTCPInSegs_Object = MibTableColumn
npTCPInSegs = _NpTCPInSegs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 10),
    _NpTCPInSegs_Type()
)
npTCPInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPInSegs.setStatus("mandatory")
_NpTCPOutSegs_Type = Counter32
_NpTCPOutSegs_Object = MibTableColumn
npTCPOutSegs = _NpTCPOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 11),
    _NpTCPOutSegs_Type()
)
npTCPOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPOutSegs.setStatus("mandatory")
_NpTCPRetransSegs_Type = Counter32
_NpTCPRetransSegs_Object = MibTableColumn
npTCPRetransSegs = _NpTCPRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 12),
    _NpTCPRetransSegs_Type()
)
npTCPRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPRetransSegs.setStatus("mandatory")
_NpTCPInErrs_Type = Counter32
_NpTCPInErrs_Object = MibTableColumn
npTCPInErrs = _NpTCPInErrs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 13),
    _NpTCPInErrs_Type()
)
npTCPInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPInErrs.setStatus("mandatory")
_NpTCPOutRsts_Type = Counter32
_NpTCPOutRsts_Object = MibTableColumn
npTCPOutRsts = _NpTCPOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 3, 1, 14),
    _NpTCPOutRsts_Type()
)
npTCPOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTCPOutRsts.setStatus("mandatory")
_NpUDPTable_Object = MibTable
npUDPTable = _NpUDPTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    npUDPTable.setStatus("mandatory")
_NpUDPEntry_Object = MibTableRow
npUDPEntry = _NpUDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 4, 1)
)
npUDPEntry.setIndexNames(
    (0, "NETSERVER-MIB", "npIndex"),
)
if mibBuilder.loadTexts:
    npUDPEntry.setStatus("mandatory")
_NpUDPInDatagrams_Type = Counter32
_NpUDPInDatagrams_Object = MibTableColumn
npUDPInDatagrams = _NpUDPInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 4, 1, 1),
    _NpUDPInDatagrams_Type()
)
npUDPInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npUDPInDatagrams.setStatus("mandatory")
_NpUDPNoPorts_Type = Counter32
_NpUDPNoPorts_Object = MibTableColumn
npUDPNoPorts = _NpUDPNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 4, 1, 2),
    _NpUDPNoPorts_Type()
)
npUDPNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npUDPNoPorts.setStatus("mandatory")
_NpUDPInErrors_Type = Counter32
_NpUDPInErrors_Object = MibTableColumn
npUDPInErrors = _NpUDPInErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 4, 1, 3),
    _NpUDPInErrors_Type()
)
npUDPInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npUDPInErrors.setStatus("mandatory")
_NpUDPOutDatagrams_Type = Counter32
_NpUDPOutDatagrams_Object = MibTableColumn
npUDPOutDatagrams = _NpUDPOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 4, 1, 4),
    _NpUDPOutDatagrams_Type()
)
npUDPOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npUDPOutDatagrams.setStatus("mandatory")
_NpNFSTable_Object = MibTable
npNFSTable = _NpNFSTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 5)
)
if mibBuilder.loadTexts:
    npNFSTable.setStatus("mandatory")
_NpNFSEntry_Object = MibTableRow
npNFSEntry = _NpNFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 5, 1)
)
npNFSEntry.setIndexNames(
    (0, "NETSERVER-MIB", "npIndex"),
)
if mibBuilder.loadTexts:
    npNFSEntry.setStatus("mandatory")
_NpNFSDCounts_Type = Counter32
_NpNFSDCounts_Object = MibTableColumn
npNFSDCounts = _NpNFSDCounts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 5, 1, 1),
    _NpNFSDCounts_Type()
)
npNFSDCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npNFSDCounts.setStatus("mandatory")
_NpNFSDNJobs_Type = Counter32
_NpNFSDNJobs_Object = MibTableColumn
npNFSDNJobs = _NpNFSDNJobs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 5, 1, 2),
    _NpNFSDNJobs_Type()
)
npNFSDNJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npNFSDNJobs.setStatus("mandatory")
_NpNFSDBusyCounts_Type = Counter32
_NpNFSDBusyCounts_Object = MibTableColumn
npNFSDBusyCounts = _NpNFSDBusyCounts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 5, 1, 3),
    _NpNFSDBusyCounts_Type()
)
npNFSDBusyCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npNFSDBusyCounts.setStatus("mandatory")
_NpSMBTable_Object = MibTable
npSMBTable = _NpSMBTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6)
)
if mibBuilder.loadTexts:
    npSMBTable.setStatus("mandatory")
_NpSMBEntry_Object = MibTableRow
npSMBEntry = _NpSMBEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1)
)
npSMBEntry.setIndexNames(
    (0, "NETSERVER-MIB", "npIndex"),
)
if mibBuilder.loadTexts:
    npSMBEntry.setStatus("mandatory")
_NpSMBRcvd_Type = Counter32
_NpSMBRcvd_Object = MibTableColumn
npSMBRcvd = _NpSMBRcvd_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1, 1),
    _NpSMBRcvd_Type()
)
npSMBRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSMBRcvd.setStatus("mandatory")
_NpSMBBytesRcvd_Type = Counter32
_NpSMBBytesRcvd_Object = MibTableColumn
npSMBBytesRcvd = _NpSMBBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1, 2),
    _NpSMBBytesRcvd_Type()
)
npSMBBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSMBBytesRcvd.setStatus("mandatory")
_NpSMBBytesSent_Type = Counter32
_NpSMBBytesSent_Object = MibTableColumn
npSMBBytesSent = _NpSMBBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1, 3),
    _NpSMBBytesSent_Type()
)
npSMBBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSMBBytesSent.setStatus("mandatory")
_NpSMBReads_Type = Counter32
_NpSMBReads_Object = MibTableColumn
npSMBReads = _NpSMBReads_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1, 4),
    _NpSMBReads_Type()
)
npSMBReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSMBReads.setStatus("mandatory")
_NpSMBWrites_Type = Counter32
_NpSMBWrites_Object = MibTableColumn
npSMBWrites = _NpSMBWrites_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1, 5),
    _NpSMBWrites_Type()
)
npSMBWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSMBWrites.setStatus("mandatory")
_NpSMBOpens_Type = Counter32
_NpSMBOpens_Object = MibTableColumn
npSMBOpens = _NpSMBOpens_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1, 6),
    _NpSMBOpens_Type()
)
npSMBOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSMBOpens.setStatus("mandatory")
_NpSMBCloses_Type = Counter32
_NpSMBCloses_Object = MibTableColumn
npSMBCloses = _NpSMBCloses_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1, 7),
    _NpSMBCloses_Type()
)
npSMBCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSMBCloses.setStatus("mandatory")
_NpSMBErrors_Type = Counter32
_NpSMBErrors_Object = MibTableColumn
npSMBErrors = _NpSMBErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1, 8),
    _NpSMBErrors_Type()
)
npSMBErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSMBErrors.setStatus("mandatory")
_NpSMBLocksHeld_Type = Integer32
_NpSMBLocksHeld_Object = MibTableColumn
npSMBLocksHeld = _NpSMBLocksHeld_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 2, 3, 6, 1, 9),
    _NpSMBLocksHeld_Type()
)
npSMBLocksHeld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npSMBLocksHeld.setStatus("mandatory")
_AxFSP_ObjectIdentity = ObjectIdentity
axFSP = _AxFSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 3)
)
_FspTable_Object = MibTable
fspTable = _FspTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 1)
)
if mibBuilder.loadTexts:
    fspTable.setStatus("mandatory")
_FspEntry_Object = MibTableRow
fspEntry = _FspEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 1, 1)
)
fspEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
)
if mibBuilder.loadTexts:
    fspEntry.setStatus("mandatory")
_FspIndex_Type = Integer32
_FspIndex_Object = MibTableColumn
fspIndex = _FspIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 1, 1, 1),
    _FspIndex_Type()
)
fspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspIndex.setStatus("mandatory")
_FspBusyCount_Type = Counter32
_FspBusyCount_Object = MibTableColumn
fspBusyCount = _FspBusyCount_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 1, 1, 2),
    _FspBusyCount_Type()
)
fspBusyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspBusyCount.setStatus("mandatory")
_FspIdleCount_Type = Counter32
_FspIdleCount_Object = MibTableColumn
fspIdleCount = _FspIdleCount_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 1, 1, 3),
    _FspIdleCount_Type()
)
fspIdleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspIdleCount.setStatus("mandatory")
_AxFP_ObjectIdentity = ObjectIdentity
axFP = _AxFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2)
)
_FpLFSTable_Object = MibTable
fpLFSTable = _FpLFSTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fpLFSTable.setStatus("mandatory")
_FpLFSEntry_Object = MibTableRow
fpLFSEntry = _FpLFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1)
)
fpLFSEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
)
if mibBuilder.loadTexts:
    fpLFSEntry.setStatus("mandatory")
_FpLFSVersion_Type = Integer32
_FpLFSVersion_Object = MibTableColumn
fpLFSVersion = _FpLFSVersion_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 1),
    _FpLFSVersion_Type()
)
fpLFSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSVersion.setStatus("mandatory")
_FpLFSMounts_Type = Counter32
_FpLFSMounts_Object = MibTableColumn
fpLFSMounts = _FpLFSMounts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 2),
    _FpLFSMounts_Type()
)
fpLFSMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSMounts.setStatus("mandatory")
_FpLFSUMounts_Type = Counter32
_FpLFSUMounts_Object = MibTableColumn
fpLFSUMounts = _FpLFSUMounts_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 3),
    _FpLFSUMounts_Type()
)
fpLFSUMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSUMounts.setStatus("mandatory")
_FpLFSReads_Type = Counter32
_FpLFSReads_Object = MibTableColumn
fpLFSReads = _FpLFSReads_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 4),
    _FpLFSReads_Type()
)
fpLFSReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSReads.setStatus("mandatory")
_FpLFSWrites_Type = Counter32
_FpLFSWrites_Object = MibTableColumn
fpLFSWrites = _FpLFSWrites_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 5),
    _FpLFSWrites_Type()
)
fpLFSWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSWrites.setStatus("mandatory")
_FpLFSReaddirs_Type = Counter32
_FpLFSReaddirs_Object = MibTableColumn
fpLFSReaddirs = _FpLFSReaddirs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 6),
    _FpLFSReaddirs_Type()
)
fpLFSReaddirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSReaddirs.setStatus("mandatory")
_FpLFSReadlinks_Type = Counter32
_FpLFSReadlinks_Object = MibTableColumn
fpLFSReadlinks = _FpLFSReadlinks_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 7),
    _FpLFSReadlinks_Type()
)
fpLFSReadlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSReadlinks.setStatus("mandatory")
_FpLFSMkdirs_Type = Counter32
_FpLFSMkdirs_Object = MibTableColumn
fpLFSMkdirs = _FpLFSMkdirs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 8),
    _FpLFSMkdirs_Type()
)
fpLFSMkdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSMkdirs.setStatus("mandatory")
_FpLFSMknods_Type = Counter32
_FpLFSMknods_Object = MibTableColumn
fpLFSMknods = _FpLFSMknods_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 9),
    _FpLFSMknods_Type()
)
fpLFSMknods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSMknods.setStatus("mandatory")
_FpLFSReaddirPluses_Type = Counter32
_FpLFSReaddirPluses_Object = MibTableColumn
fpLFSReaddirPluses = _FpLFSReaddirPluses_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 10),
    _FpLFSReaddirPluses_Type()
)
fpLFSReaddirPluses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSReaddirPluses.setStatus("mandatory")
_FpLFSFsstats_Type = Counter32
_FpLFSFsstats_Object = MibTableColumn
fpLFSFsstats = _FpLFSFsstats_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 11),
    _FpLFSFsstats_Type()
)
fpLFSFsstats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSFsstats.setStatus("mandatory")
_FpLFSNull_Type = Counter32
_FpLFSNull_Object = MibTableColumn
fpLFSNull = _FpLFSNull_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 12),
    _FpLFSNull_Type()
)
fpLFSNull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSNull.setStatus("mandatory")
_FpLFSFsinfo_Type = Counter32
_FpLFSFsinfo_Object = MibTableColumn
fpLFSFsinfo = _FpLFSFsinfo_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 13),
    _FpLFSFsinfo_Type()
)
fpLFSFsinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSFsinfo.setStatus("mandatory")
_FpLFSGetattrs_Type = Counter32
_FpLFSGetattrs_Object = MibTableColumn
fpLFSGetattrs = _FpLFSGetattrs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 14),
    _FpLFSGetattrs_Type()
)
fpLFSGetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSGetattrs.setStatus("mandatory")
_FpLFSSetattrs_Type = Counter32
_FpLFSSetattrs_Object = MibTableColumn
fpLFSSetattrs = _FpLFSSetattrs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 15),
    _FpLFSSetattrs_Type()
)
fpLFSSetattrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSSetattrs.setStatus("mandatory")
_FpLFSLookups_Type = Counter32
_FpLFSLookups_Object = MibTableColumn
fpLFSLookups = _FpLFSLookups_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 16),
    _FpLFSLookups_Type()
)
fpLFSLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSLookups.setStatus("mandatory")
_FpLFSCreates_Type = Counter32
_FpLFSCreates_Object = MibTableColumn
fpLFSCreates = _FpLFSCreates_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 17),
    _FpLFSCreates_Type()
)
fpLFSCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSCreates.setStatus("mandatory")
_FpLFSRemoves_Type = Counter32
_FpLFSRemoves_Object = MibTableColumn
fpLFSRemoves = _FpLFSRemoves_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 18),
    _FpLFSRemoves_Type()
)
fpLFSRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSRemoves.setStatus("mandatory")
_FpLFSRenames_Type = Counter32
_FpLFSRenames_Object = MibTableColumn
fpLFSRenames = _FpLFSRenames_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 19),
    _FpLFSRenames_Type()
)
fpLFSRenames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSRenames.setStatus("mandatory")
_FpLFSLinks_Type = Counter32
_FpLFSLinks_Object = MibTableColumn
fpLFSLinks = _FpLFSLinks_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 20),
    _FpLFSLinks_Type()
)
fpLFSLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSLinks.setStatus("mandatory")
_FpLFSSymlinks_Type = Counter32
_FpLFSSymlinks_Object = MibTableColumn
fpLFSSymlinks = _FpLFSSymlinks_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 21),
    _FpLFSSymlinks_Type()
)
fpLFSSymlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSSymlinks.setStatus("mandatory")
_FpLFSRmdirs_Type = Counter32
_FpLFSRmdirs_Object = MibTableColumn
fpLFSRmdirs = _FpLFSRmdirs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 22),
    _FpLFSRmdirs_Type()
)
fpLFSRmdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSRmdirs.setStatus("mandatory")
_FpLFSCkpntons_Type = Counter32
_FpLFSCkpntons_Object = MibTableColumn
fpLFSCkpntons = _FpLFSCkpntons_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 23),
    _FpLFSCkpntons_Type()
)
fpLFSCkpntons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSCkpntons.setStatus("mandatory")
_FpLFSCkpntoffs_Type = Counter32
_FpLFSCkpntoffs_Object = MibTableColumn
fpLFSCkpntoffs = _FpLFSCkpntoffs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 24),
    _FpLFSCkpntoffs_Type()
)
fpLFSCkpntoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSCkpntoffs.setStatus("mandatory")
_FpLFSClears_Type = Counter32
_FpLFSClears_Object = MibTableColumn
fpLFSClears = _FpLFSClears_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 25),
    _FpLFSClears_Type()
)
fpLFSClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSClears.setStatus("mandatory")
_FpLFSIsolateFs_Type = Counter32
_FpLFSIsolateFs_Object = MibTableColumn
fpLFSIsolateFs = _FpLFSIsolateFs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 26),
    _FpLFSIsolateFs_Type()
)
fpLFSIsolateFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSIsolateFs.setStatus("mandatory")
_FpLFSReleaseFs_Type = Counter32
_FpLFSReleaseFs_Object = MibTableColumn
fpLFSReleaseFs = _FpLFSReleaseFs_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 27),
    _FpLFSReleaseFs_Type()
)
fpLFSReleaseFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSReleaseFs.setStatus("mandatory")
_FpLFSIsolationStates_Type = Counter32
_FpLFSIsolationStates_Object = MibTableColumn
fpLFSIsolationStates = _FpLFSIsolationStates_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 28),
    _FpLFSIsolationStates_Type()
)
fpLFSIsolationStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSIsolationStates.setStatus("mandatory")
_FpLFSDiagnostics_Type = Counter32
_FpLFSDiagnostics_Object = MibTableColumn
fpLFSDiagnostics = _FpLFSDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 29),
    _FpLFSDiagnostics_Type()
)
fpLFSDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSDiagnostics.setStatus("mandatory")
_FpLFSPurges_Type = Counter32
_FpLFSPurges_Object = MibTableColumn
fpLFSPurges = _FpLFSPurges_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 1, 1, 30),
    _FpLFSPurges_Type()
)
fpLFSPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLFSPurges.setStatus("mandatory")
_FpFileSystemTable_Object = MibTable
fpFileSystemTable = _FpFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fpFileSystemTable.setStatus("mandatory")
_FpFSEntry_Object = MibTableRow
fpFSEntry = _FpFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 2, 1)
)
fpFSEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
    (0, "NETSERVER-MIB", "fpFSIndex"),
)
if mibBuilder.loadTexts:
    fpFSEntry.setStatus("mandatory")
_FpFSIndex_Type = Integer32
_FpFSIndex_Object = MibTableColumn
fpFSIndex = _FpFSIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 2, 1, 1),
    _FpFSIndex_Type()
)
fpFSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpFSIndex.setStatus("mandatory")
_FpHrFSIndex_Type = Integer32
_FpHrFSIndex_Object = MibTableColumn
fpHrFSIndex = _FpHrFSIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 2, 1, 2),
    _FpHrFSIndex_Type()
)
fpHrFSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpHrFSIndex.setStatus("mandatory")
_FpHTFS_ObjectIdentity = ObjectIdentity
fpHTFS = _FpHTFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3)
)
_FpDNLCTStatTable_Object = MibTable
fpDNLCTStatTable = _FpDNLCTStatTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fpDNLCTStatTable.setStatus("mandatory")
_FpDNLCSEntry_Object = MibTableRow
fpDNLCSEntry = _FpDNLCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 1, 1)
)
fpDNLCSEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
)
if mibBuilder.loadTexts:
    fpDNLCSEntry.setStatus("mandatory")
_FpDNLCHit_Type = Integer32
_FpDNLCHit_Object = MibTableColumn
fpDNLCHit = _FpDNLCHit_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 1, 1, 1),
    _FpDNLCHit_Type()
)
fpDNLCHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDNLCHit.setStatus("mandatory")
_FpDNLCMiss_Type = Integer32
_FpDNLCMiss_Object = MibTableColumn
fpDNLCMiss = _FpDNLCMiss_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 1, 1, 2),
    _FpDNLCMiss_Type()
)
fpDNLCMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDNLCMiss.setStatus("mandatory")
_FpDNLCEnter_Type = Integer32
_FpDNLCEnter_Object = MibTableColumn
fpDNLCEnter = _FpDNLCEnter_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 1, 1, 3),
    _FpDNLCEnter_Type()
)
fpDNLCEnter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDNLCEnter.setStatus("mandatory")
_FpDNLCConflict_Type = Integer32
_FpDNLCConflict_Object = MibTableColumn
fpDNLCConflict = _FpDNLCConflict_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 1, 1, 4),
    _FpDNLCConflict_Type()
)
fpDNLCConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDNLCConflict.setStatus("mandatory")
_FpDNLCPurgevfsp_Type = Integer32
_FpDNLCPurgevfsp_Object = MibTableColumn
fpDNLCPurgevfsp = _FpDNLCPurgevfsp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 1, 1, 5),
    _FpDNLCPurgevfsp_Type()
)
fpDNLCPurgevfsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDNLCPurgevfsp.setStatus("mandatory")
_FpDNLCPurgevp_Type = Integer32
_FpDNLCPurgevp_Object = MibTableColumn
fpDNLCPurgevp = _FpDNLCPurgevp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 1, 1, 6),
    _FpDNLCPurgevp_Type()
)
fpDNLCPurgevp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDNLCPurgevp.setStatus("mandatory")
_FpDNLCHashsz_Type = Integer32
_FpDNLCHashsz_Object = MibTableColumn
fpDNLCHashsz = _FpDNLCHashsz_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 1, 1, 7),
    _FpDNLCHashsz_Type()
)
fpDNLCHashsz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDNLCHashsz.setStatus("mandatory")
_FpPageStatTable_Object = MibTable
fpPageStatTable = _FpPageStatTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fpPageStatTable.setStatus("mandatory")
_FpPageEntry_Object = MibTableRow
fpPageEntry = _FpPageEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1)
)
fpPageEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
)
if mibBuilder.loadTexts:
    fpPageEntry.setStatus("mandatory")
_FpPAGETotalmem_Type = Integer32
_FpPAGETotalmem_Object = MibTableColumn
fpPAGETotalmem = _FpPAGETotalmem_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 1),
    _FpPAGETotalmem_Type()
)
fpPAGETotalmem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGETotalmem.setStatus("mandatory")
_FpPAGEFreelistcnt_Type = Integer32
_FpPAGEFreelistcnt_Object = MibTableColumn
fpPAGEFreelistcnt = _FpPAGEFreelistcnt_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 2),
    _FpPAGEFreelistcnt_Type()
)
fpPAGEFreelistcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEFreelistcnt.setStatus("mandatory")
_FpPAGECachelistcnt_Type = Integer32
_FpPAGECachelistcnt_Object = MibTableColumn
fpPAGECachelistcnt = _FpPAGECachelistcnt_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 3),
    _FpPAGECachelistcnt_Type()
)
fpPAGECachelistcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGECachelistcnt.setStatus("mandatory")
_FpPAGEDirtyflistcnt_Type = Integer32
_FpPAGEDirtyflistcnt_Object = MibTableColumn
fpPAGEDirtyflistcnt = _FpPAGEDirtyflistcnt_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 4),
    _FpPAGEDirtyflistcnt_Type()
)
fpPAGEDirtyflistcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEDirtyflistcnt.setStatus("mandatory")
_FpPAGEDirtydlistcnt_Type = Integer32
_FpPAGEDirtydlistcnt_Object = MibTableColumn
fpPAGEDirtydlistcnt = _FpPAGEDirtydlistcnt_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 5),
    _FpPAGEDirtydlistcnt_Type()
)
fpPAGEDirtydlistcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEDirtydlistcnt.setStatus("mandatory")
_FpPAGECachehit_Type = Integer32
_FpPAGECachehit_Object = MibTableColumn
fpPAGECachehit = _FpPAGECachehit_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 6),
    _FpPAGECachehit_Type()
)
fpPAGECachehit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGECachehit.setStatus("mandatory")
_FpPAGECachemiss_Type = Integer32
_FpPAGECachemiss_Object = MibTableColumn
fpPAGECachemiss = _FpPAGECachemiss_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 7),
    _FpPAGECachemiss_Type()
)
fpPAGECachemiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGECachemiss.setStatus("mandatory")
_FpPAGEWritehit_Type = Integer32
_FpPAGEWritehit_Object = MibTableColumn
fpPAGEWritehit = _FpPAGEWritehit_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 8),
    _FpPAGEWritehit_Type()
)
fpPAGEWritehit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEWritehit.setStatus("mandatory")
_FpPAGEWritemiss_Type = Integer32
_FpPAGEWritemiss_Object = MibTableColumn
fpPAGEWritemiss = _FpPAGEWritemiss_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 9),
    _FpPAGEWritemiss_Type()
)
fpPAGEWritemiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEWritemiss.setStatus("mandatory")
_FpPAGEZcref_Type = Integer32
_FpPAGEZcref_Object = MibTableColumn
fpPAGEZcref = _FpPAGEZcref_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 10),
    _FpPAGEZcref_Type()
)
fpPAGEZcref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEZcref.setStatus("mandatory")
_FpPAGEZcbreak_Type = Integer32
_FpPAGEZcbreak_Object = MibTableColumn
fpPAGEZcbreak = _FpPAGEZcbreak_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 11),
    _FpPAGEZcbreak_Type()
)
fpPAGEZcbreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEZcbreak.setStatus("mandatory")
_FpPAGEOutscan_Type = Integer32
_FpPAGEOutscan_Object = MibTableColumn
fpPAGEOutscan = _FpPAGEOutscan_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 12),
    _FpPAGEOutscan_Type()
)
fpPAGEOutscan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEOutscan.setStatus("mandatory")
_FpPAGEOutputpage_Type = Integer32
_FpPAGEOutputpage_Object = MibTableColumn
fpPAGEOutputpage = _FpPAGEOutputpage_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 13),
    _FpPAGEOutputpage_Type()
)
fpPAGEOutputpage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEOutputpage.setStatus("mandatory")
_FpPAGEFsflushscan_Type = Integer32
_FpPAGEFsflushscan_Object = MibTableColumn
fpPAGEFsflushscan = _FpPAGEFsflushscan_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 14),
    _FpPAGEFsflushscan_Type()
)
fpPAGEFsflushscan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEFsflushscan.setStatus("mandatory")
_FpPAGEFsflushputpage_Type = Integer32
_FpPAGEFsflushputpage_Object = MibTableColumn
fpPAGEFsflushputpage = _FpPAGEFsflushputpage_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 15),
    _FpPAGEFsflushputpage_Type()
)
fpPAGEFsflushputpage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEFsflushputpage.setStatus("mandatory")
_FpPAGEOutcnt_Type = Integer32
_FpPAGEOutcnt_Object = MibTableColumn
fpPAGEOutcnt = _FpPAGEOutcnt_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 2, 1, 16),
    _FpPAGEOutcnt_Type()
)
fpPAGEOutcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPAGEOutcnt.setStatus("mandatory")
_FpBufferStatTable_Object = MibTable
fpBufferStatTable = _FpBufferStatTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    fpBufferStatTable.setStatus("mandatory")
_FpBufferEntry_Object = MibTableRow
fpBufferEntry = _FpBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3, 1)
)
fpBufferEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
)
if mibBuilder.loadTexts:
    fpBufferEntry.setStatus("mandatory")
_FpBUFLreads_Type = Integer32
_FpBUFLreads_Object = MibTableColumn
fpBUFLreads = _FpBUFLreads_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3, 1, 1),
    _FpBUFLreads_Type()
)
fpBUFLreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpBUFLreads.setStatus("mandatory")
_FpBUFBreads_Type = Integer32
_FpBUFBreads_Object = MibTableColumn
fpBUFBreads = _FpBUFBreads_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3, 1, 2),
    _FpBUFBreads_Type()
)
fpBUFBreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpBUFBreads.setStatus("mandatory")
_FpBUFLwrites_Type = Integer32
_FpBUFLwrites_Object = MibTableColumn
fpBUFLwrites = _FpBUFLwrites_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3, 1, 3),
    _FpBUFLwrites_Type()
)
fpBUFLwrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpBUFLwrites.setStatus("mandatory")
_FpBUFBwrites_Type = Integer32
_FpBUFBwrites_Object = MibTableColumn
fpBUFBwrites = _FpBUFBwrites_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3, 1, 4),
    _FpBUFBwrites_Type()
)
fpBUFBwrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpBUFBwrites.setStatus("mandatory")
_FpBUFIOwaits_Type = Integer32
_FpBUFIOwaits_Object = MibTableColumn
fpBUFIOwaits = _FpBUFIOwaits_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3, 1, 5),
    _FpBUFIOwaits_Type()
)
fpBUFIOwaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpBUFIOwaits.setStatus("mandatory")
_FpBUFResid_Type = Integer32
_FpBUFResid_Object = MibTableColumn
fpBUFResid = _FpBUFResid_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3, 1, 6),
    _FpBUFResid_Type()
)
fpBUFResid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpBUFResid.setStatus("mandatory")
_FpBUFBufsize_Type = Integer32
_FpBUFBufsize_Object = MibTableColumn
fpBUFBufsize = _FpBUFBufsize_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3, 1, 7),
    _FpBUFBufsize_Type()
)
fpBUFBufsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpBUFBufsize.setStatus("mandatory")
_FpBUFBcount_Type = Integer32
_FpBUFBcount_Object = MibTableColumn
fpBUFBcount = _FpBUFBcount_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 3, 1, 8),
    _FpBUFBcount_Type()
)
fpBUFBcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpBUFBcount.setStatus("mandatory")
_FpInodeTable_Object = MibTable
fpInodeTable = _FpInodeTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    fpInodeTable.setStatus("mandatory")
_FpInodeEntry_Object = MibTableRow
fpInodeEntry = _FpInodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 4, 1)
)
fpInodeEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
)
if mibBuilder.loadTexts:
    fpInodeEntry.setStatus("mandatory")
_FpINODEIgetcalls_Type = Integer32
_FpINODEIgetcalls_Object = MibTableColumn
fpINODEIgetcalls = _FpINODEIgetcalls_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 4, 1, 1),
    _FpINODEIgetcalls_Type()
)
fpINODEIgetcalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpINODEIgetcalls.setStatus("mandatory")
_FpFoundinodes_Type = Integer32
_FpFoundinodes_Object = MibTableColumn
fpFoundinodes = _FpFoundinodes_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 4, 1, 2),
    _FpFoundinodes_Type()
)
fpFoundinodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpFoundinodes.setStatus("mandatory")
_FpTotalinodes_Type = Integer32
_FpTotalinodes_Object = MibTableColumn
fpTotalinodes = _FpTotalinodes_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 4, 1, 3),
    _FpTotalinodes_Type()
)
fpTotalinodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpTotalinodes.setStatus("mandatory")
_FpGoneinodes_Type = Integer32
_FpGoneinodes_Object = MibTableColumn
fpGoneinodes = _FpGoneinodes_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 4, 1, 4),
    _FpGoneinodes_Type()
)
fpGoneinodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpGoneinodes.setStatus("mandatory")
_FpFreeinodes_Type = Integer32
_FpFreeinodes_Object = MibTableColumn
fpFreeinodes = _FpFreeinodes_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 4, 1, 5),
    _FpFreeinodes_Type()
)
fpFreeinodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpFreeinodes.setStatus("mandatory")
_FpCacheinodes_Type = Integer32
_FpCacheinodes_Object = MibTableColumn
fpCacheinodes = _FpCacheinodes_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 4, 1, 6),
    _FpCacheinodes_Type()
)
fpCacheinodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpCacheinodes.setStatus("mandatory")
_FpSyncinodes_Type = Integer32
_FpSyncinodes_Object = MibTableColumn
fpSyncinodes = _FpSyncinodes_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 2, 3, 4, 1, 7),
    _FpSyncinodes_Type()
)
fpSyncinodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpSyncinodes.setStatus("mandatory")
_AxSP_ObjectIdentity = ObjectIdentity
axSP = _AxSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 3)
)
_SpRaid_ObjectIdentity = ObjectIdentity
spRaid = _SpRaid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 3, 2)
)
_AxFab_ObjectIdentity = ObjectIdentity
axFab = _AxFab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4)
)
_FabAdptTable_Object = MibTable
fabAdptTable = _FabAdptTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    fabAdptTable.setStatus("mandatory")
_FabAdptEntry_Object = MibTableRow
fabAdptEntry = _FabAdptEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1)
)
fabAdptEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
    (0, "NETSERVER-MIB", "fabIndex"),
)
if mibBuilder.loadTexts:
    fabAdptEntry.setStatus("mandatory")
_FabIndex_Type = Integer32
_FabIndex_Object = MibTableColumn
fabIndex = _FabIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 1),
    _FabIndex_Type()
)
fabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabIndex.setStatus("mandatory")
_FabPCIBusNum_Type = U16Bits
_FabPCIBusNum_Object = MibTableColumn
fabPCIBusNum = _FabPCIBusNum_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 2),
    _FabPCIBusNum_Type()
)
fabPCIBusNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabPCIBusNum.setStatus("mandatory")
_FabSlotNum_Type = U16Bits
_FabSlotNum_Object = MibTableColumn
fabSlotNum = _FabSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 3),
    _FabSlotNum_Type()
)
fabSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabSlotNum.setStatus("mandatory")
_FabIntLine_Type = U16Bits
_FabIntLine_Object = MibTableColumn
fabIntLine = _FabIntLine_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 4),
    _FabIntLine_Type()
)
fabIntLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabIntLine.setStatus("mandatory")
_FabIntPin_Type = U16Bits
_FabIntPin_Object = MibTableColumn
fabIntPin = _FabIntPin_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 5),
    _FabIntPin_Type()
)
fabIntPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabIntPin.setStatus("mandatory")
_FabType_Type = U16Bits
_FabType_Object = MibTableColumn
fabType = _FabType_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 6),
    _FabType_Type()
)
fabType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabType.setStatus("mandatory")
_FabVendorId_Type = U16Bits
_FabVendorId_Object = MibTableColumn
fabVendorId = _FabVendorId_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 7),
    _FabVendorId_Type()
)
fabVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabVendorId.setStatus("mandatory")
_FabDeviceId_Type = U16Bits
_FabDeviceId_Object = MibTableColumn
fabDeviceId = _FabDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 8),
    _FabDeviceId_Type()
)
fabDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabDeviceId.setStatus("mandatory")
_FabRevisionId_Type = U16Bits
_FabRevisionId_Object = MibTableColumn
fabRevisionId = _FabRevisionId_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 9),
    _FabRevisionId_Type()
)
fabRevisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabRevisionId.setStatus("mandatory")
_FabWWN_Type = DisplayString
_FabWWN_Object = MibTableColumn
fabWWN = _FabWWN_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 10),
    _FabWWN_Type()
)
fabWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabWWN.setStatus("mandatory")
_FabNumOfTargets_Type = U16Bits
_FabNumOfTargets_Object = MibTableColumn
fabNumOfTargets = _FabNumOfTargets_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 11),
    _FabNumOfTargets_Type()
)
fabNumOfTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabNumOfTargets.setStatus("mandatory")
_FabAdptNumber_Type = U08Bits
_FabAdptNumber_Object = MibTableColumn
fabAdptNumber = _FabAdptNumber_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 1, 1, 12),
    _FabAdptNumber_Type()
)
fabAdptNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabAdptNumber.setStatus("mandatory")
_FabTargetTable_Object = MibTable
fabTargetTable = _FabTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    fabTargetTable.setStatus("mandatory")
_FabTargetEntry_Object = MibTableRow
fabTargetEntry = _FabTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2, 1)
)
fabTargetEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
    (0, "NETSERVER-MIB", "fabTargetIndex"),
)
if mibBuilder.loadTexts:
    fabTargetEntry.setStatus("mandatory")
_FabTargetIndex_Type = Integer32
_FabTargetIndex_Object = MibTableColumn
fabTargetIndex = _FabTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2, 1, 1),
    _FabTargetIndex_Type()
)
fabTargetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabTargetIndex.setStatus("mandatory")
_FabTargetAdapterNum_Type = U08Bits
_FabTargetAdapterNum_Object = MibTableColumn
fabTargetAdapterNum = _FabTargetAdapterNum_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2, 1, 2),
    _FabTargetAdapterNum_Type()
)
fabTargetAdapterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabTargetAdapterNum.setStatus("mandatory")
_FabTargetNumber_Type = U16Bits
_FabTargetNumber_Object = MibTableColumn
fabTargetNumber = _FabTargetNumber_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2, 1, 3),
    _FabTargetNumber_Type()
)
fabTargetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabTargetNumber.setStatus("mandatory")
_FabTargetWWN_Type = DisplayString
_FabTargetWWN_Object = MibTableColumn
fabTargetWWN = _FabTargetWWN_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2, 1, 4),
    _FabTargetWWN_Type()
)
fabTargetWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabTargetWWN.setStatus("mandatory")
_FabTargetPortWWN_Type = DisplayString
_FabTargetPortWWN_Object = MibTableColumn
fabTargetPortWWN = _FabTargetPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2, 1, 5),
    _FabTargetPortWWN_Type()
)
fabTargetPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabTargetPortWWN.setStatus("mandatory")
_FabTargetAliasName_Type = DisplayString
_FabTargetAliasName_Object = MibTableColumn
fabTargetAliasName = _FabTargetAliasName_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2, 1, 6),
    _FabTargetAliasName_Type()
)
fabTargetAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabTargetAliasName.setStatus("mandatory")


class _FabTargetType_Type(Integer32):
    """Custom type fabTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disk", 1),
          ("other", 2))
    )


_FabTargetType_Type.__name__ = "Integer32"
_FabTargetType_Object = MibTableColumn
fabTargetType = _FabTargetType_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2, 1, 7),
    _FabTargetType_Type()
)
fabTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabTargetType.setStatus("mandatory")
_FabTargetNumOfLuns_Type = U16Bits
_FabTargetNumOfLuns_Object = MibTableColumn
fabTargetNumOfLuns = _FabTargetNumOfLuns_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 2, 1, 8),
    _FabTargetNumOfLuns_Type()
)
fabTargetNumOfLuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabTargetNumOfLuns.setStatus("mandatory")
_FabLunTable_Object = MibTable
fabLunTable = _FabLunTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3)
)
if mibBuilder.loadTexts:
    fabLunTable.setStatus("mandatory")
_FabLunEntry_Object = MibTableRow
fabLunEntry = _FabLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3, 1)
)
fabLunEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
    (0, "NETSERVER-MIB", "fabLunIndex"),
)
if mibBuilder.loadTexts:
    fabLunEntry.setStatus("mandatory")
_FabLunIndex_Type = Integer32
_FabLunIndex_Object = MibTableColumn
fabLunIndex = _FabLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3, 1, 1),
    _FabLunIndex_Type()
)
fabLunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunIndex.setStatus("mandatory")
_FabLunNumber_Type = U16Bits
_FabLunNumber_Object = MibTableColumn
fabLunNumber = _FabLunNumber_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3, 1, 2),
    _FabLunNumber_Type()
)
fabLunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunNumber.setStatus("mandatory")
_FabLunAdptNumber_Type = U08Bits
_FabLunAdptNumber_Object = MibTableColumn
fabLunAdptNumber = _FabLunAdptNumber_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3, 1, 3),
    _FabLunAdptNumber_Type()
)
fabLunAdptNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunAdptNumber.setStatus("mandatory")
_FabLunTarNumber_Type = U16Bits
_FabLunTarNumber_Object = MibTableColumn
fabLunTarNumber = _FabLunTarNumber_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3, 1, 4),
    _FabLunTarNumber_Type()
)
fabLunTarNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunTarNumber.setStatus("mandatory")
_FabLunWWN_Type = DisplayString
_FabLunWWN_Object = MibTableColumn
fabLunWWN = _FabLunWWN_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3, 1, 5),
    _FabLunWWN_Type()
)
fabLunWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunWWN.setStatus("mandatory")
_FabLunType_Type = U08Bits
_FabLunType_Object = MibTableColumn
fabLunType = _FabLunType_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3, 1, 6),
    _FabLunType_Type()
)
fabLunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunType.setStatus("mandatory")
_FabLunSize_Type = Integer32
_FabLunSize_Object = MibTableColumn
fabLunSize = _FabLunSize_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3, 1, 7),
    _FabLunSize_Type()
)
fabLunSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunSize.setStatus("mandatory")


class _FabLunMap_Type(Integer32):
    """Custom type fabLunMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mapped", 1),
          ("unmapped", 0))
    )


_FabLunMap_Type.__name__ = "Integer32"
_FabLunMap_Object = MibTableColumn
fabLunMap = _FabLunMap_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 3, 1, 8),
    _FabLunMap_Type()
)
fabLunMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunMap.setStatus("mandatory")
_FabLunMapTable_Object = MibTable
fabLunMapTable = _FabLunMapTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 4)
)
if mibBuilder.loadTexts:
    fabLunMapTable.setStatus("mandatory")
_FabLunMapEntry_Object = MibTableRow
fabLunMapEntry = _FabLunMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 4, 1)
)
fabLunMapEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
    (0, "NETSERVER-MIB", "fabLunMapIndex"),
)
if mibBuilder.loadTexts:
    fabLunMapEntry.setStatus("mandatory")
_FabLunMapIndex_Type = Integer32
_FabLunMapIndex_Object = MibTableColumn
fabLunMapIndex = _FabLunMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 4, 1, 1),
    _FabLunMapIndex_Type()
)
fabLunMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunMapIndex.setStatus("mandatory")
_FabLunMNumber_Type = U16Bits
_FabLunMNumber_Object = MibTableColumn
fabLunMNumber = _FabLunMNumber_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 4, 1, 2),
    _FabLunMNumber_Type()
)
fabLunMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunMNumber.setStatus("mandatory")
_FabLunAlias_Type = DisplayString
_FabLunAlias_Object = MibTableColumn
fabLunAlias = _FabLunAlias_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 4, 1, 3),
    _FabLunAlias_Type()
)
fabLunAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunAlias.setStatus("mandatory")
_FabLunMapWWN_Type = DisplayString
_FabLunMapWWN_Object = MibTableColumn
fabLunMapWWN = _FabLunMapWWN_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 4, 1, 4),
    _FabLunMapWWN_Type()
)
fabLunMapWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunMapWWN.setStatus("mandatory")


class _FabLunLabel_Type(Integer32):
    """Custom type fabLunLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("labelled", 1),
          ("labelledactive", 2),
          ("unlabelled", 0))
    )


_FabLunLabel_Type.__name__ = "Integer32"
_FabLunLabel_Object = MibTableColumn
fabLunLabel = _FabLunLabel_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 4, 1, 5),
    _FabLunLabel_Type()
)
fabLunLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabLunLabel.setStatus("mandatory")
_FabRaid_ObjectIdentity = ObjectIdentity
fabRaid = _FabRaid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5)
)
_FabLogDevTable_Object = MibTable
fabLogDevTable = _FabLogDevTable_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1)
)
if mibBuilder.loadTexts:
    fabLogDevTable.setStatus("mandatory")
_FabLogDevEntry_Object = MibTableRow
fabLogDevEntry = _FabLogDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1)
)
fabLogDevEntry.setIndexNames(
    (0, "NETSERVER-MIB", "fspIndex"),
    (0, "NETSERVER-MIB", "ldIndex"),
)
if mibBuilder.loadTexts:
    fabLogDevEntry.setStatus("mandatory")
_LdIndex_Type = Integer32
_LdIndex_Object = MibTableColumn
ldIndex = _LdIndex_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1, 1),
    _LdIndex_Type()
)
ldIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldIndex.setStatus("mandatory")
_LdSectorReads_Type = Integer32
_LdSectorReads_Object = MibTableColumn
ldSectorReads = _LdSectorReads_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1, 2),
    _LdSectorReads_Type()
)
ldSectorReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldSectorReads.setStatus("mandatory")
_LdWBufReads_Type = Integer32
_LdWBufReads_Object = MibTableColumn
ldWBufReads = _LdWBufReads_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1, 3),
    _LdWBufReads_Type()
)
ldWBufReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldWBufReads.setStatus("mandatory")
_LdSectorWrites_Type = Integer32
_LdSectorWrites_Object = MibTableColumn
ldSectorWrites = _LdSectorWrites_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1, 4),
    _LdSectorWrites_Type()
)
ldSectorWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldSectorWrites.setStatus("mandatory")
_LdReadIO_Type = Integer32
_LdReadIO_Object = MibTableColumn
ldReadIO = _LdReadIO_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1, 5),
    _LdReadIO_Type()
)
ldReadIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldReadIO.setStatus("mandatory")
_LdWriteIO_Type = Integer32
_LdWriteIO_Object = MibTableColumn
ldWriteIO = _LdWriteIO_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1, 6),
    _LdWriteIO_Type()
)
ldWriteIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldWriteIO.setStatus("mandatory")
_LdMediaErrors_Type = Integer32
_LdMediaErrors_Object = MibTableColumn
ldMediaErrors = _LdMediaErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1, 7),
    _LdMediaErrors_Type()
)
ldMediaErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldMediaErrors.setStatus("mandatory")
_LdDriveErrors_Type = Integer32
_LdDriveErrors_Object = MibTableColumn
ldDriveErrors = _LdDriveErrors_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1, 8),
    _LdDriveErrors_Type()
)
ldDriveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldDriveErrors.setStatus("mandatory")
_LdTotalTime_Type = Integer32
_LdTotalTime_Object = MibTableColumn
ldTotalTime = _LdTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 3, 4, 5, 1, 1, 9),
    _LdTotalTime_Type()
)
ldTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldTotalTime.setStatus("mandatory")
_AxTrapData_ObjectIdentity = ObjectIdentity
axTrapData = _AxTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 4)
)
_TrapFSFull_ObjectIdentity = ObjectIdentity
trapFSFull = _TrapFSFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 1)
)
_TrapFSFullMsg_Type = DisplayString
_TrapFSFullMsg_Object = MibScalar
trapFSFullMsg = _TrapFSFullMsg_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 1, 1),
    _TrapFSFullMsg_Type()
)
trapFSFullMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFSFullMsg.setStatus("mandatory")
_TrapFSFullTimeStamp_Type = TimeTicks
_TrapFSFullTimeStamp_Object = MibScalar
trapFSFullTimeStamp = _TrapFSFullTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 1, 2),
    _TrapFSFullTimeStamp_Type()
)
trapFSFullTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFSFullTimeStamp.setStatus("mandatory")
_TrapFSDegradation_ObjectIdentity = ObjectIdentity
trapFSDegradation = _TrapFSDegradation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 2)
)
_TrapFSDegradationMsg_Type = DisplayString
_TrapFSDegradationMsg_Object = MibScalar
trapFSDegradationMsg = _TrapFSDegradationMsg_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 2, 1),
    _TrapFSDegradationMsg_Type()
)
trapFSDegradationMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFSDegradationMsg.setStatus("mandatory")
_TrapFSDegradationTimeStamp_Type = TimeTicks
_TrapFSDegradationTimeStamp_Object = MibScalar
trapFSDegradationTimeStamp = _TrapFSDegradationTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 2, 2),
    _TrapFSDegradationTimeStamp_Type()
)
trapFSDegradationTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFSDegradationTimeStamp.setStatus("mandatory")
_TrapDiskUpdation_ObjectIdentity = ObjectIdentity
trapDiskUpdation = _TrapDiskUpdation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 3)
)
_TrapDiskMsg_Type = DisplayString
_TrapDiskMsg_Object = MibScalar
trapDiskMsg = _TrapDiskMsg_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 3, 1),
    _TrapDiskMsg_Type()
)
trapDiskMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDiskMsg.setStatus("mandatory")
_TrapDiskTimeStamp_Type = TimeTicks
_TrapDiskTimeStamp_Object = MibScalar
trapDiskTimeStamp = _TrapDiskTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 3, 2),
    _TrapDiskTimeStamp_Type()
)
trapDiskTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDiskTimeStamp.setStatus("mandatory")
_TrapFCAdptLinkFailure_ObjectIdentity = ObjectIdentity
trapFCAdptLinkFailure = _TrapFCAdptLinkFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 4)
)
_TrapFCAdptLinkFailureMsg_Type = DisplayString
_TrapFCAdptLinkFailureMsg_Object = MibScalar
trapFCAdptLinkFailureMsg = _TrapFCAdptLinkFailureMsg_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 4, 1),
    _TrapFCAdptLinkFailureMsg_Type()
)
trapFCAdptLinkFailureMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFCAdptLinkFailureMsg.setStatus("mandatory")
_TrapFCAdptLinkFailureTimeStamp_Type = TimeTicks
_TrapFCAdptLinkFailureTimeStamp_Object = MibScalar
trapFCAdptLinkFailureTimeStamp = _TrapFCAdptLinkFailureTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 4, 2),
    _TrapFCAdptLinkFailureTimeStamp_Type()
)
trapFCAdptLinkFailureTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFCAdptLinkFailureTimeStamp.setStatus("mandatory")
_TrapFCAdptLinkUp_ObjectIdentity = ObjectIdentity
trapFCAdptLinkUp = _TrapFCAdptLinkUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 5)
)
_TrapFCAdptLinkUpMsg_Type = DisplayString
_TrapFCAdptLinkUpMsg_Object = MibScalar
trapFCAdptLinkUpMsg = _TrapFCAdptLinkUpMsg_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 5, 1),
    _TrapFCAdptLinkUpMsg_Type()
)
trapFCAdptLinkUpMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFCAdptLinkUpMsg.setStatus("mandatory")
_TrapFCAdptLinkUpTimeStamp_Type = TimeTicks
_TrapFCAdptLinkUpTimeStamp_Object = MibScalar
trapFCAdptLinkUpTimeStamp = _TrapFCAdptLinkUpTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 5, 2),
    _TrapFCAdptLinkUpTimeStamp_Type()
)
trapFCAdptLinkUpTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFCAdptLinkUpTimeStamp.setStatus("mandatory")
_TrapFCLossOfLinkFailure_ObjectIdentity = ObjectIdentity
trapFCLossOfLinkFailure = _TrapFCLossOfLinkFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 6)
)
_TrapFCLossOfLinkFailureMsg_Type = DisplayString
_TrapFCLossOfLinkFailureMsg_Object = MibScalar
trapFCLossOfLinkFailureMsg = _TrapFCLossOfLinkFailureMsg_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 6, 1),
    _TrapFCLossOfLinkFailureMsg_Type()
)
trapFCLossOfLinkFailureMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFCLossOfLinkFailureMsg.setStatus("mandatory")
_TrapFCLossOfLinkFailureTimeStamp_Type = TimeTicks
_TrapFCLossOfLinkFailureTimeStamp_Object = MibScalar
trapFCLossOfLinkFailureTimeStamp = _TrapFCLossOfLinkFailureTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 6, 2),
    _TrapFCLossOfLinkFailureTimeStamp_Type()
)
trapFCLossOfLinkFailureTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFCLossOfLinkFailureTimeStamp.setStatus("mandatory")
_TrapLunDisappear_ObjectIdentity = ObjectIdentity
trapLunDisappear = _TrapLunDisappear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 7)
)
_TrapLunDisappearMsg_Type = DisplayString
_TrapLunDisappearMsg_Object = MibScalar
trapLunDisappearMsg = _TrapLunDisappearMsg_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 7, 1),
    _TrapLunDisappearMsg_Type()
)
trapLunDisappearMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLunDisappearMsg.setStatus("mandatory")
_TrapLunDisappearTimeStamp_Type = TimeTicks
_TrapLunDisappearTimeStamp_Object = MibScalar
trapLunDisappearTimeStamp = _TrapLunDisappearTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 7, 2),
    _TrapLunDisappearTimeStamp_Type()
)
trapLunDisappearTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLunDisappearTimeStamp.setStatus("mandatory")
_TrapLunSizeChange_ObjectIdentity = ObjectIdentity
trapLunSizeChange = _TrapLunSizeChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 8)
)
_TrapLunSizeChangeMsg_Type = DisplayString
_TrapLunSizeChangeMsg_Object = MibScalar
trapLunSizeChangeMsg = _TrapLunSizeChangeMsg_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 8, 1),
    _TrapLunSizeChangeMsg_Type()
)
trapLunSizeChangeMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLunSizeChangeMsg.setStatus("mandatory")
_TrapLunSizeChangeTimeStamp_Type = TimeTicks
_TrapLunSizeChangeTimeStamp_Object = MibScalar
trapLunSizeChangeTimeStamp = _TrapLunSizeChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 80, 3, 4, 8, 2),
    _TrapLunSizeChangeTimeStamp_Type()
)
trapLunSizeChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLunSizeChangeTimeStamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects

fileSystemFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 80, 0, 1)
)
fileSystemFullTrap.setObjects(
      *(("NETSERVER-MIB", "trapFSFullMsg"),
        ("NETSERVER-MIB", "trapFSFullTimeStamp"))
)
if mibBuilder.loadTexts:
    fileSystemFullTrap.setStatus(
        ""
    )

fileSystemDegradationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 80, 0, 2)
)
fileSystemDegradationTrap.setObjects(
      *(("NETSERVER-MIB", "trapFSDegradationMsg"),
        ("NETSERVER-MIB", "trapFSDegradationTimeStamp"))
)
if mibBuilder.loadTexts:
    fileSystemDegradationTrap.setStatus(
        ""
    )

diskStackUpdationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 80, 0, 3)
)
diskStackUpdationTrap.setObjects(
      *(("NETSERVER-MIB", "trapDiskMsg"),
        ("NETSERVER-MIB", "trapDiskTimeStamp"))
)
if mibBuilder.loadTexts:
    diskStackUpdationTrap.setStatus(
        ""
    )

fcLinkFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 80, 0, 4)
)
fcLinkFailureTrap.setObjects(
      *(("NETSERVER-MIB", "trapFCAdptLinkFailureMsg"),
        ("NETSERVER-MIB", "trapFCAdptLinkFailureTimeStamp"))
)
if mibBuilder.loadTexts:
    fcLinkFailureTrap.setStatus(
        ""
    )

fcLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 80, 0, 5)
)
fcLinkUpTrap.setObjects(
      *(("NETSERVER-MIB", "trapFCAdptLinkUpMsg"),
        ("NETSERVER-MIB", "trapFCAdptLinkUpTimeStamp"))
)
if mibBuilder.loadTexts:
    fcLinkUpTrap.setStatus(
        ""
    )

fcCompleteLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 80, 0, 6)
)
fcCompleteLossTrap.setObjects(
      *(("NETSERVER-MIB", "trapFCLossOfLinkFailureMsg"),
        ("NETSERVER-MIB", "trapFCLossOfLinkFailureTimeStamp"))
)
if mibBuilder.loadTexts:
    fcCompleteLossTrap.setStatus(
        ""
    )

lunDisappearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 80, 0, 7)
)
lunDisappearTrap.setObjects(
      *(("NETSERVER-MIB", "trapLunDisappearMsg"),
        ("NETSERVER-MIB", "trapLunDisappearTimeStamp"))
)
if mibBuilder.loadTexts:
    lunDisappearTrap.setStatus(
        ""
    )

lunSizeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 80, 0, 8)
)
lunSizeChangeTrap.setObjects(
      *(("NETSERVER-MIB", "trapLunSizeChangeMsg"),
        ("NETSERVER-MIB", "trapLunSizeChangeTimeStamp"))
)
if mibBuilder.loadTexts:
    lunSizeChangeTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSERVER-MIB",
    **{"RaidLevel": RaidLevel,
       "RebuildFlag": RebuildFlag,
       "BusType": BusType,
       "ControllerType": ControllerType,
       "VendorName": VendorName,
       "U08Bits": U08Bits,
       "U16Bits": U16Bits,
       "Boolean": Boolean,
       "KBytes": KBytes,
       "ProductID": ProductID,
       "DateAndTime": DateAndTime,
       "InternationalDisplayString": InternationalDisplayString,
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
       "auspex": auspex,
       "fileSystemFullTrap": fileSystemFullTrap,
       "fileSystemDegradationTrap": fileSystemDegradationTrap,
       "diskStackUpdationTrap": diskStackUpdationTrap,
       "fcLinkFailureTrap": fcLinkFailureTrap,
       "fcLinkUpTrap": fcLinkUpTrap,
       "fcCompleteLossTrap": fcCompleteLossTrap,
       "lunDisappearTrap": lunDisappearTrap,
       "lunSizeChangeTrap": lunSizeChangeTrap,
       "netServer": netServer,
       "axProductInfo": axProductInfo,
       "axProductName": axProductName,
       "axSWVersion": axSWVersion,
       "axNumNPFSP": axNumNPFSP,
       "axNP": axNP,
       "npTable": npTable,
       "npEntry": npEntry,
       "npIndex": npIndex,
       "npBusyCount": npBusyCount,
       "npIdleCount": npIdleCount,
       "npIfTable": npIfTable,
       "npIfEntry": npIfEntry,
       "npIfIndex": npIfIndex,
       "npIfifIndex": npIfifIndex,
       "npIfType": npIfType,
       "npIfSpeed": npIfSpeed,
       "npIfInOctets": npIfInOctets,
       "npIfInUcastPkts": npIfInUcastPkts,
       "npIfInNUcastPkts": npIfInNUcastPkts,
       "npIfInDiscards": npIfInDiscards,
       "npIfInErrors": npIfInErrors,
       "npIfInUnknownProto": npIfInUnknownProto,
       "npIfOutOctets": npIfOutOctets,
       "npIfOutUcastPkts": npIfOutUcastPkts,
       "npIfOutNUcastPkts": npIfOutNUcastPkts,
       "npIfOutDiscards": npIfOutDiscards,
       "npIfOutErrors": npIfOutErrors,
       "npIfOutCollisions": npIfOutCollisions,
       "npIfOutQLen": npIfOutQLen,
       "npIfAdminStatus": npIfAdminStatus,
       "npIfOperStatus": npIfOperStatus,
       "npProtocols": npProtocols,
       "npIPTable": npIPTable,
       "npIPEntry": npIPEntry,
       "npIPForwarding": npIPForwarding,
       "npIPDefaultTTL": npIPDefaultTTL,
       "npIPInReceives": npIPInReceives,
       "npIPInHdrErrors": npIPInHdrErrors,
       "npIPInAddrErrors": npIPInAddrErrors,
       "npIPForwDatagrams": npIPForwDatagrams,
       "npIPInUnknownProtos": npIPInUnknownProtos,
       "npIPInDiscards": npIPInDiscards,
       "npIPInDelivers": npIPInDelivers,
       "npIPOutRequests": npIPOutRequests,
       "npIPOutDiscards": npIPOutDiscards,
       "npIPOutNoRoutes": npIPOutNoRoutes,
       "npIPReasmTimeout": npIPReasmTimeout,
       "npIPReasmReqds": npIPReasmReqds,
       "npIPReasmOKs": npIPReasmOKs,
       "npIPReasmFails": npIPReasmFails,
       "npIPFragOKs": npIPFragOKs,
       "npIPFragFails": npIPFragFails,
       "npIPFragCreates": npIPFragCreates,
       "npIPRoutingDiscards": npIPRoutingDiscards,
       "npICMPTable": npICMPTable,
       "npICMPEntry": npICMPEntry,
       "npICMPInMsgs": npICMPInMsgs,
       "npICMPInErrors": npICMPInErrors,
       "npICMPInDestUnreachs": npICMPInDestUnreachs,
       "npICMPInTimeExcds": npICMPInTimeExcds,
       "npICMPInParmProbs": npICMPInParmProbs,
       "npICMPInSrcQuenchs": npICMPInSrcQuenchs,
       "npICMPInRedirects": npICMPInRedirects,
       "npICMPInEchos": npICMPInEchos,
       "npICMPInEchoReps": npICMPInEchoReps,
       "npICMPInTimestamps": npICMPInTimestamps,
       "npICMPInTimestampReps": npICMPInTimestampReps,
       "npICMPInAddrMasks": npICMPInAddrMasks,
       "npICMPInAddrMaskReps": npICMPInAddrMaskReps,
       "npICMPOutMsgs": npICMPOutMsgs,
       "npICMPOutErrors": npICMPOutErrors,
       "npICMPOutDestUnreachs": npICMPOutDestUnreachs,
       "npICMPOutTimeExcds": npICMPOutTimeExcds,
       "npICMPOutParmProbs": npICMPOutParmProbs,
       "npICMPOutSrcQuenchs": npICMPOutSrcQuenchs,
       "npICMPOutRedirects": npICMPOutRedirects,
       "npICMPOutEchos": npICMPOutEchos,
       "npICMPOutEchoReps": npICMPOutEchoReps,
       "npICMPOutTimestamps": npICMPOutTimestamps,
       "npICMPOutTimestampReps": npICMPOutTimestampReps,
       "npICMPOutAddrMasks": npICMPOutAddrMasks,
       "npICMPOutAddrMaskReps": npICMPOutAddrMaskReps,
       "npTCPTable": npTCPTable,
       "npTCPEntry": npTCPEntry,
       "npTCPRtoAlgorithm": npTCPRtoAlgorithm,
       "npTCPRtoMin": npTCPRtoMin,
       "npTCPRtoMax": npTCPRtoMax,
       "npTCPMaxConn": npTCPMaxConn,
       "npTCPActiveOpens": npTCPActiveOpens,
       "npTCPPassiveOpens": npTCPPassiveOpens,
       "npTCPAttemptFails": npTCPAttemptFails,
       "npTCPEstabResets": npTCPEstabResets,
       "npTCPCurrEstab": npTCPCurrEstab,
       "npTCPInSegs": npTCPInSegs,
       "npTCPOutSegs": npTCPOutSegs,
       "npTCPRetransSegs": npTCPRetransSegs,
       "npTCPInErrs": npTCPInErrs,
       "npTCPOutRsts": npTCPOutRsts,
       "npUDPTable": npUDPTable,
       "npUDPEntry": npUDPEntry,
       "npUDPInDatagrams": npUDPInDatagrams,
       "npUDPNoPorts": npUDPNoPorts,
       "npUDPInErrors": npUDPInErrors,
       "npUDPOutDatagrams": npUDPOutDatagrams,
       "npNFSTable": npNFSTable,
       "npNFSEntry": npNFSEntry,
       "npNFSDCounts": npNFSDCounts,
       "npNFSDNJobs": npNFSDNJobs,
       "npNFSDBusyCounts": npNFSDBusyCounts,
       "npSMBTable": npSMBTable,
       "npSMBEntry": npSMBEntry,
       "npSMBRcvd": npSMBRcvd,
       "npSMBBytesRcvd": npSMBBytesRcvd,
       "npSMBBytesSent": npSMBBytesSent,
       "npSMBReads": npSMBReads,
       "npSMBWrites": npSMBWrites,
       "npSMBOpens": npSMBOpens,
       "npSMBCloses": npSMBCloses,
       "npSMBErrors": npSMBErrors,
       "npSMBLocksHeld": npSMBLocksHeld,
       "axFSP": axFSP,
       "fspTable": fspTable,
       "fspEntry": fspEntry,
       "fspIndex": fspIndex,
       "fspBusyCount": fspBusyCount,
       "fspIdleCount": fspIdleCount,
       "axFP": axFP,
       "fpLFSTable": fpLFSTable,
       "fpLFSEntry": fpLFSEntry,
       "fpLFSVersion": fpLFSVersion,
       "fpLFSMounts": fpLFSMounts,
       "fpLFSUMounts": fpLFSUMounts,
       "fpLFSReads": fpLFSReads,
       "fpLFSWrites": fpLFSWrites,
       "fpLFSReaddirs": fpLFSReaddirs,
       "fpLFSReadlinks": fpLFSReadlinks,
       "fpLFSMkdirs": fpLFSMkdirs,
       "fpLFSMknods": fpLFSMknods,
       "fpLFSReaddirPluses": fpLFSReaddirPluses,
       "fpLFSFsstats": fpLFSFsstats,
       "fpLFSNull": fpLFSNull,
       "fpLFSFsinfo": fpLFSFsinfo,
       "fpLFSGetattrs": fpLFSGetattrs,
       "fpLFSSetattrs": fpLFSSetattrs,
       "fpLFSLookups": fpLFSLookups,
       "fpLFSCreates": fpLFSCreates,
       "fpLFSRemoves": fpLFSRemoves,
       "fpLFSRenames": fpLFSRenames,
       "fpLFSLinks": fpLFSLinks,
       "fpLFSSymlinks": fpLFSSymlinks,
       "fpLFSRmdirs": fpLFSRmdirs,
       "fpLFSCkpntons": fpLFSCkpntons,
       "fpLFSCkpntoffs": fpLFSCkpntoffs,
       "fpLFSClears": fpLFSClears,
       "fpLFSIsolateFs": fpLFSIsolateFs,
       "fpLFSReleaseFs": fpLFSReleaseFs,
       "fpLFSIsolationStates": fpLFSIsolationStates,
       "fpLFSDiagnostics": fpLFSDiagnostics,
       "fpLFSPurges": fpLFSPurges,
       "fpFileSystemTable": fpFileSystemTable,
       "fpFSEntry": fpFSEntry,
       "fpFSIndex": fpFSIndex,
       "fpHrFSIndex": fpHrFSIndex,
       "fpHTFS": fpHTFS,
       "fpDNLCTStatTable": fpDNLCTStatTable,
       "fpDNLCSEntry": fpDNLCSEntry,
       "fpDNLCHit": fpDNLCHit,
       "fpDNLCMiss": fpDNLCMiss,
       "fpDNLCEnter": fpDNLCEnter,
       "fpDNLCConflict": fpDNLCConflict,
       "fpDNLCPurgevfsp": fpDNLCPurgevfsp,
       "fpDNLCPurgevp": fpDNLCPurgevp,
       "fpDNLCHashsz": fpDNLCHashsz,
       "fpPageStatTable": fpPageStatTable,
       "fpPageEntry": fpPageEntry,
       "fpPAGETotalmem": fpPAGETotalmem,
       "fpPAGEFreelistcnt": fpPAGEFreelistcnt,
       "fpPAGECachelistcnt": fpPAGECachelistcnt,
       "fpPAGEDirtyflistcnt": fpPAGEDirtyflistcnt,
       "fpPAGEDirtydlistcnt": fpPAGEDirtydlistcnt,
       "fpPAGECachehit": fpPAGECachehit,
       "fpPAGECachemiss": fpPAGECachemiss,
       "fpPAGEWritehit": fpPAGEWritehit,
       "fpPAGEWritemiss": fpPAGEWritemiss,
       "fpPAGEZcref": fpPAGEZcref,
       "fpPAGEZcbreak": fpPAGEZcbreak,
       "fpPAGEOutscan": fpPAGEOutscan,
       "fpPAGEOutputpage": fpPAGEOutputpage,
       "fpPAGEFsflushscan": fpPAGEFsflushscan,
       "fpPAGEFsflushputpage": fpPAGEFsflushputpage,
       "fpPAGEOutcnt": fpPAGEOutcnt,
       "fpBufferStatTable": fpBufferStatTable,
       "fpBufferEntry": fpBufferEntry,
       "fpBUFLreads": fpBUFLreads,
       "fpBUFBreads": fpBUFBreads,
       "fpBUFLwrites": fpBUFLwrites,
       "fpBUFBwrites": fpBUFBwrites,
       "fpBUFIOwaits": fpBUFIOwaits,
       "fpBUFResid": fpBUFResid,
       "fpBUFBufsize": fpBUFBufsize,
       "fpBUFBcount": fpBUFBcount,
       "fpInodeTable": fpInodeTable,
       "fpInodeEntry": fpInodeEntry,
       "fpINODEIgetcalls": fpINODEIgetcalls,
       "fpFoundinodes": fpFoundinodes,
       "fpTotalinodes": fpTotalinodes,
       "fpGoneinodes": fpGoneinodes,
       "fpFreeinodes": fpFreeinodes,
       "fpCacheinodes": fpCacheinodes,
       "fpSyncinodes": fpSyncinodes,
       "axSP": axSP,
       "spRaid": spRaid,
       "axFab": axFab,
       "fabAdptTable": fabAdptTable,
       "fabAdptEntry": fabAdptEntry,
       "fabIndex": fabIndex,
       "fabPCIBusNum": fabPCIBusNum,
       "fabSlotNum": fabSlotNum,
       "fabIntLine": fabIntLine,
       "fabIntPin": fabIntPin,
       "fabType": fabType,
       "fabVendorId": fabVendorId,
       "fabDeviceId": fabDeviceId,
       "fabRevisionId": fabRevisionId,
       "fabWWN": fabWWN,
       "fabNumOfTargets": fabNumOfTargets,
       "fabAdptNumber": fabAdptNumber,
       "fabTargetTable": fabTargetTable,
       "fabTargetEntry": fabTargetEntry,
       "fabTargetIndex": fabTargetIndex,
       "fabTargetAdapterNum": fabTargetAdapterNum,
       "fabTargetNumber": fabTargetNumber,
       "fabTargetWWN": fabTargetWWN,
       "fabTargetPortWWN": fabTargetPortWWN,
       "fabTargetAliasName": fabTargetAliasName,
       "fabTargetType": fabTargetType,
       "fabTargetNumOfLuns": fabTargetNumOfLuns,
       "fabLunTable": fabLunTable,
       "fabLunEntry": fabLunEntry,
       "fabLunIndex": fabLunIndex,
       "fabLunNumber": fabLunNumber,
       "fabLunAdptNumber": fabLunAdptNumber,
       "fabLunTarNumber": fabLunTarNumber,
       "fabLunWWN": fabLunWWN,
       "fabLunType": fabLunType,
       "fabLunSize": fabLunSize,
       "fabLunMap": fabLunMap,
       "fabLunMapTable": fabLunMapTable,
       "fabLunMapEntry": fabLunMapEntry,
       "fabLunMapIndex": fabLunMapIndex,
       "fabLunMNumber": fabLunMNumber,
       "fabLunAlias": fabLunAlias,
       "fabLunMapWWN": fabLunMapWWN,
       "fabLunLabel": fabLunLabel,
       "fabRaid": fabRaid,
       "fabLogDevTable": fabLogDevTable,
       "fabLogDevEntry": fabLogDevEntry,
       "ldIndex": ldIndex,
       "ldSectorReads": ldSectorReads,
       "ldWBufReads": ldWBufReads,
       "ldSectorWrites": ldSectorWrites,
       "ldReadIO": ldReadIO,
       "ldWriteIO": ldWriteIO,
       "ldMediaErrors": ldMediaErrors,
       "ldDriveErrors": ldDriveErrors,
       "ldTotalTime": ldTotalTime,
       "axTrapData": axTrapData,
       "trapFSFull": trapFSFull,
       "trapFSFullMsg": trapFSFullMsg,
       "trapFSFullTimeStamp": trapFSFullTimeStamp,
       "trapFSDegradation": trapFSDegradation,
       "trapFSDegradationMsg": trapFSDegradationMsg,
       "trapFSDegradationTimeStamp": trapFSDegradationTimeStamp,
       "trapDiskUpdation": trapDiskUpdation,
       "trapDiskMsg": trapDiskMsg,
       "trapDiskTimeStamp": trapDiskTimeStamp,
       "trapFCAdptLinkFailure": trapFCAdptLinkFailure,
       "trapFCAdptLinkFailureMsg": trapFCAdptLinkFailureMsg,
       "trapFCAdptLinkFailureTimeStamp": trapFCAdptLinkFailureTimeStamp,
       "trapFCAdptLinkUp": trapFCAdptLinkUp,
       "trapFCAdptLinkUpMsg": trapFCAdptLinkUpMsg,
       "trapFCAdptLinkUpTimeStamp": trapFCAdptLinkUpTimeStamp,
       "trapFCLossOfLinkFailure": trapFCLossOfLinkFailure,
       "trapFCLossOfLinkFailureMsg": trapFCLossOfLinkFailureMsg,
       "trapFCLossOfLinkFailureTimeStamp": trapFCLossOfLinkFailureTimeStamp,
       "trapLunDisappear": trapLunDisappear,
       "trapLunDisappearMsg": trapLunDisappearMsg,
       "trapLunDisappearTimeStamp": trapLunDisappearTimeStamp,
       "trapLunSizeChange": trapLunSizeChange,
       "trapLunSizeChangeMsg": trapLunSizeChangeMsg,
       "trapLunSizeChangeTimeStamp": trapLunSizeChangeTimeStamp}
)
