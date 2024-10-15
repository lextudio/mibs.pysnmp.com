# SNMP MIB module (MYLEXDAC960SCSIRAIDCONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MYLEXDAC960SCSIRAIDCONTROLLER-MIB
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



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDateX(OctetString):
    """Custom type DmiDateX based on OctetString"""
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
_Mib_ObjectIdentity = ObjectIdentity
mib = _Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1608, 3)
)
_V2_ObjectIdentity = ObjectIdentity
v2 = _V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")
_A1Verify_Type = DmiInteger
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TControllerInformation_Object = MibTable
tControllerInformation = _TControllerInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tControllerInformation.setStatus("mandatory")
_EControllerInformation_Object = MibTableRow
eControllerInformation = _EControllerInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1)
)
eControllerInformation.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a2ControllerNumber"),
)
if mibBuilder.loadTexts:
    eControllerInformation.setStatus("mandatory")
_A2ControllerNumber_Type = DmiInteger
_A2ControllerNumber_Object = MibTableColumn
a2ControllerNumber = _A2ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 1),
    _A2ControllerNumber_Type()
)
a2ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ControllerNumber.setStatus("mandatory")
_A2OperationalState_Type = DmiInteger
_A2OperationalState_Object = MibTableColumn
a2OperationalState = _A2OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 2),
    _A2OperationalState_Type()
)
a2OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2OperationalState.setStatus("mandatory")
_A2FirmwareRevision_Type = DmiDisplaystring
_A2FirmwareRevision_Object = MibTableColumn
a2FirmwareRevision = _A2FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 3),
    _A2FirmwareRevision_Type()
)
a2FirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2FirmwareRevision.setStatus("mandatory")
_A2ConfiguredChannels_Type = DmiInteger
_A2ConfiguredChannels_Object = MibTableColumn
a2ConfiguredChannels = _A2ConfiguredChannels_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 4),
    _A2ConfiguredChannels_Type()
)
a2ConfiguredChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ConfiguredChannels.setStatus("mandatory")
_A2ActualChannels_Type = DmiInteger
_A2ActualChannels_Object = MibTableColumn
a2ActualChannels = _A2ActualChannels_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 5),
    _A2ActualChannels_Type()
)
a2ActualChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ActualChannels.setStatus("mandatory")
_A2MaximumLogicalDrives_Type = DmiInteger
_A2MaximumLogicalDrives_Object = MibTableColumn
a2MaximumLogicalDrives = _A2MaximumLogicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 6),
    _A2MaximumLogicalDrives_Type()
)
a2MaximumLogicalDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumLogicalDrives.setStatus("mandatory")
_A2MaximumTargetsPerChannel_Type = DmiInteger
_A2MaximumTargetsPerChannel_Object = MibTableColumn
a2MaximumTargetsPerChannel = _A2MaximumTargetsPerChannel_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 7),
    _A2MaximumTargetsPerChannel_Type()
)
a2MaximumTargetsPerChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumTargetsPerChannel.setStatus("mandatory")
_A2MaximumTaggedRequests_Type = DmiInteger
_A2MaximumTaggedRequests_Object = MibTableColumn
a2MaximumTaggedRequests = _A2MaximumTaggedRequests_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 8),
    _A2MaximumTaggedRequests_Type()
)
a2MaximumTaggedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumTaggedRequests.setStatus("mandatory")
_A2MaximumDataTransferSizePerIoRequestInK_Type = DmiInteger
_A2MaximumDataTransferSizePerIoRequestInK_Object = MibTableColumn
a2MaximumDataTransferSizePerIoRequestInK = _A2MaximumDataTransferSizePerIoRequestInK_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 9),
    _A2MaximumDataTransferSizePerIoRequestInK_Type()
)
a2MaximumDataTransferSizePerIoRequestInK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumDataTransferSizePerIoRequestInK.setStatus("mandatory")
_A2MaximumConcurrentCommands_Type = DmiInteger
_A2MaximumConcurrentCommands_Object = MibTableColumn
a2MaximumConcurrentCommands = _A2MaximumConcurrentCommands_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 10),
    _A2MaximumConcurrentCommands_Type()
)
a2MaximumConcurrentCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MaximumConcurrentCommands.setStatus("mandatory")
_A2RebuildRate_Type = DmiInteger
_A2RebuildRate_Object = MibTableColumn
a2RebuildRate = _A2RebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 11),
    _A2RebuildRate_Type()
)
a2RebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2RebuildRate.setStatus("mandatory")
_A2LogicalSectorSizeInBytes_Type = DmiInteger
_A2LogicalSectorSizeInBytes_Object = MibTableColumn
a2LogicalSectorSizeInBytes = _A2LogicalSectorSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 12),
    _A2LogicalSectorSizeInBytes_Type()
)
a2LogicalSectorSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2LogicalSectorSizeInBytes.setStatus("mandatory")
_A2PhysicalSectorSizeInBytes_Type = DmiInteger
_A2PhysicalSectorSizeInBytes_Object = MibTableColumn
a2PhysicalSectorSizeInBytes = _A2PhysicalSectorSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 13),
    _A2PhysicalSectorSizeInBytes_Type()
)
a2PhysicalSectorSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2PhysicalSectorSizeInBytes.setStatus("mandatory")
_A2CacheLineSizeInBytes_Type = DmiInteger
_A2CacheLineSizeInBytes_Object = MibTableColumn
a2CacheLineSizeInBytes = _A2CacheLineSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 14),
    _A2CacheLineSizeInBytes_Type()
)
a2CacheLineSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2CacheLineSizeInBytes.setStatus("mandatory")
_A2DramSizeInMb_Type = DmiInteger
_A2DramSizeInMb_Object = MibTableColumn
a2DramSizeInMb = _A2DramSizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 15),
    _A2DramSizeInMb_Type()
)
a2DramSizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2DramSizeInMb.setStatus("mandatory")
_A2EpromSizeInKb_Type = DmiInteger
_A2EpromSizeInKb_Object = MibTableColumn
a2EpromSizeInKb = _A2EpromSizeInKb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 16),
    _A2EpromSizeInKb_Type()
)
a2EpromSizeInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2EpromSizeInKb.setStatus("mandatory")
_A2BusType_Type = DmiDisplaystring
_A2BusType_Object = MibTableColumn
a2BusType = _A2BusType_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 17),
    _A2BusType_Type()
)
a2BusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2BusType.setStatus("mandatory")
_A2SystemBusNumber_Type = DmiInteger
_A2SystemBusNumber_Object = MibTableColumn
a2SystemBusNumber = _A2SystemBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 18),
    _A2SystemBusNumber_Type()
)
a2SystemBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2SystemBusNumber.setStatus("mandatory")
_A2SlotNumber_Type = DmiInteger
_A2SlotNumber_Object = MibTableColumn
a2SlotNumber = _A2SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 19),
    _A2SlotNumber_Type()
)
a2SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2SlotNumber.setStatus("mandatory")
_A2InterruptVectorNumber_Type = DmiInteger
_A2InterruptVectorNumber_Object = MibTableColumn
a2InterruptVectorNumber = _A2InterruptVectorNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 20),
    _A2InterruptVectorNumber_Type()
)
a2InterruptVectorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2InterruptVectorNumber.setStatus("mandatory")
_A2InterruptMode_Type = DmiDisplaystring
_A2InterruptMode_Object = MibTableColumn
a2InterruptMode = _A2InterruptMode_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 2, 1, 21),
    _A2InterruptMode_Type()
)
a2InterruptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2InterruptMode.setStatus("mandatory")
_TLogicalDriveInformation_Object = MibTable
tLogicalDriveInformation = _TLogicalDriveInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tLogicalDriveInformation.setStatus("mandatory")
_ELogicalDriveInformation_Object = MibTableRow
eLogicalDriveInformation = _ELogicalDriveInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3, 1)
)
eLogicalDriveInformation.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a3ControllerNumber"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a3LogicalDriveNumber"),
)
if mibBuilder.loadTexts:
    eLogicalDriveInformation.setStatus("mandatory")
