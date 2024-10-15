# SNMP MIB module (MIMOSA-NETWORKS-BFIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIMOSA-NETWORKS-BFIVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:04 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mimosaConformanceGroup,
 mimosaWireless) = mibBuilder.importSymbols(
    "MIMOSA-NETWORKS-BASE-MIB",
    "mimosaConformanceGroup",
    "mimosaWireless")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mimosaB5Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 1)
)
mimosaB5Module.setRevisions(
        ("2016-10-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DecimalOne(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class DecimalTwo(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class DecimalFive(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-5"


# MIB Managed Objects in the order of their OIDs

_MimosaGeneral_ObjectIdentity = ObjectIdentity
mimosaGeneral = _MimosaGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1)
)


class _MimosaDeviceName_Type(DisplayString):
    """Custom type mimosaDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaDeviceName_Type.__name__ = "DisplayString"
_MimosaDeviceName_Object = MibScalar
mimosaDeviceName = _MimosaDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 1),
    _MimosaDeviceName_Type()
)
mimosaDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaDeviceName.setStatus("current")


class _MimosaSerialNumber_Type(DisplayString):
    """Custom type mimosaSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaSerialNumber_Type.__name__ = "DisplayString"
_MimosaSerialNumber_Object = MibScalar
mimosaSerialNumber = _MimosaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 2),
    _MimosaSerialNumber_Type()
)
mimosaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaSerialNumber.setStatus("current")


class _MimosaFirmwareVersion_Type(DisplayString):
    """Custom type mimosaFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaFirmwareVersion_Type.__name__ = "DisplayString"
_MimosaFirmwareVersion_Object = MibScalar
mimosaFirmwareVersion = _MimosaFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 3),
    _MimosaFirmwareVersion_Type()
)
mimosaFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaFirmwareVersion.setStatus("current")


class _MimosaFirmwareBuildDate_Type(DisplayString):
    """Custom type mimosaFirmwareBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaFirmwareBuildDate_Type.__name__ = "DisplayString"
_MimosaFirmwareBuildDate_Object = MibScalar
mimosaFirmwareBuildDate = _MimosaFirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 4),
    _MimosaFirmwareBuildDate_Type()
)
mimosaFirmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaFirmwareBuildDate.setStatus("current")


class _MimosaLastRebootTime_Type(DisplayString):
    """Custom type mimosaLastRebootTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaLastRebootTime_Type.__name__ = "DisplayString"
_MimosaLastRebootTime_Object = MibScalar
mimosaLastRebootTime = _MimosaLastRebootTime_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 5),
    _MimosaLastRebootTime_Type()
)
mimosaLastRebootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLastRebootTime.setStatus("current")


class _MimosaUnlockCode_Type(DisplayString):
    """Custom type mimosaUnlockCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaUnlockCode_Type.__name__ = "DisplayString"
_MimosaUnlockCode_Object = MibScalar
mimosaUnlockCode = _MimosaUnlockCode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 6),
    _MimosaUnlockCode_Type()
)
mimosaUnlockCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaUnlockCode.setStatus("current")


class _MimosaLEDBrightness_Type(Integer32):
    """Custom type mimosaLEDBrightness based on Integer32"""
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
        *(("auto", 1),
          ("high", 4),
          ("low", 2),
          ("medium", 3))
    )


_MimosaLEDBrightness_Type.__name__ = "Integer32"
_MimosaLEDBrightness_Object = MibScalar
mimosaLEDBrightness = _MimosaLEDBrightness_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 7),
    _MimosaLEDBrightness_Type()
)
mimosaLEDBrightness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLEDBrightness.setStatus("current")
_MimosaInternalTemp_Type = DecimalOne
_MimosaInternalTemp_Object = MibScalar
mimosaInternalTemp = _MimosaInternalTemp_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 8),
    _MimosaInternalTemp_Type()
)
mimosaInternalTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaInternalTemp.setStatus("current")
if mibBuilder.loadTexts:
    mimosaInternalTemp.setUnits("C")


