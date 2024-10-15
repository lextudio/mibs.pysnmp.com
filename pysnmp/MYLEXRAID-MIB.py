# SNMP MIB module (MYLEXRAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MYLEXRAID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:32 2024
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



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDate(OctetString):
    """Custom type DmiDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mylex_ObjectIdentity = ObjectIdentity
mylex = _Mylex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1608)
)
_DmtfStd_ObjectIdentity = ObjectIdentity
dmtfStd = _DmtfStd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1608, 1)
)
_DmtfComponents_ObjectIdentity = ObjectIdentity
dmtfComponents = _DmtfComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1)
)
_TControllerInformation_Object = MibTable
tControllerInformation = _TControllerInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tControllerInformation.setStatus("mandatory")
_EControllerInformation_Object = MibTableRow
eControllerInformation = _EControllerInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1)
)
eControllerInformation.setIndexNames(
    (0, "MYLEXRAID-MIB", "a2ControllerNumber"),
)
if mibBuilder.loadTexts:
    eControllerInformation.setStatus("mandatory")
_A2ControllerNumber_Type = DmiInteger
_A2ControllerNumber_Object = MibTableColumn
a2ControllerNumber = _A2ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 1),
    _A2ControllerNumber_Type()
)
a2ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ControllerNumber.setStatus("mandatory")


class _A2OperationalState_Type(Integer32):
    """Custom type a2OperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("vFunctional", 1),
          ("vNon-functional", 2),
          ("vNotPresent", 128))
    )


_A2OperationalState_Type.__name__ = "Integer32"
_A2OperationalState_Object = MibTableColumn
a2OperationalState = _A2OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 2),
    _A2OperationalState_Type()
)
a2OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2OperationalState.setStatus("mandatory")
_A2FirmwareRevision_Type = DmiDisplaystring
_A2FirmwareRevision_Object = MibTableColumn
a2FirmwareRevision = _A2FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 3),
    _A2FirmwareRevision_Type()
)
a2FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2FirmwareRevision.setStatus("mandatory")
_A2ConfiguredChannels_Type = DmiInteger
_A2ConfiguredChannels_Object = MibTableColumn
a2ConfiguredChannels = _A2ConfiguredChannels_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 4),
    _A2ConfiguredChannels_Type()
)
a2ConfiguredChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ConfiguredChannels.setStatus("mandatory")
_A2ActualChannels_Type = DmiInteger
_A2ActualChannels_Object = MibTableColumn
a2ActualChannels = _A2ActualChannels_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 5),
    _A2ActualChannels_Type()
)
a2ActualChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ActualChannels.setStatus("mandatory")
_A2MaximumLogicalDrives_Type = DmiInteger
_A2MaximumLogicalDrives_Object = MibTableColumn
a2MaximumLogicalDrives = _A2MaximumLogicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 6),
    _A2MaximumLogicalDrives_Type()
)
a2MaximumLogicalDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumLogicalDrives.setStatus("mandatory")
_A2MaximumTargetsPerChannel_Type = DmiInteger
_A2MaximumTargetsPerChannel_Object = MibTableColumn
a2MaximumTargetsPerChannel = _A2MaximumTargetsPerChannel_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 7),
    _A2MaximumTargetsPerChannel_Type()
)
a2MaximumTargetsPerChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumTargetsPerChannel.setStatus("mandatory")
_A2MaximumTaggedRequests_Type = DmiInteger
_A2MaximumTaggedRequests_Object = MibTableColumn
a2MaximumTaggedRequests = _A2MaximumTaggedRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 8),
    _A2MaximumTaggedRequests_Type()
)
a2MaximumTaggedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumTaggedRequests.setStatus("mandatory")
_A2MaximumDataTransferSizePerIoRequestInK_Type = DmiInteger
_A2MaximumDataTransferSizePerIoRequestInK_Object = MibTableColumn
a2MaximumDataTransferSizePerIoRequestInK = _A2MaximumDataTransferSizePerIoRequestInK_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 9),
    _A2MaximumDataTransferSizePerIoRequestInK_Type()
)
a2MaximumDataTransferSizePerIoRequestInK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumDataTransferSizePerIoRequestInK.setStatus("mandatory")
_A2MaximumConcurrentCommands_Type = DmiInteger
_A2MaximumConcurrentCommands_Object = MibTableColumn
a2MaximumConcurrentCommands = _A2MaximumConcurrentCommands_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 10),
    _A2MaximumConcurrentCommands_Type()
)
a2MaximumConcurrentCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumConcurrentCommands.setStatus("mandatory")
_A2RebuildRate_Type = DmiInteger
_A2RebuildRate_Object = MibTableColumn
a2RebuildRate = _A2RebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 11),
    _A2RebuildRate_Type()
)
a2RebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2RebuildRate.setStatus("mandatory")
_A2LogicalSectorSizeInBytes_Type = DmiInteger
_A2LogicalSectorSizeInBytes_Object = MibTableColumn
a2LogicalSectorSizeInBytes = _A2LogicalSectorSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 12),
    _A2LogicalSectorSizeInBytes_Type()
)
a2LogicalSectorSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2LogicalSectorSizeInBytes.setStatus("mandatory")
_A2PhysicalSectorSizeInBytes_Type = DmiInteger
_A2PhysicalSectorSizeInBytes_Object = MibTableColumn
a2PhysicalSectorSizeInBytes = _A2PhysicalSectorSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 13),
    _A2PhysicalSectorSizeInBytes_Type()
)
a2PhysicalSectorSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2PhysicalSectorSizeInBytes.setStatus("mandatory")
_A2CacheLineSizeInBytes_Type = DmiInteger
_A2CacheLineSizeInBytes_Object = MibTableColumn
a2CacheLineSizeInBytes = _A2CacheLineSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 14),
    _A2CacheLineSizeInBytes_Type()
)
a2CacheLineSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2CacheLineSizeInBytes.setStatus("mandatory")
_A2CacheSizeInMb_Type = DmiInteger
_A2CacheSizeInMb_Object = MibTableColumn
a2CacheSizeInMb = _A2CacheSizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 15),
    _A2CacheSizeInMb_Type()
)
a2CacheSizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2CacheSizeInMb.setStatus("mandatory")


class _A2CacheMemoryType_Type(Integer32):
    """Custom type a2CacheMemoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              65,
              66,
              67,
              68,
              129,
              130,
              131,
              132,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vDram", 1),
          ("vDram-ecc", 129),
          ("vDram-parity", 65),
          ("vEdo", 3),
          ("vEdo-ecc", 131),
          ("vEdo-parity", 67),
          ("vEdram", 2),
          ("vEdram-ecc", 130),
          ("vEdram-parity", 66),
          ("vSdram", 4),
          ("vSdram-ecc", 132),
          ("vSdram-parity", 68),
          ("vUnknown", 255))
    )


_A2CacheMemoryType_Type.__name__ = "Integer32"
_A2CacheMemoryType_Object = MibTableColumn
a2CacheMemoryType = _A2CacheMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 16),
    _A2CacheMemoryType_Type()
)
a2CacheMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2CacheMemoryType.setStatus("mandatory")
_A2EpromSizeInKb_Type = DmiInteger
_A2EpromSizeInKb_Object = MibTableColumn
a2EpromSizeInKb = _A2EpromSizeInKb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 17),
    _A2EpromSizeInKb_Type()
)
a2EpromSizeInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2EpromSizeInKb.setStatus("mandatory")


class _A2BusType_Type(Integer32):
    """Custom type a2BusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vEisa", 1),
          ("vIsa", 5),
          ("vMca", 2),
          ("vPci", 3),
          ("vUnknown", 255),
          ("vVesa", 4))
    )


_A2BusType_Type.__name__ = "Integer32"
_A2BusType_Object = MibTableColumn
a2BusType = _A2BusType_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 18),
    _A2BusType_Type()
)
a2BusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2BusType.setStatus("mandatory")


class _A2ControllerClass_Type(Integer32):
    """Custom type a2ControllerClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              128,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vHba", 128),
          ("vRaid", 1),
          ("vUnknown", 255))
    )


_A2ControllerClass_Type.__name__ = "Integer32"
_A2ControllerClass_Object = MibTableColumn
a2ControllerClass = _A2ControllerClass_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 19),
    _A2ControllerClass_Type()
)
a2ControllerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ControllerClass.setStatus("mandatory")


class _A2ControllerModel_Type(Integer32):
    """Custom type a2ControllerModel based on Integer32"""
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
              27,
              28,
              29,
              30,
              31,
              32,
              35,
              36,
              37,
              38,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              109,
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
              195,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vAcceleraid160", 32),
          ("vAcceleraid170", 31),
          ("vAcceleraid352", 30),
          ("vAcceleraid400", 38),
          ("vAcceleraid500", 37),
          ("vBt-440", 129),
          ("vBt-440c", 130),
          ("vBt-445", 131),
          ("vBt-445c", 132),
          ("vBt-445s", 134),
          ("vBt-44xc", 133),
          ("vBt-540", 160),
          ("vBt-540c", 161),
          ("vBt-542", 162),
          ("vBt-542b", 163),
          ("vBt-542c", 164),
          ("vBt-542d", 165),
          ("vBt-545", 166),
          ("vBt-545c", 167),
          ("vBt-545s", 168),
          ("vBt-54xc", 169),
          ("vBt-640", 136),
          ("vBt-640a", 137),
          ("vBt-646", 138),
          ("vBt-646d", 139),
          ("vBt-646s", 140),
          ("vBt-742", 144),
          ("vBt-742a", 145),
          ("vBt-747", 146),
          ("vBt-747c", 155),
          ("vBt-747d", 147),
          ("vBt-747s", 148),
          ("vBt-74xc", 149),
          ("vBt-757", 150),
          ("vBt-757c", 156),
          ("vBt-757cd", 153),
          ("vBt-757d", 151),
          ("vBt-757s", 152),
          ("vBt-75xc", 154),
          ("vBt-946", 176),
          ("vBt-946c", 177),
          ("vBt-948", 178),
          ("vBt-948c", 179),
          ("vBt-956", 180),
          ("vBt-956c", 181),
          ("vBt-956cd", 185),
          ("vBt-958", 182),
          ("vBt-958c", 183),
          ("vBt-958cd", 186),
          ("vBt-958d", 184),
          ("vBt930", 192),
          ("vBt932", 193),
          ("vBt950", 194),
          ("vBt952", 195),
          ("vDac1164p", 26),
          ("vDac960e", 1),
          ("vDac960ff", 103),
          ("vDac960fl", 101),
          ("vDac960ll", 102),
          ("vDac960m", 8),
          ("vDac960mff", 106),
          ("vDac960mfl", 105),
          ("vDac960pd", 16),
          ("vDac960pdu", 18),
          ("vDac960pe", 19),
          ("vDac960pg", 20),
          ("vDac960pj", 21),
          ("vDac960pl", 17),
          ("vDac960pr", 23),
          ("vDac960prl", 24),
          ("vDac960pt", 25),
          ("vDac960ptl0", 22),
          ("vDac960ptl1", 27),
          ("vDac960s", 96),
          ("vDac960sf", 99),
          ("vDac960ss", 100),
          ("vDac960su", 97),
          ("vDac960sx", 98),
          ("vDacffx", 107),
          ("vDacffx2", 109),
          ("vExtremeraid2000", 28),
          ("vExtremeraid3000", 29),
          ("vExtremeraid4000", 35),
          ("vExtremeraid5000", 36),
          ("vFcarray", 104),
          ("vUnknown", 255))
    )


_A2ControllerModel_Type.__name__ = "Integer32"
_A2ControllerModel_Object = MibTableColumn
a2ControllerModel = _A2ControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 20),
    _A2ControllerModel_Type()
)
a2ControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ControllerModel.setStatus("mandatory")
_A2SystemBusNumber_Type = DmiInteger
_A2SystemBusNumber_Object = MibTableColumn
a2SystemBusNumber = _A2SystemBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 21),
    _A2SystemBusNumber_Type()
)
a2SystemBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2SystemBusNumber.setStatus("mandatory")
_A2SlotNumber_Type = DmiInteger
_A2SlotNumber_Object = MibTableColumn
a2SlotNumber = _A2SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 22),
    _A2SlotNumber_Type()
)
a2SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2SlotNumber.setStatus("mandatory")
_A2InterruptVectorNumber_Type = DmiInteger
_A2InterruptVectorNumber_Object = MibTableColumn
a2InterruptVectorNumber = _A2InterruptVectorNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 23),
    _A2InterruptVectorNumber_Type()
)
a2InterruptVectorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2InterruptVectorNumber.setStatus("mandatory")


class _A2InterruptMode_Type(Integer32):
    """Custom type a2InterruptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vEdge", 0),
          ("vLevel", 1),
          ("vUnknown", 255))
    )


_A2InterruptMode_Type.__name__ = "Integer32"
_A2InterruptMode_Object = MibTableColumn
a2InterruptMode = _A2InterruptMode_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 24),
    _A2InterruptMode_Type()
)
a2InterruptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2InterruptMode.setStatus("mandatory")
_A2NumberOfPhysicalDevices_Type = DmiInteger
_A2NumberOfPhysicalDevices_Object = MibTableColumn
a2NumberOfPhysicalDevices = _A2NumberOfPhysicalDevices_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 25),
    _A2NumberOfPhysicalDevices_Type()
)
a2NumberOfPhysicalDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2NumberOfPhysicalDevices.setStatus("mandatory")
_A2NumberOfPhysicalDevicesOffline_Type = DmiInteger
_A2NumberOfPhysicalDevicesOffline_Object = MibTableColumn
a2NumberOfPhysicalDevicesOffline = _A2NumberOfPhysicalDevicesOffline_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 26),
    _A2NumberOfPhysicalDevicesOffline_Type()
)
a2NumberOfPhysicalDevicesOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2NumberOfPhysicalDevicesOffline.setStatus("mandatory")
_A2NumberOfLogicalDevices_Type = DmiInteger
_A2NumberOfLogicalDevices_Object = MibTableColumn
a2NumberOfLogicalDevices = _A2NumberOfLogicalDevices_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 27),
    _A2NumberOfLogicalDevices_Type()
)
a2NumberOfLogicalDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2NumberOfLogicalDevices.setStatus("mandatory")
_A2NumberOfLogicalDevicesCritical_Type = DmiInteger
_A2NumberOfLogicalDevicesCritical_Object = MibTableColumn
a2NumberOfLogicalDevicesCritical = _A2NumberOfLogicalDevicesCritical_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 28),
    _A2NumberOfLogicalDevicesCritical_Type()
)
a2NumberOfLogicalDevicesCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2NumberOfLogicalDevicesCritical.setStatus("mandatory")
_A2NumberOfLogicalDevicesOffline_Type = DmiInteger
_A2NumberOfLogicalDevicesOffline_Object = MibTableColumn
a2NumberOfLogicalDevicesOffline = _A2NumberOfLogicalDevicesOffline_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 29),
    _A2NumberOfLogicalDevicesOffline_Type()
)
a2NumberOfLogicalDevicesOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2NumberOfLogicalDevicesOffline.setStatus("mandatory")


