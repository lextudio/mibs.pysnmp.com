# SNMP MIB module (ASSETMANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASSETMANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:52 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raritan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13742)
)
raritan.setRevisions(
        ("2015-01-05 00:00",
         "2014-09-25 00:00",
         "2014-04-04 00:00",
         "2012-03-29 00:00",
         "2012-03-26 00:00",
         "2012-02-14 00:00",
         "2012-02-10 00:00",
         "2012-02-08 00:00",
         "2012-02-07 00:00",
         "2012-02-03 00:00",
         "2012-01-17 00:00",
         "2012-01-04 00:00",
         "2011-12-08 00:00",
         "2011-11-11 00:00",
         "2011-11-09 00:00",
         "2011-10-25 00:00",
         "2011-10-05 00:00",
         "2011-09-05 00:00",
         "2011-09-01 00:00",
         "2011-08-23 00:00",
         "2011-05-18 00:00",
         "2011-05-04 00:00",
         "2011-04-15 00:00",
         "2011-02-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AssetManagementLEDModeEnumeration(Integer32, TextualConvention):
    status = "current"
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
        *(("fastBlink", 3),
          ("off", 2),
          ("on", 1),
          ("slowBlink", 4))
    )



class AssetManagementLEDOperationModeEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )



class AssetStripStateEnumeration(Integer32, TextualConvention):
    status = "current"
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
        *(("available", 4),
          ("disconnected", 1),
          ("firmwareUpdate", 2),
          ("unsupported", 3))
    )



class AssetStripFirmwareUpdateStateEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("started", 1),
          ("successful", 2))
    )



class RackUnitTypeEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("blade", 2),
          ("none", 30),
          ("single", 1),
          ("unknown", 31))
    )



class RGBCOLOR(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d;"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class RackUnitNumberingModeEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bottomUp", 1),
          ("topDown", 0))
    )



class AssetStripOrientationEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bottomConnector", 1),
          ("topConnector", 0))
    )



class DeviceConfigurationParameterEnumeration(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("assetStripName", 3),
          ("assetStripOrientation", 6),
          ("assetStripRackUnitNumberingMode", 4),
          ("assetStripRackUnitNumberingOffset", 5),
          ("defaultLEDColorConnected", 0),
          ("defaultLEDColorDisconnected", 1),
          ("rackUnitCount", 2))
    )



class AssetStripTypeEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("composite", 1),
          ("simple", 0))
    )



class LogEventTypeEnumeration(Integer32, TextualConvention):
    status = "current"
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
        *(("assetStripStateChange", 3),
          ("assetTagConnected", 1),
          ("assetTagDisconnected", 2),
          ("empty", 0))
    )



# MIB Managed Objects in the order of their OIDs

_AssetManager_ObjectIdentity = ObjectIdentity
assetManager = _AssetManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0)
)
_TrapInformation_ObjectIdentity = ObjectIdentity
trapInformation = _TrapInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0)
)
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_DeviceInetAddressType_Type = InetAddressType
_DeviceInetAddressType_Object = MibScalar
deviceInetAddressType = _DeviceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 2),
    _DeviceInetAddressType_Type()
)
deviceInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInetAddressType.setStatus("current")
_DeviceInetIPAddress_Type = InetAddress
_DeviceInetIPAddress_Object = MibScalar
deviceInetIPAddress = _DeviceInetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 3),
    _DeviceInetIPAddress_Type()
)
deviceInetIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInetIPAddress.setStatus("current")


class _AssetStripNumber_Type(Integer32):
    """Custom type assetStripNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AssetStripNumber_Type.__name__ = "Integer32"
_AssetStripNumber_Object = MibScalar
assetStripNumber = _AssetStripNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 4),
    _AssetStripNumber_Type()
)
assetStripNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    assetStripNumber.setStatus("current")


class _RackUnitNumber_Type(Integer32):
    """Custom type rackUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RackUnitNumber_Type.__name__ = "Integer32"
_RackUnitNumber_Object = MibScalar
rackUnitNumber = _RackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 5),
    _RackUnitNumber_Type()
)
rackUnitNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rackUnitNumber.setStatus("current")
_AssetStripFirmwareUpdateState_Type = AssetStripFirmwareUpdateStateEnumeration
_AssetStripFirmwareUpdateState_Object = MibScalar
assetStripFirmwareUpdateState = _AssetStripFirmwareUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 6),
    _AssetStripFirmwareUpdateState_Type()
)
assetStripFirmwareUpdateState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    assetStripFirmwareUpdateState.setStatus("current")
_DeviceUserName_Type = DisplayString
_DeviceUserName_Object = MibScalar
deviceUserName = _DeviceUserName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 7),
    _DeviceUserName_Type()
)
deviceUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUserName.setStatus("current")
_DeviceChangedParameter_Type = DeviceConfigurationParameterEnumeration
_DeviceChangedParameter_Object = MibScalar
deviceChangedParameter = _DeviceChangedParameter_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 8),
    _DeviceChangedParameter_Type()
)
deviceChangedParameter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceChangedParameter.setStatus("current")
_ChangedParameterNewValue_Type = DisplayString
_ChangedParameterNewValue_Object = MibScalar
changedParameterNewValue = _ChangedParameterNewValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 9),
    _ChangedParameterNewValue_Type()
)
changedParameterNewValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    changedParameterNewValue.setStatus("current")


