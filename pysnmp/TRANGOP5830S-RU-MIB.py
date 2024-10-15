# SNMP MIB module (TRANGOP5830S-RU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRANGOP5830S-RU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:21 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Trango_ObjectIdentity = ObjectIdentity
trango = _Trango_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454)
)
_Tbw_ObjectIdentity = ObjectIdentity
tbw = _Tbw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1)
)
_P5830sru_ObjectIdentity = ObjectIdentity
p5830sru = _P5830sru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24)
)
_Rusys_ObjectIdentity = ObjectIdentity
rusys = _Rusys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1)
)
_Ruversion_ObjectIdentity = ObjectIdentity
ruversion = _Ruversion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 1)
)


class _RuversionHW_Type(OctetString):
    """Custom type ruversionHW based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_RuversionHW_Type.__name__ = "OctetString"
_RuversionHW_Object = MibScalar
ruversionHW = _RuversionHW_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 1, 1),
    _RuversionHW_Type()
)
ruversionHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruversionHW.setStatus("mandatory")


class _RuversionFW_Type(DisplayString):
    """Custom type ruversionFW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RuversionFW_Type.__name__ = "DisplayString"
_RuversionFW_Object = MibScalar
ruversionFW = _RuversionFW_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 1, 2),
    _RuversionFW_Type()
)
ruversionFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruversionFW.setStatus("mandatory")


class _RuversionFPGA_Type(OctetString):
    """Custom type ruversionFPGA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RuversionFPGA_Type.__name__ = "OctetString"
_RuversionFPGA_Object = MibScalar
ruversionFPGA = _RuversionFPGA_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 1, 3),
    _RuversionFPGA_Type()
)
ruversionFPGA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruversionFPGA.setStatus("mandatory")


class _RuversionFWChecksum_Type(OctetString):
    """Custom type ruversionFWChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RuversionFWChecksum_Type.__name__ = "OctetString"
_RuversionFWChecksum_Object = MibScalar
ruversionFWChecksum = _RuversionFWChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 1, 4),
    _RuversionFWChecksum_Type()
)
ruversionFWChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruversionFWChecksum.setStatus("mandatory")


class _RuversionFPGAChecksum_Type(OctetString):
    """Custom type ruversionFPGAChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_RuversionFPGAChecksum_Type.__name__ = "OctetString"
_RuversionFPGAChecksum_Object = MibScalar
ruversionFPGAChecksum = _RuversionFPGAChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 1, 5),
    _RuversionFPGAChecksum_Type()
)
ruversionFPGAChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruversionFPGAChecksum.setStatus("mandatory")


class _RusysDeviceId_Type(OctetString):
    """Custom type rusysDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RusysDeviceId_Type.__name__ = "OctetString"
_RusysDeviceId_Object = MibScalar
rusysDeviceId = _RusysDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 2),
    _RusysDeviceId_Type()
)
rusysDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rusysDeviceId.setStatus("mandatory")


class _RusysDefOpMode_Type(Integer32):
    """Custom type rusysDefOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 16))
    )


_RusysDefOpMode_Type.__name__ = "Integer32"
_RusysDefOpMode_Object = MibScalar
rusysDefOpMode = _RusysDefOpMode_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 3),
    _RusysDefOpMode_Type()
)
rusysDefOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rusysDefOpMode.setStatus("mandatory")


class _RusysCurOpMode_Type(Integer32):
    """Custom type rusysCurOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 16))
    )


_RusysCurOpMode_Type.__name__ = "Integer32"
_RusysCurOpMode_Object = MibScalar
rusysCurOpMode = _RusysCurOpMode_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 4),
    _RusysCurOpMode_Type()
)
rusysCurOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rusysCurOpMode.setStatus("mandatory")


class _RusysActivateOpmode_Type(Integer32):
    """Custom type rusysActivateOpmode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 0))
    )


_RusysActivateOpmode_Type.__name__ = "Integer32"
_RusysActivateOpmode_Object = MibScalar
rusysActivateOpmode = _RusysActivateOpmode_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 5),
    _RusysActivateOpmode_Type()
)
rusysActivateOpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rusysActivateOpmode.setStatus("mandatory")


class _RusysReadCommStr_Type(DisplayString):
    """Custom type rusysReadCommStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RusysReadCommStr_Type.__name__ = "DisplayString"