class _A2FaultManagementType_Type(Integer32):
    """Custom type a2FaultManagementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("vAemi", 1),
          ("vConner", 16),
          ("vNotPresent", 0),
          ("vOem1", 2),
          ("vOem2", 4),
          ("vOem3", 8),
          ("vSafte", 32),
          ("vSes", 64))
    )


_A2FaultManagementType_Type.__name__ = "Integer32"
_A2FaultManagementType_Object = MibTableColumn
a2FaultManagementType = _A2FaultManagementType_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 30),
    _A2FaultManagementType_Type()
)
a2FaultManagementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2FaultManagementType.setStatus("mandatory")
_A2ArrayInformation_Type = DmiDisplaystring
_A2ArrayInformation_Object = MibTableColumn
a2ArrayInformation = _A2ArrayInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 31),
    _A2ArrayInformation_Type()
)
a2ArrayInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ArrayInformation.setStatus("mandatory")
_A2LogicalDriveReadRequests_Type = DmiCounter
_A2LogicalDriveReadRequests_Object = MibTableColumn
a2LogicalDriveReadRequests = _A2LogicalDriveReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 32),
    _A2LogicalDriveReadRequests_Type()
)
a2LogicalDriveReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2LogicalDriveReadRequests.setStatus("mandatory")
_A2DataReadFromLogicalDrivesInMb_Type = DmiInteger
_A2DataReadFromLogicalDrivesInMb_Object = MibTableColumn
a2DataReadFromLogicalDrivesInMb = _A2DataReadFromLogicalDrivesInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 33),
    _A2DataReadFromLogicalDrivesInMb_Type()
)
a2DataReadFromLogicalDrivesInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2DataReadFromLogicalDrivesInMb.setStatus("mandatory")
_A2LogicalDriveWriteRequests_Type = DmiCounter
_A2LogicalDriveWriteRequests_Object = MibTableColumn
a2LogicalDriveWriteRequests = _A2LogicalDriveWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 34),
    _A2LogicalDriveWriteRequests_Type()
)
a2LogicalDriveWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2LogicalDriveWriteRequests.setStatus("mandatory")
_A2DataWrittenToLogicalDrivesInMb_Type = DmiInteger
_A2DataWrittenToLogicalDrivesInMb_Object = MibTableColumn
a2DataWrittenToLogicalDrivesInMb = _A2DataWrittenToLogicalDrivesInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 35),
    _A2DataWrittenToLogicalDrivesInMb_Type()
)
a2DataWrittenToLogicalDrivesInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2DataWrittenToLogicalDrivesInMb.setStatus("mandatory")
_A2LogicalDrivesReadCacheHitPercentage_Type = DmiInteger
_A2LogicalDrivesReadCacheHitPercentage_Object = MibTableColumn
a2LogicalDrivesReadCacheHitPercentage = _A2LogicalDrivesReadCacheHitPercentage_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 36),
    _A2LogicalDrivesReadCacheHitPercentage_Type()
)
a2LogicalDrivesReadCacheHitPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2LogicalDrivesReadCacheHitPercentage.setStatus("mandatory")
_A2PhysicalDriveReadRequests_Type = DmiCounter
_A2PhysicalDriveReadRequests_Object = MibTableColumn
a2PhysicalDriveReadRequests = _A2PhysicalDriveReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 37),
    _A2PhysicalDriveReadRequests_Type()
)
a2PhysicalDriveReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2PhysicalDriveReadRequests.setStatus("mandatory")
_A2DataReadFromPhysicalDrivesInMb_Type = DmiInteger
_A2DataReadFromPhysicalDrivesInMb_Object = MibTableColumn
a2DataReadFromPhysicalDrivesInMb = _A2DataReadFromPhysicalDrivesInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 38),
    _A2DataReadFromPhysicalDrivesInMb_Type()
)
a2DataReadFromPhysicalDrivesInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2DataReadFromPhysicalDrivesInMb.setStatus("mandatory")
_A2PhysicalDriveWriteRequests_Type = DmiCounter
_A2PhysicalDriveWriteRequests_Object = MibTableColumn
a2PhysicalDriveWriteRequests = _A2PhysicalDriveWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 39),
    _A2PhysicalDriveWriteRequests_Type()
)
a2PhysicalDriveWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2PhysicalDriveWriteRequests.setStatus("mandatory")
_A2DataWrittenToPhysicalDrivesInMb_Type = DmiInteger
_A2DataWrittenToPhysicalDrivesInMb_Object = MibTableColumn
a2DataWrittenToPhysicalDrivesInMb = _A2DataWrittenToPhysicalDrivesInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 40),
    _A2DataWrittenToPhysicalDrivesInMb_Type()
)
a2DataWrittenToPhysicalDrivesInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2DataWrittenToPhysicalDrivesInMb.setStatus("mandatory")


class _A2StorageworksCabinetStatusOnChannel0_Type(Integer32):
    """Custom type a2StorageworksCabinetStatusOnChannel0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vNotOk", 2),
          ("vNotPresent", 3),
          ("vOk", 1))
    )


_A2StorageworksCabinetStatusOnChannel0_Type.__name__ = "Integer32"
_A2StorageworksCabinetStatusOnChannel0_Object = MibTableColumn
a2StorageworksCabinetStatusOnChannel0 = _A2StorageworksCabinetStatusOnChannel0_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 41),
    _A2StorageworksCabinetStatusOnChannel0_Type()
)
a2StorageworksCabinetStatusOnChannel0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2StorageworksCabinetStatusOnChannel0.setStatus("mandatory")


class _A2StorageworksCabinetStatusOnChannel1_Type(Integer32):
    """Custom type a2StorageworksCabinetStatusOnChannel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vNotOk", 2),
          ("vNotPresent", 3),
          ("vOk", 1))
    )


_A2StorageworksCabinetStatusOnChannel1_Type.__name__ = "Integer32"
_A2StorageworksCabinetStatusOnChannel1_Object = MibTableColumn
a2StorageworksCabinetStatusOnChannel1 = _A2StorageworksCabinetStatusOnChannel1_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 42),
    _A2StorageworksCabinetStatusOnChannel1_Type()
)
a2StorageworksCabinetStatusOnChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2StorageworksCabinetStatusOnChannel1.setStatus("mandatory")


class _A2StorageworksCabinetStatusOnChannel2_Type(Integer32):
    """Custom type a2StorageworksCabinetStatusOnChannel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vNotOk", 2),
          ("vNotPresent", 3),
          ("vOk", 1))
    )


_A2StorageworksCabinetStatusOnChannel2_Type.__name__ = "Integer32"
_A2StorageworksCabinetStatusOnChannel2_Object = MibTableColumn
a2StorageworksCabinetStatusOnChannel2 = _A2StorageworksCabinetStatusOnChannel2_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 43),
    _A2StorageworksCabinetStatusOnChannel2_Type()
)
a2StorageworksCabinetStatusOnChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2StorageworksCabinetStatusOnChannel2.setStatus("mandatory")


class _A2BatteryBackupUnitStatus_Type(Integer32):
    """Custom type a2BatteryBackupUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vNotPresent", 0),
          ("vPresent", 1))
    )


_A2BatteryBackupUnitStatus_Type.__name__ = "Integer32"
_A2BatteryBackupUnitStatus_Object = MibTableColumn
a2BatteryBackupUnitStatus = _A2BatteryBackupUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 44),
    _A2BatteryBackupUnitStatus_Type()
)
a2BatteryBackupUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2BatteryBackupUnitStatus.setStatus("mandatory")
_A2PartnerControllerNumber_Type = DmiInteger
_A2PartnerControllerNumber_Object = MibTableColumn
a2PartnerControllerNumber = _A2PartnerControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 45),
    _A2PartnerControllerNumber_Type()
)
a2PartnerControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2PartnerControllerNumber.setStatus("mandatory")
_A2WwName_Type = DmiDisplaystring
_A2WwName_Object = MibTableColumn
a2WwName = _A2WwName_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 46),
    _A2WwName_Type()
)
a2WwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2WwName.setStatus("mandatory")
_A2HostControllerNumber_Type = DmiInteger
_A2HostControllerNumber_Object = MibTableColumn
a2HostControllerNumber = _A2HostControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 47),
    _A2HostControllerNumber_Type()
)
a2HostControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2HostControllerNumber.setStatus("mandatory")
_A2HostChannelNumber_Type = DmiInteger
_A2HostChannelNumber_Object = MibTableColumn
a2HostChannelNumber = _A2HostChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 48),
    _A2HostChannelNumber_Type()
)
a2HostChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2HostChannelNumber.setStatus("mandatory")
_A2HostTargetId_Type = DmiInteger
_A2HostTargetId_Object = MibTableColumn
a2HostTargetId = _A2HostTargetId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 2, 1, 49),
    _A2HostTargetId_Type()
)
a2HostTargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2HostTargetId.setStatus("mandatory")
_TLogicalDriveInformation_Object = MibTable
tLogicalDriveInformation = _TLogicalDriveInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tLogicalDriveInformation.setStatus("mandatory")
_ELogicalDriveInformation_Object = MibTableRow
eLogicalDriveInformation = _ELogicalDriveInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1)
)
eLogicalDriveInformation.setIndexNames(
    (0, "MYLEXRAID-MIB", "a3ControllerNumber"),
    (0, "MYLEXRAID-MIB", "a3LogicalDriveNumber"),
)
if mibBuilder.loadTexts:
    eLogicalDriveInformation.setStatus("mandatory")
_A3ControllerNumber_Type = DmiInteger
_A3ControllerNumber_Object = MibTableColumn
a3ControllerNumber = _A3ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 1),
    _A3ControllerNumber_Type()
)
a3ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ControllerNumber.setStatus("mandatory")
_A3LogicalDriveNumber_Type = DmiInteger
_A3LogicalDriveNumber_Object = MibTableColumn
a3LogicalDriveNumber = _A3LogicalDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 2),
    _A3LogicalDriveNumber_Type()
)
a3LogicalDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3LogicalDriveNumber.setStatus("mandatory")


class _A3OperationalState_Type(Integer32):
    """Custom type a3OperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              128,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 4),
          ("vNotPresent", 128),
          ("vOffline", 255),
          ("vOnline", 3))
    )


_A3OperationalState_Type.__name__ = "Integer32"
_A3OperationalState_Object = MibTableColumn
a3OperationalState = _A3OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 3),
    _A3OperationalState_Type()
)
a3OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperationalState.setStatus("mandatory")
_A3RaidLevel_Type = DmiInteger
_A3RaidLevel_Object = MibTableColumn
a3RaidLevel = _A3RaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 4),
    _A3RaidLevel_Type()
)
a3RaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RaidLevel.setStatus("mandatory")


class _A3WritePolicy_Type(Integer32):
    """Custom type a3WritePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128)
        )
    )
    namedValues = NamedValues(
        *(("vWriteBack", 128),
          ("vWriteThru", 0))
    )


_A3WritePolicy_Type.__name__ = "Integer32"
_A3WritePolicy_Object = MibTableColumn
a3WritePolicy = _A3WritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 5),
    _A3WritePolicy_Type()
)
a3WritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3WritePolicy.setStatus("mandatory")
_A3SizeInMb_Type = DmiInteger
_A3SizeInMb_Object = MibTableColumn
a3SizeInMb = _A3SizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 6),
    _A3SizeInMb_Type()
)
a3SizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3SizeInMb.setStatus("mandatory")
_A3PhysicalSizeInMb_Type = DmiInteger
_A3PhysicalSizeInMb_Object = MibTableColumn
a3PhysicalSizeInMb = _A3PhysicalSizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 7),
    _A3PhysicalSizeInMb_Type()
)
a3PhysicalSizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3PhysicalSizeInMb.setStatus("mandatory")
_A3StripeSizeInBytes_Type = DmiInteger
_A3StripeSizeInBytes_Object = MibTableColumn
a3StripeSizeInBytes = _A3StripeSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 8),
    _A3StripeSizeInBytes_Type()
)
a3StripeSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3StripeSizeInBytes.setStatus("mandatory")
_A3PhysicalDriveMap_Type = DmiDisplaystring
_A3PhysicalDriveMap_Object = MibTableColumn
a3PhysicalDriveMap = _A3PhysicalDriveMap_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 9),
    _A3PhysicalDriveMap_Type()
)
a3PhysicalDriveMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3PhysicalDriveMap.setStatus("mandatory")
_A3ArrayList_Type = DmiDisplaystring
_A3ArrayList_Object = MibTableColumn
a3ArrayList = _A3ArrayList_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 10),
    _A3ArrayList_Type()
)
a3ArrayList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ArrayList.setStatus("mandatory")
_A3RaidLevelString_Type = DmiDisplaystring
_A3RaidLevelString_Object = MibTableColumn
a3RaidLevelString = _A3RaidLevelString_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 3, 1, 11),
    _A3RaidLevelString_Type()
)
a3RaidLevelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RaidLevelString.setStatus("mandatory")
_TPhysicalDeviceInformation_Object = MibTable
tPhysicalDeviceInformation = _TPhysicalDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tPhysicalDeviceInformation.setStatus("mandatory")
_EPhysicalDeviceInformation_Object = MibTableRow
ePhysicalDeviceInformation = _EPhysicalDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1)
)
ePhysicalDeviceInformation.setIndexNames(
    (0, "MYLEXRAID-MIB", "a4ControllerNumber"),
    (0, "MYLEXRAID-MIB", "a4ChannelNumber"),
    (0, "MYLEXRAID-MIB", "a4TargetId"),
)
if mibBuilder.loadTexts:
    ePhysicalDeviceInformation.setStatus("mandatory")
_A4ControllerNumber_Type = DmiInteger
_A4ControllerNumber_Object = MibTableColumn
a4ControllerNumber = _A4ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 1),
    _A4ControllerNumber_Type()
)
a4ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ControllerNumber.setStatus("mandatory")
_A4ChannelNumber_Type = DmiInteger
_A4ChannelNumber_Object = MibTableColumn
a4ChannelNumber = _A4ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 2),
    _A4ChannelNumber_Type()
)
a4ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ChannelNumber.setStatus("mandatory")
_A4TargetId_Type = DmiInteger
_A4TargetId_Object = MibTableColumn
a4TargetId = _A4TargetId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 3),
    _A4TargetId_Type()
)
a4TargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4TargetId.setStatus("mandatory")
_A4Lun_Type = DmiInteger
_A4Lun_Object = MibTableColumn
a4Lun = _A4Lun_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 4),
    _A4Lun_Type()
)
a4Lun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Lun.setStatus("mandatory")


class _A4OperationalState_Type(Integer32):
    """Custom type a4OperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              16,
              130)
        )
    )
    namedValues = NamedValues(
        *(("vDead", 0),
          ("vHotspare", 16),
          ("vInstallationAbort", 4),
          ("vNotPresent", 6),
          ("vOnline", 3),
          ("vPresent", 5),
          ("vRebuildCancelled", 130),
          ("vRebuilding", 2))
    )


_A4OperationalState_Type.__name__ = "Integer32"
_A4OperationalState_Object = MibTableColumn
a4OperationalState = _A4OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 5),
    _A4OperationalState_Type()
)
a4OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4OperationalState.setStatus("mandatory")
_A4VendorId_Type = DmiDisplaystring
_A4VendorId_Object = MibTableColumn
a4VendorId = _A4VendorId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 6),
    _A4VendorId_Type()
)
a4VendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4VendorId.setStatus("mandatory")
_A4ProductId_Type = DmiDisplaystring
_A4ProductId_Object = MibTableColumn
a4ProductId = _A4ProductId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 7),
    _A4ProductId_Type()
)
a4ProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ProductId.setStatus("mandatory")
_A4ProductRevisionLevel_Type = DmiDisplaystring
_A4ProductRevisionLevel_Object = MibTableColumn
a4ProductRevisionLevel = _A4ProductRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 8),
    _A4ProductRevisionLevel_Type()
)
a4ProductRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ProductRevisionLevel.setStatus("mandatory")
_A4SizeInMb_Type = DmiInteger
_A4SizeInMb_Object = MibTableColumn
a4SizeInMb = _A4SizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 9),
    _A4SizeInMb_Type()
)
a4SizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4SizeInMb.setStatus("mandatory")