_A3ControllerNumber_Type = DmiInteger
_A3ControllerNumber_Object = MibTableColumn
a3ControllerNumber = _A3ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3, 1, 1),
    _A3ControllerNumber_Type()
)
a3ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ControllerNumber.setStatus("mandatory")
_A3LogicalDriveNumber_Type = DmiInteger
_A3LogicalDriveNumber_Object = MibTableColumn
a3LogicalDriveNumber = _A3LogicalDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3, 1, 2),
    _A3LogicalDriveNumber_Type()
)
a3LogicalDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3LogicalDriveNumber.setStatus("mandatory")
_A3OperationalState_Type = DmiInteger
_A3OperationalState_Object = MibTableColumn
a3OperationalState = _A3OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3, 1, 3),
    _A3OperationalState_Type()
)
a3OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperationalState.setStatus("mandatory")
_A3RaidLevel_Type = DmiInteger
_A3RaidLevel_Object = MibTableColumn
a3RaidLevel = _A3RaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3, 1, 4),
    _A3RaidLevel_Type()
)
a3RaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3RaidLevel.setStatus("mandatory")
_A3WritePolicy_Type = DmiDisplaystring
_A3WritePolicy_Object = MibTableColumn
a3WritePolicy = _A3WritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3, 1, 5),
    _A3WritePolicy_Type()
)
a3WritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3WritePolicy.setStatus("mandatory")
_A3SizeInMb_Type = DmiInteger
_A3SizeInMb_Object = MibTableColumn
a3SizeInMb = _A3SizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3, 1, 6),
    _A3SizeInMb_Type()
)
a3SizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3SizeInMb.setStatus("mandatory")
_A3StripeSizeInBytes_Type = DmiInteger
_A3StripeSizeInBytes_Object = MibTableColumn
a3StripeSizeInBytes = _A3StripeSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3, 1, 7),
    _A3StripeSizeInBytes_Type()
)
a3StripeSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3StripeSizeInBytes.setStatus("mandatory")
_A3PhysicalDriveMap_Type = DmiDisplaystring
_A3PhysicalDriveMap_Object = MibTableColumn
a3PhysicalDriveMap = _A3PhysicalDriveMap_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 3, 1, 8),
    _A3PhysicalDriveMap_Type()
)
a3PhysicalDriveMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3PhysicalDriveMap.setStatus("mandatory")
_TPhyicalDeviceInformation_Object = MibTable
tPhyicalDeviceInformation = _TPhyicalDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tPhyicalDeviceInformation.setStatus("mandatory")
_EPhyicalDeviceInformation_Object = MibTableRow
ePhyicalDeviceInformation = _EPhyicalDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1)
)
ePhyicalDeviceInformation.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a4ControllerNumber"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a4ScsiBusId"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a4ScsiTargetId"),
)
if mibBuilder.loadTexts:
    ePhyicalDeviceInformation.setStatus("mandatory")