class _MimosaRegulatoryDomain_Type(DisplayString):
    """Custom type mimosaRegulatoryDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaRegulatoryDomain_Type.__name__ = "DisplayString"
_MimosaRegulatoryDomain_Object = MibScalar
mimosaRegulatoryDomain = _MimosaRegulatoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 9),
    _MimosaRegulatoryDomain_Type()
)
mimosaRegulatoryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRegulatoryDomain.setStatus("current")
_MimosaLocInfo_ObjectIdentity = ObjectIdentity
mimosaLocInfo = _MimosaLocInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2)
)
_MimosaLongitude_Type = DecimalFive
_MimosaLongitude_Object = MibScalar
mimosaLongitude = _MimosaLongitude_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 1),
    _MimosaLongitude_Type()
)
mimosaLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLongitude.setStatus("current")
_MimosaLatitude_Type = DecimalFive
_MimosaLatitude_Object = MibScalar
mimosaLatitude = _MimosaLatitude_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 2),
    _MimosaLatitude_Type()
)
mimosaLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLatitude.setStatus("current")
_MimosaAltitude_Type = Integer32
_MimosaAltitude_Object = MibScalar
mimosaAltitude = _MimosaAltitude_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 3),
    _MimosaAltitude_Type()
)
mimosaAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaAltitude.setStatus("current")
if mibBuilder.loadTexts:
    mimosaAltitude.setUnits("meters")
_MimosaSatelliteSNR_Type = DecimalOne
_MimosaSatelliteSNR_Object = MibScalar
mimosaSatelliteSNR = _MimosaSatelliteSNR_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 4),
    _MimosaSatelliteSNR_Type()
)
mimosaSatelliteSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaSatelliteSNR.setStatus("current")
if mibBuilder.loadTexts:
    mimosaSatelliteSNR.setUnits("dB")


class _MimosaSatelliteStrength_Type(Integer32):
    """Custom type mimosaSatelliteStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_MimosaSatelliteStrength_Type.__name__ = "Integer32"
_MimosaSatelliteStrength_Object = MibScalar
mimosaSatelliteStrength = _MimosaSatelliteStrength_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 5),
    _MimosaSatelliteStrength_Type()
)
mimosaSatelliteStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaSatelliteStrength.setStatus("current")
_MimosaGPSSatellites_Type = Integer32
_MimosaGPSSatellites_Object = MibScalar
mimosaGPSSatellites = _MimosaGPSSatellites_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 6),
    _MimosaGPSSatellites_Type()
)
mimosaGPSSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaGPSSatellites.setStatus("current")
_MimosaGlonassSatellites_Type = Integer32
_MimosaGlonassSatellites_Object = MibScalar
mimosaGlonassSatellites = _MimosaGlonassSatellites_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 7),
    _MimosaGlonassSatellites_Type()
)
mimosaGlonassSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaGlonassSatellites.setStatus("current")
_MimosaClockAccuracy_Type = DecimalTwo
_MimosaClockAccuracy_Object = MibScalar
mimosaClockAccuracy = _MimosaClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 8),
    _MimosaClockAccuracy_Type()
)
mimosaClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaClockAccuracy.setStatus("current")
if mibBuilder.loadTexts:
    mimosaClockAccuracy.setUnits("PPB")
_MimosaWanInfo_ObjectIdentity = ObjectIdentity
mimosaWanInfo = _MimosaWanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3)
)


class _MimosaWanSsid_Type(DisplayString):
    """Custom type mimosaWanSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaWanSsid_Type.__name__ = "DisplayString"
_MimosaWanSsid_Object = MibScalar
mimosaWanSsid = _MimosaWanSsid_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 1),
    _MimosaWanSsid_Type()
)
mimosaWanSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaWanSsid.setStatus("current")
_MimosaWanMac_Type = PhysAddress
_MimosaWanMac_Object = MibScalar
mimosaWanMac = _MimosaWanMac_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 2),
    _MimosaWanMac_Type()
)
mimosaWanMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaWanMac.setStatus("current")


class _MimosaWanStatus_Type(Integer32):
    """Custom type mimosaWanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_MimosaWanStatus_Type.__name__ = "Integer32"
_MimosaWanStatus_Object = MibScalar
mimosaWanStatus = _MimosaWanStatus_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 3),
    _MimosaWanStatus_Type()
)
mimosaWanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaWanStatus.setStatus("current")
_MimosaWanUpTime_Type = TimeTicks
_MimosaWanUpTime_Object = MibScalar
mimosaWanUpTime = _MimosaWanUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 4),
    _MimosaWanUpTime_Type()
)
mimosaWanUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaWanUpTime.setStatus("current")
_MimosaTdmaInfo_ObjectIdentity = ObjectIdentity
mimosaTdmaInfo = _MimosaTdmaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4)
)