_RusysReadCommStr_Object = MibScalar
rusysReadCommStr = _RusysReadCommStr_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 6),
    _RusysReadCommStr_Type()
)
rusysReadCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rusysReadCommStr.setStatus("mandatory")


class _RusysWriteCommStr_Type(DisplayString):
    """Custom type rusysWriteCommStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RusysWriteCommStr_Type.__name__ = "DisplayString"
_RusysWriteCommStr_Object = MibScalar
rusysWriteCommStr = _RusysWriteCommStr_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 7),
    _RusysWriteCommStr_Type()
)
rusysWriteCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rusysWriteCommStr.setStatus("mandatory")
_Ruswitches_ObjectIdentity = ObjectIdentity
ruswitches = _Ruswitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 8)
)


class _RuswitchesBlockBroadcastMulticast_Type(Integer32):
    """Custom type ruswitchesBlockBroadcastMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("passed", 0))
    )


_RuswitchesBlockBroadcastMulticast_Type.__name__ = "Integer32"
_RuswitchesBlockBroadcastMulticast_Object = MibScalar
ruswitchesBlockBroadcastMulticast = _RuswitchesBlockBroadcastMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 8, 1),
    _RuswitchesBlockBroadcastMulticast_Type()
)
ruswitchesBlockBroadcastMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruswitchesBlockBroadcastMulticast.setStatus("mandatory")


class _RuswitchesHTTPD_Type(Integer32):
    """Custom type ruswitchesHTTPD based on Integer32"""
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


_RuswitchesHTTPD_Type.__name__ = "Integer32"
_RuswitchesHTTPD_Object = MibScalar
ruswitchesHTTPD = _RuswitchesHTTPD_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 8, 5),
    _RuswitchesHTTPD_Type()
)
ruswitchesHTTPD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruswitchesHTTPD.setStatus("mandatory")


class _RuswitchesAutoScanMasterSignal_Type(Integer32):
    """Custom type ruswitchesAutoScanMasterSignal based on Integer32"""
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


_RuswitchesAutoScanMasterSignal_Type.__name__ = "Integer32"
_RuswitchesAutoScanMasterSignal_Object = MibScalar
ruswitchesAutoScanMasterSignal = _RuswitchesAutoScanMasterSignal_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 8, 6),
    _RuswitchesAutoScanMasterSignal_Type()
)
ruswitchesAutoScanMasterSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruswitchesAutoScanMasterSignal.setStatus("mandatory")
_Rutraffic_ObjectIdentity = ObjectIdentity
rutraffic = _Rutraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 9)
)
_RutrafficEthInOctets_Type = Counter32
_RutrafficEthInOctets_Object = MibScalar
rutrafficEthInOctets = _RutrafficEthInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 9, 1),
    _RutrafficEthInOctets_Type()
)
rutrafficEthInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rutrafficEthInOctets.setStatus("mandatory")
_RutrafficEthOutOctets_Type = Counter32
_RutrafficEthOutOctets_Object = MibScalar
rutrafficEthOutOctets = _RutrafficEthOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 9, 2),
    _RutrafficEthOutOctets_Type()
)
rutrafficEthOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rutrafficEthOutOctets.setStatus("mandatory")
_RutrafficRfInOctets_Type = Counter32
_RutrafficRfInOctets_Object = MibScalar
rutrafficRfInOctets = _RutrafficRfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 9, 3),
    _RutrafficRfInOctets_Type()
)
rutrafficRfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rutrafficRfInOctets.setStatus("mandatory")
_RutrafficRfOutOctets_Type = Counter32
_RutrafficRfOutOctets_Object = MibScalar
rutrafficRfOutOctets = _RutrafficRfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 9, 4),
    _RutrafficRfOutOctets_Type()
)
rutrafficRfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rutrafficRfOutOctets.setStatus("mandatory")


class _RusysTemperature_Type(Integer32):
    """Custom type rusysTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_RusysTemperature_Type.__name__ = "Integer32"
_RusysTemperature_Object = MibScalar
rusysTemperature = _RusysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 10),
    _RusysTemperature_Type()
)
rusysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rusysTemperature.setStatus("mandatory")


class _RusysUpdateFlashAndActivate_Type(Integer32):
    """Custom type rusysUpdateFlashAndActivate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RusysUpdateFlashAndActivate_Type.__name__ = "Integer32"