_A4ControllerNumber_Type = DmiInteger
_A4ControllerNumber_Object = MibTableColumn
a4ControllerNumber = _A4ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 1),
    _A4ControllerNumber_Type()
)
a4ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ControllerNumber.setStatus("mandatory")
_A4ScsiBusId_Type = DmiInteger
_A4ScsiBusId_Object = MibTableColumn
a4ScsiBusId = _A4ScsiBusId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 2),
    _A4ScsiBusId_Type()
)
a4ScsiBusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ScsiBusId.setStatus("mandatory")
_A4ScsiTargetId_Type = DmiInteger
_A4ScsiTargetId_Object = MibTableColumn
a4ScsiTargetId = _A4ScsiTargetId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 3),
    _A4ScsiTargetId_Type()
)
a4ScsiTargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ScsiTargetId.setStatus("mandatory")
_A4OperationalState_Type = DmiInteger
_A4OperationalState_Object = MibTableColumn
a4OperationalState = _A4OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 4),
    _A4OperationalState_Type()
)
a4OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4OperationalState.setStatus("mandatory")
_A4VendorId_Type = DmiDisplaystring
_A4VendorId_Object = MibTableColumn
a4VendorId = _A4VendorId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 5),
    _A4VendorId_Type()
)
a4VendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4VendorId.setStatus("mandatory")
_A4ProductId_Type = DmiDisplaystring
_A4ProductId_Object = MibTableColumn
a4ProductId = _A4ProductId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 6),
    _A4ProductId_Type()
)
a4ProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ProductId.setStatus("mandatory")
_A4ProductRevisionLevel_Type = DmiDisplaystring
_A4ProductRevisionLevel_Object = MibTableColumn
a4ProductRevisionLevel = _A4ProductRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 7),
    _A4ProductRevisionLevel_Type()
)
a4ProductRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ProductRevisionLevel.setStatus("mandatory")
_A4SizeInMb_Type = DmiInteger
_A4SizeInMb_Object = MibTableColumn
a4SizeInMb = _A4SizeInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 8),
    _A4SizeInMb_Type()
)
a4SizeInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4SizeInMb.setStatus("mandatory")
_A4DeviceType_Type = DmiDisplaystring
_A4DeviceType_Object = MibTableColumn
a4DeviceType = _A4DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 9),
    _A4DeviceType_Type()
)
a4DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4DeviceType.setStatus("mandatory")
_A4SoftErrorsCount_Type = DmiCounter
_A4SoftErrorsCount_Object = MibTableColumn
a4SoftErrorsCount = _A4SoftErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 10),
    _A4SoftErrorsCount_Type()
)
a4SoftErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4SoftErrorsCount.setStatus("mandatory")
_A4HardErrorsCount_Type = DmiCounter
_A4HardErrorsCount_Object = MibTableColumn
a4HardErrorsCount = _A4HardErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 11),
    _A4HardErrorsCount_Type()
)
a4HardErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4HardErrorsCount.setStatus("mandatory")
_A4ParityErrorsCount_Type = DmiCounter
_A4ParityErrorsCount_Object = MibTableColumn
a4ParityErrorsCount = _A4ParityErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 12),
    _A4ParityErrorsCount_Type()
)
a4ParityErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ParityErrorsCount.setStatus("mandatory")
_A4MiscErrorsCount_Type = DmiCounter
_A4MiscErrorsCount_Object = MibTableColumn
a4MiscErrorsCount = _A4MiscErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 4, 1, 13),
    _A4MiscErrorsCount_Type()
)
a4MiscErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4MiscErrorsCount.setStatus("mandatory")
_TMylexDac960ComponentInstrumentationInfo_Object = MibTable
tMylexDac960ComponentInstrumentationInfo = _TMylexDac960ComponentInstrumentationInfo_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tMylexDac960ComponentInstrumentationInfo.setStatus("mandatory")
_EMylexDac960ComponentInstrumentationInfo_Object = MibTableRow
eMylexDac960ComponentInstrumentationInfo = _EMylexDac960ComponentInstrumentationInfo_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 5, 1)
)
eMylexDac960ComponentInstrumentationInfo.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMylexDac960ComponentInstrumentationInfo.setStatus("mandatory")
_A5CiRevision_Type = DmiDisplaystring
_A5CiRevision_Object = MibTableColumn
a5CiRevision = _A5CiRevision_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 5, 1, 1),
    _A5CiRevision_Type()
)
a5CiRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5CiRevision.setStatus("mandatory")
_A5CiBuildDate_Type = DmiDisplaystring
_A5CiBuildDate_Object = MibTableColumn
a5CiBuildDate = _A5CiBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 5, 1, 2),
    _A5CiBuildDate_Type()
)
a5CiBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5CiBuildDate.setStatus("mandatory")
_A5MdacDeviceDriverRevision_Type = DmiDisplaystring
_A5MdacDeviceDriverRevision_Object = MibTableColumn
a5MdacDeviceDriverRevision = _A5MdacDeviceDriverRevision_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 5, 1, 3),
    _A5MdacDeviceDriverRevision_Type()
)
a5MdacDeviceDriverRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5MdacDeviceDriverRevision.setStatus("mandatory")
_A5MdacDeviceDriverBuildDate_Type = DmiDisplaystring
_A5MdacDeviceDriverBuildDate_Object = MibTableColumn
a5MdacDeviceDriverBuildDate = _A5MdacDeviceDriverBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 5, 1, 4),
    _A5MdacDeviceDriverBuildDate_Type()
)
a5MdacDeviceDriverBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5MdacDeviceDriverBuildDate.setStatus("mandatory")
_TLogicalDriveStatistics_Object = MibTable
tLogicalDriveStatistics = _TLogicalDriveStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tLogicalDriveStatistics.setStatus("mandatory")
_ELogicalDriveStatistics_Object = MibTableRow
eLogicalDriveStatistics = _ELogicalDriveStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 6, 1)
)
eLogicalDriveStatistics.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a6ControllerNumber"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a6LogicalDriveNumber"),
)
if mibBuilder.loadTexts:
    eLogicalDriveStatistics.setStatus("mandatory")