class _MimosaWirelessMode_Type(Integer32):
    """Custom type mimosaWirelessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessPoint", 1),
          ("station", 2))
    )


_MimosaWirelessMode_Type.__name__ = "Integer32"
_MimosaWirelessMode_Object = MibScalar
mimosaWirelessMode = _MimosaWirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 1),
    _MimosaWirelessMode_Type()
)
mimosaWirelessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaWirelessMode.setStatus("current")


class _MimosaWirelessProtocol_Type(Integer32):
    """Custom type mimosaWirelessProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csma", 2),
          ("tdma", 1))
    )


_MimosaWirelessProtocol_Type.__name__ = "Integer32"
_MimosaWirelessProtocol_Object = MibScalar
mimosaWirelessProtocol = _MimosaWirelessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 2),
    _MimosaWirelessProtocol_Type()
)
mimosaWirelessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaWirelessProtocol.setStatus("current")


class _MimosaTDMAMode_Type(Integer32):
    """Custom type mimosaTDMAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_MimosaTDMAMode_Type.__name__ = "Integer32"
_MimosaTDMAMode_Object = MibScalar
mimosaTDMAMode = _MimosaTDMAMode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 3),
    _MimosaTDMAMode_Type()
)
mimosaTDMAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTDMAMode.setStatus("current")
_MimosaTDMAWindow_Type = Integer32
_MimosaTDMAWindow_Object = MibScalar
mimosaTDMAWindow = _MimosaTDMAWindow_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 4),
    _MimosaTDMAWindow_Type()
)
mimosaTDMAWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTDMAWindow.setStatus("current")
if mibBuilder.loadTexts:
    mimosaTDMAWindow.setUnits("ms")


class _MimosaTrafficSplit_Type(Integer32):
    """Custom type mimosaTrafficSplit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 2),
          ("auto", 3),
          ("symmetric", 1))
    )


_MimosaTrafficSplit_Type.__name__ = "Integer32"
_MimosaTrafficSplit_Object = MibScalar
mimosaTrafficSplit = _MimosaTrafficSplit_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 5),
    _MimosaTrafficSplit_Type()
)
mimosaTrafficSplit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTrafficSplit.setStatus("current")
_MimosaMgmtInfo_ObjectIdentity = ObjectIdentity
mimosaMgmtInfo = _MimosaMgmtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5)
)


class _MimosaNetworkMode_Type(Integer32):
    """Custom type mimosaNetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_MimosaNetworkMode_Type.__name__ = "Integer32"
_MimosaNetworkMode_Object = MibScalar
mimosaNetworkMode = _MimosaNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 1),
    _MimosaNetworkMode_Type()
)
mimosaNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaNetworkMode.setStatus("current")


class _MimosaRecoverySsid_Type(DisplayString):
    """Custom type mimosaRecoverySsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MimosaRecoverySsid_Type.__name__ = "DisplayString"
_MimosaRecoverySsid_Object = MibScalar
mimosaRecoverySsid = _MimosaRecoverySsid_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 2),
    _MimosaRecoverySsid_Type()
)
mimosaRecoverySsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRecoverySsid.setStatus("current")