class _SlotNumber_Type(Integer32):
    """Custom type slotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SlotNumber_Type.__name__ = "Integer32"
_SlotNumber_Object = MibScalar
slotNumber = _SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 10),
    _SlotNumber_Type()
)
slotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slotNumber.setStatus("current")


class _OldNumberOfComponentAssetStrips_Type(Integer32):
    """Custom type oldNumberOfComponentAssetStrips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OldNumberOfComponentAssetStrips_Type.__name__ = "Integer32"
_OldNumberOfComponentAssetStrips_Object = MibScalar
oldNumberOfComponentAssetStrips = _OldNumberOfComponentAssetStrips_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 11),
    _OldNumberOfComponentAssetStrips_Type()
)
oldNumberOfComponentAssetStrips.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oldNumberOfComponentAssetStrips.setStatus("current")
_AgentInetPortNumber_Type = InetPortNumber
_AgentInetPortNumber_Object = MibScalar
agentInetPortNumber = _AgentInetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 0, 12),
    _AgentInetPortNumber_Type()
)
agentInetPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentInetPortNumber.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1)
)


class _AssetStripCount_Type(Integer32):
    """Custom type assetStripCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AssetStripCount_Type.__name__ = "Integer32"
_AssetStripCount_Object = MibScalar
assetStripCount = _AssetStripCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 1),
    _AssetStripCount_Type()
)
assetStripCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assetStripCount.setStatus("current")
_DefaultLEDColorConnected_Type = RGBCOLOR
_DefaultLEDColorConnected_Object = MibScalar
defaultLEDColorConnected = _DefaultLEDColorConnected_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 2),
    _DefaultLEDColorConnected_Type()
)
defaultLEDColorConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultLEDColorConnected.setStatus("deprecated")
_DefaultLEDColorConnectedStr_Type = DisplayString
_DefaultLEDColorConnectedStr_Object = MibScalar
defaultLEDColorConnectedStr = _DefaultLEDColorConnectedStr_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 3),
    _DefaultLEDColorConnectedStr_Type()
)
defaultLEDColorConnectedStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultLEDColorConnectedStr.setStatus("deprecated")
_DefaultLEDColorDisconnected_Type = RGBCOLOR
_DefaultLEDColorDisconnected_Object = MibScalar
defaultLEDColorDisconnected = _DefaultLEDColorDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 4),
    _DefaultLEDColorDisconnected_Type()
)
defaultLEDColorDisconnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultLEDColorDisconnected.setStatus("deprecated")
_DefaultLEDColorDisconnectedStr_Type = DisplayString
_DefaultLEDColorDisconnectedStr_Object = MibScalar
defaultLEDColorDisconnectedStr = _DefaultLEDColorDisconnectedStr_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 5),
    _DefaultLEDColorDisconnectedStr_Type()
)
defaultLEDColorDisconnectedStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultLEDColorDisconnectedStr.setStatus("deprecated")
_AssetStrip_ObjectIdentity = ObjectIdentity
assetStrip = _AssetStrip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6)
)
_AssetStripConfigurationTable_Object = MibTable
assetStripConfigurationTable = _AssetStripConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1)
)
if mibBuilder.loadTexts:
    assetStripConfigurationTable.setStatus("current")
_AssetStripConfigurationEntry_Object = MibTableRow
assetStripConfigurationEntry = _AssetStripConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1)
)
assetStripConfigurationEntry.setIndexNames(
    (0, "ASSETMANAGEMENT-MIB", "assetStripID"),
)
if mibBuilder.loadTexts:
    assetStripConfigurationEntry.setStatus("current")


class _AssetStripID_Type(Integer32):
    """Custom type assetStripID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AssetStripID_Type.__name__ = "Integer32"
_AssetStripID_Object = MibTableColumn
assetStripID = _AssetStripID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 1),
    _AssetStripID_Type()
)
assetStripID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    assetStripID.setStatus("current")


class _RackUnitCount_Type(Integer32):
    """Custom type rackUnitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 64),
    )


_RackUnitCount_Type.__name__ = "Integer32"
_RackUnitCount_Object = MibTableColumn
rackUnitCount = _RackUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 2),
    _RackUnitCount_Type()
)
rackUnitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rackUnitCount.setStatus("current")
_AssetStripState_Type = AssetStripStateEnumeration
_AssetStripState_Object = MibTableColumn
assetStripState = _AssetStripState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 3),
    _AssetStripState_Type()
)
assetStripState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assetStripState.setStatus("current")
_AssetStripName_Type = DisplayString
_AssetStripName_Object = MibTableColumn
assetStripName = _AssetStripName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 4),
    _AssetStripName_Type()
)
assetStripName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assetStripName.setStatus("current")
_RackUnitNumberingMode_Type = RackUnitNumberingModeEnumeration
_RackUnitNumberingMode_Object = MibTableColumn
rackUnitNumberingMode = _RackUnitNumberingMode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 5),
    _RackUnitNumberingMode_Type()
)
rackUnitNumberingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rackUnitNumberingMode.setStatus("current")
_RackUnitNumberingOffset_Type = Integer32
_RackUnitNumberingOffset_Object = MibTableColumn
rackUnitNumberingOffset = _RackUnitNumberingOffset_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 6),
    _RackUnitNumberingOffset_Type()
)
rackUnitNumberingOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rackUnitNumberingOffset.setStatus("current")
_AssetStripOrientation_Type = AssetStripOrientationEnumeration
_AssetStripOrientation_Object = MibTableColumn
assetStripOrientation = _AssetStripOrientation_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 7),
    _AssetStripOrientation_Type()
)
assetStripOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assetStripOrientation.setStatus("current")
_CurrentMainTagCount_Type = Integer32
_CurrentMainTagCount_Object = MibTableColumn
currentMainTagCount = _CurrentMainTagCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 8),
    _CurrentMainTagCount_Type()
)
currentMainTagCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMainTagCount.setStatus("current")
_CurrentBladeTagCount_Type = Integer32
_CurrentBladeTagCount_Object = MibTableColumn
currentBladeTagCount = _CurrentBladeTagCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 9),
    _CurrentBladeTagCount_Type()
)
currentBladeTagCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentBladeTagCount.setStatus("current")
_MaxMainTagCount_Type = Integer32
_MaxMainTagCount_Object = MibTableColumn
maxMainTagCount = _MaxMainTagCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 10),
    _MaxMainTagCount_Type()
)
maxMainTagCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxMainTagCount.setStatus("current")
_MaxBladeTagCount_Type = Integer32
_MaxBladeTagCount_Object = MibTableColumn
maxBladeTagCount = _MaxBladeTagCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 11),
    _MaxBladeTagCount_Type()
)
maxBladeTagCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBladeTagCount.setStatus("current")
_BladeExtensionOverflow_Type = TruthValue
_BladeExtensionOverflow_Object = MibTableColumn
bladeExtensionOverflow = _BladeExtensionOverflow_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 12),
    _BladeExtensionOverflow_Type()
)
bladeExtensionOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeExtensionOverflow.setStatus("current")
_AssetStripType_Type = AssetStripTypeEnumeration
_AssetStripType_Object = MibTableColumn
assetStripType = _AssetStripType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 13),
    _AssetStripType_Type()
)
assetStripType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assetStripType.setStatus("current")


class _NumberOfComponentAssetStrips_Type(Integer32):
    """Custom type numberOfComponentAssetStrips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NumberOfComponentAssetStrips_Type.__name__ = "Integer32"