_RusysUpdateFlashAndActivate_Object = MibScalar
rusysUpdateFlashAndActivate = _RusysUpdateFlashAndActivate_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 11),
    _RusysUpdateFlashAndActivate_Type()
)
rusysUpdateFlashAndActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rusysUpdateFlashAndActivate.setStatus("mandatory")


class _RusysReboot_Type(Integer32):
    """Custom type rusysReboot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 0))
    )


_RusysReboot_Type.__name__ = "Integer32"
_RusysReboot_Object = MibScalar
rusysReboot = _RusysReboot_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 12),
    _RusysReboot_Type()
)
rusysReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rusysReboot.setStatus("mandatory")
_Ruipconfig_ObjectIdentity = ObjectIdentity
ruipconfig = _Ruipconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 13)
)
_RuipconfigIpAddress_Type = IpAddress
_RuipconfigIpAddress_Object = MibScalar
ruipconfigIpAddress = _RuipconfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 13, 1),
    _RuipconfigIpAddress_Type()
)
ruipconfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruipconfigIpAddress.setStatus("mandatory")
_RuipconfigSubnet_Type = IpAddress
_RuipconfigSubnet_Object = MibScalar
ruipconfigSubnet = _RuipconfigSubnet_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 13, 2),
    _RuipconfigSubnet_Type()
)
ruipconfigSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruipconfigSubnet.setStatus("mandatory")
_RuipconfigDefaultGateway_Type = IpAddress
_RuipconfigDefaultGateway_Object = MibScalar
ruipconfigDefaultGateway = _RuipconfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 1, 13, 3),
    _RuipconfigDefaultGateway_Type()
)
ruipconfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruipconfigDefaultGateway.setStatus("mandatory")
_Rurf_ObjectIdentity = ObjectIdentity
rurf = _Rurf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2)
)


class _RurfRSSI_Type(Integer32):
    """Custom type rurfRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_RurfRSSI_Type.__name__ = "Integer32"
_RurfRSSI_Object = MibScalar
rurfRSSI = _RurfRSSI_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 1),
    _RurfRSSI_Type()
)
rurfRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurfRSSI.setStatus("mandatory")
_Rurftable_ObjectIdentity = ObjectIdentity
rurftable = _Rurftable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4)
)


class _RurftableChannel1_Type(Integer32):
    """Custom type rurftableChannel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel1_Type.__name__ = "Integer32"
_RurftableChannel1_Object = MibScalar
rurftableChannel1 = _RurftableChannel1_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 1),
    _RurftableChannel1_Type()
)
rurftableChannel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel1.setStatus("mandatory")


class _RurftableChannel2_Type(Integer32):
    """Custom type rurftableChannel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel2_Type.__name__ = "Integer32"
_RurftableChannel2_Object = MibScalar
rurftableChannel2 = _RurftableChannel2_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 2),
    _RurftableChannel2_Type()
)
rurftableChannel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel2.setStatus("mandatory")


class _RurftableChannel3_Type(Integer32):
    """Custom type rurftableChannel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel3_Type.__name__ = "Integer32"
_RurftableChannel3_Object = MibScalar
rurftableChannel3 = _RurftableChannel3_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 3),
    _RurftableChannel3_Type()
)
rurftableChannel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel3.setStatus("mandatory")


class _RurftableChannel4_Type(Integer32):
    """Custom type rurftableChannel4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel4_Type.__name__ = "Integer32"
_RurftableChannel4_Object = MibScalar
rurftableChannel4 = _RurftableChannel4_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 4),
    _RurftableChannel4_Type()
)
rurftableChannel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel4.setStatus("mandatory")


class _RurftableChannel5_Type(Integer32):
    """Custom type rurftableChannel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel5_Type.__name__ = "Integer32"
_RurftableChannel5_Object = MibScalar
rurftableChannel5 = _RurftableChannel5_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 5),
    _RurftableChannel5_Type()
)
rurftableChannel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel5.setStatus("mandatory")


class _RurftableChannel6_Type(Integer32):
    """Custom type rurftableChannel6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel6_Type.__name__ = "Integer32"