class _MimosaLocalSsid_Type(DisplayString):
    """Custom type mimosaLocalSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MimosaLocalSsid_Type.__name__ = "DisplayString"
_MimosaLocalSsid_Object = MibScalar
mimosaLocalSsid = _MimosaLocalSsid_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 3),
    _MimosaLocalSsid_Type()
)
mimosaLocalSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLocalSsid.setStatus("current")
_MimosaLocalChannel_Type = Integer32
_MimosaLocalChannel_Object = MibScalar
mimosaLocalChannel = _MimosaLocalChannel_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 4),
    _MimosaLocalChannel_Type()
)
mimosaLocalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLocalChannel.setStatus("current")
_MimosaConsoleTimeout_Type = Integer32
_MimosaConsoleTimeout_Object = MibScalar
mimosaConsoleTimeout = _MimosaConsoleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 5),
    _MimosaConsoleTimeout_Type()
)
mimosaConsoleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaConsoleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    mimosaConsoleTimeout.setUnits("min")
_MimosaMaxClients_Type = Integer32
_MimosaMaxClients_Object = MibScalar
mimosaMaxClients = _MimosaMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 6),
    _MimosaMaxClients_Type()
)
mimosaMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaMaxClients.setStatus("current")
_MimosaLocalMac_Type = PhysAddress
_MimosaLocalMac_Object = MibScalar
mimosaLocalMac = _MimosaLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 7),
    _MimosaLocalMac_Type()
)
mimosaLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLocalMac.setStatus("current")
_MimosaLocalIpAddr_Type = IpAddress
_MimosaLocalIpAddr_Object = MibScalar
mimosaLocalIpAddr = _MimosaLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 8),
    _MimosaLocalIpAddr_Type()
)
mimosaLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLocalIpAddr.setStatus("current")
_MimosaLocalNetMask_Type = IpAddress
_MimosaLocalNetMask_Object = MibScalar
mimosaLocalNetMask = _MimosaLocalNetMask_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 9),
    _MimosaLocalNetMask_Type()
)
mimosaLocalNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLocalNetMask.setStatus("current")
_MimosaLocalGateway_Type = IpAddress
_MimosaLocalGateway_Object = MibScalar
mimosaLocalGateway = _MimosaLocalGateway_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 10),
    _MimosaLocalGateway_Type()
)
mimosaLocalGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaLocalGateway.setStatus("current")


class _MimosaFlowControl_Type(Integer32):
    """Custom type mimosaFlowControl based on Integer32"""
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


_MimosaFlowControl_Type.__name__ = "Integer32"
_MimosaFlowControl_Object = MibScalar
mimosaFlowControl = _MimosaFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 11),
    _MimosaFlowControl_Type()
)
mimosaFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaFlowControl.setStatus("current")
_MimosaRfInfo_ObjectIdentity = ObjectIdentity
mimosaRfInfo = _MimosaRfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6)
)
_MimosaChainTable_Object = MibTable
mimosaChainTable = _MimosaChainTable_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mimosaChainTable.setStatus("current")
_MimosaChainEntry_Object = MibTableRow
mimosaChainEntry = _MimosaChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1)
)
mimosaChainEntry.setIndexNames(
    (0, "MIMOSA-NETWORKS-BFIVE-MIB", "mimosaChain"),
)
if mibBuilder.loadTexts:
    mimosaChainEntry.setStatus("current")


class _MimosaChain_Type(Integer32):
    """Custom type mimosaChain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MimosaChain_Type.__name__ = "Integer32"
_MimosaChain_Object = MibTableColumn
mimosaChain = _MimosaChain_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 1),
    _MimosaChain_Type()
)
mimosaChain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mimosaChain.setStatus("current")
_MimosaTxPower_Type = Integer32
_MimosaTxPower_Object = MibTableColumn
mimosaTxPower = _MimosaTxPower_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 2),
    _MimosaTxPower_Type()
)
mimosaTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTxPower.setStatus("current")
if mibBuilder.loadTexts:
    mimosaTxPower.setUnits("dBm")
_MimosaRxPower_Type = Integer32
_MimosaRxPower_Object = MibTableColumn
mimosaRxPower = _MimosaRxPower_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 3),
    _MimosaRxPower_Type()
)
mimosaRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRxPower.setStatus("current")
if mibBuilder.loadTexts:
    mimosaRxPower.setUnits("dBm")
_MimosaRxNoise_Type = Integer32
_MimosaRxNoise_Object = MibTableColumn
mimosaRxNoise = _MimosaRxNoise_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 4),
    _MimosaRxNoise_Type()
)
mimosaRxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRxNoise.setStatus("current")
if mibBuilder.loadTexts:
    mimosaRxNoise.setUnits("dBm")
_MimosaSNR_Type = Integer32
_MimosaSNR_Object = MibTableColumn
mimosaSNR = _MimosaSNR_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 5),
    _MimosaSNR_Type()
)
mimosaSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaSNR.setStatus("current")
if mibBuilder.loadTexts:
    mimosaSNR.setUnits("dB")
_MimosaCenterFreq_Type = Integer32
_MimosaCenterFreq_Object = MibTableColumn
mimosaCenterFreq = _MimosaCenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 6),
    _MimosaCenterFreq_Type()
)
mimosaCenterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    mimosaCenterFreq.setUnits("MHz")


class _MimosaPolarization_Type(Integer32):
    """Custom type mimosaPolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 1),
          ("vertical", 2))
    )


_MimosaPolarization_Type.__name__ = "Integer32"
_MimosaPolarization_Object = MibTableColumn
mimosaPolarization = _MimosaPolarization_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 7),
    _MimosaPolarization_Type()
)
mimosaPolarization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPolarization.setStatus("current")
_MimosaStreamTable_Object = MibTable
mimosaStreamTable = _MimosaStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    mimosaStreamTable.setStatus("current")
_MimosaStreamEntry_Object = MibTableRow
mimosaStreamEntry = _MimosaStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1)
)
mimosaStreamEntry.setIndexNames(
    (0, "MIMOSA-NETWORKS-BFIVE-MIB", "mimosaStream"),
)
if mibBuilder.loadTexts:
    mimosaStreamEntry.setStatus("current")


class _MimosaStream_Type(Integer32):
    """Custom type mimosaStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MimosaStream_Type.__name__ = "Integer32"
