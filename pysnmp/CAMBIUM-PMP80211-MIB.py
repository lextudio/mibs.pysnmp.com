# SNMP MIB module (CAMBIUM-PMP80211-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAMBIUM-PMP80211-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:26 2024
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

pmpMibTree = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21)
)
pmpMibTree.setRevisions(
        ("2013-04-26 12:38",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cambium_ObjectIdentity = ObjectIdentity
cambium = _Cambium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713)
)
_Cambiumpmp80211SystemTraps_ObjectIdentity = ObjectIdentity
cambiumpmp80211SystemTraps = _Cambiumpmp80211SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0)
)
_CambiumPmp80211SystemStatus_ObjectIdentity = ObjectIdentity
cambiumPmp80211SystemStatus = _CambiumPmp80211SystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1)
)
_CambiumGeneralStatus_ObjectIdentity = ObjectIdentity
cambiumGeneralStatus = _CambiumGeneralStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1)
)


class _CambiumCurrentSWInfo_Type(DisplayString):
    """Custom type cambiumCurrentSWInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumCurrentSWInfo_Type.__name__ = "DisplayString"
_CambiumCurrentSWInfo_Object = MibScalar
cambiumCurrentSWInfo = _CambiumCurrentSWInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 1),
    _CambiumCurrentSWInfo_Type()
)
cambiumCurrentSWInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCurrentSWInfo.setStatus("current")


class _CambiumHWInfo_Type(Integer32):
    """Custom type cambiumHWInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(12, 12),
    )


_CambiumHWInfo_Type.__name__ = "Integer32"
_CambiumHWInfo_Object = MibScalar
cambiumHWInfo = _CambiumHWInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 2),
    _CambiumHWInfo_Type()
)
cambiumHWInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumHWInfo.setStatus("current")


class _CambiumDateTime_Type(DisplayString):
    """Custom type cambiumDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumDateTime_Type.__name__ = "DisplayString"
_CambiumDateTime_Object = MibScalar
cambiumDateTime = _CambiumDateTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 3),
    _CambiumDateTime_Type()
)
cambiumDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDateTime.setStatus("current")


class _CambiumSystemUptime_Type(DisplayString):
    """Custom type cambiumSystemUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumSystemUptime_Type.__name__ = "DisplayString"
_CambiumSystemUptime_Object = MibScalar
cambiumSystemUptime = _CambiumSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 4),
    _CambiumSystemUptime_Type()
)
cambiumSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSystemUptime.setStatus("current")


class _CambiumWirelessMACAddress_Type(DisplayString):
    """Custom type cambiumWirelessMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumWirelessMACAddress_Type.__name__ = "DisplayString"
_CambiumWirelessMACAddress_Object = MibScalar
cambiumWirelessMACAddress = _CambiumWirelessMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 5),
    _CambiumWirelessMACAddress_Type()
)
cambiumWirelessMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWirelessMACAddress.setStatus("current")


class _CambiumDFSStatus_Type(Integer32):
    """Custom type cambiumDFSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CambiumDFSStatus_Type.__name__ = "Integer32"
_CambiumDFSStatus_Object = MibScalar
cambiumDFSStatus = _CambiumDFSStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 6),
    _CambiumDFSStatus_Type()
)
cambiumDFSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDFSStatus.setStatus("current")


class _CambiumEffectiveSyncSource_Type(Integer32):
    """Custom type cambiumEffectiveSyncSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
    )


_CambiumEffectiveSyncSource_Type.__name__ = "Integer32"
_CambiumEffectiveSyncSource_Object = MibScalar
cambiumEffectiveSyncSource = _CambiumEffectiveSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 7),
    _CambiumEffectiveSyncSource_Type()
)
cambiumEffectiveSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveSyncSource.setStatus("current")


class _CambiumEffectiveCountryCode_Type(DisplayString):
    """Custom type cambiumEffectiveCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CambiumEffectiveCountryCode_Type.__name__ = "DisplayString"
_CambiumEffectiveCountryCode_Object = MibScalar
cambiumEffectiveCountryCode = _CambiumEffectiveCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 8),
    _CambiumEffectiveCountryCode_Type()
)
cambiumEffectiveCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveCountryCode.setStatus("current")


class _CambiumEffectiveAntennaGain_Type(Integer32):
    """Custom type cambiumEffectiveAntennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CambiumEffectiveAntennaGain_Type.__name__ = "Integer32"
_CambiumEffectiveAntennaGain_Object = MibScalar
cambiumEffectiveAntennaGain = _CambiumEffectiveAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 9),
    _CambiumEffectiveAntennaGain_Type()
)
cambiumEffectiveAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveAntennaGain.setStatus("current")


class _CambiumEffectiveTDDRatio_Type(Integer32):
    """Custom type cambiumEffectiveTDDRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CambiumEffectiveTDDRatio_Type.__name__ = "Integer32"
_CambiumEffectiveTDDRatio_Object = MibScalar
cambiumEffectiveTDDRatio = _CambiumEffectiveTDDRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 10),
    _CambiumEffectiveTDDRatio_Type()
)
cambiumEffectiveTDDRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveTDDRatio.setStatus("current")


class _CambiumEffectiveSSID_Type(DisplayString):
    """Custom type cambiumEffectiveSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumEffectiveSSID_Type.__name__ = "DisplayString"
_CambiumEffectiveSSID_Object = MibScalar
cambiumEffectiveSSID = _CambiumEffectiveSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 11),
    _CambiumEffectiveSSID_Type()
)
cambiumEffectiveSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveSSID.setStatus("current")


class _CambiumEffectiveAuthenticationType_Type(Integer32):
    """Custom type cambiumEffectiveAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_CambiumEffectiveAuthenticationType_Type.__name__ = "Integer32"
_CambiumEffectiveAuthenticationType_Object = MibScalar
cambiumEffectiveAuthenticationType = _CambiumEffectiveAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 12),
    _CambiumEffectiveAuthenticationType_Type()
)
cambiumEffectiveAuthenticationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveAuthenticationType.setStatus("current")


class _CambiumEffectiveDeviceName_Type(DisplayString):
    """Custom type cambiumEffectiveDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumEffectiveDeviceName_Type.__name__ = "DisplayString"
_CambiumEffectiveDeviceName_Object = MibScalar
cambiumEffectiveDeviceName = _CambiumEffectiveDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 13),
    _CambiumEffectiveDeviceName_Type()
)
cambiumEffectiveDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceName.setStatus("current")


class _CambiumUbootVersion_Type(DisplayString):
    """Custom type cambiumUbootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumUbootVersion_Type.__name__ = "DisplayString"
_CambiumUbootVersion_Object = MibScalar
cambiumUbootVersion = _CambiumUbootVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 14),
    _CambiumUbootVersion_Type()
)
cambiumUbootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumUbootVersion.setStatus("current")


class _CambiumLANMACAddress_Type(DisplayString):
    """Custom type cambiumLANMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumLANMACAddress_Type.__name__ = "DisplayString"
_CambiumLANMACAddress_Object = MibScalar
cambiumLANMACAddress = _CambiumLANMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 15),
    _CambiumLANMACAddress_Type()
)
cambiumLANMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLANMACAddress.setStatus("current")


class _CambiumCurrentuImageIVersion_Type(DisplayString):
    """Custom type cambiumCurrentuImageIVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CambiumCurrentuImageIVersion_Type.__name__ = "DisplayString"
_CambiumCurrentuImageIVersion_Object = MibScalar
cambiumCurrentuImageIVersion = _CambiumCurrentuImageIVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 16),
    _CambiumCurrentuImageIVersion_Type()
)
cambiumCurrentuImageIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCurrentuImageIVersion.setStatus("current")


class _CambiumCurrentuImageVersion_Type(DisplayString):
    """Custom type cambiumCurrentuImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CambiumCurrentuImageVersion_Type.__name__ = "DisplayString"
_CambiumCurrentuImageVersion_Object = MibScalar
cambiumCurrentuImageVersion = _CambiumCurrentuImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 17),
    _CambiumCurrentuImageVersion_Type()
)
cambiumCurrentuImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCurrentuImageVersion.setStatus("current")
_CambiumDeviceLatitude_Type = DisplayString
_CambiumDeviceLatitude_Object = MibScalar
cambiumDeviceLatitude = _CambiumDeviceLatitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 18),
    _CambiumDeviceLatitude_Type()
)
cambiumDeviceLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceLatitude.setStatus("current")
_CambiumDeviceLongitude_Type = DisplayString
_CambiumDeviceLongitude_Object = MibScalar
cambiumDeviceLongitude = _CambiumDeviceLongitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 19),
    _CambiumDeviceLongitude_Type()
)
cambiumDeviceLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceLongitude.setStatus("current")
_SysRebootCounter_Type = Integer32
_SysRebootCounter_Object = MibScalar
sysRebootCounter = _SysRebootCounter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 20),
    _SysRebootCounter_Type()
)
sysRebootCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRebootCounter.setStatus("current")


class _CambiumDFSStatusStr_Type(DisplayString):
    """Custom type cambiumDFSStatusStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumDFSStatusStr_Type.__name__ = "DisplayString"
_CambiumDFSStatusStr_Object = MibScalar
cambiumDFSStatusStr = _CambiumDFSStatusStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 21),
    _CambiumDFSStatusStr_Type()
)
cambiumDFSStatusStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDFSStatusStr.setStatus("current")


class _CambiumDriverType_Type(Integer32):
    """Custom type cambiumDriverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumDriverType_Type.__name__ = "Integer32"
_CambiumDriverType_Object = MibScalar
cambiumDriverType = _CambiumDriverType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 22),
    _CambiumDriverType_Type()
)
cambiumDriverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDriverType.setStatus("current")


class _CambiumESN_Type(DisplayString):
    """Custom type cambiumESN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_CambiumESN_Type.__name__ = "DisplayString"
_CambiumESN_Object = MibScalar
cambiumESN = _CambiumESN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 30),
    _CambiumESN_Type()
)
cambiumESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumESN.setStatus("current")


class _CambiumEPMPMSN_Type(DisplayString):
    """Custom type cambiumEPMPMSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_CambiumEPMPMSN_Type.__name__ = "DisplayString"
_CambiumEPMPMSN_Object = MibScalar
cambiumEPMPMSN = _CambiumEPMPMSN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 31),
    _CambiumEPMPMSN_Type()
)
cambiumEPMPMSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEPMPMSN.setStatus("current")


class _CambiumFactoryReset_Type(Integer32):
    """Custom type cambiumFactoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumFactoryReset_Type.__name__ = "Integer32"
_CambiumFactoryReset_Object = MibScalar
cambiumFactoryReset = _CambiumFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 32),
    _CambiumFactoryReset_Type()
)
cambiumFactoryReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFactoryReset.setStatus("current")


class _CambiumSubModeType_Type(Integer32):
    """Custom type cambiumSubModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_CambiumSubModeType_Type.__name__ = "Integer32"
_CambiumSubModeType_Object = MibScalar
cambiumSubModeType = _CambiumSubModeType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 1, 33),
    _CambiumSubModeType_Type()
)
cambiumSubModeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSubModeType.setStatus("current")
_CambiumRFStatus_ObjectIdentity = ObjectIdentity
cambiumRFStatus = _CambiumRFStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2)
)


class _CambiumSTAConnectedRFFrequency_Type(Integer32):
    """Custom type cambiumSTAConnectedRFFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2407, 5970),
    )


_CambiumSTAConnectedRFFrequency_Type.__name__ = "Integer32"
_CambiumSTAConnectedRFFrequency_Object = MibScalar
cambiumSTAConnectedRFFrequency = _CambiumSTAConnectedRFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 1),
    _CambiumSTAConnectedRFFrequency_Type()
)
cambiumSTAConnectedRFFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAConnectedRFFrequency.setStatus("current")


class _CambiumSTAConnectedRFBandwidth_Type(Integer32):
    """Custom type cambiumSTAConnectedRFBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumSTAConnectedRFBandwidth_Type.__name__ = "Integer32"
_CambiumSTAConnectedRFBandwidth_Object = MibScalar
cambiumSTAConnectedRFBandwidth = _CambiumSTAConnectedRFBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 2),
    _CambiumSTAConnectedRFBandwidth_Type()
)
cambiumSTAConnectedRFBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAConnectedRFBandwidth.setStatus("current")
_CambiumSTADLRSSI_Type = Integer32
_CambiumSTADLRSSI_Object = MibScalar
cambiumSTADLRSSI = _CambiumSTADLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 3),
    _CambiumSTADLRSSI_Type()
)
cambiumSTADLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADLRSSI.setStatus("current")
_CambiumSTADLCINR_Type = Integer32
_CambiumSTADLCINR_Object = MibScalar
cambiumSTADLCINR = _CambiumSTADLCINR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 4),
    _CambiumSTADLCINR_Type()
)
cambiumSTADLCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADLCINR.setStatus("obsolete")


class _CambiumSTAConductedTXPower_Type(Integer32):
    """Custom type cambiumSTAConductedTXPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25, 30),
    )


_CambiumSTAConductedTXPower_Type.__name__ = "Integer32"
_CambiumSTAConductedTXPower_Object = MibScalar
cambiumSTAConductedTXPower = _CambiumSTAConductedTXPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 5),
    _CambiumSTAConductedTXPower_Type()
)
cambiumSTAConductedTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAConductedTXPower.setStatus("current")


class _CambiumSTAUplinkMCSMode_Type(Integer32):
    """Custom type cambiumSTAUplinkMCSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(9, 15),
    )


_CambiumSTAUplinkMCSMode_Type.__name__ = "Integer32"
_CambiumSTAUplinkMCSMode_Object = MibScalar
cambiumSTAUplinkMCSMode = _CambiumSTAUplinkMCSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 6),
    _CambiumSTAUplinkMCSMode_Type()
)
cambiumSTAUplinkMCSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAUplinkMCSMode.setStatus("current")


class _CambiumSTADownlinkMCSMode_Type(Integer32):
    """Custom type cambiumSTADownlinkMCSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(9, 15),
    )


_CambiumSTADownlinkMCSMode_Type.__name__ = "Integer32"
_CambiumSTADownlinkMCSMode_Object = MibScalar
cambiumSTADownlinkMCSMode = _CambiumSTADownlinkMCSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 7),
    _CambiumSTADownlinkMCSMode_Type()
)
cambiumSTADownlinkMCSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADownlinkMCSMode.setStatus("current")


class _CambiumSTAConnectedAP_Type(DisplayString):
    """Custom type cambiumSTAConnectedAP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumSTAConnectedAP_Type.__name__ = "DisplayString"
_CambiumSTAConnectedAP_Object = MibScalar
cambiumSTAConnectedAP = _CambiumSTAConnectedAP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 8),
    _CambiumSTAConnectedAP_Type()
)
cambiumSTAConnectedAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAConnectedAP.setStatus("current")


class _CambiumSTAPowerControlMode_Type(Integer32):
    """Custom type cambiumSTAPowerControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumSTAPowerControlMode_Type.__name__ = "Integer32"
_CambiumSTAPowerControlMode_Object = MibScalar
cambiumSTAPowerControlMode = _CambiumSTAPowerControlMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 9),
    _CambiumSTAPowerControlMode_Type()
)
cambiumSTAPowerControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAPowerControlMode.setStatus("current")


class _CambiumAPNumberOfConnectedSTA_Type(Integer32):
    """Custom type cambiumAPNumberOfConnectedSTA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CambiumAPNumberOfConnectedSTA_Type.__name__ = "Integer32"
_CambiumAPNumberOfConnectedSTA_Object = MibScalar
cambiumAPNumberOfConnectedSTA = _CambiumAPNumberOfConnectedSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 10),
    _CambiumAPNumberOfConnectedSTA_Type()
)
cambiumAPNumberOfConnectedSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPNumberOfConnectedSTA.setStatus("current")
_CambiumAPConnectedSTAListTable_Object = MibTable
cambiumAPConnectedSTAListTable = _CambiumAPConnectedSTAListTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cambiumAPConnectedSTAListTable.setStatus("obsolete")
_CambiumAPConnectedSTAListEntry_Object = MibTableRow
cambiumAPConnectedSTAListEntry = _CambiumAPConnectedSTAListEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1)
)
cambiumAPConnectedSTAListEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumAPNumberOfConnectedSTA"),
)
if mibBuilder.loadTexts:
    cambiumAPConnectedSTAListEntry.setStatus("obsolete")


class _ConnectedSTAListMAC_Type(DisplayString):
    """Custom type connectedSTAListMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_ConnectedSTAListMAC_Type.__name__ = "DisplayString"
_ConnectedSTAListMAC_Object = MibTableColumn
connectedSTAListMAC = _ConnectedSTAListMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 1),
    _ConnectedSTAListMAC_Type()
)
connectedSTAListMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListMAC.setStatus("obsolete")
_ConnectedSTAListAID_Type = Integer32
_ConnectedSTAListAID_Object = MibTableColumn
connectedSTAListAID = _ConnectedSTAListAID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 2),
    _ConnectedSTAListAID_Type()
)
connectedSTAListAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListAID.setStatus("obsolete")
_ConnectedSTAListChannel_Type = Integer32
_ConnectedSTAListChannel_Object = MibTableColumn
connectedSTAListChannel = _ConnectedSTAListChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 3),
    _ConnectedSTAListChannel_Type()
)
connectedSTAListChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListChannel.setStatus("obsolete")
_ConnectedSTAListULRSSI_Type = Integer32
_ConnectedSTAListULRSSI_Object = MibTableColumn
connectedSTAListULRSSI = _ConnectedSTAListULRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 4),
    _ConnectedSTAListULRSSI_Type()
)
connectedSTAListULRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListULRSSI.setStatus("obsolete")
_ConnectedSTAListDLRSSI_Type = Integer32
_ConnectedSTAListDLRSSI_Object = MibTableColumn
connectedSTAListDLRSSI = _ConnectedSTAListDLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 5),
    _ConnectedSTAListDLRSSI_Type()
)
connectedSTAListDLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListDLRSSI.setStatus("obsolete")
_ConnectedSTAListULCINR_Type = Integer32
_ConnectedSTAListULCINR_Object = MibTableColumn
connectedSTAListULCINR = _ConnectedSTAListULCINR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 6),
    _ConnectedSTAListULCINR_Type()
)
connectedSTAListULCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListULCINR.setStatus("obsolete")
_ConnectedSTAListDLCINR_Type = Integer32
_ConnectedSTAListDLCINR_Object = MibTableColumn
connectedSTAListDLCINR = _ConnectedSTAListDLCINR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 7),
    _ConnectedSTAListDLCINR_Type()
)
connectedSTAListDLCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListDLCINR.setStatus("obsolete")


class _ConnectedSTAListULMCS_Type(Integer32):
    """Custom type connectedSTAListULMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ConnectedSTAListULMCS_Type.__name__ = "Integer32"
_ConnectedSTAListULMCS_Object = MibTableColumn
connectedSTAListULMCS = _ConnectedSTAListULMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 8),
    _ConnectedSTAListULMCS_Type()
)
connectedSTAListULMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListULMCS.setStatus("obsolete")


class _ConnectedSTAListDLMCS_Type(Integer32):
    """Custom type connectedSTAListDLMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ConnectedSTAListDLMCS_Type.__name__ = "Integer32"
_ConnectedSTAListDLMCS_Object = MibTableColumn
connectedSTAListDLMCS = _ConnectedSTAListDLMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 9),
    _ConnectedSTAListDLMCS_Type()
)
connectedSTAListDLMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListDLMCS.setStatus("obsolete")
_ConnectedSTAListIP_Type = IpAddress
_ConnectedSTAListIP_Object = MibTableColumn
connectedSTAListIP = _ConnectedSTAListIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 10),
    _ConnectedSTAListIP_Type()
)
connectedSTAListIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListIP.setStatus("obsolete")
_ConnectedSTAListMirSrc_Type = DisplayString
_ConnectedSTAListMirSrc_Object = MibTableColumn
connectedSTAListMirSrc = _ConnectedSTAListMirSrc_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 12),
    _ConnectedSTAListMirSrc_Type()
)
connectedSTAListMirSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListMirSrc.setStatus("obsolete")
_ConnectedSTAListMirULRate_Type = DisplayString
_ConnectedSTAListMirULRate_Object = MibTableColumn
connectedSTAListMirULRate = _ConnectedSTAListMirULRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 13),
    _ConnectedSTAListMirULRate_Type()
)
connectedSTAListMirULRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListMirULRate.setStatus("obsolete")
_ConnectedSTAListMirDLRate_Type = DisplayString
_ConnectedSTAListMirDLRate_Object = MibTableColumn
connectedSTAListMirDLRate = _ConnectedSTAListMirDLRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 11, 1, 14),
    _ConnectedSTAListMirDLRate_Type()
)
connectedSTAListMirDLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAListMirDLRate.setStatus("obsolete")
_CambiumSTADistanceKm_Type = DisplayString
_CambiumSTADistanceKm_Object = MibScalar
cambiumSTADistanceKm = _CambiumSTADistanceKm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 12),
    _CambiumSTADistanceKm_Type()
)
cambiumSTADistanceKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADistanceKm.setStatus("current")
_CambiumSTADistanceMil_Type = DisplayString
_CambiumSTADistanceMil_Object = MibScalar
cambiumSTADistanceMil = _CambiumSTADistanceMil_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 13),
    _CambiumSTADistanceMil_Type()
)
cambiumSTADistanceMil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADistanceMil.setStatus("current")


class _CambiumPropagationDelay_Type(Integer32):
    """Custom type cambiumPropagationDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 5000000),
    )


_CambiumPropagationDelay_Type.__name__ = "Integer32"
_CambiumPropagationDelay_Object = MibScalar
cambiumPropagationDelay = _CambiumPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 14),
    _CambiumPropagationDelay_Type()
)
cambiumPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumPropagationDelay.setStatus("current")
_CambiumSTAConnectedAPListTable_Object = MibTable
cambiumSTAConnectedAPListTable = _CambiumSTAConnectedAPListTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cambiumSTAConnectedAPListTable.setStatus("obsolete")
_CambiumSTAConnectedAPListEntry_Object = MibTableRow
cambiumSTAConnectedAPListEntry = _CambiumSTAConnectedAPListEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1)
)
cambiumSTAConnectedAPListEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "connectedAPListSSID"),
)
if mibBuilder.loadTexts:
    cambiumSTAConnectedAPListEntry.setStatus("obsolete")
_ConnectedAPListSSID_Type = DisplayString
_ConnectedAPListSSID_Object = MibTableColumn
connectedAPListSSID = _ConnectedAPListSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 1),
    _ConnectedAPListSSID_Type()
)
connectedAPListSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListSSID.setStatus("obsolete")
_ConnectedAPListBSSID_Type = DisplayString
_ConnectedAPListBSSID_Object = MibTableColumn
connectedAPListBSSID = _ConnectedAPListBSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 2),
    _ConnectedAPListBSSID_Type()
)
connectedAPListBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListBSSID.setStatus("obsolete")
_ConnectedAPListChannel_Type = Integer32
_ConnectedAPListChannel_Object = MibTableColumn
connectedAPListChannel = _ConnectedAPListChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 3),
    _ConnectedAPListChannel_Type()
)
connectedAPListChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListChannel.setStatus("obsolete")
_ConnectedAPListFrequency_Type = Integer32
_ConnectedAPListFrequency_Object = MibTableColumn
connectedAPListFrequency = _ConnectedAPListFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 4),
    _ConnectedAPListFrequency_Type()
)
connectedAPListFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListFrequency.setStatus("obsolete")
_ConnectedAPListBandwidth_Type = DisplayString
_ConnectedAPListBandwidth_Object = MibTableColumn
connectedAPListBandwidth = _ConnectedAPListBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 5),
    _ConnectedAPListBandwidth_Type()
)
connectedAPListBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListBandwidth.setStatus("obsolete")
_ConnectedAPListRate_Type = DisplayString
_ConnectedAPListRate_Object = MibTableColumn
connectedAPListRate = _ConnectedAPListRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 6),
    _ConnectedAPListRate_Type()
)
connectedAPListRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListRate.setStatus("obsolete")
_ConnectedAPListCINR_Type = Integer32
_ConnectedAPListCINR_Object = MibTableColumn
connectedAPListCINR = _ConnectedAPListCINR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 7),
    _ConnectedAPListCINR_Type()
)
connectedAPListCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListCINR.setStatus("obsolete")
_ConnectedAPListRSSI_Type = Integer32
_ConnectedAPListRSSI_Object = MibTableColumn
connectedAPListRSSI = _ConnectedAPListRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 8),
    _ConnectedAPListRSSI_Type()
)
connectedAPListRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListRSSI.setStatus("obsolete")
_ConnectedAPListNoise_Type = Integer32
_ConnectedAPListNoise_Object = MibTableColumn
connectedAPListNoise = _ConnectedAPListNoise_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 9),
    _ConnectedAPListNoise_Type()
)
connectedAPListNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListNoise.setStatus("obsolete")
_ConnectedAPListINT_Type = Integer32
_ConnectedAPListINT_Object = MibTableColumn
connectedAPListINT = _ConnectedAPListINT_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 10),
    _ConnectedAPListINT_Type()
)
connectedAPListINT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListINT.setStatus("obsolete")
_ConnectedAPListNEState_Type = Integer32
_ConnectedAPListNEState_Object = MibTableColumn
connectedAPListNEState = _ConnectedAPListNEState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 11),
    _ConnectedAPListNEState_Type()
)
connectedAPListNEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListNEState.setStatus("obsolete")
_ConnectedAPListNEAge_Type = DisplayString
_ConnectedAPListNEAge_Object = MibTableColumn
connectedAPListNEAge = _ConnectedAPListNEAge_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 12),
    _ConnectedAPListNEAge_Type()
)
connectedAPListNEAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListNEAge.setStatus("obsolete")
_ConnectedAPListScanAge_Type = DisplayString
_ConnectedAPListScanAge_Object = MibTableColumn
connectedAPListScanAge = _ConnectedAPListScanAge_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 13),
    _ConnectedAPListScanAge_Type()
)
connectedAPListScanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListScanAge.setStatus("obsolete")
_ConnectedAPListRemainingSTA_Type = Integer32
_ConnectedAPListRemainingSTA_Object = MibTableColumn
connectedAPListRemainingSTA = _ConnectedAPListRemainingSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 14),
    _ConnectedAPListRemainingSTA_Type()
)
connectedAPListRemainingSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListRemainingSTA.setStatus("obsolete")
_ConnectedAPListCAPS_Type = DisplayString
_ConnectedAPListCAPS_Object = MibTableColumn
connectedAPListCAPS = _ConnectedAPListCAPS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 15),
    _ConnectedAPListCAPS_Type()
)
connectedAPListCAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListCAPS.setStatus("obsolete")
_ConnectedAPAuthMethod_Type = DisplayString
_ConnectedAPAuthMethod_Object = MibTableColumn
connectedAPAuthMethod = _ConnectedAPAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 16),
    _ConnectedAPAuthMethod_Type()
)
connectedAPAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPAuthMethod.setStatus("obsolete")
_ConnectedAPListMeetNEAttemptCriteria_Type = DisplayString
_ConnectedAPListMeetNEAttemptCriteria_Object = MibTableColumn
connectedAPListMeetNEAttemptCriteria = _ConnectedAPListMeetNEAttemptCriteria_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 15, 1, 17),
    _ConnectedAPListMeetNEAttemptCriteria_Type()
)
connectedAPListMeetNEAttemptCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPListMeetNEAttemptCriteria.setStatus("obsolete")


class _WirelessInterfaceConnectionState_Type(Integer32):
    """Custom type wirelessInterfaceConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_WirelessInterfaceConnectionState_Type.__name__ = "Integer32"
_WirelessInterfaceConnectionState_Object = MibScalar
wirelessInterfaceConnectionState = _WirelessInterfaceConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 16),
    _WirelessInterfaceConnectionState_Type()
)
wirelessInterfaceConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessInterfaceConnectionState.setStatus("current")


class _CambiumSTAPriority_Type(Integer32):
    """Custom type cambiumSTAPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumSTAPriority_Type.__name__ = "Integer32"
_CambiumSTAPriority_Object = MibScalar
cambiumSTAPriority = _CambiumSTAPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 17),
    _CambiumSTAPriority_Type()
)
cambiumSTAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAPriority.setStatus("current")
_CambiumSTADLSNR_Type = Integer32
_CambiumSTADLSNR_Object = MibScalar
cambiumSTADLSNR = _CambiumSTADLSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 18),
    _CambiumSTADLSNR_Type()
)
cambiumSTADLSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADLSNR.setStatus("current")


class _CambiumConnectedAPMACAddress_Type(DisplayString):
    """Custom type cambiumConnectedAPMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_CambiumConnectedAPMACAddress_Type.__name__ = "DisplayString"
_CambiumConnectedAPMACAddress_Object = MibScalar
cambiumConnectedAPMACAddress = _CambiumConnectedAPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 19),
    _CambiumConnectedAPMACAddress_Type()
)
cambiumConnectedAPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumConnectedAPMACAddress.setStatus("current")
_CambiumSTAConnectedAPTable_Object = MibTable
cambiumSTAConnectedAPTable = _CambiumSTAConnectedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20)
)
if mibBuilder.loadTexts:
    cambiumSTAConnectedAPTable.setStatus("current")
_CambiumSTAConnectedAPEntry_Object = MibTableRow
cambiumSTAConnectedAPEntry = _CambiumSTAConnectedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1)
)
cambiumSTAConnectedAPEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "connectedAPListSSID"),
)
if mibBuilder.loadTexts:
    cambiumSTAConnectedAPEntry.setStatus("current")
_ConnectedAPSSID_Type = DisplayString
_ConnectedAPSSID_Object = MibTableColumn
connectedAPSSID = _ConnectedAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 1),
    _ConnectedAPSSID_Type()
)
connectedAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPSSID.setStatus("current")
_ConnectedAPBSSID_Type = DisplayString
_ConnectedAPBSSID_Object = MibTableColumn
connectedAPBSSID = _ConnectedAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 2),
    _ConnectedAPBSSID_Type()
)
connectedAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPBSSID.setStatus("current")
_ConnectedAPChannel_Type = Integer32
_ConnectedAPChannel_Object = MibTableColumn
connectedAPChannel = _ConnectedAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 3),
    _ConnectedAPChannel_Type()
)
connectedAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPChannel.setStatus("current")
_ConnectedAPFrequency_Type = Integer32
_ConnectedAPFrequency_Object = MibTableColumn
connectedAPFrequency = _ConnectedAPFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 4),
    _ConnectedAPFrequency_Type()
)
connectedAPFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPFrequency.setStatus("current")
_ConnectedAPBandwidth_Type = DisplayString
_ConnectedAPBandwidth_Object = MibTableColumn
connectedAPBandwidth = _ConnectedAPBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 5),
    _ConnectedAPBandwidth_Type()
)
connectedAPBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPBandwidth.setStatus("current")
_ConnectedAPRate_Type = DisplayString
_ConnectedAPRate_Object = MibTableColumn
connectedAPRate = _ConnectedAPRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 6),
    _ConnectedAPRate_Type()
)
connectedAPRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPRate.setStatus("current")
_ConnectedAPSNR_Type = Integer32
_ConnectedAPSNR_Object = MibTableColumn
connectedAPSNR = _ConnectedAPSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 7),
    _ConnectedAPSNR_Type()
)
connectedAPSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPSNR.setStatus("current")
_ConnectedAPRSSI_Type = Integer32
_ConnectedAPRSSI_Object = MibTableColumn
connectedAPRSSI = _ConnectedAPRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 8),
    _ConnectedAPRSSI_Type()
)
connectedAPRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPRSSI.setStatus("current")
_ConnectedAPNoise_Type = Integer32
_ConnectedAPNoise_Object = MibTableColumn
connectedAPNoise = _ConnectedAPNoise_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 9),
    _ConnectedAPNoise_Type()
)
connectedAPNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPNoise.setStatus("current")
_ConnectedAPINT_Type = Integer32
_ConnectedAPINT_Object = MibTableColumn
connectedAPINT = _ConnectedAPINT_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 10),
    _ConnectedAPINT_Type()
)
connectedAPINT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPINT.setStatus("current")
_ConnectedAPNEState_Type = Integer32
_ConnectedAPNEState_Object = MibTableColumn
connectedAPNEState = _ConnectedAPNEState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 11),
    _ConnectedAPNEState_Type()
)
connectedAPNEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPNEState.setStatus("current")
_ConnectedAPNEAge_Type = DisplayString
_ConnectedAPNEAge_Object = MibTableColumn
connectedAPNEAge = _ConnectedAPNEAge_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 12),
    _ConnectedAPNEAge_Type()
)
connectedAPNEAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPNEAge.setStatus("current")
_ConnectedAPScanAge_Type = DisplayString
_ConnectedAPScanAge_Object = MibTableColumn
connectedAPScanAge = _ConnectedAPScanAge_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 13),
    _ConnectedAPScanAge_Type()
)
connectedAPScanAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPScanAge.setStatus("current")
_ConnectedAPRemainingSTA_Type = Integer32
_ConnectedAPRemainingSTA_Object = MibTableColumn
connectedAPRemainingSTA = _ConnectedAPRemainingSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 14),
    _ConnectedAPRemainingSTA_Type()
)
connectedAPRemainingSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPRemainingSTA.setStatus("current")
_ConnectedAPCAPS_Type = DisplayString
_ConnectedAPCAPS_Object = MibTableColumn
connectedAPCAPS = _ConnectedAPCAPS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 15),
    _ConnectedAPCAPS_Type()
)
connectedAPCAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPCAPS.setStatus("current")
_ConnectedAPAuthenticationMethod_Type = DisplayString
_ConnectedAPAuthenticationMethod_Object = MibTableColumn
connectedAPAuthenticationMethod = _ConnectedAPAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 16),
    _ConnectedAPAuthenticationMethod_Type()
)
connectedAPAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPAuthenticationMethod.setStatus("current")
_ConnectedAPMeetNEAttemptCriteria_Type = DisplayString
_ConnectedAPMeetNEAttemptCriteria_Object = MibTableColumn
connectedAPMeetNEAttemptCriteria = _ConnectedAPMeetNEAttemptCriteria_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 20, 1, 17),
    _ConnectedAPMeetNEAttemptCriteria_Type()
)
connectedAPMeetNEAttemptCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedAPMeetNEAttemptCriteria.setStatus("current")


class _StaTxCapacity_Type(Integer32):
    """Custom type staTxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StaTxCapacity_Type.__name__ = "Integer32"
_StaTxCapacity_Object = MibScalar
staTxCapacity = _StaTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 21),
    _StaTxCapacity_Type()
)
staTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTxCapacity.setStatus("current")


class _StaTxQuality_Type(Integer32):
    """Custom type staTxQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StaTxQuality_Type.__name__ = "Integer32"
_StaTxQuality_Object = MibScalar
staTxQuality = _StaTxQuality_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 22),
    _StaTxQuality_Type()
)
staTxQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staTxQuality.setStatus("current")
_CambiumAPConnectedSTATable_Object = MibTable
cambiumAPConnectedSTATable = _CambiumAPConnectedSTATable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30)
)
if mibBuilder.loadTexts:
    cambiumAPConnectedSTATable.setStatus("current")
_CambiumAPConnectedSTAEntry_Object = MibTableRow
cambiumAPConnectedSTAEntry = _CambiumAPConnectedSTAEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1)
)
cambiumAPConnectedSTAEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumAPNumberOfConnectedSTA"),
)
if mibBuilder.loadTexts:
    cambiumAPConnectedSTAEntry.setStatus("current")


class _ConnectedSTAMAC_Type(DisplayString):
    """Custom type connectedSTAMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_ConnectedSTAMAC_Type.__name__ = "DisplayString"
_ConnectedSTAMAC_Object = MibTableColumn
connectedSTAMAC = _ConnectedSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 1),
    _ConnectedSTAMAC_Type()
)
connectedSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMAC.setStatus("current")
_ConnectedSTAAID_Type = Integer32
_ConnectedSTAAID_Object = MibTableColumn
connectedSTAAID = _ConnectedSTAAID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 2),
    _ConnectedSTAAID_Type()
)
connectedSTAAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAAID.setStatus("current")
_ConnectedSTAChannel_Type = Integer32
_ConnectedSTAChannel_Object = MibTableColumn
connectedSTAChannel = _ConnectedSTAChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 3),
    _ConnectedSTAChannel_Type()
)
connectedSTAChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAChannel.setStatus("current")
_ConnectedSTAULRSSI_Type = Integer32
_ConnectedSTAULRSSI_Object = MibTableColumn
connectedSTAULRSSI = _ConnectedSTAULRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 4),
    _ConnectedSTAULRSSI_Type()
)
connectedSTAULRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAULRSSI.setStatus("current")
_ConnectedSTADLRSSI_Type = Integer32
_ConnectedSTADLRSSI_Object = MibTableColumn
connectedSTADLRSSI = _ConnectedSTADLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 5),
    _ConnectedSTADLRSSI_Type()
)
connectedSTADLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTADLRSSI.setStatus("current")
_ConnectedSTAULSNR_Type = Integer32
_ConnectedSTAULSNR_Object = MibTableColumn
connectedSTAULSNR = _ConnectedSTAULSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 6),
    _ConnectedSTAULSNR_Type()
)
connectedSTAULSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAULSNR.setStatus("current")
_ConnectedSTADLSNR_Type = Integer32
_ConnectedSTADLSNR_Object = MibTableColumn
connectedSTADLSNR = _ConnectedSTADLSNR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 7),
    _ConnectedSTADLSNR_Type()
)
connectedSTADLSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTADLSNR.setStatus("current")


class _ConnectedSTAULMCS_Type(Integer32):
    """Custom type connectedSTAULMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ConnectedSTAULMCS_Type.__name__ = "Integer32"
_ConnectedSTAULMCS_Object = MibTableColumn
connectedSTAULMCS = _ConnectedSTAULMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 8),
    _ConnectedSTAULMCS_Type()
)
connectedSTAULMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAULMCS.setStatus("current")


class _ConnectedSTADLMCS_Type(Integer32):
    """Custom type connectedSTADLMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ConnectedSTADLMCS_Type.__name__ = "Integer32"
_ConnectedSTADLMCS_Object = MibTableColumn
connectedSTADLMCS = _ConnectedSTADLMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 9),
    _ConnectedSTADLMCS_Type()
)
connectedSTADLMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTADLMCS.setStatus("current")
_ConnectedSTAIP_Type = IpAddress
_ConnectedSTAIP_Object = MibTableColumn
connectedSTAIP = _ConnectedSTAIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 10),
    _ConnectedSTAIP_Type()
)
connectedSTAIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAIP.setStatus("current")
_ConnectedSTAPriority_Type = DisplayString
_ConnectedSTAPriority_Object = MibTableColumn
connectedSTAPriority = _ConnectedSTAPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 11),
    _ConnectedSTAPriority_Type()
)
connectedSTAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAPriority.setStatus("current")
_ConnectedSTAMirSrc_Type = DisplayString
_ConnectedSTAMirSrc_Object = MibTableColumn
connectedSTAMirSrc = _ConnectedSTAMirSrc_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 12),
    _ConnectedSTAMirSrc_Type()
)
connectedSTAMirSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMirSrc.setStatus("current")
_ConnectedSTAMirULRate_Type = DisplayString
_ConnectedSTAMirULRate_Object = MibTableColumn
connectedSTAMirULRate = _ConnectedSTAMirULRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 13),
    _ConnectedSTAMirULRate_Type()
)
connectedSTAMirULRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMirULRate.setStatus("current")
_ConnectedSTAMirDLRate_Type = DisplayString
_ConnectedSTAMirDLRate_Object = MibTableColumn
connectedSTAMirDLRate = _ConnectedSTAMirDLRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 14),
    _ConnectedSTAMirDLRate_Type()
)
connectedSTAMirDLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMirDLRate.setStatus("current")
_ConnectedSTAClickTHWAddr_Type = DisplayString
_ConnectedSTAClickTHWAddr_Object = MibTableColumn
connectedSTAClickTHWAddr = _ConnectedSTAClickTHWAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 15),
    _ConnectedSTAClickTHWAddr_Type()
)
connectedSTAClickTHWAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAClickTHWAddr.setStatus("current")
_ConnectedSTAClickTWebPort_Type = Integer32
_ConnectedSTAClickTWebPort_Object = MibTableColumn
connectedSTAClickTWebPort = _ConnectedSTAClickTWebPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 16),
    _ConnectedSTAClickTWebPort_Type()
)
connectedSTAClickTWebPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAClickTWebPort.setStatus("current")
_ConnectedSTAClickTWebSec_Type = Integer32
_ConnectedSTAClickTWebSec_Object = MibTableColumn
connectedSTAClickTWebSec = _ConnectedSTAClickTWebSec_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 17),
    _ConnectedSTAClickTWebSec_Type()
)
connectedSTAClickTWebSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAClickTWebSec.setStatus("current")
_ConnectedSTAClickTHostName_Type = DisplayString
_ConnectedSTAClickTHostName_Object = MibTableColumn
connectedSTAClickTHostName = _ConnectedSTAClickTHostName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 18),
    _ConnectedSTAClickTHostName_Type()
)
connectedSTAClickTHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAClickTHostName.setStatus("current")


class _ConnectedSTATXCapacity_Type(Integer32):
    """Custom type connectedSTATXCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConnectedSTATXCapacity_Type.__name__ = "Integer32"
_ConnectedSTATXCapacity_Object = MibTableColumn
connectedSTATXCapacity = _ConnectedSTATXCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 19),
    _ConnectedSTATXCapacity_Type()
)
connectedSTATXCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTATXCapacity.setStatus("current")


class _ConnectedSTATXQuality_Type(Integer32):
    """Custom type connectedSTATXQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConnectedSTATXQuality_Type.__name__ = "Integer32"
_ConnectedSTATXQuality_Object = MibTableColumn
connectedSTATXQuality = _ConnectedSTATXQuality_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 20),
    _ConnectedSTATXQuality_Type()
)
connectedSTATXQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTATXQuality.setStatus("current")
_ConnectedSTAMcastTotalGroups_Type = Integer32
_ConnectedSTAMcastTotalGroups_Object = MibTableColumn
connectedSTAMcastTotalGroups = _ConnectedSTAMcastTotalGroups_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 21),
    _ConnectedSTAMcastTotalGroups_Type()
)
connectedSTAMcastTotalGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastTotalGroups.setStatus("current")
_ConnectedSTAMcastGRP0_Type = IpAddress
_ConnectedSTAMcastGRP0_Object = MibTableColumn
connectedSTAMcastGRP0 = _ConnectedSTAMcastGRP0_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 22),
    _ConnectedSTAMcastGRP0_Type()
)
connectedSTAMcastGRP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP0.setStatus("current")
_ConnectedSTAMcastGRP1_Type = IpAddress
_ConnectedSTAMcastGRP1_Object = MibTableColumn
connectedSTAMcastGRP1 = _ConnectedSTAMcastGRP1_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 23),
    _ConnectedSTAMcastGRP1_Type()
)
connectedSTAMcastGRP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP1.setStatus("current")
_ConnectedSTAMcastGRP2_Type = IpAddress
_ConnectedSTAMcastGRP2_Object = MibTableColumn
connectedSTAMcastGRP2 = _ConnectedSTAMcastGRP2_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 24),
    _ConnectedSTAMcastGRP2_Type()
)
connectedSTAMcastGRP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP2.setStatus("current")
_ConnectedSTAMcastGRP3_Type = IpAddress
_ConnectedSTAMcastGRP3_Object = MibTableColumn
connectedSTAMcastGRP3 = _ConnectedSTAMcastGRP3_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 25),
    _ConnectedSTAMcastGRP3_Type()
)
connectedSTAMcastGRP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP3.setStatus("current")
_ConnectedSTAMcastGRP4_Type = IpAddress
_ConnectedSTAMcastGRP4_Object = MibTableColumn
connectedSTAMcastGRP4 = _ConnectedSTAMcastGRP4_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 26),
    _ConnectedSTAMcastGRP4_Type()
)
connectedSTAMcastGRP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTAMcastGRP4.setStatus("current")
_ConnectedSTASessionTime_Type = DisplayString
_ConnectedSTASessionTime_Object = MibTableColumn
connectedSTASessionTime = _ConnectedSTASessionTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 27),
    _ConnectedSTASessionTime_Type()
)
connectedSTASessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTASessionTime.setStatus("current")
_ConnectedSTADLRateMbps_Type = DisplayString
_ConnectedSTADLRateMbps_Object = MibTableColumn
connectedSTADLRateMbps = _ConnectedSTADLRateMbps_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 30, 1, 28),
    _ConnectedSTADLRateMbps_Type()
)
connectedSTADLRateMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectedSTADLRateMbps.setStatus("current")
_CambiumAPBridgeTable_Object = MibTable
cambiumAPBridgeTable = _CambiumAPBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40)
)
if mibBuilder.loadTexts:
    cambiumAPBridgeTable.setStatus("current")
_CambiumAPBridgeEntry_Object = MibTableRow
cambiumAPBridgeEntry = _CambiumAPBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1)
)
cambiumAPBridgeEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "camAPBrTabDevMACAddress"),
)
if mibBuilder.loadTexts:
    cambiumAPBridgeEntry.setStatus("current")
_CamAPBrTabBridgeName_Type = DisplayString
_CamAPBrTabBridgeName_Object = MibTableColumn
camAPBrTabBridgeName = _CamAPBrTabBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 1),
    _CamAPBrTabBridgeName_Type()
)
camAPBrTabBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabBridgeName.setStatus("current")
_CamAPBrTabDevMACAddress_Type = DisplayString
_CamAPBrTabDevMACAddress_Object = MibTableColumn
camAPBrTabDevMACAddress = _CamAPBrTabDevMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 2),
    _CamAPBrTabDevMACAddress_Type()
)
camAPBrTabDevMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabDevMACAddress.setStatus("current")
_CamAPBrTabDevPort_Type = DisplayString
_CamAPBrTabDevPort_Object = MibTableColumn
camAPBrTabDevPort = _CamAPBrTabDevPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 3),
    _CamAPBrTabDevPort_Type()
)
camAPBrTabDevPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabDevPort.setStatus("current")
_CamAPBrTabSTAMACAddress_Type = DisplayString
_CamAPBrTabSTAMACAddress_Object = MibTableColumn
camAPBrTabSTAMACAddress = _CamAPBrTabSTAMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 4),
    _CamAPBrTabSTAMACAddress_Type()
)
camAPBrTabSTAMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabSTAMACAddress.setStatus("current")
_CamAPBrTabAgingTime_Type = Counter32
_CamAPBrTabAgingTime_Object = MibTableColumn
camAPBrTabAgingTime = _CamAPBrTabAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 40, 1, 5),
    _CamAPBrTabAgingTime_Type()
)
camAPBrTabAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camAPBrTabAgingTime.setStatus("current")
_CambiumSTABridgeTable_Object = MibTable
cambiumSTABridgeTable = _CambiumSTABridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50)
)
if mibBuilder.loadTexts:
    cambiumSTABridgeTable.setStatus("current")
_CambiumSTABridgeEntry_Object = MibTableRow
cambiumSTABridgeEntry = _CambiumSTABridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1)
)
cambiumSTABridgeEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "camSTABrTabDevMACAddress"),
)
if mibBuilder.loadTexts:
    cambiumSTABridgeEntry.setStatus("current")
_CamSTABrTabBridgeName_Type = DisplayString
_CamSTABrTabBridgeName_Object = MibTableColumn
camSTABrTabBridgeName = _CamSTABrTabBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1, 1),
    _CamSTABrTabBridgeName_Type()
)
camSTABrTabBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camSTABrTabBridgeName.setStatus("current")
_CamSTABrTabDevMACAddress_Type = DisplayString
_CamSTABrTabDevMACAddress_Object = MibTableColumn
camSTABrTabDevMACAddress = _CamSTABrTabDevMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1, 2),
    _CamSTABrTabDevMACAddress_Type()
)
camSTABrTabDevMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camSTABrTabDevMACAddress.setStatus("current")
_CamSTABrTabDevPort_Type = DisplayString
_CamSTABrTabDevPort_Object = MibTableColumn
camSTABrTabDevPort = _CamSTABrTabDevPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1, 3),
    _CamSTABrTabDevPort_Type()
)
camSTABrTabDevPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camSTABrTabDevPort.setStatus("current")
_CamSTABrTabAgingTime_Type = Counter32
_CamSTABrTabAgingTime_Object = MibTableColumn
camSTABrTabAgingTime = _CamSTABrTabAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 50, 1, 4),
    _CamSTABrTabAgingTime_Type()
)
camSTABrTabAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    camSTABrTabAgingTime.setStatus("current")


class _CambiumSTAMAC_Type(DisplayString):
    """Custom type cambiumSTAMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_CambiumSTAMAC_Type.__name__ = "DisplayString"
_CambiumSTAMAC_Object = MibScalar
cambiumSTAMAC = _CambiumSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 60),
    _CambiumSTAMAC_Type()
)
cambiumSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTAMAC.setStatus("current")


class _CambiumSTADropReason_Type(DisplayString):
    """Custom type cambiumSTADropReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CambiumSTADropReason_Type.__name__ = "DisplayString"
_CambiumSTADropReason_Object = MibScalar
cambiumSTADropReason = _CambiumSTADropReason_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 2, 61),
    _CambiumSTADropReason_Type()
)
cambiumSTADropReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSTADropReason.setStatus("current")
_CambiumGPSStatus_ObjectIdentity = ObjectIdentity
cambiumGPSStatus = _CambiumGPSStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3)
)


class _CambiumGPSCurrentSyncState_Type(Integer32):
    """Custom type cambiumGPSCurrentSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CambiumGPSCurrentSyncState_Type.__name__ = "Integer32"
_CambiumGPSCurrentSyncState_Object = MibScalar
cambiumGPSCurrentSyncState = _CambiumGPSCurrentSyncState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 1),
    _CambiumGPSCurrentSyncState_Type()
)
cambiumGPSCurrentSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSCurrentSyncState.setStatus("current")


class _CambiumGPSLatitude_Type(DisplayString):
    """Custom type cambiumGPSLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSLatitude_Type.__name__ = "DisplayString"
_CambiumGPSLatitude_Object = MibScalar
cambiumGPSLatitude = _CambiumGPSLatitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 2),
    _CambiumGPSLatitude_Type()
)
cambiumGPSLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSLatitude.setStatus("current")


class _CambiumGPSLongitude_Type(DisplayString):
    """Custom type cambiumGPSLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSLongitude_Type.__name__ = "DisplayString"
_CambiumGPSLongitude_Object = MibScalar
cambiumGPSLongitude = _CambiumGPSLongitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 3),
    _CambiumGPSLongitude_Type()
)
cambiumGPSLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSLongitude.setStatus("current")


class _CambiumGPSHeight_Type(DisplayString):
    """Custom type cambiumGPSHeight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSHeight_Type.__name__ = "DisplayString"
_CambiumGPSHeight_Object = MibScalar
cambiumGPSHeight = _CambiumGPSHeight_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 4),
    _CambiumGPSHeight_Type()
)
cambiumGPSHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSHeight.setStatus("current")


class _CambiumGPSTime_Type(DisplayString):
    """Custom type cambiumGPSTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSTime_Type.__name__ = "DisplayString"
_CambiumGPSTime_Object = MibScalar
cambiumGPSTime = _CambiumGPSTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 5),
    _CambiumGPSTime_Type()
)
cambiumGPSTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSTime.setStatus("current")


class _CambiumGPSNumTrackedSat_Type(Integer32):
    """Custom type cambiumGPSNumTrackedSat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CambiumGPSNumTrackedSat_Type.__name__ = "Integer32"
_CambiumGPSNumTrackedSat_Object = MibScalar
cambiumGPSNumTrackedSat = _CambiumGPSNumTrackedSat_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 6),
    _CambiumGPSNumTrackedSat_Type()
)
cambiumGPSNumTrackedSat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSNumTrackedSat.setStatus("current")


class _CambiumGPSNumVisibleSat_Type(Integer32):
    """Custom type cambiumGPSNumVisibleSat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CambiumGPSNumVisibleSat_Type.__name__ = "Integer32"
_CambiumGPSNumVisibleSat_Object = MibScalar
cambiumGPSNumVisibleSat = _CambiumGPSNumVisibleSat_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 7),
    _CambiumGPSNumVisibleSat_Type()
)
cambiumGPSNumVisibleSat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSNumVisibleSat.setStatus("current")
_CambiumGPSSatSNRTable_Object = MibTable
cambiumGPSSatSNRTable = _CambiumGPSSatSNRTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cambiumGPSSatSNRTable.setStatus("current")
_CambiumGPSSatSNREntry_Object = MibTableRow
cambiumGPSSatSNREntry = _CambiumGPSSatSNREntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8, 1)
)
cambiumGPSSatSNREntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "gpsSatelliteId"),
)
if mibBuilder.loadTexts:
    cambiumGPSSatSNREntry.setStatus("current")


class _GpsSatelliteId_Type(Integer32):
    """Custom type gpsSatelliteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GpsSatelliteId_Type.__name__ = "Integer32"
_GpsSatelliteId_Object = MibTableColumn
gpsSatelliteId = _GpsSatelliteId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8, 1, 1),
    _GpsSatelliteId_Type()
)
gpsSatelliteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatelliteId.setStatus("current")


class _GpsSnrValue_Type(Integer32):
    """Custom type gpsSnrValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_GpsSnrValue_Type.__name__ = "Integer32"
_GpsSnrValue_Object = MibTableColumn
gpsSnrValue = _GpsSnrValue_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8, 1, 2),
    _GpsSnrValue_Type()
)
gpsSnrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSnrValue.setStatus("current")


class _GpsSatelliteStatus_Type(Integer32):
    """Custom type gpsSatelliteStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_GpsSatelliteStatus_Type.__name__ = "Integer32"
_GpsSatelliteStatus_Object = MibTableColumn
gpsSatelliteStatus = _GpsSatelliteStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 8, 1, 3),
    _GpsSatelliteStatus_Type()
)
gpsSatelliteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatelliteStatus.setStatus("current")


class _CambiumGPSDeviceInfo_Type(DisplayString):
    """Custom type cambiumGPSDeviceInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumGPSDeviceInfo_Type.__name__ = "DisplayString"
_CambiumGPSDeviceInfo_Object = MibScalar
cambiumGPSDeviceInfo = _CambiumGPSDeviceInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 9),
    _CambiumGPSDeviceInfo_Type()
)
cambiumGPSDeviceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSDeviceInfo.setStatus("current")


class _CambiumGPSFirmwareUpdateStatus_Type(Integer32):
    """Custom type cambiumGPSFirmwareUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CambiumGPSFirmwareUpdateStatus_Type.__name__ = "Integer32"
_CambiumGPSFirmwareUpdateStatus_Object = MibScalar
cambiumGPSFirmwareUpdateStatus = _CambiumGPSFirmwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 3, 10),
    _CambiumGPSFirmwareUpdateStatus_Type()
)
cambiumGPSFirmwareUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumGPSFirmwareUpdateStatus.setStatus("current")
_CambiumLinkStatus_ObjectIdentity = ObjectIdentity
cambiumLinkStatus = _CambiumLinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4)
)


class _CambiumLANStatus_Type(Integer32):
    """Custom type cambiumLANStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumLANStatus_Type.__name__ = "Integer32"
_CambiumLANStatus_Object = MibScalar
cambiumLANStatus = _CambiumLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 1),
    _CambiumLANStatus_Type()
)
cambiumLANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLANStatus.setStatus("current")


class _CambiumWLANStatus_Type(Integer32):
    """Custom type cambiumWLANStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumWLANStatus_Type.__name__ = "Integer32"
_CambiumWLANStatus_Object = MibScalar
cambiumWLANStatus = _CambiumWLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 2),
    _CambiumWLANStatus_Type()
)
cambiumWLANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumWLANStatus.setStatus("current")
_CambiumEffectiveDeviceIPAddress_Type = IpAddress
_CambiumEffectiveDeviceIPAddress_Object = MibScalar
cambiumEffectiveDeviceIPAddress = _CambiumEffectiveDeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 3),
    _CambiumEffectiveDeviceIPAddress_Type()
)
cambiumEffectiveDeviceIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceIPAddress.setStatus("current")


class _CambiumEffectiveSTANetworkMode_Type(Integer32):
    """Custom type cambiumEffectiveSTANetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_CambiumEffectiveSTANetworkMode_Type.__name__ = "Integer32"
_CambiumEffectiveSTANetworkMode_Object = MibScalar
cambiumEffectiveSTANetworkMode = _CambiumEffectiveSTANetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 4),
    _CambiumEffectiveSTANetworkMode_Type()
)
cambiumEffectiveSTANetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveSTANetworkMode.setStatus("current")
_CambiumEffectiveDeviceLANNetMask_Type = IpAddress
_CambiumEffectiveDeviceLANNetMask_Object = MibScalar
cambiumEffectiveDeviceLANNetMask = _CambiumEffectiveDeviceLANNetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 5),
    _CambiumEffectiveDeviceLANNetMask_Type()
)
cambiumEffectiveDeviceLANNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceLANNetMask.setStatus("current")
_CambiumEffectiveDeviceDefaultGateWay_Type = IpAddress
_CambiumEffectiveDeviceDefaultGateWay_Object = MibScalar
cambiumEffectiveDeviceDefaultGateWay = _CambiumEffectiveDeviceDefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 6),
    _CambiumEffectiveDeviceDefaultGateWay_Type()
)
cambiumEffectiveDeviceDefaultGateWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceDefaultGateWay.setStatus("current")
_CambiumEffectiveDeviceDNSIPAddress_Type = IpAddress
_CambiumEffectiveDeviceDNSIPAddress_Object = MibScalar
cambiumEffectiveDeviceDNSIPAddress = _CambiumEffectiveDeviceDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 7),
    _CambiumEffectiveDeviceDNSIPAddress_Type()
)
cambiumEffectiveDeviceDNSIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceDNSIPAddress.setStatus("current")
_CambiumEffectiveWANIPAddress_Type = IpAddress
_CambiumEffectiveWANIPAddress_Object = MibScalar
cambiumEffectiveWANIPAddress = _CambiumEffectiveWANIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 8),
    _CambiumEffectiveWANIPAddress_Type()
)
cambiumEffectiveWANIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveWANIPAddress.setStatus("current")
_CambiumEffectiveDeviceWANNetMask_Type = IpAddress
_CambiumEffectiveDeviceWANNetMask_Object = MibScalar
cambiumEffectiveDeviceWANNetMask = _CambiumEffectiveDeviceWANNetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 9),
    _CambiumEffectiveDeviceWANNetMask_Type()
)
cambiumEffectiveDeviceWANNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceWANNetMask.setStatus("current")


class _CambiumEffectiveDeviceWANPPPoEStatus_Type(Integer32):
    """Custom type cambiumEffectiveDeviceWANPPPoEStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumEffectiveDeviceWANPPPoEStatus_Type.__name__ = "Integer32"
_CambiumEffectiveDeviceWANPPPoEStatus_Object = MibScalar
cambiumEffectiveDeviceWANPPPoEStatus = _CambiumEffectiveDeviceWANPPPoEStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 10),
    _CambiumEffectiveDeviceWANPPPoEStatus_Type()
)
cambiumEffectiveDeviceWANPPPoEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveDeviceWANPPPoEStatus.setStatus("current")


class _CambiumLANModeStatus_Type(Integer32):
    """Custom type cambiumLANModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumLANModeStatus_Type.__name__ = "Integer32"
_CambiumLANModeStatus_Object = MibScalar
cambiumLANModeStatus = _CambiumLANModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 11),
    _CambiumLANModeStatus_Type()
)
cambiumLANModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLANModeStatus.setStatus("current")


class _CambiumLANSpeedStatus_Type(Integer32):
    """Custom type cambiumLANSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_CambiumLANSpeedStatus_Type.__name__ = "Integer32"
_CambiumLANSpeedStatus_Object = MibScalar
cambiumLANSpeedStatus = _CambiumLANSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 12),
    _CambiumLANSpeedStatus_Type()
)
cambiumLANSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLANSpeedStatus.setStatus("current")


class _CambiumDHCPOption82Status_Type(Integer32):
    """Custom type cambiumDHCPOption82Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumDHCPOption82Status_Type.__name__ = "Integer32"
_CambiumDHCPOption82Status_Object = MibScalar
cambiumDHCPOption82Status = _CambiumDHCPOption82Status_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 13),
    _CambiumDHCPOption82Status_Type()
)
cambiumDHCPOption82Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDHCPOption82Status.setStatus("current")


class _CambiumLAN2ModeStatus_Type(Integer32):
    """Custom type cambiumLAN2ModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumLAN2ModeStatus_Type.__name__ = "Integer32"
_CambiumLAN2ModeStatus_Object = MibScalar
cambiumLAN2ModeStatus = _CambiumLAN2ModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 14),
    _CambiumLAN2ModeStatus_Type()
)
cambiumLAN2ModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLAN2ModeStatus.setStatus("current")


class _CambiumLAN2SpeedStatus_Type(Integer32):
    """Custom type cambiumLAN2SpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_CambiumLAN2SpeedStatus_Type.__name__ = "Integer32"
_CambiumLAN2SpeedStatus_Object = MibScalar
cambiumLAN2SpeedStatus = _CambiumLAN2SpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 15),
    _CambiumLAN2SpeedStatus_Type()
)
cambiumLAN2SpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLAN2SpeedStatus.setStatus("current")


class _CambiumLAN2Status_Type(Integer32):
    """Custom type cambiumLAN2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumLAN2Status_Type.__name__ = "Integer32"
_CambiumLAN2Status_Object = MibScalar
cambiumLAN2Status = _CambiumLAN2Status_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 16),
    _CambiumLAN2Status_Type()
)
cambiumLAN2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLAN2Status.setStatus("current")
_CambiumARPTable_Object = MibTable
cambiumARPTable = _CambiumARPTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20)
)
if mibBuilder.loadTexts:
    cambiumARPTable.setStatus("current")
_CambiumARPEntry_Object = MibTableRow
cambiumARPEntry = _CambiumARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1)
)
cambiumARPEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumARPIndex"),
)
if mibBuilder.loadTexts:
    cambiumARPEntry.setStatus("current")


class _CambiumARPIndex_Type(Integer32):
    """Custom type cambiumARPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CambiumARPIndex_Type.__name__ = "Integer32"
_CambiumARPIndex_Object = MibTableColumn
cambiumARPIndex = _CambiumARPIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1, 1),
    _CambiumARPIndex_Type()
)
cambiumARPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumARPIndex.setStatus("current")


class _CambiumARPMAC_Type(DisplayString):
    """Custom type cambiumARPMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_CambiumARPMAC_Type.__name__ = "DisplayString"
_CambiumARPMAC_Object = MibTableColumn
cambiumARPMAC = _CambiumARPMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1, 2),
    _CambiumARPMAC_Type()
)
cambiumARPMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumARPMAC.setStatus("current")
_CambiumARPIP_Type = IpAddress
_CambiumARPIP_Object = MibTableColumn
cambiumARPIP = _CambiumARPIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1, 3),
    _CambiumARPIP_Type()
)
cambiumARPIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumARPIP.setStatus("current")


class _CambiumARPInterface_Type(DisplayString):
    """Custom type cambiumARPInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_CambiumARPInterface_Type.__name__ = "DisplayString"
_CambiumARPInterface_Object = MibTableColumn
cambiumARPInterface = _CambiumARPInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 20, 1, 4),
    _CambiumARPInterface_Type()
)
cambiumARPInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumARPInterface.setStatus("current")


class _CambiumManagementIFStatus_Type(Integer32):
    """Custom type cambiumManagementIFStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumManagementIFStatus_Type.__name__ = "Integer32"
_CambiumManagementIFStatus_Object = MibScalar
cambiumManagementIFStatus = _CambiumManagementIFStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 25),
    _CambiumManagementIFStatus_Type()
)
cambiumManagementIFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFStatus.setStatus("current")
_CambiumManagementIFIPAddress_Type = IpAddress
_CambiumManagementIFIPAddress_Object = MibScalar
cambiumManagementIFIPAddress = _CambiumManagementIFIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 26),
    _CambiumManagementIFIPAddress_Type()
)
cambiumManagementIFIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFIPAddress.setStatus("current")
_CambiumManagementIFNetMask_Type = IpAddress
_CambiumManagementIFNetMask_Object = MibScalar
cambiumManagementIFNetMask = _CambiumManagementIFNetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 27),
    _CambiumManagementIFNetMask_Type()
)
cambiumManagementIFNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFNetMask.setStatus("current")
_CambiumManagementIFGateway_Type = IpAddress
_CambiumManagementIFGateway_Object = MibScalar
cambiumManagementIFGateway = _CambiumManagementIFGateway_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 28),
    _CambiumManagementIFGateway_Type()
)
cambiumManagementIFGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumManagementIFGateway.setStatus("current")


class _CambiumEffectiveNetworkLanMTU_Type(Integer32):
    """Custom type cambiumEffectiveNetworkLanMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 1700),
    )


_CambiumEffectiveNetworkLanMTU_Type.__name__ = "Integer32"
_CambiumEffectiveNetworkLanMTU_Object = MibScalar
cambiumEffectiveNetworkLanMTU = _CambiumEffectiveNetworkLanMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 29),
    _CambiumEffectiveNetworkLanMTU_Type()
)
cambiumEffectiveNetworkLanMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveNetworkLanMTU.setStatus("current")


class _CambiumEffectiveNetworkBridgeMTU_Type(Integer32):
    """Custom type cambiumEffectiveNetworkBridgeMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 1700),
    )


_CambiumEffectiveNetworkBridgeMTU_Type.__name__ = "Integer32"
_CambiumEffectiveNetworkBridgeMTU_Object = MibScalar
cambiumEffectiveNetworkBridgeMTU = _CambiumEffectiveNetworkBridgeMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 30),
    _CambiumEffectiveNetworkBridgeMTU_Type()
)
cambiumEffectiveNetworkBridgeMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveNetworkBridgeMTU.setStatus("current")
_CambiumStaticRoutesTable_Object = MibTable
cambiumStaticRoutesTable = _CambiumStaticRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31)
)
if mibBuilder.loadTexts:
    cambiumStaticRoutesTable.setStatus("current")
_CambiumStaticRoutesEntry_Object = MibTableRow
cambiumStaticRoutesEntry = _CambiumStaticRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1)
)
cambiumStaticRoutesEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumStaticRoutesIndex"),
)
if mibBuilder.loadTexts:
    cambiumStaticRoutesEntry.setStatus("current")


class _CambiumStaticRoutesIndex_Type(Integer32):
    """Custom type cambiumStaticRoutesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CambiumStaticRoutesIndex_Type.__name__ = "Integer32"
_CambiumStaticRoutesIndex_Object = MibTableColumn
cambiumStaticRoutesIndex = _CambiumStaticRoutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 1),
    _CambiumStaticRoutesIndex_Type()
)
cambiumStaticRoutesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesIndex.setStatus("current")
_CambiumStaticRoutesDestIP_Type = IpAddress
_CambiumStaticRoutesDestIP_Object = MibTableColumn
cambiumStaticRoutesDestIP = _CambiumStaticRoutesDestIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 2),
    _CambiumStaticRoutesDestIP_Type()
)
cambiumStaticRoutesDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesDestIP.setStatus("current")
_CambiumStaticRoutesGW_Type = IpAddress
_CambiumStaticRoutesGW_Object = MibTableColumn
cambiumStaticRoutesGW = _CambiumStaticRoutesGW_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 3),
    _CambiumStaticRoutesGW_Type()
)
cambiumStaticRoutesGW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesGW.setStatus("current")
_CambiumStaticRoutesNetmask_Type = IpAddress
_CambiumStaticRoutesNetmask_Object = MibTableColumn
cambiumStaticRoutesNetmask = _CambiumStaticRoutesNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 4),
    _CambiumStaticRoutesNetmask_Type()
)
cambiumStaticRoutesNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesNetmask.setStatus("current")


class _CambiumStaticRoutesInterface_Type(DisplayString):
    """Custom type cambiumStaticRoutesInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_CambiumStaticRoutesInterface_Type.__name__ = "DisplayString"
_CambiumStaticRoutesInterface_Object = MibTableColumn
cambiumStaticRoutesInterface = _CambiumStaticRoutesInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 31, 1, 5),
    _CambiumStaticRoutesInterface_Type()
)
cambiumStaticRoutesInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStaticRoutesInterface.setStatus("current")
_CambiumIPAliasTable_Object = MibTable
cambiumIPAliasTable = _CambiumIPAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32)
)
if mibBuilder.loadTexts:
    cambiumIPAliasTable.setStatus("current")
_CambiumIPAliasEntry_Object = MibTableRow
cambiumIPAliasEntry = _CambiumIPAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32, 1)
)
cambiumIPAliasEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumIPAliasTableIndex"),
)
if mibBuilder.loadTexts:
    cambiumIPAliasEntry.setStatus("current")


class _CambiumIPAliasTableIndex_Type(Integer32):
    """Custom type cambiumIPAliasTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CambiumIPAliasTableIndex_Type.__name__ = "Integer32"
_CambiumIPAliasTableIndex_Object = MibTableColumn
cambiumIPAliasTableIndex = _CambiumIPAliasTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32, 1, 1),
    _CambiumIPAliasTableIndex_Type()
)
cambiumIPAliasTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIPAliasTableIndex.setStatus("current")
_CambiumIPAliasIP_Type = IpAddress
_CambiumIPAliasIP_Object = MibTableColumn
cambiumIPAliasIP = _CambiumIPAliasIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32, 1, 2),
    _CambiumIPAliasIP_Type()
)
cambiumIPAliasIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIPAliasIP.setStatus("current")
_CambiumIPAliasNetmask_Type = IpAddress
_CambiumIPAliasNetmask_Object = MibTableColumn
cambiumIPAliasNetmask = _CambiumIPAliasNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 32, 1, 3),
    _CambiumIPAliasNetmask_Type()
)
cambiumIPAliasNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIPAliasNetmask.setStatus("current")


class _CambiumCnsServConsStat_Type(DisplayString):
    """Custom type cambiumCnsServConsStat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumCnsServConsStat_Type.__name__ = "DisplayString"
_CambiumCnsServConsStat_Object = MibScalar
cambiumCnsServConsStat = _CambiumCnsServConsStat_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 33),
    _CambiumCnsServConsStat_Type()
)
cambiumCnsServConsStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCnsServConsStat.setStatus("current")


class _CambiumCnsServAccountID_Type(DisplayString):
    """Custom type cambiumCnsServAccountID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumCnsServAccountID_Type.__name__ = "DisplayString"
_CambiumCnsServAccountID_Object = MibScalar
cambiumCnsServAccountID = _CambiumCnsServAccountID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 34),
    _CambiumCnsServAccountID_Type()
)
cambiumCnsServAccountID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumCnsServAccountID.setStatus("current")


class _CambiumAPCnsMGMTState_Type(Integer32):
    """Custom type cambiumAPCnsMGMTState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CambiumAPCnsMGMTState_Type.__name__ = "Integer32"
_CambiumAPCnsMGMTState_Object = MibScalar
cambiumAPCnsMGMTState = _CambiumAPCnsMGMTState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 4, 35),
    _CambiumAPCnsMGMTState_Type()
)
cambiumAPCnsMGMTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPCnsMGMTState.setStatus("current")
_CambiumAcsStatus_ObjectIdentity = ObjectIdentity
cambiumAcsStatus = _CambiumAcsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 5)
)


class _AcsState_Type(Integer32):
    """Custom type acsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcsState_Type.__name__ = "Integer32"
_AcsState_Object = MibScalar
acsState = _AcsState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 5, 1),
    _AcsState_Type()
)
acsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsState.setStatus("current")
_CambiumMcastStatus_ObjectIdentity = ObjectIdentity
cambiumMcastStatus = _CambiumMcastStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6)
)


class _CambiumEffectiveMcastGroupLimit_Type(Integer32):
    """Custom type cambiumEffectiveMcastGroupLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CambiumEffectiveMcastGroupLimit_Type.__name__ = "Integer32"
_CambiumEffectiveMcastGroupLimit_Object = MibScalar
cambiumEffectiveMcastGroupLimit = _CambiumEffectiveMcastGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 1),
    _CambiumEffectiveMcastGroupLimit_Type()
)
cambiumEffectiveMcastGroupLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEffectiveMcastGroupLimit.setStatus("current")


class _CambiumSubscribedMcastGroupNum_Type(Integer32):
    """Custom type cambiumSubscribedMcastGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CambiumSubscribedMcastGroupNum_Type.__name__ = "Integer32"
_CambiumSubscribedMcastGroupNum_Object = MibScalar
cambiumSubscribedMcastGroupNum = _CambiumSubscribedMcastGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 2),
    _CambiumSubscribedMcastGroupNum_Type()
)
cambiumSubscribedMcastGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumSubscribedMcastGroupNum.setStatus("current")


class _CambiumAPMcastTotalGroupCount_Type(Integer32):
    """Custom type cambiumAPMcastTotalGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_CambiumAPMcastTotalGroupCount_Type.__name__ = "Integer32"
_CambiumAPMcastTotalGroupCount_Object = MibScalar
cambiumAPMcastTotalGroupCount = _CambiumAPMcastTotalGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 3),
    _CambiumAPMcastTotalGroupCount_Type()
)
cambiumAPMcastTotalGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAPMcastTotalGroupCount.setStatus("current")


class _CambiumMcastHandlingStatus_Type(Integer32):
    """Custom type cambiumMcastHandlingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
    )


_CambiumMcastHandlingStatus_Type.__name__ = "Integer32"
_CambiumMcastHandlingStatus_Object = MibScalar
cambiumMcastHandlingStatus = _CambiumMcastHandlingStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 4),
    _CambiumMcastHandlingStatus_Type()
)
cambiumMcastHandlingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMcastHandlingStatus.setStatus("current")
_CambiumSubscribedMcastGroupTable_Object = MibTable
cambiumSubscribedMcastGroupTable = _CambiumSubscribedMcastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 10)
)
if mibBuilder.loadTexts:
    cambiumSubscribedMcastGroupTable.setStatus("current")
_CambiumSubscribedMcastGroupEntry_Object = MibTableRow
cambiumSubscribedMcastGroupEntry = _CambiumSubscribedMcastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 10, 1)
)
cambiumSubscribedMcastGroupEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumSubscribedMcastGroupNum"),
)
if mibBuilder.loadTexts:
    cambiumSubscribedMcastGroupEntry.setStatus("current")
_CambiumRegisteredMcastGroupIP_Type = IpAddress
_CambiumRegisteredMcastGroupIP_Object = MibTableColumn
cambiumRegisteredMcastGroupIP = _CambiumRegisteredMcastGroupIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 6, 10, 1, 1),
    _CambiumRegisteredMcastGroupIP_Type()
)
cambiumRegisteredMcastGroupIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumRegisteredMcastGroupIP.setStatus("current")
_CambiumDhcpStatus_ObjectIdentity = ObjectIdentity
cambiumDhcpStatus = _CambiumDhcpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7)
)
_DhcpServerStartIP_Type = IpAddress
_DhcpServerStartIP_Object = MibScalar
dhcpServerStartIP = _DhcpServerStartIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 1),
    _DhcpServerStartIP_Type()
)
dhcpServerStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerStartIP.setStatus("current")
_DhcpServerEndIP_Type = IpAddress
_DhcpServerEndIP_Object = MibScalar
dhcpServerEndIP = _DhcpServerEndIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 2),
    _DhcpServerEndIP_Type()
)
dhcpServerEndIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerEndIP.setStatus("current")
_DhcpServerGatewayIP_Type = IpAddress
_DhcpServerGatewayIP_Object = MibScalar
dhcpServerGatewayIP = _DhcpServerGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 3),
    _DhcpServerGatewayIP_Type()
)
dhcpServerGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerGatewayIP.setStatus("current")
_DhcpServerDNSIP_Type = IpAddress
_DhcpServerDNSIP_Object = MibScalar
dhcpServerDNSIP = _DhcpServerDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 4),
    _DhcpServerDNSIP_Type()
)
dhcpServerDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDNSIP.setStatus("current")
_DhcpServerStaticHostTable_Object = MibTable
dhcpServerStaticHostTable = _DhcpServerStaticHostTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5)
)
if mibBuilder.loadTexts:
    dhcpServerStaticHostTable.setStatus("current")
_DhcpServerStaticHostEntry_Object = MibTableRow
dhcpServerStaticHostEntry = _DhcpServerStaticHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5, 1)
)
dhcpServerStaticHostEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "dhcpStaticIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerStaticHostEntry.setStatus("current")


class _DhcpStaticIndex_Type(Integer32):
    """Custom type dhcpStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DhcpStaticIndex_Type.__name__ = "Integer32"
_DhcpStaticIndex_Object = MibTableColumn
dhcpStaticIndex = _DhcpStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5, 1, 1),
    _DhcpStaticIndex_Type()
)
dhcpStaticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticIndex.setStatus("current")


class _DhcpStaticMAC_Type(DisplayString):
    """Custom type dhcpStaticMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_DhcpStaticMAC_Type.__name__ = "DisplayString"
_DhcpStaticMAC_Object = MibTableColumn
dhcpStaticMAC = _DhcpStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5, 1, 2),
    _DhcpStaticMAC_Type()
)
dhcpStaticMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticMAC.setStatus("current")
_DhcpStaticIP_Type = IpAddress
_DhcpStaticIP_Object = MibTableColumn
dhcpStaticIP = _DhcpStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 5, 1, 3),
    _DhcpStaticIP_Type()
)
dhcpStaticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpStaticIP.setStatus("current")
_DhcpServerLeaseTable_Object = MibTable
dhcpServerLeaseTable = _DhcpServerLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6)
)
if mibBuilder.loadTexts:
    dhcpServerLeaseTable.setStatus("current")
_DhcpServerLeaseEntry_Object = MibTableRow
dhcpServerLeaseEntry = _DhcpServerLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1)
)
dhcpServerLeaseEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "dhcpLeaseIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerLeaseEntry.setStatus("current")


class _DhcpLeaseIndex_Type(Integer32):
    """Custom type dhcpLeaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DhcpLeaseIndex_Type.__name__ = "Integer32"
_DhcpLeaseIndex_Object = MibTableColumn
dhcpLeaseIndex = _DhcpLeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1, 1),
    _DhcpLeaseIndex_Type()
)
dhcpLeaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseIndex.setStatus("current")


class _DhcpLeaseMAC_Type(DisplayString):
    """Custom type dhcpLeaseMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_DhcpLeaseMAC_Type.__name__ = "DisplayString"
_DhcpLeaseMAC_Object = MibTableColumn
dhcpLeaseMAC = _DhcpLeaseMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1, 2),
    _DhcpLeaseMAC_Type()
)
dhcpLeaseMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseMAC.setStatus("current")
_DhcpLeaseIP_Type = IpAddress
_DhcpLeaseIP_Object = MibTableColumn
dhcpLeaseIP = _DhcpLeaseIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1, 3),
    _DhcpLeaseIP_Type()
)
dhcpLeaseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseIP.setStatus("current")
_DhcpLeaseDevName_Type = DisplayString
_DhcpLeaseDevName_Object = MibTableColumn
dhcpLeaseDevName = _DhcpLeaseDevName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 1, 7, 6, 1, 4),
    _DhcpLeaseDevName_Type()
)
dhcpLeaseDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpLeaseDevName.setStatus("current")
_CambiumPmp80211SystemMonitoring_ObjectIdentity = ObjectIdentity
cambiumPmp80211SystemMonitoring = _CambiumPmp80211SystemMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2)
)
_CambiumPerformanceMonitoring_ObjectIdentity = ObjectIdentity
cambiumPerformanceMonitoring = _CambiumPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1)
)


class _CambiumStatsForceUpdate_Type(Integer32):
    """Custom type cambiumStatsForceUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumStatsForceUpdate_Type.__name__ = "Integer32"
_CambiumStatsForceUpdate_Object = MibScalar
cambiumStatsForceUpdate = _CambiumStatsForceUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 1),
    _CambiumStatsForceUpdate_Type()
)
cambiumStatsForceUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStatsForceUpdate.setStatus("current")
_CambiumEthRXBytes_Type = Counter64
_CambiumEthRXBytes_Object = MibScalar
cambiumEthRXBytes = _CambiumEthRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 2),
    _CambiumEthRXBytes_Type()
)
cambiumEthRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXBytes.setStatus("current")
_CambiumEthRXPackets_Type = Counter64
_CambiumEthRXPackets_Object = MibScalar
cambiumEthRXPackets = _CambiumEthRXPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 3),
    _CambiumEthRXPackets_Type()
)
cambiumEthRXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXPackets.setStatus("current")
_CambiumEthRXErrors_Type = Counter64
_CambiumEthRXErrors_Object = MibScalar
cambiumEthRXErrors = _CambiumEthRXErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 4),
    _CambiumEthRXErrors_Type()
)
cambiumEthRXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXErrors.setStatus("current")
_CambiumEthRXDrops_Type = Counter64
_CambiumEthRXDrops_Object = MibScalar
cambiumEthRXDrops = _CambiumEthRXDrops_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 5),
    _CambiumEthRXDrops_Type()
)
cambiumEthRXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXDrops.setStatus("current")
_CambiumEthRXMulticast_Type = Counter64
_CambiumEthRXMulticast_Object = MibScalar
cambiumEthRXMulticast = _CambiumEthRXMulticast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 6),
    _CambiumEthRXMulticast_Type()
)
cambiumEthRXMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXMulticast.setStatus("current")
_CambiumEthRXBroadcast_Type = Counter64
_CambiumEthRXBroadcast_Object = MibScalar
cambiumEthRXBroadcast = _CambiumEthRXBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 7),
    _CambiumEthRXBroadcast_Type()
)
cambiumEthRXBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthRXBroadcast.setStatus("current")
_CambiumEthTXBytes_Type = Counter64
_CambiumEthTXBytes_Object = MibScalar
cambiumEthTXBytes = _CambiumEthTXBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 8),
    _CambiumEthTXBytes_Type()
)
cambiumEthTXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXBytes.setStatus("current")
_CambiumEthTXPackets_Type = Counter64
_CambiumEthTXPackets_Object = MibScalar
cambiumEthTXPackets = _CambiumEthTXPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 9),
    _CambiumEthTXPackets_Type()
)
cambiumEthTXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXPackets.setStatus("current")
_CambiumEthTXErrors_Type = Counter64
_CambiumEthTXErrors_Object = MibScalar
cambiumEthTXErrors = _CambiumEthTXErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 10),
    _CambiumEthTXErrors_Type()
)
cambiumEthTXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXErrors.setStatus("current")
_CambiumEthTXDrops_Type = Counter64
_CambiumEthTXDrops_Object = MibScalar
cambiumEthTXDrops = _CambiumEthTXDrops_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 11),
    _CambiumEthTXDrops_Type()
)
cambiumEthTXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXDrops.setStatus("current")
_CambiumEthTXMulticast_Type = Counter64
_CambiumEthTXMulticast_Object = MibScalar
cambiumEthTXMulticast = _CambiumEthTXMulticast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 12),
    _CambiumEthTXMulticast_Type()
)
cambiumEthTXMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXMulticast.setStatus("current")
_CambiumEthTXBroadcast_Type = Counter64
_CambiumEthTXBroadcast_Object = MibScalar
cambiumEthTXBroadcast = _CambiumEthTXBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 13),
    _CambiumEthTXBroadcast_Type()
)
cambiumEthTXBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumEthTXBroadcast.setStatus("current")
_CambiumAthRXBytes_Type = Counter64
_CambiumAthRXBytes_Object = MibScalar
cambiumAthRXBytes = _CambiumAthRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 21),
    _CambiumAthRXBytes_Type()
)
cambiumAthRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXBytes.setStatus("obsolete")
_CambiumAthRXPackets_Type = Counter64
_CambiumAthRXPackets_Object = MibScalar
cambiumAthRXPackets = _CambiumAthRXPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 22),
    _CambiumAthRXPackets_Type()
)
cambiumAthRXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXPackets.setStatus("obsolete")
_CambiumAthRXErrors_Type = Counter64
_CambiumAthRXErrors_Object = MibScalar
cambiumAthRXErrors = _CambiumAthRXErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 23),
    _CambiumAthRXErrors_Type()
)
cambiumAthRXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXErrors.setStatus("obsolete")
_CambiumAthRXDrops_Type = Counter64
_CambiumAthRXDrops_Object = MibScalar
cambiumAthRXDrops = _CambiumAthRXDrops_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 24),
    _CambiumAthRXDrops_Type()
)
cambiumAthRXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXDrops.setStatus("obsolete")
_CambiumAthRXMulticast_Type = Counter64
_CambiumAthRXMulticast_Object = MibScalar
cambiumAthRXMulticast = _CambiumAthRXMulticast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 25),
    _CambiumAthRXMulticast_Type()
)
cambiumAthRXMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXMulticast.setStatus("obsolete")
_CambiumAthRXBroadcast_Type = Counter64
_CambiumAthRXBroadcast_Object = MibScalar
cambiumAthRXBroadcast = _CambiumAthRXBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 26),
    _CambiumAthRXBroadcast_Type()
)
cambiumAthRXBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthRXBroadcast.setStatus("obsolete")
_CambiumAthTXBytes_Type = Counter64
_CambiumAthTXBytes_Object = MibScalar
cambiumAthTXBytes = _CambiumAthTXBytes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 27),
    _CambiumAthTXBytes_Type()
)
cambiumAthTXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXBytes.setStatus("obsolete")
_CambiumAthTXPackets_Type = Counter64
_CambiumAthTXPackets_Object = MibScalar
cambiumAthTXPackets = _CambiumAthTXPackets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 28),
    _CambiumAthTXPackets_Type()
)
cambiumAthTXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXPackets.setStatus("obsolete")
_CambiumAthTXErrors_Type = Counter64
_CambiumAthTXErrors_Object = MibScalar
cambiumAthTXErrors = _CambiumAthTXErrors_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 29),
    _CambiumAthTXErrors_Type()
)
cambiumAthTXErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXErrors.setStatus("obsolete")
_CambiumAthTXDrops_Type = Counter64
_CambiumAthTXDrops_Object = MibScalar
cambiumAthTXDrops = _CambiumAthTXDrops_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 30),
    _CambiumAthTXDrops_Type()
)
cambiumAthTXDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXDrops.setStatus("obsolete")
_CambiumAthTXMulticast_Type = Counter64
_CambiumAthTXMulticast_Object = MibScalar
cambiumAthTXMulticast = _CambiumAthTXMulticast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 31),
    _CambiumAthTXMulticast_Type()
)
cambiumAthTXMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXMulticast.setStatus("obsolete")
_CambiumAthTXBroadcast_Type = Counter64
_CambiumAthTXBroadcast_Object = MibScalar
cambiumAthTXBroadcast = _CambiumAthTXBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 32),
    _CambiumAthTXBroadcast_Type()
)
cambiumAthTXBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumAthTXBroadcast.setStatus("obsolete")
_SysNetworkEntryAttempt_Type = Counter32
_SysNetworkEntryAttempt_Object = MibScalar
sysNetworkEntryAttempt = _SysNetworkEntryAttempt_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 33),
    _SysNetworkEntryAttempt_Type()
)
sysNetworkEntryAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetworkEntryAttempt.setStatus("current")
_SysNetworkEntrySuccess_Type = Counter32
_SysNetworkEntrySuccess_Object = MibScalar
sysNetworkEntrySuccess = _SysNetworkEntrySuccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 34),
    _SysNetworkEntrySuccess_Type()
)
sysNetworkEntrySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetworkEntrySuccess.setStatus("current")
_SysNetworkEntryAuthenticationFailure_Type = Counter32
_SysNetworkEntryAuthenticationFailure_Object = MibScalar
sysNetworkEntryAuthenticationFailure = _SysNetworkEntryAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 35),
    _SysNetworkEntryAuthenticationFailure_Type()
)
sysNetworkEntryAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNetworkEntryAuthenticationFailure.setStatus("current")
_SysDFSDetectedCount_Type = Counter32
_SysDFSDetectedCount_Object = MibScalar
sysDFSDetectedCount = _SysDFSDetectedCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 36),
    _SysDFSDetectedCount_Type()
)
sysDFSDetectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDFSDetectedCount.setStatus("current")
_UlWLanKbitCount_Type = Counter64
_UlWLanKbitCount_Object = MibScalar
ulWLanKbitCount = _UlWLanKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 37),
    _UlWLanKbitCount_Type()
)
ulWLanKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanKbitCount.setStatus("current")
_DlWLanKbitCount_Type = Counter64
_DlWLanKbitCount_Object = MibScalar
dlWLanKbitCount = _DlWLanKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 38),
    _DlWLanKbitCount_Type()
)
dlWLanKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanKbitCount.setStatus("current")
_UlWLanTotalPacketCount_Type = Counter64
_UlWLanTotalPacketCount_Object = MibScalar
ulWLanTotalPacketCount = _UlWLanTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 39),
    _UlWLanTotalPacketCount_Type()
)
ulWLanTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanTotalPacketCount.setStatus("current")
_SysRebootCount_Type = Integer32
_SysRebootCount_Object = MibScalar
sysRebootCount = _SysRebootCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 41),
    _SysRebootCount_Type()
)
sysRebootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRebootCount.setStatus("obsolete")
_DlWLanTotalPacketCount_Type = Counter64
_DlWLanTotalPacketCount_Object = MibScalar
dlWLanTotalPacketCount = _DlWLanTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 42),
    _DlWLanTotalPacketCount_Type()
)
dlWLanTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanTotalPacketCount.setStatus("current")
_UlWLanMultiBroadcastKbitCount_Type = Counter64
_UlWLanMultiBroadcastKbitCount_Object = MibScalar
ulWLanMultiBroadcastKbitCount = _UlWLanMultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 43),
    _UlWLanMultiBroadcastKbitCount_Type()
)
ulWLanMultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMultiBroadcastKbitCount.setStatus("current")
_DlWLanMultiBroadcastKbitCount_Type = Counter64
_DlWLanMultiBroadcastKbitCount_Object = MibScalar
dlWLanMultiBroadcastKbitCount = _DlWLanMultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 44),
    _DlWLanMultiBroadcastKbitCount_Type()
)
dlWLanMultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMultiBroadcastKbitCount.setStatus("current")
_WLanSessionDroppedCount_Type = Counter32
_WLanSessionDroppedCount_Object = MibScalar
wLanSessionDroppedCount = _WLanSessionDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 45),
    _WLanSessionDroppedCount_Type()
)
wLanSessionDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wLanSessionDroppedCount.setStatus("current")
_CambiumTDDStatsPerSTATable_Object = MibTable
cambiumTDDStatsPerSTATable = _CambiumTDDStatsPerSTATable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46)
)
if mibBuilder.loadTexts:
    cambiumTDDStatsPerSTATable.setStatus("current")
_CambiumTDDStatsPerSTAEntry_Object = MibTableRow
cambiumTDDStatsPerSTAEntry = _CambiumTDDStatsPerSTAEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1)
)
cambiumTDDStatsPerSTAEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumTDDStatsPerSTAIndex"),
)
if mibBuilder.loadTexts:
    cambiumTDDStatsPerSTAEntry.setStatus("current")


class _CambiumTDDStatsPerSTAIndex_Type(Integer32):
    """Custom type cambiumTDDStatsPerSTAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CambiumTDDStatsPerSTAIndex_Type.__name__ = "Integer32"
_CambiumTDDStatsPerSTAIndex_Object = MibTableColumn
cambiumTDDStatsPerSTAIndex = _CambiumTDDStatsPerSTAIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 1),
    _CambiumTDDStatsPerSTAIndex_Type()
)
cambiumTDDStatsPerSTAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTDDStatsPerSTAIndex.setStatus("current")


class _CambiumTDDStatsListMAC_Type(DisplayString):
    """Custom type cambiumTDDStatsListMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_CambiumTDDStatsListMAC_Type.__name__ = "DisplayString"
_CambiumTDDStatsListMAC_Object = MibTableColumn
cambiumTDDStatsListMAC = _CambiumTDDStatsListMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 2),
    _CambiumTDDStatsListMAC_Type()
)
cambiumTDDStatsListMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumTDDStatsListMAC.setStatus("current")
_UlWLanPerUserKbitCount_Type = Counter64
_UlWLanPerUserKbitCount_Object = MibTableColumn
ulWLanPerUserKbitCount = _UlWLanPerUserKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 3),
    _UlWLanPerUserKbitCount_Type()
)
ulWLanPerUserKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanPerUserKbitCount.setStatus("current")
_DlWLanPerUserKbitCount_Type = Counter64
_DlWLanPerUserKbitCount_Object = MibTableColumn
dlWLanPerUserKbitCount = _DlWLanPerUserKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 4),
    _DlWLanPerUserKbitCount_Type()
)
dlWLanPerUserKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserKbitCount.setStatus("current")
_UlWLanPerUserTotalPacketCount_Type = Counter64
_UlWLanPerUserTotalPacketCount_Object = MibTableColumn
ulWLanPerUserTotalPacketCount = _UlWLanPerUserTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 5),
    _UlWLanPerUserTotalPacketCount_Type()
)
ulWLanPerUserTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanPerUserTotalPacketCount.setStatus("current")
_DlWLanPerUserTotalPacketCount_Type = Counter64
_DlWLanPerUserTotalPacketCount_Object = MibTableColumn
dlWLanPerUserTotalPacketCount = _DlWLanPerUserTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 6),
    _DlWLanPerUserTotalPacketCount_Type()
)
dlWLanPerUserTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserTotalPacketCount.setStatus("current")
_UlWLanPerUserErrorDroppedPacketCount_Type = Counter64
_UlWLanPerUserErrorDroppedPacketCount_Object = MibTableColumn
ulWLanPerUserErrorDroppedPacketCount = _UlWLanPerUserErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 7),
    _UlWLanPerUserErrorDroppedPacketCount_Type()
)
ulWLanPerUserErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanPerUserErrorDroppedPacketCount.setStatus("current")
_DlWLanPerUserErrorDroppedPacketCount_Type = Counter64
_DlWLanPerUserErrorDroppedPacketCount_Object = MibTableColumn
dlWLanPerUserErrorDroppedPacketCount = _DlWLanPerUserErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 8),
    _DlWLanPerUserErrorDroppedPacketCount_Type()
)
dlWLanPerUserErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserErrorDroppedPacketCount.setStatus("current")
_DlWLanPerUserCapacityDroppedPacketCount_Type = Counter64
_DlWLanPerUserCapacityDroppedPacketCount_Object = MibTableColumn
dlWLanPerUserCapacityDroppedPacketCount = _DlWLanPerUserCapacityDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 9),
    _DlWLanPerUserCapacityDroppedPacketCount_Type()
)
dlWLanPerUserCapacityDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserCapacityDroppedPacketCount.setStatus("current")
_DlWLanPerUserRetransmitPacketCount_Type = Counter64
_DlWLanPerUserRetransmitPacketCount_Object = MibTableColumn
dlWLanPerUserRetransmitPacketCount = _DlWLanPerUserRetransmitPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 10),
    _DlWLanPerUserRetransmitPacketCount_Type()
)
dlWLanPerUserRetransmitPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserRetransmitPacketCount.setStatus("current")
_DlWLanPerUserTxPower_Type = Integer32
_DlWLanPerUserTxPower_Object = MibTableColumn
dlWLanPerUserTxPower = _DlWLanPerUserTxPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 46, 1, 11),
    _DlWLanPerUserTxPower_Type()
)
dlWLanPerUserTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanPerUserTxPower.setStatus("current")
_UlWLanErrorDroppedPacketCount_Type = Counter64
_UlWLanErrorDroppedPacketCount_Object = MibScalar
ulWLanErrorDroppedPacketCount = _UlWLanErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 47),
    _UlWLanErrorDroppedPacketCount_Type()
)
ulWLanErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanErrorDroppedPacketCount.setStatus("current")
_DlWLanErrorDroppedPacketCount_Type = Counter64
_DlWLanErrorDroppedPacketCount_Object = MibScalar
dlWLanErrorDroppedPacketCount = _DlWLanErrorDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 48),
    _DlWLanErrorDroppedPacketCount_Type()
)
dlWLanErrorDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanErrorDroppedPacketCount.setStatus("current")
_UlWLanCapacityDroppedPacketCount_Type = Counter64
_UlWLanCapacityDroppedPacketCount_Object = MibScalar
ulWLanCapacityDroppedPacketCount = _UlWLanCapacityDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 49),
    _UlWLanCapacityDroppedPacketCount_Type()
)
ulWLanCapacityDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanCapacityDroppedPacketCount.setStatus("current")
_DlWLanCapacityDroppedPacketCount_Type = Counter64
_DlWLanCapacityDroppedPacketCount_Object = MibScalar
dlWLanCapacityDroppedPacketCount = _DlWLanCapacityDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 50),
    _DlWLanCapacityDroppedPacketCount_Type()
)
dlWLanCapacityDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanCapacityDroppedPacketCount.setStatus("current")
_UlWLanTotalAvailableFrameTimePerSecond_Type = Counter32
_UlWLanTotalAvailableFrameTimePerSecond_Object = MibScalar
ulWLanTotalAvailableFrameTimePerSecond = _UlWLanTotalAvailableFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 51),
    _UlWLanTotalAvailableFrameTimePerSecond_Type()
)
ulWLanTotalAvailableFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanTotalAvailableFrameTimePerSecond.setStatus("current")
_DlWLanTotalAvailableFrameTimePerSecond_Type = Counter32
_DlWLanTotalAvailableFrameTimePerSecond_Object = MibScalar
dlWLanTotalAvailableFrameTimePerSecond = _DlWLanTotalAvailableFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 52),
    _DlWLanTotalAvailableFrameTimePerSecond_Type()
)
dlWLanTotalAvailableFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanTotalAvailableFrameTimePerSecond.setStatus("current")
_UlWLanTotalUsedFrameTimePerSecond_Type = Counter32
_UlWLanTotalUsedFrameTimePerSecond_Object = MibScalar
ulWLanTotalUsedFrameTimePerSecond = _UlWLanTotalUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 53),
    _UlWLanTotalUsedFrameTimePerSecond_Type()
)
ulWLanTotalUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanTotalUsedFrameTimePerSecond.setStatus("current")
_DlWLanTotalUsedFrameTimePerSecond_Type = Counter32
_DlWLanTotalUsedFrameTimePerSecond_Object = MibScalar
dlWLanTotalUsedFrameTimePerSecond = _DlWLanTotalUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 54),
    _DlWLanTotalUsedFrameTimePerSecond_Type()
)
dlWLanTotalUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanTotalUsedFrameTimePerSecond.setStatus("current")
_UlWLanTotalOverheadFrameTimePerSecond_Type = Counter32
_UlWLanTotalOverheadFrameTimePerSecond_Object = MibScalar
ulWLanTotalOverheadFrameTimePerSecond = _UlWLanTotalOverheadFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 55),
    _UlWLanTotalOverheadFrameTimePerSecond_Type()
)
ulWLanTotalOverheadFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanTotalOverheadFrameTimePerSecond.setStatus("current")
_DlWLanTotalOverheadFrameTimePerSecond_Type = Counter32
_DlWLanTotalOverheadFrameTimePerSecond_Object = MibScalar
dlWLanTotalOverheadFrameTimePerSecond = _DlWLanTotalOverheadFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 56),
    _DlWLanTotalOverheadFrameTimePerSecond_Type()
)
dlWLanTotalOverheadFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanTotalOverheadFrameTimePerSecond.setStatus("current")
_CambiumMCSTable_Object = MibTable
cambiumMCSTable = _CambiumMCSTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57)
)
if mibBuilder.loadTexts:
    cambiumMCSTable.setStatus("obsolete")
_CambiumMCSEntry_Object = MibTableRow
cambiumMCSEntry = _CambiumMCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1)
)
cambiumMCSEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumMCSIndex"),
)
if mibBuilder.loadTexts:
    cambiumMCSEntry.setStatus("obsolete")


class _CambiumMCSIndex_Type(Integer32):
    """Custom type cambiumMCSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CambiumMCSIndex_Type.__name__ = "Integer32"
_CambiumMCSIndex_Object = MibTableColumn
cambiumMCSIndex = _CambiumMCSIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1, 1),
    _CambiumMCSIndex_Type()
)
cambiumMCSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMCSIndex.setStatus("obsolete")
_CambiumMCSNumber_Type = DisplayString
_CambiumMCSNumber_Object = MibTableColumn
cambiumMCSNumber = _CambiumMCSNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1, 2),
    _CambiumMCSNumber_Type()
)
cambiumMCSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumMCSNumber.setStatus("obsolete")
_UlWLanMCSUsedFrameTimePerSecond_Type = Counter32
_UlWLanMCSUsedFrameTimePerSecond_Object = MibTableColumn
ulWLanMCSUsedFrameTimePerSecond = _UlWLanMCSUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1, 3),
    _UlWLanMCSUsedFrameTimePerSecond_Type()
)
ulWLanMCSUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCSUsedFrameTimePerSecond.setStatus("obsolete")
_DlWLanMCSUsedFrameTimePerSecond_Type = Counter32
_DlWLanMCSUsedFrameTimePerSecond_Object = MibTableColumn
dlWLanMCSUsedFrameTimePerSecond = _DlWLanMCSUsedFrameTimePerSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 57, 1, 4),
    _DlWLanMCSUsedFrameTimePerSecond_Type()
)
dlWLanMCSUsedFrameTimePerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCSUsedFrameTimePerSecond.setStatus("obsolete")
_UlWLanRetransPacketCount_Type = Counter64
_UlWLanRetransPacketCount_Object = MibScalar
ulWLanRetransPacketCount = _UlWLanRetransPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 58),
    _UlWLanRetransPacketCount_Type()
)
ulWLanRetransPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanRetransPacketCount.setStatus("current")
_DlWLanRetransPacketCount_Type = Counter64
_DlWLanRetransPacketCount_Object = MibScalar
dlWLanRetransPacketCount = _DlWLanRetransPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 59),
    _DlWLanRetransPacketCount_Type()
)
dlWLanRetransPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanRetransPacketCount.setStatus("current")
_UlWLanBroadcastPacketCount_Type = Counter32
_UlWLanBroadcastPacketCount_Object = MibScalar
ulWLanBroadcastPacketCount = _UlWLanBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 60),
    _UlWLanBroadcastPacketCount_Type()
)
ulWLanBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanBroadcastPacketCount.setStatus("current")
_DlWLanBroadcastPacketCount_Type = Counter32
_DlWLanBroadcastPacketCount_Object = MibScalar
dlWLanBroadcastPacketCount = _DlWLanBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 61),
    _DlWLanBroadcastPacketCount_Type()
)
dlWLanBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanBroadcastPacketCount.setStatus("current")
_UlWLanMulticastPacketCount_Type = Counter32
_UlWLanMulticastPacketCount_Object = MibScalar
ulWLanMulticastPacketCount = _UlWLanMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 62),
    _UlWLanMulticastPacketCount_Type()
)
ulWLanMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMulticastPacketCount.setStatus("current")
_DlWLanMulticastPacketCount_Type = Counter32
_DlWLanMulticastPacketCount_Object = MibScalar
dlWLanMulticastPacketCount = _DlWLanMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 63),
    _DlWLanMulticastPacketCount_Type()
)
dlWLanMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMulticastPacketCount.setStatus("current")
_SysCPUUsage_Type = Counter32
_SysCPUUsage_Object = MibScalar
sysCPUUsage = _SysCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 64),
    _SysCPUUsage_Type()
)
sysCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUUsage.setStatus("current")
_RxEtherLanKbitCount_Type = Counter64
_RxEtherLanKbitCount_Object = MibScalar
rxEtherLanKbitCount = _RxEtherLanKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 65),
    _RxEtherLanKbitCount_Type()
)
rxEtherLanKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanKbitCount.setStatus("current")
_RxEtherLanTotalPacketCount_Type = Counter64
_RxEtherLanTotalPacketCount_Object = MibScalar
rxEtherLanTotalPacketCount = _RxEtherLanTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 66),
    _RxEtherLanTotalPacketCount_Type()
)
rxEtherLanTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanTotalPacketCount.setStatus("current")
_RxEtherLanErrorPacketCount_Type = Counter64
_RxEtherLanErrorPacketCount_Object = MibScalar
rxEtherLanErrorPacketCount = _RxEtherLanErrorPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 67),
    _RxEtherLanErrorPacketCount_Type()
)
rxEtherLanErrorPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanErrorPacketCount.setStatus("current")
_RxEtherLanDroppedPacketCount_Type = Counter64
_RxEtherLanDroppedPacketCount_Object = MibScalar
rxEtherLanDroppedPacketCount = _RxEtherLanDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 68),
    _RxEtherLanDroppedPacketCount_Type()
)
rxEtherLanDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanDroppedPacketCount.setStatus("current")
_RxEtherLanMulticastPacketCount_Type = Counter64
_RxEtherLanMulticastPacketCount_Object = MibScalar
rxEtherLanMulticastPacketCount = _RxEtherLanMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 69),
    _RxEtherLanMulticastPacketCount_Type()
)
rxEtherLanMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanMulticastPacketCount.setStatus("current")
_RxEtherLanBroadcastPacketCount_Type = Counter64
_RxEtherLanBroadcastPacketCount_Object = MibScalar
rxEtherLanBroadcastPacketCount = _RxEtherLanBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 70),
    _RxEtherLanBroadcastPacketCount_Type()
)
rxEtherLanBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanBroadcastPacketCount.setStatus("current")
_RxEtherLanMultiBroadcastKbitCount_Type = Counter64
_RxEtherLanMultiBroadcastKbitCount_Object = MibScalar
rxEtherLanMultiBroadcastKbitCount = _RxEtherLanMultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 71),
    _RxEtherLanMultiBroadcastKbitCount_Type()
)
rxEtherLanMultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxEtherLanMultiBroadcastKbitCount.setStatus("current")
_TxEtherLanKbitCount_Type = Counter64
_TxEtherLanKbitCount_Object = MibScalar
txEtherLanKbitCount = _TxEtherLanKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 72),
    _TxEtherLanKbitCount_Type()
)
txEtherLanKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanKbitCount.setStatus("current")
_TxEtherLanTotalPacketCount_Type = Counter64
_TxEtherLanTotalPacketCount_Object = MibScalar
txEtherLanTotalPacketCount = _TxEtherLanTotalPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 73),
    _TxEtherLanTotalPacketCount_Type()
)
txEtherLanTotalPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanTotalPacketCount.setStatus("current")
_TxEtherLanErrorPacketCount_Type = Counter64
_TxEtherLanErrorPacketCount_Object = MibScalar
txEtherLanErrorPacketCount = _TxEtherLanErrorPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 74),
    _TxEtherLanErrorPacketCount_Type()
)
txEtherLanErrorPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanErrorPacketCount.setStatus("current")
_TxEtherLanDroppedPacketCount_Type = Counter64
_TxEtherLanDroppedPacketCount_Object = MibScalar
txEtherLanDroppedPacketCount = _TxEtherLanDroppedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 75),
    _TxEtherLanDroppedPacketCount_Type()
)
txEtherLanDroppedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanDroppedPacketCount.setStatus("current")
_TxEtherLanMulticastPacketCount_Type = Counter64
_TxEtherLanMulticastPacketCount_Object = MibScalar
txEtherLanMulticastPacketCount = _TxEtherLanMulticastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 76),
    _TxEtherLanMulticastPacketCount_Type()
)
txEtherLanMulticastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanMulticastPacketCount.setStatus("current")
_TxEtherLanBroadcastPacketCount_Type = Counter64
_TxEtherLanBroadcastPacketCount_Object = MibScalar
txEtherLanBroadcastPacketCount = _TxEtherLanBroadcastPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 77),
    _TxEtherLanBroadcastPacketCount_Type()
)
txEtherLanBroadcastPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanBroadcastPacketCount.setStatus("current")
_TxEtherLanMultiBroadcastKbitCount_Type = Counter64
_TxEtherLanMultiBroadcastKbitCount_Object = MibScalar
txEtherLanMultiBroadcastKbitCount = _TxEtherLanMultiBroadcastKbitCount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 78),
    _TxEtherLanMultiBroadcastKbitCount_Type()
)
txEtherLanMultiBroadcastKbitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txEtherLanMultiBroadcastKbitCount.setStatus("current")
_CambiumStatsResetTimer_Type = TimeTicks
_CambiumStatsResetTimer_Object = MibScalar
cambiumStatsResetTimer = _CambiumStatsResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 79),
    _CambiumStatsResetTimer_Type()
)
cambiumStatsResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumStatsResetTimer.setStatus("current")
_UlWLanMCS00Packets_Type = Counter64
_UlWLanMCS00Packets_Object = MibScalar
ulWLanMCS00Packets = _UlWLanMCS00Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 80),
    _UlWLanMCS00Packets_Type()
)
ulWLanMCS00Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS00Packets.setStatus("current")
_UlWLanMCS01Packets_Type = Counter64
_UlWLanMCS01Packets_Object = MibScalar
ulWLanMCS01Packets = _UlWLanMCS01Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 81),
    _UlWLanMCS01Packets_Type()
)
ulWLanMCS01Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS01Packets.setStatus("current")
_UlWLanMCS02Packets_Type = Counter64
_UlWLanMCS02Packets_Object = MibScalar
ulWLanMCS02Packets = _UlWLanMCS02Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 82),
    _UlWLanMCS02Packets_Type()
)
ulWLanMCS02Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS02Packets.setStatus("current")
_UlWLanMCS03Packets_Type = Counter64
_UlWLanMCS03Packets_Object = MibScalar
ulWLanMCS03Packets = _UlWLanMCS03Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 83),
    _UlWLanMCS03Packets_Type()
)
ulWLanMCS03Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS03Packets.setStatus("current")
_UlWLanMCS04Packets_Type = Counter64
_UlWLanMCS04Packets_Object = MibScalar
ulWLanMCS04Packets = _UlWLanMCS04Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 84),
    _UlWLanMCS04Packets_Type()
)
ulWLanMCS04Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS04Packets.setStatus("current")
_UlWLanMCS05Packets_Type = Counter64
_UlWLanMCS05Packets_Object = MibScalar
ulWLanMCS05Packets = _UlWLanMCS05Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 85),
    _UlWLanMCS05Packets_Type()
)
ulWLanMCS05Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS05Packets.setStatus("current")
_UlWLanMCS06Packets_Type = Counter64
_UlWLanMCS06Packets_Object = MibScalar
ulWLanMCS06Packets = _UlWLanMCS06Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 86),
    _UlWLanMCS06Packets_Type()
)
ulWLanMCS06Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS06Packets.setStatus("current")
_UlWLanMCS07Packets_Type = Counter64
_UlWLanMCS07Packets_Object = MibScalar
ulWLanMCS07Packets = _UlWLanMCS07Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 87),
    _UlWLanMCS07Packets_Type()
)
ulWLanMCS07Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS07Packets.setStatus("current")
_UlWLanMCS08Packets_Type = Counter64
_UlWLanMCS08Packets_Object = MibScalar
ulWLanMCS08Packets = _UlWLanMCS08Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 88),
    _UlWLanMCS08Packets_Type()
)
ulWLanMCS08Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS08Packets.setStatus("current")
_UlWLanMCS09Packets_Type = Counter64
_UlWLanMCS09Packets_Object = MibScalar
ulWLanMCS09Packets = _UlWLanMCS09Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 89),
    _UlWLanMCS09Packets_Type()
)
ulWLanMCS09Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS09Packets.setStatus("current")
_UlWLanMCS10Packets_Type = Counter64
_UlWLanMCS10Packets_Object = MibScalar
ulWLanMCS10Packets = _UlWLanMCS10Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 90),
    _UlWLanMCS10Packets_Type()
)
ulWLanMCS10Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS10Packets.setStatus("current")
_UlWLanMCS11Packets_Type = Counter64
_UlWLanMCS11Packets_Object = MibScalar
ulWLanMCS11Packets = _UlWLanMCS11Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 91),
    _UlWLanMCS11Packets_Type()
)
ulWLanMCS11Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS11Packets.setStatus("current")
_UlWLanMCS12Packets_Type = Counter64
_UlWLanMCS12Packets_Object = MibScalar
ulWLanMCS12Packets = _UlWLanMCS12Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 92),
    _UlWLanMCS12Packets_Type()
)
ulWLanMCS12Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS12Packets.setStatus("current")
_UlWLanMCS13Packets_Type = Counter64
_UlWLanMCS13Packets_Object = MibScalar
ulWLanMCS13Packets = _UlWLanMCS13Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 93),
    _UlWLanMCS13Packets_Type()
)
ulWLanMCS13Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS13Packets.setStatus("current")
_UlWLanMCS14Packets_Type = Counter64
_UlWLanMCS14Packets_Object = MibScalar
ulWLanMCS14Packets = _UlWLanMCS14Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 94),
    _UlWLanMCS14Packets_Type()
)
ulWLanMCS14Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS14Packets.setStatus("current")
_UlWLanMCS15Packets_Type = Counter64
_UlWLanMCS15Packets_Object = MibScalar
ulWLanMCS15Packets = _UlWLanMCS15Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 95),
    _UlWLanMCS15Packets_Type()
)
ulWLanMCS15Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulWLanMCS15Packets.setStatus("current")
_DlWLanMCS00Packets_Type = Counter64
_DlWLanMCS00Packets_Object = MibScalar
dlWLanMCS00Packets = _DlWLanMCS00Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 96),
    _DlWLanMCS00Packets_Type()
)
dlWLanMCS00Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS00Packets.setStatus("current")
_DlWLanMCS01Packets_Type = Counter64
_DlWLanMCS01Packets_Object = MibScalar
dlWLanMCS01Packets = _DlWLanMCS01Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 97),
    _DlWLanMCS01Packets_Type()
)
dlWLanMCS01Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS01Packets.setStatus("current")
_DlWLanMCS02Packets_Type = Counter64
_DlWLanMCS02Packets_Object = MibScalar
dlWLanMCS02Packets = _DlWLanMCS02Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 98),
    _DlWLanMCS02Packets_Type()
)
dlWLanMCS02Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS02Packets.setStatus("current")
_DlWLanMCS03Packets_Type = Counter64
_DlWLanMCS03Packets_Object = MibScalar
dlWLanMCS03Packets = _DlWLanMCS03Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 99),
    _DlWLanMCS03Packets_Type()
)
dlWLanMCS03Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS03Packets.setStatus("current")
_DlWLanMCS04Packets_Type = Counter64
_DlWLanMCS04Packets_Object = MibScalar
dlWLanMCS04Packets = _DlWLanMCS04Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 100),
    _DlWLanMCS04Packets_Type()
)
dlWLanMCS04Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS04Packets.setStatus("current")
_DlWLanMCS05Packets_Type = Counter64
_DlWLanMCS05Packets_Object = MibScalar
dlWLanMCS05Packets = _DlWLanMCS05Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 101),
    _DlWLanMCS05Packets_Type()
)
dlWLanMCS05Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS05Packets.setStatus("current")
_DlWLanMCS06Packets_Type = Counter64
_DlWLanMCS06Packets_Object = MibScalar
dlWLanMCS06Packets = _DlWLanMCS06Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 102),
    _DlWLanMCS06Packets_Type()
)
dlWLanMCS06Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS06Packets.setStatus("current")
_DlWLanMCS07Packets_Type = Counter64
_DlWLanMCS07Packets_Object = MibScalar
dlWLanMCS07Packets = _DlWLanMCS07Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 103),
    _DlWLanMCS07Packets_Type()
)
dlWLanMCS07Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS07Packets.setStatus("current")
_DlWLanMCS08Packets_Type = Counter64
_DlWLanMCS08Packets_Object = MibScalar
dlWLanMCS08Packets = _DlWLanMCS08Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 104),
    _DlWLanMCS08Packets_Type()
)
dlWLanMCS08Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS08Packets.setStatus("current")
_DlWLanMCS09Packets_Type = Counter64
_DlWLanMCS09Packets_Object = MibScalar
dlWLanMCS09Packets = _DlWLanMCS09Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 105),
    _DlWLanMCS09Packets_Type()
)
dlWLanMCS09Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS09Packets.setStatus("current")
_DlWLanMCS10Packets_Type = Counter64
_DlWLanMCS10Packets_Object = MibScalar
dlWLanMCS10Packets = _DlWLanMCS10Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 106),
    _DlWLanMCS10Packets_Type()
)
dlWLanMCS10Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS10Packets.setStatus("current")
_DlWLanMCS11Packets_Type = Counter64
_DlWLanMCS11Packets_Object = MibScalar
dlWLanMCS11Packets = _DlWLanMCS11Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 107),
    _DlWLanMCS11Packets_Type()
)
dlWLanMCS11Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS11Packets.setStatus("current")
_DlWLanMCS12Packets_Type = Counter64
_DlWLanMCS12Packets_Object = MibScalar
dlWLanMCS12Packets = _DlWLanMCS12Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 108),
    _DlWLanMCS12Packets_Type()
)
dlWLanMCS12Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS12Packets.setStatus("current")
_DlWLanMCS13Packets_Type = Counter64
_DlWLanMCS13Packets_Object = MibScalar
dlWLanMCS13Packets = _DlWLanMCS13Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 109),
    _DlWLanMCS13Packets_Type()
)
dlWLanMCS13Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS13Packets.setStatus("current")
_DlWLanMCS14Packets_Type = Counter64
_DlWLanMCS14Packets_Object = MibScalar
dlWLanMCS14Packets = _DlWLanMCS14Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 110),
    _DlWLanMCS14Packets_Type()
)
dlWLanMCS14Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS14Packets.setStatus("current")
_DlWLanMCS15Packets_Type = Counter64
_DlWLanMCS15Packets_Object = MibScalar
dlWLanMCS15Packets = _DlWLanMCS15Packets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 1, 111),
    _DlWLanMCS15Packets_Type()
)
dlWLanMCS15Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlWLanMCS15Packets.setStatus("current")
_CambiumRealTimeStatsMonitoring_ObjectIdentity = ObjectIdentity
cambiumRealTimeStatsMonitoring = _CambiumRealTimeStatsMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 2)
)
_CambiumAdvancedPerformanceMonitoring_ObjectIdentity = ObjectIdentity
cambiumAdvancedPerformanceMonitoring = _CambiumAdvancedPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 2, 3)
)
_Cambiumpmp80211SystemConfiguration_ObjectIdentity = ObjectIdentity
cambiumpmp80211SystemConfiguration = _Cambiumpmp80211SystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3)
)
_CambiumSystemLog_ObjectIdentity = ObjectIdentity
cambiumSystemLog = _CambiumSystemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1)
)
_SyslogServerIPFirst_Type = IpAddress
_SyslogServerIPFirst_Object = MibScalar
syslogServerIPFirst = _SyslogServerIPFirst_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 1),
    _SyslogServerIPFirst_Type()
)
syslogServerIPFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIPFirst.setStatus("current")
_SyslogServerIPSecond_Type = IpAddress
_SyslogServerIPSecond_Object = MibScalar
syslogServerIPSecond = _SyslogServerIPSecond_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 2),
    _SyslogServerIPSecond_Type()
)
syslogServerIPSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIPSecond.setStatus("current")
_SyslogServerIPThird_Type = IpAddress
_SyslogServerIPThird_Object = MibScalar
syslogServerIPThird = _SyslogServerIPThird_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 3),
    _SyslogServerIPThird_Type()
)
syslogServerIPThird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIPThird.setStatus("current")
_SyslogServerIPFourth_Type = IpAddress
_SyslogServerIPFourth_Object = MibScalar
syslogServerIPFourth = _SyslogServerIPFourth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 4),
    _SyslogServerIPFourth_Type()
)
syslogServerIPFourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIPFourth.setStatus("current")


class _SyslogServerLogToWeb_Type(Integer32):
    """Custom type syslogServerLogToWeb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SyslogServerLogToWeb_Type.__name__ = "Integer32"
_SyslogServerLogToWeb_Object = MibScalar
syslogServerLogToWeb = _SyslogServerLogToWeb_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 5),
    _SyslogServerLogToWeb_Type()
)
syslogServerLogToWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerLogToWeb.setStatus("current")


class _SyslogServerLogMask_Type(Integer32):
    """Custom type syslogServerLogMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SyslogServerLogMask_Type.__name__ = "Integer32"
_SyslogServerLogMask_Object = MibScalar
syslogServerLogMask = _SyslogServerLogMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 1, 6),
    _SyslogServerLogMask_Type()
)
syslogServerLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerLogMask.setStatus("current")
_CambiumDHCP_ObjectIdentity = ObjectIdentity
cambiumDHCP = _CambiumDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2)
)


class _DhcpLanEnable_Type(Integer32):
    """Custom type dhcpLanEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DhcpLanEnable_Type.__name__ = "Integer32"
_DhcpLanEnable_Object = MibScalar
dhcpLanEnable = _DhcpLanEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 1),
    _DhcpLanEnable_Type()
)
dhcpLanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanEnable.setStatus("current")


class _DhcpLanStart_Type(Integer32):
    """Custom type dhcpLanStart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_DhcpLanStart_Type.__name__ = "Integer32"
_DhcpLanStart_Object = MibScalar
dhcpLanStart = _DhcpLanStart_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 2),
    _DhcpLanStart_Type()
)
dhcpLanStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanStart.setStatus("current")


class _DhcpLanLimit_Type(Integer32):
    """Custom type dhcpLanLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_DhcpLanLimit_Type.__name__ = "Integer32"
_DhcpLanLimit_Object = MibScalar
dhcpLanLimit = _DhcpLanLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 3),
    _DhcpLanLimit_Type()
)
dhcpLanLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanLimit.setStatus("current")


class _DhcpLanLeasetime_Type(Integer32):
    """Custom type dhcpLanLeasetime based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_DhcpLanLeasetime_Type.__name__ = "Integer32"
_DhcpLanLeasetime_Object = MibScalar
dhcpLanLeasetime = _DhcpLanLeasetime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 4),
    _DhcpLanLeasetime_Type()
)
dhcpLanLeasetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanLeasetime.setStatus("current")
_DhcpLanHostTable_Object = MibTable
dhcpLanHostTable = _DhcpLanHostTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5)
)
if mibBuilder.loadTexts:
    dhcpLanHostTable.setStatus("current")
_DhcpLanHostEntry_Object = MibTableRow
dhcpLanHostEntry = _DhcpLanHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1)
)
dhcpLanHostEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "dhcpLanHostIndex"),
)
if mibBuilder.loadTexts:
    dhcpLanHostEntry.setStatus("current")


class _DhcpLanHostIndex_Type(Integer32):
    """Custom type dhcpLanHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DhcpLanHostIndex_Type.__name__ = "Integer32"
_DhcpLanHostIndex_Object = MibTableColumn
dhcpLanHostIndex = _DhcpLanHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1, 1),
    _DhcpLanHostIndex_Type()
)
dhcpLanHostIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanHostIndex.setStatus("current")
_DhcpLanHostIP_Type = IpAddress
_DhcpLanHostIP_Object = MibTableColumn
dhcpLanHostIP = _DhcpLanHostIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1, 2),
    _DhcpLanHostIP_Type()
)
dhcpLanHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanHostIP.setStatus("current")


class _DhcpLanHostMAC_Type(DisplayString):
    """Custom type dhcpLanHostMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_DhcpLanHostMAC_Type.__name__ = "DisplayString"
_DhcpLanHostMAC_Object = MibTableColumn
dhcpLanHostMAC = _DhcpLanHostMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1, 3),
    _DhcpLanHostMAC_Type()
)
dhcpLanHostMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanHostMAC.setStatus("current")


class _DhcpLanHostName_Type(DisplayString):
    """Custom type dhcpLanHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_DhcpLanHostName_Type.__name__ = "DisplayString"
_DhcpLanHostName_Object = MibTableColumn
dhcpLanHostName = _DhcpLanHostName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 5, 1, 4),
    _DhcpLanHostName_Type()
)
dhcpLanHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLanHostName.setStatus("current")


class _DhcpOption82_Type(Integer32):
    """Custom type dhcpOption82 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DhcpOption82_Type.__name__ = "Integer32"
_DhcpOption82_Object = MibScalar
dhcpOption82 = _DhcpOption82_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 2, 6),
    _DhcpOption82_Type()
)
dhcpOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82.setStatus("current")
_CambiumSSHServer_ObjectIdentity = ObjectIdentity
cambiumSSHServer = _CambiumSSHServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 3)
)


class _CambiumSSHServerEnable_Type(Integer32):
    """Custom type cambiumSSHServerEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumSSHServerEnable_Type.__name__ = "Integer32"
_CambiumSSHServerEnable_Object = MibScalar
cambiumSSHServerEnable = _CambiumSSHServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 3, 1),
    _CambiumSSHServerEnable_Type()
)
cambiumSSHServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSSHServerEnable.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4)
)


class _NetworkMode_Type(Integer32):
    """Custom type networkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_NetworkMode_Type.__name__ = "Integer32"
_NetworkMode_Object = MibScalar
networkMode = _NetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 1),
    _NetworkMode_Type()
)
networkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkMode.setStatus("current")
_NetworkLan_ObjectIdentity = ObjectIdentity
networkLan = _NetworkLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2)
)


class _NetworkLanIPAddressMode_Type(Integer32):
    """Custom type networkLanIPAddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkLanIPAddressMode_Type.__name__ = "Integer32"
_NetworkLanIPAddressMode_Object = MibScalar
networkLanIPAddressMode = _NetworkLanIPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 1),
    _NetworkLanIPAddressMode_Type()
)
networkLanIPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanIPAddressMode.setStatus("current")
_NetworkLanIPAddr_Type = IpAddress
_NetworkLanIPAddr_Object = MibScalar
networkLanIPAddr = _NetworkLanIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 2),
    _NetworkLanIPAddr_Type()
)
networkLanIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanIPAddr.setStatus("current")
_NetworkLanNetmask_Type = IpAddress
_NetworkLanNetmask_Object = MibScalar
networkLanNetmask = _NetworkLanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 3),
    _NetworkLanNetmask_Type()
)
networkLanNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanNetmask.setStatus("current")
_NetworkLanGatewayIP_Type = IpAddress
_NetworkLanGatewayIP_Object = MibScalar
networkLanGatewayIP = _NetworkLanGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 4),
    _NetworkLanGatewayIP_Type()
)
networkLanGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanGatewayIP.setStatus("current")
_NetworkLanDNSIPAddr_Type = IpAddress
_NetworkLanDNSIPAddr_Object = MibScalar
networkLanDNSIPAddr = _NetworkLanDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 5),
    _NetworkLanDNSIPAddr_Type()
)
networkLanDNSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDNSIPAddr.setStatus("obsolete")


class _NetworkLanMTU_Type(Integer32):
    """Custom type networkLanMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 1700),
    )


_NetworkLanMTU_Type.__name__ = "Integer32"
_NetworkLanMTU_Object = MibScalar
networkLanMTU = _NetworkLanMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 6),
    _NetworkLanMTU_Type()
)
networkLanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanMTU.setStatus("current")
_NetworkLanDNSIPAddrPrimary_Type = IpAddress
_NetworkLanDNSIPAddrPrimary_Object = MibScalar
networkLanDNSIPAddrPrimary = _NetworkLanDNSIPAddrPrimary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 7),
    _NetworkLanDNSIPAddrPrimary_Type()
)
networkLanDNSIPAddrPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDNSIPAddrPrimary.setStatus("current")
_NetworkLanDNSIPAddrSecondary_Type = IpAddress
_NetworkLanDNSIPAddrSecondary_Object = MibScalar
networkLanDNSIPAddrSecondary = _NetworkLanDNSIPAddrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 8),
    _NetworkLanDNSIPAddrSecondary_Type()
)
networkLanDNSIPAddrSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDNSIPAddrSecondary.setStatus("current")


class _NetworkLanAutoNegotiation_Type(Integer32):
    """Custom type networkLanAutoNegotiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLanAutoNegotiation_Type.__name__ = "Integer32"
_NetworkLanAutoNegotiation_Object = MibScalar
networkLanAutoNegotiation = _NetworkLanAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 9),
    _NetworkLanAutoNegotiation_Type()
)
networkLanAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanAutoNegotiation.setStatus("current")


class _NetworkLanSpeed_Type(Integer32):
    """Custom type networkLanSpeed based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_NetworkLanSpeed_Type.__name__ = "Integer32"
_NetworkLanSpeed_Object = MibScalar
networkLanSpeed = _NetworkLanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 10),
    _NetworkLanSpeed_Type()
)
networkLanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanSpeed.setStatus("current")


class _NetworkLanDuplex_Type(Integer32):
    """Custom type networkLanDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLanDuplex_Type.__name__ = "Integer32"
_NetworkLanDuplex_Object = MibScalar
networkLanDuplex = _NetworkLanDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 11),
    _NetworkLanDuplex_Type()
)
networkLanDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDuplex.setStatus("current")


class _NetworkBroadcastStormEnabled_Type(Integer32):
    """Custom type networkBroadcastStormEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkBroadcastStormEnabled_Type.__name__ = "Integer32"
_NetworkBroadcastStormEnabled_Object = MibScalar
networkBroadcastStormEnabled = _NetworkBroadcastStormEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 12),
    _NetworkBroadcastStormEnabled_Type()
)
networkBroadcastStormEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBroadcastStormEnabled.setStatus("current")


class _NetworkBroadcastStormRate_Type(Integer32):
    """Custom type networkBroadcastStormRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_NetworkBroadcastStormRate_Type.__name__ = "Integer32"
_NetworkBroadcastStormRate_Object = MibScalar
networkBroadcastStormRate = _NetworkBroadcastStormRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 13),
    _NetworkBroadcastStormRate_Type()
)
networkBroadcastStormRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBroadcastStormRate.setStatus("current")


class _NetworkLan2Enabled_Type(Integer32):
    """Custom type networkLan2Enabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLan2Enabled_Type.__name__ = "Integer32"
_NetworkLan2Enabled_Object = MibScalar
networkLan2Enabled = _NetworkLan2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 20),
    _NetworkLan2Enabled_Type()
)
networkLan2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2Enabled.setStatus("current")


class _NetworkLan2AutoNegotiation_Type(Integer32):
    """Custom type networkLan2AutoNegotiation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLan2AutoNegotiation_Type.__name__ = "Integer32"
_NetworkLan2AutoNegotiation_Object = MibScalar
networkLan2AutoNegotiation = _NetworkLan2AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 21),
    _NetworkLan2AutoNegotiation_Type()
)
networkLan2AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2AutoNegotiation.setStatus("current")


class _NetworkLan2Speed_Type(Integer32):
    """Custom type networkLan2Speed based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
    )


_NetworkLan2Speed_Type.__name__ = "Integer32"
_NetworkLan2Speed_Object = MibScalar
networkLan2Speed = _NetworkLan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 22),
    _NetworkLan2Speed_Type()
)
networkLan2Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2Speed.setStatus("current")


class _NetworkLan2Duplex_Type(Integer32):
    """Custom type networkLan2Duplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLan2Duplex_Type.__name__ = "Integer32"
_NetworkLan2Duplex_Object = MibScalar
networkLan2Duplex = _NetworkLan2Duplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 23),
    _NetworkLan2Duplex_Type()
)
networkLan2Duplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2Duplex.setStatus("current")


class _NetworkLan2PoEEnabled_Type(Integer32):
    """Custom type networkLan2PoEEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLan2PoEEnabled_Type.__name__ = "Integer32"
_NetworkLan2PoEEnabled_Object = MibScalar
networkLan2PoEEnabled = _NetworkLan2PoEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 24),
    _NetworkLan2PoEEnabled_Type()
)
networkLan2PoEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLan2PoEEnabled.setStatus("current")


class _NetworkLanEnabled_Type(Integer32):
    """Custom type networkLanEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkLanEnabled_Type.__name__ = "Integer32"
_NetworkLanEnabled_Object = MibScalar
networkLanEnabled = _NetworkLanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 2, 25),
    _NetworkLanEnabled_Type()
)
networkLanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanEnabled.setStatus("current")
_NetworkWan_ObjectIdentity = ObjectIdentity
networkWan = _NetworkWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3)
)


class _NetworkWanIPAddressMode_Type(Integer32):
    """Custom type networkWanIPAddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkWanIPAddressMode_Type.__name__ = "Integer32"
_NetworkWanIPAddressMode_Object = MibScalar
networkWanIPAddressMode = _NetworkWanIPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 1),
    _NetworkWanIPAddressMode_Type()
)
networkWanIPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanIPAddressMode.setStatus("current")
_NetworkWanIPAddr_Type = IpAddress
_NetworkWanIPAddr_Object = MibScalar
networkWanIPAddr = _NetworkWanIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 2),
    _NetworkWanIPAddr_Type()
)
networkWanIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanIPAddr.setStatus("current")
_NetworkWanNetmask_Type = IpAddress
_NetworkWanNetmask_Object = MibScalar
networkWanNetmask = _NetworkWanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 3),
    _NetworkWanNetmask_Type()
)
networkWanNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanNetmask.setStatus("current")
_NetworkWanGatewayIP_Type = IpAddress
_NetworkWanGatewayIP_Object = MibScalar
networkWanGatewayIP = _NetworkWanGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 4),
    _NetworkWanGatewayIP_Type()
)
networkWanGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanGatewayIP.setStatus("current")
_NetworkWanDNSIPAddr_Type = IpAddress
_NetworkWanDNSIPAddr_Object = MibScalar
networkWanDNSIPAddr = _NetworkWanDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 5),
    _NetworkWanDNSIPAddr_Type()
)
networkWanDNSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanDNSIPAddr.setStatus("obsolete")


class _NetworkWanMTU_Type(Integer32):
    """Custom type networkWanMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 1700),
    )


_NetworkWanMTU_Type.__name__ = "Integer32"
_NetworkWanMTU_Object = MibScalar
networkWanMTU = _NetworkWanMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 6),
    _NetworkWanMTU_Type()
)
networkWanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanMTU.setStatus("current")
_NetworkWanDNSIPAddrPrimary_Type = IpAddress
_NetworkWanDNSIPAddrPrimary_Object = MibScalar
networkWanDNSIPAddrPrimary = _NetworkWanDNSIPAddrPrimary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 7),
    _NetworkWanDNSIPAddrPrimary_Type()
)
networkWanDNSIPAddrPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanDNSIPAddrPrimary.setStatus("current")
_NetworkWanDNSIPAddrSecondary_Type = IpAddress
_NetworkWanDNSIPAddrSecondary_Object = MibScalar
networkWanDNSIPAddrSecondary = _NetworkWanDNSIPAddrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 8),
    _NetworkWanDNSIPAddrSecondary_Type()
)
networkWanDNSIPAddrSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanDNSIPAddrSecondary.setStatus("current")


class _NetworkWanPPPoE_Type(Integer32):
    """Custom type networkWanPPPoE based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkWanPPPoE_Type.__name__ = "Integer32"
_NetworkWanPPPoE_Object = MibScalar
networkWanPPPoE = _NetworkWanPPPoE_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 9),
    _NetworkWanPPPoE_Type()
)
networkWanPPPoE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoE.setStatus("current")


class _NetworkWanPPPoEUsername_Type(DisplayString):
    """Custom type networkWanPPPoEUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetworkWanPPPoEUsername_Type.__name__ = "DisplayString"
_NetworkWanPPPoEUsername_Object = MibScalar
networkWanPPPoEUsername = _NetworkWanPPPoEUsername_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 10),
    _NetworkWanPPPoEUsername_Type()
)
networkWanPPPoEUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEUsername.setStatus("current")


class _NetworkWanPPPoEPassword_Type(DisplayString):
    """Custom type networkWanPPPoEPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetworkWanPPPoEPassword_Type.__name__ = "DisplayString"
_NetworkWanPPPoEPassword_Object = MibScalar
networkWanPPPoEPassword = _NetworkWanPPPoEPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 11),
    _NetworkWanPPPoEPassword_Type()
)
networkWanPPPoEPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEPassword.setStatus("current")


class _NetworkWanPPPoEAC_Type(DisplayString):
    """Custom type networkWanPPPoEAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetworkWanPPPoEAC_Type.__name__ = "DisplayString"
_NetworkWanPPPoEAC_Object = MibScalar
networkWanPPPoEAC = _NetworkWanPPPoEAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 12),
    _NetworkWanPPPoEAC_Type()
)
networkWanPPPoEAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEAC.setStatus("current")


class _NetworkWanPPPoEService_Type(DisplayString):
    """Custom type networkWanPPPoEService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetworkWanPPPoEService_Type.__name__ = "DisplayString"
_NetworkWanPPPoEService_Object = MibScalar
networkWanPPPoEService = _NetworkWanPPPoEService_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 13),
    _NetworkWanPPPoEService_Type()
)
networkWanPPPoEService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEService.setStatus("current")


class _NetworkWanPPPoEAuth_Type(Integer32):
    """Custom type networkWanPPPoEAuth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkWanPPPoEAuth_Type.__name__ = "Integer32"
_NetworkWanPPPoEAuth_Object = MibScalar
networkWanPPPoEAuth = _NetworkWanPPPoEAuth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 14),
    _NetworkWanPPPoEAuth_Type()
)
networkWanPPPoEAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEAuth.setStatus("current")


class _NetworkWanPPPoEMTU_Type(Integer32):
    """Custom type networkWanPPPoEMTU based on Integer32"""
    defaultValue = 1492

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 1492),
    )


_NetworkWanPPPoEMTU_Type.__name__ = "Integer32"
_NetworkWanPPPoEMTU_Object = MibScalar
networkWanPPPoEMTU = _NetworkWanPPPoEMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 15),
    _NetworkWanPPPoEMTU_Type()
)
networkWanPPPoEMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEMTU.setStatus("current")


class _NetworkWanPPPoEKeepAlive_Type(Integer32):
    """Custom type networkWanPPPoEKeepAlive based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 180),
    )


_NetworkWanPPPoEKeepAlive_Type.__name__ = "Integer32"
_NetworkWanPPPoEKeepAlive_Object = MibScalar
networkWanPPPoEKeepAlive = _NetworkWanPPPoEKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 16),
    _NetworkWanPPPoEKeepAlive_Type()
)
networkWanPPPoEKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEKeepAlive.setStatus("current")


class _NetworkWanPPPoEMSSClamping_Type(Integer32):
    """Custom type networkWanPPPoEMSSClamping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkWanPPPoEMSSClamping_Type.__name__ = "Integer32"
_NetworkWanPPPoEMSSClamping_Object = MibScalar
networkWanPPPoEMSSClamping = _NetworkWanPPPoEMSSClamping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 3, 17),
    _NetworkWanPPPoEMSSClamping_Type()
)
networkWanPPPoEMSSClamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkWanPPPoEMSSClamping.setStatus("current")
_MgmtVLAN_ObjectIdentity = ObjectIdentity
mgmtVLAN = _MgmtVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 4)
)


class _MgmtVLANEnable_Type(Integer32):
    """Custom type mgmtVLANEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_MgmtVLANEnable_Type.__name__ = "Integer32"
_MgmtVLANEnable_Object = MibScalar
mgmtVLANEnable = _MgmtVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 4, 1),
    _MgmtVLANEnable_Type()
)
mgmtVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtVLANEnable.setStatus("current")


class _MgmtVLANVID_Type(Integer32):
    """Custom type mgmtVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MgmtVLANVID_Type.__name__ = "Integer32"
_MgmtVLANVID_Object = MibScalar
mgmtVLANVID = _MgmtVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 4, 2),
    _MgmtVLANVID_Type()
)
mgmtVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtVLANVID.setStatus("current")


class _MgmtVLANVP_Type(Integer32):
    """Custom type mgmtVLANVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgmtVLANVP_Type.__name__ = "Integer32"
_MgmtVLANVP_Object = MibScalar
mgmtVLANVP = _MgmtVLANVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 4, 3),
    _MgmtVLANVP_Type()
)
mgmtVLANVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtVLANVP.setStatus("current")
_DataVLAN_ObjectIdentity = ObjectIdentity
dataVLAN = _DataVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 5)
)


class _DataVLANEnable_Type(Integer32):
    """Custom type dataVLANEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DataVLANEnable_Type.__name__ = "Integer32"
_DataVLANEnable_Object = MibScalar
dataVLANEnable = _DataVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 5, 1),
    _DataVLANEnable_Type()
)
dataVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataVLANEnable.setStatus("current")


class _DataVLANVID_Type(Integer32):
    """Custom type dataVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_DataVLANVID_Type.__name__ = "Integer32"
_DataVLANVID_Object = MibScalar
dataVLANVID = _DataVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 5, 2),
    _DataVLANVID_Type()
)
dataVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataVLANVID.setStatus("current")


class _DataVLANVP_Type(Integer32):
    """Custom type dataVLANVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DataVLANVP_Type.__name__ = "Integer32"
_DataVLANVP_Object = MibScalar
dataVLANVP = _DataVLANVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 5, 3),
    _DataVLANVP_Type()
)
dataVLANVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataVLANVP.setStatus("current")


class _NetworkSTP_Type(Integer32):
    """Custom type networkSTP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkSTP_Type.__name__ = "Integer32"
_NetworkSTP_Object = MibScalar
networkSTP = _NetworkSTP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 6),
    _NetworkSTP_Type()
)
networkSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkSTP.setStatus("current")
_NetworkBridge_ObjectIdentity = ObjectIdentity
networkBridge = _NetworkBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7)
)


class _NetworkBridgeIPAddressMode_Type(Integer32):
    """Custom type networkBridgeIPAddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_NetworkBridgeIPAddressMode_Type.__name__ = "Integer32"
_NetworkBridgeIPAddressMode_Object = MibScalar
networkBridgeIPAddressMode = _NetworkBridgeIPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 1),
    _NetworkBridgeIPAddressMode_Type()
)
networkBridgeIPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeIPAddressMode.setStatus("current")
_NetworkBridgeIPAddr_Type = IpAddress
_NetworkBridgeIPAddr_Object = MibScalar
networkBridgeIPAddr = _NetworkBridgeIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 2),
    _NetworkBridgeIPAddr_Type()
)
networkBridgeIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeIPAddr.setStatus("current")
_NetworkBridgeNetmask_Type = IpAddress
_NetworkBridgeNetmask_Object = MibScalar
networkBridgeNetmask = _NetworkBridgeNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 3),
    _NetworkBridgeNetmask_Type()
)
networkBridgeNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeNetmask.setStatus("current")
_NetworkBridgeGatewayIP_Type = IpAddress
_NetworkBridgeGatewayIP_Object = MibScalar
networkBridgeGatewayIP = _NetworkBridgeGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 4),
    _NetworkBridgeGatewayIP_Type()
)
networkBridgeGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeGatewayIP.setStatus("current")
_NetworkBridgeDNSIPAddr_Type = IpAddress
_NetworkBridgeDNSIPAddr_Object = MibScalar
networkBridgeDNSIPAddr = _NetworkBridgeDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 5),
    _NetworkBridgeDNSIPAddr_Type()
)
networkBridgeDNSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeDNSIPAddr.setStatus("obsolete")


class _NetworkBridgeMTU_Type(Integer32):
    """Custom type networkBridgeMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 1700),
    )


_NetworkBridgeMTU_Type.__name__ = "Integer32"
_NetworkBridgeMTU_Object = MibScalar
networkBridgeMTU = _NetworkBridgeMTU_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 6),
    _NetworkBridgeMTU_Type()
)
networkBridgeMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeMTU.setStatus("current")
_NetworkBridgeDNSIPAddrPrimary_Type = IpAddress
_NetworkBridgeDNSIPAddrPrimary_Object = MibScalar
networkBridgeDNSIPAddrPrimary = _NetworkBridgeDNSIPAddrPrimary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 7),
    _NetworkBridgeDNSIPAddrPrimary_Type()
)
networkBridgeDNSIPAddrPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeDNSIPAddrPrimary.setStatus("current")
_NetworkBridgeDNSIPAddrSecondary_Type = IpAddress
_NetworkBridgeDNSIPAddrSecondary_Object = MibScalar
networkBridgeDNSIPAddrSecondary = _NetworkBridgeDNSIPAddrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 7, 8),
    _NetworkBridgeDNSIPAddrSecondary_Type()
)
networkBridgeDNSIPAddrSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkBridgeDNSIPAddrSecondary.setStatus("current")


class _NetworkPortSecurity_Type(Integer32):
    """Custom type networkPortSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkPortSecurity_Type.__name__ = "Integer32"
_NetworkPortSecurity_Object = MibScalar
networkPortSecurity = _NetworkPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 8),
    _NetworkPortSecurity_Type()
)
networkPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPortSecurity.setStatus("current")


class _NetworkPortSecurityMax_Type(Integer32):
    """Custom type networkPortSecurityMax based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NetworkPortSecurityMax_Type.__name__ = "Integer32"
_NetworkPortSecurityMax_Object = MibScalar
networkPortSecurityMax = _NetworkPortSecurityMax_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 9),
    _NetworkPortSecurityMax_Type()
)
networkPortSecurityMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPortSecurityMax.setStatus("current")


class _NetworkPortSecurityAgingTime_Type(Integer32):
    """Custom type networkPortSecurityAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_NetworkPortSecurityAgingTime_Type.__name__ = "Integer32"
_NetworkPortSecurityAgingTime_Object = MibScalar
networkPortSecurityAgingTime = _NetworkPortSecurityAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 10),
    _NetworkPortSecurityAgingTime_Type()
)
networkPortSecurityAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPortSecurityAgingTime.setStatus("current")
_McastVLAN_ObjectIdentity = ObjectIdentity
mcastVLAN = _McastVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 15)
)


class _McastVLANEnable_Type(Integer32):
    """Custom type mcastVLANEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_McastVLANEnable_Type.__name__ = "Integer32"
_McastVLANEnable_Object = MibScalar
mcastVLANEnable = _McastVLANEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 15, 1),
    _McastVLANEnable_Type()
)
mcastVLANEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastVLANEnable.setStatus("current")


class _McastVLANVID_Type(Integer32):
    """Custom type mcastVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_McastVLANVID_Type.__name__ = "Integer32"
_McastVLANVID_Object = MibScalar
mcastVLANVID = _McastVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 15, 2),
    _McastVLANVID_Type()
)
mcastVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastVLANVID.setStatus("current")


class _McastVLANVP_Type(Integer32):
    """Custom type mcastVLANVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_McastVLANVP_Type.__name__ = "Integer32"
_McastVLANVP_Object = MibScalar
mcastVLANVP = _McastVLANVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 15, 3),
    _McastVLANVP_Type()
)
mcastVLANVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastVLANVP.setStatus("current")


class _McastGroupLimit_Type(Integer32):
    """Custom type mcastGroupLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 5),
    )


_McastGroupLimit_Type.__name__ = "Integer32"
_McastGroupLimit_Object = MibScalar
mcastGroupLimit = _McastGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 17),
    _McastGroupLimit_Type()
)
mcastGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastGroupLimit.setStatus("current")
_MgmtIF_ObjectIdentity = ObjectIdentity
mgmtIF = _MgmtIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20)
)


class _MgmtIFEnable_Type(Integer32):
    """Custom type mgmtIFEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_MgmtIFEnable_Type.__name__ = "Integer32"
_MgmtIFEnable_Object = MibScalar
mgmtIFEnable = _MgmtIFEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 1),
    _MgmtIFEnable_Type()
)
mgmtIFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFEnable.setStatus("current")


class _MgmtIFVLAN_Type(Integer32):
    """Custom type mgmtIFVLAN based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_MgmtIFVLAN_Type.__name__ = "Integer32"
_MgmtIFVLAN_Object = MibScalar
mgmtIFVLAN = _MgmtIFVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 2),
    _MgmtIFVLAN_Type()
)
mgmtIFVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFVLAN.setStatus("current")


class _MgmtIFVID_Type(Integer32):
    """Custom type mgmtIFVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MgmtIFVID_Type.__name__ = "Integer32"
_MgmtIFVID_Object = MibScalar
mgmtIFVID = _MgmtIFVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 3),
    _MgmtIFVID_Type()
)
mgmtIFVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFVID.setStatus("current")


class _MgmtIFVP_Type(Integer32):
    """Custom type mgmtIFVP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgmtIFVP_Type.__name__ = "Integer32"
_MgmtIFVP_Object = MibScalar
mgmtIFVP = _MgmtIFVP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 4),
    _MgmtIFVP_Type()
)
mgmtIFVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFVP.setStatus("current")


class _MgmtIFIPAddressMode_Type(Integer32):
    """Custom type mgmtIFIPAddressMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_MgmtIFIPAddressMode_Type.__name__ = "Integer32"
_MgmtIFIPAddressMode_Object = MibScalar
mgmtIFIPAddressMode = _MgmtIFIPAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 5),
    _MgmtIFIPAddressMode_Type()
)
mgmtIFIPAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFIPAddressMode.setStatus("current")
_MgmtIFIPAddr_Type = IpAddress
_MgmtIFIPAddr_Object = MibScalar
mgmtIFIPAddr = _MgmtIFIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 6),
    _MgmtIFIPAddr_Type()
)
mgmtIFIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFIPAddr.setStatus("current")
_MgmtIFNetmask_Type = IpAddress
_MgmtIFNetmask_Object = MibScalar
mgmtIFNetmask = _MgmtIFNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 7),
    _MgmtIFNetmask_Type()
)
mgmtIFNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFNetmask.setStatus("current")
_MgmtIFGateway_Type = IpAddress
_MgmtIFGateway_Object = MibScalar
mgmtIFGateway = _MgmtIFGateway_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 20, 8),
    _MgmtIFGateway_Type()
)
mgmtIFGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIFGateway.setStatus("current")
_NetworkLanDefaultIP_Type = IpAddress
_NetworkLanDefaultIP_Object = MibScalar
networkLanDefaultIP = _NetworkLanDefaultIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 25),
    _NetworkLanDefaultIP_Type()
)
networkLanDefaultIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLanDefaultIP.setStatus("current")


class _NetworkRelaydEnable_Type(Integer32):
    """Custom type networkRelaydEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkRelaydEnable_Type.__name__ = "Integer32"
_NetworkRelaydEnable_Object = MibScalar
networkRelaydEnable = _NetworkRelaydEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 26),
    _NetworkRelaydEnable_Type()
)
networkRelaydEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRelaydEnable.setStatus("current")
_NetworkAliases_ObjectIdentity = ObjectIdentity
networkAliases = _NetworkAliases_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27)
)
_CambiumIPAliasCnfTable_Object = MibTable
cambiumIPAliasCnfTable = _CambiumIPAliasCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1)
)
if mibBuilder.loadTexts:
    cambiumIPAliasCnfTable.setStatus("current")
_CambiumIPAliasCnfEntry_Object = MibTableRow
cambiumIPAliasCnfEntry = _CambiumIPAliasCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1)
)
cambiumIPAliasCnfEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumIPAliasesIndex"),
)
if mibBuilder.loadTexts:
    cambiumIPAliasCnfEntry.setStatus("current")


class _CambiumIPAliasesIndex_Type(Integer32):
    """Custom type cambiumIPAliasesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CambiumIPAliasesIndex_Type.__name__ = "Integer32"
_CambiumIPAliasesIndex_Object = MibTableColumn
cambiumIPAliasesIndex = _CambiumIPAliasesIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1, 1),
    _CambiumIPAliasesIndex_Type()
)
cambiumIPAliasesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesIndex.setStatus("current")
_CambiumIPAliasesIpAddr_Type = IpAddress
_CambiumIPAliasesIpAddr_Object = MibTableColumn
cambiumIPAliasesIpAddr = _CambiumIPAliasesIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1, 2),
    _CambiumIPAliasesIpAddr_Type()
)
cambiumIPAliasesIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesIpAddr.setStatus("current")
_CambiumIPAliasesNetmask_Type = IpAddress
_CambiumIPAliasesNetmask_Object = MibTableColumn
cambiumIPAliasesNetmask = _CambiumIPAliasesNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1, 3),
    _CambiumIPAliasesNetmask_Type()
)
cambiumIPAliasesNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesNetmask.setStatus("current")


class _CambiumIPAliasesInfo_Type(DisplayString):
    """Custom type cambiumIPAliasesInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumIPAliasesInfo_Type.__name__ = "DisplayString"
_CambiumIPAliasesInfo_Object = MibTableColumn
cambiumIPAliasesInfo = _CambiumIPAliasesInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 1, 1, 4),
    _CambiumIPAliasesInfo_Type()
)
cambiumIPAliasesInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesInfo.setStatus("current")


class _CambiumIPAliasesEnable_Type(Integer32):
    """Custom type cambiumIPAliasesEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumIPAliasesEnable_Type.__name__ = "Integer32"
_CambiumIPAliasesEnable_Object = MibScalar
cambiumIPAliasesEnable = _CambiumIPAliasesEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 4, 27, 2),
    _CambiumIPAliasesEnable_Type()
)
cambiumIPAliasesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIPAliasesEnable.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5)
)


class _SnmpReadOnlyCommunity_Type(DisplayString):
    """Custom type snmpReadOnlyCommunity based on DisplayString"""
    defaultValue = OctetString("public")


_SnmpReadOnlyCommunity_Object = MibScalar
snmpReadOnlyCommunity = _SnmpReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 1),
    _SnmpReadOnlyCommunity_Type()
)
snmpReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadOnlyCommunity.setStatus("current")


class _SnmpReadWriteCommunity_Type(DisplayString):
    """Custom type snmpReadWriteCommunity based on DisplayString"""
    defaultValue = OctetString("private")


_SnmpReadWriteCommunity_Object = MibScalar
snmpReadWriteCommunity = _SnmpReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 2),
    _SnmpReadWriteCommunity_Type()
)
snmpReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadWriteCommunity.setStatus("current")


class _SnmpSystemName_Type(DisplayString):
    """Custom type snmpSystemName based on DisplayString"""
    defaultValue = OctetString("CambiumNetworks")


_SnmpSystemName_Object = MibScalar
snmpSystemName = _SnmpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 3),
    _SnmpSystemName_Type()
)
snmpSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemName.setStatus("current")
_SnmpSystemDescription_Type = DisplayString
_SnmpSystemDescription_Object = MibScalar
snmpSystemDescription = _SnmpSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 4),
    _SnmpSystemDescription_Type()
)
snmpSystemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemDescription.setStatus("current")


class _SnmpTrapEnable_Type(Integer32):
    """Custom type snmpTrapEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SnmpTrapEnable_Type.__name__ = "Integer32"
_SnmpTrapEnable_Object = MibScalar
snmpTrapEnable = _SnmpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 5),
    _SnmpTrapEnable_Type()
)
snmpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEnable.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 6),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_SnmpTrapTable_Object = MibTable
snmpTrapTable = _SnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7)
)
if mibBuilder.loadTexts:
    snmpTrapTable.setStatus("current")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "snmpTrapEntryIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("current")


class _SnmpTrapEntryIndex_Type(Integer32):
    """Custom type snmpTrapEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SnmpTrapEntryIndex_Type.__name__ = "Integer32"
_SnmpTrapEntryIndex_Object = MibTableColumn
snmpTrapEntryIndex = _SnmpTrapEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7, 1, 1),
    _SnmpTrapEntryIndex_Type()
)
snmpTrapEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntryIndex.setStatus("current")
_SnmpTrapEntryIP_Type = IpAddress
_SnmpTrapEntryIP_Object = MibTableColumn
snmpTrapEntryIP = _SnmpTrapEntryIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7, 1, 2),
    _SnmpTrapEntryIP_Type()
)
snmpTrapEntryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntryIP.setStatus("current")


class _SnmpTrapEntryPort_Type(Integer32):
    """Custom type snmpTrapEntryPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpTrapEntryPort_Type.__name__ = "Integer32"
_SnmpTrapEntryPort_Object = MibTableColumn
snmpTrapEntryPort = _SnmpTrapEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 7, 1, 3),
    _SnmpTrapEntryPort_Type()
)
snmpTrapEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapEntryPort.setStatus("current")


class _SnmpDomainAccessEnable_Type(Integer32):
    """Custom type snmpDomainAccessEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SnmpDomainAccessEnable_Type.__name__ = "Integer32"
_SnmpDomainAccessEnable_Object = MibScalar
snmpDomainAccessEnable = _SnmpDomainAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 8),
    _SnmpDomainAccessEnable_Type()
)
snmpDomainAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDomainAccessEnable.setStatus("current")


class _SnmpDomainAccessIP_Type(DisplayString):
    """Custom type snmpDomainAccessIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 15),
    )


_SnmpDomainAccessIP_Type.__name__ = "DisplayString"
_SnmpDomainAccessIP_Object = MibScalar
snmpDomainAccessIP = _SnmpDomainAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 9),
    _SnmpDomainAccessIP_Type()
)
snmpDomainAccessIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDomainAccessIP.setStatus("current")


class _SnmpDomainAccessIPMask_Type(DisplayString):
    """Custom type snmpDomainAccessIPMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 15),
    )


_SnmpDomainAccessIPMask_Type.__name__ = "DisplayString"
_SnmpDomainAccessIPMask_Object = MibScalar
snmpDomainAccessIPMask = _SnmpDomainAccessIPMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 5, 10),
    _SnmpDomainAccessIPMask_Type()
)
snmpDomainAccessIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpDomainAccessIPMask.setStatus("current")
_CambiumSystem_ObjectIdentity = ObjectIdentity
cambiumSystem = _CambiumSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6)
)
_SystemConfig_ObjectIdentity = ObjectIdentity
systemConfig = _SystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1)
)


class _SystemConfigTimezone_Type(DisplayString):
    """Custom type systemConfigTimezone based on DisplayString"""
    defaultValue = OctetString("GMT")


_SystemConfigTimezone_Object = MibScalar
systemConfigTimezone = _SystemConfigTimezone_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 1),
    _SystemConfigTimezone_Type()
)
systemConfigTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigTimezone.setStatus("current")


class _SystemConfigDeviceName_Type(DisplayString):
    """Custom type systemConfigDeviceName based on DisplayString"""
    defaultValue = OctetString("Cambium-STA")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_SystemConfigDeviceName_Type.__name__ = "DisplayString"
_SystemConfigDeviceName_Object = MibScalar
systemConfigDeviceName = _SystemConfigDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 2),
    _SystemConfigDeviceName_Type()
)
systemConfigDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigDeviceName.setStatus("current")


class _SystemConfigETSILicense_Type(DisplayString):
    """Custom type systemConfigETSILicense based on DisplayString"""
    defaultValue = OctetString("ETSIkey")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemConfigETSILicense_Type.__name__ = "DisplayString"
_SystemConfigETSILicense_Object = MibScalar
systemConfigETSILicense = _SystemConfigETSILicense_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 3),
    _SystemConfigETSILicense_Type()
)
systemConfigETSILicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemConfigETSILicense.setStatus("current")


class _SystemConfigSWLockBit_Type(Integer32):
    """Custom type systemConfigSWLockBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigSWLockBit_Type.__name__ = "Integer32"
_SystemConfigSWLockBit_Object = MibScalar
systemConfigSWLockBit = _SystemConfigSWLockBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 4),
    _SystemConfigSWLockBit_Type()
)
systemConfigSWLockBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigSWLockBit.setStatus("current")


class _SystemConfigHWLockBit_Type(Integer32):
    """Custom type systemConfigHWLockBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigHWLockBit_Type.__name__ = "Integer32"
_SystemConfigHWLockBit_Object = MibScalar
systemConfigHWLockBit = _SystemConfigHWLockBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 5),
    _SystemConfigHWLockBit_Type()
)
systemConfigHWLockBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigHWLockBit.setStatus("current")


class _SystemDeviceLocLatitude_Type(DisplayString):
    """Custom type systemDeviceLocLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemDeviceLocLatitude_Type.__name__ = "DisplayString"
_SystemDeviceLocLatitude_Object = MibScalar
systemDeviceLocLatitude = _SystemDeviceLocLatitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 6),
    _SystemDeviceLocLatitude_Type()
)
systemDeviceLocLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDeviceLocLatitude.setStatus("current")


class _SystemDeviceLocLongitude_Type(DisplayString):
    """Custom type systemDeviceLocLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemDeviceLocLongitude_Type.__name__ = "DisplayString"
_SystemDeviceLocLongitude_Object = MibScalar
systemDeviceLocLongitude = _SystemDeviceLocLongitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 7),
    _SystemDeviceLocLongitude_Type()
)
systemDeviceLocLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDeviceLocLongitude.setStatus("current")


class _SystemDeviceLocHeight_Type(DisplayString):
    """Custom type systemDeviceLocHeight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SystemDeviceLocHeight_Type.__name__ = "DisplayString"
_SystemDeviceLocHeight_Object = MibScalar
systemDeviceLocHeight = _SystemDeviceLocHeight_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 8),
    _SystemDeviceLocHeight_Type()
)
systemDeviceLocHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDeviceLocHeight.setStatus("current")


class _SystemConfigisGPSkeyOK_Type(Integer32):
    """Custom type systemConfigisGPSkeyOK based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SystemConfigisGPSkeyOK_Type.__name__ = "Integer32"
_SystemConfigisGPSkeyOK_Object = MibScalar
systemConfigisGPSkeyOK = _SystemConfigisGPSkeyOK_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 10),
    _SystemConfigisGPSkeyOK_Type()
)
systemConfigisGPSkeyOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigisGPSkeyOK.setStatus("obsolete")


class _SystemConfigGPSLockBit_Type(Integer32):
    """Custom type systemConfigGPSLockBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SystemConfigGPSLockBit_Type.__name__ = "Integer32"
_SystemConfigGPSLockBit_Object = MibScalar
systemConfigGPSLockBit = _SystemConfigGPSLockBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 11),
    _SystemConfigGPSLockBit_Type()
)
systemConfigGPSLockBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigGPSLockBit.setStatus("obsolete")


class _SystemConfigSMLockBit_Type(Integer32):
    """Custom type systemConfigSMLockBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SystemConfigSMLockBit_Type.__name__ = "Integer32"
_SystemConfigSMLockBit_Object = MibScalar
systemConfigSMLockBit = _SystemConfigSMLockBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 12),
    _SystemConfigSMLockBit_Type()
)
systemConfigSMLockBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigSMLockBit.setStatus("current")


class _SystemConfigSMLimit_Type(Integer32):
    """Custom type systemConfigSMLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_SystemConfigSMLimit_Type.__name__ = "Integer32"
_SystemConfigSMLimit_Object = MibScalar
systemConfigSMLimit = _SystemConfigSMLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 13),
    _SystemConfigSMLimit_Type()
)
systemConfigSMLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigSMLimit.setStatus("current")


class _PowerSequenceFactoryDefault_Type(Integer32):
    """Custom type powerSequenceFactoryDefault based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_PowerSequenceFactoryDefault_Type.__name__ = "Integer32"
_PowerSequenceFactoryDefault_Object = MibScalar
powerSequenceFactoryDefault = _PowerSequenceFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 15),
    _PowerSequenceFactoryDefault_Type()
)
powerSequenceFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSequenceFactoryDefault.setStatus("current")


class _SystemConfigLockedCC_Type(DisplayString):
    """Custom type systemConfigLockedCC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 2),
    )


_SystemConfigLockedCC_Type.__name__ = "DisplayString"
_SystemConfigLockedCC_Object = MibScalar
systemConfigLockedCC = _SystemConfigLockedCC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 16),
    _SystemConfigLockedCC_Type()
)
systemConfigLockedCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigLockedCC.setStatus("current")


class _SystemConfigMinAntGain_Type(Integer32):
    """Custom type systemConfigMinAntGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SystemConfigMinAntGain_Type.__name__ = "Integer32"
_SystemConfigMinAntGain_Object = MibScalar
systemConfigMinAntGain = _SystemConfigMinAntGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 1, 17),
    _SystemConfigMinAntGain_Type()
)
systemConfigMinAntGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigMinAntGain.setStatus("current")
_SystemNtpServer_ObjectIdentity = ObjectIdentity
systemNtpServer = _SystemNtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 2)
)


class _SystemNtpServerIPMode_Type(Integer32):
    """Custom type systemNtpServerIPMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_SystemNtpServerIPMode_Type.__name__ = "Integer32"
_SystemNtpServerIPMode_Object = MibScalar
systemNtpServerIPMode = _SystemNtpServerIPMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 2, 1),
    _SystemNtpServerIPMode_Type()
)
systemNtpServerIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtpServerIPMode.setStatus("current")
_SystemNtpServerPrimaryIP_Type = IpAddress
_SystemNtpServerPrimaryIP_Object = MibScalar
systemNtpServerPrimaryIP = _SystemNtpServerPrimaryIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 2, 2),
    _SystemNtpServerPrimaryIP_Type()
)
systemNtpServerPrimaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtpServerPrimaryIP.setStatus("current")
_SystemNtpServerSecondaryIP_Type = IpAddress
_SystemNtpServerSecondaryIP_Object = MibScalar
systemNtpServerSecondaryIP = _SystemNtpServerSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 6, 2, 3),
    _SystemNtpServerSecondaryIP_Type()
)
systemNtpServerSecondaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtpServerSecondaryIP.setStatus("current")
_CambiumWebServer_ObjectIdentity = ObjectIdentity
cambiumWebServer = _CambiumWebServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7)
)


class _WebService_Type(Integer32):
    """Custom type webService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WebService_Type.__name__ = "Integer32"
_WebService_Object = MibScalar
webService = _WebService_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7, 1),
    _WebService_Type()
)
webService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webService.setStatus("current")


class _HttpPort_Type(Integer32):
    """Custom type httpPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HttpPort_Type.__name__ = "Integer32"
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7, 2),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")


class _HttpsPort_Type(Integer32):
    """Custom type httpsPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HttpsPort_Type.__name__ = "Integer32"
_HttpsPort_Object = MibScalar
httpsPort = _HttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 7, 3),
    _HttpsPort_Type()
)
httpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsPort.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8)
)
_WirelessDevice_ObjectIdentity = ObjectIdentity
wirelessDevice = _WirelessDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1)
)


class _WirelessDeviceCountryCode_Type(DisplayString):
    """Custom type wirelessDeviceCountryCode based on DisplayString"""
    defaultValue = OctetString("NS")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )


_WirelessDeviceCountryCode_Type.__name__ = "DisplayString"
_WirelessDeviceCountryCode_Object = MibScalar
wirelessDeviceCountryCode = _WirelessDeviceCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 1),
    _WirelessDeviceCountryCode_Type()
)
wirelessDeviceCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDeviceCountryCode.setStatus("current")


class _WirelessType_Type(Integer32):
    """Custom type wirelessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessType_Type.__name__ = "Integer32"
_WirelessType_Object = MibScalar
wirelessType = _WirelessType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 2),
    _WirelessType_Type()
)
wirelessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessType.setStatus("obsolete")


class _WirelessDefaultCountryCode_Type(DisplayString):
    """Custom type wirelessDefaultCountryCode based on DisplayString"""
    defaultValue = OctetString("OT")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )


_WirelessDefaultCountryCode_Type.__name__ = "DisplayString"
_WirelessDefaultCountryCode_Object = MibScalar
wirelessDefaultCountryCode = _WirelessDefaultCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 1, 3),
    _WirelessDefaultCountryCode_Type()
)
wirelessDefaultCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDefaultCountryCode.setStatus("current")
_WirelessInterface_ObjectIdentity = ObjectIdentity
wirelessInterface = _WirelessInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2)
)


class _WirelessInterfaceMode_Type(Integer32):
    """Custom type wirelessInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_WirelessInterfaceMode_Type.__name__ = "Integer32"
_WirelessInterfaceMode_Object = MibScalar
wirelessInterfaceMode = _WirelessInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 1),
    _WirelessInterfaceMode_Type()
)
wirelessInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceMode.setStatus("current")


class _WirelessInterfaceSSID_Type(DisplayString):
    """Custom type wirelessInterfaceSSID based on DisplayString"""
    defaultValue = OctetString("Cambium-AP")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WirelessInterfaceSSID_Type.__name__ = "DisplayString"
_WirelessInterfaceSSID_Object = MibScalar
wirelessInterfaceSSID = _WirelessInterfaceSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 2),
    _WirelessInterfaceSSID_Type()
)
wirelessInterfaceSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceSSID.setStatus("current")


class _WirelessInterfaceEncryption_Type(Integer32):
    """Custom type wirelessInterfaceEncryption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_WirelessInterfaceEncryption_Type.__name__ = "Integer32"
_WirelessInterfaceEncryption_Object = MibScalar
wirelessInterfaceEncryption = _WirelessInterfaceEncryption_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 3),
    _WirelessInterfaceEncryption_Type()
)
wirelessInterfaceEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceEncryption.setStatus("current")


class _WirelessInterfaceEncryptionKey_Type(DisplayString):
    """Custom type wirelessInterfaceEncryptionKey based on DisplayString"""
    defaultValue = OctetString("Cam39-Tai!wdmv")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 63),
    )


_WirelessInterfaceEncryptionKey_Type.__name__ = "DisplayString"
_WirelessInterfaceEncryptionKey_Object = MibScalar
wirelessInterfaceEncryptionKey = _WirelessInterfaceEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 4),
    _WirelessInterfaceEncryptionKey_Type()
)
wirelessInterfaceEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceEncryptionKey.setStatus("current")


class _WirelessInterfaceHTMode_Type(Integer32):
    """Custom type wirelessInterfaceHTMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WirelessInterfaceHTMode_Type.__name__ = "Integer32"
_WirelessInterfaceHTMode_Object = MibScalar
wirelessInterfaceHTMode = _WirelessInterfaceHTMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 5),
    _WirelessInterfaceHTMode_Type()
)
wirelessInterfaceHTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceHTMode.setStatus("current")


class _WirelessInterfaceTXPower_Type(Integer32):
    """Custom type wirelessInterfaceTXPower based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 30),
    )


_WirelessInterfaceTXPower_Type.__name__ = "Integer32"
_WirelessInterfaceTXPower_Object = MibScalar
wirelessInterfaceTXPower = _WirelessInterfaceTXPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 6),
    _WirelessInterfaceTXPower_Type()
)
wirelessInterfaceTXPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTXPower.setStatus("current")


class _WirelessInterfaceTDDAntennaGain_Type(Integer32):
    """Custom type wirelessInterfaceTDDAntennaGain based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_WirelessInterfaceTDDAntennaGain_Type.__name__ = "Integer32"
_WirelessInterfaceTDDAntennaGain_Object = MibScalar
wirelessInterfaceTDDAntennaGain = _WirelessInterfaceTDDAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 7),
    _WirelessInterfaceTDDAntennaGain_Type()
)
wirelessInterfaceTDDAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTDDAntennaGain.setStatus("current")


class _WirelessInterfaceTDDRatio_Type(Integer32):
    """Custom type wirelessInterfaceTDDRatio based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
    )


_WirelessInterfaceTDDRatio_Type.__name__ = "Integer32"
_WirelessInterfaceTDDRatio_Object = MibScalar
wirelessInterfaceTDDRatio = _WirelessInterfaceTDDRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 9),
    _WirelessInterfaceTDDRatio_Type()
)
wirelessInterfaceTDDRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTDDRatio.setStatus("current")


class _WirelessInterfaceTPCTRL_Type(Integer32):
    """Custom type wirelessInterfaceTPCTRL based on Integer32"""
    defaultValue = -60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -40),
    )


_WirelessInterfaceTPCTRL_Type.__name__ = "Integer32"
_WirelessInterfaceTPCTRL_Object = MibScalar
wirelessInterfaceTPCTRL = _WirelessInterfaceTPCTRL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 10),
    _WirelessInterfaceTPCTRL_Type()
)
wirelessInterfaceTPCTRL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTPCTRL.setStatus("current")


class _WirelessInterfaceTPCMode_Type(Integer32):
    """Custom type wirelessInterfaceTPCMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessInterfaceTPCMode_Type.__name__ = "Integer32"
_WirelessInterfaceTPCMode_Object = MibScalar
wirelessInterfaceTPCMode = _WirelessInterfaceTPCMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 11),
    _WirelessInterfaceTPCMode_Type()
)
wirelessInterfaceTPCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTPCMode.setStatus("obsolete")


class _WirelessInterfacePTPMode_Type(Integer32):
    """Custom type wirelessInterfacePTPMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessInterfacePTPMode_Type.__name__ = "Integer32"
_WirelessInterfacePTPMode_Object = MibScalar
wirelessInterfacePTPMode = _WirelessInterfacePTPMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 12),
    _WirelessInterfacePTPMode_Type()
)
wirelessInterfacePTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfacePTPMode.setStatus("current")


class _WirelessInterfacePTPMACAddress_Type(DisplayString):
    """Custom type wirelessInterfacePTPMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_WirelessInterfacePTPMACAddress_Type.__name__ = "DisplayString"
_WirelessInterfacePTPMACAddress_Object = MibScalar
wirelessInterfacePTPMACAddress = _WirelessInterfacePTPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 13),
    _WirelessInterfacePTPMACAddress_Type()
)
wirelessInterfacePTPMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfacePTPMACAddress.setStatus("current")


class _WirelessInterfaceSyncSource_Type(Integer32):
    """Custom type wirelessInterfaceSyncSource based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
    )


_WirelessInterfaceSyncSource_Type.__name__ = "Integer32"
_WirelessInterfaceSyncSource_Object = MibScalar
wirelessInterfaceSyncSource = _WirelessInterfaceSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 14),
    _WirelessInterfaceSyncSource_Type()
)
wirelessInterfaceSyncSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceSyncSource.setStatus("current")


class _WirelessInterfaceSyncHoldTime_Type(Integer32):
    """Custom type wirelessInterfaceSyncHoldTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 864000),
    )


_WirelessInterfaceSyncHoldTime_Type.__name__ = "Integer32"
_WirelessInterfaceSyncHoldTime_Object = MibScalar
wirelessInterfaceSyncHoldTime = _WirelessInterfaceSyncHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 15),
    _WirelessInterfaceSyncHoldTime_Type()
)
wirelessInterfaceSyncHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceSyncHoldTime.setStatus("current")


class _WirelessInterfaceScanFrequencyListTwenty_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyListTwenty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1064),
    )


_WirelessInterfaceScanFrequencyListTwenty_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyListTwenty_Object = MibScalar
wirelessInterfaceScanFrequencyListTwenty = _WirelessInterfaceScanFrequencyListTwenty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 16),
    _WirelessInterfaceScanFrequencyListTwenty_Type()
)
wirelessInterfaceScanFrequencyListTwenty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyListTwenty.setStatus("current")


class _WirelessInterfaceScanFrequencyListForty_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyListForty based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1064),
    )


_WirelessInterfaceScanFrequencyListForty_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyListForty_Object = MibScalar
wirelessInterfaceScanFrequencyListForty = _WirelessInterfaceScanFrequencyListForty_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 17),
    _WirelessInterfaceScanFrequencyListForty_Type()
)
wirelessInterfaceScanFrequencyListForty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyListForty.setStatus("current")


class _CenterFrequency_Type(Integer32):
    """Custom type centerFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2407, 5970),
    )


_CenterFrequency_Type.__name__ = "Integer32"
_CenterFrequency_Object = MibScalar
centerFrequency = _CenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 18),
    _CenterFrequency_Type()
)
centerFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    centerFrequency.setStatus("current")


class _DfsAlternative1CenterFrequency_Type(Integer32):
    """Custom type dfsAlternative1CenterFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2407, 5970),
    )


_DfsAlternative1CenterFrequency_Type.__name__ = "Integer32"
_DfsAlternative1CenterFrequency_Object = MibScalar
dfsAlternative1CenterFrequency = _DfsAlternative1CenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 19),
    _DfsAlternative1CenterFrequency_Type()
)
dfsAlternative1CenterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative1CenterFrequency.setStatus("current")


class _DfsAlternative2CenterFrequency_Type(Integer32):
    """Custom type dfsAlternative2CenterFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2407, 5970),
    )


_DfsAlternative2CenterFrequency_Type.__name__ = "Integer32"
_DfsAlternative2CenterFrequency_Object = MibScalar
dfsAlternative2CenterFrequency = _DfsAlternative2CenterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 20),
    _DfsAlternative2CenterFrequency_Type()
)
dfsAlternative2CenterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative2CenterFrequency.setStatus("current")


class _WirelessMaximumCellSize_Type(Integer32):
    """Custom type wirelessMaximumCellSize based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65),
    )


_WirelessMaximumCellSize_Type.__name__ = "Integer32"
_WirelessMaximumCellSize_Object = MibScalar
wirelessMaximumCellSize = _WirelessMaximumCellSize_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 21),
    _WirelessMaximumCellSize_Type()
)
wirelessMaximumCellSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMaximumCellSize.setStatus("current")


class _WirelessCellSizeUnit_Type(Integer32):
    """Custom type wirelessCellSizeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessCellSizeUnit_Type.__name__ = "Integer32"
_WirelessCellSizeUnit_Object = MibScalar
wirelessCellSizeUnit = _WirelessCellSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 22),
    _WirelessCellSizeUnit_Type()
)
wirelessCellSizeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessCellSizeUnit.setStatus("current")


class _WirelessMaximumSTA_Type(Integer32):
    """Custom type wirelessMaximumSTA based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 120),
    )


_WirelessMaximumSTA_Type.__name__ = "Integer32"
_WirelessMaximumSTA_Object = MibScalar
wirelessMaximumSTA = _WirelessMaximumSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 23),
    _WirelessMaximumSTA_Type()
)
wirelessMaximumSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMaximumSTA.setStatus("current")


class _DfsAlternative1Bandwidth_Type(Integer32):
    """Custom type dfsAlternative1Bandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
    )


_DfsAlternative1Bandwidth_Type.__name__ = "Integer32"
_DfsAlternative1Bandwidth_Object = MibScalar
dfsAlternative1Bandwidth = _DfsAlternative1Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 24),
    _DfsAlternative1Bandwidth_Type()
)
dfsAlternative1Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative1Bandwidth.setStatus("current")


class _DfsAlternative2Bandwidth_Type(Integer32):
    """Custom type dfsAlternative2Bandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
    )


_DfsAlternative2Bandwidth_Type.__name__ = "Integer32"
_DfsAlternative2Bandwidth_Object = MibScalar
dfsAlternative2Bandwidth = _DfsAlternative2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 25),
    _DfsAlternative2Bandwidth_Type()
)
dfsAlternative2Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsAlternative2Bandwidth.setStatus("current")


class _WirelessAcceptableAPRSSIThreshold_Type(Integer32):
    """Custom type wirelessAcceptableAPRSSIThreshold based on Integer32"""
    defaultValue = -90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -20),
    )


_WirelessAcceptableAPRSSIThreshold_Type.__name__ = "Integer32"
_WirelessAcceptableAPRSSIThreshold_Object = MibScalar
wirelessAcceptableAPRSSIThreshold = _WirelessAcceptableAPRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 26),
    _WirelessAcceptableAPRSSIThreshold_Type()
)
wirelessAcceptableAPRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAcceptableAPRSSIThreshold.setStatus("current")


class _WirelessAcceptableAPCINRThreshold_Type(Integer32):
    """Custom type wirelessAcceptableAPCINRThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 60),
    )


_WirelessAcceptableAPCINRThreshold_Type.__name__ = "Integer32"
_WirelessAcceptableAPCINRThreshold_Object = MibScalar
wirelessAcceptableAPCINRThreshold = _WirelessAcceptableAPCINRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 27),
    _WirelessAcceptableAPCINRThreshold_Type()
)
wirelessAcceptableAPCINRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAcceptableAPCINRThreshold.setStatus("obsolete")


class _WirelessInterfaceUnblockUSfreqs_Type(Integer32):
    """Custom type wirelessInterfaceUnblockUSfreqs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterfaceUnblockUSfreqs_Type.__name__ = "Integer32"
_WirelessInterfaceUnblockUSfreqs_Object = MibScalar
wirelessInterfaceUnblockUSfreqs = _WirelessInterfaceUnblockUSfreqs_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 28),
    _WirelessInterfaceUnblockUSfreqs_Type()
)
wirelessInterfaceUnblockUSfreqs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceUnblockUSfreqs.setStatus("obsolete")


class _WirelessMIREnable_Type(Integer32):
    """Custom type wirelessMIREnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessMIREnable_Type.__name__ = "Integer32"
_WirelessMIREnable_Object = MibScalar
wirelessMIREnable = _WirelessMIREnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 29),
    _WirelessMIREnable_Type()
)
wirelessMIREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIREnable.setStatus("current")


class _WirelessMIRSTAProfileNumber_Type(Integer32):
    """Custom type wirelessMIRSTAProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WirelessMIRSTAProfileNumber_Type.__name__ = "Integer32"
_WirelessMIRSTAProfileNumber_Object = MibScalar
wirelessMIRSTAProfileNumber = _WirelessMIRSTAProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 30),
    _WirelessMIRSTAProfileNumber_Type()
)
wirelessMIRSTAProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRSTAProfileNumber.setStatus("current")


class _WirelessMIRAPDefaultProfileNumber_Type(Integer32):
    """Custom type wirelessMIRAPDefaultProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WirelessMIRAPDefaultProfileNumber_Type.__name__ = "Integer32"
_WirelessMIRAPDefaultProfileNumber_Object = MibScalar
wirelessMIRAPDefaultProfileNumber = _WirelessMIRAPDefaultProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 31),
    _WirelessMIRAPDefaultProfileNumber_Type()
)
wirelessMIRAPDefaultProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRAPDefaultProfileNumber.setStatus("current")


class _WirelessInterfaceScanFrequencyBandwidth_Type(Integer32):
    """Custom type wirelessInterfaceScanFrequencyBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WirelessInterfaceScanFrequencyBandwidth_Type.__name__ = "Integer32"
_WirelessInterfaceScanFrequencyBandwidth_Object = MibScalar
wirelessInterfaceScanFrequencyBandwidth = _WirelessInterfaceScanFrequencyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 32),
    _WirelessInterfaceScanFrequencyBandwidth_Type()
)
wirelessInterfaceScanFrequencyBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyBandwidth.setStatus("current")


class _WirelessInterfaceGuardInterval_Type(Integer32):
    """Custom type wirelessInterfaceGuardInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessInterfaceGuardInterval_Type.__name__ = "Integer32"
_WirelessInterfaceGuardInterval_Object = MibScalar
wirelessInterfaceGuardInterval = _WirelessInterfaceGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 33),
    _WirelessInterfaceGuardInterval_Type()
)
wirelessInterfaceGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceGuardInterval.setStatus("current")


class _WirelessInterfaceiFreqReuseMode_Type(Integer32):
    """Custom type wirelessInterfaceiFreqReuseMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessInterfaceiFreqReuseMode_Type.__name__ = "Integer32"
_WirelessInterfaceiFreqReuseMode_Object = MibScalar
wirelessInterfaceiFreqReuseMode = _WirelessInterfaceiFreqReuseMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 34),
    _WirelessInterfaceiFreqReuseMode_Type()
)
wirelessInterfaceiFreqReuseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceiFreqReuseMode.setStatus("current")


class _WirelessSTAPriority_Type(Integer32):
    """Custom type wirelessSTAPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessSTAPriority_Type.__name__ = "Integer32"
_WirelessSTAPriority_Object = MibScalar
wirelessSTAPriority = _WirelessSTAPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 35),
    _WirelessSTAPriority_Type()
)
wirelessSTAPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSTAPriority.setStatus("current")


class _WirelessSmoothingBit_Type(Integer32):
    """Custom type wirelessSmoothingBit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessSmoothingBit_Type.__name__ = "Integer32"
_WirelessSmoothingBit_Object = MibScalar
wirelessSmoothingBit = _WirelessSmoothingBit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 36),
    _WirelessSmoothingBit_Type()
)
wirelessSmoothingBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSmoothingBit.setStatus("obsolete")


class _WirelessSecurityMethod_Type(Integer32):
    """Custom type wirelessSecurityMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_WirelessSecurityMethod_Type.__name__ = "Integer32"
_WirelessSecurityMethod_Object = MibScalar
wirelessSecurityMethod = _WirelessSecurityMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 37),
    _WirelessSecurityMethod_Type()
)
wirelessSecurityMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSecurityMethod.setStatus("current")


class _WirelessAcceptableAPSNRThreshold_Type(Integer32):
    """Custom type wirelessAcceptableAPSNRThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5, 60),
    )


_WirelessAcceptableAPSNRThreshold_Type.__name__ = "Integer32"
_WirelessAcceptableAPSNRThreshold_Object = MibScalar
wirelessAcceptableAPSNRThreshold = _WirelessAcceptableAPSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 38),
    _WirelessAcceptableAPSNRThreshold_Type()
)
wirelessAcceptableAPSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAcceptableAPSNRThreshold.setStatus("current")


class _WirelessMgmtPacketRate_Type(Integer32):
    """Custom type wirelessMgmtPacketRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessMgmtPacketRate_Type.__name__ = "Integer32"
_WirelessMgmtPacketRate_Object = MibScalar
wirelessMgmtPacketRate = _WirelessMgmtPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 39),
    _WirelessMgmtPacketRate_Type()
)
wirelessMgmtPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMgmtPacketRate.setStatus("current")


class _WirelessStaIsolate_Type(Integer32):
    """Custom type wirelessStaIsolate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessStaIsolate_Type.__name__ = "Integer32"
_WirelessStaIsolate_Object = MibScalar
wirelessStaIsolate = _WirelessStaIsolate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 40),
    _WirelessStaIsolate_Type()
)
wirelessStaIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessStaIsolate.setStatus("current")


class _WirelessCcaEnable_Type(Integer32):
    """Custom type wirelessCcaEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessCcaEnable_Type.__name__ = "Integer32"
_WirelessCcaEnable_Object = MibScalar
wirelessCcaEnable = _WirelessCcaEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 41),
    _WirelessCcaEnable_Type()
)
wirelessCcaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessCcaEnable.setStatus("current")


class _WirelessInterfaceScanFrequencyListTen_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyListTen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1064),
    )


_WirelessInterfaceScanFrequencyListTen_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyListTen_Object = MibScalar
wirelessInterfaceScanFrequencyListTen = _WirelessInterfaceScanFrequencyListTen_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 42),
    _WirelessInterfaceScanFrequencyListTen_Type()
)
wirelessInterfaceScanFrequencyListTen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyListTen.setStatus("current")


class _WirelessInterfaceScanFrequencyListFive_Type(DisplayString):
    """Custom type wirelessInterfaceScanFrequencyListFive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1064),
    )


_WirelessInterfaceScanFrequencyListFive_Type.__name__ = "DisplayString"
_WirelessInterfaceScanFrequencyListFive_Object = MibScalar
wirelessInterfaceScanFrequencyListFive = _WirelessInterfaceScanFrequencyListFive_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 43),
    _WirelessInterfaceScanFrequencyListFive_Type()
)
wirelessInterfaceScanFrequencyListFive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceScanFrequencyListFive.setStatus("current")


class _WirelessMulticastEnhanceMode_Type(Integer32):
    """Custom type wirelessMulticastEnhanceMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
    )


_WirelessMulticastEnhanceMode_Type.__name__ = "Integer32"
_WirelessMulticastEnhanceMode_Object = MibScalar
wirelessMulticastEnhanceMode = _WirelessMulticastEnhanceMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 44),
    _WirelessMulticastEnhanceMode_Type()
)
wirelessMulticastEnhanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMulticastEnhanceMode.setStatus("current")


class _WirelessTXPowerManualLimit_Type(Integer32):
    """Custom type wirelessTXPowerManualLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessTXPowerManualLimit_Type.__name__ = "Integer32"
_WirelessTXPowerManualLimit_Object = MibScalar
wirelessTXPowerManualLimit = _WirelessTXPowerManualLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 48),
    _WirelessTXPowerManualLimit_Type()
)
wirelessTXPowerManualLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessTXPowerManualLimit.setStatus("current")


class _WirelessRateMaxMCS_Type(Integer32):
    """Custom type wirelessRateMaxMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WirelessRateMaxMCS_Type.__name__ = "Integer32"
_WirelessRateMaxMCS_Object = MibScalar
wirelessRateMaxMCS = _WirelessRateMaxMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 49),
    _WirelessRateMaxMCS_Type()
)
wirelessRateMaxMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRateMaxMCS.setStatus("current")


class _WirelessSMWifiDistance_Type(Integer32):
    """Custom type wirelessSMWifiDistance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_WirelessSMWifiDistance_Type.__name__ = "Integer32"
_WirelessSMWifiDistance_Object = MibScalar
wirelessSMWifiDistance = _WirelessSMWifiDistance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 50),
    _WirelessSMWifiDistance_Type()
)
wirelessSMWifiDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessSMWifiDistance.setStatus("current")


class _WirelessInterfaceProtocolMode_Type(Integer32):
    """Custom type wirelessInterfaceProtocolMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
    )


_WirelessInterfaceProtocolMode_Type.__name__ = "Integer32"
_WirelessInterfaceProtocolMode_Object = MibScalar
wirelessInterfaceProtocolMode = _WirelessInterfaceProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 51),
    _WirelessInterfaceProtocolMode_Type()
)
wirelessInterfaceProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceProtocolMode.setStatus("current")


class _ForceMcastBcast4Addr_Type(Integer32):
    """Custom type forceMcastBcast4Addr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_ForceMcastBcast4Addr_Type.__name__ = "Integer32"
_ForceMcastBcast4Addr_Object = MibScalar
forceMcastBcast4Addr = _ForceMcastBcast4Addr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 53),
    _ForceMcastBcast4Addr_Type()
)
forceMcastBcast4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forceMcastBcast4Addr.setStatus("current")


class _WirelessInterfaceRateMinMCS_Type(Integer32):
    """Custom type wirelessInterfaceRateMinMCS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WirelessInterfaceRateMinMCS_Type.__name__ = "Integer32"
_WirelessInterfaceRateMinMCS_Object = MibScalar
wirelessInterfaceRateMinMCS = _WirelessInterfaceRateMinMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 55),
    _WirelessInterfaceRateMinMCS_Type()
)
wirelessInterfaceRateMinMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceRateMinMCS.setStatus("current")


class _WirelessInterfaceRateMaxMCS_Type(Integer32):
    """Custom type wirelessInterfaceRateMaxMCS based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WirelessInterfaceRateMaxMCS_Type.__name__ = "Integer32"
_WirelessInterfaceRateMaxMCS_Object = MibScalar
wirelessInterfaceRateMaxMCS = _WirelessInterfaceRateMaxMCS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 56),
    _WirelessInterfaceRateMaxMCS_Type()
)
wirelessInterfaceRateMaxMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceRateMaxMCS.setStatus("current")


class _WirelessMulticastIgmpFastLeave_Type(Integer32):
    """Custom type wirelessMulticastIgmpFastLeave based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessMulticastIgmpFastLeave_Type.__name__ = "Integer32"
_WirelessMulticastIgmpFastLeave_Object = MibScalar
wirelessMulticastIgmpFastLeave = _WirelessMulticastIgmpFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 57),
    _WirelessMulticastIgmpFastLeave_Type()
)
wirelessMulticastIgmpFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMulticastIgmpFastLeave.setStatus("current")


class _WirelessInterfaceTDDFrameSize_Type(Integer32):
    """Custom type wirelessInterfaceTDDFrameSize based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2500, 2500),
        ValueRangeConstraint(5000, 5000),
    )


_WirelessInterfaceTDDFrameSize_Type.__name__ = "Integer32"
_WirelessInterfaceTDDFrameSize_Object = MibScalar
wirelessInterfaceTDDFrameSize = _WirelessInterfaceTDDFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 58),
    _WirelessInterfaceTDDFrameSize_Type()
)
wirelessInterfaceTDDFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceTDDFrameSize.setStatus("current")


class _WirelessInterfaceColocState_Type(Integer32):
    """Custom type wirelessInterfaceColocState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessInterfaceColocState_Type.__name__ = "Integer32"
_WirelessInterfaceColocState_Object = MibScalar
wirelessInterfaceColocState = _WirelessInterfaceColocState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 59),
    _WirelessInterfaceColocState_Type()
)
wirelessInterfaceColocState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceColocState.setStatus("current")


class _WirelessInterfaceColocSystemSyncSrc_Type(Integer32):
    """Custom type wirelessInterfaceColocSystemSyncSrc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_WirelessInterfaceColocSystemSyncSrc_Type.__name__ = "Integer32"
_WirelessInterfaceColocSystemSyncSrc_Object = MibScalar
wirelessInterfaceColocSystemSyncSrc = _WirelessInterfaceColocSystemSyncSrc_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 60),
    _WirelessInterfaceColocSystemSyncSrc_Type()
)
wirelessInterfaceColocSystemSyncSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessInterfaceColocSystemSyncSrc.setStatus("current")


class _WirelessAPWifiWLANmode_Type(Integer32):
    """Custom type wirelessAPWifiWLANmode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessAPWifiWLANmode_Type.__name__ = "Integer32"
_WirelessAPWifiWLANmode_Object = MibScalar
wirelessAPWifiWLANmode = _WirelessAPWifiWLANmode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 61),
    _WirelessAPWifiWLANmode_Type()
)
wirelessAPWifiWLANmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPWifiWLANmode.setStatus("current")


class _ApWiFiDLCTSMode_Type(Integer32):
    """Custom type apWiFiDLCTSMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_ApWiFiDLCTSMode_Type.__name__ = "Integer32"
_ApWiFiDLCTSMode_Object = MibScalar
apWiFiDLCTSMode = _ApWiFiDLCTSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 62),
    _ApWiFiDLCTSMode_Type()
)
apWiFiDLCTSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWiFiDLCTSMode.setStatus("current")


class _ApWiFiULCTSRTSMode_Type(Integer32):
    """Custom type apWiFiULCTSRTSMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_ApWiFiULCTSRTSMode_Type.__name__ = "Integer32"
_ApWiFiULCTSRTSMode_Object = MibScalar
apWiFiULCTSRTSMode = _ApWiFiULCTSRTSMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 63),
    _ApWiFiULCTSRTSMode_Type()
)
apWiFiULCTSRTSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWiFiULCTSRTSMode.setStatus("current")


class _ApWiFiRTSThreshold_Type(Integer32):
    """Custom type apWiFiRTSThreshold based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2346),
    )


_ApWiFiRTSThreshold_Type.__name__ = "Integer32"
_ApWiFiRTSThreshold_Object = MibScalar
apWiFiRTSThreshold = _ApWiFiRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 2, 64),
    _ApWiFiRTSThreshold_Type()
)
apWiFiRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWiFiRTSThreshold.setStatus("current")
_WirelessPrefList_ObjectIdentity = ObjectIdentity
wirelessPrefList = _WirelessPrefList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3)
)
_PrefferedAPTable_Object = MibTable
prefferedAPTable = _PrefferedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1)
)
if mibBuilder.loadTexts:
    prefferedAPTable.setStatus("current")
_PrefferedAPEntry_Object = MibTableRow
prefferedAPEntry = _PrefferedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1)
)
prefferedAPEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "prefferedListTableEntryIndex"),
)
if mibBuilder.loadTexts:
    prefferedAPEntry.setStatus("current")


class _PrefferedListTableEntryIndex_Type(Integer32):
    """Custom type prefferedListTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PrefferedListTableEntryIndex_Type.__name__ = "Integer32"
_PrefferedListTableEntryIndex_Object = MibTableColumn
prefferedListTableEntryIndex = _PrefferedListTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1, 1),
    _PrefferedListTableEntryIndex_Type()
)
prefferedListTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefferedListTableEntryIndex.setStatus("current")


class _PrefferedListTableEntrySSID_Type(DisplayString):
    """Custom type prefferedListTableEntrySSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 32),
    )


_PrefferedListTableEntrySSID_Type.__name__ = "DisplayString"
_PrefferedListTableEntrySSID_Object = MibTableColumn
prefferedListTableEntrySSID = _PrefferedListTableEntrySSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1, 2),
    _PrefferedListTableEntrySSID_Type()
)
prefferedListTableEntrySSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefferedListTableEntrySSID.setStatus("current")


class _PrefferedListTableEntryKEY_Type(DisplayString):
    """Custom type prefferedListTableEntryKEY based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 63),
    )


_PrefferedListTableEntryKEY_Type.__name__ = "DisplayString"
_PrefferedListTableEntryKEY_Object = MibTableColumn
prefferedListTableEntryKEY = _PrefferedListTableEntryKEY_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1, 3),
    _PrefferedListTableEntryKEY_Type()
)
prefferedListTableEntryKEY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefferedListTableEntryKEY.setStatus("current")


class _PrefferedListTableSecurityMethod_Type(Integer32):
    """Custom type prefferedListTableSecurityMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_PrefferedListTableSecurityMethod_Type.__name__ = "Integer32"
_PrefferedListTableSecurityMethod_Object = MibTableColumn
prefferedListTableSecurityMethod = _PrefferedListTableSecurityMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 3, 1, 1, 4),
    _PrefferedListTableSecurityMethod_Type()
)
prefferedListTableSecurityMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefferedListTableSecurityMethod.setStatus("current")
_WirelessMIRList_ObjectIdentity = ObjectIdentity
wirelessMIRList = _WirelessMIRList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4)
)
_WirelessMIRProfileTable_Object = MibTable
wirelessMIRProfileTable = _WirelessMIRProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1)
)
if mibBuilder.loadTexts:
    wirelessMIRProfileTable.setStatus("current")
_WirelessMIRProfileEntry_Object = MibTableRow
wirelessMIRProfileEntry = _WirelessMIRProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1)
)
wirelessMIRProfileEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "wirelessMIRProfileIndex"),
)
if mibBuilder.loadTexts:
    wirelessMIRProfileEntry.setStatus("current")


class _WirelessMIRProfileIndex_Type(Integer32):
    """Custom type wirelessMIRProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WirelessMIRProfileIndex_Type.__name__ = "Integer32"
_WirelessMIRProfileIndex_Object = MibTableColumn
wirelessMIRProfileIndex = _WirelessMIRProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 1),
    _WirelessMIRProfileIndex_Type()
)
wirelessMIRProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRProfileIndex.setStatus("current")


class _WirelessMIRProfileNumber_Type(Integer32):
    """Custom type wirelessMIRProfileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WirelessMIRProfileNumber_Type.__name__ = "Integer32"
_WirelessMIRProfileNumber_Object = MibTableColumn
wirelessMIRProfileNumber = _WirelessMIRProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 2),
    _WirelessMIRProfileNumber_Type()
)
wirelessMIRProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRProfileNumber.setStatus("current")


class _WirelessMIRProfileDescription_Type(DisplayString):
    """Custom type wirelessMIRProfileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_WirelessMIRProfileDescription_Type.__name__ = "DisplayString"
_WirelessMIRProfileDescription_Object = MibTableColumn
wirelessMIRProfileDescription = _WirelessMIRProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 3),
    _WirelessMIRProfileDescription_Type()
)
wirelessMIRProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMIRProfileDescription.setStatus("current")


class _WirelessDLMIR_Type(Integer32):
    """Custom type wirelessDLMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_WirelessDLMIR_Type.__name__ = "Integer32"
_WirelessDLMIR_Object = MibTableColumn
wirelessDLMIR = _WirelessDLMIR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 4),
    _WirelessDLMIR_Type()
)
wirelessDLMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDLMIR.setStatus("current")


class _WirelessULMIR_Type(Integer32):
    """Custom type wirelessULMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_WirelessULMIR_Type.__name__ = "Integer32"
_WirelessULMIR_Object = MibTableColumn
wirelessULMIR = _WirelessULMIR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 4, 1, 1, 5),
    _WirelessULMIR_Type()
)
wirelessULMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessULMIR.setStatus("current")
_WirelessRadius_ObjectIdentity = ObjectIdentity
wirelessRadius = _WirelessRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5)
)


class _WirelessRadiusTimeout_Type(Integer32):
    """Custom type wirelessRadiusTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WirelessRadiusTimeout_Type.__name__ = "Integer32"
_WirelessRadiusTimeout_Object = MibScalar
wirelessRadiusTimeout = _WirelessRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 1),
    _WirelessRadiusTimeout_Type()
)
wirelessRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusTimeout.setStatus("current")


class _WirelessRadiusRetry_Type(Integer32):
    """Custom type wirelessRadiusRetry based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_WirelessRadiusRetry_Type.__name__ = "Integer32"
_WirelessRadiusRetry_Object = MibScalar
wirelessRadiusRetry = _WirelessRadiusRetry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 2),
    _WirelessRadiusRetry_Type()
)
wirelessRadiusRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusRetry.setStatus("current")


class _WirelessRadiusGUIUserAuth_Type(Integer32):
    """Custom type wirelessRadiusGUIUserAuth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessRadiusGUIUserAuth_Type.__name__ = "Integer32"
_WirelessRadiusGUIUserAuth_Object = MibScalar
wirelessRadiusGUIUserAuth = _WirelessRadiusGUIUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 3),
    _WirelessRadiusGUIUserAuth_Type()
)
wirelessRadiusGUIUserAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusGUIUserAuth.setStatus("current")


class _WirelessRadiusCurrentGUIUserAuth_Type(Integer32):
    """Custom type wirelessRadiusCurrentGUIUserAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_WirelessRadiusCurrentGUIUserAuth_Type.__name__ = "Integer32"
_WirelessRadiusCurrentGUIUserAuth_Object = MibScalar
wirelessRadiusCurrentGUIUserAuth = _WirelessRadiusCurrentGUIUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 4),
    _WirelessRadiusCurrentGUIUserAuth_Type()
)
wirelessRadiusCurrentGUIUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusCurrentGUIUserAuth.setStatus("current")


class _WirelessRadiusSeverInfo_Type(DisplayString):
    """Custom type wirelessRadiusSeverInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WirelessRadiusSeverInfo_Type.__name__ = "DisplayString"
_WirelessRadiusSeverInfo_Object = MibScalar
wirelessRadiusSeverInfo = _WirelessRadiusSeverInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 5),
    _WirelessRadiusSeverInfo_Type()
)
wirelessRadiusSeverInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusSeverInfo.setStatus("current")


class _WirelessRadiusIdentityStr_Type(DisplayString):
    """Custom type wirelessRadiusIdentityStr based on DisplayString"""
    defaultValue = OctetString("anonymous")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WirelessRadiusIdentityStr_Type.__name__ = "DisplayString"
_WirelessRadiusIdentityStr_Object = MibScalar
wirelessRadiusIdentityStr = _WirelessRadiusIdentityStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 6),
    _WirelessRadiusIdentityStr_Type()
)
wirelessRadiusIdentityStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusIdentityStr.setStatus("current")


class _WirelessRadiusIdentityRealm_Type(DisplayString):
    """Custom type wirelessRadiusIdentityRealm based on DisplayString"""
    defaultValue = OctetString("cambiumnetworks.com")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WirelessRadiusIdentityRealm_Type.__name__ = "DisplayString"
_WirelessRadiusIdentityRealm_Object = MibScalar
wirelessRadiusIdentityRealm = _WirelessRadiusIdentityRealm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 7),
    _WirelessRadiusIdentityRealm_Type()
)
wirelessRadiusIdentityRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusIdentityRealm.setStatus("current")


class _WirelessRadiusUsername_Type(DisplayString):
    """Custom type wirelessRadiusUsername based on DisplayString"""
    defaultValue = OctetString("cambium-station")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WirelessRadiusUsername_Type.__name__ = "DisplayString"
_WirelessRadiusUsername_Object = MibScalar
wirelessRadiusUsername = _WirelessRadiusUsername_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 8),
    _WirelessRadiusUsername_Type()
)
wirelessRadiusUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUsername.setStatus("current")


class _WirelessRadiusPassword_Type(DisplayString):
    """Custom type wirelessRadiusPassword based on DisplayString"""
    defaultValue = OctetString("cambium")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WirelessRadiusPassword_Type.__name__ = "DisplayString"
_WirelessRadiusPassword_Object = MibScalar
wirelessRadiusPassword = _WirelessRadiusPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 5, 9),
    _WirelessRadiusPassword_Type()
)
wirelessRadiusPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusPassword.setStatus("current")
_WirelessRadiusServerList_ObjectIdentity = ObjectIdentity
wirelessRadiusServerList = _WirelessRadiusServerList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6)
)
_WirelessRadiusServerTable_Object = MibTable
wirelessRadiusServerTable = _WirelessRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1)
)
if mibBuilder.loadTexts:
    wirelessRadiusServerTable.setStatus("current")
_WirelessRadiusServerEntry_Object = MibTableRow
wirelessRadiusServerEntry = _WirelessRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1)
)
wirelessRadiusServerEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "wirelessRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    wirelessRadiusServerEntry.setStatus("current")


class _WirelessRadiusServerIndex_Type(Integer32):
    """Custom type wirelessRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WirelessRadiusServerIndex_Type.__name__ = "Integer32"
_WirelessRadiusServerIndex_Object = MibTableColumn
wirelessRadiusServerIndex = _WirelessRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1, 1),
    _WirelessRadiusServerIndex_Type()
)
wirelessRadiusServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusServerIndex.setStatus("current")
_WirelessRadiusServerIP_Type = IpAddress
_WirelessRadiusServerIP_Object = MibTableColumn
wirelessRadiusServerIP = _WirelessRadiusServerIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1, 2),
    _WirelessRadiusServerIP_Type()
)
wirelessRadiusServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusServerIP.setStatus("current")


class _WirelessRadiusServerPort_Type(Integer32):
    """Custom type wirelessRadiusServerPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WirelessRadiusServerPort_Type.__name__ = "Integer32"
_WirelessRadiusServerPort_Object = MibTableColumn
wirelessRadiusServerPort = _WirelessRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1, 3),
    _WirelessRadiusServerPort_Type()
)
wirelessRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusServerPort.setStatus("current")


class _WirelessRadiusServerSecret_Type(DisplayString):
    """Custom type wirelessRadiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_WirelessRadiusServerSecret_Type.__name__ = "DisplayString"
_WirelessRadiusServerSecret_Object = MibTableColumn
wirelessRadiusServerSecret = _WirelessRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 6, 1, 1, 4),
    _WirelessRadiusServerSecret_Type()
)
wirelessRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusServerSecret.setStatus("current")
_WirelessRadiusCertificateList_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateList = _WirelessRadiusCertificateList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7)
)
_WirelessRadiusCertificateListRow1_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateListRow1 = _WirelessRadiusCertificateListRow1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 1)
)


class _WirelessRadiusUseDefCertificate_Type(Integer32):
    """Custom type wirelessRadiusUseDefCertificate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessRadiusUseDefCertificate_Type.__name__ = "Integer32"
_WirelessRadiusUseDefCertificate_Object = MibScalar
wirelessRadiusUseDefCertificate = _WirelessRadiusUseDefCertificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 1, 1),
    _WirelessRadiusUseDefCertificate_Type()
)
wirelessRadiusUseDefCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUseDefCertificate.setStatus("obsolete")
_WirelessRadiusDefCertificateView_Type = DisplayString
_WirelessRadiusDefCertificateView_Object = MibScalar
wirelessRadiusDefCertificateView = _WirelessRadiusDefCertificateView_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 1, 2),
    _WirelessRadiusDefCertificateView_Type()
)
wirelessRadiusDefCertificateView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusDefCertificateView.setStatus("obsolete")
_WirelessRadiusCertificateListRow2_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateListRow2 = _WirelessRadiusCertificateListRow2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 2)
)


class _WirelessRadiusUser1CertificateName_Type(DisplayString):
    """Custom type wirelessRadiusUser1CertificateName based on DisplayString"""
    defaultValue = OctetString("cert2")


_WirelessRadiusUser1CertificateName_Object = MibScalar
wirelessRadiusUser1CertificateName = _WirelessRadiusUser1CertificateName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 2, 1),
    _WirelessRadiusUser1CertificateName_Type()
)
wirelessRadiusUser1CertificateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUser1CertificateName.setStatus("obsolete")
_WirelessRadiusUser1CertificateView_Type = DisplayString
_WirelessRadiusUser1CertificateView_Object = MibScalar
wirelessRadiusUser1CertificateView = _WirelessRadiusUser1CertificateView_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 2, 2),
    _WirelessRadiusUser1CertificateView_Type()
)
wirelessRadiusUser1CertificateView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusUser1CertificateView.setStatus("obsolete")
_WirelessRadiusCertificateListRow3_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateListRow3 = _WirelessRadiusCertificateListRow3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 3)
)


class _WirelessRadiusUser2CertificateName_Type(DisplayString):
    """Custom type wirelessRadiusUser2CertificateName based on DisplayString"""
    defaultValue = OctetString("cert3")


_WirelessRadiusUser2CertificateName_Object = MibScalar
wirelessRadiusUser2CertificateName = _WirelessRadiusUser2CertificateName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 3, 1),
    _WirelessRadiusUser2CertificateName_Type()
)
wirelessRadiusUser2CertificateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUser2CertificateName.setStatus("obsolete")
_WirelessRadiusUser2CertificateView_Type = DisplayString
_WirelessRadiusUser2CertificateView_Object = MibScalar
wirelessRadiusUser2CertificateView = _WirelessRadiusUser2CertificateView_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 7, 3, 2),
    _WirelessRadiusUser2CertificateView_Type()
)
wirelessRadiusUser2CertificateView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusUser2CertificateView.setStatus("obsolete")
_WirelessRadiusCertificateSet_ObjectIdentity = ObjectIdentity
wirelessRadiusCertificateSet = _WirelessRadiusCertificateSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8)
)


class _WirelessRadiusDefaultCertificate_Type(OctetString):
    """Custom type wirelessRadiusDefaultCertificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_WirelessRadiusDefaultCertificate_Type.__name__ = "OctetString"
_WirelessRadiusDefaultCertificate_Object = MibScalar
wirelessRadiusDefaultCertificate = _WirelessRadiusDefaultCertificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8, 1),
    _WirelessRadiusDefaultCertificate_Type()
)
wirelessRadiusDefaultCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusDefaultCertificate.setStatus("current")


class _WirelessRadiusUser1Certificate_Type(OctetString):
    """Custom type wirelessRadiusUser1Certificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 8192),
    )


_WirelessRadiusUser1Certificate_Type.__name__ = "OctetString"
_WirelessRadiusUser1Certificate_Object = MibScalar
wirelessRadiusUser1Certificate = _WirelessRadiusUser1Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8, 2),
    _WirelessRadiusUser1Certificate_Type()
)
wirelessRadiusUser1Certificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUser1Certificate.setStatus("current")


class _WirelessRadiusUser2Certificate_Type(OctetString):
    """Custom type wirelessRadiusUser2Certificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 8192),
    )


_WirelessRadiusUser2Certificate_Type.__name__ = "OctetString"
_WirelessRadiusUser2Certificate_Object = MibScalar
wirelessRadiusUser2Certificate = _WirelessRadiusUser2Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8, 3),
    _WirelessRadiusUser2Certificate_Type()
)
wirelessRadiusUser2Certificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUser2Certificate.setStatus("current")


class _WirelessRadiusUseDefaultCertificate_Type(Integer32):
    """Custom type wirelessRadiusUseDefaultCertificate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessRadiusUseDefaultCertificate_Type.__name__ = "Integer32"
_WirelessRadiusUseDefaultCertificate_Object = MibScalar
wirelessRadiusUseDefaultCertificate = _WirelessRadiusUseDefaultCertificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 8, 4),
    _WirelessRadiusUseDefaultCertificate_Type()
)
wirelessRadiusUseDefaultCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUseDefaultCertificate.setStatus("current")
_WirelessRadiusExtraCertificateSet_ObjectIdentity = ObjectIdentity
wirelessRadiusExtraCertificateSet = _WirelessRadiusExtraCertificateSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9)
)


class _WirelessRadiusPMP320Certificate_Type(OctetString):
    """Custom type wirelessRadiusPMP320Certificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_WirelessRadiusPMP320Certificate_Type.__name__ = "OctetString"
_WirelessRadiusPMP320Certificate_Object = MibScalar
wirelessRadiusPMP320Certificate = _WirelessRadiusPMP320Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9, 1),
    _WirelessRadiusPMP320Certificate_Type()
)
wirelessRadiusPMP320Certificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusPMP320Certificate.setStatus("current")


class _WirelessRadiusUsePMP320Certificate_Type(Integer32):
    """Custom type wirelessRadiusUsePMP320Certificate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessRadiusUsePMP320Certificate_Type.__name__ = "Integer32"
_WirelessRadiusUsePMP320Certificate_Object = MibScalar
wirelessRadiusUsePMP320Certificate = _WirelessRadiusUsePMP320Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9, 2),
    _WirelessRadiusUsePMP320Certificate_Type()
)
wirelessRadiusUsePMP320Certificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUsePMP320Certificate.setStatus("current")


class _WirelessRadiusPMP450Certificate_Type(OctetString):
    """Custom type wirelessRadiusPMP450Certificate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_WirelessRadiusPMP450Certificate_Type.__name__ = "OctetString"
_WirelessRadiusPMP450Certificate_Object = MibScalar
wirelessRadiusPMP450Certificate = _WirelessRadiusPMP450Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9, 3),
    _WirelessRadiusPMP450Certificate_Type()
)
wirelessRadiusPMP450Certificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadiusPMP450Certificate.setStatus("current")


class _WirelessRadiusUsePMP450Certificate_Type(Integer32):
    """Custom type wirelessRadiusUsePMP450Certificate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WirelessRadiusUsePMP450Certificate_Type.__name__ = "Integer32"
_WirelessRadiusUsePMP450Certificate_Object = MibScalar
wirelessRadiusUsePMP450Certificate = _WirelessRadiusUsePMP450Certificate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 9, 4),
    _WirelessRadiusUsePMP450Certificate_Type()
)
wirelessRadiusUsePMP450Certificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessRadiusUsePMP450Certificate.setStatus("current")
_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 8, 10)
)
_L2Firewall_ObjectIdentity = ObjectIdentity
l2Firewall = _L2Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9)
)


class _L2FirewallEnable_Type(Integer32):
    """Custom type l2FirewallEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2FirewallEnable_Type.__name__ = "Integer32"
_L2FirewallEnable_Object = MibScalar
l2FirewallEnable = _L2FirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 1),
    _L2FirewallEnable_Type()
)
l2FirewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEnable.setStatus("current")
_L2FirewallTable_Object = MibTable
l2FirewallTable = _L2FirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2)
)
if mibBuilder.loadTexts:
    l2FirewallTable.setStatus("current")
_L2FirewallEntry_Object = MibTableRow
l2FirewallEntry = _L2FirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1)
)
l2FirewallEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "l2FirewallEntryIndex"),
)
if mibBuilder.loadTexts:
    l2FirewallEntry.setStatus("current")


class _L2FirewallEntryIndex_Type(Integer32):
    """Custom type l2FirewallEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_L2FirewallEntryIndex_Type.__name__ = "Integer32"
_L2FirewallEntryIndex_Object = MibTableColumn
l2FirewallEntryIndex = _L2FirewallEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 1),
    _L2FirewallEntryIndex_Type()
)
l2FirewallEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryIndex.setStatus("current")


class _L2FirewallEntryName_Type(DisplayString):
    """Custom type l2FirewallEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_L2FirewallEntryName_Type.__name__ = "DisplayString"
_L2FirewallEntryName_Object = MibTableColumn
l2FirewallEntryName = _L2FirewallEntryName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 2),
    _L2FirewallEntryName_Type()
)
l2FirewallEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryName.setStatus("current")


class _L2FirewallEntryAction_Type(Integer32):
    """Custom type l2FirewallEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2FirewallEntryAction_Type.__name__ = "Integer32"
_L2FirewallEntryAction_Object = MibTableColumn
l2FirewallEntryAction = _L2FirewallEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 3),
    _L2FirewallEntryAction_Type()
)
l2FirewallEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryAction.setStatus("current")


class _L2FirewallEntryInterface_Type(Integer32):
    """Custom type l2FirewallEntryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_L2FirewallEntryInterface_Type.__name__ = "Integer32"
_L2FirewallEntryInterface_Object = MibTableColumn
l2FirewallEntryInterface = _L2FirewallEntryInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 4),
    _L2FirewallEntryInterface_Type()
)
l2FirewallEntryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryInterface.setStatus("current")


class _L2FirewallEntryLog_Type(Integer32):
    """Custom type l2FirewallEntryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2FirewallEntryLog_Type.__name__ = "Integer32"
_L2FirewallEntryLog_Object = MibTableColumn
l2FirewallEntryLog = _L2FirewallEntryLog_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 5),
    _L2FirewallEntryLog_Type()
)
l2FirewallEntryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryLog.setStatus("current")


class _L2FirewallEntryEtherType_Type(Integer32):
    """Custom type l2FirewallEntryEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2FirewallEntryEtherType_Type.__name__ = "Integer32"
_L2FirewallEntryEtherType_Object = MibTableColumn
l2FirewallEntryEtherType = _L2FirewallEntryEtherType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 6),
    _L2FirewallEntryEtherType_Type()
)
l2FirewallEntryEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryEtherType.setStatus("current")


class _L2FirewallEntryVlanID_Type(Integer32):
    """Custom type l2FirewallEntryVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_L2FirewallEntryVlanID_Type.__name__ = "Integer32"
_L2FirewallEntryVlanID_Object = MibTableColumn
l2FirewallEntryVlanID = _L2FirewallEntryVlanID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 7),
    _L2FirewallEntryVlanID_Type()
)
l2FirewallEntryVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryVlanID.setStatus("current")


class _L2FirewallEntrySrcMAC_Type(DisplayString):
    """Custom type l2FirewallEntrySrcMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_L2FirewallEntrySrcMAC_Type.__name__ = "DisplayString"
_L2FirewallEntrySrcMAC_Object = MibTableColumn
l2FirewallEntrySrcMAC = _L2FirewallEntrySrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 8),
    _L2FirewallEntrySrcMAC_Type()
)
l2FirewallEntrySrcMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntrySrcMAC.setStatus("current")


class _L2FirewallEntrySrcMask_Type(DisplayString):
    """Custom type l2FirewallEntrySrcMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_L2FirewallEntrySrcMask_Type.__name__ = "DisplayString"
_L2FirewallEntrySrcMask_Object = MibTableColumn
l2FirewallEntrySrcMask = _L2FirewallEntrySrcMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 9),
    _L2FirewallEntrySrcMask_Type()
)
l2FirewallEntrySrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntrySrcMask.setStatus("current")


class _L2FirewallEntryDstMAC_Type(DisplayString):
    """Custom type l2FirewallEntryDstMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_L2FirewallEntryDstMAC_Type.__name__ = "DisplayString"
_L2FirewallEntryDstMAC_Object = MibTableColumn
l2FirewallEntryDstMAC = _L2FirewallEntryDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 10),
    _L2FirewallEntryDstMAC_Type()
)
l2FirewallEntryDstMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryDstMAC.setStatus("current")


class _L2FirewallEntryDstMask_Type(DisplayString):
    """Custom type l2FirewallEntryDstMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(11, 17),
    )


_L2FirewallEntryDstMask_Type.__name__ = "DisplayString"
_L2FirewallEntryDstMask_Object = MibTableColumn
l2FirewallEntryDstMask = _L2FirewallEntryDstMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 2, 1, 11),
    _L2FirewallEntryDstMask_Type()
)
l2FirewallEntryDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2FirewallEntryDstMask.setStatus("current")


class _L2WanRemoteAccess_Type(Integer32):
    """Custom type l2WanRemoteAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2WanRemoteAccess_Type.__name__ = "Integer32"
_L2WanRemoteAccess_Object = MibScalar
l2WanRemoteAccess = _L2WanRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 3),
    _L2WanRemoteAccess_Type()
)
l2WanRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2WanRemoteAccess.setStatus("current")


class _L2SnmpLanRemoteAccess_Type(Integer32):
    """Custom type l2SnmpLanRemoteAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2SnmpLanRemoteAccess_Type.__name__ = "Integer32"
_L2SnmpLanRemoteAccess_Object = MibScalar
l2SnmpLanRemoteAccess = _L2SnmpLanRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 4),
    _L2SnmpLanRemoteAccess_Type()
)
l2SnmpLanRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2SnmpLanRemoteAccess.setStatus("current")


class _L2DHCPServersBelowSTA_Type(Integer32):
    """Custom type l2DHCPServersBelowSTA based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2DHCPServersBelowSTA_Type.__name__ = "Integer32"
_L2DHCPServersBelowSTA_Object = MibScalar
l2DHCPServersBelowSTA = _L2DHCPServersBelowSTA_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 5),
    _L2DHCPServersBelowSTA_Type()
)
l2DHCPServersBelowSTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2DHCPServersBelowSTA.setStatus("current")


class _L2LanRemoteAccess_Type(Integer32):
    """Custom type l2LanRemoteAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L2LanRemoteAccess_Type.__name__ = "Integer32"
_L2LanRemoteAccess_Object = MibScalar
l2LanRemoteAccess = _L2LanRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 9, 6),
    _L2LanRemoteAccess_Type()
)
l2LanRemoteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2LanRemoteAccess.setStatus("current")
_L3Firewall_ObjectIdentity = ObjectIdentity
l3Firewall = _L3Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10)
)


class _L3FirewallEnable_Type(Integer32):
    """Custom type l3FirewallEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L3FirewallEnable_Type.__name__ = "Integer32"
_L3FirewallEnable_Object = MibScalar
l3FirewallEnable = _L3FirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 1),
    _L3FirewallEnable_Type()
)
l3FirewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEnable.setStatus("current")
_L3FirewallTable_Object = MibTable
l3FirewallTable = _L3FirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2)
)
if mibBuilder.loadTexts:
    l3FirewallTable.setStatus("current")
_L3FirewallEntry_Object = MibTableRow
l3FirewallEntry = _L3FirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1)
)
l3FirewallEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "l3FirewallEntryIndex"),
)
if mibBuilder.loadTexts:
    l3FirewallEntry.setStatus("current")


class _L3FirewallEntryIndex_Type(Integer32):
    """Custom type l3FirewallEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_L3FirewallEntryIndex_Type.__name__ = "Integer32"
_L3FirewallEntryIndex_Object = MibTableColumn
l3FirewallEntryIndex = _L3FirewallEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 1),
    _L3FirewallEntryIndex_Type()
)
l3FirewallEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryIndex.setStatus("current")


class _L3FirewallEntryName_Type(DisplayString):
    """Custom type l3FirewallEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 128),
    )


_L3FirewallEntryName_Type.__name__ = "DisplayString"
_L3FirewallEntryName_Object = MibTableColumn
l3FirewallEntryName = _L3FirewallEntryName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 2),
    _L3FirewallEntryName_Type()
)
l3FirewallEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryName.setStatus("current")


class _L3FirewallEntryAction_Type(Integer32):
    """Custom type l3FirewallEntryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L3FirewallEntryAction_Type.__name__ = "Integer32"
_L3FirewallEntryAction_Object = MibTableColumn
l3FirewallEntryAction = _L3FirewallEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 3),
    _L3FirewallEntryAction_Type()
)
l3FirewallEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryAction.setStatus("current")


class _L3FirewallEntryInterface_Type(Integer32):
    """Custom type l3FirewallEntryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_L3FirewallEntryInterface_Type.__name__ = "Integer32"
_L3FirewallEntryInterface_Object = MibTableColumn
l3FirewallEntryInterface = _L3FirewallEntryInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 4),
    _L3FirewallEntryInterface_Type()
)
l3FirewallEntryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryInterface.setStatus("current")


class _L3FirewallEntryLog_Type(Integer32):
    """Custom type l3FirewallEntryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_L3FirewallEntryLog_Type.__name__ = "Integer32"
_L3FirewallEntryLog_Object = MibTableColumn
l3FirewallEntryLog = _L3FirewallEntryLog_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 5),
    _L3FirewallEntryLog_Type()
)
l3FirewallEntryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryLog.setStatus("current")


class _L3FirewallEntryProtocol_Type(Integer32):
    """Custom type l3FirewallEntryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
    )


_L3FirewallEntryProtocol_Type.__name__ = "Integer32"
_L3FirewallEntryProtocol_Object = MibTableColumn
l3FirewallEntryProtocol = _L3FirewallEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 6),
    _L3FirewallEntryProtocol_Type()
)
l3FirewallEntryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryProtocol.setStatus("current")


class _L3FirewallEntryPort_Type(Integer32):
    """Custom type l3FirewallEntryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L3FirewallEntryPort_Type.__name__ = "Integer32"
_L3FirewallEntryPort_Object = MibTableColumn
l3FirewallEntryPort = _L3FirewallEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 7),
    _L3FirewallEntryPort_Type()
)
l3FirewallEntryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryPort.setStatus("current")
_L3FirewallEntrySrcIP_Type = IpAddress
_L3FirewallEntrySrcIP_Object = MibTableColumn
l3FirewallEntrySrcIP = _L3FirewallEntrySrcIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 8),
    _L3FirewallEntrySrcIP_Type()
)
l3FirewallEntrySrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntrySrcIP.setStatus("current")
_L3FirewallEntrySrcMask_Type = IpAddress
_L3FirewallEntrySrcMask_Object = MibTableColumn
l3FirewallEntrySrcMask = _L3FirewallEntrySrcMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 9),
    _L3FirewallEntrySrcMask_Type()
)
l3FirewallEntrySrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntrySrcMask.setStatus("current")
_L3FirewallEntryDstIP_Type = IpAddress
_L3FirewallEntryDstIP_Object = MibTableColumn
l3FirewallEntryDstIP = _L3FirewallEntryDstIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 10),
    _L3FirewallEntryDstIP_Type()
)
l3FirewallEntryDstIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryDstIP.setStatus("current")
_L3FirewallEntryDstMask_Type = IpAddress
_L3FirewallEntryDstMask_Object = MibTableColumn
l3FirewallEntryDstMask = _L3FirewallEntryDstMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 11),
    _L3FirewallEntryDstMask_Type()
)
l3FirewallEntryDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryDstMask.setStatus("current")


class _L3FirewallEntryDSCP_Type(Integer32):
    """Custom type l3FirewallEntryDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_L3FirewallEntryDSCP_Type.__name__ = "Integer32"
_L3FirewallEntryDSCP_Object = MibTableColumn
l3FirewallEntryDSCP = _L3FirewallEntryDSCP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 12),
    _L3FirewallEntryDSCP_Type()
)
l3FirewallEntryDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryDSCP.setStatus("current")


class _L3FirewallEntryToS_Type(Integer32):
    """Custom type l3FirewallEntryToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_L3FirewallEntryToS_Type.__name__ = "Integer32"
_L3FirewallEntryToS_Object = MibTableColumn
l3FirewallEntryToS = _L3FirewallEntryToS_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 10, 2, 1, 13),
    _L3FirewallEntryToS_Type()
)
l3FirewallEntryToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3FirewallEntryToS.setStatus("current")
_ConfQoS_ObjectIdentity = ObjectIdentity
confQoS = _ConfQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11)
)


class _VoipEnable_Type(Integer32):
    """Custom type voipEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_VoipEnable_Type.__name__ = "Integer32"
_VoipEnable_Object = MibScalar
voipEnable = _VoipEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 1),
    _VoipEnable_Type()
)
voipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voipEnable.setStatus("current")


class _QosEnable_Type(Integer32):
    """Custom type qosEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_QosEnable_Type.__name__ = "Integer32"
_QosEnable_Object = MibScalar
qosEnable = _QosEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 2),
    _QosEnable_Type()
)
qosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEnable.setStatus("current")
_ClassificationListTable_Object = MibTable
classificationListTable = _ClassificationListTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3)
)
if mibBuilder.loadTexts:
    classificationListTable.setStatus("current")
_ClassificationListEntry_Object = MibTableRow
classificationListEntry = _ClassificationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1)
)
classificationListEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "classificationRuleIndex"),
)
if mibBuilder.loadTexts:
    classificationListEntry.setStatus("current")


class _ClassificationRuleIndex_Type(Integer32):
    """Custom type classificationRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ClassificationRuleIndex_Type.__name__ = "Integer32"
_ClassificationRuleIndex_Object = MibTableColumn
classificationRuleIndex = _ClassificationRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 1),
    _ClassificationRuleIndex_Type()
)
classificationRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleIndex.setStatus("current")


class _ClassificationRuleType_Type(Integer32):
    """Custom type classificationRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 9),
    )


_ClassificationRuleType_Type.__name__ = "Integer32"
_ClassificationRuleType_Object = MibTableColumn
classificationRuleType = _ClassificationRuleType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 2),
    _ClassificationRuleType_Type()
)
classificationRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleType.setStatus("current")


class _ClassificationRuleValue_Type(Integer32):
    """Custom type classificationRuleValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClassificationRuleValue_Type.__name__ = "Integer32"
_ClassificationRuleValue_Object = MibTableColumn
classificationRuleValue = _ClassificationRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 3),
    _ClassificationRuleValue_Type()
)
classificationRuleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleValue.setStatus("current")
_ClassificationRuleIP_Type = IpAddress
_ClassificationRuleIP_Object = MibTableColumn
classificationRuleIP = _ClassificationRuleIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 4),
    _ClassificationRuleIP_Type()
)
classificationRuleIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleIP.setStatus("current")


class _ClassificationRuleMAC_Type(DisplayString):
    """Custom type classificationRuleMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(17, 17),
    )


_ClassificationRuleMAC_Type.__name__ = "DisplayString"
_ClassificationRuleMAC_Object = MibTableColumn
classificationRuleMAC = _ClassificationRuleMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 5),
    _ClassificationRuleMAC_Type()
)
classificationRuleMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleMAC.setStatus("current")


class _ClassificationRuleMask_Type(DisplayString):
    """Custom type classificationRuleMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 17),
    )


_ClassificationRuleMask_Type.__name__ = "DisplayString"
_ClassificationRuleMask_Object = MibTableColumn
classificationRuleMask = _ClassificationRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 6),
    _ClassificationRuleMask_Type()
)
classificationRuleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleMask.setStatus("current")


class _ClassificationRuleDirection_Type(Integer32):
    """Custom type classificationRuleDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3),
    )


_ClassificationRuleDirection_Type.__name__ = "Integer32"
_ClassificationRuleDirection_Object = MibTableColumn
classificationRuleDirection = _ClassificationRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 7),
    _ClassificationRuleDirection_Type()
)
classificationRuleDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleDirection.setStatus("current")


class _ClassificationRuleQueue_Type(Integer32):
    """Custom type classificationRuleQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3),
    )


_ClassificationRuleQueue_Type.__name__ = "Integer32"
_ClassificationRuleQueue_Object = MibTableColumn
classificationRuleQueue = _ClassificationRuleQueue_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 3, 1, 8),
    _ClassificationRuleQueue_Type()
)
classificationRuleQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classificationRuleQueue.setStatus("current")


class _McPriority_Type(Integer32):
    """Custom type mcPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_McPriority_Type.__name__ = "Integer32"
_McPriority_Object = MibScalar
mcPriority = _McPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 4),
    _McPriority_Type()
)
mcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcPriority.setStatus("current")


class _BcPriority_Type(Integer32):
    """Custom type bcPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_BcPriority_Type.__name__ = "Integer32"
_BcPriority_Object = MibScalar
bcPriority = _BcPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 11, 5),
    _BcPriority_Type()
)
bcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcPriority.setStatus("current")
_Dmz_ObjectIdentity = ObjectIdentity
dmz = _Dmz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 12)
)


class _DmzEnable_Type(Integer32):
    """Custom type dmzEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DmzEnable_Type.__name__ = "Integer32"
_DmzEnable_Object = MibScalar
dmzEnable = _DmzEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 12, 1),
    _DmzEnable_Type()
)
dmzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmzEnable.setStatus("current")
_DmzIPAddress_Type = IpAddress
_DmzIPAddress_Object = MibScalar
dmzIPAddress = _DmzIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 12, 2),
    _DmzIPAddress_Type()
)
dmzIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmzIPAddress.setStatus("current")
_PortForwarding_ObjectIdentity = ObjectIdentity
portForwarding = _PortForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13)
)


class _PortForwardingEntryEnable_Type(Integer32):
    """Custom type portForwardingEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_PortForwardingEntryEnable_Type.__name__ = "Integer32"
_PortForwardingEntryEnable_Object = MibScalar
portForwardingEntryEnable = _PortForwardingEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 1),
    _PortForwardingEntryEnable_Type()
)
portForwardingEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingEntryEnable.setStatus("current")
_PortForwardingTable_Object = MibTable
portForwardingTable = _PortForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2)
)
if mibBuilder.loadTexts:
    portForwardingTable.setStatus("current")
_PortForwardingEntry_Object = MibTableRow
portForwardingEntry = _PortForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1)
)
portForwardingEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "portForwardingTableEntryIndex"),
)
if mibBuilder.loadTexts:
    portForwardingEntry.setStatus("current")


class _PortForwardingTableEntryIndex_Type(Integer32):
    """Custom type portForwardingTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PortForwardingTableEntryIndex_Type.__name__ = "Integer32"
_PortForwardingTableEntryIndex_Object = MibTableColumn
portForwardingTableEntryIndex = _PortForwardingTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 1),
    _PortForwardingTableEntryIndex_Type()
)
portForwardingTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryIndex.setStatus("current")


class _PortForwardingTableEntryProtocol_Type(Integer32):
    """Custom type portForwardingTableEntryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_PortForwardingTableEntryProtocol_Type.__name__ = "Integer32"
_PortForwardingTableEntryProtocol_Object = MibTableColumn
portForwardingTableEntryProtocol = _PortForwardingTableEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 2),
    _PortForwardingTableEntryProtocol_Type()
)
portForwardingTableEntryProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryProtocol.setStatus("current")


class _PortForwardingTableEntryWLANPortBegin_Type(Integer32):
    """Custom type portForwardingTableEntryWLANPortBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortForwardingTableEntryWLANPortBegin_Type.__name__ = "Integer32"
_PortForwardingTableEntryWLANPortBegin_Object = MibTableColumn
portForwardingTableEntryWLANPortBegin = _PortForwardingTableEntryWLANPortBegin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 3),
    _PortForwardingTableEntryWLANPortBegin_Type()
)
portForwardingTableEntryWLANPortBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryWLANPortBegin.setStatus("current")


class _PortForwardingTableEntryWLANPortEnd_Type(Integer32):
    """Custom type portForwardingTableEntryWLANPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortForwardingTableEntryWLANPortEnd_Type.__name__ = "Integer32"
_PortForwardingTableEntryWLANPortEnd_Object = MibTableColumn
portForwardingTableEntryWLANPortEnd = _PortForwardingTableEntryWLANPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 4),
    _PortForwardingTableEntryWLANPortEnd_Type()
)
portForwardingTableEntryWLANPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryWLANPortEnd.setStatus("current")
_PortForwardingTableEntryLANIP_Type = IpAddress
_PortForwardingTableEntryLANIP_Object = MibTableColumn
portForwardingTableEntryLANIP = _PortForwardingTableEntryLANIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 13, 2, 1, 5),
    _PortForwardingTableEntryLANIP_Type()
)
portForwardingTableEntryLANIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingTableEntryLANIP.setStatus("current")
_Vlans_ObjectIdentity = ObjectIdentity
vlans = _Vlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14)
)
_MembershipVLANTable_Object = MibTable
membershipVLANTable = _MembershipVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3)
)
if mibBuilder.loadTexts:
    membershipVLANTable.setStatus("current")
_MembershipVLANEntry_Object = MibTableRow
membershipVLANEntry = _MembershipVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3, 1)
)
membershipVLANEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "membershipVLANTableEntryIndex"),
)
if mibBuilder.loadTexts:
    membershipVLANEntry.setStatus("current")


class _MembershipVLANTableEntryIndex_Type(Integer32):
    """Custom type membershipVLANTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MembershipVLANTableEntryIndex_Type.__name__ = "Integer32"
_MembershipVLANTableEntryIndex_Object = MibTableColumn
membershipVLANTableEntryIndex = _MembershipVLANTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3, 1, 1),
    _MembershipVLANTableEntryIndex_Type()
)
membershipVLANTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    membershipVLANTableEntryIndex.setStatus("current")


class _MembershipVLANTableEntryVIDBegin_Type(Integer32):
    """Custom type membershipVLANTableEntryVIDBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_MembershipVLANTableEntryVIDBegin_Type.__name__ = "Integer32"
_MembershipVLANTableEntryVIDBegin_Object = MibTableColumn
membershipVLANTableEntryVIDBegin = _MembershipVLANTableEntryVIDBegin_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3, 1, 2),
    _MembershipVLANTableEntryVIDBegin_Type()
)
membershipVLANTableEntryVIDBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    membershipVLANTableEntryVIDBegin.setStatus("current")


class _MembershipVLANTableEntryVIDEnd_Type(Integer32):
    """Custom type membershipVLANTableEntryVIDEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_MembershipVLANTableEntryVIDEnd_Type.__name__ = "Integer32"
_MembershipVLANTableEntryVIDEnd_Object = MibTableColumn
membershipVLANTableEntryVIDEnd = _MembershipVLANTableEntryVIDEnd_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 3, 1, 3),
    _MembershipVLANTableEntryVIDEnd_Type()
)
membershipVLANTableEntryVIDEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    membershipVLANTableEntryVIDEnd.setStatus("current")
_MappingVLANTable_Object = MibTable
mappingVLANTable = _MappingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5)
)
if mibBuilder.loadTexts:
    mappingVLANTable.setStatus("current")
_MappingVLANEntry_Object = MibTableRow
mappingVLANEntry = _MappingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5, 1)
)
mappingVLANEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "mappingVLANTableEntryIndex"),
)
if mibBuilder.loadTexts:
    mappingVLANEntry.setStatus("current")


class _MappingVLANTableEntryIndex_Type(Integer32):
    """Custom type mappingVLANTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MappingVLANTableEntryIndex_Type.__name__ = "Integer32"
_MappingVLANTableEntryIndex_Object = MibTableColumn
mappingVLANTableEntryIndex = _MappingVLANTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5, 1, 1),
    _MappingVLANTableEntryIndex_Type()
)
mappingVLANTableEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingVLANTableEntryIndex.setStatus("current")


class _MappingVLANTableEntryCVLAN_Type(Integer32):
    """Custom type mappingVLANTableEntryCVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_MappingVLANTableEntryCVLAN_Type.__name__ = "Integer32"
_MappingVLANTableEntryCVLAN_Object = MibTableColumn
mappingVLANTableEntryCVLAN = _MappingVLANTableEntryCVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5, 1, 2),
    _MappingVLANTableEntryCVLAN_Type()
)
mappingVLANTableEntryCVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingVLANTableEntryCVLAN.setStatus("current")


class _MappingVLANTableEntrySVLAN_Type(Integer32):
    """Custom type mappingVLANTableEntrySVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_MappingVLANTableEntrySVLAN_Type.__name__ = "Integer32"
_MappingVLANTableEntrySVLAN_Object = MibTableColumn
mappingVLANTableEntrySVLAN = _MappingVLANTableEntrySVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 14, 5, 1, 3),
    _MappingVLANTableEntrySVLAN_Type()
)
mappingVLANTableEntrySVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mappingVLANTableEntrySVLAN.setStatus("current")
_Dlkm_ObjectIdentity = ObjectIdentity
dlkm = _Dlkm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 15)
)


class _DlkmNATSIPHelpers_Type(Integer32):
    """Custom type dlkmNATSIPHelpers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DlkmNATSIPHelpers_Type.__name__ = "Integer32"
_DlkmNATSIPHelpers_Object = MibScalar
dlkmNATSIPHelpers = _DlkmNATSIPHelpers_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 15, 1),
    _DlkmNATSIPHelpers_Type()
)
dlkmNATSIPHelpers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlkmNATSIPHelpers.setStatus("current")
_Routing_ObjectIdentity = ObjectIdentity
routing = _Routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16)
)


class _StaticRoutesEnableMain_Type(Integer32):
    """Custom type staticRoutesEnableMain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_StaticRoutesEnableMain_Type.__name__ = "Integer32"
_StaticRoutesEnableMain_Object = MibScalar
staticRoutesEnableMain = _StaticRoutesEnableMain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 1),
    _StaticRoutesEnableMain_Type()
)
staticRoutesEnableMain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRoutesEnableMain.setStatus("current")
_CambiumStaticRoutesCnfTable_Object = MibTable
cambiumStaticRoutesCnfTable = _CambiumStaticRoutesCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2)
)
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfTable.setStatus("current")
_CambiumStaticRoutesCnfEntry_Object = MibTableRow
cambiumStaticRoutesCnfEntry = _CambiumStaticRoutesCnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1)
)
cambiumStaticRoutesCnfEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumStaticRoutesCnfIndex"),
)
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfEntry.setStatus("current")


class _CambiumStaticRoutesCnfIndex_Type(Integer32):
    """Custom type cambiumStaticRoutesCnfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CambiumStaticRoutesCnfIndex_Type.__name__ = "Integer32"
_CambiumStaticRoutesCnfIndex_Object = MibTableColumn
cambiumStaticRoutesCnfIndex = _CambiumStaticRoutesCnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 1),
    _CambiumStaticRoutesCnfIndex_Type()
)
cambiumStaticRoutesCnfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfIndex.setStatus("current")
_CambiumStaticRoutesCnfDestIP_Type = IpAddress
_CambiumStaticRoutesCnfDestIP_Object = MibTableColumn
cambiumStaticRoutesCnfDestIP = _CambiumStaticRoutesCnfDestIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 2),
    _CambiumStaticRoutesCnfDestIP_Type()
)
cambiumStaticRoutesCnfDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfDestIP.setStatus("current")
_CambiumStaticRoutesCnfGW_Type = IpAddress
_CambiumStaticRoutesCnfGW_Object = MibTableColumn
cambiumStaticRoutesCnfGW = _CambiumStaticRoutesCnfGW_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 3),
    _CambiumStaticRoutesCnfGW_Type()
)
cambiumStaticRoutesCnfGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfGW.setStatus("current")
_CambiumStaticRoutesCnfNetmask_Type = IpAddress
_CambiumStaticRoutesCnfNetmask_Object = MibTableColumn
cambiumStaticRoutesCnfNetmask = _CambiumStaticRoutesCnfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 4),
    _CambiumStaticRoutesCnfNetmask_Type()
)
cambiumStaticRoutesCnfNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfNetmask.setStatus("current")


class _CambiumStaticRoutesCnfEnbl_Type(Integer32):
    """Custom type cambiumStaticRoutesCnfEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumStaticRoutesCnfEnbl_Type.__name__ = "Integer32"
_CambiumStaticRoutesCnfEnbl_Object = MibTableColumn
cambiumStaticRoutesCnfEnbl = _CambiumStaticRoutesCnfEnbl_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 5),
    _CambiumStaticRoutesCnfEnbl_Type()
)
cambiumStaticRoutesCnfEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfEnbl.setStatus("current")


class _CambiumStaticRoutesCnfInfo_Type(DisplayString):
    """Custom type cambiumStaticRoutesCnfInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CambiumStaticRoutesCnfInfo_Type.__name__ = "DisplayString"
_CambiumStaticRoutesCnfInfo_Object = MibTableColumn
cambiumStaticRoutesCnfInfo = _CambiumStaticRoutesCnfInfo_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 16, 2, 1, 6),
    _CambiumStaticRoutesCnfInfo_Type()
)
cambiumStaticRoutesCnfInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStaticRoutesCnfInfo.setStatus("current")
_CambiumDeviceAgent_ObjectIdentity = ObjectIdentity
cambiumDeviceAgent = _CambiumDeviceAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20)
)


class _CambiumDeviceAgentEnable_Type(Integer32):
    """Custom type cambiumDeviceAgentEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumDeviceAgentEnable_Type.__name__ = "Integer32"
_CambiumDeviceAgentEnable_Object = MibScalar
cambiumDeviceAgentEnable = _CambiumDeviceAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 1),
    _CambiumDeviceAgentEnable_Type()
)
cambiumDeviceAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceAgentEnable.setStatus("current")


class _CambiumDeviceAgentCNSURL_Type(DisplayString):
    """Custom type cambiumDeviceAgentCNSURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumDeviceAgentCNSURL_Type.__name__ = "DisplayString"
_CambiumDeviceAgentCNSURL_Object = MibScalar
cambiumDeviceAgentCNSURL = _CambiumDeviceAgentCNSURL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 2),
    _CambiumDeviceAgentCNSURL_Type()
)
cambiumDeviceAgentCNSURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceAgentCNSURL.setStatus("current")


class _CambiumCNSDeviceAgentID_Type(DisplayString):
    """Custom type cambiumCNSDeviceAgentID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumCNSDeviceAgentID_Type.__name__ = "DisplayString"
_CambiumCNSDeviceAgentID_Object = MibScalar
cambiumCNSDeviceAgentID = _CambiumCNSDeviceAgentID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 3),
    _CambiumCNSDeviceAgentID_Type()
)
cambiumCNSDeviceAgentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCNSDeviceAgentID.setStatus("current")


class _CambiumCNSDeviceAgentPassword_Type(DisplayString):
    """Custom type cambiumCNSDeviceAgentPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumCNSDeviceAgentPassword_Type.__name__ = "DisplayString"
_CambiumCNSDeviceAgentPassword_Object = MibScalar
cambiumCNSDeviceAgentPassword = _CambiumCNSDeviceAgentPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 20, 4),
    _CambiumCNSDeviceAgentPassword_Type()
)
cambiumCNSDeviceAgentPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCNSDeviceAgentPassword.setStatus("current")
_Upnpd_ObjectIdentity = ObjectIdentity
upnpd = _Upnpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 21)
)


class _NetworkUPNP_Type(Integer32):
    """Custom type networkUPNP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkUPNP_Type.__name__ = "Integer32"
_NetworkUPNP_Object = MibScalar
networkUPNP = _NetworkUPNP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 21, 1),
    _NetworkUPNP_Type()
)
networkUPNP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkUPNP.setStatus("current")


class _NetworkNATPMP_Type(Integer32):
    """Custom type networkNATPMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_NetworkNATPMP_Type.__name__ = "Integer32"
_NetworkNATPMP_Object = MibScalar
networkNATPMP = _NetworkNATPMP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 3, 21, 2),
    _NetworkNATPMP_Type()
)
networkNATPMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkNATPMP.setStatus("current")
_Cambiumpmp80211SystemActions_ObjectIdentity = ObjectIdentity
cambiumpmp80211SystemActions = _Cambiumpmp80211SystemActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4)
)


class _Cambiumpmp80211DeviceReboot_Type(Integer32):
    """Custom type cambiumpmp80211DeviceReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211DeviceReboot_Type.__name__ = "Integer32"
_Cambiumpmp80211DeviceReboot_Object = MibScalar
cambiumpmp80211DeviceReboot = _Cambiumpmp80211DeviceReboot_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 1),
    _Cambiumpmp80211DeviceReboot_Type()
)
cambiumpmp80211DeviceReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211DeviceReboot.setStatus("current")


class _Cambiumpmp80211ConfigurationReset_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211ConfigurationReset_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationReset_Object = MibScalar
cambiumpmp80211ConfigurationReset = _Cambiumpmp80211ConfigurationReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 2),
    _Cambiumpmp80211ConfigurationReset_Type()
)
cambiumpmp80211ConfigurationReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationReset.setStatus("current")


class _Cambiumpmp80211ConfigurationSave_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211ConfigurationSave_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationSave_Object = MibScalar
cambiumpmp80211ConfigurationSave = _Cambiumpmp80211ConfigurationSave_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 3),
    _Cambiumpmp80211ConfigurationSave_Type()
)
cambiumpmp80211ConfigurationSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationSave.setStatus("current")


class _Cambiumpmp80211ConfigurationApply_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211ConfigurationApply_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationApply_Object = MibScalar
cambiumpmp80211ConfigurationApply = _Cambiumpmp80211ConfigurationApply_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 4),
    _Cambiumpmp80211ConfigurationApply_Type()
)
cambiumpmp80211ConfigurationApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationApply.setStatus("current")


class _Cambiumpmp80211ConfigurationDiscard_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211ConfigurationDiscard_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationDiscard_Object = MibScalar
cambiumpmp80211ConfigurationDiscard = _Cambiumpmp80211ConfigurationDiscard_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 5),
    _Cambiumpmp80211ConfigurationDiscard_Type()
)
cambiumpmp80211ConfigurationDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationDiscard.setStatus("current")


class _Cambiumpmp80211ConfigurationState_Type(Integer32):
    """Custom type cambiumpmp80211ConfigurationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cambiumpmp80211ConfigurationState_Type.__name__ = "Integer32"
_Cambiumpmp80211ConfigurationState_Object = MibScalar
cambiumpmp80211ConfigurationState = _Cambiumpmp80211ConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 6),
    _Cambiumpmp80211ConfigurationState_Type()
)
cambiumpmp80211ConfigurationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211ConfigurationState.setStatus("current")
_Cambiumpmp80211SoftwareUpdate_Type = DisplayString
_Cambiumpmp80211SoftwareUpdate_Object = MibScalar
cambiumpmp80211SoftwareUpdate = _Cambiumpmp80211SoftwareUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 7),
    _Cambiumpmp80211SoftwareUpdate_Type()
)
cambiumpmp80211SoftwareUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdate.setStatus("current")


class _Cambiumpmp80211SoftwareUpdateStatus_Type(Integer32):
    """Custom type cambiumpmp80211SoftwareUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Cambiumpmp80211SoftwareUpdateStatus_Type.__name__ = "Integer32"
_Cambiumpmp80211SoftwareUpdateStatus_Object = MibScalar
cambiumpmp80211SoftwareUpdateStatus = _Cambiumpmp80211SoftwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 8),
    _Cambiumpmp80211SoftwareUpdateStatus_Type()
)
cambiumpmp80211SoftwareUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdateStatus.setStatus("current")


class _Cambiumpmp80211STAListUpdate_Type(Integer32):
    """Custom type cambiumpmp80211STAListUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211STAListUpdate_Type.__name__ = "Integer32"
_Cambiumpmp80211STAListUpdate_Object = MibScalar
cambiumpmp80211STAListUpdate = _Cambiumpmp80211STAListUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 9),
    _Cambiumpmp80211STAListUpdate_Type()
)
cambiumpmp80211STAListUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211STAListUpdate.setStatus("current")


class _Cambiumpmp80211STAListUpdateStatus_Type(Integer32):
    """Custom type cambiumpmp80211STAListUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Cambiumpmp80211STAListUpdateStatus_Type.__name__ = "Integer32"
_Cambiumpmp80211STAListUpdateStatus_Object = MibScalar
cambiumpmp80211STAListUpdateStatus = _Cambiumpmp80211STAListUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 10),
    _Cambiumpmp80211STAListUpdateStatus_Type()
)
cambiumpmp80211STAListUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211STAListUpdateStatus.setStatus("current")


class _Cambiumpmp80211APListUpdate_Type(Integer32):
    """Custom type cambiumpmp80211APListUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211APListUpdate_Type.__name__ = "Integer32"
_Cambiumpmp80211APListUpdate_Object = MibScalar
cambiumpmp80211APListUpdate = _Cambiumpmp80211APListUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 11),
    _Cambiumpmp80211APListUpdate_Type()
)
cambiumpmp80211APListUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211APListUpdate.setStatus("current")


class _Cambiumpmp80211APListUpdateStatus_Type(Integer32):
    """Custom type cambiumpmp80211APListUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Cambiumpmp80211APListUpdateStatus_Type.__name__ = "Integer32"
_Cambiumpmp80211APListUpdateStatus_Object = MibScalar
cambiumpmp80211APListUpdateStatus = _Cambiumpmp80211APListUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 12),
    _Cambiumpmp80211APListUpdateStatus_Type()
)
cambiumpmp80211APListUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211APListUpdateStatus.setStatus("current")


class _Cambiumpmp80211SoftwareUpdateError_Type(Integer32):
    """Custom type cambiumpmp80211SoftwareUpdateError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Cambiumpmp80211SoftwareUpdateError_Type.__name__ = "Integer32"
_Cambiumpmp80211SoftwareUpdateError_Object = MibScalar
cambiumpmp80211SoftwareUpdateError = _Cambiumpmp80211SoftwareUpdateError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 13),
    _Cambiumpmp80211SoftwareUpdateError_Type()
)
cambiumpmp80211SoftwareUpdateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdateError.setStatus("current")


class _Cambiumpmp80211StatsPerSTAListUpdateStatus_Type(Integer32):
    """Custom type cambiumpmp80211StatsPerSTAListUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_Cambiumpmp80211StatsPerSTAListUpdateStatus_Type.__name__ = "Integer32"
_Cambiumpmp80211StatsPerSTAListUpdateStatus_Object = MibScalar
cambiumpmp80211StatsPerSTAListUpdateStatus = _Cambiumpmp80211StatsPerSTAListUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 14),
    _Cambiumpmp80211StatsPerSTAListUpdateStatus_Type()
)
cambiumpmp80211StatsPerSTAListUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211StatsPerSTAListUpdateStatus.setStatus("current")


class _Cambiumpmp80211StatsPerSTAListUpdate_Type(Integer32):
    """Custom type cambiumpmp80211StatsPerSTAListUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211StatsPerSTAListUpdate_Type.__name__ = "Integer32"
_Cambiumpmp80211StatsPerSTAListUpdate_Object = MibScalar
cambiumpmp80211StatsPerSTAListUpdate = _Cambiumpmp80211StatsPerSTAListUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 15),
    _Cambiumpmp80211StatsPerSTAListUpdate_Type()
)
cambiumpmp80211StatsPerSTAListUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211StatsPerSTAListUpdate.setStatus("current")


class _Cambiumpmp80211STADisconnect_Type(Integer32):
    """Custom type cambiumpmp80211STADisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Cambiumpmp80211STADisconnect_Type.__name__ = "Integer32"
_Cambiumpmp80211STADisconnect_Object = MibScalar
cambiumpmp80211STADisconnect = _Cambiumpmp80211STADisconnect_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 16),
    _Cambiumpmp80211STADisconnect_Type()
)
cambiumpmp80211STADisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211STADisconnect.setStatus("current")


class _Cambiumpmp80211GPSAutopopulate_Type(Integer32):
    """Custom type cambiumpmp80211GPSAutopopulate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Cambiumpmp80211GPSAutopopulate_Type.__name__ = "Integer32"
_Cambiumpmp80211GPSAutopopulate_Object = MibScalar
cambiumpmp80211GPSAutopopulate = _Cambiumpmp80211GPSAutopopulate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 17),
    _Cambiumpmp80211GPSAutopopulate_Type()
)
cambiumpmp80211GPSAutopopulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211GPSAutopopulate.setStatus("current")


class _Cambiumpmp80211SoftwareUpdateErrorStr_Type(DisplayString):
    """Custom type cambiumpmp80211SoftwareUpdateErrorStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Cambiumpmp80211SoftwareUpdateErrorStr_Type.__name__ = "DisplayString"
_Cambiumpmp80211SoftwareUpdateErrorStr_Object = MibScalar
cambiumpmp80211SoftwareUpdateErrorStr = _Cambiumpmp80211SoftwareUpdateErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 18),
    _Cambiumpmp80211SoftwareUpdateErrorStr_Type()
)
cambiumpmp80211SoftwareUpdateErrorStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdateErrorStr.setStatus("current")
_Cambiumpmp80211GpsFirmwareUpdate_Type = DisplayString
_Cambiumpmp80211GpsFirmwareUpdate_Object = MibScalar
cambiumpmp80211GpsFirmwareUpdate = _Cambiumpmp80211GpsFirmwareUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 19),
    _Cambiumpmp80211GpsFirmwareUpdate_Type()
)
cambiumpmp80211GpsFirmwareUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumpmp80211GpsFirmwareUpdate.setStatus("current")


class _Cambiumpmp80211GpsFirmwareUpdateError_Type(Integer32):
    """Custom type cambiumpmp80211GpsFirmwareUpdateError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cambiumpmp80211GpsFirmwareUpdateError_Type.__name__ = "Integer32"
_Cambiumpmp80211GpsFirmwareUpdateError_Object = MibScalar
cambiumpmp80211GpsFirmwareUpdateError = _Cambiumpmp80211GpsFirmwareUpdateError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 21),
    _Cambiumpmp80211GpsFirmwareUpdateError_Type()
)
cambiumpmp80211GpsFirmwareUpdateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211GpsFirmwareUpdateError.setStatus("current")


class _Cambiumpmp80211GpsFirmwareUpdateErrorStr_Type(DisplayString):
    """Custom type cambiumpmp80211GpsFirmwareUpdateErrorStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Cambiumpmp80211GpsFirmwareUpdateErrorStr_Type.__name__ = "DisplayString"
_Cambiumpmp80211GpsFirmwareUpdateErrorStr_Object = MibScalar
cambiumpmp80211GpsFirmwareUpdateErrorStr = _Cambiumpmp80211GpsFirmwareUpdateErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 22),
    _Cambiumpmp80211GpsFirmwareUpdateErrorStr_Type()
)
cambiumpmp80211GpsFirmwareUpdateErrorStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumpmp80211GpsFirmwareUpdateErrorStr.setStatus("current")


class _CambiumBridgeTableAPStatus_Type(Integer32):
    """Custom type cambiumBridgeTableAPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumBridgeTableAPStatus_Type.__name__ = "Integer32"
_CambiumBridgeTableAPStatus_Object = MibScalar
cambiumBridgeTableAPStatus = _CambiumBridgeTableAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 25),
    _CambiumBridgeTableAPStatus_Type()
)
cambiumBridgeTableAPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumBridgeTableAPStatus.setStatus("current")


class _CambiumBridgeTableSTAUpdate_Type(Integer32):
    """Custom type cambiumBridgeTableSTAUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumBridgeTableSTAUpdate_Type.__name__ = "Integer32"
_CambiumBridgeTableSTAUpdate_Object = MibScalar
cambiumBridgeTableSTAUpdate = _CambiumBridgeTableSTAUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 26),
    _CambiumBridgeTableSTAUpdate_Type()
)
cambiumBridgeTableSTAUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumBridgeTableSTAUpdate.setStatus("current")


class _CambiumBridgeTableSTAStatus_Type(Integer32):
    """Custom type cambiumBridgeTableSTAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_CambiumBridgeTableSTAStatus_Type.__name__ = "Integer32"
_CambiumBridgeTableSTAStatus_Object = MibScalar
cambiumBridgeTableSTAStatus = _CambiumBridgeTableSTAStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 27),
    _CambiumBridgeTableSTAStatus_Type()
)
cambiumBridgeTableSTAStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumBridgeTableSTAStatus.setStatus("current")


class _CambiumBridgeTableAPUpdate_Type(Integer32):
    """Custom type cambiumBridgeTableAPUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumBridgeTableAPUpdate_Type.__name__ = "Integer32"
_CambiumBridgeTableAPUpdate_Object = MibScalar
cambiumBridgeTableAPUpdate = _CambiumBridgeTableAPUpdate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 28),
    _CambiumBridgeTableAPUpdate_Type()
)
cambiumBridgeTableAPUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumBridgeTableAPUpdate.setStatus("current")


class _CambiumForceTabUpdDHCP_Type(Integer32):
    """Custom type cambiumForceTabUpdDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdDHCP_Type.__name__ = "Integer32"
_CambiumForceTabUpdDHCP_Object = MibScalar
cambiumForceTabUpdDHCP = _CambiumForceTabUpdDHCP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 30),
    _CambiumForceTabUpdDHCP_Type()
)
cambiumForceTabUpdDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdDHCP.setStatus("current")


class _CambiumForceTabUpdTrap_Type(Integer32):
    """Custom type cambiumForceTabUpdTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdTrap_Type.__name__ = "Integer32"
_CambiumForceTabUpdTrap_Object = MibScalar
cambiumForceTabUpdTrap = _CambiumForceTabUpdTrap_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 31),
    _CambiumForceTabUpdTrap_Type()
)
cambiumForceTabUpdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdTrap.setStatus("current")


class _CambiumForceTabUpdl2Frw_Type(Integer32):
    """Custom type cambiumForceTabUpdl2Frw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdl2Frw_Type.__name__ = "Integer32"
_CambiumForceTabUpdl2Frw_Object = MibScalar
cambiumForceTabUpdl2Frw = _CambiumForceTabUpdl2Frw_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 32),
    _CambiumForceTabUpdl2Frw_Type()
)
cambiumForceTabUpdl2Frw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdl2Frw.setStatus("current")


class _CambiumForceTabUpdl3Frw_Type(Integer32):
    """Custom type cambiumForceTabUpdl3Frw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdl3Frw_Type.__name__ = "Integer32"
_CambiumForceTabUpdl3Frw_Object = MibScalar
cambiumForceTabUpdl3Frw = _CambiumForceTabUpdl3Frw_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 33),
    _CambiumForceTabUpdl3Frw_Type()
)
cambiumForceTabUpdl3Frw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdl3Frw.setStatus("current")


class _CambiumForceTabUpdQos_Type(Integer32):
    """Custom type cambiumForceTabUpdQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdQos_Type.__name__ = "Integer32"
_CambiumForceTabUpdQos_Object = MibScalar
cambiumForceTabUpdQos = _CambiumForceTabUpdQos_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 34),
    _CambiumForceTabUpdQos_Type()
)
cambiumForceTabUpdQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdQos.setStatus("current")


class _CambiumForceTabUpdPortFw_Type(Integer32):
    """Custom type cambiumForceTabUpdPortFw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdPortFw_Type.__name__ = "Integer32"
_CambiumForceTabUpdPortFw_Object = MibScalar
cambiumForceTabUpdPortFw = _CambiumForceTabUpdPortFw_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 35),
    _CambiumForceTabUpdPortFw_Type()
)
cambiumForceTabUpdPortFw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdPortFw.setStatus("current")


class _CambiumForceTabUpdVlan_Type(Integer32):
    """Custom type cambiumForceTabUpdVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdVlan_Type.__name__ = "Integer32"
_CambiumForceTabUpdVlan_Object = MibScalar
cambiumForceTabUpdVlan = _CambiumForceTabUpdVlan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 36),
    _CambiumForceTabUpdVlan_Type()
)
cambiumForceTabUpdVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdVlan.setStatus("current")


class _CambiumForceTabUpdMappingVlan_Type(Integer32):
    """Custom type cambiumForceTabUpdMappingVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdMappingVlan_Type.__name__ = "Integer32"
_CambiumForceTabUpdMappingVlan_Object = MibScalar
cambiumForceTabUpdMappingVlan = _CambiumForceTabUpdMappingVlan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 37),
    _CambiumForceTabUpdMappingVlan_Type()
)
cambiumForceTabUpdMappingVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdMappingVlan.setStatus("current")


class _CambiumConfigurationApplyOnReboot_Type(Integer32):
    """Custom type cambiumConfigurationApplyOnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumConfigurationApplyOnReboot_Type.__name__ = "Integer32"
_CambiumConfigurationApplyOnReboot_Object = MibScalar
cambiumConfigurationApplyOnReboot = _CambiumConfigurationApplyOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 38),
    _CambiumConfigurationApplyOnReboot_Type()
)
cambiumConfigurationApplyOnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumConfigurationApplyOnReboot.setStatus("current")


class _CambiumForceSTARescan_Type(Integer32):
    """Custom type cambiumForceSTARescan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceSTARescan_Type.__name__ = "Integer32"
_CambiumForceSTARescan_Object = MibScalar
cambiumForceSTARescan = _CambiumForceSTARescan_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 39),
    _CambiumForceSTARescan_Type()
)
cambiumForceSTARescan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceSTARescan.setStatus("current")


class _CambiumForceTabUpdMcastDeny_Type(Integer32):
    """Custom type cambiumForceTabUpdMcastDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdMcastDeny_Type.__name__ = "Integer32"
_CambiumForceTabUpdMcastDeny_Object = MibScalar
cambiumForceTabUpdMcastDeny = _CambiumForceTabUpdMcastDeny_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 40),
    _CambiumForceTabUpdMcastDeny_Type()
)
cambiumForceTabUpdMcastDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdMcastDeny.setStatus("current")


class _CambiumForceTabUpdStaticRoutesCnf_Type(Integer32):
    """Custom type cambiumForceTabUpdStaticRoutesCnf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdStaticRoutesCnf_Type.__name__ = "Integer32"
_CambiumForceTabUpdStaticRoutesCnf_Object = MibScalar
cambiumForceTabUpdStaticRoutesCnf = _CambiumForceTabUpdStaticRoutesCnf_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 41),
    _CambiumForceTabUpdStaticRoutesCnf_Type()
)
cambiumForceTabUpdStaticRoutesCnf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdStaticRoutesCnf.setStatus("current")


class _CambiumForceTabUpdMIR_Type(Integer32):
    """Custom type cambiumForceTabUpdMIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdMIR_Type.__name__ = "Integer32"
_CambiumForceTabUpdMIR_Object = MibScalar
cambiumForceTabUpdMIR = _CambiumForceTabUpdMIR_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 42),
    _CambiumForceTabUpdMIR_Type()
)
cambiumForceTabUpdMIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdMIR.setStatus("current")


class _CambiumForceTabUpdRadiusServ_Type(Integer32):
    """Custom type cambiumForceTabUpdRadiusServ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdRadiusServ_Type.__name__ = "Integer32"
_CambiumForceTabUpdRadiusServ_Object = MibScalar
cambiumForceTabUpdRadiusServ = _CambiumForceTabUpdRadiusServ_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 43),
    _CambiumForceTabUpdRadiusServ_Type()
)
cambiumForceTabUpdRadiusServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdRadiusServ.setStatus("current")


class _CambiumForceTabUpdPrefAPList_Type(Integer32):
    """Custom type cambiumForceTabUpdPrefAPList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdPrefAPList_Type.__name__ = "Integer32"
_CambiumForceTabUpdPrefAPList_Object = MibScalar
cambiumForceTabUpdPrefAPList = _CambiumForceTabUpdPrefAPList_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 44),
    _CambiumForceTabUpdPrefAPList_Type()
)
cambiumForceTabUpdPrefAPList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdPrefAPList.setStatus("current")


class _CambiumForceTabUpdAPAlias_Type(Integer32):
    """Custom type cambiumForceTabUpdAPAlias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CambiumForceTabUpdAPAlias_Type.__name__ = "Integer32"
_CambiumForceTabUpdAPAlias_Object = MibScalar
cambiumForceTabUpdAPAlias = _CambiumForceTabUpdAPAlias_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 4, 45),
    _CambiumForceTabUpdAPAlias_Type()
)
cambiumForceTabUpdAPAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumForceTabUpdAPAlias.setStatus("current")
_Cambiumpmp80211Tools_ObjectIdentity = ObjectIdentity
cambiumpmp80211Tools = _Cambiumpmp80211Tools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6)
)
_CambiumLinkTest_ObjectIdentity = ObjectIdentity
cambiumLinkTest = _CambiumLinkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1)
)


class _CambiumLinkTestDuration_Type(Integer32):
    """Custom type cambiumLinkTestDuration based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(14, 14),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(18, 18),
        ValueRangeConstraint(20, 20),
    )


_CambiumLinkTestDuration_Type.__name__ = "Integer32"
_CambiumLinkTestDuration_Object = MibScalar
cambiumLinkTestDuration = _CambiumLinkTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 1),
    _CambiumLinkTestDuration_Type()
)
cambiumLinkTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestDuration.setStatus("current")


class _CambiumLinkTestPckSize_Type(Integer32):
    """Custom type cambiumLinkTestPckSize based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(800, 800),
        ValueRangeConstraint(1500, 1500),
    )


_CambiumLinkTestPckSize_Type.__name__ = "Integer32"
_CambiumLinkTestPckSize_Object = MibScalar
cambiumLinkTestPckSize = _CambiumLinkTestPckSize_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 2),
    _CambiumLinkTestPckSize_Type()
)
cambiumLinkTestPckSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestPckSize.setStatus("current")


class _CambiumLinkTestStartForMAC_Type(DisplayString):
    """Custom type cambiumLinkTestStartForMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumLinkTestStartForMAC_Type.__name__ = "DisplayString"
_CambiumLinkTestStartForMAC_Object = MibScalar
cambiumLinkTestStartForMAC = _CambiumLinkTestStartForMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 3),
    _CambiumLinkTestStartForMAC_Type()
)
cambiumLinkTestStartForMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumLinkTestStartForMAC.setStatus("current")


class _CambiumLinkTestStatus_Type(Integer32):
    """Custom type cambiumLinkTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_CambiumLinkTestStatus_Type.__name__ = "Integer32"
_CambiumLinkTestStatus_Object = MibScalar
cambiumLinkTestStatus = _CambiumLinkTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 4),
    _CambiumLinkTestStatus_Type()
)
cambiumLinkTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkTestStatus.setStatus("current")


class _CambiumLinkTestResultDate_Type(DisplayString):
    """Custom type cambiumLinkTestResultDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 24),
    )


_CambiumLinkTestResultDate_Type.__name__ = "DisplayString"
_CambiumLinkTestResultDate_Object = MibScalar
cambiumLinkTestResultDate = _CambiumLinkTestResultDate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 5),
    _CambiumLinkTestResultDate_Type()
)
cambiumLinkTestResultDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkTestResultDate.setStatus("current")


class _CambiumLinkTestResultUL_Type(Integer32):
    """Custom type cambiumLinkTestResultUL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CambiumLinkTestResultUL_Type.__name__ = "Integer32"
_CambiumLinkTestResultUL_Object = MibScalar
cambiumLinkTestResultUL = _CambiumLinkTestResultUL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 6),
    _CambiumLinkTestResultUL_Type()
)
cambiumLinkTestResultUL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkTestResultUL.setStatus("current")


class _CambiumLinkTestResultDL_Type(Integer32):
    """Custom type cambiumLinkTestResultDL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CambiumLinkTestResultDL_Type.__name__ = "Integer32"
_CambiumLinkTestResultDL_Object = MibScalar
cambiumLinkTestResultDL = _CambiumLinkTestResultDL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 1, 7),
    _CambiumLinkTestResultDL_Type()
)
cambiumLinkTestResultDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLinkTestResultDL.setStatus("current")
_Caminfo_ObjectIdentity = ObjectIdentity
caminfo = _Caminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2)
)


class _CaminfoScanFrequencyListCountry_Type(DisplayString):
    """Custom type caminfoScanFrequencyListCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CaminfoScanFrequencyListCountry_Type.__name__ = "DisplayString"
_CaminfoScanFrequencyListCountry_Object = MibScalar
caminfoScanFrequencyListCountry = _CaminfoScanFrequencyListCountry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2, 1),
    _CaminfoScanFrequencyListCountry_Type()
)
caminfoScanFrequencyListCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caminfoScanFrequencyListCountry.setStatus("current")


class _CaminfoScanFrequencyListTwentyBand_Type(DisplayString):
    """Custom type caminfoScanFrequencyListTwentyBand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1064),
    )


_CaminfoScanFrequencyListTwentyBand_Type.__name__ = "DisplayString"
_CaminfoScanFrequencyListTwentyBand_Object = MibScalar
caminfoScanFrequencyListTwentyBand = _CaminfoScanFrequencyListTwentyBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2, 2),
    _CaminfoScanFrequencyListTwentyBand_Type()
)
caminfoScanFrequencyListTwentyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caminfoScanFrequencyListTwentyBand.setStatus("current")


class _CaminfoScanFrequencyListFortyBand_Type(DisplayString):
    """Custom type caminfoScanFrequencyListFortyBand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1064),
    )


_CaminfoScanFrequencyListFortyBand_Type.__name__ = "DisplayString"
_CaminfoScanFrequencyListFortyBand_Object = MibScalar
caminfoScanFrequencyListFortyBand = _CaminfoScanFrequencyListFortyBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2, 3),
    _CaminfoScanFrequencyListFortyBand_Type()
)
caminfoScanFrequencyListFortyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caminfoScanFrequencyListFortyBand.setStatus("current")


class _CaminfoScanFrequencyListAllow59band_Type(Integer32):
    """Custom type caminfoScanFrequencyListAllow59band based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CaminfoScanFrequencyListAllow59band_Type.__name__ = "Integer32"
_CaminfoScanFrequencyListAllow59band_Object = MibScalar
caminfoScanFrequencyListAllow59band = _CaminfoScanFrequencyListAllow59band_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 2, 4),
    _CaminfoScanFrequencyListAllow59band_Type()
)
caminfoScanFrequencyListAllow59band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caminfoScanFrequencyListAllow59band.setStatus("current")
_CambiumToolBar_ObjectIdentity = ObjectIdentity
cambiumToolBar = _CambiumToolBar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3)
)
_CambiumToolBarOpts_ObjectIdentity = ObjectIdentity
cambiumToolBarOpts = _CambiumToolBarOpts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 1)
)
_CambiumInternetConnectionServerIP_Type = IpAddress
_CambiumInternetConnectionServerIP_Object = MibScalar
cambiumInternetConnectionServerIP = _CambiumInternetConnectionServerIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 1, 1),
    _CambiumInternetConnectionServerIP_Type()
)
cambiumInternetConnectionServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumInternetConnectionServerIP.setStatus("current")


class _CambiumInternetConnectionPollPeriod_Type(Integer32):
    """Custom type cambiumInternetConnectionPollPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CambiumInternetConnectionPollPeriod_Type.__name__ = "Integer32"
_CambiumInternetConnectionPollPeriod_Object = MibScalar
cambiumInternetConnectionPollPeriod = _CambiumInternetConnectionPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 1, 2),
    _CambiumInternetConnectionPollPeriod_Type()
)
cambiumInternetConnectionPollPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumInternetConnectionPollPeriod.setStatus("current")
_CambiumToolBarStates_ObjectIdentity = ObjectIdentity
cambiumToolBarStates = _CambiumToolBarStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2)
)


class _CambiumToolbarGlobeState_Type(Integer32):
    """Custom type cambiumToolbarGlobeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumToolbarGlobeState_Type.__name__ = "Integer32"
_CambiumToolbarGlobeState_Object = MibScalar
cambiumToolbarGlobeState = _CambiumToolbarGlobeState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 1),
    _CambiumToolbarGlobeState_Type()
)
cambiumToolbarGlobeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarGlobeState.setStatus("current")


class _CambiumToolbarGPSSyncState_Type(Integer32):
    """Custom type cambiumToolbarGPSSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CambiumToolbarGPSSyncState_Type.__name__ = "Integer32"
_CambiumToolbarGPSSyncState_Object = MibScalar
cambiumToolbarGPSSyncState = _CambiumToolbarGPSSyncState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 2),
    _CambiumToolbarGPSSyncState_Type()
)
cambiumToolbarGPSSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarGPSSyncState.setStatus("current")


class _CambiumToolbarDeviceConfigurationState_Type(Integer32):
    """Custom type cambiumToolbarDeviceConfigurationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CambiumToolbarDeviceConfigurationState_Type.__name__ = "Integer32"
_CambiumToolbarDeviceConfigurationState_Object = MibScalar
cambiumToolbarDeviceConfigurationState = _CambiumToolbarDeviceConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 3),
    _CambiumToolbarDeviceConfigurationState_Type()
)
cambiumToolbarDeviceConfigurationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarDeviceConfigurationState.setStatus("current")


class _CambiumToolbarSyncSource_Type(Integer32):
    """Custom type cambiumToolbarSyncSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
    )


_CambiumToolbarSyncSource_Type.__name__ = "Integer32"
_CambiumToolbarSyncSource_Object = MibScalar
cambiumToolbarSyncSource = _CambiumToolbarSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 4),
    _CambiumToolbarSyncSource_Type()
)
cambiumToolbarSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarSyncSource.setStatus("current")


class _CambiumToolbarGPSSyncStateStr_Type(DisplayString):
    """Custom type cambiumToolbarGPSSyncStateStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumToolbarGPSSyncStateStr_Type.__name__ = "DisplayString"
_CambiumToolbarGPSSyncStateStr_Object = MibScalar
cambiumToolbarGPSSyncStateStr = _CambiumToolbarGPSSyncStateStr_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 3, 2, 5),
    _CambiumToolbarGPSSyncStateStr_Type()
)
cambiumToolbarGPSSyncStateStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumToolbarGPSSyncStateStr.setStatus("current")
_CambiumCfg_ObjectIdentity = ObjectIdentity
cambiumCfg = _CambiumCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4)
)


class _CambiumJSONCfgImport_Type(DisplayString):
    """Custom type cambiumJSONCfgImport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumJSONCfgImport_Type.__name__ = "DisplayString"
_CambiumJSONCfgImport_Object = MibScalar
cambiumJSONCfgImport = _CambiumJSONCfgImport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 1),
    _CambiumJSONCfgImport_Type()
)
cambiumJSONCfgImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumJSONCfgImport.setStatus("current")


class _CambiumJSONCfgImportStatus_Type(Integer32):
    """Custom type cambiumJSONCfgImportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3),
    )


_CambiumJSONCfgImportStatus_Type.__name__ = "Integer32"
_CambiumJSONCfgImportStatus_Object = MibScalar
cambiumJSONCfgImportStatus = _CambiumJSONCfgImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 2),
    _CambiumJSONCfgImportStatus_Type()
)
cambiumJSONCfgImportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgImportStatus.setStatus("current")


class _CambiumJSONCfgImportError_Type(DisplayString):
    """Custom type cambiumJSONCfgImportError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumJSONCfgImportError_Type.__name__ = "DisplayString"
_CambiumJSONCfgImportError_Object = MibScalar
cambiumJSONCfgImportError = _CambiumJSONCfgImportError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 3),
    _CambiumJSONCfgImportError_Type()
)
cambiumJSONCfgImportError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgImportError.setStatus("current")


class _CambiumJSONCfgExport_Type(Integer32):
    """Custom type cambiumJSONCfgExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumJSONCfgExport_Type.__name__ = "Integer32"
_CambiumJSONCfgExport_Object = MibScalar
cambiumJSONCfgExport = _CambiumJSONCfgExport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 10),
    _CambiumJSONCfgExport_Type()
)
cambiumJSONCfgExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumJSONCfgExport.setStatus("current")


class _CambiumJSONCfgExportStatus_Type(Integer32):
    """Custom type cambiumJSONCfgExportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4),
    )


_CambiumJSONCfgExportStatus_Type.__name__ = "Integer32"
_CambiumJSONCfgExportStatus_Object = MibScalar
cambiumJSONCfgExportStatus = _CambiumJSONCfgExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 11),
    _CambiumJSONCfgExportStatus_Type()
)
cambiumJSONCfgExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgExportStatus.setStatus("current")


class _CambiumJSONCfgExportError_Type(DisplayString):
    """Custom type cambiumJSONCfgExportError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumJSONCfgExportError_Type.__name__ = "DisplayString"
_CambiumJSONCfgExportError_Object = MibScalar
cambiumJSONCfgExportError = _CambiumJSONCfgExportError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 12),
    _CambiumJSONCfgExportError_Type()
)
cambiumJSONCfgExportError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgExportError.setStatus("current")


class _CambiumJSONCfgExportLink_Type(DisplayString):
    """Custom type cambiumJSONCfgExportLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumJSONCfgExportLink_Type.__name__ = "DisplayString"
_CambiumJSONCfgExportLink_Object = MibScalar
cambiumJSONCfgExportLink = _CambiumJSONCfgExportLink_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 13),
    _CambiumJSONCfgExportLink_Type()
)
cambiumJSONCfgExportLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumJSONCfgExportLink.setStatus("current")


class _CambiumFullCfgRestore_Type(DisplayString):
    """Custom type cambiumFullCfgRestore based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CambiumFullCfgRestore_Type.__name__ = "DisplayString"
_CambiumFullCfgRestore_Object = MibScalar
cambiumFullCfgRestore = _CambiumFullCfgRestore_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 20),
    _CambiumFullCfgRestore_Type()
)
cambiumFullCfgRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumFullCfgRestore.setStatus("current")


class _CambiumFullCfgRestoreStatus_Type(Integer32):
    """Custom type cambiumFullCfgRestoreStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_CambiumFullCfgRestoreStatus_Type.__name__ = "Integer32"
_CambiumFullCfgRestoreStatus_Object = MibScalar
cambiumFullCfgRestoreStatus = _CambiumFullCfgRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 21),
    _CambiumFullCfgRestoreStatus_Type()
)
cambiumFullCfgRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgRestoreStatus.setStatus("current")


class _CambiumFullCfgRestoreError_Type(DisplayString):
    """Custom type cambiumFullCfgRestoreError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumFullCfgRestoreError_Type.__name__ = "DisplayString"
_CambiumFullCfgRestoreError_Object = MibScalar
cambiumFullCfgRestoreError = _CambiumFullCfgRestoreError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 22),
    _CambiumFullCfgRestoreError_Type()
)
cambiumFullCfgRestoreError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgRestoreError.setStatus("current")


class _CambiumFullCfgBackUp_Type(Integer32):
    """Custom type cambiumFullCfgBackUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CambiumFullCfgBackUp_Type.__name__ = "Integer32"
_CambiumFullCfgBackUp_Object = MibScalar
cambiumFullCfgBackUp = _CambiumFullCfgBackUp_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 30),
    _CambiumFullCfgBackUp_Type()
)
cambiumFullCfgBackUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumFullCfgBackUp.setStatus("current")


class _CambiumFullCfgBackUpStatus_Type(Integer32):
    """Custom type cambiumFullCfgBackUpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_CambiumFullCfgBackUpStatus_Type.__name__ = "Integer32"
_CambiumFullCfgBackUpStatus_Object = MibScalar
cambiumFullCfgBackUpStatus = _CambiumFullCfgBackUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 31),
    _CambiumFullCfgBackUpStatus_Type()
)
cambiumFullCfgBackUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgBackUpStatus.setStatus("current")


class _CambiumFullCfgBackUpError_Type(DisplayString):
    """Custom type cambiumFullCfgBackUpError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CambiumFullCfgBackUpError_Type.__name__ = "DisplayString"
_CambiumFullCfgBackUpError_Object = MibScalar
cambiumFullCfgBackUpError = _CambiumFullCfgBackUpError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 32),
    _CambiumFullCfgBackUpError_Type()
)
cambiumFullCfgBackUpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgBackUpError.setStatus("current")
_CambiumFullCfgBackUpLink_Type = DisplayString
_CambiumFullCfgBackUpLink_Object = MibScalar
cambiumFullCfgBackUpLink = _CambiumFullCfgBackUpLink_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 4, 33),
    _CambiumFullCfgBackUpLink_Type()
)
cambiumFullCfgBackUpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumFullCfgBackUpLink.setStatus("current")
_CambiumIDM_ObjectIdentity = ObjectIdentity
cambiumIDM = _CambiumIDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5)
)


class _CambiumIDMMode_Type(Integer32):
    """Custom type cambiumIDMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CambiumIDMMode_Type.__name__ = "Integer32"
_CambiumIDMMode_Object = MibScalar
cambiumIDMMode = _CambiumIDMMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 1),
    _CambiumIDMMode_Type()
)
cambiumIDMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIDMMode.setStatus("current")


class _CambiumIDMTime_Type(Integer32):
    """Custom type cambiumIDMTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 120000),
    )


_CambiumIDMTime_Type.__name__ = "Integer32"
_CambiumIDMTime_Object = MibScalar
cambiumIDMTime = _CambiumIDMTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 2),
    _CambiumIDMTime_Type()
)
cambiumIDMTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIDMTime.setStatus("current")


class _CambiumIDMEnable_Type(Integer32):
    """Custom type cambiumIDMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_CambiumIDMEnable_Type.__name__ = "Integer32"
_CambiumIDMEnable_Object = MibScalar
cambiumIDMEnable = _CambiumIDMEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 3),
    _CambiumIDMEnable_Type()
)
cambiumIDMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIDMEnable.setStatus("current")
_CambiumIDMResultsTable_Object = MibTable
cambiumIDMResultsTable = _CambiumIDMResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10)
)
if mibBuilder.loadTexts:
    cambiumIDMResultsTable.setStatus("current")
_CambiumIDMResultsEntry_Object = MibTableRow
cambiumIDMResultsEntry = _CambiumIDMResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1)
)
cambiumIDMResultsEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumAPNumberOfConnectedSTA"),
)
if mibBuilder.loadTexts:
    cambiumIDMResultsEntry.setStatus("current")


class _IdmDeviceListCycle_Type(Integer32):
    """Custom type idmDeviceListCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IdmDeviceListCycle_Type.__name__ = "Integer32"
_IdmDeviceListCycle_Object = MibTableColumn
idmDeviceListCycle = _IdmDeviceListCycle_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 1),
    _IdmDeviceListCycle_Type()
)
idmDeviceListCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCycle.setStatus("current")


class _IdmDeviceListMAC_Type(DisplayString):
    """Custom type idmDeviceListMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_IdmDeviceListMAC_Type.__name__ = "DisplayString"
_IdmDeviceListMAC_Object = MibTableColumn
idmDeviceListMAC = _IdmDeviceListMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 2),
    _IdmDeviceListMAC_Type()
)
idmDeviceListMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListMAC.setStatus("current")


class _IdmDeviceListLCombRSSI_Type(Integer32):
    """Custom type idmDeviceListLCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListLCombRSSI_Type.__name__ = "Integer32"
_IdmDeviceListLCombRSSI_Object = MibTableColumn
idmDeviceListLCombRSSI = _IdmDeviceListLCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 3),
    _IdmDeviceListLCombRSSI_Type()
)
idmDeviceListLCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListLCombRSSI.setStatus("current")


class _IdmDeviceListLRate_Type(DisplayString):
    """Custom type idmDeviceListLRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_IdmDeviceListLRate_Type.__name__ = "DisplayString"
_IdmDeviceListLRate_Object = MibTableColumn
idmDeviceListLRate = _IdmDeviceListLRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 4),
    _IdmDeviceListLRate_Type()
)
idmDeviceListLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListLRate.setStatus("current")


class _IdmDeviceListMaxRate_Type(DisplayString):
    """Custom type idmDeviceListMaxRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_IdmDeviceListMaxRate_Type.__name__ = "DisplayString"
_IdmDeviceListMaxRate_Object = MibTableColumn
idmDeviceListMaxRate = _IdmDeviceListMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 5),
    _IdmDeviceListMaxRate_Type()
)
idmDeviceListMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListMaxRate.setStatus("current")
_IdmDeviceListPcktsNum_Type = Integer32
_IdmDeviceListPcktsNum_Object = MibTableColumn
idmDeviceListPcktsNum = _IdmDeviceListPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 6),
    _IdmDeviceListPcktsNum_Type()
)
idmDeviceListPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPcktsNum.setStatus("current")


class _IdmDeviceListCRCCombRSSI_Type(Integer32):
    """Custom type idmDeviceListCRCCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListCRCCombRSSI_Type.__name__ = "Integer32"
_IdmDeviceListCRCCombRSSI_Object = MibTableColumn
idmDeviceListCRCCombRSSI = _IdmDeviceListCRCCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 7),
    _IdmDeviceListCRCCombRSSI_Type()
)
idmDeviceListCRCCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCRCCombRSSI.setStatus("current")


class _IdmDeviceListCRCCh0RSSI_Type(Integer32):
    """Custom type idmDeviceListCRCCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListCRCCh0RSSI_Type.__name__ = "Integer32"
_IdmDeviceListCRCCh0RSSI_Object = MibTableColumn
idmDeviceListCRCCh0RSSI = _IdmDeviceListCRCCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 8),
    _IdmDeviceListCRCCh0RSSI_Type()
)
idmDeviceListCRCCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCRCCh0RSSI.setStatus("current")


class _IdmDeviceListCRCCh1RSSI_Type(Integer32):
    """Custom type idmDeviceListCRCCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListCRCCh1RSSI_Type.__name__ = "Integer32"
_IdmDeviceListCRCCh1RSSI_Object = MibTableColumn
idmDeviceListCRCCh1RSSI = _IdmDeviceListCRCCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 9),
    _IdmDeviceListCRCCh1RSSI_Type()
)
idmDeviceListCRCCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCRCCh1RSSI.setStatus("current")
_IdmDeviceListCRCPcktsNum_Type = Integer32
_IdmDeviceListCRCPcktsNum_Object = MibTableColumn
idmDeviceListCRCPcktsNum = _IdmDeviceListCRCPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 10),
    _IdmDeviceListCRCPcktsNum_Type()
)
idmDeviceListCRCPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListCRCPcktsNum.setStatus("current")


class _IdmDeviceListPRQCombRSSI_Type(Integer32):
    """Custom type idmDeviceListPRQCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListPRQCombRSSI_Type.__name__ = "Integer32"
_IdmDeviceListPRQCombRSSI_Object = MibTableColumn
idmDeviceListPRQCombRSSI = _IdmDeviceListPRQCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 11),
    _IdmDeviceListPRQCombRSSI_Type()
)
idmDeviceListPRQCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPRQCombRSSI.setStatus("current")


class _IdmDeviceListPRQCh0RSSI_Type(Integer32):
    """Custom type idmDeviceListPRQCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListPRQCh0RSSI_Type.__name__ = "Integer32"
_IdmDeviceListPRQCh0RSSI_Object = MibTableColumn
idmDeviceListPRQCh0RSSI = _IdmDeviceListPRQCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 12),
    _IdmDeviceListPRQCh0RSSI_Type()
)
idmDeviceListPRQCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPRQCh0RSSI.setStatus("current")


class _IdmDeviceListPRQCh1RSSI_Type(Integer32):
    """Custom type idmDeviceListPRQCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmDeviceListPRQCh1RSSI_Type.__name__ = "Integer32"
_IdmDeviceListPRQCh1RSSI_Object = MibTableColumn
idmDeviceListPRQCh1RSSI = _IdmDeviceListPRQCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 13),
    _IdmDeviceListPRQCh1RSSI_Type()
)
idmDeviceListPRQCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPRQCh1RSSI.setStatus("current")
_IdmDeviceListPRQPcktsNum_Type = Integer32
_IdmDeviceListPRQPcktsNum_Object = MibTableColumn
idmDeviceListPRQPcktsNum = _IdmDeviceListPRQPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 10, 1, 14),
    _IdmDeviceListPRQPcktsNum_Type()
)
idmDeviceListPRQPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmDeviceListPRQPcktsNum.setStatus("current")


class _CambiumIDMSumMAC_Type(DisplayString):
    """Custom type cambiumIDMSumMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_CambiumIDMSumMAC_Type.__name__ = "DisplayString"
_CambiumIDMSumMAC_Object = MibScalar
cambiumIDMSumMAC = _CambiumIDMSumMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 11),
    _CambiumIDMSumMAC_Type()
)
cambiumIDMSumMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumIDMSumMAC.setStatus("current")


class _CambiumIDMSumLCombRSSI_Type(Integer32):
    """Custom type cambiumIDMSumLCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumLCombRSSI_Type.__name__ = "Integer32"
_CambiumIDMSumLCombRSSI_Object = MibScalar
cambiumIDMSumLCombRSSI = _CambiumIDMSumLCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 12),
    _CambiumIDMSumLCombRSSI_Type()
)
cambiumIDMSumLCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumLCombRSSI.setStatus("current")


class _CambiumIDMSumLRate_Type(DisplayString):
    """Custom type cambiumIDMSumLRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CambiumIDMSumLRate_Type.__name__ = "DisplayString"
_CambiumIDMSumLRate_Object = MibScalar
cambiumIDMSumLRate = _CambiumIDMSumLRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 13),
    _CambiumIDMSumLRate_Type()
)
cambiumIDMSumLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumLRate.setStatus("current")


class _CambiumIDMSumMaxRate_Type(DisplayString):
    """Custom type cambiumIDMSumMaxRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_CambiumIDMSumMaxRate_Type.__name__ = "DisplayString"
_CambiumIDMSumMaxRate_Object = MibScalar
cambiumIDMSumMaxRate = _CambiumIDMSumMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 14),
    _CambiumIDMSumMaxRate_Type()
)
cambiumIDMSumMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumMaxRate.setStatus("current")
_CambiumIDMSumPcktsNum_Type = Integer32
_CambiumIDMSumPcktsNum_Object = MibScalar
cambiumIDMSumPcktsNum = _CambiumIDMSumPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 15),
    _CambiumIDMSumPcktsNum_Type()
)
cambiumIDMSumPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPcktsNum.setStatus("current")


class _CambiumIDMSumCRCCombRSSI_Type(Integer32):
    """Custom type cambiumIDMSumCRCCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumCRCCombRSSI_Type.__name__ = "Integer32"
_CambiumIDMSumCRCCombRSSI_Object = MibScalar
cambiumIDMSumCRCCombRSSI = _CambiumIDMSumCRCCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 16),
    _CambiumIDMSumCRCCombRSSI_Type()
)
cambiumIDMSumCRCCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumCRCCombRSSI.setStatus("current")


class _CambiumIDMSumCRCCh0RSSI_Type(Integer32):
    """Custom type cambiumIDMSumCRCCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumCRCCh0RSSI_Type.__name__ = "Integer32"
_CambiumIDMSumCRCCh0RSSI_Object = MibScalar
cambiumIDMSumCRCCh0RSSI = _CambiumIDMSumCRCCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 17),
    _CambiumIDMSumCRCCh0RSSI_Type()
)
cambiumIDMSumCRCCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumCRCCh0RSSI.setStatus("current")


class _CambiumIDMSumCRCCh1RSSI_Type(Integer32):
    """Custom type cambiumIDMSumCRCCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumCRCCh1RSSI_Type.__name__ = "Integer32"
_CambiumIDMSumCRCCh1RSSI_Object = MibScalar
cambiumIDMSumCRCCh1RSSI = _CambiumIDMSumCRCCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 18),
    _CambiumIDMSumCRCCh1RSSI_Type()
)
cambiumIDMSumCRCCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumCRCCh1RSSI.setStatus("current")
_CambiumIDMSumCRCPcktsNum_Type = Integer32
_CambiumIDMSumCRCPcktsNum_Object = MibScalar
cambiumIDMSumCRCPcktsNum = _CambiumIDMSumCRCPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 19),
    _CambiumIDMSumCRCPcktsNum_Type()
)
cambiumIDMSumCRCPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumCRCPcktsNum.setStatus("current")


class _CambiumIDMSumPRQCombRSSI_Type(Integer32):
    """Custom type cambiumIDMSumPRQCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumPRQCombRSSI_Type.__name__ = "Integer32"
_CambiumIDMSumPRQCombRSSI_Object = MibScalar
cambiumIDMSumPRQCombRSSI = _CambiumIDMSumPRQCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 20),
    _CambiumIDMSumPRQCombRSSI_Type()
)
cambiumIDMSumPRQCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPRQCombRSSI.setStatus("current")


class _CambiumIDMSumPRQCh0RSSI_Type(Integer32):
    """Custom type cambiumIDMSumPRQCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumPRQCh0RSSI_Type.__name__ = "Integer32"
_CambiumIDMSumPRQCh0RSSI_Object = MibScalar
cambiumIDMSumPRQCh0RSSI = _CambiumIDMSumPRQCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 21),
    _CambiumIDMSumPRQCh0RSSI_Type()
)
cambiumIDMSumPRQCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPRQCh0RSSI.setStatus("current")


class _CambiumIDMSumPRQCh1RSSI_Type(Integer32):
    """Custom type cambiumIDMSumPRQCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CambiumIDMSumPRQCh1RSSI_Type.__name__ = "Integer32"
_CambiumIDMSumPRQCh1RSSI_Object = MibScalar
cambiumIDMSumPRQCh1RSSI = _CambiumIDMSumPRQCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 22),
    _CambiumIDMSumPRQCh1RSSI_Type()
)
cambiumIDMSumPRQCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPRQCh1RSSI.setStatus("current")
_CambiumIDMSumPRQPcktsNum_Type = Integer32
_CambiumIDMSumPRQPcktsNum_Object = MibScalar
cambiumIDMSumPRQPcktsNum = _CambiumIDMSumPRQPcktsNum_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 23),
    _CambiumIDMSumPRQPcktsNum_Type()
)
cambiumIDMSumPRQPcktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumIDMSumPRQPcktsNum.setStatus("current")
_CambiumIDMSummaryTable_Object = MibTable
cambiumIDMSummaryTable = _CambiumIDMSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30)
)
if mibBuilder.loadTexts:
    cambiumIDMSummaryTable.setStatus("current")
_CambiumIDMSummaryEntry_Object = MibTableRow
cambiumIDMSummaryEntry = _CambiumIDMSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1)
)
cambiumIDMSummaryEntry.setIndexNames(
    (0, "CAMBIUM-PMP80211-MIB", "cambiumAPNumberOfConnectedSTA"),
)
if mibBuilder.loadTexts:
    cambiumIDMSummaryEntry.setStatus("current")


class _IdmSummaryIntMAC_Type(DisplayString):
    """Custom type idmSummaryIntMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_IdmSummaryIntMAC_Type.__name__ = "DisplayString"
_IdmSummaryIntMAC_Object = MibTableColumn
idmSummaryIntMAC = _IdmSummaryIntMAC_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 1),
    _IdmSummaryIntMAC_Type()
)
idmSummaryIntMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntMAC.setStatus("current")


class _IdmSummaryIntCombRSSI_Type(Integer32):
    """Custom type idmSummaryIntCombRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmSummaryIntCombRSSI_Type.__name__ = "Integer32"
_IdmSummaryIntCombRSSI_Object = MibTableColumn
idmSummaryIntCombRSSI = _IdmSummaryIntCombRSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 2),
    _IdmSummaryIntCombRSSI_Type()
)
idmSummaryIntCombRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntCombRSSI.setStatus("current")


class _IdmSummaryIntCh0RSSI_Type(Integer32):
    """Custom type idmSummaryIntCh0RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmSummaryIntCh0RSSI_Type.__name__ = "Integer32"
_IdmSummaryIntCh0RSSI_Object = MibTableColumn
idmSummaryIntCh0RSSI = _IdmSummaryIntCh0RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 3),
    _IdmSummaryIntCh0RSSI_Type()
)
idmSummaryIntCh0RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntCh0RSSI.setStatus("current")


class _IdmSummaryIntCh1RSSI_Type(Integer32):
    """Custom type idmSummaryIntCh1RSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_IdmSummaryIntCh1RSSI_Type.__name__ = "Integer32"
_IdmSummaryIntCh1RSSI_Object = MibTableColumn
idmSummaryIntCh1RSSI = _IdmSummaryIntCh1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 4),
    _IdmSummaryIntCh1RSSI_Type()
)
idmSummaryIntCh1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntCh1RSSI.setStatus("current")


class _IdmSummaryIntSSID_Type(DisplayString):
    """Custom type idmSummaryIntSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IdmSummaryIntSSID_Type.__name__ = "DisplayString"
_IdmSummaryIntSSID_Object = MibTableColumn
idmSummaryIntSSID = _IdmSummaryIntSSID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 5, 30, 1, 5),
    _IdmSummaryIntSSID_Type()
)
idmSummaryIntSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idmSummaryIntSSID.setStatus("current")
_CambiumACSCfg_ObjectIdentity = ObjectIdentity
cambiumACSCfg = _CambiumACSCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6)
)


class _AcsEnable_Type(Integer32):
    """Custom type acsEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_AcsEnable_Type.__name__ = "Integer32"
_AcsEnable_Object = MibScalar
acsEnable = _AcsEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6, 1),
    _AcsEnable_Type()
)
acsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsEnable.setStatus("current")


class _AcsScanMinDwellTime_Type(Integer32):
    """Custom type acsScanMinDwellTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_AcsScanMinDwellTime_Type.__name__ = "Integer32"
_AcsScanMinDwellTime_Object = MibScalar
acsScanMinDwellTime = _AcsScanMinDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6, 2),
    _AcsScanMinDwellTime_Type()
)
acsScanMinDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScanMinDwellTime.setStatus("current")


class _AcsScanMaxDwellTime_Type(Integer32):
    """Custom type acsScanMaxDwellTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 600),
    )


_AcsScanMaxDwellTime_Type.__name__ = "Integer32"
_AcsScanMaxDwellTime_Object = MibScalar
acsScanMaxDwellTime = _AcsScanMaxDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6, 3),
    _AcsScanMaxDwellTime_Type()
)
acsScanMaxDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsScanMaxDwellTime.setStatus("current")


class _AcsControl_Type(Integer32):
    """Custom type acsControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcsControl_Type.__name__ = "Integer32"
_AcsControl_Object = MibScalar
acsControl = _AcsControl_Object(
    (1, 3, 6, 1, 4, 1, 17713, 21, 6, 6, 4),
    _AcsControl_Type()
)
acsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsControl.setStatus("current")

# Managed Objects groups


# Notification objects

cambiumpmp80211SoftwareUpdateStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 1)
)
cambiumpmp80211SoftwareUpdateStatusTrap.setObjects(
      *(("CAMBIUM-PMP80211-MIB", "cambiumpmp80211SoftwareUpdateError"),
        ("CAMBIUM-PMP80211-MIB", "cambiumpmp80211SoftwareUpdateErrorStr"))
)
if mibBuilder.loadTexts:
    cambiumpmp80211SoftwareUpdateStatusTrap.setStatus(
        "current"
    )

cambiumpmp80211GPSSyncStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 2)
)
cambiumpmp80211GPSSyncStatusTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumToolbarGPSSyncState")
)
if mibBuilder.loadTexts:
    cambiumpmp80211GPSSyncStatusTrap.setStatus(
        "current"
    )

cambiumpmp80211SystemUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 3)
)
if mibBuilder.loadTexts:
    cambiumpmp80211SystemUpTrap.setStatus(
        "current"
    )

cambiumpmp80211DFSStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 4)
)
cambiumpmp80211DFSStatusTrap.setObjects(
      *(("CAMBIUM-PMP80211-MIB", "cambiumDFSStatus"),
        ("CAMBIUM-PMP80211-MIB", "cambiumDFSStatusStr"))
)
if mibBuilder.loadTexts:
    cambiumpmp80211DFSStatusTrap.setStatus(
        "current"
    )

cambiumpmp80211JSONCfgImportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 5)
)
cambiumpmp80211JSONCfgImportTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumJSONCfgImportError")
)
if mibBuilder.loadTexts:
    cambiumpmp80211JSONCfgImportTrap.setStatus(
        "current"
    )

cambiumpmp80211JSONCfgExportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 6)
)
cambiumpmp80211JSONCfgExportTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumJSONCfgExportError")
)
if mibBuilder.loadTexts:
    cambiumpmp80211JSONCfgExportTrap.setStatus(
        "current"
    )

cambiumpmp80211FullCfgRestoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 7)
)
cambiumpmp80211FullCfgRestoreTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumFullCfgRestoreError")
)
if mibBuilder.loadTexts:
    cambiumpmp80211FullCfgRestoreTrap.setStatus(
        "current"
    )

cambiumpmp80211FullCfgBackupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 8)
)
cambiumpmp80211FullCfgBackupTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumFullCfgBackUpError")
)
if mibBuilder.loadTexts:
    cambiumpmp80211FullCfgBackupTrap.setStatus(
        "current"
    )

cambiumpmp80211GpsFirmwareUpdateStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 9)
)
cambiumpmp80211GpsFirmwareUpdateStatusTrap.setObjects(
      *(("CAMBIUM-PMP80211-MIB", "cambiumpmp80211GpsFirmwareUpdateError"),
        ("CAMBIUM-PMP80211-MIB", "cambiumpmp80211GpsFirmwareUpdateErrorStr"))
)
if mibBuilder.loadTexts:
    cambiumpmp80211GpsFirmwareUpdateStatusTrap.setStatus(
        "current"
    )

cambiumpmp80211STADropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 10)
)
cambiumpmp80211STADropTrap.setObjects(
      *(("CAMBIUM-PMP80211-MIB", "cambiumSTAMAC"),
        ("CAMBIUM-PMP80211-MIB", "cambiumSTADropReason"))
)
if mibBuilder.loadTexts:
    cambiumpmp80211STADropTrap.setStatus(
        "current"
    )

cambiumpmp80211SMRegTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 11)
)
cambiumpmp80211SMRegTrap.setObjects(
    ("CAMBIUM-PMP80211-MIB", "cambiumSTAMAC")
)
if mibBuilder.loadTexts:
    cambiumpmp80211SMRegTrap.setStatus(
        "current"
    )

cambiumpmp80211SystemRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 12)
)
if mibBuilder.loadTexts:
    cambiumpmp80211SystemRebootTrap.setStatus(
        "current"
    )

cambiumpmp80211SAModeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 13)
)
if mibBuilder.loadTexts:
    cambiumpmp80211SAModeTrap.setStatus(
        "current"
    )

cambiumpmpETSIframeSkipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 21, 0, 14)
)
if mibBuilder.loadTexts:
    cambiumpmpETSIframeSkipTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-PMP80211-MIB",
    **{"cambium": cambium,
       "pmpMibTree": pmpMibTree,
       "cambiumpmp80211SystemTraps": cambiumpmp80211SystemTraps,
       "cambiumpmp80211SoftwareUpdateStatusTrap": cambiumpmp80211SoftwareUpdateStatusTrap,
       "cambiumpmp80211GPSSyncStatusTrap": cambiumpmp80211GPSSyncStatusTrap,
       "cambiumpmp80211SystemUpTrap": cambiumpmp80211SystemUpTrap,
       "cambiumpmp80211DFSStatusTrap": cambiumpmp80211DFSStatusTrap,
       "cambiumpmp80211JSONCfgImportTrap": cambiumpmp80211JSONCfgImportTrap,
       "cambiumpmp80211JSONCfgExportTrap": cambiumpmp80211JSONCfgExportTrap,
       "cambiumpmp80211FullCfgRestoreTrap": cambiumpmp80211FullCfgRestoreTrap,
       "cambiumpmp80211FullCfgBackupTrap": cambiumpmp80211FullCfgBackupTrap,
       "cambiumpmp80211GpsFirmwareUpdateStatusTrap": cambiumpmp80211GpsFirmwareUpdateStatusTrap,
       "cambiumpmp80211STADropTrap": cambiumpmp80211STADropTrap,
       "cambiumpmp80211SMRegTrap": cambiumpmp80211SMRegTrap,
       "cambiumpmp80211SystemRebootTrap": cambiumpmp80211SystemRebootTrap,
       "cambiumpmp80211SAModeTrap": cambiumpmp80211SAModeTrap,
       "cambiumpmpETSIframeSkipTrap": cambiumpmpETSIframeSkipTrap,
       "cambiumPmp80211SystemStatus": cambiumPmp80211SystemStatus,
       "cambiumGeneralStatus": cambiumGeneralStatus,
       "cambiumCurrentSWInfo": cambiumCurrentSWInfo,
       "cambiumHWInfo": cambiumHWInfo,
       "cambiumDateTime": cambiumDateTime,
       "cambiumSystemUptime": cambiumSystemUptime,
       "cambiumWirelessMACAddress": cambiumWirelessMACAddress,
       "cambiumDFSStatus": cambiumDFSStatus,
       "cambiumEffectiveSyncSource": cambiumEffectiveSyncSource,
       "cambiumEffectiveCountryCode": cambiumEffectiveCountryCode,
       "cambiumEffectiveAntennaGain": cambiumEffectiveAntennaGain,
       "cambiumEffectiveTDDRatio": cambiumEffectiveTDDRatio,
       "cambiumEffectiveSSID": cambiumEffectiveSSID,
       "cambiumEffectiveAuthenticationType": cambiumEffectiveAuthenticationType,
       "cambiumEffectiveDeviceName": cambiumEffectiveDeviceName,
       "cambiumUbootVersion": cambiumUbootVersion,
       "cambiumLANMACAddress": cambiumLANMACAddress,
       "cambiumCurrentuImageIVersion": cambiumCurrentuImageIVersion,
       "cambiumCurrentuImageVersion": cambiumCurrentuImageVersion,
       "cambiumDeviceLatitude": cambiumDeviceLatitude,
       "cambiumDeviceLongitude": cambiumDeviceLongitude,
       "sysRebootCounter": sysRebootCounter,
       "cambiumDFSStatusStr": cambiumDFSStatusStr,
       "cambiumDriverType": cambiumDriverType,
       "cambiumESN": cambiumESN,
       "cambiumEPMPMSN": cambiumEPMPMSN,
       "cambiumFactoryReset": cambiumFactoryReset,
       "cambiumSubModeType": cambiumSubModeType,
       "cambiumRFStatus": cambiumRFStatus,
       "cambiumSTAConnectedRFFrequency": cambiumSTAConnectedRFFrequency,
       "cambiumSTAConnectedRFBandwidth": cambiumSTAConnectedRFBandwidth,
       "cambiumSTADLRSSI": cambiumSTADLRSSI,
       "cambiumSTADLCINR": cambiumSTADLCINR,
       "cambiumSTAConductedTXPower": cambiumSTAConductedTXPower,
       "cambiumSTAUplinkMCSMode": cambiumSTAUplinkMCSMode,
       "cambiumSTADownlinkMCSMode": cambiumSTADownlinkMCSMode,
       "cambiumSTAConnectedAP": cambiumSTAConnectedAP,
       "cambiumSTAPowerControlMode": cambiumSTAPowerControlMode,
       "cambiumAPNumberOfConnectedSTA": cambiumAPNumberOfConnectedSTA,
       "cambiumAPConnectedSTAListTable": cambiumAPConnectedSTAListTable,
       "cambiumAPConnectedSTAListEntry": cambiumAPConnectedSTAListEntry,
       "connectedSTAListMAC": connectedSTAListMAC,
       "connectedSTAListAID": connectedSTAListAID,
       "connectedSTAListChannel": connectedSTAListChannel,
       "connectedSTAListULRSSI": connectedSTAListULRSSI,
       "connectedSTAListDLRSSI": connectedSTAListDLRSSI,
       "connectedSTAListULCINR": connectedSTAListULCINR,
       "connectedSTAListDLCINR": connectedSTAListDLCINR,
       "connectedSTAListULMCS": connectedSTAListULMCS,
       "connectedSTAListDLMCS": connectedSTAListDLMCS,
       "connectedSTAListIP": connectedSTAListIP,
       "connectedSTAListMirSrc": connectedSTAListMirSrc,
       "connectedSTAListMirULRate": connectedSTAListMirULRate,
       "connectedSTAListMirDLRate": connectedSTAListMirDLRate,
       "cambiumSTADistanceKm": cambiumSTADistanceKm,
       "cambiumSTADistanceMil": cambiumSTADistanceMil,
       "cambiumPropagationDelay": cambiumPropagationDelay,
       "cambiumSTAConnectedAPListTable": cambiumSTAConnectedAPListTable,
       "cambiumSTAConnectedAPListEntry": cambiumSTAConnectedAPListEntry,
       "connectedAPListSSID": connectedAPListSSID,
       "connectedAPListBSSID": connectedAPListBSSID,
       "connectedAPListChannel": connectedAPListChannel,
       "connectedAPListFrequency": connectedAPListFrequency,
       "connectedAPListBandwidth": connectedAPListBandwidth,
       "connectedAPListRate": connectedAPListRate,
       "connectedAPListCINR": connectedAPListCINR,
       "connectedAPListRSSI": connectedAPListRSSI,
       "connectedAPListNoise": connectedAPListNoise,
       "connectedAPListINT": connectedAPListINT,
       "connectedAPListNEState": connectedAPListNEState,
       "connectedAPListNEAge": connectedAPListNEAge,
       "connectedAPListScanAge": connectedAPListScanAge,
       "connectedAPListRemainingSTA": connectedAPListRemainingSTA,
       "connectedAPListCAPS": connectedAPListCAPS,
       "connectedAPAuthMethod": connectedAPAuthMethod,
       "connectedAPListMeetNEAttemptCriteria": connectedAPListMeetNEAttemptCriteria,
       "wirelessInterfaceConnectionState": wirelessInterfaceConnectionState,
       "cambiumSTAPriority": cambiumSTAPriority,
       "cambiumSTADLSNR": cambiumSTADLSNR,
       "cambiumConnectedAPMACAddress": cambiumConnectedAPMACAddress,
       "cambiumSTAConnectedAPTable": cambiumSTAConnectedAPTable,
       "cambiumSTAConnectedAPEntry": cambiumSTAConnectedAPEntry,
       "connectedAPSSID": connectedAPSSID,
       "connectedAPBSSID": connectedAPBSSID,
       "connectedAPChannel": connectedAPChannel,
       "connectedAPFrequency": connectedAPFrequency,
       "connectedAPBandwidth": connectedAPBandwidth,
       "connectedAPRate": connectedAPRate,
       "connectedAPSNR": connectedAPSNR,
       "connectedAPRSSI": connectedAPRSSI,
       "connectedAPNoise": connectedAPNoise,
       "connectedAPINT": connectedAPINT,
       "connectedAPNEState": connectedAPNEState,
       "connectedAPNEAge": connectedAPNEAge,
       "connectedAPScanAge": connectedAPScanAge,
       "connectedAPRemainingSTA": connectedAPRemainingSTA,
       "connectedAPCAPS": connectedAPCAPS,
       "connectedAPAuthenticationMethod": connectedAPAuthenticationMethod,
       "connectedAPMeetNEAttemptCriteria": connectedAPMeetNEAttemptCriteria,
       "staTxCapacity": staTxCapacity,
       "staTxQuality": staTxQuality,
       "cambiumAPConnectedSTATable": cambiumAPConnectedSTATable,
       "cambiumAPConnectedSTAEntry": cambiumAPConnectedSTAEntry,
       "connectedSTAMAC": connectedSTAMAC,
       "connectedSTAAID": connectedSTAAID,
       "connectedSTAChannel": connectedSTAChannel,
       "connectedSTAULRSSI": connectedSTAULRSSI,
       "connectedSTADLRSSI": connectedSTADLRSSI,
       "connectedSTAULSNR": connectedSTAULSNR,
       "connectedSTADLSNR": connectedSTADLSNR,
       "connectedSTAULMCS": connectedSTAULMCS,
       "connectedSTADLMCS": connectedSTADLMCS,
       "connectedSTAIP": connectedSTAIP,
       "connectedSTAPriority": connectedSTAPriority,
       "connectedSTAMirSrc": connectedSTAMirSrc,
       "connectedSTAMirULRate": connectedSTAMirULRate,
       "connectedSTAMirDLRate": connectedSTAMirDLRate,
       "connectedSTAClickTHWAddr": connectedSTAClickTHWAddr,
       "connectedSTAClickTWebPort": connectedSTAClickTWebPort,
       "connectedSTAClickTWebSec": connectedSTAClickTWebSec,
       "connectedSTAClickTHostName": connectedSTAClickTHostName,
       "connectedSTATXCapacity": connectedSTATXCapacity,
       "connectedSTATXQuality": connectedSTATXQuality,
       "connectedSTAMcastTotalGroups": connectedSTAMcastTotalGroups,
       "connectedSTAMcastGRP0": connectedSTAMcastGRP0,
       "connectedSTAMcastGRP1": connectedSTAMcastGRP1,
       "connectedSTAMcastGRP2": connectedSTAMcastGRP2,
       "connectedSTAMcastGRP3": connectedSTAMcastGRP3,
       "connectedSTAMcastGRP4": connectedSTAMcastGRP4,
       "connectedSTASessionTime": connectedSTASessionTime,
       "connectedSTADLRateMbps": connectedSTADLRateMbps,
       "cambiumAPBridgeTable": cambiumAPBridgeTable,
       "cambiumAPBridgeEntry": cambiumAPBridgeEntry,
       "camAPBrTabBridgeName": camAPBrTabBridgeName,
       "camAPBrTabDevMACAddress": camAPBrTabDevMACAddress,
       "camAPBrTabDevPort": camAPBrTabDevPort,
       "camAPBrTabSTAMACAddress": camAPBrTabSTAMACAddress,
       "camAPBrTabAgingTime": camAPBrTabAgingTime,
       "cambiumSTABridgeTable": cambiumSTABridgeTable,
       "cambiumSTABridgeEntry": cambiumSTABridgeEntry,
       "camSTABrTabBridgeName": camSTABrTabBridgeName,
       "camSTABrTabDevMACAddress": camSTABrTabDevMACAddress,
       "camSTABrTabDevPort": camSTABrTabDevPort,
       "camSTABrTabAgingTime": camSTABrTabAgingTime,
       "cambiumSTAMAC": cambiumSTAMAC,
       "cambiumSTADropReason": cambiumSTADropReason,
       "cambiumGPSStatus": cambiumGPSStatus,
       "cambiumGPSCurrentSyncState": cambiumGPSCurrentSyncState,
       "cambiumGPSLatitude": cambiumGPSLatitude,
       "cambiumGPSLongitude": cambiumGPSLongitude,
       "cambiumGPSHeight": cambiumGPSHeight,
       "cambiumGPSTime": cambiumGPSTime,
       "cambiumGPSNumTrackedSat": cambiumGPSNumTrackedSat,
       "cambiumGPSNumVisibleSat": cambiumGPSNumVisibleSat,
       "cambiumGPSSatSNRTable": cambiumGPSSatSNRTable,
       "cambiumGPSSatSNREntry": cambiumGPSSatSNREntry,
       "gpsSatelliteId": gpsSatelliteId,
       "gpsSnrValue": gpsSnrValue,
       "gpsSatelliteStatus": gpsSatelliteStatus,
       "cambiumGPSDeviceInfo": cambiumGPSDeviceInfo,
       "cambiumGPSFirmwareUpdateStatus": cambiumGPSFirmwareUpdateStatus,
       "cambiumLinkStatus": cambiumLinkStatus,
       "cambiumLANStatus": cambiumLANStatus,
       "cambiumWLANStatus": cambiumWLANStatus,
       "cambiumEffectiveDeviceIPAddress": cambiumEffectiveDeviceIPAddress,
       "cambiumEffectiveSTANetworkMode": cambiumEffectiveSTANetworkMode,
       "cambiumEffectiveDeviceLANNetMask": cambiumEffectiveDeviceLANNetMask,
       "cambiumEffectiveDeviceDefaultGateWay": cambiumEffectiveDeviceDefaultGateWay,
       "cambiumEffectiveDeviceDNSIPAddress": cambiumEffectiveDeviceDNSIPAddress,
       "cambiumEffectiveWANIPAddress": cambiumEffectiveWANIPAddress,
       "cambiumEffectiveDeviceWANNetMask": cambiumEffectiveDeviceWANNetMask,
       "cambiumEffectiveDeviceWANPPPoEStatus": cambiumEffectiveDeviceWANPPPoEStatus,
       "cambiumLANModeStatus": cambiumLANModeStatus,
       "cambiumLANSpeedStatus": cambiumLANSpeedStatus,
       "cambiumDHCPOption82Status": cambiumDHCPOption82Status,
       "cambiumLAN2ModeStatus": cambiumLAN2ModeStatus,
       "cambiumLAN2SpeedStatus": cambiumLAN2SpeedStatus,
       "cambiumLAN2Status": cambiumLAN2Status,
       "cambiumARPTable": cambiumARPTable,
       "cambiumARPEntry": cambiumARPEntry,
       "cambiumARPIndex": cambiumARPIndex,
       "cambiumARPMAC": cambiumARPMAC,
       "cambiumARPIP": cambiumARPIP,
       "cambiumARPInterface": cambiumARPInterface,
       "cambiumManagementIFStatus": cambiumManagementIFStatus,
       "cambiumManagementIFIPAddress": cambiumManagementIFIPAddress,
       "cambiumManagementIFNetMask": cambiumManagementIFNetMask,
       "cambiumManagementIFGateway": cambiumManagementIFGateway,
       "cambiumEffectiveNetworkLanMTU": cambiumEffectiveNetworkLanMTU,
       "cambiumEffectiveNetworkBridgeMTU": cambiumEffectiveNetworkBridgeMTU,
       "cambiumStaticRoutesTable": cambiumStaticRoutesTable,
       "cambiumStaticRoutesEntry": cambiumStaticRoutesEntry,
       "cambiumStaticRoutesIndex": cambiumStaticRoutesIndex,
       "cambiumStaticRoutesDestIP": cambiumStaticRoutesDestIP,
       "cambiumStaticRoutesGW": cambiumStaticRoutesGW,
       "cambiumStaticRoutesNetmask": cambiumStaticRoutesNetmask,
       "cambiumStaticRoutesInterface": cambiumStaticRoutesInterface,
       "cambiumIPAliasTable": cambiumIPAliasTable,
       "cambiumIPAliasEntry": cambiumIPAliasEntry,
       "cambiumIPAliasTableIndex": cambiumIPAliasTableIndex,
       "cambiumIPAliasIP": cambiumIPAliasIP,
       "cambiumIPAliasNetmask": cambiumIPAliasNetmask,
       "cambiumCnsServConsStat": cambiumCnsServConsStat,
       "cambiumCnsServAccountID": cambiumCnsServAccountID,
       "cambiumAPCnsMGMTState": cambiumAPCnsMGMTState,
       "cambiumAcsStatus": cambiumAcsStatus,
       "acsState": acsState,
       "cambiumMcastStatus": cambiumMcastStatus,
       "cambiumEffectiveMcastGroupLimit": cambiumEffectiveMcastGroupLimit,
       "cambiumSubscribedMcastGroupNum": cambiumSubscribedMcastGroupNum,
       "cambiumAPMcastTotalGroupCount": cambiumAPMcastTotalGroupCount,
       "cambiumMcastHandlingStatus": cambiumMcastHandlingStatus,
       "cambiumSubscribedMcastGroupTable": cambiumSubscribedMcastGroupTable,
       "cambiumSubscribedMcastGroupEntry": cambiumSubscribedMcastGroupEntry,
       "cambiumRegisteredMcastGroupIP": cambiumRegisteredMcastGroupIP,
       "cambiumDhcpStatus": cambiumDhcpStatus,
       "dhcpServerStartIP": dhcpServerStartIP,
       "dhcpServerEndIP": dhcpServerEndIP,
       "dhcpServerGatewayIP": dhcpServerGatewayIP,
       "dhcpServerDNSIP": dhcpServerDNSIP,
       "dhcpServerStaticHostTable": dhcpServerStaticHostTable,
       "dhcpServerStaticHostEntry": dhcpServerStaticHostEntry,
       "dhcpStaticIndex": dhcpStaticIndex,
       "dhcpStaticMAC": dhcpStaticMAC,
       "dhcpStaticIP": dhcpStaticIP,
       "dhcpServerLeaseTable": dhcpServerLeaseTable,
       "dhcpServerLeaseEntry": dhcpServerLeaseEntry,
       "dhcpLeaseIndex": dhcpLeaseIndex,
       "dhcpLeaseMAC": dhcpLeaseMAC,
       "dhcpLeaseIP": dhcpLeaseIP,
       "dhcpLeaseDevName": dhcpLeaseDevName,
       "cambiumPmp80211SystemMonitoring": cambiumPmp80211SystemMonitoring,
       "cambiumPerformanceMonitoring": cambiumPerformanceMonitoring,
       "cambiumStatsForceUpdate": cambiumStatsForceUpdate,
       "cambiumEthRXBytes": cambiumEthRXBytes,
       "cambiumEthRXPackets": cambiumEthRXPackets,
       "cambiumEthRXErrors": cambiumEthRXErrors,
       "cambiumEthRXDrops": cambiumEthRXDrops,
       "cambiumEthRXMulticast": cambiumEthRXMulticast,
       "cambiumEthRXBroadcast": cambiumEthRXBroadcast,
       "cambiumEthTXBytes": cambiumEthTXBytes,
       "cambiumEthTXPackets": cambiumEthTXPackets,
       "cambiumEthTXErrors": cambiumEthTXErrors,
       "cambiumEthTXDrops": cambiumEthTXDrops,
       "cambiumEthTXMulticast": cambiumEthTXMulticast,
       "cambiumEthTXBroadcast": cambiumEthTXBroadcast,
       "cambiumAthRXBytes": cambiumAthRXBytes,
       "cambiumAthRXPackets": cambiumAthRXPackets,
       "cambiumAthRXErrors": cambiumAthRXErrors,
       "cambiumAthRXDrops": cambiumAthRXDrops,
       "cambiumAthRXMulticast": cambiumAthRXMulticast,
       "cambiumAthRXBroadcast": cambiumAthRXBroadcast,
       "cambiumAthTXBytes": cambiumAthTXBytes,
       "cambiumAthTXPackets": cambiumAthTXPackets,
       "cambiumAthTXErrors": cambiumAthTXErrors,
       "cambiumAthTXDrops": cambiumAthTXDrops,
       "cambiumAthTXMulticast": cambiumAthTXMulticast,
       "cambiumAthTXBroadcast": cambiumAthTXBroadcast,
       "sysNetworkEntryAttempt": sysNetworkEntryAttempt,
       "sysNetworkEntrySuccess": sysNetworkEntrySuccess,
       "sysNetworkEntryAuthenticationFailure": sysNetworkEntryAuthenticationFailure,
       "sysDFSDetectedCount": sysDFSDetectedCount,
       "ulWLanKbitCount": ulWLanKbitCount,
       "dlWLanKbitCount": dlWLanKbitCount,
       "ulWLanTotalPacketCount": ulWLanTotalPacketCount,
       "sysRebootCount": sysRebootCount,
       "dlWLanTotalPacketCount": dlWLanTotalPacketCount,
       "ulWLanMultiBroadcastKbitCount": ulWLanMultiBroadcastKbitCount,
       "dlWLanMultiBroadcastKbitCount": dlWLanMultiBroadcastKbitCount,
       "wLanSessionDroppedCount": wLanSessionDroppedCount,
       "cambiumTDDStatsPerSTATable": cambiumTDDStatsPerSTATable,
       "cambiumTDDStatsPerSTAEntry": cambiumTDDStatsPerSTAEntry,
       "cambiumTDDStatsPerSTAIndex": cambiumTDDStatsPerSTAIndex,
       "cambiumTDDStatsListMAC": cambiumTDDStatsListMAC,
       "ulWLanPerUserKbitCount": ulWLanPerUserKbitCount,
       "dlWLanPerUserKbitCount": dlWLanPerUserKbitCount,
       "ulWLanPerUserTotalPacketCount": ulWLanPerUserTotalPacketCount,
       "dlWLanPerUserTotalPacketCount": dlWLanPerUserTotalPacketCount,
       "ulWLanPerUserErrorDroppedPacketCount": ulWLanPerUserErrorDroppedPacketCount,
       "dlWLanPerUserErrorDroppedPacketCount": dlWLanPerUserErrorDroppedPacketCount,
       "dlWLanPerUserCapacityDroppedPacketCount": dlWLanPerUserCapacityDroppedPacketCount,
       "dlWLanPerUserRetransmitPacketCount": dlWLanPerUserRetransmitPacketCount,
       "dlWLanPerUserTxPower": dlWLanPerUserTxPower,
       "ulWLanErrorDroppedPacketCount": ulWLanErrorDroppedPacketCount,
       "dlWLanErrorDroppedPacketCount": dlWLanErrorDroppedPacketCount,
       "ulWLanCapacityDroppedPacketCount": ulWLanCapacityDroppedPacketCount,
       "dlWLanCapacityDroppedPacketCount": dlWLanCapacityDroppedPacketCount,
       "ulWLanTotalAvailableFrameTimePerSecond": ulWLanTotalAvailableFrameTimePerSecond,
       "dlWLanTotalAvailableFrameTimePerSecond": dlWLanTotalAvailableFrameTimePerSecond,
       "ulWLanTotalUsedFrameTimePerSecond": ulWLanTotalUsedFrameTimePerSecond,
       "dlWLanTotalUsedFrameTimePerSecond": dlWLanTotalUsedFrameTimePerSecond,
       "ulWLanTotalOverheadFrameTimePerSecond": ulWLanTotalOverheadFrameTimePerSecond,
       "dlWLanTotalOverheadFrameTimePerSecond": dlWLanTotalOverheadFrameTimePerSecond,
       "cambiumMCSTable": cambiumMCSTable,
       "cambiumMCSEntry": cambiumMCSEntry,
       "cambiumMCSIndex": cambiumMCSIndex,
       "cambiumMCSNumber": cambiumMCSNumber,
       "ulWLanMCSUsedFrameTimePerSecond": ulWLanMCSUsedFrameTimePerSecond,
       "dlWLanMCSUsedFrameTimePerSecond": dlWLanMCSUsedFrameTimePerSecond,
       "ulWLanRetransPacketCount": ulWLanRetransPacketCount,
       "dlWLanRetransPacketCount": dlWLanRetransPacketCount,
       "ulWLanBroadcastPacketCount": ulWLanBroadcastPacketCount,
       "dlWLanBroadcastPacketCount": dlWLanBroadcastPacketCount,
       "ulWLanMulticastPacketCount": ulWLanMulticastPacketCount,
       "dlWLanMulticastPacketCount": dlWLanMulticastPacketCount,
       "sysCPUUsage": sysCPUUsage,
       "rxEtherLanKbitCount": rxEtherLanKbitCount,
       "rxEtherLanTotalPacketCount": rxEtherLanTotalPacketCount,
       "rxEtherLanErrorPacketCount": rxEtherLanErrorPacketCount,
       "rxEtherLanDroppedPacketCount": rxEtherLanDroppedPacketCount,
       "rxEtherLanMulticastPacketCount": rxEtherLanMulticastPacketCount,
       "rxEtherLanBroadcastPacketCount": rxEtherLanBroadcastPacketCount,
       "rxEtherLanMultiBroadcastKbitCount": rxEtherLanMultiBroadcastKbitCount,
       "txEtherLanKbitCount": txEtherLanKbitCount,
       "txEtherLanTotalPacketCount": txEtherLanTotalPacketCount,
       "txEtherLanErrorPacketCount": txEtherLanErrorPacketCount,
       "txEtherLanDroppedPacketCount": txEtherLanDroppedPacketCount,
       "txEtherLanMulticastPacketCount": txEtherLanMulticastPacketCount,
       "txEtherLanBroadcastPacketCount": txEtherLanBroadcastPacketCount,
       "txEtherLanMultiBroadcastKbitCount": txEtherLanMultiBroadcastKbitCount,
       "cambiumStatsResetTimer": cambiumStatsResetTimer,
       "ulWLanMCS00Packets": ulWLanMCS00Packets,
       "ulWLanMCS01Packets": ulWLanMCS01Packets,
       "ulWLanMCS02Packets": ulWLanMCS02Packets,
       "ulWLanMCS03Packets": ulWLanMCS03Packets,
       "ulWLanMCS04Packets": ulWLanMCS04Packets,
       "ulWLanMCS05Packets": ulWLanMCS05Packets,
       "ulWLanMCS06Packets": ulWLanMCS06Packets,
       "ulWLanMCS07Packets": ulWLanMCS07Packets,
       "ulWLanMCS08Packets": ulWLanMCS08Packets,
       "ulWLanMCS09Packets": ulWLanMCS09Packets,
       "ulWLanMCS10Packets": ulWLanMCS10Packets,
       "ulWLanMCS11Packets": ulWLanMCS11Packets,
       "ulWLanMCS12Packets": ulWLanMCS12Packets,
       "ulWLanMCS13Packets": ulWLanMCS13Packets,
       "ulWLanMCS14Packets": ulWLanMCS14Packets,
       "ulWLanMCS15Packets": ulWLanMCS15Packets,
       "dlWLanMCS00Packets": dlWLanMCS00Packets,
       "dlWLanMCS01Packets": dlWLanMCS01Packets,
       "dlWLanMCS02Packets": dlWLanMCS02Packets,
       "dlWLanMCS03Packets": dlWLanMCS03Packets,
       "dlWLanMCS04Packets": dlWLanMCS04Packets,
       "dlWLanMCS05Packets": dlWLanMCS05Packets,
       "dlWLanMCS06Packets": dlWLanMCS06Packets,
       "dlWLanMCS07Packets": dlWLanMCS07Packets,
       "dlWLanMCS08Packets": dlWLanMCS08Packets,
       "dlWLanMCS09Packets": dlWLanMCS09Packets,
       "dlWLanMCS10Packets": dlWLanMCS10Packets,
       "dlWLanMCS11Packets": dlWLanMCS11Packets,
       "dlWLanMCS12Packets": dlWLanMCS12Packets,
       "dlWLanMCS13Packets": dlWLanMCS13Packets,
       "dlWLanMCS14Packets": dlWLanMCS14Packets,
       "dlWLanMCS15Packets": dlWLanMCS15Packets,
       "cambiumRealTimeStatsMonitoring": cambiumRealTimeStatsMonitoring,
       "cambiumAdvancedPerformanceMonitoring": cambiumAdvancedPerformanceMonitoring,
       "cambiumpmp80211SystemConfiguration": cambiumpmp80211SystemConfiguration,
       "cambiumSystemLog": cambiumSystemLog,
       "syslogServerIPFirst": syslogServerIPFirst,
       "syslogServerIPSecond": syslogServerIPSecond,
       "syslogServerIPThird": syslogServerIPThird,
       "syslogServerIPFourth": syslogServerIPFourth,
       "syslogServerLogToWeb": syslogServerLogToWeb,
       "syslogServerLogMask": syslogServerLogMask,
       "cambiumDHCP": cambiumDHCP,
       "dhcpLanEnable": dhcpLanEnable,
       "dhcpLanStart": dhcpLanStart,
       "dhcpLanLimit": dhcpLanLimit,
       "dhcpLanLeasetime": dhcpLanLeasetime,
       "dhcpLanHostTable": dhcpLanHostTable,
       "dhcpLanHostEntry": dhcpLanHostEntry,
       "dhcpLanHostIndex": dhcpLanHostIndex,
       "dhcpLanHostIP": dhcpLanHostIP,
       "dhcpLanHostMAC": dhcpLanHostMAC,
       "dhcpLanHostName": dhcpLanHostName,
       "dhcpOption82": dhcpOption82,
       "cambiumSSHServer": cambiumSSHServer,
       "cambiumSSHServerEnable": cambiumSSHServerEnable,
       "network": network,
       "networkMode": networkMode,
       "networkLan": networkLan,
       "networkLanIPAddressMode": networkLanIPAddressMode,
       "networkLanIPAddr": networkLanIPAddr,
       "networkLanNetmask": networkLanNetmask,
       "networkLanGatewayIP": networkLanGatewayIP,
       "networkLanDNSIPAddr": networkLanDNSIPAddr,
       "networkLanMTU": networkLanMTU,
       "networkLanDNSIPAddrPrimary": networkLanDNSIPAddrPrimary,
       "networkLanDNSIPAddrSecondary": networkLanDNSIPAddrSecondary,
       "networkLanAutoNegotiation": networkLanAutoNegotiation,
       "networkLanSpeed": networkLanSpeed,
       "networkLanDuplex": networkLanDuplex,
       "networkBroadcastStormEnabled": networkBroadcastStormEnabled,
       "networkBroadcastStormRate": networkBroadcastStormRate,
       "networkLan2Enabled": networkLan2Enabled,
       "networkLan2AutoNegotiation": networkLan2AutoNegotiation,
       "networkLan2Speed": networkLan2Speed,
       "networkLan2Duplex": networkLan2Duplex,
       "networkLan2PoEEnabled": networkLan2PoEEnabled,
       "networkLanEnabled": networkLanEnabled,
       "networkWan": networkWan,
       "networkWanIPAddressMode": networkWanIPAddressMode,
       "networkWanIPAddr": networkWanIPAddr,
       "networkWanNetmask": networkWanNetmask,
       "networkWanGatewayIP": networkWanGatewayIP,
       "networkWanDNSIPAddr": networkWanDNSIPAddr,
       "networkWanMTU": networkWanMTU,
       "networkWanDNSIPAddrPrimary": networkWanDNSIPAddrPrimary,
       "networkWanDNSIPAddrSecondary": networkWanDNSIPAddrSecondary,
       "networkWanPPPoE": networkWanPPPoE,
       "networkWanPPPoEUsername": networkWanPPPoEUsername,
       "networkWanPPPoEPassword": networkWanPPPoEPassword,
       "networkWanPPPoEAC": networkWanPPPoEAC,
       "networkWanPPPoEService": networkWanPPPoEService,
       "networkWanPPPoEAuth": networkWanPPPoEAuth,
       "networkWanPPPoEMTU": networkWanPPPoEMTU,
       "networkWanPPPoEKeepAlive": networkWanPPPoEKeepAlive,
       "networkWanPPPoEMSSClamping": networkWanPPPoEMSSClamping,
       "mgmtVLAN": mgmtVLAN,
       "mgmtVLANEnable": mgmtVLANEnable,
       "mgmtVLANVID": mgmtVLANVID,
       "mgmtVLANVP": mgmtVLANVP,
       "dataVLAN": dataVLAN,
       "dataVLANEnable": dataVLANEnable,
       "dataVLANVID": dataVLANVID,
       "dataVLANVP": dataVLANVP,
       "networkSTP": networkSTP,
       "networkBridge": networkBridge,
       "networkBridgeIPAddressMode": networkBridgeIPAddressMode,
       "networkBridgeIPAddr": networkBridgeIPAddr,
       "networkBridgeNetmask": networkBridgeNetmask,
       "networkBridgeGatewayIP": networkBridgeGatewayIP,
       "networkBridgeDNSIPAddr": networkBridgeDNSIPAddr,
       "networkBridgeMTU": networkBridgeMTU,
       "networkBridgeDNSIPAddrPrimary": networkBridgeDNSIPAddrPrimary,
       "networkBridgeDNSIPAddrSecondary": networkBridgeDNSIPAddrSecondary,
       "networkPortSecurity": networkPortSecurity,
       "networkPortSecurityMax": networkPortSecurityMax,
       "networkPortSecurityAgingTime": networkPortSecurityAgingTime,
       "mcastVLAN": mcastVLAN,
       "mcastVLANEnable": mcastVLANEnable,
       "mcastVLANVID": mcastVLANVID,
       "mcastVLANVP": mcastVLANVP,
       "mcastGroupLimit": mcastGroupLimit,
       "mgmtIF": mgmtIF,
       "mgmtIFEnable": mgmtIFEnable,
       "mgmtIFVLAN": mgmtIFVLAN,
       "mgmtIFVID": mgmtIFVID,
       "mgmtIFVP": mgmtIFVP,
       "mgmtIFIPAddressMode": mgmtIFIPAddressMode,
       "mgmtIFIPAddr": mgmtIFIPAddr,
       "mgmtIFNetmask": mgmtIFNetmask,
       "mgmtIFGateway": mgmtIFGateway,
       "networkLanDefaultIP": networkLanDefaultIP,
       "networkRelaydEnable": networkRelaydEnable,
       "networkAliases": networkAliases,
       "cambiumIPAliasCnfTable": cambiumIPAliasCnfTable,
       "cambiumIPAliasCnfEntry": cambiumIPAliasCnfEntry,
       "cambiumIPAliasesIndex": cambiumIPAliasesIndex,
       "cambiumIPAliasesIpAddr": cambiumIPAliasesIpAddr,
       "cambiumIPAliasesNetmask": cambiumIPAliasesNetmask,
       "cambiumIPAliasesInfo": cambiumIPAliasesInfo,
       "cambiumIPAliasesEnable": cambiumIPAliasesEnable,
       "snmp": snmp,
       "snmpReadOnlyCommunity": snmpReadOnlyCommunity,
       "snmpReadWriteCommunity": snmpReadWriteCommunity,
       "snmpSystemName": snmpSystemName,
       "snmpSystemDescription": snmpSystemDescription,
       "snmpTrapEnable": snmpTrapEnable,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpTrapTable": snmpTrapTable,
       "snmpTrapEntry": snmpTrapEntry,
       "snmpTrapEntryIndex": snmpTrapEntryIndex,
       "snmpTrapEntryIP": snmpTrapEntryIP,
       "snmpTrapEntryPort": snmpTrapEntryPort,
       "snmpDomainAccessEnable": snmpDomainAccessEnable,
       "snmpDomainAccessIP": snmpDomainAccessIP,
       "snmpDomainAccessIPMask": snmpDomainAccessIPMask,
       "cambiumSystem": cambiumSystem,
       "systemConfig": systemConfig,
       "systemConfigTimezone": systemConfigTimezone,
       "systemConfigDeviceName": systemConfigDeviceName,
       "systemConfigETSILicense": systemConfigETSILicense,
       "systemConfigSWLockBit": systemConfigSWLockBit,
       "systemConfigHWLockBit": systemConfigHWLockBit,
       "systemDeviceLocLatitude": systemDeviceLocLatitude,
       "systemDeviceLocLongitude": systemDeviceLocLongitude,
       "systemDeviceLocHeight": systemDeviceLocHeight,
       "systemConfigisGPSkeyOK": systemConfigisGPSkeyOK,
       "systemConfigGPSLockBit": systemConfigGPSLockBit,
       "systemConfigSMLockBit": systemConfigSMLockBit,
       "systemConfigSMLimit": systemConfigSMLimit,
       "powerSequenceFactoryDefault": powerSequenceFactoryDefault,
       "systemConfigLockedCC": systemConfigLockedCC,
       "systemConfigMinAntGain": systemConfigMinAntGain,
       "systemNtpServer": systemNtpServer,
       "systemNtpServerIPMode": systemNtpServerIPMode,
       "systemNtpServerPrimaryIP": systemNtpServerPrimaryIP,
       "systemNtpServerSecondaryIP": systemNtpServerSecondaryIP,
       "cambiumWebServer": cambiumWebServer,
       "webService": webService,
       "httpPort": httpPort,
       "httpsPort": httpsPort,
       "wireless": wireless,
       "wirelessDevice": wirelessDevice,
       "wirelessDeviceCountryCode": wirelessDeviceCountryCode,
       "wirelessType": wirelessType,
       "wirelessDefaultCountryCode": wirelessDefaultCountryCode,
       "wirelessInterface": wirelessInterface,
       "wirelessInterfaceMode": wirelessInterfaceMode,
       "wirelessInterfaceSSID": wirelessInterfaceSSID,
       "wirelessInterfaceEncryption": wirelessInterfaceEncryption,
       "wirelessInterfaceEncryptionKey": wirelessInterfaceEncryptionKey,
       "wirelessInterfaceHTMode": wirelessInterfaceHTMode,
       "wirelessInterfaceTXPower": wirelessInterfaceTXPower,
       "wirelessInterfaceTDDAntennaGain": wirelessInterfaceTDDAntennaGain,
       "wirelessInterfaceTDDRatio": wirelessInterfaceTDDRatio,
       "wirelessInterfaceTPCTRL": wirelessInterfaceTPCTRL,
       "wirelessInterfaceTPCMode": wirelessInterfaceTPCMode,
       "wirelessInterfacePTPMode": wirelessInterfacePTPMode,
       "wirelessInterfacePTPMACAddress": wirelessInterfacePTPMACAddress,
       "wirelessInterfaceSyncSource": wirelessInterfaceSyncSource,
       "wirelessInterfaceSyncHoldTime": wirelessInterfaceSyncHoldTime,
       "wirelessInterfaceScanFrequencyListTwenty": wirelessInterfaceScanFrequencyListTwenty,
       "wirelessInterfaceScanFrequencyListForty": wirelessInterfaceScanFrequencyListForty,
       "centerFrequency": centerFrequency,
       "dfsAlternative1CenterFrequency": dfsAlternative1CenterFrequency,
       "dfsAlternative2CenterFrequency": dfsAlternative2CenterFrequency,
       "wirelessMaximumCellSize": wirelessMaximumCellSize,
       "wirelessCellSizeUnit": wirelessCellSizeUnit,
       "wirelessMaximumSTA": wirelessMaximumSTA,
       "dfsAlternative1Bandwidth": dfsAlternative1Bandwidth,
       "dfsAlternative2Bandwidth": dfsAlternative2Bandwidth,
       "wirelessAcceptableAPRSSIThreshold": wirelessAcceptableAPRSSIThreshold,
       "wirelessAcceptableAPCINRThreshold": wirelessAcceptableAPCINRThreshold,
       "wirelessInterfaceUnblockUSfreqs": wirelessInterfaceUnblockUSfreqs,
       "wirelessMIREnable": wirelessMIREnable,
       "wirelessMIRSTAProfileNumber": wirelessMIRSTAProfileNumber,
       "wirelessMIRAPDefaultProfileNumber": wirelessMIRAPDefaultProfileNumber,
       "wirelessInterfaceScanFrequencyBandwidth": wirelessInterfaceScanFrequencyBandwidth,
       "wirelessInterfaceGuardInterval": wirelessInterfaceGuardInterval,
       "wirelessInterfaceiFreqReuseMode": wirelessInterfaceiFreqReuseMode,
       "wirelessSTAPriority": wirelessSTAPriority,
       "wirelessSmoothingBit": wirelessSmoothingBit,
       "wirelessSecurityMethod": wirelessSecurityMethod,
       "wirelessAcceptableAPSNRThreshold": wirelessAcceptableAPSNRThreshold,
       "wirelessMgmtPacketRate": wirelessMgmtPacketRate,
       "wirelessStaIsolate": wirelessStaIsolate,
       "wirelessCcaEnable": wirelessCcaEnable,
       "wirelessInterfaceScanFrequencyListTen": wirelessInterfaceScanFrequencyListTen,
       "wirelessInterfaceScanFrequencyListFive": wirelessInterfaceScanFrequencyListFive,
       "wirelessMulticastEnhanceMode": wirelessMulticastEnhanceMode,
       "wirelessTXPowerManualLimit": wirelessTXPowerManualLimit,
       "wirelessRateMaxMCS": wirelessRateMaxMCS,
       "wirelessSMWifiDistance": wirelessSMWifiDistance,
       "wirelessInterfaceProtocolMode": wirelessInterfaceProtocolMode,
       "forceMcastBcast4Addr": forceMcastBcast4Addr,
       "wirelessInterfaceRateMinMCS": wirelessInterfaceRateMinMCS,
       "wirelessInterfaceRateMaxMCS": wirelessInterfaceRateMaxMCS,
       "wirelessMulticastIgmpFastLeave": wirelessMulticastIgmpFastLeave,
       "wirelessInterfaceTDDFrameSize": wirelessInterfaceTDDFrameSize,
       "wirelessInterfaceColocState": wirelessInterfaceColocState,
       "wirelessInterfaceColocSystemSyncSrc": wirelessInterfaceColocSystemSyncSrc,
       "wirelessAPWifiWLANmode": wirelessAPWifiWLANmode,
       "apWiFiDLCTSMode": apWiFiDLCTSMode,
       "apWiFiULCTSRTSMode": apWiFiULCTSRTSMode,
       "apWiFiRTSThreshold": apWiFiRTSThreshold,
       "wirelessPrefList": wirelessPrefList,
       "prefferedAPTable": prefferedAPTable,
       "prefferedAPEntry": prefferedAPEntry,
       "prefferedListTableEntryIndex": prefferedListTableEntryIndex,
       "prefferedListTableEntrySSID": prefferedListTableEntrySSID,
       "prefferedListTableEntryKEY": prefferedListTableEntryKEY,
       "prefferedListTableSecurityMethod": prefferedListTableSecurityMethod,
       "wirelessMIRList": wirelessMIRList,
       "wirelessMIRProfileTable": wirelessMIRProfileTable,
       "wirelessMIRProfileEntry": wirelessMIRProfileEntry,
       "wirelessMIRProfileIndex": wirelessMIRProfileIndex,
       "wirelessMIRProfileNumber": wirelessMIRProfileNumber,
       "wirelessMIRProfileDescription": wirelessMIRProfileDescription,
       "wirelessDLMIR": wirelessDLMIR,
       "wirelessULMIR": wirelessULMIR,
       "wirelessRadius": wirelessRadius,
       "wirelessRadiusTimeout": wirelessRadiusTimeout,
       "wirelessRadiusRetry": wirelessRadiusRetry,
       "wirelessRadiusGUIUserAuth": wirelessRadiusGUIUserAuth,
       "wirelessRadiusCurrentGUIUserAuth": wirelessRadiusCurrentGUIUserAuth,
       "wirelessRadiusSeverInfo": wirelessRadiusSeverInfo,
       "wirelessRadiusIdentityStr": wirelessRadiusIdentityStr,
       "wirelessRadiusIdentityRealm": wirelessRadiusIdentityRealm,
       "wirelessRadiusUsername": wirelessRadiusUsername,
       "wirelessRadiusPassword": wirelessRadiusPassword,
       "wirelessRadiusServerList": wirelessRadiusServerList,
       "wirelessRadiusServerTable": wirelessRadiusServerTable,
       "wirelessRadiusServerEntry": wirelessRadiusServerEntry,
       "wirelessRadiusServerIndex": wirelessRadiusServerIndex,
       "wirelessRadiusServerIP": wirelessRadiusServerIP,
       "wirelessRadiusServerPort": wirelessRadiusServerPort,
       "wirelessRadiusServerSecret": wirelessRadiusServerSecret,
       "wirelessRadiusCertificateList": wirelessRadiusCertificateList,
       "wirelessRadiusCertificateListRow1": wirelessRadiusCertificateListRow1,
       "wirelessRadiusUseDefCertificate": wirelessRadiusUseDefCertificate,
       "wirelessRadiusDefCertificateView": wirelessRadiusDefCertificateView,
       "wirelessRadiusCertificateListRow2": wirelessRadiusCertificateListRow2,
       "wirelessRadiusUser1CertificateName": wirelessRadiusUser1CertificateName,
       "wirelessRadiusUser1CertificateView": wirelessRadiusUser1CertificateView,
       "wirelessRadiusCertificateListRow3": wirelessRadiusCertificateListRow3,
       "wirelessRadiusUser2CertificateName": wirelessRadiusUser2CertificateName,
       "wirelessRadiusUser2CertificateView": wirelessRadiusUser2CertificateView,
       "wirelessRadiusCertificateSet": wirelessRadiusCertificateSet,
       "wirelessRadiusDefaultCertificate": wirelessRadiusDefaultCertificate,
       "wirelessRadiusUser1Certificate": wirelessRadiusUser1Certificate,
       "wirelessRadiusUser2Certificate": wirelessRadiusUser2Certificate,
       "wirelessRadiusUseDefaultCertificate": wirelessRadiusUseDefaultCertificate,
       "wirelessRadiusExtraCertificateSet": wirelessRadiusExtraCertificateSet,
       "wirelessRadiusPMP320Certificate": wirelessRadiusPMP320Certificate,
       "wirelessRadiusUsePMP320Certificate": wirelessRadiusUsePMP320Certificate,
       "wirelessRadiusPMP450Certificate": wirelessRadiusPMP450Certificate,
       "wirelessRadiusUsePMP450Certificate": wirelessRadiusUsePMP450Certificate,
       "multicast": multicast,
       "l2Firewall": l2Firewall,
       "l2FirewallEnable": l2FirewallEnable,
       "l2FirewallTable": l2FirewallTable,
       "l2FirewallEntry": l2FirewallEntry,
       "l2FirewallEntryIndex": l2FirewallEntryIndex,
       "l2FirewallEntryName": l2FirewallEntryName,
       "l2FirewallEntryAction": l2FirewallEntryAction,
       "l2FirewallEntryInterface": l2FirewallEntryInterface,
       "l2FirewallEntryLog": l2FirewallEntryLog,
       "l2FirewallEntryEtherType": l2FirewallEntryEtherType,
       "l2FirewallEntryVlanID": l2FirewallEntryVlanID,
       "l2FirewallEntrySrcMAC": l2FirewallEntrySrcMAC,
       "l2FirewallEntrySrcMask": l2FirewallEntrySrcMask,
       "l2FirewallEntryDstMAC": l2FirewallEntryDstMAC,
       "l2FirewallEntryDstMask": l2FirewallEntryDstMask,
       "l2WanRemoteAccess": l2WanRemoteAccess,
       "l2SnmpLanRemoteAccess": l2SnmpLanRemoteAccess,
       "l2DHCPServersBelowSTA": l2DHCPServersBelowSTA,
       "l2LanRemoteAccess": l2LanRemoteAccess,
       "l3Firewall": l3Firewall,
       "l3FirewallEnable": l3FirewallEnable,
       "l3FirewallTable": l3FirewallTable,
       "l3FirewallEntry": l3FirewallEntry,
       "l3FirewallEntryIndex": l3FirewallEntryIndex,
       "l3FirewallEntryName": l3FirewallEntryName,
       "l3FirewallEntryAction": l3FirewallEntryAction,
       "l3FirewallEntryInterface": l3FirewallEntryInterface,
       "l3FirewallEntryLog": l3FirewallEntryLog,
       "l3FirewallEntryProtocol": l3FirewallEntryProtocol,
       "l3FirewallEntryPort": l3FirewallEntryPort,
       "l3FirewallEntrySrcIP": l3FirewallEntrySrcIP,
       "l3FirewallEntrySrcMask": l3FirewallEntrySrcMask,
       "l3FirewallEntryDstIP": l3FirewallEntryDstIP,
       "l3FirewallEntryDstMask": l3FirewallEntryDstMask,
       "l3FirewallEntryDSCP": l3FirewallEntryDSCP,
       "l3FirewallEntryToS": l3FirewallEntryToS,
       "confQoS": confQoS,
       "voipEnable": voipEnable,
       "qosEnable": qosEnable,
       "classificationListTable": classificationListTable,
       "classificationListEntry": classificationListEntry,
       "classificationRuleIndex": classificationRuleIndex,
       "classificationRuleType": classificationRuleType,
       "classificationRuleValue": classificationRuleValue,
       "classificationRuleIP": classificationRuleIP,
       "classificationRuleMAC": classificationRuleMAC,
       "classificationRuleMask": classificationRuleMask,
       "classificationRuleDirection": classificationRuleDirection,
       "classificationRuleQueue": classificationRuleQueue,
       "mcPriority": mcPriority,
       "bcPriority": bcPriority,
       "dmz": dmz,
       "dmzEnable": dmzEnable,
       "dmzIPAddress": dmzIPAddress,
       "portForwarding": portForwarding,
       "portForwardingEntryEnable": portForwardingEntryEnable,
       "portForwardingTable": portForwardingTable,
       "portForwardingEntry": portForwardingEntry,
       "portForwardingTableEntryIndex": portForwardingTableEntryIndex,
       "portForwardingTableEntryProtocol": portForwardingTableEntryProtocol,
       "portForwardingTableEntryWLANPortBegin": portForwardingTableEntryWLANPortBegin,
       "portForwardingTableEntryWLANPortEnd": portForwardingTableEntryWLANPortEnd,
       "portForwardingTableEntryLANIP": portForwardingTableEntryLANIP,
       "vlans": vlans,
       "membershipVLANTable": membershipVLANTable,
       "membershipVLANEntry": membershipVLANEntry,
       "membershipVLANTableEntryIndex": membershipVLANTableEntryIndex,
       "membershipVLANTableEntryVIDBegin": membershipVLANTableEntryVIDBegin,
       "membershipVLANTableEntryVIDEnd": membershipVLANTableEntryVIDEnd,
       "mappingVLANTable": mappingVLANTable,
       "mappingVLANEntry": mappingVLANEntry,
       "mappingVLANTableEntryIndex": mappingVLANTableEntryIndex,
       "mappingVLANTableEntryCVLAN": mappingVLANTableEntryCVLAN,
       "mappingVLANTableEntrySVLAN": mappingVLANTableEntrySVLAN,
       "dlkm": dlkm,
       "dlkmNATSIPHelpers": dlkmNATSIPHelpers,
       "routing": routing,
       "staticRoutesEnableMain": staticRoutesEnableMain,
       "cambiumStaticRoutesCnfTable": cambiumStaticRoutesCnfTable,
       "cambiumStaticRoutesCnfEntry": cambiumStaticRoutesCnfEntry,
       "cambiumStaticRoutesCnfIndex": cambiumStaticRoutesCnfIndex,
       "cambiumStaticRoutesCnfDestIP": cambiumStaticRoutesCnfDestIP,
       "cambiumStaticRoutesCnfGW": cambiumStaticRoutesCnfGW,
       "cambiumStaticRoutesCnfNetmask": cambiumStaticRoutesCnfNetmask,
       "cambiumStaticRoutesCnfEnbl": cambiumStaticRoutesCnfEnbl,
       "cambiumStaticRoutesCnfInfo": cambiumStaticRoutesCnfInfo,
       "cambiumDeviceAgent": cambiumDeviceAgent,
       "cambiumDeviceAgentEnable": cambiumDeviceAgentEnable,
       "cambiumDeviceAgentCNSURL": cambiumDeviceAgentCNSURL,
       "cambiumCNSDeviceAgentID": cambiumCNSDeviceAgentID,
       "cambiumCNSDeviceAgentPassword": cambiumCNSDeviceAgentPassword,
       "upnpd": upnpd,
       "networkUPNP": networkUPNP,
       "networkNATPMP": networkNATPMP,
       "cambiumpmp80211SystemActions": cambiumpmp80211SystemActions,
       "cambiumpmp80211DeviceReboot": cambiumpmp80211DeviceReboot,
       "cambiumpmp80211ConfigurationReset": cambiumpmp80211ConfigurationReset,
       "cambiumpmp80211ConfigurationSave": cambiumpmp80211ConfigurationSave,
       "cambiumpmp80211ConfigurationApply": cambiumpmp80211ConfigurationApply,
       "cambiumpmp80211ConfigurationDiscard": cambiumpmp80211ConfigurationDiscard,
       "cambiumpmp80211ConfigurationState": cambiumpmp80211ConfigurationState,
       "cambiumpmp80211SoftwareUpdate": cambiumpmp80211SoftwareUpdate,
       "cambiumpmp80211SoftwareUpdateStatus": cambiumpmp80211SoftwareUpdateStatus,
       "cambiumpmp80211STAListUpdate": cambiumpmp80211STAListUpdate,
       "cambiumpmp80211STAListUpdateStatus": cambiumpmp80211STAListUpdateStatus,
       "cambiumpmp80211APListUpdate": cambiumpmp80211APListUpdate,
       "cambiumpmp80211APListUpdateStatus": cambiumpmp80211APListUpdateStatus,
       "cambiumpmp80211SoftwareUpdateError": cambiumpmp80211SoftwareUpdateError,
       "cambiumpmp80211StatsPerSTAListUpdateStatus": cambiumpmp80211StatsPerSTAListUpdateStatus,
       "cambiumpmp80211StatsPerSTAListUpdate": cambiumpmp80211StatsPerSTAListUpdate,
       "cambiumpmp80211STADisconnect": cambiumpmp80211STADisconnect,
       "cambiumpmp80211GPSAutopopulate": cambiumpmp80211GPSAutopopulate,
       "cambiumpmp80211SoftwareUpdateErrorStr": cambiumpmp80211SoftwareUpdateErrorStr,
       "cambiumpmp80211GpsFirmwareUpdate": cambiumpmp80211GpsFirmwareUpdate,
       "cambiumpmp80211GpsFirmwareUpdateError": cambiumpmp80211GpsFirmwareUpdateError,
       "cambiumpmp80211GpsFirmwareUpdateErrorStr": cambiumpmp80211GpsFirmwareUpdateErrorStr,
       "cambiumBridgeTableAPStatus": cambiumBridgeTableAPStatus,
       "cambiumBridgeTableSTAUpdate": cambiumBridgeTableSTAUpdate,
       "cambiumBridgeTableSTAStatus": cambiumBridgeTableSTAStatus,
       "cambiumBridgeTableAPUpdate": cambiumBridgeTableAPUpdate,
       "cambiumForceTabUpdDHCP": cambiumForceTabUpdDHCP,
       "cambiumForceTabUpdTrap": cambiumForceTabUpdTrap,
       "cambiumForceTabUpdl2Frw": cambiumForceTabUpdl2Frw,
       "cambiumForceTabUpdl3Frw": cambiumForceTabUpdl3Frw,
       "cambiumForceTabUpdQos": cambiumForceTabUpdQos,
       "cambiumForceTabUpdPortFw": cambiumForceTabUpdPortFw,
       "cambiumForceTabUpdVlan": cambiumForceTabUpdVlan,
       "cambiumForceTabUpdMappingVlan": cambiumForceTabUpdMappingVlan,
       "cambiumConfigurationApplyOnReboot": cambiumConfigurationApplyOnReboot,
       "cambiumForceSTARescan": cambiumForceSTARescan,
       "cambiumForceTabUpdMcastDeny": cambiumForceTabUpdMcastDeny,
       "cambiumForceTabUpdStaticRoutesCnf": cambiumForceTabUpdStaticRoutesCnf,
       "cambiumForceTabUpdMIR": cambiumForceTabUpdMIR,
       "cambiumForceTabUpdRadiusServ": cambiumForceTabUpdRadiusServ,
       "cambiumForceTabUpdPrefAPList": cambiumForceTabUpdPrefAPList,
       "cambiumForceTabUpdAPAlias": cambiumForceTabUpdAPAlias,
       "cambiumpmp80211Tools": cambiumpmp80211Tools,
       "cambiumLinkTest": cambiumLinkTest,
       "cambiumLinkTestDuration": cambiumLinkTestDuration,
       "cambiumLinkTestPckSize": cambiumLinkTestPckSize,
       "cambiumLinkTestStartForMAC": cambiumLinkTestStartForMAC,
       "cambiumLinkTestStatus": cambiumLinkTestStatus,
       "cambiumLinkTestResultDate": cambiumLinkTestResultDate,
       "cambiumLinkTestResultUL": cambiumLinkTestResultUL,
       "cambiumLinkTestResultDL": cambiumLinkTestResultDL,
       "caminfo": caminfo,
       "caminfoScanFrequencyListCountry": caminfoScanFrequencyListCountry,
       "caminfoScanFrequencyListTwentyBand": caminfoScanFrequencyListTwentyBand,
       "caminfoScanFrequencyListFortyBand": caminfoScanFrequencyListFortyBand,
       "caminfoScanFrequencyListAllow59band": caminfoScanFrequencyListAllow59band,
       "cambiumToolBar": cambiumToolBar,
       "cambiumToolBarOpts": cambiumToolBarOpts,
       "cambiumInternetConnectionServerIP": cambiumInternetConnectionServerIP,
       "cambiumInternetConnectionPollPeriod": cambiumInternetConnectionPollPeriod,
       "cambiumToolBarStates": cambiumToolBarStates,
       "cambiumToolbarGlobeState": cambiumToolbarGlobeState,
       "cambiumToolbarGPSSyncState": cambiumToolbarGPSSyncState,
       "cambiumToolbarDeviceConfigurationState": cambiumToolbarDeviceConfigurationState,
       "cambiumToolbarSyncSource": cambiumToolbarSyncSource,
       "cambiumToolbarGPSSyncStateStr": cambiumToolbarGPSSyncStateStr,
       "cambiumCfg": cambiumCfg,
       "cambiumJSONCfgImport": cambiumJSONCfgImport,
       "cambiumJSONCfgImportStatus": cambiumJSONCfgImportStatus,
       "cambiumJSONCfgImportError": cambiumJSONCfgImportError,
       "cambiumJSONCfgExport": cambiumJSONCfgExport,
       "cambiumJSONCfgExportStatus": cambiumJSONCfgExportStatus,
       "cambiumJSONCfgExportError": cambiumJSONCfgExportError,
       "cambiumJSONCfgExportLink": cambiumJSONCfgExportLink,
       "cambiumFullCfgRestore": cambiumFullCfgRestore,
       "cambiumFullCfgRestoreStatus": cambiumFullCfgRestoreStatus,
       "cambiumFullCfgRestoreError": cambiumFullCfgRestoreError,
       "cambiumFullCfgBackUp": cambiumFullCfgBackUp,
       "cambiumFullCfgBackUpStatus": cambiumFullCfgBackUpStatus,
       "cambiumFullCfgBackUpError": cambiumFullCfgBackUpError,
       "cambiumFullCfgBackUpLink": cambiumFullCfgBackUpLink,
       "cambiumIDM": cambiumIDM,
       "cambiumIDMMode": cambiumIDMMode,
       "cambiumIDMTime": cambiumIDMTime,
       "cambiumIDMEnable": cambiumIDMEnable,
       "cambiumIDMResultsTable": cambiumIDMResultsTable,
       "cambiumIDMResultsEntry": cambiumIDMResultsEntry,
       "idmDeviceListCycle": idmDeviceListCycle,
       "idmDeviceListMAC": idmDeviceListMAC,
       "idmDeviceListLCombRSSI": idmDeviceListLCombRSSI,
       "idmDeviceListLRate": idmDeviceListLRate,
       "idmDeviceListMaxRate": idmDeviceListMaxRate,
       "idmDeviceListPcktsNum": idmDeviceListPcktsNum,
       "idmDeviceListCRCCombRSSI": idmDeviceListCRCCombRSSI,
       "idmDeviceListCRCCh0RSSI": idmDeviceListCRCCh0RSSI,
       "idmDeviceListCRCCh1RSSI": idmDeviceListCRCCh1RSSI,
       "idmDeviceListCRCPcktsNum": idmDeviceListCRCPcktsNum,
       "idmDeviceListPRQCombRSSI": idmDeviceListPRQCombRSSI,
       "idmDeviceListPRQCh0RSSI": idmDeviceListPRQCh0RSSI,
       "idmDeviceListPRQCh1RSSI": idmDeviceListPRQCh1RSSI,
       "idmDeviceListPRQPcktsNum": idmDeviceListPRQPcktsNum,
       "cambiumIDMSumMAC": cambiumIDMSumMAC,
       "cambiumIDMSumLCombRSSI": cambiumIDMSumLCombRSSI,
       "cambiumIDMSumLRate": cambiumIDMSumLRate,
       "cambiumIDMSumMaxRate": cambiumIDMSumMaxRate,
       "cambiumIDMSumPcktsNum": cambiumIDMSumPcktsNum,
       "cambiumIDMSumCRCCombRSSI": cambiumIDMSumCRCCombRSSI,
       "cambiumIDMSumCRCCh0RSSI": cambiumIDMSumCRCCh0RSSI,
       "cambiumIDMSumCRCCh1RSSI": cambiumIDMSumCRCCh1RSSI,
       "cambiumIDMSumCRCPcktsNum": cambiumIDMSumCRCPcktsNum,
       "cambiumIDMSumPRQCombRSSI": cambiumIDMSumPRQCombRSSI,
       "cambiumIDMSumPRQCh0RSSI": cambiumIDMSumPRQCh0RSSI,
       "cambiumIDMSumPRQCh1RSSI": cambiumIDMSumPRQCh1RSSI,
       "cambiumIDMSumPRQPcktsNum": cambiumIDMSumPRQPcktsNum,
       "cambiumIDMSummaryTable": cambiumIDMSummaryTable,
       "cambiumIDMSummaryEntry": cambiumIDMSummaryEntry,
       "idmSummaryIntMAC": idmSummaryIntMAC,
       "idmSummaryIntCombRSSI": idmSummaryIntCombRSSI,
       "idmSummaryIntCh0RSSI": idmSummaryIntCh0RSSI,
       "idmSummaryIntCh1RSSI": idmSummaryIntCh1RSSI,
       "idmSummaryIntSSID": idmSummaryIntSSID,
       "cambiumACSCfg": cambiumACSCfg,
       "acsEnable": acsEnable,
       "acsScanMinDwellTime": acsScanMinDwellTime,
       "acsScanMaxDwellTime": acsScanMaxDwellTime,
       "acsControl": acsControl}
)