_NumberOfComponentAssetStrips_Object = MibTableColumn
numberOfComponentAssetStrips = _NumberOfComponentAssetStrips_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 14),
    _NumberOfComponentAssetStrips_Type()
)
numberOfComponentAssetStrips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfComponentAssetStrips.setStatus("current")
_AssetStripDefaultLEDColorConnected_Type = RGBCOLOR
_AssetStripDefaultLEDColorConnected_Object = MibTableColumn
assetStripDefaultLEDColorConnected = _AssetStripDefaultLEDColorConnected_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 15),
    _AssetStripDefaultLEDColorConnected_Type()
)
assetStripDefaultLEDColorConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assetStripDefaultLEDColorConnected.setStatus("current")
_AssetStripDefaultLEDColorConnectedStr_Type = DisplayString
_AssetStripDefaultLEDColorConnectedStr_Object = MibTableColumn
assetStripDefaultLEDColorConnectedStr = _AssetStripDefaultLEDColorConnectedStr_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 16),
    _AssetStripDefaultLEDColorConnectedStr_Type()
)
assetStripDefaultLEDColorConnectedStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assetStripDefaultLEDColorConnectedStr.setStatus("current")
_AssetStripDefaultLEDColorDisconnected_Type = RGBCOLOR
_AssetStripDefaultLEDColorDisconnected_Object = MibTableColumn
assetStripDefaultLEDColorDisconnected = _AssetStripDefaultLEDColorDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 17),
    _AssetStripDefaultLEDColorDisconnected_Type()
)
assetStripDefaultLEDColorDisconnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assetStripDefaultLEDColorDisconnected.setStatus("current")
_AssetStripDefaultLEDColorDisconnectedStr_Type = DisplayString
_AssetStripDefaultLEDColorDisconnectedStr_Object = MibTableColumn
assetStripDefaultLEDColorDisconnectedStr = _AssetStripDefaultLEDColorDisconnectedStr_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 6, 1, 1, 18),
    _AssetStripDefaultLEDColorDisconnectedStr_Type()
)
assetStripDefaultLEDColorDisconnectedStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assetStripDefaultLEDColorDisconnectedStr.setStatus("current")
_AssetManagement_ObjectIdentity = ObjectIdentity
assetManagement = _AssetManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7)
)
_AssetManagementTable_Object = MibTable
assetManagementTable = _AssetManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1)
)
if mibBuilder.loadTexts:
    assetManagementTable.setStatus("current")
_AssetManagementEntry_Object = MibTableRow
assetManagementEntry = _AssetManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1)
)
assetManagementEntry.setIndexNames(
    (0, "ASSETMANAGEMENT-MIB", "assetStripID"),
    (0, "ASSETMANAGEMENT-MIB", "rackUnitID"),
)
if mibBuilder.loadTexts:
    assetManagementEntry.setStatus("current")


class _RackUnitID_Type(Integer32):
    """Custom type rackUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RackUnitID_Type.__name__ = "Integer32"
_RackUnitID_Object = MibTableColumn
rackUnitID = _RackUnitID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 1),
    _RackUnitID_Type()
)
rackUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rackUnitID.setStatus("current")
_LedOperationMode_Type = AssetManagementLEDOperationModeEnumeration
_LedOperationMode_Object = MibTableColumn
ledOperationMode = _LedOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 2),
    _LedOperationMode_Type()
)
ledOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledOperationMode.setStatus("current")
_LedMode_Type = AssetManagementLEDModeEnumeration
_LedMode_Object = MibTableColumn
ledMode = _LedMode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 3),
    _LedMode_Type()
)
ledMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledMode.setStatus("current")
_LedColor_Type = RGBCOLOR
_LedColor_Object = MibTableColumn
ledColor = _LedColor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 4),
    _LedColor_Type()
)
ledColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledColor.setStatus("current")
_LedColorStr_Type = DisplayString
_LedColorStr_Object = MibTableColumn
ledColorStr = _LedColorStr_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 5),
    _LedColorStr_Type()
)
ledColorStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ledColorStr.setStatus("current")
_TagID_Type = DisplayString
_TagID_Object = MibTableColumn
tagID = _TagID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 6),
    _TagID_Type()
)
tagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tagID.setStatus("current")
_TagFamily_Type = DisplayString
_TagFamily_Object = MibTableColumn
tagFamily = _TagFamily_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 7),
    _TagFamily_Type()
)
tagFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tagFamily.setStatus("current")


class _RackUnitPosition_Type(Integer32):
    """Custom type rackUnitPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RackUnitPosition_Type.__name__ = "Integer32"