_MimosaStream_Object = MibTableColumn
mimosaStream = _MimosaStream_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 1),
    _MimosaStream_Type()
)
mimosaStream.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mimosaStream.setStatus("current")
_MimosaTxPhy_Type = Integer32
_MimosaTxPhy_Object = MibTableColumn
mimosaTxPhy = _MimosaTxPhy_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 2),
    _MimosaTxPhy_Type()
)
mimosaTxPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTxPhy.setStatus("current")
if mibBuilder.loadTexts:
    mimosaTxPhy.setUnits("Mbps")
_MimosaTxMCS_Type = Integer32
_MimosaTxMCS_Object = MibTableColumn
mimosaTxMCS = _MimosaTxMCS_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 3),
    _MimosaTxMCS_Type()
)
mimosaTxMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTxMCS.setStatus("current")
_MimosaTxWidth_Type = Integer32
_MimosaTxWidth_Object = MibTableColumn
mimosaTxWidth = _MimosaTxWidth_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 4),
    _MimosaTxWidth_Type()
)
mimosaTxWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTxWidth.setStatus("current")
if mibBuilder.loadTexts:
    mimosaTxWidth.setUnits("MHz")
_MimosaRxPhy_Type = Integer32
_MimosaRxPhy_Object = MibTableColumn
mimosaRxPhy = _MimosaRxPhy_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 5),
    _MimosaRxPhy_Type()
)
mimosaRxPhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRxPhy.setStatus("current")
if mibBuilder.loadTexts:
    mimosaRxPhy.setUnits("Mbps")
_MimosaRxMCS_Type = Integer32
_MimosaRxMCS_Object = MibTableColumn
mimosaRxMCS = _MimosaRxMCS_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 6),
    _MimosaRxMCS_Type()
)
mimosaRxMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRxMCS.setStatus("current")
_MimosaRxWidth_Type = Integer32
_MimosaRxWidth_Object = MibTableColumn
mimosaRxWidth = _MimosaRxWidth_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 7),
    _MimosaRxWidth_Type()
)
mimosaRxWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRxWidth.setStatus("current")
if mibBuilder.loadTexts:
    mimosaRxWidth.setUnits("MHz")
_MimosaRxEVM_Type = Integer32
_MimosaRxEVM_Object = MibTableColumn
mimosaRxEVM = _MimosaRxEVM_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 8),
    _MimosaRxEVM_Type()
)
mimosaRxEVM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRxEVM.setStatus("current")
if mibBuilder.loadTexts:
    mimosaRxEVM.setUnits("dB")
_MimosaChannelTable_Object = MibTable
mimosaChannelTable = _MimosaChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    mimosaChannelTable.setStatus("current")
_MimosaChannelEntry_Object = MibTableRow
mimosaChannelEntry = _MimosaChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1)
)
mimosaChannelEntry.setIndexNames(
    (0, "MIMOSA-NETWORKS-BFIVE-MIB", "mimosaChannel"),
)
if mibBuilder.loadTexts:
    mimosaChannelEntry.setStatus("current")


class _MimosaChannel_Type(Integer32):
    """Custom type mimosaChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MimosaChannel_Type.__name__ = "Integer32"
_MimosaChannel_Object = MibTableColumn
mimosaChannel = _MimosaChannel_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 1),
    _MimosaChannel_Type()
)
mimosaChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mimosaChannel.setStatus("current")


class _MimosaChannelMode_Type(Integer32):
    """Custom type mimosaChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("receive", 2),
          ("transmit", 1))
    )


_MimosaChannelMode_Type.__name__ = "Integer32"
_MimosaChannelMode_Object = MibTableColumn
mimosaChannelMode = _MimosaChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 2),
    _MimosaChannelMode_Type()
)
mimosaChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaChannelMode.setStatus("current")
_MimosaChannelWidth_Type = Integer32
_MimosaChannelWidth_Object = MibTableColumn
mimosaChannelWidth = _MimosaChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 3),
    _MimosaChannelWidth_Type()
)
mimosaChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    mimosaChannelWidth.setUnits("MHz")
_MimosaChannelTxPower_Type = Integer32
_MimosaChannelTxPower_Object = MibTableColumn
mimosaChannelTxPower = _MimosaChannelTxPower_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 4),
    _MimosaChannelTxPower_Type()
)
mimosaChannelTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaChannelTxPower.setStatus("current")
if mibBuilder.loadTexts:
    mimosaChannelTxPower.setUnits("dBm")