class _A4DeviceType_Type(Integer32):
    """Custom type a4DeviceType based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              199,
              204)
        )
    )
    namedValues = NamedValues(
        *(("vCdrom", 5),
          ("vChanger", 8),
          ("vCommunications", 9),
          ("vCtrlChannel", 204),
          ("vFixedDrive", 0),
          ("vGraphics-0", 10),
          ("vGraphics-1", 11),
          ("vMo", 7),
          ("vPrinter", 2),
          ("vProcessor", 3),
          ("vReserved-0", 12),
          ("vReserved-1", 13),
          ("vReserved-10", 22),
          ("vReserved-11", 23),
          ("vReserved-12", 24),
          ("vReserved-13", 25),
          ("vReserved-14", 26),
          ("vReserved-15", 27),
          ("vReserved-16", 28),
          ("vReserved-17", 29),
          ("vReserved-18", 30),
          ("vReserved-2", 14),
          ("vReserved-3", 15),
          ("vReserved-4", 16),
          ("vReserved-5", 17),
          ("vReserved-6", 18),
          ("vReserved-7", 19),
          ("vReserved-8", 20),
          ("vReserved-9", 21),
          ("vScanner", 6),
          ("vScsiHostBusAdapter", 199),
          ("vTape", 1),
          ("vUnknown", 31),
          ("vWorm", 4))
    )


_A4DeviceType_Type.__name__ = "Integer32"
_A4DeviceType_Object = MibTableColumn
a4DeviceType = _A4DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 10),
    _A4DeviceType_Type()
)
a4DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4DeviceType.setStatus("mandatory")
_A4SoftErrors_Type = DmiCounter
_A4SoftErrors_Object = MibTableColumn
a4SoftErrors = _A4SoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 11),
    _A4SoftErrors_Type()
)
a4SoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4SoftErrors.setStatus("mandatory")
_A4HardErrors_Type = DmiCounter
_A4HardErrors_Object = MibTableColumn
a4HardErrors = _A4HardErrors_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 12),
    _A4HardErrors_Type()
)
a4HardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4HardErrors.setStatus("mandatory")
_A4ParityErrors_Type = DmiCounter
_A4ParityErrors_Object = MibTableColumn
a4ParityErrors = _A4ParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 13),
    _A4ParityErrors_Type()
)
a4ParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ParityErrors.setStatus("mandatory")
_A4MiscErrors_Type = DmiCounter
_A4MiscErrors_Object = MibTableColumn
a4MiscErrors = _A4MiscErrors_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 14),
    _A4MiscErrors_Type()
)
a4MiscErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4MiscErrors.setStatus("mandatory")
_A4ArrayList_Type = DmiDisplaystring
_A4ArrayList_Object = MibTableColumn
a4ArrayList = _A4ArrayList_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 15),
    _A4ArrayList_Type()
)
a4ArrayList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ArrayList.setStatus("mandatory")
_A4LogicalDriveList_Type = DmiDisplaystring
_A4LogicalDriveList_Object = MibTableColumn
a4LogicalDriveList = _A4LogicalDriveList_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 16),
    _A4LogicalDriveList_Type()
)
a4LogicalDriveList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4LogicalDriveList.setStatus("mandatory")
_A4BusSpeed_Type = DmiDisplaystring
_A4BusSpeed_Object = MibTableColumn
a4BusSpeed = _A4BusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 17),
    _A4BusSpeed_Type()
)
a4BusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BusSpeed.setStatus("mandatory")
_A4BusWidth_Type = DmiDisplaystring
_A4BusWidth_Object = MibTableColumn
a4BusWidth = _A4BusWidth_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 18),
    _A4BusWidth_Type()
)
a4BusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BusWidth.setStatus("mandatory")


class _A4CommandQueuing_Type(Integer32):
    """Custom type a4CommandQueuing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A4CommandQueuing_Type.__name__ = "Integer32"
_A4CommandQueuing_Object = MibTableColumn
a4CommandQueuing = _A4CommandQueuing_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 19),
    _A4CommandQueuing_Type()
)
a4CommandQueuing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4CommandQueuing.setStatus("mandatory")
_A4PfaErrors_Type = DmiCounter
_A4PfaErrors_Object = MibTableColumn
a4PfaErrors = _A4PfaErrors_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 4, 1, 20),
    _A4PfaErrors_Type()
)
a4PfaErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4PfaErrors.setStatus("mandatory")
_TMylexDacManagementSoftware_ObjectIdentity = ObjectIdentity
tMylexDacManagementSoftware = _TMylexDacManagementSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 5)
)
_EMylexDacManagementSoftware_ObjectIdentity = ObjectIdentity
eMylexDacManagementSoftware = _EMylexDacManagementSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 5, 1)
)
_A5ManagementSoftwareRevision_Type = DmiDisplaystring
_A5ManagementSoftwareRevision_Object = MibScalar
a5ManagementSoftwareRevision = _A5ManagementSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 5, 1, 1),
    _A5ManagementSoftwareRevision_Type()
)
a5ManagementSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5ManagementSoftwareRevision.setStatus("mandatory")
_A5ManagementSoftwareBuildDate_Type = DmiDisplaystring
_A5ManagementSoftwareBuildDate_Object = MibScalar
a5ManagementSoftwareBuildDate = _A5ManagementSoftwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 5, 1, 2),
    _A5ManagementSoftwareBuildDate_Type()
)
a5ManagementSoftwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5ManagementSoftwareBuildDate.setStatus("mandatory")
_A5MylexDacDeviceDriverRevision_Type = DmiDisplaystring
_A5MylexDacDeviceDriverRevision_Object = MibScalar
a5MylexDacDeviceDriverRevision = _A5MylexDacDeviceDriverRevision_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 5, 1, 3),
    _A5MylexDacDeviceDriverRevision_Type()
)
a5MylexDacDeviceDriverRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5MylexDacDeviceDriverRevision.setStatus("mandatory")
_A5MylexDacDeviceDriverBuildDate_Type = DmiDisplaystring
_A5MylexDacDeviceDriverBuildDate_Object = MibScalar
a5MylexDacDeviceDriverBuildDate = _A5MylexDacDeviceDriverBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 5, 1, 4),
    _A5MylexDacDeviceDriverBuildDate_Type()
)
a5MylexDacDeviceDriverBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5MylexDacDeviceDriverBuildDate.setStatus("mandatory")
_A5GamDriverRevision_Type = DmiDisplaystring
_A5GamDriverRevision_Object = MibScalar
a5GamDriverRevision = _A5GamDriverRevision_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 5, 1, 5),
    _A5GamDriverRevision_Type()
)
a5GamDriverRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5GamDriverRevision.setStatus("mandatory")
_A5GamDriverBuildDate_Type = DmiDisplaystring
_A5GamDriverBuildDate_Object = MibScalar
a5GamDriverBuildDate = _A5GamDriverBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 5, 1, 6),
    _A5GamDriverBuildDate_Type()
)
a5GamDriverBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5GamDriverBuildDate.setStatus("mandatory")
_TLogicalDriveStatistics_Object = MibTable
tLogicalDriveStatistics = _TLogicalDriveStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tLogicalDriveStatistics.setStatus("mandatory")
_ELogicalDriveStatistics_Object = MibTableRow
eLogicalDriveStatistics = _ELogicalDriveStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 6, 1)
)
eLogicalDriveStatistics.setIndexNames(
    (0, "MYLEXRAID-MIB", "a6ControllerNumber"),
    (0, "MYLEXRAID-MIB", "a6LogicalDriveNumber"),
)
if mibBuilder.loadTexts:
    eLogicalDriveStatistics.setStatus("mandatory")
_A6ControllerNumber_Type = DmiInteger
_A6ControllerNumber_Object = MibTableColumn
a6ControllerNumber = _A6ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 6, 1, 1),
    _A6ControllerNumber_Type()
)
a6ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ControllerNumber.setStatus("mandatory")
_A6LogicalDriveNumber_Type = DmiInteger
_A6LogicalDriveNumber_Object = MibTableColumn
a6LogicalDriveNumber = _A6LogicalDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 6, 1, 2),
    _A6LogicalDriveNumber_Type()
)
a6LogicalDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6LogicalDriveNumber.setStatus("mandatory")
_A6ReadRequests_Type = DmiCounter
_A6ReadRequests_Object = MibTableColumn
a6ReadRequests = _A6ReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 6, 1, 3),
    _A6ReadRequests_Type()
)
a6ReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ReadRequests.setStatus("mandatory")
_A6DataReadInMb_Type = DmiInteger
_A6DataReadInMb_Object = MibTableColumn
a6DataReadInMb = _A6DataReadInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 6, 1, 4),
    _A6DataReadInMb_Type()
)
a6DataReadInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DataReadInMb.setStatus("mandatory")
_A6WriteRequests_Type = DmiCounter
_A6WriteRequests_Object = MibTableColumn
a6WriteRequests = _A6WriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 6, 1, 5),
    _A6WriteRequests_Type()
)
a6WriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6WriteRequests.setStatus("mandatory")
_A6DataWrittenInMb_Type = DmiInteger
_A6DataWrittenInMb_Object = MibTableColumn
a6DataWrittenInMb = _A6DataWrittenInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 6, 1, 6),
    _A6DataWrittenInMb_Type()
)
a6DataWrittenInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DataWrittenInMb.setStatus("mandatory")
_A6ReadCacheHitPercentage_Type = DmiInteger
_A6ReadCacheHitPercentage_Object = MibTableColumn
a6ReadCacheHitPercentage = _A6ReadCacheHitPercentage_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 6, 1, 7),
    _A6ReadCacheHitPercentage_Type()
)
a6ReadCacheHitPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ReadCacheHitPercentage.setStatus("mandatory")
_TPhysicalDriveStatistics_Object = MibTable
tPhysicalDriveStatistics = _TPhysicalDriveStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tPhysicalDriveStatistics.setStatus("mandatory")
_EPhysicalDriveStatistics_Object = MibTableRow
ePhysicalDriveStatistics = _EPhysicalDriveStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7, 1)
)
ePhysicalDriveStatistics.setIndexNames(
    (0, "MYLEXRAID-MIB", "a7ControllerNumber"),
    (0, "MYLEXRAID-MIB", "a7ChannelNumber"),
    (0, "MYLEXRAID-MIB", "a7TargetId"),
)
if mibBuilder.loadTexts:
    ePhysicalDriveStatistics.setStatus("mandatory")
_A7ControllerNumber_Type = DmiInteger
_A7ControllerNumber_Object = MibTableColumn
a7ControllerNumber = _A7ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7, 1, 1),
    _A7ControllerNumber_Type()
)
a7ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ControllerNumber.setStatus("mandatory")
_A7ChannelNumber_Type = DmiInteger
_A7ChannelNumber_Object = MibTableColumn
a7ChannelNumber = _A7ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7, 1, 2),
    _A7ChannelNumber_Type()
)
a7ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ChannelNumber.setStatus("mandatory")
_A7TargetId_Type = DmiInteger
_A7TargetId_Object = MibTableColumn
a7TargetId = _A7TargetId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7, 1, 3),
    _A7TargetId_Type()
)
a7TargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7TargetId.setStatus("mandatory")
_A7Lun_Type = DmiInteger
_A7Lun_Object = MibTableColumn
a7Lun = _A7Lun_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7, 1, 4),
    _A7Lun_Type()
)
a7Lun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Lun.setStatus("mandatory")
_A7ReadRequests_Type = DmiCounter
_A7ReadRequests_Object = MibTableColumn
a7ReadRequests = _A7ReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7, 1, 5),
    _A7ReadRequests_Type()
)
a7ReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ReadRequests.setStatus("mandatory")
_A7DataReadInMb_Type = DmiInteger
_A7DataReadInMb_Object = MibTableColumn
a7DataReadInMb = _A7DataReadInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7, 1, 6),
    _A7DataReadInMb_Type()
)
a7DataReadInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7DataReadInMb.setStatus("mandatory")
_A7WriteRequests_Type = DmiCounter
_A7WriteRequests_Object = MibTableColumn
a7WriteRequests = _A7WriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7, 1, 7),
    _A7WriteRequests_Type()
)
a7WriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7WriteRequests.setStatus("mandatory")
_A7DataWrittenInMb_Type = DmiInteger
_A7DataWrittenInMb_Object = MibTableColumn
a7DataWrittenInMb = _A7DataWrittenInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 7, 1, 8),
    _A7DataWrittenInMb_Type()
)
a7DataWrittenInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7DataWrittenInMb.setStatus("mandatory")
_TFaultManagementCabinetInformation_Object = MibTable
tFaultManagementCabinetInformation = _TFaultManagementCabinetInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tFaultManagementCabinetInformation.setStatus("mandatory")
_EFaultManagementCabinetInformation_Object = MibTableRow
eFaultManagementCabinetInformation = _EFaultManagementCabinetInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1)
)
eFaultManagementCabinetInformation.setIndexNames(
    (0, "MYLEXRAID-MIB", "a8ControllerNumber"),
    (0, "MYLEXRAID-MIB", "a8ChannelNumber"),
    (0, "MYLEXRAID-MIB", "a8CabinetNumber"),
)
if mibBuilder.loadTexts:
    eFaultManagementCabinetInformation.setStatus("mandatory")
_A8ControllerNumber_Type = DmiInteger
_A8ControllerNumber_Object = MibTableColumn
a8ControllerNumber = _A8ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 1),
    _A8ControllerNumber_Type()
)
a8ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8ControllerNumber.setStatus("mandatory")
_A8ChannelNumber_Type = DmiInteger
_A8ChannelNumber_Object = MibTableColumn
a8ChannelNumber = _A8ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 2),
    _A8ChannelNumber_Type()
)
a8ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8ChannelNumber.setStatus("mandatory")
_A8CabinetNumber_Type = DmiInteger
_A8CabinetNumber_Object = MibTableColumn
a8CabinetNumber = _A8CabinetNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 3),
    _A8CabinetNumber_Type()
)
a8CabinetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8CabinetNumber.setStatus("mandatory")
_A8TargetId_Type = DmiInteger
_A8TargetId_Object = MibTableColumn
a8TargetId = _A8TargetId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 4),
    _A8TargetId_Type()
)
a8TargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8TargetId.setStatus("mandatory")
_A8Lun_Type = DmiInteger
_A8Lun_Object = MibTableColumn
a8Lun = _A8Lun_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 5),
    _A8Lun_Type()
)
a8Lun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Lun.setStatus("mandatory")