_RackUnitPosition_Object = MibTableColumn
rackUnitPosition = _RackUnitPosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 8),
    _RackUnitPosition_Type()
)
rackUnitPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackUnitPosition.setStatus("current")
_RackUnitType_Type = RackUnitTypeEnumeration
_RackUnitType_Object = MibTableColumn
rackUnitType = _RackUnitType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 9),
    _RackUnitType_Type()
)
rackUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackUnitType.setStatus("current")


class _BladeExtensionSize_Type(Integer32):
    """Custom type bladeExtensionSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BladeExtensionSize_Type.__name__ = "Integer32"
_BladeExtensionSize_Object = MibTableColumn
bladeExtensionSize = _BladeExtensionSize_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 10),
    _BladeExtensionSize_Type()
)
bladeExtensionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeExtensionSize.setStatus("current")
_RackUnitName_Type = DisplayString
_RackUnitName_Object = MibTableColumn
rackUnitName = _RackUnitName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 12),
    _RackUnitName_Type()
)
rackUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rackUnitName.setStatus("current")


class _AssetStripCascadePosition_Type(Integer32):
    """Custom type assetStripCascadePosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AssetStripCascadePosition_Type.__name__ = "Integer32"
_AssetStripCascadePosition_Object = MibTableColumn
assetStripCascadePosition = _AssetStripCascadePosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 13),
    _AssetStripCascadePosition_Type()
)
assetStripCascadePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assetStripCascadePosition.setStatus("current")


class _RackUnitRelativePosition_Type(Integer32):
    """Custom type rackUnitRelativePosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_RackUnitRelativePosition_Type.__name__ = "Integer32"
_RackUnitRelativePosition_Object = MibTableColumn
rackUnitRelativePosition = _RackUnitRelativePosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 14),
    _RackUnitRelativePosition_Type()
)
rackUnitRelativePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackUnitRelativePosition.setStatus("current")


class _AssetStripNumberOfRackUnits_Type(Integer32):
    """Custom type assetStripNumberOfRackUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AssetStripNumberOfRackUnits_Type.__name__ = "Integer32"
_AssetStripNumberOfRackUnits_Object = MibTableColumn
assetStripNumberOfRackUnits = _AssetStripNumberOfRackUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 1, 1, 15),
    _AssetStripNumberOfRackUnits_Type()
)
assetStripNumberOfRackUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assetStripNumberOfRackUnits.setStatus("current")
_BladeExtensionTable_Object = MibTable
bladeExtensionTable = _BladeExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 2)
)
if mibBuilder.loadTexts:
    bladeExtensionTable.setStatus("current")
_BladeExtensionEntry_Object = MibTableRow
bladeExtensionEntry = _BladeExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 2, 1)
)
bladeExtensionEntry.setIndexNames(
    (0, "ASSETMANAGEMENT-MIB", "assetStripID"),
    (0, "ASSETMANAGEMENT-MIB", "rackUnitID"),
    (0, "ASSETMANAGEMENT-MIB", "bladeSlotID"),
)
if mibBuilder.loadTexts:
    bladeExtensionEntry.setStatus("current")


class _BladeSlotID_Type(Integer32):
    """Custom type bladeSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BladeSlotID_Type.__name__ = "Integer32"
_BladeSlotID_Object = MibTableColumn
bladeSlotID = _BladeSlotID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 2, 1, 1),
    _BladeSlotID_Type()
)
bladeSlotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bladeSlotID.setStatus("current")
_BladeTagID_Type = DisplayString
_BladeTagID_Object = MibTableColumn
bladeTagID = _BladeTagID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 2, 1, 2),
    _BladeTagID_Type()
)
bladeTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeTagID.setStatus("current")


class _BladeSlotPosition_Type(Integer32):
    """Custom type bladeSlotPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BladeSlotPosition_Type.__name__ = "Integer32"
_BladeSlotPosition_Object = MibTableColumn
bladeSlotPosition = _BladeSlotPosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 1, 7, 2, 1, 3),
    _BladeSlotPosition_Type()
)
bladeSlotPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSlotPosition.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 2)
)
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3)
)
_LogConfiguration_ObjectIdentity = ObjectIdentity
logConfiguration = _LogConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 1)
)
_LogSize_Type = Integer32
_LogSize_Object = MibScalar
logSize = _LogSize_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 1, 1),
    _LogSize_Type()
)
logSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSize.setStatus("current")
_OldestLogID_Type = Integer32
_OldestLogID_Object = MibScalar
oldestLogID = _OldestLogID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 1, 2),
    _OldestLogID_Type()
)
oldestLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oldestLogID.setStatus("current")
_NewestLogID_Type = Integer32
_NewestLogID_Object = MibScalar
newestLogID = _NewestLogID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 1, 3),
    _NewestLogID_Type()
)
newestLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newestLogID.setStatus("current")
_LogEventCount_Type = Integer32
_LogEventCount_Object = MibScalar
logEventCount = _LogEventCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 1, 4),
    _LogEventCount_Type()
)
logEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventCount.setStatus("current")
_AssetManagementLogTable_Object = MibTable
assetManagementLogTable = _AssetManagementLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2)
)
if mibBuilder.loadTexts:
    assetManagementLogTable.setStatus("current")