_MimosaChannelCenterFreq_Type = Integer32
_MimosaChannelCenterFreq_Object = MibTableColumn
mimosaChannelCenterFreq = _MimosaChannelCenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 5),
    _MimosaChannelCenterFreq_Type()
)
mimosaChannelCenterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaChannelCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    mimosaChannelCenterFreq.setUnits("MHz")
_MimosaAntennaGain_Type = Integer32
_MimosaAntennaGain_Object = MibScalar
mimosaAntennaGain = _MimosaAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 4),
    _MimosaAntennaGain_Type()
)
mimosaAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaAntennaGain.setStatus("current")
if mibBuilder.loadTexts:
    mimosaAntennaGain.setUnits("dBi")
_MimosaTotalTxPower_Type = DecimalOne
_MimosaTotalTxPower_Object = MibScalar
mimosaTotalTxPower = _MimosaTotalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 5),
    _MimosaTotalTxPower_Type()
)
mimosaTotalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTotalTxPower.setStatus("current")
if mibBuilder.loadTexts:
    mimosaTotalTxPower.setUnits("dBm")
_MimosaTotalRxPower_Type = DecimalOne
_MimosaTotalRxPower_Object = MibScalar
mimosaTotalRxPower = _MimosaTotalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 6),
    _MimosaTotalRxPower_Type()
)
mimosaTotalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTotalRxPower.setStatus("current")
if mibBuilder.loadTexts:
    mimosaTotalRxPower.setUnits("dBm")
_MimosaTargetSignalStrength_Type = Integer32
_MimosaTargetSignalStrength_Object = MibScalar
mimosaTargetSignalStrength = _MimosaTargetSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 7),
    _MimosaTargetSignalStrength_Type()
)
mimosaTargetSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaTargetSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    mimosaTargetSignalStrength.setUnits("dB")
_MimosaPerfInfo_ObjectIdentity = ObjectIdentity
mimosaPerfInfo = _MimosaPerfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7)
)
_MimosaPhyTxRate_Type = DecimalTwo
_MimosaPhyTxRate_Object = MibScalar
mimosaPhyTxRate = _MimosaPhyTxRate_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 1),
    _MimosaPhyTxRate_Type()
)
mimosaPhyTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPhyTxRate.setStatus("current")
if mibBuilder.loadTexts:
    mimosaPhyTxRate.setUnits("kbps")
_MimosaPhyRxRate_Type = DecimalTwo
_MimosaPhyRxRate_Object = MibScalar
mimosaPhyRxRate = _MimosaPhyRxRate_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 2),
    _MimosaPhyRxRate_Type()
)
mimosaPhyRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPhyRxRate.setStatus("current")
if mibBuilder.loadTexts:
    mimosaPhyRxRate.setUnits("kbps")
_MimosaPerTxRate_Type = DecimalTwo
_MimosaPerTxRate_Object = MibScalar
mimosaPerTxRate = _MimosaPerTxRate_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 3),
    _MimosaPerTxRate_Type()
)
mimosaPerTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPerTxRate.setStatus("current")
if mibBuilder.loadTexts:
    mimosaPerTxRate.setUnits("%")
_MimosaPerRxRate_Type = DecimalTwo
_MimosaPerRxRate_Object = MibScalar
mimosaPerRxRate = _MimosaPerRxRate_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 4),
    _MimosaPerRxRate_Type()
)
mimosaPerRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPerRxRate.setStatus("current")
_MimosaServices_ObjectIdentity = ObjectIdentity
mimosaServices = _MimosaServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8)
)


class _MimosaHttpsEnabled_Type(Integer32):
    """Custom type mimosaHttpsEnabled based on Integer32"""
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


_MimosaHttpsEnabled_Type.__name__ = "Integer32"
_MimosaHttpsEnabled_Object = MibScalar
mimosaHttpsEnabled = _MimosaHttpsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 1),
    _MimosaHttpsEnabled_Type()
)
mimosaHttpsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaHttpsEnabled.setStatus("current")


class _MimosaMgmtVlanEnabled_Type(Integer32):
    """Custom type mimosaMgmtVlanEnabled based on Integer32"""
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


