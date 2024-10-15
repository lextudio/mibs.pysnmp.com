# SNMP MIB module (TRIPPLITE-PRODUCTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRIPPLITE-PRODUCTS
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:48 2024
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tripplite,) = mibBuilder.importSymbols(
    "TRIPPLITE",
    "tripplite")


# MODULE-IDENTITY

tlpProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1)
)
tlpProducts.setRevisions(
        ("2016-06-22 11:15",
         "2016-02-02 11:15",
         "2016-01-25 12:30",
         "2016-01-20 12:00",
         "2016-01-08 11:40",
         "2015-11-25 13:00",
         "2015-11-10 13:00",
         "2015-10-16 12:30",
         "2015-08-19 12:00",
         "2014-12-04 10:00",
         "2014-04-14 09:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TlpHardware_ObjectIdentity = ObjectIdentity
tlpHardware = _TlpHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1)
)
_TlpDevice_ObjectIdentity = ObjectIdentity
tlpDevice = _TlpDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1)
)
_TlpDeviceNumDevices_Type = Unsigned32
_TlpDeviceNumDevices_Object = MibScalar
tlpDeviceNumDevices = _TlpDeviceNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 1),
    _TlpDeviceNumDevices_Type()
)
tlpDeviceNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceNumDevices.setStatus("current")
_TlpDeviceTable_Object = MibTable
tlpDeviceTable = _TlpDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tlpDeviceTable.setStatus("current")
_TlpDeviceEntry_Object = MibTableRow
tlpDeviceEntry = _TlpDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1)
)
tlpDeviceEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpDeviceEntry.setStatus("current")
_TlpDeviceIndex_Type = Unsigned32
_TlpDeviceIndex_Object = MibTableColumn
tlpDeviceIndex = _TlpDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 1),
    _TlpDeviceIndex_Type()
)
tlpDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIndex.setStatus("current")
_TlpDeviceRowStatus_Type = RowStatus
_TlpDeviceRowStatus_Object = MibTableColumn
tlpDeviceRowStatus = _TlpDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 2),
    _TlpDeviceRowStatus_Type()
)
tlpDeviceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceRowStatus.setStatus("current")
_TlpDeviceType_Type = ObjectIdentifier
_TlpDeviceType_Object = MibTableColumn
tlpDeviceType = _TlpDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 3),
    _TlpDeviceType_Type()
)
tlpDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceType.setStatus("current")
_TlpDeviceManufacturer_Type = DisplayString
_TlpDeviceManufacturer_Object = MibTableColumn
tlpDeviceManufacturer = _TlpDeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 4),
    _TlpDeviceManufacturer_Type()
)
tlpDeviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceManufacturer.setStatus("current")
_TlpDeviceModel_Type = DisplayString
_TlpDeviceModel_Object = MibTableColumn
tlpDeviceModel = _TlpDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 5),
    _TlpDeviceModel_Type()
)
tlpDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceModel.setStatus("current")
_TlpDeviceName_Type = DisplayString
_TlpDeviceName_Object = MibTableColumn
tlpDeviceName = _TlpDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 6),
    _TlpDeviceName_Type()
)
tlpDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceName.setStatus("current")


class _TlpDeviceID_Type(Integer32):
    """Custom type tlpDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TlpDeviceID_Type.__name__ = "Integer32"
_TlpDeviceID_Object = MibTableColumn
tlpDeviceID = _TlpDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 7),
    _TlpDeviceID_Type()
)
tlpDeviceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceID.setStatus("current")
_TlpDeviceLocation_Type = DisplayString
_TlpDeviceLocation_Object = MibTableColumn
tlpDeviceLocation = _TlpDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 8),
    _TlpDeviceLocation_Type()
)
tlpDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceLocation.setStatus("current")
_TlpDeviceRegion_Type = DisplayString
_TlpDeviceRegion_Object = MibTableColumn
tlpDeviceRegion = _TlpDeviceRegion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 9),
    _TlpDeviceRegion_Type()
)
tlpDeviceRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceRegion.setStatus("current")


class _TlpDeviceStatus_Type(Integer32):
    """Custom type tlpDeviceStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 7),
          ("critical", 1),
          ("custom", 6),
          ("info", 3),
          ("none", 0),
          ("offline", 5),
          ("status", 4),
          ("warning", 2))
    )


_TlpDeviceStatus_Type.__name__ = "Integer32"
_TlpDeviceStatus_Object = MibTableColumn
tlpDeviceStatus = _TlpDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2, 1, 10),
    _TlpDeviceStatus_Type()
)
tlpDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceStatus.setStatus("current")
_TlpDeviceDetail_ObjectIdentity = ObjectIdentity
tlpDeviceDetail = _TlpDeviceDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2)
)
_TlpDeviceIdentTable_Object = MibTable
tlpDeviceIdentTable = _TlpDeviceIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tlpDeviceIdentTable.setStatus("current")
_TlpDeviceIdentEntry_Object = MibTableRow
tlpDeviceIdentEntry = _TlpDeviceIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1)
)
tlpDeviceIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpDeviceIdentEntry.setStatus("current")
_TlpDeviceIdentProtocol_Type = DisplayString
_TlpDeviceIdentProtocol_Object = MibTableColumn
tlpDeviceIdentProtocol = _TlpDeviceIdentProtocol_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 1),
    _TlpDeviceIdentProtocol_Type()
)
tlpDeviceIdentProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentProtocol.setStatus("current")


class _TlpDeviceIdentCommPortType_Type(Integer32):
    """Custom type tlpDeviceIdentCommPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hid", 3),
          ("serial", 1),
          ("simulated", 4),
          ("unittest", 5),
          ("unknown", 0),
          ("usb", 2))
    )


_TlpDeviceIdentCommPortType_Type.__name__ = "Integer32"
_TlpDeviceIdentCommPortType_Object = MibTableColumn
tlpDeviceIdentCommPortType = _TlpDeviceIdentCommPortType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 2),
    _TlpDeviceIdentCommPortType_Type()
)
tlpDeviceIdentCommPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentCommPortType.setStatus("current")
_TlpDeviceIdentCommPortName_Type = DisplayString
_TlpDeviceIdentCommPortName_Object = MibTableColumn
tlpDeviceIdentCommPortName = _TlpDeviceIdentCommPortName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 3),
    _TlpDeviceIdentCommPortName_Type()
)
tlpDeviceIdentCommPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentCommPortName.setStatus("current")
_TlpDeviceIdentFirmwareVersion_Type = DisplayString
_TlpDeviceIdentFirmwareVersion_Object = MibTableColumn
tlpDeviceIdentFirmwareVersion = _TlpDeviceIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 4),
    _TlpDeviceIdentFirmwareVersion_Type()
)
tlpDeviceIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentFirmwareVersion.setStatus("current")
_TlpDeviceIdentSerialNum_Type = DisplayString
_TlpDeviceIdentSerialNum_Object = MibTableColumn
tlpDeviceIdentSerialNum = _TlpDeviceIdentSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 5),
    _TlpDeviceIdentSerialNum_Type()
)
tlpDeviceIdentSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentSerialNum.setStatus("current")
_TlpDeviceIdentDateInstalled_Type = DisplayString
_TlpDeviceIdentDateInstalled_Object = MibTableColumn
tlpDeviceIdentDateInstalled = _TlpDeviceIdentDateInstalled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 6),
    _TlpDeviceIdentDateInstalled_Type()
)
tlpDeviceIdentDateInstalled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpDeviceIdentDateInstalled.setStatus("current")
_TlpDeviceIdentHardwareVersion_Type = DisplayString
_TlpDeviceIdentHardwareVersion_Object = MibTableColumn
tlpDeviceIdentHardwareVersion = _TlpDeviceIdentHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 7),
    _TlpDeviceIdentHardwareVersion_Type()
)
tlpDeviceIdentHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentHardwareVersion.setStatus("current")
_TlpDeviceIdentCurrentUptime_Type = DisplayString
_TlpDeviceIdentCurrentUptime_Object = MibTableColumn
tlpDeviceIdentCurrentUptime = _TlpDeviceIdentCurrentUptime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 8),
    _TlpDeviceIdentCurrentUptime_Type()
)
tlpDeviceIdentCurrentUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentCurrentUptime.setStatus("current")
_TlpDeviceIdentTotalUptime_Type = DisplayString
_TlpDeviceIdentTotalUptime_Object = MibTableColumn
tlpDeviceIdentTotalUptime = _TlpDeviceIdentTotalUptime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1, 1, 9),
    _TlpDeviceIdentTotalUptime_Type()
)
tlpDeviceIdentTotalUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpDeviceIdentTotalUptime.setStatus("current")
_TlpDeviceTypes_ObjectIdentity = ObjectIdentity
tlpDeviceTypes = _TlpDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3)
)
_TlpUps_ObjectIdentity = ObjectIdentity
tlpUps = _TlpUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1)
)
_TlpUpsIdent_ObjectIdentity = ObjectIdentity
tlpUpsIdent = _TlpUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1)
)
_TlpUpsIdentNumUps_Type = Unsigned32
_TlpUpsIdentNumUps_Object = MibScalar
tlpUpsIdentNumUps = _TlpUpsIdentNumUps_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 1),
    _TlpUpsIdentNumUps_Type()
)
tlpUpsIdentNumUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumUps.setStatus("current")
_TlpUpsIdentTable_Object = MibTable
tlpUpsIdentTable = _TlpUpsIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tlpUpsIdentTable.setStatus("current")
_TlpUpsIdentEntry_Object = MibTableRow
tlpUpsIdentEntry = _TlpUpsIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1)
)
tlpUpsIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsIdentEntry.setStatus("current")
_TlpUpsIdentNumInputs_Type = Unsigned32
_TlpUpsIdentNumInputs_Object = MibTableColumn
tlpUpsIdentNumInputs = _TlpUpsIdentNumInputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 1),
    _TlpUpsIdentNumInputs_Type()
)
tlpUpsIdentNumInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumInputs.setStatus("current")
_TlpUpsIdentNumOutputs_Type = Unsigned32
_TlpUpsIdentNumOutputs_Object = MibTableColumn
tlpUpsIdentNumOutputs = _TlpUpsIdentNumOutputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 2),
    _TlpUpsIdentNumOutputs_Type()
)
tlpUpsIdentNumOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumOutputs.setStatus("current")
_TlpUpsIdentNumBypass_Type = Unsigned32
_TlpUpsIdentNumBypass_Object = MibTableColumn
tlpUpsIdentNumBypass = _TlpUpsIdentNumBypass_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 3),
    _TlpUpsIdentNumBypass_Type()
)
tlpUpsIdentNumBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumBypass.setStatus("current")
_TlpUpsIdentNumPhases_Type = Unsigned32
_TlpUpsIdentNumPhases_Object = MibTableColumn
tlpUpsIdentNumPhases = _TlpUpsIdentNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 4),
    _TlpUpsIdentNumPhases_Type()
)
tlpUpsIdentNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumPhases.setStatus("current")
_TlpUpsIdentNumOutlets_Type = Unsigned32
_TlpUpsIdentNumOutlets_Object = MibTableColumn
tlpUpsIdentNumOutlets = _TlpUpsIdentNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 5),
    _TlpUpsIdentNumOutlets_Type()
)
tlpUpsIdentNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumOutlets.setStatus("current")
_TlpUpsIdentNumOutletGroups_Type = Unsigned32
_TlpUpsIdentNumOutletGroups_Object = MibTableColumn
tlpUpsIdentNumOutletGroups = _TlpUpsIdentNumOutletGroups_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 6),
    _TlpUpsIdentNumOutletGroups_Type()
)
tlpUpsIdentNumOutletGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumOutletGroups.setStatus("current")
_TlpUpsIdentNumBatteryPacks_Type = Unsigned32
_TlpUpsIdentNumBatteryPacks_Object = MibTableColumn
tlpUpsIdentNumBatteryPacks = _TlpUpsIdentNumBatteryPacks_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 2, 1, 7),
    _TlpUpsIdentNumBatteryPacks_Type()
)
tlpUpsIdentNumBatteryPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsIdentNumBatteryPacks.setStatus("current")
_TlpUpsSupportsTable_Object = MibTable
tlpUpsSupportsTable = _TlpUpsSupportsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tlpUpsSupportsTable.setStatus("current")
_TlpUpsSupportsEntry_Object = MibTableRow
tlpUpsSupportsEntry = _TlpUpsSupportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1)
)
tlpUpsSupportsEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsSupportsEntry.setStatus("current")
_TlpUpsSupportsEnergywise_Type = TruthValue
_TlpUpsSupportsEnergywise_Object = MibTableColumn
tlpUpsSupportsEnergywise = _TlpUpsSupportsEnergywise_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 1),
    _TlpUpsSupportsEnergywise_Type()
)
tlpUpsSupportsEnergywise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsEnergywise.setStatus("current")
_TlpUpsSupportsRampShed_Type = TruthValue
_TlpUpsSupportsRampShed_Object = MibTableColumn
tlpUpsSupportsRampShed = _TlpUpsSupportsRampShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 2),
    _TlpUpsSupportsRampShed_Type()
)
tlpUpsSupportsRampShed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsRampShed.setStatus("current")
_TlpUpsSupportsOutletGroup_Type = TruthValue
_TlpUpsSupportsOutletGroup_Object = MibTableColumn
tlpUpsSupportsOutletGroup = _TlpUpsSupportsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 3),
    _TlpUpsSupportsOutletGroup_Type()
)
tlpUpsSupportsOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsOutletGroup.setStatus("current")
_TlpUpsSupportsOutletCurrentPower_Type = TruthValue
_TlpUpsSupportsOutletCurrentPower_Object = MibTableColumn
tlpUpsSupportsOutletCurrentPower = _TlpUpsSupportsOutletCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 4),
    _TlpUpsSupportsOutletCurrentPower_Type()
)
tlpUpsSupportsOutletCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsOutletCurrentPower.setStatus("current")
_TlpUpsSupportsOutletVoltage_Type = TruthValue
_TlpUpsSupportsOutletVoltage_Object = MibTableColumn
tlpUpsSupportsOutletVoltage = _TlpUpsSupportsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 1, 3, 1, 5),
    _TlpUpsSupportsOutletVoltage_Type()
)
tlpUpsSupportsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSupportsOutletVoltage.setStatus("current")
_TlpUpsDevice_ObjectIdentity = ObjectIdentity
tlpUpsDevice = _TlpUpsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2)
)
_TlpUpsDeviceTable_Object = MibTable
tlpUpsDeviceTable = _TlpUpsDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tlpUpsDeviceTable.setStatus("current")
_TlpUpsDeviceEntry_Object = MibTableRow
tlpUpsDeviceEntry = _TlpUpsDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1)
)
tlpUpsDeviceEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsDeviceEntry.setStatus("current")


class _TlpUpsDeviceMainLoadState_Type(Integer32):
    """Custom type tlpUpsDeviceMainLoadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlpUpsDeviceMainLoadState_Type.__name__ = "Integer32"
_TlpUpsDeviceMainLoadState_Object = MibTableColumn
tlpUpsDeviceMainLoadState = _TlpUpsDeviceMainLoadState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 1),
    _TlpUpsDeviceMainLoadState_Type()
)
tlpUpsDeviceMainLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceMainLoadState.setStatus("current")
_TlpUpsDeviceMainLoadControllable_Type = TruthValue
_TlpUpsDeviceMainLoadControllable_Object = MibTableColumn
tlpUpsDeviceMainLoadControllable = _TlpUpsDeviceMainLoadControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 2),
    _TlpUpsDeviceMainLoadControllable_Type()
)
tlpUpsDeviceMainLoadControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceMainLoadControllable.setStatus("current")


class _TlpUpsDeviceMainLoadCommand_Type(Integer32):
    """Custom type tlpUpsDeviceMainLoadCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlpUpsDeviceMainLoadCommand_Type.__name__ = "Integer32"
_TlpUpsDeviceMainLoadCommand_Object = MibTableColumn
tlpUpsDeviceMainLoadCommand = _TlpUpsDeviceMainLoadCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 3),
    _TlpUpsDeviceMainLoadCommand_Type()
)
tlpUpsDeviceMainLoadCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsDeviceMainLoadCommand.setStatus("current")
_TlpUpsDevicePowerOnDelay_Type = Integer32
_TlpUpsDevicePowerOnDelay_Object = MibTableColumn
tlpUpsDevicePowerOnDelay = _TlpUpsDevicePowerOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 4),
    _TlpUpsDevicePowerOnDelay_Type()
)
tlpUpsDevicePowerOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsDevicePowerOnDelay.setStatus("current")
_TlpUpsDeviceTestDate_Type = DisplayString
_TlpUpsDeviceTestDate_Object = MibTableColumn
tlpUpsDeviceTestDate = _TlpUpsDeviceTestDate_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 5),
    _TlpUpsDeviceTestDate_Type()
)
tlpUpsDeviceTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceTestDate.setStatus("current")


class _TlpUpsDeviceTestResultsStatus_Type(Integer32):
    """Custom type tlpUpsDeviceTestResultsStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 4),
          ("badBattery", 7),
          ("batteryFailed", 9),
          ("doneAndError", 3),
          ("doneAndPassed", 1),
          ("doneAndWarning", 2),
          ("inProgress", 5),
          ("noTest", 0),
          ("noTestInitiated", 6),
          ("overCurrent", 8))
    )


_TlpUpsDeviceTestResultsStatus_Type.__name__ = "Integer32"
_TlpUpsDeviceTestResultsStatus_Object = MibTableColumn
tlpUpsDeviceTestResultsStatus = _TlpUpsDeviceTestResultsStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 6),
    _TlpUpsDeviceTestResultsStatus_Type()
)
tlpUpsDeviceTestResultsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceTestResultsStatus.setStatus("current")
_TlpUpsDeviceTemperatureC_Type = Integer32
_TlpUpsDeviceTemperatureC_Object = MibTableColumn
tlpUpsDeviceTemperatureC = _TlpUpsDeviceTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 7),
    _TlpUpsDeviceTemperatureC_Type()
)
tlpUpsDeviceTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsDeviceTemperatureC.setUnits("degrees Centigrade")
_TlpUpsDeviceTemperatureF_Type = Integer32
_TlpUpsDeviceTemperatureF_Object = MibTableColumn
tlpUpsDeviceTemperatureF = _TlpUpsDeviceTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 2, 1, 1, 8),
    _TlpUpsDeviceTemperatureF_Type()
)
tlpUpsDeviceTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsDeviceTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsDeviceTemperatureF.setUnits("degrees Farenheit")
_TlpUpsDetail_ObjectIdentity = ObjectIdentity
tlpUpsDetail = _TlpUpsDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3)
)
_TlpUpsBattery_ObjectIdentity = ObjectIdentity
tlpUpsBattery = _TlpUpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1)
)
_TlpUpsBatterySummaryTable_Object = MibTable
tlpUpsBatterySummaryTable = _TlpUpsBatterySummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tlpUpsBatterySummaryTable.setStatus("current")
_TlpUpsBatterySummaryEntry_Object = MibTableRow
tlpUpsBatterySummaryEntry = _TlpUpsBatterySummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1)
)
tlpUpsBatterySummaryEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatterySummaryEntry.setStatus("current")


class _TlpUpsBatteryStatus_Type(Integer32):
    """Custom type tlpUpsBatteryStatus based on Integer32"""
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
        *(("batteryDepleted", 4),
          ("batteryLow", 3),
          ("batteryNormal", 2),
          ("unknown", 1))
    )


_TlpUpsBatteryStatus_Type.__name__ = "Integer32"
_TlpUpsBatteryStatus_Object = MibTableColumn
tlpUpsBatteryStatus = _TlpUpsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 1),
    _TlpUpsBatteryStatus_Type()
)
tlpUpsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryStatus.setStatus("current")
_TlpUpsSecondsOnBattery_Type = Unsigned32
_TlpUpsSecondsOnBattery_Object = MibTableColumn
tlpUpsSecondsOnBattery = _TlpUpsSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 2),
    _TlpUpsSecondsOnBattery_Type()
)
tlpUpsSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsSecondsOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsSecondsOnBattery.setUnits("seconds")
_TlpUpsEstimatedMinutesRemaining_Type = Unsigned32
_TlpUpsEstimatedMinutesRemaining_Object = MibTableColumn
tlpUpsEstimatedMinutesRemaining = _TlpUpsEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 3),
    _TlpUpsEstimatedMinutesRemaining_Type()
)
tlpUpsEstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsEstimatedMinutesRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsEstimatedMinutesRemaining.setUnits("minutes")


class _TlpUpsEstimatedChargeRemaining_Type(Integer32):
    """Custom type tlpUpsEstimatedChargeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpUpsEstimatedChargeRemaining_Type.__name__ = "Integer32"
_TlpUpsEstimatedChargeRemaining_Object = MibTableColumn
tlpUpsEstimatedChargeRemaining = _TlpUpsEstimatedChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 4),
    _TlpUpsEstimatedChargeRemaining_Type()
)
tlpUpsEstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsEstimatedChargeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsEstimatedChargeRemaining.setUnits("percent")
_TlpUpsBatteryRunTimeRemaining_Type = TimeTicks
_TlpUpsBatteryRunTimeRemaining_Object = MibTableColumn
tlpUpsBatteryRunTimeRemaining = _TlpUpsBatteryRunTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 1, 1, 5),
    _TlpUpsBatteryRunTimeRemaining_Type()
)
tlpUpsBatteryRunTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryRunTimeRemaining.setStatus("current")
_TlpUpsBatteryDetailTable_Object = MibTable
tlpUpsBatteryDetailTable = _TlpUpsBatteryDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailTable.setStatus("current")
_TlpUpsBatteryDetailEntry_Object = MibTableRow
tlpUpsBatteryDetailEntry = _TlpUpsBatteryDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1)
)
tlpUpsBatteryDetailEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailEntry.setStatus("current")
_TlpUpsBatteryDetailVoltage_Type = Unsigned32
_TlpUpsBatteryDetailVoltage_Object = MibTableColumn
tlpUpsBatteryDetailVoltage = _TlpUpsBatteryDetailVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 1),
    _TlpUpsBatteryDetailVoltage_Type()
)
tlpUpsBatteryDetailVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailVoltage.setUnits("0.1 Volt DC")
_TlpUpsBatteryDetailCurrent_Type = Unsigned32
_TlpUpsBatteryDetailCurrent_Object = MibTableColumn
tlpUpsBatteryDetailCurrent = _TlpUpsBatteryDetailCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 2),
    _TlpUpsBatteryDetailCurrent_Type()
)
tlpUpsBatteryDetailCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCurrent.setUnits("0.1 Amp DC")


class _TlpUpsBatteryDetailCapacity_Type(Integer32):
    """Custom type tlpUpsBatteryDetailCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpUpsBatteryDetailCapacity_Type.__name__ = "Integer32"
_TlpUpsBatteryDetailCapacity_Object = MibTableColumn
tlpUpsBatteryDetailCapacity = _TlpUpsBatteryDetailCapacity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 3),
    _TlpUpsBatteryDetailCapacity_Type()
)
tlpUpsBatteryDetailCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCapacity.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCapacity.setUnits("percent")


class _TlpUpsBatteryDetailCharge_Type(Integer32):
    """Custom type tlpUpsBatteryDetailCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("charging", 1),
          ("discharging", 3),
          ("floating", 0),
          ("normal", 4),
          ("resting", 2),
          ("standby", 5))
    )


_TlpUpsBatteryDetailCharge_Type.__name__ = "Integer32"
_TlpUpsBatteryDetailCharge_Object = MibTableColumn
tlpUpsBatteryDetailCharge = _TlpUpsBatteryDetailCharge_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 4),
    _TlpUpsBatteryDetailCharge_Type()
)
tlpUpsBatteryDetailCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailCharge.setStatus("current")


class _TlpUpsBatteryDetailChargerStatus_Type(Integer32):
    """Custom type tlpUpsBatteryDetailChargerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inFaultCondition", 1),
          ("ok", 0))
    )


_TlpUpsBatteryDetailChargerStatus_Type.__name__ = "Integer32"
_TlpUpsBatteryDetailChargerStatus_Object = MibTableColumn
tlpUpsBatteryDetailChargerStatus = _TlpUpsBatteryDetailChargerStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 2, 1, 5),
    _TlpUpsBatteryDetailChargerStatus_Type()
)
tlpUpsBatteryDetailChargerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryDetailChargerStatus.setStatus("current")
_TlpUpsBatteryPackIdentTable_Object = MibTable
tlpUpsBatteryPackIdentTable = _TlpUpsBatteryPackIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentTable.setStatus("current")
_TlpUpsBatteryPackIdentEntry_Object = MibTableRow
tlpUpsBatteryPackIdentEntry = _TlpUpsBatteryPackIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1)
)
tlpUpsBatteryPackIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsBatteryPackIdentIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentEntry.setStatus("current")
_TlpUpsBatteryPackIdentIndex_Type = Unsigned32
_TlpUpsBatteryPackIdentIndex_Object = MibTableColumn
tlpUpsBatteryPackIdentIndex = _TlpUpsBatteryPackIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 1),
    _TlpUpsBatteryPackIdentIndex_Type()
)
tlpUpsBatteryPackIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentIndex.setStatus("current")
_TlpUpsBatteryPackIdentManufacturer_Type = DisplayString
_TlpUpsBatteryPackIdentManufacturer_Object = MibTableColumn
tlpUpsBatteryPackIdentManufacturer = _TlpUpsBatteryPackIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 2),
    _TlpUpsBatteryPackIdentManufacturer_Type()
)
tlpUpsBatteryPackIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentManufacturer.setStatus("current")
_TlpUpsBatteryPackIdentModel_Type = DisplayString
_TlpUpsBatteryPackIdentModel_Object = MibTableColumn
tlpUpsBatteryPackIdentModel = _TlpUpsBatteryPackIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 3),
    _TlpUpsBatteryPackIdentModel_Type()
)
tlpUpsBatteryPackIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentModel.setStatus("current")
_TlpUpsBatteryPackIdentSerialNum_Type = DisplayString
_TlpUpsBatteryPackIdentSerialNum_Object = MibTableColumn
tlpUpsBatteryPackIdentSerialNum = _TlpUpsBatteryPackIdentSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 4),
    _TlpUpsBatteryPackIdentSerialNum_Type()
)
tlpUpsBatteryPackIdentSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentSerialNum.setStatus("current")
_TlpUpsBatteryPackIdentFirmware_Type = DisplayString
_TlpUpsBatteryPackIdentFirmware_Object = MibTableColumn
tlpUpsBatteryPackIdentFirmware = _TlpUpsBatteryPackIdentFirmware_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 5),
    _TlpUpsBatteryPackIdentFirmware_Type()
)
tlpUpsBatteryPackIdentFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentFirmware.setStatus("current")
_TlpUpsBatteryPackIdentSKU_Type = DisplayString
_TlpUpsBatteryPackIdentSKU_Object = MibTableColumn
tlpUpsBatteryPackIdentSKU = _TlpUpsBatteryPackIdentSKU_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 3, 1, 6),
    _TlpUpsBatteryPackIdentSKU_Type()
)
tlpUpsBatteryPackIdentSKU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackIdentSKU.setStatus("current")
_TlpUpsBatteryPackConfigTable_Object = MibTable
tlpUpsBatteryPackConfigTable = _TlpUpsBatteryPackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigTable.setStatus("current")
_TlpUpsBatteryPackConfigEntry_Object = MibTableRow
tlpUpsBatteryPackConfigEntry = _TlpUpsBatteryPackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1)
)
tlpUpsBatteryPackConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsBatteryPackIdentIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigEntry.setStatus("current")


class _TlpUpsBatteryPackConfigChemistry_Type(Integer32):
    """Custom type tlpUpsBatteryPackConfigChemistry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leadAcid", 1),
          ("lithiumIon", 3),
          ("nickelCadmium", 2),
          ("unknown", 0))
    )


_TlpUpsBatteryPackConfigChemistry_Type.__name__ = "Integer32"
_TlpUpsBatteryPackConfigChemistry_Object = MibTableColumn
tlpUpsBatteryPackConfigChemistry = _TlpUpsBatteryPackConfigChemistry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 1),
    _TlpUpsBatteryPackConfigChemistry_Type()
)
tlpUpsBatteryPackConfigChemistry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigChemistry.setStatus("current")


class _TlpUpsBatteryPackConfigStyle_Type(Integer32):
    """Custom type tlpUpsBatteryPackConfigStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bms", 3),
          ("nonsmart", 1),
          ("smart", 2),
          ("unknown", 0))
    )


_TlpUpsBatteryPackConfigStyle_Type.__name__ = "Integer32"
_TlpUpsBatteryPackConfigStyle_Object = MibTableColumn
tlpUpsBatteryPackConfigStyle = _TlpUpsBatteryPackConfigStyle_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 2),
    _TlpUpsBatteryPackConfigStyle_Type()
)
tlpUpsBatteryPackConfigStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigStyle.setStatus("current")


class _TlpUpsBatteryPackConfigLocation_Type(Integer32):
    """Custom type tlpUpsBatteryPackConfigLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("unknown", 0))
    )


_TlpUpsBatteryPackConfigLocation_Type.__name__ = "Integer32"
_TlpUpsBatteryPackConfigLocation_Object = MibTableColumn
tlpUpsBatteryPackConfigLocation = _TlpUpsBatteryPackConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 3),
    _TlpUpsBatteryPackConfigLocation_Type()
)
tlpUpsBatteryPackConfigLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigLocation.setStatus("current")
_TlpUpsBatteryPackConfigStrings_Type = Unsigned32
_TlpUpsBatteryPackConfigStrings_Object = MibTableColumn
tlpUpsBatteryPackConfigStrings = _TlpUpsBatteryPackConfigStrings_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 4),
    _TlpUpsBatteryPackConfigStrings_Type()
)
tlpUpsBatteryPackConfigStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigStrings.setStatus("current")
_TlpUpsBatteryPackConfigBatteriesPerString_Type = Unsigned32
_TlpUpsBatteryPackConfigBatteriesPerString_Object = MibTableColumn
tlpUpsBatteryPackConfigBatteriesPerString = _TlpUpsBatteryPackConfigBatteriesPerString_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 5),
    _TlpUpsBatteryPackConfigBatteriesPerString_Type()
)
tlpUpsBatteryPackConfigBatteriesPerString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigBatteriesPerString.setStatus("current")


class _TlpUpsBatteryPackConfigCellsPerBattery_Type(Integer32):
    """Custom type tlpUpsBatteryPackConfigCellsPerBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("four", 4),
          ("one", 1),
          ("six", 6),
          ("two", 2),
          ("unknown", 0))
    )


_TlpUpsBatteryPackConfigCellsPerBattery_Type.__name__ = "Integer32"
_TlpUpsBatteryPackConfigCellsPerBattery_Object = MibTableColumn
tlpUpsBatteryPackConfigCellsPerBattery = _TlpUpsBatteryPackConfigCellsPerBattery_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 6),
    _TlpUpsBatteryPackConfigCellsPerBattery_Type()
)
tlpUpsBatteryPackConfigCellsPerBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigCellsPerBattery.setStatus("current")
_TlpUpsBatteryPackConfigNumBatteries_Type = Unsigned32
_TlpUpsBatteryPackConfigNumBatteries_Object = MibTableColumn
tlpUpsBatteryPackConfigNumBatteries = _TlpUpsBatteryPackConfigNumBatteries_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 7),
    _TlpUpsBatteryPackConfigNumBatteries_Type()
)
tlpUpsBatteryPackConfigNumBatteries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigNumBatteries.setStatus("current")


class _TlpUpsBatteryPackConfigCapacityUnits_Type(Integer32):
    """Custom type tlpUpsBatteryPackConfigCapacityUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mAHr", 0),
          ("mWHr", 1))
    )


_TlpUpsBatteryPackConfigCapacityUnits_Type.__name__ = "Integer32"
_TlpUpsBatteryPackConfigCapacityUnits_Object = MibTableColumn
tlpUpsBatteryPackConfigCapacityUnits = _TlpUpsBatteryPackConfigCapacityUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 8),
    _TlpUpsBatteryPackConfigCapacityUnits_Type()
)
tlpUpsBatteryPackConfigCapacityUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigCapacityUnits.setStatus("current")
_TlpUpsBatteryPackConfigDesignCapacity_Type = Unsigned32
_TlpUpsBatteryPackConfigDesignCapacity_Object = MibTableColumn
tlpUpsBatteryPackConfigDesignCapacity = _TlpUpsBatteryPackConfigDesignCapacity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 9),
    _TlpUpsBatteryPackConfigDesignCapacity_Type()
)
tlpUpsBatteryPackConfigDesignCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigDesignCapacity.setStatus("current")
_TlpUpsBatteryPackConfigCellCapacity_Type = Unsigned32
_TlpUpsBatteryPackConfigCellCapacity_Object = MibTableColumn
tlpUpsBatteryPackConfigCellCapacity = _TlpUpsBatteryPackConfigCellCapacity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 10),
    _TlpUpsBatteryPackConfigCellCapacity_Type()
)
tlpUpsBatteryPackConfigCellCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigCellCapacity.setStatus("current")
_TlpUpsBatteryPackConfigMinCellVoltage_Type = Unsigned32
_TlpUpsBatteryPackConfigMinCellVoltage_Object = MibTableColumn
tlpUpsBatteryPackConfigMinCellVoltage = _TlpUpsBatteryPackConfigMinCellVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 11),
    _TlpUpsBatteryPackConfigMinCellVoltage_Type()
)
tlpUpsBatteryPackConfigMinCellVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigMinCellVoltage.setStatus("current")
_TlpUpsBatteryPackConfigMaxCellVoltage_Type = Unsigned32
_TlpUpsBatteryPackConfigMaxCellVoltage_Object = MibTableColumn
tlpUpsBatteryPackConfigMaxCellVoltage = _TlpUpsBatteryPackConfigMaxCellVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 4, 1, 12),
    _TlpUpsBatteryPackConfigMaxCellVoltage_Type()
)
tlpUpsBatteryPackConfigMaxCellVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackConfigMaxCellVoltage.setStatus("current")
_TlpUpsBatteryPackDetailTable_Object = MibTable
tlpUpsBatteryPackDetailTable = _TlpUpsBatteryPackDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTable.setStatus("current")
_TlpUpsBatteryPackDetailEntry_Object = MibTableRow
tlpUpsBatteryPackDetailEntry = _TlpUpsBatteryPackDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1)
)
tlpUpsBatteryPackDetailEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsBatteryPackIdentIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailEntry.setStatus("current")


class _TlpUpsBatteryPackDetailCondition_Type(Integer32):
    """Custom type tlpUpsBatteryPackDetailCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 3),
          ("good", 1),
          ("unknown", 0),
          ("weak", 2))
    )


_TlpUpsBatteryPackDetailCondition_Type.__name__ = "Integer32"
_TlpUpsBatteryPackDetailCondition_Object = MibTableColumn
tlpUpsBatteryPackDetailCondition = _TlpUpsBatteryPackDetailCondition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 1),
    _TlpUpsBatteryPackDetailCondition_Type()
)
tlpUpsBatteryPackDetailCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailCondition.setStatus("current")
_TlpUpsBatteryPackDetailTemperatureC_Type = Unsigned32
_TlpUpsBatteryPackDetailTemperatureC_Object = MibTableColumn
tlpUpsBatteryPackDetailTemperatureC = _TlpUpsBatteryPackDetailTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 2),
    _TlpUpsBatteryPackDetailTemperatureC_Type()
)
tlpUpsBatteryPackDetailTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTemperatureC.setUnits("degrees Centigrade")
_TlpUpsBatteryPackDetailTemperatureF_Type = Unsigned32
_TlpUpsBatteryPackDetailTemperatureF_Object = MibTableColumn
tlpUpsBatteryPackDetailTemperatureF = _TlpUpsBatteryPackDetailTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 3),
    _TlpUpsBatteryPackDetailTemperatureF_Type()
)
tlpUpsBatteryPackDetailTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailTemperatureF.setUnits("0.1 degrees Farenheit")
_TlpUpsBatteryPackDetailAge_Type = Unsigned32
_TlpUpsBatteryPackDetailAge_Object = MibTableColumn
tlpUpsBatteryPackDetailAge = _TlpUpsBatteryPackDetailAge_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 4),
    _TlpUpsBatteryPackDetailAge_Type()
)
tlpUpsBatteryPackDetailAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailAge.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailAge.setUnits("0.1 Years")
_TlpUpsBatteryPackDetailLastReplaceDate_Type = DisplayString
_TlpUpsBatteryPackDetailLastReplaceDate_Object = MibTableColumn
tlpUpsBatteryPackDetailLastReplaceDate = _TlpUpsBatteryPackDetailLastReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 5),
    _TlpUpsBatteryPackDetailLastReplaceDate_Type()
)
tlpUpsBatteryPackDetailLastReplaceDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailLastReplaceDate.setStatus("current")
_TlpUpsBatteryPackDetailNextReplaceDate_Type = DisplayString
_TlpUpsBatteryPackDetailNextReplaceDate_Object = MibTableColumn
tlpUpsBatteryPackDetailNextReplaceDate = _TlpUpsBatteryPackDetailNextReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 6),
    _TlpUpsBatteryPackDetailNextReplaceDate_Type()
)
tlpUpsBatteryPackDetailNextReplaceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailNextReplaceDate.setStatus("current")
_TlpUpsBatteryPackDetailCycleCount_Type = Unsigned32
_TlpUpsBatteryPackDetailCycleCount_Object = MibTableColumn
tlpUpsBatteryPackDetailCycleCount = _TlpUpsBatteryPackDetailCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 1, 5, 1, 7),
    _TlpUpsBatteryPackDetailCycleCount_Type()
)
tlpUpsBatteryPackDetailCycleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBatteryPackDetailCycleCount.setStatus("current")
_TlpUpsInput_ObjectIdentity = ObjectIdentity
tlpUpsInput = _TlpUpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2)
)
_TlpUpsInputTable_Object = MibTable
tlpUpsInputTable = _TlpUpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tlpUpsInputTable.setStatus("current")
_TlpUpsInputEntry_Object = MibTableRow
tlpUpsInputEntry = _TlpUpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1)
)
tlpUpsInputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsInputEntry.setStatus("current")
_TlpUpsInputLineBads_Type = Integer32
_TlpUpsInputLineBads_Object = MibTableColumn
tlpUpsInputLineBads = _TlpUpsInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 1),
    _TlpUpsInputLineBads_Type()
)
tlpUpsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputLineBads.setStatus("current")
_TlpUpsInputNominalVoltage_Type = Unsigned32
_TlpUpsInputNominalVoltage_Object = MibTableColumn
tlpUpsInputNominalVoltage = _TlpUpsInputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 2),
    _TlpUpsInputNominalVoltage_Type()
)
tlpUpsInputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputNominalVoltage.setStatus("current")
_TlpUpsInputNominalFrequency_Type = Unsigned32
_TlpUpsInputNominalFrequency_Object = MibTableColumn
tlpUpsInputNominalFrequency = _TlpUpsInputNominalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 3),
    _TlpUpsInputNominalFrequency_Type()
)
tlpUpsInputNominalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputNominalFrequency.setStatus("current")
_TlpUpsInputLowTransferVoltage_Type = Unsigned32
_TlpUpsInputLowTransferVoltage_Object = MibTableColumn
tlpUpsInputLowTransferVoltage = _TlpUpsInputLowTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 4),
    _TlpUpsInputLowTransferVoltage_Type()
)
tlpUpsInputLowTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltage.setUnits("0.1 Volts")
_TlpUpsInputLowTransferVoltageLowerBound_Type = Unsigned32
_TlpUpsInputLowTransferVoltageLowerBound_Object = MibTableColumn
tlpUpsInputLowTransferVoltageLowerBound = _TlpUpsInputLowTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 5),
    _TlpUpsInputLowTransferVoltageLowerBound_Type()
)
tlpUpsInputLowTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageLowerBound.setUnits("0.1 Volts")
_TlpUpsInputLowTransferVoltageUpperBound_Type = Unsigned32
_TlpUpsInputLowTransferVoltageUpperBound_Object = MibTableColumn
tlpUpsInputLowTransferVoltageUpperBound = _TlpUpsInputLowTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 6),
    _TlpUpsInputLowTransferVoltageUpperBound_Type()
)
tlpUpsInputLowTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputLowTransferVoltageUpperBound.setUnits("0.1 Volts")
_TlpUpsInputHighTransferVoltage_Type = Unsigned32
_TlpUpsInputHighTransferVoltage_Object = MibTableColumn
tlpUpsInputHighTransferVoltage = _TlpUpsInputHighTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 7),
    _TlpUpsInputHighTransferVoltage_Type()
)
tlpUpsInputHighTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltage.setUnits("0.1 Volts")
_TlpUpsInputHighTransferVoltageLowerBound_Type = Unsigned32
_TlpUpsInputHighTransferVoltageLowerBound_Object = MibTableColumn
tlpUpsInputHighTransferVoltageLowerBound = _TlpUpsInputHighTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 8),
    _TlpUpsInputHighTransferVoltageLowerBound_Type()
)
tlpUpsInputHighTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageLowerBound.setUnits("0.1 Volts")
_TlpUpsInputHighTransferVoltageUpperBound_Type = Unsigned32
_TlpUpsInputHighTransferVoltageUpperBound_Object = MibTableColumn
tlpUpsInputHighTransferVoltageUpperBound = _TlpUpsInputHighTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 1, 1, 9),
    _TlpUpsInputHighTransferVoltageUpperBound_Type()
)
tlpUpsInputHighTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputHighTransferVoltageUpperBound.setUnits("0.1 Volts")
_TlpUpsInputPhaseTable_Object = MibTable
tlpUpsInputPhaseTable = _TlpUpsInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tlpUpsInputPhaseTable.setStatus("current")
_TlpUpsInputPhaseEntry_Object = MibTableRow
tlpUpsInputPhaseEntry = _TlpUpsInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1)
)
tlpUpsInputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsInputPhaseEntry.setStatus("current")
_TlpUpsInputPhaseIndex_Type = Unsigned32
_TlpUpsInputPhaseIndex_Object = MibTableColumn
tlpUpsInputPhaseIndex = _TlpUpsInputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 1),
    _TlpUpsInputPhaseIndex_Type()
)
tlpUpsInputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseIndex.setStatus("current")
_TlpUpsInputPhaseFrequency_Type = Unsigned32
_TlpUpsInputPhaseFrequency_Object = MibTableColumn
tlpUpsInputPhaseFrequency = _TlpUpsInputPhaseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 2),
    _TlpUpsInputPhaseFrequency_Type()
)
tlpUpsInputPhaseFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseFrequency.setUnits("0.1 Hertz")
_TlpUpsInputPhaseVoltage_Type = Unsigned32
_TlpUpsInputPhaseVoltage_Object = MibTableColumn
tlpUpsInputPhaseVoltage = _TlpUpsInputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 3),
    _TlpUpsInputPhaseVoltage_Type()
)
tlpUpsInputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltage.setUnits("0.1 Volt DC")
_TlpUpsInputPhaseVoltageMin_Type = Unsigned32
_TlpUpsInputPhaseVoltageMin_Object = MibTableColumn
tlpUpsInputPhaseVoltageMin = _TlpUpsInputPhaseVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 4),
    _TlpUpsInputPhaseVoltageMin_Type()
)
tlpUpsInputPhaseVoltageMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltageMin.setUnits("0.1 Volt DC")
_TlpUpsInputPhaseVoltageMax_Type = Unsigned32
_TlpUpsInputPhaseVoltageMax_Object = MibTableColumn
tlpUpsInputPhaseVoltageMax = _TlpUpsInputPhaseVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 5),
    _TlpUpsInputPhaseVoltageMax_Type()
)
tlpUpsInputPhaseVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseVoltageMax.setUnits("0.1 Volt DC")
_TlpUpsInputPhaseCurrent_Type = Unsigned32
_TlpUpsInputPhaseCurrent_Object = MibTableColumn
tlpUpsInputPhaseCurrent = _TlpUpsInputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 6),
    _TlpUpsInputPhaseCurrent_Type()
)
tlpUpsInputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhaseCurrent.setUnits("0.01 Amp DC")
_TlpUpsInputPhasePower_Type = Unsigned32
_TlpUpsInputPhasePower_Object = MibTableColumn
tlpUpsInputPhasePower = _TlpUpsInputPhasePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 2, 2, 1, 7),
    _TlpUpsInputPhasePower_Type()
)
tlpUpsInputPhasePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsInputPhasePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsInputPhasePower.setUnits("Watts")
_TlpUpsOutput_ObjectIdentity = ObjectIdentity
tlpUpsOutput = _TlpUpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3)
)
_TlpUpsOutputTable_Object = MibTable
tlpUpsOutputTable = _TlpUpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpUpsOutputTable.setStatus("current")
_TlpUpsOutputEntry_Object = MibTableRow
tlpUpsOutputEntry = _TlpUpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1)
)
tlpUpsOutputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsOutputEntry.setStatus("current")


class _TlpUpsOutputSource_Type(Integer32):
    """Custom type tlpUpsOutputSource based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("battery", 5),
          ("boosting", 6),
          ("bypass", 4),
          ("economy", 9),
          ("none", 2),
          ("normal", 3),
          ("other", 1),
          ("reducing", 7),
          ("second", 8),
          ("unknown", 0))
    )


_TlpUpsOutputSource_Type.__name__ = "Integer32"
_TlpUpsOutputSource_Object = MibTableColumn
tlpUpsOutputSource = _TlpUpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 1),
    _TlpUpsOutputSource_Type()
)
tlpUpsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputSource.setStatus("current")
_TlpUpsOutputNominalVoltage_Type = Unsigned32
_TlpUpsOutputNominalVoltage_Object = MibTableColumn
tlpUpsOutputNominalVoltage = _TlpUpsOutputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 2),
    _TlpUpsOutputNominalVoltage_Type()
)
tlpUpsOutputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputNominalVoltage.setStatus("current")
_TlpUpsOutputFrequency_Type = Unsigned32
_TlpUpsOutputFrequency_Object = MibTableColumn
tlpUpsOutputFrequency = _TlpUpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 1, 1, 3),
    _TlpUpsOutputFrequency_Type()
)
tlpUpsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputFrequency.setUnits("0.1 Hertz")
_TlpUpsOutputLineTable_Object = MibTable
tlpUpsOutputLineTable = _TlpUpsOutputLineTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpUpsOutputLineTable.setStatus("current")
_TlpUpsOutputLineEntry_Object = MibTableRow
tlpUpsOutputLineEntry = _TlpUpsOutputLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1)
)
tlpUpsOutputLineEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsOutputLineEntry.setStatus("current")
_TlpUpsOutputLineIndex_Type = Unsigned32
_TlpUpsOutputLineIndex_Object = MibTableColumn
tlpUpsOutputLineIndex = _TlpUpsOutputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 1),
    _TlpUpsOutputLineIndex_Type()
)
tlpUpsOutputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineIndex.setStatus("current")
_TlpUpsOutputLineVoltage_Type = Unsigned32
_TlpUpsOutputLineVoltage_Object = MibTableColumn
tlpUpsOutputLineVoltage = _TlpUpsOutputLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 2),
    _TlpUpsOutputLineVoltage_Type()
)
tlpUpsOutputLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineVoltage.setUnits("0.1 Volt DC")
_TlpUpsOutputLineCurrent_Type = Unsigned32
_TlpUpsOutputLineCurrent_Object = MibTableColumn
tlpUpsOutputLineCurrent = _TlpUpsOutputLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 3),
    _TlpUpsOutputLineCurrent_Type()
)
tlpUpsOutputLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineCurrent.setUnits("0.1 Amp")
_TlpUpsOutputLinePower_Type = Unsigned32
_TlpUpsOutputLinePower_Object = MibTableColumn
tlpUpsOutputLinePower = _TlpUpsOutputLinePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 4),
    _TlpUpsOutputLinePower_Type()
)
tlpUpsOutputLinePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePower.setUnits("Watts")


class _TlpUpsOutputLinePercentLoad_Type(Integer32):
    """Custom type tlpUpsOutputLinePercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TlpUpsOutputLinePercentLoad_Type.__name__ = "Integer32"
_TlpUpsOutputLinePercentLoad_Object = MibTableColumn
tlpUpsOutputLinePercentLoad = _TlpUpsOutputLinePercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 5),
    _TlpUpsOutputLinePercentLoad_Type()
)
tlpUpsOutputLinePercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLinePercentLoad.setUnits("percent")
_TlpUpsOutputLineFrequency_Type = Unsigned32
_TlpUpsOutputLineFrequency_Object = MibTableColumn
tlpUpsOutputLineFrequency = _TlpUpsOutputLineFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 3, 2, 1, 6),
    _TlpUpsOutputLineFrequency_Type()
)
tlpUpsOutputLineFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutputLineFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutputLineFrequency.setUnits("0.1 Hertz")
_TlpUpsBypass_ObjectIdentity = ObjectIdentity
tlpUpsBypass = _TlpUpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4)
)
_TlpUpsBypassTable_Object = MibTable
tlpUpsBypassTable = _TlpUpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpUpsBypassTable.setStatus("current")
_TlpUpsBypassEntry_Object = MibTableRow
tlpUpsBypassEntry = _TlpUpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 1, 1)
)
tlpUpsBypassEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBypassEntry.setStatus("current")
_TlpUpsBypassFrequency_Type = Unsigned32
_TlpUpsBypassFrequency_Object = MibTableColumn
tlpUpsBypassFrequency = _TlpUpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 1, 1, 1),
    _TlpUpsBypassFrequency_Type()
)
tlpUpsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBypassFrequency.setUnits("0.1 Hertz")
_TlpUpsBypassLineTable_Object = MibTable
tlpUpsBypassLineTable = _TlpUpsBypassLineTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    tlpUpsBypassLineTable.setStatus("current")
_TlpUpsBypassLineEntry_Object = MibTableRow
tlpUpsBypassLineEntry = _TlpUpsBypassLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1)
)
tlpUpsBypassLineEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsBypassLineIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsBypassLineEntry.setStatus("current")
_TlpUpsBypassLineIndex_Type = Unsigned32
_TlpUpsBypassLineIndex_Object = MibTableColumn
tlpUpsBypassLineIndex = _TlpUpsBypassLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1, 1),
    _TlpUpsBypassLineIndex_Type()
)
tlpUpsBypassLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassLineIndex.setStatus("current")
_TlpUpsBypassLineVoltage_Type = Unsigned32
_TlpUpsBypassLineVoltage_Object = MibTableColumn
tlpUpsBypassLineVoltage = _TlpUpsBypassLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1, 2),
    _TlpUpsBypassLineVoltage_Type()
)
tlpUpsBypassLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassLineVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBypassLineVoltage.setUnits("0.1 Volt DC")
_TlpUpsBypassLineCurrent_Type = Unsigned32
_TlpUpsBypassLineCurrent_Object = MibTableColumn
tlpUpsBypassLineCurrent = _TlpUpsBypassLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1, 3),
    _TlpUpsBypassLineCurrent_Type()
)
tlpUpsBypassLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBypassLineCurrent.setUnits("0.1 Amp")
_TlpUpsBypassLinePower_Type = Unsigned32
_TlpUpsBypassLinePower_Object = MibTableColumn
tlpUpsBypassLinePower = _TlpUpsBypassLinePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 4, 2, 1, 4),
    _TlpUpsBypassLinePower_Type()
)
tlpUpsBypassLinePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsBypassLinePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsBypassLinePower.setUnits("Watts")
_TlpUpsOutlet_ObjectIdentity = ObjectIdentity
tlpUpsOutlet = _TlpUpsOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5)
)
_TlpUpsOutletTable_Object = MibTable
tlpUpsOutletTable = _TlpUpsOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpUpsOutletTable.setStatus("current")
_TlpUpsOutletEntry_Object = MibTableRow
tlpUpsOutletEntry = _TlpUpsOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1)
)
tlpUpsOutletEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsOutletIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsOutletEntry.setStatus("current")
_TlpUpsOutletIndex_Type = Unsigned32
_TlpUpsOutletIndex_Object = MibTableColumn
tlpUpsOutletIndex = _TlpUpsOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 1),
    _TlpUpsOutletIndex_Type()
)
tlpUpsOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletIndex.setStatus("current")
_TlpUpsOutletName_Type = DisplayString
_TlpUpsOutletName_Object = MibTableColumn
tlpUpsOutletName = _TlpUpsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 2),
    _TlpUpsOutletName_Type()
)
tlpUpsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletName.setStatus("current")
_TlpUpsOutletDescription_Type = DisplayString
_TlpUpsOutletDescription_Object = MibTableColumn
tlpUpsOutletDescription = _TlpUpsOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 3),
    _TlpUpsOutletDescription_Type()
)
tlpUpsOutletDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletDescription.setStatus("current")


class _TlpUpsOutletState_Type(Integer32):
    """Custom type tlpUpsOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlpUpsOutletState_Type.__name__ = "Integer32"
_TlpUpsOutletState_Object = MibTableColumn
tlpUpsOutletState = _TlpUpsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 4),
    _TlpUpsOutletState_Type()
)
tlpUpsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletState.setStatus("current")
_TlpUpsOutletControllable_Type = TruthValue
_TlpUpsOutletControllable_Object = MibTableColumn
tlpUpsOutletControllable = _TlpUpsOutletControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 5),
    _TlpUpsOutletControllable_Type()
)
tlpUpsOutletControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletControllable.setStatus("current")


class _TlpUpsOutletCommand_Type(Integer32):
    """Custom type tlpUpsOutletCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlpUpsOutletCommand_Type.__name__ = "Integer32"
_TlpUpsOutletCommand_Object = MibTableColumn
tlpUpsOutletCommand = _TlpUpsOutletCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 6),
    _TlpUpsOutletCommand_Type()
)
tlpUpsOutletCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletCommand.setStatus("current")
_TlpUpsOutletVoltage_Type = Unsigned32
_TlpUpsOutletVoltage_Object = MibTableColumn
tlpUpsOutletVoltage = _TlpUpsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 7),
    _TlpUpsOutletVoltage_Type()
)
tlpUpsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletVoltage.setUnits("0.1 Volt DC")
_TlpUpsOutletCurrent_Type = Unsigned32
_TlpUpsOutletCurrent_Object = MibTableColumn
tlpUpsOutletCurrent = _TlpUpsOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 8),
    _TlpUpsOutletCurrent_Type()
)
tlpUpsOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletCurrent.setUnits("0.01 RMS Amp")
_TlpUpsOutletPower_Type = Unsigned32
_TlpUpsOutletPower_Object = MibTableColumn
tlpUpsOutletPower = _TlpUpsOutletPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 9),
    _TlpUpsOutletPower_Type()
)
tlpUpsOutletPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletPower.setUnits("Watts")


class _TlpUpsOutletRampAction_Type(Integer32):
    """Custom type tlpUpsOutletRampAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOff", 0),
          ("turnOnAfterDelay", 1))
    )


_TlpUpsOutletRampAction_Type.__name__ = "Integer32"
_TlpUpsOutletRampAction_Object = MibTableColumn
tlpUpsOutletRampAction = _TlpUpsOutletRampAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 10),
    _TlpUpsOutletRampAction_Type()
)
tlpUpsOutletRampAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletRampAction.setStatus("current")
_TlpUpsOutletRampDelay_Type = Integer32
_TlpUpsOutletRampDelay_Object = MibTableColumn
tlpUpsOutletRampDelay = _TlpUpsOutletRampDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 11),
    _TlpUpsOutletRampDelay_Type()
)
tlpUpsOutletRampDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletRampDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletRampDelay.setUnits("seconds")


class _TlpUpsOutletShedAction_Type(Integer32):
    """Custom type tlpUpsOutletShedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOn", 0),
          ("turnOffAfterDelay", 1))
    )


_TlpUpsOutletShedAction_Type.__name__ = "Integer32"
_TlpUpsOutletShedAction_Object = MibTableColumn
tlpUpsOutletShedAction = _TlpUpsOutletShedAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 12),
    _TlpUpsOutletShedAction_Type()
)
tlpUpsOutletShedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletShedAction.setStatus("current")
_TlpUpsOutletShedDelay_Type = Integer32
_TlpUpsOutletShedDelay_Object = MibTableColumn
tlpUpsOutletShedDelay = _TlpUpsOutletShedDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 13),
    _TlpUpsOutletShedDelay_Type()
)
tlpUpsOutletShedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletShedDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsOutletShedDelay.setUnits("seconds")
_TlpUpsOutletGroup_Type = Integer32
_TlpUpsOutletGroup_Object = MibTableColumn
tlpUpsOutletGroup = _TlpUpsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 1, 1, 14),
    _TlpUpsOutletGroup_Type()
)
tlpUpsOutletGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroup.setStatus("current")
_TlpUpsOutletGroupTable_Object = MibTable
tlpUpsOutletGroupTable = _TlpUpsOutletGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    tlpUpsOutletGroupTable.setStatus("current")
_TlpUpsOutletGroupEntry_Object = MibTableRow
tlpUpsOutletGroupEntry = _TlpUpsOutletGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1)
)
tlpUpsOutletGroupEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpUpsOutletGroupIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsOutletGroupEntry.setStatus("current")
_TlpUpsOutletGroupIndex_Type = Unsigned32
_TlpUpsOutletGroupIndex_Object = MibTableColumn
tlpUpsOutletGroupIndex = _TlpUpsOutletGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 1),
    _TlpUpsOutletGroupIndex_Type()
)
tlpUpsOutletGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupIndex.setStatus("current")
_TlpUpsOutletGroupRowStatus_Type = RowStatus
_TlpUpsOutletGroupRowStatus_Object = MibTableColumn
tlpUpsOutletGroupRowStatus = _TlpUpsOutletGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 2),
    _TlpUpsOutletGroupRowStatus_Type()
)
tlpUpsOutletGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupRowStatus.setStatus("current")
_TlpUpsOutletGroupName_Type = DisplayString
_TlpUpsOutletGroupName_Object = MibTableColumn
tlpUpsOutletGroupName = _TlpUpsOutletGroupName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 3),
    _TlpUpsOutletGroupName_Type()
)
tlpUpsOutletGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupName.setStatus("current")
_TlpUpsOutletGroupDescription_Type = DisplayString
_TlpUpsOutletGroupDescription_Object = MibTableColumn
tlpUpsOutletGroupDescription = _TlpUpsOutletGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 4),
    _TlpUpsOutletGroupDescription_Type()
)
tlpUpsOutletGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupDescription.setStatus("current")


class _TlpUpsOutletGroupState_Type(Integer32):
    """Custom type tlpUpsOutletGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 3),
          ("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlpUpsOutletGroupState_Type.__name__ = "Integer32"
_TlpUpsOutletGroupState_Object = MibTableColumn
tlpUpsOutletGroupState = _TlpUpsOutletGroupState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 5),
    _TlpUpsOutletGroupState_Type()
)
tlpUpsOutletGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupState.setStatus("current")


class _TlpUpsOutletGroupCommand_Type(Integer32):
    """Custom type tlpUpsOutletGroupCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlpUpsOutletGroupCommand_Type.__name__ = "Integer32"
_TlpUpsOutletGroupCommand_Object = MibTableColumn
tlpUpsOutletGroupCommand = _TlpUpsOutletGroupCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 5, 2, 1, 6),
    _TlpUpsOutletGroupCommand_Type()
)
tlpUpsOutletGroupCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsOutletGroupCommand.setStatus("current")
_TlpUpsWatchdog_ObjectIdentity = ObjectIdentity
tlpUpsWatchdog = _TlpUpsWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6)
)
_TlpUpsWatchdogTable_Object = MibTable
tlpUpsWatchdogTable = _TlpUpsWatchdogTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    tlpUpsWatchdogTable.setStatus("current")
_TlpUpsWatchdogEntry_Object = MibTableRow
tlpUpsWatchdogEntry = _TlpUpsWatchdogEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1, 1)
)
tlpUpsWatchdogEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsWatchdogEntry.setStatus("current")
_TlpUpsWatchdogSupported_Type = TruthValue
_TlpUpsWatchdogSupported_Object = MibTableColumn
tlpUpsWatchdogSupported = _TlpUpsWatchdogSupported_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1, 1, 1),
    _TlpUpsWatchdogSupported_Type()
)
tlpUpsWatchdogSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpUpsWatchdogSupported.setStatus("current")
_TlpUpsWatchdogSecsBeforeReboot_Type = Unsigned32
_TlpUpsWatchdogSecsBeforeReboot_Object = MibTableColumn
tlpUpsWatchdogSecsBeforeReboot = _TlpUpsWatchdogSecsBeforeReboot_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 3, 6, 1, 1, 2),
    _TlpUpsWatchdogSecsBeforeReboot_Type()
)
tlpUpsWatchdogSecsBeforeReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsWatchdogSecsBeforeReboot.setStatus("current")
_TlpUpsControl_ObjectIdentity = ObjectIdentity
tlpUpsControl = _TlpUpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4)
)
_TlpUpsControlTable_Object = MibTable
tlpUpsControlTable = _TlpUpsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tlpUpsControlTable.setStatus("current")
_TlpUpsControlEntry_Object = MibTableRow
tlpUpsControlEntry = _TlpUpsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1)
)
tlpUpsControlEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsControlEntry.setStatus("current")
_TlpUpsControlSelfTest_Type = TruthValue
_TlpUpsControlSelfTest_Object = MibTableColumn
tlpUpsControlSelfTest = _TlpUpsControlSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 1),
    _TlpUpsControlSelfTest_Type()
)
tlpUpsControlSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlSelfTest.setStatus("current")
_TlpUpsControlRamp_Type = TruthValue
_TlpUpsControlRamp_Object = MibTableColumn
tlpUpsControlRamp = _TlpUpsControlRamp_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 2),
    _TlpUpsControlRamp_Type()
)
tlpUpsControlRamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlRamp.setStatus("current")
_TlpUpsControlShed_Type = TruthValue
_TlpUpsControlShed_Object = MibTableColumn
tlpUpsControlShed = _TlpUpsControlShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 3),
    _TlpUpsControlShed_Type()
)
tlpUpsControlShed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlShed.setStatus("current")
_TlpUpsControlUpsOn_Type = TruthValue
_TlpUpsControlUpsOn_Object = MibTableColumn
tlpUpsControlUpsOn = _TlpUpsControlUpsOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 4),
    _TlpUpsControlUpsOn_Type()
)
tlpUpsControlUpsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlUpsOn.setStatus("current")
_TlpUpsControlUpsOff_Type = TruthValue
_TlpUpsControlUpsOff_Object = MibTableColumn
tlpUpsControlUpsOff = _TlpUpsControlUpsOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 5),
    _TlpUpsControlUpsOff_Type()
)
tlpUpsControlUpsOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlUpsOff.setStatus("current")
_TlpUpsControlUpsReboot_Type = TruthValue
_TlpUpsControlUpsReboot_Object = MibTableColumn
tlpUpsControlUpsReboot = _TlpUpsControlUpsReboot_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 6),
    _TlpUpsControlUpsReboot_Type()
)
tlpUpsControlUpsReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlUpsReboot.setStatus("current")


class _TlpUpsControlBypass_Type(Integer32):
    """Custom type tlpUpsControlBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TlpUpsControlBypass_Type.__name__ = "Integer32"
_TlpUpsControlBypass_Object = MibTableColumn
tlpUpsControlBypass = _TlpUpsControlBypass_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 4, 1, 1, 7),
    _TlpUpsControlBypass_Type()
)
tlpUpsControlBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsControlBypass.setStatus("current")
_TlpUpsConfig_ObjectIdentity = ObjectIdentity
tlpUpsConfig = _TlpUpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5)
)
_TlpUpsConfigTable_Object = MibTable
tlpUpsConfigTable = _TlpUpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tlpUpsConfigTable.setStatus("current")
_TlpUpsConfigEntry_Object = MibTableRow
tlpUpsConfigEntry = _TlpUpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1)
)
tlpUpsConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigEntry.setStatus("current")
_TlpUpsConfigInputVoltage_Type = Unsigned32
_TlpUpsConfigInputVoltage_Object = MibTableColumn
tlpUpsConfigInputVoltage = _TlpUpsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 1),
    _TlpUpsConfigInputVoltage_Type()
)
tlpUpsConfigInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigInputVoltage.setUnits("Volts")
_TlpUpsConfigInputFrequency_Type = Unsigned32
_TlpUpsConfigInputFrequency_Object = MibTableColumn
tlpUpsConfigInputFrequency = _TlpUpsConfigInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 2),
    _TlpUpsConfigInputFrequency_Type()
)
tlpUpsConfigInputFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigInputFrequency.setUnits("0.1 Hertz")
_TlpUpsConfigOutputVoltage_Type = Unsigned32
_TlpUpsConfigOutputVoltage_Object = MibTableColumn
tlpUpsConfigOutputVoltage = _TlpUpsConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 3),
    _TlpUpsConfigOutputVoltage_Type()
)
tlpUpsConfigOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputVoltage.setUnits("Volts")
_TlpUpsConfigOutputFrequency_Type = Unsigned32
_TlpUpsConfigOutputFrequency_Object = MibTableColumn
tlpUpsConfigOutputFrequency = _TlpUpsConfigOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 4),
    _TlpUpsConfigOutputFrequency_Type()
)
tlpUpsConfigOutputFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOutputFrequency.setUnits("0.1 Hertz")


class _TlpUpsConfigAudibleStatus_Type(Integer32):
    """Custom type tlpUpsConfigAudibleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("muted", 3))
    )


_TlpUpsConfigAudibleStatus_Type.__name__ = "Integer32"
_TlpUpsConfigAudibleStatus_Object = MibTableColumn
tlpUpsConfigAudibleStatus = _TlpUpsConfigAudibleStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 5),
    _TlpUpsConfigAudibleStatus_Type()
)
tlpUpsConfigAudibleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAudibleStatus.setStatus("current")


class _TlpUpsConfigAutoBatteryTest_Type(Integer32):
    """Custom type tlpUpsConfigAutoBatteryTest based on Integer32"""
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
        *(("biweekly", 1),
          ("disabled", 0),
          ("monthly", 2),
          ("quarterly", 3),
          ("semiannually", 4))
    )


_TlpUpsConfigAutoBatteryTest_Type.__name__ = "Integer32"
_TlpUpsConfigAutoBatteryTest_Object = MibTableColumn
tlpUpsConfigAutoBatteryTest = _TlpUpsConfigAutoBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 6),
    _TlpUpsConfigAutoBatteryTest_Type()
)
tlpUpsConfigAutoBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoBatteryTest.setStatus("current")


class _TlpUpsConfigAutoRestartAfterShutdown_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartAfterShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartAfterShutdown_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartAfterShutdown_Object = MibTableColumn
tlpUpsConfigAutoRestartAfterShutdown = _TlpUpsConfigAutoRestartAfterShutdown_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 7),
    _TlpUpsConfigAutoRestartAfterShutdown_Type()
)
tlpUpsConfigAutoRestartAfterShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartAfterShutdown.setStatus("current")


class _TlpUpsConfigAutoRampOnTransition_Type(Integer32):
    """Custom type tlpUpsConfigAutoRampOnTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRampOnTransition_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRampOnTransition_Object = MibTableColumn
tlpUpsConfigAutoRampOnTransition = _TlpUpsConfigAutoRampOnTransition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 8),
    _TlpUpsConfigAutoRampOnTransition_Type()
)
tlpUpsConfigAutoRampOnTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRampOnTransition.setStatus("current")


class _TlpUpsConfigAutoShedOnTransition_Type(Integer32):
    """Custom type tlpUpsConfigAutoShedOnTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoShedOnTransition_Type.__name__ = "Integer32"
_TlpUpsConfigAutoShedOnTransition_Object = MibTableColumn
tlpUpsConfigAutoShedOnTransition = _TlpUpsConfigAutoShedOnTransition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 9),
    _TlpUpsConfigAutoShedOnTransition_Type()
)
tlpUpsConfigAutoShedOnTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoShedOnTransition.setStatus("current")


class _TlpUpsConfigBypassLowerLimitPercent_Type(Integer32):
    """Custom type tlpUpsConfigBypassLowerLimitPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, -5),
    )


_TlpUpsConfigBypassLowerLimitPercent_Type.__name__ = "Integer32"
_TlpUpsConfigBypassLowerLimitPercent_Object = MibTableColumn
tlpUpsConfigBypassLowerLimitPercent = _TlpUpsConfigBypassLowerLimitPercent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 10),
    _TlpUpsConfigBypassLowerLimitPercent_Type()
)
tlpUpsConfigBypassLowerLimitPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassLowerLimitPercent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassLowerLimitPercent.setUnits("percent")


class _TlpUpsConfigBypassUpperLimitPercent_Type(Integer32):
    """Custom type tlpUpsConfigBypassUpperLimitPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_TlpUpsConfigBypassUpperLimitPercent_Type.__name__ = "Integer32"
_TlpUpsConfigBypassUpperLimitPercent_Object = MibTableColumn
tlpUpsConfigBypassUpperLimitPercent = _TlpUpsConfigBypassUpperLimitPercent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 11),
    _TlpUpsConfigBypassUpperLimitPercent_Type()
)
tlpUpsConfigBypassUpperLimitPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassUpperLimitPercent.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassUpperLimitPercent.setUnits("percent")
_TlpUpsConfigBypassLowerLimitVoltage_Type = Unsigned32
_TlpUpsConfigBypassLowerLimitVoltage_Object = MibTableColumn
tlpUpsConfigBypassLowerLimitVoltage = _TlpUpsConfigBypassLowerLimitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 12),
    _TlpUpsConfigBypassLowerLimitVoltage_Type()
)
tlpUpsConfigBypassLowerLimitVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassLowerLimitVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassLowerLimitVoltage.setUnits("Volts")
_TlpUpsConfigBypassUpperLimitVoltage_Type = Unsigned32
_TlpUpsConfigBypassUpperLimitVoltage_Object = MibTableColumn
tlpUpsConfigBypassUpperLimitVoltage = _TlpUpsConfigBypassUpperLimitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 13),
    _TlpUpsConfigBypassUpperLimitVoltage_Type()
)
tlpUpsConfigBypassUpperLimitVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassUpperLimitVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBypassUpperLimitVoltage.setUnits("Volts")


class _TlpUpsConfigColdStart_Type(Integer32):
    """Custom type tlpUpsConfigColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigColdStart_Type.__name__ = "Integer32"
_TlpUpsConfigColdStart_Object = MibTableColumn
tlpUpsConfigColdStart = _TlpUpsConfigColdStart_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 14),
    _TlpUpsConfigColdStart_Type()
)
tlpUpsConfigColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigColdStart.setStatus("current")


class _TlpUpsConfigEconomicMode_Type(Integer32):
    """Custom type tlpUpsConfigEconomicMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("autoAdaptive", 5),
          ("constant50Hz", 2),
          ("constant60Hz", 3),
          ("constantAuto", 4),
          ("economy", 1),
          ("online", 0))
    )


_TlpUpsConfigEconomicMode_Type.__name__ = "Integer32"
_TlpUpsConfigEconomicMode_Object = MibTableColumn
tlpUpsConfigEconomicMode = _TlpUpsConfigEconomicMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 15),
    _TlpUpsConfigEconomicMode_Type()
)
tlpUpsConfigEconomicMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigEconomicMode.setStatus("current")


class _TlpUpsConfigFaultAction_Type(Integer32):
    """Custom type tlpUpsConfigFaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 0),
          ("standby", 1))
    )


_TlpUpsConfigFaultAction_Type.__name__ = "Integer32"
_TlpUpsConfigFaultAction_Object = MibTableColumn
tlpUpsConfigFaultAction = _TlpUpsConfigFaultAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 16),
    _TlpUpsConfigFaultAction_Type()
)
tlpUpsConfigFaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigFaultAction.setStatus("current")


class _TlpUpsConfigOffMode_Type(Integer32):
    """Custom type tlpUpsConfigOffMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 1),
          ("standby", 0))
    )


_TlpUpsConfigOffMode_Type.__name__ = "Integer32"
_TlpUpsConfigOffMode_Object = MibTableColumn
tlpUpsConfigOffMode = _TlpUpsConfigOffMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 17),
    _TlpUpsConfigOffMode_Type()
)
tlpUpsConfigOffMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOffMode.setStatus("current")


class _TlpUpsConfigLineSensitivity_Type(Integer32):
    """Custom type tlpUpsConfigLineSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullyReduced", 2),
          ("normal", 0),
          ("reduced", 1))
    )


_TlpUpsConfigLineSensitivity_Type.__name__ = "Integer32"
_TlpUpsConfigLineSensitivity_Object = MibTableColumn
tlpUpsConfigLineSensitivity = _TlpUpsConfigLineSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 1, 1, 18),
    _TlpUpsConfigLineSensitivity_Type()
)
tlpUpsConfigLineSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLineSensitivity.setStatus("current")
_TlpUpsConfigAutoRestartTable_Object = MibTable
tlpUpsConfigAutoRestartTable = _TlpUpsConfigAutoRestartTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartTable.setStatus("current")
_TlpUpsConfigAutoRestartEntry_Object = MibTableRow
tlpUpsConfigAutoRestartEntry = _TlpUpsConfigAutoRestartEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1)
)
tlpUpsConfigAutoRestartEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartEntry.setStatus("current")


class _TlpUpsConfigAutoRestartInverterShutdown_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartInverterShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartInverterShutdown_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartInverterShutdown_Object = MibTableColumn
tlpUpsConfigAutoRestartInverterShutdown = _TlpUpsConfigAutoRestartInverterShutdown_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 1),
    _TlpUpsConfigAutoRestartInverterShutdown_Type()
)
tlpUpsConfigAutoRestartInverterShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartInverterShutdown.setStatus("current")


class _TlpUpsConfigAutoRestartDelayedWakeup_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartDelayedWakeup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartDelayedWakeup_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartDelayedWakeup_Object = MibTableColumn
tlpUpsConfigAutoRestartDelayedWakeup = _TlpUpsConfigAutoRestartDelayedWakeup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 2),
    _TlpUpsConfigAutoRestartDelayedWakeup_Type()
)
tlpUpsConfigAutoRestartDelayedWakeup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartDelayedWakeup.setStatus("current")


class _TlpUpsConfigAutoRestartLowVoltageCutoff_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartLowVoltageCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartLowVoltageCutoff_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartLowVoltageCutoff_Object = MibTableColumn
tlpUpsConfigAutoRestartLowVoltageCutoff = _TlpUpsConfigAutoRestartLowVoltageCutoff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 3),
    _TlpUpsConfigAutoRestartLowVoltageCutoff_Type()
)
tlpUpsConfigAutoRestartLowVoltageCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartLowVoltageCutoff.setStatus("current")


class _TlpUpsConfigAutoRestartOverLoad_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartOverLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartOverLoad_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartOverLoad_Object = MibTableColumn
tlpUpsConfigAutoRestartOverLoad = _TlpUpsConfigAutoRestartOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 4),
    _TlpUpsConfigAutoRestartOverLoad_Type()
)
tlpUpsConfigAutoRestartOverLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartOverLoad.setStatus("current")


class _TlpUpsConfigAutoRestartOverTemperature_Type(Integer32):
    """Custom type tlpUpsConfigAutoRestartOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpUpsConfigAutoRestartOverTemperature_Type.__name__ = "Integer32"
_TlpUpsConfigAutoRestartOverTemperature_Object = MibTableColumn
tlpUpsConfigAutoRestartOverTemperature = _TlpUpsConfigAutoRestartOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 2, 1, 5),
    _TlpUpsConfigAutoRestartOverTemperature_Type()
)
tlpUpsConfigAutoRestartOverTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigAutoRestartOverTemperature.setStatus("current")
_TlpUpsConfigThresholdTable_Object = MibTable
tlpUpsConfigThresholdTable = _TlpUpsConfigThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tlpUpsConfigThresholdTable.setStatus("current")
_TlpUpsConfigThresholdEntry_Object = MibTableRow
tlpUpsConfigThresholdEntry = _TlpUpsConfigThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1)
)
tlpUpsConfigThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpUpsConfigThresholdEntry.setStatus("current")
_TlpUpsConfigBatteryAgeThreshold_Type = Unsigned32
_TlpUpsConfigBatteryAgeThreshold_Object = MibTableColumn
tlpUpsConfigBatteryAgeThreshold = _TlpUpsConfigBatteryAgeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 1),
    _TlpUpsConfigBatteryAgeThreshold_Type()
)
tlpUpsConfigBatteryAgeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryAgeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigBatteryAgeThreshold.setUnits("months")


class _TlpUpsConfigLowBatteryThreshold_Type(Integer32):
    """Custom type tlpUpsConfigLowBatteryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 95),
    )


_TlpUpsConfigLowBatteryThreshold_Type.__name__ = "Integer32"
_TlpUpsConfigLowBatteryThreshold_Object = MibTableColumn
tlpUpsConfigLowBatteryThreshold = _TlpUpsConfigLowBatteryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 2),
    _TlpUpsConfigLowBatteryThreshold_Type()
)
tlpUpsConfigLowBatteryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryThreshold.setUnits("percent")
_TlpUpsConfigLowBatteryTime_Type = Unsigned32
_TlpUpsConfigLowBatteryTime_Object = MibTableColumn
tlpUpsConfigLowBatteryTime = _TlpUpsConfigLowBatteryTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 3),
    _TlpUpsConfigLowBatteryTime_Type()
)
tlpUpsConfigLowBatteryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryTime.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigLowBatteryTime.setUnits("seconds")


class _TlpUpsConfigOverLoadThreshold_Type(Integer32):
    """Custom type tlpUpsConfigOverLoadThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 105),
    )


_TlpUpsConfigOverLoadThreshold_Type.__name__ = "Integer32"
_TlpUpsConfigOverLoadThreshold_Object = MibTableColumn
tlpUpsConfigOverLoadThreshold = _TlpUpsConfigOverLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1, 5, 3, 1, 4),
    _TlpUpsConfigOverLoadThreshold_Type()
)
tlpUpsConfigOverLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpUpsConfigOverLoadThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpUpsConfigOverLoadThreshold.setUnits("percent")
_TlpPdu_ObjectIdentity = ObjectIdentity
tlpPdu = _TlpPdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2)
)
_TlpPduIdent_ObjectIdentity = ObjectIdentity
tlpPduIdent = _TlpPduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1)
)
_TlpPduIdentNumPdu_Type = Unsigned32
_TlpPduIdentNumPdu_Object = MibScalar
tlpPduIdentNumPdu = _TlpPduIdentNumPdu_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 1),
    _TlpPduIdentNumPdu_Type()
)
tlpPduIdentNumPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumPdu.setStatus("current")
_TlpPduIdentTable_Object = MibTable
tlpPduIdentTable = _TlpPduIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tlpPduIdentTable.setStatus("current")
_TlpPduIdentEntry_Object = MibTableRow
tlpPduIdentEntry = _TlpPduIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1)
)
tlpPduIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduIdentEntry.setStatus("current")
_TlpPduIdentNumInputs_Type = Unsigned32
_TlpPduIdentNumInputs_Object = MibTableColumn
tlpPduIdentNumInputs = _TlpPduIdentNumInputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 1),
    _TlpPduIdentNumInputs_Type()
)
tlpPduIdentNumInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumInputs.setStatus("current")
_TlpPduIdentNumOutputs_Type = Unsigned32
_TlpPduIdentNumOutputs_Object = MibTableColumn
tlpPduIdentNumOutputs = _TlpPduIdentNumOutputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 2),
    _TlpPduIdentNumOutputs_Type()
)
tlpPduIdentNumOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumOutputs.setStatus("current")
_TlpPduIdentNumPhases_Type = Unsigned32
_TlpPduIdentNumPhases_Object = MibTableColumn
tlpPduIdentNumPhases = _TlpPduIdentNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 3),
    _TlpPduIdentNumPhases_Type()
)
tlpPduIdentNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumPhases.setStatus("current")
_TlpPduIdentNumOutlets_Type = Unsigned32
_TlpPduIdentNumOutlets_Object = MibTableColumn
tlpPduIdentNumOutlets = _TlpPduIdentNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 4),
    _TlpPduIdentNumOutlets_Type()
)
tlpPduIdentNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumOutlets.setStatus("current")
_TlpPduIdentNumOutletGroups_Type = Unsigned32
_TlpPduIdentNumOutletGroups_Object = MibTableColumn
tlpPduIdentNumOutletGroups = _TlpPduIdentNumOutletGroups_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 5),
    _TlpPduIdentNumOutletGroups_Type()
)
tlpPduIdentNumOutletGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumOutletGroups.setStatus("current")
_TlpPduIdentNumCircuits_Type = Unsigned32
_TlpPduIdentNumCircuits_Object = MibTableColumn
tlpPduIdentNumCircuits = _TlpPduIdentNumCircuits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 6),
    _TlpPduIdentNumCircuits_Type()
)
tlpPduIdentNumCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumCircuits.setStatus("current")
_TlpPduIdentNumBreakers_Type = Unsigned32
_TlpPduIdentNumBreakers_Object = MibTableColumn
tlpPduIdentNumBreakers = _TlpPduIdentNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 7),
    _TlpPduIdentNumBreakers_Type()
)
tlpPduIdentNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumBreakers.setStatus("current")
_TlpPduIdentNumHeatsinks_Type = Unsigned32
_TlpPduIdentNumHeatsinks_Object = MibTableColumn
tlpPduIdentNumHeatsinks = _TlpPduIdentNumHeatsinks_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 2, 1, 8),
    _TlpPduIdentNumHeatsinks_Type()
)
tlpPduIdentNumHeatsinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduIdentNumHeatsinks.setStatus("current")
_TlpPduSupportsTable_Object = MibTable
tlpPduSupportsTable = _TlpPduSupportsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tlpPduSupportsTable.setStatus("current")
_TlpPduSupportsEntry_Object = MibTableRow
tlpPduSupportsEntry = _TlpPduSupportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1)
)
tlpPduSupportsEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduSupportsEntry.setStatus("current")
_TlpPduSupportsEnergywise_Type = TruthValue
_TlpPduSupportsEnergywise_Object = MibTableColumn
tlpPduSupportsEnergywise = _TlpPduSupportsEnergywise_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 1),
    _TlpPduSupportsEnergywise_Type()
)
tlpPduSupportsEnergywise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsEnergywise.setStatus("current")
_TlpPduSupportsRampShed_Type = TruthValue
_TlpPduSupportsRampShed_Object = MibTableColumn
tlpPduSupportsRampShed = _TlpPduSupportsRampShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 2),
    _TlpPduSupportsRampShed_Type()
)
tlpPduSupportsRampShed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsRampShed.setStatus("current")
_TlpPduSupportsOutletGroup_Type = TruthValue
_TlpPduSupportsOutletGroup_Object = MibTableColumn
tlpPduSupportsOutletGroup = _TlpPduSupportsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 3),
    _TlpPduSupportsOutletGroup_Type()
)
tlpPduSupportsOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsOutletGroup.setStatus("current")
_TlpPduSupportsOutletCurrentPower_Type = TruthValue
_TlpPduSupportsOutletCurrentPower_Object = MibTableColumn
tlpPduSupportsOutletCurrentPower = _TlpPduSupportsOutletCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 4),
    _TlpPduSupportsOutletCurrentPower_Type()
)
tlpPduSupportsOutletCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsOutletCurrentPower.setStatus("current")
_TlpPduSupportsOutletVoltage_Type = TruthValue
_TlpPduSupportsOutletVoltage_Object = MibTableColumn
tlpPduSupportsOutletVoltage = _TlpPduSupportsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 3, 1, 5),
    _TlpPduSupportsOutletVoltage_Type()
)
tlpPduSupportsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduSupportsOutletVoltage.setStatus("current")
_TlpPduDisplayTable_Object = MibTable
tlpPduDisplayTable = _TlpPduDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tlpPduDisplayTable.setStatus("current")
_TlpPduDisplayEntry_Object = MibTableRow
tlpPduDisplayEntry = _TlpPduDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1)
)
tlpPduDisplayEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduDisplayEntry.setStatus("current")


class _TlpPduDisplayScheme_Type(Integer32):
    """Custom type tlpPduDisplayScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("schemeNormal", 1),
          ("schemeReverse", 0))
    )


_TlpPduDisplayScheme_Type.__name__ = "Integer32"
_TlpPduDisplayScheme_Object = MibTableColumn
tlpPduDisplayScheme = _TlpPduDisplayScheme_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 1),
    _TlpPduDisplayScheme_Type()
)
tlpPduDisplayScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayScheme.setStatus("current")


class _TlpPduDisplayOrientation_Type(Integer32):
    """Custom type tlpPduDisplayOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("displayNormal", 0),
          ("displayReverse", 1))
    )


_TlpPduDisplayOrientation_Type.__name__ = "Integer32"
_TlpPduDisplayOrientation_Object = MibTableColumn
tlpPduDisplayOrientation = _TlpPduDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 2),
    _TlpPduDisplayOrientation_Type()
)
tlpPduDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayOrientation.setStatus("current")


class _TlpPduDisplayAutoScroll_Type(Integer32):
    """Custom type tlpPduDisplayAutoScroll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("scrollDisabled", 0),
          ("scrollEnabled", 1))
    )


_TlpPduDisplayAutoScroll_Type.__name__ = "Integer32"
_TlpPduDisplayAutoScroll_Object = MibTableColumn
tlpPduDisplayAutoScroll = _TlpPduDisplayAutoScroll_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 3),
    _TlpPduDisplayAutoScroll_Type()
)
tlpPduDisplayAutoScroll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayAutoScroll.setStatus("current")


class _TlpPduDisplayIntensity_Type(Integer32):
    """Custom type tlpPduDisplayIntensity based on Integer32"""
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
        *(("intensity100", 4),
          ("intensity25", 1),
          ("intensity50", 2),
          ("intensity75", 3))
    )


_TlpPduDisplayIntensity_Type.__name__ = "Integer32"
_TlpPduDisplayIntensity_Object = MibTableColumn
tlpPduDisplayIntensity = _TlpPduDisplayIntensity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 4),
    _TlpPduDisplayIntensity_Type()
)
tlpPduDisplayIntensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayIntensity.setStatus("current")


class _TlpPduDisplayUnits_Type(Integer32):
    """Custom type tlpPduDisplayUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("metric", 1),
          ("normal", 0))
    )


_TlpPduDisplayUnits_Type.__name__ = "Integer32"
_TlpPduDisplayUnits_Object = MibTableColumn
tlpPduDisplayUnits = _TlpPduDisplayUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 1, 4, 1, 5),
    _TlpPduDisplayUnits_Type()
)
tlpPduDisplayUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDisplayUnits.setStatus("current")
_TlpPduDevice_ObjectIdentity = ObjectIdentity
tlpPduDevice = _TlpPduDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2)
)
_TlpPduDeviceTable_Object = MibTable
tlpPduDeviceTable = _TlpPduDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tlpPduDeviceTable.setStatus("current")
_TlpPduDeviceEntry_Object = MibTableRow
tlpPduDeviceEntry = _TlpPduDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1)
)
tlpPduDeviceEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduDeviceEntry.setStatus("current")


class _TlpPduDeviceMainLoadState_Type(Integer32):
    """Custom type tlpPduDeviceMainLoadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlpPduDeviceMainLoadState_Type.__name__ = "Integer32"
_TlpPduDeviceMainLoadState_Object = MibTableColumn
tlpPduDeviceMainLoadState = _TlpPduDeviceMainLoadState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 1),
    _TlpPduDeviceMainLoadState_Type()
)
tlpPduDeviceMainLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceMainLoadState.setStatus("current")
_TlpPduDeviceMainLoadControllable_Type = TruthValue
_TlpPduDeviceMainLoadControllable_Object = MibTableColumn
tlpPduDeviceMainLoadControllable = _TlpPduDeviceMainLoadControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 2),
    _TlpPduDeviceMainLoadControllable_Type()
)
tlpPduDeviceMainLoadControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceMainLoadControllable.setStatus("current")


class _TlpPduDeviceMainLoadCommand_Type(Integer32):
    """Custom type tlpPduDeviceMainLoadCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlpPduDeviceMainLoadCommand_Type.__name__ = "Integer32"
_TlpPduDeviceMainLoadCommand_Object = MibTableColumn
tlpPduDeviceMainLoadCommand = _TlpPduDeviceMainLoadCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 3),
    _TlpPduDeviceMainLoadCommand_Type()
)
tlpPduDeviceMainLoadCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDeviceMainLoadCommand.setStatus("current")
_TlpPduDevicePowerOnDelay_Type = Integer32
_TlpPduDevicePowerOnDelay_Object = MibTableColumn
tlpPduDevicePowerOnDelay = _TlpPduDevicePowerOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 4),
    _TlpPduDevicePowerOnDelay_Type()
)
tlpPduDevicePowerOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduDevicePowerOnDelay.setStatus("current")
_TlpPduDeviceTotalInputPowerRating_Type = Integer32
_TlpPduDeviceTotalInputPowerRating_Object = MibTableColumn
tlpPduDeviceTotalInputPowerRating = _TlpPduDeviceTotalInputPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 5),
    _TlpPduDeviceTotalInputPowerRating_Type()
)
tlpPduDeviceTotalInputPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceTotalInputPowerRating.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceTotalInputPowerRating.setUnits("Watts")
_TlpPduDeviceTemperatureC_Type = Integer32
_TlpPduDeviceTemperatureC_Object = MibTableColumn
tlpPduDeviceTemperatureC = _TlpPduDeviceTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 6),
    _TlpPduDeviceTemperatureC_Type()
)
tlpPduDeviceTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceTemperatureC.setUnits("degrees Centigrade")
_TlpPduDeviceTemperatureF_Type = Integer32
_TlpPduDeviceTemperatureF_Object = MibTableColumn
tlpPduDeviceTemperatureF = _TlpPduDeviceTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 7),
    _TlpPduDeviceTemperatureF_Type()
)
tlpPduDeviceTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceTemperatureF.setUnits("degrees Farenheit")


class _TlpPduDevicePhaseImbalance_Type(Integer32):
    """Custom type tlpPduDevicePhaseImbalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TlpPduDevicePhaseImbalance_Type.__name__ = "Integer32"
_TlpPduDevicePhaseImbalance_Object = MibTableColumn
tlpPduDevicePhaseImbalance = _TlpPduDevicePhaseImbalance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 8),
    _TlpPduDevicePhaseImbalance_Type()
)
tlpPduDevicePhaseImbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDevicePhaseImbalance.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDevicePhaseImbalance.setUnits("percent")
_TlpPduDeviceOutputPowerTotal_Type = Unsigned32
_TlpPduDeviceOutputPowerTotal_Object = MibTableColumn
tlpPduDeviceOutputPowerTotal = _TlpPduDeviceOutputPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 9),
    _TlpPduDeviceOutputPowerTotal_Type()
)
tlpPduDeviceOutputPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputPowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputPowerTotal.setUnits("Watts")
_TlpPduDeviceAggregatePowerFactor_Type = Unsigned32
_TlpPduDeviceAggregatePowerFactor_Object = MibTableColumn
tlpPduDeviceAggregatePowerFactor = _TlpPduDeviceAggregatePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 10),
    _TlpPduDeviceAggregatePowerFactor_Type()
)
tlpPduDeviceAggregatePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceAggregatePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduDeviceAggregatePowerFactor.setUnits("0.1 Watts")


class _TlpPduDeviceOutputCurrentPrecision_Type(Integer32):
    """Custom type tlpPduDeviceOutputCurrentPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hundredths", 2),
          ("none", 0),
          ("tenths", 1))
    )


_TlpPduDeviceOutputCurrentPrecision_Type.__name__ = "Integer32"
_TlpPduDeviceOutputCurrentPrecision_Object = MibTableColumn
tlpPduDeviceOutputCurrentPrecision = _TlpPduDeviceOutputCurrentPrecision_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 2, 1, 1, 11),
    _TlpPduDeviceOutputCurrentPrecision_Type()
)
tlpPduDeviceOutputCurrentPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduDeviceOutputCurrentPrecision.setStatus("current")
_TlpPduDetail_ObjectIdentity = ObjectIdentity
tlpPduDetail = _TlpPduDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3)
)
_TlpPduInput_ObjectIdentity = ObjectIdentity
tlpPduInput = _TlpPduInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1)
)
_TlpPduInputTable_Object = MibTable
tlpPduInputTable = _TlpPduInputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tlpPduInputTable.setStatus("current")
_TlpPduInputEntry_Object = MibTableRow
tlpPduInputEntry = _TlpPduInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1)
)
tlpPduInputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduInputEntry.setStatus("current")
_TlpPduInputNominalVoltage_Type = Unsigned32
_TlpPduInputNominalVoltage_Object = MibTableColumn
tlpPduInputNominalVoltage = _TlpPduInputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 1),
    _TlpPduInputNominalVoltage_Type()
)
tlpPduInputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltage.setStatus("current")
_TlpPduInputNominalVoltagePhaseToPhase_Type = Unsigned32
_TlpPduInputNominalVoltagePhaseToPhase_Object = MibTableColumn
tlpPduInputNominalVoltagePhaseToPhase = _TlpPduInputNominalVoltagePhaseToPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 2),
    _TlpPduInputNominalVoltagePhaseToPhase_Type()
)
tlpPduInputNominalVoltagePhaseToPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltagePhaseToPhase.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltagePhaseToPhase.setUnits("0.1 Volt DC")
_TlpPduInputNominalVoltagePhaseToNeutral_Type = Unsigned32
_TlpPduInputNominalVoltagePhaseToNeutral_Object = MibTableColumn
tlpPduInputNominalVoltagePhaseToNeutral = _TlpPduInputNominalVoltagePhaseToNeutral_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 3),
    _TlpPduInputNominalVoltagePhaseToNeutral_Type()
)
tlpPduInputNominalVoltagePhaseToNeutral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltagePhaseToNeutral.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputNominalVoltagePhaseToNeutral.setUnits("0.1 Volt DC")
_TlpPduInputLowTransferVoltage_Type = Unsigned32
_TlpPduInputLowTransferVoltage_Object = MibTableColumn
tlpPduInputLowTransferVoltage = _TlpPduInputLowTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 4),
    _TlpPduInputLowTransferVoltage_Type()
)
tlpPduInputLowTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltage.setUnits("0.1 Volts")
_TlpPduInputLowTransferVoltageLowerBound_Type = Unsigned32
_TlpPduInputLowTransferVoltageLowerBound_Object = MibTableColumn
tlpPduInputLowTransferVoltageLowerBound = _TlpPduInputLowTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 5),
    _TlpPduInputLowTransferVoltageLowerBound_Type()
)
tlpPduInputLowTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltageLowerBound.setUnits("Volts")
_TlpPduInputLowTransferVoltageUpperBound_Type = Unsigned32
_TlpPduInputLowTransferVoltageUpperBound_Object = MibTableColumn
tlpPduInputLowTransferVoltageUpperBound = _TlpPduInputLowTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 6),
    _TlpPduInputLowTransferVoltageUpperBound_Type()
)
tlpPduInputLowTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputLowTransferVoltageUpperBound.setUnits("Volts")
_TlpPduInputHighTransferVoltage_Type = Unsigned32
_TlpPduInputHighTransferVoltage_Object = MibTableColumn
tlpPduInputHighTransferVoltage = _TlpPduInputHighTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 7),
    _TlpPduInputHighTransferVoltage_Type()
)
tlpPduInputHighTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltage.setUnits("0.1 Volts")
_TlpPduInputHighTransferVoltageLowerBound_Type = Unsigned32
_TlpPduInputHighTransferVoltageLowerBound_Object = MibTableColumn
tlpPduInputHighTransferVoltageLowerBound = _TlpPduInputHighTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 8),
    _TlpPduInputHighTransferVoltageLowerBound_Type()
)
tlpPduInputHighTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltageLowerBound.setUnits("Volts")
_TlpPduInputHighTransferVoltageUpperBound_Type = Unsigned32
_TlpPduInputHighTransferVoltageUpperBound_Object = MibTableColumn
tlpPduInputHighTransferVoltageUpperBound = _TlpPduInputHighTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 9),
    _TlpPduInputHighTransferVoltageUpperBound_Type()
)
tlpPduInputHighTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputHighTransferVoltageUpperBound.setUnits("Volts")
_TlpPduInputCurrentLimit_Type = Unsigned32
_TlpPduInputCurrentLimit_Object = MibTableColumn
tlpPduInputCurrentLimit = _TlpPduInputCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 1, 1, 10),
    _TlpPduInputCurrentLimit_Type()
)
tlpPduInputCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputCurrentLimit.setUnits("Amp DC")
_TlpPduInputPhaseTable_Object = MibTable
tlpPduInputPhaseTable = _TlpPduInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpPduInputPhaseTable.setStatus("current")
_TlpPduInputPhaseEntry_Object = MibTableRow
tlpPduInputPhaseEntry = _TlpPduInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1)
)
tlpPduInputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpPduInputPhaseEntry.setStatus("current")
_TlpPduInputPhaseIndex_Type = Unsigned32
_TlpPduInputPhaseIndex_Object = MibTableColumn
tlpPduInputPhaseIndex = _TlpPduInputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 1),
    _TlpPduInputPhaseIndex_Type()
)
tlpPduInputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhaseIndex.setStatus("current")


class _TlpPduInputPhasePhaseType_Type(Integer32):
    """Custom type tlpPduInputPhasePhaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phaseToNeutral", 0),
          ("phaseToPhase", 1))
    )


_TlpPduInputPhasePhaseType_Type.__name__ = "Integer32"
_TlpPduInputPhasePhaseType_Object = MibTableColumn
tlpPduInputPhasePhaseType = _TlpPduInputPhasePhaseType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 2),
    _TlpPduInputPhasePhaseType_Type()
)
tlpPduInputPhasePhaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhasePhaseType.setStatus("current")
_TlpPduInputPhaseFrequency_Type = Unsigned32
_TlpPduInputPhaseFrequency_Object = MibTableColumn
tlpPduInputPhaseFrequency = _TlpPduInputPhaseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 3),
    _TlpPduInputPhaseFrequency_Type()
)
tlpPduInputPhaseFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhaseFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseFrequency.setUnits("0.1 Hertz")
_TlpPduInputPhaseVoltage_Type = Unsigned32
_TlpPduInputPhaseVoltage_Object = MibTableColumn
tlpPduInputPhaseVoltage = _TlpPduInputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 4),
    _TlpPduInputPhaseVoltage_Type()
)
tlpPduInputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltage.setUnits("0.1 Volt DC")
_TlpPduInputPhaseVoltageMin_Type = Unsigned32
_TlpPduInputPhaseVoltageMin_Object = MibTableColumn
tlpPduInputPhaseVoltageMin = _TlpPduInputPhaseVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 5),
    _TlpPduInputPhaseVoltageMin_Type()
)
tlpPduInputPhaseVoltageMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltageMin.setUnits("0.1 Volt DC")
_TlpPduInputPhaseVoltageMax_Type = Unsigned32
_TlpPduInputPhaseVoltageMax_Object = MibTableColumn
tlpPduInputPhaseVoltageMax = _TlpPduInputPhaseVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 6),
    _TlpPduInputPhaseVoltageMax_Type()
)
tlpPduInputPhaseVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseVoltageMax.setUnits("0.1 Volt DC")
_TlpPduInputPhaseCurrent_Type = Unsigned32
_TlpPduInputPhaseCurrent_Object = MibTableColumn
tlpPduInputPhaseCurrent = _TlpPduInputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 1, 2, 1, 7),
    _TlpPduInputPhaseCurrent_Type()
)
tlpPduInputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduInputPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduInputPhaseCurrent.setUnits("0.01 Amp DC")
_TlpPduOutput_ObjectIdentity = ObjectIdentity
tlpPduOutput = _TlpPduOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2)
)
_TlpPduOutputTable_Object = MibTable
tlpPduOutputTable = _TlpPduOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tlpPduOutputTable.setStatus("current")
_TlpPduOutputEntry_Object = MibTableRow
tlpPduOutputEntry = _TlpPduOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1)
)
tlpPduOutputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduOutputIndex"),
)
if mibBuilder.loadTexts:
    tlpPduOutputEntry.setStatus("current")
_TlpPduOutputIndex_Type = Unsigned32
_TlpPduOutputIndex_Object = MibTableColumn
tlpPduOutputIndex = _TlpPduOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 1),
    _TlpPduOutputIndex_Type()
)
tlpPduOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputIndex.setStatus("current")


class _TlpPduOutputPhase_Type(Integer32):
    """Custom type tlpPduOutputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_TlpPduOutputPhase_Type.__name__ = "Integer32"
_TlpPduOutputPhase_Object = MibTableColumn
tlpPduOutputPhase = _TlpPduOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 2),
    _TlpPduOutputPhase_Type()
)
tlpPduOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputPhase.setStatus("current")


class _TlpPduOutputPhaseType_Type(Integer32):
    """Custom type tlpPduOutputPhaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phaseToNeutral", 0),
          ("phaseToPhase", 1))
    )


_TlpPduOutputPhaseType_Type.__name__ = "Integer32"
_TlpPduOutputPhaseType_Object = MibTableColumn
tlpPduOutputPhaseType = _TlpPduOutputPhaseType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 3),
    _TlpPduOutputPhaseType_Type()
)
tlpPduOutputPhaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputPhaseType.setStatus("current")
_TlpPduOutputVoltage_Type = Unsigned32
_TlpPduOutputVoltage_Object = MibTableColumn
tlpPduOutputVoltage = _TlpPduOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 4),
    _TlpPduOutputVoltage_Type()
)
tlpPduOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputVoltage.setUnits("0.1 Volt DC")
_TlpPduOutputCurrent_Type = Unsigned32
_TlpPduOutputCurrent_Object = MibTableColumn
tlpPduOutputCurrent = _TlpPduOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 5),
    _TlpPduOutputCurrent_Type()
)
tlpPduOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputCurrent.setUnits("0.01 Amp DC")
_TlpPduOutputCurrentMin_Type = Unsigned32
_TlpPduOutputCurrentMin_Object = MibTableColumn
tlpPduOutputCurrentMin = _TlpPduOutputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 6),
    _TlpPduOutputCurrentMin_Type()
)
tlpPduOutputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputCurrentMin.setUnits("0.01 Amp DC")
_TlpPduOutputCurrentMax_Type = Unsigned32
_TlpPduOutputCurrentMax_Object = MibTableColumn
tlpPduOutputCurrentMax = _TlpPduOutputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 7),
    _TlpPduOutputCurrentMax_Type()
)
tlpPduOutputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputCurrentMax.setUnits("0.01 Amp DC")
_TlpPduOutputActivePower_Type = Unsigned32
_TlpPduOutputActivePower_Object = MibTableColumn
tlpPduOutputActivePower = _TlpPduOutputActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 8),
    _TlpPduOutputActivePower_Type()
)
tlpPduOutputActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputActivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputActivePower.setUnits("Watts")
_TlpPduOutputPowerFactor_Type = Unsigned32
_TlpPduOutputPowerFactor_Object = MibTableColumn
tlpPduOutputPowerFactor = _TlpPduOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 9),
    _TlpPduOutputPowerFactor_Type()
)
tlpPduOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutputPowerFactor.setUnits("0.01 percent")


class _TlpPduOutputSource_Type(Integer32):
    """Custom type tlpPduOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("normal", 1))
    )


_TlpPduOutputSource_Type.__name__ = "Integer32"
_TlpPduOutputSource_Object = MibTableColumn
tlpPduOutputSource = _TlpPduOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 2, 1, 1, 10),
    _TlpPduOutputSource_Type()
)
tlpPduOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutputSource.setStatus("current")
_TlpPduOutlet_ObjectIdentity = ObjectIdentity
tlpPduOutlet = _TlpPduOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3)
)
_TlpPduOutletTable_Object = MibTable
tlpPduOutletTable = _TlpPduOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpPduOutletTable.setStatus("current")
_TlpPduOutletEntry_Object = MibTableRow
tlpPduOutletEntry = _TlpPduOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1)
)
tlpPduOutletEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduOutletIndex"),
)
if mibBuilder.loadTexts:
    tlpPduOutletEntry.setStatus("current")
_TlpPduOutletIndex_Type = Unsigned32
_TlpPduOutletIndex_Object = MibTableColumn
tlpPduOutletIndex = _TlpPduOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 1),
    _TlpPduOutletIndex_Type()
)
tlpPduOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletIndex.setStatus("current")
_TlpPduOutletName_Type = DisplayString
_TlpPduOutletName_Object = MibTableColumn
tlpPduOutletName = _TlpPduOutletName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 2),
    _TlpPduOutletName_Type()
)
tlpPduOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletName.setStatus("current")
_TlpPduOutletDescription_Type = DisplayString
_TlpPduOutletDescription_Object = MibTableColumn
tlpPduOutletDescription = _TlpPduOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 3),
    _TlpPduOutletDescription_Type()
)
tlpPduOutletDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletDescription.setStatus("current")


class _TlpPduOutletState_Type(Integer32):
    """Custom type tlpPduOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlpPduOutletState_Type.__name__ = "Integer32"
_TlpPduOutletState_Object = MibTableColumn
tlpPduOutletState = _TlpPduOutletState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 4),
    _TlpPduOutletState_Type()
)
tlpPduOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletState.setStatus("current")
_TlpPduOutletControllable_Type = TruthValue
_TlpPduOutletControllable_Object = MibTableColumn
tlpPduOutletControllable = _TlpPduOutletControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 5),
    _TlpPduOutletControllable_Type()
)
tlpPduOutletControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletControllable.setStatus("current")


class _TlpPduOutletCommand_Type(Integer32):
    """Custom type tlpPduOutletCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlpPduOutletCommand_Type.__name__ = "Integer32"
_TlpPduOutletCommand_Object = MibTableColumn
tlpPduOutletCommand = _TlpPduOutletCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 6),
    _TlpPduOutletCommand_Type()
)
tlpPduOutletCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletCommand.setStatus("current")
_TlpPduOutletVoltage_Type = Unsigned32
_TlpPduOutletVoltage_Object = MibTableColumn
tlpPduOutletVoltage = _TlpPduOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 7),
    _TlpPduOutletVoltage_Type()
)
tlpPduOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletVoltage.setUnits("0.1 Volt DC")
_TlpPduOutletCurrent_Type = Unsigned32
_TlpPduOutletCurrent_Object = MibTableColumn
tlpPduOutletCurrent = _TlpPduOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 8),
    _TlpPduOutletCurrent_Type()
)
tlpPduOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletCurrent.setUnits("0.01 RMS Amp")
_TlpPduOutletPower_Type = Unsigned32
_TlpPduOutletPower_Object = MibTableColumn
tlpPduOutletPower = _TlpPduOutletPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 9),
    _TlpPduOutletPower_Type()
)
tlpPduOutletPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletPower.setUnits("Watts")


class _TlpPduOutletRampAction_Type(Integer32):
    """Custom type tlpPduOutletRampAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOff", 0),
          ("turnOnAfterDelay", 1))
    )


_TlpPduOutletRampAction_Type.__name__ = "Integer32"
_TlpPduOutletRampAction_Object = MibTableColumn
tlpPduOutletRampAction = _TlpPduOutletRampAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 10),
    _TlpPduOutletRampAction_Type()
)
tlpPduOutletRampAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletRampAction.setStatus("current")
_TlpPduOutletRampDelay_Type = Integer32
_TlpPduOutletRampDelay_Object = MibTableColumn
tlpPduOutletRampDelay = _TlpPduOutletRampDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 11),
    _TlpPduOutletRampDelay_Type()
)
tlpPduOutletRampDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletRampDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletRampDelay.setUnits("seconds")


class _TlpPduOutletShedAction_Type(Integer32):
    """Custom type tlpPduOutletShedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOn", 0),
          ("turnOffAfterDelay", 1))
    )


_TlpPduOutletShedAction_Type.__name__ = "Integer32"
_TlpPduOutletShedAction_Object = MibTableColumn
tlpPduOutletShedAction = _TlpPduOutletShedAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 12),
    _TlpPduOutletShedAction_Type()
)
tlpPduOutletShedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletShedAction.setStatus("current")
_TlpPduOutletShedDelay_Type = Integer32
_TlpPduOutletShedDelay_Object = MibTableColumn
tlpPduOutletShedDelay = _TlpPduOutletShedDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 13),
    _TlpPduOutletShedDelay_Type()
)
tlpPduOutletShedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletShedDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduOutletShedDelay.setUnits("seconds")
_TlpPduOutletGroup_Type = Integer32
_TlpPduOutletGroup_Object = MibTableColumn
tlpPduOutletGroup = _TlpPduOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 14),
    _TlpPduOutletGroup_Type()
)
tlpPduOutletGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroup.setStatus("current")
_TlpPduOutletBank_Type = Integer32
_TlpPduOutletBank_Object = MibTableColumn
tlpPduOutletBank = _TlpPduOutletBank_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 15),
    _TlpPduOutletBank_Type()
)
tlpPduOutletBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletBank.setStatus("current")
_TlpPduOutletCircuit_Type = Integer32
_TlpPduOutletCircuit_Object = MibTableColumn
tlpPduOutletCircuit = _TlpPduOutletCircuit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 16),
    _TlpPduOutletCircuit_Type()
)
tlpPduOutletCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletCircuit.setStatus("current")


class _TlpPduOutletPhase_Type(Integer32):
    """Custom type tlpPduOutletPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase1-2", 4),
          ("phase2", 2),
          ("phase2-3", 5),
          ("phase3", 3),
          ("phase3-1", 6),
          ("unknown", 0))
    )


_TlpPduOutletPhase_Type.__name__ = "Integer32"
_TlpPduOutletPhase_Object = MibTableColumn
tlpPduOutletPhase = _TlpPduOutletPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 1, 1, 17),
    _TlpPduOutletPhase_Type()
)
tlpPduOutletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletPhase.setStatus("current")
_TlpPduOutletGroupTable_Object = MibTable
tlpPduOutletGroupTable = _TlpPduOutletGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpPduOutletGroupTable.setStatus("current")
_TlpPduOutletGroupEntry_Object = MibTableRow
tlpPduOutletGroupEntry = _TlpPduOutletGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1)
)
tlpPduOutletGroupEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduOutletGroupIndex"),
)
if mibBuilder.loadTexts:
    tlpPduOutletGroupEntry.setStatus("current")
_TlpPduOutletGroupIndex_Type = Unsigned32
_TlpPduOutletGroupIndex_Object = MibTableColumn
tlpPduOutletGroupIndex = _TlpPduOutletGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 1),
    _TlpPduOutletGroupIndex_Type()
)
tlpPduOutletGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletGroupIndex.setStatus("current")
_TlpPduOutletGroupRowStatus_Type = RowStatus
_TlpPduOutletGroupRowStatus_Object = MibTableColumn
tlpPduOutletGroupRowStatus = _TlpPduOutletGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 2),
    _TlpPduOutletGroupRowStatus_Type()
)
tlpPduOutletGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroupRowStatus.setStatus("current")
_TlpPduOutletGroupName_Type = DisplayString
_TlpPduOutletGroupName_Object = MibTableColumn
tlpPduOutletGroupName = _TlpPduOutletGroupName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 3),
    _TlpPduOutletGroupName_Type()
)
tlpPduOutletGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroupName.setStatus("current")
_TlpPduOutletGroupDescription_Type = DisplayString
_TlpPduOutletGroupDescription_Object = MibTableColumn
tlpPduOutletGroupDescription = _TlpPduOutletGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 4),
    _TlpPduOutletGroupDescription_Type()
)
tlpPduOutletGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroupDescription.setStatus("current")


class _TlpPduOutletGroupState_Type(Integer32):
    """Custom type tlpPduOutletGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 3),
          ("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlpPduOutletGroupState_Type.__name__ = "Integer32"
_TlpPduOutletGroupState_Object = MibTableColumn
tlpPduOutletGroupState = _TlpPduOutletGroupState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 5),
    _TlpPduOutletGroupState_Type()
)
tlpPduOutletGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduOutletGroupState.setStatus("current")


class _TlpPduOutletGroupCommand_Type(Integer32):
    """Custom type tlpPduOutletGroupCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlpPduOutletGroupCommand_Type.__name__ = "Integer32"
_TlpPduOutletGroupCommand_Object = MibTableColumn
tlpPduOutletGroupCommand = _TlpPduOutletGroupCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 3, 2, 1, 6),
    _TlpPduOutletGroupCommand_Type()
)
tlpPduOutletGroupCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduOutletGroupCommand.setStatus("current")
_TlpPduCircuit_ObjectIdentity = ObjectIdentity
tlpPduCircuit = _TlpPduCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4)
)
_TlpPduCircuitTable_Object = MibTable
tlpPduCircuitTable = _TlpPduCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpPduCircuitTable.setStatus("current")
_TlpPduCircuitEntry_Object = MibTableRow
tlpPduCircuitEntry = _TlpPduCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1)
)
tlpPduCircuitEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduCircuitIndex"),
)
if mibBuilder.loadTexts:
    tlpPduCircuitEntry.setStatus("current")
_TlpPduCircuitIndex_Type = Unsigned32
_TlpPduCircuitIndex_Object = MibTableColumn
tlpPduCircuitIndex = _TlpPduCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 1),
    _TlpPduCircuitIndex_Type()
)
tlpPduCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitIndex.setStatus("current")


class _TlpPduCircuitPhase_Type(Integer32):
    """Custom type tlpPduCircuitPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase1-2", 4),
          ("phase2", 2),
          ("phase2-3", 5),
          ("phase3", 3),
          ("phase3-1", 6),
          ("unknown", 0))
    )


_TlpPduCircuitPhase_Type.__name__ = "Integer32"
_TlpPduCircuitPhase_Object = MibTableColumn
tlpPduCircuitPhase = _TlpPduCircuitPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 2),
    _TlpPduCircuitPhase_Type()
)
tlpPduCircuitPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitPhase.setStatus("current")
_TlpPduCircuitInputVoltage_Type = Integer32
_TlpPduCircuitInputVoltage_Object = MibTableColumn
tlpPduCircuitInputVoltage = _TlpPduCircuitInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 3),
    _TlpPduCircuitInputVoltage_Type()
)
tlpPduCircuitInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitInputVoltage.setUnits("0.1 Volt DC")
_TlpPduCircuitTotalCurrent_Type = Integer32
_TlpPduCircuitTotalCurrent_Object = MibTableColumn
tlpPduCircuitTotalCurrent = _TlpPduCircuitTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 4),
    _TlpPduCircuitTotalCurrent_Type()
)
tlpPduCircuitTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitTotalCurrent.setUnits("0.01 Amp DC")
_TlpPduCircuitCurrentLimit_Type = Integer32
_TlpPduCircuitCurrentLimit_Object = MibTableColumn
tlpPduCircuitCurrentLimit = _TlpPduCircuitCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 5),
    _TlpPduCircuitCurrentLimit_Type()
)
tlpPduCircuitCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentLimit.setUnits("0.01 Amp DC")
_TlpPduCircuitCurrentMin_Type = Integer32
_TlpPduCircuitCurrentMin_Object = MibTableColumn
tlpPduCircuitCurrentMin = _TlpPduCircuitCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 6),
    _TlpPduCircuitCurrentMin_Type()
)
tlpPduCircuitCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentMin.setUnits("0.01 Amp DC")
_TlpPduCircuitCurrentMax_Type = Integer32
_TlpPduCircuitCurrentMax_Object = MibTableColumn
tlpPduCircuitCurrentMax = _TlpPduCircuitCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 7),
    _TlpPduCircuitCurrentMax_Type()
)
tlpPduCircuitCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitCurrentMax.setUnits("0.01 Amp DC")
_TlpPduCircuitTotalPower_Type = Integer32
_TlpPduCircuitTotalPower_Object = MibTableColumn
tlpPduCircuitTotalPower = _TlpPduCircuitTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 8),
    _TlpPduCircuitTotalPower_Type()
)
tlpPduCircuitTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitTotalPower.setUnits("Watts")


class _TlpPduCircuitPowerFactor_Type(Integer32):
    """Custom type tlpPduCircuitPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TlpPduCircuitPowerFactor_Type.__name__ = "Integer32"
_TlpPduCircuitPowerFactor_Object = MibTableColumn
tlpPduCircuitPowerFactor = _TlpPduCircuitPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 9),
    _TlpPduCircuitPowerFactor_Type()
)
tlpPduCircuitPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitPowerFactor.setUnits("percent")
_TlpPduCircuitUtilization_Type = Unsigned32
_TlpPduCircuitUtilization_Object = MibTableColumn
tlpPduCircuitUtilization = _TlpPduCircuitUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 4, 1, 1, 10),
    _TlpPduCircuitUtilization_Type()
)
tlpPduCircuitUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduCircuitUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduCircuitUtilization.setUnits("0.01 %")
_TlpPduBreaker_ObjectIdentity = ObjectIdentity
tlpPduBreaker = _TlpPduBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5)
)
_TlpPduBreakerTable_Object = MibTable
tlpPduBreakerTable = _TlpPduBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpPduBreakerTable.setStatus("current")
_TlpPduBreakerEntry_Object = MibTableRow
tlpPduBreakerEntry = _TlpPduBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5, 1, 1)
)
tlpPduBreakerEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduBreakerIndex"),
)
if mibBuilder.loadTexts:
    tlpPduBreakerEntry.setStatus("current")
_TlpPduBreakerIndex_Type = Unsigned32
_TlpPduBreakerIndex_Object = MibTableColumn
tlpPduBreakerIndex = _TlpPduBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5, 1, 1, 1),
    _TlpPduBreakerIndex_Type()
)
tlpPduBreakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduBreakerIndex.setStatus("current")


class _TlpPduBreakerStatus_Type(Integer32):
    """Custom type tlpPduBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("notInstalled", 2),
          ("open", 0))
    )


_TlpPduBreakerStatus_Type.__name__ = "Integer32"
_TlpPduBreakerStatus_Object = MibTableColumn
tlpPduBreakerStatus = _TlpPduBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 5, 1, 1, 2),
    _TlpPduBreakerStatus_Type()
)
tlpPduBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduBreakerStatus.setStatus("current")
_TlpPduHeatsink_ObjectIdentity = ObjectIdentity
tlpPduHeatsink = _TlpPduHeatsink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6)
)
_TlpPduHeatsinkTable_Object = MibTable
tlpPduHeatsinkTable = _TlpPduHeatsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    tlpPduHeatsinkTable.setStatus("current")
_TlpPduHeatsinkEntry_Object = MibTableRow
tlpPduHeatsinkEntry = _TlpPduHeatsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1)
)
tlpPduHeatsinkEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpPduHeatsinkIndex"),
)
if mibBuilder.loadTexts:
    tlpPduHeatsinkEntry.setStatus("current")
_TlpPduHeatsinkIndex_Type = Unsigned32
_TlpPduHeatsinkIndex_Object = MibTableColumn
tlpPduHeatsinkIndex = _TlpPduHeatsinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1, 1),
    _TlpPduHeatsinkIndex_Type()
)
tlpPduHeatsinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduHeatsinkIndex.setStatus("current")


class _TlpPduHeatsinkStatus_Type(Integer32):
    """Custom type tlpPduHeatsinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 0))
    )


_TlpPduHeatsinkStatus_Type.__name__ = "Integer32"
_TlpPduHeatsinkStatus_Object = MibTableColumn
tlpPduHeatsinkStatus = _TlpPduHeatsinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1, 2),
    _TlpPduHeatsinkStatus_Type()
)
tlpPduHeatsinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduHeatsinkStatus.setStatus("current")
_TlpPduHeatsinkTemperatureC_Type = Integer32
_TlpPduHeatsinkTemperatureC_Object = MibTableColumn
tlpPduHeatsinkTemperatureC = _TlpPduHeatsinkTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1, 3),
    _TlpPduHeatsinkTemperatureC_Type()
)
tlpPduHeatsinkTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduHeatsinkTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduHeatsinkTemperatureC.setUnits("0.1 degrees Centigrade")
_TlpPduHeatsinkTemperatureF_Type = Integer32
_TlpPduHeatsinkTemperatureF_Object = MibTableColumn
tlpPduHeatsinkTemperatureF = _TlpPduHeatsinkTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 3, 6, 1, 1, 4),
    _TlpPduHeatsinkTemperatureF_Type()
)
tlpPduHeatsinkTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpPduHeatsinkTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpPduHeatsinkTemperatureF.setUnits("0.1 degrees Farenheit")
_TlpPduControl_ObjectIdentity = ObjectIdentity
tlpPduControl = _TlpPduControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4)
)
_TlpPduControlTable_Object = MibTable
tlpPduControlTable = _TlpPduControlTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tlpPduControlTable.setStatus("current")
_TlpPduControlEntry_Object = MibTableRow
tlpPduControlEntry = _TlpPduControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1)
)
tlpPduControlEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduControlEntry.setStatus("current")
_TlpPduControlRamp_Type = TruthValue
_TlpPduControlRamp_Object = MibTableColumn
tlpPduControlRamp = _TlpPduControlRamp_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 1),
    _TlpPduControlRamp_Type()
)
tlpPduControlRamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlRamp.setStatus("current")
_TlpPduControlShed_Type = TruthValue
_TlpPduControlShed_Object = MibTableColumn
tlpPduControlShed = _TlpPduControlShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 2),
    _TlpPduControlShed_Type()
)
tlpPduControlShed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlShed.setStatus("current")
_TlpPduControlPduOn_Type = TruthValue
_TlpPduControlPduOn_Object = MibTableColumn
tlpPduControlPduOn = _TlpPduControlPduOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 3),
    _TlpPduControlPduOn_Type()
)
tlpPduControlPduOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlPduOn.setStatus("current")
_TlpPduControlPduOff_Type = TruthValue
_TlpPduControlPduOff_Object = MibTableColumn
tlpPduControlPduOff = _TlpPduControlPduOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 4),
    _TlpPduControlPduOff_Type()
)
tlpPduControlPduOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlPduOff.setStatus("current")
_TlpPduControlPduReboot_Type = TruthValue
_TlpPduControlPduReboot_Object = MibTableColumn
tlpPduControlPduReboot = _TlpPduControlPduReboot_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 4, 1, 1, 5),
    _TlpPduControlPduReboot_Type()
)
tlpPduControlPduReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduControlPduReboot.setStatus("current")
_TlpPduConfig_ObjectIdentity = ObjectIdentity
tlpPduConfig = _TlpPduConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5)
)
_TlpPduConfigTable_Object = MibTable
tlpPduConfigTable = _TlpPduConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tlpPduConfigTable.setStatus("current")
_TlpPduConfigEntry_Object = MibTableRow
tlpPduConfigEntry = _TlpPduConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1, 1)
)
tlpPduConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpPduConfigEntry.setStatus("current")
_TlpPduConfigInputVoltage_Type = Unsigned32
_TlpPduConfigInputVoltage_Object = MibTableColumn
tlpPduConfigInputVoltage = _TlpPduConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2, 5, 1, 1, 1),
    _TlpPduConfigInputVoltage_Type()
)
tlpPduConfigInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpPduConfigInputVoltage.setStatus("current")
_TlpEnvirosense_ObjectIdentity = ObjectIdentity
tlpEnvirosense = _TlpEnvirosense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3)
)
_TlpEnvIdent_ObjectIdentity = ObjectIdentity
tlpEnvIdent = _TlpEnvIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1)
)
_TlpEnvIdentNumEnvirosense_Type = Unsigned32
_TlpEnvIdentNumEnvirosense_Object = MibScalar
tlpEnvIdentNumEnvirosense = _TlpEnvIdentNumEnvirosense_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 1),
    _TlpEnvIdentNumEnvirosense_Type()
)
tlpEnvIdentNumEnvirosense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvIdentNumEnvirosense.setStatus("current")
_TlpEnvIdentTable_Object = MibTable
tlpEnvIdentTable = _TlpEnvIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpEnvIdentTable.setStatus("current")
_TlpEnvIdentEntry_Object = MibTableRow
tlpEnvIdentEntry = _TlpEnvIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1)
)
tlpEnvIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvIdentEntry.setStatus("current")
_TlpEnvIdentTempSupported_Type = TruthValue
_TlpEnvIdentTempSupported_Object = MibTableColumn
tlpEnvIdentTempSupported = _TlpEnvIdentTempSupported_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1, 1),
    _TlpEnvIdentTempSupported_Type()
)
tlpEnvIdentTempSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvIdentTempSupported.setStatus("current")
_TlpEnvIdentHumiditySupported_Type = TruthValue
_TlpEnvIdentHumiditySupported_Object = MibTableColumn
tlpEnvIdentHumiditySupported = _TlpEnvIdentHumiditySupported_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1, 2),
    _TlpEnvIdentHumiditySupported_Type()
)
tlpEnvIdentHumiditySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvIdentHumiditySupported.setStatus("current")
_TlpEnvNumInputContacts_Type = Unsigned32
_TlpEnvNumInputContacts_Object = MibTableColumn
tlpEnvNumInputContacts = _TlpEnvNumInputContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1, 3),
    _TlpEnvNumInputContacts_Type()
)
tlpEnvNumInputContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvNumInputContacts.setStatus("current")
_TlpEnvNumOutputContacts_Type = Unsigned32
_TlpEnvNumOutputContacts_Object = MibTableColumn
tlpEnvNumOutputContacts = _TlpEnvNumOutputContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 1, 2, 1, 4),
    _TlpEnvNumOutputContacts_Type()
)
tlpEnvNumOutputContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvNumOutputContacts.setStatus("current")
_TlpEnvDetail_ObjectIdentity = ObjectIdentity
tlpEnvDetail = _TlpEnvDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3)
)
_TlpEnvTemperatureTable_Object = MibTable
tlpEnvTemperatureTable = _TlpEnvTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpEnvTemperatureTable.setStatus("current")
_TlpEnvTemperatureEntry_Object = MibTableRow
tlpEnvTemperatureEntry = _TlpEnvTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1, 1)
)
tlpEnvTemperatureEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvTemperatureEntry.setStatus("current")
_TlpEnvTemperatureC_Type = Integer32
_TlpEnvTemperatureC_Object = MibTableColumn
tlpEnvTemperatureC = _TlpEnvTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1, 1, 1),
    _TlpEnvTemperatureC_Type()
)
tlpEnvTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvTemperatureC.setUnits("degrees Centigrade")
_TlpEnvTemperatureF_Type = Integer32
_TlpEnvTemperatureF_Object = MibTableColumn
tlpEnvTemperatureF = _TlpEnvTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1, 1, 2),
    _TlpEnvTemperatureF_Type()
)
tlpEnvTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvTemperatureF.setUnits("0.1 degrees Farenheit")
_TlpEnvTemperatureInAlarm_Type = TruthValue
_TlpEnvTemperatureInAlarm_Object = MibTableColumn
tlpEnvTemperatureInAlarm = _TlpEnvTemperatureInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 1, 1, 3),
    _TlpEnvTemperatureInAlarm_Type()
)
tlpEnvTemperatureInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvTemperatureInAlarm.setStatus("current")
_TlpEnvHumidityTable_Object = MibTable
tlpEnvHumidityTable = _TlpEnvHumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpEnvHumidityTable.setStatus("current")
_TlpEnvHumidityEntry_Object = MibTableRow
tlpEnvHumidityEntry = _TlpEnvHumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 2, 1)
)
tlpEnvHumidityEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvHumidityEntry.setStatus("current")


class _TlpEnvHumidityHumidity_Type(Integer32):
    """Custom type tlpEnvHumidityHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpEnvHumidityHumidity_Type.__name__ = "Integer32"
_TlpEnvHumidityHumidity_Object = MibTableColumn
tlpEnvHumidityHumidity = _TlpEnvHumidityHumidity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 2, 1, 1),
    _TlpEnvHumidityHumidity_Type()
)
tlpEnvHumidityHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvHumidityHumidity.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvHumidityHumidity.setUnits("percent")
_TlpEnvHumidityInAlarm_Type = TruthValue
_TlpEnvHumidityInAlarm_Object = MibTableColumn
tlpEnvHumidityInAlarm = _TlpEnvHumidityInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 2, 1, 2),
    _TlpEnvHumidityInAlarm_Type()
)
tlpEnvHumidityInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvHumidityInAlarm.setStatus("current")
_TlpEnvInputContactTable_Object = MibTable
tlpEnvInputContactTable = _TlpEnvInputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3)
)
if mibBuilder.loadTexts:
    tlpEnvInputContactTable.setStatus("current")
_TlpEnvInputContactEntry_Object = MibTableRow
tlpEnvInputContactEntry = _TlpEnvInputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1)
)
tlpEnvInputContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpEnvInputContactIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvInputContactEntry.setStatus("current")
_TlpEnvInputContactIndex_Type = Unsigned32
_TlpEnvInputContactIndex_Object = MibTableColumn
tlpEnvInputContactIndex = _TlpEnvInputContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 1),
    _TlpEnvInputContactIndex_Type()
)
tlpEnvInputContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvInputContactIndex.setStatus("current")
_TlpEnvInputContactName_Type = DisplayString
_TlpEnvInputContactName_Object = MibTableColumn
tlpEnvInputContactName = _TlpEnvInputContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 2),
    _TlpEnvInputContactName_Type()
)
tlpEnvInputContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvInputContactName.setStatus("current")


class _TlpEnvInputContactNormalState_Type(Integer32):
    """Custom type tlpEnvInputContactNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_TlpEnvInputContactNormalState_Type.__name__ = "Integer32"
_TlpEnvInputContactNormalState_Object = MibTableColumn
tlpEnvInputContactNormalState = _TlpEnvInputContactNormalState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 3),
    _TlpEnvInputContactNormalState_Type()
)
tlpEnvInputContactNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvInputContactNormalState.setStatus("current")


class _TlpEnvInputContactCurrentState_Type(Integer32):
    """Custom type tlpEnvInputContactCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_TlpEnvInputContactCurrentState_Type.__name__ = "Integer32"
_TlpEnvInputContactCurrentState_Object = MibTableColumn
tlpEnvInputContactCurrentState = _TlpEnvInputContactCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 4),
    _TlpEnvInputContactCurrentState_Type()
)
tlpEnvInputContactCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvInputContactCurrentState.setStatus("current")
_TlpEnvInputContactInAlarm_Type = TruthValue
_TlpEnvInputContactInAlarm_Object = MibTableColumn
tlpEnvInputContactInAlarm = _TlpEnvInputContactInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 3, 1, 5),
    _TlpEnvInputContactInAlarm_Type()
)
tlpEnvInputContactInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvInputContactInAlarm.setStatus("current")
_TlpEnvOutputContactTable_Object = MibTable
tlpEnvOutputContactTable = _TlpEnvOutputContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4)
)
if mibBuilder.loadTexts:
    tlpEnvOutputContactTable.setStatus("current")
_TlpEnvOutputContactEntry_Object = MibTableRow
tlpEnvOutputContactEntry = _TlpEnvOutputContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1)
)
tlpEnvOutputContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpEnvOutputContactIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvOutputContactEntry.setStatus("current")
_TlpEnvOutputContactIndex_Type = Unsigned32
_TlpEnvOutputContactIndex_Object = MibTableColumn
tlpEnvOutputContactIndex = _TlpEnvOutputContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 1),
    _TlpEnvOutputContactIndex_Type()
)
tlpEnvOutputContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvOutputContactIndex.setStatus("current")
_TlpEnvOutputContactName_Type = DisplayString
_TlpEnvOutputContactName_Object = MibTableColumn
tlpEnvOutputContactName = _TlpEnvOutputContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 2),
    _TlpEnvOutputContactName_Type()
)
tlpEnvOutputContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvOutputContactName.setStatus("current")


class _TlpEnvOutputContactNormalState_Type(Integer32):
    """Custom type tlpEnvOutputContactNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_TlpEnvOutputContactNormalState_Type.__name__ = "Integer32"
_TlpEnvOutputContactNormalState_Object = MibTableColumn
tlpEnvOutputContactNormalState = _TlpEnvOutputContactNormalState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 3),
    _TlpEnvOutputContactNormalState_Type()
)
tlpEnvOutputContactNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvOutputContactNormalState.setStatus("current")


class _TlpEnvOutputContactCurrentState_Type(Integer32):
    """Custom type tlpEnvOutputContactCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_TlpEnvOutputContactCurrentState_Type.__name__ = "Integer32"
_TlpEnvOutputContactCurrentState_Object = MibTableColumn
tlpEnvOutputContactCurrentState = _TlpEnvOutputContactCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 4),
    _TlpEnvOutputContactCurrentState_Type()
)
tlpEnvOutputContactCurrentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvOutputContactCurrentState.setStatus("current")
_TlpEnvOutputContactInAlarm_Type = TruthValue
_TlpEnvOutputContactInAlarm_Object = MibTableColumn
tlpEnvOutputContactInAlarm = _TlpEnvOutputContactInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 3, 4, 1, 5),
    _TlpEnvOutputContactInAlarm_Type()
)
tlpEnvOutputContactInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpEnvOutputContactInAlarm.setStatus("current")
_TlpEnvConfig_ObjectIdentity = ObjectIdentity
tlpEnvConfig = _TlpEnvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5)
)
_TlpEnvConfigTable_Object = MibTable
tlpEnvConfigTable = _TlpEnvConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpEnvConfigTable.setStatus("current")
_TlpEnvConfigEntry_Object = MibTableRow
tlpEnvConfigEntry = _TlpEnvConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1)
)
tlpEnvConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpEnvConfigEntry.setStatus("current")
_TlpEnvTemperatureLowLimit_Type = Integer32
_TlpEnvTemperatureLowLimit_Object = MibTableColumn
tlpEnvTemperatureLowLimit = _TlpEnvTemperatureLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1, 1),
    _TlpEnvTemperatureLowLimit_Type()
)
tlpEnvTemperatureLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvTemperatureLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvTemperatureLowLimit.setUnits("degrees Farenheit")
_TlpEnvTemperatureHighLimit_Type = Integer32
_TlpEnvTemperatureHighLimit_Object = MibTableColumn
tlpEnvTemperatureHighLimit = _TlpEnvTemperatureHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1, 2),
    _TlpEnvTemperatureHighLimit_Type()
)
tlpEnvTemperatureHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvTemperatureHighLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvTemperatureHighLimit.setUnits("degrees Farenheit")


class _TlpEnvHumidityLowLimit_Type(Integer32):
    """Custom type tlpEnvHumidityLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpEnvHumidityLowLimit_Type.__name__ = "Integer32"
_TlpEnvHumidityLowLimit_Object = MibTableColumn
tlpEnvHumidityLowLimit = _TlpEnvHumidityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1, 3),
    _TlpEnvHumidityLowLimit_Type()
)
tlpEnvHumidityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvHumidityLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvHumidityLowLimit.setUnits("percent")


class _TlpEnvHumidityHighLimit_Type(Integer32):
    """Custom type tlpEnvHumidityHighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TlpEnvHumidityHighLimit_Type.__name__ = "Integer32"
_TlpEnvHumidityHighLimit_Object = MibTableColumn
tlpEnvHumidityHighLimit = _TlpEnvHumidityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3, 5, 1, 1, 4),
    _TlpEnvHumidityHighLimit_Type()
)
tlpEnvHumidityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpEnvHumidityHighLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpEnvHumidityHighLimit.setUnits("percent")
_TlpAts_ObjectIdentity = ObjectIdentity
tlpAts = _TlpAts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4)
)
_TlpAtsIdent_ObjectIdentity = ObjectIdentity
tlpAtsIdent = _TlpAtsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1)
)
_TlpAtsIdentNumAts_Type = Unsigned32
_TlpAtsIdentNumAts_Object = MibScalar
tlpAtsIdentNumAts = _TlpAtsIdentNumAts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 1),
    _TlpAtsIdentNumAts_Type()
)
tlpAtsIdentNumAts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumAts.setStatus("current")
_TlpAtsIdentTable_Object = MibTable
tlpAtsIdentTable = _TlpAtsIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    tlpAtsIdentTable.setStatus("current")
_TlpAtsIdentEntry_Object = MibTableRow
tlpAtsIdentEntry = _TlpAtsIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1)
)
tlpAtsIdentEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsIdentEntry.setStatus("current")
_TlpAtsIdentNumInputs_Type = Unsigned32
_TlpAtsIdentNumInputs_Object = MibTableColumn
tlpAtsIdentNumInputs = _TlpAtsIdentNumInputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 1),
    _TlpAtsIdentNumInputs_Type()
)
tlpAtsIdentNumInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumInputs.setStatus("current")
_TlpAtsIdentNumOutputs_Type = Unsigned32
_TlpAtsIdentNumOutputs_Object = MibTableColumn
tlpAtsIdentNumOutputs = _TlpAtsIdentNumOutputs_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 2),
    _TlpAtsIdentNumOutputs_Type()
)
tlpAtsIdentNumOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumOutputs.setStatus("current")
_TlpAtsIdentNumPhases_Type = Unsigned32
_TlpAtsIdentNumPhases_Object = MibTableColumn
tlpAtsIdentNumPhases = _TlpAtsIdentNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 3),
    _TlpAtsIdentNumPhases_Type()
)
tlpAtsIdentNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumPhases.setStatus("current")
_TlpAtsIdentNumOutlets_Type = Unsigned32
_TlpAtsIdentNumOutlets_Object = MibTableColumn
tlpAtsIdentNumOutlets = _TlpAtsIdentNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 4),
    _TlpAtsIdentNumOutlets_Type()
)
tlpAtsIdentNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumOutlets.setStatus("current")
_TlpAtsIdentNumOutletGroups_Type = Unsigned32
_TlpAtsIdentNumOutletGroups_Object = MibTableColumn
tlpAtsIdentNumOutletGroups = _TlpAtsIdentNumOutletGroups_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 5),
    _TlpAtsIdentNumOutletGroups_Type()
)
tlpAtsIdentNumOutletGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumOutletGroups.setStatus("current")
_TlpAtsIdentNumCircuits_Type = Unsigned32
_TlpAtsIdentNumCircuits_Object = MibTableColumn
tlpAtsIdentNumCircuits = _TlpAtsIdentNumCircuits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 6),
    _TlpAtsIdentNumCircuits_Type()
)
tlpAtsIdentNumCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumCircuits.setStatus("current")
_TlpAtsIdentNumBreakers_Type = Unsigned32
_TlpAtsIdentNumBreakers_Object = MibTableColumn
tlpAtsIdentNumBreakers = _TlpAtsIdentNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 7),
    _TlpAtsIdentNumBreakers_Type()
)
tlpAtsIdentNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumBreakers.setStatus("current")
_TlpAtsIdentNumHeatsinks_Type = Unsigned32
_TlpAtsIdentNumHeatsinks_Object = MibTableColumn
tlpAtsIdentNumHeatsinks = _TlpAtsIdentNumHeatsinks_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 2, 1, 8),
    _TlpAtsIdentNumHeatsinks_Type()
)
tlpAtsIdentNumHeatsinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsIdentNumHeatsinks.setStatus("current")
_TlpAtsSupportsTable_Object = MibTable
tlpAtsSupportsTable = _TlpAtsSupportsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    tlpAtsSupportsTable.setStatus("current")
_TlpAtsSupportsEntry_Object = MibTableRow
tlpAtsSupportsEntry = _TlpAtsSupportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1)
)
tlpAtsSupportsEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsSupportsEntry.setStatus("current")
_TlpAtsSupportsEnergywise_Type = TruthValue
_TlpAtsSupportsEnergywise_Object = MibTableColumn
tlpAtsSupportsEnergywise = _TlpAtsSupportsEnergywise_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 1),
    _TlpAtsSupportsEnergywise_Type()
)
tlpAtsSupportsEnergywise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsEnergywise.setStatus("current")
_TlpAtsSupportsRampShed_Type = TruthValue
_TlpAtsSupportsRampShed_Object = MibTableColumn
tlpAtsSupportsRampShed = _TlpAtsSupportsRampShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 2),
    _TlpAtsSupportsRampShed_Type()
)
tlpAtsSupportsRampShed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsRampShed.setStatus("current")
_TlpAtsSupportsOutletGroup_Type = TruthValue
_TlpAtsSupportsOutletGroup_Object = MibTableColumn
tlpAtsSupportsOutletGroup = _TlpAtsSupportsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 3),
    _TlpAtsSupportsOutletGroup_Type()
)
tlpAtsSupportsOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsOutletGroup.setStatus("current")
_TlpAtsSupportsOutletCurrentPower_Type = TruthValue
_TlpAtsSupportsOutletCurrentPower_Object = MibTableColumn
tlpAtsSupportsOutletCurrentPower = _TlpAtsSupportsOutletCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 4),
    _TlpAtsSupportsOutletCurrentPower_Type()
)
tlpAtsSupportsOutletCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsOutletCurrentPower.setStatus("current")
_TlpAtsSupportsOutletVoltage_Type = TruthValue
_TlpAtsSupportsOutletVoltage_Object = MibTableColumn
tlpAtsSupportsOutletVoltage = _TlpAtsSupportsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 3, 1, 5),
    _TlpAtsSupportsOutletVoltage_Type()
)
tlpAtsSupportsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsSupportsOutletVoltage.setStatus("current")
_TlpAtsDisplayTable_Object = MibTable
tlpAtsDisplayTable = _TlpAtsDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4)
)
if mibBuilder.loadTexts:
    tlpAtsDisplayTable.setStatus("current")
_TlpAtsDisplayEntry_Object = MibTableRow
tlpAtsDisplayEntry = _TlpAtsDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1)
)
tlpAtsDisplayEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsDisplayEntry.setStatus("current")


class _TlpAtsDisplayScheme_Type(Integer32):
    """Custom type tlpAtsDisplayScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("schemeNormal", 1),
          ("schemeReverse", 0))
    )


_TlpAtsDisplayScheme_Type.__name__ = "Integer32"
_TlpAtsDisplayScheme_Object = MibTableColumn
tlpAtsDisplayScheme = _TlpAtsDisplayScheme_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 1),
    _TlpAtsDisplayScheme_Type()
)
tlpAtsDisplayScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayScheme.setStatus("current")


class _TlpAtsDisplayOrientation_Type(Integer32):
    """Custom type tlpAtsDisplayOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("displayNormal", 0),
          ("displayReverse", 1))
    )


_TlpAtsDisplayOrientation_Type.__name__ = "Integer32"
_TlpAtsDisplayOrientation_Object = MibTableColumn
tlpAtsDisplayOrientation = _TlpAtsDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 2),
    _TlpAtsDisplayOrientation_Type()
)
tlpAtsDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayOrientation.setStatus("current")


class _TlpAtsDisplayAutoScroll_Type(Integer32):
    """Custom type tlpAtsDisplayAutoScroll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("scrollDisabled", 0),
          ("scrollEnabled", 1))
    )


_TlpAtsDisplayAutoScroll_Type.__name__ = "Integer32"
_TlpAtsDisplayAutoScroll_Object = MibTableColumn
tlpAtsDisplayAutoScroll = _TlpAtsDisplayAutoScroll_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 3),
    _TlpAtsDisplayAutoScroll_Type()
)
tlpAtsDisplayAutoScroll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayAutoScroll.setStatus("current")


class _TlpAtsDisplayIntensity_Type(Integer32):
    """Custom type tlpAtsDisplayIntensity based on Integer32"""
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
        *(("intensity100", 4),
          ("intensity25", 1),
          ("intensity50", 2),
          ("intensity75", 3))
    )


_TlpAtsDisplayIntensity_Type.__name__ = "Integer32"
_TlpAtsDisplayIntensity_Object = MibTableColumn
tlpAtsDisplayIntensity = _TlpAtsDisplayIntensity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 4),
    _TlpAtsDisplayIntensity_Type()
)
tlpAtsDisplayIntensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayIntensity.setStatus("current")


class _TlpAtsDisplayUnits_Type(Integer32):
    """Custom type tlpAtsDisplayUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("metric", 1),
          ("normal", 0))
    )


_TlpAtsDisplayUnits_Type.__name__ = "Integer32"
_TlpAtsDisplayUnits_Object = MibTableColumn
tlpAtsDisplayUnits = _TlpAtsDisplayUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 1, 4, 1, 5),
    _TlpAtsDisplayUnits_Type()
)
tlpAtsDisplayUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDisplayUnits.setStatus("current")
_TlpAtsDevice_ObjectIdentity = ObjectIdentity
tlpAtsDevice = _TlpAtsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2)
)
_TlpAtsDeviceTable_Object = MibTable
tlpAtsDeviceTable = _TlpAtsDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAtsDeviceTable.setStatus("current")
_TlpAtsDeviceEntry_Object = MibTableRow
tlpAtsDeviceEntry = _TlpAtsDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1)
)
tlpAtsDeviceEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsDeviceEntry.setStatus("current")


class _TlpAtsDeviceMainLoadState_Type(Integer32):
    """Custom type tlpAtsDeviceMainLoadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlpAtsDeviceMainLoadState_Type.__name__ = "Integer32"
_TlpAtsDeviceMainLoadState_Object = MibTableColumn
tlpAtsDeviceMainLoadState = _TlpAtsDeviceMainLoadState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 1),
    _TlpAtsDeviceMainLoadState_Type()
)
tlpAtsDeviceMainLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceMainLoadState.setStatus("current")
_TlpAtsDeviceMainLoadControllable_Type = TruthValue
_TlpAtsDeviceMainLoadControllable_Object = MibTableColumn
tlpAtsDeviceMainLoadControllable = _TlpAtsDeviceMainLoadControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 2),
    _TlpAtsDeviceMainLoadControllable_Type()
)
tlpAtsDeviceMainLoadControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceMainLoadControllable.setStatus("current")


class _TlpAtsDeviceMainLoadCommand_Type(Integer32):
    """Custom type tlpAtsDeviceMainLoadCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlpAtsDeviceMainLoadCommand_Type.__name__ = "Integer32"
_TlpAtsDeviceMainLoadCommand_Object = MibTableColumn
tlpAtsDeviceMainLoadCommand = _TlpAtsDeviceMainLoadCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 3),
    _TlpAtsDeviceMainLoadCommand_Type()
)
tlpAtsDeviceMainLoadCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDeviceMainLoadCommand.setStatus("current")
_TlpAtsDevicePowerOnDelay_Type = Integer32
_TlpAtsDevicePowerOnDelay_Object = MibTableColumn
tlpAtsDevicePowerOnDelay = _TlpAtsDevicePowerOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 4),
    _TlpAtsDevicePowerOnDelay_Type()
)
tlpAtsDevicePowerOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsDevicePowerOnDelay.setStatus("current")
_TlpAtsDeviceTotalInputPowerRating_Type = Integer32
_TlpAtsDeviceTotalInputPowerRating_Object = MibTableColumn
tlpAtsDeviceTotalInputPowerRating = _TlpAtsDeviceTotalInputPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 5),
    _TlpAtsDeviceTotalInputPowerRating_Type()
)
tlpAtsDeviceTotalInputPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceTotalInputPowerRating.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceTotalInputPowerRating.setUnits("Watts")
_TlpAtsDeviceTemperatureC_Type = Integer32
_TlpAtsDeviceTemperatureC_Object = MibTableColumn
tlpAtsDeviceTemperatureC = _TlpAtsDeviceTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 6),
    _TlpAtsDeviceTemperatureC_Type()
)
tlpAtsDeviceTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceTemperatureC.setUnits("degrees Centigrade")
_TlpAtsDeviceTemperatureF_Type = Integer32
_TlpAtsDeviceTemperatureF_Object = MibTableColumn
tlpAtsDeviceTemperatureF = _TlpAtsDeviceTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 7),
    _TlpAtsDeviceTemperatureF_Type()
)
tlpAtsDeviceTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceTemperatureF.setUnits("degrees Farenheit")


class _TlpAtsDevicePhaseImbalance_Type(Integer32):
    """Custom type tlpAtsDevicePhaseImbalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TlpAtsDevicePhaseImbalance_Type.__name__ = "Integer32"
_TlpAtsDevicePhaseImbalance_Object = MibTableColumn
tlpAtsDevicePhaseImbalance = _TlpAtsDevicePhaseImbalance_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 8),
    _TlpAtsDevicePhaseImbalance_Type()
)
tlpAtsDevicePhaseImbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDevicePhaseImbalance.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDevicePhaseImbalance.setUnits("percent")
_TlpAtsDeviceOutputPowerTotal_Type = Unsigned32
_TlpAtsDeviceOutputPowerTotal_Object = MibTableColumn
tlpAtsDeviceOutputPowerTotal = _TlpAtsDeviceOutputPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 9),
    _TlpAtsDeviceOutputPowerTotal_Type()
)
tlpAtsDeviceOutputPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputPowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputPowerTotal.setUnits("Watts")
_TlpAtsDeviceAggregatePowerFactor_Type = Unsigned32
_TlpAtsDeviceAggregatePowerFactor_Object = MibTableColumn
tlpAtsDeviceAggregatePowerFactor = _TlpAtsDeviceAggregatePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 10),
    _TlpAtsDeviceAggregatePowerFactor_Type()
)
tlpAtsDeviceAggregatePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceAggregatePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsDeviceAggregatePowerFactor.setUnits("0.1 Watts")


class _TlpAtsDeviceOutputCurrentPrecision_Type(Integer32):
    """Custom type tlpAtsDeviceOutputCurrentPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hundredths", 2),
          ("none", 0),
          ("tenths", 1))
    )


_TlpAtsDeviceOutputCurrentPrecision_Type.__name__ = "Integer32"
_TlpAtsDeviceOutputCurrentPrecision_Object = MibTableColumn
tlpAtsDeviceOutputCurrentPrecision = _TlpAtsDeviceOutputCurrentPrecision_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 11),
    _TlpAtsDeviceOutputCurrentPrecision_Type()
)
tlpAtsDeviceOutputCurrentPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceOutputCurrentPrecision.setStatus("current")
_TlpAtsDeviceGeneralFault_Type = TruthValue
_TlpAtsDeviceGeneralFault_Object = MibTableColumn
tlpAtsDeviceGeneralFault = _TlpAtsDeviceGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 2, 1, 1, 12),
    _TlpAtsDeviceGeneralFault_Type()
)
tlpAtsDeviceGeneralFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsDeviceGeneralFault.setStatus("current")
_TlpAtsDetail_ObjectIdentity = ObjectIdentity
tlpAtsDetail = _TlpAtsDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3)
)
_TlpAtsInput_ObjectIdentity = ObjectIdentity
tlpAtsInput = _TlpAtsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1)
)
_TlpAtsInputTable_Object = MibTable
tlpAtsInputTable = _TlpAtsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tlpAtsInputTable.setStatus("current")
_TlpAtsInputEntry_Object = MibTableRow
tlpAtsInputEntry = _TlpAtsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1)
)
tlpAtsInputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsInputEntry.setStatus("current")
_TlpAtsInputNominalVoltage_Type = Unsigned32
_TlpAtsInputNominalVoltage_Object = MibTableColumn
tlpAtsInputNominalVoltage = _TlpAtsInputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 1),
    _TlpAtsInputNominalVoltage_Type()
)
tlpAtsInputNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltage.setStatus("current")
_TlpAtsInputNominalVoltagePhaseToPhase_Type = Unsigned32
_TlpAtsInputNominalVoltagePhaseToPhase_Object = MibTableColumn
tlpAtsInputNominalVoltagePhaseToPhase = _TlpAtsInputNominalVoltagePhaseToPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 2),
    _TlpAtsInputNominalVoltagePhaseToPhase_Type()
)
tlpAtsInputNominalVoltagePhaseToPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltagePhaseToPhase.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltagePhaseToPhase.setUnits("0.1 Volt DC")
_TlpAtsInputNominalVoltagePhaseToNeutral_Type = Unsigned32
_TlpAtsInputNominalVoltagePhaseToNeutral_Object = MibTableColumn
tlpAtsInputNominalVoltagePhaseToNeutral = _TlpAtsInputNominalVoltagePhaseToNeutral_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 3),
    _TlpAtsInputNominalVoltagePhaseToNeutral_Type()
)
tlpAtsInputNominalVoltagePhaseToNeutral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltagePhaseToNeutral.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputNominalVoltagePhaseToNeutral.setUnits("0.1 Volt DC")
_TlpAtsInputBadTransferVoltage_Type = Unsigned32
_TlpAtsInputBadTransferVoltage_Object = MibTableColumn
tlpAtsInputBadTransferVoltage = _TlpAtsInputBadTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 4),
    _TlpAtsInputBadTransferVoltage_Type()
)
tlpAtsInputBadTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputBadTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputBadTransferVoltage.setUnits("0.1 Volts")
_TlpAtsInputBadTransferVoltageLowerBound_Type = Unsigned32
_TlpAtsInputBadTransferVoltageLowerBound_Object = MibTableColumn
tlpAtsInputBadTransferVoltageLowerBound = _TlpAtsInputBadTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 5),
    _TlpAtsInputBadTransferVoltageLowerBound_Type()
)
tlpAtsInputBadTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputBadTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputBadTransferVoltageLowerBound.setUnits("Volts")
_TlpAtsInputBadTransferVoltageUpperBound_Type = Unsigned32
_TlpAtsInputBadTransferVoltageUpperBound_Object = MibTableColumn
tlpAtsInputBadTransferVoltageUpperBound = _TlpAtsInputBadTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 6),
    _TlpAtsInputBadTransferVoltageUpperBound_Type()
)
tlpAtsInputBadTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputBadTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputBadTransferVoltageUpperBound.setUnits("Volts")
_TlpAtsInputHighTransferVoltage_Type = Unsigned32
_TlpAtsInputHighTransferVoltage_Object = MibTableColumn
tlpAtsInputHighTransferVoltage = _TlpAtsInputHighTransferVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 7),
    _TlpAtsInputHighTransferVoltage_Type()
)
tlpAtsInputHighTransferVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltage.setUnits("0.1 Volts")
_TlpAtsInputHighTransferVoltageLowerBound_Type = Unsigned32
_TlpAtsInputHighTransferVoltageLowerBound_Object = MibTableColumn
tlpAtsInputHighTransferVoltageLowerBound = _TlpAtsInputHighTransferVoltageLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 8),
    _TlpAtsInputHighTransferVoltageLowerBound_Type()
)
tlpAtsInputHighTransferVoltageLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltageLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltageLowerBound.setUnits("Volts")
_TlpAtsInputHighTransferVoltageUpperBound_Type = Unsigned32
_TlpAtsInputHighTransferVoltageUpperBound_Object = MibTableColumn
tlpAtsInputHighTransferVoltageUpperBound = _TlpAtsInputHighTransferVoltageUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 9),
    _TlpAtsInputHighTransferVoltageUpperBound_Type()
)
tlpAtsInputHighTransferVoltageUpperBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltageUpperBound.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputHighTransferVoltageUpperBound.setUnits("Volts")
_TlpAtsInputFairVoltageThreshold_Type = Unsigned32
_TlpAtsInputFairVoltageThreshold_Object = MibTableColumn
tlpAtsInputFairVoltageThreshold = _TlpAtsInputFairVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 10),
    _TlpAtsInputFairVoltageThreshold_Type()
)
tlpAtsInputFairVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputFairVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputFairVoltageThreshold.setUnits("Volts")
_TlpAtsInputBadVoltageThreshold_Type = Unsigned32
_TlpAtsInputBadVoltageThreshold_Object = MibTableColumn
tlpAtsInputBadVoltageThreshold = _TlpAtsInputBadVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 11),
    _TlpAtsInputBadVoltageThreshold_Type()
)
tlpAtsInputBadVoltageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputBadVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputBadVoltageThreshold.setUnits("Volts")


class _TlpAtsInputSourceAvailability_Type(Integer32):
    """Custom type tlpAtsInputSourceAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inputSourceA", 1),
          ("inputSourceAB", 3),
          ("inputSourceB", 2),
          ("none", 0))
    )


_TlpAtsInputSourceAvailability_Type.__name__ = "Integer32"
_TlpAtsInputSourceAvailability_Object = MibTableColumn
tlpAtsInputSourceAvailability = _TlpAtsInputSourceAvailability_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 12),
    _TlpAtsInputSourceAvailability_Type()
)
tlpAtsInputSourceAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputSourceAvailability.setStatus("current")


class _TlpAtsInputSourceInUse_Type(Integer32):
    """Custom type tlpAtsInputSourceInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inputSourceA", 0),
          ("inputSourceB", 1))
    )


_TlpAtsInputSourceInUse_Type.__name__ = "Integer32"
_TlpAtsInputSourceInUse_Object = MibTableColumn
tlpAtsInputSourceInUse = _TlpAtsInputSourceInUse_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 13),
    _TlpAtsInputSourceInUse_Type()
)
tlpAtsInputSourceInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputSourceInUse.setStatus("current")
_TlpAtsInputSourceTransitionCount_Type = Unsigned32
_TlpAtsInputSourceTransitionCount_Object = MibTableColumn
tlpAtsInputSourceTransitionCount = _TlpAtsInputSourceTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 14),
    _TlpAtsInputSourceTransitionCount_Type()
)
tlpAtsInputSourceTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputSourceTransitionCount.setStatus("current")
_TlpAtsInputCurrentLimit_Type = Unsigned32
_TlpAtsInputCurrentLimit_Object = MibTableColumn
tlpAtsInputCurrentLimit = _TlpAtsInputCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 1, 1, 15),
    _TlpAtsInputCurrentLimit_Type()
)
tlpAtsInputCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputCurrentLimit.setUnits("Amp DC")
_TlpAtsInputPhaseTable_Object = MibTable
tlpAtsInputPhaseTable = _TlpAtsInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpAtsInputPhaseTable.setStatus("current")
_TlpAtsInputPhaseEntry_Object = MibTableRow
tlpAtsInputPhaseEntry = _TlpAtsInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1)
)
tlpAtsInputPhaseEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsInputLineIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsInputPhaseEntry.setStatus("current")
_TlpAtsInputLineIndex_Type = Unsigned32
_TlpAtsInputLineIndex_Object = MibTableColumn
tlpAtsInputLineIndex = _TlpAtsInputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 1),
    _TlpAtsInputLineIndex_Type()
)
tlpAtsInputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputLineIndex.setStatus("current")
_TlpAtsInputPhaseIndex_Type = Unsigned32
_TlpAtsInputPhaseIndex_Object = MibTableColumn
tlpAtsInputPhaseIndex = _TlpAtsInputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 2),
    _TlpAtsInputPhaseIndex_Type()
)
tlpAtsInputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseIndex.setStatus("current")


class _TlpAtsInputPhaseType_Type(Integer32):
    """Custom type tlpAtsInputPhaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phaseToNeutral", 0),
          ("phaseToPhase", 1))
    )


_TlpAtsInputPhaseType_Type.__name__ = "Integer32"
_TlpAtsInputPhaseType_Object = MibTableColumn
tlpAtsInputPhaseType = _TlpAtsInputPhaseType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 3),
    _TlpAtsInputPhaseType_Type()
)
tlpAtsInputPhaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseType.setStatus("current")
_TlpAtsInputPhaseFrequency_Type = Unsigned32
_TlpAtsInputPhaseFrequency_Object = MibTableColumn
tlpAtsInputPhaseFrequency = _TlpAtsInputPhaseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 4),
    _TlpAtsInputPhaseFrequency_Type()
)
tlpAtsInputPhaseFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseFrequency.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseFrequency.setUnits("0.1 Hertz")
_TlpAtsInputPhaseVoltage_Type = Unsigned32
_TlpAtsInputPhaseVoltage_Object = MibTableColumn
tlpAtsInputPhaseVoltage = _TlpAtsInputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 5),
    _TlpAtsInputPhaseVoltage_Type()
)
tlpAtsInputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltage.setUnits("0.1 Volt DC")
_TlpAtsInputPhaseVoltageMin_Type = Unsigned32
_TlpAtsInputPhaseVoltageMin_Object = MibTableColumn
tlpAtsInputPhaseVoltageMin = _TlpAtsInputPhaseVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 6),
    _TlpAtsInputPhaseVoltageMin_Type()
)
tlpAtsInputPhaseVoltageMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltageMin.setUnits("0.1 Volt DC")
_TlpAtsInputPhaseVoltageMax_Type = Unsigned32
_TlpAtsInputPhaseVoltageMax_Object = MibTableColumn
tlpAtsInputPhaseVoltageMax = _TlpAtsInputPhaseVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 7),
    _TlpAtsInputPhaseVoltageMax_Type()
)
tlpAtsInputPhaseVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseVoltageMax.setUnits("0.1 Volt DC")
_TlpAtsInputPhaseCurrent_Type = Unsigned32
_TlpAtsInputPhaseCurrent_Object = MibTableColumn
tlpAtsInputPhaseCurrent = _TlpAtsInputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 1, 2, 1, 8),
    _TlpAtsInputPhaseCurrent_Type()
)
tlpAtsInputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsInputPhaseCurrent.setUnits("0.01 Amp DC")
_TlpAtsOutput_ObjectIdentity = ObjectIdentity
tlpAtsOutput = _TlpAtsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2)
)
_TlpAtsOutputTable_Object = MibTable
tlpAtsOutputTable = _TlpAtsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAtsOutputTable.setStatus("current")
_TlpAtsOutputEntry_Object = MibTableRow
tlpAtsOutputEntry = _TlpAtsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1)
)
tlpAtsOutputEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsOutputIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsOutputEntry.setStatus("current")
_TlpAtsOutputIndex_Type = Unsigned32
_TlpAtsOutputIndex_Object = MibTableColumn
tlpAtsOutputIndex = _TlpAtsOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 1),
    _TlpAtsOutputIndex_Type()
)
tlpAtsOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputIndex.setStatus("current")


class _TlpAtsOutputPhase_Type(Integer32):
    """Custom type tlpAtsOutputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_TlpAtsOutputPhase_Type.__name__ = "Integer32"
_TlpAtsOutputPhase_Object = MibTableColumn
tlpAtsOutputPhase = _TlpAtsOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 2),
    _TlpAtsOutputPhase_Type()
)
tlpAtsOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputPhase.setStatus("current")


class _TlpAtsOutputPhaseType_Type(Integer32):
    """Custom type tlpAtsOutputPhaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phaseToNeutral", 0),
          ("phaseToPhase", 1))
    )


_TlpAtsOutputPhaseType_Type.__name__ = "Integer32"
_TlpAtsOutputPhaseType_Object = MibTableColumn
tlpAtsOutputPhaseType = _TlpAtsOutputPhaseType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 3),
    _TlpAtsOutputPhaseType_Type()
)
tlpAtsOutputPhaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputPhaseType.setStatus("current")
_TlpAtsOutputVoltage_Type = Unsigned32
_TlpAtsOutputVoltage_Object = MibTableColumn
tlpAtsOutputVoltage = _TlpAtsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 4),
    _TlpAtsOutputVoltage_Type()
)
tlpAtsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputVoltage.setUnits("0.1 Volt DC")
_TlpAtsOutputCurrent_Type = Unsigned32
_TlpAtsOutputCurrent_Object = MibTableColumn
tlpAtsOutputCurrent = _TlpAtsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 5),
    _TlpAtsOutputCurrent_Type()
)
tlpAtsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrent.setUnits("0.01 Amp DC")
_TlpAtsOutputCurrentMin_Type = Unsigned32
_TlpAtsOutputCurrentMin_Object = MibTableColumn
tlpAtsOutputCurrentMin = _TlpAtsOutputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 6),
    _TlpAtsOutputCurrentMin_Type()
)
tlpAtsOutputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrentMin.setUnits("0.01 Amp DC")
_TlpAtsOutputCurrentMax_Type = Unsigned32
_TlpAtsOutputCurrentMax_Object = MibTableColumn
tlpAtsOutputCurrentMax = _TlpAtsOutputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 7),
    _TlpAtsOutputCurrentMax_Type()
)
tlpAtsOutputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputCurrentMax.setUnits("0.01 Amp DC")
_TlpAtsOutputActivePower_Type = Unsigned32
_TlpAtsOutputActivePower_Object = MibTableColumn
tlpAtsOutputActivePower = _TlpAtsOutputActivePower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 8),
    _TlpAtsOutputActivePower_Type()
)
tlpAtsOutputActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputActivePower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputActivePower.setUnits("Watts")
_TlpAtsOutputPowerFactor_Type = Unsigned32
_TlpAtsOutputPowerFactor_Object = MibTableColumn
tlpAtsOutputPowerFactor = _TlpAtsOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 9),
    _TlpAtsOutputPowerFactor_Type()
)
tlpAtsOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutputPowerFactor.setUnits("0.01 percent")


class _TlpAtsOutputSource_Type(Integer32):
    """Custom type tlpAtsOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("normal", 1))
    )


_TlpAtsOutputSource_Type.__name__ = "Integer32"
_TlpAtsOutputSource_Object = MibTableColumn
tlpAtsOutputSource = _TlpAtsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 2, 1, 1, 10),
    _TlpAtsOutputSource_Type()
)
tlpAtsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutputSource.setStatus("current")
_TlpAtsOutlet_ObjectIdentity = ObjectIdentity
tlpAtsOutlet = _TlpAtsOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3)
)
_TlpAtsOutletTable_Object = MibTable
tlpAtsOutletTable = _TlpAtsOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpAtsOutletTable.setStatus("current")
_TlpAtsOutletEntry_Object = MibTableRow
tlpAtsOutletEntry = _TlpAtsOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1)
)
tlpAtsOutletEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsOutletIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsOutletEntry.setStatus("current")
_TlpAtsOutletIndex_Type = Unsigned32
_TlpAtsOutletIndex_Object = MibTableColumn
tlpAtsOutletIndex = _TlpAtsOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 1),
    _TlpAtsOutletIndex_Type()
)
tlpAtsOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletIndex.setStatus("current")
_TlpAtsOutletName_Type = DisplayString
_TlpAtsOutletName_Object = MibTableColumn
tlpAtsOutletName = _TlpAtsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 2),
    _TlpAtsOutletName_Type()
)
tlpAtsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletName.setStatus("current")
_TlpAtsOutletDescription_Type = DisplayString
_TlpAtsOutletDescription_Object = MibTableColumn
tlpAtsOutletDescription = _TlpAtsOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 3),
    _TlpAtsOutletDescription_Type()
)
tlpAtsOutletDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletDescription.setStatus("current")


class _TlpAtsOutletState_Type(Integer32):
    """Custom type tlpAtsOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlpAtsOutletState_Type.__name__ = "Integer32"
_TlpAtsOutletState_Object = MibTableColumn
tlpAtsOutletState = _TlpAtsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 4),
    _TlpAtsOutletState_Type()
)
tlpAtsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletState.setStatus("current")
_TlpAtsOutletControllable_Type = TruthValue
_TlpAtsOutletControllable_Object = MibTableColumn
tlpAtsOutletControllable = _TlpAtsOutletControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 5),
    _TlpAtsOutletControllable_Type()
)
tlpAtsOutletControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletControllable.setStatus("current")


class _TlpAtsOutletCommand_Type(Integer32):
    """Custom type tlpAtsOutletCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlpAtsOutletCommand_Type.__name__ = "Integer32"
_TlpAtsOutletCommand_Object = MibTableColumn
tlpAtsOutletCommand = _TlpAtsOutletCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 6),
    _TlpAtsOutletCommand_Type()
)
tlpAtsOutletCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletCommand.setStatus("current")
_TlpAtsOutletVoltage_Type = Unsigned32
_TlpAtsOutletVoltage_Object = MibTableColumn
tlpAtsOutletVoltage = _TlpAtsOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 7),
    _TlpAtsOutletVoltage_Type()
)
tlpAtsOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletVoltage.setUnits("0.1 Volt DC")
_TlpAtsOutletCurrent_Type = Unsigned32
_TlpAtsOutletCurrent_Object = MibTableColumn
tlpAtsOutletCurrent = _TlpAtsOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 8),
    _TlpAtsOutletCurrent_Type()
)
tlpAtsOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletCurrent.setUnits("0.01 RMS Amp")
_TlpAtsOutletPower_Type = Unsigned32
_TlpAtsOutletPower_Object = MibTableColumn
tlpAtsOutletPower = _TlpAtsOutletPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 9),
    _TlpAtsOutletPower_Type()
)
tlpAtsOutletPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletPower.setUnits("Watts")


class _TlpAtsOutletRampAction_Type(Integer32):
    """Custom type tlpAtsOutletRampAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOff", 0),
          ("turnOnAfterDelay", 1))
    )


_TlpAtsOutletRampAction_Type.__name__ = "Integer32"
_TlpAtsOutletRampAction_Object = MibTableColumn
tlpAtsOutletRampAction = _TlpAtsOutletRampAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 10),
    _TlpAtsOutletRampAction_Type()
)
tlpAtsOutletRampAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletRampAction.setStatus("current")
_TlpAtsOutletRampDelay_Type = Integer32
_TlpAtsOutletRampDelay_Object = MibTableColumn
tlpAtsOutletRampDelay = _TlpAtsOutletRampDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 11),
    _TlpAtsOutletRampDelay_Type()
)
tlpAtsOutletRampDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletRampDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletRampDelay.setUnits("seconds")


class _TlpAtsOutletShedAction_Type(Integer32):
    """Custom type tlpAtsOutletShedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOn", 0),
          ("turnOffAfterDelay", 1))
    )


_TlpAtsOutletShedAction_Type.__name__ = "Integer32"
_TlpAtsOutletShedAction_Object = MibTableColumn
tlpAtsOutletShedAction = _TlpAtsOutletShedAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 12),
    _TlpAtsOutletShedAction_Type()
)
tlpAtsOutletShedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletShedAction.setStatus("current")
_TlpAtsOutletShedDelay_Type = Integer32
_TlpAtsOutletShedDelay_Object = MibTableColumn
tlpAtsOutletShedDelay = _TlpAtsOutletShedDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 13),
    _TlpAtsOutletShedDelay_Type()
)
tlpAtsOutletShedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletShedDelay.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsOutletShedDelay.setUnits("seconds")
_TlpAtsOutletGroup_Type = Integer32
_TlpAtsOutletGroup_Object = MibTableColumn
tlpAtsOutletGroup = _TlpAtsOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 14),
    _TlpAtsOutletGroup_Type()
)
tlpAtsOutletGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroup.setStatus("current")
_TlpAtsOutletBank_Type = Integer32
_TlpAtsOutletBank_Object = MibTableColumn
tlpAtsOutletBank = _TlpAtsOutletBank_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 15),
    _TlpAtsOutletBank_Type()
)
tlpAtsOutletBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletBank.setStatus("current")
_TlpAtsOutletCircuit_Type = Integer32
_TlpAtsOutletCircuit_Object = MibTableColumn
tlpAtsOutletCircuit = _TlpAtsOutletCircuit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 16),
    _TlpAtsOutletCircuit_Type()
)
tlpAtsOutletCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletCircuit.setStatus("current")


class _TlpAtsOutletPhase_Type(Integer32):
    """Custom type tlpAtsOutletPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase1-2", 4),
          ("phase2", 2),
          ("phase2-3", 5),
          ("phase3", 3),
          ("phase3-1", 6),
          ("unknown", 0))
    )


_TlpAtsOutletPhase_Type.__name__ = "Integer32"
_TlpAtsOutletPhase_Object = MibTableColumn
tlpAtsOutletPhase = _TlpAtsOutletPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 1, 1, 17),
    _TlpAtsOutletPhase_Type()
)
tlpAtsOutletPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletPhase.setStatus("current")
_TlpAtsOutletGroupTable_Object = MibTable
tlpAtsOutletGroupTable = _TlpAtsOutletGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpAtsOutletGroupTable.setStatus("current")
_TlpAtsOutletGroupEntry_Object = MibTableRow
tlpAtsOutletGroupEntry = _TlpAtsOutletGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1)
)
tlpAtsOutletGroupEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsOutletGroupIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsOutletGroupEntry.setStatus("current")
_TlpAtsOutletGroupIndex_Type = Unsigned32
_TlpAtsOutletGroupIndex_Object = MibTableColumn
tlpAtsOutletGroupIndex = _TlpAtsOutletGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 1),
    _TlpAtsOutletGroupIndex_Type()
)
tlpAtsOutletGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupIndex.setStatus("current")
_TlpAtsOutletGroupRowStatus_Type = RowStatus
_TlpAtsOutletGroupRowStatus_Object = MibTableColumn
tlpAtsOutletGroupRowStatus = _TlpAtsOutletGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 2),
    _TlpAtsOutletGroupRowStatus_Type()
)
tlpAtsOutletGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupRowStatus.setStatus("current")
_TlpAtsOutletGroupName_Type = DisplayString
_TlpAtsOutletGroupName_Object = MibTableColumn
tlpAtsOutletGroupName = _TlpAtsOutletGroupName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 3),
    _TlpAtsOutletGroupName_Type()
)
tlpAtsOutletGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupName.setStatus("current")
_TlpAtsOutletGroupDescription_Type = DisplayString
_TlpAtsOutletGroupDescription_Object = MibTableColumn
tlpAtsOutletGroupDescription = _TlpAtsOutletGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 4),
    _TlpAtsOutletGroupDescription_Type()
)
tlpAtsOutletGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupDescription.setStatus("current")


class _TlpAtsOutletGroupState_Type(Integer32):
    """Custom type tlpAtsOutletGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 3),
          ("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlpAtsOutletGroupState_Type.__name__ = "Integer32"
_TlpAtsOutletGroupState_Object = MibTableColumn
tlpAtsOutletGroupState = _TlpAtsOutletGroupState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 5),
    _TlpAtsOutletGroupState_Type()
)
tlpAtsOutletGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupState.setStatus("current")


class _TlpAtsOutletGroupCommand_Type(Integer32):
    """Custom type tlpAtsOutletGroupCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlpAtsOutletGroupCommand_Type.__name__ = "Integer32"
_TlpAtsOutletGroupCommand_Object = MibTableColumn
tlpAtsOutletGroupCommand = _TlpAtsOutletGroupCommand_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 3, 2, 1, 6),
    _TlpAtsOutletGroupCommand_Type()
)
tlpAtsOutletGroupCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsOutletGroupCommand.setStatus("current")
_TlpAtsCircuit_ObjectIdentity = ObjectIdentity
tlpAtsCircuit = _TlpAtsCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4)
)
_TlpAtsCircuitTable_Object = MibTable
tlpAtsCircuitTable = _TlpAtsCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpAtsCircuitTable.setStatus("current")
_TlpAtsCircuitEntry_Object = MibTableRow
tlpAtsCircuitEntry = _TlpAtsCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1)
)
tlpAtsCircuitEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsCircuitIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsCircuitEntry.setStatus("current")
_TlpAtsCircuitIndex_Type = Unsigned32
_TlpAtsCircuitIndex_Object = MibTableColumn
tlpAtsCircuitIndex = _TlpAtsCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 1),
    _TlpAtsCircuitIndex_Type()
)
tlpAtsCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitIndex.setStatus("current")


class _TlpAtsCircuitPhase_Type(Integer32):
    """Custom type tlpAtsCircuitPhase based on Integer32"""
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
        *(("phase1", 1),
          ("phase1-2", 4),
          ("phase2", 2),
          ("phase2-3", 5),
          ("phase3", 3),
          ("phase3-1", 6),
          ("unknown", 0))
    )


_TlpAtsCircuitPhase_Type.__name__ = "Integer32"
_TlpAtsCircuitPhase_Object = MibTableColumn
tlpAtsCircuitPhase = _TlpAtsCircuitPhase_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 2),
    _TlpAtsCircuitPhase_Type()
)
tlpAtsCircuitPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitPhase.setStatus("current")
_TlpAtsCircuitInputVoltage_Type = Integer32
_TlpAtsCircuitInputVoltage_Object = MibTableColumn
tlpAtsCircuitInputVoltage = _TlpAtsCircuitInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 3),
    _TlpAtsCircuitInputVoltage_Type()
)
tlpAtsCircuitInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitInputVoltage.setUnits("0.1 Volt DC")
_TlpAtsCircuitTotalCurrent_Type = Integer32
_TlpAtsCircuitTotalCurrent_Object = MibTableColumn
tlpAtsCircuitTotalCurrent = _TlpAtsCircuitTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 4),
    _TlpAtsCircuitTotalCurrent_Type()
)
tlpAtsCircuitTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitTotalCurrent.setUnits("0.01 Amp DC")
_TlpAtsCircuitCurrentLimit_Type = Integer32
_TlpAtsCircuitCurrentLimit_Object = MibTableColumn
tlpAtsCircuitCurrentLimit = _TlpAtsCircuitCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 5),
    _TlpAtsCircuitCurrentLimit_Type()
)
tlpAtsCircuitCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentLimit.setUnits("0.01 Amp DC")
_TlpAtsCircuitCurrentMin_Type = Integer32
_TlpAtsCircuitCurrentMin_Object = MibTableColumn
tlpAtsCircuitCurrentMin = _TlpAtsCircuitCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 6),
    _TlpAtsCircuitCurrentMin_Type()
)
tlpAtsCircuitCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentMin.setUnits("0.01 Amp DC")
_TlpAtsCircuitCurrentMax_Type = Integer32
_TlpAtsCircuitCurrentMax_Object = MibTableColumn
tlpAtsCircuitCurrentMax = _TlpAtsCircuitCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 7),
    _TlpAtsCircuitCurrentMax_Type()
)
tlpAtsCircuitCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitCurrentMax.setUnits("0.01 Amp DC")
_TlpAtsCircuitTotalPower_Type = Integer32
_TlpAtsCircuitTotalPower_Object = MibTableColumn
tlpAtsCircuitTotalPower = _TlpAtsCircuitTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 8),
    _TlpAtsCircuitTotalPower_Type()
)
tlpAtsCircuitTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitTotalPower.setUnits("Watts")


class _TlpAtsCircuitPowerFactor_Type(Integer32):
    """Custom type tlpAtsCircuitPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TlpAtsCircuitPowerFactor_Type.__name__ = "Integer32"
_TlpAtsCircuitPowerFactor_Object = MibTableColumn
tlpAtsCircuitPowerFactor = _TlpAtsCircuitPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 9),
    _TlpAtsCircuitPowerFactor_Type()
)
tlpAtsCircuitPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitPowerFactor.setUnits("percent")
_TlpAtsCircuitUtilization_Type = Unsigned32
_TlpAtsCircuitUtilization_Object = MibTableColumn
tlpAtsCircuitUtilization = _TlpAtsCircuitUtilization_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 4, 1, 1, 10),
    _TlpAtsCircuitUtilization_Type()
)
tlpAtsCircuitUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsCircuitUtilization.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsCircuitUtilization.setUnits("0.01 %")
_TlpAtsBreaker_ObjectIdentity = ObjectIdentity
tlpAtsBreaker = _TlpAtsBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5)
)
_TlpAtsBreakerTable_Object = MibTable
tlpAtsBreakerTable = _TlpAtsBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpAtsBreakerTable.setStatus("current")
_TlpAtsBreakerEntry_Object = MibTableRow
tlpAtsBreakerEntry = _TlpAtsBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5, 1, 1)
)
tlpAtsBreakerEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsBreakerIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsBreakerEntry.setStatus("current")
_TlpAtsBreakerIndex_Type = Unsigned32
_TlpAtsBreakerIndex_Object = MibTableColumn
tlpAtsBreakerIndex = _TlpAtsBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5, 1, 1, 1),
    _TlpAtsBreakerIndex_Type()
)
tlpAtsBreakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsBreakerIndex.setStatus("current")


class _TlpAtsBreakerStatus_Type(Integer32):
    """Custom type tlpAtsBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("notInstalled", 2),
          ("open", 0))
    )


_TlpAtsBreakerStatus_Type.__name__ = "Integer32"
_TlpAtsBreakerStatus_Object = MibTableColumn
tlpAtsBreakerStatus = _TlpAtsBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 5, 1, 1, 2),
    _TlpAtsBreakerStatus_Type()
)
tlpAtsBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsBreakerStatus.setStatus("current")
_TlpAtsHeatsink_ObjectIdentity = ObjectIdentity
tlpAtsHeatsink = _TlpAtsHeatsink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6)
)
_TlpAtsHeatsinkTable_Object = MibTable
tlpAtsHeatsinkTable = _TlpAtsHeatsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1)
)
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTable.setStatus("current")
_TlpAtsHeatsinkEntry_Object = MibTableRow
tlpAtsHeatsinkEntry = _TlpAtsHeatsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1)
)
tlpAtsHeatsinkEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAtsHeatsinkIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsHeatsinkEntry.setStatus("current")
_TlpAtsHeatsinkIndex_Type = Unsigned32
_TlpAtsHeatsinkIndex_Object = MibTableColumn
tlpAtsHeatsinkIndex = _TlpAtsHeatsinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1, 1),
    _TlpAtsHeatsinkIndex_Type()
)
tlpAtsHeatsinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkIndex.setStatus("current")


class _TlpAtsHeatsinkStatus_Type(Integer32):
    """Custom type tlpAtsHeatsinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 0))
    )


_TlpAtsHeatsinkStatus_Type.__name__ = "Integer32"
_TlpAtsHeatsinkStatus_Object = MibTableColumn
tlpAtsHeatsinkStatus = _TlpAtsHeatsinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1, 2),
    _TlpAtsHeatsinkStatus_Type()
)
tlpAtsHeatsinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkStatus.setStatus("current")
_TlpAtsHeatsinkTemperatureC_Type = Integer32
_TlpAtsHeatsinkTemperatureC_Object = MibTableColumn
tlpAtsHeatsinkTemperatureC = _TlpAtsHeatsinkTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1, 3),
    _TlpAtsHeatsinkTemperatureC_Type()
)
tlpAtsHeatsinkTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTemperatureC.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTemperatureC.setUnits("0.1 degrees Centigrade")
_TlpAtsHeatsinkTemperatureF_Type = Integer32
_TlpAtsHeatsinkTemperatureF_Object = MibTableColumn
tlpAtsHeatsinkTemperatureF = _TlpAtsHeatsinkTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 3, 6, 1, 1, 4),
    _TlpAtsHeatsinkTemperatureF_Type()
)
tlpAtsHeatsinkTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTemperatureF.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsHeatsinkTemperatureF.setUnits("0.1 degrees Farenheit")
_TlpAtsControl_ObjectIdentity = ObjectIdentity
tlpAtsControl = _TlpAtsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4)
)
_TlpAtsControlTable_Object = MibTable
tlpAtsControlTable = _TlpAtsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    tlpAtsControlTable.setStatus("current")
_TlpAtsControlEntry_Object = MibTableRow
tlpAtsControlEntry = _TlpAtsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1)
)
tlpAtsControlEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsControlEntry.setStatus("current")
_TlpAtsControlRamp_Type = TruthValue
_TlpAtsControlRamp_Object = MibTableColumn
tlpAtsControlRamp = _TlpAtsControlRamp_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 1),
    _TlpAtsControlRamp_Type()
)
tlpAtsControlRamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlRamp.setStatus("current")
_TlpAtsControlShed_Type = TruthValue
_TlpAtsControlShed_Object = MibTableColumn
tlpAtsControlShed = _TlpAtsControlShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 2),
    _TlpAtsControlShed_Type()
)
tlpAtsControlShed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlShed.setStatus("current")
_TlpAtsControlAtsOn_Type = TruthValue
_TlpAtsControlAtsOn_Object = MibTableColumn
tlpAtsControlAtsOn = _TlpAtsControlAtsOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 3),
    _TlpAtsControlAtsOn_Type()
)
tlpAtsControlAtsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlAtsOn.setStatus("current")
_TlpAtsControlAtsOff_Type = TruthValue
_TlpAtsControlAtsOff_Object = MibTableColumn
tlpAtsControlAtsOff = _TlpAtsControlAtsOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 4),
    _TlpAtsControlAtsOff_Type()
)
tlpAtsControlAtsOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlAtsOff.setStatus("current")
_TlpAtsControlAtsReboot_Type = TruthValue
_TlpAtsControlAtsReboot_Object = MibTableColumn
tlpAtsControlAtsReboot = _TlpAtsControlAtsReboot_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 5),
    _TlpAtsControlAtsReboot_Type()
)
tlpAtsControlAtsReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlAtsReboot.setStatus("current")
_TlpAtsControlResetGeneralFault_Type = TruthValue
_TlpAtsControlResetGeneralFault_Object = MibTableColumn
tlpAtsControlResetGeneralFault = _TlpAtsControlResetGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 4, 1, 1, 6),
    _TlpAtsControlResetGeneralFault_Type()
)
tlpAtsControlResetGeneralFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsControlResetGeneralFault.setStatus("current")
_TlpAtsConfig_ObjectIdentity = ObjectIdentity
tlpAtsConfig = _TlpAtsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5)
)
_TlpAtsConfigTable_Object = MibTable
tlpAtsConfigTable = _TlpAtsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1)
)
if mibBuilder.loadTexts:
    tlpAtsConfigTable.setStatus("current")
_TlpAtsConfigEntry_Object = MibTableRow
tlpAtsConfigEntry = _TlpAtsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1)
)
tlpAtsConfigEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigEntry.setStatus("current")
_TlpAtsConfigInputVoltage_Type = Unsigned32
_TlpAtsConfigInputVoltage_Object = MibTableColumn
tlpAtsConfigInputVoltage = _TlpAtsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 1),
    _TlpAtsConfigInputVoltage_Type()
)
tlpAtsConfigInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigInputVoltage.setStatus("current")


class _TlpAtsConfigSourceSelect_Type(Integer32):
    """Custom type tlpAtsConfigSourceSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inputSourceA", 1),
          ("inputSourceB", 2))
    )


_TlpAtsConfigSourceSelect_Type.__name__ = "Integer32"
_TlpAtsConfigSourceSelect_Object = MibTableColumn
tlpAtsConfigSourceSelect = _TlpAtsConfigSourceSelect_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 2),
    _TlpAtsConfigSourceSelect_Type()
)
tlpAtsConfigSourceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceSelect.setStatus("current")
_TlpAtsConfigSource1ReturnTime_Type = Unsigned32
_TlpAtsConfigSource1ReturnTime_Object = MibTableColumn
tlpAtsConfigSource1ReturnTime = _TlpAtsConfigSource1ReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 3),
    _TlpAtsConfigSource1ReturnTime_Type()
)
tlpAtsConfigSource1ReturnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1ReturnTime.setStatus("current")
_TlpAtsConfigSource2ReturnTime_Type = Unsigned32
_TlpAtsConfigSource2ReturnTime_Object = MibTableColumn
tlpAtsConfigSource2ReturnTime = _TlpAtsConfigSource2ReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 4),
    _TlpAtsConfigSource2ReturnTime_Type()
)
tlpAtsConfigSource2ReturnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2ReturnTime.setStatus("current")


class _TlpAtsConfigAutoRampOnTransition_Type(Integer32):
    """Custom type tlpAtsConfigAutoRampOnTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpAtsConfigAutoRampOnTransition_Type.__name__ = "Integer32"
_TlpAtsConfigAutoRampOnTransition_Object = MibTableColumn
tlpAtsConfigAutoRampOnTransition = _TlpAtsConfigAutoRampOnTransition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 5),
    _TlpAtsConfigAutoRampOnTransition_Type()
)
tlpAtsConfigAutoRampOnTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigAutoRampOnTransition.setStatus("current")


class _TlpAtsConfigAutoShedOnTransition_Type(Integer32):
    """Custom type tlpAtsConfigAutoShedOnTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlpAtsConfigAutoShedOnTransition_Type.__name__ = "Integer32"
_TlpAtsConfigAutoShedOnTransition_Object = MibTableColumn
tlpAtsConfigAutoShedOnTransition = _TlpAtsConfigAutoShedOnTransition_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 1, 1, 6),
    _TlpAtsConfigAutoShedOnTransition_Type()
)
tlpAtsConfigAutoShedOnTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigAutoShedOnTransition.setStatus("current")
_TlpAtsConfigVoltageRangeTable_Object = MibTable
tlpAtsConfigVoltageRangeTable = _TlpAtsConfigVoltageRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2)
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeTable.setStatus("current")
_TlpAtsConfigVoltageRangeEntry_Object = MibTableRow
tlpAtsConfigVoltageRangeEntry = _TlpAtsConfigVoltageRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1)
)
tlpAtsConfigVoltageRangeEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeEntry.setStatus("current")
_TlpAtsConfigHighVoltageTransfer_Type = Unsigned32
_TlpAtsConfigHighVoltageTransfer_Object = MibTableColumn
tlpAtsConfigHighVoltageTransfer = _TlpAtsConfigHighVoltageTransfer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 1),
    _TlpAtsConfigHighVoltageTransfer_Type()
)
tlpAtsConfigHighVoltageTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageTransfer.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageTransfer.setUnits("0.1 Volts")
_TlpAtsConfigHighVoltageReset_Type = Unsigned32
_TlpAtsConfigHighVoltageReset_Object = MibTableColumn
tlpAtsConfigHighVoltageReset = _TlpAtsConfigHighVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 2),
    _TlpAtsConfigHighVoltageReset_Type()
)
tlpAtsConfigHighVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageReset.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigHighVoltageReset.setUnits("0.1 Volts")
_TlpAtsConfigSource1TransferReset_Type = Unsigned32
_TlpAtsConfigSource1TransferReset_Object = MibTableColumn
tlpAtsConfigSource1TransferReset = _TlpAtsConfigSource1TransferReset_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 3),
    _TlpAtsConfigSource1TransferReset_Type()
)
tlpAtsConfigSource1TransferReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1TransferReset.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1TransferReset.setUnits("0.1 Volts")
_TlpAtsConfigSource1BrownoutSet_Type = Unsigned32
_TlpAtsConfigSource1BrownoutSet_Object = MibTableColumn
tlpAtsConfigSource1BrownoutSet = _TlpAtsConfigSource1BrownoutSet_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 4),
    _TlpAtsConfigSource1BrownoutSet_Type()
)
tlpAtsConfigSource1BrownoutSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1BrownoutSet.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1BrownoutSet.setUnits("0.1 Volts")
_TlpAtsConfigSource1TransferSet_Type = Unsigned32
_TlpAtsConfigSource1TransferSet_Object = MibTableColumn
tlpAtsConfigSource1TransferSet = _TlpAtsConfigSource1TransferSet_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 5),
    _TlpAtsConfigSource1TransferSet_Type()
)
tlpAtsConfigSource1TransferSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1TransferSet.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSource1TransferSet.setUnits("0.1 Volts")
_TlpAtsConfigSource2TransferReset_Type = Unsigned32
_TlpAtsConfigSource2TransferReset_Object = MibTableColumn
tlpAtsConfigSource2TransferReset = _TlpAtsConfigSource2TransferReset_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 6),
    _TlpAtsConfigSource2TransferReset_Type()
)
tlpAtsConfigSource2TransferReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2TransferReset.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2TransferReset.setUnits("0.1 Volts")
_TlpAtsConfigSource2BrownoutSet_Type = Unsigned32
_TlpAtsConfigSource2BrownoutSet_Object = MibTableColumn
tlpAtsConfigSource2BrownoutSet = _TlpAtsConfigSource2BrownoutSet_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 7),
    _TlpAtsConfigSource2BrownoutSet_Type()
)
tlpAtsConfigSource2BrownoutSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2BrownoutSet.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2BrownoutSet.setUnits("0.1 Volts")
_TlpAtsConfigSource2TransferSet_Type = Unsigned32
_TlpAtsConfigSource2TransferSet_Object = MibTableColumn
tlpAtsConfigSource2TransferSet = _TlpAtsConfigSource2TransferSet_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 8),
    _TlpAtsConfigSource2TransferSet_Type()
)
tlpAtsConfigSource2TransferSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2TransferSet.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSource2TransferSet.setUnits("0.1 Volts")
_TlpAtsConfigLowVoltageReset_Type = Unsigned32
_TlpAtsConfigLowVoltageReset_Object = MibTableColumn
tlpAtsConfigLowVoltageReset = _TlpAtsConfigLowVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 9),
    _TlpAtsConfigLowVoltageReset_Type()
)
tlpAtsConfigLowVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageReset.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageReset.setUnits("0.1 Volts")
_TlpAtsConfigLowVoltageTransfer_Type = Unsigned32
_TlpAtsConfigLowVoltageTransfer_Object = MibTableColumn
tlpAtsConfigLowVoltageTransfer = _TlpAtsConfigLowVoltageTransfer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 2, 1, 10),
    _TlpAtsConfigLowVoltageTransfer_Type()
)
tlpAtsConfigLowVoltageTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageTransfer.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigLowVoltageTransfer.setUnits("0.1 Volts")
_TlpAtsConfigVoltageRangeLimitsTable_Object = MibTable
tlpAtsConfigVoltageRangeLimitsTable = _TlpAtsConfigVoltageRangeLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3)
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeLimitsTable.setStatus("current")
_TlpAtsConfigVoltageRangeLimitsEntry_Object = MibTableRow
tlpAtsConfigVoltageRangeLimitsEntry = _TlpAtsConfigVoltageRangeLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1)
)
tlpAtsConfigVoltageRangeLimitsEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigVoltageRangeLimitsEntry.setStatus("current")
_TlpAtsConfigSourceBrownoutSetMinimum_Type = Unsigned32
_TlpAtsConfigSourceBrownoutSetMinimum_Object = MibTableColumn
tlpAtsConfigSourceBrownoutSetMinimum = _TlpAtsConfigSourceBrownoutSetMinimum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1, 1),
    _TlpAtsConfigSourceBrownoutSetMinimum_Type()
)
tlpAtsConfigSourceBrownoutSetMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceBrownoutSetMinimum.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceBrownoutSetMinimum.setUnits("0.1 Volts")
_TlpAtsConfigSourceBrownoutSetMaximum_Type = Unsigned32
_TlpAtsConfigSourceBrownoutSetMaximum_Object = MibTableColumn
tlpAtsConfigSourceBrownoutSetMaximum = _TlpAtsConfigSourceBrownoutSetMaximum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1, 2),
    _TlpAtsConfigSourceBrownoutSetMaximum_Type()
)
tlpAtsConfigSourceBrownoutSetMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceBrownoutSetMaximum.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceBrownoutSetMaximum.setUnits("0.1 Volts")
_TlpAtsConfigSourceTransferSetMinimum_Type = Unsigned32
_TlpAtsConfigSourceTransferSetMinimum_Object = MibTableColumn
tlpAtsConfigSourceTransferSetMinimum = _TlpAtsConfigSourceTransferSetMinimum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1, 3),
    _TlpAtsConfigSourceTransferSetMinimum_Type()
)
tlpAtsConfigSourceTransferSetMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceTransferSetMinimum.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceTransferSetMinimum.setUnits("0.1 Volts")
_TlpAtsConfigSourceTransferSetMaximum_Type = Unsigned32
_TlpAtsConfigSourceTransferSetMaximum_Object = MibTableColumn
tlpAtsConfigSourceTransferSetMaximum = _TlpAtsConfigSourceTransferSetMaximum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 3, 1, 4),
    _TlpAtsConfigSourceTransferSetMaximum_Type()
)
tlpAtsConfigSourceTransferSetMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceTransferSetMaximum.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigSourceTransferSetMaximum.setUnits("0.1 Volts")
_TlpAtsConfigThresholdTable_Object = MibTable
tlpAtsConfigThresholdTable = _TlpAtsConfigThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4)
)
if mibBuilder.loadTexts:
    tlpAtsConfigThresholdTable.setStatus("current")
_TlpAtsConfigThresholdEntry_Object = MibTableRow
tlpAtsConfigThresholdEntry = _TlpAtsConfigThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1)
)
tlpAtsConfigThresholdEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
)
if mibBuilder.loadTexts:
    tlpAtsConfigThresholdEntry.setStatus("current")
_TlpAtsConfigOverCurrentThreshold_Type = Unsigned32
_TlpAtsConfigOverCurrentThreshold_Object = MibTableColumn
tlpAtsConfigOverCurrentThreshold = _TlpAtsConfigOverCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1, 1),
    _TlpAtsConfigOverCurrentThreshold_Type()
)
tlpAtsConfigOverCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOverCurrentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOverCurrentThreshold.setUnits("0.1 Amps")
_TlpAtsConfigOverTemperatureThreshold_Type = Unsigned32
_TlpAtsConfigOverTemperatureThreshold_Object = MibTableColumn
tlpAtsConfigOverTemperatureThreshold = _TlpAtsConfigOverTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1, 2),
    _TlpAtsConfigOverTemperatureThreshold_Type()
)
tlpAtsConfigOverTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOverTemperatureThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOverTemperatureThreshold.setUnits("0.1 Centigrade")
_TlpAtsConfigOverVoltageThreshold_Type = Unsigned32
_TlpAtsConfigOverVoltageThreshold_Object = MibTableColumn
tlpAtsConfigOverVoltageThreshold = _TlpAtsConfigOverVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1, 3),
    _TlpAtsConfigOverVoltageThreshold_Type()
)
tlpAtsConfigOverVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOverVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tlpAtsConfigOverVoltageThreshold.setUnits("0.1 Volts")
_TlpAtsConfigOverLoadThreshold_Type = Unsigned32
_TlpAtsConfigOverLoadThreshold_Object = MibTableColumn
tlpAtsConfigOverLoadThreshold = _TlpAtsConfigOverLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4, 5, 4, 1, 4),
    _TlpAtsConfigOverLoadThreshold_Type()
)
tlpAtsConfigOverLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAtsConfigOverLoadThreshold.setStatus("current")
_TlpCooling_ObjectIdentity = ObjectIdentity
tlpCooling = _TlpCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5)
)
_TlpCoolingIdent_ObjectIdentity = ObjectIdentity
tlpCoolingIdent = _TlpCoolingIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 1)
)
_TlpCoolingIdentNumCooling_Type = Unsigned32
_TlpCoolingIdentNumCooling_Object = MibScalar
tlpCoolingIdentNumCooling = _TlpCoolingIdentNumCooling_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 1, 1),
    _TlpCoolingIdentNumCooling_Type()
)
tlpCoolingIdentNumCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpCoolingIdentNumCooling.setStatus("current")
_TlpCoolingDevice_ObjectIdentity = ObjectIdentity
tlpCoolingDevice = _TlpCoolingDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 2)
)
_TlpCoolingDetail_ObjectIdentity = ObjectIdentity
tlpCoolingDetail = _TlpCoolingDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3)
)
_TlpCoolingInput_ObjectIdentity = ObjectIdentity
tlpCoolingInput = _TlpCoolingInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 1)
)
_TlpCoolingOutput_ObjectIdentity = ObjectIdentity
tlpCoolingOutput = _TlpCoolingOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 3, 2)
)
_TlpCoolingControl_ObjectIdentity = ObjectIdentity
tlpCoolingControl = _TlpCoolingControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 4)
)
_TlpCoolingConfig_ObjectIdentity = ObjectIdentity
tlpCoolingConfig = _TlpCoolingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 5)
)
_TlpKvm_ObjectIdentity = ObjectIdentity
tlpKvm = _TlpKvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6)
)
_TlpKvmIdent_ObjectIdentity = ObjectIdentity
tlpKvmIdent = _TlpKvmIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 1)
)
_TlpKvmIdentNumKvm_Type = Unsigned32
_TlpKvmIdentNumKvm_Object = MibScalar
tlpKvmIdentNumKvm = _TlpKvmIdentNumKvm_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 1, 1),
    _TlpKvmIdentNumKvm_Type()
)
tlpKvmIdentNumKvm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpKvmIdentNumKvm.setStatus("current")
_TlpKvmDevice_ObjectIdentity = ObjectIdentity
tlpKvmDevice = _TlpKvmDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 2)
)
_TlpKvmDetail_ObjectIdentity = ObjectIdentity
tlpKvmDetail = _TlpKvmDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 3)
)
_TlpKvmControl_ObjectIdentity = ObjectIdentity
tlpKvmControl = _TlpKvmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 4)
)
_TlpKvmConfig_ObjectIdentity = ObjectIdentity
tlpKvmConfig = _TlpKvmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 6, 5)
)
_TlpRackTrack_ObjectIdentity = ObjectIdentity
tlpRackTrack = _TlpRackTrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7)
)
_TlpRackTrackIdent_ObjectIdentity = ObjectIdentity
tlpRackTrackIdent = _TlpRackTrackIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 1)
)
_TlpRackTrackIdentNumRackTrack_Type = Unsigned32
_TlpRackTrackIdentNumRackTrack_Object = MibScalar
tlpRackTrackIdentNumRackTrack = _TlpRackTrackIdentNumRackTrack_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 1, 1),
    _TlpRackTrackIdentNumRackTrack_Type()
)
tlpRackTrackIdentNumRackTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpRackTrackIdentNumRackTrack.setStatus("current")
_TlpRackTrackDevice_ObjectIdentity = ObjectIdentity
tlpRackTrackDevice = _TlpRackTrackDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 2)
)
_TlpRackTrackDetail_ObjectIdentity = ObjectIdentity
tlpRackTrackDetail = _TlpRackTrackDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 3)
)
_TlpRackTrackControl_ObjectIdentity = ObjectIdentity
tlpRackTrackControl = _TlpRackTrackControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 4)
)
_TlpRackTrackConfig_ObjectIdentity = ObjectIdentity
tlpRackTrackConfig = _TlpRackTrackConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 7, 5)
)
_TlpSwitch_ObjectIdentity = ObjectIdentity
tlpSwitch = _TlpSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8)
)
_TlpSwitchIdent_ObjectIdentity = ObjectIdentity
tlpSwitchIdent = _TlpSwitchIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 1)
)
_TlpSwitchIdentNumSwitch_Type = Unsigned32
_TlpSwitchIdentNumSwitch_Object = MibScalar
tlpSwitchIdentNumSwitch = _TlpSwitchIdentNumSwitch_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 1, 1),
    _TlpSwitchIdentNumSwitch_Type()
)
tlpSwitchIdentNumSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpSwitchIdentNumSwitch.setStatus("current")
_TlpSwitchDevice_ObjectIdentity = ObjectIdentity
tlpSwitchDevice = _TlpSwitchDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 2)
)
_TlpSwitchDetail_ObjectIdentity = ObjectIdentity
tlpSwitchDetail = _TlpSwitchDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 3)
)
_TlpSwitchControl_ObjectIdentity = ObjectIdentity
tlpSwitchControl = _TlpSwitchControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 4)
)
_TlpSwitchConfig_ObjectIdentity = ObjectIdentity
tlpSwitchConfig = _TlpSwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 8, 5)
)
_TlpSoftware_ObjectIdentity = ObjectIdentity
tlpSoftware = _TlpSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2)
)
_TlpAgentDetails_ObjectIdentity = ObjectIdentity
tlpAgentDetails = _TlpAgentDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1)
)
_TlpAgentIdent_ObjectIdentity = ObjectIdentity
tlpAgentIdent = _TlpAgentIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1)
)


class _TlpAgentType_Type(Integer32):
    """Custom type tlpAgentType based on Integer32"""
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
        *(("delta", 3),
          ("netos6", 5),
          ("netos7", 6),
          ("nmc5", 8),
          ("pal", 1),
          ("panms", 7),
          ("pansa", 2),
          ("sinetica", 4),
          ("unknown", 0))
    )


_TlpAgentType_Type.__name__ = "Integer32"
_TlpAgentType_Object = MibScalar
tlpAgentType = _TlpAgentType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 1),
    _TlpAgentType_Type()
)
tlpAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentType.setStatus("current")
_TlpAgentVersion_Type = DisplayString
_TlpAgentVersion_Object = MibScalar
tlpAgentVersion = _TlpAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 2),
    _TlpAgentVersion_Type()
)
tlpAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentVersion.setStatus("current")
_TlpAgentDriverVersion_Type = DisplayString
_TlpAgentDriverVersion_Object = MibScalar
tlpAgentDriverVersion = _TlpAgentDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 3),
    _TlpAgentDriverVersion_Type()
)
tlpAgentDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentDriverVersion.setStatus("current")
_TlpAgentMAC_Type = DisplayString
_TlpAgentMAC_Object = MibScalar
tlpAgentMAC = _TlpAgentMAC_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 4),
    _TlpAgentMAC_Type()
)
tlpAgentMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentMAC.setStatus("current")
_TlpAgentSerialNum_Type = DisplayString
_TlpAgentSerialNum_Object = MibScalar
tlpAgentSerialNum = _TlpAgentSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 5),
    _TlpAgentSerialNum_Type()
)
tlpAgentSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentSerialNum.setStatus("current")
_TlpAgentUuid_Type = DisplayString
_TlpAgentUuid_Object = MibScalar
tlpAgentUuid = _TlpAgentUuid_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 1, 6),
    _TlpAgentUuid_Type()
)
tlpAgentUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentUuid.setStatus("current")
_TlpAgentAttributes_ObjectIdentity = ObjectIdentity
tlpAgentAttributes = _TlpAgentAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2)
)
_TlpAgentAttributesSupports_ObjectIdentity = ObjectIdentity
tlpAgentAttributesSupports = _TlpAgentAttributesSupports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1)
)
_TlpAgentAttributesSupportsHTTP_Type = TruthValue
_TlpAgentAttributesSupportsHTTP_Object = MibScalar
tlpAgentAttributesSupportsHTTP = _TlpAgentAttributesSupportsHTTP_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 1),
    _TlpAgentAttributesSupportsHTTP_Type()
)
tlpAgentAttributesSupportsHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsHTTP.setStatus("current")
_TlpAgentAttributesSupportsHTTPS_Type = TruthValue
_TlpAgentAttributesSupportsHTTPS_Object = MibScalar
tlpAgentAttributesSupportsHTTPS = _TlpAgentAttributesSupportsHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 2),
    _TlpAgentAttributesSupportsHTTPS_Type()
)
tlpAgentAttributesSupportsHTTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsHTTPS.setStatus("current")
_TlpAgentAttributesSupportsFTP_Type = TruthValue
_TlpAgentAttributesSupportsFTP_Object = MibScalar
tlpAgentAttributesSupportsFTP = _TlpAgentAttributesSupportsFTP_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 3),
    _TlpAgentAttributesSupportsFTP_Type()
)
tlpAgentAttributesSupportsFTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsFTP.setStatus("current")
_TlpAgentAttributesSupportsTelnetMenu_Type = TruthValue
_TlpAgentAttributesSupportsTelnetMenu_Object = MibScalar
tlpAgentAttributesSupportsTelnetMenu = _TlpAgentAttributesSupportsTelnetMenu_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 4),
    _TlpAgentAttributesSupportsTelnetMenu_Type()
)
tlpAgentAttributesSupportsTelnetMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsTelnetMenu.setStatus("current")
_TlpAgentAttributesSupportsTelnetCLI_Type = TruthValue
_TlpAgentAttributesSupportsTelnetCLI_Object = MibScalar
tlpAgentAttributesSupportsTelnetCLI = _TlpAgentAttributesSupportsTelnetCLI_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 5),
    _TlpAgentAttributesSupportsTelnetCLI_Type()
)
tlpAgentAttributesSupportsTelnetCLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsTelnetCLI.setStatus("current")
_TlpAgentAttributesSupportsSSHMenu_Type = TruthValue
_TlpAgentAttributesSupportsSSHMenu_Object = MibScalar
tlpAgentAttributesSupportsSSHMenu = _TlpAgentAttributesSupportsSSHMenu_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 6),
    _TlpAgentAttributesSupportsSSHMenu_Type()
)
tlpAgentAttributesSupportsSSHMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsSSHMenu.setStatus("current")
_TlpAgentAttributesSupportsSSHCLI_Type = TruthValue
_TlpAgentAttributesSupportsSSHCLI_Object = MibScalar
tlpAgentAttributesSupportsSSHCLI = _TlpAgentAttributesSupportsSSHCLI_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 7),
    _TlpAgentAttributesSupportsSSHCLI_Type()
)
tlpAgentAttributesSupportsSSHCLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsSSHCLI.setStatus("current")
_TlpAgentAttributesSupportsSNMP_Type = TruthValue
_TlpAgentAttributesSupportsSNMP_Object = MibScalar
tlpAgentAttributesSupportsSNMP = _TlpAgentAttributesSupportsSNMP_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 8),
    _TlpAgentAttributesSupportsSNMP_Type()
)
tlpAgentAttributesSupportsSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsSNMP.setStatus("current")
_TlpAgentAttributesSupportsSNMPTrap_Type = TruthValue
_TlpAgentAttributesSupportsSNMPTrap_Object = MibScalar
tlpAgentAttributesSupportsSNMPTrap = _TlpAgentAttributesSupportsSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 1, 9),
    _TlpAgentAttributesSupportsSNMPTrap_Type()
)
tlpAgentAttributesSupportsSNMPTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSupportsSNMPTrap.setStatus("current")
_TlpAgentAttributesAutostart_ObjectIdentity = ObjectIdentity
tlpAgentAttributesAutostart = _TlpAgentAttributesAutostart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2)
)
_TlpAgentAttributesAutostartHTTP_Type = TruthValue
_TlpAgentAttributesAutostartHTTP_Object = MibScalar
tlpAgentAttributesAutostartHTTP = _TlpAgentAttributesAutostartHTTP_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 1),
    _TlpAgentAttributesAutostartHTTP_Type()
)
tlpAgentAttributesAutostartHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesAutostartHTTP.setStatus("current")
_TlpAgentAttributesAutostartHTTPS_Type = TruthValue
_TlpAgentAttributesAutostartHTTPS_Object = MibScalar
tlpAgentAttributesAutostartHTTPS = _TlpAgentAttributesAutostartHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 2),
    _TlpAgentAttributesAutostartHTTPS_Type()
)
tlpAgentAttributesAutostartHTTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesAutostartHTTPS.setStatus("current")
_TlpAgentAttributesAutostartFTP_Type = TruthValue
_TlpAgentAttributesAutostartFTP_Object = MibScalar
tlpAgentAttributesAutostartFTP = _TlpAgentAttributesAutostartFTP_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 3),
    _TlpAgentAttributesAutostartFTP_Type()
)
tlpAgentAttributesAutostartFTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesAutostartFTP.setStatus("current")
_TlpAgentAttributesAutostartTelnetMenu_Type = TruthValue
_TlpAgentAttributesAutostartTelnetMenu_Object = MibScalar
tlpAgentAttributesAutostartTelnetMenu = _TlpAgentAttributesAutostartTelnetMenu_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 4),
    _TlpAgentAttributesAutostartTelnetMenu_Type()
)
tlpAgentAttributesAutostartTelnetMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesAutostartTelnetMenu.setStatus("current")
_TlpAgentAttributesAutostartTelnetCLI_Type = TruthValue
_TlpAgentAttributesAutostartTelnetCLI_Object = MibScalar
tlpAgentAttributesAutostartTelnetCLI = _TlpAgentAttributesAutostartTelnetCLI_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 5),
    _TlpAgentAttributesAutostartTelnetCLI_Type()
)
tlpAgentAttributesAutostartTelnetCLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesAutostartTelnetCLI.setStatus("current")
_TlpAgentAttributesAutostartSSHMenu_Type = TruthValue
_TlpAgentAttributesAutostartSSHMenu_Object = MibScalar
tlpAgentAttributesAutostartSSHMenu = _TlpAgentAttributesAutostartSSHMenu_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 6),
    _TlpAgentAttributesAutostartSSHMenu_Type()
)
tlpAgentAttributesAutostartSSHMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesAutostartSSHMenu.setStatus("current")
_TlpAgentAttributesAutostartSSHCLI_Type = TruthValue
_TlpAgentAttributesAutostartSSHCLI_Object = MibScalar
tlpAgentAttributesAutostartSSHCLI = _TlpAgentAttributesAutostartSSHCLI_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 7),
    _TlpAgentAttributesAutostartSSHCLI_Type()
)
tlpAgentAttributesAutostartSSHCLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesAutostartSSHCLI.setStatus("current")
_TlpAgentAttributesAutostartSNMP_Type = TruthValue
_TlpAgentAttributesAutostartSNMP_Object = MibScalar
tlpAgentAttributesAutostartSNMP = _TlpAgentAttributesAutostartSNMP_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 2, 8),
    _TlpAgentAttributesAutostartSNMP_Type()
)
tlpAgentAttributesAutostartSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesAutostartSNMP.setStatus("current")
_TlpAgentAttributesSnmp_ObjectIdentity = ObjectIdentity
tlpAgentAttributesSnmp = _TlpAgentAttributesSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 3)
)
_TlpAgentAttributesSNMPv1Enabled_Type = TruthValue
_TlpAgentAttributesSNMPv1Enabled_Object = MibScalar
tlpAgentAttributesSNMPv1Enabled = _TlpAgentAttributesSNMPv1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 3, 1),
    _TlpAgentAttributesSNMPv1Enabled_Type()
)
tlpAgentAttributesSNMPv1Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPv1Enabled.setStatus("current")
_TlpAgentAttributesSNMPv2cEnabled_Type = TruthValue
_TlpAgentAttributesSNMPv2cEnabled_Object = MibScalar
tlpAgentAttributesSNMPv2cEnabled = _TlpAgentAttributesSNMPv2cEnabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 3, 2),
    _TlpAgentAttributesSNMPv2cEnabled_Type()
)
tlpAgentAttributesSNMPv2cEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPv2cEnabled.setStatus("current")
_TlpAgentAttributesSNMPv3Enabled_Type = TruthValue
_TlpAgentAttributesSNMPv3Enabled_Object = MibScalar
tlpAgentAttributesSNMPv3Enabled = _TlpAgentAttributesSNMPv3Enabled_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 3, 3),
    _TlpAgentAttributesSNMPv3Enabled_Type()
)
tlpAgentAttributesSNMPv3Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPv3Enabled.setStatus("current")
_TlpAgentAttributesPorts_ObjectIdentity = ObjectIdentity
tlpAgentAttributesPorts = _TlpAgentAttributesPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4)
)
_TlpAgentAttributesHTTPPort_Type = Unsigned32
_TlpAgentAttributesHTTPPort_Object = MibScalar
tlpAgentAttributesHTTPPort = _TlpAgentAttributesHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 1),
    _TlpAgentAttributesHTTPPort_Type()
)
tlpAgentAttributesHTTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesHTTPPort.setStatus("current")
_TlpAgentAttributesHTTPSPort_Type = Unsigned32
_TlpAgentAttributesHTTPSPort_Object = MibScalar
tlpAgentAttributesHTTPSPort = _TlpAgentAttributesHTTPSPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 2),
    _TlpAgentAttributesHTTPSPort_Type()
)
tlpAgentAttributesHTTPSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesHTTPSPort.setStatus("current")
_TlpAgentAttributesFTPPort_Type = Unsigned32
_TlpAgentAttributesFTPPort_Object = MibScalar
tlpAgentAttributesFTPPort = _TlpAgentAttributesFTPPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 3),
    _TlpAgentAttributesFTPPort_Type()
)
tlpAgentAttributesFTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesFTPPort.setStatus("current")
_TlpAgentAttributesTelnetMenuPort_Type = Unsigned32
_TlpAgentAttributesTelnetMenuPort_Object = MibScalar
tlpAgentAttributesTelnetMenuPort = _TlpAgentAttributesTelnetMenuPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 4),
    _TlpAgentAttributesTelnetMenuPort_Type()
)
tlpAgentAttributesTelnetMenuPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesTelnetMenuPort.setStatus("current")
_TlpAgentAttributesTelnetCLIPort_Type = Unsigned32
_TlpAgentAttributesTelnetCLIPort_Object = MibScalar
tlpAgentAttributesTelnetCLIPort = _TlpAgentAttributesTelnetCLIPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 5),
    _TlpAgentAttributesTelnetCLIPort_Type()
)
tlpAgentAttributesTelnetCLIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesTelnetCLIPort.setStatus("current")
_TlpAgentAttributesSSHMenuPort_Type = Unsigned32
_TlpAgentAttributesSSHMenuPort_Object = MibScalar
tlpAgentAttributesSSHMenuPort = _TlpAgentAttributesSSHMenuPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 6),
    _TlpAgentAttributesSSHMenuPort_Type()
)
tlpAgentAttributesSSHMenuPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSSHMenuPort.setStatus("current")
_TlpAgentAttributesSSHCLIPort_Type = Unsigned32
_TlpAgentAttributesSSHCLIPort_Object = MibScalar
tlpAgentAttributesSSHCLIPort = _TlpAgentAttributesSSHCLIPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 7),
    _TlpAgentAttributesSSHCLIPort_Type()
)
tlpAgentAttributesSSHCLIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSSHCLIPort.setStatus("current")
_TlpAgentAttributesSNMPPort_Type = Unsigned32
_TlpAgentAttributesSNMPPort_Object = MibScalar
tlpAgentAttributesSNMPPort = _TlpAgentAttributesSNMPPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 8),
    _TlpAgentAttributesSNMPPort_Type()
)
tlpAgentAttributesSNMPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPPort.setStatus("current")
_TlpAgentAttributesSNMPTrapPort_Type = Unsigned32
_TlpAgentAttributesSNMPTrapPort_Object = MibScalar
tlpAgentAttributesSNMPTrapPort = _TlpAgentAttributesSNMPTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 1, 2, 4, 9),
    _TlpAgentAttributesSNMPTrapPort_Type()
)
tlpAgentAttributesSNMPTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentAttributesSNMPTrapPort.setStatus("current")
_TlpAgentSettings_ObjectIdentity = ObjectIdentity
tlpAgentSettings = _TlpAgentSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 2)
)
_TlpAgentConfig_ObjectIdentity = ObjectIdentity
tlpAgentConfig = _TlpAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 2, 1)
)
_TlpAgentConfigRemoteRegistration_Type = DisplayString
_TlpAgentConfigRemoteRegistration_Object = MibScalar
tlpAgentConfigRemoteRegistration = _TlpAgentConfigRemoteRegistration_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 2, 1, 1),
    _TlpAgentConfigRemoteRegistration_Type()
)
tlpAgentConfigRemoteRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentConfigRemoteRegistration.setStatus("current")
_TlpAgentConfigCurrentTime_Type = DisplayString
_TlpAgentConfigCurrentTime_Object = MibScalar
tlpAgentConfigCurrentTime = _TlpAgentConfigCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 2, 1, 2),
    _TlpAgentConfigCurrentTime_Type()
)
tlpAgentConfigCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentConfigCurrentTime.setStatus("current")
_TlpAgentContacts_ObjectIdentity = ObjectIdentity
tlpAgentContacts = _TlpAgentContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3)
)
_TlpAgentEmailContacts_ObjectIdentity = ObjectIdentity
tlpAgentEmailContacts = _TlpAgentEmailContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1)
)
_TlpAgentNumEmailContacts_Type = Unsigned32
_TlpAgentNumEmailContacts_Object = MibScalar
tlpAgentNumEmailContacts = _TlpAgentNumEmailContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 1),
    _TlpAgentNumEmailContacts_Type()
)
tlpAgentNumEmailContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentNumEmailContacts.setStatus("current")
_TlpAgentEmailContactTable_Object = MibTable
tlpAgentEmailContactTable = _TlpAgentEmailContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tlpAgentEmailContactTable.setStatus("current")
_TlpAgentEmailContactEntry_Object = MibTableRow
tlpAgentEmailContactEntry = _TlpAgentEmailContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1)
)
tlpAgentEmailContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpAgentEmailContactIndex"),
)
if mibBuilder.loadTexts:
    tlpAgentEmailContactEntry.setStatus("current")
_TlpAgentEmailContactIndex_Type = Unsigned32
_TlpAgentEmailContactIndex_Object = MibTableColumn
tlpAgentEmailContactIndex = _TlpAgentEmailContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1, 1),
    _TlpAgentEmailContactIndex_Type()
)
tlpAgentEmailContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentEmailContactIndex.setStatus("current")
_TlpAgentEmailContactRowStatus_Type = RowStatus
_TlpAgentEmailContactRowStatus_Object = MibTableColumn
tlpAgentEmailContactRowStatus = _TlpAgentEmailContactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1, 2),
    _TlpAgentEmailContactRowStatus_Type()
)
tlpAgentEmailContactRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentEmailContactRowStatus.setStatus("current")
_TlpAgentEmailContactName_Type = DisplayString
_TlpAgentEmailContactName_Object = MibTableColumn
tlpAgentEmailContactName = _TlpAgentEmailContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1, 3),
    _TlpAgentEmailContactName_Type()
)
tlpAgentEmailContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentEmailContactName.setStatus("current")
_TlpAgentEmailContactAddress_Type = DisplayString
_TlpAgentEmailContactAddress_Object = MibTableColumn
tlpAgentEmailContactAddress = _TlpAgentEmailContactAddress_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 1, 2, 1, 4),
    _TlpAgentEmailContactAddress_Type()
)
tlpAgentEmailContactAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentEmailContactAddress.setStatus("current")
_TlpAgentSnmpContacts_ObjectIdentity = ObjectIdentity
tlpAgentSnmpContacts = _TlpAgentSnmpContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2)
)
_TlpAgentNumSnmpContacts_Type = Unsigned32
_TlpAgentNumSnmpContacts_Object = MibScalar
tlpAgentNumSnmpContacts = _TlpAgentNumSnmpContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 1),
    _TlpAgentNumSnmpContacts_Type()
)
tlpAgentNumSnmpContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentNumSnmpContacts.setStatus("current")
_TlpAgentSnmpContactTable_Object = MibTable
tlpAgentSnmpContactTable = _TlpAgentSnmpContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tlpAgentSnmpContactTable.setStatus("current")
_TlpAgentSnmpContactEntry_Object = MibTableRow
tlpAgentSnmpContactEntry = _TlpAgentSnmpContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1)
)
tlpAgentSnmpContactEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpAgentSnmpContactIndex"),
)
if mibBuilder.loadTexts:
    tlpAgentSnmpContactEntry.setStatus("current")
_TlpAgentSnmpContactIndex_Type = Unsigned32
_TlpAgentSnmpContactIndex_Object = MibTableColumn
tlpAgentSnmpContactIndex = _TlpAgentSnmpContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 1),
    _TlpAgentSnmpContactIndex_Type()
)
tlpAgentSnmpContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactIndex.setStatus("current")
_TlpAgentSnmpContactRowStatus_Type = RowStatus
_TlpAgentSnmpContactRowStatus_Object = MibTableColumn
tlpAgentSnmpContactRowStatus = _TlpAgentSnmpContactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 2),
    _TlpAgentSnmpContactRowStatus_Type()
)
tlpAgentSnmpContactRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactRowStatus.setStatus("current")
_TlpAgentSnmpContactName_Type = DisplayString
_TlpAgentSnmpContactName_Object = MibTableColumn
tlpAgentSnmpContactName = _TlpAgentSnmpContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 3),
    _TlpAgentSnmpContactName_Type()
)
tlpAgentSnmpContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactName.setStatus("current")
_TlpAgentSnmpContactIpAddress_Type = DisplayString
_TlpAgentSnmpContactIpAddress_Object = MibTableColumn
tlpAgentSnmpContactIpAddress = _TlpAgentSnmpContactIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 4),
    _TlpAgentSnmpContactIpAddress_Type()
)
tlpAgentSnmpContactIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactIpAddress.setStatus("current")
_TlpAgentSnmpContactPort_Type = Unsigned32
_TlpAgentSnmpContactPort_Object = MibTableColumn
tlpAgentSnmpContactPort = _TlpAgentSnmpContactPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 5),
    _TlpAgentSnmpContactPort_Type()
)
tlpAgentSnmpContactPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactPort.setStatus("current")


class _TlpAgentSnmpContactSnmpVersion_Type(Integer32):
    """Custom type tlpAgentSnmpContactSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2),
          ("snmpv3", 3))
    )


_TlpAgentSnmpContactSnmpVersion_Type.__name__ = "Integer32"
_TlpAgentSnmpContactSnmpVersion_Object = MibTableColumn
tlpAgentSnmpContactSnmpVersion = _TlpAgentSnmpContactSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 6),
    _TlpAgentSnmpContactSnmpVersion_Type()
)
tlpAgentSnmpContactSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactSnmpVersion.setStatus("current")
_TlpAgentSnmpContactSecurityName_Type = DisplayString
_TlpAgentSnmpContactSecurityName_Object = MibTableColumn
tlpAgentSnmpContactSecurityName = _TlpAgentSnmpContactSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 7),
    _TlpAgentSnmpContactSecurityName_Type()
)
tlpAgentSnmpContactSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactSecurityName.setStatus("current")
_TlpAgentSnmpContactPrivPassword_Type = DisplayString
_TlpAgentSnmpContactPrivPassword_Object = MibTableColumn
tlpAgentSnmpContactPrivPassword = _TlpAgentSnmpContactPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 8),
    _TlpAgentSnmpContactPrivPassword_Type()
)
tlpAgentSnmpContactPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactPrivPassword.setStatus("current")
_TlpAgentSnmpContactAuthPassword_Type = DisplayString
_TlpAgentSnmpContactAuthPassword_Object = MibTableColumn
tlpAgentSnmpContactAuthPassword = _TlpAgentSnmpContactAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 2, 3, 2, 2, 1, 9),
    _TlpAgentSnmpContactAuthPassword_Type()
)
tlpAgentSnmpContactAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAgentSnmpContactAuthPassword.setStatus("current")
_TlpAlarms_ObjectIdentity = ObjectIdentity
tlpAlarms = _TlpAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3)
)
_TlpAlarmsPresent_Type = Unsigned32
_TlpAlarmsPresent_Object = MibScalar
tlpAlarmsPresent = _TlpAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 1),
    _TlpAlarmsPresent_Type()
)
tlpAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmsPresent.setStatus("current")
_TlpAlarmTable_Object = MibTable
tlpAlarmTable = _TlpAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tlpAlarmTable.setStatus("current")
_TlpAlarmEntry_Object = MibTableRow
tlpAlarmEntry = _TlpAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1)
)
tlpAlarmEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpAlarmId"),
)
if mibBuilder.loadTexts:
    tlpAlarmEntry.setStatus("current")
_TlpAlarmId_Type = Unsigned32
_TlpAlarmId_Object = MibTableColumn
tlpAlarmId = _TlpAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 1),
    _TlpAlarmId_Type()
)
tlpAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmId.setStatus("current")
_TlpAlarmDescr_Type = ObjectIdentifier
_TlpAlarmDescr_Object = MibTableColumn
tlpAlarmDescr = _TlpAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 2),
    _TlpAlarmDescr_Type()
)
tlpAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmDescr.setStatus("current")
_TlpAlarmTime_Type = TimeStamp
_TlpAlarmTime_Object = MibTableColumn
tlpAlarmTime = _TlpAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 3),
    _TlpAlarmTime_Type()
)
tlpAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmTime.setStatus("current")
_TlpAlarmTableRef_Type = ObjectIdentifier
_TlpAlarmTableRef_Object = MibTableColumn
tlpAlarmTableRef = _TlpAlarmTableRef_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 4),
    _TlpAlarmTableRef_Type()
)
tlpAlarmTableRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmTableRef.setStatus("current")
_TlpAlarmTableRowRef_Type = ObjectIdentifier
_TlpAlarmTableRowRef_Object = MibTableColumn
tlpAlarmTableRowRef = _TlpAlarmTableRowRef_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 5),
    _TlpAlarmTableRowRef_Type()
)
tlpAlarmTableRowRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmTableRowRef.setStatus("current")
_TlpAlarmDetail_Type = DisplayString
_TlpAlarmDetail_Object = MibTableColumn
tlpAlarmDetail = _TlpAlarmDetail_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 6),
    _TlpAlarmDetail_Type()
)
tlpAlarmDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmDetail.setStatus("current")


class _TlpAlarmType_Type(Integer32):
    """Custom type tlpAlarmType based on Integer32"""
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
        *(("critical", 1),
          ("custom", 6),
          ("info", 3),
          ("offline", 5),
          ("status", 4),
          ("warning", 2))
    )


_TlpAlarmType_Type.__name__ = "Integer32"
_TlpAlarmType_Object = MibTableColumn
tlpAlarmType = _TlpAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 7),
    _TlpAlarmType_Type()
)
tlpAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmType.setStatus("current")


class _TlpAlarmState_Type(Integer32):
    """Custom type tlpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_TlpAlarmState_Type.__name__ = "Integer32"
_TlpAlarmState_Object = MibTableColumn
tlpAlarmState = _TlpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 8),
    _TlpAlarmState_Type()
)
tlpAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmState.setStatus("current")


class _TlpAlarmAcknowledged_Type(Integer32):
    """Custom type tlpAlarmAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 2),
          ("notAcknowledged", 1))
    )


_TlpAlarmAcknowledged_Type.__name__ = "Integer32"
_TlpAlarmAcknowledged_Object = MibTableColumn
tlpAlarmAcknowledged = _TlpAlarmAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 2, 1, 9),
    _TlpAlarmAcknowledged_Type()
)
tlpAlarmAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAlarmAcknowledged.setStatus("current")
_TlpAlarmsWellKnown_ObjectIdentity = ObjectIdentity
tlpAlarmsWellKnown = _TlpAlarmsWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3)
)
_TlpAgentAlarms_ObjectIdentity = ObjectIdentity
tlpAgentAlarms = _TlpAgentAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 1)
)
_TlpDeviceAlarms_ObjectIdentity = ObjectIdentity
tlpDeviceAlarms = _TlpDeviceAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2)
)
_TlpAlarmCommunicationsLost_ObjectIdentity = ObjectIdentity
tlpAlarmCommunicationsLost = _TlpAlarmCommunicationsLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAlarmCommunicationsLost.setStatus("current")
_TlpAlarmUserDefined_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined = _TlpAlarmUserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2)
)
_TlpAlarmUserDefined01_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined01 = _TlpAlarmUserDefined01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined01.setStatus("current")
_TlpAlarmUserDefined02_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined02 = _TlpAlarmUserDefined02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined02.setStatus("current")
_TlpAlarmUserDefined03_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined03 = _TlpAlarmUserDefined03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined03.setStatus("current")
_TlpAlarmUserDefined04_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined04 = _TlpAlarmUserDefined04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined04.setStatus("current")
_TlpAlarmUserDefined05_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined05 = _TlpAlarmUserDefined05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined05.setStatus("current")
_TlpAlarmUserDefined06_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined06 = _TlpAlarmUserDefined06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined06.setStatus("current")
_TlpAlarmUserDefined07_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined07 = _TlpAlarmUserDefined07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 7)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined07.setStatus("current")
_TlpAlarmUserDefined08_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined08 = _TlpAlarmUserDefined08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 8)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined08.setStatus("current")
_TlpAlarmUserDefined09_ObjectIdentity = ObjectIdentity
tlpAlarmUserDefined09 = _TlpAlarmUserDefined09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 2, 2, 9)
)
if mibBuilder.loadTexts:
    tlpAlarmUserDefined09.setStatus("current")
_TlpUpsAlarms_ObjectIdentity = ObjectIdentity
tlpUpsAlarms = _TlpUpsAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3)
)
_TlpUpsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryBad = _TlpUpsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryBad.setStatus("current")
_TlpUpsAlarmOnBattery_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOnBattery = _TlpUpsAlarmOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOnBattery.setStatus("current")
_TlpUpsAlarmLowBattery_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLowBattery = _TlpUpsAlarmLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLowBattery.setStatus("current")
_TlpUpsAlarmDepletedBattery_ObjectIdentity = ObjectIdentity
tlpUpsAlarmDepletedBattery = _TlpUpsAlarmDepletedBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 4)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmDepletedBattery.setStatus("current")
_TlpUpsAlarmTempBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmTempBad = _TlpUpsAlarmTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 5)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmTempBad.setStatus("current")
_TlpUpsAlarmInputBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInputBad = _TlpUpsAlarmInputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 6)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInputBad.setStatus("current")
_TlpUpsAlarmOutputBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputBad = _TlpUpsAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 7)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputBad.setStatus("current")
_TlpUpsAlarmOutputOverload_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputOverload = _TlpUpsAlarmOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 8)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputOverload.setStatus("current")
_TlpUpsAlarmOnBypass_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOnBypass = _TlpUpsAlarmOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 9)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOnBypass.setStatus("current")
_TlpUpsAlarmBypassBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBypassBad = _TlpUpsAlarmBypassBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 10)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBypassBad.setStatus("current")
_TlpUpsAlarmOutputOffAsRequested_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputOffAsRequested = _TlpUpsAlarmOutputOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 11)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputOffAsRequested.setStatus("current")
_TlpUpsAlarmUpsOffAsRequested_ObjectIdentity = ObjectIdentity
tlpUpsAlarmUpsOffAsRequested = _TlpUpsAlarmUpsOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 12)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmUpsOffAsRequested.setStatus("current")
_TlpUpsAlarmChargerFailed_ObjectIdentity = ObjectIdentity
tlpUpsAlarmChargerFailed = _TlpUpsAlarmChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 13)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmChargerFailed.setStatus("current")
_TlpUpsAlarmUpsOutputOff_ObjectIdentity = ObjectIdentity
tlpUpsAlarmUpsOutputOff = _TlpUpsAlarmUpsOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 14)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmUpsOutputOff.setStatus("current")
_TlpUpsAlarmUpsSystemOff_ObjectIdentity = ObjectIdentity
tlpUpsAlarmUpsSystemOff = _TlpUpsAlarmUpsSystemOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 15)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmUpsSystemOff.setStatus("current")
_TlpUpsAlarmFanFailure_ObjectIdentity = ObjectIdentity
tlpUpsAlarmFanFailure = _TlpUpsAlarmFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 16)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmFanFailure.setStatus("current")
_TlpUpsAlarmFuseFailure_ObjectIdentity = ObjectIdentity
tlpUpsAlarmFuseFailure = _TlpUpsAlarmFuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 17)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmFuseFailure.setStatus("current")
_TlpUpsAlarmGeneralFault_ObjectIdentity = ObjectIdentity
tlpUpsAlarmGeneralFault = _TlpUpsAlarmGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 18)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmGeneralFault.setStatus("current")
_TlpUpsAlarmDiagnosticTestFailed_ObjectIdentity = ObjectIdentity
tlpUpsAlarmDiagnosticTestFailed = _TlpUpsAlarmDiagnosticTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 19)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmDiagnosticTestFailed.setStatus("current")
_TlpUpsAlarmAwaitingPower_ObjectIdentity = ObjectIdentity
tlpUpsAlarmAwaitingPower = _TlpUpsAlarmAwaitingPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 20)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmAwaitingPower.setStatus("current")
_TlpUpsAlarmShutdownPending_ObjectIdentity = ObjectIdentity
tlpUpsAlarmShutdownPending = _TlpUpsAlarmShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 21)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmShutdownPending.setStatus("current")
_TlpUpsAlarmShutdownImminent_ObjectIdentity = ObjectIdentity
tlpUpsAlarmShutdownImminent = _TlpUpsAlarmShutdownImminent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 22)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmShutdownImminent.setStatus("current")
_TlpUpsAlarmLoadLevelAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThreshold = _TlpUpsAlarmLoadLevelAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23)
)
_TlpUpsAlarmLoadLevelAboveThresholdTotal_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThresholdTotal = _TlpUpsAlarmLoadLevelAboveThresholdTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadLevelAboveThresholdTotal.setStatus("current")
_TlpUpsAlarmLoadLevelAboveThresholdPhase1_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThresholdPhase1 = _TlpUpsAlarmLoadLevelAboveThresholdPhase1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadLevelAboveThresholdPhase1.setStatus("current")
_TlpUpsAlarmLoadLevelAboveThresholdPhase2_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThresholdPhase2 = _TlpUpsAlarmLoadLevelAboveThresholdPhase2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadLevelAboveThresholdPhase2.setStatus("current")
_TlpUpsAlarmLoadLevelAboveThresholdPhase3_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadLevelAboveThresholdPhase3 = _TlpUpsAlarmLoadLevelAboveThresholdPhase3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 23, 4)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadLevelAboveThresholdPhase3.setStatus("current")
_TlpUpsAlarmOutputCurrentChanged_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOutputCurrentChanged = _TlpUpsAlarmOutputCurrentChanged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 24)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOutputCurrentChanged.setStatus("current")
_TlpUpsAlarmBatteryAgeAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryAgeAboveThreshold = _TlpUpsAlarmBatteryAgeAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 25)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryAgeAboveThreshold.setStatus("current")
_TlpUpsAlarmLoadOff_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff = _TlpUpsAlarmLoadOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26)
)
_TlpUpsAlarmLoadOff01_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff01 = _TlpUpsAlarmLoadOff01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff01.setStatus("current")
_TlpUpsAlarmLoadOff02_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff02 = _TlpUpsAlarmLoadOff02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff02.setStatus("current")
_TlpUpsAlarmLoadOff03_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff03 = _TlpUpsAlarmLoadOff03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff03.setStatus("current")
_TlpUpsAlarmLoadOff04_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff04 = _TlpUpsAlarmLoadOff04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 4)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff04.setStatus("current")
_TlpUpsAlarmLoadOff05_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff05 = _TlpUpsAlarmLoadOff05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 5)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff05.setStatus("current")
_TlpUpsAlarmLoadOff06_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff06 = _TlpUpsAlarmLoadOff06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 6)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff06.setStatus("current")
_TlpUpsAlarmLoadOff07_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff07 = _TlpUpsAlarmLoadOff07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 7)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff07.setStatus("current")
_TlpUpsAlarmLoadOff08_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff08 = _TlpUpsAlarmLoadOff08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 8)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff08.setStatus("current")
_TlpUpsAlarmLoadOff09_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff09 = _TlpUpsAlarmLoadOff09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 9)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff09.setStatus("current")
_TlpUpsAlarmLoadOff10_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff10 = _TlpUpsAlarmLoadOff10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 10)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff10.setStatus("current")
_TlpUpsAlarmLoadOff11_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff11 = _TlpUpsAlarmLoadOff11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 11)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff11.setStatus("current")
_TlpUpsAlarmLoadOff12_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff12 = _TlpUpsAlarmLoadOff12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 12)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff12.setStatus("current")
_TlpUpsAlarmLoadOff13_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff13 = _TlpUpsAlarmLoadOff13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 13)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff13.setStatus("current")
_TlpUpsAlarmLoadOff14_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff14 = _TlpUpsAlarmLoadOff14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 14)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff14.setStatus("current")
_TlpUpsAlarmLoadOff15_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff15 = _TlpUpsAlarmLoadOff15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 15)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff15.setStatus("current")
_TlpUpsAlarmLoadOff16_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff16 = _TlpUpsAlarmLoadOff16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 16)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff16.setStatus("current")
_TlpUpsAlarmLoadOff17_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff17 = _TlpUpsAlarmLoadOff17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 17)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff17.setStatus("current")
_TlpUpsAlarmLoadOff18_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff18 = _TlpUpsAlarmLoadOff18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 18)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff18.setStatus("current")
_TlpUpsAlarmLoadOff19_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff19 = _TlpUpsAlarmLoadOff19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 19)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff19.setStatus("current")
_TlpUpsAlarmLoadOff20_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff20 = _TlpUpsAlarmLoadOff20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 20)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff20.setStatus("current")
_TlpUpsAlarmLoadOff21_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff21 = _TlpUpsAlarmLoadOff21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 21)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff21.setStatus("current")
_TlpUpsAlarmLoadOff22_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff22 = _TlpUpsAlarmLoadOff22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 22)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff22.setStatus("current")
_TlpUpsAlarmLoadOff23_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff23 = _TlpUpsAlarmLoadOff23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 23)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff23.setStatus("current")
_TlpUpsAlarmLoadOff24_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff24 = _TlpUpsAlarmLoadOff24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 24)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff24.setStatus("current")
_TlpUpsAlarmLoadOff25_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff25 = _TlpUpsAlarmLoadOff25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 25)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff25.setStatus("current")
_TlpUpsAlarmLoadOff26_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff26 = _TlpUpsAlarmLoadOff26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 26)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff26.setStatus("current")
_TlpUpsAlarmLoadOff27_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff27 = _TlpUpsAlarmLoadOff27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 27)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff27.setStatus("current")
_TlpUpsAlarmLoadOff28_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff28 = _TlpUpsAlarmLoadOff28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 28)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff28.setStatus("current")
_TlpUpsAlarmLoadOff29_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff29 = _TlpUpsAlarmLoadOff29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 29)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff29.setStatus("current")
_TlpUpsAlarmLoadOff30_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff30 = _TlpUpsAlarmLoadOff30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 30)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff30.setStatus("current")
_TlpUpsAlarmLoadOff31_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff31 = _TlpUpsAlarmLoadOff31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 31)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff31.setStatus("current")
_TlpUpsAlarmLoadOff32_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff32 = _TlpUpsAlarmLoadOff32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 32)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff32.setStatus("current")
_TlpUpsAlarmLoadOff33_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff33 = _TlpUpsAlarmLoadOff33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 33)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff33.setStatus("current")
_TlpUpsAlarmLoadOff34_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff34 = _TlpUpsAlarmLoadOff34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 34)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff34.setStatus("current")
_TlpUpsAlarmLoadOff35_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff35 = _TlpUpsAlarmLoadOff35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 35)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff35.setStatus("current")
_TlpUpsAlarmLoadOff36_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff36 = _TlpUpsAlarmLoadOff36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 36)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff36.setStatus("current")
_TlpUpsAlarmLoadOff37_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff37 = _TlpUpsAlarmLoadOff37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 37)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff37.setStatus("current")
_TlpUpsAlarmLoadOff38_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff38 = _TlpUpsAlarmLoadOff38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 38)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff38.setStatus("current")
_TlpUpsAlarmLoadOff39_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff39 = _TlpUpsAlarmLoadOff39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 39)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff39.setStatus("current")
_TlpUpsAlarmLoadOff40_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadOff40 = _TlpUpsAlarmLoadOff40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 26, 40)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadOff40.setStatus("current")
_TlpUpsAlarmCurrentAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold = _TlpUpsAlarmCurrentAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27)
)
_TlpUpsAlarmCurrentAboveThreshold1_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold1 = _TlpUpsAlarmCurrentAboveThreshold1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27, 1)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentAboveThreshold1.setStatus("current")
_TlpUpsAlarmCurrentAboveThreshold2_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold2 = _TlpUpsAlarmCurrentAboveThreshold2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27, 2)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentAboveThreshold2.setStatus("current")
_TlpUpsAlarmCurrentAboveThreshold3_ObjectIdentity = ObjectIdentity
tlpUpsAlarmCurrentAboveThreshold3 = _TlpUpsAlarmCurrentAboveThreshold3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 27, 3)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmCurrentAboveThreshold3.setStatus("current")
_TlpUpsAlarmRuntimeBelowWarningLevel_ObjectIdentity = ObjectIdentity
tlpUpsAlarmRuntimeBelowWarningLevel = _TlpUpsAlarmRuntimeBelowWarningLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 28)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmRuntimeBelowWarningLevel.setStatus("current")
_TlpUpsAlarmBusStartVoltageLow_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBusStartVoltageLow = _TlpUpsAlarmBusStartVoltageLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 29)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBusStartVoltageLow.setStatus("current")
_TlpUpsAlarmBusOverVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBusOverVoltage = _TlpUpsAlarmBusOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 30)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBusOverVoltage.setStatus("current")
_TlpUpsAlarmBusUnderVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBusUnderVoltage = _TlpUpsAlarmBusUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 31)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBusUnderVoltage.setStatus("current")
_TlpUpsAlarmBusVoltageUnbalanced_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBusVoltageUnbalanced = _TlpUpsAlarmBusVoltageUnbalanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 32)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBusVoltageUnbalanced.setStatus("current")
_TlpUpsAlarmInverterSoftStartBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInverterSoftStartBad = _TlpUpsAlarmInverterSoftStartBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 33)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInverterSoftStartBad.setStatus("current")
_TlpUpsAlarmInverterOverVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInverterOverVoltage = _TlpUpsAlarmInverterOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 34)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInverterOverVoltage.setStatus("current")
_TlpUpsAlarmInverterUnderVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInverterUnderVoltage = _TlpUpsAlarmInverterUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 35)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInverterUnderVoltage.setStatus("current")
_TlpUpsAlarmInverterCircuitBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmInverterCircuitBad = _TlpUpsAlarmInverterCircuitBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 36)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmInverterCircuitBad.setStatus("current")
_TlpUpsAlarmBatteryOverVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryOverVoltage = _TlpUpsAlarmBatteryOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 37)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryOverVoltage.setStatus("current")
_TlpUpsAlarmBatteryUnderVoltage_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBatteryUnderVoltage = _TlpUpsAlarmBatteryUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 38)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBatteryUnderVoltage.setStatus("current")
_TlpUpsAlarmSiteWiringFault_ObjectIdentity = ObjectIdentity
tlpUpsAlarmSiteWiringFault = _TlpUpsAlarmSiteWiringFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 39)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmSiteWiringFault.setStatus("current")
_TlpUpsAlarmOverTemperatureProtection_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOverTemperatureProtection = _TlpUpsAlarmOverTemperatureProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 40)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOverTemperatureProtection.setStatus("current")
_TlpUpsAlarmOverCharged_ObjectIdentity = ObjectIdentity
tlpUpsAlarmOverCharged = _TlpUpsAlarmOverCharged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 41)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmOverCharged.setStatus("current")
_TlpUpsAlarmEPOActive_ObjectIdentity = ObjectIdentity
tlpUpsAlarmEPOActive = _TlpUpsAlarmEPOActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 42)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmEPOActive.setStatus("current")
_TlpUpsAlarmBypassFrequencyBad_ObjectIdentity = ObjectIdentity
tlpUpsAlarmBypassFrequencyBad = _TlpUpsAlarmBypassFrequencyBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 43)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmBypassFrequencyBad.setStatus("current")
_TlpUpsAlarmExternalSmartBatteryAgeAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmExternalSmartBatteryAgeAboveThreshold = _TlpUpsAlarmExternalSmartBatteryAgeAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 44)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmExternalSmartBatteryAgeAboveThreshold.setStatus("current")
_TlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold_ObjectIdentity = ObjectIdentity
tlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold = _TlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 45)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold.setStatus("current")
_TlpUpsAlarmSmartBatteryCommLost_ObjectIdentity = ObjectIdentity
tlpUpsAlarmSmartBatteryCommLost = _TlpUpsAlarmSmartBatteryCommLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 46)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmSmartBatteryCommLost.setStatus("current")
_TlpUpsAlarmLoadsNotAllOn_ObjectIdentity = ObjectIdentity
tlpUpsAlarmLoadsNotAllOn = _TlpUpsAlarmLoadsNotAllOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 3, 47)
)
if mibBuilder.loadTexts:
    tlpUpsAlarmLoadsNotAllOn.setStatus("current")
_TlpPduAlarms_ObjectIdentity = ObjectIdentity
tlpPduAlarms = _TlpPduAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4)
)
_TlpPduAlarmLoadLevelAboveThreshold_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadLevelAboveThreshold = _TlpPduAlarmLoadLevelAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadLevelAboveThreshold.setStatus("current")
_TlpPduAlarmInputBad_ObjectIdentity = ObjectIdentity
tlpPduAlarmInputBad = _TlpPduAlarmInputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    tlpPduAlarmInputBad.setStatus("current")
_TlpPduAlarmOutputBad_ObjectIdentity = ObjectIdentity
tlpPduAlarmOutputBad = _TlpPduAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 3)
)
if mibBuilder.loadTexts:
    tlpPduAlarmOutputBad.setStatus("current")
_TlpPduAlarmOutputOverload_ObjectIdentity = ObjectIdentity
tlpPduAlarmOutputOverload = _TlpPduAlarmOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 4)
)
if mibBuilder.loadTexts:
    tlpPduAlarmOutputOverload.setStatus("current")
_TlpPduAlarmOutputOff_ObjectIdentity = ObjectIdentity
tlpPduAlarmOutputOff = _TlpPduAlarmOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 5)
)
if mibBuilder.loadTexts:
    tlpPduAlarmOutputOff.setStatus("current")
_TlpPduAlarmLoadOff_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff = _TlpPduAlarmLoadOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6)
)
_TlpPduAlarmLoadOff01_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff01 = _TlpPduAlarmLoadOff01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff01.setStatus("current")
_TlpPduAlarmLoadOff02_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff02 = _TlpPduAlarmLoadOff02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 2)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff02.setStatus("current")
_TlpPduAlarmLoadOff03_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff03 = _TlpPduAlarmLoadOff03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 3)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff03.setStatus("current")
_TlpPduAlarmLoadOff04_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff04 = _TlpPduAlarmLoadOff04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 4)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff04.setStatus("current")
_TlpPduAlarmLoadOff05_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff05 = _TlpPduAlarmLoadOff05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 5)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff05.setStatus("current")
_TlpPduAlarmLoadOff06_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff06 = _TlpPduAlarmLoadOff06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 6)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff06.setStatus("current")
_TlpPduAlarmLoadOff07_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff07 = _TlpPduAlarmLoadOff07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 7)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff07.setStatus("current")
_TlpPduAlarmLoadOff08_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff08 = _TlpPduAlarmLoadOff08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 8)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff08.setStatus("current")
_TlpPduAlarmLoadOff09_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff09 = _TlpPduAlarmLoadOff09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 9)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff09.setStatus("current")
_TlpPduAlarmLoadOff10_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff10 = _TlpPduAlarmLoadOff10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 10)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff10.setStatus("current")
_TlpPduAlarmLoadOff11_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff11 = _TlpPduAlarmLoadOff11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 11)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff11.setStatus("current")
_TlpPduAlarmLoadOff12_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff12 = _TlpPduAlarmLoadOff12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 12)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff12.setStatus("current")
_TlpPduAlarmLoadOff13_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff13 = _TlpPduAlarmLoadOff13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 13)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff13.setStatus("current")
_TlpPduAlarmLoadOff14_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff14 = _TlpPduAlarmLoadOff14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 14)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff14.setStatus("current")
_TlpPduAlarmLoadOff15_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff15 = _TlpPduAlarmLoadOff15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 15)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff15.setStatus("current")
_TlpPduAlarmLoadOff16_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff16 = _TlpPduAlarmLoadOff16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 16)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff16.setStatus("current")
_TlpPduAlarmLoadOff17_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff17 = _TlpPduAlarmLoadOff17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 17)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff17.setStatus("current")
_TlpPduAlarmLoadOff18_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff18 = _TlpPduAlarmLoadOff18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 18)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff18.setStatus("current")
_TlpPduAlarmLoadOff19_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff19 = _TlpPduAlarmLoadOff19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 19)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff19.setStatus("current")
_TlpPduAlarmLoadOff20_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff20 = _TlpPduAlarmLoadOff20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 20)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff20.setStatus("current")
_TlpPduAlarmLoadOff21_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff21 = _TlpPduAlarmLoadOff21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 21)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff21.setStatus("current")
_TlpPduAlarmLoadOff22_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff22 = _TlpPduAlarmLoadOff22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 22)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff22.setStatus("current")
_TlpPduAlarmLoadOff23_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff23 = _TlpPduAlarmLoadOff23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 23)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff23.setStatus("current")
_TlpPduAlarmLoadOff24_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff24 = _TlpPduAlarmLoadOff24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 24)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff24.setStatus("current")
_TlpPduAlarmLoadOff25_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff25 = _TlpPduAlarmLoadOff25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 25)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff25.setStatus("current")
_TlpPduAlarmLoadOff26_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff26 = _TlpPduAlarmLoadOff26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 26)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff26.setStatus("current")
_TlpPduAlarmLoadOff27_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff27 = _TlpPduAlarmLoadOff27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 27)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff27.setStatus("current")
_TlpPduAlarmLoadOff28_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff28 = _TlpPduAlarmLoadOff28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 28)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff28.setStatus("current")
_TlpPduAlarmLoadOff29_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff29 = _TlpPduAlarmLoadOff29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 29)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff29.setStatus("current")
_TlpPduAlarmLoadOff30_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff30 = _TlpPduAlarmLoadOff30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 30)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff30.setStatus("current")
_TlpPduAlarmLoadOff31_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff31 = _TlpPduAlarmLoadOff31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 31)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff31.setStatus("current")
_TlpPduAlarmLoadOff32_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff32 = _TlpPduAlarmLoadOff32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 32)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff32.setStatus("current")
_TlpPduAlarmLoadOff33_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff33 = _TlpPduAlarmLoadOff33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 33)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff33.setStatus("current")
_TlpPduAlarmLoadOff34_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff34 = _TlpPduAlarmLoadOff34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 34)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff34.setStatus("current")
_TlpPduAlarmLoadOff35_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff35 = _TlpPduAlarmLoadOff35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 35)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff35.setStatus("current")
_TlpPduAlarmLoadOff36_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff36 = _TlpPduAlarmLoadOff36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 36)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff36.setStatus("current")
_TlpPduAlarmLoadOff37_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff37 = _TlpPduAlarmLoadOff37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 37)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff37.setStatus("current")
_TlpPduAlarmLoadOff38_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff38 = _TlpPduAlarmLoadOff38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 38)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff38.setStatus("current")
_TlpPduAlarmLoadOff39_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff39 = _TlpPduAlarmLoadOff39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 39)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff39.setStatus("current")
_TlpPduAlarmLoadOff40_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadOff40 = _TlpPduAlarmLoadOff40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 6, 40)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadOff40.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen = _TlpPduAlarmCircuitBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7)
)
_TlpPduAlarmCircuitBreakerOpen01_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen01 = _TlpPduAlarmCircuitBreakerOpen01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 1)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen01.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen02_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen02 = _TlpPduAlarmCircuitBreakerOpen02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 2)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen02.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen03_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen03 = _TlpPduAlarmCircuitBreakerOpen03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 3)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen03.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen04_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen04 = _TlpPduAlarmCircuitBreakerOpen04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 4)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen04.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen05_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen05 = _TlpPduAlarmCircuitBreakerOpen05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 5)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen05.setStatus("current")
_TlpPduAlarmCircuitBreakerOpen06_ObjectIdentity = ObjectIdentity
tlpPduAlarmCircuitBreakerOpen06 = _TlpPduAlarmCircuitBreakerOpen06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 7, 6)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCircuitBreakerOpen06.setStatus("current")
_TlpPduAlarmCurrentAboveThreshold_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold = _TlpPduAlarmCurrentAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8)
)
_TlpPduAlarmCurrentAboveThreshold1_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold1 = _TlpPduAlarmCurrentAboveThreshold1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8, 1)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentAboveThreshold1.setStatus("current")
_TlpPduAlarmCurrentAboveThreshold2_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold2 = _TlpPduAlarmCurrentAboveThreshold2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8, 2)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentAboveThreshold2.setStatus("current")
_TlpPduAlarmCurrentAboveThreshold3_ObjectIdentity = ObjectIdentity
tlpPduAlarmCurrentAboveThreshold3 = _TlpPduAlarmCurrentAboveThreshold3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 8, 3)
)
if mibBuilder.loadTexts:
    tlpPduAlarmCurrentAboveThreshold3.setStatus("current")
_TlpPduAlarmLoadsNotAllOn_ObjectIdentity = ObjectIdentity
tlpPduAlarmLoadsNotAllOn = _TlpPduAlarmLoadsNotAllOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 4, 9)
)
if mibBuilder.loadTexts:
    tlpPduAlarmLoadsNotAllOn.setStatus("current")
_TlpEnvAlarms_ObjectIdentity = ObjectIdentity
tlpEnvAlarms = _TlpEnvAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5)
)
_TlpEnvAlarmTemperatureBeyondLimits_ObjectIdentity = ObjectIdentity
tlpEnvAlarmTemperatureBeyondLimits = _TlpEnvAlarmTemperatureBeyondLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmTemperatureBeyondLimits.setStatus("current")
_TlpEnvAlarmHumidityBeyondLimits_ObjectIdentity = ObjectIdentity
tlpEnvAlarmHumidityBeyondLimits = _TlpEnvAlarmHumidityBeyondLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 2)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmHumidityBeyondLimits.setStatus("current")
_TlpEnvAlarmInputContact_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact = _TlpEnvAlarmInputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3)
)
_TlpEnvAlarmInputContact01_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact01 = _TlpEnvAlarmInputContact01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmInputContact01.setStatus("current")
_TlpEnvAlarmInputContact02_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact02 = _TlpEnvAlarmInputContact02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmInputContact02.setStatus("current")
_TlpEnvAlarmInputContact03_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact03 = _TlpEnvAlarmInputContact03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3, 3)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmInputContact03.setStatus("current")
_TlpEnvAlarmInputContact04_ObjectIdentity = ObjectIdentity
tlpEnvAlarmInputContact04 = _TlpEnvAlarmInputContact04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 3, 4)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmInputContact04.setStatus("current")
_TlpEnvAlarmOutputContact_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact = _TlpEnvAlarmOutputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4)
)
_TlpEnvAlarmOutputContact01_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact01 = _TlpEnvAlarmOutputContact01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4, 1)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmOutputContact01.setStatus("current")
_TlpEnvAlarmOutputContact02_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact02 = _TlpEnvAlarmOutputContact02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4, 2)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmOutputContact02.setStatus("current")
_TlpEnvAlarmOutputContact03_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact03 = _TlpEnvAlarmOutputContact03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4, 3)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmOutputContact03.setStatus("current")
_TlpEnvAlarmOutputContact04_ObjectIdentity = ObjectIdentity
tlpEnvAlarmOutputContact04 = _TlpEnvAlarmOutputContact04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 5, 4, 4)
)
if mibBuilder.loadTexts:
    tlpEnvAlarmOutputContact04.setStatus("current")
_TlpAtsAlarms_ObjectIdentity = ObjectIdentity
tlpAtsAlarms = _TlpAtsAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6)
)
_TlpAtsAlarmOutage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOutage = _TlpAtsAlarmOutage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 1)
)
_TlpAtsAlarmSource1Outage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource1Outage = _TlpAtsAlarmSource1Outage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource1Outage.setStatus("current")
_TlpAtsAlarmSource2Outage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource2Outage = _TlpAtsAlarmSource2Outage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource2Outage.setStatus("current")
_TlpAtsAlarmTemperature_ObjectIdentity = ObjectIdentity
tlpAtsAlarmTemperature = _TlpAtsAlarmTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 2)
)
_TlpAtsAlarmSystemTemperature_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSystemTemperature = _TlpAtsAlarmSystemTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSystemTemperature.setStatus("current")
_TlpAtsAlarmSource1Temperature_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource1Temperature = _TlpAtsAlarmSource1Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 2, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource1Temperature.setStatus("current")
_TlpAtsAlarmSource2Temperature_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource2Temperature = _TlpAtsAlarmSource2Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 2, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource2Temperature.setStatus("current")
_TlpAtsAlarmLoadLevelAboveThreshold_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadLevelAboveThreshold = _TlpAtsAlarmLoadLevelAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadLevelAboveThreshold.setStatus("current")
_TlpAtsAlarmInputBad_ObjectIdentity = ObjectIdentity
tlpAtsAlarmInputBad = _TlpAtsAlarmInputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 4)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmInputBad.setStatus("current")
_TlpAtsAlarmOutputBad_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOutputBad = _TlpAtsAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 5)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmOutputBad.setStatus("current")
_TlpAtsAlarmOutputOverload_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOutputOverload = _TlpAtsAlarmOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 6)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmOutputOverload.setStatus("current")
_TlpAtsAlarmOutputOff_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOutputOff = _TlpAtsAlarmOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 7)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmOutputOff.setStatus("current")
_TlpAtsAlarmLoadOff_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff = _TlpAtsAlarmLoadOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8)
)
_TlpAtsAlarmLoadOff01_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff01 = _TlpAtsAlarmLoadOff01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff01.setStatus("current")
_TlpAtsAlarmLoadOff02_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff02 = _TlpAtsAlarmLoadOff02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff02.setStatus("current")
_TlpAtsAlarmLoadOff03_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff03 = _TlpAtsAlarmLoadOff03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff03.setStatus("current")
_TlpAtsAlarmLoadOff04_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff04 = _TlpAtsAlarmLoadOff04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 4)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff04.setStatus("current")
_TlpAtsAlarmLoadOff05_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff05 = _TlpAtsAlarmLoadOff05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 5)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff05.setStatus("current")
_TlpAtsAlarmLoadOff06_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff06 = _TlpAtsAlarmLoadOff06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 6)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff06.setStatus("current")
_TlpAtsAlarmLoadOff07_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff07 = _TlpAtsAlarmLoadOff07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 7)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff07.setStatus("current")
_TlpAtsAlarmLoadOff08_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff08 = _TlpAtsAlarmLoadOff08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 8)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff08.setStatus("current")
_TlpAtsAlarmLoadOff09_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff09 = _TlpAtsAlarmLoadOff09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 9)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff09.setStatus("current")
_TlpAtsAlarmLoadOff10_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff10 = _TlpAtsAlarmLoadOff10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 10)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff10.setStatus("current")
_TlpAtsAlarmLoadOff11_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff11 = _TlpAtsAlarmLoadOff11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 11)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff11.setStatus("current")
_TlpAtsAlarmLoadOff12_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff12 = _TlpAtsAlarmLoadOff12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 12)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff12.setStatus("current")
_TlpAtsAlarmLoadOff13_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff13 = _TlpAtsAlarmLoadOff13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 13)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff13.setStatus("current")
_TlpAtsAlarmLoadOff14_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff14 = _TlpAtsAlarmLoadOff14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 14)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff14.setStatus("current")
_TlpAtsAlarmLoadOff15_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff15 = _TlpAtsAlarmLoadOff15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 15)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff15.setStatus("current")
_TlpAtsAlarmLoadOff16_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff16 = _TlpAtsAlarmLoadOff16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 16)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff16.setStatus("current")
_TlpAtsAlarmLoadOff17_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff17 = _TlpAtsAlarmLoadOff17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 17)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff17.setStatus("current")
_TlpAtsAlarmLoadOff18_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff18 = _TlpAtsAlarmLoadOff18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 18)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff18.setStatus("current")
_TlpAtsAlarmLoadOff19_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff19 = _TlpAtsAlarmLoadOff19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 19)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff19.setStatus("current")
_TlpAtsAlarmLoadOff20_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff20 = _TlpAtsAlarmLoadOff20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 20)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff20.setStatus("current")
_TlpAtsAlarmLoadOff21_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff21 = _TlpAtsAlarmLoadOff21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 21)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff21.setStatus("current")
_TlpAtsAlarmLoadOff22_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff22 = _TlpAtsAlarmLoadOff22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 22)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff22.setStatus("current")
_TlpAtsAlarmLoadOff23_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff23 = _TlpAtsAlarmLoadOff23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 23)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff23.setStatus("current")
_TlpAtsAlarmLoadOff24_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff24 = _TlpAtsAlarmLoadOff24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 24)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff24.setStatus("current")
_TlpAtsAlarmLoadOff25_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff25 = _TlpAtsAlarmLoadOff25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 25)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff25.setStatus("current")
_TlpAtsAlarmLoadOff26_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff26 = _TlpAtsAlarmLoadOff26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 26)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff26.setStatus("current")
_TlpAtsAlarmLoadOff27_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff27 = _TlpAtsAlarmLoadOff27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 27)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff27.setStatus("current")
_TlpAtsAlarmLoadOff28_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff28 = _TlpAtsAlarmLoadOff28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 28)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff28.setStatus("current")
_TlpAtsAlarmLoadOff29_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff29 = _TlpAtsAlarmLoadOff29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 29)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff29.setStatus("current")
_TlpAtsAlarmLoadOff30_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff30 = _TlpAtsAlarmLoadOff30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 30)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff30.setStatus("current")
_TlpAtsAlarmLoadOff31_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff31 = _TlpAtsAlarmLoadOff31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 31)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff31.setStatus("current")
_TlpAtsAlarmLoadOff32_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff32 = _TlpAtsAlarmLoadOff32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 32)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff32.setStatus("current")
_TlpAtsAlarmLoadOff33_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff33 = _TlpAtsAlarmLoadOff33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 33)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff33.setStatus("current")
_TlpAtsAlarmLoadOff34_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff34 = _TlpAtsAlarmLoadOff34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 34)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff34.setStatus("current")
_TlpAtsAlarmLoadOff35_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff35 = _TlpAtsAlarmLoadOff35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 35)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff35.setStatus("current")
_TlpAtsAlarmLoadOff36_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff36 = _TlpAtsAlarmLoadOff36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 36)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff36.setStatus("current")
_TlpAtsAlarmLoadOff37_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff37 = _TlpAtsAlarmLoadOff37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 37)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff37.setStatus("current")
_TlpAtsAlarmLoadOff38_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff38 = _TlpAtsAlarmLoadOff38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 38)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff38.setStatus("current")
_TlpAtsAlarmLoadOff39_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff39 = _TlpAtsAlarmLoadOff39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 39)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff39.setStatus("current")
_TlpAtsAlarmLoadOff40_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadOff40 = _TlpAtsAlarmLoadOff40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 8, 40)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadOff40.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen = _TlpAtsAlarmCircuitBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9)
)
_TlpAtsAlarmCircuitBreakerOpen01_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen01 = _TlpAtsAlarmCircuitBreakerOpen01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen01.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen02_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen02 = _TlpAtsAlarmCircuitBreakerOpen02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen02.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen03_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen03 = _TlpAtsAlarmCircuitBreakerOpen03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen03.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen04_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen04 = _TlpAtsAlarmCircuitBreakerOpen04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 4)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen04.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen05_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen05 = _TlpAtsAlarmCircuitBreakerOpen05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 5)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen05.setStatus("current")
_TlpAtsAlarmCircuitBreakerOpen06_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCircuitBreakerOpen06 = _TlpAtsAlarmCircuitBreakerOpen06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 9, 6)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCircuitBreakerOpen06.setStatus("current")
_TlpAtsAlarmCurrentAboveThreshold_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThreshold = _TlpAtsAlarmCurrentAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10)
)
_TlpAtsAlarmCurrentAboveThresholdA1_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThresholdA1 = _TlpAtsAlarmCurrentAboveThresholdA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThresholdA1.setStatus("current")
_TlpAtsAlarmCurrentAboveThresholdA2_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThresholdA2 = _TlpAtsAlarmCurrentAboveThresholdA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThresholdA2.setStatus("current")
_TlpAtsAlarmCurrentAboveThresholdA3_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThresholdA3 = _TlpAtsAlarmCurrentAboveThresholdA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThresholdA3.setStatus("current")
_TlpAtsAlarmCurrentAboveThresholdB1_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThresholdB1 = _TlpAtsAlarmCurrentAboveThresholdB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 4)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThresholdB1.setStatus("current")
_TlpAtsAlarmCurrentAboveThresholdB2_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThresholdB2 = _TlpAtsAlarmCurrentAboveThresholdB2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 5)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThresholdB2.setStatus("current")
_TlpAtsAlarmCurrentAboveThresholdB3_ObjectIdentity = ObjectIdentity
tlpAtsAlarmCurrentAboveThresholdB3 = _TlpAtsAlarmCurrentAboveThresholdB3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 10, 6)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmCurrentAboveThresholdB3.setStatus("current")
_TlpAtsAlarmLoadsNotAllOn_ObjectIdentity = ObjectIdentity
tlpAtsAlarmLoadsNotAllOn = _TlpAtsAlarmLoadsNotAllOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 11)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmLoadsNotAllOn.setStatus("current")
_TlpAtsAlarmGeneralFault_ObjectIdentity = ObjectIdentity
tlpAtsAlarmGeneralFault = _TlpAtsAlarmGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 12)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmGeneralFault.setStatus("current")
_TlpAtsAlarmVoltage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmVoltage = _TlpAtsAlarmVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 13)
)
_TlpAtsAlarmOverVoltage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmOverVoltage = _TlpAtsAlarmOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 13, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmOverVoltage.setStatus("current")
_TlpAtsAlarmSource1OverVoltage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource1OverVoltage = _TlpAtsAlarmSource1OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 13, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource1OverVoltage.setStatus("current")
_TlpAtsAlarmSource2OverVoltage_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource2OverVoltage = _TlpAtsAlarmSource2OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 13, 3)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource2OverVoltage.setStatus("current")
_TlpAtsAlarmFrequency_ObjectIdentity = ObjectIdentity
tlpAtsAlarmFrequency = _TlpAtsAlarmFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 14)
)
_TlpAtsAlarmSource1InvalidFrequency_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource1InvalidFrequency = _TlpAtsAlarmSource1InvalidFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 14, 1)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource1InvalidFrequency.setStatus("current")
_TlpAtsAlarmSource2InvalidFrequency_ObjectIdentity = ObjectIdentity
tlpAtsAlarmSource2InvalidFrequency = _TlpAtsAlarmSource2InvalidFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 6, 14, 2)
)
if mibBuilder.loadTexts:
    tlpAtsAlarmSource2InvalidFrequency.setStatus("current")
_TlpCoolingAlarms_ObjectIdentity = ObjectIdentity
tlpCoolingAlarms = _TlpCoolingAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7)
)
_TlpCoolingAlarmSupplyAirSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSupplyAirSensorFault = _TlpCoolingAlarmSupplyAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 1)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSupplyAirSensorFault.setStatus("current")
_TlpCoolingAlarmReturnAirSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmReturnAirSensorFault = _TlpCoolingAlarmReturnAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 2)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmReturnAirSensorFault.setStatus("current")
_TlpCoolingAlarmCondenserInletAirSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondenserInletAirSensorFault = _TlpCoolingAlarmCondenserInletAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 3)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondenserInletAirSensorFault.setStatus("current")
_TlpCoolingAlarmCondenserOutletAirSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondenserOutletAirSensorFault = _TlpCoolingAlarmCondenserOutletAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 4)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondenserOutletAirSensorFault.setStatus("current")
_TlpCoolingAlarmSuctionTemperatureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionTemperatureSensorFault = _TlpCoolingAlarmSuctionTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 5)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionTemperatureSensorFault.setStatus("current")
_TlpCoolingAlarmEvaporatorTemperatureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmEvaporatorTemperatureSensorFault = _TlpCoolingAlarmEvaporatorTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 6)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmEvaporatorTemperatureSensorFault.setStatus("current")
_TlpCoolingAlarmAirFilterClogged_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmAirFilterClogged = _TlpCoolingAlarmAirFilterClogged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 7)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmAirFilterClogged.setStatus("current")
_TlpCoolingAlarmAirFilterRunHoursViolation_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmAirFilterRunHoursViolation = _TlpCoolingAlarmAirFilterRunHoursViolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 8)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmAirFilterRunHoursViolation.setStatus("current")
_TlpCoolingAlarmSuctionPressureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionPressureSensorFault = _TlpCoolingAlarmSuctionPressureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 9)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionPressureSensorFault.setStatus("current")
_TlpCoolingAlarmInverterCommunicationsFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmInverterCommunicationsFault = _TlpCoolingAlarmInverterCommunicationsFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 10)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmInverterCommunicationsFault.setStatus("current")
_TlpCoolingAlarmRemoteShutdownViaInputContact_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmRemoteShutdownViaInputContact = _TlpCoolingAlarmRemoteShutdownViaInputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 11)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmRemoteShutdownViaInputContact.setStatus("current")
_TlpCoolingAlarmCondensatePumpFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondensatePumpFault = _TlpCoolingAlarmCondensatePumpFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 12)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondensatePumpFault.setStatus("current")
_TlpCoolingAlarmLowRefrigerantStartupFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmLowRefrigerantStartupFault = _TlpCoolingAlarmLowRefrigerantStartupFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 13)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmLowRefrigerantStartupFault.setStatus("current")
_TlpCoolingAlarmCondenserFanFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondenserFanFault = _TlpCoolingAlarmCondenserFanFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 14)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondenserFanFault.setStatus("current")
_TlpCoolingAlarmCondenserFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCondenserFailure = _TlpCoolingAlarmCondenserFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 15)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCondenserFailure.setStatus("current")
_TlpCoolingAlarmEvaporatorCoolingFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmEvaporatorCoolingFailure = _TlpCoolingAlarmEvaporatorCoolingFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 16)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmEvaporatorCoolingFailure.setStatus("current")
_TlpCoolingAlarmReturnAirTempHigh_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmReturnAirTempHigh = _TlpCoolingAlarmReturnAirTempHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 17)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmReturnAirTempHigh.setStatus("current")
_TlpCoolingAlarmSupplyAirTempHigh_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSupplyAirTempHigh = _TlpCoolingAlarmSupplyAirTempHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 18)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSupplyAirTempHigh.setStatus("current")
_TlpCoolingAlarmEvaporatorFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmEvaporatorFailure = _TlpCoolingAlarmEvaporatorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 19)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmEvaporatorFailure.setStatus("current")
_TlpCoolingAlarmEvaporatorFreezeUp_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmEvaporatorFreezeUp = _TlpCoolingAlarmEvaporatorFreezeUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 20)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmEvaporatorFreezeUp.setStatus("current")
_TlpCoolingAlarmDischargePressureHigh_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmDischargePressureHigh = _TlpCoolingAlarmDischargePressureHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 21)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmDischargePressureHigh.setStatus("current")
_TlpCoolingAlarmPressureGaugeFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmPressureGaugeFailure = _TlpCoolingAlarmPressureGaugeFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 22)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmPressureGaugeFailure.setStatus("current")
_TlpCoolingAlarmDischargePressurePersistentHigh_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmDischargePressurePersistentHigh = _TlpCoolingAlarmDischargePressurePersistentHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 23)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmDischargePressurePersistentHigh.setStatus("current")
_TlpCoolingAlarmSuctionPressureLowStartFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionPressureLowStartFailure = _TlpCoolingAlarmSuctionPressureLowStartFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 24)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionPressureLowStartFailure.setStatus("current")
_TlpCoolingAlarmSuctionPressureLow_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionPressureLow = _TlpCoolingAlarmSuctionPressureLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 25)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionPressureLow.setStatus("current")
_TlpCoolingAlarmSuctionPressurePersistentLow_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmSuctionPressurePersistentLow = _TlpCoolingAlarmSuctionPressurePersistentLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 26)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmSuctionPressurePersistentLow.setStatus("current")
_TlpCoolingAlarmStartupLinePressureImbalance_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmStartupLinePressureImbalance = _TlpCoolingAlarmStartupLinePressureImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 27)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmStartupLinePressureImbalance.setStatus("current")
_TlpCoolingAlarmCompressorFailure_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCompressorFailure = _TlpCoolingAlarmCompressorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 28)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCompressorFailure.setStatus("current")
_TlpCoolingAlarmCurrentLimit_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmCurrentLimit = _TlpCoolingAlarmCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 29)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmCurrentLimit.setStatus("current")
_TlpCoolingAlarmWaterLeak_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmWaterLeak = _TlpCoolingAlarmWaterLeak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 30)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmWaterLeak.setStatus("current")
_TlpCoolingAlarmFanUnderCurrent_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmFanUnderCurrent = _TlpCoolingAlarmFanUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 31)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmFanUnderCurrent.setStatus("current")
_TlpCoolingAlarmFanOverCurrent_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmFanOverCurrent = _TlpCoolingAlarmFanOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 32)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmFanOverCurrent.setStatus("current")
_TlpCoolingAlarmDischargePressureSensorFault_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmDischargePressureSensorFault = _TlpCoolingAlarmDischargePressureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 33)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmDischargePressureSensorFault.setStatus("current")
_TlpCoolingAlarmWaterFull_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmWaterFull = _TlpCoolingAlarmWaterFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 34)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmWaterFull.setStatus("current")
_TlpCoolingAlarmAutoCoolingOn_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmAutoCoolingOn = _TlpCoolingAlarmAutoCoolingOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 35)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmAutoCoolingOn.setStatus("current")
_TlpCoolingAlarmPowerButtonPressed_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmPowerButtonPressed = _TlpCoolingAlarmPowerButtonPressed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 36)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmPowerButtonPressed.setStatus("current")
_TlpCoolingAlarmDisconnectedFromDevice_ObjectIdentity = ObjectIdentity
tlpCoolingAlarmDisconnectedFromDevice = _TlpCoolingAlarmDisconnectedFromDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 7, 37)
)
if mibBuilder.loadTexts:
    tlpCoolingAlarmDisconnectedFromDevice.setStatus("current")
_TlpKvmAlarms_ObjectIdentity = ObjectIdentity
tlpKvmAlarms = _TlpKvmAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 8)
)
_TlpRackTrackAlarms_ObjectIdentity = ObjectIdentity
tlpRackTrackAlarms = _TlpRackTrackAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 9)
)
_TlpSwitchAlarms_ObjectIdentity = ObjectIdentity
tlpSwitchAlarms = _TlpSwitchAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 3, 10)
)
_TlpAlarmControl_ObjectIdentity = ObjectIdentity
tlpAlarmControl = _TlpAlarmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4)
)
_TlpAlarmControlTable_Object = MibTable
tlpAlarmControlTable = _TlpAlarmControlTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tlpAlarmControlTable.setStatus("current")
_TlpAlarmControlEntry_Object = MibTableRow
tlpAlarmControlEntry = _TlpAlarmControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1)
)
tlpAlarmControlEntry.setIndexNames(
    (0, "TRIPPLITE-PRODUCTS", "tlpDeviceIndex"),
    (0, "TRIPPLITE-PRODUCTS", "tlpAlarmControlIndex"),
)
if mibBuilder.loadTexts:
    tlpAlarmControlEntry.setStatus("current")
_TlpAlarmControlIndex_Type = Unsigned32
_TlpAlarmControlIndex_Object = MibTableColumn
tlpAlarmControlIndex = _TlpAlarmControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1, 1),
    _TlpAlarmControlIndex_Type()
)
tlpAlarmControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmControlIndex.setStatus("current")
_TlpAlarmControlDescr_Type = ObjectIdentifier
_TlpAlarmControlDescr_Object = MibTableColumn
tlpAlarmControlDescr = _TlpAlarmControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1, 2),
    _TlpAlarmControlDescr_Type()
)
tlpAlarmControlDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmControlDescr.setStatus("current")
_TlpAlarmControlDetail_Type = DisplayString
_TlpAlarmControlDetail_Object = MibTableColumn
tlpAlarmControlDetail = _TlpAlarmControlDetail_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1, 3),
    _TlpAlarmControlDetail_Type()
)
tlpAlarmControlDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlpAlarmControlDetail.setStatus("current")


class _TlpAlarmControlSeverity_Type(Integer32):
    """Custom type tlpAlarmControlSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("info", 3),
          ("warning", 2))
    )


_TlpAlarmControlSeverity_Type.__name__ = "Integer32"
_TlpAlarmControlSeverity_Object = MibTableColumn
tlpAlarmControlSeverity = _TlpAlarmControlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 3, 4, 1, 1, 4),
    _TlpAlarmControlSeverity_Type()
)
tlpAlarmControlSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlpAlarmControlSeverity.setStatus("current")
_TlpNotify_ObjectIdentity = ObjectIdentity
tlpNotify = _TlpNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4)
)
_TlpNotifications_ObjectIdentity = ObjectIdentity
tlpNotifications = _TlpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1)
)

# Managed Objects groups


# Notification objects

tlpNotificationsAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 1)
)
tlpNotificationsAlarmEntryAdded.setObjects(
      *(("TRIPPLITE-PRODUCTS", "tlpAlarmId"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmDescr"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTime"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTableRowRef"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmDetail"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmType"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAlarmEntryAdded.setStatus(
        "current"
    )

tlpNotificationsAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 2)
)
tlpNotificationsAlarmEntryRemoved.setObjects(
      *(("TRIPPLITE-PRODUCTS", "tlpAlarmId"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmDescr"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTime"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTableRef"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmTableRowRef"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmDetail"),
        ("TRIPPLITE-PRODUCTS", "tlpAlarmType"))
)
if mibBuilder.loadTexts:
    tlpNotificationsAlarmEntryRemoved.setStatus(
        "current"
    )

tlpNotifySystemStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    tlpNotifySystemStartup.setStatus(
        "current"
    )

tlpNotifySystemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    tlpNotifySystemShutdown.setStatus(
        "current"
    )

tlpNotifySystemUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    tlpNotifySystemUpdate.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRIPPLITE-PRODUCTS",
    **{"tlpProducts": tlpProducts,
       "tlpHardware": tlpHardware,
       "tlpDevice": tlpDevice,
       "tlpDeviceNumDevices": tlpDeviceNumDevices,
       "tlpDeviceTable": tlpDeviceTable,
       "tlpDeviceEntry": tlpDeviceEntry,
       "tlpDeviceIndex": tlpDeviceIndex,
       "tlpDeviceRowStatus": tlpDeviceRowStatus,
       "tlpDeviceType": tlpDeviceType,
       "tlpDeviceManufacturer": tlpDeviceManufacturer,
       "tlpDeviceModel": tlpDeviceModel,
       "tlpDeviceName": tlpDeviceName,
       "tlpDeviceID": tlpDeviceID,
       "tlpDeviceLocation": tlpDeviceLocation,
       "tlpDeviceRegion": tlpDeviceRegion,
       "tlpDeviceStatus": tlpDeviceStatus,
       "tlpDeviceDetail": tlpDeviceDetail,
       "tlpDeviceIdentTable": tlpDeviceIdentTable,
       "tlpDeviceIdentEntry": tlpDeviceIdentEntry,
       "tlpDeviceIdentProtocol": tlpDeviceIdentProtocol,
       "tlpDeviceIdentCommPortType": tlpDeviceIdentCommPortType,
       "tlpDeviceIdentCommPortName": tlpDeviceIdentCommPortName,
       "tlpDeviceIdentFirmwareVersion": tlpDeviceIdentFirmwareVersion,
       "tlpDeviceIdentSerialNum": tlpDeviceIdentSerialNum,
       "tlpDeviceIdentDateInstalled": tlpDeviceIdentDateInstalled,
       "tlpDeviceIdentHardwareVersion": tlpDeviceIdentHardwareVersion,
       "tlpDeviceIdentCurrentUptime": tlpDeviceIdentCurrentUptime,
       "tlpDeviceIdentTotalUptime": tlpDeviceIdentTotalUptime,
       "tlpDeviceTypes": tlpDeviceTypes,
       "tlpUps": tlpUps,
       "tlpUpsIdent": tlpUpsIdent,
       "tlpUpsIdentNumUps": tlpUpsIdentNumUps,
       "tlpUpsIdentTable": tlpUpsIdentTable,
       "tlpUpsIdentEntry": tlpUpsIdentEntry,
       "tlpUpsIdentNumInputs": tlpUpsIdentNumInputs,
       "tlpUpsIdentNumOutputs": tlpUpsIdentNumOutputs,
       "tlpUpsIdentNumBypass": tlpUpsIdentNumBypass,
       "tlpUpsIdentNumPhases": tlpUpsIdentNumPhases,
       "tlpUpsIdentNumOutlets": tlpUpsIdentNumOutlets,
       "tlpUpsIdentNumOutletGroups": tlpUpsIdentNumOutletGroups,
       "tlpUpsIdentNumBatteryPacks": tlpUpsIdentNumBatteryPacks,
       "tlpUpsSupportsTable": tlpUpsSupportsTable,
       "tlpUpsSupportsEntry": tlpUpsSupportsEntry,
       "tlpUpsSupportsEnergywise": tlpUpsSupportsEnergywise,
       "tlpUpsSupportsRampShed": tlpUpsSupportsRampShed,
       "tlpUpsSupportsOutletGroup": tlpUpsSupportsOutletGroup,
       "tlpUpsSupportsOutletCurrentPower": tlpUpsSupportsOutletCurrentPower,
       "tlpUpsSupportsOutletVoltage": tlpUpsSupportsOutletVoltage,
       "tlpUpsDevice": tlpUpsDevice,
       "tlpUpsDeviceTable": tlpUpsDeviceTable,
       "tlpUpsDeviceEntry": tlpUpsDeviceEntry,
       "tlpUpsDeviceMainLoadState": tlpUpsDeviceMainLoadState,
       "tlpUpsDeviceMainLoadControllable": tlpUpsDeviceMainLoadControllable,
       "tlpUpsDeviceMainLoadCommand": tlpUpsDeviceMainLoadCommand,
       "tlpUpsDevicePowerOnDelay": tlpUpsDevicePowerOnDelay,
       "tlpUpsDeviceTestDate": tlpUpsDeviceTestDate,
       "tlpUpsDeviceTestResultsStatus": tlpUpsDeviceTestResultsStatus,
       "tlpUpsDeviceTemperatureC": tlpUpsDeviceTemperatureC,
       "tlpUpsDeviceTemperatureF": tlpUpsDeviceTemperatureF,
       "tlpUpsDetail": tlpUpsDetail,
       "tlpUpsBattery": tlpUpsBattery,
       "tlpUpsBatterySummaryTable": tlpUpsBatterySummaryTable,
       "tlpUpsBatterySummaryEntry": tlpUpsBatterySummaryEntry,
       "tlpUpsBatteryStatus": tlpUpsBatteryStatus,
       "tlpUpsSecondsOnBattery": tlpUpsSecondsOnBattery,
       "tlpUpsEstimatedMinutesRemaining": tlpUpsEstimatedMinutesRemaining,
       "tlpUpsEstimatedChargeRemaining": tlpUpsEstimatedChargeRemaining,
       "tlpUpsBatteryRunTimeRemaining": tlpUpsBatteryRunTimeRemaining,
       "tlpUpsBatteryDetailTable": tlpUpsBatteryDetailTable,
       "tlpUpsBatteryDetailEntry": tlpUpsBatteryDetailEntry,
       "tlpUpsBatteryDetailVoltage": tlpUpsBatteryDetailVoltage,
       "tlpUpsBatteryDetailCurrent": tlpUpsBatteryDetailCurrent,
       "tlpUpsBatteryDetailCapacity": tlpUpsBatteryDetailCapacity,
       "tlpUpsBatteryDetailCharge": tlpUpsBatteryDetailCharge,
       "tlpUpsBatteryDetailChargerStatus": tlpUpsBatteryDetailChargerStatus,
       "tlpUpsBatteryPackIdentTable": tlpUpsBatteryPackIdentTable,
       "tlpUpsBatteryPackIdentEntry": tlpUpsBatteryPackIdentEntry,
       "tlpUpsBatteryPackIdentIndex": tlpUpsBatteryPackIdentIndex,
       "tlpUpsBatteryPackIdentManufacturer": tlpUpsBatteryPackIdentManufacturer,
       "tlpUpsBatteryPackIdentModel": tlpUpsBatteryPackIdentModel,
       "tlpUpsBatteryPackIdentSerialNum": tlpUpsBatteryPackIdentSerialNum,
       "tlpUpsBatteryPackIdentFirmware": tlpUpsBatteryPackIdentFirmware,
       "tlpUpsBatteryPackIdentSKU": tlpUpsBatteryPackIdentSKU,
       "tlpUpsBatteryPackConfigTable": tlpUpsBatteryPackConfigTable,
       "tlpUpsBatteryPackConfigEntry": tlpUpsBatteryPackConfigEntry,
       "tlpUpsBatteryPackConfigChemistry": tlpUpsBatteryPackConfigChemistry,
       "tlpUpsBatteryPackConfigStyle": tlpUpsBatteryPackConfigStyle,
       "tlpUpsBatteryPackConfigLocation": tlpUpsBatteryPackConfigLocation,
       "tlpUpsBatteryPackConfigStrings": tlpUpsBatteryPackConfigStrings,
       "tlpUpsBatteryPackConfigBatteriesPerString": tlpUpsBatteryPackConfigBatteriesPerString,
       "tlpUpsBatteryPackConfigCellsPerBattery": tlpUpsBatteryPackConfigCellsPerBattery,
       "tlpUpsBatteryPackConfigNumBatteries": tlpUpsBatteryPackConfigNumBatteries,
       "tlpUpsBatteryPackConfigCapacityUnits": tlpUpsBatteryPackConfigCapacityUnits,
       "tlpUpsBatteryPackConfigDesignCapacity": tlpUpsBatteryPackConfigDesignCapacity,
       "tlpUpsBatteryPackConfigCellCapacity": tlpUpsBatteryPackConfigCellCapacity,
       "tlpUpsBatteryPackConfigMinCellVoltage": tlpUpsBatteryPackConfigMinCellVoltage,
       "tlpUpsBatteryPackConfigMaxCellVoltage": tlpUpsBatteryPackConfigMaxCellVoltage,
       "tlpUpsBatteryPackDetailTable": tlpUpsBatteryPackDetailTable,
       "tlpUpsBatteryPackDetailEntry": tlpUpsBatteryPackDetailEntry,
       "tlpUpsBatteryPackDetailCondition": tlpUpsBatteryPackDetailCondition,
       "tlpUpsBatteryPackDetailTemperatureC": tlpUpsBatteryPackDetailTemperatureC,
       "tlpUpsBatteryPackDetailTemperatureF": tlpUpsBatteryPackDetailTemperatureF,
       "tlpUpsBatteryPackDetailAge": tlpUpsBatteryPackDetailAge,
       "tlpUpsBatteryPackDetailLastReplaceDate": tlpUpsBatteryPackDetailLastReplaceDate,
       "tlpUpsBatteryPackDetailNextReplaceDate": tlpUpsBatteryPackDetailNextReplaceDate,
       "tlpUpsBatteryPackDetailCycleCount": tlpUpsBatteryPackDetailCycleCount,
       "tlpUpsInput": tlpUpsInput,
       "tlpUpsInputTable": tlpUpsInputTable,
       "tlpUpsInputEntry": tlpUpsInputEntry,
       "tlpUpsInputLineBads": tlpUpsInputLineBads,
       "tlpUpsInputNominalVoltage": tlpUpsInputNominalVoltage,
       "tlpUpsInputNominalFrequency": tlpUpsInputNominalFrequency,
       "tlpUpsInputLowTransferVoltage": tlpUpsInputLowTransferVoltage,
       "tlpUpsInputLowTransferVoltageLowerBound": tlpUpsInputLowTransferVoltageLowerBound,
       "tlpUpsInputLowTransferVoltageUpperBound": tlpUpsInputLowTransferVoltageUpperBound,
       "tlpUpsInputHighTransferVoltage": tlpUpsInputHighTransferVoltage,
       "tlpUpsInputHighTransferVoltageLowerBound": tlpUpsInputHighTransferVoltageLowerBound,
       "tlpUpsInputHighTransferVoltageUpperBound": tlpUpsInputHighTransferVoltageUpperBound,
       "tlpUpsInputPhaseTable": tlpUpsInputPhaseTable,
       "tlpUpsInputPhaseEntry": tlpUpsInputPhaseEntry,
       "tlpUpsInputPhaseIndex": tlpUpsInputPhaseIndex,
       "tlpUpsInputPhaseFrequency": tlpUpsInputPhaseFrequency,
       "tlpUpsInputPhaseVoltage": tlpUpsInputPhaseVoltage,
       "tlpUpsInputPhaseVoltageMin": tlpUpsInputPhaseVoltageMin,
       "tlpUpsInputPhaseVoltageMax": tlpUpsInputPhaseVoltageMax,
       "tlpUpsInputPhaseCurrent": tlpUpsInputPhaseCurrent,
       "tlpUpsInputPhasePower": tlpUpsInputPhasePower,
       "tlpUpsOutput": tlpUpsOutput,
       "tlpUpsOutputTable": tlpUpsOutputTable,
       "tlpUpsOutputEntry": tlpUpsOutputEntry,
       "tlpUpsOutputSource": tlpUpsOutputSource,
       "tlpUpsOutputNominalVoltage": tlpUpsOutputNominalVoltage,
       "tlpUpsOutputFrequency": tlpUpsOutputFrequency,
       "tlpUpsOutputLineTable": tlpUpsOutputLineTable,
       "tlpUpsOutputLineEntry": tlpUpsOutputLineEntry,
       "tlpUpsOutputLineIndex": tlpUpsOutputLineIndex,
       "tlpUpsOutputLineVoltage": tlpUpsOutputLineVoltage,
       "tlpUpsOutputLineCurrent": tlpUpsOutputLineCurrent,
       "tlpUpsOutputLinePower": tlpUpsOutputLinePower,
       "tlpUpsOutputLinePercentLoad": tlpUpsOutputLinePercentLoad,
       "tlpUpsOutputLineFrequency": tlpUpsOutputLineFrequency,
       "tlpUpsBypass": tlpUpsBypass,
       "tlpUpsBypassTable": tlpUpsBypassTable,
       "tlpUpsBypassEntry": tlpUpsBypassEntry,
       "tlpUpsBypassFrequency": tlpUpsBypassFrequency,
       "tlpUpsBypassLineTable": tlpUpsBypassLineTable,
       "tlpUpsBypassLineEntry": tlpUpsBypassLineEntry,
       "tlpUpsBypassLineIndex": tlpUpsBypassLineIndex,
       "tlpUpsBypassLineVoltage": tlpUpsBypassLineVoltage,
       "tlpUpsBypassLineCurrent": tlpUpsBypassLineCurrent,
       "tlpUpsBypassLinePower": tlpUpsBypassLinePower,
       "tlpUpsOutlet": tlpUpsOutlet,
       "tlpUpsOutletTable": tlpUpsOutletTable,
       "tlpUpsOutletEntry": tlpUpsOutletEntry,
       "tlpUpsOutletIndex": tlpUpsOutletIndex,
       "tlpUpsOutletName": tlpUpsOutletName,
       "tlpUpsOutletDescription": tlpUpsOutletDescription,
       "tlpUpsOutletState": tlpUpsOutletState,
       "tlpUpsOutletControllable": tlpUpsOutletControllable,
       "tlpUpsOutletCommand": tlpUpsOutletCommand,
       "tlpUpsOutletVoltage": tlpUpsOutletVoltage,
       "tlpUpsOutletCurrent": tlpUpsOutletCurrent,
       "tlpUpsOutletPower": tlpUpsOutletPower,
       "tlpUpsOutletRampAction": tlpUpsOutletRampAction,
       "tlpUpsOutletRampDelay": tlpUpsOutletRampDelay,
       "tlpUpsOutletShedAction": tlpUpsOutletShedAction,
       "tlpUpsOutletShedDelay": tlpUpsOutletShedDelay,
       "tlpUpsOutletGroup": tlpUpsOutletGroup,
       "tlpUpsOutletGroupTable": tlpUpsOutletGroupTable,
       "tlpUpsOutletGroupEntry": tlpUpsOutletGroupEntry,
       "tlpUpsOutletGroupIndex": tlpUpsOutletGroupIndex,
       "tlpUpsOutletGroupRowStatus": tlpUpsOutletGroupRowStatus,
       "tlpUpsOutletGroupName": tlpUpsOutletGroupName,
       "tlpUpsOutletGroupDescription": tlpUpsOutletGroupDescription,
       "tlpUpsOutletGroupState": tlpUpsOutletGroupState,
       "tlpUpsOutletGroupCommand": tlpUpsOutletGroupCommand,
       "tlpUpsWatchdog": tlpUpsWatchdog,
       "tlpUpsWatchdogTable": tlpUpsWatchdogTable,
       "tlpUpsWatchdogEntry": tlpUpsWatchdogEntry,
       "tlpUpsWatchdogSupported": tlpUpsWatchdogSupported,
       "tlpUpsWatchdogSecsBeforeReboot": tlpUpsWatchdogSecsBeforeReboot,
       "tlpUpsControl": tlpUpsControl,
       "tlpUpsControlTable": tlpUpsControlTable,
       "tlpUpsControlEntry": tlpUpsControlEntry,
       "tlpUpsControlSelfTest": tlpUpsControlSelfTest,
       "tlpUpsControlRamp": tlpUpsControlRamp,
       "tlpUpsControlShed": tlpUpsControlShed,
       "tlpUpsControlUpsOn": tlpUpsControlUpsOn,
       "tlpUpsControlUpsOff": tlpUpsControlUpsOff,
       "tlpUpsControlUpsReboot": tlpUpsControlUpsReboot,
       "tlpUpsControlBypass": tlpUpsControlBypass,
       "tlpUpsConfig": tlpUpsConfig,
       "tlpUpsConfigTable": tlpUpsConfigTable,
       "tlpUpsConfigEntry": tlpUpsConfigEntry,
       "tlpUpsConfigInputVoltage": tlpUpsConfigInputVoltage,
       "tlpUpsConfigInputFrequency": tlpUpsConfigInputFrequency,
       "tlpUpsConfigOutputVoltage": tlpUpsConfigOutputVoltage,
       "tlpUpsConfigOutputFrequency": tlpUpsConfigOutputFrequency,
       "tlpUpsConfigAudibleStatus": tlpUpsConfigAudibleStatus,
       "tlpUpsConfigAutoBatteryTest": tlpUpsConfigAutoBatteryTest,
       "tlpUpsConfigAutoRestartAfterShutdown": tlpUpsConfigAutoRestartAfterShutdown,
       "tlpUpsConfigAutoRampOnTransition": tlpUpsConfigAutoRampOnTransition,
       "tlpUpsConfigAutoShedOnTransition": tlpUpsConfigAutoShedOnTransition,
       "tlpUpsConfigBypassLowerLimitPercent": tlpUpsConfigBypassLowerLimitPercent,
       "tlpUpsConfigBypassUpperLimitPercent": tlpUpsConfigBypassUpperLimitPercent,
       "tlpUpsConfigBypassLowerLimitVoltage": tlpUpsConfigBypassLowerLimitVoltage,
       "tlpUpsConfigBypassUpperLimitVoltage": tlpUpsConfigBypassUpperLimitVoltage,
       "tlpUpsConfigColdStart": tlpUpsConfigColdStart,
       "tlpUpsConfigEconomicMode": tlpUpsConfigEconomicMode,
       "tlpUpsConfigFaultAction": tlpUpsConfigFaultAction,
       "tlpUpsConfigOffMode": tlpUpsConfigOffMode,
       "tlpUpsConfigLineSensitivity": tlpUpsConfigLineSensitivity,
       "tlpUpsConfigAutoRestartTable": tlpUpsConfigAutoRestartTable,
       "tlpUpsConfigAutoRestartEntry": tlpUpsConfigAutoRestartEntry,
       "tlpUpsConfigAutoRestartInverterShutdown": tlpUpsConfigAutoRestartInverterShutdown,
       "tlpUpsConfigAutoRestartDelayedWakeup": tlpUpsConfigAutoRestartDelayedWakeup,
       "tlpUpsConfigAutoRestartLowVoltageCutoff": tlpUpsConfigAutoRestartLowVoltageCutoff,
       "tlpUpsConfigAutoRestartOverLoad": tlpUpsConfigAutoRestartOverLoad,
       "tlpUpsConfigAutoRestartOverTemperature": tlpUpsConfigAutoRestartOverTemperature,
       "tlpUpsConfigThresholdTable": tlpUpsConfigThresholdTable,
       "tlpUpsConfigThresholdEntry": tlpUpsConfigThresholdEntry,
       "tlpUpsConfigBatteryAgeThreshold": tlpUpsConfigBatteryAgeThreshold,
       "tlpUpsConfigLowBatteryThreshold": tlpUpsConfigLowBatteryThreshold,
       "tlpUpsConfigLowBatteryTime": tlpUpsConfigLowBatteryTime,
       "tlpUpsConfigOverLoadThreshold": tlpUpsConfigOverLoadThreshold,
       "tlpPdu": tlpPdu,
       "tlpPduIdent": tlpPduIdent,
       "tlpPduIdentNumPdu": tlpPduIdentNumPdu,
       "tlpPduIdentTable": tlpPduIdentTable,
       "tlpPduIdentEntry": tlpPduIdentEntry,
       "tlpPduIdentNumInputs": tlpPduIdentNumInputs,
       "tlpPduIdentNumOutputs": tlpPduIdentNumOutputs,
       "tlpPduIdentNumPhases": tlpPduIdentNumPhases,
       "tlpPduIdentNumOutlets": tlpPduIdentNumOutlets,
       "tlpPduIdentNumOutletGroups": tlpPduIdentNumOutletGroups,
       "tlpPduIdentNumCircuits": tlpPduIdentNumCircuits,
       "tlpPduIdentNumBreakers": tlpPduIdentNumBreakers,
       "tlpPduIdentNumHeatsinks": tlpPduIdentNumHeatsinks,
       "tlpPduSupportsTable": tlpPduSupportsTable,
       "tlpPduSupportsEntry": tlpPduSupportsEntry,
       "tlpPduSupportsEnergywise": tlpPduSupportsEnergywise,
       "tlpPduSupportsRampShed": tlpPduSupportsRampShed,
       "tlpPduSupportsOutletGroup": tlpPduSupportsOutletGroup,
       "tlpPduSupportsOutletCurrentPower": tlpPduSupportsOutletCurrentPower,
       "tlpPduSupportsOutletVoltage": tlpPduSupportsOutletVoltage,
       "tlpPduDisplayTable": tlpPduDisplayTable,
       "tlpPduDisplayEntry": tlpPduDisplayEntry,
       "tlpPduDisplayScheme": tlpPduDisplayScheme,
       "tlpPduDisplayOrientation": tlpPduDisplayOrientation,
       "tlpPduDisplayAutoScroll": tlpPduDisplayAutoScroll,
       "tlpPduDisplayIntensity": tlpPduDisplayIntensity,
       "tlpPduDisplayUnits": tlpPduDisplayUnits,
       "tlpPduDevice": tlpPduDevice,
       "tlpPduDeviceTable": tlpPduDeviceTable,
       "tlpPduDeviceEntry": tlpPduDeviceEntry,
       "tlpPduDeviceMainLoadState": tlpPduDeviceMainLoadState,
       "tlpPduDeviceMainLoadControllable": tlpPduDeviceMainLoadControllable,
       "tlpPduDeviceMainLoadCommand": tlpPduDeviceMainLoadCommand,
       "tlpPduDevicePowerOnDelay": tlpPduDevicePowerOnDelay,
       "tlpPduDeviceTotalInputPowerRating": tlpPduDeviceTotalInputPowerRating,
       "tlpPduDeviceTemperatureC": tlpPduDeviceTemperatureC,
       "tlpPduDeviceTemperatureF": tlpPduDeviceTemperatureF,
       "tlpPduDevicePhaseImbalance": tlpPduDevicePhaseImbalance,
       "tlpPduDeviceOutputPowerTotal": tlpPduDeviceOutputPowerTotal,
       "tlpPduDeviceAggregatePowerFactor": tlpPduDeviceAggregatePowerFactor,
       "tlpPduDeviceOutputCurrentPrecision": tlpPduDeviceOutputCurrentPrecision,
       "tlpPduDetail": tlpPduDetail,
       "tlpPduInput": tlpPduInput,
       "tlpPduInputTable": tlpPduInputTable,
       "tlpPduInputEntry": tlpPduInputEntry,
       "tlpPduInputNominalVoltage": tlpPduInputNominalVoltage,
       "tlpPduInputNominalVoltagePhaseToPhase": tlpPduInputNominalVoltagePhaseToPhase,
       "tlpPduInputNominalVoltagePhaseToNeutral": tlpPduInputNominalVoltagePhaseToNeutral,
       "tlpPduInputLowTransferVoltage": tlpPduInputLowTransferVoltage,
       "tlpPduInputLowTransferVoltageLowerBound": tlpPduInputLowTransferVoltageLowerBound,
       "tlpPduInputLowTransferVoltageUpperBound": tlpPduInputLowTransferVoltageUpperBound,
       "tlpPduInputHighTransferVoltage": tlpPduInputHighTransferVoltage,
       "tlpPduInputHighTransferVoltageLowerBound": tlpPduInputHighTransferVoltageLowerBound,
       "tlpPduInputHighTransferVoltageUpperBound": tlpPduInputHighTransferVoltageUpperBound,
       "tlpPduInputCurrentLimit": tlpPduInputCurrentLimit,
       "tlpPduInputPhaseTable": tlpPduInputPhaseTable,
       "tlpPduInputPhaseEntry": tlpPduInputPhaseEntry,
       "tlpPduInputPhaseIndex": tlpPduInputPhaseIndex,
       "tlpPduInputPhasePhaseType": tlpPduInputPhasePhaseType,
       "tlpPduInputPhaseFrequency": tlpPduInputPhaseFrequency,
       "tlpPduInputPhaseVoltage": tlpPduInputPhaseVoltage,
       "tlpPduInputPhaseVoltageMin": tlpPduInputPhaseVoltageMin,
       "tlpPduInputPhaseVoltageMax": tlpPduInputPhaseVoltageMax,
       "tlpPduInputPhaseCurrent": tlpPduInputPhaseCurrent,
       "tlpPduOutput": tlpPduOutput,
       "tlpPduOutputTable": tlpPduOutputTable,
       "tlpPduOutputEntry": tlpPduOutputEntry,
       "tlpPduOutputIndex": tlpPduOutputIndex,
       "tlpPduOutputPhase": tlpPduOutputPhase,
       "tlpPduOutputPhaseType": tlpPduOutputPhaseType,
       "tlpPduOutputVoltage": tlpPduOutputVoltage,
       "tlpPduOutputCurrent": tlpPduOutputCurrent,
       "tlpPduOutputCurrentMin": tlpPduOutputCurrentMin,
       "tlpPduOutputCurrentMax": tlpPduOutputCurrentMax,
       "tlpPduOutputActivePower": tlpPduOutputActivePower,
       "tlpPduOutputPowerFactor": tlpPduOutputPowerFactor,
       "tlpPduOutputSource": tlpPduOutputSource,
       "tlpPduOutlet": tlpPduOutlet,
       "tlpPduOutletTable": tlpPduOutletTable,
       "tlpPduOutletEntry": tlpPduOutletEntry,
       "tlpPduOutletIndex": tlpPduOutletIndex,
       "tlpPduOutletName": tlpPduOutletName,
       "tlpPduOutletDescription": tlpPduOutletDescription,
       "tlpPduOutletState": tlpPduOutletState,
       "tlpPduOutletControllable": tlpPduOutletControllable,
       "tlpPduOutletCommand": tlpPduOutletCommand,
       "tlpPduOutletVoltage": tlpPduOutletVoltage,
       "tlpPduOutletCurrent": tlpPduOutletCurrent,
       "tlpPduOutletPower": tlpPduOutletPower,
       "tlpPduOutletRampAction": tlpPduOutletRampAction,
       "tlpPduOutletRampDelay": tlpPduOutletRampDelay,
       "tlpPduOutletShedAction": tlpPduOutletShedAction,
       "tlpPduOutletShedDelay": tlpPduOutletShedDelay,
       "tlpPduOutletGroup": tlpPduOutletGroup,
       "tlpPduOutletBank": tlpPduOutletBank,
       "tlpPduOutletCircuit": tlpPduOutletCircuit,
       "tlpPduOutletPhase": tlpPduOutletPhase,
       "tlpPduOutletGroupTable": tlpPduOutletGroupTable,
       "tlpPduOutletGroupEntry": tlpPduOutletGroupEntry,
       "tlpPduOutletGroupIndex": tlpPduOutletGroupIndex,
       "tlpPduOutletGroupRowStatus": tlpPduOutletGroupRowStatus,
       "tlpPduOutletGroupName": tlpPduOutletGroupName,
       "tlpPduOutletGroupDescription": tlpPduOutletGroupDescription,
       "tlpPduOutletGroupState": tlpPduOutletGroupState,
       "tlpPduOutletGroupCommand": tlpPduOutletGroupCommand,
       "tlpPduCircuit": tlpPduCircuit,
       "tlpPduCircuitTable": tlpPduCircuitTable,
       "tlpPduCircuitEntry": tlpPduCircuitEntry,
       "tlpPduCircuitIndex": tlpPduCircuitIndex,
       "tlpPduCircuitPhase": tlpPduCircuitPhase,
       "tlpPduCircuitInputVoltage": tlpPduCircuitInputVoltage,
       "tlpPduCircuitTotalCurrent": tlpPduCircuitTotalCurrent,
       "tlpPduCircuitCurrentLimit": tlpPduCircuitCurrentLimit,
       "tlpPduCircuitCurrentMin": tlpPduCircuitCurrentMin,
       "tlpPduCircuitCurrentMax": tlpPduCircuitCurrentMax,
       "tlpPduCircuitTotalPower": tlpPduCircuitTotalPower,
       "tlpPduCircuitPowerFactor": tlpPduCircuitPowerFactor,
       "tlpPduCircuitUtilization": tlpPduCircuitUtilization,
       "tlpPduBreaker": tlpPduBreaker,
       "tlpPduBreakerTable": tlpPduBreakerTable,
       "tlpPduBreakerEntry": tlpPduBreakerEntry,
       "tlpPduBreakerIndex": tlpPduBreakerIndex,
       "tlpPduBreakerStatus": tlpPduBreakerStatus,
       "tlpPduHeatsink": tlpPduHeatsink,
       "tlpPduHeatsinkTable": tlpPduHeatsinkTable,
       "tlpPduHeatsinkEntry": tlpPduHeatsinkEntry,
       "tlpPduHeatsinkIndex": tlpPduHeatsinkIndex,
       "tlpPduHeatsinkStatus": tlpPduHeatsinkStatus,
       "tlpPduHeatsinkTemperatureC": tlpPduHeatsinkTemperatureC,
       "tlpPduHeatsinkTemperatureF": tlpPduHeatsinkTemperatureF,
       "tlpPduControl": tlpPduControl,
       "tlpPduControlTable": tlpPduControlTable,
       "tlpPduControlEntry": tlpPduControlEntry,
       "tlpPduControlRamp": tlpPduControlRamp,
       "tlpPduControlShed": tlpPduControlShed,
       "tlpPduControlPduOn": tlpPduControlPduOn,
       "tlpPduControlPduOff": tlpPduControlPduOff,
       "tlpPduControlPduReboot": tlpPduControlPduReboot,
       "tlpPduConfig": tlpPduConfig,
       "tlpPduConfigTable": tlpPduConfigTable,
       "tlpPduConfigEntry": tlpPduConfigEntry,
       "tlpPduConfigInputVoltage": tlpPduConfigInputVoltage,
       "tlpEnvirosense": tlpEnvirosense,
       "tlpEnvIdent": tlpEnvIdent,
       "tlpEnvIdentNumEnvirosense": tlpEnvIdentNumEnvirosense,
       "tlpEnvIdentTable": tlpEnvIdentTable,
       "tlpEnvIdentEntry": tlpEnvIdentEntry,
       "tlpEnvIdentTempSupported": tlpEnvIdentTempSupported,
       "tlpEnvIdentHumiditySupported": tlpEnvIdentHumiditySupported,
       "tlpEnvNumInputContacts": tlpEnvNumInputContacts,
       "tlpEnvNumOutputContacts": tlpEnvNumOutputContacts,
       "tlpEnvDetail": tlpEnvDetail,
       "tlpEnvTemperatureTable": tlpEnvTemperatureTable,
       "tlpEnvTemperatureEntry": tlpEnvTemperatureEntry,
       "tlpEnvTemperatureC": tlpEnvTemperatureC,
       "tlpEnvTemperatureF": tlpEnvTemperatureF,
       "tlpEnvTemperatureInAlarm": tlpEnvTemperatureInAlarm,
       "tlpEnvHumidityTable": tlpEnvHumidityTable,
       "tlpEnvHumidityEntry": tlpEnvHumidityEntry,
       "tlpEnvHumidityHumidity": tlpEnvHumidityHumidity,
       "tlpEnvHumidityInAlarm": tlpEnvHumidityInAlarm,
       "tlpEnvInputContactTable": tlpEnvInputContactTable,
       "tlpEnvInputContactEntry": tlpEnvInputContactEntry,
       "tlpEnvInputContactIndex": tlpEnvInputContactIndex,
       "tlpEnvInputContactName": tlpEnvInputContactName,
       "tlpEnvInputContactNormalState": tlpEnvInputContactNormalState,
       "tlpEnvInputContactCurrentState": tlpEnvInputContactCurrentState,
       "tlpEnvInputContactInAlarm": tlpEnvInputContactInAlarm,
       "tlpEnvOutputContactTable": tlpEnvOutputContactTable,
       "tlpEnvOutputContactEntry": tlpEnvOutputContactEntry,
       "tlpEnvOutputContactIndex": tlpEnvOutputContactIndex,
       "tlpEnvOutputContactName": tlpEnvOutputContactName,
       "tlpEnvOutputContactNormalState": tlpEnvOutputContactNormalState,
       "tlpEnvOutputContactCurrentState": tlpEnvOutputContactCurrentState,
       "tlpEnvOutputContactInAlarm": tlpEnvOutputContactInAlarm,
       "tlpEnvConfig": tlpEnvConfig,
       "tlpEnvConfigTable": tlpEnvConfigTable,
       "tlpEnvConfigEntry": tlpEnvConfigEntry,
       "tlpEnvTemperatureLowLimit": tlpEnvTemperatureLowLimit,
       "tlpEnvTemperatureHighLimit": tlpEnvTemperatureHighLimit,
       "tlpEnvHumidityLowLimit": tlpEnvHumidityLowLimit,
       "tlpEnvHumidityHighLimit": tlpEnvHumidityHighLimit,
       "tlpAts": tlpAts,
       "tlpAtsIdent": tlpAtsIdent,
       "tlpAtsIdentNumAts": tlpAtsIdentNumAts,
       "tlpAtsIdentTable": tlpAtsIdentTable,
       "tlpAtsIdentEntry": tlpAtsIdentEntry,
       "tlpAtsIdentNumInputs": tlpAtsIdentNumInputs,
       "tlpAtsIdentNumOutputs": tlpAtsIdentNumOutputs,
       "tlpAtsIdentNumPhases": tlpAtsIdentNumPhases,
       "tlpAtsIdentNumOutlets": tlpAtsIdentNumOutlets,
       "tlpAtsIdentNumOutletGroups": tlpAtsIdentNumOutletGroups,
       "tlpAtsIdentNumCircuits": tlpAtsIdentNumCircuits,
       "tlpAtsIdentNumBreakers": tlpAtsIdentNumBreakers,
       "tlpAtsIdentNumHeatsinks": tlpAtsIdentNumHeatsinks,
       "tlpAtsSupportsTable": tlpAtsSupportsTable,
       "tlpAtsSupportsEntry": tlpAtsSupportsEntry,
       "tlpAtsSupportsEnergywise": tlpAtsSupportsEnergywise,
       "tlpAtsSupportsRampShed": tlpAtsSupportsRampShed,
       "tlpAtsSupportsOutletGroup": tlpAtsSupportsOutletGroup,
       "tlpAtsSupportsOutletCurrentPower": tlpAtsSupportsOutletCurrentPower,
       "tlpAtsSupportsOutletVoltage": tlpAtsSupportsOutletVoltage,
       "tlpAtsDisplayTable": tlpAtsDisplayTable,
       "tlpAtsDisplayEntry": tlpAtsDisplayEntry,
       "tlpAtsDisplayScheme": tlpAtsDisplayScheme,
       "tlpAtsDisplayOrientation": tlpAtsDisplayOrientation,
       "tlpAtsDisplayAutoScroll": tlpAtsDisplayAutoScroll,
       "tlpAtsDisplayIntensity": tlpAtsDisplayIntensity,
       "tlpAtsDisplayUnits": tlpAtsDisplayUnits,
       "tlpAtsDevice": tlpAtsDevice,
       "tlpAtsDeviceTable": tlpAtsDeviceTable,
       "tlpAtsDeviceEntry": tlpAtsDeviceEntry,
       "tlpAtsDeviceMainLoadState": tlpAtsDeviceMainLoadState,
       "tlpAtsDeviceMainLoadControllable": tlpAtsDeviceMainLoadControllable,
       "tlpAtsDeviceMainLoadCommand": tlpAtsDeviceMainLoadCommand,
       "tlpAtsDevicePowerOnDelay": tlpAtsDevicePowerOnDelay,
       "tlpAtsDeviceTotalInputPowerRating": tlpAtsDeviceTotalInputPowerRating,
       "tlpAtsDeviceTemperatureC": tlpAtsDeviceTemperatureC,
       "tlpAtsDeviceTemperatureF": tlpAtsDeviceTemperatureF,
       "tlpAtsDevicePhaseImbalance": tlpAtsDevicePhaseImbalance,
       "tlpAtsDeviceOutputPowerTotal": tlpAtsDeviceOutputPowerTotal,
       "tlpAtsDeviceAggregatePowerFactor": tlpAtsDeviceAggregatePowerFactor,
       "tlpAtsDeviceOutputCurrentPrecision": tlpAtsDeviceOutputCurrentPrecision,
       "tlpAtsDeviceGeneralFault": tlpAtsDeviceGeneralFault,
       "tlpAtsDetail": tlpAtsDetail,
       "tlpAtsInput": tlpAtsInput,
       "tlpAtsInputTable": tlpAtsInputTable,
       "tlpAtsInputEntry": tlpAtsInputEntry,
       "tlpAtsInputNominalVoltage": tlpAtsInputNominalVoltage,
       "tlpAtsInputNominalVoltagePhaseToPhase": tlpAtsInputNominalVoltagePhaseToPhase,
       "tlpAtsInputNominalVoltagePhaseToNeutral": tlpAtsInputNominalVoltagePhaseToNeutral,
       "tlpAtsInputBadTransferVoltage": tlpAtsInputBadTransferVoltage,
       "tlpAtsInputBadTransferVoltageLowerBound": tlpAtsInputBadTransferVoltageLowerBound,
       "tlpAtsInputBadTransferVoltageUpperBound": tlpAtsInputBadTransferVoltageUpperBound,
       "tlpAtsInputHighTransferVoltage": tlpAtsInputHighTransferVoltage,
       "tlpAtsInputHighTransferVoltageLowerBound": tlpAtsInputHighTransferVoltageLowerBound,
       "tlpAtsInputHighTransferVoltageUpperBound": tlpAtsInputHighTransferVoltageUpperBound,
       "tlpAtsInputFairVoltageThreshold": tlpAtsInputFairVoltageThreshold,
       "tlpAtsInputBadVoltageThreshold": tlpAtsInputBadVoltageThreshold,
       "tlpAtsInputSourceAvailability": tlpAtsInputSourceAvailability,
       "tlpAtsInputSourceInUse": tlpAtsInputSourceInUse,
       "tlpAtsInputSourceTransitionCount": tlpAtsInputSourceTransitionCount,
       "tlpAtsInputCurrentLimit": tlpAtsInputCurrentLimit,
       "tlpAtsInputPhaseTable": tlpAtsInputPhaseTable,
       "tlpAtsInputPhaseEntry": tlpAtsInputPhaseEntry,
       "tlpAtsInputLineIndex": tlpAtsInputLineIndex,
       "tlpAtsInputPhaseIndex": tlpAtsInputPhaseIndex,
       "tlpAtsInputPhaseType": tlpAtsInputPhaseType,
       "tlpAtsInputPhaseFrequency": tlpAtsInputPhaseFrequency,
       "tlpAtsInputPhaseVoltage": tlpAtsInputPhaseVoltage,
       "tlpAtsInputPhaseVoltageMin": tlpAtsInputPhaseVoltageMin,
       "tlpAtsInputPhaseVoltageMax": tlpAtsInputPhaseVoltageMax,
       "tlpAtsInputPhaseCurrent": tlpAtsInputPhaseCurrent,
       "tlpAtsOutput": tlpAtsOutput,
       "tlpAtsOutputTable": tlpAtsOutputTable,
       "tlpAtsOutputEntry": tlpAtsOutputEntry,
       "tlpAtsOutputIndex": tlpAtsOutputIndex,
       "tlpAtsOutputPhase": tlpAtsOutputPhase,
       "tlpAtsOutputPhaseType": tlpAtsOutputPhaseType,
       "tlpAtsOutputVoltage": tlpAtsOutputVoltage,
       "tlpAtsOutputCurrent": tlpAtsOutputCurrent,
       "tlpAtsOutputCurrentMin": tlpAtsOutputCurrentMin,
       "tlpAtsOutputCurrentMax": tlpAtsOutputCurrentMax,
       "tlpAtsOutputActivePower": tlpAtsOutputActivePower,
       "tlpAtsOutputPowerFactor": tlpAtsOutputPowerFactor,
       "tlpAtsOutputSource": tlpAtsOutputSource,
       "tlpAtsOutlet": tlpAtsOutlet,
       "tlpAtsOutletTable": tlpAtsOutletTable,
       "tlpAtsOutletEntry": tlpAtsOutletEntry,
       "tlpAtsOutletIndex": tlpAtsOutletIndex,
       "tlpAtsOutletName": tlpAtsOutletName,
       "tlpAtsOutletDescription": tlpAtsOutletDescription,
       "tlpAtsOutletState": tlpAtsOutletState,
       "tlpAtsOutletControllable": tlpAtsOutletControllable,
       "tlpAtsOutletCommand": tlpAtsOutletCommand,
       "tlpAtsOutletVoltage": tlpAtsOutletVoltage,
       "tlpAtsOutletCurrent": tlpAtsOutletCurrent,
       "tlpAtsOutletPower": tlpAtsOutletPower,
       "tlpAtsOutletRampAction": tlpAtsOutletRampAction,
       "tlpAtsOutletRampDelay": tlpAtsOutletRampDelay,
       "tlpAtsOutletShedAction": tlpAtsOutletShedAction,
       "tlpAtsOutletShedDelay": tlpAtsOutletShedDelay,
       "tlpAtsOutletGroup": tlpAtsOutletGroup,
       "tlpAtsOutletBank": tlpAtsOutletBank,
       "tlpAtsOutletCircuit": tlpAtsOutletCircuit,
       "tlpAtsOutletPhase": tlpAtsOutletPhase,
       "tlpAtsOutletGroupTable": tlpAtsOutletGroupTable,
       "tlpAtsOutletGroupEntry": tlpAtsOutletGroupEntry,
       "tlpAtsOutletGroupIndex": tlpAtsOutletGroupIndex,
       "tlpAtsOutletGroupRowStatus": tlpAtsOutletGroupRowStatus,
       "tlpAtsOutletGroupName": tlpAtsOutletGroupName,
       "tlpAtsOutletGroupDescription": tlpAtsOutletGroupDescription,
       "tlpAtsOutletGroupState": tlpAtsOutletGroupState,
       "tlpAtsOutletGroupCommand": tlpAtsOutletGroupCommand,
       "tlpAtsCircuit": tlpAtsCircuit,
       "tlpAtsCircuitTable": tlpAtsCircuitTable,
       "tlpAtsCircuitEntry": tlpAtsCircuitEntry,
       "tlpAtsCircuitIndex": tlpAtsCircuitIndex,
       "tlpAtsCircuitPhase": tlpAtsCircuitPhase,
       "tlpAtsCircuitInputVoltage": tlpAtsCircuitInputVoltage,
       "tlpAtsCircuitTotalCurrent": tlpAtsCircuitTotalCurrent,
       "tlpAtsCircuitCurrentLimit": tlpAtsCircuitCurrentLimit,
       "tlpAtsCircuitCurrentMin": tlpAtsCircuitCurrentMin,
       "tlpAtsCircuitCurrentMax": tlpAtsCircuitCurrentMax,
       "tlpAtsCircuitTotalPower": tlpAtsCircuitTotalPower,
       "tlpAtsCircuitPowerFactor": tlpAtsCircuitPowerFactor,
       "tlpAtsCircuitUtilization": tlpAtsCircuitUtilization,
       "tlpAtsBreaker": tlpAtsBreaker,
       "tlpAtsBreakerTable": tlpAtsBreakerTable,
       "tlpAtsBreakerEntry": tlpAtsBreakerEntry,
       "tlpAtsBreakerIndex": tlpAtsBreakerIndex,
       "tlpAtsBreakerStatus": tlpAtsBreakerStatus,
       "tlpAtsHeatsink": tlpAtsHeatsink,
       "tlpAtsHeatsinkTable": tlpAtsHeatsinkTable,
       "tlpAtsHeatsinkEntry": tlpAtsHeatsinkEntry,
       "tlpAtsHeatsinkIndex": tlpAtsHeatsinkIndex,
       "tlpAtsHeatsinkStatus": tlpAtsHeatsinkStatus,
       "tlpAtsHeatsinkTemperatureC": tlpAtsHeatsinkTemperatureC,
       "tlpAtsHeatsinkTemperatureF": tlpAtsHeatsinkTemperatureF,
       "tlpAtsControl": tlpAtsControl,
       "tlpAtsControlTable": tlpAtsControlTable,
       "tlpAtsControlEntry": tlpAtsControlEntry,
       "tlpAtsControlRamp": tlpAtsControlRamp,
       "tlpAtsControlShed": tlpAtsControlShed,
       "tlpAtsControlAtsOn": tlpAtsControlAtsOn,
       "tlpAtsControlAtsOff": tlpAtsControlAtsOff,
       "tlpAtsControlAtsReboot": tlpAtsControlAtsReboot,
       "tlpAtsControlResetGeneralFault": tlpAtsControlResetGeneralFault,
       "tlpAtsConfig": tlpAtsConfig,
       "tlpAtsConfigTable": tlpAtsConfigTable,
       "tlpAtsConfigEntry": tlpAtsConfigEntry,
       "tlpAtsConfigInputVoltage": tlpAtsConfigInputVoltage,
       "tlpAtsConfigSourceSelect": tlpAtsConfigSourceSelect,
       "tlpAtsConfigSource1ReturnTime": tlpAtsConfigSource1ReturnTime,
       "tlpAtsConfigSource2ReturnTime": tlpAtsConfigSource2ReturnTime,
       "tlpAtsConfigAutoRampOnTransition": tlpAtsConfigAutoRampOnTransition,
       "tlpAtsConfigAutoShedOnTransition": tlpAtsConfigAutoShedOnTransition,
       "tlpAtsConfigVoltageRangeTable": tlpAtsConfigVoltageRangeTable,
       "tlpAtsConfigVoltageRangeEntry": tlpAtsConfigVoltageRangeEntry,
       "tlpAtsConfigHighVoltageTransfer": tlpAtsConfigHighVoltageTransfer,
       "tlpAtsConfigHighVoltageReset": tlpAtsConfigHighVoltageReset,
       "tlpAtsConfigSource1TransferReset": tlpAtsConfigSource1TransferReset,
       "tlpAtsConfigSource1BrownoutSet": tlpAtsConfigSource1BrownoutSet,
       "tlpAtsConfigSource1TransferSet": tlpAtsConfigSource1TransferSet,
       "tlpAtsConfigSource2TransferReset": tlpAtsConfigSource2TransferReset,
       "tlpAtsConfigSource2BrownoutSet": tlpAtsConfigSource2BrownoutSet,
       "tlpAtsConfigSource2TransferSet": tlpAtsConfigSource2TransferSet,
       "tlpAtsConfigLowVoltageReset": tlpAtsConfigLowVoltageReset,
       "tlpAtsConfigLowVoltageTransfer": tlpAtsConfigLowVoltageTransfer,
       "tlpAtsConfigVoltageRangeLimitsTable": tlpAtsConfigVoltageRangeLimitsTable,
       "tlpAtsConfigVoltageRangeLimitsEntry": tlpAtsConfigVoltageRangeLimitsEntry,
       "tlpAtsConfigSourceBrownoutSetMinimum": tlpAtsConfigSourceBrownoutSetMinimum,
       "tlpAtsConfigSourceBrownoutSetMaximum": tlpAtsConfigSourceBrownoutSetMaximum,
       "tlpAtsConfigSourceTransferSetMinimum": tlpAtsConfigSourceTransferSetMinimum,
       "tlpAtsConfigSourceTransferSetMaximum": tlpAtsConfigSourceTransferSetMaximum,
       "tlpAtsConfigThresholdTable": tlpAtsConfigThresholdTable,
       "tlpAtsConfigThresholdEntry": tlpAtsConfigThresholdEntry,
       "tlpAtsConfigOverCurrentThreshold": tlpAtsConfigOverCurrentThreshold,
       "tlpAtsConfigOverTemperatureThreshold": tlpAtsConfigOverTemperatureThreshold,
       "tlpAtsConfigOverVoltageThreshold": tlpAtsConfigOverVoltageThreshold,
       "tlpAtsConfigOverLoadThreshold": tlpAtsConfigOverLoadThreshold,
       "tlpCooling": tlpCooling,
       "tlpCoolingIdent": tlpCoolingIdent,
       "tlpCoolingIdentNumCooling": tlpCoolingIdentNumCooling,
       "tlpCoolingDevice": tlpCoolingDevice,
       "tlpCoolingDetail": tlpCoolingDetail,
       "tlpCoolingInput": tlpCoolingInput,
       "tlpCoolingOutput": tlpCoolingOutput,
       "tlpCoolingControl": tlpCoolingControl,
       "tlpCoolingConfig": tlpCoolingConfig,
       "tlpKvm": tlpKvm,
       "tlpKvmIdent": tlpKvmIdent,
       "tlpKvmIdentNumKvm": tlpKvmIdentNumKvm,
       "tlpKvmDevice": tlpKvmDevice,
       "tlpKvmDetail": tlpKvmDetail,
       "tlpKvmControl": tlpKvmControl,
       "tlpKvmConfig": tlpKvmConfig,
       "tlpRackTrack": tlpRackTrack,
       "tlpRackTrackIdent": tlpRackTrackIdent,
       "tlpRackTrackIdentNumRackTrack": tlpRackTrackIdentNumRackTrack,
       "tlpRackTrackDevice": tlpRackTrackDevice,
       "tlpRackTrackDetail": tlpRackTrackDetail,
       "tlpRackTrackControl": tlpRackTrackControl,
       "tlpRackTrackConfig": tlpRackTrackConfig,
       "tlpSwitch": tlpSwitch,
       "tlpSwitchIdent": tlpSwitchIdent,
       "tlpSwitchIdentNumSwitch": tlpSwitchIdentNumSwitch,
       "tlpSwitchDevice": tlpSwitchDevice,
       "tlpSwitchDetail": tlpSwitchDetail,
       "tlpSwitchControl": tlpSwitchControl,
       "tlpSwitchConfig": tlpSwitchConfig,
       "tlpSoftware": tlpSoftware,
       "tlpAgentDetails": tlpAgentDetails,
       "tlpAgentIdent": tlpAgentIdent,
       "tlpAgentType": tlpAgentType,
       "tlpAgentVersion": tlpAgentVersion,
       "tlpAgentDriverVersion": tlpAgentDriverVersion,
       "tlpAgentMAC": tlpAgentMAC,
       "tlpAgentSerialNum": tlpAgentSerialNum,
       "tlpAgentUuid": tlpAgentUuid,
       "tlpAgentAttributes": tlpAgentAttributes,
       "tlpAgentAttributesSupports": tlpAgentAttributesSupports,
       "tlpAgentAttributesSupportsHTTP": tlpAgentAttributesSupportsHTTP,
       "tlpAgentAttributesSupportsHTTPS": tlpAgentAttributesSupportsHTTPS,
       "tlpAgentAttributesSupportsFTP": tlpAgentAttributesSupportsFTP,
       "tlpAgentAttributesSupportsTelnetMenu": tlpAgentAttributesSupportsTelnetMenu,
       "tlpAgentAttributesSupportsTelnetCLI": tlpAgentAttributesSupportsTelnetCLI,
       "tlpAgentAttributesSupportsSSHMenu": tlpAgentAttributesSupportsSSHMenu,
       "tlpAgentAttributesSupportsSSHCLI": tlpAgentAttributesSupportsSSHCLI,
       "tlpAgentAttributesSupportsSNMP": tlpAgentAttributesSupportsSNMP,
       "tlpAgentAttributesSupportsSNMPTrap": tlpAgentAttributesSupportsSNMPTrap,
       "tlpAgentAttributesAutostart": tlpAgentAttributesAutostart,
       "tlpAgentAttributesAutostartHTTP": tlpAgentAttributesAutostartHTTP,
       "tlpAgentAttributesAutostartHTTPS": tlpAgentAttributesAutostartHTTPS,
       "tlpAgentAttributesAutostartFTP": tlpAgentAttributesAutostartFTP,
       "tlpAgentAttributesAutostartTelnetMenu": tlpAgentAttributesAutostartTelnetMenu,
       "tlpAgentAttributesAutostartTelnetCLI": tlpAgentAttributesAutostartTelnetCLI,
       "tlpAgentAttributesAutostartSSHMenu": tlpAgentAttributesAutostartSSHMenu,
       "tlpAgentAttributesAutostartSSHCLI": tlpAgentAttributesAutostartSSHCLI,
       "tlpAgentAttributesAutostartSNMP": tlpAgentAttributesAutostartSNMP,
       "tlpAgentAttributesSnmp": tlpAgentAttributesSnmp,
       "tlpAgentAttributesSNMPv1Enabled": tlpAgentAttributesSNMPv1Enabled,
       "tlpAgentAttributesSNMPv2cEnabled": tlpAgentAttributesSNMPv2cEnabled,
       "tlpAgentAttributesSNMPv3Enabled": tlpAgentAttributesSNMPv3Enabled,
       "tlpAgentAttributesPorts": tlpAgentAttributesPorts,
       "tlpAgentAttributesHTTPPort": tlpAgentAttributesHTTPPort,
       "tlpAgentAttributesHTTPSPort": tlpAgentAttributesHTTPSPort,
       "tlpAgentAttributesFTPPort": tlpAgentAttributesFTPPort,
       "tlpAgentAttributesTelnetMenuPort": tlpAgentAttributesTelnetMenuPort,
       "tlpAgentAttributesTelnetCLIPort": tlpAgentAttributesTelnetCLIPort,
       "tlpAgentAttributesSSHMenuPort": tlpAgentAttributesSSHMenuPort,
       "tlpAgentAttributesSSHCLIPort": tlpAgentAttributesSSHCLIPort,
       "tlpAgentAttributesSNMPPort": tlpAgentAttributesSNMPPort,
       "tlpAgentAttributesSNMPTrapPort": tlpAgentAttributesSNMPTrapPort,
       "tlpAgentSettings": tlpAgentSettings,
       "tlpAgentConfig": tlpAgentConfig,
       "tlpAgentConfigRemoteRegistration": tlpAgentConfigRemoteRegistration,
       "tlpAgentConfigCurrentTime": tlpAgentConfigCurrentTime,
       "tlpAgentContacts": tlpAgentContacts,
       "tlpAgentEmailContacts": tlpAgentEmailContacts,
       "tlpAgentNumEmailContacts": tlpAgentNumEmailContacts,
       "tlpAgentEmailContactTable": tlpAgentEmailContactTable,
       "tlpAgentEmailContactEntry": tlpAgentEmailContactEntry,
       "tlpAgentEmailContactIndex": tlpAgentEmailContactIndex,
       "tlpAgentEmailContactRowStatus": tlpAgentEmailContactRowStatus,
       "tlpAgentEmailContactName": tlpAgentEmailContactName,
       "tlpAgentEmailContactAddress": tlpAgentEmailContactAddress,
       "tlpAgentSnmpContacts": tlpAgentSnmpContacts,
       "tlpAgentNumSnmpContacts": tlpAgentNumSnmpContacts,
       "tlpAgentSnmpContactTable": tlpAgentSnmpContactTable,
       "tlpAgentSnmpContactEntry": tlpAgentSnmpContactEntry,
       "tlpAgentSnmpContactIndex": tlpAgentSnmpContactIndex,
       "tlpAgentSnmpContactRowStatus": tlpAgentSnmpContactRowStatus,
       "tlpAgentSnmpContactName": tlpAgentSnmpContactName,
       "tlpAgentSnmpContactIpAddress": tlpAgentSnmpContactIpAddress,
       "tlpAgentSnmpContactPort": tlpAgentSnmpContactPort,
       "tlpAgentSnmpContactSnmpVersion": tlpAgentSnmpContactSnmpVersion,
       "tlpAgentSnmpContactSecurityName": tlpAgentSnmpContactSecurityName,
       "tlpAgentSnmpContactPrivPassword": tlpAgentSnmpContactPrivPassword,
       "tlpAgentSnmpContactAuthPassword": tlpAgentSnmpContactAuthPassword,
       "tlpAlarms": tlpAlarms,
       "tlpAlarmsPresent": tlpAlarmsPresent,
       "tlpAlarmTable": tlpAlarmTable,
       "tlpAlarmEntry": tlpAlarmEntry,
       "tlpAlarmId": tlpAlarmId,
       "tlpAlarmDescr": tlpAlarmDescr,
       "tlpAlarmTime": tlpAlarmTime,
       "tlpAlarmTableRef": tlpAlarmTableRef,
       "tlpAlarmTableRowRef": tlpAlarmTableRowRef,
       "tlpAlarmDetail": tlpAlarmDetail,
       "tlpAlarmType": tlpAlarmType,
       "tlpAlarmState": tlpAlarmState,
       "tlpAlarmAcknowledged": tlpAlarmAcknowledged,
       "tlpAlarmsWellKnown": tlpAlarmsWellKnown,
       "tlpAgentAlarms": tlpAgentAlarms,
       "tlpDeviceAlarms": tlpDeviceAlarms,
       "tlpAlarmCommunicationsLost": tlpAlarmCommunicationsLost,
       "tlpAlarmUserDefined": tlpAlarmUserDefined,
       "tlpAlarmUserDefined01": tlpAlarmUserDefined01,
       "tlpAlarmUserDefined02": tlpAlarmUserDefined02,
       "tlpAlarmUserDefined03": tlpAlarmUserDefined03,
       "tlpAlarmUserDefined04": tlpAlarmUserDefined04,
       "tlpAlarmUserDefined05": tlpAlarmUserDefined05,
       "tlpAlarmUserDefined06": tlpAlarmUserDefined06,
       "tlpAlarmUserDefined07": tlpAlarmUserDefined07,
       "tlpAlarmUserDefined08": tlpAlarmUserDefined08,
       "tlpAlarmUserDefined09": tlpAlarmUserDefined09,
       "tlpUpsAlarms": tlpUpsAlarms,
       "tlpUpsAlarmBatteryBad": tlpUpsAlarmBatteryBad,
       "tlpUpsAlarmOnBattery": tlpUpsAlarmOnBattery,
       "tlpUpsAlarmLowBattery": tlpUpsAlarmLowBattery,
       "tlpUpsAlarmDepletedBattery": tlpUpsAlarmDepletedBattery,
       "tlpUpsAlarmTempBad": tlpUpsAlarmTempBad,
       "tlpUpsAlarmInputBad": tlpUpsAlarmInputBad,
       "tlpUpsAlarmOutputBad": tlpUpsAlarmOutputBad,
       "tlpUpsAlarmOutputOverload": tlpUpsAlarmOutputOverload,
       "tlpUpsAlarmOnBypass": tlpUpsAlarmOnBypass,
       "tlpUpsAlarmBypassBad": tlpUpsAlarmBypassBad,
       "tlpUpsAlarmOutputOffAsRequested": tlpUpsAlarmOutputOffAsRequested,
       "tlpUpsAlarmUpsOffAsRequested": tlpUpsAlarmUpsOffAsRequested,
       "tlpUpsAlarmChargerFailed": tlpUpsAlarmChargerFailed,
       "tlpUpsAlarmUpsOutputOff": tlpUpsAlarmUpsOutputOff,
       "tlpUpsAlarmUpsSystemOff": tlpUpsAlarmUpsSystemOff,
       "tlpUpsAlarmFanFailure": tlpUpsAlarmFanFailure,
       "tlpUpsAlarmFuseFailure": tlpUpsAlarmFuseFailure,
       "tlpUpsAlarmGeneralFault": tlpUpsAlarmGeneralFault,
       "tlpUpsAlarmDiagnosticTestFailed": tlpUpsAlarmDiagnosticTestFailed,
       "tlpUpsAlarmAwaitingPower": tlpUpsAlarmAwaitingPower,
       "tlpUpsAlarmShutdownPending": tlpUpsAlarmShutdownPending,
       "tlpUpsAlarmShutdownImminent": tlpUpsAlarmShutdownImminent,
       "tlpUpsAlarmLoadLevelAboveThreshold": tlpUpsAlarmLoadLevelAboveThreshold,
       "tlpUpsAlarmLoadLevelAboveThresholdTotal": tlpUpsAlarmLoadLevelAboveThresholdTotal,
       "tlpUpsAlarmLoadLevelAboveThresholdPhase1": tlpUpsAlarmLoadLevelAboveThresholdPhase1,
       "tlpUpsAlarmLoadLevelAboveThresholdPhase2": tlpUpsAlarmLoadLevelAboveThresholdPhase2,
       "tlpUpsAlarmLoadLevelAboveThresholdPhase3": tlpUpsAlarmLoadLevelAboveThresholdPhase3,
       "tlpUpsAlarmOutputCurrentChanged": tlpUpsAlarmOutputCurrentChanged,
       "tlpUpsAlarmBatteryAgeAboveThreshold": tlpUpsAlarmBatteryAgeAboveThreshold,
       "tlpUpsAlarmLoadOff": tlpUpsAlarmLoadOff,
       "tlpUpsAlarmLoadOff01": tlpUpsAlarmLoadOff01,
       "tlpUpsAlarmLoadOff02": tlpUpsAlarmLoadOff02,
       "tlpUpsAlarmLoadOff03": tlpUpsAlarmLoadOff03,
       "tlpUpsAlarmLoadOff04": tlpUpsAlarmLoadOff04,
       "tlpUpsAlarmLoadOff05": tlpUpsAlarmLoadOff05,
       "tlpUpsAlarmLoadOff06": tlpUpsAlarmLoadOff06,
       "tlpUpsAlarmLoadOff07": tlpUpsAlarmLoadOff07,
       "tlpUpsAlarmLoadOff08": tlpUpsAlarmLoadOff08,
       "tlpUpsAlarmLoadOff09": tlpUpsAlarmLoadOff09,
       "tlpUpsAlarmLoadOff10": tlpUpsAlarmLoadOff10,
       "tlpUpsAlarmLoadOff11": tlpUpsAlarmLoadOff11,
       "tlpUpsAlarmLoadOff12": tlpUpsAlarmLoadOff12,
       "tlpUpsAlarmLoadOff13": tlpUpsAlarmLoadOff13,
       "tlpUpsAlarmLoadOff14": tlpUpsAlarmLoadOff14,
       "tlpUpsAlarmLoadOff15": tlpUpsAlarmLoadOff15,
       "tlpUpsAlarmLoadOff16": tlpUpsAlarmLoadOff16,
       "tlpUpsAlarmLoadOff17": tlpUpsAlarmLoadOff17,
       "tlpUpsAlarmLoadOff18": tlpUpsAlarmLoadOff18,
       "tlpUpsAlarmLoadOff19": tlpUpsAlarmLoadOff19,
       "tlpUpsAlarmLoadOff20": tlpUpsAlarmLoadOff20,
       "tlpUpsAlarmLoadOff21": tlpUpsAlarmLoadOff21,
       "tlpUpsAlarmLoadOff22": tlpUpsAlarmLoadOff22,
       "tlpUpsAlarmLoadOff23": tlpUpsAlarmLoadOff23,
       "tlpUpsAlarmLoadOff24": tlpUpsAlarmLoadOff24,
       "tlpUpsAlarmLoadOff25": tlpUpsAlarmLoadOff25,
       "tlpUpsAlarmLoadOff26": tlpUpsAlarmLoadOff26,
       "tlpUpsAlarmLoadOff27": tlpUpsAlarmLoadOff27,
       "tlpUpsAlarmLoadOff28": tlpUpsAlarmLoadOff28,
       "tlpUpsAlarmLoadOff29": tlpUpsAlarmLoadOff29,
       "tlpUpsAlarmLoadOff30": tlpUpsAlarmLoadOff30,
       "tlpUpsAlarmLoadOff31": tlpUpsAlarmLoadOff31,
       "tlpUpsAlarmLoadOff32": tlpUpsAlarmLoadOff32,
       "tlpUpsAlarmLoadOff33": tlpUpsAlarmLoadOff33,
       "tlpUpsAlarmLoadOff34": tlpUpsAlarmLoadOff34,
       "tlpUpsAlarmLoadOff35": tlpUpsAlarmLoadOff35,
       "tlpUpsAlarmLoadOff36": tlpUpsAlarmLoadOff36,
       "tlpUpsAlarmLoadOff37": tlpUpsAlarmLoadOff37,
       "tlpUpsAlarmLoadOff38": tlpUpsAlarmLoadOff38,
       "tlpUpsAlarmLoadOff39": tlpUpsAlarmLoadOff39,
       "tlpUpsAlarmLoadOff40": tlpUpsAlarmLoadOff40,
       "tlpUpsAlarmCurrentAboveThreshold": tlpUpsAlarmCurrentAboveThreshold,
       "tlpUpsAlarmCurrentAboveThreshold1": tlpUpsAlarmCurrentAboveThreshold1,
       "tlpUpsAlarmCurrentAboveThreshold2": tlpUpsAlarmCurrentAboveThreshold2,
       "tlpUpsAlarmCurrentAboveThreshold3": tlpUpsAlarmCurrentAboveThreshold3,
       "tlpUpsAlarmRuntimeBelowWarningLevel": tlpUpsAlarmRuntimeBelowWarningLevel,
       "tlpUpsAlarmBusStartVoltageLow": tlpUpsAlarmBusStartVoltageLow,
       "tlpUpsAlarmBusOverVoltage": tlpUpsAlarmBusOverVoltage,
       "tlpUpsAlarmBusUnderVoltage": tlpUpsAlarmBusUnderVoltage,
       "tlpUpsAlarmBusVoltageUnbalanced": tlpUpsAlarmBusVoltageUnbalanced,
       "tlpUpsAlarmInverterSoftStartBad": tlpUpsAlarmInverterSoftStartBad,
       "tlpUpsAlarmInverterOverVoltage": tlpUpsAlarmInverterOverVoltage,
       "tlpUpsAlarmInverterUnderVoltage": tlpUpsAlarmInverterUnderVoltage,
       "tlpUpsAlarmInverterCircuitBad": tlpUpsAlarmInverterCircuitBad,
       "tlpUpsAlarmBatteryOverVoltage": tlpUpsAlarmBatteryOverVoltage,
       "tlpUpsAlarmBatteryUnderVoltage": tlpUpsAlarmBatteryUnderVoltage,
       "tlpUpsAlarmSiteWiringFault": tlpUpsAlarmSiteWiringFault,
       "tlpUpsAlarmOverTemperatureProtection": tlpUpsAlarmOverTemperatureProtection,
       "tlpUpsAlarmOverCharged": tlpUpsAlarmOverCharged,
       "tlpUpsAlarmEPOActive": tlpUpsAlarmEPOActive,
       "tlpUpsAlarmBypassFrequencyBad": tlpUpsAlarmBypassFrequencyBad,
       "tlpUpsAlarmExternalSmartBatteryAgeAboveThreshold": tlpUpsAlarmExternalSmartBatteryAgeAboveThreshold,
       "tlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold": tlpUpsAlarmExternalNonSmartBatteryAgeAboveThreshold,
       "tlpUpsAlarmSmartBatteryCommLost": tlpUpsAlarmSmartBatteryCommLost,
       "tlpUpsAlarmLoadsNotAllOn": tlpUpsAlarmLoadsNotAllOn,
       "tlpPduAlarms": tlpPduAlarms,
       "tlpPduAlarmLoadLevelAboveThreshold": tlpPduAlarmLoadLevelAboveThreshold,
       "tlpPduAlarmInputBad": tlpPduAlarmInputBad,
       "tlpPduAlarmOutputBad": tlpPduAlarmOutputBad,
       "tlpPduAlarmOutputOverload": tlpPduAlarmOutputOverload,
       "tlpPduAlarmOutputOff": tlpPduAlarmOutputOff,
       "tlpPduAlarmLoadOff": tlpPduAlarmLoadOff,
       "tlpPduAlarmLoadOff01": tlpPduAlarmLoadOff01,
       "tlpPduAlarmLoadOff02": tlpPduAlarmLoadOff02,
       "tlpPduAlarmLoadOff03": tlpPduAlarmLoadOff03,
       "tlpPduAlarmLoadOff04": tlpPduAlarmLoadOff04,
       "tlpPduAlarmLoadOff05": tlpPduAlarmLoadOff05,
       "tlpPduAlarmLoadOff06": tlpPduAlarmLoadOff06,
       "tlpPduAlarmLoadOff07": tlpPduAlarmLoadOff07,
       "tlpPduAlarmLoadOff08": tlpPduAlarmLoadOff08,
       "tlpPduAlarmLoadOff09": tlpPduAlarmLoadOff09,
       "tlpPduAlarmLoadOff10": tlpPduAlarmLoadOff10,
       "tlpPduAlarmLoadOff11": tlpPduAlarmLoadOff11,
       "tlpPduAlarmLoadOff12": tlpPduAlarmLoadOff12,
       "tlpPduAlarmLoadOff13": tlpPduAlarmLoadOff13,
       "tlpPduAlarmLoadOff14": tlpPduAlarmLoadOff14,
       "tlpPduAlarmLoadOff15": tlpPduAlarmLoadOff15,
       "tlpPduAlarmLoadOff16": tlpPduAlarmLoadOff16,
       "tlpPduAlarmLoadOff17": tlpPduAlarmLoadOff17,
       "tlpPduAlarmLoadOff18": tlpPduAlarmLoadOff18,
       "tlpPduAlarmLoadOff19": tlpPduAlarmLoadOff19,
       "tlpPduAlarmLoadOff20": tlpPduAlarmLoadOff20,
       "tlpPduAlarmLoadOff21": tlpPduAlarmLoadOff21,
       "tlpPduAlarmLoadOff22": tlpPduAlarmLoadOff22,
       "tlpPduAlarmLoadOff23": tlpPduAlarmLoadOff23,
       "tlpPduAlarmLoadOff24": tlpPduAlarmLoadOff24,
       "tlpPduAlarmLoadOff25": tlpPduAlarmLoadOff25,
       "tlpPduAlarmLoadOff26": tlpPduAlarmLoadOff26,
       "tlpPduAlarmLoadOff27": tlpPduAlarmLoadOff27,
       "tlpPduAlarmLoadOff28": tlpPduAlarmLoadOff28,
       "tlpPduAlarmLoadOff29": tlpPduAlarmLoadOff29,
       "tlpPduAlarmLoadOff30": tlpPduAlarmLoadOff30,
       "tlpPduAlarmLoadOff31": tlpPduAlarmLoadOff31,
       "tlpPduAlarmLoadOff32": tlpPduAlarmLoadOff32,
       "tlpPduAlarmLoadOff33": tlpPduAlarmLoadOff33,
       "tlpPduAlarmLoadOff34": tlpPduAlarmLoadOff34,
       "tlpPduAlarmLoadOff35": tlpPduAlarmLoadOff35,
       "tlpPduAlarmLoadOff36": tlpPduAlarmLoadOff36,
       "tlpPduAlarmLoadOff37": tlpPduAlarmLoadOff37,
       "tlpPduAlarmLoadOff38": tlpPduAlarmLoadOff38,
       "tlpPduAlarmLoadOff39": tlpPduAlarmLoadOff39,
       "tlpPduAlarmLoadOff40": tlpPduAlarmLoadOff40,
       "tlpPduAlarmCircuitBreakerOpen": tlpPduAlarmCircuitBreakerOpen,
       "tlpPduAlarmCircuitBreakerOpen01": tlpPduAlarmCircuitBreakerOpen01,
       "tlpPduAlarmCircuitBreakerOpen02": tlpPduAlarmCircuitBreakerOpen02,
       "tlpPduAlarmCircuitBreakerOpen03": tlpPduAlarmCircuitBreakerOpen03,
       "tlpPduAlarmCircuitBreakerOpen04": tlpPduAlarmCircuitBreakerOpen04,
       "tlpPduAlarmCircuitBreakerOpen05": tlpPduAlarmCircuitBreakerOpen05,
       "tlpPduAlarmCircuitBreakerOpen06": tlpPduAlarmCircuitBreakerOpen06,
       "tlpPduAlarmCurrentAboveThreshold": tlpPduAlarmCurrentAboveThreshold,
       "tlpPduAlarmCurrentAboveThreshold1": tlpPduAlarmCurrentAboveThreshold1,
       "tlpPduAlarmCurrentAboveThreshold2": tlpPduAlarmCurrentAboveThreshold2,
       "tlpPduAlarmCurrentAboveThreshold3": tlpPduAlarmCurrentAboveThreshold3,
       "tlpPduAlarmLoadsNotAllOn": tlpPduAlarmLoadsNotAllOn,
       "tlpEnvAlarms": tlpEnvAlarms,
       "tlpEnvAlarmTemperatureBeyondLimits": tlpEnvAlarmTemperatureBeyondLimits,
       "tlpEnvAlarmHumidityBeyondLimits": tlpEnvAlarmHumidityBeyondLimits,
       "tlpEnvAlarmInputContact": tlpEnvAlarmInputContact,
       "tlpEnvAlarmInputContact01": tlpEnvAlarmInputContact01,
       "tlpEnvAlarmInputContact02": tlpEnvAlarmInputContact02,
       "tlpEnvAlarmInputContact03": tlpEnvAlarmInputContact03,
       "tlpEnvAlarmInputContact04": tlpEnvAlarmInputContact04,
       "tlpEnvAlarmOutputContact": tlpEnvAlarmOutputContact,
       "tlpEnvAlarmOutputContact01": tlpEnvAlarmOutputContact01,
       "tlpEnvAlarmOutputContact02": tlpEnvAlarmOutputContact02,
       "tlpEnvAlarmOutputContact03": tlpEnvAlarmOutputContact03,
       "tlpEnvAlarmOutputContact04": tlpEnvAlarmOutputContact04,
       "tlpAtsAlarms": tlpAtsAlarms,
       "tlpAtsAlarmOutage": tlpAtsAlarmOutage,
       "tlpAtsAlarmSource1Outage": tlpAtsAlarmSource1Outage,
       "tlpAtsAlarmSource2Outage": tlpAtsAlarmSource2Outage,
       "tlpAtsAlarmTemperature": tlpAtsAlarmTemperature,
       "tlpAtsAlarmSystemTemperature": tlpAtsAlarmSystemTemperature,
       "tlpAtsAlarmSource1Temperature": tlpAtsAlarmSource1Temperature,
       "tlpAtsAlarmSource2Temperature": tlpAtsAlarmSource2Temperature,
       "tlpAtsAlarmLoadLevelAboveThreshold": tlpAtsAlarmLoadLevelAboveThreshold,
       "tlpAtsAlarmInputBad": tlpAtsAlarmInputBad,
       "tlpAtsAlarmOutputBad": tlpAtsAlarmOutputBad,
       "tlpAtsAlarmOutputOverload": tlpAtsAlarmOutputOverload,
       "tlpAtsAlarmOutputOff": tlpAtsAlarmOutputOff,
       "tlpAtsAlarmLoadOff": tlpAtsAlarmLoadOff,
       "tlpAtsAlarmLoadOff01": tlpAtsAlarmLoadOff01,
       "tlpAtsAlarmLoadOff02": tlpAtsAlarmLoadOff02,
       "tlpAtsAlarmLoadOff03": tlpAtsAlarmLoadOff03,
       "tlpAtsAlarmLoadOff04": tlpAtsAlarmLoadOff04,
       "tlpAtsAlarmLoadOff05": tlpAtsAlarmLoadOff05,
       "tlpAtsAlarmLoadOff06": tlpAtsAlarmLoadOff06,
       "tlpAtsAlarmLoadOff07": tlpAtsAlarmLoadOff07,
       "tlpAtsAlarmLoadOff08": tlpAtsAlarmLoadOff08,
       "tlpAtsAlarmLoadOff09": tlpAtsAlarmLoadOff09,
       "tlpAtsAlarmLoadOff10": tlpAtsAlarmLoadOff10,
       "tlpAtsAlarmLoadOff11": tlpAtsAlarmLoadOff11,
       "tlpAtsAlarmLoadOff12": tlpAtsAlarmLoadOff12,
       "tlpAtsAlarmLoadOff13": tlpAtsAlarmLoadOff13,
       "tlpAtsAlarmLoadOff14": tlpAtsAlarmLoadOff14,
       "tlpAtsAlarmLoadOff15": tlpAtsAlarmLoadOff15,
       "tlpAtsAlarmLoadOff16": tlpAtsAlarmLoadOff16,
       "tlpAtsAlarmLoadOff17": tlpAtsAlarmLoadOff17,
       "tlpAtsAlarmLoadOff18": tlpAtsAlarmLoadOff18,
       "tlpAtsAlarmLoadOff19": tlpAtsAlarmLoadOff19,
       "tlpAtsAlarmLoadOff20": tlpAtsAlarmLoadOff20,
       "tlpAtsAlarmLoadOff21": tlpAtsAlarmLoadOff21,
       "tlpAtsAlarmLoadOff22": tlpAtsAlarmLoadOff22,
       "tlpAtsAlarmLoadOff23": tlpAtsAlarmLoadOff23,
       "tlpAtsAlarmLoadOff24": tlpAtsAlarmLoadOff24,
       "tlpAtsAlarmLoadOff25": tlpAtsAlarmLoadOff25,
       "tlpAtsAlarmLoadOff26": tlpAtsAlarmLoadOff26,
       "tlpAtsAlarmLoadOff27": tlpAtsAlarmLoadOff27,
       "tlpAtsAlarmLoadOff28": tlpAtsAlarmLoadOff28,
       "tlpAtsAlarmLoadOff29": tlpAtsAlarmLoadOff29,
       "tlpAtsAlarmLoadOff30": tlpAtsAlarmLoadOff30,
       "tlpAtsAlarmLoadOff31": tlpAtsAlarmLoadOff31,
       "tlpAtsAlarmLoadOff32": tlpAtsAlarmLoadOff32,
       "tlpAtsAlarmLoadOff33": tlpAtsAlarmLoadOff33,
       "tlpAtsAlarmLoadOff34": tlpAtsAlarmLoadOff34,
       "tlpAtsAlarmLoadOff35": tlpAtsAlarmLoadOff35,
       "tlpAtsAlarmLoadOff36": tlpAtsAlarmLoadOff36,
       "tlpAtsAlarmLoadOff37": tlpAtsAlarmLoadOff37,
       "tlpAtsAlarmLoadOff38": tlpAtsAlarmLoadOff38,
       "tlpAtsAlarmLoadOff39": tlpAtsAlarmLoadOff39,
       "tlpAtsAlarmLoadOff40": tlpAtsAlarmLoadOff40,
       "tlpAtsAlarmCircuitBreakerOpen": tlpAtsAlarmCircuitBreakerOpen,
       "tlpAtsAlarmCircuitBreakerOpen01": tlpAtsAlarmCircuitBreakerOpen01,
       "tlpAtsAlarmCircuitBreakerOpen02": tlpAtsAlarmCircuitBreakerOpen02,
       "tlpAtsAlarmCircuitBreakerOpen03": tlpAtsAlarmCircuitBreakerOpen03,
       "tlpAtsAlarmCircuitBreakerOpen04": tlpAtsAlarmCircuitBreakerOpen04,
       "tlpAtsAlarmCircuitBreakerOpen05": tlpAtsAlarmCircuitBreakerOpen05,
       "tlpAtsAlarmCircuitBreakerOpen06": tlpAtsAlarmCircuitBreakerOpen06,
       "tlpAtsAlarmCurrentAboveThreshold": tlpAtsAlarmCurrentAboveThreshold,
       "tlpAtsAlarmCurrentAboveThresholdA1": tlpAtsAlarmCurrentAboveThresholdA1,
       "tlpAtsAlarmCurrentAboveThresholdA2": tlpAtsAlarmCurrentAboveThresholdA2,
       "tlpAtsAlarmCurrentAboveThresholdA3": tlpAtsAlarmCurrentAboveThresholdA3,
       "tlpAtsAlarmCurrentAboveThresholdB1": tlpAtsAlarmCurrentAboveThresholdB1,
       "tlpAtsAlarmCurrentAboveThresholdB2": tlpAtsAlarmCurrentAboveThresholdB2,
       "tlpAtsAlarmCurrentAboveThresholdB3": tlpAtsAlarmCurrentAboveThresholdB3,
       "tlpAtsAlarmLoadsNotAllOn": tlpAtsAlarmLoadsNotAllOn,
       "tlpAtsAlarmGeneralFault": tlpAtsAlarmGeneralFault,
       "tlpAtsAlarmVoltage": tlpAtsAlarmVoltage,
       "tlpAtsAlarmOverVoltage": tlpAtsAlarmOverVoltage,
       "tlpAtsAlarmSource1OverVoltage": tlpAtsAlarmSource1OverVoltage,
       "tlpAtsAlarmSource2OverVoltage": tlpAtsAlarmSource2OverVoltage,
       "tlpAtsAlarmFrequency": tlpAtsAlarmFrequency,
       "tlpAtsAlarmSource1InvalidFrequency": tlpAtsAlarmSource1InvalidFrequency,
       "tlpAtsAlarmSource2InvalidFrequency": tlpAtsAlarmSource2InvalidFrequency,
       "tlpCoolingAlarms": tlpCoolingAlarms,
       "tlpCoolingAlarmSupplyAirSensorFault": tlpCoolingAlarmSupplyAirSensorFault,
       "tlpCoolingAlarmReturnAirSensorFault": tlpCoolingAlarmReturnAirSensorFault,
       "tlpCoolingAlarmCondenserInletAirSensorFault": tlpCoolingAlarmCondenserInletAirSensorFault,
       "tlpCoolingAlarmCondenserOutletAirSensorFault": tlpCoolingAlarmCondenserOutletAirSensorFault,
       "tlpCoolingAlarmSuctionTemperatureSensorFault": tlpCoolingAlarmSuctionTemperatureSensorFault,
       "tlpCoolingAlarmEvaporatorTemperatureSensorFault": tlpCoolingAlarmEvaporatorTemperatureSensorFault,
       "tlpCoolingAlarmAirFilterClogged": tlpCoolingAlarmAirFilterClogged,
       "tlpCoolingAlarmAirFilterRunHoursViolation": tlpCoolingAlarmAirFilterRunHoursViolation,
       "tlpCoolingAlarmSuctionPressureSensorFault": tlpCoolingAlarmSuctionPressureSensorFault,
       "tlpCoolingAlarmInverterCommunicationsFault": tlpCoolingAlarmInverterCommunicationsFault,
       "tlpCoolingAlarmRemoteShutdownViaInputContact": tlpCoolingAlarmRemoteShutdownViaInputContact,
       "tlpCoolingAlarmCondensatePumpFault": tlpCoolingAlarmCondensatePumpFault,
       "tlpCoolingAlarmLowRefrigerantStartupFault": tlpCoolingAlarmLowRefrigerantStartupFault,
       "tlpCoolingAlarmCondenserFanFault": tlpCoolingAlarmCondenserFanFault,
       "tlpCoolingAlarmCondenserFailure": tlpCoolingAlarmCondenserFailure,
       "tlpCoolingAlarmEvaporatorCoolingFailure": tlpCoolingAlarmEvaporatorCoolingFailure,
       "tlpCoolingAlarmReturnAirTempHigh": tlpCoolingAlarmReturnAirTempHigh,
       "tlpCoolingAlarmSupplyAirTempHigh": tlpCoolingAlarmSupplyAirTempHigh,
       "tlpCoolingAlarmEvaporatorFailure": tlpCoolingAlarmEvaporatorFailure,
       "tlpCoolingAlarmEvaporatorFreezeUp": tlpCoolingAlarmEvaporatorFreezeUp,
       "tlpCoolingAlarmDischargePressureHigh": tlpCoolingAlarmDischargePressureHigh,
       "tlpCoolingAlarmPressureGaugeFailure": tlpCoolingAlarmPressureGaugeFailure,
       "tlpCoolingAlarmDischargePressurePersistentHigh": tlpCoolingAlarmDischargePressurePersistentHigh,
       "tlpCoolingAlarmSuctionPressureLowStartFailure": tlpCoolingAlarmSuctionPressureLowStartFailure,
       "tlpCoolingAlarmSuctionPressureLow": tlpCoolingAlarmSuctionPressureLow,
       "tlpCoolingAlarmSuctionPressurePersistentLow": tlpCoolingAlarmSuctionPressurePersistentLow,
       "tlpCoolingAlarmStartupLinePressureImbalance": tlpCoolingAlarmStartupLinePressureImbalance,
       "tlpCoolingAlarmCompressorFailure": tlpCoolingAlarmCompressorFailure,
       "tlpCoolingAlarmCurrentLimit": tlpCoolingAlarmCurrentLimit,
       "tlpCoolingAlarmWaterLeak": tlpCoolingAlarmWaterLeak,
       "tlpCoolingAlarmFanUnderCurrent": tlpCoolingAlarmFanUnderCurrent,
       "tlpCoolingAlarmFanOverCurrent": tlpCoolingAlarmFanOverCurrent,
       "tlpCoolingAlarmDischargePressureSensorFault": tlpCoolingAlarmDischargePressureSensorFault,
       "tlpCoolingAlarmWaterFull": tlpCoolingAlarmWaterFull,
       "tlpCoolingAlarmAutoCoolingOn": tlpCoolingAlarmAutoCoolingOn,
       "tlpCoolingAlarmPowerButtonPressed": tlpCoolingAlarmPowerButtonPressed,
       "tlpCoolingAlarmDisconnectedFromDevice": tlpCoolingAlarmDisconnectedFromDevice,
       "tlpKvmAlarms": tlpKvmAlarms,
       "tlpRackTrackAlarms": tlpRackTrackAlarms,
       "tlpSwitchAlarms": tlpSwitchAlarms,
       "tlpAlarmControl": tlpAlarmControl,
       "tlpAlarmControlTable": tlpAlarmControlTable,
       "tlpAlarmControlEntry": tlpAlarmControlEntry,
       "tlpAlarmControlIndex": tlpAlarmControlIndex,
       "tlpAlarmControlDescr": tlpAlarmControlDescr,
       "tlpAlarmControlDetail": tlpAlarmControlDetail,
       "tlpAlarmControlSeverity": tlpAlarmControlSeverity,
       "tlpNotify": tlpNotify,
       "tlpNotifications": tlpNotifications,
       "tlpNotificationsAlarmEntryAdded": tlpNotificationsAlarmEntryAdded,
       "tlpNotificationsAlarmEntryRemoved": tlpNotificationsAlarmEntryRemoved,
       "tlpNotifySystemStartup": tlpNotifySystemStartup,
       "tlpNotifySystemShutdown": tlpNotifySystemShutdown,
       "tlpNotifySystemUpdate": tlpNotifySystemUpdate}
)