_A6ControllerNumber_Type = DmiInteger
_A6ControllerNumber_Object = MibTableColumn
a6ControllerNumber = _A6ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 6, 1, 1),
    _A6ControllerNumber_Type()
)
a6ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ControllerNumber.setStatus("mandatory")
_A6LogicalDriveNumber_Type = DmiInteger
_A6LogicalDriveNumber_Object = MibTableColumn
a6LogicalDriveNumber = _A6LogicalDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 6, 1, 2),
    _A6LogicalDriveNumber_Type()
)
a6LogicalDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6LogicalDriveNumber.setStatus("mandatory")
_A6ReadRequestsCount_Type = DmiCounter
_A6ReadRequestsCount_Object = MibTableColumn
a6ReadRequestsCount = _A6ReadRequestsCount_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 6, 1, 3),
    _A6ReadRequestsCount_Type()
)
a6ReadRequestsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ReadRequestsCount.setStatus("mandatory")
_A6AmountOfDataReadInMb_Type = DmiCounter
_A6AmountOfDataReadInMb_Object = MibTableColumn
a6AmountOfDataReadInMb = _A6AmountOfDataReadInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 6, 1, 4),
    _A6AmountOfDataReadInMb_Type()
)
a6AmountOfDataReadInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6AmountOfDataReadInMb.setStatus("mandatory")
_A6WriteRequestsCount_Type = DmiCounter
_A6WriteRequestsCount_Object = MibTableColumn
a6WriteRequestsCount = _A6WriteRequestsCount_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 6, 1, 5),
    _A6WriteRequestsCount_Type()
)
a6WriteRequestsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6WriteRequestsCount.setStatus("mandatory")
_A6AmountOfDataWrittenInMb_Type = DmiCounter
_A6AmountOfDataWrittenInMb_Object = MibTableColumn
a6AmountOfDataWrittenInMb = _A6AmountOfDataWrittenInMb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 6, 1, 6),
    _A6AmountOfDataWrittenInMb_Type()
)
a6AmountOfDataWrittenInMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6AmountOfDataWrittenInMb.setStatus("mandatory")
_A6ReadCacheHit_Type = DmiCounter
_A6ReadCacheHit_Object = MibTableColumn
a6ReadCacheHit = _A6ReadCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 6, 1, 7),
    _A6ReadCacheHit_Type()
)
a6ReadCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ReadCacheHit.setStatus("mandatory")
_TPhysicalDriveStatistics_Object = MibTable
tPhysicalDriveStatistics = _TPhysicalDriveStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tPhysicalDriveStatistics.setStatus("mandatory")
_EPhysicalDriveStatistics_Object = MibTableRow
ePhysicalDriveStatistics = _EPhysicalDriveStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 7, 1)
)
ePhysicalDriveStatistics.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a7ControllerNumber"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a7ScsiBusId"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a7ScsiTargetId"),
)
if mibBuilder.loadTexts:
    ePhysicalDriveStatistics.setStatus("mandatory")