_MimosaMgmtVlanEnabled_Type.__name__ = "Integer32"
_MimosaMgmtVlanEnabled_Object = MibScalar
mimosaMgmtVlanEnabled = _MimosaMgmtVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 2),
    _MimosaMgmtVlanEnabled_Type()
)
mimosaMgmtVlanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaMgmtVlanEnabled.setStatus("current")


class _MimosaMgmtCloudEnabled_Type(Integer32):
    """Custom type mimosaMgmtCloudEnabled based on Integer32"""
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


_MimosaMgmtCloudEnabled_Type.__name__ = "Integer32"
_MimosaMgmtCloudEnabled_Object = MibScalar
mimosaMgmtCloudEnabled = _MimosaMgmtCloudEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 3),
    _MimosaMgmtCloudEnabled_Type()
)
mimosaMgmtCloudEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaMgmtCloudEnabled.setStatus("current")


class _MimosaRestMgmtEnabled_Type(Integer32):
    """Custom type mimosaRestMgmtEnabled based on Integer32"""
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


_MimosaRestMgmtEnabled_Type.__name__ = "Integer32"
_MimosaRestMgmtEnabled_Object = MibScalar
mimosaRestMgmtEnabled = _MimosaRestMgmtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 4),
    _MimosaRestMgmtEnabled_Type()
)
mimosaRestMgmtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaRestMgmtEnabled.setStatus("current")


class _MimosaPingWatchdogEnabled_Type(Integer32):
    """Custom type mimosaPingWatchdogEnabled based on Integer32"""
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


_MimosaPingWatchdogEnabled_Type.__name__ = "Integer32"
_MimosaPingWatchdogEnabled_Object = MibScalar
mimosaPingWatchdogEnabled = _MimosaPingWatchdogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 5),
    _MimosaPingWatchdogEnabled_Type()
)
mimosaPingWatchdogEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPingWatchdogEnabled.setStatus("current")


class _MimosaSyslogEnabled_Type(Integer32):
    """Custom type mimosaSyslogEnabled based on Integer32"""
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


_MimosaSyslogEnabled_Type.__name__ = "Integer32"
_MimosaSyslogEnabled_Object = MibScalar
mimosaSyslogEnabled = _MimosaSyslogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 6),
    _MimosaSyslogEnabled_Type()
)
mimosaSyslogEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaSyslogEnabled.setStatus("current")


class _MimosaNtpMode_Type(Integer32):
    """Custom type mimosaNtpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 1),
          ("standard", 2))
    )


_MimosaNtpMode_Type.__name__ = "Integer32"
_MimosaNtpMode_Object = MibScalar
mimosaNtpMode = _MimosaNtpMode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 7),
    _MimosaNtpMode_Type()
)
mimosaNtpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaNtpMode.setStatus("current")


class _MimosaNtpServer_Type(DisplayString):
    """Custom type mimosaNtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MimosaNtpServer_Type.__name__ = "DisplayString"