_AssetManagementLogEntry_Object = MibTableRow
assetManagementLogEntry = _AssetManagementLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1)
)
assetManagementLogEntry.setIndexNames(
    (0, "ASSETMANAGEMENT-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    assetManagementLogEntry.setStatus("current")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")
_LogTimeStamp_Type = Unsigned32
_LogTimeStamp_Object = MibTableColumn
logTimeStamp = _LogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 2),
    _LogTimeStamp_Type()
)
logTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTimeStamp.setStatus("current")
_LogEventType_Type = LogEventTypeEnumeration
_LogEventType_Object = MibTableColumn
logEventType = _LogEventType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 3),
    _LogEventType_Type()
)
logEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventType.setStatus("current")


class _LogAssetStripNumber_Type(Integer32):
    """Custom type logAssetStripNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_LogAssetStripNumber_Type.__name__ = "Integer32"
_LogAssetStripNumber_Object = MibTableColumn
logAssetStripNumber = _LogAssetStripNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 4),
    _LogAssetStripNumber_Type()
)
logAssetStripNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAssetStripNumber.setStatus("current")


class _LogRackUnitNumber_Type(Integer32):
    """Custom type logRackUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_LogRackUnitNumber_Type.__name__ = "Integer32"
_LogRackUnitNumber_Object = MibTableColumn
logRackUnitNumber = _LogRackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 5),
    _LogRackUnitNumber_Type()
)
logRackUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRackUnitNumber.setStatus("current")


class _LogRackUnitPosition_Type(Integer32):
    """Custom type logRackUnitPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_LogRackUnitPosition_Type.__name__ = "Integer32"
_LogRackUnitPosition_Object = MibTableColumn
logRackUnitPosition = _LogRackUnitPosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 6),
    _LogRackUnitPosition_Type()
)
logRackUnitPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRackUnitPosition.setStatus("current")


class _LogSlotNumber_Type(Integer32):
    """Custom type logSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_LogSlotNumber_Type.__name__ = "Integer32"
_LogSlotNumber_Object = MibTableColumn
logSlotNumber = _LogSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 7),
    _LogSlotNumber_Type()
)
logSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSlotNumber.setStatus("current")
_LogTagID_Type = DisplayString
_LogTagID_Object = MibTableColumn
logTagID = _LogTagID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 8),
    _LogTagID_Type()
)
logTagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTagID.setStatus("current")
_LogAssetStripState_Type = AssetStripStateEnumeration
_LogAssetStripState_Object = MibTableColumn
logAssetStripState = _LogAssetStripState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 9),
    _LogAssetStripState_Type()
)
logAssetStripState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAssetStripState.setStatus("current")
_LogParentBladeID_Type = DisplayString
_LogParentBladeID_Object = MibTableColumn
logParentBladeID = _LogParentBladeID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 7, 3, 2, 1, 10),
    _LogParentBladeID_Type()
)
logParentBladeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logParentBladeID.setStatus("current")

# Managed Objects groups

configGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 2, 1)
)
configGroup.setObjects(
      *(("ASSETMANAGEMENT-MIB", "defaultLEDColorConnected"),
        ("ASSETMANAGEMENT-MIB", "defaultLEDColorConnectedStr"),
        ("ASSETMANAGEMENT-MIB", "defaultLEDColorDisconnected"),
        ("ASSETMANAGEMENT-MIB", "defaultLEDColorDisconnectedStr"))
)
if mibBuilder.loadTexts:
    configGroup.setStatus("deprecated")

assetManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 2, 2)
)
assetManagementGroup.setObjects(
      *(("ASSETMANAGEMENT-MIB", "ledOperationMode"),
        ("ASSETMANAGEMENT-MIB", "ledMode"),
        ("ASSETMANAGEMENT-MIB", "ledColor"),
        ("ASSETMANAGEMENT-MIB", "ledColorStr"),
        ("ASSETMANAGEMENT-MIB", "tagID"),
        ("ASSETMANAGEMENT-MIB", "bladeTagID"),
        ("ASSETMANAGEMENT-MIB", "tagFamily"),
        ("ASSETMANAGEMENT-MIB", "rackUnitPosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitType"),
        ("ASSETMANAGEMENT-MIB", "bladeExtensionSize"),
        ("ASSETMANAGEMENT-MIB", "bladeSlotPosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitName"),
        ("ASSETMANAGEMENT-MIB", "assetStripCascadePosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitRelativePosition"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumberOfRackUnits"))
)
if mibBuilder.loadTexts:
    assetManagementGroup.setStatus("current")

trapInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 2, 4)
)
trapInformationGroup.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "rackUnitNumber"),
        ("ASSETMANAGEMENT-MIB", "slotNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripFirmwareUpdateState"),
        ("ASSETMANAGEMENT-MIB", "deviceUserName"),
        ("ASSETMANAGEMENT-MIB", "deviceChangedParameter"),
        ("ASSETMANAGEMENT-MIB", "changedParameterNewValue"),
        ("ASSETMANAGEMENT-MIB", "oldNumberOfComponentAssetStrips"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"))
)
if mibBuilder.loadTexts:
    trapInformationGroup.setStatus("current")

configGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 2, 5)
)
configGroup2.setObjects(
      *(("ASSETMANAGEMENT-MIB", "assetStripCount"),
        ("ASSETMANAGEMENT-MIB", "assetStripState"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "rackUnitCount"),
        ("ASSETMANAGEMENT-MIB", "rackUnitNumberingMode"),
        ("ASSETMANAGEMENT-MIB", "rackUnitNumberingOffset"),
        ("ASSETMANAGEMENT-MIB", "assetStripOrientation"),
        ("ASSETMANAGEMENT-MIB", "currentMainTagCount"),
        ("ASSETMANAGEMENT-MIB", "currentBladeTagCount"),
        ("ASSETMANAGEMENT-MIB", "maxMainTagCount"),
        ("ASSETMANAGEMENT-MIB", "maxBladeTagCount"),
        ("ASSETMANAGEMENT-MIB", "bladeExtensionOverflow"),
        ("ASSETMANAGEMENT-MIB", "assetStripType"),
        ("ASSETMANAGEMENT-MIB", "numberOfComponentAssetStrips"),
        ("ASSETMANAGEMENT-MIB", "assetStripDefaultLEDColorConnected"),
        ("ASSETMANAGEMENT-MIB", "assetStripDefaultLEDColorConnectedStr"),
        ("ASSETMANAGEMENT-MIB", "assetStripDefaultLEDColorDisconnected"),
        ("ASSETMANAGEMENT-MIB", "assetStripDefaultLEDColorDisconnectedStr"))
)
if mibBuilder.loadTexts:
    configGroup2.setStatus("current")

logGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 2, 6)
)
logGroup.setObjects(
      *(("ASSETMANAGEMENT-MIB", "logSize"),
        ("ASSETMANAGEMENT-MIB", "oldestLogID"),
        ("ASSETMANAGEMENT-MIB", "newestLogID"),
        ("ASSETMANAGEMENT-MIB", "logEventCount"),
        ("ASSETMANAGEMENT-MIB", "logTimeStamp"),
        ("ASSETMANAGEMENT-MIB", "logEventType"),
        ("ASSETMANAGEMENT-MIB", "logAssetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "logRackUnitNumber"),
        ("ASSETMANAGEMENT-MIB", "logRackUnitPosition"),
        ("ASSETMANAGEMENT-MIB", "logSlotNumber"),
        ("ASSETMANAGEMENT-MIB", "logTagID"),
        ("ASSETMANAGEMENT-MIB", "logAssetStripState"),
        ("ASSETMANAGEMENT-MIB", "logParentBladeID"))
)
if mibBuilder.loadTexts:
    logGroup.setStatus("current")


# Notification objects

assetTagConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 1)
)
assetTagConnected.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "rackUnitNumber"),
        ("ASSETMANAGEMENT-MIB", "rackUnitPosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitName"),
        ("ASSETMANAGEMENT-MIB", "slotNumber"),
        ("ASSETMANAGEMENT-MIB", "tagID"),
        ("ASSETMANAGEMENT-MIB", "bladeTagID"),
        ("ASSETMANAGEMENT-MIB", "ledColor"),
        ("ASSETMANAGEMENT-MIB", "ledMode"),
        ("ASSETMANAGEMENT-MIB", "ledOperationMode"),
        ("ASSETMANAGEMENT-MIB", "rackUnitCount"),
        ("ASSETMANAGEMENT-MIB", "assetStripType"),
        ("ASSETMANAGEMENT-MIB", "assetStripCascadePosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitRelativePosition"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumberOfRackUnits"))
)
if mibBuilder.loadTexts:
    assetTagConnected.setStatus(
        "current"
    )

assetTagDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 2)
)
assetTagDisconnected.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "rackUnitNumber"),
        ("ASSETMANAGEMENT-MIB", "rackUnitPosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitName"),
        ("ASSETMANAGEMENT-MIB", "slotNumber"),
        ("ASSETMANAGEMENT-MIB", "tagID"),
        ("ASSETMANAGEMENT-MIB", "bladeTagID"),
        ("ASSETMANAGEMENT-MIB", "ledColor"),
        ("ASSETMANAGEMENT-MIB", "ledMode"),
        ("ASSETMANAGEMENT-MIB", "ledOperationMode"),
        ("ASSETMANAGEMENT-MIB", "rackUnitCount"),
        ("ASSETMANAGEMENT-MIB", "assetStripType"),
        ("ASSETMANAGEMENT-MIB", "assetStripCascadePosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitRelativePosition"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumberOfRackUnits"))
)
if mibBuilder.loadTexts:
    assetTagDisconnected.setStatus(
        "current"
    )

assetStripStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 3)
)
assetStripStateChange.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "assetStripState"),
        ("ASSETMANAGEMENT-MIB", "rackUnitCount"))
)
if mibBuilder.loadTexts:
    assetStripStateChange.setStatus(
        "current"
    )

assetStripFirmwareUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 4)
)
assetStripFirmwareUpdate.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "assetStripFirmwareUpdateState"))
)
if mibBuilder.loadTexts:
    assetStripFirmwareUpdate.setStatus(
        "current"
    )

deviceConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 5)
)
deviceConfigurationChanged.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "deviceUserName"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "deviceChangedParameter"),
        ("ASSETMANAGEMENT-MIB", "changedParameterNewValue"))
)
if mibBuilder.loadTexts:
    deviceConfigurationChanged.setStatus(
        "current"
    )

rackUnitConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 6)
)
rackUnitConfigurationChanged.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "deviceUserName"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "rackUnitNumber"),
        ("ASSETMANAGEMENT-MIB", "rackUnitPosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitName"),
        ("ASSETMANAGEMENT-MIB", "ledColor"),
        ("ASSETMANAGEMENT-MIB", "ledMode"),
        ("ASSETMANAGEMENT-MIB", "ledOperationMode"))
)
if mibBuilder.loadTexts:
    rackUnitConfigurationChanged.setStatus(
        "current"
    )

bladeExtensionConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 7)
)
bladeExtensionConnected.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "rackUnitNumber"),
        ("ASSETMANAGEMENT-MIB", "rackUnitPosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitName"),
        ("ASSETMANAGEMENT-MIB", "tagID"),
        ("ASSETMANAGEMENT-MIB", "bladeExtensionSize"),
        ("ASSETMANAGEMENT-MIB", "ledColor"),
        ("ASSETMANAGEMENT-MIB", "ledMode"),
        ("ASSETMANAGEMENT-MIB", "ledOperationMode"),
        ("ASSETMANAGEMENT-MIB", "rackUnitCount"),
        ("ASSETMANAGEMENT-MIB", "assetStripType"),
        ("ASSETMANAGEMENT-MIB", "assetStripCascadePosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitRelativePosition"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumberOfRackUnits"))
)
if mibBuilder.loadTexts:
    bladeExtensionConnected.setStatus(
        "current"
    )

bladeExtensionDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 8)
)
bladeExtensionDisconnected.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "rackUnitNumber"),
        ("ASSETMANAGEMENT-MIB", "rackUnitPosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitName"),
        ("ASSETMANAGEMENT-MIB", "tagID"),
        ("ASSETMANAGEMENT-MIB", "bladeExtensionSize"),
        ("ASSETMANAGEMENT-MIB", "ledColor"),
        ("ASSETMANAGEMENT-MIB", "ledMode"),
        ("ASSETMANAGEMENT-MIB", "ledOperationMode"),
        ("ASSETMANAGEMENT-MIB", "rackUnitCount"),
        ("ASSETMANAGEMENT-MIB", "assetStripType"),
        ("ASSETMANAGEMENT-MIB", "assetStripCascadePosition"),
        ("ASSETMANAGEMENT-MIB", "rackUnitRelativePosition"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumberOfRackUnits"))
)
if mibBuilder.loadTexts:
    bladeExtensionDisconnected.setStatus(
        "current"
    )

bladeExtensionOverflowOccured = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 9)
)
bladeExtensionOverflowOccured.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"))
)
if mibBuilder.loadTexts:
    bladeExtensionOverflowOccured.setStatus(
        "current"
    )

bladeExtensionOverflowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 10)
)
bladeExtensionOverflowCleared.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"))
)
if mibBuilder.loadTexts:
    bladeExtensionOverflowCleared.setStatus(
        "current"
    )

compositeAssetStripCompositionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 7, 0, 11)
)
compositeAssetStripCompositionChanged.setObjects(
      *(("ASSETMANAGEMENT-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("ASSETMANAGEMENT-MIB", "deviceInetAddressType"),
        ("ASSETMANAGEMENT-MIB", "deviceInetIPAddress"),
        ("ASSETMANAGEMENT-MIB", "agentInetPortNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripNumber"),
        ("ASSETMANAGEMENT-MIB", "assetStripName"),
        ("ASSETMANAGEMENT-MIB", "oldNumberOfComponentAssetStrips"),
        ("ASSETMANAGEMENT-MIB", "numberOfComponentAssetStrips"))
)
if mibBuilder.loadTexts:
    compositeAssetStripCompositionChanged.setStatus(
        "current"
    )


# Notifications groups

trapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 2, 3)
)
trapsGroup.setObjects(
      *(("ASSETMANAGEMENT-MIB", "assetStripStateChange"),
        ("ASSETMANAGEMENT-MIB", "assetTagConnected"),
        ("ASSETMANAGEMENT-MIB", "assetTagDisconnected"),
        ("ASSETMANAGEMENT-MIB", "assetStripFirmwareUpdate"),
        ("ASSETMANAGEMENT-MIB", "deviceConfigurationChanged"),
        ("ASSETMANAGEMENT-MIB", "rackUnitConfigurationChanged"),
        ("ASSETMANAGEMENT-MIB", "bladeExtensionConnected"),
        ("ASSETMANAGEMENT-MIB", "bladeExtensionDisconnected"),
        ("ASSETMANAGEMENT-MIB", "bladeExtensionOverflowOccured"),
        ("ASSETMANAGEMENT-MIB", "bladeExtensionOverflowCleared"),
        ("ASSETMANAGEMENT-MIB", "compositeAssetStripCompositionChanged"))
)
if mibBuilder.loadTexts:
    trapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

complianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    complianceRev1.setStatus(
        "deprecated"
    )

complianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    complianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASSETMANAGEMENT-MIB",
    **{"AssetManagementLEDModeEnumeration": AssetManagementLEDModeEnumeration,
       "AssetManagementLEDOperationModeEnumeration": AssetManagementLEDOperationModeEnumeration,
       "AssetStripStateEnumeration": AssetStripStateEnumeration,
       "AssetStripFirmwareUpdateStateEnumeration": AssetStripFirmwareUpdateStateEnumeration,
       "RackUnitTypeEnumeration": RackUnitTypeEnumeration,
       "RGBCOLOR": RGBCOLOR,
       "RackUnitNumberingModeEnumeration": RackUnitNumberingModeEnumeration,
       "AssetStripOrientationEnumeration": AssetStripOrientationEnumeration,
       "DeviceConfigurationParameterEnumeration": DeviceConfigurationParameterEnumeration,
       "AssetStripTypeEnumeration": AssetStripTypeEnumeration,
       "LogEventTypeEnumeration": LogEventTypeEnumeration,
       "raritan": raritan,
       "assetManager": assetManager,
       "traps": traps,
       "trapInformation": trapInformation,
       "deviceName": deviceName,
       "deviceInetAddressType": deviceInetAddressType,
       "deviceInetIPAddress": deviceInetIPAddress,
       "assetStripNumber": assetStripNumber,
       "rackUnitNumber": rackUnitNumber,
       "assetStripFirmwareUpdateState": assetStripFirmwareUpdateState,
       "deviceUserName": deviceUserName,
       "deviceChangedParameter": deviceChangedParameter,
       "changedParameterNewValue": changedParameterNewValue,
       "slotNumber": slotNumber,
       "oldNumberOfComponentAssetStrips": oldNumberOfComponentAssetStrips,
       "agentInetPortNumber": agentInetPortNumber,
       "assetTagConnected": assetTagConnected,
       "assetTagDisconnected": assetTagDisconnected,
       "assetStripStateChange": assetStripStateChange,
       "assetStripFirmwareUpdate": assetStripFirmwareUpdate,
       "deviceConfigurationChanged": deviceConfigurationChanged,
       "rackUnitConfigurationChanged": rackUnitConfigurationChanged,
       "bladeExtensionConnected": bladeExtensionConnected,
       "bladeExtensionDisconnected": bladeExtensionDisconnected,
       "bladeExtensionOverflowOccured": bladeExtensionOverflowOccured,
       "bladeExtensionOverflowCleared": bladeExtensionOverflowCleared,
       "compositeAssetStripCompositionChanged": compositeAssetStripCompositionChanged,
       "configuration": configuration,
       "assetStripCount": assetStripCount,
       "defaultLEDColorConnected": defaultLEDColorConnected,
       "defaultLEDColorConnectedStr": defaultLEDColorConnectedStr,
       "defaultLEDColorDisconnected": defaultLEDColorDisconnected,
       "defaultLEDColorDisconnectedStr": defaultLEDColorDisconnectedStr,
       "assetStrip": assetStrip,
       "assetStripConfigurationTable": assetStripConfigurationTable,
       "assetStripConfigurationEntry": assetStripConfigurationEntry,
       "assetStripID": assetStripID,
       "rackUnitCount": rackUnitCount,
       "assetStripState": assetStripState,
       "assetStripName": assetStripName,
       "rackUnitNumberingMode": rackUnitNumberingMode,
       "rackUnitNumberingOffset": rackUnitNumberingOffset,
       "assetStripOrientation": assetStripOrientation,
       "currentMainTagCount": currentMainTagCount,
       "currentBladeTagCount": currentBladeTagCount,
       "maxMainTagCount": maxMainTagCount,
       "maxBladeTagCount": maxBladeTagCount,
       "bladeExtensionOverflow": bladeExtensionOverflow,
       "assetStripType": assetStripType,
       "numberOfComponentAssetStrips": numberOfComponentAssetStrips,
       "assetStripDefaultLEDColorConnected": assetStripDefaultLEDColorConnected,
       "assetStripDefaultLEDColorConnectedStr": assetStripDefaultLEDColorConnectedStr,
       "assetStripDefaultLEDColorDisconnected": assetStripDefaultLEDColorDisconnected,
       "assetStripDefaultLEDColorDisconnectedStr": assetStripDefaultLEDColorDisconnectedStr,
       "assetManagement": assetManagement,
       "assetManagementTable": assetManagementTable,
       "assetManagementEntry": assetManagementEntry,
       "rackUnitID": rackUnitID,
       "ledOperationMode": ledOperationMode,
       "ledMode": ledMode,
       "ledColor": ledColor,
       "ledColorStr": ledColorStr,
       "tagID": tagID,
       "tagFamily": tagFamily,
       "rackUnitPosition": rackUnitPosition,
       "rackUnitType": rackUnitType,
       "bladeExtensionSize": bladeExtensionSize,
       "rackUnitName": rackUnitName,
       "assetStripCascadePosition": assetStripCascadePosition,
       "rackUnitRelativePosition": rackUnitRelativePosition,
       "assetStripNumberOfRackUnits": assetStripNumberOfRackUnits,
       "bladeExtensionTable": bladeExtensionTable,
       "bladeExtensionEntry": bladeExtensionEntry,
       "bladeSlotID": bladeSlotID,
       "bladeTagID": bladeTagID,
       "bladeSlotPosition": bladeSlotPosition,
       "conformance": conformance,
       "compliances": compliances,
       "complianceRev1": complianceRev1,
       "complianceRev2": complianceRev2,
       "groups": groups,
       "configGroup": configGroup,
       "assetManagementGroup": assetManagementGroup,
       "trapsGroup": trapsGroup,
       "trapInformationGroup": trapInformationGroup,
       "configGroup2": configGroup2,
       "logGroup": logGroup,
       "log": log,
       "logConfiguration": logConfiguration,
       "logSize": logSize,
       "oldestLogID": oldestLogID,
       "newestLogID": newestLogID,
       "logEventCount": logEventCount,
       "assetManagementLogTable": assetManagementLogTable,
       "assetManagementLogEntry": assetManagementLogEntry,
       "logIndex": logIndex,
       "logTimeStamp": logTimeStamp,
       "logEventType": logEventType,
       "logAssetStripNumber": logAssetStripNumber,
       "logRackUnitNumber": logRackUnitNumber,
       "logRackUnitPosition": logRackUnitPosition,
       "logSlotNumber": logSlotNumber,
       "logTagID": logTagID,
       "logAssetStripState": logAssetStripState,
       "logParentBladeID": logParentBladeID}
)