_RurftableChannel6_Object = MibScalar
rurftableChannel6 = _RurftableChannel6_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 6),
    _RurftableChannel6_Type()
)
rurftableChannel6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel6.setStatus("mandatory")


class _RurftableChannel7_Type(Integer32):
    """Custom type rurftableChannel7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel7_Type.__name__ = "Integer32"
_RurftableChannel7_Object = MibScalar
rurftableChannel7 = _RurftableChannel7_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 7),
    _RurftableChannel7_Type()
)
rurftableChannel7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel7.setStatus("mandatory")


class _RurftableChannel8_Type(Integer32):
    """Custom type rurftableChannel8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel8_Type.__name__ = "Integer32"
_RurftableChannel8_Object = MibScalar
rurftableChannel8 = _RurftableChannel8_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 8),
    _RurftableChannel8_Type()
)
rurftableChannel8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel8.setStatus("mandatory")


class _RurftableChannel9_Type(Integer32):
    """Custom type rurftableChannel9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel9_Type.__name__ = "Integer32"
_RurftableChannel9_Object = MibScalar
rurftableChannel9 = _RurftableChannel9_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 9),
    _RurftableChannel9_Type()
)
rurftableChannel9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel9.setStatus("mandatory")


class _RurftableChannel10_Type(Integer32):
    """Custom type rurftableChannel10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel10_Type.__name__ = "Integer32"
_RurftableChannel10_Object = MibScalar
rurftableChannel10 = _RurftableChannel10_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 10),
    _RurftableChannel10_Type()
)
rurftableChannel10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel10.setStatus("mandatory")


class _RurftableChannel11_Type(Integer32):
    """Custom type rurftableChannel11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel11_Type.__name__ = "Integer32"
_RurftableChannel11_Object = MibScalar
rurftableChannel11 = _RurftableChannel11_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 11),
    _RurftableChannel11_Type()
)
rurftableChannel11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel11.setStatus("mandatory")


class _RurftableChannel12_Type(Integer32):
    """Custom type rurftableChannel12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel12_Type.__name__ = "Integer32"
_RurftableChannel12_Object = MibScalar
rurftableChannel12 = _RurftableChannel12_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 12),
    _RurftableChannel12_Type()
)
rurftableChannel12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel12.setStatus("mandatory")


class _RurftableChannel13_Type(Integer32):
    """Custom type rurftableChannel13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel13_Type.__name__ = "Integer32"
_RurftableChannel13_Object = MibScalar
rurftableChannel13 = _RurftableChannel13_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 13),
    _RurftableChannel13_Type()
)
rurftableChannel13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel13.setStatus("mandatory")


class _RurftableChannel14_Type(Integer32):
    """Custom type rurftableChannel14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel14_Type.__name__ = "Integer32"
_RurftableChannel14_Object = MibScalar
rurftableChannel14 = _RurftableChannel14_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 14),
    _RurftableChannel14_Type()
)
rurftableChannel14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel14.setStatus("mandatory")


class _RurftableChannel15_Type(Integer32):
    """Custom type rurftableChannel15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel15_Type.__name__ = "Integer32"
_RurftableChannel15_Object = MibScalar
rurftableChannel15 = _RurftableChannel15_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 15),
    _RurftableChannel15_Type()
)
rurftableChannel15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel15.setStatus("mandatory")


class _RurftableChannel16_Type(Integer32):
    """Custom type rurftableChannel16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel16_Type.__name__ = "Integer32"
_RurftableChannel16_Object = MibScalar
rurftableChannel16 = _RurftableChannel16_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 16),
    _RurftableChannel16_Type()
)
rurftableChannel16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel16.setStatus("mandatory")


class _RurftableChannel17_Type(Integer32):
    """Custom type rurftableChannel17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel17_Type.__name__ = "Integer32"
_RurftableChannel17_Object = MibScalar
rurftableChannel17 = _RurftableChannel17_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 17),
    _RurftableChannel17_Type()
)
rurftableChannel17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel17.setStatus("mandatory")


class _RurftableChannel18_Type(Integer32):
    """Custom type rurftableChannel18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel18_Type.__name__ = "Integer32"
_RurftableChannel18_Object = MibScalar
rurftableChannel18 = _RurftableChannel18_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 18),
    _RurftableChannel18_Type()
)
rurftableChannel18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel18.setStatus("mandatory")