_MimosaNtpServer_Object = MibScalar
mimosaNtpServer = _MimosaNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 8),
    _MimosaNtpServer_Type()
)
mimosaNtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaNtpServer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIMOSA-NETWORKS-BFIVE-MIB",
    **{"DecimalOne": DecimalOne,
       "DecimalTwo": DecimalTwo,
       "DecimalFive": DecimalFive,
       "mimosaGeneral": mimosaGeneral,
       "mimosaDeviceName": mimosaDeviceName,
       "mimosaSerialNumber": mimosaSerialNumber,
       "mimosaFirmwareVersion": mimosaFirmwareVersion,
       "mimosaFirmwareBuildDate": mimosaFirmwareBuildDate,
       "mimosaLastRebootTime": mimosaLastRebootTime,
       "mimosaUnlockCode": mimosaUnlockCode,
       "mimosaLEDBrightness": mimosaLEDBrightness,
       "mimosaInternalTemp": mimosaInternalTemp,
       "mimosaRegulatoryDomain": mimosaRegulatoryDomain,
       "mimosaLocInfo": mimosaLocInfo,
       "mimosaLongitude": mimosaLongitude,
       "mimosaLatitude": mimosaLatitude,
       "mimosaAltitude": mimosaAltitude,
       "mimosaSatelliteSNR": mimosaSatelliteSNR,
       "mimosaSatelliteStrength": mimosaSatelliteStrength,
       "mimosaGPSSatellites": mimosaGPSSatellites,
       "mimosaGlonassSatellites": mimosaGlonassSatellites,
       "mimosaClockAccuracy": mimosaClockAccuracy,
       "mimosaWanInfo": mimosaWanInfo,
       "mimosaWanSsid": mimosaWanSsid,
       "mimosaWanMac": mimosaWanMac,
       "mimosaWanStatus": mimosaWanStatus,
       "mimosaWanUpTime": mimosaWanUpTime,
       "mimosaTdmaInfo": mimosaTdmaInfo,
       "mimosaWirelessMode": mimosaWirelessMode,
       "mimosaWirelessProtocol": mimosaWirelessProtocol,
       "mimosaTDMAMode": mimosaTDMAMode,
       "mimosaTDMAWindow": mimosaTDMAWindow,
       "mimosaTrafficSplit": mimosaTrafficSplit,
       "mimosaMgmtInfo": mimosaMgmtInfo,
       "mimosaNetworkMode": mimosaNetworkMode,
       "mimosaRecoverySsid": mimosaRecoverySsid,
       "mimosaLocalSsid": mimosaLocalSsid,
       "mimosaLocalChannel": mimosaLocalChannel,
       "mimosaConsoleTimeout": mimosaConsoleTimeout,
       "mimosaMaxClients": mimosaMaxClients,
       "mimosaLocalMac": mimosaLocalMac,
       "mimosaLocalIpAddr": mimosaLocalIpAddr,
       "mimosaLocalNetMask": mimosaLocalNetMask,
       "mimosaLocalGateway": mimosaLocalGateway,
       "mimosaFlowControl": mimosaFlowControl,
       "mimosaRfInfo": mimosaRfInfo,
       "mimosaChainTable": mimosaChainTable,
       "mimosaChainEntry": mimosaChainEntry,
       "mimosaChain": mimosaChain,
       "mimosaTxPower": mimosaTxPower,
       "mimosaRxPower": mimosaRxPower,
       "mimosaRxNoise": mimosaRxNoise,
       "mimosaSNR": mimosaSNR,
       "mimosaCenterFreq": mimosaCenterFreq,
       "mimosaPolarization": mimosaPolarization,
       "mimosaStreamTable": mimosaStreamTable,
       "mimosaStreamEntry": mimosaStreamEntry,
       "mimosaStream": mimosaStream,
       "mimosaTxPhy": mimosaTxPhy,
       "mimosaTxMCS": mimosaTxMCS,
       "mimosaTxWidth": mimosaTxWidth,
       "mimosaRxPhy": mimosaRxPhy,
       "mimosaRxMCS": mimosaRxMCS,
       "mimosaRxWidth": mimosaRxWidth,
       "mimosaRxEVM": mimosaRxEVM,
       "mimosaChannelTable": mimosaChannelTable,
       "mimosaChannelEntry": mimosaChannelEntry,
       "mimosaChannel": mimosaChannel,
       "mimosaChannelMode": mimosaChannelMode,
       "mimosaChannelWidth": mimosaChannelWidth,
       "mimosaChannelTxPower": mimosaChannelTxPower,
       "mimosaChannelCenterFreq": mimosaChannelCenterFreq,
       "mimosaAntennaGain": mimosaAntennaGain,
       "mimosaTotalTxPower": mimosaTotalTxPower,
       "mimosaTotalRxPower": mimosaTotalRxPower,
       "mimosaTargetSignalStrength": mimosaTargetSignalStrength,
       "mimosaPerfInfo": mimosaPerfInfo,
       "mimosaPhyTxRate": mimosaPhyTxRate,
       "mimosaPhyRxRate": mimosaPhyRxRate,
       "mimosaPerTxRate": mimosaPerTxRate,
       "mimosaPerRxRate": mimosaPerRxRate,
       "mimosaServices": mimosaServices,
       "mimosaHttpsEnabled": mimosaHttpsEnabled,
       "mimosaMgmtVlanEnabled": mimosaMgmtVlanEnabled,
       "mimosaMgmtCloudEnabled": mimosaMgmtCloudEnabled,
       "mimosaRestMgmtEnabled": mimosaRestMgmtEnabled,
       "mimosaPingWatchdogEnabled": mimosaPingWatchdogEnabled,
       "mimosaSyslogEnabled": mimosaSyslogEnabled,
       "mimosaNtpMode": mimosaNtpMode,
       "mimosaNtpServer": mimosaNtpServer,
       "mimosaB5Module": mimosaB5Module}
)