class _A8CabinetType_Type(Integer32):
    """Custom type a8CabinetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              32,
              64,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vConnerCr-6", 1),
          ("vConnerSmartCabinet", 2),
          ("vSafte", 32),
          ("vSafte1", 3),
          ("vSes", 64),
          ("vUnknown", 255))
    )


_A8CabinetType_Type.__name__ = "Integer32"
_A8CabinetType_Object = MibTableColumn
a8CabinetType = _A8CabinetType_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 6),
    _A8CabinetType_Type()
)
a8CabinetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8CabinetType.setStatus("mandatory")
_A8NumberOfFans_Type = DmiInteger
_A8NumberOfFans_Object = MibTableColumn
a8NumberOfFans = _A8NumberOfFans_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 7),
    _A8NumberOfFans_Type()
)
a8NumberOfFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfFans.setStatus("mandatory")
_A8NumberOfPowerSupplyUnits_Type = DmiInteger
_A8NumberOfPowerSupplyUnits_Object = MibTableColumn
a8NumberOfPowerSupplyUnits = _A8NumberOfPowerSupplyUnits_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 8),
    _A8NumberOfPowerSupplyUnits_Type()
)
a8NumberOfPowerSupplyUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfPowerSupplyUnits.setStatus("mandatory")
_A8NumberOfHeatSensors_Type = DmiInteger
_A8NumberOfHeatSensors_Object = MibTableColumn
a8NumberOfHeatSensors = _A8NumberOfHeatSensors_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 9),
    _A8NumberOfHeatSensors_Type()
)
a8NumberOfHeatSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfHeatSensors.setStatus("mandatory")
_A8NumberOfDriveSlots_Type = DmiInteger
_A8NumberOfDriveSlots_Object = MibTableColumn
a8NumberOfDriveSlots = _A8NumberOfDriveSlots_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 10),
    _A8NumberOfDriveSlots_Type()
)
a8NumberOfDriveSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfDriveSlots.setStatus("mandatory")
_A8NumberOfDoorLocks_Type = DmiInteger
_A8NumberOfDoorLocks_Object = MibTableColumn
a8NumberOfDoorLocks = _A8NumberOfDoorLocks_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 11),
    _A8NumberOfDoorLocks_Type()
)
a8NumberOfDoorLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfDoorLocks.setStatus("mandatory")
_A8NumberOfSpeakers_Type = DmiInteger
_A8NumberOfSpeakers_Object = MibTableColumn
a8NumberOfSpeakers = _A8NumberOfSpeakers_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 12),
    _A8NumberOfSpeakers_Type()
)
a8NumberOfSpeakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfSpeakers.setStatus("mandatory")
_A8NumberOfFansCritical_Type = DmiInteger
_A8NumberOfFansCritical_Object = MibTableColumn
a8NumberOfFansCritical = _A8NumberOfFansCritical_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 13),
    _A8NumberOfFansCritical_Type()
)
a8NumberOfFansCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfFansCritical.setStatus("mandatory")
_A8NumberOfPowerSupplyUnitsCritical_Type = DmiInteger
_A8NumberOfPowerSupplyUnitsCritical_Object = MibTableColumn
a8NumberOfPowerSupplyUnitsCritical = _A8NumberOfPowerSupplyUnitsCritical_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 14),
    _A8NumberOfPowerSupplyUnitsCritical_Type()
)
a8NumberOfPowerSupplyUnitsCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfPowerSupplyUnitsCritical.setStatus("mandatory")
_A8NumberOfHeatSensorsCritical_Type = DmiInteger
_A8NumberOfHeatSensorsCritical_Object = MibTableColumn
a8NumberOfHeatSensorsCritical = _A8NumberOfHeatSensorsCritical_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 15),
    _A8NumberOfHeatSensorsCritical_Type()
)
a8NumberOfHeatSensorsCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfHeatSensorsCritical.setStatus("mandatory")
_A8NumberOfFansFailed_Type = DmiInteger
_A8NumberOfFansFailed_Object = MibTableColumn
a8NumberOfFansFailed = _A8NumberOfFansFailed_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 16),
    _A8NumberOfFansFailed_Type()
)
a8NumberOfFansFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfFansFailed.setStatus("mandatory")
_A8NumberOfPowerSupplyUnitsFailed_Type = DmiInteger
_A8NumberOfPowerSupplyUnitsFailed_Object = MibTableColumn
a8NumberOfPowerSupplyUnitsFailed = _A8NumberOfPowerSupplyUnitsFailed_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 17),
    _A8NumberOfPowerSupplyUnitsFailed_Type()
)
a8NumberOfPowerSupplyUnitsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfPowerSupplyUnitsFailed.setStatus("mandatory")
_A8NumberOfHeatSensorsFailed_Type = DmiInteger
_A8NumberOfHeatSensorsFailed_Object = MibTableColumn
a8NumberOfHeatSensorsFailed = _A8NumberOfHeatSensorsFailed_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 8, 1, 18),
    _A8NumberOfHeatSensorsFailed_Type()
)
a8NumberOfHeatSensorsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfHeatSensorsFailed.setStatus("mandatory")
_TMylexRaidEventInformation_Object = MibTable
tMylexRaidEventInformation = _TMylexRaidEventInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tMylexRaidEventInformation.setStatus("mandatory")
_EMylexRaidEventInformation_Object = MibTableRow
eMylexRaidEventInformation = _EMylexRaidEventInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1)
)
eMylexRaidEventInformation.setIndexNames(
    (0, "MYLEXRAID-MIB", "a9EventTableIndex"),
)
if mibBuilder.loadTexts:
    eMylexRaidEventInformation.setStatus("mandatory")
_A9EventTableIndex_Type = DmiInteger
_A9EventTableIndex_Object = MibTableColumn
a9EventTableIndex = _A9EventTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 1),
    _A9EventTableIndex_Type()
)
a9EventTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9EventTableIndex.setStatus("mandatory")


class _A9EventCode_Type(Integer32):
    """Custom type a9EventCode based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              96,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
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
              157,
              158,
              159,
              160,
              161,
              162,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              256,
              257,
              258,
              259,
              272,
              273,
              274,
              275,
              288,
              289,
              290,
              291,
              292,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              384,
              385,
              386,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              419,
              420,
              421,
              422,
              423,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              431,
              432,
              433,
              434,
              435,
              436,
              437,
              438,
              439,
              440,
              441,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              640,
              641,
              642,
              643,
              644,
              645,
              700,
              701,
              702,
              703,
              800,
              801,
              802,
              803,
              804,
              805,
              806,
              807,
              808,
              809,
              896,
              897,
              912,
              928,
              944,
              268435455)
        )
    )
    namedValues = NamedValues(
        *(("vAemi-fan-failed", 258),
          ("vAemi-over-temperature", 291),
          ("vAemi-pwr-supply-failed", 274),
          ("vAutoboot-changed", 518),
          ("vCfg-clear", 801),
          ("vCfg-cod-access-error", 803),
          ("vCfg-cod-converted", 804),
          ("vCfg-cod-import-failed", 805),
          ("vCfg-cod-lun-map-not-found", 809),
          ("vCfg-cod-not-found", 808),
          ("vCfg-invalid", 802),
          ("vCfg-new", 800),
          ("vChannel-failed", 640),
          ("vChannel-fiber-alive", 645),
          ("vChannel-fiber-dead", 644),
          ("vChannel-ok", 641),
          ("vChannel-scsi-bus-alive", 643),
          ("vChannel-scsi-bus-dead", 642),
          ("vCtldev-automatic-flash-started", 432),
          ("vCtldev-bad-bootrom-image", 425),
          ("vCtldev-bad-mac-address", 426),
          ("vCtldev-bbu-batt-test-canceled", 521),
          ("vCtldev-bbu-batt-test-complete", 520),
          ("vCtldev-bbu-batt-test-failed", 522),
          ("vCtldev-bbu-batt-test-start", 519),
          ("vCtldev-bbu-calibrate-abort", 409),
          ("vCtldev-bbu-calibrate-done", 408),
          ("vCtldev-bbu-calibrate-start", 407),
          ("vCtldev-bbu-found", 392),
          ("vCtldev-bbu-no-battery", 410),
          ("vCtldev-bbu-noresponse", 405),
          ("vCtldev-bbu-out-of-service", 418),
          ("vCtldev-bbu-power-low", 393),
          ("vCtldev-bbu-power-ok", 394),
          ("vCtldev-bbu-recond-abort", 402),
          ("vCtldev-bbu-recond-done", 401),
          ("vCtldev-bbu-recond-needed", 416),
          ("vCtldev-bbu-recond-start", 400),
          ("vCtldev-conserv-cache-mode", 411),
          ("vCtldev-critical", 399),
          ("vCtldev-ctrl-params-checksum-failed", 72),
          ("vCtldev-dead", 388),
          ("vCtldev-dev-start-cmplt", 413),
          ("vCtldev-dual-enabled", 422),
          ("vCtldev-firmware-mismatch", 404),
          ("vCtldev-found", 390),
          ("vCtldev-gone", 391),
          ("vCtldev-hard-ecc-corrected", 415),
          ("vCtldev-in-cluster", 429),
          ("vCtldev-inserted-ptnr", 421),
          ("vCtldev-installation-aborted", 403),
          ("vCtldev-kill-ptnr", 423),
          ("vCtldev-mirror-critical-drive", 428),
          ("vCtldev-mirror-race-entry-failed", 71),
          ("vCtldev-mirror-race-recovery-failed", 427),
          ("vCtldev-mirror-race-table-error", 440),
          ("vCtldev-negotiation-board-type", 435),
          ("vCtldev-negotiation-cache-size", 439),
          ("vCtldev-negotiation-disk-channels", 436),
          ("vCtldev-negotiation-failed-jumpers", 433),
          ("vCtldev-negotiation-host-channels", 437),
          ("vCtldev-negotiation-memory-size", 438),
          ("vCtldev-negotiation-same-id", 434),
          ("vCtldev-nexus", 424),
          ("vCtldev-normal-cache-mode", 412),
          ("vCtldev-not-in-cluster", 430),
          ("vCtldev-offline", 398),
          ("vCtldev-online", 397),
          ("vCtldev-power-off", 395),
          ("vCtldev-power-on", 396),
          ("vCtldev-relinquish-ptnr", 420),
          ("vCtldev-removed-ptnr", 417),
          ("vCtldev-reset", 389),
          ("vCtldev-soft-ecc-corrected", 414),
          ("vCtldev-state-table-full", 386),
          ("vCtldev-stop-rejected", 441),
          ("vCtldev-update-ptnr-status", 419),
          ("vCtldev-warm-boot-error", 406),
          ("vCtldev-writeback-error", 385),
          ("vDebug-dump-generated", 806),
          ("vDebug-dump-generated-partner", 807),
          ("vEnclaccess-critical", 330),
          ("vEnclaccess-offline", 332),
          ("vEnclaccess-ok", 331),
          ("vEnclaccess-ready", 334),
          ("vEnclcold-fail", 340),
          ("vEnclcold-warn", 339),
          ("vEnclfan-failed", 320),
          ("vEnclfan-notpresent", 322),
          ("vEnclfan-ok", 321),
          ("vEnclfan-unknown", 337),
          ("vEnclheat-bad", 326),
          ("vEnclheat-critical", 327),
          ("vEnclheat-notpresent", 329),
          ("vEnclheat-ok", 328),
          ("vEnclheat-unknown", 335),
          ("vEnclosure-shutdown", 338),
          ("vEnclpower-failed", 323),
          ("vEnclpower-notpresent", 325),
          ("vEnclpower-ok", 324),
          ("vEnclpower-unknown", 336),
          ("vEnclses-softaddr-occurred", 333),
          ("vFatal-brkp", 897),
          ("vFatal-hang", 896),
          ("vFibredev-loopid-softaddr-occurred", 96),
          ("vFirmware-upgrade-complete", 74),
          ("vFirmware-upgrade-failed", 75),
          ("vFirmware-upgrade-started", 73),
          ("vFmt-ups-ac-fail", 308),
          ("vFmt-ups-bat-low", 309),
          ("vFmt-ups-disabled", 307),
          ("vFmt-ups-failed", 310),
          ("vFmt-ups-ok", 311),
          ("vFmtfan-failed", 256),
          ("vFmtfan-notpresent", 259),
          ("vFmtfan-ok", 257),
          ("vFmtheat-bad", 288),
          ("vFmtheat-critical", 289),
          ("vFmtheat-notpresent", 292),
          ("vFmtheat-ok", 290),
          ("vFmtpower-failed", 272),
          ("vFmtpower-notpresent", 275),
          ("vFmtpower-ok", 273),
          ("vFmtstwk-critical", 305),
          ("vFmtstwk-failed", 304),
          ("vFmtstwk-ok", 306),
          ("vI960-hw-err", 912),
          ("vLog-empty", 700),
          ("vLog-out-sync", 701),
          ("vLog-request-sense", 702),
          ("vLog-set-rtc", 703),
          ("vPhysdev-activespare", 26),
          ("vPhysdev-auto-rebuild-start", 5),
          ("vPhysdev-badtag-dead", 38),
          ("vPhysdev-bdtwrfail-dead", 49),
          ("vPhysdev-bsypar-dead", 41),
          ("vPhysdev-bycmd-dead", 42),
          ("vPhysdev-codwrfail-dead", 48),
          ("vPhysdev-command-abort", 20),
          ("vPhysdev-command-retried", 21),
          ("vPhysdev-command-timeout", 19),
          ("vPhysdev-dblcc-dead", 35),
          ("vPhysdev-dead", 12),
          ("vPhysdev-expandcapacity-done", 17),
          ("vPhysdev-expandcapacity-error", 18),
          ("vPhysdev-expandcapacity-start", 16),
          ("vPhysdev-failed-start", 54),
          ("vPhysdev-found", 13),
          ("vPhysdev-gone", 14),
          ("vPhysdev-grosserr-dead", 37),
          ("vPhysdev-hard-error", 3),
          ("vPhysdev-hot-spare-smaller", 62),
          ("vPhysdev-hotspare", 2),
          ("vPhysdev-id-mismatch", 53),
          ("vPhysdev-init-canceled", 32),
          ("vPhysdev-init-done", 30),
          ("vPhysdev-init-failed", 31),
          ("vPhysdev-init-started", 29),
          ("vPhysdev-manual-rebuild-start", 6),
          ("vPhysdev-misc-error", 24),
          ("vPhysdev-missing-dead", 47),
          ("vPhysdev-missing-onstartup", 57),
          ("vPhysdev-moving-to-other-chn", 59),
          ("vPhysdev-non-redundant-access", 67),
          ("vPhysdev-notrdy-dead", 46),
          ("vPhysdev-offline", 50),
          ("vPhysdev-offline-device-made-online", 60),
          ("vPhysdev-offset-set", 55),
          ("vPhysdev-online", 1),
          ("vPhysdev-parity-error", 22),
          ("vPhysdev-pfa", 4),
          ("vPhysdev-port-failed", 70),
          ("vPhysdev-rebuild", 52),
          ("vPhysdev-rebuild-canceled", 8),
          ("vPhysdev-rebuild-done", 7),
          ("vPhysdev-rebuild-error", 9),
          ("vPhysdev-rebuild-newdev-failed", 10),
          ("vPhysdev-rebuild-start-failed", 58),
          ("vPhysdev-rebuild-sysdev-failed", 11),
          ("vPhysdev-removed-dead", 36),
          ("vPhysdev-reqsense", 28),
          ("vPhysdev-reset", 25),
          ("vPhysdev-reset-dead", 34),
          ("vPhysdev-scsitmo-dead", 39),
          ("vPhysdev-seltmo-dead", 43),
          ("vPhysdev-seqerr-dead", 44),
          ("vPhysdev-set-bus-width", 56),
          ("vPhysdev-soft-error", 23),
          ("vPhysdev-soft-id", 69),
          ("vPhysdev-standby", 51),
          ("vPhysdev-standby-rebuild-start", 61),
          ("vPhysdev-sysreset-dead", 40),
          ("vPhysdev-type-invalid", 68),
          ("vPhysdev-unconfigured", 15),
          ("vPhysdev-unknownsts-dead", 45),
          ("vPhysdev-warmspare", 27),
          ("vPhysdev-writerec-dead", 33),
          ("vPpilot-logical-disk-offline", 64),
          ("vPpilot-logical-disk-online", 63),
          ("vPpilot-logical-disk-path-failback", 66),
          ("vPpilot-logical-disk-path-failover", 65),
          ("vSarm-hw-err", 928),
          ("vScsi-hw-err", 944),
          ("vSysdev-auto-rebuild-start", 137),
          ("vSysdev-badblock", 153),
          ("vSysdev-baddatablock", 156),
          ("vSysdev-bg-init-completed", 181),
          ("vSysdev-bg-init-failed", 180),
          ("vSysdev-bg-init-paused", 178),
          ("vSysdev-bg-init-restarted", 179),
          ("vSysdev-bg-init-started", 176),
          ("vSysdev-bg-init-stopped", 177),
          ("vSysdev-check-canceled", 130),
          ("vSysdev-check-done", 129),
          ("vSysdev-check-error", 131),
          ("vSysdev-check-physdev-failed", 133),
          ("vSysdev-check-start", 128),
          ("vSysdev-check-sysdev-failed", 132),
          ("vSysdev-critical", 135),
          ("vSysdev-data-for-block-lost", 159),
          ("vSysdev-data-loss-improper-shutdown", 431),
          ("vSysdev-data-loss-low-bbu-charge", 182),
          ("vSysdev-dataread-from-block-in-bdt", 158),
          ("vSysdev-expandcapacity-done", 151),
          ("vSysdev-expandcapacity-error", 152),
          ("vSysdev-expandcapacity-start", 150),
          ("vSysdev-found", 148),
          ("vSysdev-gone", 149),
          ("vSysdev-init-canceled", 146),
          ("vSysdev-init-done", 145),
          ("vSysdev-init-failed", 147),
          ("vSysdev-init-started", 144),
          ("vSysdev-manual-rebuild-start", 138),
          ("vSysdev-offline", 134),
          ("vSysdev-offline-device-made-available", 161),
          ("vSysdev-offline-device-made-available-wi", 160),
          ("vSysdev-online", 136),
          ("vSysdev-rebuild-canceled", 140),
          ("vSysdev-rebuild-done", 139),
          ("vSysdev-rebuild-error", 141),
          ("vSysdev-rebuild-newdev-failed", 142),
          ("vSysdev-rebuild-sysdev-failed", 143),
          ("vSysdev-sizechanged", 154),
          ("vSysdev-standby-rebuild-start", 162),
          ("vSysdev-typechanged", 155),
          ("vSysdev-wr-lun-map", 157),
          ("vSystem-alive", 516),
          ("vSystem-dead", 517),
          ("vSystem-size-table-full", 513),
          ("vSystem-started", 384),
          ("vSystem-started-new", 512),
          ("vSystem-user-logged-in", 514),
          ("vSystem-user-logged-out", 515),
          ("vUnknown", 268435455))
    )