_A7ControllerNumber_Type = DmiInteger
_A7ControllerNumber_Object = MibTableColumn
a7ControllerNumber = _A7ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 7, 1, 1),
    _A7ControllerNumber_Type()
)
a7ControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ControllerNumber.setStatus("mandatory")
_A7ScsiBusId_Type = DmiInteger
_A7ScsiBusId_Object = MibTableColumn
a7ScsiBusId = _A7ScsiBusId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 7, 1, 2),
    _A7ScsiBusId_Type()
)
a7ScsiBusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ScsiBusId.setStatus("mandatory")
_A7ScsiTargetId_Type = DmiInteger
_A7ScsiTargetId_Object = MibTableColumn
a7ScsiTargetId = _A7ScsiTargetId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 7, 1, 3),
    _A7ScsiTargetId_Type()
)
a7ScsiTargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ScsiTargetId.setStatus("mandatory")
_A7ReadRequestsCount_Type = DmiCounter
_A7ReadRequestsCount_Object = MibTableColumn
a7ReadRequestsCount = _A7ReadRequestsCount_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 7, 1, 4),
    _A7ReadRequestsCount_Type()
)
a7ReadRequestsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ReadRequestsCount.setStatus("mandatory")
_A7AmountOfDataReadInKb_Type = DmiCounter
_A7AmountOfDataReadInKb_Object = MibTableColumn
a7AmountOfDataReadInKb = _A7AmountOfDataReadInKb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 7, 1, 5),
    _A7AmountOfDataReadInKb_Type()
)
a7AmountOfDataReadInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7AmountOfDataReadInKb.setStatus("mandatory")
_A7WriteRequestsCount_Type = DmiCounter
_A7WriteRequestsCount_Object = MibTableColumn
a7WriteRequestsCount = _A7WriteRequestsCount_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 7, 1, 6),
    _A7WriteRequestsCount_Type()
)
a7WriteRequestsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7WriteRequestsCount.setStatus("mandatory")
_A7AmountOfDataWrittenInKb_Type = DmiCounter
_A7AmountOfDataWrittenInKb_Object = MibTableColumn
a7AmountOfDataWrittenInKb = _A7AmountOfDataWrittenInKb_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 7, 1, 7),
    _A7AmountOfDataWrittenInKb_Type()
)
a7AmountOfDataWrittenInKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7AmountOfDataWrittenInKb.setStatus("mandatory")
_TErrorControl_Object = MibTable
tErrorControl = _TErrorControl_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 98)
)
if mibBuilder.loadTexts:
    tErrorControl.setStatus("mandatory")