class _RurftableChannel19_Type(Integer32):
    """Custom type rurftableChannel19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel19_Type.__name__ = "Integer32"
_RurftableChannel19_Object = MibScalar
rurftableChannel19 = _RurftableChannel19_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 19),
    _RurftableChannel19_Type()
)
rurftableChannel19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel19.setStatus("mandatory")


class _RurftableChannel20_Type(Integer32):
    """Custom type rurftableChannel20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel20_Type.__name__ = "Integer32"
_RurftableChannel20_Object = MibScalar
rurftableChannel20 = _RurftableChannel20_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 20),
    _RurftableChannel20_Type()
)
rurftableChannel20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel20.setStatus("mandatory")


class _RurftableChannel21_Type(Integer32):
    """Custom type rurftableChannel21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel21_Type.__name__ = "Integer32"
_RurftableChannel21_Object = MibScalar
rurftableChannel21 = _RurftableChannel21_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 21),
    _RurftableChannel21_Type()
)
rurftableChannel21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel21.setStatus("mandatory")


class _RurftableChannel22_Type(Integer32):
    """Custom type rurftableChannel22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel22_Type.__name__ = "Integer32"
_RurftableChannel22_Object = MibScalar
rurftableChannel22 = _RurftableChannel22_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 22),
    _RurftableChannel22_Type()
)
rurftableChannel22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel22.setStatus("mandatory")


class _RurftableChannel23_Type(Integer32):
    """Custom type rurftableChannel23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel23_Type.__name__ = "Integer32"
_RurftableChannel23_Object = MibScalar
rurftableChannel23 = _RurftableChannel23_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 23),
    _RurftableChannel23_Type()
)
rurftableChannel23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel23.setStatus("mandatory")


class _RurftableChannel24_Type(Integer32):
    """Custom type rurftableChannel24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel24_Type.__name__ = "Integer32"
_RurftableChannel24_Object = MibScalar
rurftableChannel24 = _RurftableChannel24_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 24),
    _RurftableChannel24_Type()
)
rurftableChannel24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel24.setStatus("mandatory")


class _RurftableChannel25_Type(Integer32):
    """Custom type rurftableChannel25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel25_Type.__name__ = "Integer32"
_RurftableChannel25_Object = MibScalar
rurftableChannel25 = _RurftableChannel25_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 25),
    _RurftableChannel25_Type()
)
rurftableChannel25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel25.setStatus("mandatory")


class _RurftableChannel26_Type(Integer32):
    """Custom type rurftableChannel26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel26_Type.__name__ = "Integer32"
_RurftableChannel26_Object = MibScalar
rurftableChannel26 = _RurftableChannel26_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 26),
    _RurftableChannel26_Type()
)
rurftableChannel26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel26.setStatus("mandatory")


class _RurftableChannel27_Type(Integer32):
    """Custom type rurftableChannel27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel27_Type.__name__ = "Integer32"
_RurftableChannel27_Object = MibScalar
rurftableChannel27 = _RurftableChannel27_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 27),
    _RurftableChannel27_Type()
)
rurftableChannel27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel27.setStatus("mandatory")


class _RurftableChannel28_Type(Integer32):
    """Custom type rurftableChannel28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel28_Type.__name__ = "Integer32"
_RurftableChannel28_Object = MibScalar
rurftableChannel28 = _RurftableChannel28_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 28),
    _RurftableChannel28_Type()
)
rurftableChannel28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel28.setStatus("mandatory")


class _RurftableChannel29_Type(Integer32):
    """Custom type rurftableChannel29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel29_Type.__name__ = "Integer32"
_RurftableChannel29_Object = MibScalar
rurftableChannel29 = _RurftableChannel29_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 29),
    _RurftableChannel29_Type()
)
rurftableChannel29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel29.setStatus("mandatory")


class _RurftableChannel30_Type(Integer32):
    """Custom type rurftableChannel30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5260, 5340),
        ValueRangeConstraint(5736, 5836),
    )


_RurftableChannel30_Type.__name__ = "Integer32"
_RurftableChannel30_Object = MibScalar
rurftableChannel30 = _RurftableChannel30_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 4, 30),
    _RurftableChannel30_Type()
)
rurftableChannel30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rurftableChannel30.setStatus("mandatory")
_Ruism_ObjectIdentity = ObjectIdentity
ruism = _Ruism_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 5)
)