_A9EventCode_Type.__name__ = "Integer32"
_A9EventCode_Object = MibTableColumn
a9EventCode = _A9EventCode_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 2),
    _A9EventCode_Type()
)
a9EventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9EventCode.setStatus("mandatory")
_A9EventTimeStamp_Type = DmiInteger
_A9EventTimeStamp_Object = MibTableColumn
a9EventTimeStamp = _A9EventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 3),
    _A9EventTimeStamp_Type()
)
a9EventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9EventTimeStamp.setStatus("mandatory")
_A9ControllerNumber_Type = DmiInteger
_A9ControllerNumber_Object = MibTableColumn
a9ControllerNumber = _A9ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 4),
    _A9ControllerNumber_Type()
)
a9ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ControllerNumber.setStatus("mandatory")
_A9ChannelNumber_Type = DmiInteger
_A9ChannelNumber_Object = MibTableColumn
a9ChannelNumber = _A9ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 5),
    _A9ChannelNumber_Type()
)
a9ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ChannelNumber.setStatus("mandatory")
_A9TargetId_Type = DmiInteger
_A9TargetId_Object = MibTableColumn
a9TargetId = _A9TargetId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 6),
    _A9TargetId_Type()
)
a9TargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9TargetId.setStatus("mandatory")
_A9Lun_Type = DmiInteger
_A9Lun_Object = MibTableColumn
a9Lun = _A9Lun_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 7),
    _A9Lun_Type()
)
a9Lun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9Lun.setStatus("mandatory")
_A9LogicalDriveNumber_Type = DmiInteger
_A9LogicalDriveNumber_Object = MibTableColumn
a9LogicalDriveNumber = _A9LogicalDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 8),
    _A9LogicalDriveNumber_Type()
)
a9LogicalDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9LogicalDriveNumber.setStatus("mandatory")
_A9FmtCabinetNumber_Type = DmiInteger
_A9FmtCabinetNumber_Object = MibTableColumn
a9FmtCabinetNumber = _A9FmtCabinetNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 9),
    _A9FmtCabinetNumber_Type()
)
a9FmtCabinetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9FmtCabinetNumber.setStatus("mandatory")
_A9FanUnitNumber_Type = DmiInteger
_A9FanUnitNumber_Object = MibTableColumn
a9FanUnitNumber = _A9FanUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 10),
    _A9FanUnitNumber_Type()
)
a9FanUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9FanUnitNumber.setStatus("mandatory")
_A9PowerSupplyUnitNumber_Type = DmiInteger
_A9PowerSupplyUnitNumber_Object = MibTableColumn
a9PowerSupplyUnitNumber = _A9PowerSupplyUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 11),
    _A9PowerSupplyUnitNumber_Type()
)
a9PowerSupplyUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9PowerSupplyUnitNumber.setStatus("mandatory")
_A9HeatSensorUnitNumber_Type = DmiInteger
_A9HeatSensorUnitNumber_Object = MibTableColumn
a9HeatSensorUnitNumber = _A9HeatSensorUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 12),
    _A9HeatSensorUnitNumber_Type()
)
a9HeatSensorUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9HeatSensorUnitNumber.setStatus("mandatory")
_A9EnclosureUnitNumber_Type = DmiInteger
_A9EnclosureUnitNumber_Object = MibTableColumn
a9EnclosureUnitNumber = _A9EnclosureUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 13),
    _A9EnclosureUnitNumber_Type()
)
a9EnclosureUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9EnclosureUnitNumber.setStatus("mandatory")
_TBatteryBackupUnitInformation_Object = MibTable
tBatteryBackupUnitInformation = _TBatteryBackupUnitInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tBatteryBackupUnitInformation.setStatus("mandatory")
_EBatteryBackupUnitInformation_Object = MibTableRow
eBatteryBackupUnitInformation = _EBatteryBackupUnitInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1)
)
eBatteryBackupUnitInformation.setIndexNames(
    (0, "MYLEXRAID-MIB", "a10ControllerNumber"),
)
if mibBuilder.loadTexts:
    eBatteryBackupUnitInformation.setStatus("mandatory")
_A10ControllerNumber_Type = DmiInteger
_A10ControllerNumber_Object = MibTableColumn
a10ControllerNumber = _A10ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1, 1),
    _A10ControllerNumber_Type()
)
a10ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10ControllerNumber.setStatus("mandatory")
_A10OperationalState_Type = DmiInteger
_A10OperationalState_Object = MibTableColumn
a10OperationalState = _A10OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1, 2),
    _A10OperationalState_Type()
)
a10OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10OperationalState.setStatus("mandatory")