_EErrorControl_Object = MibTableRow
eErrorControl = _EErrorControl_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 98, 1)
)
eErrorControl.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a98Selfid"),
)
if mibBuilder.loadTexts:
    eErrorControl.setStatus("mandatory")
_A98Selfid_Type = DmiInteger
_A98Selfid_Object = MibTableColumn
a98Selfid = _A98Selfid_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 98, 1, 1),
    _A98Selfid_Type()
)
a98Selfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a98Selfid.setStatus("mandatory")
_A98NumberOfFatalErrors_Type = DmiCounter
_A98NumberOfFatalErrors_Object = MibTableColumn
a98NumberOfFatalErrors = _A98NumberOfFatalErrors_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 98, 1, 2),
    _A98NumberOfFatalErrors_Type()
)
a98NumberOfFatalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a98NumberOfFatalErrors.setStatus("mandatory")
_A98NumberOfMajorErrors_Type = DmiCounter
_A98NumberOfMajorErrors_Object = MibTableColumn
a98NumberOfMajorErrors = _A98NumberOfMajorErrors_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 98, 1, 3),
    _A98NumberOfMajorErrors_Type()
)
a98NumberOfMajorErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a98NumberOfMajorErrors.setStatus("mandatory")
_A98NumberOfWarnings_Type = DmiCounter
_A98NumberOfWarnings_Object = MibTableColumn
a98NumberOfWarnings = _A98NumberOfWarnings_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 98, 1, 4),
    _A98NumberOfWarnings_Type()
)
a98NumberOfWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a98NumberOfWarnings.setStatus("mandatory")


class _A98ErrorStatus_Type(Integer32):
    """Custom type a98ErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("vFatal", 3),
          ("vInformational", 4),
          ("vMajor", 2),
          ("vOk", 0),
          ("vWarning", 1))
    )


_A98ErrorStatus_Type.__name__ = "Integer32"
_A98ErrorStatus_Object = MibTableColumn
a98ErrorStatus = _A98ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 98, 1, 5),
    _A98ErrorStatus_Type()
)
a98ErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a98ErrorStatus.setStatus("mandatory")


class _A98ErrorStatusType_Type(Integer32):
    """Custom type a98ErrorStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDiagnosticTest", 2),
          ("vPost", 0),
          ("vRuntime", 1))
    )


_A98ErrorStatusType_Type.__name__ = "Integer32"
_A98ErrorStatusType_Object = MibTableColumn
a98ErrorStatusType = _A98ErrorStatusType_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 98, 1, 6),
    _A98ErrorStatusType_Type()
)
a98ErrorStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a98ErrorStatusType.setStatus("mandatory")