class _RuismTxPowerMax_Type(Integer32):
    """Custom type ruismTxPowerMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_RuismTxPowerMax_Type.__name__ = "Integer32"
_RuismTxPowerMax_Object = MibScalar
ruismTxPowerMax = _RuismTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 5, 1),
    _RuismTxPowerMax_Type()
)
ruismTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruismTxPowerMax.setStatus("mandatory")


class _RuismTxPowerMin_Type(Integer32):
    """Custom type ruismTxPowerMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_RuismTxPowerMin_Type.__name__ = "Integer32"
_RuismTxPowerMin_Object = MibScalar
ruismTxPowerMin = _RuismTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 5, 2),
    _RuismTxPowerMin_Type()
)
ruismTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruismTxPowerMin.setStatus("mandatory")


class _RuismTxPower_Type(Integer32):
    """Custom type ruismTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_RuismTxPower_Type.__name__ = "Integer32"
_RuismTxPower_Object = MibScalar
ruismTxPower = _RuismTxPower_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 5, 3),
    _RuismTxPower_Type()
)
ruismTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruismTxPower.setStatus("mandatory")


class _RuismRxThreshold_Type(Integer32):
    """Custom type ruismRxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -90),
        ValueRangeConstraint(-85, -85),
        ValueRangeConstraint(-80, -80),
        ValueRangeConstraint(-75, -75),
        ValueRangeConstraint(-70, -70),
        ValueRangeConstraint(-65, -65),
    )


_RuismRxThreshold_Type.__name__ = "Integer32"
_RuismRxThreshold_Object = MibScalar
ruismRxThreshold = _RuismRxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 5, 4),
    _RuismRxThreshold_Type()
)
ruismRxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruismRxThreshold.setStatus("mandatory")
_Ruunii_ObjectIdentity = ObjectIdentity
ruunii = _Ruunii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 6)
)


class _RuuniiTxPowerMax_Type(Integer32):
    """Custom type ruuniiTxPowerMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_RuuniiTxPowerMax_Type.__name__ = "Integer32"
_RuuniiTxPowerMax_Object = MibScalar
ruuniiTxPowerMax = _RuuniiTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 6, 1),
    _RuuniiTxPowerMax_Type()
)
ruuniiTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruuniiTxPowerMax.setStatus("mandatory")


class _RuuniiTxPowerMin_Type(Integer32):
    """Custom type ruuniiTxPowerMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_RuuniiTxPowerMin_Type.__name__ = "Integer32"
_RuuniiTxPowerMin_Object = MibScalar
ruuniiTxPowerMin = _RuuniiTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 6, 2),
    _RuuniiTxPowerMin_Type()
)
ruuniiTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruuniiTxPowerMin.setStatus("mandatory")


class _RuuniiTxPower_Type(Integer32):
    """Custom type ruuniiTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_RuuniiTxPower_Type.__name__ = "Integer32"
_RuuniiTxPower_Object = MibScalar
ruuniiTxPower = _RuuniiTxPower_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 6, 3),
    _RuuniiTxPower_Type()
)
ruuniiTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruuniiTxPower.setStatus("mandatory")


class _RuuniiRxThreshold_Type(Integer32):
    """Custom type ruuniiRxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -90),
        ValueRangeConstraint(-85, -85),
        ValueRangeConstraint(-80, -80),
        ValueRangeConstraint(-75, -75),
        ValueRangeConstraint(-70, -70),
        ValueRangeConstraint(-65, -65),
    )


_RuuniiRxThreshold_Type.__name__ = "Integer32"
_RuuniiRxThreshold_Object = MibScalar
ruuniiRxThreshold = _RuuniiRxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 2, 6, 4),
    _RuuniiRxThreshold_Type()
)
ruuniiRxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruuniiRxThreshold.setStatus("mandatory")
_Mibinfo_ObjectIdentity = ObjectIdentity
mibinfo = _Mibinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 5)
)