class _A10BatteryType_Type(Integer32):
    """Custom type a10BatteryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("vLithiumion", 3),
          ("vNickelCadmium", 1),
          ("vNimh", 2),
          ("vNoBatterBackupPresent", 254),
          ("vUnknown", 0))
    )


_A10BatteryType_Type.__name__ = "Integer32"
_A10BatteryType_Object = MibTableColumn
a10BatteryType = _A10BatteryType_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1, 3),
    _A10BatteryType_Type()
)
a10BatteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10BatteryType.setStatus("mandatory")
_A10CurrentPowerInHours_Type = DmiInteger
_A10CurrentPowerInHours_Object = MibTableColumn
a10CurrentPowerInHours = _A10CurrentPowerInHours_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1, 4),
    _A10CurrentPowerInHours_Type()
)
a10CurrentPowerInHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10CurrentPowerInHours.setStatus("mandatory")
_A10MaximumPowerInHours_Type = DmiInteger
_A10MaximumPowerInHours_Object = MibTableColumn
a10MaximumPowerInHours = _A10MaximumPowerInHours_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1, 5),
    _A10MaximumPowerInHours_Type()
)
a10MaximumPowerInHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10MaximumPowerInHours.setStatus("mandatory")
_A10ThresholdValueInHours_Type = DmiInteger
_A10ThresholdValueInHours_Object = MibTableColumn
a10ThresholdValueInHours = _A10ThresholdValueInHours_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1, 6),
    _A10ThresholdValueInHours_Type()
)
a10ThresholdValueInHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10ThresholdValueInHours.setStatus("mandatory")
_A10ChargeLevelInPercentage_Type = DmiInteger
_A10ChargeLevelInPercentage_Object = MibTableColumn
a10ChargeLevelInPercentage = _A10ChargeLevelInPercentage_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1, 7),
    _A10ChargeLevelInPercentage_Type()
)
a10ChargeLevelInPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10ChargeLevelInPercentage.setStatus("mandatory")
_A10Version_Type = DmiInteger
_A10Version_Object = MibTableColumn
a10Version = _A10Version_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1, 8),
    _A10Version_Type()
)
a10Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10Version.setStatus("mandatory")
_A10OperationalStateString_Type = DmiDisplaystring
_A10OperationalStateString_Object = MibTableColumn
a10OperationalStateString = _A10OperationalStateString_Object(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 10, 1, 9),
    _A10OperationalStateString_Type()
)
a10OperationalStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10OperationalStateString.setStatus("mandatory")

# Managed Objects groups


# Notification objects

physdevOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 1)
)
physdevOnline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevOnline.setStatus(
        ""
    )

physdevHotspare = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 2)
)
physdevHotspare.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevHotspare.setStatus(
        ""
    )

physdevHardError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 3)
)
physdevHardError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevHardError.setStatus(
        ""
    )

physdevPfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 4)
)
physdevPfa.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevPfa.setStatus(
        ""
    )

physdevAutoRebuildStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 5)
)
physdevAutoRebuildStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevAutoRebuildStart.setStatus(
        ""
    )

physdevManualRebuildStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 6)
)
physdevManualRebuildStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevManualRebuildStart.setStatus(
        ""
    )

physdevRebuildDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 7)
)
physdevRebuildDone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevRebuildDone.setStatus(
        ""
    )

physdevRebuildCanceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 8)
)
physdevRebuildCanceled.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevRebuildCanceled.setStatus(
        ""
    )

physdevRebuildError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 9)
)
physdevRebuildError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevRebuildError.setStatus(
        ""
    )

physdevRebuildNewdevFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 10)
)
physdevRebuildNewdevFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevRebuildNewdevFailed.setStatus(
        ""
    )

physdevRebuildSysdevFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 11)
)
physdevRebuildSysdevFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevRebuildSysdevFailed.setStatus(
        ""
    )

physdevDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 12)
)
physdevDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevDead.setStatus(
        ""
    )

physdevFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 13)
)
physdevFound.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevFound.setStatus(
        ""
    )

physdevGone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 14)
)
physdevGone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevGone.setStatus(
        ""
    )

physdevUnconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 15)
)
physdevUnconfigured.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevUnconfigured.setStatus(
        ""
    )

physdevExpandcapacityStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 16)
)
physdevExpandcapacityStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevExpandcapacityStart.setStatus(
        ""
    )

physdevExpandcapacityDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 17)
)
physdevExpandcapacityDone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevExpandcapacityDone.setStatus(
        ""
    )

physdevExpandcapacityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 18)
)
physdevExpandcapacityError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevExpandcapacityError.setStatus(
        ""
    )

physdevCommandTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 19)
)
physdevCommandTimeout.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevCommandTimeout.setStatus(
        ""
    )

physdevCommandAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 20)
)
physdevCommandAbort.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevCommandAbort.setStatus(
        ""
    )

physdevCommandRetried = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 21)
)
physdevCommandRetried.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevCommandRetried.setStatus(
        ""
    )

physdevParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 22)
)
physdevParityError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevParityError.setStatus(
        ""
    )

physdevSoftError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 23)
)
physdevSoftError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevSoftError.setStatus(
        ""
    )

physdevMiscError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 24)
)
physdevMiscError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevMiscError.setStatus(
        ""
    )

physdevReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 25)
)
physdevReset.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevReset.setStatus(
        ""
    )

physdevActivespare = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 26)
)
physdevActivespare.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevActivespare.setStatus(
        ""
    )

physdevWarmspare = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 27)
)
physdevWarmspare.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevWarmspare.setStatus(
        ""
    )

physdevReqsense = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 28)
)
physdevReqsense.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevReqsense.setStatus(
        ""
    )

physdevInitStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 29)
)
physdevInitStarted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevInitStarted.setStatus(
        ""
    )

physdevInitDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 30)
)
physdevInitDone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevInitDone.setStatus(
        ""
    )

physdevInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 31)
)
physdevInitFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevInitFailed.setStatus(
        ""
    )

physdevInitCanceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 32)
)
physdevInitCanceled.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevInitCanceled.setStatus(
        ""
    )

physdevWriterecDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 33)
)
physdevWriterecDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevWriterecDead.setStatus(
        ""
    )

physdevResetDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 34)
)
physdevResetDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevResetDead.setStatus(
        ""
    )

physdevDblccDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 35)
)
physdevDblccDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevDblccDead.setStatus(
        ""
    )

physdevRemovedDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 36)
)
physdevRemovedDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevRemovedDead.setStatus(
        ""
    )

physdevGrosserrDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 37)
)
physdevGrosserrDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevGrosserrDead.setStatus(
        ""
    )

physdevBadtagDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 38)
)
physdevBadtagDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevBadtagDead.setStatus(
        ""
    )

physdevScsitmoDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 39)
)
physdevScsitmoDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevScsitmoDead.setStatus(
        ""
    )

physdevSysresetDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 40)
)
physdevSysresetDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevSysresetDead.setStatus(
        ""
    )

physdevBsyparDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 41)
)
physdevBsyparDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevBsyparDead.setStatus(
        ""
    )

physdevBycmdDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 42)
)
physdevBycmdDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevBycmdDead.setStatus(
        ""
    )

physdevSeltmoDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 43)
)
physdevSeltmoDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevSeltmoDead.setStatus(
        ""
    )

physdevSeqerrDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 44)
)
physdevSeqerrDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevSeqerrDead.setStatus(
        ""
    )

physdevUnknownstsDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 45)
)
physdevUnknownstsDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevUnknownstsDead.setStatus(
        ""
    )

physdevNotrdyDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 46)
)
physdevNotrdyDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevNotrdyDead.setStatus(
        ""
    )

physdevMissingDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 47)
)
physdevMissingDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevMissingDead.setStatus(
        ""
    )

physdevCodwrfailDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 48)
)
physdevCodwrfailDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevCodwrfailDead.setStatus(
        ""
    )

physdevBdtwrfailDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 49)
)
physdevBdtwrfailDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevBdtwrfailDead.setStatus(
        ""
    )

physdevOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 50)
)
physdevOffline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevOffline.setStatus(
        ""
    )

physdevStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 51)
)
physdevStandby.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevStandby.setStatus(
        ""
    )

physdevRebuild = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 52)
)
physdevRebuild.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevRebuild.setStatus(
        ""
    )

physdevIdMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 53)
)
physdevIdMismatch.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevIdMismatch.setStatus(
        ""
    )

physdevFailedStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 54)
)
physdevFailedStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevFailedStart.setStatus(
        ""
    )

physdevOffsetSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 55)
)
physdevOffsetSet.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevOffsetSet.setStatus(
        ""
    )

physdevSetBusWidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 56)
)
physdevSetBusWidth.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevSetBusWidth.setStatus(
        ""
    )

physdevMissingOnstartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 57)
)
physdevMissingOnstartup.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevMissingOnstartup.setStatus(
        ""
    )

physdevRebuildStartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 58)
)
physdevRebuildStartFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevRebuildStartFailed.setStatus(
        ""
    )

physdevMovingToOtherChn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 59)
)
physdevMovingToOtherChn.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevMovingToOtherChn.setStatus(
        ""
    )

physdevOfflineDeviceMadeOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 60)
)
physdevOfflineDeviceMadeOnline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevOfflineDeviceMadeOnline.setStatus(
        ""
    )

physdevStandbyRebuildStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 61)
)
physdevStandbyRebuildStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevStandbyRebuildStart.setStatus(
        ""
    )

physdevHotSpareSmaller = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 62)
)
physdevHotSpareSmaller.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevHotSpareSmaller.setStatus(
        ""
    )

ppilotLogicalDiskOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 63)
)
ppilotLogicalDiskOnline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ppilotLogicalDiskOnline.setStatus(
        ""
    )

ppilotLogicalDiskOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 64)
)
ppilotLogicalDiskOffline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ppilotLogicalDiskOffline.setStatus(
        ""
    )

ppilotLogicalDiskPathFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 65)
)
ppilotLogicalDiskPathFailover.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ppilotLogicalDiskPathFailover.setStatus(
        ""
    )

ppilotLogicalDiskPathFailback = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 66)
)
ppilotLogicalDiskPathFailback.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ppilotLogicalDiskPathFailback.setStatus(
        ""
    )

physdevNonRedundantAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 67)
)
physdevNonRedundantAccess.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevNonRedundantAccess.setStatus(
        ""
    )

physdevTypeInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 68)
)
physdevTypeInvalid.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevTypeInvalid.setStatus(
        ""
    )

physdevSoftId = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 69)
)
physdevSoftId.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevSoftId.setStatus(
        ""
    )

physdevPortFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 70)
)
physdevPortFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    physdevPortFailed.setStatus(
        ""
    )

ctldevMirrorRaceEntryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 71)
)
ctldevMirrorRaceEntryFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevMirrorRaceEntryFailed.setStatus(
        ""
    )

ctldevCtrlParamsChecksumFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 72)
)
ctldevCtrlParamsChecksumFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevCtrlParamsChecksumFailed.setStatus(
        ""
    )

firmwareUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 73)
)
firmwareUpgradeStarted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    firmwareUpgradeStarted.setStatus(
        ""
    )

firmwareUpgradeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 74)
)
firmwareUpgradeComplete.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    firmwareUpgradeComplete.setStatus(
        ""
    )

firmwareUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 75)
)
firmwareUpgradeFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    firmwareUpgradeFailed.setStatus(
        ""
    )

fibredevLoopidSoftaddrOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 96)
)
fibredevLoopidSoftaddrOccurred.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fibredevLoopidSoftaddrOccurred.setStatus(
        ""
    )

sysdevCheckStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 128)
)
sysdevCheckStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevCheckStart.setStatus(
        ""
    )

sysdevCheckDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 129)
)
sysdevCheckDone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevCheckDone.setStatus(
        ""
    )

sysdevCheckCanceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 130)
)
sysdevCheckCanceled.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevCheckCanceled.setStatus(
        ""
    )

sysdevCheckError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 131)
)
sysdevCheckError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevCheckError.setStatus(
        ""
    )

sysdevCheckSysdevFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 132)
)
sysdevCheckSysdevFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevCheckSysdevFailed.setStatus(
        ""
    )

sysdevCheckPhysdevFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 133)
)
sysdevCheckPhysdevFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevCheckPhysdevFailed.setStatus(
        ""
    )

sysdevOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 134)
)
sysdevOffline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevOffline.setStatus(
        ""
    )

sysdevCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 135)
)
sysdevCritical.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevCritical.setStatus(
        ""
    )

sysdevOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 136)
)
sysdevOnline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevOnline.setStatus(
        ""
    )

sysdevAutoRebuildStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 137)
)
sysdevAutoRebuildStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevAutoRebuildStart.setStatus(
        ""
    )

sysdevManualRebuildStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 138)
)
sysdevManualRebuildStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevManualRebuildStart.setStatus(
        ""
    )

sysdevRebuildDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 139)
)
sysdevRebuildDone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevRebuildDone.setStatus(
        ""
    )

sysdevRebuildCanceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 140)
)
sysdevRebuildCanceled.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevRebuildCanceled.setStatus(
        ""
    )

sysdevRebuildError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 141)
)
sysdevRebuildError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevRebuildError.setStatus(
        ""
    )

sysdevRebuildNewdevFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 142)
)
sysdevRebuildNewdevFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevRebuildNewdevFailed.setStatus(
        ""
    )

sysdevRebuildSysdevFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 143)
)
sysdevRebuildSysdevFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevRebuildSysdevFailed.setStatus(
        ""
    )

sysdevInitStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 144)
)
sysdevInitStarted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevInitStarted.setStatus(
        ""
    )

sysdevInitDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 145)
)
sysdevInitDone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevInitDone.setStatus(
        ""
    )

sysdevInitCanceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 146)
)
sysdevInitCanceled.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevInitCanceled.setStatus(
        ""
    )

sysdevInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 147)
)
sysdevInitFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevInitFailed.setStatus(
        ""
    )

sysdevFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 148)
)
sysdevFound.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevFound.setStatus(
        ""
    )

sysdevGone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 149)
)
sysdevGone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevGone.setStatus(
        ""
    )

sysdevExpandcapacityStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 150)
)
sysdevExpandcapacityStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevExpandcapacityStart.setStatus(
        ""
    )

sysdevExpandcapacityDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 151)
)
sysdevExpandcapacityDone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevExpandcapacityDone.setStatus(
        ""
    )

sysdevExpandcapacityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 152)
)
sysdevExpandcapacityError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevExpandcapacityError.setStatus(
        ""
    )

sysdevBadblock = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 153)
)
sysdevBadblock.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevBadblock.setStatus(
        ""
    )

sysdevSizechanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 154)
)
sysdevSizechanged.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevSizechanged.setStatus(
        ""
    )

sysdevTypechanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 155)
)
sysdevTypechanged.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevTypechanged.setStatus(
        ""
    )

sysdevBaddatablock = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 156)
)
sysdevBaddatablock.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevBaddatablock.setStatus(
        ""
    )

sysdevWrLunMap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 157)
)
sysdevWrLunMap.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevWrLunMap.setStatus(
        ""
    )

sysdevDatareadFromBlockInBdt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 158)
)
sysdevDatareadFromBlockInBdt.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevDatareadFromBlockInBdt.setStatus(
        ""
    )

sysdevDataForBlockLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 159)
)
sysdevDataForBlockLost.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevDataForBlockLost.setStatus(
        ""
    )

sysdevOfflineDeviceMadeAvailableWithDataloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 160)
)
sysdevOfflineDeviceMadeAvailableWithDataloss.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevOfflineDeviceMadeAvailableWithDataloss.setStatus(
        ""
    )

sysdevOfflineDeviceMadeAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 161)
)
sysdevOfflineDeviceMadeAvailable.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevOfflineDeviceMadeAvailable.setStatus(
        ""
    )

sysdevStandbyRebuildStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 162)
)
sysdevStandbyRebuildStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevStandbyRebuildStart.setStatus(
        ""
    )

sysdevBgInitStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 176)
)
sysdevBgInitStarted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevBgInitStarted.setStatus(
        ""
    )

sysdevBgInitStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 177)
)
sysdevBgInitStopped.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevBgInitStopped.setStatus(
        ""
    )

sysdevBgInitPaused = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 178)
)
sysdevBgInitPaused.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevBgInitPaused.setStatus(
        ""
    )

sysdevBgInitRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 179)
)
sysdevBgInitRestarted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevBgInitRestarted.setStatus(
        ""
    )

sysdevBgInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 180)
)
sysdevBgInitFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevBgInitFailed.setStatus(
        ""
    )

sysdevBgInitCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 181)
)
sysdevBgInitCompleted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevBgInitCompleted.setStatus(
        ""
    )

sysdevDataLossLowBbuCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 182)
)
sysdevDataLossLowBbuCharge.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevDataLossLowBbuCharge.setStatus(
        ""
    )

fmtfanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 256)
)
fmtfanFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtfanFailed.setStatus(
        ""
    )

fmtfanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 257)
)
fmtfanOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtfanOk.setStatus(
        ""
    )

aemiFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 258)
)
aemiFanFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9FanUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    aemiFanFailed.setStatus(
        ""
    )

fmtfanNotpresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 259)
)
fmtfanNotpresent.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtfanNotpresent.setStatus(
        ""
    )

fmtpowerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 272)
)
fmtpowerFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtpowerFailed.setStatus(
        ""
    )

fmtpowerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 273)
)
fmtpowerOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtpowerOk.setStatus(
        ""
    )

aemiPwrSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 274)
)
aemiPwrSupplyFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9PowerSupplyUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    aemiPwrSupplyFailed.setStatus(
        ""
    )

fmtpowerNotpresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 275)
)
fmtpowerNotpresent.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtpowerNotpresent.setStatus(
        ""
    )

fmtheatBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 288)
)
fmtheatBad.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9HeatSensorUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtheatBad.setStatus(
        ""
    )

fmtheatCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 289)
)
fmtheatCritical.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtheatCritical.setStatus(
        ""
    )

fmtheatOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 290)
)
fmtheatOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtheatOk.setStatus(
        ""
    )

aemiOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 291)
)
aemiOverTemperature.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9HeatSensorUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    aemiOverTemperature.setStatus(
        ""
    )

fmtheatNotpresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 292)
)
fmtheatNotpresent.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtheatNotpresent.setStatus(
        ""
    )

fmtstwkFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 304)
)
fmtstwkFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtstwkFailed.setStatus(
        ""
    )

fmtstwkCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 305)
)
fmtstwkCritical.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtstwkCritical.setStatus(
        ""
    )

fmtstwkOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 306)
)
fmtstwkOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtstwkOk.setStatus(
        ""
    )

fmtUpsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 307)
)
fmtUpsDisabled.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtUpsDisabled.setStatus(
        ""
    )

fmtUpsAcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 308)
)
fmtUpsAcFail.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtUpsAcFail.setStatus(
        ""
    )

fmtUpsBatLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 309)
)
fmtUpsBatLow.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtUpsBatLow.setStatus(
        ""
    )

fmtUpsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 310)
)
fmtUpsFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtUpsFailed.setStatus(
        ""
    )

fmtUpsOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 311)
)
fmtUpsOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fmtUpsOk.setStatus(
        ""
    )

enclfanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 320)
)
enclfanFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclfanFailed.setStatus(
        ""
    )

enclfanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 321)
)
enclfanOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclfanOk.setStatus(
        ""
    )

enclfanNotpresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 322)
)
enclfanNotpresent.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclfanNotpresent.setStatus(
        ""
    )

enclpowerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 323)
)
enclpowerFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclpowerFailed.setStatus(
        ""
    )

enclpowerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 324)
)
enclpowerOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclpowerOk.setStatus(
        ""
    )

enclpowerNotpresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 325)
)
enclpowerNotpresent.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclpowerNotpresent.setStatus(
        ""
    )

enclheatBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 326)
)
enclheatBad.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclheatBad.setStatus(
        ""
    )

enclheatCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 327)
)
enclheatCritical.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclheatCritical.setStatus(
        ""
    )

enclheatOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 328)
)
enclheatOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclheatOk.setStatus(
        ""
    )

enclheatNotpresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 329)
)
enclheatNotpresent.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclheatNotpresent.setStatus(
        ""
    )

enclaccessCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 330)
)
enclaccessCritical.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclaccessCritical.setStatus(
        ""
    )

enclaccessOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 331)
)
enclaccessOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclaccessOk.setStatus(
        ""
    )

enclaccessOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 332)
)
enclaccessOffline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclaccessOffline.setStatus(
        ""
    )

enclsesSoftaddrOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 333)
)
enclsesSoftaddrOccurred.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclsesSoftaddrOccurred.setStatus(
        ""
    )

enclaccessReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 334)
)
enclaccessReady.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclaccessReady.setStatus(
        ""
    )

enclheatUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 335)
)
enclheatUnknown.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclheatUnknown.setStatus(
        ""
    )

enclpowerUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 336)
)
enclpowerUnknown.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclpowerUnknown.setStatus(
        ""
    )

enclfanUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 337)
)
enclfanUnknown.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclfanUnknown.setStatus(
        ""
    )

enclosureShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 338)
)
enclosureShutdown.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EnclosureUnitNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclosureShutdown.setStatus(
        ""
    )

enclcoldWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 339)
)
enclcoldWarn.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclcoldWarn.setStatus(
        ""
    )

enclcoldFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 340)
)
enclcoldFail.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9FmtCabinetNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    enclcoldFail.setStatus(
        ""
    )

systemStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 384)
)
systemStarted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    systemStarted.setStatus(
        ""
    )

ctldevWritebackError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 385)
)
ctldevWritebackError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevWritebackError.setStatus(
        ""
    )

ctldevStateTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 386)
)
ctldevStateTableFull.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevStateTableFull.setStatus(
        ""
    )

ctldevDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 388)
)
ctldevDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevDead.setStatus(
        ""
    )

ctldevReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 389)
)
ctldevReset.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevReset.setStatus(
        ""
    )

ctldevFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 390)
)
ctldevFound.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevFound.setStatus(
        ""
    )

ctldevGone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 391)
)
ctldevGone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevGone.setStatus(
        ""
    )

ctldevBbuFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 392)
)
ctldevBbuFound.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuFound.setStatus(
        ""
    )

ctldevBbuPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 393)
)
ctldevBbuPowerLow.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuPowerLow.setStatus(
        ""
    )

ctldevBbuPowerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 394)
)
ctldevBbuPowerOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuPowerOk.setStatus(
        ""
    )

ctldevPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 395)
)
ctldevPowerOff.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevPowerOff.setStatus(
        ""
    )

ctldevPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 396)
)
ctldevPowerOn.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevPowerOn.setStatus(
        ""
    )

ctldevOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 397)
)
ctldevOnline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevOnline.setStatus(
        ""
    )

ctldevOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 398)
)
ctldevOffline.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevOffline.setStatus(
        ""
    )

ctldevCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 399)
)
ctldevCritical.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevCritical.setStatus(
        ""
    )

ctldevBbuRecondStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 400)
)
ctldevBbuRecondStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuRecondStart.setStatus(
        ""
    )

ctldevBbuRecondDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 401)
)
ctldevBbuRecondDone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuRecondDone.setStatus(
        ""
    )

ctldevBbuRecondAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 402)
)
ctldevBbuRecondAbort.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuRecondAbort.setStatus(
        ""
    )

ctldevInstallationAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 403)
)
ctldevInstallationAborted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevInstallationAborted.setStatus(
        ""
    )

ctldevFirmwareMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 404)
)
ctldevFirmwareMismatch.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevFirmwareMismatch.setStatus(
        ""
    )

ctldevBbuNoresponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 405)
)
ctldevBbuNoresponse.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuNoresponse.setStatus(
        ""
    )

ctldevWarmBootError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 406)
)
ctldevWarmBootError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevWarmBootError.setStatus(
        ""
    )

ctldevBbuCalibrateStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 407)
)
ctldevBbuCalibrateStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuCalibrateStart.setStatus(
        ""
    )

ctldevBbuCalibrateDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 408)
)
ctldevBbuCalibrateDone.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuCalibrateDone.setStatus(
        ""
    )

ctldevBbuCalibrateAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 409)
)
ctldevBbuCalibrateAbort.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuCalibrateAbort.setStatus(
        ""
    )

ctldevBbuNoBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 410)
)
ctldevBbuNoBattery.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuNoBattery.setStatus(
        ""
    )

ctldevConservCacheMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 411)
)
ctldevConservCacheMode.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevConservCacheMode.setStatus(
        ""
    )

ctldevNormalCacheMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 412)
)
ctldevNormalCacheMode.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNormalCacheMode.setStatus(
        ""
    )

ctldevDevStartCmplt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 413)
)
ctldevDevStartCmplt.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevDevStartCmplt.setStatus(
        ""
    )

ctldevSoftEccCorrected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 414)
)
ctldevSoftEccCorrected.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevSoftEccCorrected.setStatus(
        ""
    )

ctldevHardEccCorrected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 415)
)
ctldevHardEccCorrected.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevHardEccCorrected.setStatus(
        ""
    )

ctldevBbuRecondNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 416)
)
ctldevBbuRecondNeeded.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuRecondNeeded.setStatus(
        ""
    )

ctldevRemovedPtnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 417)
)
ctldevRemovedPtnr.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevRemovedPtnr.setStatus(
        ""
    )

ctldevBbuOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 418)
)
ctldevBbuOutOfService.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuOutOfService.setStatus(
        ""
    )

ctldevUpdatePtnrStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 419)
)
ctldevUpdatePtnrStatus.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevUpdatePtnrStatus.setStatus(
        ""
    )

ctldevRelinquishPtnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 420)
)
ctldevRelinquishPtnr.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevRelinquishPtnr.setStatus(
        ""
    )

ctldevInsertedPtnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 421)
)
ctldevInsertedPtnr.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevInsertedPtnr.setStatus(
        ""
    )

ctldevDualEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 422)
)
ctldevDualEnabled.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevDualEnabled.setStatus(
        ""
    )

ctldevKillPtnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 423)
)
ctldevKillPtnr.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevKillPtnr.setStatus(
        ""
    )

ctldevNexus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 424)
)
ctldevNexus.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNexus.setStatus(
        ""
    )

ctldevBadBootromImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 425)
)
ctldevBadBootromImage.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBadBootromImage.setStatus(
        ""
    )

ctldevBadMacAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 426)
)
ctldevBadMacAddress.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBadMacAddress.setStatus(
        ""
    )

ctldevMirrorRaceRecoveryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 427)
)
ctldevMirrorRaceRecoveryFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevMirrorRaceRecoveryFailed.setStatus(
        ""
    )

ctldevMirrorCriticalDrive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 428)
)
ctldevMirrorCriticalDrive.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevMirrorCriticalDrive.setStatus(
        ""
    )

ctldevInCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 429)
)
ctldevInCluster.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevInCluster.setStatus(
        ""
    )

ctldevNotInCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 430)
)
ctldevNotInCluster.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNotInCluster.setStatus(
        ""
    )

sysdevDataLossImproperShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 431)
)
sysdevDataLossImproperShutdown.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sysdevDataLossImproperShutdown.setStatus(
        ""
    )

ctldevAutomaticFlashStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 432)
)
ctldevAutomaticFlashStarted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevAutomaticFlashStarted.setStatus(
        ""
    )

ctldevNegotiationFailedJumpers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 433)
)
ctldevNegotiationFailedJumpers.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNegotiationFailedJumpers.setStatus(
        ""
    )

ctldevNegotiationSameId = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 434)
)
ctldevNegotiationSameId.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNegotiationSameId.setStatus(
        ""
    )

ctldevNegotiationBoardType = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 435)
)
ctldevNegotiationBoardType.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNegotiationBoardType.setStatus(
        ""
    )

ctldevNegotiationDiskChannels = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 436)
)
ctldevNegotiationDiskChannels.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNegotiationDiskChannels.setStatus(
        ""
    )

ctldevNegotiationHostChannels = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 437)
)
ctldevNegotiationHostChannels.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNegotiationHostChannels.setStatus(
        ""
    )

ctldevNegotiationMemorySize = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 438)
)
ctldevNegotiationMemorySize.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNegotiationMemorySize.setStatus(
        ""
    )

ctldevNegotiationCacheSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 439)
)
ctldevNegotiationCacheSize.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevNegotiationCacheSize.setStatus(
        ""
    )

ctldevMirrorRaceTableError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 440)
)
ctldevMirrorRaceTableError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9LogicalDriveNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevMirrorRaceTableError.setStatus(
        ""
    )

ctldevStopRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 441)
)
ctldevStopRejected.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevStopRejected.setStatus(
        ""
    )

systemStartedNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 512)
)
systemStartedNew.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    systemStartedNew.setStatus(
        ""
    )

systemSizeTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 513)
)
systemSizeTableFull.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    systemSizeTableFull.setStatus(
        ""
    )

systemUserLoggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 514)
)
systemUserLoggedIn.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    systemUserLoggedIn.setStatus(
        ""
    )

systemUserLoggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 515)
)
systemUserLoggedOut.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    systemUserLoggedOut.setStatus(
        ""
    )

systemAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 516)
)
systemAlive.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    systemAlive.setStatus(
        ""
    )

systemDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 517)
)
systemDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    systemDead.setStatus(
        ""
    )

autobootChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 518)
)
autobootChanged.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    autobootChanged.setStatus(
        ""
    )

ctldevBbuBattTestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 519)
)
ctldevBbuBattTestStart.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuBattTestStart.setStatus(
        ""
    )

ctldevBbuBattTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 520)
)
ctldevBbuBattTestComplete.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuBattTestComplete.setStatus(
        ""
    )

ctldevBbuBattTestCanceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 521)
)
ctldevBbuBattTestCanceled.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuBattTestCanceled.setStatus(
        ""
    )

ctldevBbuBattTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 522)
)
ctldevBbuBattTestFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    ctldevBbuBattTestFailed.setStatus(
        ""
    )

channelFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 640)
)
channelFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    channelFailed.setStatus(
        ""
    )

channelOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 641)
)
channelOk.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    channelOk.setStatus(
        ""
    )

channelScsiBusDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 642)
)
channelScsiBusDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    channelScsiBusDead.setStatus(
        ""
    )

channelScsiBusAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 643)
)
channelScsiBusAlive.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    channelScsiBusAlive.setStatus(
        ""
    )

channelFiberDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 644)
)
channelFiberDead.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    channelFiberDead.setStatus(
        ""
    )

channelFiberAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 645)
)
channelFiberAlive.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    channelFiberAlive.setStatus(
        ""
    )

logEmpty = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 700)
)
logEmpty.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    logEmpty.setStatus(
        ""
    )

logOutSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 701)
)
logOutSync.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    logOutSync.setStatus(
        ""
    )

logRequestSense = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 702)
)
logRequestSense.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    logRequestSense.setStatus(
        ""
    )

logSetRtc = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 703)
)
logSetRtc.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    logSetRtc.setStatus(
        ""
    )

cfgNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 800)
)
cfgNew.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    cfgNew.setStatus(
        ""
    )

cfgClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 801)
)
cfgClear.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    cfgClear.setStatus(
        ""
    )

cfgInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 802)
)
cfgInvalid.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    cfgInvalid.setStatus(
        ""
    )

cfgCodAccessError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 803)
)
cfgCodAccessError.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    cfgCodAccessError.setStatus(
        ""
    )

cfgCodConverted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 804)
)
cfgCodConverted.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    cfgCodConverted.setStatus(
        ""
    )

cfgCodImportFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 805)
)
cfgCodImportFailed.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    cfgCodImportFailed.setStatus(
        ""
    )

debugDumpGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 806)
)
debugDumpGenerated.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    debugDumpGenerated.setStatus(
        ""
    )

debugDumpGeneratedPartner = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 807)
)
debugDumpGeneratedPartner.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    debugDumpGeneratedPartner.setStatus(
        ""
    )

cfgCodNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 808)
)
cfgCodNotFound.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    cfgCodNotFound.setStatus(
        ""
    )

cfgCodLunMapNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 809)
)
cfgCodLunMapNotFound.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    cfgCodLunMapNotFound.setStatus(
        ""
    )

fatalHang = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 896)
)
fatalHang.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9Lun"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fatalHang.setStatus(
        ""
    )

fatalBrkp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 897)
)
fatalBrkp.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9Lun"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    fatalBrkp.setStatus(
        ""
    )

i960HwErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 912)
)
i960HwErr.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9Lun"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    i960HwErr.setStatus(
        ""
    )

sarmHwErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 928)
)
sarmHwErr.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9Lun"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    sarmHwErr.setStatus(
        ""
    )

scsiHwErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 1, 1, 1, 9, 1, 0, 944)
)
scsiHwErr.setObjects(
      *(("MYLEXRAID-MIB", "a9EventCode"),
        ("MYLEXRAID-MIB", "a9ControllerNumber"),
        ("MYLEXRAID-MIB", "a9ChannelNumber"),
        ("MYLEXRAID-MIB", "a9TargetId"),
        ("MYLEXRAID-MIB", "a9Lun"),
        ("MYLEXRAID-MIB", "a9EventTimeStamp"))
)
if mibBuilder.loadTexts:
    scsiHwErr.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MYLEXRAID-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDate": DmiDate,
       "DmiComponentIndex": DmiComponentIndex,
       "mylex": mylex,
       "dmtfStd": dmtfStd,
       "dmtfComponents": dmtfComponents,
       "dmtfGroups": dmtfGroups,
       "tControllerInformation": tControllerInformation,
       "eControllerInformation": eControllerInformation,
       "a2ControllerNumber": a2ControllerNumber,
       "a2OperationalState": a2OperationalState,
       "a2FirmwareRevision": a2FirmwareRevision,
       "a2ConfiguredChannels": a2ConfiguredChannels,
       "a2ActualChannels": a2ActualChannels,
       "a2MaximumLogicalDrives": a2MaximumLogicalDrives,
       "a2MaximumTargetsPerChannel": a2MaximumTargetsPerChannel,
       "a2MaximumTaggedRequests": a2MaximumTaggedRequests,
       "a2MaximumDataTransferSizePerIoRequestInK": a2MaximumDataTransferSizePerIoRequestInK,
       "a2MaximumConcurrentCommands": a2MaximumConcurrentCommands,
       "a2RebuildRate": a2RebuildRate,
       "a2LogicalSectorSizeInBytes": a2LogicalSectorSizeInBytes,
       "a2PhysicalSectorSizeInBytes": a2PhysicalSectorSizeInBytes,
       "a2CacheLineSizeInBytes": a2CacheLineSizeInBytes,
       "a2CacheSizeInMb": a2CacheSizeInMb,
       "a2CacheMemoryType": a2CacheMemoryType,
       "a2EpromSizeInKb": a2EpromSizeInKb,
       "a2BusType": a2BusType,
       "a2ControllerClass": a2ControllerClass,
       "a2ControllerModel": a2ControllerModel,
       "a2SystemBusNumber": a2SystemBusNumber,
       "a2SlotNumber": a2SlotNumber,
       "a2InterruptVectorNumber": a2InterruptVectorNumber,
       "a2InterruptMode": a2InterruptMode,
       "a2NumberOfPhysicalDevices": a2NumberOfPhysicalDevices,
       "a2NumberOfPhysicalDevicesOffline": a2NumberOfPhysicalDevicesOffline,
       "a2NumberOfLogicalDevices": a2NumberOfLogicalDevices,
       "a2NumberOfLogicalDevicesCritical": a2NumberOfLogicalDevicesCritical,
       "a2NumberOfLogicalDevicesOffline": a2NumberOfLogicalDevicesOffline,
       "a2FaultManagementType": a2FaultManagementType,
       "a2ArrayInformation": a2ArrayInformation,
       "a2LogicalDriveReadRequests": a2LogicalDriveReadRequests,
       "a2DataReadFromLogicalDrivesInMb": a2DataReadFromLogicalDrivesInMb,
       "a2LogicalDriveWriteRequests": a2LogicalDriveWriteRequests,
       "a2DataWrittenToLogicalDrivesInMb": a2DataWrittenToLogicalDrivesInMb,
       "a2LogicalDrivesReadCacheHitPercentage": a2LogicalDrivesReadCacheHitPercentage,
       "a2PhysicalDriveReadRequests": a2PhysicalDriveReadRequests,
       "a2DataReadFromPhysicalDrivesInMb": a2DataReadFromPhysicalDrivesInMb,
       "a2PhysicalDriveWriteRequests": a2PhysicalDriveWriteRequests,
       "a2DataWrittenToPhysicalDrivesInMb": a2DataWrittenToPhysicalDrivesInMb,
       "a2StorageworksCabinetStatusOnChannel0": a2StorageworksCabinetStatusOnChannel0,
       "a2StorageworksCabinetStatusOnChannel1": a2StorageworksCabinetStatusOnChannel1,
       "a2StorageworksCabinetStatusOnChannel2": a2StorageworksCabinetStatusOnChannel2,
       "a2BatteryBackupUnitStatus": a2BatteryBackupUnitStatus,
       "a2PartnerControllerNumber": a2PartnerControllerNumber,
       "a2WwName": a2WwName,
       "a2HostControllerNumber": a2HostControllerNumber,
       "a2HostChannelNumber": a2HostChannelNumber,
       "a2HostTargetId": a2HostTargetId,
       "tLogicalDriveInformation": tLogicalDriveInformation,
       "eLogicalDriveInformation": eLogicalDriveInformation,
       "a3ControllerNumber": a3ControllerNumber,
       "a3LogicalDriveNumber": a3LogicalDriveNumber,
       "a3OperationalState": a3OperationalState,
       "a3RaidLevel": a3RaidLevel,
       "a3WritePolicy": a3WritePolicy,
       "a3SizeInMb": a3SizeInMb,
       "a3PhysicalSizeInMb": a3PhysicalSizeInMb,
       "a3StripeSizeInBytes": a3StripeSizeInBytes,
       "a3PhysicalDriveMap": a3PhysicalDriveMap,
       "a3ArrayList": a3ArrayList,
       "a3RaidLevelString": a3RaidLevelString,
       "tPhysicalDeviceInformation": tPhysicalDeviceInformation,
       "ePhysicalDeviceInformation": ePhysicalDeviceInformation,
       "a4ControllerNumber": a4ControllerNumber,
       "a4ChannelNumber": a4ChannelNumber,
       "a4TargetId": a4TargetId,
       "a4Lun": a4Lun,
       "a4OperationalState": a4OperationalState,
       "a4VendorId": a4VendorId,
       "a4ProductId": a4ProductId,
       "a4ProductRevisionLevel": a4ProductRevisionLevel,
       "a4SizeInMb": a4SizeInMb,
       "a4DeviceType": a4DeviceType,
       "a4SoftErrors": a4SoftErrors,
       "a4HardErrors": a4HardErrors,
       "a4ParityErrors": a4ParityErrors,
       "a4MiscErrors": a4MiscErrors,
       "a4ArrayList": a4ArrayList,
       "a4LogicalDriveList": a4LogicalDriveList,
       "a4BusSpeed": a4BusSpeed,
       "a4BusWidth": a4BusWidth,
       "a4CommandQueuing": a4CommandQueuing,
       "a4PfaErrors": a4PfaErrors,
       "tMylexDacManagementSoftware": tMylexDacManagementSoftware,
       "eMylexDacManagementSoftware": eMylexDacManagementSoftware,
       "a5ManagementSoftwareRevision": a5ManagementSoftwareRevision,
       "a5ManagementSoftwareBuildDate": a5ManagementSoftwareBuildDate,
       "a5MylexDacDeviceDriverRevision": a5MylexDacDeviceDriverRevision,
       "a5MylexDacDeviceDriverBuildDate": a5MylexDacDeviceDriverBuildDate,
       "a5GamDriverRevision": a5GamDriverRevision,
       "a5GamDriverBuildDate": a5GamDriverBuildDate,
       "tLogicalDriveStatistics": tLogicalDriveStatistics,
       "eLogicalDriveStatistics": eLogicalDriveStatistics,
       "a6ControllerNumber": a6ControllerNumber,
       "a6LogicalDriveNumber": a6LogicalDriveNumber,
       "a6ReadRequests": a6ReadRequests,
       "a6DataReadInMb": a6DataReadInMb,
       "a6WriteRequests": a6WriteRequests,
       "a6DataWrittenInMb": a6DataWrittenInMb,
       "a6ReadCacheHitPercentage": a6ReadCacheHitPercentage,
       "tPhysicalDriveStatistics": tPhysicalDriveStatistics,
       "ePhysicalDriveStatistics": ePhysicalDriveStatistics,
       "a7ControllerNumber": a7ControllerNumber,
       "a7ChannelNumber": a7ChannelNumber,
       "a7TargetId": a7TargetId,
       "a7Lun": a7Lun,
       "a7ReadRequests": a7ReadRequests,
       "a7DataReadInMb": a7DataReadInMb,
       "a7WriteRequests": a7WriteRequests,
       "a7DataWrittenInMb": a7DataWrittenInMb,
       "tFaultManagementCabinetInformation": tFaultManagementCabinetInformation,
       "eFaultManagementCabinetInformation": eFaultManagementCabinetInformation,
       "a8ControllerNumber": a8ControllerNumber,
       "a8ChannelNumber": a8ChannelNumber,
       "a8CabinetNumber": a8CabinetNumber,
       "a8TargetId": a8TargetId,
       "a8Lun": a8Lun,
       "a8CabinetType": a8CabinetType,
       "a8NumberOfFans": a8NumberOfFans,
       "a8NumberOfPowerSupplyUnits": a8NumberOfPowerSupplyUnits,
       "a8NumberOfHeatSensors": a8NumberOfHeatSensors,
       "a8NumberOfDriveSlots": a8NumberOfDriveSlots,
       "a8NumberOfDoorLocks": a8NumberOfDoorLocks,
       "a8NumberOfSpeakers": a8NumberOfSpeakers,
       "a8NumberOfFansCritical": a8NumberOfFansCritical,
       "a8NumberOfPowerSupplyUnitsCritical": a8NumberOfPowerSupplyUnitsCritical,
       "a8NumberOfHeatSensorsCritical": a8NumberOfHeatSensorsCritical,
       "a8NumberOfFansFailed": a8NumberOfFansFailed,
       "a8NumberOfPowerSupplyUnitsFailed": a8NumberOfPowerSupplyUnitsFailed,
       "a8NumberOfHeatSensorsFailed": a8NumberOfHeatSensorsFailed,
       "tMylexRaidEventInformation": tMylexRaidEventInformation,
       "eMylexRaidEventInformation": eMylexRaidEventInformation,
       "physdevOnline": physdevOnline,
       "physdevHotspare": physdevHotspare,
       "physdevHardError": physdevHardError,
       "physdevPfa": physdevPfa,
       "physdevAutoRebuildStart": physdevAutoRebuildStart,
       "physdevManualRebuildStart": physdevManualRebuildStart,
       "physdevRebuildDone": physdevRebuildDone,
       "physdevRebuildCanceled": physdevRebuildCanceled,
       "physdevRebuildError": physdevRebuildError,
       "physdevRebuildNewdevFailed": physdevRebuildNewdevFailed,
       "physdevRebuildSysdevFailed": physdevRebuildSysdevFailed,
       "physdevDead": physdevDead,
       "physdevFound": physdevFound,
       "physdevGone": physdevGone,
       "physdevUnconfigured": physdevUnconfigured,
       "physdevExpandcapacityStart": physdevExpandcapacityStart,
       "physdevExpandcapacityDone": physdevExpandcapacityDone,
       "physdevExpandcapacityError": physdevExpandcapacityError,
       "physdevCommandTimeout": physdevCommandTimeout,
       "physdevCommandAbort": physdevCommandAbort,
       "physdevCommandRetried": physdevCommandRetried,
       "physdevParityError": physdevParityError,
       "physdevSoftError": physdevSoftError,
       "physdevMiscError": physdevMiscError,
       "physdevReset": physdevReset,
       "physdevActivespare": physdevActivespare,
       "physdevWarmspare": physdevWarmspare,
       "physdevReqsense": physdevReqsense,
       "physdevInitStarted": physdevInitStarted,
       "physdevInitDone": physdevInitDone,
       "physdevInitFailed": physdevInitFailed,
       "physdevInitCanceled": physdevInitCanceled,
       "physdevWriterecDead": physdevWriterecDead,
       "physdevResetDead": physdevResetDead,
       "physdevDblccDead": physdevDblccDead,
       "physdevRemovedDead": physdevRemovedDead,
       "physdevGrosserrDead": physdevGrosserrDead,
       "physdevBadtagDead": physdevBadtagDead,
       "physdevScsitmoDead": physdevScsitmoDead,
       "physdevSysresetDead": physdevSysresetDead,
       "physdevBsyparDead": physdevBsyparDead,
       "physdevBycmdDead": physdevBycmdDead,
       "physdevSeltmoDead": physdevSeltmoDead,
       "physdevSeqerrDead": physdevSeqerrDead,
       "physdevUnknownstsDead": physdevUnknownstsDead,
       "physdevNotrdyDead": physdevNotrdyDead,
       "physdevMissingDead": physdevMissingDead,
       "physdevCodwrfailDead": physdevCodwrfailDead,
       "physdevBdtwrfailDead": physdevBdtwrfailDead,
       "physdevOffline": physdevOffline,
       "physdevStandby": physdevStandby,
       "physdevRebuild": physdevRebuild,
       "physdevIdMismatch": physdevIdMismatch,
       "physdevFailedStart": physdevFailedStart,
       "physdevOffsetSet": physdevOffsetSet,
       "physdevSetBusWidth": physdevSetBusWidth,
       "physdevMissingOnstartup": physdevMissingOnstartup,
       "physdevRebuildStartFailed": physdevRebuildStartFailed,
       "physdevMovingToOtherChn": physdevMovingToOtherChn,
       "physdevOfflineDeviceMadeOnline": physdevOfflineDeviceMadeOnline,
       "physdevStandbyRebuildStart": physdevStandbyRebuildStart,
       "physdevHotSpareSmaller": physdevHotSpareSmaller,
       "ppilotLogicalDiskOnline": ppilotLogicalDiskOnline,
       "ppilotLogicalDiskOffline": ppilotLogicalDiskOffline,
       "ppilotLogicalDiskPathFailover": ppilotLogicalDiskPathFailover,
       "ppilotLogicalDiskPathFailback": ppilotLogicalDiskPathFailback,
       "physdevNonRedundantAccess": physdevNonRedundantAccess,
       "physdevTypeInvalid": physdevTypeInvalid,
       "physdevSoftId": physdevSoftId,
       "physdevPortFailed": physdevPortFailed,
       "ctldevMirrorRaceEntryFailed": ctldevMirrorRaceEntryFailed,
       "ctldevCtrlParamsChecksumFailed": ctldevCtrlParamsChecksumFailed,
       "firmwareUpgradeStarted": firmwareUpgradeStarted,
       "firmwareUpgradeComplete": firmwareUpgradeComplete,
       "firmwareUpgradeFailed": firmwareUpgradeFailed,
       "fibredevLoopidSoftaddrOccurred": fibredevLoopidSoftaddrOccurred,
       "sysdevCheckStart": sysdevCheckStart,
       "sysdevCheckDone": sysdevCheckDone,
       "sysdevCheckCanceled": sysdevCheckCanceled,
       "sysdevCheckError": sysdevCheckError,
       "sysdevCheckSysdevFailed": sysdevCheckSysdevFailed,
       "sysdevCheckPhysdevFailed": sysdevCheckPhysdevFailed,
       "sysdevOffline": sysdevOffline,
       "sysdevCritical": sysdevCritical,
       "sysdevOnline": sysdevOnline,
       "sysdevAutoRebuildStart": sysdevAutoRebuildStart,
       "sysdevManualRebuildStart": sysdevManualRebuildStart,
       "sysdevRebuildDone": sysdevRebuildDone,
       "sysdevRebuildCanceled": sysdevRebuildCanceled,
       "sysdevRebuildError": sysdevRebuildError,
       "sysdevRebuildNewdevFailed": sysdevRebuildNewdevFailed,
       "sysdevRebuildSysdevFailed": sysdevRebuildSysdevFailed,
       "sysdevInitStarted": sysdevInitStarted,
       "sysdevInitDone": sysdevInitDone,
       "sysdevInitCanceled": sysdevInitCanceled,
       "sysdevInitFailed": sysdevInitFailed,
       "sysdevFound": sysdevFound,
       "sysdevGone": sysdevGone,
       "sysdevExpandcapacityStart": sysdevExpandcapacityStart,
       "sysdevExpandcapacityDone": sysdevExpandcapacityDone,
       "sysdevExpandcapacityError": sysdevExpandcapacityError,
       "sysdevBadblock": sysdevBadblock,
       "sysdevSizechanged": sysdevSizechanged,
       "sysdevTypechanged": sysdevTypechanged,
       "sysdevBaddatablock": sysdevBaddatablock,
       "sysdevWrLunMap": sysdevWrLunMap,
       "sysdevDatareadFromBlockInBdt": sysdevDatareadFromBlockInBdt,
       "sysdevDataForBlockLost": sysdevDataForBlockLost,
       "sysdevOfflineDeviceMadeAvailableWithDataloss": sysdevOfflineDeviceMadeAvailableWithDataloss,
       "sysdevOfflineDeviceMadeAvailable": sysdevOfflineDeviceMadeAvailable,
       "sysdevStandbyRebuildStart": sysdevStandbyRebuildStart,
       "sysdevBgInitStarted": sysdevBgInitStarted,
       "sysdevBgInitStopped": sysdevBgInitStopped,
       "sysdevBgInitPaused": sysdevBgInitPaused,
       "sysdevBgInitRestarted": sysdevBgInitRestarted,
       "sysdevBgInitFailed": sysdevBgInitFailed,
       "sysdevBgInitCompleted": sysdevBgInitCompleted,
       "sysdevDataLossLowBbuCharge": sysdevDataLossLowBbuCharge,
       "fmtfanFailed": fmtfanFailed,
       "fmtfanOk": fmtfanOk,
       "aemiFanFailed": aemiFanFailed,
       "fmtfanNotpresent": fmtfanNotpresent,
       "fmtpowerFailed": fmtpowerFailed,
       "fmtpowerOk": fmtpowerOk,
       "aemiPwrSupplyFailed": aemiPwrSupplyFailed,
       "fmtpowerNotpresent": fmtpowerNotpresent,
       "fmtheatBad": fmtheatBad,
       "fmtheatCritical": fmtheatCritical,
       "fmtheatOk": fmtheatOk,
       "aemiOverTemperature": aemiOverTemperature,
       "fmtheatNotpresent": fmtheatNotpresent,
       "fmtstwkFailed": fmtstwkFailed,
       "fmtstwkCritical": fmtstwkCritical,
       "fmtstwkOk": fmtstwkOk,
       "fmtUpsDisabled": fmtUpsDisabled,
       "fmtUpsAcFail": fmtUpsAcFail,
       "fmtUpsBatLow": fmtUpsBatLow,
       "fmtUpsFailed": fmtUpsFailed,
       "fmtUpsOk": fmtUpsOk,
       "enclfanFailed": enclfanFailed,
       "enclfanOk": enclfanOk,
       "enclfanNotpresent": enclfanNotpresent,
       "enclpowerFailed": enclpowerFailed,
       "enclpowerOk": enclpowerOk,
       "enclpowerNotpresent": enclpowerNotpresent,
       "enclheatBad": enclheatBad,
       "enclheatCritical": enclheatCritical,
       "enclheatOk": enclheatOk,
       "enclheatNotpresent": enclheatNotpresent,
       "enclaccessCritical": enclaccessCritical,
       "enclaccessOk": enclaccessOk,
       "enclaccessOffline": enclaccessOffline,
       "enclsesSoftaddrOccurred": enclsesSoftaddrOccurred,
       "enclaccessReady": enclaccessReady,
       "enclheatUnknown": enclheatUnknown,
       "enclpowerUnknown": enclpowerUnknown,
       "enclfanUnknown": enclfanUnknown,
       "enclosureShutdown": enclosureShutdown,
       "enclcoldWarn": enclcoldWarn,
       "enclcoldFail": enclcoldFail,
       "systemStarted": systemStarted,
       "ctldevWritebackError": ctldevWritebackError,
       "ctldevStateTableFull": ctldevStateTableFull,
       "ctldevDead": ctldevDead,
       "ctldevReset": ctldevReset,
       "ctldevFound": ctldevFound,
       "ctldevGone": ctldevGone,
       "ctldevBbuFound": ctldevBbuFound,
       "ctldevBbuPowerLow": ctldevBbuPowerLow,
       "ctldevBbuPowerOk": ctldevBbuPowerOk,
       "ctldevPowerOff": ctldevPowerOff,
       "ctldevPowerOn": ctldevPowerOn,
       "ctldevOnline": ctldevOnline,
       "ctldevOffline": ctldevOffline,
       "ctldevCritical": ctldevCritical,
       "ctldevBbuRecondStart": ctldevBbuRecondStart,
       "ctldevBbuRecondDone": ctldevBbuRecondDone,
       "ctldevBbuRecondAbort": ctldevBbuRecondAbort,
       "ctldevInstallationAborted": ctldevInstallationAborted,
       "ctldevFirmwareMismatch": ctldevFirmwareMismatch,
       "ctldevBbuNoresponse": ctldevBbuNoresponse,
       "ctldevWarmBootError": ctldevWarmBootError,
       "ctldevBbuCalibrateStart": ctldevBbuCalibrateStart,
       "ctldevBbuCalibrateDone": ctldevBbuCalibrateDone,
       "ctldevBbuCalibrateAbort": ctldevBbuCalibrateAbort,
       "ctldevBbuNoBattery": ctldevBbuNoBattery,
       "ctldevConservCacheMode": ctldevConservCacheMode,
       "ctldevNormalCacheMode": ctldevNormalCacheMode,
       "ctldevDevStartCmplt": ctldevDevStartCmplt,
       "ctldevSoftEccCorrected": ctldevSoftEccCorrected,
       "ctldevHardEccCorrected": ctldevHardEccCorrected,
       "ctldevBbuRecondNeeded": ctldevBbuRecondNeeded,
       "ctldevRemovedPtnr": ctldevRemovedPtnr,
       "ctldevBbuOutOfService": ctldevBbuOutOfService,
       "ctldevUpdatePtnrStatus": ctldevUpdatePtnrStatus,
       "ctldevRelinquishPtnr": ctldevRelinquishPtnr,
       "ctldevInsertedPtnr": ctldevInsertedPtnr,
       "ctldevDualEnabled": ctldevDualEnabled,
       "ctldevKillPtnr": ctldevKillPtnr,
       "ctldevNexus": ctldevNexus,
       "ctldevBadBootromImage": ctldevBadBootromImage,
       "ctldevBadMacAddress": ctldevBadMacAddress,
       "ctldevMirrorRaceRecoveryFailed": ctldevMirrorRaceRecoveryFailed,
       "ctldevMirrorCriticalDrive": ctldevMirrorCriticalDrive,
       "ctldevInCluster": ctldevInCluster,
       "ctldevNotInCluster": ctldevNotInCluster,
       "sysdevDataLossImproperShutdown": sysdevDataLossImproperShutdown,
       "ctldevAutomaticFlashStarted": ctldevAutomaticFlashStarted,
       "ctldevNegotiationFailedJumpers": ctldevNegotiationFailedJumpers,
       "ctldevNegotiationSameId": ctldevNegotiationSameId,
       "ctldevNegotiationBoardType": ctldevNegotiationBoardType,
       "ctldevNegotiationDiskChannels": ctldevNegotiationDiskChannels,
       "ctldevNegotiationHostChannels": ctldevNegotiationHostChannels,
       "ctldevNegotiationMemorySize": ctldevNegotiationMemorySize,
       "ctldevNegotiationCacheSize": ctldevNegotiationCacheSize,
       "ctldevMirrorRaceTableError": ctldevMirrorRaceTableError,
       "ctldevStopRejected": ctldevStopRejected,
       "systemStartedNew": systemStartedNew,
       "systemSizeTableFull": systemSizeTableFull,
       "systemUserLoggedIn": systemUserLoggedIn,
       "systemUserLoggedOut": systemUserLoggedOut,
       "systemAlive": systemAlive,
       "systemDead": systemDead,
       "autobootChanged": autobootChanged,
       "ctldevBbuBattTestStart": ctldevBbuBattTestStart,
       "ctldevBbuBattTestComplete": ctldevBbuBattTestComplete,
       "ctldevBbuBattTestCanceled": ctldevBbuBattTestCanceled,
       "ctldevBbuBattTestFailed": ctldevBbuBattTestFailed,
       "channelFailed": channelFailed,
       "channelOk": channelOk,
       "channelScsiBusDead": channelScsiBusDead,
       "channelScsiBusAlive": channelScsiBusAlive,
       "channelFiberDead": channelFiberDead,
       "channelFiberAlive": channelFiberAlive,
       "logEmpty": logEmpty,
       "logOutSync": logOutSync,
       "logRequestSense": logRequestSense,
       "logSetRtc": logSetRtc,
       "cfgNew": cfgNew,
       "cfgClear": cfgClear,
       "cfgInvalid": cfgInvalid,
       "cfgCodAccessError": cfgCodAccessError,
       "cfgCodConverted": cfgCodConverted,
       "cfgCodImportFailed": cfgCodImportFailed,
       "debugDumpGenerated": debugDumpGenerated,
       "debugDumpGeneratedPartner": debugDumpGeneratedPartner,
       "cfgCodNotFound": cfgCodNotFound,
       "cfgCodLunMapNotFound": cfgCodLunMapNotFound,
       "fatalHang": fatalHang,
       "fatalBrkp": fatalBrkp,
       "i960HwErr": i960HwErr,
       "sarmHwErr": sarmHwErr,
       "scsiHwErr": scsiHwErr,
       "a9EventTableIndex": a9EventTableIndex,
       "a9EventCode": a9EventCode,
       "a9EventTimeStamp": a9EventTimeStamp,
       "a9ControllerNumber": a9ControllerNumber,
       "a9ChannelNumber": a9ChannelNumber,
       "a9TargetId": a9TargetId,
       "a9Lun": a9Lun,
       "a9LogicalDriveNumber": a9LogicalDriveNumber,
       "a9FmtCabinetNumber": a9FmtCabinetNumber,
       "a9FanUnitNumber": a9FanUnitNumber,
       "a9PowerSupplyUnitNumber": a9PowerSupplyUnitNumber,
       "a9HeatSensorUnitNumber": a9HeatSensorUnitNumber,
       "a9EnclosureUnitNumber": a9EnclosureUnitNumber,
       "tBatteryBackupUnitInformation": tBatteryBackupUnitInformation,
       "eBatteryBackupUnitInformation": eBatteryBackupUnitInformation,
       "a10ControllerNumber": a10ControllerNumber,
       "a10OperationalState": a10OperationalState,
       "a10BatteryType": a10BatteryType,
       "a10CurrentPowerInHours": a10CurrentPowerInHours,
       "a10MaximumPowerInHours": a10MaximumPowerInHours,
       "a10ThresholdValueInHours": a10ThresholdValueInHours,
       "a10ChargeLevelInPercentage": a10ChargeLevelInPercentage,
       "a10Version": a10Version,
       "a10OperationalStateString": a10OperationalStateString}
)