class _A98AlarmGeneration_Type(Integer32):
    """Custom type a98AlarmGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A98AlarmGeneration_Type.__name__ = "Integer32"
_A98AlarmGeneration_Object = MibTableColumn
a98AlarmGeneration = _A98AlarmGeneration_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 98, 1, 7),
    _A98AlarmGeneration_Type()
)
a98AlarmGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a98AlarmGeneration.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99MibName_Type = DmiDisplaystring
_A99MibName_Object = MibTableColumn
a99MibName = _A99MibName_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 99, 1, 1),
    _A99MibName_Type()
)
a99MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibName.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTrap_Type = DmiInteger
_A99DisableTrap_Object = MibTableColumn
a99DisableTrap = _A99DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 99, 1, 3),
    _A99DisableTrap_Type()
)
a99DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a99DisableTrap.setStatus("mandatory")
_TTrapGroup_Object = MibTable
tTrapGroup = _TTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999)
)
if mibBuilder.loadTexts:
    tTrapGroup.setStatus("mandatory")
_ETrapGroup_Object = MibTableRow
eTrapGroup = _ETrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1)
)
eTrapGroup.setIndexNames(
    (0, "MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eTrapGroup.setStatus("mandatory")
_A9999ErrorTime_Type = DisplayString
_A9999ErrorTime_Object = MibTableColumn
a9999ErrorTime = _A9999ErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 1),
    _A9999ErrorTime_Type()
)
a9999ErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorTime.setStatus("mandatory")
_A9999ErrorStatus_Type = DmiInteger
_A9999ErrorStatus_Object = MibTableColumn
a9999ErrorStatus = _A9999ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 2),
    _A9999ErrorStatus_Type()
)
a9999ErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorStatus.setStatus("mandatory")
_A9999ErrorGroupId_Type = DmiInteger
_A9999ErrorGroupId_Object = MibTableColumn
a9999ErrorGroupId = _A9999ErrorGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 3),
    _A9999ErrorGroupId_Type()
)
a9999ErrorGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorGroupId.setStatus("mandatory")
_A9999ErrorInstanceId_Type = DmiInteger
_A9999ErrorInstanceId_Object = MibTableColumn
a9999ErrorInstanceId = _A9999ErrorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 4),
    _A9999ErrorInstanceId_Type()
)
a9999ErrorInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorInstanceId.setStatus("mandatory")
_A9999ComponentId_Type = DmiInteger
_A9999ComponentId_Object = MibTableColumn
a9999ComponentId = _A9999ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 5),
    _A9999ComponentId_Type()
)
a9999ComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ComponentId.setStatus("mandatory")
_A9999GroupId_Type = DmiInteger
_A9999GroupId_Object = MibTableColumn
a9999GroupId = _A9999GroupId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 6),
    _A9999GroupId_Type()
)
a9999GroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999GroupId.setStatus("mandatory")
_A9999InstanceId_Type = DmiInteger
_A9999InstanceId_Object = MibTableColumn
a9999InstanceId = _A9999InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 7),
    _A9999InstanceId_Type()
)
a9999InstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999InstanceId.setStatus("mandatory")
_A9999VendorCode1_Type = DmiInteger
_A9999VendorCode1_Object = MibTableColumn
a9999VendorCode1 = _A9999VendorCode1_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 8),
    _A9999VendorCode1_Type()
)
a9999VendorCode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode1.setStatus("mandatory")
_A9999VendorCode2_Type = DmiInteger
_A9999VendorCode2_Object = MibTableColumn
a9999VendorCode2 = _A9999VendorCode2_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 9),
    _A9999VendorCode2_Type()
)
a9999VendorCode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode2.setStatus("mandatory")
_A9999VendorText_Type = OctetString
_A9999VendorText_Object = MibTableColumn
a9999VendorText = _A9999VendorText_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 10),
    _A9999VendorText_Type()
)
a9999VendorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorText.setStatus("mandatory")
_A9999ParentGroupId_Type = DmiInteger
_A9999ParentGroupId_Object = MibTableColumn
a9999ParentGroupId = _A9999ParentGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 11),
    _A9999ParentGroupId_Type()
)
a9999ParentGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentGroupId.setStatus("mandatory")
_A9999ParentInstanceId_Type = DmiInteger
_A9999ParentInstanceId_Object = MibTableColumn
a9999ParentInstanceId = _A9999ParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 12),
    _A9999ParentInstanceId_Type()
)
a9999ParentInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentInstanceId.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mdacEventError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1608, 3, 2, 1, 9999, 1, 0, 1)
)
mdacEventError.setObjects(
      *(("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999ErrorTime"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999ErrorStatus"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999ErrorGroupId"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999ErrorInstanceId"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999ComponentId"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999GroupId"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999InstanceId"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999VendorCode1"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999VendorCode2"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999VendorText"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999ParentGroupId"),
        ("MYLEXDAC960SCSIRAIDCONTROLLER-MIB", "a9999ParentInstanceId"))
)
if mibBuilder.loadTexts:
    mdacEventError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MYLEXDAC960SCSIRAIDCONTROLLER-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "mylex": mylex,
       "mib": mib,
       "v2": v2,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
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
       "a2DramSizeInMb": a2DramSizeInMb,
       "a2EpromSizeInKb": a2EpromSizeInKb,
       "a2BusType": a2BusType,
       "a2SystemBusNumber": a2SystemBusNumber,
       "a2SlotNumber": a2SlotNumber,
       "a2InterruptVectorNumber": a2InterruptVectorNumber,
       "a2InterruptMode": a2InterruptMode,
       "tLogicalDriveInformation": tLogicalDriveInformation,
       "eLogicalDriveInformation": eLogicalDriveInformation,
       "a3ControllerNumber": a3ControllerNumber,
       "a3LogicalDriveNumber": a3LogicalDriveNumber,
       "a3OperationalState": a3OperationalState,
       "a3RaidLevel": a3RaidLevel,
       "a3WritePolicy": a3WritePolicy,
       "a3SizeInMb": a3SizeInMb,
       "a3StripeSizeInBytes": a3StripeSizeInBytes,
       "a3PhysicalDriveMap": a3PhysicalDriveMap,
       "tPhyicalDeviceInformation": tPhyicalDeviceInformation,
       "ePhyicalDeviceInformation": ePhyicalDeviceInformation,
       "a4ControllerNumber": a4ControllerNumber,
       "a4ScsiBusId": a4ScsiBusId,
       "a4ScsiTargetId": a4ScsiTargetId,
       "a4OperationalState": a4OperationalState,
       "a4VendorId": a4VendorId,
       "a4ProductId": a4ProductId,
       "a4ProductRevisionLevel": a4ProductRevisionLevel,
       "a4SizeInMb": a4SizeInMb,
       "a4DeviceType": a4DeviceType,
       "a4SoftErrorsCount": a4SoftErrorsCount,
       "a4HardErrorsCount": a4HardErrorsCount,
       "a4ParityErrorsCount": a4ParityErrorsCount,
       "a4MiscErrorsCount": a4MiscErrorsCount,
       "tMylexDac960ComponentInstrumentationInfo": tMylexDac960ComponentInstrumentationInfo,
       "eMylexDac960ComponentInstrumentationInfo": eMylexDac960ComponentInstrumentationInfo,
       "a5CiRevision": a5CiRevision,
       "a5CiBuildDate": a5CiBuildDate,
       "a5MdacDeviceDriverRevision": a5MdacDeviceDriverRevision,
       "a5MdacDeviceDriverBuildDate": a5MdacDeviceDriverBuildDate,
       "tLogicalDriveStatistics": tLogicalDriveStatistics,
       "eLogicalDriveStatistics": eLogicalDriveStatistics,
       "a6ControllerNumber": a6ControllerNumber,
       "a6LogicalDriveNumber": a6LogicalDriveNumber,
       "a6ReadRequestsCount": a6ReadRequestsCount,
       "a6AmountOfDataReadInMb": a6AmountOfDataReadInMb,
       "a6WriteRequestsCount": a6WriteRequestsCount,
       "a6AmountOfDataWrittenInMb": a6AmountOfDataWrittenInMb,
       "a6ReadCacheHit": a6ReadCacheHit,
       "tPhysicalDriveStatistics": tPhysicalDriveStatistics,
       "ePhysicalDriveStatistics": ePhysicalDriveStatistics,
       "a7ControllerNumber": a7ControllerNumber,
       "a7ScsiBusId": a7ScsiBusId,
       "a7ScsiTargetId": a7ScsiTargetId,
       "a7ReadRequestsCount": a7ReadRequestsCount,
       "a7AmountOfDataReadInKb": a7AmountOfDataReadInKb,
       "a7WriteRequestsCount": a7WriteRequestsCount,
       "a7AmountOfDataWrittenInKb": a7AmountOfDataWrittenInKb,
       "tErrorControl": tErrorControl,
       "eErrorControl": eErrorControl,
       "a98Selfid": a98Selfid,
       "a98NumberOfFatalErrors": a98NumberOfFatalErrors,
       "a98NumberOfMajorErrors": a98NumberOfMajorErrors,
       "a98NumberOfWarnings": a98NumberOfWarnings,
       "a98ErrorStatus": a98ErrorStatus,
       "a98ErrorStatusType": a98ErrorStatusType,
       "a98AlarmGeneration": a98AlarmGeneration,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99MibName": a99MibName,
       "a99MibOid": a99MibOid,
       "a99DisableTrap": a99DisableTrap,
       "tTrapGroup": tTrapGroup,
       "eTrapGroup": eTrapGroup,
       "mdacEventError": mdacEventError,
       "a9999ErrorTime": a9999ErrorTime,
       "a9999ErrorStatus": a9999ErrorStatus,
       "a9999ErrorGroupId": a9999ErrorGroupId,
       "a9999ErrorInstanceId": a9999ErrorInstanceId,
       "a9999ComponentId": a9999ComponentId,
       "a9999GroupId": a9999GroupId,
       "a9999InstanceId": a9999InstanceId,
       "a9999VendorCode1": a9999VendorCode1,
       "a9999VendorCode2": a9999VendorCode2,
       "a9999VendorText": a9999VendorText,
       "a9999ParentGroupId": a9999ParentGroupId,
       "a9999ParentInstanceId": a9999ParentInstanceId}
)