class _MibinfoVersion_Type(DisplayString):
    """Custom type mibinfoVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MibinfoVersion_Type.__name__ = "DisplayString"
_MibinfoVersion_Object = MibScalar
mibinfoVersion = _MibinfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 24, 5, 1),
    _MibinfoVersion_Type()
)
mibinfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibinfoVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANGOP5830S-RU-MIB",
    **{"DisplayString": DisplayString,
       "trango": trango,
       "tbw": tbw,
       "p5830sru": p5830sru,
       "rusys": rusys,
       "ruversion": ruversion,
       "ruversionHW": ruversionHW,
       "ruversionFW": ruversionFW,
       "ruversionFPGA": ruversionFPGA,
       "ruversionFWChecksum": ruversionFWChecksum,
       "ruversionFPGAChecksum": ruversionFPGAChecksum,
       "rusysDeviceId": rusysDeviceId,
       "rusysDefOpMode": rusysDefOpMode,
       "rusysCurOpMode": rusysCurOpMode,
       "rusysActivateOpmode": rusysActivateOpmode,
       "rusysReadCommStr": rusysReadCommStr,
       "rusysWriteCommStr": rusysWriteCommStr,
       "ruswitches": ruswitches,
       "ruswitchesBlockBroadcastMulticast": ruswitchesBlockBroadcastMulticast,
       "ruswitchesHTTPD": ruswitchesHTTPD,
       "ruswitchesAutoScanMasterSignal": ruswitchesAutoScanMasterSignal,
       "rutraffic": rutraffic,
       "rutrafficEthInOctets": rutrafficEthInOctets,
       "rutrafficEthOutOctets": rutrafficEthOutOctets,
       "rutrafficRfInOctets": rutrafficRfInOctets,
       "rutrafficRfOutOctets": rutrafficRfOutOctets,
       "rusysTemperature": rusysTemperature,
       "rusysUpdateFlashAndActivate": rusysUpdateFlashAndActivate,
       "rusysReboot": rusysReboot,
       "ruipconfig": ruipconfig,
       "ruipconfigIpAddress": ruipconfigIpAddress,
       "ruipconfigSubnet": ruipconfigSubnet,
       "ruipconfigDefaultGateway": ruipconfigDefaultGateway,
       "rurf": rurf,
       "rurfRSSI": rurfRSSI,
       "rurftable": rurftable,
       "rurftableChannel1": rurftableChannel1,
       "rurftableChannel2": rurftableChannel2,
       "rurftableChannel3": rurftableChannel3,
       "rurftableChannel4": rurftableChannel4,
       "rurftableChannel5": rurftableChannel5,
       "rurftableChannel6": rurftableChannel6,
       "rurftableChannel7": rurftableChannel7,
       "rurftableChannel8": rurftableChannel8,
       "rurftableChannel9": rurftableChannel9,
       "rurftableChannel10": rurftableChannel10,
       "rurftableChannel11": rurftableChannel11,
       "rurftableChannel12": rurftableChannel12,
       "rurftableChannel13": rurftableChannel13,
       "rurftableChannel14": rurftableChannel14,
       "rurftableChannel15": rurftableChannel15,
       "rurftableChannel16": rurftableChannel16,
       "rurftableChannel17": rurftableChannel17,
       "rurftableChannel18": rurftableChannel18,
       "rurftableChannel19": rurftableChannel19,
       "rurftableChannel20": rurftableChannel20,
       "rurftableChannel21": rurftableChannel21,
       "rurftableChannel22": rurftableChannel22,
       "rurftableChannel23": rurftableChannel23,
       "rurftableChannel24": rurftableChannel24,
       "rurftableChannel25": rurftableChannel25,
       "rurftableChannel26": rurftableChannel26,
       "rurftableChannel27": rurftableChannel27,
       "rurftableChannel28": rurftableChannel28,
       "rurftableChannel29": rurftableChannel29,
       "rurftableChannel30": rurftableChannel30,
       "ruism": ruism,
       "ruismTxPowerMax": ruismTxPowerMax,
       "ruismTxPowerMin": ruismTxPowerMin,
       "ruismTxPower": ruismTxPower,
       "ruismRxThreshold": ruismRxThreshold,
       "ruunii": ruunii,
       "ruuniiTxPowerMax": ruuniiTxPowerMax,
       "ruuniiTxPowerMin": ruuniiTxPowerMin,
       "ruuniiTxPower": ruuniiTxPower,
       "ruuniiRxThreshold": ruuniiRxThreshold,
       "mibinfo": mibinfo,
       "mibinfoVersion": mibinfoVersion}
)
